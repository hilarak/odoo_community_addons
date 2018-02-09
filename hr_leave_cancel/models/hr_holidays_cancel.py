# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Holidays(models.Model):

    _name = "hr.holidays.cancel"
    _description = "Leave Cancellation"
    # _order = "type desc, date_from desc"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    def _default_employee(self):
        return self.env.context.get('default_employee_id') or self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)

    name = fields.Char('Description')
    state = fields.Selection([
        ('draft', 'To Submit'),
        ('cancel', 'Cancelled'),
        ('confirm', 'To Approve'),
        ('refuse', 'Refused'),
        ('validate', 'Approved')
    ], string='Status', readonly=True, track_visibility='onchange', copy=False, default='draft',
        help="The status is set to 'To Submit', when a holiday cancel request is created." +
             "\nThe status is 'To Approve', when holiday cancel request is confirmed by user." +
             "\nThe status is 'Refused', when holiday request cancel is refused by manager." +
             "\nThe status is 'Approved', when holiday request cancel is approved by manager.")
    report_note = fields.Text('HR Comments')
    holiday = fields.Many2one("hr.holidays", string="Leaves", required=True, domain="[('state', '=', 'validate')]")
    employee_id = fields.Many2one('hr.employee', string='Employee', index=True, readonly=True,
                                  states={'draft': [('readonly', False)], 'confirm': [('readonly', False)]},
                                  default=_default_employee)

    @api.multi
    def action_approve(self):
        for record in self:
            record.holiday.action_refuse()
            record.write({'state': 'validate'})

    @api.multi
    def action_refuse(self):
        for record in self:
            record.write({'state': 'refuse'})

    @api.multi
    def action_confirm(self):
        """
        Confirm leave cancel requests and send a mail to the concerning department head.
        :return:
        """
        for record in self:
            if record.employee_id and record.employee_id.parent_id and record.employee_id.parent_id.work_email:
                vals = {
                        'email_to': record.employee_id.parent_id.work_email,
                        'subject': 'Leave Cancel Request: From {employee} , {description}'
                                    .format(employee=record.employee_id.name, description=record.name),
                        'body_html': """
                                    <p>
                                        Hello Mr {manager},
                                    </p>
                                    <p>
                                        There is a leave cancellation request on an approved leave {leave}
                                    </p>
                                    <p>
                                        Thank You.
                                    </p>
                                """.format(manager=record.employee_id.parent_id.name, leave=record.holiday.display_name)}
                mail = self.env['mail.mail'].sudo().create(vals)
                mail.send()
            record.write({'state': 'confirm'})

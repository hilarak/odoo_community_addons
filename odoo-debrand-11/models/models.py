from odoo import models, fields, api, _
from odoo.exceptions import Warning


class OdooDebrand(models.Model):
    _inherit = 'website'

    @api.one
    @api.depends('favicon')
    def get_favicon(self):
        self.favicon_url = \
            'data:image/png;base64,' + str(self.favicon.decode('UTF-8'))
        # python 3.x has sequence of bytes object,
        #  so we should decode it, else we get data starting with 'b'

    @api.one
    @api.depends('company_logo')
    def get_company_logo(self):
        self.company_logo_url = \
            ('data:image/png;base64,' +
             str(self.company_logo.decode('UTF-8')))

    company_logo = fields.Binary("Logo", attachment=True,
                                 help="This field holds"
                                      " the image used "
                                      "for the Company Logo")
    company_name = fields.Char("Company Name", help="Branding Name")
    company_website = fields.Char("Company URL")
    favicon_url = fields.Char("Url", compute='get_favicon')
    company_logo_url = fields.Char("Url", compute='get_company_logo')


class WebsiteConfig(models.TransientModel):
    _inherit = 'res.config.settings'

    company_logo = fields.Binary(related='website_id.company_logo',
                                 string="Company Logo",
                                 help="This field holds the image"
                                      " used for the Company Logo",
                                 readonly=False)
    company_name = fields.Char(related='website_id.company_name',
                               string="Company Name",
                               readonly=False)
    company_website = fields.Char(related='website_id.company_website',
                                  readonly=False)

    # Sample Error Dialogue
    @api.multi
    def error(self):
        raise ValueError

    # Sample Warning Dialogue
    @api.multi
    def warning(self):
        raise Warning(_("This is a Warning"))

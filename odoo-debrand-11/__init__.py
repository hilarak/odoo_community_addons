from . import controllers
from . import models
from odoo import api, SUPERUSER_ID


def clear_odoobot(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    # using query because write doesn't seems work here
    cr.execute("UPDATE res_partner "
               "SET name='Bot', "
               "email='bot@example.com' "
               "WHERE name='OdooBot'")

    # the below section may seem useless, even though it is kept
    # because, in a different version of odoo,
    #  there was the channel 'odoobot'
    channel = env['mail.channel'].search([('name', '=', 'OdooBot')],
                                         limit=1)
    if channel:
        channel.name = 'Bot'


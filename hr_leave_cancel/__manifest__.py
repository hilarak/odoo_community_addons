# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, HRMS Leave Cancellation
#    Copyright (C) 2018 Hilar AK All Rights Reserved
#    https://www.linkedin.com/in/hilar-ak/
#    <hilarak@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Leave Cancellation",
    'version': "10.0.1.0.0",
    'summary': """
        Leave cancellation request for approved leaves to the officers/managers.""",
    'description': """
        Leave cancellation request for approved leaves to the officers/managers.
    """,

    'author': "Hilar AK",
    'company': "",
    'website': "",
    'category': "Generic Modules/Human Resources",
    'depends': [
        "base",
        "hr_holidays"
    ],
    'data': [
        'security/hr_holidays_security.xml',
        'security/ir.model.access.csv',

        'views/views.xml',
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'application': True
}

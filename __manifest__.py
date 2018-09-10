# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2012 - 2017 PERLUR Group (<https://go.perlur.cloud/odoo-l10n-cs>).
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
    'name': 'Czech - Accounting',
    'version': '2.0',
    'category': 'Localization/Account Charts',
    'description': """
This is the latest Czech OpenERP localisation necessary to run OpenERP accounting for Czech businesses with:
============================================================================================================
    - a Chart Of Accounts for Czech Republic
    - VAT tax structure with VATs for years 2010, 2011, 2012, 2013 and 2014
    - a few other adaptations""",
    'author': 'PERLUR Group',
    'price': '100',
    'currency': 'EUR',
    'website': 'https://go.perlur.cloud/odoo-l10n-cs',
    'depends': ['account', 'base_iban', 'base_vat', 'l10n_multilang'],
    'data': [
        'data/l10n_cs_cz_chart_template.xml',
        'data/account_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_data.xml',
#        'views\partner_view.xml',
#        'wizard/l10n_cs_wizard.xml', #přesunuto do adresáře
        'data/account_chart_template_data.yml',
    ],
 #   'demo' : ['demo/demo.xml'],
 
	}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

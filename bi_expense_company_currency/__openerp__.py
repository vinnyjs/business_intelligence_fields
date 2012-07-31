# -*- encoding: utf-8 -*-
##############################################################################
#
#    bi_expense_company_currency module for OpenERP
#    Copyright (C) 2012 Akretion (http://www.akretion.com). All Rights Reserved
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
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
    'name': 'Business intelligence - Expense in company currency',
    'version': '0.2',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'complexity': 'easy',
    'description': """This module adds some fields required to do business intelligence :
it adds the amount in company currency on the expense lines.""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['hr_expense', 'anevia_hr_expense'],
    'init_xml': [],
    'update_xml': [],
    'demo_xml': [],
    'installable': True,
    'active': False,
}


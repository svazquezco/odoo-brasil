# -*- coding: utf-8 -*-
# © 2016 Danimar Ribeiro <danimaribeiro@gmail.com>, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    tipo_ambiente_nfse = fields.Selection(
        [('producao', u'Production'), ('homologacao', u'Homologation')],
        string="NFSe Environment", default='homologacao')

    nfe_email_template = fields.Many2one(
        'mail.template', string="NFe's Email Template")

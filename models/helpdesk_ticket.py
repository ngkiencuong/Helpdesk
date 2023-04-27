from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    product_ids = fields.Many2many('product.product', string='Products')
    timesheet_ids = fields.One2many('account.analytic.line', 'helpdesk_ticket_id', 'Timesheets')
    total_hours_spent = fields.Float("Spent Hours", compute='_compute_total_hours_spent', default=0, compute_sudo=True, store=True)
    encode_uom_in_days = fields.Boolean(compute='_compute_encode_uom_in_days')
    is_prj_connect = fields.Boolean(related='team_id.is_prj_connect')

    def _compute_encode_uom_in_days(self):
        self.encode_uom_in_days = self.env.company.timesheet_encode_uom_id == self.env.ref('uom.product_uom_day')

    @api.depends('timesheet_ids')
    def _compute_total_hours_spent(self):
        for ticket in self:
            ticket.total_hours_spent = round(sum(ticket.timesheet_ids.mapped('unit_amount')), 2)

    @api.onchange('team_id')
    def _onchange_project_analytic_account(self):
        if self.team_id:
            self.project_id = self.team_id.project_id

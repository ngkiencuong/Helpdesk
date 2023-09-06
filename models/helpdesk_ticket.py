from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    timesheet_ids = fields.One2many('account.analytic.line', 'helpdesk_ticket_id', 'Timesheets')
    total_hours_spent = fields.Float("Spent Hours", compute='_compute_total_hours_spent', default=0, compute_sudo=True, store=True)
    encode_uom_in_days = fields.Boolean(compute='_compute_encode_uom_in_days')
    ticket_line_ids = fields.One2many('helpdesk.ticket.line', 'ticket_id', 'Ticket Lines')
    is_prj_connect = fields.Boolean(related='team_id.is_prj_connect')
    partner_city = fields.Char('City', related='partner_id.city', store=True)
    partner_street = fields.Char('Street', related='partner_id.street', store=True)

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


class HelpdeskTicketLine(models.Model):
    _name = "helpdesk.ticket.line"
    _description = "Product in Ticket"

    ticket_id = fields.Many2one('helpdesk.ticket', string='Ticket', ondelete='cascade', index=True)
    product_id = fields.Many2one('product.product', 'Product', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)



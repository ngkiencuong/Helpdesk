from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', 'Helpdesk Ticket')

    @api.constrains('task_id', 'helpdesk_ticket_id')
    def _check_no_link_task_and_ticket(self):
        # Check if any timesheets are not linked to a ticket and a task at the same time
        if any(timesheet.task_id and timesheet.helpdesk_ticket_id for timesheet in self):
            raise ValidationError(_("A timesheet cannot be linked to a task and a ticket at the same time."))

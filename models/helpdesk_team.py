from odoo import models, fields, api


class HelpdeskTeam(models.Model):
    _inherit = 'helpdesk.ticket.team'

    is_prj_connect = fields.Boolean('Connected to a Project', default=False)
    project_id = fields.Many2one("project.project", string="Project", ondelete="restrict",
                                 domain="[('allow_timesheets', '=', True)]",
                                 help="Project to which the tickets (and the timesheets) will be linked by default.")

    @api.onchange('is_prj_connect')
    def _check_project_connect(self):
        if not self.is_prj_connect:
            self.project_id = False

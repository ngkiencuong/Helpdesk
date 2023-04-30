{
    'name': 'Helpdesk Enhancement',
    'version': '1.0',
    'category': 'Helpdesk',
    'summary': 'Enhancing the OCA Odoo Helpdesk module',
    'author': 'Simplify-ERP™',
    'website': 'https://simplify-erp.de',
    'depends': [
        'helpdesk_mgmt',
        'helpdesk_mgmt_project',
        'product',
        'hr_timesheet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/helpdesk_ticket.xml',
        'report/helpdesk_ticket_analysis_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}

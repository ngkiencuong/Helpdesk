# OCA Odoo Helpdesk Enhancement Module

This module enhances the OCA Odoo Helpdesk module by adding new features and improving existing ones. The module is designed to work with Odoo v15.

## Features

- Connect to a web form for instant ticket creation, protected by CAPTCHA.
- Open a new ticket by sending an email to a designated email address.
- Attach one or more products to a helpdesk ticket.
- Merge multiple tickets into a single ticket.
- Track support agents' time spent on tickets using timesheets.

## Installation

1. Download the `oca_odoo_helpdesk_enhancement` module and place it in your Odoo addons folder.
2. Go to the Odoo Apps menu, search for "OCA Odoo Helpdesk Enhancement," and click on "Install."

## Configuration

To configure this module, please follow these steps:

1. Set up your email server to receive emails and create tickets automatically.
2. Configure the CAPTCHA settings for the web form.
3. Set up time tracking integrations with third-party tools, if needed.

## Usage

1. To create a ticket using the web form, embed the web form on your website or use the provided form link.
2. To open a ticket by email, send an email to the designated email address with the required information.
3. To attach products to a ticket, go to the ticket form and search for the products using the product field.
4. To merge multiple tickets, select the tickets from the ticket list view and choose the "Merge Tickets" action.
5. To log time spent on a ticket, go to the ticket form and add a timesheet entry with the start and end times, and a description of the activity.

## Support

If you need assistance or have any questions, please contact the module author or create an issue on the project repository.

## License

This module is released under the [GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.en.html).

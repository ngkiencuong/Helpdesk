
# Helpdesk Module with Timesheets and Material List

## 1. Introduction
This outlines the software requirements specification for enhancing the [OCA Odoo Helpdesk module](https://github.com/OCA/helpdesk). 
The existing module provides basic functionality for creating helpdesk channels, opening tickets, assigning to users, and attaching tags. 
This enhancement will introduce additional features such as connecting from a web form, ~opening tickets by email~, attaching products, merging tickets, and logging time on Tickets in Odoo Timesheets.

**Product Name:** OCA Odoo Helpdesk Enhancements

**Product Version:** 1.0

**Target Platform:** Odoo v15

## 2. Features

### 2.1 Connect to Web Form (**Postoponed to future Version 2.0**)

The module should allow public users to create a helpdesk ticket instantaneously using a web form. 
The following are the requirements for this feature:

- The form should be protected by a CAPTCHA to prevent spam and automated submissions.
- Upon successful submission, the module should automatically create a new ticket with the submitted information.
- The web form should allow selection as in this screenshot.
![image](https://user-images.githubusercontent.com/7826363/233783295-3df5a4f9-5ce7-47ca-8f84-a55c9cd5d57a.png)


### ~2.2 Open Tickets by Email~
~The module should be able to create a new helpdesk ticket when a customer sends an email to a designated email address. 
The following are the requirements for this feature:~

- ~The module should automatically create a new ticket with the email's subject, body, sender's email address, and attachments.~
- ~The email parser should be configurable to extract additional information, such as product or priority, from the email.~
- ~The system should send an automatic acknowledgment email to the sender to confirm receipt of the ticket.~

### 2.3 Attach Products to Tickets
The module should allow users to attach products to a helpdesk ticket. The following are the requirements for this feature:

- Users should be able to search and select one or more products from the existing Odoo product catalog.
- The attached products should be visible on the ticket details page.
- The attached products should be taken into account when generating reports and analytics.

### ~2.4 Merge Multiple Tickets~
~The module should allow users to merge multiple tickets into a single ticket.~

The [TicketMerge module should be used for this functionality](https://github.com/euroblaze/TicketMerge). 
Minor adaptations might be necessary.

~The following are the requirements for this feature:~

- ~Users should be able to select multiple tickets and merge them into a single surviving_ticket.~
- ~The merged ticket should contain a consolidated history of all the merged tickets.~
- ~The original tickets should be marked as 'merged' and linked to the newly created merged ticket.~

### 2.5 Timesheets
The module should support timesheets for tracking the time spent by support agents on each ticket. 
The following are the requirements for this feature:

- Users should be able to log time spent on a ticket, including start and end times, as well as a brief description of the activity.
- The logged time should be visible on the ticket details page and included in reports and analytics.
- The system should support time tracking integrations with popular third-party time tracking tools.

## 3. Non-functional Requirements

- **Usability:** The enhanced module should be user-friendly and easy to use for both customers and support agents.
- **Scalability:** The module should be able to handle a high volume of tickets without affecting system performance.
- **Security:** The module should ensure the security and privacy of customer data.
- **Compatibility:** The module should be compatible with Odoo v15 and other related modules.
- **Localization:** The module should support multiple languages and currency formats.
- **Customizability:** The module should be highly customizable to cater to the unique requirements of different businesses.

## 4. Acceptance Criteria

- All features outlined in section 2 should be implemented and functional.
- The enhanced module should be compatible with Odoo v15.+
- Code must be compliant with [OCA guidelines](https://github.com/OCA/odoo-community.org/blob/master/website/Contribution/CONTRIBUTING.rst).

---
## After Issues

- https://github.com/euroblaze/Helpdesk/issues/2

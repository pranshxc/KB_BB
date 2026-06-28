---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-15_the-outlook-winner-is-dash.md
original_filename: 2019-04-15_the-outlook-winner-is-dash.md
title: The Outlook Winner is Dash
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 7d44095cc0e6cf5b482db302efca3dac3d594f7bfefdd20c656627f8ee9a8aa6
text_sha256: 8c3d2a44a9992c0ddc9766e0fa11538869b6539a50995a8b21a4802e8215a7f4
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# The Outlook Winner is Dash

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-15_the-outlook-winner-is-dash.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7d44095cc0e6cf5b482db302efca3dac3d594f7bfefdd20c656627f8ee9a8aa6`
- Text SHA256: `8c3d2a44a9992c0ddc9766e0fa11538869b6539a50995a8b21a4802e8215a7f4`


## Content

---
title: "The Outlook Winner is Dash"
url: "https://blog.ettic.ca/the-outlook-winner-is-dash-ac15dbc4098d"
authors: ["marcan2020 (@marcan2020)"]
programs: ["Microsoft"]
bugs: ["Broken authorization"]
publication_date: "2019-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5311
scraped_via: "browseros"
---

# The Outlook Winner is Dash

The Outlook Winner is Dash
marcan2020
Follow
3 min read
·
Apr 15, 2019

4

Abusing Office Groups

Office 365 added a new feature that allows users to create groups with a custom name and email address. When creating a group, a new entry in the Global Address List is added for it. Theses groups are the new way to create a distribution list. By default, Microsoft blocked some reserved groups like:

admin@example.com
postmaster@example.com
webmaster@example.com

Mainly to mitigate risk of requesting SSL certificates, since they are frequently used in the verification process. However, it is still possible to create some groups that could be used in multiple phishing scenarios. Just to name a few:

security@example.com
hr@example.com
support@example.com

The only limitation is the email address needs to be available to register it. Sadly (for red teamers)/Hopefully (for organizations), you cannot send mails directly from these addresses since they are distribution lists. Yet, we still can abuse this functionality by spoofing the sender address when we send a mail. The real game changer though is if our victims reply to the mail, we will receive the answer directly in our inbox which is pretty nice.

An Unexpected Winner

When trying to abuse the Office groups, I stepped on a single character group Dash “-”. At first, I reserved the group Dash for the mail -@example.com as it is somewhat uncommon to see a single “special” character mail address.

The next morning (after the creation of this group), I had already received 5 mails. I was not expecting this… It was the time to begin an investigation. After a few attempts to accidentally send a mail to Dash. I realized that my group was the first entry of the Outlook Global Address List.

Whenever a user of the Outlook Desktop Application adds a new recipient using the Global Address List, the first address is automatically selected which is now our Dash group. If you accidentally press Enter in this form, you will add the group to your recipients and leak your mail.

Get marcan2020’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Also, the team is almost invisible in the recipients list, some people don’t notice it when they are sending a mail.

These are the two main causes why I started receiving unexpected mails. A lot of employees accidentally added the group as a recipient to their mail without noticing it. Resulting in data leaks.

Creating an Office Group
Create a new group.

2. Select the desired name and email. If you compromise an O365 account, you should disable the notifications to be stealthier.

3. Wait for interesting mails to be sent to -@example.com.

If a lot of users in the targeted organization are using the Outlook Desktop Application, it shouldn’t be long before you start receiving mails.

Mitigation and Conclusion

The easiest way to fix this issue is to add a prefix to all created groups trough Office 365. Doing so will prevent someone to get the first address of the address book. Additionally, it will reduce the effectiveness of groups created for phishing by an attacker, since the group support would become O365_group_support@example.com.

With or without Office groups, you should also make sure you own or keep an eye of the first address of the global address book.

Disclosure

Finally, the problem was disclosed to Microsoft and they replied that the

reporting appears to be a product suggestion, but would not meet the bar for security servicing.

Which is kind of true… So register your group Dash and start receiving data!

TLDR: A custom group with a single character can be used to obtain interesting mails exchanged within an organization.

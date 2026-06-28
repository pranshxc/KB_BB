---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-02_one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-c_2.md
original_filename: 2019-08-02_one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-c_2.md
title: One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune
  500 Companies!
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
language: en
raw_sha256: 9abe27eb68690acfe7ed7262b08273c4c75f5050df52961e5f27fd4a73bfa3ef
text_sha256: 0b97c08ed6bd0328ea215ceef1fa62bb503322ad3a83c913c4a001d316a40a4b
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune 500 Companies!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-02_one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-c_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `9abe27eb68690acfe7ed7262b08273c4c75f5050df52961e5f27fd4a73bfa3ef`
- Text SHA256: `0b97c08ed6bd0328ea215ceef1fa62bb503322ad3a83c913c4a001d316a40a4b`


## Content

---
title: "One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune 500 Companies!"
url: "https://medium.com/@logicbomb_1/one-misconfig-jira-to-leak-them-all-including-nasa-and-hundreds-of-fortune-500-companies-a70957ef03c7"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Information disclosure"]
publication_date: "2019-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5104
scraped_via: "browseros"
---

# One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune 500 Companies!

Top highlight

One Misconfig (JIRA) to Leak Them All- Including NASA and Hundreds of Fortune 500 Companies!
Avinash Jain (@logicbomb)
Follow
7 min read
·
Aug 2, 2019

1.5K

11

Press enter or click to view image in full size

Hi Guys,

Some months back, I published an article on “Exposed JIRA server leaks NASA staff and project data” in which I was able to find NASA staff details, their username, their email ids along with their internal project details which were getting leaked by one of their tools — JIRA which is an Atlassian task tracking systems/project management software used by around 135,000 companies and organization globally. The root cause behind the leak was the wild misconfiguration which was present in JIRA. Why the term “wild” being used is because, with the help of the same misconfiguration, I happened to access internal user data, internal project details of hundreds and thousands of companies which were using JIRA.

Lots of companies were from Alexa and Fortune top lists as well. The affected customers ranges from companies as big as NASA, Google, Yahoo to HipChat, Zendesk, Sapient, Dubsmash, Western union, Lenovo, 1password, Informatica, etc and many sectors of various government around the world also suffered the same privacy issue like one of the portal of European government, United Nations, NASA, Brazilian government transport portal, Canadain governement finance portal.

where due to some misconfiguration issues in JIRA, their internal user data, their name, email ids, their project details on which they were working, assignee of those projects and various other information were getting exposed.

Here, I’ll be sharing about what was that critical vulnerability that I happened to find in Jira (An Atlassian task tracking systems/project management software) or more specifically a misconfiguration issue which caused the leakage of internal sensitive information of organization and companies. Let’s see what was the exact issue —

In Jira, while creating filters or dashboards it provides some visibility option to apply to them. The issue was due to the wrong permissions assigned to them. When the filters and dashboards for the projects/issues are created in JIRA, then by default the visibility is set to “All users” and “Everyone” respectively, which instead of sharing with everyone of the organizations (which people think and interpret), it share them publically. There is also a user picker functionality in Jira which gives a complete list of every user’s username and email address. This information disclosure is the result of an authorization misconfiguration in Jira’s Global Permissions settings. Because of the wrong permissions scheme, the following internal information appeared to be vulnerable:

all account’s employees’ names and emails,
employees’ roles through JIRA groups,
current projects, upcoming milestones through JIRA dashboards/filters

Anyone with the link can access them from anywhere and get hold of various sensitive information and because they are being indexed by all the search engines so anyone can easily find them with some simple search queries.

Press enter or click to view image in full size
NASA Staff data because of misconfigured Jira user picker functionality
Press enter or click to view image in full size
Jira Filter Publically accessible
Press enter or click to view image in full size
Jira Dashboard Publically accessible
Press enter or click to view image in full size
NASA Project details getting exposed due to public Filter and dashboard

As can be seen above, it discloses employees names, employee roles, upcoming milestones, secret project, and various other features due to these misconfigured Jira settings.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, how I found the links/URLs of these publically exposed user picker functionality, filters, and dashboards of so many companies and the help came from “Google dorks” (search query). To search for the companies having user picker functionality in Jira as misconfigured and so the complete list of their staff username and email address exposed, here is the search query —

inurl:/UserPickerBrowser.jspa -intitle:Login -intitle:Log
Press enter or click to view image in full size

This query list all the URLs having “UserPickerBrowser” in their URI to find all the misconfigured Jira User picker functionality which are publically exposed and also not authenticated.

Press enter or click to view image in full size
Google Acquisition Apigee staff data publicly exposed
Press enter or click to view image in full size
One of the largest online on-demand transport platform
Press enter or click to view image in full size
NASA Staff data exposed by misconfigured Jira

While for filters and dashboards, we can see the URLs of these filters and dashboards containing “Managefilters” and “ConfigurePortal” as a part. I went on to create the search query —

inurl:/ManageFilters.jspa?filterView=popular AND ( intext:All users OR intext:Shared with the public OR intext:Public )

This query list all the URLs having “Managefilters” in their URI and having text as “Public” so to find all the misconfigured JIRA filters which are publically exposed and also not authenticated.

Press enter or click to view image in full size
inurl:/ConfigurePortalPages!default.jspa?view=popular

This query list all the URLs having “ConfigurePortalPages” in their URI to find all the JIRA dashboard which are publically exposed.

Press enter or click to view image in full size

On further recon(information gathering), I have found that various companies have JIRA URL in the format “company.atlassian.net” so if you want to check for any company who have misconfigured filter, dashboard or user picker functionality, you need to just put their name in the URL like —

https://companyname.atlassian.net/secure/popups/UserPickerBrowser.jspa
https://companyname.atlassian.net/secure/ManageFilters.jspa?filterView=popular 
https://companyname.atlassian.net/secure/ConfigurePortalPages!default.jspa?view=popular 

Thousands of companies filters, dashboards and staff data were publically exposed. It occurs because of the wrong permissions scheme set to filters and dashboards hence providing their access even to non-logged in users and hence leading to leaking of sensitive data. I have discovered several such misconfigured JIRA accounts in hundreds of companies. Some of the companies were from Alexa and Fortune top list including big giants like NASA, Google, Yahoo, etc and government sites as well like —

The Brazilian government has Jira filter misconfigured of their Road and Transport system hence exposing some of their project details, employee names, etc which was fixed after reaching out to them.

Similarly, the United Nations accidentally made their Jira filters and Jira dashboard public hence exposed their internal project details, secrets milestones, etc which was fixed by them after I reported it and was rewarded by them in their Hall of fame list.

Even the European government suffered the same exposure when their Commercial finance software systems and solutions had the same Jira misconfiguration and exposing their internal sensitive project and staff details. They also fixed it after I sent out the report to them and was also recognized in their Hall of fame list.

Press enter or click to view image in full size
NASA Jira filters publicly accessible
Press enter or click to view image in full size
Gov.uk Jira Filters publicly accessible
Press enter or click to view image in full size
Informatica Jira filters publically exposed
Press enter or click to view image in full size
Zendesk Jira dashboard publically exposed
Press enter or click to view image in full size
Swiggy Jira filters publically exposed
Press enter or click to view image in full size
Informatica Jira dashboard publically exposed
Press enter or click to view image in full size
Western union staff data exposed
Press enter or click to view image in full size
Luminate yahoo acquisition having Jira filters publically exposed

These publically available filters and dashboards were providing details such as employees roles, employees names, their mail id, upcoming milestones, secret project, and features. While the user picker functionality discloses internal user data. Useful information for a competitor company to get to know about the kind of upcoming milestones or secret projects their competitor is working upon. Even an attacker can gain some information from this and tie it with some other type of attacks. Clearly, it is something which shouldn’t be public. Not a security issue but more of a privacy issue.

I reported this to various companies, some rewarded me, some fixed it while some are still living with it. While it is more of a misconfiguration issue which Atlassian(JIRA) must take care of and be more explicitly clear about what is meant by “Any logged-in user” whether it is any logged-in user of JIRA or just a logged-in user belonging to a specific Jira company account.

Press enter or click to view image in full size
Filter visibility settings

and set the visibility to “Private” by default and if anyone wants to make their dashboard or filter public, they have to explicitly go to the setting and change them. While user picker functionality settings must also be taken into account.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )

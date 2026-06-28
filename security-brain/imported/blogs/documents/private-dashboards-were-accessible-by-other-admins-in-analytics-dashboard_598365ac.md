---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-02_private-dashboards-were-accessible-by-other-admins-in-analytics-dashboard.md
original_filename: 2020-05-02_private-dashboards-were-accessible-by-other-admins-in-analytics-dashboard.md
title: Private Dashboards were accessible by other Admins in Analytics Dashboard
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 598365acb916ba86e3c71a781023ca70c803e622ace01e9e08d44fd92449484b
text_sha256: 181b186e63797e4dc90259157c3185b3985b837e76db69ba42655e29631707f4
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Private Dashboards were accessible by other Admins in Analytics Dashboard

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-02_private-dashboards-were-accessible-by-other-admins-in-analytics-dashboard.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `598365acb916ba86e3c71a781023ca70c803e622ace01e9e08d44fd92449484b`
- Text SHA256: `181b186e63797e4dc90259157c3185b3985b837e76db69ba42655e29631707f4`


## Content

---
title: "Private Dashboards were accessible by other Admins in Analytics Dashboard"
url: "https://medium.com/@rohitcoder/private-dashboards-were-accessible-by-other-admins-in-analytics-dashboard-558010a379ab"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2020-05-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4612
scraped_via: "browseros"
---

# Private Dashboards were accessible by other Admins in Analytics Dashboard

Private Dashboards were accessible by other Admins in Analytics Dashboard
Rohit kumar
Follow
2 min read
·
May 2, 2020

162

Vuln Type

Privacy / Authorization

Product Area

Facebook — Web

Complete Details
===
The analytics tool in Facebook is having an option to create dashboards and the creator can change the privacy of dashboard to “Public” or “Private”. I found that private dashboards can be accessed by other admins of that App. Which leads to sensitive data exposure.

Impact
===
Private dashboards can be accessed by other Admins, which leads to sensitive data exposure.

Get Rohit kumar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Repro steps

Setup
===
USER A, USER B with admin permission of Any Developer Application (https://developers.facebook.com/apps)

Steps
==
1. From USER A account visit https://www.facebook.com/analytics/APP_ID/dashboards
2. Here on the sidebar, you will get the option to create Dashboard.
3. Click on that option, and fill require details, Here don’t check that checkbox (For now we will keep it public)
4. Now click on Create Dashboard button. Your dashboard is ready and it’s also accessible to other Admins of that Application. (Try to access https://www.facebook.com/analytics/APP_ID/dashboards from USER B account)
5. Now, let’s make this Dashboard private from USER A account by clicking on the private checkbox.
6. Now, this shouldn’t be accessible to USER B. But navigate back to USER B account and reload that opened the dashboard tab. You can still access it!
7. You will not notice dashboard list on home page you need to access id by dashboard_id like this https://www.facebook.com/analytics/464468544452617/dashboards/?dashboard_id=489192518646886
Now, how can I get dashboard_id? We can easily get it by our browser history (in case we previously accessed it and admin made it private after we accessed it)
8. We can also access these dashboards by brute-forcing dashboard_id param

Timeline

Reported: 14 January 2020

Pre-Triaged: 16 January 2020

Triaged: 18 January 2020

Fix Deployed & Confirmed: 25 January 2020

Bounty Awarded: 28 January 2020

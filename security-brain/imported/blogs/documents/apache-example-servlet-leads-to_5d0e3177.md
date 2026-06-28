---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-06_apache-example-servlet-leads-to-.md
original_filename: 2020-08-06_apache-example-servlet-leads-to-.md
title: Apache Example Servlet leads to $$$$
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: 5d0e31777a2f8ac7c1833d4226feb6cc843b86c4da2f9accfd8b76dd878fca8b
text_sha256: 48a9bef4416295a8b23c7e0f5f1611432b92e385f47af68b40a9022516fb91a7
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Apache Example Servlet leads to $$$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-06_apache-example-servlet-leads-to-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `5d0e31777a2f8ac7c1833d4226feb6cc843b86c4da2f9accfd8b76dd878fca8b`
- Text SHA256: `48a9bef4416295a8b23c7e0f5f1611432b92e385f47af68b40a9022516fb91a7`


## Content

---
title: "Apache Example Servlet leads to $$$$"
url: "https://medium.com/@DK999/apache-example-servlet-leads-to-61a2720cac20"
authors: ["Debangshu Kundu (@debangshu_kundu)"]
bugs: ["Clickjacking"]
publication_date: "2020-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4349
scraped_via: "browseros"
---

# Apache Example Servlet leads to $$$$

Apache Example Servlet leads to $$$$
Debangshu Kundu
Follow
4 min read
·
Aug 7, 2020

550

2

Hey Friends, hope you’re doing good during these quarantine days! It’s been quite some time I blogged about something.

So, There’s an interesting vulnerability I found lately and want to share it with you guys!

But first, Let’s get to know what Apache Examples are!

Apache Tomcat Examples are a part of the default Tomcat Installation Page that appears right when you first install the application. It is recommended to remove this page ASAP to be on a safer side.

Path: site.com/examples

OR site.com/tomcat-dir/examples

Press enter or click to view image in full size

Firstly, I’d like to reference another blogpost by Rapid7:

Apache Tomcat Example Scripts Information Leakage
Description The following example scripts that come with Apache Tomcat v4.x - v7.x and can be used by attackers to gain…

www.rapid7.com

This has a list of pages potentially vulnerable to XSS issues. Altough in my case I wasn’t so lucky :/

Me :)

Anyway, there were 3 servlets available:

Servlet Examples
JSP Examples
Websocket Examples

First, I went for the Websocket examples.

There was a functionality as described below, allowing to connect to an external WSS(WebSocket) Server and possibly display messages here. But since this was on a secluded subdomain, away from the main application, CSWSH(Cross-Site-Websocket-Hijacking) would’nt be much impactful here. Still, there was an external connection initiated here(exploitable by connecting to your own WSS server)

Press enter or click to view image in full size

Had a quick chat with hakluke about the impact, he said likewise and cleared my doubts with some questions of his and shared some of his valuable experience :D .

Moving On! I looked at the JSP Servlet to find something other than XSS

Press enter or click to view image in full size
:)

Hmmpph! Interesting but nothing so impactful. There could very well be vulnerabilities in this JSP Servlet buttt I didn’t find any responsive input fields. Sooo, TRASHED!

Then, I finally moved on to the Servlets Examples.

Press enter or click to view image in full size

First, I tried the Byte Counter example, since it had an upload functionality. But but but but but hard luck :( No success here too. If you guys find this in the wild, feel free to use your ideas, try and get an exploit here and ping me too maybe) :P

Press enter or click to view image in full size

At last, I targeted the Session Example and Cookie Example.

Press enter or click to view image in full size
Sessions Example

Interesting! But since its on a secluded sub, not that much impactful.

Get Debangshu Kundu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then, I checked the Cookie Example and it was gold!

Press enter or click to view image in full size

Cookies from the main site were reflecting here! I quickly thought of a scenario, on how can this be exploited. Click-jacking came to my mind. I quickly head over to SecurityHeaders andddddd as expected :D

Press enter or click to view image in full size
summarizes my mood :P

Wrote a hasty piece of code(which obviously can be improved further, haha)

enough to demonstrate impact ;)
Press enter or click to view image in full size
the usual lottery ticket haha

[NOTE: you can reduce the opacity to minimal and add an overlay element to make it more convincing. I didn’t do it due to time constraints/i am just too lazy?]

Press enter or click to view image in full size

Here it comes!!! Now, simply paste the url-encoded cookie to a decoder and its done!

COOKIES == STOLEN

Press enter or click to view image in full size

Thank you guys for reading till the end! Hope you liked it!

Dox me at https://twitter.com/debangshu_kundu

Timeline:

Reported: 29 Jun 2020

Rewarded: 17 Jul 2020

Takeaways: Always stay on the lookout for abandoned/rarely-used subdomains. Specially, If the site says “This Web Application Has Been Disabled” !

Take care guys! Stay safe and secure.

./logout.sh

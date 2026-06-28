---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-23_frapp-technologies-erpnext-server-side-template-injection.md
original_filename: 2019-01-23_frapp-technologies-erpnext-server-side-template-injection.md
title: Frappé Technologies ERPNext Server Side Template Injection
category: documents
detected_topics:
- xss
- sqli
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- cloud-security
language: en
raw_sha256: c644f78c23dc7af94b447d44f47b66c8db6dc73bda4df100abd49c444f051b1a
text_sha256: de4fbc8749ff75a55d373b5e91ad7119a12240258416d9cff4775b62a32ed748
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Frappé Technologies ERPNext Server Side Template Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-23_frapp-technologies-erpnext-server-side-template-injection.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `c644f78c23dc7af94b447d44f47b66c8db6dc73bda4df100abd49c444f051b1a`
- Text SHA256: `de4fbc8749ff75a55d373b5e91ad7119a12240258416d9cff4775b62a32ed748`


## Content

---
title: "Frappé Technologies ERPNext Server Side Template Injection"
url: "https://medium.com/bugbountywriteup/frapp%C3%A9-technologies-erpnext-server-side-template-injection-74e1c95ec872"
authors: ["Brian Hyde (@0xHyde)"]
programs: ["ERPNext"]
bugs: ["SSTI"]
publication_date: "2019-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5456
scraped_via: "browseros"
---

# Frappé Technologies ERPNext Server Side Template Injection

Frappé Technologies ERPNext Server Side Template Injection
hyde
Follow
4 min read
·
Jan 23, 2019

283

A few months ago I was particularly focused on researching vulnerabilities that occurred in Electronic Medical Record web applications. During my research I found ERPNext which is an enterprise resource planning software developed by Frappé Technologies Pvt. Ltd. which has healthcare modules available as well as a vulnerability disclosure program so I decided to take a look into ERPNext and audit the free trial of their product. It didn’t take very long before I discovered a Server Side Template Injection vulnerability in the web applications user profile page.

Press enter or click to view image in full size
Server Side Template Injection Proof of Concept

As you can see in the photo above, the first name {{7*7}} and last name {{8*8}} fields are getting rendered above as 49 and 64. This was a very clear indication that a template injection vulnerability was present. I used the image below found in the Portswigger blog at https://portswigger.net/blog/server-side-template-injection by James Kettle to identify the template engine that was being used as Jinja2.

Template Engine Identification Flowchart

I then set the first name field to:

{{ ''.__class__.__mro__[2].__subclasses__()[40]('/etc/passwd').read() }}

After refreshing the page I was greeted with the following page which demonstrated that I had read capabilities on the server running the web application.

Press enter or click to view image in full size
Successful Arbitrary File Read

Next, I set my first name to:

{{ ''.__class__.__mro__[2].__subclasses__()[40]('/home/frappe/PoC.txt', 'w').write(' Proof of Concept: brian@hyde.solutions') }}

Refreshed the page, and then set my first name to:

{{ ''.__class__.__mro__[2].__subclasses__()[40]('/home/frappe/PoC.txt').read() }}

One more refresh and the following message appeared, demonstrating that I was able to successfully write files on the filesystem as well.

Press enter or click to view image in full size
Read + Write Proof of Concept Successful

I was also able to read their SSH RSA private key, however I will not be posting that image as I don’t think the folks at Frappé would appreciate that. In conclusion, this was a very serious security flaw. I reported this vulnerability to Frappé and they quickly rolled out a patch which appeared to resolve this issue, partially. Essentially, their attempt to patch this issue was just to blacklist any name that contained the string .__ and not render the template. However, anything else such as {{ 7*7 }} would still be rendered as 49. After reading some of the documentation for Frappé and reviewing some of the source code for ERPNext on Github I found out that I could exfiltrate even more sensitive information by submitting the following template syntax as my first or last name:

{{ frappe.local.conf }}

After refreshing the page the following information was displayed:

Press enter or click to view image in full size
Successful Frappe Local Configuration Exfiltration

I then reported this issue for the second time and it appears that the patch they rolled out is working much better than the previous patch. The developers of ERPNext were very grateful for my audit and report and rewarded me $1,250 as a result. I would like to note that the vulnerability disclosure program by Frappé does not officially offer rewards. However, they will provide recognition as well as get a CVE assigned to any vulnerabilities you identify and responsibly disclose to them.

Get hyde’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In addition to the SSTI listed above, I also discovered multiple XSS vulnerabilities, an SQL Injection vulnerability, and another SSTI in the following E-Mail responses:

Press enter or click to view image in full size
SSTI Proof of Concept
Press enter or click to view image in full size
SSTI Proof of Concept

In conclusion, if you’re looking to contribute to an open source software foundation or a good target to get some practice and CVE’s assigned to your findings check out ERPNext by Frappé Technologies Pvt. Ltd.

Reporting Security Vulnerabilities
You are responsible for complying with all applicable laws and must only ever use or otherwise access your own test…

erpnext.com

Frappe Security Bulletin
This security bulletin contains detailed information about vulnerabilities affecting Frappe.

frappe.io

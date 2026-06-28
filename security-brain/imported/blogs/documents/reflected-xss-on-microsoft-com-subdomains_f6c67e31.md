---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-19_reflected-xss-on-microsoftcom-subdomains.md
original_filename: 2020-03-19_reflected-xss-on-microsoftcom-subdomains.md
title: Reflected XSS on microsoft.com subdomains
category: documents
detected_topics:
- xss
- sso
- command-injection
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- api-security
language: en
raw_sha256: f6c67e31e4e9ed26cb971387dea54aa74492f09d9fe64ae1b2fb70a80efc235d
text_sha256: 238d7d25d6cc37af495c7387afd16b91f3aa800b69e7d8bc85536e1e8f525cf4
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS on microsoft.com subdomains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-19_reflected-xss-on-microsoftcom-subdomains.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `f6c67e31e4e9ed26cb971387dea54aa74492f09d9fe64ae1b2fb70a80efc235d`
- Text SHA256: `238d7d25d6cc37af495c7387afd16b91f3aa800b69e7d8bc85536e1e8f525cf4`


## Content

---
title: "Reflected XSS on microsoft.com subdomains"
url: "https://medium.com/bugbountywriteup/reflected-xss-on-microsoft-com-subdomains-4bdfc2c716df"
authors: ["Raimonds Liepins (@lv_linkers)"]
programs: ["Microsoft"]
bugs: ["Reflected XSS"]
publication_date: "2020-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4700
scraped_via: "browseros"
---

# Reflected XSS on microsoft.com subdomains

Reflected XSS on microsoft.com subdomains
Raimonds Liepins
Follow
3 min read
·
Mar 19, 2020

136

2

Microsoft replied that this is out of scope of their security program as well as not deemed this as a security vulnerability at all, so I am going to do a write-up about this.

“ This does not meet the bar for security servicing as it requires a user copy and paste malicious code into a text field or modify user-side code/traffic. Self targeting attacks like this are not considered a security vulnerability as it requires social engineering to target another user.”

UPDATE 3/24/2020:

Microsoft actually re-assessed the rejected vulnerabilities on 23rd of March and these issues actually do meet their bar for service. Since I am all about responsible disclosure the details are removed until they are patched.

“This submission was incorrectly assessed as self-XSS instead of reflected XSS. It was later informed to us that these do meet the bar for service.”

With this vulnerability I actually got into Microsoft’s newbie hall of fame on March 2020 section. Lesson learned from this experience is that you should never ever submit reflected XSS to Microsoft without a proper escalation and you can trust me that there was a lot of possibility for that, as described in the article below.

Affected domains:

activateuat.microsoft.com
gallery.technet.microsoft.com
ppe.gallery.technet.microsoft.com
ppe.code.msdn.microsoft.com

What can you do with a reflected XSS?
If an attacker can control a script that is executed in the victim’s browser, then they can typically fully compromise that user. Among other things, the attacker can:
- Perform any action within the application that the user can perform.
- View any information that the user is able to view.
- Modify any information that the user is able to modify.
- Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

What is cross-site scripting (XSS) and how to prevent it? | Web Security Academy
In this section, we'll explain what cross-site scripting is, describe the different varieties of cross-site scripting…

portswigger.net

Finding vulnerabilities:
Finding vulnerabilities like these is not hard. I ran the following command:

assetfinder -subs-only microsoft.com | httprobe | cookieless

assetfinder https://github.com/tomnomnom/assetfinder
httprobe https://github.com/tomnomnom/httprobe
cookieless https://github.com/RealLinkers/cookieless

Get Raimonds Liepins’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The last github repository is a tool created by me to automate manual testing process. Hopefully it is useful for other researches as well.

What is cookieless and how do you turn that into reflected XSS?
Essentially this only works for .NET websites if the developers used a tilde symbol to resolve a resource

<script src=”<%= ResolveUrl(“~/Script.js”) %>”></script>

The cookieless part of the URL which in the following example is (A(ABCD)) is in no way htmlencoded by design, letting an attacker escape the context of the HTML tag in the following url

https://gallery.technet.microsoft.com/(A(ABCD))/ that will translate to <script src=”/(A(ABCD))/Script.js”>
Not all characters are supported, but with enough tinkering you can find a way to get the alert to popup. Obviously if you are an attacker you can do much more than an alert as previously described.

https://gallery.technet.microsoft.com/(A(%22onerror='alert%601%60'testabcd))/

Since some of these domains don’t even have a Content-Security-Policy you can actually include scripts from 3rd party locations, bypassing the restrictions that you would have defined within the scope of URL length and characters allowed by cookieless identifier.

For a much deeper dive into this please refer to this amazing article https://blog.isec.pl/all-is-xss-that-comes-to-the-net/ and Microsoft’s documentation:
https://docs.microsoft.com/en-us/dotnet/api/system.web.configuration.sessionstatesection.cookieless?view=netframework-4.8

Disclosure timeline:
March 17/2020 Submitted vulnerability to Microsoft MSRC
March 19/2020 Public disclosure as deemed not a vulnerability by Microsoft MSRC
March 23/2020 Public disclosure hidden since Microsoft MSRC reassessed the vulnerabilities and they do in fact meet their bar for service
Issues have been addressed

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

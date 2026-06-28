---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-03_look-at-what-i-found-in-comodo.md
original_filename: 2020-08-03_look-at-what-i-found-in-comodo.md
title: Look at what i found in Comodo
category: documents
detected_topics:
- xss
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: f015a7df908bf903daffcd1f383e5c3cc84d94edff86b0de923da3fbd20c185e
text_sha256: a54416736e8ee40ec52f85b889a3c605609716f2d816eb240d0a9be7c3a722a8
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Look at what i found in Comodo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-03_look-at-what-i-found-in-comodo.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f015a7df908bf903daffcd1f383e5c3cc84d94edff86b0de923da3fbd20c185e`
- Text SHA256: `a54416736e8ee40ec52f85b889a3c605609716f2d816eb240d0a9be7c3a722a8`


## Content

---
title: "Look at what i found in Comodo"
url: "https://maordayanofficial.medium.com/look-at-what-i-found-in-comodo-57d62af2f263"
authors: ["Maor Dayan (@mord1234)"]
programs: ["Comodo"]
bugs: ["Stored XSS", "Reflected XSS"]
publication_date: "2020-08-03"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 4357
scraped_via: "browseros"
---

# Look at what i found in Comodo

Look at what i found in Comodo
Maor Dayan - מאור דיין
Follow
5 min read
·
Aug 3, 2020

3

First let’s start with what is Comodo?

Comodo Security Solutions, Inc. is a cybersecurity company headquartered in Clifton, New Jersey in the United States.

The firm operates a certificate authority that issues SSL certificates, and offers information security products for both enterprises and consumers.

The company also helped on setting standards by contributing to the IETF (Internet Engineering Task Force) DNS Certification Authority Authorization (CAA) Resource Record. “Wikipedia”

Press enter or click to view image in full size

Now that you know what is Comodo, let’s move to the next part.

On Comodo’s website, I found 6 vulnerabilities, 2 Stored XSS and 4 Reflected XSS

Where did i find these vulnerabilities?

https://support.comodo.com — Stored XSS that can be used against the help desk employees
https://servicedesk.comodo.com/ — Stored XSS that can be used against the help desk employees
https://blog.comodo.com — Reflected XSS
https://verdict.valkyrie.comodo.com — Reflected XSS
https://verdict-devops.valkyrie.comodo.com — Reflected XSS
https://www.comodosecuritycouncil.com — Reflected XSS

I believe that most of you know what is XSS and the types of XSS, but i’ll give a short explanation for those who don’t know:

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy. Cross-site scripting carried out on websites accounted for roughly 84% of all security vulnerabilities documented by Symantec up until 2007. In 2017, XSS attacks were still considered a major threat vector. XSS effects vary in range from petty nuisance to significant security risk, depending on the sensitivity of the data handled by the vulnerable site and the nature of any security mitigation implemented by the site’s owner network. “Wikipedia”

Types of XSS found in Comodo.com:

Reflected XSS — Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim’s browser.

The script is activated through a link, which sends a request to a website with. a vulnerability that enables execution of malicious scripts. “imperva”

Stored XSS — Stored XSS, also known as persistent XSS, is the more damaging of the two. It occurs when a malicious script is injected directly into a vulnerable web application. “imperva”

_________________________________________________________________

Reflected XSS at https://blog.comodo.com
Press enter or click to view image in full size

Vulnerable Parameters:

track
af

those parameters are used to track users around the website and in any page in the code those parameters are encoded but in the blog section of the website Comodo just put a simple defence, every time someone enter “ or “>< the system automatically added \ to the start and blocked this code from been executed, how did i bypassed it? with a simple apostrophe: ‘ like:

‘“><svg onload=alert(1)>

Yeah that simple…

The impact of this vulnerability:
Attacker can use it to redirect the ‘victim’ from Comodo’s website to a phishing page.
Automatic malware download
Attacker can use it to execute js code at the ‘victim’ browser to steal cookies,steal information etc…

_________________________________________________________________

2. Reflected XSS at https://verdict.valkyrie.comodo.com

Press enter or click to view image in full size

Vulnerable Parameter:

url
The impact of this vulnerability:
Attacker can use it to redirect the ‘victim’ from Comodo’s website to a phishing page.
Automatic malware download
Attacker can use it to execute js code at the ‘victim’ browser to steal cookies,steal information etc…

_________________________________________________________________

Get Maor Dayan - מאור דיין’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Reflected XSS at https://verdict-devops.valkyrie.comodo.com

Press enter or click to view image in full size

Vulnerable Parameter:

domain
The impact of this vulnerability:
Attacker can use it to redirect the ‘victim’ from Comodo’s website to a phishing page.
Automatic malware download
Attacker can use it to execute js code at the ‘victim’ browser to steal cookies,steal information etc…

_________________________________________________________________

4. Reflected XSS at https://www.comodosecuritycouncil.com

Press enter or click to view image in full size

Vulnerable Parameter:

s
The impact of this vulnerability:
Attacker can use it to redirect the ‘victim’ from Comodo’s website to a phishing page.
Automatic malware download
Attacker can use it to execute js code at the ‘victim’ browser to steal cookies,steal information etc…

_________________________________________________________________

5. Stored XSS at https://support.comodo.com

The impact of this vulnerability:

This Stored XSS can be used against the company(and other companies that use their service) help desk workers from https://support.comodo.com if a js script will be executed at the side of the workers it can be very dangerous to the company! another thing is after the ticket submission the attacker can take the link and just send it to anyone this link is public and can be access without an account !! (in the next Stored XSS i proved that it can be used against the workers)

_________________________________________________________________

6. Stored XSS at https://servicedesk.comodo.com/

Press enter or click to view image in full size
Press enter or click to view image in full size

if you know Comodo you know they have a service desk service (they probably using it themself for their Support center), but think what can happen if this support center has Stored XSS vulnerability that can be used against your company, this is what happens here and below, you will see the POC video that proves that this can be used against the company employees

POC:

In this POC i created my own account and started a help desk service to prove they have Stored XSS vulnerability at the help desk workers side.

The impact of this vulnerability:

This Stored XSS can be used against the company(and other 200+ companies that use their service) help desk workers from https://servicedesk.comodo.com, if a js script will be executed at the side of the workers it can be very dangerous to the company! another thing is after the ticket submission the attacker can take the link and just send it to anyone this link is public and can be access without an account !! (in the next Stored XSS i proved that it can be used against the workers)

_________________________________________________________________

I reported about the vulnerabilities and those vulnerabilities have been Fixed by Comodo IT Department

Maor Dayan.

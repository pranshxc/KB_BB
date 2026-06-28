---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-08_asus-control-center-an-information-disclosure-and-a-database-connection-clear-te.md
original_filename: 2018-05-08_asus-control-center-an-information-disclosure-and-a-database-connection-clear-te.md
title: Asus Control Center – An Information Disclosure and a database connection Clear-Text
  password leakage Vulnerability
category: documents
detected_topics:
- access-control
- command-injection
- mfa
- rate-limit
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- mfa
- rate-limit
- information-disclosure
- api-security
language: en
raw_sha256: 22f49e2f8ce4fbcc39d6ccc7f9e6df2f9bfdf33a5bdf4f3543a662592a7d5e0f
text_sha256: 95d72db099b97ee897520d12787e5182093da71cc0271abafc94fe7f945e3e75
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Asus Control Center – An Information Disclosure and a database connection Clear-Text password leakage Vulnerability

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-08_asus-control-center-an-information-disclosure-and-a-database-connection-clear-te.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa, rate-limit, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `22f49e2f8ce4fbcc39d6ccc7f9e6df2f9bfdf33a5bdf4f3543a662592a7d5e0f`
- Text SHA256: `95d72db099b97ee897520d12787e5182093da71cc0271abafc94fe7f945e3e75`


## Content

---
title: "Asus Control Center – An Information Disclosure and a database connection Clear-Text password leakage Vulnerability"
page_title: "Asus Control Center – An Information Disclosure and a database connection Clear-Text password leakage Vulnerability – Seekurity"
url: "https://www.seekurity.com/blog/general/asus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability/"
final_url: "https://seekurity.com/blog/2018/05/08/admin/general/asus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability"
authors: ["Mohamed A. Baset"]
programs: ["Asus"]
bugs: ["Broken authorization", "Information disclosure"]
publication_date: "2018-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5886
---

What is Asus Control Center?

ASUS Control Center is a whole new centralized IT management software. The software is capable of monitoring and controlling ASUS servers, workstations, and commercial products including notebooks, desktops, All-in-One (AiO) PCs, thin client, and digital signage.

![](https://seekurity.com/blog/wp-content/uploads/2018/05/Screen-Shot-2018-05-07-at-11.25.41-PM.png)

ASUS is focusing on providing convenient, suitable, secured and cost saving solutions for enterprises, small and medium-sized businesses, and data centers across every industry. With the help of ASUS Control Center, your organization is primed to deal with the demands of the most challenging modern IT environments. ~”ASUS CONTROL CENTER WEBSITE”

### **Long story short:**

During our free-time bug hunting (under responsible disclosure rules) we have discovered a misconfiguration issue which led to a critical Information Disclosure vulnerability in their “Asus Control Center” during conducting a passive reconnaissance we have discovered that their Apache Tomcat installation is leaking its configuration file to the public which contains a clear-text database connection password=***REDACTED***

After that we have contacted Asus asking permission for escalation to prove that our PoC is working but they replied us that they acknowledge the issue as it is without any going further so we had to report it as it is.

Then the issue got fixed:

![](https://seekurity.com/blog/wp-content/uploads/2018/05/Screen-Shot-2018-03-19-at-11.11.24-AM.png)

And after that we’ve got an acknowledgment for our submission:

![](https://seekurity.com/blog/wp-content/uploads/2018/05/Screen-Shot-2018-05-07-at-10.31.48-PM.png)  
Hall of Fame link: <https://www.asus.com/Static_WebPage/ASUS-Product-Security-Advisory/>

Vulnerable Product Page: [https://asuscontrolcenter.asus.com ](https://asuscontrolcenter.asus.com)

Vulnerable Link: <http://asuscontrolcenter.asus.com/META-INF/context.xml>

.

### **Time for some conclusion:**

  1. For bug hunters: Do a recon on your target first before anything, Dig into their deep secrets and Brute-force their hidden resources also as a gift use our finding Google dork “ _inurl:/META-INF/context.xml_ ” and **Happy Hunting**!
  2. For server-admins, Developers, Maintaining monkeys: Please take care about your installations and its configurations and be sure that any of sensitive files are exposed to the internet specially if you have “Apache Tomcat” installation aaaand **Stay Safe Please**!

Thanks for reading!

.  
.  
.  
**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F05%2F08%2Fadmin%2Fgeneral%2Fasus-control-center-an-information-disclosure-and-a-database-connection-clear-text-password-leakage-vulnerability&linkname=Asus%20Control%20Center%20%E2%80%93%20An%20Information%20Disclosure%20and%20a%20database%20connection%20Clear-Text%20password%20leakage%20Vulnerability "Gmail")[](https://www.addtoany.com/share)

An  and  Asus  Center  Clear-Text  connection  Control  database  disclosure  Information  leakage  password  Vulnerability

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-08_self-xss-to-stored-through-idor.md
original_filename: 2023-03-08_self-xss-to-stored-through-idor.md
title: Self XSS To Stored Through IDOR/
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
language: en
raw_sha256: 3e7d31cfa1842d40aef861b40b952b8104f8e14c6ec011c4efe64fa3cf6cb0ca
text_sha256: fc1d36233372ae8ea577f0eba4e159277702db914c812b43ca7a753bf4e6e0bb
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Self XSS To Stored Through IDOR/

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-08_self-xss-to-stored-through-idor.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `3e7d31cfa1842d40aef861b40b952b8104f8e14c6ec011c4efe64fa3cf6cb0ca`
- Text SHA256: `fc1d36233372ae8ea577f0eba4e159277702db914c812b43ca7a753bf4e6e0bb`


## Content

---
title: "Self XSS To Stored Through IDOR/"
page_title: "Self XSS to Stored XSS through IDOR"
url: "https://arben.sh/bugbounty/SelfXSS-To-Stored-Through-IDOR/"
final_url: "https://arben.sh/bugbounty/SelfXSS-To-Stored-Through-IDOR/"
authors: ["Arben Shala (@arbennsh)"]
bugs: ["IDOR", "Self-XSS", "Stored XSS"]
publication_date: "2023-03-08"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1405
---

![image50](/assets/images/50.png)

**Table of Contents:**

  * Summary
  * Steps
  * Suggested Fix

# Summary

In this blog post I will explain how I turned a Self-XSS (cross-site scripting) vulnerability into a Stored-XSS by chaining it with an IDOR (insecure direct object reference) vulnerability. By chaining these two, I was able to turn a limited attack into a much more serious one. But first, let’s define these terms: 

**XSS** (cross-site scripting) is a type of vulnerability that allows an attacker to inject malicious code into a website, which is then executed by the victim’s browser, while on the other side, **IDOR** is a type of vulnerability that occurs when an application exposes internal object references, such as database IDs, in a way that allows an attacker to manipulate them. This can be exploited to access sensitive information or perform unauthorized actions. 

**Where did the vulnerability occur?**

An admin user could create his own folder structure within the web application. The created folder’s name was not properly sanitized, which allowed the attacker to inject malicious javascript code. Because only the owner of the folder could see and access it, this resulted in a Self-XSS. Due to the presence of an IDOR, an attacker could use it to increment the organization ID, transforming this vulnerability into a stored XSS that could attack other organization administrators and possibly takeover their accounts. Making it even worse, this could also be exploited from low-privileged users. 

Because there was no WAF (web application firewall) and the organizational IDs were easily guessable, this flaw was easily exploited and demonstrates the need of properly securing web applications and protecting them against all types of vulnerabilities.

# Steps

I’ve logged into an admin account and proved that a folder containing a malicious payload was not present, as seen on the screenshot below.

![image51](/assets/images/51.png)

Now using a low-privileged account, I’ve created a new folder and intercepted the request in order to modify the data before the folder is created on the backend.

![image52](/assets/images/52.png)

As seen on the screenshot above, I modified the following data: 
  
  
  project_id=0
  &parent_folder_id=7 //<- Admin's main folder
  &company_id=10 //<- Admin's Company
  &client_id= 
  &folder_name=><img+src=x+onerror=alert(document.domain)>  // <- malicious payload
  &addFolderBtn=+Add+
  

Heading back to the admin account, we can see that the malicious folder has been created. ![image53](/assets/images/53.png)

In order for the payload to get executed, the victim, in this case the admin user should perform an action such as “Previewing” or “Moving” any of the present files inside that structure.

![image54](/assets/images/54.png)

![image55](/assets/images/55.png)

# Suggested Fix

In order to mitigate XSS (cross-site scripting) attacks, the below requirements should be followed (as suggested by [OWASP](https://owasp.org)): 

  * Require strong input validation. Do not accept untrusted input or HTML content in your application unless required. If needed, perform HTML encoding.
  * Always perform output encoding. Do not render or process input as it is. Perform encoding, escaping, or any technique to break the structure of a malicious payload so it is not rendered.
  * Use libraries and software components, such as the [OWASP ESAPI](https://owasp.org/www-project-enterprise-security-api/), which provide reusable software components for input validation, escaping, and more.

Whereas for IDOR (insecure direct object reference) the below checks should be in place: 

  * **Use per user or session indirect object references**. This prevents attackers from directly targeting unauthorized resources
  * **Check access**. Each use of a direct object reference from an untrusted source must include an access control check to ensure the user is authorized for the requested object.

_Thank you for taking the time to read this, and I hope you’ll find it useful._

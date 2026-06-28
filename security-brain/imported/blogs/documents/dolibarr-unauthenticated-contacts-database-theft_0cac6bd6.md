---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-13_dolibarr-unauthenticated-contacts-database-theft.md
original_filename: 2023-03-13_dolibarr-unauthenticated-contacts-database-theft.md
title: 'Dolibarr : unauthenticated contacts database theft'
category: documents
detected_topics:
- sso
- xss
- sqli
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- sso
- xss
- sqli
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: 0cac6bd6d0320f93738ebbbd42571e5e9b81cc7e12152e73f2d9d034fe56b433
text_sha256: 7fb91ac742907c85afb3c7d5d7c92133c9d9ffa5d0600b91fc979fae23e4794e
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Dolibarr : unauthenticated contacts database theft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-13_dolibarr-unauthenticated-contacts-database-theft.md
- Source Type: markdown
- Detected Topics: sso, xss, sqli, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `0cac6bd6d0320f93738ebbbd42571e5e9b81cc7e12152e73f2d9d034fe56b433`
- Text SHA256: `7fb91ac742907c85afb3c7d5d7c92133c9d9ffa5d0600b91fc979fae23e4794e`


## Content

---
title: "Dolibarr : unauthenticated contacts database theft"
page_title: "Dolibarr : unauthenticated contacts database theft | DSecBypass"
url: "https://www.dsecbypass.com/en/dolibarr-pre-auth-contact-database-dump/"
final_url: "https://www.dsecbypass.com/en/dolibarr-pre-auth-contact-database-dump/"
authors: ["Vladimir"]
programs: ["Dolibarr"]
bugs: ["SQL injection", "Security code review"]
publication_date: "2023-03-13"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1387
---

# Dolibarr : unauthenticated contacts database theft

Mar 13, 2023

![Dolibarr logo ](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolibarr_logo-300x150.png)

Vladimir had the opportunity to test the security of the Open Source CRM software [Dolibarr](https://www.dolibarr.org/ "Dolibarr official website") during an [intrusion test](https://www.dsecbypass.com/en/website-pentest/ "Website security audit") of a business tool.

> Dolibarr ERP CRM is a modern software package to manage your company or foundation’s activity (contacts, suppliers, invoices, orders, stocks, agenda, accounting, …). It is open source software (written in PHP) and designed for small and medium businesses, foundations and freelancers. 
> 
> Ref: https://github.com/Dolibarr/dolibarr  
> 

Our pentester discovered a **critical vulnerability** exploitable by an **unauthenticated attacker**. It provides access to a **competitor’s entire customer file,** prospects, suppliers, and potentially employee information if a contact file exists. Both public and private notes can also be retrieved. Very easy to exploit, it **affects Dolibarr 16.x versions**.

**EDIT (22/03/2023)** : Dolibarr version 16.0.5 fixes this vulnerability for v16. (<https://github.com/Dolibarr/dolibarr/blob/16.0.5/ChangeLog#L34>).

**EDIT2 (13/06/2023)** : CVE-2023-33568 assigned.**  
**

## Discovery of the vulnerability

In order to perform tests on the software itself without impacting the client’s production, and having access to as much information as possible, the consultant created a local Dolibarr environment in the identified version.

The containerized image <https://hub.docker.com/r/tuxgasy/dolibarr> allows one to have a functional environment in minutes with Docker to start hunting for vulnerabilities. The `tuxgasy/dolibarr:16` image was used to discover this vulnerability.

Without necessarily trying to delve too much into the details of the Dolibarr code base, the auditor simply listed all the PHP files accessible from the root of the web server in order to identify those which are accessible without authentication:

> **find . -type f -name “*.php”**

One of the scripts thus accessible attracts attention because its response differs from the others:<https://github.com/Dolibarr/dolibarr/blob/16.0.4/htdocs/public/ticket/ajax/ajax.php>.

Reading the PHP code instructs us on the required parameters: **_action_** and **_email_**.

In particular, **_action_** must be equal to “**getContacts** “.

When all conditions are met, the following response is returned to the unauthenticated user:  
![Dolibarr ticket ajax](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_first_try.png)Dolibarr integrates some protections and checks that the variables sent by users do not contain suspicious patterns (XSS, SQL injections):

![Dolibarr WAF example](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_example_waf-1.png)

If the parameters have been protected in this way, the injections are therefore generally more complex to exploit.

We are therefore currently in the presence of unauthenticated access to the details of a contact, provided that the attacker knows the email address associated with it.

Digging deeper into the PHP code, the pentester lands on the SQL query called:

![SQL query getContacts Dolibarr](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_sql_like_contact.png)

We can observe the use of the SQL LIKE operator: with a bit of luck the ‘**%** ‘ character can be used to transform the query and make it return all the records!

![Dolibarr unauthenticated contact database dump](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_json_dump_unauth.png)

All contact details are returned in a single request.

A sorting on a few fields demonstrates the interest of this vulnerability:

![Dolibarr vulnerability contacts details](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_parse_json_basique-1-1024x340.png)

An attacker could access a **competitor’s entire customer file** , suppliers, and potentially employee information if a contact file exists. Both public and private notes can also be retrieved.

Attacker can get other information such as technical data about the database:

![Dolibarr vulnerability database information](https://www.dsecbypass.com/wp-content/uploads/2023/02/dolib_json_dump_unauth_db_data-1024x47.png)

## Impact & PoC

Dolibarr 16.x versions are affected. Version 17 disables access to this page by default, a specific Dolibarr option must be set for it to be accessible again.

The estimated CVSSv3 score is 7.5 ([https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N&version=3.1](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N&version=3.1)), however the nature of the data and the ease of exploitation make it **a critical vulnerability**.

Linux command to reproduce the vulnerability and display some arbitrary fields:

> **curl -sk ‘[URI_DOLIBARR]/public/ticket/ajax/ajax.php?action=getContacts &email=%’ | jq -r ‘.contacts[] | {id, socname, poste, email, phone_perso, phone_pro, note_public, note_private}’**

## Recommendations

Business tools as important as an ERP/CRM must be properly secured:

  * Open access to the Internet only if strictly necessary (prefer VPN access)
  * Only use the plugins useful for your use cases
  * Perform regular account reviews
  * Keep the various software components up to date
  * Ensure that your access policy is correctly implemented (password complexity, 2FA, …)
  * Implement, and maintain, a policy of least privilege
  * Perform regular penetration testing (regardless of application exposure)

✅ Many Dolibarr instances are exposed on the Internet: for those which are in version 16.x remember to upgrade quickly!

## Communication with the software publisher

Dolibarr’s Coordinated Disclosure Process is documented at the following URL: <https://github.com/Dolibarr/dolibarr/security/policy>.

The firs answer was (very) fast. On the other hand, the Dolibarr ecosystem could gain in security by communicating in a clear and precise manner on the vulnerabilities discovered and fixed in a centralized place, such as the Github “Security Advisories”.

21/02/2023 : First email sent by Vladimir following the Dolibarr process

21/02/2023 : Response from developer Eldy validating the vulnerability and indicating that the feature in question will be disabled with Dolibarr 17

05/03/2023 : Dolibarr v17 released

14/03/2023 : Article published

🛡️ DSecBypass accompanies you on the [security audits of your business applications](https://www.dsecbypass.com/en/website-pentest/ "Internal penetration tests on your business applications"). Do not hesitate to [contact ](https://www.dsecbypass.com/en/contact/)us for additional information and/or a personalized quote 📝.

[CONTACT US](https://www.dsecbypass.com/en/contact/)

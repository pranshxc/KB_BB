---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-24_stored-xss-in-the-heart-of-the-russian-email-provider-giant-mailru.md
original_filename: 2017-06-24_stored-xss-in-the-heart-of-the-russian-email-provider-giant-mailru.md
title: Stored XSS in the heart of the Russian email provider giant (Mail.ru)
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: a90c08841cab47d5956804bd5156f63bbee3dc97de6700f7869ebdb9b5b38260
text_sha256: 0580cc2e1f40b9a58b153a3cf329552cdc86594bdf023ffa4d32c2db1f0ee2ec
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS in the heart of the Russian email provider giant (Mail.ru)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-24_stored-xss-in-the-heart-of-the-russian-email-provider-giant-mailru.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `a90c08841cab47d5956804bd5156f63bbee3dc97de6700f7869ebdb9b5b38260`
- Text SHA256: `0580cc2e1f40b9a58b153a3cf329552cdc86594bdf023ffa4d32c2db1f0ee2ec`


## Content

---
title: "Stored XSS in the heart of the Russian email provider giant (Mail.ru)"
page_title: "Stored XSS in the heart of the Russian email provider giant (Mail.ru) – Seekurity"
url: "https://www.seekurity.com/blog/general/stored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru/"
final_url: "https://seekurity.com/blog/2017/06/24/seif-elsallamy/general/stored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru"
authors: ["Seif Elsallamy (@seifelsallamy)"]
programs: ["Mail.ru"]
bugs: ["Stored XSS"]
bounty: "600"
publication_date: "2017-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6173
---

Hi, I’m Seif Elsallamy a bug hunter from Seekurity Team, Today i will show you a critical reflected Cross Site Scripting bug affecting mail.ru and could be used as an [XSS worm ](https://en.wikipedia.org/wiki/Samy_\(computer_worm\))but first let’s dive into some general information.  
**  
**

## **What is mail.ru?**

[mail.ru](https://en.wikipedia.org/wiki/Mail.Ru) is a Russian mailing services like yahoo, hotmail and gmail.  
Mail.Ru Group, ООО (commonly referred to as Mail.Ru) is a Russian Internet company. It was started in 1998 as an e-mail service and went on to become a major corporate figure in the Russian-speaking segment of the Internet. As of 2013 according to comScore, websites owned by Mail.ru collectively had the largest audience in Russia and captured the most screen time. Mail.Ru’s sites reach approximately 86% of Russian Internet users on a monthly basis and the company is in the top 5 of largest Internet companies, based on the number of total pages viewed. Mail.ru controls the 3 largest Russian social networking sites. It operates the second and third most popular Russian social networking sites, Odnoklassniki and Moi Mir, respectively. Mail.ru holds 100% of shares of Russia’s most popular social network VKontakte and minority stakes in Qiwi, formerly OE Investments (15.04%). It also operates two instant messaging networks (Mail.Ru Agent and ICQ), an e-mail service and Internet portal Mail.ru, as well as a number of online games.

## **What is Cross-site scripting AKA XSS? And why ours is stored?**

[Cross-site scripting](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\)) simply is a security bug that may affect websites allowing users (Attackers) to inject scripts (javascript) to another users (Victims) to modify or steal there data as example, session emails passwords page content. Stored Cross-site scripting is an XSS type which if successfully injected it will be stored permanently in the application’s database and retrieved whenever the user call back a vulnerable page calling this stored payload

## What is eml files?

Used by many email clients including Novell GroupWise, Microsoft Outlook Express, Lotus notes, Windows Mail, Mozilla Thunderbird, and Postbox. .eml files contain the email contents as plain text in MIME format, containing the email header and body, including attachments in one or more of several formats.

Now lets back to mail.ru bug….

Mail.ru is parsing .eml files and fetches the “subject” automatically then reflecting it in the email subject without sanitizing, filtering or validating it for malicious content which was the main root cause for our Stored XSS to occur.

So to reproduce this behavior, We simply created a new eml file “test.eml”, Edited this file and included a simple XSS payload ie. “subject : <script>alert(“XSS”);</script>” then we saved the file, After that we went to we navigated to “m.mail.ru” (the mobile version of mail.ru), Created a new mail, uploaded the eml file and then we hit “send”

Once a victim receive our malicious message, Opening it, you will find this lovely and cute popup alert box with word “XSS” inside it which mean that the script has been executed so that’s mean XSS occurs.

## Impact of a simple attack scenario:

Imagine that an XSS work behavior which spreads over your mail.ru contacts, send the same malicious message to all of your contact with a JS execution of stealing user’s session and act on behalf of the currently logged in user! And possibilities are endless here.

## **PoC Video:**

We responsibly disclosed the vulnerability to Mail.ru through their [HackerOne](https://hackerone.com/reports/116570) bug bounty program and they fixed it and rewarded us with a generous bounty, Thanks Mail.ru

Original source of the report: <https://hackerone.com/reports/116570>

## **Hey!**

Building a website, an application or any kind of business? Or already have one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F06%2F24%2Fseif-elsallamy%2Fgeneral%2Fstored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru&linkname=Stored%20XSS%20in%20the%20heart%20of%20the%20Russian%20email%20provider%20giant%20%28Mail.ru%29 "Gmail")[](https://www.addtoany.com/share)

(Mail.ru)  email  giant  in  provider  Russian  Stored  the  XSS

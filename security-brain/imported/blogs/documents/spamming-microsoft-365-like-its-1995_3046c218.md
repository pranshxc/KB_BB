---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-14_spamming-microsoft-365-like-its-1995.md
original_filename: 2023-12-14_spamming-microsoft-365-like-its-1995.md
title: 'Spamming Microsoft 365 Like It’s 1995 '
category: documents
detected_topics:
- sso
- access-control
- command-injection
- otp
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- otp
- api-security
- cloud-security
language: en
raw_sha256: 3046c218985923e400733caf0449014f9fb9ed3d5409e69178d56b80c363fdbc
text_sha256: 3343309834ee95c94e596c5b5642806cc47db7cbb873c11d4e7e008f545c7c84
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Spamming Microsoft 365 Like It’s 1995 

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-14_spamming-microsoft-365-like-its-1995.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, otp, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `3046c218985923e400733caf0449014f9fb9ed3d5409e69178d56b80c363fdbc`
- Text SHA256: `3343309834ee95c94e596c5b5642806cc47db7cbb873c11d4e7e008f545c7c84`


## Content

---
title: "Spamming Microsoft 365 Like It’s 1995 "
page_title: "Spamming Microsoft 365 Like It’s 1995  - Black Hills Information Security, Inc."
url: "https://www.blackhillsinfosec.com/spamming-microsoft-365-like-its-1995/"
final_url: "https://www.blackhillsinfosec.com/spamming-microsoft-365-like-its-1995/"
authors: ["Steve Borosh (@424f424f)"]
programs: ["Microsoft (Exchange)"]
bugs: ["Phishing"]
publication_date: "2023-12-14"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 626
---

14 Dec 2023

[Phishing](https://www.blackhillsinfosec.com/category/red-team/phishing/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Social Engineering](https://www.blackhillsinfosec.com/category/red-team/social-engineering/), [Steve Borosh](https://www.blackhillsinfosec.com/category/author/steve-borosh/)

# [Spamming Microsoft 365 Like It’s 1995 ](https://www.blackhillsinfosec.com/spamming-microsoft-365-like-its-1995/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Untitled-design-2-150x150.png)

| [Steve Borosh](https://twitter.com/424f424f)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/BLOG_chalkboard_00649-1024x576.png)

I previously blogged about spoofing Microsoft 365 using the direct send feature enabled by default when creating a business 365 Exchange Online instance (<https://www.blackhillsinfosec.com/spoofing-microsoft-365-like-its-1995/>). Using the direct send feature, it may be possible to send emails from outside or inside of the organization to other users in the tenant “by design.” A “smart host” is created with the default Exchange Online instance at “company.mail.protection.outlook.com”. A quick `nslookup company.mail.protection.outlook.com` will show the IP addresses of the smart host if it exists. If a TLD is associated with the Azure tenant, the smart host may have a “-TLD” like company-io.mail.protection.outlook.com.

In this blog post, I will cover some default protections provided by Microsoft, show my research methodology, land some spoofed device code phishing emails in a default tenant inbox, and discuss mitigations.

## Default Protections

Some default protections do apply from the start, as documented here: <https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spam-protection-about?view=o365-worldwide#default-anti-spam-policy>.

Per Microsoft’s documentation:

Every organization has a built-in anti-spam policy named Default that has the following properties:

  * The policy is the default policy (the **IsDefault** property has the value True), and you can’t delete the default policy.
  * The policy is automatically applied to all recipients in the organization, and you can’t turn it off.
  * The policy is always applied last (the **Priority** value is **Lowest** and you can’t change it).1

Exchange Online Protection (EOP) helps reduce junk email using proprietary spam filtering, also known as content filtering. EOP attempts to learn from known spam and phishing threats to protect end-users.

EOP’s spoof intelligence attempts to detect if an email was spoofed and either sends it to Junk (still making it into the user’s mailbox) or sends it to Quarantine.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture1-1.png)Figure 1 – Spoof Intelligence

Exchange Online administrators can create policies above the default policies but may not disable them. The strictest policies are applied first.2

## Conducting Research

_Preemptive disclaimer: Throughout this research, results varied due to the proprietary nature of Microsoft’s email protections. An email with a ‘from’ address from a certain domain might make it to inboxes in a tenant with default protections, but not another tenant with unidentified filter tags applied. Real-world testing against domains with Exchange Online and a third-party email gateway resulted in successful spoofing, as well with varying domains that were not on an “allow” list._

_Organizations should follow similar procedures to test the efficacy of anti-spoofing and SPAM filters._

To evaluate default SPAM protections against an *.onmicrosoft.com business tenant, I used the Azure Cloud33 shell to send messages via SMTP through the target organization’s Direct Send smart host “<domain>.mail.protection.outlook.com”.

Though it is possible to use telnet (yes, I said telnet), PowerShell provides the Send-MailMessage command that wraps the connection for you.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture2-1.png)Figure 2 – Send-MailMessage

You may use an html-formatted file as a template. Note that the “-Body” flag takes a string format. Convert the html file into a string like so:
  
  
  $email = Get-Content ./email.html | Out-String

To simplify the research process, I wrote a PowerShell script to wrap Send-Mail message into an easy-to-use email defense efficacy testing tool: <https://github.com/rvrsh3ll/FindIngressEmail>.

I used a very simple device code html template as shown below. If your target uses the Outlook desktop client application, the app will display a non “href” tag URL as a link, which may lower the SPAM score in some content filtering instances.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture3-1.png)Figure 3 – Device Code Template

Note: The Azure Console will timeout after 20 minutes of inactivity. I suggest using “Start-Job” to background your command. Then, keep the terminal alive with “watch ls”.

If you’re testing a single target domain, you might use a command like:
  
  
  Start-Job -name asciiDeviceCode -ScriptBlock {  Import-Module /home/rev/FindIngressEmails.ps1; Invoke-FindIngressEmail -smtpServer “<insert target domain>.mail.protection.outlook.com" -Subject "Microsoft 365 Session Sync Required" -bodyFile /home/rev/DeviceCodePhish.html -fromFile /home/rev/from_domains.txt -toEmail $_ -Delay 10 -Encoding ascii}} 

The first test was spoofed from [[email protected]](/cdn-cgi/l/email-protection) to three separate default-protected Microsoft 365 tenants such as “bydesign[@]REDACTED.onmicrosoft.com”.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture4-1.png)Figure 4 – Target User Example ![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture5-1.png)Figure 5 – Sending Ascii Device Code Phish

The results started entering junk folders as seen below.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture6-1.png)Figure 6 – Ascii Device Code Phish Result

The ascii encoded email landed in two of three mailboxes’ junk folders. It did not land in the “bydesign@” mailbox. Oddly, it was not in quarantine either.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture7.png)Figure 7 – Quarantine

I tried the same email again from the same IP address and Cloud Shell hostname. This time with UTF32 encoding.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture8.png)Figure 8 – Sending UTF32 Encoded Phish

This time, the emails landed in the junk folders of all three mailboxes.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture9.png)Figure 9 – UTF32 Encoded Phish in Junk-1 ![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture10.png)Figure 10 – UTF32 Encoded Phish in Junk-2

Next, to test whether the Cloud Shell IP range had any visible effect, I restarted the shell to obtain a new IP address and re-send the emails.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture11.png)Figure 11 – UTF32 Encoded Phish in Junk-2

Next, I changed the subject of the email and re-sent.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture12.png)Figure 12 – Subject Change

These emails also landed in the junk folders.

I changed the encoding to UTF7 and observed the results also landing in the junk folders.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture13.png)Figure 13 – UTF7 Phish ![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture14.png)Figure 14 – UTF7 Encoded Email in Junk

To dive a little deeper into the why this landed in the junk folder, I used <https://mha.azurewebsites.net> to parse the headers.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture15.png)Figure 15 – Analyzing utf-7 Email Headers

Next, I used this script — <https://github.com/mgeeky/decode-spam-headers> — to further analyze the headers. It can output a handy html file for review.
  
  
  python .\decode-spam-headers.py .\globo_header.txt -f html -o report.html 

The script will identify SPAM headers.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture16.png)Figure 16 – Globo.com SPAM Headers

Using a different domain email from address [[email protected]](/cdn-cgi/l/email-protection), I re-sent the same campaign.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture17.png)Figure 17 – Ascii Encoded Email from EIRCOM in Inbox

The same email template email landed in all three inboxes this time. This shows that the “From” domain’s email authorization settings, such as SPF, DKIM, and DMARC, may play a significant role in Microsoft’s determination of the SPAM confidence level.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture18.png)Figure 18 – Analyzing Ascii Headers

I then parsed these headers with the python script to show the difference between the globo.com header.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture19.png)Figure 19 – Eircom.net SPAM Headers

Notice the confidence level dropped to -1.

The emails contain a “X-EOPTenantAttributedMessage” header. I noticed this header did not identify the remote tenant that I sent the messages from. It identified the receiving tenant ID.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture20.png)Figure 20 – Tenant Attribution

These tests were performed using default tenant settings in Exchange Online Protection. Additional testing was performed against Black Hills Information Security (BHIS) ANTISOC customers using a mix of additional filters, transport rules, and third-party email gateways. In all cases where the smart host allowed sending of emails into the organization, BHIS was successful in landing device code phishing emails in the inbox of the organization. Including using “Known-Bad” templates such as the original TokenTactics device code phishing template. <https://github.com/rvrsh3ll/TokenTactics/blob/main/resources/example_phish.html>.

To test a large number of sending domains, the FindIngressEmails.ps1 script will take a list of email addresses, one-per-line.
  
  
  Import-Module ./FindIngressEmails.ps1
  Invoke-FindIngressEmail -smtpServer “yourclientorg.mail.protection.outlok.com” -Subject "Device Reset" -bodyFile ./emailTemplate.html -toEmail “[[email protected]](/cdn-cgi/l/email-protection)” -Delay 15 -RetryDelay 60 
  

Lastly, I sent a few hundred of these phishes to the three tenant simultaneously.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture21.png)Figure 21 – 133 Inbox

The first account received 133 inbox and 207 in junk.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture22.png)Figure 22 – 41 Inbox

The next mailbox had 41 in the inbox and 174 in junk.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture23.png)Figure 23 – 5 Inbox

A quick peek at <https://security.microsoft.com/quarantine> shows some landed in quarantine as well.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/12/Picture24.png)Figure 24 – Quarantined Emails

The results are very inconsistent between tenants however, the test shows that the same template is interpreted differently for various, some proprietary Microsoft rules.

## For Defenders

Unfortunately, I haven’t found a method to completely disable the smart host on Exchange Online. Since posting the original blog4 about spoofing Microsoft 365, the only effective solution I’ve encountered, doubtfully exhaustive, is to secure the smart host by restricting sending emails on behalf of the organization to IP address or certificate.5

## Closing

I hope this blog post highlights the need for Exchange Online administrators to continuously test the effectiveness of their inbound email controls and secure the Direct Send smart host from allowing arbitrary unauthenticated users from sending spoofed emails into the organization.

* * *

## References

  1. https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/anti-spam-protection-about?view=o365-worldwide#default-anti-spam-policy ↩︎
  2. https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/preset-security-policies?view=o365-worldwide#order-of-precedence-for-preset-security-policies-and-other-policies ↩︎
  3. https://learn.microsoft.com/en-us/azure/cloud-shell/overview ↩︎
  4. https://www.blackhillsinfosec.com/spoofing-microsoft-365-like-its-1995/ ↩︎
  5. https://learn.microsoft.com/en-us/exchange/troubleshoot/email-delivery/office-365-notice ↩︎

* * *

* * *

Enjoy this blog?

Steve teaches a class you can check out here:

**[Enterprise Attack Initial Access](https://www.antisyphontraining.com/on-demand-courses/enterprise-attack-initial-access-w-steve-borosh/)**

Available live/virtual and on-demand

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/11/AntiSyphon_3-1-150x150.png)

* * *

* * *

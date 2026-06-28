---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-15_smtp-injection-in-gsuite.md
original_filename: 2020-06-15_smtp-injection-in-gsuite.md
title: SMTP Injection in Gsuite
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: e51d860a067557c6c50b099a23dbee023e144d42a55a10e717904f1758abdf55
text_sha256: 2d0335e59a51363849c1eb107413cc4309ef1522623a511b14dd53e150e31a28
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# SMTP Injection in Gsuite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-15_smtp-injection-in-gsuite.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `e51d860a067557c6c50b099a23dbee023e144d42a55a10e717904f1758abdf55`
- Text SHA256: `2d0335e59a51363849c1eb107413cc4309ef1522623a511b14dd53e150e31a28`


## Content

---
title: "SMTP Injection in Gsuite"
url: "https://www.ehpus.com/post/smtp-injection-in-gsuite"
final_url: "https://www.ehpus.com/post/smtp-injection-in-gsuite"
authors: ["Zohar Shachar"]
programs: ["Google"]
bugs: ["SMTP injection"]
bounty: "3,133.7"
publication_date: "2020-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4494
---

# SMTP Injection in Gsuite

  * zohar shachar
  * Jun 15, 2020
  * 4 min read

Gsuite is an immensely powerful tool for account administration. It allows the administrator to control just about anything regarding the user accounts in his organization, from determining how one can login and which apps he can access, to which contacts are allowed and what Email headers should be applied. 

  

This last one sparked my interest. Modern email headers are somewhat of a ‘hack’ into SMTP, a very old communication protocol that is still very much in use by just about every person who is connected to the internet. This ‘hack’ means there are a lot of opportunities for mistakes when trying to mess with it. Tl;dr: Google is not immune from errors! Or in other words, Gsuite’s email configuration was vulnerable and allowed attackers to spoof email messages from Google’s servers.

  

  

**SMTP?**

The year is 2020 and SMTP is still with us. I guess not everyone is familiar with it, so let’s have a quick intro ([_check here_](https://www.acunetix.com/blog/articles/email-header-injection/) for more detailed information, or skip ahead if you know the basics).

SMTP is a simple, text based protocol that does not enforce authentication (yep, you read this right). Basically, if you can open a socket to an SMTP server you can instruct it to send an email to any address, and more importantly you can send this email **from any address**. This of course opens a whole bounce of issues, as you can not (natively) trust the origin of the email you just received (Is it really my bank contacting me? Is it really the queen sending me money?!) 

  

Generally, there are very few SMTP instructions that are native to the protocol. Are you ready? Here we go:

  1. **‘MAIL FROM’:** who sends the email. Again, natively this can be anything (including [_queen@yesIReallyAmTheQueen.com_](mailto:queen@yesIReallyAmTheQueen.com)) 

  2. **‘RCPT TO’:** Who the email is sent to.

  3. **‘DATA’:** The contents of the email. 

And.. that’s it. That’s right - no cc, no bcc, no subject. All these headers came later, and were hacked into the system. So how do you use them? You place these extra headers inside the ‘DATA’ header content. Basically, at the beginning of the ‘DATA’ contents you add any header you want, as long as both the sender and receiver know how to parse and read it. The convention (that was also added to the RFC) is that each header is put in a new line, and the header name / value are separated by ‘:’.  

Here is a quick example:

  

  
  
  SMTP FROM:
  admin@google.com
  SMTP TO:
  Victim@gmail.com
  DATA:
  bcc: attacker@gmail.com
  
  Send me all your money!!
  
  .

  

**Wait, so was it not the queen?!**

Obviously, email would not be a very useful tool if these issues remained unaddressed, and overtime various mechanisms were developed on top of SMTP to give some more assurance of identity and content. While I won’t go into details on these defenses, let’s keep one important thing in mind: the main tool used today to verify that the sender of the email is actually who he says he is, is DNS domain validation. If I own ‘google.com’, I can set a DNS record that instructs all SMTP servers in the world to only accept ‘google.com’ emails from me (all others will go to spam). If you can spoof email from Google’s own servers, there is no other mechanism that can verify the sender’s identity. 

  

**Back to Gsuite**

Now that we have our bearings, let’s head back to Gsuite. If you login to admin.google.com and navigate to Apps -> G Suite -> Settings for Gmail->Advanced settings->Routing, you have the option to ‘add a routing setting’ for inbound/outbound traffic. One of these optional setting is configuring a ‘custom header’ to be added to all emails:

  

[![](https://static.wixstatic.com/media/5527e6_7b27763477854a88993ce5a7743b764e~mv2.png/v1/fill/w_71,h_48,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_7b27763477854a88993ce5a7743b764e~mv2.png)](https://static.wixstatic.com/media/5527e6_7b27763477854a88993ce5a7743b764e~mv2.png)

Following the concepts detailed above, we can assume that these ‘custom headers’ will be added to the SMTP ‘data’ content. So if I could just add any header I wanted, I could manipulate the email content. However as evident from the image, that is not the case. Custom headers in Gsuite have a leading ‘X-’, so we don’t have full control of the header name. But wait! We said that by convention, every header is written in a new line. What if we can inject a new line as part of the header name? The next line will already be a new header, under our control!

  

Alas, that failed. Google made sure you cannot include newline chars into the header name. But then I noticed something else. Just beneath the ‘custom header’ option, there is the option to prepend a ‘custom subject’ to each mail. And as we know, there is no ‘subject’ in SMTP - It is just another header in the ‘DATA’ section. 

  

I launched up my proxy and added newline chars (‘\r\n’) into the’ subject’ setting:

  

[![](https://static.wixstatic.com/media/5527e6_bd6e6b4853434e04afc3f63fcea0dac6~mv2.png/v1/fill/w_48,h_20,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_bd6e6b4853434e04afc3f63fcea0dac6~mv2.png)](https://static.wixstatic.com/media/5527e6_bd6e6b4853434e04afc3f63fcea0dac6~mv2.png)

No errors were returned. I quickly sent a test email to the account, launched up gmail And saw this:

[![](https://static.wixstatic.com/media/5527e6_1c69e5181c4a48b7ac8746085fb8596e~mv2.png/v1/fill/w_49,h_21,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_1c69e5181c4a48b7ac8746085fb8596e~mv2.png)](https://static.wixstatic.com/media/5527e6_1c69e5181c4a48b7ac8746085fb8596e~mv2.png)

Alright! That’s a clear indication that the payload worked. The newline chars were rendered at the server side and the ‘subject’ header was split into several lines. As each header is represented in a new line, that meant the rest of the payload (what came after the newline chars) was pushed to the next header, which in this case was the email body. This is a successful SMTP injection!

  

I was now ready for a more interesting payload. I’ve changed the ‘subject’ setting again, this time to include a spoofed ‘From’ header:

[![](https://static.wixstatic.com/media/5527e6_22d8cb6f3ef34edba22f07b53c6dbcb6~mv2.png/v1/fill/w_49,h_3,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_22d8cb6f3ef34edba22f07b53c6dbcb6~mv2.png)](https://static.wixstatic.com/media/5527e6_22d8cb6f3ef34edba22f07b53c6dbcb6~mv2.png)

That worked too! Gmail presented this email as if it actually came from [_admin@google.com_](mailto:admin@google.com). I tweaked my payload a bit, and the final result can be seen here:

[![](https://static.wixstatic.com/media/5527e6_b830d93a97b54f30b810eeab9c607994~mv2.png/v1/fill/w_49,h_14,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/5527e6_b830d93a97b54f30b810eeab9c607994~mv2.png)](https://static.wixstatic.com/media/5527e6_b830d93a97b54f30b810eeab9c607994~mv2.png)

  

Yippy! I was now able to spoof emails from arbitrary ‘@google.com’ addresses :)

  

Timeline:

  * 01/05/2020 Issue reported to Google with initial payload

  * 01/13/2020 bug accepted by Google

  * 01/15/2020 I sent further details, including a working POC for [_admin@google.com_](mailto:admin@google.com)

  * 02/11/2020 reward (3133.7$) was issued

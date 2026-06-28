---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-31_business-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-block.md
original_filename: 2017-07-31_business-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-block.md
title: 'Business Logic Vulnerabilities Series: How I became invisible and immune to
  blocking on Instagram!'
category: documents
detected_topics:
- business-logic
- idor
- xss
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- business-logic
- idor
- xss
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: 741ae55d0ffcff2c3859c2e8a64fb5df899d60a77bc5c6ebb5996b79298c68cd
text_sha256: 95a293c864279fbd841209846f69aab229df80dc299ffddef1d17af6087b1e0f
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Vulnerabilities Series: How I became invisible and immune to blocking on Instagram!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-31_business-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-block.md
- Source Type: markdown
- Detected Topics: business-logic, idor, xss, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `741ae55d0ffcff2c3859c2e8a64fb5df899d60a77bc5c6ebb5996b79298c68cd`
- Text SHA256: `95a293c864279fbd841209846f69aab229df80dc299ffddef1d17af6087b1e0f`


## Content

---
title: "Business Logic Vulnerabilities Series: How I became invisible and immune to blocking on Instagram!"
page_title: "Business Logic Vulnerabilities Series: How I became invisible and immune to blocking on Instagram! – Seekurity"
url: "https://www.seekurity.com/blog/general/business-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram/"
final_url: "https://seekurity.com/blog/2017/07/31/ali-kabeel/general/business-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram"
authors: ["Ali Kabeel"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2017-07-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6133
---

Hey Folks,

Welcome back again, This is Ali Kabeel in case you don’t remember me read my first blog about [Abusing invitations systems](https://www.seekurity.com/blog/general/business-logic-vulnerabilities-series-a-brief-on-abusing-invitation-systems/).

In this blog we will be continuing our talk about [Business logic bugs](https://www.owasp.org/index.php/Testing_for_business_logic) and how dangerous and simple they can become, I will be showing you one of the simplest yet the most dangerous bugs I have found in the gigantic photo sharing app Instagram but first lets get an overview of some concepts and general knowledge.

###### What is Instagram? ~Wikipedia

Instagram is a mobile, desktop, and Internet-based photo-sharing application and service that allows users to share pictures and videos either publicly or privately. Instagram lets registered users upload photos or videos to the service. Users can apply various digital filters to their images, and add locations. They can add hashtags to their posts, linking the photos up to other content on Instagram featuring the same subject or overall topic. Instagram was acquired by Facebook in April 2012 for approximately US$1 billion in cash and stock.Soon enough after being acquired Instagram joined Facebook bug bounty program.

###### General features of social media applications:

A social media app generally has features such as follow, unfollow block, unblock, Private account, public account, inviting friends, connecting to other social media apps and adding applications to your account, etc… Those features must be tested thoroughly for bugs such as [XSS](https://www.owasp.org/index.php/Cross-site_Scripting_\(XSS\)), [IDOR](https://www.owasp.org/index.php/Unvalidated_Redirects_and_Forwards_Cheat_Sheet), [CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_\(CSRF\)), etc.. but most importantly these features must work as intended or else the app will be vulnerable to business logic attacks.

###### Background of bug hunting in Instagram:

I was searching around the “Block feature” and trying to understand what can I do after blocking somebody and the level of interaction i can have with somebody I have blocked.I figured out after blocking somebody I can mention them in any post and they won’t get a notification, I can tag them in pics and they won’t also get notifications. Those 2 trivial bugs were reported and both were refused as having low risk to users.

Determined to get in Facebook Hall of fame I continued my research to the successful end.

###### Why did the bug existed:

Following the rejection of those 2 bugs (Mentions and Tags) I came out with the nastiest of them all 😈 I can follow somebody after blocking them without unblocking them that is to say I am following you but blocking you simultaneously at the same time! So the bug existed because the app has broken logic where I could follow and block somebody at the same time.

This could be exploited from the app without any tools just block somebody then follow them. It is really that simple!

###### What is the impact of this bug?

  1. You don’t get notified of that follow I made after blocking you.
  2. I don’t appear in the followers list although the number of followers will increase by one.
  3. I see your photos, activities and everything related BUT you can’t block me, you don’t know I exist in your followers list in the first place 😀

Facebook fixed this bug and awarded a generous bounty reflecting the simplicity of exploitation as well as the high impact.

I hear some people are saying “Easy Money!” No it’s not, trust me, those kind of logical bugs need a well and full study of how the application in front of you operates (which takes time, and time is money for sure).

You can see a video of the bug [here](https://www.youtube.com/watch?v=be4UdQWNWcY)

Thanks for reading, Hope you enjoyed it!

## **A minute if you please!**

Building a website, an application or any kind of business? Or already have one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2017%2F07%2F31%2Fali-kabeel%2Fgeneral%2Fbusiness-logic-vulnerabilities-series-how-i-became-invisible-and-immune-to-blocking-on-instagram&linkname=Business%20Logic%20Vulnerabilities%20Series%3A%20How%20I%20became%20invisible%20and%20immune%20to%20blocking%20on%20Instagram%21 "Gmail")[](https://www.addtoany.com/share)

and  became  blocking  Business  How  I  immune  Instagram  invisible  Logic  on  Series  to  Vulnerabilities

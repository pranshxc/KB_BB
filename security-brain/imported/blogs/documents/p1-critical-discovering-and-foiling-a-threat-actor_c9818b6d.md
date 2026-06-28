---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-27_p1-critical-discovering-and-foiling-a-threat-actor.md
original_filename: 2020-09-27_p1-critical-discovering-and-foiling-a-threat-actor.md
title: 'P1: Critical - Discovering and Foiling a Threat Actor'
category: documents
detected_topics:
- jwt
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
tags:
- imported
- documents
- jwt
- idor
- command-injection
- otp
- rate-limit
- information-disclosure
language: en
raw_sha256: c9818b6dc270dc67f47a94ff244d5aa94ba775459d5ec3f70a4b087db32138d2
text_sha256: bca1767111117bfe65eb3c092d832dea66569fa68c6e3748bb8dca4189ea043a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# P1: Critical - Discovering and Foiling a Threat Actor

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-27_p1-critical-discovering-and-foiling-a-threat-actor.md
- Source Type: markdown
- Detected Topics: jwt, idor, command-injection, otp, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c9818b6dc270dc67f47a94ff244d5aa94ba775459d5ec3f70a4b087db32138d2`
- Text SHA256: `bca1767111117bfe65eb3c092d832dea66569fa68c6e3748bb8dca4189ea043a`


## Content

---
title: "P1: Critical - Discovering and Foiling a Threat Actor"
page_title: "Hack the Galaxy"
url: "https://johnjhacking.com/blog/p1-critical-discovering-and-foiling-a-threat-actor/"
final_url: "https://johnjhacking.com/blog/p1-critical-discovering-and-foiling-a-threat-actor/"
authors: ["Jackson Henry (@JacksonHHax)", "John Jackson (@johnjhacking)"]
bugs: ["Information disclosure"]
bounty: "1,550"
publication_date: "2020-09-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4233
---

* [ Home ](/)
  * [Blog](/blog)
  * [Research](/research)

  * [ Home ](https://johnjhacking.com)
  * [Blog](/blog)
  * [Research](/research)

# P1: Critical - Discovering and Foiling a Threat Actor

How Jackson and I managed to land a Critical Vulnerability Bounty - and through persistence, ensure that justice was served.

Published on Sep 27, 2020

Reading time: 5 minutes.

* * *

# P1: Critical - Discovering and Foiling a Threat Actor

# Disclaimers, Credits:

Thank you to everyone who helped validate any part of the project. It took a lot of work to figure out the extent of who was/is affected. I appreciate all of the help that we have received, with a special thank you to those who confirmed our suspicions.

As a general rule of thumb, we will have to redact specific parts of this writeup as well as completely leave out special homebrewed technology that would give away the affected organizations, or cause further damage.

# Summary

While working on a Private Bug Bounty Program for Hackerone, [Jackson](https://twitter.com/JacksonHHax "Twitter") and I found client-side laravel PHP debugging that allowed for the full takeover of a SQL Server, and account takeover of the Admin account for a Mail Marketing Application.

Upon further inspection, there was more than meets the eye. This Mail Marketing Application was custom built and used as a focal point for a malicious Mail Marketing campaign. We were able to discover this by looking at the SQL server logs and noting an extensive email database (millions of email addresses) coupled with millions of advertising emails sent out for random products. I consulted with an expert who wished to be unnamed over the phone and confirmed assumptions, fortifying my suspicions in a factual manner.

It was difficult to bridge the gap and make a full determination of what was going on at first. The server that we had initially found appeared to be owned by the company that we were searching for vulnerabilities on. Upon examining the DNS records of the server, the SOA (Start of Authority) was configured to utilize the Company Nameserver. This led us to believe that the asset was in scope.

1\. Unfortunately, we had made note of this to the program through Hackerone, and disagreements in the Program’s part that was played resulted in a (low) bounty.  
2\. Fortunately/Unfortunately, they were not the only Company being exploited - therefore the Mail Marketing company providing services to the other affected companies paid us for identifying these security issues for their customers.

# Process

  1. Enumeration began in every normal sense: subdomain finding with Amass, screenshots with Aquatone, Shodan queries, etc. Oddly enough, we noticed an IP address that appeared to be a mail server of some sort, and a quick scan revealed a Web Application.

  2. Navigating to the IP Address, we found a login portal, nothing that either of us had seen before, and reverse image searches revealed no similar applications:  
ex: http://X.X.X.X

(_The unique nature of this portal makes it so we cannot include pictures in this writeup_)

  3. What stuck out was this PHP Laravel Debugging Button:

![](/uploads/3-1.png)  
Without being experts, it was obvious that this button had some sort of functionality baked into it

  4. Upon clicking the button, many POST and GET requests were seen, in a neat and tidy list:

![](/uploads/4-1.png)

Our eyes lit up. We were able to see the client-side POST and GET requests, many with SQL Queries being sent to the backend. A little research helped us understand the functionality of the PHP DebugBar, and we started to see credentials, JWT tokens, full responses of the requests, etc.

![](/uploads/yellow-glasses-guy-27092020161326.jpg)

At this point - we knew it was good game. Now, we needed to document the leaked sensitive information, and see what we could do with it.

  5. Immediately, we discover admin credentials in a POST request to the login URL:

![](/uploads/5-1.png)

  6. We then attempted a login to this Mail Marketing Application, and we were immediately in. It was easy to celebrate at this point - we had full Command and Control of this application, and it appeared to be a central Email Marketing console with 13 different servers connected. It was actively running processes. To avoid disrupting any production activities, we logged out.

(_The unique nature of this application makes it so we cannot include pictures in this writeup_)

  7. Even though we had control over this application, we were not satisfied. After discussion we decided to see if we could do anything else besides Account Takeover. With a little bit of research we were able to find a URL that exposed .env variables on the client-side:

![](/uploads/7-1.png)

  8. OK. Once again our exploitation methodology began to heat up, not only did we have full control of the Application, we now owned the backend for the Application…maybe.

  9. We tried to authenticate to the MYSQL Server: `mysql -h x.x.x.x -u username -p`

**WE’RE IN**

![](/uploads/8-1.png)

  10. There wasn’t a point in continuing. The last thing we wanted to do is expose any exceedingly sensitive Database information or run the risk of being held accountable, it’s generally good practice to stop when you have this much control. We then went to report it to Hackerone. The plot thickens…

# Reporting

Obviously, we had a lot of information in our hands. We could dump the Database information if we wanted, modify the Applications, send emails on behalf of the server(s), etc. It was apparent that our findings were Critical - we brought them to Hackerone.

The reporting process to Hackerone was similar to what is seen in this Writeup, however, this Bounty was like a psychological thriller, the dreaded words researchers never want to hear:

![](/uploads/11.png)

**“We don’t host ‘x’ on our name servers, looks to be owned by x."**

![](/uploads/joeys-delayed-reaction-27092020175612.jpg)

This was bad news bears for us, this opened up another possibility - a threat actor actively exploiting the company that we had reported to.

![](/uploads/10.png)

This appeared to be spam email marketing, but why would a legitimate company be sending out these emails? The answer was simple - **they didn’t know it was happening.**

  1. We then went back to the Email Marketing Application and logged in once again. After enumeration, we had uncovered that **13** separate companies DNS Nameservers were in this console - they weren’t owned by the Company we were testing on as previously expected.

  2. It wasn’t clear what exactly they were doing, we had to put all the pieces together but a final determination was made:

**Roughly 1.7+ Million Email addresses were in this Database  
Roughly 5+ Million Black Hat Marketing emails had been sent out  
13 separate Companies with DNS Nameservers Possibly Being Abused, and one Confirmed DNS Nameserver Abuse Case**

  3. The situation had now taken a complete shift. We had uncovered a malicious Marketing campaign running. While we have no idea how effectively this campaign was running or how many companies of the 13 were actively being exploited, we at least had confirmation that 1 was being exploited (the Company we were reporting to on Hackerone)

  4. Now what? We obviously had to have a conversation with the Company on Hackerone and let them know that their DNS Nameserver was misconfigured and that they were being used to send spam marketing emails to millions of people.

# Mail Marketing Vendor Pays Us

The program on HackerOne only rated their part in the misconfiguration a low ($50), while we respectfully disagree with their rationale, the Mail Marketing Company ended up paying us for our findings on Bugcrowd instead ($1500), and we appreciate their kindness and understanding to their client’s security.

It was nice to make an extra $1550 for helping out.

![](/uploads/123123.png)

![Creative Commons](https://mirrors.creativecommons.org/presskit/icons/cc.svg) ![CC-BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) 2020 John

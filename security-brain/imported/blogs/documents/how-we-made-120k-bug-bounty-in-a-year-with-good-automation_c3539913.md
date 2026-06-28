---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-06_how-we-made-120k-bug-bounty-in-a-year-with-good-automation.md
original_filename: 2023-02-06_how-we-made-120k-bug-bounty-in-a-year-with-good-automation.md
title: How we made $120k bug bounty in a year with good automation
category: documents
detected_topics:
- rate-limit
- automation-abuse
- xss
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- rate-limit
- automation-abuse
- xss
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: c35399134cb77e0f160fdd365eb5208c969c3627747fb8632f268e6b6b4b3b8f
text_sha256: 6c96813ece0e496dabbddc83a6d838ae9f77446445892dc158836380cc768b5c
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# How we made $120k bug bounty in a year with good automation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-06_how-we-made-120k-bug-bounty-in-a-year-with-good-automation.md
- Source Type: markdown
- Detected Topics: rate-limit, automation-abuse, xss, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `c35399134cb77e0f160fdd365eb5208c969c3627747fb8632f268e6b6b4b3b8f`
- Text SHA256: `6c96813ece0e496dabbddc83a6d838ae9f77446445892dc158836380cc768b5c`


## Content

---
title: "How we made $120k bug bounty in a year with good automation"
page_title: "How we made $120k bug bounty in a year with good automation - Vidoc Security Lab"
url: "https://www.vidocsecurity.com/blog/2022-summary-how-we-made-120k-bug-bounty-in-a-year/"
final_url: "https://blog.vidocsecurity.com/blog/2022-summary-how-we-made-120k-bug-bounty-in-a-year"
authors: ["Dawid Moczadło (@kannthu1)", "Klaudia Kloc"]
bugs: ["XSS", "Security misconfiguration", "Log4shell", "Debug mode enabled"]
bounty: "120,000"
publication_date: "2023-02-06"
added_date: "2023-02-07"
source: "pentester.land/writeups.json"
original_index: 1574
---

Beginning of the new year is always a good time to reflect and summarize achievements in the previous one. 2022 was very busy for several reasons, today we want to present to you what we did and learned doing large-scale bug bounty hunting.

💡 VIDOC - The Future of Cybersecurity

Our research has evolved. Explore what’s new at Vidoc →

[vidocsecurity.com](https://www.vidocsecurity.com/)

### Our setup

In the beginning we tried to use some open-source tools such as Amass, Subfinder, nuclei engine. They were overall hard to work with, not optimized for large-scale hacking, slow and inaccurate. Unexpected output and bugs made the whole process painful. Using these tools on distributed infrastructure (which was necessary to avoid rate limiting and WAFs), with queues and task managers required so many code modifications, we decided it is not worth it. We wrote a whole request engine from scratch.

The tool we use was built by us, it consists of a reconnaissance part and custom request engine that allows us testing vulnerabilities by modules (nuclei-like templates) across all targets.

Recon part was running 24/7, we were **monitoring 1400 domains** and whenever a new host appeared on given subdomain it was added to target lists and scanned against vulnerability modules defined by nuclei-like templates.

We were **scanning 2,5 mln hosts daily.** We found thousands of vulnerabilities, and reported over 140 of them.

## Strategy

In the beginning we were scanning for many vulnerabilities to test what works. We got a lot of false positives - it was very time consuming to check them all. To reduce the amount of work we decided to focus on quality instead of quantity. We chose a few vulnerabilities that we tuned to reduce false positives rates and started scanning for them 24/7.

### Some tech details - skip if you are not interested - what we scanned for

All vulnerabilities we scanned for are defined in modules.

CVEs and known vulnerabilities:

  * Log4Shell (module will be added to the library soon)
  * [Confluence 0day CVE-2022-26134](https://app.vidocsecurity.com/public-library/23fb4170-e47f-4311-9f0e-67b4d076fdd4?ref=blog.vidocsecurity.com)
  * [Swagger UI XSS](https://app.vidocsecurity.com/public-library/787db825-d8c0-4182-a79f-6c7520745c49?ref=blog.vidocsecurity.com) (details in this [article](https://blog.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers/))

Common misconfigurations:

  * Debug mode in popular frameworks - [Django](https://app.vidocsecurity.com/public-library/b8bdebd9-898c-443a-b835-54a3d3905e6b?ref=blog.vidocsecurity.com), [Symfony](https://app.vidocsecurity.com/public-library/631278b2-902c-480c-999a-eeb9bf201680?ref=blog.vidocsecurity.com)
  * [Nginx](https://app.vidocsecurity.com/public-library/57f5f870-eb8d-469a-af42-6676fd0ec9d1?ref=blog.vidocsecurity.com) and [Apache](https://app.vidocsecurity.com/public-library/7b9cecc5-472f-43f0-bc0b-e256bdecd2ab?ref=blog.vidocsecurity.com) misconfigurations
  * [Directory listing](https://app.vidocsecurity.com/public-library/7831677d-424c-4b3c-be6d-df89dd8f29c5?ref=blog.vidocsecurity.com)
  * [Bucket takeover/subdomain takeover](https://app.vidocsecurity.com/public-library/d2b4ba92-21fb-449d-b2b9-03817ede41af?ref=blog.vidocsecurity.com)
  * [Exposed Prometheus panel](https://app.vidocsecurity.com/public-library/33c1539f-f742-4ce4-94a2-5a1205b2cf6d?ref=blog.vidocsecurity.com)
  * [Elasticsearch instance](https://app.vidocsecurity.com/public-library/190af348-bb30-4592-9d0d-3a41407dc420?ref=blog.vidocsecurity.com)
  * [Leaked credentials in appsettings.json](https://app.vidocsecurity.com/public-library/4061e117-3a34-40e2-a779-062a4d35f855?ref=blog.vidocsecurity.com)
  * [Exposed .git folder](https://app.vidocsecurity.com/public-library/d377c5be-00f7-4e3a-bf91-9ff30d95f54b?ref=blog.vidocsecurity.com) (we could clone git repo) or svn (we could clone svn repository)
  * [Springboot heap dump](https://app.vidocsecurity.com/public-library/6864ca08-2507-4d4d-a810-666243af7580?ref=blog.vidocsecurity.com)

We researched these vulnerabilities and explored ways of identifying them, so after tuning we ended up with 27 modules - one vulnerability each.

## Our Top 3

Here we share some statistics. We won’t go deep into technical details of each report or vulnerability - some of them are still not disclosed.

We researched these vulnerabilities and explored ways of identifying them, so after tuning we ended up with 27 modules - one vulnerability each:

### Top 3 most common vulnerabilities detected

  * XSS in Swagger UI (one of original once, we covered it in details in our article: [Hacking Swagger-UI - from XSS to account takeovers](https://blog.vidocsecurity.com/blog/hacking-swagger-ui-from-xss-to-account-takeovers/))
  * Nginx misconfiguration
  * Log4Shell (remember Log4Shell?)

💡

****Fun Fact**** Our biggest source of Swagger UI XSS vulnerability was… Microsoft. We found over 100 hosts with this vulnerability across their infrastructure. We reported several of them, after some time we noticed that Microsoft added a new entry to their bug bounty policy - Swagger UI related bugs were out of scope from now on. Nice one, Microsoft.

Not all vulnerabilities detected were reported by us for several reasons. Some of them were verified a few hours after detection and hosts were already not available - hence we couldn’t provide PoC. Some of them had really low potential of being paid for (what we learned it the hard way) so we didn’t even bother writing a report. Some of them were out of scope. Some of them were false positives. Here is our top reported category:

### Top 3 reported vulnerabilities

  * XSS in Swagger UI (37 reports)
  * Debug mode (13 reports)
  * Log4Shell (8 reports)

Mass reporting of one type of vulnerability drew us to an interesting conclusion - there seems to be no correlation between how easy it is to exploit vulnerability/time spent on a given PoC and amount of bounty. For exactly the same vulnerability we got paid $100 from one company and $10 000 from the other. That being said we have some interesting data about top 3 most profitable vulnerabilities:

### Top 3 best earning vulnerabilities

  * Log4Shell
  * XSS on SwaggerUI
  * Common misconfigurations

The more reports the more money you get for given type of vulnerability, however it’s some of the one-time payouts that surprised us the most:

### Top 3 vulnerabilities with biggest one-time payout

  * Exposed Springboot Heapdump $10 000 (not disclosed)
  * Swagger UI Shopify $9 400 - [link to report](https://hackerone.com/reports/1444682?ref=blog.vidocsecurity.com)
  * Log4Shell $6 000 (not disclosed)

![](/_next/image?url=%2Fimages%2Fblog%2F2022-summary-how-we-made-120k-bug-bounty-in-a-year%2Finline%2F01-image-1.png&w=3840&q=75)

Not all reports resulted in payouts. Thanks to our continuous scanning we made sure we report given vulnerability as soon as the host was available on the internet, however, sometimes other researchers were faster (or companies decided that “root cause” was already reported by others). Here is our top duplicates list:

### Top 3 duplicated vulnerabilities

  * Swagger UI
  * Debug mode
  * Subdomain takeover

Not every company will pay you the same amount of money for the same bug with similar impact. One of the things we learned along the way was that some programs are more profitable than others not because they promise higher amounts of money for critical bugs but because they pay researchers without wasting their time and are more generous in evaluating the value of the bug.

And finally our personal, subjective and totally biassed Top 1 situations in last year bug bounty adventure:

**Most exciting report(s) Log4j.** It happened at the end of 2021 but the majority of the reports were submitted by us in January 2022, hence we added it to this summary. It was exciting because of the scale of it, literally EVERYBODY was talking about log4Shell. Exploit was relatively easy to apply and we found a lot of critical and high bugs. It made you feel like you are part of history.

**Most ridiculous situation** And again Log4Shell. We reported this vulnerability to one of the top 5 tech companies, few hours later we got a response that… **This vulnerability is too new, below 30days 0day, hence it won’t be paid for.** They closed the report. We were shocked, it was one of the more serious cases - we could read environment variables from a server, that included credentials to databases etc. They reopened the report 3 days later saying they are sorry and it was a mistake, and after consideration they are going to pay us $3 500. Better late than never!

## Conclusions

We decided to divide conclusions into 3 sections: what we learned, what we did right and what we did wrong.

### What we learned

**Conclusion 1: Consistency is a key -** companies make the same mistakes all over again. We noticed very early that if we find a given type of bug on one endpoint that belongs to some company there is a huge probability you will find the same bug on different parts of their infrastructure.

**Conclusion 2: Collaboration for the win -** it is always better to work with someone than alone. We all have strong and weak sides, different set of skills, experience and competence. When you cooperate with someone it’s usually easier to work on more advanced exploits. And of course the more people the faster bugs will be reported meaning less chance it will be a duplicate.

**Conclusion 3: Quality of the report matters** \- you need to learn how to anticipate the value of your bug and make it as easy as possible for the company to validate. The easier it is to confirm the bug and the better you describe the impact - the bigger bounty. For the same type of vulnerability we tested several templates and chose the best one that worked for most reports. Today we use AI to generate templates for us.

### What we did right:

  1. **Engine optimization from day 1 -** it really paid out it terms of both speed of research and amount of money for infrastructure
  2. **Focusing on quality of vulnerability rather than amount of modules used for scanning**
  3. **Keep everything in one place -** when we were building our tools we wanted to make sure we have bug backlog, module definitions, comments and recon reports available for every team member whenever they need. It was a huge advantage for everybody to be able to track progress, it made collaboration so much easier.

When we worked in AppSec team we were frequently working together on penetration tests and security assessments of soon-to-be-released web applications. The biggest issue was how to share our research in efficient and secure way. Vidoc Research solves that problem. "Share with team members" feature will be avialble soon.

### What was challenging:

  1. **In the beginning we tried to report all the vulnerabilities, and didn’t focus on the most valuable ones/with biggest potential to actually get payout.** We were spending a lot of time writing reports instead of searching for bugs in companies with good reputation
  2. Request engine initially in JS - had to rewrite.
  3. Some of the technologies and supporting services we used in the backend were not the best choice, using open source projects in nice unless it is supported by only one guy who decides not to continue it after few months

During the process we developed a tool for researchers we needed to make our research easier. We made over $120k in many bug bounty programs and decided to share the tool - VIDOC - with people.

Vidoc Security Lab was founded by two hackers - Dawid and Klaudia, and for a year we worked with several other researchers (thank you Ori!).

2022 looked good, can’t wait for 2023! We are already working on a series of tutorials and a new research article for you about Log4Shell. If you want to be up to date with our research feel free to sign up to our newsletter and follow us on Twitter.

💡 VIDOC - The Future of Cybersecurity

Our research has evolved. Explore what’s new at Vidoc →

[vidocsecurity.com](https://www.vidocsecurity.com/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-09_how-i-used-a-simple-google-query-to-mine-passwords-from-dozens-of-public-trello-.md
original_filename: 2018-05-09_how-i-used-a-simple-google-query-to-mine-passwords-from-dozens-of-public-trello-.md
title: How I used a simple Google query to mine passwords from dozens of public Trello
  boards
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
language: en
raw_sha256: 1049009969c5d9e325f9eae16b1c35f48701bfea0ff1c6dba7a8a920285b5434
text_sha256: 0bfffb0a4222809fe214fcd5a62192cef123e69a1ebf2a9481ff34accf1d97e2
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I used a simple Google query to mine passwords from dozens of public Trello boards

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-09_how-i-used-a-simple-google-query-to-mine-passwords-from-dozens-of-public-trello-.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1049009969c5d9e325f9eae16b1c35f48701bfea0ff1c6dba7a8a920285b5434`
- Text SHA256: `0bfffb0a4222809fe214fcd5a62192cef123e69a1ebf2a9481ff34accf1d97e2`


## Content

---
title: "How I used a simple Google query to mine passwords from dozens of public Trello boards"
url: "https://medium.freecodecamp.org/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724"
final_url: "https://www.freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724"
authors: ["Kushagra Pathak (@xKushagra)"]
programs: ["Trello"]
bugs: ["Broken authorization", "Information disclosure"]
publication_date: "2018-05-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5884
---

May 9, 2018  / [ #cybersecurity ](/news/tag/cybersecurity/)

# How I used a simple Google query to mine passwords from dozens of public Trello boards

![How I used a simple Google query to mine passwords from dozens of public Trello boards](https://cdn-media-1.freecodecamp.org/images/1*6PO4cITaemxEBISjKuRimg.png)

By Kushagra Pathak

A few days ago on 25th April, while researching, I found that a lot of individuals and companies are putting their sensitive information on their public Trello boards. Information like **unfixed bugs and security vulnerabilities** , **the credentials of their social media accounts** , **email accounts** , **server** and **admin dashboards** — you name it, is available on their public Trello Boards which are being indexed by all the search engines and anyone can easily find them.

### How did I discover this?

I searched for [Jira](https://www.atlassian.com/software/jira) instances of companies running [Bug Bounty Programs](https://en.wikipedia.org/wiki/Bug_bounty_program) with the following search query:
  
  
  inurl:jira AND intitle:login AND inurl:[company_name]
  

> _Note: I used a Google dork query, sometimes referred to as a dork. It is a search string that uses advanced[search operators](https://whatis.techtarget.com/definition/search-operator) to find information that is not readily available on a website. — [WhatIs.com](https://whatis.techtarget.com/definition/Google-dork-query)_

I entered `Trello` in place of `[company name]`. Google presented a few results on Trello Boards. Their visibility was set to Public, and they displayed login details to some Jira instances. It was around 8:19 AM, UTC.

**I was so shocked and amazed ?**

So why was this a problem? Well, [Trello](https://trello.com/tour) is an online tool for managing projects and personal tasks. And it has Boards which are used to manage those projects and tasks. The user can set the visibility of their boards to Private or Public.

After finding this flaw, I thought — why not check for other security issues like email account credentials?

I went on to modify my search query to focus on Trello Boards containing the passwords for Gmail accounts.
  
  
  inurl:https://trello.com AND intext:@gmail.com AND intext:password
  

![Image](https://cdn-media-1.freecodecamp.org/images/ZTQwW7EGpyypN0rJ09BMXUnzOEoLNx7vATRi)

And what about SSH and FTP?
  
  
  inurl:https://trello.com AND intext:ftp AND intext:password
  
  
  
  inurl:https://trello.com AND intext:ssh AND intext:password
  

![Image](https://cdn-media-1.freecodecamp.org/images/5sbSgGKEZQ4dCjahS1A20HGRvjJ0NJozV942)

### ? What else I found

After spending a few hours using this technique, I uncovered more amazing discoveries. All while I kept on changing my search query.

Some companies use `Public` Trello boards to manage bugs and security vulnerabilities found in their applications and websites.

![Image](https://cdn-media-1.freecodecamp.org/images/rcT--o5vH-ohrAqIOxSzzbLRAWcvfZOYONUP)

People also use Public Trello boards as a **fancy** public password manager for their organization’s credentials.

Some examples included the server, [CMS](https://en.wikipedia.org/wiki/Content_management_system), [CRM](https://en.wikipedia.org/wiki/Customer_relationship_management), business emails, social media accounts, website analytics, Stripe, AdWords accounts, and much more.

![Image](https://cdn-media-1.freecodecamp.org/images/jqPEJQruX8MPqIZor6NIR3wxoH9lhpgfAH84) _Examples of public Trello boards which contain sensitive credentials_

Here’s another example:

![Image](https://cdn-media-1.freecodecamp.org/images/M0IhGrqZYJgqwUZsLeZpyUummXbonwDEzD6l) _An NGO sharing login details to their Donor Management Software (database) which contained a lot of PII ([personally identifiable information](https://en.wikipedia.org/wiki/Personally_identifiable_information" rel="noopener" target="_blank" title=")), and details like donor and financial records_

Until then I was not focusing on any specific company or Bug Bounty Programs.

But nine hours after I discovered this thing, I had found the contact details of almost **25 companies** that were leaking some very sensitive information. So I reported them. Finding contact details for some of them was a tedious and challenging task.

I posted about this in a private Slack of bug bounty hunters and a infosec Discord server. I also [tweeted about this](https://twitter.com/xKushagra/status/989074112411824129) right after discovering this Trello technique. The people there were as amazed and astonished as I was.

Then people started telling me that they were finding cool things like business emails, Jira credentials, and sensitive internal information of Bug Bounty Programs through the Trello technique I shared.

![Image](https://cdn-media-1.freecodecamp.org/images/23G9wAjLnJmsDCY5tN8ZQhSncOwYbcbsRM9r)

Almost 10 hours after discovering this Trello technique, I started testing companies running Bug Bounty Programs specifically. I then began with checking a well-known ridesharing company using the search query.
  
  
  inurl:https://trello.com AND intext:[company_name]
  

I instantly found a Trello board that contained login details of an emplyee’s business email account, and another that contained some internal information.

To verify this, I contacted someone from their Security Team. They said they had received a report about the Board containing email credentials of an employee right before mine and about the other board containing some internal information. The security team asked me to submit a complete report to them because this is a new finding.

Unfortunately, my report got closed as a `Duplicate`. The ridesharing company later found out that they had already had received a report about the Trello board I found.

In the coming days, **I reported issues to 15 more companies** about their Trello boards that were leaking highly sensitive information about their organizations. Some were big companies, but many don’t run a Bug Bounty Program.

One of the 15 companies was running a Bug Bounty Program, however, so I reported to them through it. Unfortunately, they didn’t reward me because it was an issue for which they currently don’t pay. ?

#### Update — 18 May 2018:

And just the other day, I found a bunch of **public Trello Boards** containing really sensitive information (including login details!) **of a government**. Amazing!

[The Next Web](https://thenextweb.com/security/2018/05/10/psa-saving-passwords-in-public-trello-boards-is-a-really-really-bad-idea/) and [Security Affairs](https://securityaffairs.co/wordpress/72380/data-breach/trello-data-leak.html) has also reported about this.

#### Update —17 August 2018:

In the recent months I had discovered a total of **50 Trello Boards of the British and Canadian governments** containing internal confidential information and credentials. [The Intercept](https://www.freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724/undefined) wrote a detailed article about it [here](https://theintercept.com/2018/08/16/trello-board-uk-canada/).

[**British and Canadian Governments Accidentally Exposed Passwords and Security Plans to the Entire…**](https://theintercept.com/2018/08/16/trello-board-uk-canada/)  
[_By misconfiguring pages on Trello, a popular project management website, the governments of the United Kingdom and…_theintercept.com](https://theintercept.com/2018/08/16/trello-board-uk-canada/)

#### Update —24 September 2018:

In August, **I found 60 public Trello boards** , a public Jira and bunch of Google Docs of **United Nations** which were containing credentials to multiple FTP servers, social media & email account, lots of internal communication and documents. [The Intercept](https://www.freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724/undefined) wrote a detailed article about it [here](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords).

[**United Nations Accidentally Exposed Passwords and Sensitive Information to the Whole Internet**](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords)  
[_The United Nations accidentally published passwords, internal documents, and technical details about websites when it…_theintercept.com](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords)

Thanks for reading my story.

If you liked this article, give me some claps ?

And you can [follow me on Twitter](https://twitter.com/xKushagra/) ✌️

[**Kushagra Pathak (@xKushagra) | Twitter**](https://twitter.com/xKushagra)  
[_The latest Tweets from Kushagra Pathak (@xKushagra). Security researcher ?‍? | Looking for a job. ?twi_tter.com](https://twitter.com/xKushagra)

_I’d like to thank_ [CyberSecStu](https://twitter.com/cybersecstu/) _,_ [Toffee](https://twitter.com/PolarToffee) _and the_ freeCodeCamp editorial team _for helping me proofread and edit this article._

* * *

If you read this far, thank the author to show them you care. Say Thanks

Learn to code for free. freeCodeCamp's open source curriculum has helped more than 40,000 people get jobs as developers. [Get started](https://www.freecodecamp.org/learn)

ADVERTISEMENT

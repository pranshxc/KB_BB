---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-02_hundreds-of-internal-servicedesks-exposed-due-to-covid-19.md
original_filename: 2020-04-02_hundreds-of-internal-servicedesks-exposed-due-to-covid-19.md
title: Hundreds of internal servicedesks exposed due to COVID-19
category: documents
detected_topics:
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- command-injection
- mfa
- api-security
language: en
raw_sha256: 2cf4a9ced4f3ac6c95611fdd538653223c248482db536ef5d26d37e6b8dc4c61
text_sha256: 070e37c231803b1c33cccb2b334822f0d0232def00b52e17b9dc394841400b32
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Hundreds of internal servicedesks exposed due to COVID-19

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-02_hundreds-of-internal-servicedesks-exposed-due-to-covid-19.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2cf4a9ced4f3ac6c95611fdd538653223c248482db536ef5d26d37e6b8dc4c61`
- Text SHA256: `070e37c231803b1c33cccb2b334822f0d0232def00b52e17b9dc394841400b32`


## Content

---
title: "Hundreds of internal servicedesks exposed due to COVID-19"
url: "https://medium.com/@intideceukelaire/hundreds-of-internal-servicedesks-exposed-due-to-covid-19-ecd0baec87bd"
authors: ["Inti De Ceukelaire (@securinti)"]
bugs: ["Security misconfiguration"]
bounty: "10,000"
publication_date: "2020-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4671
scraped_via: "browseros"
---

# Hundreds of internal servicedesks exposed due to COVID-19

Hundreds of internal servicedesks exposed due to COVID-19
Inti De Ceukelaire
Follow
8 min read
·
Apr 2, 2020

452

2

Press enter or click to view image in full size

Inti De Ceukelaire currently works as the Head of Hackers at ethical hacking platform intigriti. In his spare time, Inti identifies and reports security problems to affected companies.

In the light of the COVID-19 crisis, millions of organisations across the globe had to quickly relocate their daily operations from an office to employee’s residences. As expected, this turned out to be a challenging task, even for companies already familiar with remote working solutions. Numerous cybersecurity professionals raised concerns about the potential security consequences the sudden migration from office to household can cause, but very few were able to provide tangible data of the effects of COVID-19 on the global state of cybersecurity.

Internal ticketing tools like JIRA and Asana enable organisations to get work done in a structured way. Most corporations require its employees to create tickets to request, change or get help with something that is out of their control. Whether it is ordering a new ID badge, requesting access to a tool, getting expenses reimbursed or troubleshooting login problems, the solution is often a ticket away in a remote work environment. And so are hacking attempts — if your internal helpdesk is publicly exposed.

An increasing number of Atlassian JIRA Servicedesks have been misconfigured to be accessible for anyone to sign up. In essence, this is nothing to worry about as servicedesks may have legitimate reasons to be public. However, a growing number of instances have been repurposed to serve as an internal service ticket portal, allowing attackers to impersonate employees and create legitimate internal requests. Verifying the legitimacy of these requests has proven to be far less convenient without offline verification channels: you can’t just walk up to your colleague and ask them about it.

The issue

A substantial amount of internal service desks are being exposed to the outside world for anyone to access. In order to join a misconfigured service desk, all an attacker needs to do is navigate to the service desk login page of an Atlassian instance — often just the name of the company.

For the sake of a proof of concept, I have created a service desk at https://yourcompanyname.atlassian.net. The instance itself will load the default Atlassian login page, which is properly protected against external intruders:

Press enter or click to view image in full size

Unknowing administrators might think they’re protected, whereas their service desk is in fact, still open to the public. The only thing an attacker needs to do is to navigate to this URL instead:

https://yourcompanyname.atlassian.net/servicedesk/customer/user/login

This link provides access to a second login portal, that allows everyone to sign up in this configuration (click on sign up) and access the support portals:

Press enter or click to view image in full size
Press enter or click to view image in full size
Our demo environment is obviously empty — so let’s look at some real examples!

Projects can be set up for various purposes, such as IT, HR, Facilities, Finance & Legal, but this does not seem to affect the public registration settings.

Press enter or click to view image in full size
Exploitation in the wild

I was curious just how many companies had their internal servicedesks publicly available and decided to automate this process: I took a list of 10.000 popular domain names globally and found out that no less than 288 of 1.972 (roughly 15%) corresponding Atlassian instances were open to the public. This was an increase of 12% compared to tests conducted before the COVID-19 crisis — my earliest scans date back from last summer. This was only a rough estimate: my automated workflow would just extract the domain name and check whether sign ups are enabled for this namespace. It wouldn’t check whether the company name is different from the domain name, or if the service desk actually belongs to the company that shares the same name.

So I went ahead and signed up for some of these service desks. They were public, after all. Pretty soon I discovered that these service desks should never have been exposed, looking at their titles only. The screenshots below are real, but slightly modified in order to remove references to affected companies (with permission).

Press enter or click to view image in full size
Just one of the hundreds of ‘internal’ service portals exposed to the internet

The example above is very similar to the numerous instances I tested. The support portals cover various topics, such as HR, internal IT troubleshooting, Developer Operations, Office Helpdesks, Data & Privacy Requests, Information Security, UX, Marketing, Data Science, …

Get Inti De Ceukelaire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

All of these portals would contain various sub-topics with common requests internal employees can create:

Press enter or click to view image in full size
Press enter or click to view image in full size

I won’t flood this blog with screenshots of company’s internal service portals, but here’s a selection of things I’ve seen:

Getting new access badges to the physical office delivered
Onboarding new employees
Requesting salary changes
Requesting information about employees
Requesting information about customers
Requesting changes to online assets or webpages
Requesting access to social media channels
Requesting access to internal tools
Requesting internal security assessment reports
Unblocking users
Resetting multi-factor authentication
Declaring expenses
Initiating a GDPR request for a customer
VPN whitelisting
Requesting execution of queries on the database
Requesting code to be executed on the company’s web server
…

Misconfigured servicedesks leaking tons of PII

About one third of the servicedesks I joined allowed me to assign tickets to other users. In certain configurations, where users are created for any inbound support e-mail (with their display name automatically set to their e-mail address), this would leak the e-mail addresses of every user that has interacted with the external support channels as well.

Press enter or click to view image in full size
Some misconfigured service desks would leak (customer) e-mail addresses through the ‘assign’ functionality
Press enter or click to view image in full size
A servicedesk accidentally leaking personal e-mail addresses of its customers
The aftermath: from being ignored to $10,000

Since the only thing I had to do was check whether a signup page existed or not, I could easily test this for hundreds of companies without the risk of getting into legal trouble: the service desks were public, after all. Once I had identified possible victims, the disclosure process was painful to say the least: more than 85% of all vulnerable companies did not have a way for me to responsibly disclose a vulnerability to them. Of course, I could create an internal ticket myself in this case, but I’m not sure how that would have been perceived from a legal perspective. In some cases, I went through the hustle of contacting the external customer service, but about half of all reach-outs did not get escalated.

Over the past few weeks, I have worked with around 25 companies to properly secure their service desk. At least one had noticed other rogue accounts except for mine, so it seems like more hackers are aware of this configuration flaw as well.

The impact assessments greatly varied from accepted risk to critical. Some companies decided to award a monetary reward, ranging from €50 to $10,000 (In the latter case, I would have been able to run malicious code through submitting a code execution request their service desk).

Whether you offer rewards for security bugs or not, every company should have a policy and contact for individuals to report security vulnerabilities to them. Thousands of internal service desks are most likely still exposed, simply because I had no escalate this to the right people, as an outsider.

There is no excuse not to have a vulnerability disclosure process in 2020. They come at all forms and sizes — from implementing something as simple as security.txt to running a bug bounty program at intigriti.com: the choices are endless.

FAQ
Is this a vulnerability in Atlassian products?
No. This is a common misconfiguration made by the individual companies. In some cases, the service desk was supposed to be public, but later reorganised to serve internal purposes.
How many companies are affected?
Hard to tell because I simply could not test all of them, but from my list of 10.000 popular domain names, 1.972 correlated to an Atlassian instance, of which 15% (288) had a service desk with public sign ups enabled. It’s hard to tell how many of these are intended to be public or not. I manually joined a few an have made about 25 responsible disclosures so far, with bug bounties ranging from €50 to $10.000.
How can I prevent this from happening at my organisation?
Atlassian provides some excellent documentation that explains how to choose the right settings from your intended purposes.
Can external attackers get access to existing tickets?
I haven’t encountered any case in which newly created accounts have access to others’ tickets.
How is this different from social engineering an external support agent?
The impact of this misconfiguration is highly contextual. Successful exploitation mainly depends on the expectation patterns of the support agent. In a customer-facing setting, there are more reasons to be suspicious about unexpected requests than in an internal company tool. For bigger organisations, the risk of malicious ticket handling seems more likely, as there are simply more possible ticket creators and teams involved. We’d expect these companies to have strict procedures and checks to make sure requests are authorised, but tests have pointed out that the reality is different. The vigilance agents have for external threats fade away in a presumably authorised environment.
I have found a public sign up for a service desk. Is this a vulnerability?
Only if the company uses the service desk for internal purposes. The best way to know is to either join the service desk and look at the content, or ask the company through other means.
Is the increase of misconfigured instances related to COVID-19?
It’s hard to tell for sure. What I’ve seen is that there’s been at least a 12% increase of vulnerable internal service desks since my previous scans this summer. What I do know for sure is some of these have been restructured to fit internal needs only, but forgot to change the registration settings.
Is this actually being exploited in the wild?
There has been at least one case in which a company identified a rogue account except for mine, but I don’t have insights in whether it was used for malicious purposes.
Our company would like to get a hacker policy, so people that stumble upon bugs like this can easily let us know
That’s great to hear! They come at all forms and sizes — from implementing something as simple as security.txt to running a bug bounty program at intigriti.com. If you have any questions or need help, feel free to contact me!

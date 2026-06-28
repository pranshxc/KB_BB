---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-10_how-i-hacked-hundreds-of-companies-through-their-helpdesk.md
original_filename: 2017-09-10_how-i-hacked-hundreds-of-companies-through-their-helpdesk.md
title: How I hacked hundreds of companies through their helpdesk
category: documents
detected_topics:
- sso
- password-reset
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- sso
- password-reset
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: c8b065b32170f052641e968f036e9adbc00dc01c6f7d9b5672b00d7d34307886
text_sha256: 8be592d97beb9ac52b65d904575ce11210ace76b0b2efdc44a669d0cdb0d7fa3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked hundreds of companies through their helpdesk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-10_how-i-hacked-hundreds-of-companies-through-their-helpdesk.md
- Source Type: markdown
- Detected Topics: sso, password-reset, command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `c8b065b32170f052641e968f036e9adbc00dc01c6f7d9b5672b00d7d34307886`
- Text SHA256: `8be592d97beb9ac52b65d904575ce11210ace76b0b2efdc44a669d0cdb0d7fa3`


## Content

---
title: "How I hacked hundreds of companies through their helpdesk"
url: "https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c"
authors: ["Inti De Ceukelaire (@securinti)"]
programs: ["GitLab", "Slack", "Yammer", "Kayako", "Zendesk"]
bugs: ["Ticket Trick", "Logic flaw"]
bounty: "5,000"
publication_date: "2017-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6105
scraped_via: "browseros"
---

# How I hacked hundreds of companies through their helpdesk

Top highlight

1

1

1

How I hacked hundreds of companies through their helpdesk
Inti De Ceukelaire
Follow
10 min read
·
Sep 10, 2017

34K

43

UPDATE: The Next Web wrote a story about my findings: https://thenextweb.com/security/2017/09/21/ticket-trick-see-hackers-gain-unauthorized-access-slack-teams-exploiting-issue-trackers/

Introduction

Months ago I discovered a flaw hackers can use to access a company’s internal communications. The flaw only takes a couple of clicks to potentially access intranets, social media accounts such as Twitter, and most commonly Yammer and Slack teams.

The bug is still out there. It isn’t something that can be fixed right away. Over the past few months, I contacted dozens of companies and affected vendors as part of their bug bounty programs in order to get their setup fixed. Due to the number of affected companies it was not possible to contact everyone. On the recommendation of some of my hacker heroes, and with approval of the affected vendors, I’m publishing this blog so everyone affected can act immediately. Introducing what I’ve been calling Ticket Trick:

Press enter or click to view image in full size
I gave my finding a name and a logo. Deal with it.
THE DOOR — sign up with your @company email

Popular business communication tools such as Slack, Yammer and Facebook Workplace require employees to sign up with their @company e-mail address. Once an employee clicks on the verification link sent to their internal email address, they can join the company’s instance and access internal communication.

Press enter or click to view image in full size
Slack: Users with the same @company mail can join the team by default, this can be replaced by SSO or set to invite-only.
Press enter or click to view image in full size
Yammer: everyone with an @company mail can join.
Press enter or click to view image in full size
Facebook Workplace: everyone with an @company mail can join.
THE KEYS — The helpdesk or create-by-email feature

METHOD #1 — THE ISSUE TRACKER

It started when I discovered a way to bypass this authentication with GitLab. Anyone with a valid @gitlab.com e-mail address could join their team.

Press enter or click to view image in full size

At the same time, GitLab offers a feature to create issues by e-mail by sending them… to a unique @gitlab.com e-mail address. See *where this is headed?

Press enter or click to view image in full size
GitLab is one of many issue trackers that provide issue creation by e-mail

I tried to join their Slack team using this issue creating email address, just to see what would happen.

Press enter or click to view image in full size

I quickly refreshed my issue list and saw the verification e-mails added as an issue to my project:

Press enter or click to view image in full size

The freshly added issue contained the magic link needed to join their internal Slack team:

Press enter or click to view image in full size

I clicked the link to see if it’d actually work — and it did. I was greeted by the list of channels I was able to join and immediately removed my account and notified GitLab.

Press enter or click to view image in full size
A censored snapshot of the channel list

The GitLab team responded to my report on the same Sunday evening I reported it.

Press enter or click to view image in full size

They immediately set their slack to invite-only and took additional measures to inform their customers about the dangers of this functionality.

METHOD #2 — THE SUPPORT DESK

Only a handful of websites have public issue trackers so I decided to dig deeper to see whether a more common exploitation vector existed. As it turned out, it did, and is was far more common that I would’ve ever guessed: customer service.

E-mails sent to support@company.com sometimes turned up in an online support portal such as Zendesk, Kayako, (Fresh)Desk, WHMCS or a custom tool. So I decided to play with that and see whether a hacker could somehow extract the links from the database.

Most support portals can be integrated with single sign-on: an authenticated user will automatically be logged into the support desk to ensure a seamless experience. More than half of the websites I tested did not require e-mail verification, which means any one could sign up with any e-mail address and effectively read any support tickets created by that e-mail address. Online video sharing platform [censored*] was one of the many companies that did not require verification.

So I registered a [censored*] account the same email address Slack uses to send their magic verification links: feedback@slack.com.

Press enter or click to view image in full size

Using Slack’s handy find your workspace feature, I found [censored*] slack instance and signed up with the email address support@[censored*].com.

Press enter or click to view image in full size

Behind the scenes, feedback@slack.com now sends an e-mail to support@[censored*].com containing the verification link.

When support@[censored*].com receives the e-mail, it will be classified as a support ticket created by feedback@slack.com… which is the exact e-mail I signed up with.

Get Inti De Ceukelaire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I went to the help center to check my support tickets.

Press enter or click to view image in full size

I had one open support ticket… which contained the magic verification link I needed to join the [censored*] team.

Press enter or click to view image in full size

The [censored*] team immediately responded to this report and awarded a $2,000 bounty as part of their Bug Bounty program.

All websites that integrate a support portal without e-mail verification are vulnerable to this. And it gets even worse.

I found two additional flaws, in Kayako and Zendesk, that allowed me to bypass the e-mail verification process in their common setups. This allowed me to always execute the attack even when SSO was not enabled and e-mail verification was required. I reported these issues as part of their responsible disclosure program on June 1st and both have put a fix into place.

Next to that, websites that require users to verify their e-mail address upon registration, but not when changing it afterwards are vulnerable as well.

Increasing the impact

If a company does not use Slack and thinks it’s safe… it’s probably out of luck, given how widespread I found this issue to be. For example: Other business communication tools such as Yammer are also prone to this attack:

Press enter or click to view image in full size
I was able to join the Yammer intranet of an undisclosed company

And because we can read e-mails sent to support@, we can also see any password reset link sent to that e-mail address. As it turns out, quite a few companies use this exact e-mail address to sign up for third party services and social media like Twitter.

This means an attacker could also hijack any account linked to the support@ mail address:

Press enter or click to view image in full size
Press enter or click to view image in full size
I was able to hijack multiple Twitter accounts with over one million followers

In some cases, this e-mail address also had a privileged account on the website itself. By registering no-reply@company.com, you could intercept the password reset token for support@company.com and gain access to privileged accounts providing access to all customer information.

If none of the above worked, the attacker could still read and respond to past and future support tickets created by e-mail. A friend of mine once sent an e-mail to the support address of a company because something wasn’t working properly. Investigating this issue, I found that particular company to be vulnerable, so I signed up with his e-mail address, clicked on the “my support cases” tab and saw that particular e-mail appear. I could literally read and respond to every e-mail people sent to the customer service, as long as they didn’t have an account on the support desk. Users thinking they are talking to the customer service would instead be talking to a hacker.

Vendor and company responses

It was interesting to see how differently each company handled the disclosure.

Most affected companies handled my reports very professionally. Some companies even decided to issue a bug bounty as high as $8,000. I occasionally got a negative response and some chose to ignore my disclosure entirely.
Issue Tracker GitLab (#21823, disclosed) quickly took action by disabling trust for their own company domain and changing their Slack settings. They also updated their documentation to prevent their users from making the same mistake.
I disclosed this issue to Slack (#23923, pending disclosure) to check whether we could prevent this at a higher level. Even though they aren’t directly responsible for this issue, it affects a significant portion of their customers.
Slack took the risk seriously and changed their no-reply e-mail address to include a random token. This effectively prevents the attack in helpdesk software. The issue still persists for issue trackers and other e-mail integrations. Despite the fact that this is not a vulnerability in Slack itself, Slack decided to award a generous $1,500 bounty for my report.
Press enter or click to view image in full size
Slack added a randomized token to their no-reply email address to prevent abuse in helpdesks
I also tried to contact Yammer about this issue. Initially I got no response. Two weeks later I sent a follow-up e-mail which they replied telling me they forwarded it to the Yammer team along with the definition of a security vulnerability. To date, they haven’t taken any proactive measures to tackle this issue at a higher level like Slack did.
Press enter or click to view image in full size
Attackers are still able to join Yammer workspaces with using methods I discovered.
I contacted Kayako and Zendesk (#235139, disclosed) about the SSO bypass as part of their bug bounty program. Both resolved this issue and rewarded me respectively with a $1000 and a $750 bounty.
Lessons learned
Once inside, most company’s security is significantly weaker. Internal impact assessments showed employees pasted passwords, company secrets and customer information in channels everyone in the team had access to.
We need to keep looking for security issues in all possible places.
This vulnerability existed for years in hundreds of websites screened by security professionals, but as far as I know, nobody found it.
Large companies have no clue what their employees are doing. I discussed this flaw a CISO of a giant payment processing company. He assured me this wouldn’t be a problem, as their employees weren’t supposed to communicate through Slack. They had their own intranet set up to handle these things. I proved him wrong by joining 8 rogue Slack channels actively used by 332 employees all around the globe. I ended up getting a $5,000 bounty for it.
If you are wondering which Slack teams you are able to join using your company e-mail, you can use Slack’s find your team functionality.
FAQ
How do I know if my company is affected?
This vulnerability exists if support tickets can be created through e-mail and if support tickets are accessible by users with an unverified e-mail address. It also exists in public issue trackers or responders providing a unique @company.com e-mail address to submit information directly to a ticket, forum post, private message or user account.
As an affected company, how can we remediate this issue?
I’ve seen several approaches. Companies like AirBnb, LinkedIn and GitHub provide e-mail addresses with a different domain, like @reply.linkedin.com or @mail.github.com. They cannot be used to sign up for services like Yammer or Slack. GitLab updated their documentation with this advice to prevent this attack in issue trackers.
Some chose to disable the e-mail functionality, the service portal or the single sign on, while others implemented a proper e-mail verification.
It is also not advised to sign up for services such as Twitter, Slack or Zendesk with the official support@ e-mail address.
As an affected vendor of business communication software, how can we prevent this from happening?
You could implement extra security measures for people signing up with a customer service e-mail, but in many cases that would not be practical and or efficient. Facebook Workplace has a better approach as they send their e-mails from a randomly generated e-mail address like notification+ajivdw9kpwld@fbworkmail.com which is impossible for an attacker to guess. In response to my discovery, Slack also decided to implement these randomized e-mail addresses.
Why are you disclosing this information when hundreds of companies are still vulnerable?
Due to the number of affected companies, it is impossible to inform all of them, risking legal threats from companies that didn’t ask for security advice. I only contacted the small minority of affected companies and vendors with public responsible disclosure programs. Disclosing this now is a tough decision and could directly lead to security breaches, but history has revealed us hoarding bugs isn’t a good idea either.
Who are you?
I’m Inti and I live in Oilsjt, Belgium. As a kid, I was extremely skilled at breaking stuff. I’m 22 now and work as a creative coder for Studio Brussel, Belgium’s biggest radio station. At night I still break stuff as an ethical hacker with thanks from Google, Facebook, Microsoft, Yahoo and so on.
Any other projects?
I hijacked a Trump tweet, made StalkScan.com that highlights the creepy side of the Facebook graph search and like to blog about my bug bounty findings on medium.

FOLLOW ME ON TWITTER FOR MORE: https://twitter.com/securinti

I’d like to thank the amazing Pete Yaworski for proofreading and fixing my English. Also a shout out to Arne, Preben and Jerome from #teambelgium as a thank you for keeping their mouths shut. Thanks to Slack, Gitlab, [censored*] and Zendesk for their cooperation and approval of my blogpost.

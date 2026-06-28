---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-20_ggvulnz-how-i-hacked-hundreds-of-companies-through-google-groups.md
original_filename: 2020-01-20_ggvulnz-how-i-hacked-hundreds-of-companies-through-google-groups.md
title: GGvulnz — How I hacked hundreds of companies through Google Groups
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- password-reset
- api-security
- command-injection
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- password-reset
- api-security
- command-injection
language: en
raw_sha256: b8300fe9533c8b0aae38f1022b27aff01a3832a3d2870f1898eeb3b7f7d07163
text_sha256: d8ccbcddb45a431036b18bb7519f69713d68d17b8a7f20fc114ac6873d3c8539
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# GGvulnz — How I hacked hundreds of companies through Google Groups

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-20_ggvulnz-how-i-hacked-hundreds-of-companies-through-google-groups.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, password-reset, api-security, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b8300fe9533c8b0aae38f1022b27aff01a3832a3d2870f1898eeb3b7f7d07163`
- Text SHA256: `d8ccbcddb45a431036b18bb7519f69713d68d17b8a7f20fc114ac6873d3c8539`


## Content

---
title: "GGvulnz — How I hacked hundreds of companies through Google Groups"
url: "https://medium.com/@milanmagyar/ggvulnz-how-i-hacked-hundreds-of-companies-through-google-groups-b69c658c8924"
authors: ["Milan Magyar"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2020-01-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4824
scraped_via: "browseros"
---

# GGvulnz — How I hacked hundreds of companies through Google Groups

GGvulnz — How I hacked hundreds of companies through Google Groups
Milan Magyar
Follow
10 min read
·
Jan 21, 2020

471

5

Introduction

This logic flaw is the lovechild of two previous reports:

One: How I hacked hundreds of companies through their helpdesk — aka “Ticket Trick” by Inti De Ceukelaire

How I hacked hundreds of companies through their helpdesk
UPDATE: The Next Web wrote a story about my findings…

medium.comhttps://en.wikipedia.org/wiki/General_Data_Protection_Regulation

Two: Kenna Security’s research on the widespread Google Groups misconfiguration issue affecting thousands of instances, “Fortune 500 organizations; Hospitals; Universities and Colleges; Newspapers and Television stations; and even US government agencies”.

Widespread Google Groups Misconfiguration Exposes Sensitive Information | Kenna Security
Summary A widespread misconfiguration in Google Groups for organizations utilizing G Suite was recently investigated…

www.kennasecurity.com

I would suggest reading both as they are the building blocks of this one.

Press enter or click to view image in full size
Yes, a name and a logo. I had to.

I was looking at the emails inside a company’s Google Groups instance when I noticed some are related to various account registrations. My spidey sense told me to look up 
Inti De Ceukelaire
’s paper, something I faintly remembered reading over 2 years ago. After processing that report again, I realized it’s actually relevant to my scenario.

The Ticket Trick bug relied on the existence of issue trackers or helpdesk software that allow you to open tickets through email. An attacker had to sign up to the target’s main service with a special email address, exploiting the lack of address validation (or circumventing the one in place) and log into the target’s help desk service through SSO. In this case, all those components are simply replaced by the service of Google Groups mailing lists.

Here’s the sequence diagram of the bug:

Press enter or click to view image in full size
My finest work in GIMP so far
METHOD A)

The method above works when the mailing list has the “Anyone can view content.” and “Anyone can post.” permissions.
The first one is necessary for us to be able to see and open the email and the second is to let Slack (and other external services) post to the mailing list.

Press enter or click to view image in full size

In the screenshot below the green text under the mailing list indicates that you have at least view access to the topics/emails.

Press enter or click to view image in full size
Only @android.com email addresses can post, so these mailing lists are not vulnerable

How to exploit this logic flaw in a few easy steps:

Visit https://groups.google.com/a/$domain/forum/#!forumsearch/ and look for a public mailing list
Clicking the list will take you to: https://groups.google.com/a/$domain/forum/#!forum/$listname
Visit one of these pages in another tab and enter this email address: $listname@$domain
https://slack.com/signin/find
https://www.yammer.com/signup/
https://work.workplace.com/
https://twitter.com/account/begin_password_reset
https://www.facebook.com/login/identify/
https://www.instagram.com/accounts/password/reset/
…
Refresh the mailing list from Step 2) and open the email you got from the service in Step 3)
Click the confirmation link (or copy the account recovery code, other ~6 digit code from the email’s subject / body).
METHOD B)

There’s an other case when the Google Groups instance in misconfigured in a way that all mailing lists seem to be locked off properly at first glance, but search results disclose snippets of private emails’ around the search keywords.

In this example none of the mailing lists have the green “#XY topics last post: $DATE” indicator, so we shouldn’t be able to read emails sent to them.
The domain owner is probably confident that unathorized parties don’t have access to internal communication.

Press enter or click to view image in full size
No green text here

But searching for “password” for example, discloses sensitive emails:

Press enter or click to view image in full size
:(

Note that this is something that Google has known about since at least Kenna Security’s research back in 2018. Yet they decided that the privacy and security of their customers is not that important that anything should be done about it. Google Groups access controls are still as foggy as they were years ago.
GDPR’s wiki page says that “Controllers and processors of personal data must put in place appropriate technical and organizational measures to implement the data protection principles.” I think Google should at least alert its customers when those “appropriate technical measures” are not in place.

Compared to METHOD A), the steps to exploit are a bit different here:

You don’t know the name of the mailing list that is misconfigured to begin with, so you first search for something that has a high probability of being in an email’s subject or body, something like the letter ‘a’, “hi” or “hello”.
Hover your mouse over the group’s name in one of the search results to see the URL it points to:
https://groups.google.com/a/$domain/forum/#!forum/$listname corresponds to the $listname@$domain email address.
Send a test email or directly a signup / password reset email from Method A)’s Step 3) and hope that it appears in your search results, since you didn’t have a chance to confirm the “Anyone can post” permission because you don’t have access to the “About Group” page either.
Search for your test email to confirm that external senders are allowed or search for a string that’s part of the target service’s signup / password reset email.
Press enter or click to view image in full size
Signing up for Facebook with a public mailing list address is not a good idea

support@-, contactus@-, brand@-, media@company.com can easily be an (unwittingly misconfigured) public mailing list and also being used to sign up for Facebook, Twitter or Instagram since it’s convenient.

Press enter or click to view image in full size
Access Slack, Yammer, Facebook, Twitter and others. All from a single mailing list

Password reset flows are usually nice enough to include the code / token in the email’s subject or body so you don’t actually have to click a link.
Some registration emails also provide the option to “copy and paste this URL into your browser’s address bar” if you can’t click the link for some reason.

Get Milan Magyar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As an example, I was able to join an organization’s Yammer network purely through Google Groups search results.
They didn’t have “View Topics” set to “Anyone on the Internet” so I couldn’t open the signup email or even see the email in the list of topics/emails (there was no list), but the search feature was disclosing private emails, thus revealing the Yammer activation URL. Fortunately, the GET parameters are not necessary for the signup process so everything after the question mark can be discarded.

Press enter or click to view image in full size
Search for “into your browser:” and you get the activation URL that follows your search string
Press enter or click to view image in full size
Welcome to the company’s Yammer network

Keep in mind that virtually infinite new accounts can be created with the same email address (mailing list):
list@company.com and list+123@company.com are the same account on Google’s side, but treated as different in Slack and other services.

Tools
EdOverflow / googlegroups.sh

I’ve used this script to look for public Google Groups domains
I noticed curl was following unnecessary redirects, so I could make it run a lot faster by changing the URL.

Using Alexa top 1 million sites:
wget http://s3.amazonaws.com/alexa-static/top-1m.csv.zip
unzip top-1m.csv.zip
sed -i.bak ‘s/.*,//’ top-1m.csv
./googlegroups.sh top-1m.csv

I recommend removing domains that you know will be false positives to save some time. E.g. there are over 100 *.lpages.co sites:
grep ‘lpages.co$’ top-1m.csv | wc -l
101

vim top-1m.csv
:%! grep -v ‘lpages.co$’
ZZ

maaaaz / webscreenshot

I needed a tool to be able to quickly check for vulnerable mailing lists. Google Groups’ HTTP responses are obfuscated and hard to read so I opted for visual recon. Scrolling through screenshots lets you quickly see the “green text indicator”. I found webscreenshot to be reliable, but in many cases the Google Groups pages didn’t fully load before the screenshot was taken.
We increased the default timeout for the PhantomJS renderer and added an option to change it manually in v2.8.
I also helped in adding labels to the images in v2.7 so you can quickly see the URL that belongs to the screenshot.

EdOverflow / contact.sh

Companies with a bug bounty program usually already have a private domain in Google Groups or have their individual mailing lists configured properly. Organizations with less security awareness are at a higher risk and ironically they are also the ones without a dedicated security contact, which makes it hard to communicate the issue.

contact.sh was helpful in finding contact info for the affected domains.
I helped to fix a bug with the security@ email address lookup.

In some cases it took more time to find a contact info than it took to confirm the existence of the vulnerability.
Companies above a certain size should be legally required to adopt security.txt and utilize a dedicated security@ email address.

emtunc / SlackPirate

You might think that sending a signup or password reset email to a mailing list used by — in some cases — hundreds of people is pretty suspicious, and an admin would notice and deactivate the accounts.
This may be true, but an attacker can use tools like SlackPirate to quickly dump sensitive information (private keys, passwords, API keys, links to GCP and S3 buckets, link-only Google Docs, etc.) from the breached workspace using Slack’s API.
Once inside the company’s perimeter — Slack workspace in this case — these type of things are generally shared without much regard to security or authorization.

Timeline

Dec 13th — First report to a company with a VDP (vulnerability disclosure policy)
Dec 15th — I realize this is a widespread thing and report the issue to Google (1st report) and Slack
Dec 16th — I find one of Google’s major projects to be vulnerable as well and open a 2nd report as a PoC for the 1st one
Dec 17th — Google closes my 1st report as “Won’t fix (Intended Behaviour)”:
“The decision to prevent signups on Yammer or Slack via email confirmations coming from public Google Groups should be determine (sic) by those providers and not Google. I would recommend reaching out to both companies about this issue.”
Dec 17th — I comment on my 2nd Google report, emphasizing that this logic flaw completely bypasses Slack’s mandatory workspace 2FA as well. I could easily set it up for myself when joining the Google project’s workspace.
I also asked Slack to consider having mandatory review of new accounts for workspaces where mandatory 2FA is turned on.
Dec 18th — report to Microsoft (Yammer)
Dec 19th — Microsoft closes my report, claiming that it relied on social engineering. :)
Dec 20th — Slack closes my issue:
“While the behavior you described in your report is quite interesting, we feel that this is a case where improved user education rather than a technical fix of some type would be a more appropriate action. Ultimately, users are responsible for ensuring that the domain they are using to sign up for their Workspace does not have a publicly readable email inbox.”
…
“You suggested attempting to check Google Groups itself for an existing mailing list, and while this may be a useful method of finding a potential target, it’s impractical to prevent such an attack at scale. Google Groups is certainly not the only existing service that can create an open inbox in this way. Surely you’re not suggesting that Slack check every mailing list service on the Internet with each new Team sign-up to determine if it’s an unsafe email address?”
Dec 31st — Google on my 2nd report:
“I’ve shared your submission with our team working on [PROJECT] to investigate this further. Since it’s a holiday period, we are expecting longer delays — apologies for that in advance!”
Jan 8th — Google closed my 2nd report as “Won’t fix (Intended Behaviour)”:
“As I mentioned, we have shared your report with the [PROJECT] team for their review. Unfortunately, this is not a technical bug that would be in scope of our program and that is why we made the decision not to track it as a security bug.”
Jan 20th — Publish this blogpost

You read that right, everything I’ve said so far is still in effect.
By the way Google does have a category for “Logic flaw bugs bypassing significant security controls” in their Vulnerability Reward Program, so this is not even a valid argument for rejecting my report.

I left out Facebook (and Workplace), Twitter and other vendors from the timeline to keep it short, but basically everyone was blaming the users for having a “publicly readable email inbox”.

Am I affected?

This vulnerability exists if your organization has at least one public mailing list and your Slack allows for signup with an @company.com email address or you use Yammer, Workplace, etc.

Ideally https://groups.google.com/a/[DOMAIN]/forum/#!forumsearch/ should show the following:

If it displays anything else, review your settings in G Suite and make sure that your publicly visible mailing lists restrict posting to @company.com email addresses or members only.
Also, set your Slack workspace to use SSO (e.g. Okta) or make it invite-only.

Summary

Having a public mailing list where you want to discuss topics with people outside your company seems to be a completely normal idea. Having a Slack workspace that allows for registration with a company email address is not special either. But sometimes you put two and two together and the result ends up being five.

Google Groups is not only a privacy disaster, but also a security threat for many organisations.
Google has unknowingly created an email service provider that can give free @company.com email addresses to the public and is not willing to take responsibility for it. I’m publishing this in the hope that the publicity would push Google to mitigate the risk and also to help raise awareness.

Twitter: @0xmilan

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-26_how-i-compromised-1500-accountsmonth-with-no-technical-skill.md
original_filename: 2024-06-26_how-i-compromised-1500-accountsmonth-with-no-technical-skill.md
title: How I compromised 1500 accounts/month with no technical skill
category: documents
detected_topics:
- command-injection
- password-reset
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- password-reset
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: ba1ac85875dbb2bc18b61f19f22315d6d83c58ac81e3bf91da775d18df059a12
text_sha256: 60b125229f316e78c76f925771d9172bd303819b87830524267f10e387b14d22
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# How I compromised 1500 accounts/month with no technical skill

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-26_how-i-compromised-1500-accountsmonth-with-no-technical-skill.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `ba1ac85875dbb2bc18b61f19f22315d6d83c58ac81e3bf91da775d18df059a12`
- Text SHA256: `60b125229f316e78c76f925771d9172bd303819b87830524267f10e387b14d22`


## Content

---
title: "How I compromised 1500 accounts/month with no technical skill"
page_title: "Hacking airline company with no skill | Medium"
url: "https://theclemvp.medium.com/how-i-compromised-1500-accounts-month-with-no-technical-skill-6a83ecd5c8eb"
authors: ["Molx32"]
bugs: ["Privacy issue", "Information disclosure"]
publication_date: "2024-06-26"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 223
scraped_via: "browseros"
---

# How I compromised 1500 accounts/month with no technical skill

How I compromised 1500 accounts/month with no technical skill
Molx32
Follow
7 min read
·
Jun 26, 2024

68

Feel free to check my personnal blog where I post those articles. Check the free version of this post here. Have a nice reading .

A little bit of context

For the past few months, I investigated what I call Public SMS Service (PSS), which are simple websites proposing virtual phone numbers for free, to receive SMSs e.g. SMS To Me. This is used by many people for testing purposes and privacy. But SMS received on these phone numbers can be read by anyone, and that’s what I did.

If you take a look at SMS To Me or similar websites, you probably won’t see any sensitive information. So why would I spend months investigating those messages? Because I once saw something like this.

Hi redacted@gmail.com, your new access code is 458953. You can now connect on https://REDACTED.com.

Free credentials!

I quickly configured an anonymization pipeline and accessed the account. The website was a cryptocurrency application that allowed users to access their different wallets. I had access to personal information and to a significative amount of 65 Bitcoins. I had three hypothesis in mind:

This is a human mistake — The person owning the account used a Public SMS Service (PSS) ignoring what the consequences could be.
This is a development environment — In this case, the account is not a real one, or at least this is a test account, with mocking data.
This is some kind of aggressive honeypot — Since the message is received on a PSS, and that it leaks the three key information needed to access the account (website, username and password), it seemed too obvious not to be a honeypot.

In the end, the domain was created three months ago, and all features were not implemented yet, so it probably was a development environment.

The security risks

Sometimes, people use this kind of public phone numbers to register on web applications, to avoid sharing their real phone number. This is a mistake! As a end users, we don’t know what SMS the application could send to the PSS :

A SMS with a password reset URL
A SMS with a URL leaking various informations e.g. an order summary.
A SMS with a URL to access the user account, directly authenticated.

Anyways, that triggered my attention, so I developped a Python Flask web app to help me parse and analyze SMSs I could find on https://receive-smss.com/ (I chose this website because it was easy to automate).

SMS Explorer ✉️👀

I’ll probably publish the app and post about it to explain what is does, but real quick :

It collects all SMSs and extract URLs (and domains)
It analyzes domains and tag them as interesting
It automates data collection by navigating to URLs

Here is a simplified DB scheme.

# SMS
id | content  | url  | has_data
1  | Hello, [...] | https://domain1.net/some/path | True
2  | Hello, [...] | https://domain2.net/some/path | True
3  | Hello, [...] | https://domain3.net/some/path | False
4  | Some ad  | -  | False

# TARGETS
id | domain  | is_interesting | is_automated
1  | domain1.net | True  | True
2  | domain2.net | True  | True
3  | domain3.net | True  | False

# DATA
id | url  | data
1  | https://domain1.net/some/path | {"some":"json"}
2  | https://domain2.net/some/path | {"some":"json"}

After adding some metadata and waiting a few week, the interface looks like this.

Press enter or click to view image in full size

Before getting to the data leak, here are some statistics.

4% of SMSs contain URL, the 96% remaining are mainly garbage.
The SMS rate is approximately 2200 SMS/hour
Most SMSs are received on UK phone numbers. Actually, if we divide this count by the number of phone numbers available by country, Indian phone numbers are the most active ones.
More than 50% of SMSs that contain a URL are scams or ads.
Press enter or click to view image in full size

I collected millions of SMSs at different states of the development, and it requires a tremendous amount of time to analyze all the different targets, so I can’t tell how much URLs lead to data leaks or account takeovers.

The airline hack

Before we start :

⚠️I started collecting SMS approximately 6 months ago. I estimated the total leaked users to 1500 users per month which gives at least total of 9000 records leaked.
⚠️ Since this is still confidential, let’s name the company AirLine.

I was excited to work of my final version on SMS Explorer, and I wanted to work on a case I observed a few days ago : the AirLine case. By using a quick search, I retrieved a list a hundreds of SMSs looking like this.

Thank you for flying with us. Please, rate your experience : https://sub.airline.tld/rEDaCt3d — AirLine

Press enter or click to view image in full size
SMS Explorer — Search feature

When navigating to the URL, we are redirected to a survey, hosted at https://airline.qualtrics.com. For your information, Qualtrics is a SaaS solution to create various things, including surveys. The URL looks like this :

https://airline.qualtrics.com/jfe/form/Un1Qu3_1D3nt1f13R?param1=a&par[…]

Press enter or click to view image in full size

Here is a table summarizing all URL parameters.

Press enter or click to view image in full size
Qualtrics parameters

As you can see, there is all the reservation-related information, which I double checked with web apps like https://flightstats.com/. Beyond personal information which represent itself a data leak, there are two fields that can be exploited : PNR (Passenger Name Record) and PLN (Passenger Last Name), which if you didn’t guess are credentials to login into AirLine web application (like many airlines, if not all)!

Credentials!

Here is the information we can retrieve.

Press enter or click to view image in full size
List of flights for a given PNR
Press enter or click to view image in full size
PNR detailed information

You can see on the pictures that some fields are obsfuscated with stars *, but they are actually in clear text in the session storage. The only thing that can’t be retrieved is the payment card information.

Press enter or click to view image in full size
Session storage data
Impact

So an attacker can connect to manage their flights, even if the flight already occured. What can be achieved once connected?

Access more data, such as birth date and future/past flights.
Take over the account by editing contact and password resetting.
Contact the AirLine support to make a change on the flight (first name, last name, and so on). This would allow an attacker to pay only for a change rather than a flight (still it may be very expansive).
Add extra services, and cause a price increase for the end customer (the real user may need to re-validate payment, so not sure for this).

A funny thing is that the survey is meant to get a feedback about reservation, check-in, in-flight meal, arrival and exit, but it seems to be sent immediately after tickets are bought i.e. before the flight date.

Fixing the issue

In order for me to understand how the survey works I created a test survey available here that reads a URL parameter Name and display its value in the first question. Example with a survey for Molx, or for Bender.

Get Molx32’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This way of doing things is actually approved by Qualtrics, but the issue is that too many parameters are passed here. The PNR only would be enough for AirLine to match its travelers database, and to prevent accounts to be compromised.

Responsible disclosure

I contacted a national CERT which quickly acknowledged, and the issue took a few months to be fixed : now I don’t see any SMS asking for feedbacks, but I guess new SMS will be sent, in a safe way let’s hope.

Final thought

Although it is a user mistake to use public phone numbers to register on web applications, it is possible to filter such phone numbers when registering travelers. On the other hand, using such phone number (when data is not leaked) is a good way of improving end user privacy.

This first post is some kind of introduction for my SMS Explorer web app which should be release this year. Until then, I will probably post about how I compromised other targets again with no technical skill!

Thanks for reading.

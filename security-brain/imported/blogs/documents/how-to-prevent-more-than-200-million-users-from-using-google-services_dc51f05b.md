---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-16_how-to-prevent-more-than-200-million-users-from-using-google-services.md
original_filename: 2021-05-16_how-to-prevent-more-than-200-million-users-from-using-google-services.md
title: How to prevent more than 200 million users from using Google services
category: documents
detected_topics:
- sso
- command-injection
- rate-limit
- business-logic
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- rate-limit
- business-logic
- cloud-security
language: en
raw_sha256: dc51f05b2d11ca7f3f7b3f080e31aa769d36cf8c5fe3f8600b208de3b133d38c
text_sha256: b718b884ff30594ed6bb8422964a5a38c20fb7029d4a369b0de0cfb490edc330
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How to prevent more than 200 million users from using Google services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-16_how-to-prevent-more-than-200-million-users-from-using-google-services.md
- Source Type: markdown
- Detected Topics: sso, command-injection, rate-limit, business-logic, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `dc51f05b2d11ca7f3f7b3f080e31aa769d36cf8c5fe3f8600b208de3b133d38c`
- Text SHA256: `b718b884ff30594ed6bb8422964a5a38c20fb7029d4a369b0de0cfb490edc330`


## Content

---
title: "How to prevent more than 200 million users from using Google services"
url: "https://omar0x01.medium.com/how-to-prevent-more-than-200-million-users-from-using-google-services-136b3b8e221f"
authors: ["Omar Hashem (@OmarHashem666)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2021-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3653
scraped_via: "browseros"
---

# How to prevent more than 200 million users from using Google services

How to prevent more than 200 million users from using Google services
Omar Hashem
Follow
3 min read
·
May 16, 2021

171

Hi Folks,

when hunting in Google I found that Google own this domain appsheet.com you can check this here https://whois.com/whois/appsheet.com
so I started to search for vulnerabilities in it, so I found some bugs and they can associate together to abuse a harmful risk to a company so let’s start
first bug let’s see this Proof of concept first and then complete

I notice while register in https://community.appsheet.com you should first enter your personal information like Email, Name, UserName, Password and Portfolio URL so after enter your information and register, your information entered directly to database and that not the right way to register new accounts, the right way is to verify your account first then your personal data get into database as a new user, so the first bug is Denial Of Service as you can prevent users from register by simply using them emails and after that they will receive verification message and because they didn’t request it they will ignore it and after some hours the verification email will expire and after that there is no way to register with this account at all and if the owner of email try to register he will find message tell him that (email has already been taken) the other scenario is the owner of the email decide to click on verification link before it expire and activate account so now his account under attacker control because he assigned username and password for the victim account

So now we in the first stage let’s go to next one
so as a reason for the first bug you can prevent all users from register except Gmail users they have one way to register with Google, but there is second bug let’s see second proof of concept and complete (you can make speed of video 1.25x)

so as you can see that you can assign Name, UserName and App portfolio URL to users that register with Google email, so maybe you can put to them in Name field like welcome message and in Portfolio URL field Phishing link or any malicious link that should be trusted because new user will think it comes from Google Company, but it’s not

Get Omar Hashem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

now let’s go to final stage

there is misconfiguration in rate limit in registration form that developer give you possibility to register 300 new account and then ban you from register for some hours and to register new account you should send three requests, so I wrote this python script to do the job here it is

now let’s see attack scenario and do small calculation:
First thing attacker will do is collect all emails in data leaks after that you can use my script and edit it to make requests pass through tor proxy or any tool for IP rotation and after register 300 new account in approximately 3 minutes then change IPs with this method you can prevent 6000 users from using all services in this subdomain in one hour and in one day you can prevent 6000 user in an hour * 24 hours in a day == 108000 user from using this sub then if you are a college student azure give you 100 dollar for using 2 VPS you can collect your friends accounts let’s say at minimum 30 accounts, so now additionally to your account you have (31 accounts * 2 VPS * 108000 user in a day * 30 day in month == 200880000 user every month) so you can increase the number of the users that you can prevent them or phishing them every month according to your capabilities

If there is something you do not understand in this write-up or need any help in bug bounty hunting you can DM me on Twitter or Linkedin

Thanks for reading

Stay in touch

Linkedin | Youtube | Twitter

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

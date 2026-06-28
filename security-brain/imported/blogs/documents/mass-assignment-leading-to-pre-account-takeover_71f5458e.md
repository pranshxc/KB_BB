---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-21_mass-assignment-leading-to-pre-account-takeover.md
original_filename: 2022-09-21_mass-assignment-leading-to-pre-account-takeover.md
title: Mass Assignment Leading to Pre Account Takeover
category: documents
detected_topics:
- api-security
- command-injection
tags:
- imported
- documents
- api-security
- command-injection
language: en
raw_sha256: 71f5458ed1c5f8abd699ada4ed52e0cd12d6f5e45d06377e25414e635674bbba
text_sha256: 470da4a1892122b4025644efabbaf219795498d5e4e4b92138e7d9f691b6c038
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Mass Assignment Leading to Pre Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-21_mass-assignment-leading-to-pre-account-takeover.md
- Source Type: markdown
- Detected Topics: api-security, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `71f5458ed1c5f8abd699ada4ed52e0cd12d6f5e45d06377e25414e635674bbba`
- Text SHA256: `470da4a1892122b4025644efabbaf219795498d5e4e4b92138e7d9f691b6c038`


## Content

---
title: "Mass Assignment Leading to Pre Account Takeover"
url: "https://medium.com/@cyberali/mass-assignment-leading-to-pre-account-takeover-13041280a0d9"
authors: ["Cyberali"]
bugs: ["Mass assignment"]
bounty: "1,300"
publication_date: "2022-09-21"
added_date: "2022-09-22"
source: "pentester.land/writeups.json"
original_index: 2141
scraped_via: "browseros"
---

# Mass Assignment Leading to Pre Account Takeover

Mass Assignment Leading to Pre Account Takeover
Cyberali
Follow
4 min read
·
Sep 21, 2022

92

5

API also called as Application Programmable Interface is used everywhere from modern automotive (smart), mobile, web and IOT devices etc. They are the building block of application now a days. Moving from web2.0 to web3.0 we find it everywhere. It helps the computing capabilities to utilize the resources of each other by providing ease in communication. Like in order to make two individuals from different language and country, come on same point of understanding we will have to come on same level so we will invite a third person who will help those two individuals in translating. So that third person is acting as API between two.

We have a basic idea about why API’s are used. Moving forward towards security perspective, I want to share one of my interesting finding on a private program. I found some interesting vulnerabilities in the target domain but at that time I just started API testing and I was looking to exploit the API level vulnerability to evaluate my learning. I focused on API OWASP top 10 which I learned from VAmpI Lab.

My target was under-development and the scope was limited. I though to break the scope while being in the scope (I know you didn’t understood this line. Haahahha).

Following Functionality which is appearing in the below screen shot was restricted:

Email Edit.

Profile Photo.

We can only change the Name field.

Press enter or click to view image in full size
Profile Information of Target

I was thinking what else I could do at this endpoint. When reviewing the OWASP top 10 I got stuck on Mass Assignment.

Mass Assignment

In this vulnerability the developer has left an “open window” for a normal user to be able to manipulate the request post body and add sensitive parameter’s like is_Admin, email, new_password etc. The guessing of parameters and it’s value is a little bit challenging. Once parameter is guessed the exploit is easy and interesting. This is something more known as Mass Assignment where guessing object`s properties and exploring options in endpoints is involved.

In target Web Application, The attacker can easily register and verify on the behalf of other users without their knowledge. When changing the profile record there is no option for changing the email account on target, due to mass assignment the attacker can easily inject a custom key value “email”:”victims_email” to register on victims account. After injecting the email of the victim, the attacker can also verify his email. Just click on the verify account the attacker will receive an email with a verification link, click it and the account is verified. Now logout and again login with the attackers credentials you will not be able to login. Change the email with new email(victims) You will be logged in.

Since you have a clear concept about how Mass Assignment Vulnerability works, now let’s move towards the steps which I followed to exploit this vulnerability.

Get Cyberali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps to Reproduce:

Create an account on your target domain.
Navigate towards the Edit Profile Option and sharply filter the functionality. Like what options are available to edit and what options are restricted. In my case, change email option was not allowed to edit.
Change the Name field and Turn on your burp suite proxy intercept.
Click on submit button. Capture the request on burp suite.
In proxy tab, right click and send the request to repeater. Add a parameter named as “email” in request body and click on send.
Press enter or click to view image in full size
Request Captured in Burp suite

6. The request will be successfully completed and attacker will receive a conformation link in his account i.e. to confirm if he wants to change the email or not. After the attacker confirms the link victims email will be added to the attackers account.

Press enter or click to view image in full size
Confirmation Link Attacker Receives

Bounty:

Bounty Received

It the end, I would like to say don’t just stick to the available functionality. Think out of the box and try to make the application behave abnormally. Like I did, the normal behavior was something else and I closed the bug on a different functionality which was not apparently present on the system.

Just Chill….Don’t forget the coffee cup…

Thank you!

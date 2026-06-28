---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-09_facebook-emailphone-disclosure-using-binary-search.md
original_filename: 2021-07-09_facebook-emailphone-disclosure-using-binary-search.md
title: Facebook Email/phone disclosure using Binary search
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
- information-disclosure
- mobile-security
language: en
raw_sha256: 190107f3bb9b99bccf2e95c1b1a6e455fc0ec67411dfed2b1b1ca639a0f565e3
text_sha256: 50d1e4536d46a6ba51f04c72ab29206388b8415995b446010ddaffb4976f6000
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Email/phone disclosure using Binary search

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-09_facebook-emailphone-disclosure-using-binary-search.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `190107f3bb9b99bccf2e95c1b1a6e455fc0ec67411dfed2b1b1ca639a0f565e3`
- Text SHA256: `50d1e4536d46a6ba51f04c72ab29206388b8415995b446010ddaffb4976f6000`


## Content

---
title: "Facebook Email/phone disclosure using Binary search"
url: "https://medium.com/pentesternepal/facebook-email-phone-disclosure-using-binary-search-d50430758c54"
authors: ["Rikesh Baniya (@rikeshbaniya)"]
programs: ["Meta / Facebook"]
bugs: ["Password reset", "Information disclosure", "Bruteforce"]
publication_date: "2021-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3520
scraped_via: "browseros"
---

# Facebook Email/phone disclosure using Binary search

Facebook Email/phone disclosure using Binary search
Rikesh Baniya
Follow
3 min read
·
Jul 9, 2021

668

1

So in December I decided to hunt on Facebook, and chose to go with the Facebook Android App

I was analyzing the Facebook app’s password recovery flow.

I noticed that the following endpoint was being used.

When a user enters his email/phone number his email is supplied in the following manner using parameter `q`

The endpoint contained manyyyyy parameters, more than it required.

So I was eager to test what those parameters did.

I quickly noticed that although the user’s email is being carried by `q` parameter, it also contains a `qs` parameter.

Now, incase you don't know;
In Facebook the character `s` behind a parameter means plural.

Example:
invite_id, Plural= invite_ids
user_id, Plural=user_ids

I knew that in plural parameters you can supply array of data
like:
user_ids=[“UserID1”,”UserID2"]

so I supplied data in following manner:

qs=[“vicitmemail1@gmail.com”,”victimemail2@gmail.com”]

But it gave an error stating the array key are invalid.

So this wasn't a normal array, it had its own keys.

So after some fuzzing I finally figured out that the parameter `qs` takes the value in json wrapped format along with the keys “phone” and “email” and the values of email/phone are the ones that will be supplied as an array

Example:
q=victim@gmail.com
qs={“email”:[“victim@gmail.com”],”phone”:[“981234567890”]}

Now,
When you supply an email in the forget password endpoint, the data belonging to you is given in the response in encrypted format.

The response will contain:
your encrypted userID ,contact points etc

Press enter or click to view image in full size

Along with the data there was a value `summary` and it was set to `1`.

Initially I thought it to be a Boolean.
But turns out:

When we supply one email in `qs`
qs={“email”:[“user1@gmail.com”]}
Data of one user is obtained in response.
hence: summary=1

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When we supply two emails in `qs`
qs={“email”:[“user1@gmail.com”,”user2@gmail.com”]}
Data of two users is obtained in response.
Hence: summary=2

But here comes the final part:

Lets say I supply:
qs={“email”:[“victim1@gmail.com”,”victim2@gmail.com]}
Data of only 1 user is obtained.

What does that mean?
Both the emails belong to the same user and both emails pointed to same user resulting in the response “summary”:1

Now, basically it was bruteforce attack scenario.

I supply victim's username along with a email and if the email belonged to victim the response is “summary:1”

qs={“email”:[“victimUserName”,”Email”]}

//Yup, We can supply username in email parameter

BinarySearch to the rescue

Bruteforce attacks are noisyyy.
But using binary search, this attack became much easier.

Refer to this video to learn about BinarySearch:

Since, the endpoint was accepting an array of data:
I wasn’t forced to only submit
1 username+1 email

I could supply
1username+ 100s of email.

Example;

qs={“email”:[“victimUserName”,”email1@gmail.com”,”email2@gmail.com”,”email3@gmail.com”]}

Now if any of the email from the request belonged to vicitmUserName:

Summary=3
//Response of email1+email2+email3

Else summary=4
//Response of vicitmUsername+email1+email2+email3

This made it easier to bruteforce and effectively identify any user’s private email.

Diagram demonstrating the binarySearch

Press enter or click to view image in full size

I also received this sweeeet response from the Facebook team,
felt good ;)

Press enter or click to view image in full size

Timeline
Submitted : January 3
Triaged: February 13
Bounty $XXXX Awarded :March 22

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-23_responsible-disclosure-retrieving-a-users-private-facebook-friends.md
original_filename: 2018-09-23_responsible-disclosure-retrieving-a-users-private-facebook-friends.md
title: 'Responsible disclosure: retrieving a user''s private Facebook friends.'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: 693c59ce8f19411b1d90efcf51b11ad1080ed272f2047b102d109db2e91c4269
text_sha256: b0665f3fcef17a82ecc4a4ab067dc19675eddc7f0060d88c437c825252fd1d3c
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Responsible disclosure: retrieving a user's private Facebook friends.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-23_responsible-disclosure-retrieving-a-users-private-facebook-friends.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `693c59ce8f19411b1d90efcf51b11ad1080ed272f2047b102d109db2e91c4269`
- Text SHA256: `b0665f3fcef17a82ecc4a4ab067dc19675eddc7f0060d88c437c825252fd1d3c`


## Content

---
title: "Responsible disclosure: retrieving a user's private Facebook friends."
url: "https://rpadovani.com/facebook-responsible-disclosure"
final_url: "https://rpadovani.com/facebook-responsible-disclosure"
authors: ["Riccardo Padovani (@rpadovani93)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization", "Information disclosure"]
bounty: "3,000"
publication_date: "2018-09-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5684
---

# Responsible disclosure: retrieving a user's private Facebook friends.

Data access control isn’t easy. While it can sound quite simple, it is very difficult, both on a theoretical side and on a practical side.

[ ![Profile picture of Riccardo Padovani](https://rpadovani.com/media/ptrpi1Gl1jueItEHEK7cAistnEI0oU5kLV14EQsL.png) Riccardo Padovani ](https://rpadovani.com/author/riccardo-padovani)

|  Published  Sep 23, 2018 

On the pratical side, how we will see, disclose of private data is often a unwanted side effect of an useful feature.

## Facebook and Instagram

Facebook bought Instagram back in 2012. Since then, a lot of integrations have been implemented between them: among the others, when you suscribe to Instagram, it will suggest you who to follow based on your Facebook friends.

Your Instagram and Facebook accounts are then somehow linked: it happens both if you sign up to Instagram using your Facebook account (doh!), but also if you sign up to Instagram creating a new account but using the same email you use in your Facebook account (there are also other way Instagram links your new account with an existing Facebook account, but they are not of our interest here).

So if you want to create a _secret_ Instagram account, create a new mail for it ;-)

Back in topic: Instagram used to enable all its feature to new users, **before** they have confirmed their email address. This was to do not “interrupt” usage of the website / app, they would have been time to confirm the email later in their usage.

Email address confirmation is useful to confirm you are signing up using your own email address, and not one of someone else.

## Data leak

One of the features available **before** confirming the email address, was the suggestion of who to follow based on the Facebook friends of the account Instagram automatically linked.

This made super easy to retrieve the Facebook’s friend list of anyone who doesn’t have an Instagram account, and since there are more than 2 billions Facebook accounts but just 800 millions Instagram accounts, it means that at least 1 billion and half accounts were vulnerable.

The method was simple: knowing the email address of the target (and an email address is all but secret), the attacker had just to sign up to Instagram with that email, and then go to the suggestions of people to follow to see victim’s friends.

![List of victim's friends](https://rpadovani.hyvorblogs.io/media/k4nkFhEvnnALNEKn.png)

## Conclusion

The combination of two useful features (suggestion of people to follow based on a linked Facebook account, being able to use the new Instagram account immediately) made this data leak possible.

It wasn’t important if the attacker was a Facebook’s friend with the victim, or the privacy settings of the victim’s account on Facebook. Heck, the attacker didn’t need a Facebook account at all!

## Timeline

  * **20 August 2018** : first disclosure to Facebook

  * **20 August 2018** : request of other information from Facebook

  * **20 August 2018** : more information provided to Facebook

  * **21 August 2018** : Facebook closed the issue saying wasn’t a security issue

  * **21 August 2018** : I submitted a new demo with more information

  * **23 August 2018** : Facebook confirmed the issue

  * **30 August 2018** : Facebook deployed a fix and asked for a test

  * **12 September 2018** : Facebook awarded me a bounty

## Bounty

Facebook awarded me a $3000 bounty award for the disclosure. This was the first time I was awarded for a [security disclosure for Facebook](https://www.facebook.com/whitehat), I am quite happy with the result and I applaude Facebook for making all the process really straightforward.

For any comment, feedback, critic, leave me a comment below or drop an email at `[[email protected]](/cdn-cgi/l/email-protection)`.

Regards, R.

[security](https://rpadovani.com/tag/security)

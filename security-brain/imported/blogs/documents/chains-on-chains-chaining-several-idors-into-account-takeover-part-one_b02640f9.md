---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-15_chains-on-chains-chaining-several-idors-into-account-takeoverpart-one.md
original_filename: 2019-11-15_chains-on-chains-chaining-several-idors-into-account-takeoverpart-one.md
title: Chains on Chains!! Chaining several IDOR’s into Account Takeover(PART ONE)
category: documents
detected_topics:
- rate-limit
- sso
- idor
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- rate-limit
- sso
- idor
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: b02640f97998bb5c3132764e9cad63d71ad462101427fa020ec7a166fa4e90fc
text_sha256: e1c9935141ec5700d42a6c3f8b4c6fa908f7cc47f0a0964bc26c201e57aa464d
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Chains on Chains!! Chaining several IDOR’s into Account Takeover(PART ONE)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-15_chains-on-chains-chaining-several-idors-into-account-takeoverpart-one.md
- Source Type: markdown
- Detected Topics: rate-limit, sso, idor, command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b02640f97998bb5c3132764e9cad63d71ad462101427fa020ec7a166fa4e90fc`
- Text SHA256: `e1c9935141ec5700d42a6c3f8b4c6fa908f7cc47f0a0964bc26c201e57aa464d`


## Content

---
title: "Chains on Chains!! Chaining several IDOR’s into Account Takeover(PART ONE)"
url: "https://medium.com/@masonhck357/chains-on-chains-chaining-several-idors-into-account-takeover-part-one-373627f2910f"
authors: ["Daniel Marte (@DanielM59720745)"]
bugs: ["IDOR"]
publication_date: "2019-11-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4943
scraped_via: "browseros"
---

# Chains on Chains!! Chaining several IDOR’s into Account Takeover(PART ONE)

Chains on Chains!! Chaining several IDOR’s into Account Takeover(PART ONE)
Daniel Marte
Follow
4 min read
·
Nov 15, 2019

220

2

Press enter or click to view image in full size

Hello Everybody,

Welcome to my FIRST writeup! Just to give you some background, My name is Daniel, I started hacking about 4 months ago and can’t stop! I’ve really been enjoying learning and exploiting some bugs! :D This writeup will be about how I achieved my first Account Takeover by chaining a couple of IDORS and taking advantage of leaked information.

Background on the program: The program is a utility company that provides services to a state. Within this program, you can signup for several services using the same credentials. We will call it https://gas.com/

So I was doing some content discovery and I located a service that gas.com uses. let us call this service “utility”(https://gas.com/utility/)

*Do Note*: I do have an account set up on gas.com and now I will be enrolling in the “utility” services utilizing the same account information as gas.com

So I am able to enroll in “Utility” as long as I had my accountID and 4-digit pin.

Step 1: Input AccountID and pin

Step 2: It asked me to confirm the email address associated with the AccountID yet the email address was already prepopulated (remember this)

Step 3: Then gives you the option to set your username(also prepopulated) and password.

Once logged in, you can create an agreement to submit which prepopulates sensitive information when you are ready to submit(name, phone number, employer, address, first and last name)

In the profile section of “utility”, I am able to change the email address, username, and password.

Get Daniel Marte’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Ok, so cool, everything working as intended, right? How am I supposed to retrieve a user’s Account ID’s, 4- digit pins AND email addresses?

How Can I capture the victims AccountID?

Well, let's go back to Step 1 of enrollment, when I input the AccountID, the server automatically calls this endpoint to validate https://gas.com/utility/account/check/{{AccountID}} that returns a True or false.

So I ended up looking at the account ID’s for both of my accounts and I found something interesting! Both AccountID’s were only different on the first 6 digits! It definitely looks like the AccountID endpoint is able to be enumerated very easily via brute force if you only try and brute-force the first 6 digits of the accountID followed by 4 zeros and a single digit (1–9) with no problem. For example. My account ID number is 12345600007. ‘123456’ is what I will brute force. The 4 zero’s following it stay the same and the ‘7’ can be changed between 0–9. I was able to enumerate several account ID’s just running the brute force for about 15 minutes(Disclaimer: I did NOT take additional action with those accounts!!!) I can also verify if that account has been enrolled by calling this endpoint: https://gas.com/utility/enrolled/check/{{AccountID}} which will return a True or False if it been enrolled or not.

Ok, got the victims AccountID but how do I capture the pin number?

Once you add the pin, the server does yet another validation, this one is for the pin: https://gas.com/utility/pin/check POST sending the following parameters” {“accountNumber”:”12345600007",”accountPin”:”1234"}” I think we can all agree that brute-forcing a 4 digit pin is very easy and quick. Once I hit the right pin number, it will validate that the account DOES exist, as well as spit out the email address associated with the victim. So now I can use this endpoint to enumerate victim’s Accountpins and email addresses by simply having an AccountID.

So now I have a victims accountID, accountpin, and email address, now what?

Ok, back to Step 1 with victim information and let's enroll them:

Step 1: I enrolled using victims AccountID and AccountPin and pressed next

Step 2: It asked to enter victims email address and confirm it(remember its already populated) so I press next

Step 3: Confirm username(already populated) and set password

Now, I have officially enrolled the victim in the property portal. So what do I see?

Well, I can act on behalf of the victim in any action I take now that I am logged in. If I were to create an agreement on behalf of the victim, It will prepopulate it with sensitive information from its main account(name, phone number, employer, address, first and last name) I am also able to change the email address on the My profile section.

That was a light switch for me. If these accounts are tied together, what If I were to change the password, would the password change also work on the main account? Unfortunately, that did not work at all BUT I did notice a notification that stated IF I were to change the password here, it will propagate on the main page

What this means is that if I change my email address here, It will reflect on the account services as well! This ultimately means that I can now go on ahead an easily change the victim's password by being able to change the email address in utility and then send the forgot password request on the main page. This allows 100% full takeover of every Account that I can enumerate.

Conclusion: How fun was that? I encourage those who test programs to always test for IDOR’s and see what information is leaking. Always ask yourself, can you leverage this information into something impactful? I really hope this helps some beginners while they are developing their methodology. I will be releasing Part Deux this week on how I found another Account Takeover in the same program by parsing Old Javascript files from Wayback archive.

If you have any questions, feel free to hit the DM https://twitter.com/Masonhck3571:D

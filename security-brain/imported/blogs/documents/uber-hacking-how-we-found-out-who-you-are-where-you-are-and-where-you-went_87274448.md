---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-06-24_uber-hacking-how-we-found-out-who-you-are-where-you-are-and-where-you-went.md
original_filename: 2016-06-24_uber-hacking-how-we-found-out-who-you-are-where-you-are-and-where-you-went.md
title: 'Uber Hacking: How we found out who you are, where you are and where you went'
category: documents
detected_topics:
- rate-limit
- mobile-security
- access-control
- sso
- idor
- command-injection
tags:
- imported
- documents
- rate-limit
- mobile-security
- access-control
- sso
- idor
- command-injection
language: en
raw_sha256: 87274448483da9d3bb42141319637e4dd14634f07a040ea683d351787969294e
text_sha256: 68cc5cf7bb98a89684c084070ba40d48c259624f0cb6ede1c7c4a2cb7081c5e8
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Uber Hacking: How we found out who you are, where you are and where you went

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-06-24_uber-hacking-how-we-found-out-who-you-are-where-you-are-and-where-you-went.md
- Source Type: markdown
- Detected Topics: rate-limit, mobile-security, access-control, sso, idor, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `87274448483da9d3bb42141319637e4dd14634f07a040ea683d351787969294e`
- Text SHA256: `68cc5cf7bb98a89684c084070ba40d48c259624f0cb6ede1c7c4a2cb7081c5e8`


## Content

---
title: "Uber Hacking: How we found out who you are, where you are and where you went"
url: "https://medium.com/@r0t1v/uber-hacking-how-we-found-out-who-you-are-where-you-are-and-where-you-went-1e0769674535"
authors: ["Vitor “r0t” Oliveira (@r0t1v)"]
programs: ["Uber"]
bugs: ["Bruteforce", "Information disclosure", "Logic flaw", "IDOR"]
bounty: "18,000"
publication_date: "2016-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6284
scraped_via: "browseros"
---

# Uber Hacking: How we found out who you are, where you are and where you went

Uber Hacking: How we found out who you are, where you are and where you went
Vitor “r0t1v” Oliveira
Follow
11 min read
·
Jun 24, 2016

153

1

Here at Integrity we love to be challenged, so whenever there is some free time, there is encouragement to do research or to break some things (http://labs.integrity.pt/advisories/) in addition to play foosball.

We (@r0t1v, @fjreis, @fabiopirespt) decided to use this time to jump into some bug bounties.

What is a bug bounty?

As stated in wikipedia:

A bug bounty program is a deal offered by many websites and software developers by which individuals can receive recognition and compensation for reporting bugs, especially those pertaining to exploits and vulnerabilities. These programs allow the developers to discover and resolve bugs before the general public is aware of them, preventing incidents of widespread abuse.

For our luck, Uber decided to open their bug bounty program to the public, and in Portugal, Uber was almost a daily issue in the news because of the taxi drivers, so we dove right into this program.

After a couple of hours, we found out two open redirects that we reported right away. This could be the start of something good (we thought), but both issues were already reported by other researchers.

At first it was a bit disappointing, but not giving up we doubled back and decided to implement some processes/methodologies.

The process / Methodology

In order to implement some kind of methodology, we went back to the Uber bug bounty program to check again their scope, which is far extensive as it can be seen below:

https://*.uber.com/
http://*.uberinternal.com/ (added later into the program)
http://petition.uber.org
http://ubermovement.com
iPhone Rider Application
iPhone Partner Application
Android Rider Application
Android Partner Application
Information Gathering

To gather more information about Uber subdomains we started with a dns brute-force.

Press enter or click to view image in full size

With all subdomains enumerated, all that was left to do was to use nmap and check for banners, page titles, page redirects as well as exploit-db and some blogs for known vulnerabilities.

For the mobile apps, jd-gui was used to read the java classes in order to map the mobile endpoints, later we also turned toMobSF.

Press enter or click to view image in full size

Now, judging from the information that we gathered, we felt that it was more than enough to start searching for some vulnerabilities.

Vulnerabilities

0×01 — Possibility to brute force promo codes in riders.uber.com

Uber has a feature that allows the usage of promotion codes. This codes can be given by other users or companies. The application riders.uber.com had this feature in the payment page, so after adding a new promotion code we grabbed the request and realised that the application didn’t had any kind of protection against brute-force attacks, which helped us to find many different promotion codes.

Press enter or click to view image in full size

The image below illustrates our brute force attack. As stated before different codes were found and can be distinguished by their response.

Responses length:

1951 — Valid code
1931 — Not valid
1921 — Code Expired
Press enter or click to view image in full size

Uber also gives an option to customize promotion codes, and since all the default codes began with the word “uber”, it was possible to drop the time of the brute force considerably allowing us to find more than 1000 valid codes.

Initially this issue was not considered valid because the promotions codes are supposed to be public and be given by anyone. This was true until finding an $100 ERH (Emergency Ride Home) code which they (uber-sec team) had no knowledge about. This ERH codes work differently from all others since even if a promotion code is already applied this ones can still be added.

Press enter or click to view image in full size
DISCLOSURE TIMELINE

March 23, 2016 — Bug reported to Uber
March 23, 2016 — Uber’s team changed status to Informative
March 24, 2016 — We provided new information
March 24, 2016 — Uber’s team changed status to Triaged
April 19, 2016 — Uber’s team changed status to Resolved
May 2, 2016 — Uber rewarded us with a bounty.

0×02 — Possibility to get private email using UUID

As you can see in the picture below, inside Uber riders mobile application there is a “Help” section that allow users to send questions directly to support. Let’s be honest, many of us almost never use the “Help” or even know that it exists, but as pentesters we can’t say no to another form. (later we found that the Partners application had the same forms).

Press enter or click to view image in full size

After submitting a question, the server would reply with the message: “We’ve received your request and will be in touch as soon as possible via <my-email-address>”. Looking at this message we thought that maybe we could enumerate some user emails.

By looking at the request there are two places (the x-uber-uuid header and the uuid parameter) that might allow us to get emails from other users if we change them for another valid UUID. We tried to change both, but unfortunately the server returned our email again. Although there is a token parameter also, our first approach was to fuzz a bit into this parameter but in the end we end up by changing it to another user UUID and something magic happened, the webserver returned the email address for that user.

It’s a bit hard to say why a UUID has been interpreted as a valid token, but it is indeed.

Since the application wasn’t throttling our requests in this endpoint, we grabbed a small amount of UUIDs and with them we were able to get all the emails corresponding to those UUIDs. Now you’re probably asking: “how can you know UUIDs from other users?”, that’s what we will explain later.

DISCLOSURE TIMELINE

March 31, 2016 — Bug reported to Uber
March 31, 2016 — Uber’s team changed status to Triaged
April 11, 2016 — Uber’s team changed status to Resolved
April 13, 2016 — Uber rewarded us with a bounty.

0×03 — Enumerating UserIDs with phone numbers (duplicated)

When looking for vulnerabilities we always try to find all of the application/webapp features, especially those that aren’t easily found or used. With this in mind, we decided to get our phones, computers and called for a Uber and so we did. During our trip we intercepted all the requests and one of those requests caught our attention.

This request happens when an user tries to split his fare with others. To invite someone to split the fare, the user needs to add a phone number from his contact list.

The problem here is that the response is leaking too much information such as driver UUID, invitees UUIDs and the invitees picture, even before they accepting the fare split.

Get Vitor “r0t1v” Oliveira’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can see the app leaking the information in the pictures below:

Press enter or click to view image in full size
Press enter or click to view image in full size

Remember before when we told you that we would explain how we got a list of UUIDs? This is how!

Now, joining this vulnerability with the previous one we could get anyones email address that was associated to the phone number.

Unfortunately, after reporting this issue, it was marked as duplicated.

DISCLOSURE TIMELINE

April 6, 2016 — Bug reported to Uber
April 7, 2016 — Uber’s team changed status to Needs more info
April 7, 2016 — We provided new information
April 7, 2016 — Uber’s team changed status to Duplicate

0×04 — Use Partner/Driver App Without Being Activated (duplicated)

Every user is able to create a driver account but it remains not activated until Uber verify all your driver documents.

After started to test the Partner/Driver app, we realized that you can only enter in the mobile app after the activation process.

Looking on the request of the response above, you can see a parameter called allowNotActivated and his value wasfalse.

By manipulating the login request and changing the parameter allowNotActivated to true, it was possible to obtain a valid session token. So at least, it means that the server create a valid token even when the account was not activated.

As you can see on the response, there is a field called isActivated setted to false. Changing this to true allowed us to get into the app.

Now we got a couple of new features to test.

DISCLOSURE TIMELINE

March 31, 2016 — Bug reported to Uber
March 31, 2016 — Uber’s team changed status to Needs more info.
March 31, 2016 — We provided new information
April 7, 2016 — Uber’s team changed status to Duplicated

0×05 — Possible to View Driver Waybill via Driver UUID

Using the previous vulnerability we were able to test a new functionality called waybill. By crafting the request that the app sends, we notice that it has a broken access control vulnerability that allowed us to see the last trip from every driver, by only knowing his uuid.

To get a driver UUID you can, for example, request a random car, let the driver accept the trip and after this you cancel it. In the meanwhile you are able to capture the driver UUID.

In the response of this request, we were able to get the driver name, license plate, last tripUUID, last passenger name, number of passengers, the origin and destination of the trip.

Notice the TRIP # in this response? To get the full path of the trip, we ended up discovering a new functionality that returns the full path of the trip, the driver name, client name, license plate and even the car model.

This functionatility could not be detailed in this moment, but as soon as we are authorized, we will talk about it.

Press enter or click to view image in full size
DISCLOSURE TIMELINE

March 31, 2016 — Bug reported to Uber
April 1, 2016 — Uber’s team changed status to Triaged
April 13, 2016 — Uber’s team changed status to Resolved
April 18, 2016 — Uber rewarded us with a bounty.

0×06 — Information regarding trips from other users

Remember the vulnerability 0×03 where we found out that by changing the token by a UUID we could impersonate another user?

Press enter or click to view image in full size

The request above allow an user to view the trips made by himself. Notice that in the request there is any session headers or session cookies. All the **session** details are sent via GET parameters.

By changing the highlighted uuid and maintaining the original token, the server return a 403 unauthorized access. If we change the UUID and the token for the UUID of the user that you want to see the trips, we get a bunch of new information

This was the response when asking for trips by sending the same value in UUID and TOKEN fields.

Press enter or click to view image in full size

As it can be seen we were able to get the date of the trip, driver name and picture, the id and cost of the trip and the map of where he have been.

The response above only demonstrate one single trip, but the full response gives us all the trips made by the user.

DISCLOSURE TIMELINE

March 31, 2016 — Bug reported to Uber
March 31, 2016 — Uber’s team changed status to Triaged
April 5, 2016 — Uber’s team changed status to Resolved
April 13, 2016 — Uber rewarded us with a bounty.

What about profits?
DUPLICATED VULNERABILITIES

Open Redirect in trip.uber.com

Open Redirect in riders.uber.com

Possibility to enumerate users via getrush.uber.com and bruteforce login via iOS app to get a valid account

Possibility to download beta app as admin (Riders app IOS)

Use Partner/Driver App Without Being Activated

Enumerating userIDs with phone numbers06/04/2016

TRIAGED/CLOSED VULNERABILITIES

Possibility to brute force invite codes in riders.uber.com — 5000$

Possible to View Driver Waybill via Driver UUID — 3000$

Possibility to get private email using UUID — 5000$

Information regarding trips from other users — 5000$

And more to be disclosed…

Conclusion

This was our first bug bounty program that we really dedicated some time, and we think it had a positive outcome. At the beginning we weren’t too confident with this program because a lot of people had already tested Uber in the private program, but after some time and when we started to find some good vulnerabilities it gave us the drive to continue and see where it could lead us.

For the people who are starting the bug bounty programs, our advice is: never give up or be afraid if it is a big company, just have fun and try to learn as much as possible along the way and in time the profits will come.

As a final note to our article, we want to say that Uber should provide testing accounts to bug hunters. During our tests we did have our accounts being locked due to the nature of our tests and to unlock them, it was a bit of a nightmare. At that moment we tried to talk with Uber support team and they didn’t helped much, so the only thing to do was to try to talk with the security team directly. In this case we have to say that they did help, and much! (A big thank you to all of them).

With this being said, we think that Uber has one of the best bug bounty programs, with great payouts.

From a pentester’s view, the security team takes this program very seriously by trying to resolve all the issues as fast as they can.

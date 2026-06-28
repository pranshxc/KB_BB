---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-31_never-give-up-story-of-hacking-dutch-government-and-earning-that-dutch-swag.md
original_filename: 2021-10-31_never-give-up-story-of-hacking-dutch-government-and-earning-that-dutch-swag.md
title: Never Give Up — Story of Hacking Dutch Government and Earning that Dutch Swag.
category: documents
detected_topics:
- access-control
- idor
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- idor
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6c0012e51fbb13d706e89771e82e2c7630c23edc7b25a81ddb51a56070657ff2
text_sha256: ebe6af22fe5249991818f65b50fd7020ec0589182290e8c56ee989ccc589e286
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Never Give Up — Story of Hacking Dutch Government and Earning that Dutch Swag.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-31_never-give-up-story-of-hacking-dutch-government-and-earning-that-dutch-swag.md
- Source Type: markdown
- Detected Topics: access-control, idor, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `6c0012e51fbb13d706e89771e82e2c7630c23edc7b25a81ddb51a56070657ff2`
- Text SHA256: `ebe6af22fe5249991818f65b50fd7020ec0589182290e8c56ee989ccc589e286`


## Content

---
title: "Never Give Up — Story of Hacking Dutch Government and Earning that Dutch Swag."
url: "https://medium.com/@bababounty99/never-give-up-story-of-hacking-dutch-government-and-earning-that-swag-b518cca81c78"
authors: ["BabaBounty (@Rohan96867358)"]
programs: ["Dutch Government"]
bugs: ["IDOR"]
publication_date: "2021-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3200
scraped_via: "browseros"
---

# Never Give Up — Story of Hacking Dutch Government and Earning that Dutch Swag.

Never Give Up — Story of Hacking Dutch Government and Earning that Dutch Swag.
BabaBounty
Follow
3 min read
·
Oct 31, 2021

200

Hmm!! Dutch Swag!! Who Wants it ?Almost everybody wants it. It was one of my goals to earn Dutch Swag. I started this journey almost 6 to 7 months back. So the first most important thing was to find the domains and subdomains, as much as possible and then My first approach was always XSS and other Low hanging bugs. I tried a lot to find Xss and also reported it but that was not enough to get the swag because it used to get duplicate or low impact XSS.

So out of Frustration , I left trying on Dutch gov websites but soon I came back with a goal and a positive attitude and decided not to go for XSS. So while recon , I found one dutch gov website , wherein , it was a portal where a user can add some data in his account to a field called “Endpoint” which was later used for certificate validation.

So I Created one account and tried adding data in that field and observed that the “Endpoint data” was only viewed by me and no other user could view and delete it , As it was my account’s data.

Next thing I tried deleting the data and while observing the request , one interesting thing I found was that my data was recognized by an “organization ID” parameter by the application.

Quickly I created another account and tried adding data in the second account too and observed the request , So one thing was clear to me that if any user adds any data in that “Endpoint” Field , Application assigns a particular ID to that added data.

So while deleting the data , one important thing I observed was that the “ID value” was sequential .

Press enter or click to view image in full size

So the Attack scenario was :-

After reading till this point , You must be knowing now to which attack I am heading to 🤪

Steps :-

Get BabaBounty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1 — Create two accounts , add the data in the “ Manage endpoints” tabs of both the accounts .

2 — Tried deleting the data of any one account and captured the request in a proxy tool. The application was recognizing data with an ID parameter , As my captured data ID was “109” , So I changed it to “110”.

3 — Next thing , I observed that my another account’s “Endpoint Data” got deleted due to Improper access control ( IDOR attack ) .

And that is how I was able to do Broken Access Control attack

🔥 IDOR — Resulting in deleting other user’s data. 🔥

Quickly I reported the finding , in few days got this reply ☺️

Then for getting the swag was a long wait of three months but totally worth it 😍

Press enter or click to view image in full size
Press enter or click to view image in full size

Always Read Write Ups , Keep Changing your approach and Never Give Up. ✌️

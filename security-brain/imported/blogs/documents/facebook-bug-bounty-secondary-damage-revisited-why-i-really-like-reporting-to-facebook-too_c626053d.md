---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-10-30_facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-fa.md
original_filename: 2014-10-30_facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-fa.md
title: 'Facebook Bug Bounty: secondary damage (revisited) why I really like reporting
  to Facebook too :)'
category: documents
detected_topics:
- api-security
- oauth
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- api-security
- oauth
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: c626053d095a20f1ffcc7f93e59a54707a4e8ff9b84adc8e9358028da5127f02
text_sha256: 62e6c13ac4a0c09b8f1e2c9020710d9b886eabc5637fb517d850e2c04a237dbd
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug Bounty: secondary damage (revisited) why I really like reporting to Facebook too :)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-10-30_facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-fa.md
- Source Type: markdown
- Detected Topics: api-security, oauth, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c626053d095a20f1ffcc7f93e59a54707a4e8ff9b84adc8e9358028da5127f02`
- Text SHA256: `62e6c13ac4a0c09b8f1e2c9020710d9b886eabc5637fb517d850e2c04a237dbd`


## Content

---
title: "Facebook Bug Bounty: secondary damage (revisited) why I really like reporting to Facebook too :)"
page_title: "Facebook Bug Bounty: secondary damage (revisited) why I really like reporting to Facebook too :) - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-facebook-too/"
final_url: "https://philippeharewood.com/facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-facebook-too/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2014-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6362
---

Posted on [October 30, 2014](https://philippeharewood.com/facebook-bug-bounty-secondary-damage-revisited-why-i-really-like-reporting-to-facebook-too/)

# Facebook Bug Bounty: secondary damage (revisited) why I really like reporting to Facebook too :)

If you read Josip Franjković blog, you’d remember this report <http://josipfranjkovic.blogspot.com/2013/11/facebook-bug-bounty-secondary-damage.html>. Turns out this isn’t just a one hit wonder. Reports that lead to bugs can in fact be more valuable than initially expected.

When I was digging into Ads endpoints for a [double bounty](https://www.facebook.com/notes/protect-the-graph/doubling-up-on-ads-code-bounties/1519314984975314), I came across some inconsistencies in the Facebook Ads API documentation.

**Description**

According to the ad level limits here <https://developers.facebook.com/docs/reference/ads-api/access#limits>, a developer Ads API should not have access to Business Manager API calls.

This does not seem to be true, as I am able to inspect the business ID for my account as well as execute Business changes such as modifying the vertical, thus not obeying the limit imposed for my level.

**Proof of Concept**

ID: 458290410972131 Name: NotLeepingTest

Execute a call to a business ID (1506156432945949)

`HTTP GET /1506156432945949`

Response

`{"error": {  
"message": "(#294) Managing advertisements requires the extended permission ads_management and an application that is whitelisted to access the Ads API",  
"type": "OAuthException",  
"code": 294}}`

An error is returned as I expect from the limit described at <https://developers.facebook.com/docs/reference/ads-api/access#limits> but not the error I thought would be presented, seeing that this ID is associated with the business not Ads.

Trying for an application with `ads_management` permission, basically I am just pleasing the error message at this point

ID: 269335163238875 Name: AnyLeepingTest

Execute a call to the same business ID

`HTTP GET /1506156432945949`

Response

`{"id": "1506156432945949", "name": "00Agency"}`

Here I would expect an error message stating that I am only at Developer Level access when I need at least Standard Level access. It can be said that maybe Developer Level allows read access (which isn’t explicitly stated in the docs) and that’s why I’m able to access it.

So, let’s try a write call, specifically one from <https://developers.facebook.com/docs/reference/ads-api/businessmanager>. I am going to change the vertical of my business to RETAIL from ADVERTISING

described in the docs as

`curl  
-F "vertical=RETAIL"  
-F "access_token=<ACCESS_TOKEN>"  
"https://graph.facebook.com/<business_id>"`

So for my app and business

`curl  
-F "vertical=RETAIL"  
-F "access_token=ACCESS_TOKEN"  
"https://graph.facebook.com/1506156432945949"`

The response is just the ID of the business (which is probably not a good indicator of success/failure)

Checking the new properties with a GET call to

`/1506156432945949?fields=vertical,vertical_id`

`{"vertical": "RETAIL", "vertical_id": 14, "id": "1506156432945949"}`

Notice the new vertical is indeed RETAIL and the vertical ID has changed from 1 (ADVERTISING) to 14 (RETAIL).

Thus from this POC, I am able to use the Business Manager API while only at developer level access when here <https://developers.facebook.com/docs/reference/ads-api/access#limits> explicitly states that I should not be able to this for Development and Basic level.

**Facebook’s First Response**

> Hi Philippe, Interesting. I’ll follow up with our Business Manager team about the behavior you’re describing here: it sounds like they may have wanted to be more restrictive about who is able to use their APIs. I’ll let you know when I hear back from them. 🙂 Good so far,

**Facebook’s Second Response**

> Hi Philippe, Docs have been updated to reflect when access is actually allowed 🙂 That being said, I dug in to these APIs a bit more and found some areas of concern. The team is working on fixing those up. Normally just a documentation change wouldn’t be enough for a bounty, but these additional issues should qualify. I’ll be in touch once they’re closer to being fixed. Yup, a documentation change to clarify access. I’m very gracious at the generosity here.

**Facebook’s Explanation**

> Hi Philippe, There are a few Business Manager API endpoints which are accessible to more applications than they should be. The team is in the process of locking them down. 🙂 I’m sure if I sat down comparing applications for access I might have reached one of these, but I’m guessing it sure would have been a long trial and error process.

So as Josip stated before, Thanks to the Facebook Security Team in the manner in which they carry out the bug bounty program. Very sincere and welcoming program.

Happy Hunting!

**Timeline**

  * Oct 30, 2014 at 6:50 AM – Report sent 
  * Nov 5, 2014 at 2:02 AM – First Response from Facebook 
  * Nov 21, 2014 at 4:02 PM – Second response from Facebook 
  * Dec 30, 2014 at 3:07 PM – Bounty awarded by Facebook 
  * Jan 9, 2015 at 3:19 PM – Clarification from Facebook about the actual bug

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-23_how-i-hacked-scopely-with-sign-in-with-google.md
original_filename: 2023-01-23_how-i-hacked-scopely-with-sign-in-with-google.md
title: How i Hacked Scopely with “Sign in with Google”
category: documents
detected_topics:
- oauth
- command-injection
- path-traversal
- otp
- cors
- api-security
tags:
- imported
- documents
- oauth
- command-injection
- path-traversal
- otp
- cors
- api-security
language: en
raw_sha256: 4d8dd406de5a35a15d1bcad51a5481ab21b12f216f7de8af07a2b08b6dcf2533
text_sha256: 573f448c20381a6efb1de68972f12d41b8356cc47015a34c3da5edc156e2feb1
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How i Hacked Scopely with “Sign in with Google”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-23_how-i-hacked-scopely-with-sign-in-with-google.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, path-traversal, otp, cors, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `4d8dd406de5a35a15d1bcad51a5481ab21b12f216f7de8af07a2b08b6dcf2533`
- Text SHA256: `573f448c20381a6efb1de68972f12d41b8356cc47015a34c3da5edc156e2feb1`


## Content

---
title: "How i Hacked Scopely with “Sign in with Google”"
url: "https://ph-hitachi.medium.com/how-i-hacked-scopely-using-sign-in-with-google-298a9c166ad"
authors: ["Ph.Hitachi"]
programs: ["Scopely"]
bugs: ["Account takeover", "CORS misconfiguration", "Client-side enforcement of server-side security", "OAuth"]
publication_date: "2023-01-23"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1635
scraped_via: "browseros"
---

# How i Hacked Scopely with “Sign in with Google”

Ph.Hitachi
 highlighted

How i Hacked Scopely with “Sign in with Google”
Ph.Hitachi
Follow
6 min read
·
Jan 23, 2023

151

1

Hi guys,

so i’m here again to share you a new knowledge and amazing writes up with other interesting vulnerability i found in the program on HackerOne .

it’s been a year since my last writes up and doing Bug Bounty Hunting since i already have work im busy doing with my Jobs, Thanks to Bug bounty i got stable job with a young age, and it helps me to fully understand the flow of the system and how things works.

So let’s start…

as i mentioned im busy with my work and not doing hunting for a long time but on Oct 30, 2021 it’s Saturday so basically i don’t have work on that day, but i miss doing something… so im scrolling on the social media platform and i see a post about bug bounty so it cross to my mind why i will try to do bug bounty again?

so i start visiting hackerone website again after a long time and finding a target so as bug bounty hunter my instinct work like spider-man so i chose the correct tartget for my testing, i only chose one program and that is Scopely so after that i read the Policy & Scopes so my spider-man instinct are activated and i picked the domain scope that i want to penetrate, it not like penetration in your on mid its “Web pentesting”.

Note: Choosing the correct target is important, its not about bugs it’s about the target… the bug is only a bonus…

so first i test the authentecation flow of the system, thats part of my methology i don’t skip authentecation flow when im doing pentesting…

The system have no registration its only a Login, but the system use Google oauth2

so i try to to login “Sign in with Google”

and its look normal, like other website so i tried to logout my account and its also normal.

So i started reviewing the source code…, btw I’m Web Developer so it’s easy to me to read a code. So Lets do this!!

Press enter or click to view image in full size

So when i look on the soure code, There’s have a 2 file gets my attention, the [AuthService.js, TeamworkApi.js]

First i look on the AuthService.js and i found something interesting here,
The loginWithGoogle function is use only window.location to get the google access token.

so again my spider-man instinct are activated again i felt something went wrong on the loginWithGoogle, so lets analyze it.

Press enter or click to view image in full size
AuthService.js

The login function generate a universal unique identifier (UUIDv4) as preregId, its use basically as ID of users.

But what their doing on loginWithGoogle function and also use to finishLogin function?

btw, What finishLogin function do? so the finishLogin is getting preregId and returning AuthToken? i felt very special here…

Let’s read more code.

TeamworkApi.js

Wait…. What!?? they are getting authToken from “/user/fullfilledAuthToken/{prepregId}”. ???

so what’s the problem here?

The problem here, is the auth Flow is f*ck!! the preregId is client side generated not back-end/server-side, when you look at AuthService.js on line 32. where preregId are generated on the client Side…

Means, You can generate your own custom preregId to get your authToken on that endpoint and they can’t validate the preregId they can only validate the format of UUIDv4 (if they impliment it), They can only validate the UUIDv4 if it already existing on the database but in this case this is client-side generated !!!

SO when you send a request to “/user/preregister” endpoint you can get your authToken in “/user/fullfilledAuthToken/{prepregId}”

Example:

POST /user/preregister 
{preregistrationId: 'xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx'}

you can get your authToken in this endpoint:

GET /user/fullfilledAuthToken/xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx 

Response:

{
  authToken: 'access_token',
  ...
}

Now, How can we identify who is the user behind the preregId (xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx) if this only client side generated? and there’s no credentials?

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s deep dive more here…

Ok.. Now we know the flow of the login so ok let’s focus on that how can you exploit that.. let’s start using burp suite to capture all request 1 by 1

Press enter or click to view image in full size

So confirm!!! you can enter our own custom UUIDv4 so the UUIDv4 is now already exist on their database so whats next?

Press enter or click to view image in full size

So after you registered the custom UUIDv4 as preregId they passing it to Google oauth2 end point.

in the response it will redirecting to:

https://teamwork.games.scopely.io/api/googlelogin?state=/_xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx&code=[access_token]&scope=profile+https://www.googleapis.com/auth/userinfo.profile

So this is how they identify who is the users who owned the preregId,
This is how they verified the UUIDv4 that we insert in preregistration and how they identified which user is attempting to login using code from google..

The code returning from google is also a access_token, so it should be your access token of your account’s

so basically in the state they are returning xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx (preregId) and code parammeter (access_token)

as you can see they returning preregId in the scope and also returning the code from google.

so the proccess is when you login with xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx (preregId) using your gmail account so means when you go to the “/user/fullfilledAuthToken/xxxxxxxx-xxxx-4xxx-xxxx-xxxxxxxxxxxx” endpoint the authToken you get from that response is from the gmail account that you login.

Press enter or click to view image in full size

When we look at code snips of the loginWithGoogle, we can see that they are passing fromPath & preregId.

so we can hacked the victim by sending a link like this:

https://accounts.google.com/o/oauth2/v2/auth?client_id=145493605239-49vt1voervjoekkbh88nck1dja8cq6fk.apps.googleusercontent.com&scope=profile&response_type=code&state=/_[preregid]&redirect_uri=https://teamwork.games.scopely.io/api/googlelogin

so if the victim click the link, if he have already account and their gmail account is loged-in in the thier browser, You can force the victim to login-in their account’s via visiting the link.

Let’s make more research about this.

Press enter or click to view image in full size
I test for open redirect

So i test the open redirect from fromPath.

‘fromPath’ is a path where user’s redirect after they successfully login.

Press enter or click to view image in full size
By adding double slashes we can exploit open redirect in fromPath parametter

Note: when the preregId is already used you can’t use it again, so i make a lot of test on this.

So after i test open redirect i check my burp collaborator client and i’m surprise in the result.

Press enter or click to view image in full size

we can leaked the access token from gmail account in the Referer headers!!!

So means we can hack the google account that used to sign-in to the scopely

We are one more step to make more impact and automate on this…

Press enter or click to view image in full size
since the data get from api i check the CORS Misconfiguration….

Another vulnerable confirm again, Let’s combine all vulnerability we found on this to make huge impact!!

so i created simple script:

Press enter or click to view image in full size
Triaged
Press enter or click to view image in full size
Closed as informative

Contact:
Email: ph-hitachi@wearehackerone.com
Twitter: https://x.com/PhHitachi
LinkedIn: www.linkedin.com/in/phhitachi

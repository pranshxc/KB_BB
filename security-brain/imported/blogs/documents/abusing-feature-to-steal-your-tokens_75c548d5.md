---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-17_abusing-feature-to-steal-your-tokens.md
original_filename: 2019-12-17_abusing-feature-to-steal-your-tokens.md
title: Abusing feature to steal your tokens
category: documents
detected_topics:
- oauth
- jwt
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- oauth
- jwt
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: 75c548d5daf91cd04137946e695d4fc004972d1f1292c49bfd8d47478d56ba3d
text_sha256: 41d027387eb65ae8fb74f053db5601f38535113008b8b9951831dfdebbe3cfe0
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing feature to steal your tokens

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-17_abusing-feature-to-steal-your-tokens.md
- Source Type: markdown
- Detected Topics: oauth, jwt, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `75c548d5daf91cd04137946e695d4fc004972d1f1292c49bfd8d47478d56ba3d`
- Text SHA256: `41d027387eb65ae8fb74f053db5601f38535113008b8b9951831dfdebbe3cfe0`


## Content

---
title: "Abusing feature to steal your tokens"
url: "https://medium.com/@rootxharsh_90844/abusing-feature-to-steal-your-tokens-f15f78cebf74"
authors: ["Harsh Jaiswal (@rootxharsh)"]
bugs: ["OAuth"]
bounty: "3,750"
publication_date: "2019-12-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4882
scraped_via: "browseros"
---

# Abusing feature to steal your tokens

Abusing feature to steal your tokens
Harsh Jaiswal
Follow
6 min read
·
Dec 17, 2019

540

2

In mid-2018, Linode private Hackerone program got me engaged because of how well the program was getting managed. I found quite of issues there which are privately disclosed on Hackerone, These two issues were particularly interesting so I wanted to do a public disclosure. So let's not waste more time and get started :) This bug will involve a bit of OAuth understanding so I hope you guys are familiar with it. I find the second one more interesting.

Linode is a VPS provider as you may already know, They provide this feature where your VPS will resolve to <id>.members.linode.com, Just looking at this and I knew we could abuse this one way or another. This basically means we fully control the subdomain of Linode.com that is even executing server-side scripting language on a Linode’s subdomain.

Diving down Linode’s Authentication

Linode has 4 web apps for users;

https://manager.linode.com Classic/Old Linode Manager

https://linode.com/community Community portal

https://login.linode.com OAuth issuing server

https://cloud.linode.com New Linode manager

As we fully control the subdomain, We could read any cookie set to .linode.com (Cookies set to wildcard domain), I started checking https://manager.linode.com for session/CSRF cookie, But all cookies were set properly to only manager.linode.com , Then I moved to another app i.e. https://linode.com/community which does a lot of OAuth things via `login.linode.com`.

Let's understand how does the authentication work here.

On clicking Login A GET request is made to https://www.linode.com/community/questions/login?next=/community/ following is the response of the request.

Press enter or click to view image in full size
HTTP/1.1 302 Found
Server: nginx
Date: Sat, 29 Sep 2018 23:36:51 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: close
Vary: Cookie
Location: https://login.linode.com/oauth/authorize?scopes=events%3Amodify&state=bce45f7c-6a37-46c7-9ede-c9979c152081&client_id=a38f156de7fa9819c110&redirect_uri=https%3A%2F%2Fwww.linode.com%2Fcommunity%2F&response_type=code
Set-Cookie: sessionid=dgagljcsrcg0m3klfd2o16x9q1smbgvd; Domain=.linode.com; expires=Sat, 13-Oct-2018 23:36:51 GMT; HttpOnly; Max-Age=1209600; Path=/; Secure
.....

Which does the following,

Sets cookie :

sessionid=dgagljcsrcg0m3klfd2o16x9q1smbgvd; which is linked to a state token state=bce45f7c-6a37-46c7-9ede-c9979c152081. The cookie is set to .linode.com

Redirect to OAuth page :

https://login.linode.com/oauth/authorize?scopes=events%3Amodify&state=bce45f7c-6a37-46c7-9ede-c9979c152081&client_id=a38f156de7fa9819c110&redirect_uri=https%3A%2F%2Fwww.linode.com%2Fcommunity%2F&response_type=code

If logged in on https://login.linode.com/ The user gets redirected to

https://www.linode.com/community/?state=bce45f7c-6a37-46c7-9ede-c9979c152081&code=6f422a104f5bf039f9dc

The state parameter token is cross-checked against the earlier set sessionid, If the verification succeeds, We get this response.

HTTP/1.1 302 Found
Server: nginx
Date: Sat, 29 Sep 2018 23:04:02 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 0
Connection: close
Vary: Cookie
Location: /community/
Set-Cookie: sessionid=qaff7xdtoxxhnc6tds7ym2d7d9lpweci; Domain=.linode.com; expires=Sat, 13-Oct-2018 23:04:02 GMT; HttpOnly; Max-Age=1209600; Path=/; Secure
....

Which does the following

sessionid gets reset (again to .linode.com) which is an actual session for community portal and the user gets logged in into community portal.
Exploiting… OAuth + Cookies = ❤

Our first goal is that we want wildcard (* ) scope access token from the community portal. if we want the user to login to the community portal with * scope access token we need to bypass the CSRF mechanism. the login mechanism looks for sessionid and cross-verify it against the given state token.
because we can also set .linode.com cookies we can bypass this :)

Here’s the hacky PHP code to do this.

Exploit begins

The above code simply iframes setcookie.php and then after 6 seconds iframe’s stc.php (stealcookie.php)

Let's understand what setcookie.php

Sets required cookies to exploit and starts login flow with * scope
Makes a request from server-side to login endpoint to get valid cookies
Extract all headers from the response
Modify Location Header, The location header consists the scopes=events%3amodify we simply change scopes=*
Extract Set-Cookie header, This consists of sessionid which is linked to the state token in theLocation header.
Sets the extracted session into the user's session & continue with the redirection to the location header but with our modified values to the scope parameter.

Now because sessionid & state will verify successfully, User will be logged into the community portal with `*` scope access token.

Now the user is all set to get his/her token stolen, Because Linode will set the legitimate session to .linode.com using sessionid and because of its set to `.linode.com` we can fetch the legit session and log in using it and as the access token is in the source of the page we can finally extract the token from the source. :) Let's automate this too using stc.php (stealcookies.php bellow)(which steals cookie and extracts the token)

Steals session & extracts token

We simply take sessionid from the user session and make a curl request from server-side & user some regex to get the access token which can be used to make an API call be it read or write to any resource :).

Get Harsh Jaiswal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Looks Complex?

Check out the exploit video.

Timeline for this issue

Sep 30th, 2018: Initial discovery & report

Oct 1st, 2018: Triaged

Oct 3rd, 2018: Rewarded as critical $2000

Oct 4th, 2018: Resolved

But wait, Can we exploit it somewhere else?

Let`s see how CSRF works on these applications;

All applications CSRF looked safe from this attack except https://login.linode.com

Let`s understand the CSRF Implementation here ;)

Press enter or click to view image in full size
A JWT is set within the session cookie, This cookie consists of a CSRF token. The cookie is not scoped to any domain it automatically scoped to login.linode.com by browser, So we can’t read it.
Once the user login, the user session is tied to the newsession cookie however the CSRF token remains not changed (CSRF fixation FTW!).
We can set this cookie from our controlled VPS to with HTTOnly flag (cookie preference), however, I guess it depends on browser & server which cookie gets the preference?

In my case, my set cookie was getting read by the server first and hence discarded user’s working session and asked the user to log in again, However even if it didn’t the cookie set by Linode is at Path=/, We could add Path=/login to get preference for our cookie, Now any path resides under /login/* will get our cookie as preference on required endpoints I guess. I’m not sure though, Here are some slides from filedescriptor ‘s talk from HITCON 2019 which explains this kind of attacks in detail. Definitely go through these slides, Awesome stuff!.

Press enter or click to view image in full size
Press enter or click to view image in full size
Exploiting... Oh! I ❤ OAuth, And these cookies are making it more awesome xD

Linode is an OAuth provider and all authorization is done on login.linode.com (its the OAuth issuing server) as mentioned earlier. So the idea is to force the user to authorize our client application with wildcard scope.

Bellow is the hacky PHP code to exploit this OAuth CRSF.

Make a request from server-side and get a session JWT.
Decode it and extract the CSRF token
Set the session cookie with the acquired JWT.
Make a POST request to authorize the attacker’s OAuth application with earlier decoded CSRF token.
Press enter or click to view image in full size
A breakdown from Linode team

Looks complex? Here’s a video PoC of the exploit

Timeline for this issue

13th Oct 2018: Initial discovery & report

15th Oct 2018: Triaged

18th Oct 2018: Rewarded as High $750 because of interaction but added a nice bonus of $1000 for a creative attack.

14th Nov 2018: Resolved by rotating CSRF token after login.

Reference

https://speakerdeck.com/filedescriptor/the-cookie-monster-in-your-browsers

https://github.blog/2013-04-09-yummy-cookies-across-domains/

That's it, folks, Thanks for reading and making till here. These issues might be confusing for some of you, If so please DM me at https://twitter.com/rootxharsh and I will try my best to help you understand, Until the next time :)

Thanks to the Linode team for allowing this disclosure.

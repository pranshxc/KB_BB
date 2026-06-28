---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-19_from-staging-to-0-click-account-takeover.md
original_filename: 2021-10-19_from-staging-to-0-click-account-takeover.md
title: From staging to 0 click account takeover
category: documents
detected_topics:
- oauth
- jwt
- idor
- sqli
- command-injection
- rate-limit
tags:
- imported
- documents
- oauth
- jwt
- idor
- sqli
- command-injection
- rate-limit
language: en
raw_sha256: f4b4a80fbe976deb1c1c66a5596d9584feb91cdeeec965547037febe769c4aad
text_sha256: 6582c1df59aba5ea7eaa841175db3cd1b7ea8058405b659ef8880d145b2af2fd
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# From staging to 0 click account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-19_from-staging-to-0-click-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, jwt, idor, sqli, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `f4b4a80fbe976deb1c1c66a5596d9584feb91cdeeec965547037febe769c4aad`
- Text SHA256: `6582c1df59aba5ea7eaa841175db3cd1b7ea8058405b659ef8880d145b2af2fd`


## Content

---
title: "From staging to 0 click account takeover"
url: "https://med-mahmoudi26.medium.com/from-staging-to-0-click-account-takeover-528a5ecaa3eb"
authors: ["mohamad mahmoudi (@Lotus_619)"]
programs: ["Pinterest"]
bugs: ["Account takeover", "Logic flaw"]
publication_date: "2021-10-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3229
scraped_via: "browseros"
---

# From staging to 0 click account takeover

From staging to 0 click account takeover
mohamad mahmoudi
Follow
2 min read
·
Oct 20, 2021

79

Often, as bug bounty hunters or pentesters, while doing our recon on a specific target, we come accross their staging or pre-production environments. And if we look at these from the right angle, hidden gems could be waiting for us.

I was hunting on a private bug bounty program with a wild scope, let’s call it *.akme.com for obvious reasons. I started with subdomain enumeration when 3 subs caught my attention:

dashboard.akme.com
dashboard-staging.akme.com
forms.akme.com
api.akme.com

After few hours clicking around, I took the following notes:

dashboard-staging.akme.com is the staging version of dashboard.akme.com(did not take much thinking)
You can create an account on both of them, most importantly with the same email(this will come in handy)
An account gets created for you automatically on forms.akme.com when you signup on dashboard app and you can login to it by hitting this endpoint with your jwt session: api.akme.com/oauth

4. You don’t need to confirm your email on dashboard.acme.com to login to forms.akme.com through oauth

Get mohamad mahmoudi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Looking at these notes, I thought about the following scenario:

Create an account A in dashboard
Create an account B in staging-dashboard
Login to forms with account A, by hitting the oauth endpoint with my user session
Login to forms with account B(same process as 3).

The desired outcome was making account B login to account’s A forms account without knowing his password. It did not work at first try, instead took me to forms-staging which is the staging version of forms app. FAIL!

Try harder:

Looking at my burp history, I found that there is a parameter that gets added to the oauth request each time. Which, if you are logging from dashboard, becomes :

api.akme.com/oauth?referer=dashboard

And if you are logging from dashboard-staging:

api.akme.com/oauth?referer=staging-dashboard

So I tried intercepting the traffic while doing the same steps(account A is vicitm account B is attacker) but changing the value of the ?referer to dashboard while using my staging jwt session(user B). And guess what ! I got redirected to our victim’s account.

This exploit was possible for two reasons:

The developers used the same jwt secret to decode the session of the users. This allowed me to access the account of anyone on forms.akme.com by knowing their email.
You don’t need email confirmation to login with oauth, otherwise if you were not to prove that the victim’s email belongs to you, you wouldn’t be able to fully signup on dahsboard-staging with is the main vector of the attack

Worst part is I found another way to mass leak emails of other users, not an sql injection, maybe we’ll leave it for another article.

Hope this was a good read !

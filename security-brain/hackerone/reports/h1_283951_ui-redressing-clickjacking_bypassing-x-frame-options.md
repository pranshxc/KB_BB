---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '283951'
original_report_id: '283951'
title: Bypassing X-frame options
weakness: UI Redressing (Clickjacking)
team_handle: gratipay
created_at: '2017-10-29T14:12:14.818Z'
disclosed_at: '2017-10-29T21:18:27.161Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: https://gratipay.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Bypassing X-frame options

## Metadata

- HackerOne Report ID: 283951
- Weakness: UI Redressing (Clickjacking)
- Program: gratipay
- Disclosed At: 2017-10-29T21:18:27.161Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

bypass X-Frame-Options ( Proxy protection NOT used )

DomainUsing: gratipay.com

Proxy protection NOT used , i can bypass X-Frame-Options header and recreate clickjacking on the whole domain.
I see that you don't have a reverse proxy protection this allows all users to proxy your website rather than iframe it. They use use it for

    Phishing
    Tricking First-time gratipay users that (fake website) is original website.
    Debug gratipay.com (see all request an response make on fake website)

Exploit

I will create a fake website which closely matches your domain or any other confusing domain.
I will post on many forums that "gratipay.com is best" etc. with my fake website link (better to use URl shortner!)
He will visit here and signup
As I have made that proxy, I can see all request made on them thus , Passwords Also!
I will hack him.
NOTE: When he clicks on confirmation link in his email , He is redirected to ORIGNAL website but I will get his password and username and I would login with the username and password i have , on original website.

How Facebook Handles it (Amazing Protection): http://i.gyazo.com/1ca03e64dac455f24d0ac1c4a59218e4.png ( https://translate.google.com/translate?hl=en&sl=auto&tl=zu&u=https://facebook.com

How your webiste handles it :( -> https://translate.googleusercontent.com/translate_c?depth=1&hl=en&rurl=translate.google.com&sl=en&sp=nmt4&tl=af&u=https://gratipay.com
AN attacker can remove the Translate interface to make the webiste look real.

POC URL: https://translate.googleusercontent.com/translate_c?depth=1&hl=en&rurl=translate.google.com&sl=en&sp=nmt4&tl=af&u=https://gratipay.com
try submitting real login data (of test account) You'll get logged in!

FIX

Here is the code that I use for stopping 100% of these types of sites:


RewriteEngine on
RewriteCond %{HTTP:VIA} !^$ [OR]
RewriteCond %{HTTP:FORWARDED} !^$ [OR]
RewriteCond %{HTTP:USERAGENT_VIA} !^$ [OR]
RewriteCond %{HTTP:X_FORWARDED_FOR} !^$ [OR]
RewriteCond %{HTTP:PROXY_CONNECTION} !^$ [OR]
RewriteCond %{HTTP:XPROXY_CONNECTION} !^$ [OR]
RewriteCond %{HTTP:HTTP_PC_REMOTE_ADDR} !^$ [OR]
RewriteCond %{HTTP:HTTP_CLIENT_IP} !^$
RewriteRule ^(.*)$ - [F]

To use this code, copy & paste into your site's root .htaccess file. Upload to your server, and test its effectiveness ! It is perfect and compared to blacklisting a million sites of this kind, itâs lightweight, concise, and very effective.

Please let me know if want more information.

Thank you!

Regards:
Hafsa Mirza
Ethical Hacker
Cyber Security Researcher

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

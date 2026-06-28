---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-12_finding-keys-under-the-door.md
original_filename: 2021-03-12_finding-keys-under-the-door.md
title: Finding keys under the door
category: documents
detected_topics:
- xss
- command-injection
- idor
- file-upload
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- command-injection
- idor
- file-upload
- rate-limit
- api-security
language: en
raw_sha256: 9d01a9ed6bc5a5e975396d0184b9d9ce50a9ce9ec51feb50a2c22555abcadaeb
text_sha256: b6256bcbf5e16710579f501b16b2a8110981fcb123dc9b282f1145c07bb42c88
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Finding keys under the door

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-12_finding-keys-under-the-door.md
- Source Type: markdown
- Detected Topics: xss, command-injection, idor, file-upload, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `9d01a9ed6bc5a5e975396d0184b9d9ce50a9ce9ec51feb50a2c22555abcadaeb`
- Text SHA256: `b6256bcbf5e16710579f501b16b2a8110981fcb123dc9b282f1145c07bb42c88`


## Content

---
title: "Finding keys under the door"
page_title: "Finding Keys Under The Door. A login page with usernames and… | by Naveen Prakaasham K S V | System Weakness"
url: "https://naveenprakaasam.medium.com/finding-keys-under-the-door-5cea8758ce86"
authors: ["Naveen Prakaasham K S V"]
programs: ["Paytm"]
bugs: ["Stored XSS", "Unrestricted file upload"]
publication_date: "2021-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3821
scraped_via: "browseros"
---

# Finding keys under the door

Finding Keys Under The Door
A login page with usernames and passwords mentioned on itself leads to an unrestricted file upload and a Stored XSS
Naveen Prakaasham K S V
Follow
4 min read
·
Mar 12, 2021

186

Press enter or click to view image in full size
https://www.freepik.com/photos/background Background photo created by mrsiraphol — www.freepik.com

Hi everyone, I am Naveen Prakaasham, a bug bounty hunter and I am going to talk about one of the highest severity bugs I’ve found. This bug I found was on a domain owned by Paytm. You can see their bug bounty program here.

Initial recon and first finding

So I began recon on one of the domains mentioned in the scope of the program.

Subdomain enumeration -> Looking for subdomains that are online -> Aquatone -> Looking manually at the report generated. (Just the usual stuff)

(For more information about recon, read this https://twitter.com/Jhaddix/status/1289258603329675264?s=20)

Then I came across an interesting subdomain. The subdomain had a login page and below that it had two usernames and passwords and it was also auto-filled with the credentials. It looked something like this.

Press enter or click to view image in full size
Vue Element Admin Login page

I was shocked to see the username and password on the login page itself. I clicked on the login button and it was logged into the dashboard. But the dashboard itself didn’t seem very promising. It was just the default dashboard and at first glance, it didn’t seem like there was anything more interesting. So I just reported what I found till now to Paytm.

Digging deeper and the second find

Paytm Security Team got back to me and asked if I was able to find any sensitive information or was able to perform any action that could cause security impact in the dashboard.

Get Naveen Prakaasham K S V’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I started looking up the framework that the website was using — “Vue Element Admin”. You can see the GitHub pages and documentation here.

PanJiaChen/vue-element-admin
SPONSORED BY vue-element-admin is a production-ready front-end solution for admin interfaces. It is based on vue and…

github.com

vue-element-admin
Typical templates for enterprise applications and various components Reasonable framework choice, good engineering…

panjiachen.github.io

There was also a test site for the framework https://panjiachen.github.io/vue-element-admin/

Looking at the test site, I noticed that, if not fully configured, this framework has the username and password in the login page itself. I logged into the test site and was looking around. I noticed the tabs on the left of the page with links to the other pages on the site.

Press enter or click to view image in full size

This made me think if the links like this were present in the original target also. I went back to that site and noticed that there were two more pages in addition to the Dashboard (that I had previously missed). They were named GameList and PvPList and the pages had lists of games with ID, Name, Channel, etc.

There were also options to create games or edit existing games. I tried inserting some XSS payloads in the name field but none of them worked. Then I named a file as an XSS payload and uploaded it in the ‘Game icon’ field that was present. No XSS fire here either. But this time I could see a Cloudfront URL to the image that is uploaded, displayed below the Upload button after the file is uploaded. Something like

https://random-chars.cloudfront.net/2021/01/random-random-random.png

So I could upload a file and see where the file is located. The first thing that came to mind was Unrestricted File Upload. Then I made a test HTML file and tried uploading it as the Game Icon but I couldn’t upload it and it displayed something along the lines of “Not an image”. Just when I was about to look for bypasses to this, I noticed another Upload button below.

The upload button was available to upload the game package. This upload functionality did not have any checks and I was able to upload any kind of files. It also displayed the Cloudfront URL of the uploaded file. So I reported it saying that it’s an unrestricted file upload and it could potentially lead to Remote Code Execution.

The Failed Road to RCE

Then the security team asked me to confirm if the RCE is possible. So I initially tried uploading a PHP shell and getting a code execution but the server just returned the file as an octet-stream.

The Cloudfront server was running OpenResty Lua Nginx Module so I tried uploading some files written in Lua. Those files also had the same behaviour. I tried uploading various files and basically, any file except HTML files were just returned as octet streams. The HTML files were rendered by the browser so I tried inserting JavaScript in the files and the XSS worked. So I had a stored XSS. Still, I spent a lot more hours reading articles, looking for ways to make it to RCE but no luck.

I reported this to the security team and they took some days to fix it and after the fix, they rewarded me with a good bounty.

So that’s all I have for now. Any suggestions or feedback are welcome!

Connect with me on Twitter or LinkedIn.

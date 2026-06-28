---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-10_access-to-staging-environment-via-user-agent-string.md
original_filename: 2018-10-10_access-to-staging-environment-via-user-agent-string.md
title: Access to staging environment via User-Agent string
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 228b032c13e17cbf31b4906aeb53406ba0f907b37e3ad96ca88ec0c2876d0fd8
text_sha256: 8d133b198336d2f02ffbcab0ef428ba89a1985a2677201efc9bf849e4ef70a5f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Access to staging environment via User-Agent string

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-10_access-to-staging-environment-via-user-agent-string.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `228b032c13e17cbf31b4906aeb53406ba0f907b37e3ad96ca88ec0c2876d0fd8`
- Text SHA256: `8d133b198336d2f02ffbcab0ef428ba89a1985a2677201efc9bf849e4ef70a5f`


## Content

---
title: "Access to staging environment via User-Agent string"
url: "https://medium.com/@yassergersy/access-to-staging-environment-via-user-agent-string-23470546577f"
authors: ["Yasser Gersy (@yassergersy)"]
bugs: ["Authentication bypass"]
publication_date: "2018-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5649
scraped_via: "browseros"
---

# Access to staging environment via User-Agent string

Access to staging environment via User-Agent string
Yasser Gersy
4 min read
·
Oct 10, 2018

--

Hi

This article demonstrates a Authentication bypass using special User-Agent string.

Disclosing something that helped me to access stage environment in a company which may help other people in their penetration testing.

Unfortunately the program does not allow any public disclosure , so it will be redacted. And we will call it Redigido

Like many , i do recon on everything , After downloading Redigido APk file .

Details

Collecting the program assets and found that it has an android application , I tried to use a new technique , i extracted the APK file , and using dex2jar , decompiled the dex files to Jar , finally i extracted the jar files again.

I do not know why i did that?

I ended up having a folder containing a dozens of files with disk space = 160 Mbs.

I used my own tool to fetch these files for something interesting .

The tool reads all files, split lines and looks for any string matches email / url / secret/password/key/token/access according to the default configuration.

Press enter or click to view image in full size

After the tool finished , i noticed credentials are leaked in a url.

https://developer22:password@stage.redigido.com/

Navigating to `stage.redigido.com` , the browser failed to reach . the subdomain is not resolvable .

Press enter or click to view image in full size

I got an idea, I resolved their main website ip address and edited my hosts file with the following :

Suppose x.x.x.x is one of their IP addresses

x.x.x.x  stage.ridigido.com`

Refreshing the browser , their server accepted the request.

WOW , i reached the stage but it’s protected with Basic Authentication.

Press enter or click to view image in full size

Submitting the leaked credentials , the authentication failed , i guessed that may someone found that before me and the developer had to change his password , so i tried to bruteforce the new password and Failed.

Get Yasser Gersy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried to find any thing that has no authentication , requesting /robots.txt also required basic authentication.

I picked up the request and changed the Host header to www.redigido.com, and the response was from the main website , tried the stage and failed again.

for any requested resource if the host header is equal to stage.redigido.com the server will respond with Restricted Authentication Required

have no other plans, giving up now.

i installed the apk on my machine and started using the application , i noticed that HTTP requests are using http:// What? the website is upgrading HTTP connections and it also has STS http header set , which means all HTTP requests must use HTTPS

I picked up a request and started looking why HTTP is not upgraded to HTTPS? ,After fuzzing all parts of the requests , i found The User-Agentis the key , the android application is using User-Agent string containing the company name User-Agent: Redigido.com and the server side accepts any connection containing this user-agent regardless the scheme.

Let’s spoof the user-agent , i opened firefox and edited my user-agent :

User-Agent: Redigido.com

Navigated to http://stage.redigido.com

And boom :D

Welcome Back .

Got access to stage by resolving host name and using crafted user-agent string.

Summary

Doing recon for all assets , Getting a large list of subdomains , reverse engineering android apk , Resolving offline hosts /internal host names , Comparing mobile requests with Desktop ones , Using ANdroid application user-agent to access stage .

Tips

Do recon as much as you can
Resolve unreachable Hosts manually using the ip address of the main website.
Try Accessing as Android User-Agent and different user-agents.
try to use everything you get

Good Luck

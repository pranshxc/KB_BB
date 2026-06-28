---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-05_unauthenticated-access-to-cloud-portal-a-without-.md
original_filename: 2021-11-05_unauthenticated-access-to-cloud-portal-a-without-.md
title: Unauthenticated Access To Cloud Portal — A 🚪 Without 🗝️
category: documents
detected_topics:
- api-security
- command-injection
tags:
- imported
- documents
- api-security
- command-injection
language: en
raw_sha256: 5616318506933b6cf0e89fe435512654630b77495e4e96d9b2b59422b646eb46
text_sha256: b33fd72083496325e7932ef61c498993bf388eb82b3f7db6e4cee4ac272ee966
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Access To Cloud Portal — A 🚪 Without 🗝️

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-05_unauthenticated-access-to-cloud-portal-a-without-.md
- Source Type: markdown
- Detected Topics: api-security, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `5616318506933b6cf0e89fe435512654630b77495e4e96d9b2b59422b646eb46`
- Text SHA256: `b33fd72083496325e7932ef61c498993bf388eb82b3f7db6e4cee4ac272ee966`


## Content

---
title: "Unauthenticated Access To Cloud Portal — A 🚪 Without 🗝️"
page_title: "UNAUTHENTICATED ACCESS TO CLOUD PORTAL — A 🚪 WITHOUT 🗝️ | by Yukesh Kumar [ 3th1c_yuk1 ] | Techiepedia | Medium"
url: "https://medium.com/techiepedia/unauthenticated-access-to-cloud-portal-a-without-%EF%B8%8F-9f29c387b937"
authors: ["Yukesh Kumar (@3th1c_yuk1)"]
bugs: ["Authentication bypass"]
publication_date: "2021-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3193
scraped_via: "browseros"
---

# Unauthenticated Access To Cloud Portal — A 🚪 Without 🗝️

Yukesh Kumar [ 3th1c_yuk1 ]
Follow
4 min read
·
Nov 5, 2021

115

1

UNAUTHENTICATED ACCESS TO CLOUD PORTAL — A 🚪 WITHOUT 🗝️

Everything changed to an offline mode including my exams so I don’t have time to hunt for bugs but I have a VPS which runs 24/7. I recommend you to buy one, it’s very helpful in many ways.

Hello Ethic_Hackers,

I’m Yukesh alias 3th1c_yuk1. In this blog, I’ll discuss Unauthenticated access to a cloud portal in which I can able to do many things as an admin.

I can able to do the following things…

Press enter or click to view image in full size
Create Organisation
Press enter or click to view image in full size
Edit Organisation
Press enter or click to view image in full size
Details of Members
Press enter or click to view image in full size
Edit Profile

There are so many things I can do with this and bug hunters know what we will do next… There are many more possibilities in this dashboard but I didn’t do anything because it’s complicated and it will affect every other users, so I reported it as simple as it is with the elaborated impact of what an attacker can do.

APPROACH :

I’ll always love to recon. I will always do some grep in Linux and yes I love it. Whenever I get a large number of domains I usually grep for some interesting domains with specific keywords like …

Staging
Stg
Dev
Portal
Admin
…..etc…..etc…..

Get Yukesh Kumar [ 3th1c_yuk1 ]’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It’s up to you to find more. So after finding subdomains of the target my script will automatically parse all the specially grepped subdomains to httpx for checking whether the host is up or not. Then it will parse the alive hosts to Eyewitness ( a tool designed to take screenshots of websites ). So after this, I will get a notification like …

Press enter or click to view image in full size

There is a tool created by 
Inside ProjectDiscovery
 called Notify. You can use that too.

Now it’s time to do manual recon. I simply visited all the grepped subdomains one by one. There are thousands of domains even after being grepped with keywords but still, I tried to visit one by one. After some time I got a weird subdomain with the name “portal” throwing out an error message. You can see it here…

Press enter or click to view image in full size

I tried to refresh it and all of a sudden I logged into the dashboard but after some seconds it throws the same error message.. 502 Proxy error. I don’t know what’s happening there so I kept opening the tab aside and checked the other subdomains and ended up getting nothing.

So now I decided to check that subdomain once again.

First time — Shows the error message.

Second time — loaded for a second and showed up the error message.

Third time — logged into the dashboard but after some seconds showed up the same error message.

I don’t know how I got this idea. I just opened the private tab ( In mobile it is incognito mode ) pasted the domain and boom 💥 ended up getting into the dashboard without any error messages.

I don’t know how it works and how the developer created this subdomain. I laughed inside me. Explored the whole application got some sensitive API keys and much more.

Thanks to 
Aseem Shrey (@aseemshrey)
 for making a video on how to get free push notifications.

If you came up with any suggestions or doubt you are always welcome …

TWITTER — https://twitter.com/3th1c_yuk1

LINKEDIN — https://www.linkedin.com/in/3th1cyuk1/

Do Follow Techiepedia for more Interesting write-ups.

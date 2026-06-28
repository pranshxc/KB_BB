---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-29_how-i-found-an-insecure-direct-object-reference-in-tiktok.md
original_filename: 2023-01-29_how-i-found-an-insecure-direct-object-reference-in-tiktok.md
title: How I Found an Insecure Direct Object Reference in TikTok
category: documents
detected_topics:
- idor
- mobile-security
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- idor
- mobile-security
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 7676ae9c39c22bd10e07fc518f6290edfa60ed4b27ebe32bda96db4a8b3d91cc
text_sha256: 65dfe778b80695c86ec9ade73325f84d2b4801bf06a58d3b447edb9c3337e73e
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found an Insecure Direct Object Reference in TikTok

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-29_how-i-found-an-insecure-direct-object-reference-in-tiktok.md
- Source Type: markdown
- Detected Topics: idor, mobile-security, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `7676ae9c39c22bd10e07fc518f6290edfa60ed4b27ebe32bda96db4a8b3d91cc`
- Text SHA256: `65dfe778b80695c86ec9ade73325f84d2b4801bf06a58d3b447edb9c3337e73e`


## Content

---
title: "How I Found an Insecure Direct Object Reference in TikTok"
url: "https://medium.com/@mrhavit/how-i-found-an-insecure-direct-object-reference-in-tiktok-c7303addf223"
authors: ["mrhavit"]
programs: ["TikTok"]
bugs: ["IDOR"]
bounty: "5,500"
publication_date: "2023-01-29"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1606
scraped_via: "browseros"
---

# How I Found an Insecure Direct Object Reference in TikTok

How I Found an Insecure Direct Object Reference in TikTok
mrhavit
Follow
4 min read
·
Jan 29, 2023

1K

4

Press enter or click to view image in full size

Hello fellow security researchers and bug bounty hunters!

In this article, I am going to share my experience of finding an Insecure Direct Object Reference (IDOR) vulnerability in TikTok while participating in their bug bounty program.

The Story

While scrolling through Hackerone and searching for new targets, I browsed the TikTok bug bounty page for the millionth time, but this time I noticed something very exciting — a new scope had been added. Upon further investigation, I discovered that TikTok had released a new app called “TikTok Now”.

I immediately turned on my old Android device, downloaded the new app, and started exploring.

Business Logic

During the first hour, I didn’t even use any security tools. Since it was a new app, I focused on learning and playing with all the features it offered and wrote down some potential scenarios that I could try to achieve later.

The TikTok Now app is very straightforward. It allows users to share “memories” with other users. These “memories” are videos/photos that the user has uploaded.

One of the most impactful security issues that I can think of for the TikTok Now app, which affects users across the platform, is the possibility of viewing other users’ private “memories.”

Let's Start

I started Burp and, as I mentioned earlier, I was trying to find a way to view the private “memories” of other users. So, my first step was to create a new “memory” and set its privacy settings to “Friends” (Friends meaning that only followers that you follow back can view).

After I uploaded the “memory,” I changed its privacy settings from “Friends” to “Everyone” and captured the request using Burp. The request looked like this:

POST /unification/privacy/item/modify/visibility/v1?carrier_region=&manifest_version_code=-1&_rticket=1665657797313&app_language=en&ac=wifi&device_id=7151368204245353990&iid=7153930339445278470&os_version=11&channel=googleplay&version_code=10203&device_type=IN2023&language=en&resolution=1080*2125&update_version_code=-1&app_name=TikTok%20Now&cdid=ffdd5c09-b345-4860-ab4a-460218871241&version_name=1.2.3&os_api=30&device_brand=OnePlus&ssmix=a&device_platform=android&dpi=450&aid=385522 HTTP/2
Host: api16-normal-c-alisg.tiktokv.com
Cookie: ...........
Content-Length: 35
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: 
Accept-Encoding: gzip, deflate

aweme_id=71539436394863*****&type=1

The ‘aweme_id’ parameter is the ID of my “memory,” and the ‘type’ parameter indicated the option I wanted to change for my “memory” — in this case, to “Everyone”. At this point, I started to think about IDOR (Insecure Direct Object References) and whether it would be possible for me to use this action on the ‘aweme_id’ of a “memory” that does not belong to me.

I quickly created a new account and uploaded a private “memory”. I then retrieved the ‘aweme_id’ for this “memory”. Now that I have obtained the ‘aweme_id’ for the target account, I can attempt to use it with my own account, which I will refer to as the ‘attacker’ account.

Get mrhavit’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I sent once again the request, but this time with the ‘aweme_id’ of the target account:

POST /unification/privacy/item/modify/visibility/v1?carrier_region=&manifest_version_code=-1&_rticket=1665657797313&app_language=en&ac=wifi&device_id=7151368204245353990&iid=7153930339445278470&os_version=11&channel=googleplay&version_code=10203&device_type=IN2023&language=en&resolution=1080*2125&update_version_code=-1&app_name=TikTok%20Now&cdid=ffdd5c09-b345-4860-ab4a-460218871241&version_name=1.2.3&os_api=30&device_brand=OnePlus&ssmix=a&device_platform=android&dpi=450&aid=385522 HTTP/2
Host: api16-normal-c-alisg.tiktokv.com
Cookie: ...........
Content-Length: 35
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
User-Agent: 
Accept-Encoding: gzip, deflate

aweme_id=TARGET-AWEME_ID&type=1

AND…. YES! It’s Worked! I got 200OK and a Successful Message!

Using the attacker’s TikTok account, I browsed the target profile and found that I was able to view their “memory” even though we were not friends. This was due to an IDOR (insecure direct object reference) vulnerability, which allowed me to change the target’s “memory” privacy setting from “Friends” to “Everyone.” Excited by this discovery, I initially considered reporting it to the TikTok team, but then I realized that I could demonstrate an even greater impact by showing how this vulnerability could be exploited.

Medium or High?

This could be considered a high-severity finding due to the potential for an attacker to view and modify the privacy settings of a user’s private “memories.” However, since the ‘aweme_id’ for these memories is not guessable, we must find a way to obtain its value in order to exploit this vulnerability.

With my attacker account, I searched for my victim’s username and browsed their profile. Since their “memory” privacy settings were set to “Friends,” the following message appeared — You can view after you become friends

Despite the message stating that the private “memories” should not be accessible, the response of the API call when browsing the user profile exposed the private “memory” “aweme_id”. This was exactly the information I needed in order to complete my task.

Press enter or click to view image in full size
The Flow
Browse the profile of the person you are interested in
Obtain their private ‘aweme_id’ memory from the response.
Send the vulnerable request using the obtained ‘aweme_id’.
The private “memory” of the person you are interested in is now public.

HackerOne Report

Timeline:

Reported — Oct 13th

Triaged — Oct 17th

Awarded 5500$— Oct 19th

Resolved — Oct 25th

Finding this IDOR vulnerability in TikTok was an exciting and rewarding experience for me. I learned a lot from it and I hope that sharing my experience will help others in their bug bounty journey.

Thank you for reading my article. If you have any questions or want to learn more about my experience, feel free to reach out to me.

@mrhavit

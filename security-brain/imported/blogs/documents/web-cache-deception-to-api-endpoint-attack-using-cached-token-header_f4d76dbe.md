---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-13_web-cache-deception-to-api-endpoint-attack-using-cached-token-header.md
original_filename: 2019-04-13_web-cache-deception-to-api-endpoint-attack-using-cached-token-header.md
title: Web Cache Deception to API endpoint attack using cached token header
category: documents
detected_topics:
- command-injection
- otp
- api-security
tags:
- imported
- documents
- command-injection
- otp
- api-security
language: en
raw_sha256: f4d76dbe2f75700168b7075552aafb108d6827a485ce2baa06ed2ec0054b3d16
text_sha256: e9d40e2da2181f823e31abf12d47551001b4c7b3eaca17a9e3e124ab5688fa63
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Web Cache Deception to API endpoint attack using cached token header

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-13_web-cache-deception-to-api-endpoint-attack-using-cached-token-header.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f4d76dbe2f75700168b7075552aafb108d6827a485ce2baa06ed2ec0054b3d16`
- Text SHA256: `e9d40e2da2181f823e31abf12d47551001b4c7b3eaca17a9e3e124ab5688fa63`


## Content

---
title: "Web Cache Deception to API endpoint attack using cached token header"
url: "https://medium.com/@kunal94/web-cache-deception-to-api-endpoint-attack-using-cached-token-header-b01a604a5ccd"
authors: ["Kunal pandey (@kunalp94)"]
bugs: ["Web cache deception"]
bounty: "250"
publication_date: "2019-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5313
scraped_via: "browseros"
---

# Web Cache Deception to API endpoint attack using cached token header

Web Cache Deception to API endpoint attack using cached token header
Kunal pandey
Follow
4 min read
·
Apr 13, 2019

432

4

Hello Everyone

In my last write-up, I wrote about web-cache deception that leads to information leakage of any personal user’s info.

This time, I got a Web cache deception attack which allows me to steal token header, user-id and further can be used for API endpoint.

This bug I have discovered on private bounty program.

User Interaction Required - Only one time.

[Note: At the end of this write-up, please go through Key Points :) ]

Let’s jump to the main part

While I was trying to understand the mechanism of their Web App, it turns out that for every interaction like upload, fetching inbox content and other settings functionality, they use API endpoint with auth token header to perform the operation along with user id.

let’s just say www.example.com was their main domain and ww4.example.com was another API domain which was performing the operation.

So, I was intercepting the request of www.example.com and in the response header, I saw X-caches-status as HIT.

But to be sure more, I tried to inject random endpoint like bb.jpg, aa.css and it was not giving an error like format not found error.

So, I injected the endpoint like example.com/aa.css, then in response, I was redirected to 404 error page something like this:

Press enter or click to view image in full size

So, I tried to visit this same page in incognito mode, and then view source code, but there was no personal info disclosure, only account name.

However, I tried to read the source code and down below, I got the token header, access-key and user encrypted ID cached in the endpoint.

Press enter or click to view image in full size

So, the above page has cached the more important parameters than personal information.

But wait, I was thinking can we perform API endpoint attack using cached parameters?

In order for API endpoint to fetch and upload contents, you only need three parameters:

User ID
X-access-token
X-app-key

So, I got a perfect condition scenario but deep down inside, I was still wondering whether these cached parameters will be validated in API endpoint or not.

Get Kunal pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, I tried to intercept the request API endpoint in guest endpoint and it was

So, I intercepted the request in guest mode and you can notice in Access token, it’s mentioned “guest” mode.

Here comes the next part:

So, now I modify the API endpoint to fetch pending request in inbox using the API endpoint with cached parameter injection (userid and token).

and the response was

So, I was finally able to retrieve the info like pending inbox request from API endpoint using the previous cached token parameter like inbox pending request.

This is just for fetching inbox content info, what further attacks I could do — I was also able to do POST method in Upload profile picture functionality using cache token, user-id.

Finally, I used API endpoint to perform unauthorized profile picture upload using cached parameters.

After successfully able to retrieve info and modify some settings, I was like time to create a report ^_^

Response and Reaction

Submitted the report to the company, they rewarded me around $250. It’s because the company is newly launched and their maximum bounty was $300. They also asked me how we can mitigate, Interaction was so awesome I felt like I was part of their Team. :)

I was happy because I was able to combine attacks up-to endpoint and fully demonstrate the impact.

Key Points

Check every parameter in the source code if you got a cached response.
If you got token header leakage and user id, try to demonstrate till endpoint and combine attacks.
Make sure that cached token header is expired or not, whether it’s still validating on API endpoint or not.
In this Attack, it was one-time user interaction, so it was more severe as you can do API operation from your side, no further user interaction required at all.

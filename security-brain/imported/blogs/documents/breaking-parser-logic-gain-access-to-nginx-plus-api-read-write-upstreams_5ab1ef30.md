---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-05_breaking-parser-logic-gain-access-to-nginx-plus-api-readwrite-upstreams.md
original_filename: 2022-01-05_breaking-parser-logic-gain-access-to-nginx-plus-api-readwrite-upstreams.md
title: 'Breaking Parser Logic: Gain Access To NGINX Plus API — Read/Write Upstreams.'
category: documents
detected_topics:
- api-security
- command-injection
- path-traversal
- rate-limit
- automation-abuse
tags:
- imported
- documents
- api-security
- command-injection
- path-traversal
- rate-limit
- automation-abuse
language: en
raw_sha256: 5ab1ef3075c9798e83ca987ec17ff8982415ece45b78f351fa835f92fc89f05d
text_sha256: 6e34829925346fc705285c1147df7cf8528a5af89586a0f1f6b9104527d200bd
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Parser Logic: Gain Access To NGINX Plus API — Read/Write Upstreams.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-05_breaking-parser-logic-gain-access-to-nginx-plus-api-readwrite-upstreams.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, path-traversal, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `5ab1ef3075c9798e83ca987ec17ff8982415ece45b78f351fa835f92fc89f05d`
- Text SHA256: `6e34829925346fc705285c1147df7cf8528a5af89586a0f1f6b9104527d200bd`


## Content

---
title: "Breaking Parser Logic: Gain Access To NGINX Plus API — Read/Write Upstreams."
page_title: "Breaking Parser Logic Gain Access To NGINX API — Read/Write Upstreams. | by zoid | Jan, 2022 | Medium | Medium"
url: "https://zoidsec.medium.com/breaking-parse-logic-gain-access-to-nginx-api-read-write-upstreams-1cb062aa44ca"
authors: ["zoid (@z0idsec)"]
bugs: ["Path traversal"]
publication_date: "2022-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3029
scraped_via: "browseros"
---

# Breaking Parser Logic: Gain Access To NGINX Plus API — Read/Write Upstreams.

zoid
 highlighted

Breaking Parser Logic: Gain Access To NGINX Plus API — Read/Write Upstreams.
zoid
Follow
6 min read
·
Jan 5, 2022

129

2

Hi hackers, in this talk I will explain how I could direct traffic from an internal server to my own by breaking the way their reverse proxy’s requests are handled.

First of all, thank you for taking the time to read this post and I hope you learn something new from this so, sit back grab a coffee and enjoy.

How do reverse proxies work?

A reverse proxy will sit between the public-facing web and the internal servers acting as an intermediate server its main job is to process the requests coming through the proxy and upstream them to the appropriate servers.

Let’s have a look at a little scenario, say we have a website

http://company.com

with a backend portal with all the customer's PII data but we don’t want this to be accessible to the public, let’s give this a hostname

http://portal.company.com:8282/

Without a reverse proxy, we would be able to access the portal directly from the browser because there is no gateway stopping anyone from accessing the portal. To stop external access, we would need to implement an intermediate proxy that sits between the website and the backend portal blocking or denying clients requests who are trying to access the portal directly from the browser. This can be done with reverse proxies such as:

Nginx
Apache
HAProxy
Squid

Nginx is one of the most popular reverse proxies.

Press enter or click to view image in full size
The workings of a reverse proxy.

You can configure them with rules or filters that tell that reverse proxy how to handle the requests being passed through.

Unfortunately, oftentimes people use bad parser logic, and bad regular expressions which allow hackers to easily break the logic Implemented allowing them to access internal servers, for example, the portal I explained above which would lead them to gain access to all the customer's PII data.

Path Normalisation goes Boom!!

I want to dive deep into one of my recent P1 findings on a private bug crowd program I was invited to. We will focus on secondary context path traversal for now because there are so many different types of reverse proxies, load balancers and caching server vulnerabilities with different variants, secondary context path traversal being one of them.

1.) My initial recon always starts with Chrome dev tools I like to make sure only Fetch/XHR and Docs are checked and everything else unchecked this greatly reduces the number of static files that get populated, FYI never ignore these files because in some cases they can help.

Press enter or click to view image in full size
Chrome Dev Tools

2.) I was looking through the requests in Chrome dev tools and found an API endpoint that looked rather interesting, so I immediately ran ffuf with some common path traversal payloads:

/experience/..;/
/experience/../
/experience/..%2f
/experience/%2e%2e%2f

3.) I use a much larger list, these are just a few out of many I try. I looked out for the nuances in the response and noticed that they all returned 403 except

/experience/..%2f

returned a 404

4.) This is a great indicator that we may be hitting the internal root of the API. To test this further I went back to one directory to see if anything changed

Nginx 400 bad request

/experience/..%2f..%2f

Get zoid’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This resulted in a 400 Bad Request which made me enter hacker mode, I put on some cyberpunk music and performed some content discovery on the path which resulted in the 404 Explained above in step 4.☝️

/experience/..%2fHERE

At this point I knew it was an Nginx reverse proxy because the 400 Bad Request leaked the server type, all I needed was a path that yielded a valid 200 Ok, I was procrastinating watching YouTube videos while the content discovery finished, it was a small scope so I had every right to sit back while the scanned finished 😂 shhh…. just kidding never do this during a pentest you need to make sure you're always doing something.

I looked at the scan results after watching IPsec on YouTube and found that there was a path /api and a dashboard.html file that both resulted in a 200 Ok with different responses I immediately navigated to it

/experience/..%2fdashboard.html

And noticed that it was an NGINX Plus API.

Live Activity Monitoring of NGINX Plus
Ever needed to know what's going on right now with your NGINX Plus server? Do you suspect a DDoS attack, or are users…

www.nginx.com

To be 100% sure this is internal and we have a valid hit, I needed to verify dashboard.html and /api was not accessible in the web root being

http://example.com/dashboard.html

and

http://example.com/api

which resulted in a 403 in both cases so this means we have a valid hit.

There was nothing much on the dashboard.html so I had a look at the /api path that was found which contained all these numbers in JSON, so I looked at the Nginx API docs.

http://nginx.org/en/docs/http/ngx_http_api_module.html#example

and collected intel on these numbers and found that they are different versions of the API, I navigated to one of the versions which contained some pretty interesting stuff, these were the different paths I could hit:

/experience/..%2f/api/7/
/experience/..%2f/api/7/nginx
/experience/..%2f/api/7/connections
/experience/..%2f/api/7/http/requests
/experience/..%2f/api/7/http/server_zones/server_backend
/experience/..%2f/api/7/http/caches/cache_backend
/experience/..%2f/api/7/http/upstreams/backend
/experience/..%2f/api/7/http/upstreams/backend/servers/
/experience/..%2f/api/7/http/upstreams/backend/servers/1
/experience/..%2f/api/7/http/keyvals/one?key=arg1
/experience/..%2f/api/7/stream/
/experience/..%2f/api/7/stream/server_zones/server_backend
/experience/..%2f/api/7/stream/upstreams/
/experience/..%2f/api/7/stream/upstreams/backend
/experience/..%2f/api/7/stream/upstreams/backend/servers/1

At this point, I had a P3 and my inner hacker beast did not wanna give up he wanted to escalate this to a P1, so I reached out to some mates on Slack and one came up with the idea of trying to write to the API. I had a look at the API docs some more and found many POST & GET verbs for some of the paths except it was documented that writing to the API is disabled by default.

I kinda lost all hope.

Press enter or click to view image in full size
Photo by Tim Gouw on Unsplash

But remember to never give up, there is always a chance so I played around with the different parameters assuming it would not allow me to write to the API except….. Wait…. 204. WTF, it worked I was able to create my upstream and write to the API which escalated it to a P1 and was triaged within an hour.

This was my final POC:

Press enter or click to view image in full size
Final POC ;)

here is the response:

Press enter or click to view image in full size
Impact

Malicious threat actors or APTs can create their upstreams to re-route traffic to their servers and disrupt internal services.

Final Takeaways

My final takeaways would be to always stay away from the crowd and never rely on tools that everyone else is using, always come up with your templates, wordlist & methods, and utilise manual testing procedures because it allows you to look much deeper into the websites core logic, also think outside the box pretend you are the developer making the mistakes. With secondary context path traversal, always test every single path and recursively go through each one, one by one because every path may contain something different.

If you’re a fan of my work, you’ll want to check out Dirstrike, our latest SaaS built for large-scale directory brute-forcing. Say goodbye to rate limits and IP bans! Join our Discord: https://discord.gg/4Q4WgNR5wg and help us turn this into something huge. Your support is truly appreciated!

I hope you enjoyed this post, and until next time happy hacking 🔥

Peace out ✌️

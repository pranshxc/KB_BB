---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-05_the-case-of-the-missing-cache-keys.md
original_filename: 2020-08-05_the-case-of-the-missing-cache-keys.md
title: The Case of the Missing Cache Keys
category: documents
detected_topics:
- xss
- automation-abuse
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- xss
- automation-abuse
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: 08a87382eaa2fea81d50e730fe98ddd4139b72b0b82eac6f3ae13137afe3c8e4
text_sha256: daf719d72f61d834e6042af99d8444bf2d25d3acbc14dc9dca262767a9100b3d
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The Case of the Missing Cache Keys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-05_the-case-of-the-missing-cache-keys.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `08a87382eaa2fea81d50e730fe98ddd4139b72b0b82eac6f3ae13137afe3c8e4`
- Text SHA256: `daf719d72f61d834e6042af99d8444bf2d25d3acbc14dc9dca262767a9100b3d`


## Content

---
title: "The Case of the Missing Cache Keys"
page_title: "The Case of the Missing Cache Keys – enumerated"
url: "https://enumerated.wordpress.com/2020/08/05/the-case-of-the-missing-cache-keys/"
final_url: "https://enumerated.wordpress.com/2020/08/05/the-case-of-the-missing-cache-keys/"
authors: ["Aaron Costello (@ConspiracyProof)"]
bugs: ["Web cache poisoning"]
publication_date: "2020-08-05"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 4350
---

# The Case of the Missing Cache Keys

[August 5, 2020August 5, 2020](https://enumerated.wordpress.com/2020/08/05/the-case-of-the-missing-cache-keys/) ~ [Dantalion](https://enumerated.wordpress.com/author/dantalion4040/)

Typically when the words ‘Cache-Poisoning’ are uttered, the first thing that comes to mind is HTTP headers. This ranges from the [legendary ‘Transfer-Encoding’ CPDoS](https://cpdos.org/) that tore down entire default CDN implementations, to the simple yet effective application leaning issues such as reflection of ‘Cookie’ values in the source (I ❤️ double-submit CSRF for XSS) or a dodgy filtering of unknown user agents leading to a block.

Now it’s time to change that, and provide a greater understanding of how we can further take advantage of the domestic dispute between what caching software wants, and what the application wants when it comes to a HTTP request body. For most use-cases I’ll be discussing the issues with regard to NGINX, as it’s won’t require the fee to purchase that a popular CDNs subscription might, and it’s relatively simple to analyse and play with. 

Before I go on, I’d like to thank [James Kettle of Portswigger](https://portswigger.net/research/james-kettle) for collaborating on the release date for this article to coincide with his [own](https://portswigger.net/research/web-cache-entanglement). 

## Security Exchanged for Performance

The first case we’ll look at is what happens when people try to get hands on with their caching configuration at the lowest level. By default, NGINX will do its utmost to be secure by only caching responses to HEAD and GET requests. However if one decided to add POST to the ‘proxy_cache_methods’ of the NGINX config and left it at that, we come to a bit of a problem. 

The source of this problem, which is relevant for the entirety of this blog post, is the fact that after the addition of another HTTP verb (specifically one that’s intended to have a request body), the ‘proxy_cache_key’ wasn’t modified along with it. But what exactly is this?

If you’re a fan of submitting caching related issues on HackerOne, chances are I may have caught you out for not paying attention to the cache key (sorry!) and pointing out that it’s not in fact exploitable against another user. The cache keys are values that will ultimately determine whether you’ll be served cached content or fresh contents from the origin. These values are reflected in the ‘Vary’ response header and are there for good reason, such as ensuring users with different ‘Cookie’ values are not given the same shared content from the cache for a specific page. 

Understanding the above, you may begin to see the problem here. By enabling requests using the ‘POST’ verb to have their responses cached, but not adding the ‘$request_body’ to the cache keys will ultimately result in both POST and GET requests being seen as the same to the cache. Remember, the caching software here is only using the HTTP verb to determine if the response SHOULD be cached, and the cache key’s are used to determine if the request has been SEEN before (and if so, serve up a shared copy if appropriate).

To quickly test, I spun up NGINX and added ‘POST’ to the verbs that should be cached. An example PHP file was created:
  
  
  <!DOCTYPE html>
  <html>
  <body>
  
  <form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
  Name: <input type="text" name="fname">
  <input type="submit">
  </form>
  
  <?php
  if($_SERVER['REQUEST_METHOD'] == "POST"){
  $name = $_POST['fname'];
  if (empty($name)) {
  echo "Name is empty";
  } else {
  echo $name;
  }
  }
  ?>
  
  </body>
  </html>
  

Sending an initial POST request like the following, resulted in XSS as you’d expect:
  
  
  POST /test.php?cachebuster=s HTTP/1.1
  Host: xxxxx
  Content-Length: 31
  Cache-Control: max-age=0
  Upgrade-Insecure-Requests: 1
  Origin: http://xxxx
  Content-Type: application/x-www-form-urlencoded
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  Referer: http://xxxxx/test.php
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Connection: close
  
  fname=<script>alert(1)</script>
  

However, a subsequent ‘GET’ request to ‘/test.php?cachebuster=s’ without any HTTP body will now also show the alert, as the response to the previous POST request was cached.

In the wild, I’ve successfully managed to exploit the lack of ‘$request_body’ absence in the cache keys in two specific scenarios a small handful of times.

  1. Stored XSS exactly like the above, due to some forgotten user inputs combined with performance hungry developers.
  2. Newsletter exploitation. It’s completely understandable to overlook this minor functionality as a dev and how it may be abused. By taking an input on a newsletter page (such as an email) and processing it on that same page (PHP_SELF style), then finally returning your email in the response of…once again that very same page, a subsequent GET request to the newsletter endpoint may very well leak the email of another user who had submitted it previous.

Fortunately, while the RFC 7234 has briefly [mentioned the possibility of POST caching](https://tools.ietf.org/html/rfc7231#section-4.3.3), it’s not a default issue among any caching software / http accelerators / CDNs, and as such this vector is only worth a shot if you’re really scraping the bottom of the barrel for that bounty. 

## The FAT GET

At the time of release, this specific vector will have been discussed and introduced for the first time by the infamous James Kettle in his Blackhat talk, and boy, is this issue prevalent. In the previous scenario we discussed a manual misconfiguration at the caching level, but now we focus moreso on what the web application itself is doing, and how it can enter into conflict with supposedly safe caching setups.

So far, we know the following from previous discussion:

  1. By default for caching software, the GET verb will be a cacheable method from the get-go. 
  2. The HTTP request body is **most** of the time not added as a cache key by default. 

Now imagine there was a world in which developers ignored the HTTP verb when processing user input, and were happy to interpret the $request_body regardless of it. 

In this world, we have the FAT GET vector. This relies on the miscommunication of how the cache wants something done, and the application; CDNs such as Cloudflare do not handle this by default as they see it as a ‘you problem’ as opposed to an ‘us problem’, and they’re right.

Take the below scenario which was morphed into a persistent CPDoS from a harmless relative redirect:

  1. Navigating to ‘/login.php’ introduces a login form

2\. After successful authentication, the HTTP body of the POST request looks like the following , redirecting you to your dashboard:
  
  
  ...&redirect=/dashboard.php
  

3\. If no username or password is provided when the form is submitted, the ‘redirect’ value returns you to ‘/login.php’ to start the process again. 

4\. However, the endpoint has public caching enabled and will happily still process the request body values in the code. As such, an attacker sends the following request and manages to be the first to have their response cached once the previous becomes stale:
  
  
  GET /login.php HTTP/1.1
  ...
  ...
  redirect=/404
  

As a result, everyone who attempts to login via ‘/login.php’ as normal is now redirected to ‘/404’ and unable to login until the cache expires. This is only a small example, more severe implications can include issues such as Persistent XSS and even [complete account takeover](https://samcurry.net/abusing-http-path-normalization-and-cache-poisoning-to-steal-rocket-league-accounts/) (This did not use the FAT GET method but rather a header, so swap that sink for a POST based open redirect converted to a persistent GET one using the aforementioned method, and it’s ultimately the same).

So if you’re at home with a file full of POST based open redirects, you may very well be able to escalate it to a ‘High’, possible a ‘Critical’ in the presence of the FAT GET and an access token smuggling bug. 

## Remediation

The remediation for the POST method being set as cacheable verb is simply not to do it, ever The RFC is a generous god, but about as trustworthy as a genie if you took it’s “I guess you can do that” approach.

For the FAT GET, it’s important to ensure you stick to the basic understanding of the HTTP verbs and what comes with them. You realistically shouldn’t be processing the request body of a GET request, and that’s putting it straight. However, feel free to yell at me about how caching software should have the $request_body as a cache key by default, it likely won’t change the reality.

## BB Report Template

Since I’ll probably be triaging this issue alot in the coming days, I’d appreciate it if you made it look pretty. 

FAT GET:
  
  
  ## Summary of the Issue
  The web application is vulnerable to a cache poisoning issue on the following endpoint:
  
  '''
  <URL>
  '''
  
  The responses to GET requests are being served from a public cache, however due to the lack of the request body being present in the cache keys, we can achieve <insert vulnerability> via the <parameter_name> parameter of our requests.
  
  ## Steps to reproduce
  
  1. Open Burp Suite and ensure it's sniffing all HTTP(S) requests in the background.
  2. Navigate to <endpoint>. Find the request to this endpoint in Burp's proxy history and send it to the repeater.
  3. Add the following cachebuster as a GET parameter: 'dontpoison=true'. This will ensure to isolate the resulting exploit to users who make requests to this endpoint with the 'dontpoison' parameter & value pair present.
  4. Insert the following POST parameter and value to the request body:
  
  <param>=<value>
  
  The entire request should now look like:
  
  <Full HTTP Request>
  
  5. Submit the request 8-10 times. Remove the POST parameter and value pair that was added in the previous step. 
  6. Change your IP address, and submit the request again. As you can see, the exploit has persisted, showing caching poisoning.
  
  ## Impact statement
  An attacker can poison the response served from the public cache to all users who navigate to the affected endpoint, resulting in <vulnerability name>
  
  ## Remediation
  
  Ensure that the application does not process the HTTP body of a GET request.
  
  

### Share this:

  * [ Share on X (Opens in new window) X ](https://enumerated.wordpress.com/2020/08/05/the-case-of-the-missing-cache-keys/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://enumerated.wordpress.com/2020/08/05/the-case-of-the-missing-cache-keys/?share=facebook)
  * 

Like Loading...

### _Related_

![Unknown's avatar](https://2.gravatar.com/avatar/b4f8d77b183e297e33889c4bcfb858506ed79424b22c0512d25ca9d2d523fc76?s=60&d=identicon&r=G)

##  Published by Dantalion

[ View all posts by Dantalion ](https://enumerated.wordpress.com/author/dantalion4040/)

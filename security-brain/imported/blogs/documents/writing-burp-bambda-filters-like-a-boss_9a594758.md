---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-05_writing-burp-bambda-filters-like-a-boss.md
original_filename: 2023-12-05_writing-burp-bambda-filters-like-a-boss.md
title: Writing Burp Bambda Filters Like a Boss
category: documents
detected_topics:
- jwt
- api-security
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- jwt
- api-security
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 9a5947589877b6acc5b46720bfb57550ef581a3f0d81a7e8fd882a6f90e8acac
text_sha256: 7062a7c3c15dd1749fa26c0f13edb35270e85a2dc9a7f32fb36d31e2bf1464c0
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Writing Burp Bambda Filters Like a Boss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-05_writing-burp-bambda-filters-like-a-boss.md
- Source Type: markdown
- Detected Topics: jwt, api-security, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `9a5947589877b6acc5b46720bfb57550ef581a3f0d81a7e8fd882a6f90e8acac`
- Text SHA256: `7062a7c3c15dd1749fa26c0f13edb35270e85a2dc9a7f32fb36d31e2bf1464c0`


## Content

---
title: "Writing Burp Bambda Filters Like a Boss"
url: "https://danaepp.com/writing-burp-bambda-filters"
final_url: "https://danaepp.com/writing-burp-bambda-filters"
authors: ["Dana Epp (@DanaEpp)"]
bugs: ["JWT", "Broken authorization"]
publication_date: "2023-12-05"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 648
---

December 5, 2023

[API Hacking Techniques](https://danaepp.com/category/api-hacking-techniques), [API Hacking Tools](https://danaepp.com/category/api-hacking-tools)

# Writing Burp Bambda Filters Like a Boss

![](https://danaepp.com/wp-content/uploads/2023/11/Writing-Burp-Bambda-Filters-Like-a-Boss.png)

I have to tell you about Burp Bambda filters. This neat new feature in Burp helped me discover a new P1 crit on a target this week.

Let me explain how.

## The backstory

I recently worked on an engagement where I stumbled upon several new undocumented API endpoints on a staging instance of a SaaS product I am hacking.

It wasn’t immediately apparent what was going on. I could tell something was “different,” but I wasn’t quite sure what. It definitely included new routes, and the sitemap clearly showed some of the new endpoints.

But as I looked closer, I noticed the **Authorization** **header** for these endpoints looked different. As I investigated, I realized that the new API endpoints used a different access token than I usually see. It was still a JWT, but it was using a different algorithm.

How many other requests were like this?

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/image-8.png?resize=892%2C892&ssl=1)

I had several hundred thousand requests in the Proxy history of Burp. I really didn’t want to slog through all of them to try to figure out what was going on. And then I remembered PortSwigger recently [released a new feature called Bambdas](https://portswigger.net/blog/introducing-bambdas) this month.

I wondered if Bambdas could help me wade through all these requests.

TL;DR … **I was able to parse through hundreds of thousands of requests in seconds** and discover not only new endpoints using this new feature, but also a new token exchange service that ended up having a vulnerability in it that I could exploit.

Let me show you how I wrote a Bambda filter that helped me discover this. Maybe it will help you to write your own Bambdas… and write them like a boss.

## What are Bambda filters?

You’ve heard of lambdas, right? Well, the naming gurus in the marketing team at Portswigger thought it would be cute to name a new feature they were introducing as “Bambdas.”

Every feature they write these days for Burp has to be named starting with a “B.” You know, like [BChecks](https://danaepp.com/improve-your-api-security-testing-with-burp-bcheck-scripts).

OK, maybe that’s not the real story… but I can envision the naming gremlins over in PortSwigger’s office in Knutsford, UK, snickering as they named this feature.

Anyways, [according to Portswigger](https://portswigger.net/blog/introducing-bambdas), Bambdas are a unique new way to customize Burp Suite directly from the UI, using only small snippets of Java. The first place they are exposing this is in the Proxy HTTP history as custom filters.

## Writing your first Bambda filter

So accessing the new feature requires installing at least version 2023.10.3 of Burp Suite. The feature is exposed directly in the Filter option within the Proxy HTTP history tab.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/Filter-Settings.jpg?resize=1404%2C698&ssl=1)

When you click on the filter, it will pop-up a dialog to configure your filter for the proxy history. If you select “Bambda mode,” you will immediately be presented with a Java snippet editor window where you can write your code snippet.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/configure-filter.jpg?resize=2064%2C1756&ssl=1)

Currently, Burp exposes two interfaces of the [Montoya API](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/MontoyaApi.html) that are available to help you write your Bambdas. These include the [ProxyHttpRequestResponse](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/proxy/ProxyHttpRequestResponse.html) and [Utilities](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/utilities/Utilities.html) interfaces.

What’s nice is that the Bambda editor supports auto-completion, allowing you to explore the interfaces directly in the coding window and get helpful hints as to what function calls are available.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/montoya-autocomplete.jpg?resize=2752%2C1284&ssl=1)

As the custom filter tries to match the conditions of your code snippet, your goal is to write meaningful code that will return TRUE if the condition matches and FALSE if it doesn’t. When it returns FALSE, it will filter that record out, leaving you with the records you want to see.

PortSwigger has [some good guidance](https://portswigger.net/burp/documentation/desktop/tools/proxy/http-history/bambdas) on writing your first filter. You can use that as a guide.

Let me show you how I wrote my first Bambda.

## A Bambda filter for authorization tokens

In the backstory, I mentioned that I needed to filter through hundreds of thousands of records to find specific requests that matched a specific Authorization header. In my case, I wanted to find all JSON Web Tokens (JWT) that were signed using HS512. The target I was testing was typically signed with HMAC-SHA256 (HS256), and I needed to find any requests that deviated from that to use a stronger hashing algorithm.

Using the normal filters wouldn’t work for this, as I would have to break apart the Authorization header, decode the JWT header, and check the algorithm used for signing in the “alg” property.

With Bambdas though, this became relatively trivial to do.

Let me show you how. Here is the final Bambda script I wrote…
  
  
  
  
  if( !requestResponse.hasResponse() )
  
  {
  
  return false;
  
  }
  
  if( requestResponse.request().hasHeader("Authorization") )
  
  {
  
  if( requestResponse.request().headerValue("Authorization").startsWith("Bearer") )
  
  {
  
  String possible_token = requestResponse.request().headerValue("Authorization").split(" ")[1].trim();
  
  
  
  if( possible_token != null && possible_token.contains(".") ) 
  
  {
  
  String jwt_header = possible_token.split("\\.")[0];
  
  if( jwt_header != null )
  
  {
  
  String decoded_header = utilities().base64Utils().decode(jwt_header).toString();
  
  String algo = decoded_header.split("\"alg\":\"")[1];
  
  if( algo.toUpperCase().startsWith("HS512") )
  
  return true;
  
  }  
  
  }
  
  }
  
  }
  
  return false;

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/bambda-filter-JWT.png?resize=2120%2C1812&ssl=1)

A quick walkthrough of what this code does if you are new to Java:

  * On line 1, I filter out any records that don’t have a response.
  * On line 6, I check to make sure the request has an Authorization header present
  * On line 8, I ensure the Authorization header is a Bearer token, which is necessary for our JWT.
  * On line 12, I ensure I can extract the Bearer token and that it’s in a format that includes periods. This is because a JWT is normally formatted as `{HEADER}.{PAYLOAD}.{SIGNATURE}`.
  * On line 14, I try to extract the JWT header.
  * On line 17, I use the Montoya Utilities API to Base64 decode the JWT header.
  * On line 18, I parse out the algorithm from the header
  * On line 19, I check to see if the algorithm property starts with “HS512”. If it does, then and only then do I mark the return from the match request as TRUE so I can see the record in the proxy history view.
  * On line 26, if we get this far, we fail the match, filtering it out of the proxy history view.

## Saving and Loading Bambdas

So once you get the hang of writing Bambas, you will want to save the code and load it later in other projects. This is actually pretty easy, albeit not so straightforward.

To the right of the editor is a gear. If you click it, a menu will pop down, offering you the option to “Save settings.”

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/save-bambda.jpg?resize=2624%2C1344&ssl=1)

This will save your Bambda into a JSON file, which you can easily check into source control and move around to other projects. To load it, it’s just as easy to select “Load settings” from the gear menu and browse to the JSON file you saved. Here is what a saved Bambda file looks like…

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/bambda-save-json.jpg?resize=2748%2C1290&ssl=1)

Pretty simple, eh?

## Limitations of Bambdas

While I found Bambdas easy to write, I will admit there are some gaps. It is only fair that I call these out so you are aware of them. As this feature matures, I expect some of these issues will be addressed.

### There is no logging.

The biggest annoyance I had with writing my first Bambda was getting any sort of indication of what was going on. It was extremely painful trying to split and parse out the access token from requests blindly.

It would be nice to see Portswigger add the [Logging](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/logging/Logging.html) interface from the **burp.api.montoya.logging** package of the Montoya API. This way, we could do “dirty debugging” at least to dump variables and trace code flow.

### There is no step-through debugging.

Writing Java code snippets blindly is no fun. It would be helpful to have a way to set breakpoints, track variables, and follow stack traces to determine precisely how code is functioning and where things are breaking.

While there is VERY rudimentary compile-time and run-time error debug output, it’s not always that useful. Here is an example of a runtime error stack trace that does little to tell me where exactly in my code this failed. It should be showing me the caller line number in my code, not the outer trace of Burp’s Bambda loader code.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/runtime-error.jpg?resize=2122%2C954&ssl=1)

## Conclusion

So there you have it. When you find yourself in a bind and need to do some complex filtering in your proxy history, the Bambda interface is there to the rescue. A bit of Java code snippet fun, and you can filter your requests however you like.

I think we are just seeing the beginning of Bambdas. Portswigger has hinted that they will start exposing them in other tools within Burp… which means we will be able to do some pretty powerful stuff in things like Repeater and Intruder in the future.

Does this replace Burp extensions? I don’t think so. At least, not yet.

When I wrote my [step-by-step guide to writing Burp extensions for API pentesting](https://danaepp.com/a-step-by-step-guide-to-writing-extensions-for-api-pentesting-in-burpsuite) I exposed you to the deep dark underbelly of Burp Suite and some of the neat places you can insert yourself. Bambdas aren’t there… yet.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/11/image-9.png?resize=974%2C544&ssl=1)

I will admit though, writing Bambdas right in Burp was something I could do quickly and easily. That removed a lot of complexity in scaffolding the project that Burp extensions require… but it did require me to write in Java instead of Python. So I think it’s a tradeoff.

Bambdas are worth checking out, at the very least. In my case, about 5 minutes of Bambda coding saved me HOURS (if not DAYS) of manual work going through hundreds of thousands of requests… and allowed me to discover some interesting endpoints that led me to find an interesting vulnerability in the system.

Well worth the effort.

### Share this:

  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://danaepp.com/writing-burp-bambda-filters?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://danaepp.com/writing-burp-bambda-filters?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://danaepp.com/writing-burp-bambda-filters?share=facebook)
  * [ Print (Opens in new window) Print ](https://danaepp.com/writing-burp-bambda-filters#print?share=print)
  * 

![Dana Epp](https://danaepp.com/wp-content/uploads/2022/08/danaepp-headshot-1-300x300.jpg)

Dana Epp

Hey, I’m Dana, aka SilverStr. I build and break software for a living, and am a Microsoft Regional Director and Developer Security MVP. I’ve spent decades as a security architect that focuses on helping secure software, data, and infrastructure on both blue and red teams. As of late, I have been focusing more on my offensive tradecraft to help developers and IT administrators see the impact of exploitation on vulnerabilities in their work. This blog is my chance to give back to the community by sharing my experiences and war wounds from the trenches.

← [Using Chaos Engineering To Hack An API](https://danaepp.com/using-chaos-engineering-to-hack-an-api)

→ [Finding “dark data” in an API](https://danaepp.com/finding-dark-data)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-19_that-time-i-broke-into-an-api-and-became-a-billionaire.md
original_filename: 2023-12-19_that-time-i-broke-into-an-api-and-became-a-billionaire.md
title: That time I broke into an API and became a billionaire
category: documents
detected_topics:
- api-security
- supply-chain
- command-injection
- automation-abuse
- information-disclosure
- business-logic
tags:
- imported
- documents
- api-security
- supply-chain
- command-injection
- automation-abuse
- information-disclosure
- business-logic
language: en
raw_sha256: c83c3d5520c5a0dea7f6fc64ec822de57ca287ad5b55a25f421198c169a25c35
text_sha256: 5c44f2cd3d34ec2440cab9c66f199d8e99fea81f695e5b030de6507e036d79d3
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# That time I broke into an API and became a billionaire

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-19_that-time-i-broke-into-an-api-and-became-a-billionaire.md
- Source Type: markdown
- Detected Topics: api-security, supply-chain, command-injection, automation-abuse, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `c83c3d5520c5a0dea7f6fc64ec822de57ca287ad5b55a25f421198c169a25c35`
- Text SHA256: `5c44f2cd3d34ec2440cab9c66f199d8e99fea81f695e5b030de6507e036d79d3`


## Content

---
title: "That time I broke into an API and became a billionaire"
url: "https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire"
final_url: "https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire"
authors: ["Dana Epp (@DanaEpp)"]
bugs: ["XXE"]
publication_date: "2023-12-19"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 608
---

December 19, 2023

[API Hacking Mindset](https://danaepp.com/category/api-hacking-mindset), [API Security Fails](https://danaepp.com/category/api-security-fails)

# That time I broke into an API and became a billionaire

![](https://danaepp.com/wp-content/uploads/2023/12/That-time-I-broke-into-an-API-and-became-a-billionaire.png)

This is a story about how patience during a pentest pays off.

Actually, it’s more than that.

It’s really about a digital bank heist.

Sort of.

It’s kind of both. Let me explain.

## The Backstory

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2022/12/image-1.png?resize=976%2C734&ssl=1)

A few years back, I was working on an engagement for a customer who handles financial transactions and transfers. This included an internal API with a dependency on a third-party banking API.

We’ll get to the banking API later in this story. It’s a fun twist that ultimately allowed me to transfer any amount of money from any account to another without being detected. It was the perfect digital bank heist where I could steal billions.

But first, I need to show you how I figured out about the dependency and stumbled upon the internal API.

That’s the real story.

## Be patient. Follow your methodology.

If you regularly read my articles, you know I preach about using a systematic approach to hacking APIs. Your methodology will change as you learn and experience new things… but staying focused and following it is a recipe for success.

Or, at the very least, it ensures you test the right things at the right time.

That served me well on this engagement. Mainly because what I found was NOT expected.

That’s all thanks to developers embracing agile development, microservices, and API gateway redirection that exposed something no one considered.

## Aging code gets brittle. But new code is far more frail.

I’ve had this customer for years. I’ve come to know their tech stack well. And it’s fair to say I may sometimes run a little fast and loose when it comes to what gets pentested during each engagement.

Over the years, the customer has moved from larger timeboxed annual pentesting to a form of continuous pentesting where we focus on areas where code has changed or been added every month. So the Statement of Work is a bit loose… with a trade-off being that the customer provides me with information on what areas developers have changed so I can focus my time more efficiently.

And herein lies the rub.

**Developers lie.**

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/03/image-7.png?resize=525%2C499&ssl=1)

Well, more to the point, they don’t always tell you everything.

They aren’t trying to be malicious. They just tend to forget to mention things that they think are trivial or don’t matter in the grand scope of things.

Move fast to get sh*t done. That’s their creed.

When you only focus on the fragility of new code, you can’t always see how this code may impact aging code unless you check. Which is more challenging to do in smaller incremental engagements.

And that was precisely what happened here.

## Vulns can exist in weird places. Trust nothing.

So things change. The whole point of API pentesting is to look at the target objectively with a clear and unbiased view. While it’s important to trust what I’m being told, I must verify everything anyway.

**This engagement reminded me why that’s so important.**

In this case, it was how the API framework was configured and used.

The API servers were configured for years to only support a `Content-Type` of ‘`application/json`**‘**. This makes sense since it was a RESTful API that relied on data models structured in JSON.

In fact, we’ve had automated tests that verify that using any other Content-Type would return an HTTP status code of 415 (unsupported media type). And that has worked well.

**Until it didn’t.**

It turned out that the developers were working on an internal API to bridge between the main API and a third party that processes currency conversion and transfers. As that external API required an XML call-back service, a slight tweak was made to the API framework to allow for a Content-Type of ‘`application/xml`‘ for the new service endpoint.

Or so they thought.

### DevOps becomes DevOops

What happened when the devs allowed for `application/xml` as a supported media type? They accidentally reconfigured the API server to support both JSON and XML for **ALL** endpoints.

Now, I know what you’re thinking… “ _why didn’t the developers tell me about this config change_?”

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/12/image.png?resize=974%2C546&ssl=1)

In the retrospective, it was explained that they didn’t want me to test those endpoints yet as they weren’t expected to be done for a couple more sprints. They assumed the API gateway would protect them as they had yet to publish the new endpoints through it.

They never realized the change to the framework exposed all the other endpoints too.

So why didn’t the automated tests catch this?

Ahhh… that’s a great question. Let me sum it up by saying API gateways aren’t always the smartest. How it processes requests and reprocesses headers sometimes makes it work in weird ways.

In this case, it returned 415 codes to the test server because it processed the request differently internally than from an external client. So, the tests were passing because the API gateway failed the request… not the API server.

## Taint everything.

This one little config change to the API server to allow XML let me get a foothold on the API server thanks to XML Entity Injection (XXE).

Well, that and a poorly configured API gateway that didn’t filter that out for unauthenticated requests.

You’ll see why that matters in a minute.

This let me exfiltrate the API artifacts from the server and ultimately reverse engineer the compiled API into source code… allowing me to find out about the external banking API before I should have known.

Let me show you how I did that.

### Taint JSON requests with XML

Whenever you see an endpoint that accepts a JSON payload, see if you can convert it to XML and resend it.

Tainting data in weird places should be part of your methodology. [I’ve talked about this before](https://danaepp.com/attacking-apis-by-tainting-data-in-weird-places).

Request headers like Content-Type are fair game.

Burp Suite is great for this, with some help from a free BApp extension called [Content Type Converter](https://portswigger.net/bappstore/db57ecbe2cb7446292a94aa6181c9278).

Look for places where successful POST or PUT operations are being done and send them to the Repeater tool. Then right-click on the body of the request and select **Extensions > Content Type Converter > Convert To XML**. It will automatically convert the JSON payload into well-structured XML and change the Content-Type accordingly.

Now send the modified request to the server.

Did it succeed? If so, the endpoint accepts XML, and you can try to abuse that.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/04/image-25.png?resize=950%2C556&ssl=1)

If it doesn’t work, try removing the Content-Type header. Some API frameworks will auto-detect the media type based on the payload. This technique has the added benefit that it can sometimes bypass content type filtering in WAF and API gateways.

Finally, if that doesn’t work, change the Content-Type to ‘`application/xml;charset=UTF-8`‘. It’s a last-ditch effort… but you’d be surprised how many filters have weak blacklist filters that can be bypassed by adding the charset in.

Have an endpoint that accepts XML? Great. Let’s abuse it.

## Exploiting an API through XXE

I’m not going to bore you with instructions on how to exploit XXE. This is already well documented in places like PortSwigger’s [XXE module](https://portswigger.net/web-security/xxe) within the Web Security Academy. What I will do is explain my thinking and approach to it.

Whenever I conduct a pentest, one of my personal goals is to get access to API artifacts and ultimately the source code. It is far easier to perform code analysis and taint tracing when you have it.

Have no clue what I am talking about? [Read this](https://danaepp.com/tracing-api-exploitability-through-code-review-and-taint-analysis).

Anyways, the potential for an XXE vuln is perfect. Done right, I should be able to exfiltrate files.

In my case, I was able to start by adding a standard <DOCTYPE> to the payload and see if it can bring back basic files:
  
  
  <!DOCTYPE danawuzhere [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>

I put an external entity of `&xxe;` into a field that was reflected in the response, and it leaked the passwd file.

Whoohoo! 🎉

But how could I use this to get the API artifacts?

### Using XXE to find API artifacts

Since I knew the API was written in Java using a special framework, I had a good idea of where to look for the files I wanted. Since they were compiled into JAR/WAR files, which are basically archives… I would have to download something more than text.

I’ll worry about that in a minute.

First, I needed to know the full path, including the filenames, of the API artifacts I wanted.

Lucky for me, since Java was in use, I could take advantage of a **little-known issue** in Java that lets you get directory listings using the `file://` protocol if it ends with a forward slash.

So if I want to list all files in the /etc directory, I just need to pass in “`file:///etc/`“.

With me? Awesome. So I just used my XXE payload several times to traverse the directories until I found the .jar file I needed.

### Downloading binary files through XXE

So JAR and WAR files are just renamed ZIP archives. Trying to use normal text-based XXE to download them won’t work.

Remember, it is UTF-8, not a binary stream.

However, with a bit of patience and some luck, I found a workaround.

In this case, the API server was built upon a base image that included PHP binaries. I took advantage of that and used the built-in PHP filters to base64 encode the file before exfiltrating it.

The payload was adjusted accordingly:
  
  
  <!DOCTYPE danawuzhere [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/path/to/jar/file"> ]>

And with that, I could download the API artifacts I needed.

## Getting to the source

Let’s recap.

So far, we’ve tainted a request to send the API server something it wasn’t expecting, which returned to us the compiled assets of the API we wanted. Now to get to the source code.

With the JAR file exfiltrated from the server and base64 decoded, I decompiled it back to a reasonable representation of the source code.

Tools like [JD-GUI](https://github.com/java-decompiler/jd-gui) and [JD-CLI](https://github.com/intoolswetrust/jd-cli) can do this.

Once decompiled, running simple source code auditing tools like [graudit](https://github.com/wireghoul/graudit) lets us peek into potentially suspicious code. In my case, I have some custom auditing tools that parse out URL fragments from source code… leading me to discover the new code.

From there, I was able to hone in on the undocumented API endpoints, the expected models and schema, and the corresponding business logic within the API that used the external banking API.

## Time to rake in billions

I won’t bore you with the gory details, but the developers were right… they weren’t ready to release the code to this new functionality.

I can’t disclose what was found, but it is fair to say that both the third-party vendor and this customer had to review their threat models and make some changes.

More importantly… and what was more fun… was that because I immediately reported this vulnerability when I did and provided a reasonable PoC exploit for my findings, I was asked to participate in some testing with the third-party vendor on a safe test environment that wouldn’t impact real accounts.

I couldn’t help it. I just had to do it.

With a few keystrokes, I updated my exploit to handle significantly more rogue transactions and ultimately transferred 1 billion dollars to my test account.

![](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/12/image-1.png?resize=972%2C500&ssl=1)

It felt so good to send the screenshot of the account balance to the vendor. It was the perfect digital bank heist.

Unfortunately, it just wasn’t real money. 

**Damn my ethics.** Why did I report this again?**🤣**

## **Conclusion**

In all seriousness, I hope this story resonates with you. And I hope you learned something.

Trust, but verify.

Taint all the things.

Don’t give up.

Be patient.

You’d be surprised what you might find.

## One last thing…

![API Hacker Inner Circle](https://i0.wp.com/danaepp.com/wp-content/uploads/2023/09/image-19.png?resize=94%2C94&ssl=1)

Have you joined **The API Hacker Inner Circle** yet? It’s my FREE weekly newsletter where I share articles like this, along with pro tips, industry insights, and community news that I don’t tend to share publicly. If you haven’t, subscribe at [https://apihacker.blog](https://apihacker.blog/).

### Share this:

  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire?share=linkedin)
  * [ Share on X (Opens in new window) X ](https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire?share=facebook)
  * [ Print (Opens in new window) Print ](https://danaepp.com/that-time-i-broke-into-an-api-and-became-a-billionaire#print?share=print)
  * 

![Dana Epp](https://danaepp.com/wp-content/uploads/2022/08/danaepp-headshot-1-300x300.jpg)

Dana Epp

Hey, I’m Dana, aka SilverStr. I build and break software for a living, and am a Microsoft Regional Director and Developer Security MVP. I’ve spent decades as a security architect that focuses on helping secure software, data, and infrastructure on both blue and red teams. As of late, I have been focusing more on my offensive tradecraft to help developers and IT administrators see the impact of exploitation on vulnerabilities in their work. This blog is my chance to give back to the community by sharing my experiences and war wounds from the trenches.

← [Finding “dark data” in an API](https://danaepp.com/finding-dark-data)

→ [Exploiting an API with Structured Format Injection](https://danaepp.com/structured-format-injection)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-19_google-maps-api-not-the-key-bugs-that-i-found-over-the-years.md
original_filename: 2020-04-19_google-maps-api-not-the-key-bugs-that-i-found-over-the-years.md
title: Google Maps API (Not the Key) Bugs That I Found Over the Years
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- business-logic
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- business-logic
language: en
raw_sha256: a87972f9ba65f8f0dcc1ea46843d713835f6d0e3f2eb627d06a7aa87937758c0
text_sha256: 05e7b2719ce053e85bcf9937818d35bb4136e85e6553c95aeac6ee4172a6b407
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Google Maps API (Not the Key) Bugs That I Found Over the Years

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-19_google-maps-api-not-the-key-bugs-that-i-found-over-the-years.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `a87972f9ba65f8f0dcc1ea46843d713835f6d0e3f2eb627d06a7aa87937758c0`
- Text SHA256: `05e7b2719ce053e85bcf9937818d35bb4136e85e6553c95aeac6ee4172a6b407`


## Content

---
title: "Google Maps API (Not the Key) Bugs That I Found Over the Years"
url: "https://medium.com/bugbountywriteup/google-maps-api-not-the-key-bugs-that-i-found-over-the-years-781840fc82aa"
authors: ["Ozgur Alp (@ozgur_bbh)"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2020-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4644
scraped_via: "browseros"
---

# Google Maps API (Not the Key) Bugs That I Found Over the Years

Google Maps API (Not the Key) Bugs That I Found Over the Years
Ozgur Alp
Follow
10 min read
·
Apr 19, 2020

286

4

After publishing my blog post Unauthorized Google Maps API Key Usage Cases, and Why You Need to Care and scanner script for it, I got several messages from the security researchers at the community about some inconsistency on my script results/client feedbacks and some potential API bugs related to them. Since these are started to becoming a known issue by some of the researchers, I decided to write a blog post about all the bugs that I found on the Google Maps API’s over the years - of course with the approval of the Google Trust & Safety Team.

Press enter or click to view image in full size
Approval from Google Trust & Safety security team for all of the vulnerabilities I have been reported

After I reported my first bug related to the Google Maps API Keys at the summer of 2018 to a private company, I decided to focus on more of the different authentication schemes Google uses on their Maps services, to see whether different kind of configuration mistakes could have been conducted by the clients which I can find and report. Things I noticed at first to focus on:

Maps services have several different API’s which can be used & has different authentication schemes.
This authentication schemes are covering both API keys and client-id mechanisms such as: https://developers.google.com/maps/premium/apikey/maps-javascript-apikey
Nearly all of the API’s also have a similar version on the JavaScript API’s, which uses different authentication mechanism rather than the other API’s.
#Vulnerability 1 — Referer Controls Doesn’t Matter Sometimes

As mentioned on my previous blog post, “HTTP Referer” controls is one of the main security control which blocks unauthorized usage of the API keys created by other customers. After a customer restricts an API key within application referer controls, Google Maps Servers are not allowing to be used from other applications as well on the normal conditions such as:

Press enter or click to view image in full size
Valid API request within valid Referer header
Press enter or click to view image in full size
Request is blocked because Referer header is not allowed

And on the most of the API’s, this control was also secure when sending without any Referer headers such as:

Press enter or click to view image in full size
Blocking request due to not having Referer header

However this security control is not actually working Staticmap, Streetview and Embed API’s properly and it is possible to bypass the security control without sending any Referer header if the key is enabled on these API’s!

Press enter or click to view image in full size
Deleting Referer header bypasses security control for Staticmap API

I reported this vulnerability at Aug 9, 2018 for the Staticmap and Streetview API’s. While the report at first is triaged, afterwards it is marked as duplicate because the issue is known from the internal team. However, the vulnerability still exist in the production systems after 1.5 years which still endangers customers API key usage security. On this year at Jan 21, 2020; I found out that this vulnerability also exist in the Embed API too while creating my scan script for all the API’s, reported it to the Google and got response as: “We’ve investigated your submission and made the decision not to track it as a security bug, as we already know about this issue.” and the issue still exist on the production. So, if you are using the Staticmap, Streetview and/or Embed API’s or these API’s are activated for any of the key you have on your account; whether you have the necessary referer security controls or not, it doesn’t matter and there is no technology exist for misusing these from attackers perspective. Really neat right?

So for full exploitation, the needed code is on the below. With the help of first line of code, the HTML file doesn’t send any Referer header to the browser and if the used key is allowed for that API, security control is successfully bypassed from another application.

<meta name="referrer" content="no-referrer"/>
<img src="http://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key=YOUR_API_KEY”>

So please know that if you are using these APIs’ on your application, this means that your key can be misused by an attacker. If you do not have any other solutions such as using another API instead of those, I highly recommend that setting up a budget or quota limit for your key for defeating potential over-bill issues: https://developers.google.com/maps/faq. Please note that if your service integration with the Google Maps covers your main business (Such as showing cars on the Map etc.), defining this quota limit may cause a denial of service attack according to this service when over-quota, so please configure it out within evaluating it with different aspects/scenarios.

30/04/2020 Update: Within the contribution of Gerard Arall, we found out that this issue exist on the Embed API just for the basic API endpoints which are free. For the Advanced ones, Referer bypass is not working and Google servers still returns 403. It turns out that even Google Maps Support was unaware of it, cheers to that!

#Vulnerability 2 — Free API Keys for All!

While I was reading documentation for the API’s, I found out that Google uses an API key on one of the pages they have at https://developers.google.com/maps/documentation/maps-static/intro as:

Press enter or click to view image in full size
Google using Google Maps API services

With the HTML code:

Press enter or click to view image in full size
Google’s own API key

So at first look, it seems that application is using a signature within the API key, which is a secure authentication mechanism, since the signatures are created on the back-end within a private api key.

However, deleting this signature value for that API didn’t returned any error:

Press enter or click to view image in full size
Successful response within only API key

Which was also exploitable within chaining #Vulnerability 1, since no referer controls have been conducted for the allowed Staticmap API:

Press enter or click to view image in full size
Scan result for leaked Google Maps API key with gmapsapiscaner

So Google’s own created API key is/was vulnerable to be misused. I reported it immediately (at Feb 22, 2019) and got response as:

Press enter or click to view image in full size

After more supplied information, at first they triaged the vulnerability and afterwards I got response as:

Press enter or click to view image in full size

More than one year is passed and still there is no secure mechanism exist on the production which is mentioned as on the messages to prevent API theft and invalid calls. So if you need to you an API key for Staticmaps, Streetview and/or Embed API’s, no need to create your own keys and having any bills/payments at all. Google’s own free API key exist on advance for you!

#Vulnerability 3— Wildcard Referer Control Bypasses

Except the ones mentioned at #Vulnerability 1, API’s are secure from being misused when used Referer headers. Well, this applied only the ones which are defined as within full domain, without wildcard subdomains. In the explanation, Google defines as:

Any subdomain or path URLs in a single domain, using wildcard asterisks (*): *.example.com/*

So if I want to use any API key for my all subdomains, I need to add it as:

Press enter or click to view image in full size

In theory, while it should only accept subdomains such as test.ozguralp.com or similar ones since only the main domain ozguralp.com and its subdomains were allowed within the stated rules, it was also possible to bypass this security control within the payloads such as:

Press enter or click to view image in full size
Bypassing the control with https://test.com#.ozguralp.com referer

In addition to https://test.com#.ozguralp.com, https://test.com?.ozguralp.com and https://test.com\.ozguralp.com was also working. If you browse directly these URL’s, you can notice that instead of browsing ozguralp.com, you will browse the first part “test.com” which is owned by another company. Due to allowing some special characters on the wildcard part of the subdomains, usage of these API keys from other domains were possible.

Get Ozgur Alp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I reported this vulnerability at Aug 7, 2018; it was triaged and accepted after a few days later, however didn’t got any bounty afterwards with the statement: “The panel decided this issue’s security impact does not meet the criteria to qualify for a reward in the program, so we won’t be issuing a reward at this time.”. When I check this vulnerability recently before the blog post, I saw that this one is patched without any notification from Google to me (Not sure whether notifying reporters exist after patching on their bug bounty process or not) however it so no big deal for me since it is the only vulnerability which is patched yet from the ones I reported!

#Vulnerability 4— Javascript API Authentication Controls

At the year 2018, in addition to API key security controls, it was also possible to use client-id’s if you are a premium plan user: https://developers.google.com/maps/premium/apikey/maps-javascript-apikey

There was also a vulnerability existing on the JavaScript API mechanism that caused misusing other client’s valid client-id mechanism, just similar to misusing the API keys as on the #Vulnerability 1.

I reported this one at Jul 19, 2018; it was triaged and accepted after a few days later, however didn’t got any bounty with the statement as same with the #Vulnerability 3: “The panel decided this issue’s security impact does not meet the criteria to qualify for a reward in the program, so we won’t be issuing a reward at this time.”.

At the present time, since the client-id mechanism is not supported by Google and marked as out-of-date, it is not possible to misuse client-id mechanism on behalf of other companies for now. However, the same authentication/quota mechanism is used within JavaScript API’s, which still makes possible to use it unauthorizedly without any valid API key, at least on your local server.

The vulnerability exist because all the data starts to be gathered from Google Maps servers before authentication request and there is no session control exist within the valid API keys, only server responses are trusted on the client side which could be tampered and easily be abused/fooled. Let’s exploit it step by step.

At first, download the example JS Map HTML code given by Google and open it in a browser: https://developers.google.com/maps/documentation/javascript/tutorial

It can be observed that at first, some tiles of the map is started loading:

Press enter or click to view image in full size

Afterwards, page returned error.

Press enter or click to view image in full size

So without any proper authentication (Without API key), starting to load data got me curious about the security of JavaScript authentication mechanism. When inspected in detail, it could be seen that file automatically sends a request to the https://maps.googleapis.com/maps/api/js/AuthenticationService.Authenticate endpoint with the API key on the URL. Since API key is not valid, server returns error.

Press enter or click to view image in full size
Invalid API key error from JavaScript API

When the same process inspected within valid API key, it could be noticed that server returns body as similar responses with:

Press enter or click to view image in full size
Valid authentication body from JavaScript API

Comparing invalid response with valid one shows that only difference between them is a detailed error message and changed error codes. So if API key is valid, server returns on the body just [1,null,0,null,null,[1]] string for the valid authentication without using any other security mechanism such as cookies, tokens etc.

So for using the JavaScript API without any API key, intercepting the response within the help of Burp Suite as:

Press enter or click to view image in full size

And changing the HTML response body from:

Press enter or click to view image in full size

To:

Press enter or click to view image in full size

Brings a bypass to the security control handled on client-side of the JavaScript code and unauthorized usage of JavaScript API on our localhosts/servers instead of getting error. (Same interception/changing response body step should also be conducted to the request made to https://maps.googleapis.com/maps/api/js/QuotaService.RecordEvent )

Press enter or click to view image in full size
Bypassing authentication mechanism handled on client-side for JavaScript API

In conclusion, no need to pay for also JS API if you are using on your local or internal applications which you also have authorization on changing responses coming to your computer/server traffic.

Conclusion

As a full time bug hunter for over 3 years & 4 year penetration tester experience before that, I observed that maybe %30–40 of the applications/customers I tested ever since uses Google Maps API services on their application integrated. This is a huge number and an indication that Google Maps Services has a lot of customers world-wide. While Google takes their security very seriously as far as I observe from the output with their VRP program, I really do not understand why they fail in terms of authentication/authorization mechanisms on the Google Maps API’s over these years. I hope this blog post can raise awareness for the risks when using Google Maps API’s as a whole.

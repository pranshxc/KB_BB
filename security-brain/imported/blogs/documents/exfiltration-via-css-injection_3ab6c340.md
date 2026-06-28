---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-25_exfiltration-via-css-injection.md
original_filename: 2018-07-25_exfiltration-via-css-injection.md
title: Exfiltration via CSS Injection
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- clickjacking
language: en
raw_sha256: 3ab6c340233a3d2b904fce65ddee98439df2d9d1e5f5c6be6095c4905e4407f4
text_sha256: 4582330adcb2e38a2eac84739f0c3d4e6ccaa5f3e021301d864a531615e8a6f4
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Exfiltration via CSS Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-25_exfiltration-via-css-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, clickjacking
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `3ab6c340233a3d2b904fce65ddee98439df2d9d1e5f5c6be6095c4905e4407f4`
- Text SHA256: `4582330adcb2e38a2eac84739f0c3d4e6ccaa5f3e021301d864a531615e8a6f4`


## Content

---
title: "Exfiltration via CSS Injection"
url: "https://medium.com/@d0nut/exfiltration-via-css-injection-4e999f63097d"
authors: ["d0nut (@d0nutptr)"]
bugs: ["CSS injection"]
publication_date: "2018-07-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5789
scraped_via: "browseros"
---

# Exfiltration via CSS Injection

Exfiltration via CSS Injection
d0nut
Follow
4 min read
·
Jul 25, 2018

330

2

Today’s topic is something that’s already pretty well covered: CSS injections. I wanted to talk about my experience implementing this attack on a real site. As you may have encountered, the situation in which you find a vulnerability may not be the pristine situation many vulnerabilities are originally described in (like XSS but with a WAF). As such, writing about the experiences researchers encounter in real life can give light to practical implementations of preventative mechanisms (or general roadblocks) and bypasses for those blockers.

As some of you may know, I’ve recently taken up bug bounties in my spare time. While doing bug bounties, I’ve had the wonderful opportunity to work with two of the best hackers in the business: 
Behrouz Sadeghipour
 and Brett Buerhaus. While we were hacking away at various targets, nahamsec (Benrouz) messaged me saying they had found a CSS injection but had trouble exploiting it.

The main use for exploiting a CSS injection is data exfiltration from input elements. The input elements we’re mostly concerned with are usually CSRF token input elements as these are commonly placed on the page as type=hidden input elements in forms. This brings us our first problem with exploiting this CSS injection: in both Chrome and Firefox, input[type=hidden] elements do not fetch background-image urls.

The general CSS injection data exfil method is to use css like:

Then, attacker.com would load an iframe with this css injection on it on target.com . attacker.com would then wait for a request to https://attacker.com/exfil/<data>.

Let’s assume the token is csrF. This CSS would trigger a page load on https://attacker.com/exfil/c. Then, we would reload the iframe but with CSS like:

Which would cause a page load at https://attacker.com/exfil/cs. Eventually, after repeating this pattern a few times, the final request to https://attacker.com/exfil/csrF which allows an attacker to learn of the visitor’s CSRF token.

With the specific site that we were looking at, there was, thankfully, no X-Frame-Options specified, which would prevent us from using iframes to exploit the cssinjection in a simple way (you could technically open more tabs.. but that’s really ugly.. and super “noisy”).

The Problem

Ok, so that’s all explained and seems simple enough to implement, what’s the problem? Well, remember that type=hidden input elements don’t actually request those images? It turns out that since almost all csrf tokens in forms are type=hidden which means that it makes directly using the input field to exfiltrate data much harder.

Originally, we looked at other methods we could use to call out from the page but we didn’t find anything simple. We figured that there was another way to do this attack but we just had to figure it out. After some investigating, we learned of ~ and + in CSS which are the general and adjacent sibling selectors.

What the sibling selectors let you do is take an element that shares a common parent and style it based on a CSS query. For example, imagine we had a page like the following:

With the following CSS:

This says (read right to left) “Any p that’s a sibling to a p[color=red] should have color: red .

Get d0nut’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What this selector lets us do is say “if any element is next to an input element that contains the CSRF token, set a background-image it”. We can construct a potential CSS directive by similarly writing right to left on the statement above:

Since there existed a form on our target with elements that were not type=hidden, we were able to cause those elements to make the request on behalf of the CSRF token element.

Press enter or click to view image in full size
Screenshot of the PoC written for our recent CSS injection CSRF token exfiltration report

Lastly, here’s an anonymized version of the PoC that we used for our report: https://gist.github.com/d0nutptr/***REDACTED-SUSPECT-TOKEN***This doesn’t include the server side code as most of that should be pretty obvious (we had the background-image requests set a value on a cookie; this also has the benefit that our PoC won’t work in Safari).

The Future

A couple of the forms on the page were concerning us when we were originally attempting to exploit this vulnerability. Some of the forms only contained hidden inputs. This would mean that we couldn’t use the sibling selector technique because none of the siblings would be able to make a request via background-image for us.

Some research into this problem yielded the following proposed directive in the selectors-4 draft from the W3C. :has() allows you to perform a similar query to the sibling selector with the big difference being that you can make this query from the parent of an element.

For example, in our proof of concept, one could instead have written:

Which says “any form that has a descendant input element with name csrf and value token should have a background-image of <url>”.

This, obviously, would work when all input fields are type=hidden and allow for easier general exploitation of this issue. Currently, this feature hasn’t made it into general support (or any support, for that matter) so it might be some time before we can use this for CSS injection exploitation. It’s definitely something to look out for, though!

Closing Remarks

That’s it for this month’s article. The next article will be either about an event I’m about to participate in at the start of August, or a phishing trick that I (re?)discovered via the macOS Mail Client.

Speaking of events and August, I’ll be in Vegas from August 6th to 13th. I’ll be around at various events during then but if you’re interested, I’d love to meet up :)

See ya next time!

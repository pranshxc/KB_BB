---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-04_journeys-in-quoteless-and-multi-reflection-xss.md
original_filename: 2021-04-04_journeys-in-quoteless-and-multi-reflection-xss.md
title: Journeys in Quoteless and Multi Reflection XSS
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: eedcab090b320364857ec49a66f629fc385616abcec1e1ceb38eac11eec1614c
text_sha256: e9de35586da30998880ff307c019ca57824d283773557aa1f4430fd7ee6f645b
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Journeys in Quoteless and Multi Reflection XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-04_journeys-in-quoteless-and-multi-reflection-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `eedcab090b320364857ec49a66f629fc385616abcec1e1ceb38eac11eec1614c`
- Text SHA256: `e9de35586da30998880ff307c019ca57824d283773557aa1f4430fd7ee6f645b`


## Content

---
title: "Journeys in Quoteless and Multi Reflection XSS"
url: "https://bendtheory.medium.com/journeys-in-quoteless-and-multi-reflection-xss-b1d67bb0c5dd"
authors: ["Bend Theory (@bendtheory)"]
bugs: ["XSS"]
bounty: "250"
publication_date: "2021-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3764
scraped_via: "browseros"
---

# Journeys in Quoteless and Multi Reflection XSS

Journeys in Quoteless and Multi Reflection XSS
Bend Theory
Follow
3 min read
·
Apr 4, 2021

761

2

Cross Site Scripting is a tricky bug to fix and bypasses for these fixes can be even trickier. While there are several ways to remediate or prevent XSS, I want to focus on HTML Entity Encoding and the contextual pitfalls that can occur with this method.

9 times out of 10, HTML entity encoding is going to block your attempts at popping an XSS. The app will render < > & " ' as HTML entities &lt; &gt; &amp; &quot; &apos;and make the reflected content safe and inert.

However, if you ever see this behavior occurring within a Javascript context, this means the HTML encoding solution is being used throughout the page without ensuring that content is being properly encoded for its context. With a well placed backslash and a bit of luck, XSS is sometimes possible without quotes or brackets.

Let’s take a look at an example:

http://example.com/page?q=test123%27%22%3c

Instead of appropriately encoding or escaping in this context (i.e. test123\'\"\x3C) HTML entities are used instead. By adding a backslash, we may be able to break the string and trigger an error.

http://example.com/page?q=test123%27%22%3c%5c

So now, we know it’s possible to break the context of this Javascript string because the injected backslash isn’t escaped. We’re escaping the double quote which essentially leaves us with an unquoted string. There’s not much we can do here, but this is where the luck aspect comes into play. If you can find…

Two reflected parameters
In a Javascript string context
On the same line of code
Using HTML entity encoding and not escaping backslash characters

…Then XSS is likely possible, despite the protections in place! Here’s a real life example of this happening:

https://example.com/savings/thankyou?id=abc%27%3c&num=123%27%3c

Unfortunately, we can’t pop an easy XSS with </script><script>alert(1)</script> or '-alert(1)-' but can we work with this!

We can inject a backslash in the id parameter to break out of our string context. By escaping the quote, the value of id in the code is 'abc\', num: '

Get Bend Theory’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With our second parameter, num, we can take advantage of the newly created string and append a Javascript payload into this “unquoted” context:

https://example.com/savings/thankyou?id=abc%5C&num=};confirm(1);//

Dangit! The reflection context here is a a bit more complex to break out of. We need to break out a string, object, function call, and function definition in order to execute a Javascript payload. Using some trial and error, I ended up with a working payload.

id is simply \ and the payload for num is now this:

-1}});}; alert(1); {$.ajax({//

https://example.com/savings/thankyou?num=-1}});};+alert(1);+{$.ajax({//&id=abc%5C

B00M! XSS 😎

Here’s the step by step explanation from my original Hackerone report:

By adding the \ in id,
we can now break out of what would have been the string context of num with -1 which performs an arithmetic operation on the string.
Next, we close out the data property, the anonymous object, and the function call to $.ajax with the following }});
Then we can close the function context of getCard with a }
Now fully broken out of the restrictive contexts, we can execute XSS: alert(1);
Lastly, syntax errors are cleaned up by rebuilding the context we just broke out of and commenting out the rest {$.ajax({//

I got a $250 bounty for this submission.

Keep your eyes open for weird encoding behaviors and multi-reflections! Param Miner and Reflection are great Burp Extensions to help when trying to exploit an XSS like this one.

If you’re interested in learning more about XSS, come join the Bounty Hunters Discord! https://discord.gg/bugbounty

Lastly, huge shout out to Brute Logic! His blog posts on quoteless and multi-reflection XSS gave me the skills and inspiration I needed for finding and exploiting this bug: https://brutelogic.com.br/blog/multi-reflection-xss/

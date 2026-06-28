---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-08_from-ssrf-to-local-file-disclosure.md
original_filename: 2017-11-08_from-ssrf-to-local-file-disclosure.md
title: From SSRF to Local File Disclosure
category: documents
detected_topics:
- ssrf
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 5c53e91c4d80392c14e1a22ce21bc41905b402da66a995a56f9118358887c760
text_sha256: 6154f262d6f724a42d2ee9010458841b838af16d45fb520021768cfae55db1a8
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# From SSRF to Local File Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-08_from-ssrf-to-local-file-disclosure.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5c53e91c4d80392c14e1a22ce21bc41905b402da66a995a56f9118358887c760`
- Text SHA256: `6154f262d6f724a42d2ee9010458841b838af16d45fb520021768cfae55db1a8`


## Content

---
title: "From SSRF to Local File Disclosure"
url: "https://medium.com/@tungpun/from-ssrf-to-local-file-disclosure-58962cdc589f"
authors: ["Tung Pun"]
bugs: ["SSRF", "Local file disclosure (LFD)"]
publication_date: "2017-11-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6059
scraped_via: "browseros"
---

# From SSRF to Local File Disclosure

From SSRF to Local File Disclosure
Tung Pun
Follow
2 min read
·
Nov 8, 2017

453

5

This blog is written about a bug (I believe), that was found on my last weekend. It located on a website from a private program X on Hackerone.

That website has an API, allows users input their URL and email. In the backend, there is a simulated browser, which tries to open that URL and send the screenshot to user’s email. Actually, I don’t have any idea about that simulated browser, not sure if it is a real one or not. First thing, I inject a requestb.in URL, and the received User-Agent is

Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36

Personally, I am interested in SSRF bug, and this case I have the response, so, I thought that I might have some funs.

After the requestb.in URL, I tried my luck with:

http://localhost
http://0
http://127.0.0.1
https://localhost
http://localhost:8080
http://192.168.0.1

The server accepts these URL, open it and send the result to my inbox. But the received responses areErr: timeout for almost times.

The hard thing is the limited number of URLs to be inputted. So, I couldn’t do the brute-force to test Boolean-based.

OK. Now is the time for the local file:

file:///
file:///etc/passwd
file:///c/
chrome://about
about:addons

These above payloads had been used to injected as URLs. However, this time, the server stopped me and said that they are invalid URLs.

I paused when there are not any ideas in my head.

Get Tung Pun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That night, after a cup of Asahi beer, I decided to brainstorm again.

Is there anything else that I forgot?

Oh, http ? Yes. file ? Yes. chrome ? Yes…. How about other services? ftp ?

Promptly, ftp://example.com has been inserted. It worked. Then, I was confused about which keyword had been filtered on the server. I replaced ftp by file , and it worked also. How so?

Yes. The problem is /// , we only need a couple of / , if there are more than, the server would think it is an invalid URL. Then, I tried with file:// .

Press enter or click to view image in full size

Index of page was in the response. Awesome!

Then, how about /etc/passwd ? Hmm. The URL would be: file://s/etc/passwd

Press enter or click to view image in full size

Awesome, again!!!

And that is my PoC.

I submitted the report to that program; unfortunately, they fixed and said that they aware of that issue and closed as Informative.

Actually, I still don’t really understand that decision, however, I don’t want to argue with triggers, then, it should be fine.

—

If you like my sharing, please consider buying me a coffee. ☕️

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-02_applying-a-small-bypass-to-steal-facebook-session-tokens-in-uber.md
original_filename: 2018-10-02_applying-a-small-bypass-to-steal-facebook-session-tokens-in-uber.md
title: Applying a small bypass to steal Facebook Session tokens in Uber
category: documents
detected_topics:
- xss
- oauth
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- xss
- oauth
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: e8deb043c19e70422ba22f4d4d1cd72da5d023b5afe8f15e748167b31db7d91c
text_sha256: ec2f301962eeae2cc7efea693c94dc286bd41f02ed50d63be9f716f4942f5c26
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Applying a small bypass to steal Facebook Session tokens in Uber

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-02_applying-a-small-bypass-to-steal-facebook-session-tokens-in-uber.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `e8deb043c19e70422ba22f4d4d1cd72da5d023b5afe8f15e748167b31db7d91c`
- Text SHA256: `ec2f301962eeae2cc7efea693c94dc286bd41f02ed50d63be9f716f4942f5c26`


## Content

---
title: "Applying a small bypass to steal Facebook Session tokens in Uber"
url: "https://medium.com/@saamux/applying-a-small-bypass-to-steal-facebook-session-tokens-in-uber-5b9638b7a18c"
authors: ["Samuel (@saamux)"]
programs: ["Uber"]
bugs: ["XSS", "CSP bypass", "OAuth"]
bounty: "2,000"
publication_date: "2018-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5669
scraped_via: "browseros"
---

# Applying a small bypass to steal Facebook Session tokens in Uber

Applying a small bypass to steal Facebook Session tokens in Uber
Samuel
Follow
3 min read
·
Oct 2, 2018

240

1

Press enter or click to view image in full size

It was a Saturday at 2:00 AM, and I was with a friend looking for some security flaws to report on a private show. After searching several things we could not detect anything (the scope was small and the sites mostly static).
Out of curiosity, I thought to change the program and scope, so I started looking for bugs in Uber. Although it is true, Uber has an interesting scope, day by day the best bugs hunters in the world are detecting security flaws in their websites.
It happens that by chance, I entered an endpoint that pointed to an information search in Santiago de Chile, which is the following.

https://www.uber.com/es-CL/blog/santiago/search/

Through this endpoint, an user could do a search for information. As usual (I imagine that many do this xd) I placed an XSS type vector, however, I did not succeed.

Later, I did a test with multiple obfuscated HTML characters, in addition to analyzing the behavior of the front-end and the DOM. I realized that it was possible to inject the characters: smaller and larger than, however when placing a slash, the vector was revoked, also if the vector contained the word “script” it was also deleted.

However, I detected a simple bypass, which was simply to get the slash character by its HTML coding (%2f) and also the script, insert it with lowercase and upper case.

Finally I created the next payload

<%fscripT><script>confirm(document.domain)<%2fscripT>

Finally the XSS has been exploited correctly.

Press enter or click to view image in full size

A couple of days later, I had the opportunity to be at the h1–702 Bug Bounty event. Then, talking to a friend (Stefano @stefanohablando), he told me that there was a mechanism to tunnel the XSS in such a way that he could obtain a Facebook session token from an Uber user’s account and thus obtain the user’s session (This is because Uber allows the login with Facebook, any website that has this mechanism poorly implemented could be affected if there is an XSS vulnerability)

Get Samuel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To perform this procedure it was necessary to make the call with JavaScript to a Facebook functionality which allows an user to extract the token, however, first had to check that Uber had that inappropriate configuration. This was important, since the site www.uber.com is static, the business logic, user sessions etc, it can be noted in the site auth.uber.com

To do the token extraction procedure, you can use the following Facebook Developers functionality.

https://developers.facebook.com/docs/javascript/quickstart/

Press enter or click to view image in full size

With this JavaScript code (if Uber allowed it) I could perform the Facebook Token extraction procedure of an Uber account. As you remember, I had to apply the small slash bypass and the word script to execute this successfully. After several tests we realized that:

Uber did not have an adequate ACL, since it was possible to make the call of the Facebook token contained in auth.uber.com.
The CSP was not implemented correctly in www.uber.com therefore it was possible to make the call to JavaScript code.

Finally, when all the conditions mentioned above were met, an exploit was created which, by sending a malicious link to the victim that was authenticated with Facebook, would obtain that user’s Facebook token. Subsequently, the valid user session would be established, in order to finally obtain the user’s mail and send the UUID to his mail as proof of concept.

In doing all this the victim would get something like the following:

Press enter or click to view image in full size

Thanks Stefano (@stefanohablando) for helping me with the creation of the final exploit, please follow it, thanks again.

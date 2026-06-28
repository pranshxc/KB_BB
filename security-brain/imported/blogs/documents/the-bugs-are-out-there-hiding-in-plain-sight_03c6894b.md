---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-15_the-bugs-are-out-there-hiding-in-plain-sight.md
original_filename: 2019-07-15_the-bugs-are-out-there-hiding-in-plain-sight.md
title: The Bugs Are Out There, Hiding in Plain Sight
category: documents
detected_topics:
- ssrf
- sso
- idor
- command-injection
- automation-abuse
- cors
tags:
- imported
- documents
- ssrf
- sso
- idor
- command-injection
- automation-abuse
- cors
language: en
raw_sha256: 03c6894b5a390992c562a3a3beb050dac113762e2d364656b2386918bd30047a
text_sha256: d17714160f6a7b6b49f7045fd8c080c54e18a562e7ce994571417a808dce98e7
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# The Bugs Are Out There, Hiding in Plain Sight

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-15_the-bugs-are-out-there-hiding-in-plain-sight.md
- Source Type: markdown
- Detected Topics: ssrf, sso, idor, command-injection, automation-abuse, cors
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `03c6894b5a390992c562a3a3beb050dac113762e2d364656b2386918bd30047a`
- Text SHA256: `d17714160f6a7b6b49f7045fd8c080c54e18a562e7ce994571417a808dce98e7`


## Content

---
title: "The Bugs Are Out There, Hiding in Plain Sight"
url: "https://medium.com/a-bugz-life/the-bugs-are-out-there-hiding-in-plain-sight-12d056613ea3"
authors: ["A Bug’z Life (@abugzlife1)"]
bugs: ["IDOR", "SSRF", "Information disclosure", "CORS misconfiguration"]
bounty: "9,000"
publication_date: "2019-07-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5147
scraped_via: "browseros"
---

# The Bugs Are Out There, Hiding in Plain Sight

Top highlight

1

The Bugs Are Out There, Hiding in Plain Sight
A Bug’z Life
Follow
6 min read
·
Jul 15, 2019

1.5K

4

It’s no secret, bug bounty is not an easy field to jump into and be successful. The top hunters likely have years of experience in not only bug hunting, but technology & security in general. The reality is that targets that have bug bounty programs are naturally going be some of the most hardened targets out there because there is incentive for people to find bugs. For those of us relatively new, it’s easy to feel that there is no light at the end of the tunnel, and that our efforts are useless because the targets are too hardened. Since starting bug hunting the beginning of 2019, there has definitely been some frustration, demotivation, and feeling like an imposter. Take a look at many comments by newcomers on places like Twitter, 
HackerOne
’s Hacker101 Discord, and other bug bounty forums — it’s simply very easy to get discouraged and feel that bugs are not out there to be found. While the feelings are understandable, we’re here to say that there are many, many bugs out there to find, and a lot of them are actually very simple. It just requires the right mindset, perseverance, and a little bit of luck.

A lot of bug hunting success and progression comes down to mindset and the way you look at things. When you’re just getting started, focusing too hard on finding any valid bug as your measure of success is an easy way to get discouraged and burnt out. If you’re not at the point where you’re comfortable understanding different bug classes, throwing everything at an application and hoping something sticks is not the best way to set yourself up for success, and you’re most likely not learning much. You should really take a step back, build some fundamentals, and understand what you’re testing for. Having a unique perspective as a triager as well as bug hunter, it’s very clear when someone does not understand the fundamentals or will submit anything and everything hoping for a bounty. They don’t understand why the report is closed as N/A and it’s a negative experience for both parties. If you take a step back and try to understand what the security risk is for the company, and if it’s a valid issue to begin with, you’ll be more likely to understand why your report wasn’t accepted. Just because you’ve found a bug, doesn’t mean it has to be fixed — it may mitigate no security risk for the company in this specific context. Even if you get a duplicate, that is something to be proud of as you just found a valid security vulnerability, and you’re learning is paying off. Having the right mindset will make it a much more enjoyable, and ultimately successful process.

The rest of this post will include some of the bugs we’ve come across in the past few months that are very simple to find, and have been missed by many other skilled bug bounty hunters. As many experienced hunters have said, there are more bugs out there than people to find them. Everyone truly does bring their own unique approach and will catch things even some of the most experienced bug hunters will miss. Also, code is changing daily with companies potentially deploying hundreds of changes each day. Just because a target is “old”, it does not mean that vulnerabilities are not being introduced every day.

(Critical) IDOR #1 — $3,000

This private program has an application that allows for creating your own contacts based on users in the application. Being a B2B-ish application, users should only have access to other users in their organization or be connected in some way.

When creating a contact, you can either manually enter in the information, or also create a contact from an existing user via the following URL: https://company.com/contacts/new?user_id={userId}. This incredibly simple IDOR allows the attacker to change the value in the user_id parameter to any user’s (sequential) ID to get access to all of their PII, including name, email, phone number, location, bio, and more. The application also had roughly 20 million users, meaning the attacker could get this information for all 20 million users in the system. Very simple to find, and very impactful as well.

(Critical) IDOR #2 — $3,000

In the same program as above, another simple IDOR was identified to access user PII for every user in the system. Users can create events for their organization, and add different users to participate in the event. By adding users, you also get access to their PII (same info as above, as well as some additional fields).

In the PUT request to create the event, a contact_ids field existed, which allows the attacker to update the event with a list of contacts. By changing this to any contact outside of their organization, the attacker can bypass the UI restriction and add any contact, getting access to their PII. Funny enough, the application actually returns this error:

{"success":false,"errors":{"contacts":["must belong to the host or owner of the event"]}}

However when refreshing the page, the users added appear regardless. The lesson here is to not blindly trust HTTP responses :)

(Critical) SSRF -> AWS Metadata Service — $1,000

One application allowed for exporting a couple different things to PDF, including a user’s resume. Many PDF generators use an HTML -> PDF conversion, and by entering in some HTML code, you may be able to get the application to run that code on the server side.

Get A Bug’z Life’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So by injecting <iframe src="http://169.254.169.254/latest/meta-data"> in the user’s resume, the application then runs that when generating the PDF. In this case, the server made a request to the AWS metadata service, and displayed that iframe in the PDF that was exported, allowing us to steal AWS credentials!

AWS Metadata service accessible through iframe in PDF generation
(High) CORS Misconfiguration — $1,500

A site-wide CORS misconfiguration was in place for an API domain. This allowed an attacker to make cross origin requests on behalf of the user as the application did not whitelist the Origin header and had Access-Control-Allow-Credentials: true meaning we could make requests from our attacker’s site using the victim’s credentials. The API domain returned a bunch of sensitive info regarding the user, the user’s organization & its users, and more. Some PoC code for displaying CORS related vulnerabilities can be found below (simply update the URL in xhr.open with the vulnerable URL):

<html>
  <body>
  <h2>CORS PoC</h2>
  <div id="demo">
  <button type="button" onclick="cors()">Exploit</button>
  </div>
  <script>
  function cors() {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
  document.getElementById("demo").innerHTML = alert(this.responseText);
  }
  };
  xhr.open("GET",
  "https://api.company.com/endpoint", true);
  xhr.withCredentials = true;
  xhr.send();
  }
  </script>
  </body>
 </html>
(Low) Forced Browsing — $500

This bug was in HackerOne itself, which allowed for an attacker to view a HackerOne challenge scope before the challenge begins. A HackerOne challenge is a temporary private program, of which the scope is not displayed until the event begins. Viewing the scope before it begins gives an unfair advantage as it allows the attacker to do recon and test for bugs before the other hackers know what the scope is, which could easily manipulate the results of the challenge.

All an attacker had to do is visit the challenge’s scope_versions page to view the scope that was hidden from the program policy page: https://hackerone.com/h1challenge_name/scope_versions

By navigating to that URL, the exact assets in scope appeared. Usually the hackers with higher reputation & experience get invited to challenges, so this had the potential to be found by many top hackers and was missed. This report can be found here.

Conclusion

We hope these examples helped paint the picture that high impact, easy to find bugs are out there! Some of these targets have been around for years, and the bugs were simply missed by everyone looking at them. Everyone has their own unique perspective, and you will find things other people miss. It’s really easy to get discouraged if you go into this with the wrong mindset. Your learning and perseverance will eventually pay off if you keep the right mindset and focus on the right areas. There are plenty of bounties out there for everyone, it’s just a matter of persistence and keeping your eyes open :)

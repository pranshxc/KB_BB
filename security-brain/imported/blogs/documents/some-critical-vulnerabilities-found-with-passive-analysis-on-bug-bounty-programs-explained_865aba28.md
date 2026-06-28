---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-07_some-critical-vulnerabilities-found-with-passive-analysis-on-bug-bounty-programs.md
original_filename: 2022-03-07_some-critical-vulnerabilities-found-with-passive-analysis-on-bug-bounty-programs.md
title: Some critical vulnerabilities found with passive analysis on bug bounty programs
  explained
category: documents
detected_topics:
- information-disclosure
- command-injection
- otp
- rate-limit
- automation-abuse
- business-logic
tags:
- imported
- documents
- information-disclosure
- command-injection
- otp
- rate-limit
- automation-abuse
- business-logic
language: en
raw_sha256: 865aba289f33f53d252fdf0a9029bd3e7dd29600aee5dbb9d02635be4a9cb322
text_sha256: 16f21fca1a639ddefa6ca6f4339d71ac41737d7661bef7d6372e994faec2eec2
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Some critical vulnerabilities found with passive analysis on bug bounty programs explained

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-07_some-critical-vulnerabilities-found-with-passive-analysis-on-bug-bounty-programs.md
- Source Type: markdown
- Detected Topics: information-disclosure, command-injection, otp, rate-limit, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `865aba289f33f53d252fdf0a9029bd3e7dd29600aee5dbb9d02635be4a9cb322`
- Text SHA256: `16f21fca1a639ddefa6ca6f4339d71ac41737d7661bef7d6372e994faec2eec2`


## Content

---
title: "Some critical vulnerabilities found with passive analysis on bug bounty programs explained"
url: "https://infosecwriteups.com/some-critical-vulnerabilities-found-with-passive-analysis-on-bug-bounty-programs-explained-1da8b01c11ad"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2022-03-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2849
scraped_via: "browseros"
---

# Some critical vulnerabilities found with passive analysis on bug bounty programs explained

Some critical vulnerabilities found with passive analysis on bug bounty programs explained
Daniel "V" Morais
Follow
6 min read
·
Mar 7, 2022

133

3

This post describes three vulnerabilities found by me on bug bounty programs along with an overview about how it was found and the performed steps. The main goal of this post is to show how to find critical/high vulnerabilities without touching the company’s assets or tampering with the requests. I hope you like it and find something useful!

Reports:
The exposed endpoint containing the invitation URL of enterprise accounts allows attackers to join the company as an employee.
Able to claim the ownership of Calendly third party service from [redacted] due to an unused calendar being mapped on the Contact page, which leads to managing scheduled client’s calls with the support team.
Source code leaked and sensitive information disclosure on public [redacted] company IP with an uncommon opened port found via Shodan analysis.
Descriptions:
1. Exposed endpoint containing the invitation URL of enterprise accounts allows to join to the company as an employee.

During the OSINT analysis, one of the first steps that I take is to retrieve the target endpoints and URLs crawled by third parties, this can be done with open-source tools such as gau and the command below:

printf target.com | gau

After that, I start to MANUALY analyze the endpoints and URLs from the output, paying particular attention to some sensitive keywords:

invoice, discount, promo-code, redirect, reset_password, reset-password, password, TrackOrder, token, invite

And for this one, the invite keyword suddenly took my attention on the target’s endpoints:

Press enter or click to view image in full size
output results from gau tool

I just clicked on the suspicious URL and it took me to a SIGN-UP page, and after creating a new account with a personal email (@gmail.com) then I just were redirected to the company’s page inside the target application, containing all the invited employees and sensitive information as well:

Press enter or click to view image in full size
sign-up page that lead me to access company’s team
Press enter or click to view image in full size
PII information from employees
Press enter or click to view image in full size
Sensitive data from company

Impact:

Any user could sign-up as an employee on the target app service using the URLs being mapped on different crawlers, which would disclosure PII and sensitive information about the company for the attackers.

Steps were taken to find this vulnerability:

Searched for all company assets available under scope using open-source tools (subfinder, amass…)
Used gau tool to retrieve a list of URLs and endpoints from the discovered domains
Grepped the results containing sensitive keywords, which in this case it was ‘invite’ grep -r "invite"
Manually accessed the URLs to see their content, and followed the page instructions, which lead me to Sign-up as an employee for many different companies registered under the affected target app.
2. Able to claim the ownership of Calendly third party service from [redacted] due to an unused calendar being mapped on the Contact page, which leads to managing the scheduled client’s calls with the support team.

Upon accessing the target for the first time, I generally like to analyze the whole structure of the application before attacking it. After just like 5 minutes of interacting with the different pages, I clicked on a calendar icon on the bottom left side of a Contact page and it ended opening up a blank page with an error from Calendly’s service:

Press enter or click to view image in full size

By inspecting the page, I was able to see a GET request to target-v2/call which comes to be the registered calendar name from the third-party service Calendly. I immediately signed up a new account there, created a new calendar, and then it asked me for a unique name that would be attached to the URL, so I automatically thought about takeovers attacks.

I provided target-v2 as the name of the Calendar, proceeded with the creation and boom!

Press enter or click to view image in full size
Calendly service takeover on target’s contact page

My newly created calendar were displaying at the contact page from the target’s domain, so if anyone scheduled a call with the support team, they would be actually scheduling with me (attacker).

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Impact:

Any user could takeover the third party service calendar being used to schedule support calls to the target company, this allowed attackers to easily perform phishing attacks and manage all the scheduled calls with target’s clients.

Steps taken to find this vulnerability:

First I manually analyzed the application functionalities and pages as a normal user
Then I found on the Contact page, a third party integrated app as a scheduling calendar (Calendly service)
Finally I thought about a possible takeover of calendars from this platform. For this, I signed up a new account, studied the creation of calendars, and then I registered the name used by the target app as my new calendar.
Instantly my calendar got linked to the Contact page from the target app, and then scheduled calls with the target support team were now totally managed by me (attacker).

3. Source code leak and sensitive information disclosure on public [redacted] IP with an uncommon opened port found via Shodan analysis.

This last one was found during a manual Shodan analysis of the target app. I started with the below Dork just to grab more info about the target:

ssl:target.com

Press enter or click to view image in full size

and manually looked for uncommon opened ports by accessing the “View Report” option. Suddenly there was one host with the port “9869” opened, which I instantly tried to access and it lead me to a password protected page in order to access the content from the page:

Then I did a bruteforce attack to find directories and endpoints using ffuf tool, which gave me good results:

Press enter or click to view image in full size

After getting a response for the share endpoint, I access it and from there it was possible to access the source code from company’s project in a directory listing:

Press enter or click to view image in full size

Impact:

Any user on the web could find this service exposing sensitive company files such as projects data and source code.

Steps taken to find this vulnerability:

Started with a simple Shodan dork to filter all domains matching the company SSL certificate name
Manually searched for uncommon open ports
Accessed them and there was one host which lead me to a password protected page (highly suspicious)
Started a brute force attack using ffuf tool to discover possible hidden endpoints/directories to bypass the password page and found one
Accessed the endpoint share and the sensitive files were there.

Takeaways:

Always perform a passive analysis over the target app using as much tools/research/dorks as possible, and there are a lot of them actually on the github, bb tips and so. One thing I learned was that as bigger the company is, the more OSINT results you`ll get, and of course, the more chances you’ll have to find a critical vulnerability such as the ones here on this article.

Daniel_v

Vendetta team

Twitter | BugCrowd Profile | H1 Profile | Linkedin

The Infosec Writeups team just completed our first Virtual Cybersecurity Conference and Networking event. We had 16 amazing speakers who conducted super valuable and inspiring sessions. To check the list of speakers and topics, and to get lifelong access to recorded versions of all 16 talks, click here.

IWCon2022 — Infosec WriteUps Virtual Conference
Network With World’s Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live

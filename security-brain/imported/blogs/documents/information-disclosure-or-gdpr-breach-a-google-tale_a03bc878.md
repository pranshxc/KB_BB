---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-10_information-disclosure-or-gdpr-breach-a-google-tale.md
original_filename: 2023-02-10_information-disclosure-or-gdpr-breach-a-google-tale.md
title: Information disclosure or GDPR breach? A Google tale…
category: documents
detected_topics:
- rate-limit
- command-injection
- automation-abuse
- information-disclosure
- mobile-security
tags:
- imported
- documents
- rate-limit
- command-injection
- automation-abuse
- information-disclosure
- mobile-security
language: en
raw_sha256: a03bc8789dc304b9d0edadcde7f4e8c1d083c549256cbd15c7707b86040a6983
text_sha256: a5234a418a067b3962c0b58c9248aacd3414130931c7b262b8f97ae76ce6aef2
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Information disclosure or GDPR breach? A Google tale…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-10_information-disclosure-or-gdpr-breach-a-google-tale.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, automation-abuse, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `a03bc8789dc304b9d0edadcde7f4e8c1d083c549256cbd15c7707b86040a6983`
- Text SHA256: `a5234a418a067b3962c0b58c9248aacd3414130931c7b262b8f97ae76ce6aef2`


## Content

---
title: "Information disclosure or GDPR breach? A Google tale…"
url: "https://medium.com/@lukeberner/information-disclosure-to-gdpr-breach-a-google-tale-f9e99fd5d648"
authors: ["Luke Berner"]
programs: ["Google"]
bugs: ["Privacy issue", "Information disclosure", "Missing authentication"]
bounty: "500"
publication_date: "2023-02-10"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1550
scraped_via: "browseros"
---

# Information disclosure or GDPR breach? A Google tale…

Information disclosure or GDPR breach? A Google tale…
Luke Berner
Follow
6 min read
·
Feb 10, 2023

174

1

This is a vulnerability I reported back in April, 2022

I had already reported a vulnerability on googlesource.com (Google's Gerrit), so I was already familiar with the topic.
To summarize, googlesource.com is a Google service that provides access to both open-source projects maintained by Google as well as internal projects. If you append “-review” to the subdomain, you can access the Gerrit version of the site.

The one that initially caught my attention was chrome-internal, because as the name says, should be internal right?

Press enter or click to view image in full size
nothing to see over here, all empty…

When I accessed it, the page was empty. Seems like Google shows the UX for every internal subdomain/project, but limits the content shown depends on the user’s role.. Makes sense.

However, when doing bug bounty, they say curiosity is key. When presented a scenario like this, I just start poking everything by instinct. And by everything I mean everything, even the most basic/obvious features. Always aiming to:

understand how it works (+ analysing with Burp),
checking if something shouldn't be there.

The search bar immediately attracted my attention. It appeared harmless, but why was it returning information if I had no access to anything related to chrome-internal?

Press enter or click to view image in full size
looks like Luke is more common than expected

From the technical-side of things, the search API returned a JSON with the following information of the first 10 accounts found:

{
  {
  "_account_id": {redacted}, // accountID
  "name": "Luke Berner", // full name
  "email": "lukeber4@gmail.com", // email 
  "avatars": [
  {
  "url": "https://lh3.googleusercontent.com/{redacted}/{redacted}/{redacted}/{redacted}/photo.jpg",
  "height": 32 // photo 32x32
  },
  {
  "url": "https://lh3.googleusercontent.com/{redacted}/{redacted}/{redacted}/{redacted}/{redacted}/photo.jpg",
  "height": 56 // photo 56x56
  },
  {
  "url": "https://lh3.googleusercontent.com/{redacted}/{redacted}/{redacted}/{redacted}/{redacted}/photo.jpg",
  "height": 100 // photo 100x100
  },
  {
  "url": "https://lh3.googleusercontent.com/{redacted}/{redacted}/{redacted}/{redacted}/{redacted}/photo.jpg",
  "height": 120 // photo 120x120
  }
  ]
  },
  {[...]}
}

As I saw some @google.com emails, I went ahead and reported it. Looked like a basic Information Disclosure report, but in these cases I prefer to report just in case and, worst case scenario, "Working as intended". And indeed, 10 days after being identified as an Abuse Risk and triaged by Trust & Safety team, that happened:

Press enter or click to view image in full size
"Working as intended"

However, as always, one needs to try and go deeper (if reasonable). At first Google's answer sounded logical, but then I kept on analysing this feature, exploring the API and noticed something that I had overlooked: I was appearing in the search results.

I had just logged in, did no contributions/collaborations whatsoever. Only action I did was hit the Google log-in button. So I started working on the premise: are all users that logged in being exposed? Suddenly the following answer was not accurate:

It looks like this is actually working as intended and is a feature of the product which allows users to search for:
Changes containing a top-level or inline comment by ‘USER’, or owned by ‘USER’.

So I explained that per their product documentation I shouldn't appear there, and asked the following:

ME: "[…] definitely not going for a 'Phishing campaign attack scenario' here, but is Google ok in leaking every 'Email & Name+Surname' of everyone who logged into every googlesource.com subdomain available?"
Google: "That’s a good question, so I’ve filed a bug with the responsible product team […]"

A few days latter, my report got accepted and I received a $500 award.

However, as you can see from my question, I also went deeper on how to exploit their API, discovering a few things before re-opening the report:

Every *.googlesource.com subdomain seemed vulnerable.
There was no authentication required to abuse the API. No authentication needed at all.
There was no throttling either.
The search API returned the first 10 results but you could get up to 100 results per query.

After reading the user-search docs, and while Google was already working on the fix, I went ahead and created a script to automate the leak. My assumption was that the issue could be worse than what was initially thought.

The search API accepted minimum 3 letters to return up to 100 results, so I crafted all combinations possible and brute-forced chrome-internal-review.googlesource.com users.

Press enter or click to view image in full size
ChatGPT explanation: This is a Python script that performs a brute-force search for valid Google Source accounts. The script starts by creating a list of all possible 3-letter combinations of keywords from a predefined list of characters including lowercase letters and digits. For each combination, the script sends a GET request to the URL with the current combination as the query and a fixed n value of 100, which represents the maximum number of results to return. If a valid response is received, it extracts the JSON data from the response text, saves it to a dictionary, and writes it to a file named "chrome-internal_leak.out".

I was surprised by the results after running the script. It took between 45 to 60 minutes to go through all the possible combinations, and I wasn’t blocked at any point. Result returned tens of thousands of accounts.

Get Luke Berner’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While waiting on Google's answer, I went ahead and re-submitted this new information. Figured out the API also allowed pagination, so 100% of the user base could be leaked (not limited to 100 per query anymore). The results were shocking:

there were lots of @google.com accounts found with just 3-letter combinations limited to 100 results per query (+12k unique accounts),
there were lots of personal accounts (@gmail.com, @hotmail.com, etc),
there were corp-partners accounts too,
and there were companies accounts as well (@intel.com, @hp.com, @samsung.com, etc).

These results were all unique accounts, and just for one subdomain. Each one of them having full_name, email and picture.

Press enter or click to view image in full size
Capture of message sent to Google. All results are unique accounts, with full_name, email and picture.

Considering the following:

The scenario involves unauthorized access to personal data through a Google service that required no login and returned full name, email address, and photo of individuals who have logged into the service.
Affected people data were both personal (gmail/hotmail) and private/work (companies like intel/hp/samsung/sap/google)
One of the fixes acknowledged it: “We will add a feature to Gerrit for individual users to hide themselves. They will be hidden by default, and must unhide themselves when they submit content. We will then analyze historical data to hide any user that never submitted content.”
It affected more/all Gerrit instances: “we started working on this wider issue (Gerrit instances other than chromium-internal) just recently”

I started to question them… "Wouldn’t this be breaching GDPR in European companies/countries?"

Press enter or click to view image in full size
Google results, and ChatGPT because why not?

There were a total of 33(!) replies to my report -from both sides- and, after having asked explicitly 3 times about this being a GDPR breach or not, I received the message that this was finally fixed.

At some point, I also pinged a Privacy Engineer from Google through LinkedIn trying to see if there was an official place to report these possible GDPR breaches. Received an email, and sent them the information and link to the issuetracker bug report.

When commenting them I was going to write a post about it, I asked them for an official answer to "Why this was not a GDPR breach":

"On googlesource.com, we offer source code review to partners, both companies and individuals. Code review is a collaborative process that requires discovering new people to interact with.

We take our partners’ privacy very seriously and are constantly improving our infrastructure to meet this bar. We therefore took your report as an opportunity to deliver an experience that better aligns with customer trust expectations, by tightening visibility controls even further. Thank you again for helping improve the service we offer to partners."

Summary of timeline:

15.04.2022: Vulnerability reported
16.04.2022: Identified as an Abuse Risk and triaged to our Trust & Safety team
26.04.2022: "working as intended"
26.04.2022: "[…] is Google ok in leaking every 'Email & Name+Surname' of everyone who logged into every googlesource.com subdomain available?"
23.05.2022: "That’s a good question, so I’ve filed a bug with the responsible product team […]"
24.05.2022: $500 bounty received
25.05.2022: Asked if this could be a GDPR breach
16.06.2022: Submitted more information + python script that leaks users, re-asked about GDPR breach
16.08.2022: Re-re-asked about GDPR breach
17.08.2022: Submitted a new script that could get more results per query (not the 100), allowing it to leak 100% of users per subdomain.
18.08.2022: Pinged a Privacy Engineer @ Google through LinkedIn, explained the situation and got a privacy-google email to report the possible GDPR breach.
25.08.2022: Partially fixed
22.11.2022: Fixed
07.02.2023: Re-re-re-asked about GDPR, asked for an official answer for the blog post
10.02.2023: Official answer received

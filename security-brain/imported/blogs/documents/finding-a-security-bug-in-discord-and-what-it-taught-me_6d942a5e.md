---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-24_finding-a-security-bug-in-discord-and-what-it-taught-me.md
original_filename: 2019-11-24_finding-a-security-bug-in-discord-and-what-it-taught-me.md
title: Finding a security bug in Discord and what it taught me
category: documents
detected_topics:
- api-security
- oauth
- command-injection
- otp
tags:
- imported
- documents
- api-security
- oauth
- command-injection
- otp
language: en
raw_sha256: 6d942a5e60c74c545c5be2cb1e23ac628eb73180188e06099fa05914bdd14c7a
text_sha256: ccb0d806bc2ca6f7bbb87a072cf610d8607df1dfc4f3c30916e3f325c9aab5dc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Finding a security bug in Discord and what it taught me

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-24_finding-a-security-bug-in-discord-and-what-it-taught-me.md
- Source Type: markdown
- Detected Topics: api-security, oauth, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6d942a5e60c74c545c5be2cb1e23ac628eb73180188e06099fa05914bdd14c7a`
- Text SHA256: `ccb0d806bc2ca6f7bbb87a072cf610d8607df1dfc4f3c30916e3f325c9aab5dc`


## Content

---
title: "Finding a security bug in Discord and what it taught me"
url: "https://medium.com/@tristanfarkas/finding-a-security-bug-in-discord-and-what-it-taught-me-516cda561295"
authors: ["Tristan Farkas (@TristanAtFarkas)"]
programs: ["Discord"]
bugs: ["OAuth"]
publication_date: "2019-11-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4918
scraped_via: "browseros"
---

# Finding a security bug in Discord and what it taught me

Finding a security bug in Discord and what it taught me
Tristan Farkas
Follow
3 min read
·
Nov 24, 2019

48

1

On the 10th of November, I was looking through some of Discords documentation for OAuth because of a project I’m working on when something interesting caught my eye, the “Client Credentials Grant” system for quickly retrieving an OAuth token for testing purposes. Now I had never used this system before, but the gist of it is that you make a request to an API endpoint with a client id and client secret, and you receive the OAuth token for the application owner that can be used for quick testing thanks to it not requiring the user to go through the OAuth flow. And a thought popped into my head, what would happen if I used an application that was not owned by a single user but rather a Team, teams on Discord are groups of users that own application(s) that they together manage. So let’s see what happens when I make a client_credentials request for a team project

Press enter or click to view image in full size
Would you look at that

So it seems we get an access_token we can use, let’s check and see if it works:

Press enter or click to view image in full size
The user object we receive when making a request to the API using our team’s access_token.

So this is getting interesting, this shows that we’re able to make requests on behalf of our team and that a team just seems to be a managed User object. I tested a few different endpoints until I decided to see if I was able to join this managed user object to a server/guild. So let’s use the Add Guild Member endpoint to see if we can accomplish that. And the request went through successfully? At first, I didn’t believe the response I received, but when I went back and checked in the Discord client and,

A team user object in a server?

This user object was causing all kinda weird issues with my client,

Parts of the API thought this user existed, other parts didn’t agree with them.
Press enter or click to view image in full size
Here it did exist!

At this point, I reached out to Discords Bug Bounty Program, and a few days later a Discord employee replied to my report and quickly addressed the issue. This was one of the better bug bounties I’ve taken part in, and I want to thank the amazing team over at Discord for handling this very professionally. I got the OK from their team yesterday evening that I was free to disclose this and so here we are. In the past when I’ve looked for vulnerabilities in software I’ve done so on purpose, in this case, it was just a random thought that put me on the track to find this security bug. And I believe that might be the most effective way to find bugs because you don’t end up wasting a bunch of time looking for issues that might not exist.

Get Tristan Farkas’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s all for me, thanks for taking your time to read through this, and if you’re interested in this kind of stuff, feel free to follow me over at Twitter: https://twitter.com/tristanatfarkas where I occasionally talk about this stuff!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-22_ssrf-google-hofhall-of-fame.md
original_filename: 2022-08-22_ssrf-google-hofhall-of-fame.md
title: SSRF & Google HOF(Hall of Fame)
category: documents
detected_topics:
- supply-chain
- ssrf
- command-injection
- path-traversal
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- ssrf
- command-injection
- path-traversal
- api-security
- mobile-security
language: en
raw_sha256: 1eb282b32be43b5bb2aa2f0ce085afd16976491b0905e6f0b2e60968ea6e4f72
text_sha256: f99ba3e281197b743f3ebf8485e8f13ebd42b795fef12c807578845327efccac
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF & Google HOF(Hall of Fame)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-22_ssrf-google-hofhall-of-fame.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, command-injection, path-traversal, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `1eb282b32be43b5bb2aa2f0ce085afd16976491b0905e6f0b2e60968ea6e4f72`
- Text SHA256: `f99ba3e281197b743f3ebf8485e8f13ebd42b795fef12c807578845327efccac`


## Content

---
title: "SSRF & Google HOF(Hall of Fame)"
url: "https://apth3hack3r.medium.com/ssrf-google-hof-hall-of-fame-2c159dda04e3"
authors: ["Aman Pareek (@aman_notsogreat)"]
programs: ["Google"]
bugs: ["SSRF"]
publication_date: "2022-08-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2278
scraped_via: "browseros"
---

# SSRF & Google HOF(Hall of Fame)

SSRF & Google HOF(Hall of Fame)
Aman Pareek
Follow
3 min read
·
Aug 22, 2022

312

1

Update: I tried explaining the impact again and again to google with some reference reports and proved that the mentioned endpoint was indeed used in production environment.
And finally they replied with a reward of $1337.

This time I will talk about a very interesting SSRF(Server Side Request Forgery) on a Google asset and interesting because the way I found the endpoint. Read below to find out.

Note: I am assuming that you know what SSRF and Dependency Confusion attack are, so if you are not familiar with these terms kindly google and get familiar with them.

In February this year, I decided to hunt on google but Iwanted to do things in different manner because with cliched methods I will get what everyone else is getting. So I decided to hunt for Dependency confusion through GitHub accounts belonging to google for their open source projects, which was a bad idea, because it is highly unlikely that you are gonna find something of that sort. So I searched for package.json files for some GitHub account and came across this particular file which looked like this:

Press enter or click to view image in full size
package_json_file

Nothing special in this, I know, and that’s why I, out of curiosity, decided to check other files. And there was a index.ts file which had reference to some other files like logger.ts and licenses.ts and there was a route defined in index.ts like this:

Now we need some domain where this was deployed and luckily in comments or in readme file there was an appspot.com URL where this project was deployed:

Press enter or click to view image in full size

Why am I hiding the domain?
Since all this is open source just take it as a challenge or practice to find the repository and subsequently the-domain.

Get Aman Pareek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I sent a POST request to /convert/licenses in response body there was a message that URL parameter is missing and the moment I saw this i was like SSRF. And then I sent a post request to same endpoint with url parameter in request body as JSON:

Press enter or click to view image in full size

And the result was LFI due to SSRF because there was no check on URI schema used.

Why no bounty?

Even I was expecting some bounty for this but Google VRP had justification for this:

Press enter or click to view image in full size

Timeline:

Reported 22/02/2022 13:31
Triaged 22/02/2022 14:12
Accepted 22/02/2022 15:47
HoF Awarded 08/03/2022 22:26
Bounty Mail 14/10/2022 00:27

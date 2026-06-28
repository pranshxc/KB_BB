---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-09_how-often-do-we-overlook-vulnerabilities.md
original_filename: 2020-09-09_how-often-do-we-overlook-vulnerabilities.md
title: How often do we overlook vulnerabilities?
category: documents
detected_topics:
- command-injection
- graphql
- information-disclosure
tags:
- imported
- documents
- command-injection
- graphql
- information-disclosure
language: en
raw_sha256: 501fd591d6a50c2bcff3dddd0eeaabf603701a8877ab4b93653f987d36270faf
text_sha256: 33079ea3eae0b86ffd5ddb3f1e126ca1ee8cb47141278a9eb2b8a91322e77fbb
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How often do we overlook vulnerabilities?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-09_how-often-do-we-overlook-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `501fd591d6a50c2bcff3dddd0eeaabf603701a8877ab4b93653f987d36270faf`
- Text SHA256: `33079ea3eae0b86ffd5ddb3f1e126ca1ee8cb47141278a9eb2b8a91322e77fbb`


## Content

---
title: "How often do we overlook vulnerabilities?"
url: "https://medium.com/infosec/how-often-do-we-overlook-vulnerabilities-960a7c45f59"
authors: ["Baibhav Anand (@SpongeBhav)"]
programs: ["HackerOne"]
bugs: ["Information disclosure"]
publication_date: "2020-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4271
scraped_via: "browseros"
---

# How often do we overlook vulnerabilities?

Baibhav Anand
 highlighted

How often do we overlook vulnerabilities?
Baibhav Anand
Follow
4 min read
·
Sep 9, 2020

646

1

Press enter or click to view image in full size

Hello Readers,
“7/10 vulnerabilities are often overlooked by hackers.” -Aristotle. I don’t know if that’s true, I just made that up. Anyway, This article is based on my recent finding in HackerOne/security.

There is a feature on HackerOne which allows program managers to assign the reports to a team member of their choice.

Press enter or click to view image in full size

When chosen to assign the report we get the list of team members and groups in our program to chose from, whom we want to assign this report to.

A GraphQL query was made to the server to fetch the team members and groups for our team.

Press enter or click to view image in full size

The reportIds variable in this mutation immediately caught my attention and I noticed that it contained the report ID of the report of my program of which I was trying to assign a team member to.

I went to my inbox and selected a report for a program I didn’t own and copied its report ID and pasted that in the reportIds value in the graphQL mutation.

The response revealed all the team members of the program. This is the exact data I got of all team members:

Press enter or click to view image in full size

I don’t see any sensitive data here but the fact that I could disclose the team members of any programs still felt like something I should report.

I reported it to them and the report gets closed as duplicate to an informative report. I was added to the original report and this is the reason why the original report was closed as informative :

Press enter or click to view image in full size

I wasn’t totally satisfied with this since there was so much of data, there must be at least something that might not be publicly available information.

Get Baibhav Anand’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I started brute-forcing the query parameters to see if I can extract any more data from what it is already showing. When I saw the email parameter was valid. I was literally shaking because I thought I was able to reveal email address of all the team members for all the programs.
But I was wrong :

Press enter or click to view image in full size

Email was indeed a valid parameter but the value I got was always null for all the programs except for my own program.

At this point I didn’t want to dig in any further but still I gave a quick glance at the information I was receiving and I started to check some profiles and I noticed for some profiles I got page does not exist error. It didn’t take me to long to realize that the value for name is also null in those profiles which I was not being able to open.

Press enter or click to view image in full size

Now again I switched to the data for my program and then I realized that these were actually API-Identifiers and most of them were not public. So the new report becomes API Identifiers visibility is public by default and can be queried for programs. I didn’t immediately report it and decided to report it after I am done with hunting.

I go to my profile -> edit profile -> Program preferences and I noticed that there was an option to turn off visibility for a program so that it doesn’t show in my profile that I am a part of that program.

Press enter or click to view image in full size

When this is turned on we can see the program in the Hacker’s profile.

When turned off it won’t be visible.

It didn’t take me to long to realize that now I could also disclose if a Hacker belongs to certain program despite of the fact that his program visibility is turned off.

Now I had two impacts for the same information disclosure vulnerability and I reported it again with the additional impacts that I discovered and finaaaallllllyyyyy :

Thanks for making it to the end of this write-up.
My twitter : @spongebhav
Feel free to comment here or DM me on twitter if you have any questions regarding this vulnerability.

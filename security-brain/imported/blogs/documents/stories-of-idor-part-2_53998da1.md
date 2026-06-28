---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-21_stories-of-idor-part-2.md
original_filename: 2019-11-21_stories-of-idor-part-2.md
title: Stories Of IDOR-Part 2
category: documents
detected_topics:
- sso
- idor
- command-injection
- api-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- api-security
language: en
raw_sha256: 53998da1be21fe24d82e4cdd5e8bd3342718ad97f2e1773bcda3e2992106df62
text_sha256: 71bd65ce89fc3e8a9d99ca5a0b7086518198f16b6370ee621f68dc10c764a786
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Stories Of IDOR-Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-21_stories-of-idor-part-2.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `53998da1be21fe24d82e4cdd5e8bd3342718ad97f2e1773bcda3e2992106df62`
- Text SHA256: `71bd65ce89fc3e8a9d99ca5a0b7086518198f16b6370ee621f68dc10c764a786`


## Content

---
title: "Stories Of IDOR-Part 2"
url: "https://medium.com/bugbountywriteup/stories-of-idor-part-2-29d313a39e55"
authors: ["Shivbihari Pandey (@ninja_pandit_)"]
bugs: ["IDOR"]
bounty: "3,650"
publication_date: "2019-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4923
scraped_via: "browseros"
---

# Stories Of IDOR-Part 2

Stories Of IDOR-Part 2
Shivbihari Pandey
Follow
4 min read
·
Nov 21, 2019

230

Press enter or click to view image in full size

Hello Welcome Back

Before you Begin i recommend you to Read about IDOR in my Previous blog

So Today i am going to share another IDOR story, well all stories in this blog is for single website, let name it xyz.com.

Before we started let me give a little Brief about this site:

Its an Education platform, mostly for the Political/Media/Historians students, where it gave a grouped platform for discussions. Worlds almost, Famous Universities are Using this Platform, for there students.

In application,There will be Teacher(Admin), who create the class and can invite students(Low Privilege Users) to Portal.

They will have Discussion , Assignments and projects.

till now you get the basic Idea about the Application.

OK, so in application there is Option to change the role of student in the discussion/debate in class, request for changing the role is look like this:

so there is 2 parameter 26201[Class admin ID] and 224410[Student Role ID].now this Student Role ID is little bit weird , its associate with the Student ID

So if we able to guess the Student Role ID, by keeping the Student_id Parameter same,

means, suppose there is an student with Student_id=48990 and now by keeping this number in student , if we start brute-forcing the student role ID, by this we able to Remove that student from previous class to our class or any other class, its depend on 26201[Class admin ID] .

and another IDOR i find after this .

another similar kind of request goes after this request .

now you can guess already, change the name by changing the ID of other Student, by this you can able to change there name.

Now this was the original request,But i want to add some additional parameter, to check, what will be response.

so in JSON parameter {“first_name”:”again”,”last_name”:”namechanged”}

i added another parameter “email”

so my request would be look like this:

and response was 200 Ok, means i can able to change any user email , by just guessing there ID.

By this i can simple able to takeover any user account.

So impact of this vulnerability is that i can able to:

1: get the detail of Any Student and change there details and this lead to account takeover

2: can Able to Remove Any student from there original class and move to any other class

3: i can permanently remove user from this application, by adding to my account and simply remove from my account.

Get Shivbihari Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For these 2 reports i was awarded $1500 for first report and $2150 for account takeover.

I have Found couple of other Interesting IDOR Issue Too.

For students there is an Assignment section ,where they able to submit there assignment to Teacher,Submission Request Look like this:

Now if you see the parameter file_url it have numeric value

so if we change these number , now i can able to upload any other student files to my assessment means , i have access to other users files.

response

i reported to them and they patched it by removing this parameter.

so after 4 month of patched, i started to check my old report and try to bypass it.

now for the same request as above it look like

Now if you notice there is no file_url parameter.

Press enter or click to view image in full size

response Look like this :

If you observe , there is parameter present “file_url”:null

but it didn’t present in the request, so i try to append this parameter in the request like this and rest is history ..!!

Press enter or click to view image in full size
Response

Again i was able to bypass it.

that is it for now.

Over all story is:

Always look for response to find Hidden Parameters

Timeline:

Report Send
Get Patched
Bounty Awarded

If you Love It , Feel Free to ReTweet it.

Rich Guy Can Donate Here 😄

Good Bye..!!

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-03_3-step-idor-in-hackerresume.md
original_filename: 2022-12-03_3-step-idor-in-hackerresume.md
title: 3 Step IDOR in HackerResume
category: documents
detected_topics:
- jwt
- idor
- access-control
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- jwt
- idor
- access-control
- command-injection
- otp
- rate-limit
language: en
raw_sha256: 132f793795dedd8add7339b2ea98dba23010032d3ece9eb6df1279eff0fef213
text_sha256: 908f00f6e7810216f13ff9d1e24bbb999596af24c0e4fe95df219d833058d8e3
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# 3 Step IDOR in HackerResume

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-03_3-step-idor-in-hackerresume.md
- Source Type: markdown
- Detected Topics: jwt, idor, access-control, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `132f793795dedd8add7339b2ea98dba23010032d3ece9eb6df1279eff0fef213`
- Text SHA256: `908f00f6e7810216f13ff9d1e24bbb999596af24c0e4fe95df219d833058d8e3`


## Content

---
title: "3 Step IDOR in HackerResume"
url: "https://medium.com/@swapmaurya20/3-step-idor-in-hackerresume-a365f2632996"
authors: ["Swapnil Maurya (@swapmaurya20)"]
programs: ["HackerResume"]
bugs: ["IDOR"]
publication_date: "2022-12-03"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 1822
scraped_via: "browseros"
---

# 3 Step IDOR in HackerResume

3 Step IDOR in HackerResume
Swapmaurya
Follow
5 min read
·
Dec 3, 2022

237

1

Before moving forward with this blog if you don’t have any context over what IDOR is you can refer the same over here

Press enter or click to view image in full size
https://hackerresume.com/auth/login

So to begin with, the story started when I was asked to test HackerResume since new features were being added on to see if there’s any security issues which can hamper the user data. So after going through the whole application it seemed most of the data we consider PII is already being public via the shared public resume.

Following the application workflow and analyzing all the request it came to my notice that there is a feature to enable and disable share the resume over a public URL and that was something which made me dig deeper and explore further. So when a user creates a resume he gets and option to share it via a public link or download the same. Thus if the users public link is by chance leaked to some attacker it can lead to a compromise of the users account since the URL shared has a unique hexadecimal path which acts as a ladder for the exploitation of the Vulnerability.

https://username.hackerresume.io/1acf1368-2467-4d81-6216-50bce103bc8a

So moving forward to the vulnerable request, while going through the HTTP history tab in Burp I tried the trail and error method to repeat the request with other users id and after a quite trails I got multiple endpoints which exposed other users data so now the point was how to arrange all the modified request in a step by step exploit scenario.

Get Swapmaurya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So initially I found that the uid parameter value is the key to exploit all the requests which was something tricky to leak. But as mentioned above the shareable resume link was the ladder that helped in further exploitation, thus using the victims hexadecimal value from the shared url in the vulnerable PUT request which updates the users resume, dumped the uid in the response.

Press enter or click to view image in full size
Vulnerable PUT request
PUT /api/user/attacker_id/resumes/victims_hex_value

Next step was to access the ATS Board which had all the details of the candidate where the user have arranged all the jobs applied and their current status, but there was one more barrier it had Authorization Header in the request but we also have a solution for that as I have already analyzed all the request through all the features there was an Auth Token generation request which generated the value for Authorization Header

POST /api/token HTTP/1.1
Host: hackerresume.com
Cookie: pamaram=value

{"uid":"RUsn78di7V6TCdbUB5878snBH"}

Thus using the output from the above request it was possible to replay the request and get the job boards of the victim user, so to guess the users board we only need to brute-force the request to get the valid board number.

Press enter or click to view image in full size
valid board number from intruder

Here in the below Screenshot we are able to see the victims ATS Board data along with the signup email used in creating HackerResume Account.

Press enter or click to view image in full size
Getting Victim Users ATS Board Data

To resolve this issue I addressed the same to the Developer who instantly understood the root cause and applied the fix, I was totally amazed with this quick fix that took only an hour to move the fix to production and taking a glance into the PR it seemed to be a 2 lines of code change. So here it can be seen that the developer had applied a check for user_id with the resume_id to validate the request is from intended user only.

Press enter or click to view image in full size
Fixed code

After exploiting this I hopped on to the ATS Board which had CRUD operation like creating and deleting a Stage, adding a Job into a particular Stage. So the thought process to exploit this was how can I perform the same actions in victim users board remotely. As usual I tried the same trail and error method by tampering the parameters in all the PUT/POST/DELETE request and within few attempts I got the exact vulnerable parameters that where vulnerable to exploit the same.

IDOR in ATS Board to move Jobs: An attacker was able to move his own Job(task) from his ATS board to victims ATS Board. Vulnerable Parameter: stage_id

PUT /ats/tasks/283 HTTP/1.1
Host: hackerresume.com
Authorization: Bearer JWT

{"company_name":"Facebook","job_title":"Data Scientist","resume_link":"ufivie","notes":"evievievk bso3o","salary":"","contact_name":"","contact_email":"","linkedin":"","board_id":"1926","stage_id":"70666"}

IDOR to add new Stages: An attacker was able to replay the below request by changing the board_id value to victims id and publish a new stage with the name hacked in victims ATS Board wherein user_id and user_email parameters were not validated while processing the request in back-end

POST /ats/stages HTTP/1.1
Host: hackerresume.com
Authorization: Bearer JWT

{"name":"hacked","board_id":"1026","user_id":"RUbkHekbYC26vGlSf7L","user_email":"test@test.com"}

IDOR to delete a Stage: An attacker was able to delete other users Stage by using the valid stage id, since the stage id was numeric it was easy for us to brute-force and delete all the existing stages

DELETE /ats/stages/1234 HTTP/1.1
Host: hackerresume.com
Authorization: Bearer JWT

Wrapping up for now, I hope this whole list of IDOR will give a better insight for you when you are testing any application. So that’s it for now and Thanks for Reading and I hope you liked this content, will meet you in next upcoming blog post with a new Learning and Experience!!!

Here’s an Instance how a Developer at HackerRank prioritize their work!!!

If you would like to connect with me refer this website

Swapnil Maurya
B.E in Computer Science and Engineering with focus on Security, actively contributing from past 2+ years through…

swapmaurya.in

Thanks to 
Harishankaran
 for proof reading this blog post!!!!!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-20_information-disclosure-that-made-me-2000-in-under-5-minutes.md
original_filename: 2024-07-20_information-disclosure-that-made-me-2000-in-under-5-minutes.md
title: Information Disclosure that made me $2000 in under 5 minutes
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- automation-abuse
- information-disclosure
language: en
raw_sha256: d42a62a25717cb8bd482a6b8d28f8352eb38843ec910584d7a26675db2f01249
text_sha256: 9b0ff3c3343ae782146c82649c0de9b16112c05c0704071c3be7603f419df661
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Information Disclosure that made me $2000 in under 5 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-20_information-disclosure-that-made-me-2000-in-under-5-minutes.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `d42a62a25717cb8bd482a6b8d28f8352eb38843ec910584d7a26675db2f01249`
- Text SHA256: `9b0ff3c3343ae782146c82649c0de9b16112c05c0704071c3be7603f419df661`


## Content

---
title: "Information Disclosure that made me $2000 in under 5 minutes"
url: "https://medium.com/@sugamdangal52/information-disclosure-that-made-me-2000-in-under-5-minutes-63e1ce00ca07"
authors: ["Sugam Dangal (@SugamDangal2)"]
bugs: ["Information disclosure"]
bounty: "2,000"
publication_date: "2024-07-20"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 151
scraped_via: "browseros"
---

# Information Disclosure that made me $2000 in under 5 minutes

Top highlight

Information Disclosure that made me $2000 in under 5 minutes
Sugam Dangal
Follow
4 min read
·
Jul 19, 2024

1.7K

9

1

On May 15 2024 , It was 3 am while i was trying to fall asleep but i couldn’t. A random thought came into my mind that i should try hunting on a new target. I took my phone and looked into bbradar.io for new programs, Thanks to https://x.com/kleoz_ for such an awesome app. Luckily, i found a new program that was just launched in intigriti.com about half an hour ago.

Press enter or click to view image in full size
bbradar

I woke up and got my laptop on and started looking for the program details. There were few targets in scope including a main wildcard *.target.com and there was an web app in scope , let’s take it as “app.redacted.com”.

As usual, i began subdomain enumeration and Js files scanning on the main wildcard domain “*.target.com”. This the part where i usually depend on automation. While it was running, i opened up another terminal and started Js file enumeration on “app.redacted.com”. I fired up the browser and navigated to the site. I saw that it was restricted to members only. The site required a valid credentials to access the resources. It was an online learning application but for the enterprises.

I analyzed the tech stack using the wappalyzer extension. First thing that came into my mind after this is directory fuzzing for sensitive files. I primarily use dirsearch and ffuf for this. Firstly, i ran a dirsearch scan:

dirsearch -u “https://app.redacted.com” -t 150 -x 403,404,500,429 -i 200,301,302 — random-agent

I started off with a default wordlist at first. And guess what, within few seconds, i got a hit. It got a status 200 for the file path /backup.zip. I was not expecting to see backup file having no access control at place. I then had an eye on the file size and to my surprise the file was 11.3GB in size. I started downloading the file. I knew the backup file must have someting interesting so meanwhile the file was downloading i started writing the report for it. I wrote all the details and only thing left was to write the file contents and to choose the correct severity for Confidentiality.

With a fear of getting it duplicate for another report, i looked for submissions in the platform and there were already few of the submissions so i was worried that it might not be accepted.

Finally after few minutes, the file download completed and i looked into the file contents and I found out that it had very sensitive information in it. The zip file contained all the source code of the application, all the application configurations, Database credentials,Database backup file, all user uploads that were meant to be private and many more such highly sensitive information.

Press enter or click to view image in full size
Exposed database credentials
Press enter or click to view image in full size
Exposed files
Press enter or click to view image in full size
Exposed user uploads and resources

I included all the information in the report and set the severity to exceptional CVSS 10 and submit the report hoping i am the first one to submit it.

Get Sugam Dangal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Luckily that afternoon my report got triaged but the traiger set the severity to high(7.5). I was not happy with it and i knew i had to ask for the justification from him as there is a high impact on confidentiality and the attack complexity is low as well, but i decided to wait for the reply from the company.

8 days passed but the report was still pending, I decided to check if the fix had been already applied. And yes the issue was fixed already, as i got 404 error. I then raised a concern to them that the issue has already been fixed but there was no any information from them. The next day, team replied with:

Press enter or click to view image in full size
Response from the team

After 6 more days. The company changed the severity back to exceptional CVSS 10. I thought , thankfully i don’t have to argue now😂. I was paid $1500 for the bounty and another $500 as a bonus for the impact that had due to this issue.

Press enter or click to view image in full size
Reward and Response from the team

This was a quick and a lucky find for me. If i was late, It’ll surely would have been duplicated by another researcher. This was all about the quickest $2000 i have made and Thank You for reading. Stay tuned for next writeup

Timeline

Bug Reported: 5/17/2024

Triaged: 5/17/2024

Asked for update: 5/25/2024

Update from the team: 5/28/2024

Rewarded: 6/04/2024

Connect with me: https://x.com/SugamDangal2

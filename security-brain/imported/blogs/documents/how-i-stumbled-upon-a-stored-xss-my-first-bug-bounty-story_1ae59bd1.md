---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-04_how-i-stumbled-upon-a-stored-xssmy-first-bug-bounty-story.md
original_filename: 2019-01-04_how-i-stumbled-upon-a-stored-xssmy-first-bug-bounty-story.md
title: How I stumbled upon a Stored XSS(My first bug bounty story).
category: documents
detected_topics:
- xss
- idor
- command-injection
- csrf
tags:
- imported
- documents
- xss
- idor
- command-injection
- csrf
language: en
raw_sha256: 1ae59bd13b29e3315a3a4b7cd57f6fc3b87c02c757dce32e22d99054ce156242
text_sha256: e0e888c1d81b126cad798eba22affdd0bbe98f84e5bf12b866bb9ebc739af047
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I stumbled upon a Stored XSS(My first bug bounty story).

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-04_how-i-stumbled-upon-a-stored-xssmy-first-bug-bounty-story.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1ae59bd13b29e3315a3a4b7cd57f6fc3b87c02c757dce32e22d99054ce156242`
- Text SHA256: `e0e888c1d81b126cad798eba22affdd0bbe98f84e5bf12b866bb9ebc739af047`


## Content

---
title: "How I stumbled upon a Stored XSS(My first bug bounty story)."
url: "https://medium.com/@parthshah14031998/how-i-stumbled-upon-a-stored-xss-my-first-bug-bounty-story-2793300d82bb"
authors: ["Parth Shah"]
programs: ["Edmodo"]
bugs: ["Stored XSS"]
publication_date: "2019-01-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5489
scraped_via: "browseros"
---

# How I stumbled upon a Stored XSS(My first bug bounty story).

How I stumbled upon a Stored XSS(My first bug bounty story).
Parth Shah
Follow
2 min read
·
Jan 5, 2019

96

1

Hello bug hunters,this is my first story so pardon my English.

I found this bug a few months back.I am grateful to the community as I have learned every damn thing from the community.I found this bug in Edmodo as who doesn’t want a swag for showing off in front of friends :).So Lets start the story.

So the first step was reading what others have found so I save my time not to find them and I realized most of the bugs were reported by them.I was a bit disappointed but I had decided to find a vulnerability.So I started visiting the website and inserting XSS payloads in almost any and every input field but nothing popped up,checked for csrf,idor but all of them failed I was like

It was late at night I thought of quitting and going to sleep I decided to test for last functionality of adding students in a group created by teacher.So i added XSS payload in first name and last name of the student and added it.As usual nothing happened.I was frustrated af.I decided to delete my account and everything and quit the target.So I started from deleting the student created from XSS Payload and BAAMMM! I got alert payload.I wasn’t able to believe I got my life’s first alert box.

Press enter or click to view image in full size

I was very happy as I got first valid bug of my life.I wasn’t able to sleep properly.I immediately made a POC video and sent to the team.They were very responsive.After few weeks I recieved the swag

PS: This bug wasn’t intentional but the amount of hard work and time I put in the website made it worthy.

Get Parth Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Takeaways:-

Always dig deeper in web application.There is always something fruitful.
Always check each and every functionality and input.
Main thing is never give up,I was going to give up and I found this.

Thank you for reading this.Focusing now more on reward based programs.Any suggestions are welcome.

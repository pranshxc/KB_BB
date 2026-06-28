---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-14_business-logic-errors-a-new-look.md
original_filename: 2020-04-14_business-logic-errors-a-new-look.md
title: Business Logic Errors - A New Look
category: documents
detected_topics:
- business-logic
- command-injection
tags:
- imported
- documents
- business-logic
- command-injection
language: en
raw_sha256: 330236c2d034f70d4bf931d81bb9c0870024c88610f2b1270d847ce9ab671d2e
text_sha256: 7e964728b26165e3ad603bec0595459d01cdcb1ba68db695e0233bf389ca62d0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Errors - A New Look

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-14_business-logic-errors-a-new-look.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `330236c2d034f70d4bf931d81bb9c0870024c88610f2b1270d847ce9ab671d2e`
- Text SHA256: `7e964728b26165e3ad603bec0595459d01cdcb1ba68db695e0233bf389ca62d0`


## Content

---
title: "Business Logic Errors - A New Look"
url: "https://medium.com/@shahjerry33/business-logic-errors-a-new-look-3b18d9c2a12f"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["Logic flaw"]
publication_date: "2020-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4655
scraped_via: "browseros"
---

# Business Logic Errors - A New Look

Business Logic Errors - A New Look
Jerry Shah (Jerry)
Follow
3 min read
·
Apr 14, 2020

716

3

Press enter or click to view image in full size
New Look

Summary :

It commonly allow attackers to manipulate the business logic of an application. Errors in business logic can be devastating to an entire application. They can be difficult to find automatically, since they typically involve legitimate use of the application’s functionality. However, many business logic errors can exhibit patterns that are similar to well-understood implementation and design weaknesses.

I found this wonderful vulnerability on one of the private program. I was able to delete anyone’s comment by just using the report feature.

This vulnerability is not limited only to comment section you can also report someone’s post, profile photo, blog, message, video etc. You’ll not always find the report feature but instead some companies also use the flag feature, you can also try their.

Press enter or click to view image in full size
Flag feature

How to find this vulnerability ?

Go to your target website that has comment feature
Press enter or click to view image in full size
Comments

2. Here you’ll find many people have commented, in my case it was “fedoraismine” was the victim. (My another test account)

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Use the report comment feature, click on report and select any option

Options

4. Now click on continue and intercept the request using burp suite and send it to intruder

Press enter or click to view image in full size
Burp Suite - Intruder

5. Now click on clear and go to payloads section in burp suite and select Null payloads

Press enter or click to view image in full size
Payload Section

6. Now select the option Continue indefinitely

Press enter or click to view image in full size
Continue indefinitely

7. Now go to options and set the Number of threads to 100

Press enter or click to view image in full size
Threads

8. Now click on start attack

Press enter or click to view image in full size
Attacking

9. Wait for 900 payloads to be executed

Press enter or click to view image in full size
900 Payloads

10. Reload the comment page

Press enter or click to view image in full size
Comment Deleted

NOTE : If the comment is not deleted wait for some more payloads to get executed and then reload the page again

Thank You :)

Instagram : jerry._.3

Happy Hacking ;)

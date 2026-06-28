---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-17_business-logic-errors-a-logic-destruction.md
original_filename: 2021-10-17_business-logic-errors-a-logic-destruction.md
title: Business Logic Errors - A Logic Destruction
category: documents
detected_topics:
- business-logic
- command-injection
- automation-abuse
tags:
- imported
- documents
- business-logic
- command-injection
- automation-abuse
language: en
raw_sha256: e55ee325b4f6c04a9fa5bde56714b16c8b4a9ca2c23f4bde1e654d5967bff928
text_sha256: 54b361885cc8297300fc039f327e3a3965f1515b49681d3b8874e357a8d71359
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Business Logic Errors - A Logic Destruction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-17_business-logic-errors-a-logic-destruction.md
- Source Type: markdown
- Detected Topics: business-logic, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `e55ee325b4f6c04a9fa5bde56714b16c8b4a9ca2c23f4bde1e654d5967bff928`
- Text SHA256: `54b361885cc8297300fc039f327e3a3965f1515b49681d3b8874e357a8d71359`


## Content

---
title: "Business Logic Errors - A Logic Destruction"
url: "https://shahjerry33.medium.com/business-logic-errors-a-logic-destruction-477c4ebc824b"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Logic flaw"]
publication_date: "2021-10-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3236
scraped_via: "browseros"
---

# Business Logic Errors - A Logic Destruction

Top highlight

Business Logic Errors - A Logic Destruction
Jerry Shah (Jerry)
Follow
4 min read
·
Oct 16, 2021

673

3

Summary :

Business logic errors will allow you to manipulate the business logic of an application. Sometimes business logic errors can have devastating effects on the applications. Business logic errors are difficult to find because they involve legitimate use of the application’s functionality. This kind of vulnerabilities are a way of using the legitimate processing flow of an application in a way that it results in a negative consequence to the organization.

Description :

I found this vulnerability in an invite feature on my private project. It was having only limited number of invitations (4 invitations) for non-premium users, means you can only invite 4 people. I sent one invite and then I was left with 3 invitations but after sending an invitation I noticed that there is an option to cancel (withdraw) your invite and when I used that cancel option, again I was having 4 invitations to send. While sending an invitation I captured the request using burpsuite and manipulated the email parameter value to an array and I checked the response and found both the emails were reflected in response. I checked both the emails and found that I got invitations on both the emails but when I checked on the web application it was counted as one invite which means I was still left with 3 invitations even after sending invitation to 2 users.

What is an array ?

In simple language, an array is a datatype that is used to store multiple values of same type together so that you do not need to specify different datatypes and variables for different values.

Similar to other programming languages, an array in JSON is a list of items surrounded in square brackets []. Each item in an array is separated by a comma and the array index begins with 0. JSON array can store multiple value types like string, number, boolean, object or other array inside JSON array.

For eg. {“email”:[“email1@gmail.com”,”email2@gmail.com”]} is considered as a whole array and changes will be applied to both at the same time.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I used the invite team member functionality
Press enter or click to view image in full size
Invite Team Member Functionality
Press enter or click to view image in full size
Sending Invitation

2. After sending an invite, I captured the request using burp to check how this invitation functionality works and it was working normal

Press enter or click to view image in full size
Captured Request
Press enter or click to view image in full size
Normal Behavior

3. In the next step, I withdrew the invitation (laneko6393@astarmax.com) which I sent before, so now I have 4 invitations again

Press enter or click to view image in full size
Invitation Withdrew (laneko6393@astarmax.com)

4. Then I sent an invitation again (laneko6393@astarmax.com) and captured the request and manipulated it with an array appending new email (winaxi9052@bombaya.com) and I received invitations on both the emails

Press enter or click to view image in full size
Manipulated Request - Array
Press enter or click to view image in full size
Manipulated Response - Array
Press enter or click to view image in full size
Invitation Received
Press enter or click to view image in full size
Invitation Received

5. In the next step, I withdrew the invitation again and this time I sent the invitation to 3 users at a time using an array and it went successful

Press enter or click to view image in full size
Manipulated Request - Array (3 Invitations)
Press enter or click to view image in full size
Manipulated Response - Array (3 Invitations)
Press enter or click to view image in full size
Invitation Received
Press enter or click to view image in full size
Invitation Received
Press enter or click to view image in full size
Invitation Received

6. As a last step, I reloaded the page and checked that how many invitations were deducted from 4 invitations and I found that I was still left with 3 more invitations as all the three invitations that I sent were counted as 1 because of an array

Press enter or click to view image in full size
3 Invitations Left

Why this happened ?

In my opinion,

It happened due to improper assignment of a datatype (array) to the email parameter, which led to abuse of invite user functionality.

Impact :

An attacker can abuse this functionality and send as many invitations as he/she wants without using the premium feature. This can lead to business loss to the company.

Mitigation :

A proper datatype should be assigned to the parameters and input validation should be done to avoid this kind of vulnerabilities.

Press enter or click to view image in full size

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-26_break-the-logic-5-different-perspectives-in-single-page-1500.md
original_filename: 2022-08-26_break-the-logic-5-different-perspectives-in-single-page-1500.md
title: 'Break the Logic: 5 Different Perspectives in Single Page (€1500)'
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 7cc60ff6df004675ecada9329b5cc70ff3cb545bd957203bff89b6f1290de98b
text_sha256: 16a2e46e4fc3a611c63d9090653ca1ef3821cb2d69ddaf8aa0db9d2e811f4470
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Break the Logic: 5 Different Perspectives in Single Page (€1500)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-26_break-the-logic-5-different-perspectives-in-single-page-1500.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `7cc60ff6df004675ecada9329b5cc70ff3cb545bd957203bff89b6f1290de98b`
- Text SHA256: `16a2e46e4fc3a611c63d9090653ca1ef3821cb2d69ddaf8aa0db9d2e811f4470`


## Content

---
title: "Break the Logic: 5 Different Perspectives in Single Page (€1500)"
url: "https://infosecwriteups.com/break-the-logic-5-different-perspectives-in-single-page-1500-5aa09da0fe7a"
authors: ["can1337 (@canmustdie)"]
bugs: ["Client-side enforcement of server-side security", "IDOR", "Broken authorization"]
bounty: "1,500"
publication_date: "2022-08-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2259
scraped_via: "browseros"
---

# Break the Logic: 5 Different Perspectives in Single Page (€1500)

Break the Logic: 5 Different Perspectives in Single Page (€1500)
can1337
Follow
5 min read
·
Aug 26, 2022

166

2

Hello everyone. Today I’m going to talk about five different vulnerabilities that I found on a single page. Three of these vulnerabilities were accepted and other two were closed as duplicate. Also the company was rewarded me with €1500.

As always, I can’t give information about the company because they run a private bug bounty program. So, let’s call them as “redacted”.

Before we get started, let me give you some info about the app. This is basically a school/student app. It has three different user models: teachers, students, and parents. Parents can only edit their own information on students’ profiles. So we have limited authority as parent user. All reports will proceed from this perspective in single contact page.

I. Users can change student’s main address even without access

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I went to a student’s profile as parent user, I came across an address section that we don’t have permission to edit. The edit button was active, but when I clicked it, all fields were disabled.

However, you can still see that the save button is active. So, as a fairly simple method, I removed the disabled attribute from the fields.

Press enter or click to view image in full size

I filled in the fields with my own information and it was pretty easy to send the request cause the save button was still active.

Press enter or click to view image in full size

I sent the request and saw that the target information had really changed. The protection was only on the frontend of application. Similarly, these infos could be changed using Burp Suite.

II. Users can edit their all section even without access

Parent users have some contact info on students’ profile. However, they cannot edit all of this information. So, they only have the right to edit some fields.

Press enter or click to view image in full size

For an example, there are also information such as name and adress, but when we click the edit button, only the contact fields can be changed.

Press enter or click to view image in full size

When I sent the request in this way, I came across the following PUT request. As you can see, there were other fields that couldn’t be changed, such as name, address, etc.

I changed some information such as name, address, relationship and sent the request.

Press enter or click to view image in full size

The information has been successfully changed and displayed on the page.

III. Users can create new parents contact field even without access

As you know, parent users can only edit their own information. They cannot add a new parent contact field.

Press enter or click to view image in full size

However, when I sent a request to edit the contact table, I changed all the ID values ​​in the parameters and was able to create a new Contact table.

Press enter or click to view image in full size

The request in the picture is the same request as the PUT request in the 2nd report. As you can see the request has many different ID values. I replaced the last digits of all ID values ​​with random values. (except learnerPersonalid because it was at the beginning of every request and was not page specific.)

Press enter or click to view image in full size

I was actually wondering how the app would respond to this action. I was probably expecting 500 or 403 answers but instead the app created a new contact field for me.

IV. Users can change address types even without access

Users cannot change the defined address types of students. For example, in the picture below, there are two defined addresses for the student and parent users can’t change their types.

Press enter or click to view image in full size

When we try to change the residential address to official addresses, the application will throw an error and our request won’t be done.

I remembered that the save button in the 1st report is still active for addresses. So, I edited a residential address, sent it and came across the following request.

Press enter or click to view image in full size

I changed the “postalTitle” parameter to official. (Likewise, I could change it to residential for official addresses.)

Press enter or click to view image in full size

In the app, only one address can be an official address but you can see that both addresses have changed to main addresses.

V. Users can delete student’s official address without access (Basic IDOR)

While examining the address types, I saw a difference. A delete button was active for residential addresses, but there was no delete button for official addresses.

Example for residential address

Note that while the “Delete” button is active for residential addresses, there is no such button for official addresses.

Example for official address

So, I clicked the student’s official address edit button. I ran Burp Suite and click save button. Then, I came across the following request again and copied the “household” value.

Then, I went back to residential addresses and clicked the delete button, got the request and replaced the “household:” value with the official address ID.

And as a result, I was able to delete the official address even without access.

That’s all for now. Thanks for reading this far and I hope you liked it!

You can follow me on twitter: https://twitter.com/canmustdie

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

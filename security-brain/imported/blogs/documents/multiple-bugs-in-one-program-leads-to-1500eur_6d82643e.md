---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-02_multiple-bugs-in-one-program-leads-to-1500.md
original_filename: 2022-08-02_multiple-bugs-in-one-program-leads-to-1500.md
title: Multiple bugs in one program leads to 1500€
category: documents
detected_topics:
- access-control
- idor
- command-injection
tags:
- imported
- documents
- access-control
- idor
- command-injection
language: en
raw_sha256: 6d82643e0da629eab10399a3e62de7506566779045daa6c2410eb1f6f6708052
text_sha256: d0a051799e24fb2367515f5d6e3d11a91d7248808ddcfcb9a06ea9df3f0a42a0
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple bugs in one program leads to 1500€

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-02_multiple-bugs-in-one-program-leads-to-1500.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `6d82643e0da629eab10399a3e62de7506566779045daa6c2410eb1f6f6708052`
- Text SHA256: `d0a051799e24fb2367515f5d6e3d11a91d7248808ddcfcb9a06ea9df3f0a42a0`


## Content

---
title: "Multiple bugs in one program leads to 1500€"
url: "https://canmustdie.medium.com/multiple-bugs-in-one-program-leads-to-1500-c35fcde06bc7"
authors: ["can1337 (@canmustdie)"]
bugs: ["Privilege escalation", "IDOR", "Broken authorization"]
bounty: "1,500"
publication_date: "2022-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2371
scraped_via: "browseros"
---

# Multiple bugs in one program leads to 1500€

Multiple bugs in one program leads to €1500
can1337
Follow
5 min read
·
Aug 2, 2022

216

2

Hi, today I‘m going to talk about three basic vulnerabilities that I discovered in the same program and were rewarded with 1500€.

Since all three approaches are similar, it would be pretty easy to connect the vulnerabilities together. Let’s call them redacted because the company runs a private bug bounty program. So let’s get started.

I. Parameter Changing & HTTP Response Manipulation leads to client admin’s PII leak

In Redacted application, users cannot access the “access” panel of the client that they do not have authorization. The “Access” button contains the information of the users for the Client and allows us to see which users are authorized or not.

A Client instance we do not have access to. Only the “properties” option appears, but we can’t click it, we don’t have access to any buttons.

Press enter or click to view image in full size
No Access client example.
Press enter or click to view image in full size
Full Access client example.

Now we will be able to access the “Access” button of a non-accessible Client by changing the parameters and using HTTP response. This will show us which users have what authority. Additionally, it will disclose users’ PII information such as email, companies, roles.

Firstly, I went to the section where the clients are listed and entered a random letter in the search button. I caught the request and faced the following situation.

Press enter or click to view image in full size

The entire request contained information for all the clients to be listed. I checked the first client.

Press enter or click to view image in full size
First client’s data

In this section two parameters “CurrentLogOnAccesType”:None and “CanControlClientAcces”:false, caught my attention. I thought of editing the parameters as I’ve seen in other full access client examples.

Press enter or click to view image in full size

I changed the parameters to “full” and “true” respectively. The same information was available for the response to the request and I did the same things. I sent the request.

Later, when I came back to the page, I saw that the target Client had changed to “Full Access”. The Access button was active and when I clicked it, I could see the privileges of all users.

Afterwards, since the user information was returned in the Access section, I caught the request again while clicking the Access button and I have viewed the response of the request.

Press enter or click to view image in full size

As a result, an attacker can activate the “Access” feature of the client wants, although does not have authorization, and can see the authorizations of all users. It can also disclose users’ PII information, including admins and authorized users.

II. “/api/Missions?ClientId=” request leads to leak No Access Client’s Missions

We cannot click on “No Access” clients while listing the clients in the Client section. Under normal circumstances, after clicking on a Client with full or read-only privileges, we are directed to the Missions section.
So, we cannot see Missions and other information because we cannot click on No Access Clients.
However, I found a request that will allow us to access Missions and other information of No Access Clients. The vulnerability is basically IDOR.

While viewing the Mission of a full-access client, the settings button caught my attention. I looked through the alternatives one by one and found the vulnerability under the “Copy from Engagement” section. I clicked the button and caught the request.

Press enter or click to view image in full size

After seeing the ClientID parameter, I sent the request to the Repeater and started looking for the ID information of the No Access Clients.

Press enter or click to view image in full size

I went to the section where the Clients are listed in the first report and opened DevTools. I was able to see the ids of the clients there.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I went back to Repeater and replaced the GUID information I copied with the target ID.

In response, I saw Mission name and information, Client dates (this information cannot be accessed for no access).
The request directly discloses Mission information. We can read No Access Client as Read-only.

III. Attackers can add Missions to No Access Clients

I found a way to add random or targeted Missions to Clients even though I have no access (No Access Client) at Redacted app.

Normally, when we want to create a new mission in the Missions section, we can only select certain Clients. These Clients are only Clients that we have full access.

As you can see, we can only select Full Access Clients.

Press enter or click to view image in full size

In the second step, I did the same as the ID copy process in the report above. I copied the ID of a No Access Client.

Press enter or click to view image in full size

Then I went back to the first episode. I created a new Client and held the request. I replaced “ClientId” parameter with the GUID I copied. You can also change the Name parameter even if you don’t have it. This means that attackers can also add random Mission names they don’t have.

Normally we cannot see Missions because we do not have access to the target Client. But using the request in the second report (/api/Missions?ClientId=) I made sure if my request was successful.

As a result, there is a vulnerability here that causes attackers to randomly insert Missions into targeted Clients. Also, as you can see, attackers can see the Missions they sent using the request in the second report.

That’s all for now. Thanks for reading. See you in another write up!

You can follow me on twitter: https://twitter.com/canmustdie

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

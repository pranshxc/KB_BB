---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-18_how-i-found-8-vulnerabilities-in-24h.md
original_filename: 2022-11-18_how-i-found-8-vulnerabilities-in-24h.md
title: How i found 8 vulnerabilities in 24h?
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 25cef0afb259862e67a58b6a858d0abb0bf077c9ef3b7b774f1a632d3f3e6cc8
text_sha256: d2b9835736e6b4c1d952b1e38d3a7b415f9fcced8fbe89e7c7fd5a57966a5bd2
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How i found 8 vulnerabilities in 24h?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-18_how-i-found-8-vulnerabilities-in-24h.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `25cef0afb259862e67a58b6a858d0abb0bf077c9ef3b7b774f1a632d3f3e6cc8`
- Text SHA256: `d2b9835736e6b4c1d952b1e38d3a7b415f9fcced8fbe89e7c7fd5a57966a5bd2`


## Content

---
title: "How i found 8 vulnerabilities in 24h?"
page_title: "How i found 8 vulnerabilities in 24h? | by Mohamed Anani | Medium"
url: "https://0xm5awy.medium.com/how-i-found-8-vulnerabilities-in-24h-aad3bd5fd487"
authors: ["Mohamed Anani (@0xM5awy)"]
bugs: ["Logic flaw"]
publication_date: "2022-11-18"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 1896
scraped_via: "browseros"
---

# How i found 8 vulnerabilities in 24h?

Mohamed Anani
Follow
6 min read
·
Nov 19, 2022

549

3

How i found 8 vulnerabilities in 24h?

Hello Awesome Hackers, I hope you all doing well!
My name is Mohamed Anani Or 0xM5awy.

Press enter or click to view image in full size

This is the second part of This Write-Up, But the difference is that there i only showed the title of the bug and i do not talk about any thing technical but here will explain every vulnerability, how I found it, and so on

Before I go into details, I have to clarify a few things, There are 3 roles on this progream
1.admin with access ( can edit/delete/post everything )
2.admin without access (can do the same things as admin with access but less)
3.assistant(able to access less endpoints then admin without access but can post some things only)
4.Viewr (able to access less endpoints then Contributor and only view)

Now it’s time to explain all the vulnerabilities :):

1.The first bug was that there are 3 different types of subscriptions/plans and no one can change/edit it only the admin/owner of the team

When we create an account in 0xM5awy.com program, this program will give us a 3-month free period During this period, you can change plans as you like in order to try what is the best plan for you and After the free trial period ends, you will purchase it so only the admin with access was able to edit it and change the plans as he want and the other roles was not be able to access/edit this plans so how we was able to do that with admin without access and assistant?

Steps To Reproduce:
Open admin with access account and change the plan to another plan( there is 3 plans)
Now copy the endpoint PUT /api/plans and the body of the request {“plan_id”:1}
Open admin without access or assistant account and made any request and Intercept the request and send it to repeter
Change Your request with the PUT /api/plans method+endpoint and the body with {“plan_id”:1}
Now you can change the subscriptions/plans successfully by change the {“plan_id”:1} ID With assistant and admin without access
2.The Second bug was that there are endpoints allow you to add your comment like facebook comment etc and you cant edit/delete the comments of other users even if you are the owner

When any user writes a comment, no user can edit/delete it, only the owner of the comment can edit/delete

Steps To Reproduce:
Open 2 accountswith any roles (admin with/out access or assistant)
Made 2 commentswith the 2 accounts
From attackeraccount delete your commentand Intercept the request
Change the ID of your commentwith Victms commentsID
You able to delete the users comments :)
Also if you use the PUTmethod you will be able to edit it also so we are able to edit/delete the commentsof users by change the ID of our comment
3.The Third bug was that the Pro Plan not allowed you to create more than one map and if you want to create more than once you need to upgrade the plan!

When we are in professional_Plan and we Downgrade to the Pro_Plan its tell us that there is some feature we will not be able to have on the Pro Plan like you only will be able to have one map and you cant create more then once

Steps To Reproduce:
Open Your Account that have the professional_Plan and create a map then Intercept the request
Copy the Method/endpoint and body of the request
Open Your Account that have the Pro_Plan and made any request
Change the Method/endpoint and body of the request with our professional_Plan request
Send the request and now you able to create a map as you want not only only one
4.The four bug was that only the admin/owner can (Duplicate) the maps and no one else can do that !

Only the admin with access can Duplicate the maps and no one can do that so i found a way to do that with admin without access and assistant

Steps To Reproduce:
Open the map that you want to Duplicatewith the 2 roles on top
make a get request and Intercept the request then send it to the repeter
add Duplicateword to the endpoint before /api/map/20500After /api/map/20500/duplicate And the GetMethodto Post And add {} to the body
Now send the requst and you will be able to Duplicatethe maps as you want :)
5.The fifth bug was that only the admin/owner can edit/rename/delete/etc the (customization)

When we open admin with access account we will be able to access the /customization Endpoint and when we do the same with admin without access account its will give us blank page or 401 Unauthorize so i found a way to enable-unenable/crate/rename/edit do that with the admin without access account

Steps To Reproduce:
Open admin with accessaccount and crate new customizationand edit/rename/delete/etcThen save all this requests on the repeater
Openadmin without accessaccount and try all these endpoints/methods/bodys with it and You will notice that you able to add/edit/rename/delete/etcthecustomization
6.The sixth bug was that only the admin/owner can edit/rename/delete/etc the (settings) of the team

When we open admin account that dont have the admin access we will notice that we can see only the settings of the team but we can not edit anything of them so i found a way to do that

Steps To Reproduce:
From the admin with accessaccount editthe settings of the team and Intercept the requests and send it to repeter
Now from the admin without accessaccount made any request and send it to the repeter
from the admin without accessaccount try all the endpoints of the settings what we save it on the repeter from the admin with accessaccount
You will notice that you can also edit/rename/delete/etc.
7.The seventh bug was that the admin/owner allowed/unallowed the insights feature and if the admin/owner make this feature off the viewer role cant send any insights

if the admin open the settings will find an option that allows viewers to submit user insights about maps that will added to the roadmaps and maps and if he make it off then the Viewer role will not be able to send any insights but i found a bypass and im able to send any insights i want

Steps To Reproduce:
FormVieweraccount open any map that the admin allow the insights on and send any insights and Intercept the request and send it to repeter
The Endpoint looks like POST /api/maps/1626 and the bodylooks like {“note”:{“name”:”0xM5awy”,”content”:”i can send nots”,”owner_id”:null,”customer_id”:11501634}}
By change the customer_id we will be able to send any insights with any user we want and byorganization_id we will be able to send any insights with any organization we want and by change the /api/maps/1626 ID we will be able to send any insights on the maps that the admin not allowd to send insights on.
8.The eighth bug was that there a endpoint call (feature) and this endpoint the viewer role cannot access/read/see_it

if we open the Viewerrole account we will see that we are only able to see the maps endpoint And when we try to Access feature-board its give us 403 so i try to bypass that by knowing the id of the features i will be able to Access to the {"activities","name","description"} of the feature

Steps To Reproduce:
Open the admin with accessaccoun Crate a new feature
Then After you Crate the feature Open it So the url will be like : https://0xM5awy.com/feature/5711304/
Now the Viewerwill use this id 16264795 to Access the {"activities","name","description"} of the feature

Endpoints That the Viewerwill Use

GET /api/features/16264795
GET /api/activities?trackable=Feature

4. Made any request with Vieweraccount and Intercept the request and send it to repeter

Get Mohamed Anani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. Use the endpoint on top on the request

6. You will be able to read the {"activities","name","description"} of the feature

All vulnerabilities accepted (business-logics/BAC always win) ..

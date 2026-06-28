---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-01_edm0d0-idor-vulnerabilities.md
original_filename: 2019-04-01_edm0d0-idor-vulnerabilities.md
title: EdM0d0 IDOR Vulnerabilities
category: documents
detected_topics:
- idor
- access-control
- command-injection
- automation-abuse
- csrf
- information-disclosure
tags:
- imported
- documents
- idor
- access-control
- command-injection
- automation-abuse
- csrf
- information-disclosure
language: en
raw_sha256: cecc8a3e2d26cd40226896cf9eded25155623195183910339da45ec8f550a001
text_sha256: 582428c374ef520439e0039412a96c84854e53fded0653a8537ee8cf8d7e8a5d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# EdM0d0 IDOR Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-01_edm0d0-idor-vulnerabilities.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, automation-abuse, csrf, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `cecc8a3e2d26cd40226896cf9eded25155623195183910339da45ec8f550a001`
- Text SHA256: `582428c374ef520439e0039412a96c84854e53fded0653a8537ee8cf8d7e8a5d`


## Content

---
title: "EdM0d0 IDOR Vulnerabilities"
url: "https://medium.com/@pratyush1337/edm0d0-idor-vulnerabilities-95ca8600ee1c"
authors: ["Pratyush Anjan Sarangi"]
programs: ["Edmodo"]
bugs: ["IDOR"]
publication_date: "2019-04-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5336
scraped_via: "browseros"
---

# EdM0d0 IDOR Vulnerabilities

EdM0d0 IDOR Vulnerabilities
Pratyush Anjan Sarangi
Follow
6 min read
·
Apr 1, 2019

167

1

Introduction:

It’s a tale of two different Insecure Direct Object Reference bugs which had a potential to Delete anyone’s comment and proper exploitation of 2nd IDOR leads to Information disclosure(Attachments:You will understand it later in the post) of all the registered users of Edmodo.

TALE of TWO IDOR Vulnerabilities in EdM0d0:

It was a fine day and i just completed few auditing of private companies websites and they accepted the vulnerabilities and were taking a management decision to award bounty and meanwhile i was free so i thought let’s try to find something interesting in a public website in which many of our community people have invested their time and made it more secure than ever but i was aback to see that these two vulnerabilities was never reported. I remember a time when every other person was posting a snapshot of Goodies Pack from Edmodo in Facebook. Even i have seen conversation where people were discussing that 3–5 bugs were pending to be validated by Edmodo Developer Team and also how many Goodies pack they have already received by reporting to Edmodo.

Story Behind Hunting in Edmodo Web-Application:

When i started my career in Information security , I guess 4–5 years back, I was one of the person who had reported them on the initial stage of their program about a CSRF Vulnerability and was rewarded with a goodies pack at that time. There is a Coffee Mug which looks pretty cool but at that time i was not using the Mug so i gifted it to my Elder brother who is working in Sweden and unfortunately he broke the Mug as it fell down from kitchen Rack :( So I thought Let’s get it back by hunting :)

First IDOR Vulnerability:

This was a pretty weird encounter of IDOR vulnerability to me for the first time , I was really not sure why that was happening but i figured it out finally at the end. So let’s check out the vulnerability.

As we all know that Edmodo is an educational technology company offering a communication, collaboration between teachers , students and parents. I have created a Teacher account and added two contacts to that teacher account , so basically when you add contacts to anyone’s account than it send a verification link to their mail id and if you click on that link than it will create a separate account in the Edmodo web application. So I added two contacts to the Teacher account and verified it. Now as a Teacher , I am able to Post anything I want in my wall and my contacts are able to view and Post comments to that Post Thread.

Here the permission was set like if a User posts any comments to a Thread than he is only allowed to DELETE the comments posted by himself , Even if the Admin of the Post Thread post a comment in the thread than he is restricted only to DELETE his own comment and he cannot DELETE anyone else’s comments in his own Post.

But…There was a miss validation on the POST request sent to the web application for deletion of any comment , if we get the comment_ID of other user’s comment and click on DELETE button of own comment and while sending the request to the web application we intercept the request and change the comment_ID to the other comment_ID posted by other contacts/user in the same thread than it was DELETING their comment :)

Burp Request Interception:

Press enter or click to view image in full size

I was Like , Here come’s the MUG!

But As you remember , I had already mentioned that this was a weird Bug and according to the above description , it was a normal IDOR and doesn’t seems like anything weird. Here come’s the next stage where I was making the POC and encountered the weirdness of the bug into the picture.

Get Pratyush Anjan Sarangi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

According to the above description , I understood that “If any user commented to a post than any user who has commented can delete anyone’s comment who have commented in that POST Thread” Which was a big Freak-in Mistake. With this concept in mind i started making POC and this time what i did is that I logged in with the contact’s account and tried to delete the comment of Admin user’s comment in the Post Thread but it was disastrous failure as it reloaded the Web Application but neither it deleted Admin User’s comment nor the User comment and I was like What the Heck went wrong?

So I guess now you figured out why its weird? Yes! You are correct , It was miss validation check in that Admin User’s POST , Only the Bug was working on the User account who has created the POST. Let me Explain you clearly , According to the permission set on the web application only a user who has created a comment in that related post can delete their own comment and there is no option to delete anyone else’s comment but the problem was that the User who has created the POST is the only User who can delete the comment of other user in that POST with the above vulnerability. If one user has created a POST and you commented as a user than if you try to change the comment_ID to another user than it won’t delete their comment from the POST. Only the Admin of the POST was able to delete the comments of another user with the above technique even though there is no option for the Admin of the POST to delete anyone’s comment. That’s Pretty Much Weird!

Also You need to understand the vulnerability , Any admin who has created the POST has the permission to delete it’s POST and hence any comment related to that POST Thread will be deleted with it and hence , This vulnerability was working with the same concept as the Developers didn’t put a check on the validation while deleting individual comment of other User.

You might be wondering how I was able to find the comment_ID of other user right? It was simple! by using Inspect element ;) For Proper clarification , You can check my POC:

Comment IDOR Vulnerability

Second IDOR Vulnerability:

The Second IDOR Vulnerability was quite tough to find but didn’t expected it to be found in that place. In a Teacher account there is a Chatting functionality in which the Teacher can interact with it’s contacts.students/parents. In chatting functionality there is a file attachment function which can be used to send files to other user while chatting. But the interesting this was that the file/attachments that are being sent are listed in the right side of the chatting panel and I saw there is another functionality in which It allows a Teacher to add the attachments to their library. I guess You have already figured it out! Yes! There was a IDOR Vulnerability which was allowing me to add other user’s files to my library and I was able to view the files of other registered User who have exchange these files during their chatting session. I uploaded a file in my chatting session with my contact and after uploading the file, I clicked on add this to library function and intercepted the request and changed the file_ID to random ID which was below the one generated by the web application.Thus, I confirmed the IDOR Vulnerability was in the file_ID:

Burp Request Interception:

Press enter or click to view image in full size

IMAGE POC:

Press enter or click to view image in full size
Private File Disclosure Vulnerability
Press enter or click to view image in full size
Private File Disclosure Vulnerability

For More Clarification , Please Check out the Video POC:

Private File Disclosure Vulnerability

After reporting both the Bugs:

Press enter or click to view image in full size

Than this Happened , No Mug this Time….Will continue the hunt in the Near Future :)

Press enter or click to view image in full size

Timeline:
Feb. 20, 2019 — Initial Report
Mar. 08, 2019 — Report Triaged
Mar. 29, 2019 — Bug Fixed and Goodies Pack Rewarded

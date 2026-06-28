---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-09_from-na-to-resolved-for-backblaze-android-apphackerone-platform-bucket-takeover.md
original_filename: 2020-07-09_from-na-to-resolved-for-backblaze-android-apphackerone-platform-bucket-takeover.md
title: From N/A to Resolved For BackBlaze Android App[Hackerone Platform] Bucket Takeover
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
- mobile-security
language: en
raw_sha256: 3552013ccf2b060a31776ad94277a66e1cb703df72e33bfd9c0e84f2a0903df5
text_sha256: e957346785530410780789a59a11d6454f66d3b4ad764fd740125bda8c8cc627
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# From N/A to Resolved For BackBlaze Android App[Hackerone Platform] Bucket Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-09_from-na-to-resolved-for-backblaze-android-apphackerone-platform-bucket-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `3552013ccf2b060a31776ad94277a66e1cb703df72e33bfd9c0e84f2a0903df5`
- Text SHA256: `e957346785530410780789a59a11d6454f66d3b4ad764fd740125bda8c8cc627`


## Content

---
title: "From N/A to Resolved For BackBlaze Android App[Hackerone Platform] Bucket Takeover"
url: "https://medium.com/@pig.wig45/from-n-a-to-resolved-for-backblaze-android-app-hackerone-platform-bucket-takeover-f817692a590"
authors: ["Sahil Tikoo (@viperbluff)"]
programs: ["BackBlaze"]
bugs: ["Hardcoded credentials", "Information disclosure"]
publication_date: "2020-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4425
scraped_via: "browseros"
---

# From N/A to Resolved For BackBlaze Android App[Hackerone Platform] Bucket Takeover

From N/A to Resolved For BackBlaze Android App[Hackerone Platform] Bucket Takeover
Sahil Tikoo
Follow
4 min read
·
Jul 9, 2020

74

Hello Everyone

Why I wrote this Blog?

This blog will help you understand the importance of never giving up and how you can turn things around in bug bounty.

Few weeks back I was looking for some programs to hunt ,stumbled upon this Public backblaze program which already had around 150+ reports resolved, anyways thought of giving a shot at the android app.

Press enter or click to view image in full size
Backblaze app on Google Play store

I read the program policies on hackerone platform and downloaded the apk from android playstore → com.backblaze.android.

I connected my android device to PC and used adb to get a shell on the device using adb shell command , straightaway went ahead and opened up the /data/app/com.backblaze.android/base.apk , fetched the apk to the local PC using adb pull command.

After I had the base.apk on my machine I unzipped the apk and found classess.dex file , passed it to dex2jar tool to decompile into jar.

Now I had a jar file which could be easily read through the jd-GUI tool for reverse engineering of the app source code.

Once I had the source code I started to look at it and in B2TemporaryCredentials.class file I found 2 keys hardcoded which were → B2_APPLICATION_KEY and B2_APPLICATION_KEY_ID.

I directly reported this to the program on hackerone and they closed it as N/A as i was not able to show the impact.I was not really happy with the decision as I knew these keys were meant for something.

Brainstorming

It finally clicked me after some hours , I thought that if Backblaze offers a bucket service then there might be a possibility that these keys could be used for API calls.

I went ahead and searched for the API documentation on the site.I found https://www.backblaze.com/b2/docs/b2_authorize_account.html where it was clearly mentioned that you can make an API call using a curl request as shown below:

curl https://api.backblazeb2.com/b2api/v2/b2_authorize_account -u “APPLICATION_KEY_ID:APPLICATION_KEY”

So , I made an api call using the keys I got and below is the output disclosing auth_token and other relevant details like accountID as well as the permissions for accessing files,buckets etc

Authorization token received with permissions

When asked by the triage team to show more impact I created a bucket in this account through the auth token and account ID that I received using the 2 application keys and kept the name of bucket `sahil-bucket` :

Get Sahil Tikoo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Create Bucket Request:

curl -H “Authorization:4_0025efbe16f705d000000000_0193def8_***********************TEukBP1H7M=” “https://api002.backblazeb2.com/b2api/v2/b2_create_bucket?accountId=5efbe16f705d&bucketName=sahil-bucket&bucketType=allPrivate"

In the Response sahil-bucket was created with a bucket ID:

Bucket Created

In order to finally verify whether my bucket was created or not and also to list all the buckets in this account I made another API call using the API docs here : https://www.backblaze.com/b2/docs/b2_list_buckets.html .So I made a curl request to disclose the public/private buckets as shown below:

Request:

curl -H ‘Authorization: 4_0025efbe16f705d0000000000_0193e672_98f146_acct_SE_0MKH8BONETu-mAiYmKJH8Ihs=’ -d ‘{“accountId”: “5efbe16f705d”, “bucketTypes”: [“allPrivate”,”allPublic”]}’ “https://api002.backblazeb2.com/b2api/v2/b2_list_buckets"

And in the response I got all the buckets:

Buckets listing

I also had the privileges to delete buckets and do much more but i stopped here and waited for the decision.

Finally the account turned out to be an internal one which was used to host test buckets.As you can guess impact lowered.

Response from team

Anyways got some bounty and the bug was patched with the new release of backblaze app version 5.0.2

Bounty awarded

So Folks never loose hope even after your reports get closed as N/A, just never give up and focus on finding an impact from the information you gather in recon.

You can always reach out to me at my twitter Handle @viperbluff for any queries and help !!!

Till next time hasta la vista !!

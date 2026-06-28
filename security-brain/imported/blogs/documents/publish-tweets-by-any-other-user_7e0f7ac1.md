---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-30_publish-tweets-by-any-other-user.md
original_filename: 2019-01-30_publish-tweets-by-any-other-user.md
title: Publish tweets by any other user
category: documents
detected_topics:
- idor
- command-injection
- file-upload
- rate-limit
- api-security
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- file-upload
- rate-limit
- api-security
- supply-chain
language: en
raw_sha256: 7e0f7ac1b68ff45d97c0482a0dff905fb5346e490491191a26e2cb566da90377
text_sha256: 3061aa0fbf29521a65967cc1ad8edbb8f834fa2c05d1475f603ac2796d696981
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Publish tweets by any other user

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-30_publish-tweets-by-any-other-user.md
- Source Type: markdown
- Detected Topics: idor, command-injection, file-upload, rate-limit, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `7e0f7ac1b68ff45d97c0482a0dff905fb5346e490491191a26e2cb566da90377`
- Text SHA256: `3061aa0fbf29521a65967cc1ad8edbb8f834fa2c05d1475f603ac2796d696981`


## Content

---
title: "Publish tweets by any other user"
url: "https://medium.com/@kedrisec/publish-tweets-by-any-other-user-6c9d892708e3"
authors: ["Kedrisec (@kedrisec)"]
programs: ["Twitter"]
bugs: ["IDOR"]
bounty: "7,560"
publication_date: "2019-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5441
scraped_via: "browseros"
---

# Publish tweets by any other user

Publish tweets by any other user
Kedrisec
Follow
5 min read
·
Jan 30, 2019

150

1

Foreword

During the security exploration of Twitter social network as part of BugBounty-program, I found the vulnerability which allowed hackers to publish entries in Twitter-network by any user of this service, meanwhile without having the access to the account of a victim.

This vulnerability was found 26-th February 2017 and was fixed on 28-th February 2017.

Report reference: https://hackerone.com/reports/208978.
Now let’s look at the technical details of the vulnerability.

Introduction

There is one service in Twitter network as: https://ads.twitter.com/ , it has media-library with the possibility to upload media-files (video, pictures, gif-animation), also has the possibility to review media-files uploaded before, which were used at the moment of tweet publication. Library is available at this link:

https://ads.twitter.com/accounts/*id_of_your_account*/media.
Now let’s get started:

Let’s take a look

If we navigate to the library we’ll see the function for uploading media-files:

Press enter or click to view image in full size

After we press the button «Download media-file» and choose an appropriate file, we will see the picture:

Press enter or click to view image in full size

Let’s click the uploaded image, then we will see:

Press enter or click to view image in full size
We are able to tweet our media-file.
We are able to share media-file with any user.

Ok! So, now let’s take a closer look to functionality of tweet:

Press enter or click to view image in full size

What we may see here:

account_id — id of account (directly in the library)
owner_id -id of image owner
user_id — tweet will be published to the user, that has this id
media_key — id of the media-file that is being published (look at the screenshot № 3, it’s illustrated in the address-string)

Let’s introduce the following notation:

account №1 — my first account
account №2 — my second account

As i don’t remember the exact statements of the output errors, so let’s call them: «error №1», «error №2».

Let’s try

My steps to reveal the vulnerability:

Get Kedrisec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First of all i intercepted request for tweet publishing and changed parameters: owner_id and user_id in GET-request and in json, which was sent by POST-method, from the id of account №1 to corresponding id of account №2, but i have not received the expected result, but the error №1 instead.

After that, i decided to change owner_id and user_id in POST only, and i’ve received error №2, as far as i remember the text was the following: «User with owner_id * id which was a substitute* is not an owner of this media-file *here should be a media_key*»

I thought: «Ok», — and then i’ve done the following:

I took the account №2, went to the service ads.twitter.com, then went to the library, and uploaded the picture to know media_key in advance.

Аnd one thing led to another

Let’s return to the account №1:

Then we intercept the request for the tweet and change owner_id, user_id in GET and POST methods for the corresponding data of the account №2 and media key for that one, which we knew while uploading the picture during the work with the account №2 before. And look ! here we see the error №1. That’s very sad … but, nevertheless, when we made the substitution for owner_id and user_id in GET and POST methods earlier, there was only one error (error №1), and in the case of the substitution for owner_id and user_id only in POST method there was other error (error №2). Let’s try?

Change in request owner_id, user_id and media_key in POST method, then … we see response that informs us about successful attempt of tweet publication ! Passing to the account №2 we see that the tweet with formerly uploaded picture from account №2 was published, though account №2 hasn’t published nothing itself.

Let’s try harder

Well, at this moment we have the possibility to publish twits by any user, but the same time we have explicit restriction, which seriously decreases the impact(severity of a vulnerability), here is: user which we use to make a publication must have a media-file uploaded. Moreover, it’s needed to know media_key of this file and it’s almost impossible to reveal it by the means of brute force, as it contains 18 digits. In my explorations i didn’t find 100 % way to know this media_key. There were always some restrictions and circumstances which allow to get that media_key. Well, It’s over ? Is there any outlet or decision ? Should we report the current situation ? Absolutely not ! I personally think that this vulnerability could be brought to the extreme point of severity ! Do you remember about the possibility to share uploaded media-file ? I came to a very interesting idea that probably if we share our media-file with the user, which is used to make a publication from his account, he will be considered as owner of this media-file, error №2 wouldn’t appear and tweet in it’s turn would be published successfully. And that was really happened !

For successful exploiting of this vulnerability we didn’t have media_key, but in the case when we’re the owners of this file, we may see it’s media_key (screenshot №3).

Now, scenario looks like that:

We upload our media-file.
Share this file with user, whose account we use to publish entry.
Intercept the query for tweet publication and simply change in POST-method following data: owner_id and user_id to id twitter of a victim account (it’s quite simple to know this, as there are a lot of online services).
We receive the message about successful attempt of tweet-publication.
Have fun

Now we can report the vulnerability with peace of mind.

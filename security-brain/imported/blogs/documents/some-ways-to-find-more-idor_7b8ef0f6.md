---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-26_some-ways-to-find-more-idor.md
original_filename: 2021-06-26_some-ways-to-find-more-idor.md
title: Some ways to find more IDOR
category: documents
detected_topics:
- idor
- jwt
- access-control
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- idor
- jwt
- access-control
- command-injection
- password-reset
- otp
language: en
raw_sha256: 7b8ef0f61a12fb80ca86c45220d6896460f85b843d32d63c14c107780b236097
text_sha256: 7b13bd9739ef74a3ff313f35162cac17425add2a6a18c70b52d0b2cbdce8d412
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Some ways to find more IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-26_some-ways-to-find-more-idor.md
- Source Type: markdown
- Detected Topics: idor, jwt, access-control, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7b8ef0f61a12fb80ca86c45220d6896460f85b843d32d63c14c107780b236097`
- Text SHA256: `7b13bd9739ef74a3ff313f35162cac17425add2a6a18c70b52d0b2cbdce8d412`


## Content

---
title: "Some ways to find more IDOR"
url: "https://16521092.medium.com/some-ways-to-find-more-idor-da16c93954e5"
authors: ["Thái Vũ  (@thaivd98)"]
bugs: ["IDOR"]
publication_date: "2021-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3543
scraped_via: "browseros"
---

# Some ways to find more IDOR

Top highlight

Some ways to find more IDOR
Thái Vũ
Follow
4 min read
·
Jun 26, 2021

1.6K

15

Hello friend!

I had learnt a lot of knowledges from others’ s blogs, write-ups, so I think I should give back to the community. :) I hope this blog will be useful for someone.

This post is about some methodologies I had used to find IDOR vulnerability and some my findings relate to IDOR bugs.

No ID, No Worry

This is an bug that I had found in the past. It’s a site-wide IDOR allow me to read/modify/delete any information of other users, and yes, sure, I could takeover all accounts.

After playing with functions of main website, I took a look back on my Burp History

Press enter or click to view image in full size

Do you notice that? There is no parameter or URL path contains ID, but there is one thing causes my eyes. These API had a common pattern

/something/something/self/something

These APIs return my information or doing some actions on behalf of me. I ask myself what if I replace that self word with my user ID ( user ID could be found on JWT token). For example, /ngprofile/aggregate/31337/fullProfile .

And BOOM! The response return my full profile information.

I tried to replace my user ID with other user ID ( the user ID is increment). So I could read other users’ s profile information.

Press enter or click to view image in full size

I observed that all API contain self word is vulnerable to that IDOR, even the Change Email API.

Press enter or click to view image in full size

So I could change email of any user. I could chain this bug with “Forgot password” function to send the reset passsword link of victim to my control emails and use that link to reset password of victim. So I could login to any account in the system.

Key Takeaways

Try to understand applications ( how could this API/request authorize users, why there is no parameter, etc.), analyze carefully requests/responses. You could find more IDORs.

2. Don’t just replace ID

When testing IDOR vulnerability, don’t just replace our own ID with others user/object ID. Sometimes one character could made a different.

Scenario 1:

The screenshot below shows when I replace my user ID with other user ID in API /accounts/0001176361, the server’s response “Invalid account number”

Press enter or click to view image in full size

The screenshot below shows when I add “/” character append to this user ID, the server’s response return all information about this user. Maybe the “/” character breaks logic of the regex or pattern that server used to restrict access.

Press enter or click to view image in full size

Scenario 2:

Get Thái Vũ’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The screenshot below shows when I replace my application ID with other’s application ID (18385027) in API api/applications/18385027, the server’s response “access_denied” with HTTP code 401

Press enter or click to view image in full size

The screenshot below shows after fuzzing all character, I could bypass authorization control by appending %20, %09, %0b, %0c, %1c, %1d, %1e, %1f to application ID in this API. The server would return full information of that application.

Press enter or click to view image in full size
Key Takeaways

(Old but gold): Don’t just replace IDs and wait for luck. Try to fuzz all possible character ( my list is %00 -> %ff) to break the logic of the regex or pattern that server used to restrict access. The more you fuzz, the more you luck.

3. Don’t Ignore IDOR in GraphQL applications.

A long time ago, I was very noob in testing GraphQL applications ( still the same now).

When playing bug bounty in a private program, I observed this application using GraphQL. Immediately I remove all endpoints /graphql from scope =)).

Press enter or click to view image in full size

After playing with some functions, I gave a look at Burp History again and there is no request is found😐. So all APIs of this application used GraphQL.

I had wanted to know what does these requests look likes. So I add again this /graphql endpoints to my scope. 😶

And luckily, I found 2 IDOR in that application ( just replace IDs).

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

After that, I realize that there is a quite hard to implement security in GraphQL, even Facebook and Google have many bugs in GraphQL endpoints.

Key Takeaways

Don’t ignore anything. 😜

I hope this blog can help someone find more IDOR vulnerability. This community help me so much so I want to give back my experience to community. 😄

You can contact me via https://twitter.com/thaivd98 .

Thanks for reading! Happy Hacking!

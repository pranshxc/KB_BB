---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-12_broken-access-control-leads-to-full-team-takeover-and-privilege-escalation.md
original_filename: 2022-10-12_broken-access-control-leads-to-full-team-takeover-and-privilege-escalation.md
title: Broken Access Control leads to full team takeover and privilege escalation
category: documents
detected_topics:
- access-control
- command-injection
- graphql
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- graphql
- api-security
- mobile-security
language: en
raw_sha256: d7c89e58dc07835ad297b42b7399e84cd804ec4b02ba894a28d0c308ad2eab65
text_sha256: 41f857e3fad04188fd65337c7e3eca99e84e7e1291004d563c0ca6a7cc461b77
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access Control leads to full team takeover and privilege escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-12_broken-access-control-leads-to-full-team-takeover-and-privilege-escalation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, graphql, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `d7c89e58dc07835ad297b42b7399e84cd804ec4b02ba894a28d0c308ad2eab65`
- Text SHA256: `41f857e3fad04188fd65337c7e3eca99e84e7e1291004d563c0ca6a7cc461b77`


## Content

---
title: "Broken Access Control leads to full team takeover and privilege escalation"
url: "https://abdelhameedghazy.medium.com/broken-access-control-leads-to-full-team-takeover-and-privilege-escalation-6f50174f29ce"
authors: ["Abdelhameed Ghazy (@El3Etraa1)"]
bugs: ["Broken Access Control", "Privilege escalation"]
publication_date: "2022-10-12"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2056
scraped_via: "browseros"
---

# Broken Access Control leads to full team takeover and privilege escalation

Broken Access Control leads to full team takeover and privilege escalation
Abdelhameed Ghazy
Follow
3 min read
·
Oct 12, 2022

145

2

Hello all,

Today I will share one of the most finding that I was interested in while finding it.

Press enter or click to view image in full size

Our target provides teams with two privileges member and admin.
the team had some sensitive data like credit cards

After testing the functions I went to invite users function

the admin is the only one who can invite new members to the team

as you see there is a request to a Graphql with Cookies and Authorization header in the request
and the request parameters :

1- account id that holds the team id
2- inviteeEmailAddress: the email address of the user that will be invited
3- inviterId: the id of the admin of this team
4- roleName: it can hold between two values ( member or admin )

The first thing i tried is to remove the cookies and then the authorization header and I notices that the server responded with 200 ok and the request was processed successfully

Press enter or click to view image in full size
the modified request without authentication or authorization element

and I received the invitation to my email successfully

so now we know that the request depends on the parameters only

Get Abdelhameed Ghazy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are two attack scenarios :

1- Privillige Escallation

as a member of the team, i can see the team id

so I only need to get the inviter id ( admin id )

but how can I get this user id ???
first, I found the admin email in the members section on the team page

so I started thinking about how to interact with him so the id may be Leaked in any request
Note that there are no public profiles for any user
after some digging, I decided to invite the victim user to join my team (hacker team )

After I sent an invitation to the victim account to join my team ( Hacker Team)

I noticed that his membership is pending for his confirmation then after I go through the burp suite history I found a request to get the team data so I repeated this request again and boom I found the victim id

Press enter or click to view image in full size

note that I got the victim's id without any interaction from him

and then I sent the invite request again with the required parameters

Press enter or click to view image in full size

finally, i received the invitation to my email and after accepting it I became an admin and take over the victim team with zero clicks from him

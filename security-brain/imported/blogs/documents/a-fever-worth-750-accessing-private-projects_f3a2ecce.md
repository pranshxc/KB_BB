---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-22_a-fever-worth-750-accessing-private-projects-.md
original_filename: 2021-09-22_a-fever-worth-750-accessing-private-projects-.md
title: A fever Worth 750$- [Accessing Private Projects ]
category: documents
detected_topics:
- idor
- command-injection
- otp
- graphql
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- otp
- graphql
- information-disclosure
language: en
raw_sha256: f3a2eccec9bd5c73bf7574abd37b93c19fb8045be96112c4b60b286527a93de9
text_sha256: 61ff52921c16cece7fd27fad8f429c61b8aae288b91befa03c0e201a811e9a01
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# A fever Worth 750$- [Accessing Private Projects ]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-22_a-fever-worth-750-accessing-private-projects-.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, graphql, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `f3a2eccec9bd5c73bf7574abd37b93c19fb8045be96112c4b60b286527a93de9`
- Text SHA256: `61ff52921c16cece7fd27fad8f429c61b8aae288b91befa03c0e201a811e9a01`


## Content

---
title: "A fever Worth 750$- [Accessing Private Projects ]"
url: "https://medium.com/@shakti.gtp/a-fever-worth-750-accessing-private-projects-d113c561311f"
authors: ["Shakti Mohanty (@3ncryptSaan)"]
programs: ["Mozilla"]
bugs: ["IDOR", "Information disclosure"]
bounty: "750"
publication_date: "2021-09-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3296
scraped_via: "browseros"
---

# A fever Worth 750$- [Accessing Private Projects ]

shakti mohanty
 highlighted

A fever Worth 750$- [Accessing Private Projects ]
shakti mohanty
Follow
3 min read
·
Sep 21, 2021

331

1

Hello Champs, Shakti here , I hope you all are having some good times. Usually i’m not a person who makes writeup for the findings, but i thought of doing it often now. #sharing_is_caring

The Bug is all about how i manage to access the private projects, So let’s start….

As i am into the cyber security profession, i used to do bug bounty not often and i hunt only on HackerOne.

It was 11 pm , I was having fever, can’t sleep & i was alone with the beast #MacM1. I thought to have a test on the pending private invitations. So it was a private program having top ranked hackers invited before. Whenever i got a target , i just roam around on each and every functionality to understand it’s flow. As it was a Single scoped domain, i did the same.

Basically it was a recruiting application for the projects. What i observed is “The Admin can Create projects and can invite talented candidates as per their need. The Project status can be either Shared or Private. If it will be private, it can be only accessed by the admin. If it will be shared , then only the invited individuals can access the projects.”

Now if admin shares the project with candidate-A then the link will be like, https://example.com/projects/alphanumeric_project_id_here?share_token_id=some_random_token_here

Observe To get access to a project you need the project_id & share_token_id , which is obviously alphanumeric and unpredictable. I quickly created project-A and project-B being an admin.[Note: Project_id of Project-A=xxxxxxxxxxxxxxx & Project-B=zzzzzzzzzzzzzzz ]. Now i shared the project-A with candidate-A, so now the status of project-A is shared and the status of project-B is private.

While sharing the Project-A to candidate-A, the url i got https://example.com/projects/xxxxxxxxxxxxxxx?share_token_id=yyyyyyyyyyyyyyyy. The idea was to access the private project with the Shared project’s share_token_id , so i changed the project_id of Project-A with project_id zzzzzzzzzzzzzzz (which is project-B’s project_id ) which was private before. So the modified url will be like https://example.com/projects/zzzzzzzzzzzzzzz?share_token_id=yyyyyyyyyyyyyyyy.

I tried to access the above modified Url and i was able to access the private project.

Yes….Yes….Yes i did it…

Now i can access the project , which was set private by the admin and that was only accessible by the admin.

Wait a minute…

Being a candidate how can we get the private project id of an admin?????

If here i would report, they might close it as informative or low saying “you can’t predict the alphanumeric private project_id” . Now the aim is to find the private project_id.

Hmmmm…. I was like …. let’s Do this…..

Get shakti mohanty’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The application was using graphQL…Hmm .. I fired up Autorize and configured with all the necessary cookies and token headers of the candidate user. Added the scope filters on it. Now i again roamed on each endpoint manually within the admin panel. After some time i checked the logs of Autorize, i got 2 graphQL endpoints where the private project_id is getting exposed due to lack of authorisation . So now the candidate who was a part of project-A can access the private project_id through the graphQL endpoint

Now we have a complete attack scenario,

1- Admin Invited candidate-A to Project-A. [note: project-B is still private ]

2- Now Candidate-A is a part of project-A.

3- Through the graphQL endpoint discussed above the candidate-A Got the Private project_id of project-B.

3- Candidate-A modified the invite Url from https://example.com/projects/project_id_of_A?share_token_id=some_random_token to https://example.com/projects/project_id_of_B?share_token_id=some_random_token to

4- Candidate got access to the Private Project-B unauthentically.

Reason:

1- Here the share_token_Id of “Project-A” getting validated as a valid share_token_Id for “project-B” and the “project-B” is being accessed by the attacker since it is in private state.

2- The private project id is getting disclosed unauthentically to the candidate through the graphQL endpoint.

Timeline

— — — — — -

Bug Reported: Sep-3 2021 11.57 Pm

Bug Triaged & Marked As High : Sep-4 2021 00:18 Am

Rewarded 750$ with a complement : Sep-4 2021 00:35 Am

See you on next write-ups.

If you found it helpful..

Follow me on: Instagram —Twitter — Linkedin

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-03_invitation-hijacking_2.md
original_filename: 2022-11-03_invitation-hijacking_2.md
title: Invitation Hijacking
category: documents
detected_topics:
- access-control
- jwt
- idor
- command-injection
- otp
tags:
- imported
- documents
- access-control
- jwt
- idor
- command-injection
- otp
language: en
raw_sha256: 1715325c459ced9e1dbcd537892d9308592c07366bf2d59af59f92a2b59e9d3e
text_sha256: 794663adbf9f6e051f6ac37bad1b0e2045c6ff77ddc6e8e57ac132ac15dc8fee
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Invitation Hijacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-03_invitation-hijacking_2.md
- Source Type: markdown
- Detected Topics: access-control, jwt, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `1715325c459ced9e1dbcd537892d9308592c07366bf2d59af59f92a2b59e9d3e`
- Text SHA256: `794663adbf9f6e051f6ac37bad1b0e2045c6ff77ddc6e8e57ac132ac15dc8fee`


## Content

---
title: "Invitation Hijacking"
url: "https://medium.com/@vflexo/invitation-hijacking-4d6467f418cc"
authors: ["vFlexo (@vflexo)"]
bugs: ["Broken authorization", "Privilege escalation"]
publication_date: "2022-11-03"
added_date: "2022-11-05"
source: "pentester.land/writeups.json"
original_index: 1953
scraped_via: "browseros"
---

# Invitation Hijacking

Invitation Hijacking
Vishal Barot
Follow
4 min read
·
Nov 3, 2022

133

3

Hi Guys! Long time no see!

Lets discuss some easy catches that you guys might not want to ignore while doing security testing/ bug bounty.

We have seen many sites with privileged users like member, admin , owner or viewer, editor, admin etc.

There are various ways through which an invitation might get sent to a new member but in most of the cases it would contain a token.

For example: https://example.com/team/clubwalterwhite/?invite_token=67fbhv7595bchfbfee33q

Now there are a few things you can do, those are:

Check if the invitation token is coming on HTTP or HTTPs protocol.

For example: If url is this http://example.com/team/clubwalterwhite/?invite_token=67fbhv7595bchfbfee33q sends an invitation token can be stolen by anyone who is in the same network and if the invitation token is not linked with the user-email for which it is created then it can lead to invitation hijack i.e attacker can add himself in the organization/group.

2. Check if the invitation token is getting leaked to untrusted third party sites.

3. Use the invitation token for another user by crafting a request with cookie/JWT of another user.

4. Use the token for IDOR techniques(If you see any User Identifier)

5. In the request if you see the group-name/organization name try to change it to some another organization and see if you can use this token to become member of some other group/organization.

6. Decode the token if it is generated using known algorithm and if you succeed then try to directly generate tokens for other users.

7. If the tokens are not generated using any known algorithm then try to read JavaScript files to see if the token generation/processing code(encode or decode) is mentioned somewhere in the code.

It is very important to follow all the security measures while implementing invitation mechanism. Otherwise, it can have dangerous consequences.

Btw.. the “Danger” word reminds me of this:

Now let's talk about what I have found very recently.

On the target site I created two accounts for the organization let's say “Heisenberg”.

One of the 2 users is admin another is member.

Get Vishal Barot’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the member user cannot invite more members to the organization, only an admin can do that.

Member user panel:

Press enter or click to view image in full size

Admin user panel:

Press enter or click to view image in full size

Now I sent invite to one of email vflexobughunting@gmail.com, copied the invitation link and opened it in new window. It showed me the panel shown below and instead of the email to which I sent the invitation I wrote some other email(barotvbvishal@gmail.com). In simple words I tried to use the invitation link of vflexobughunting@gmail.com for barotvbvishal@gmail.com.

Surprisingly it sent the magic invitation link to the email which was not supposed to be linked with the invitation token at the very first place(barotvbvishal@gmail.com).

I went to the new email that I mentioned and used magic link and then got myself added to the “Heisenberg” organization from email barotvbvishal@gmail.com who never received any invitation to join the organization.

I used the same invitation token to add many other emails as well, which is another vulnerability. Technically the token should expire once it has been used.

In the below screenshot you can see I added multiple members using same token:

Press enter or click to view image in full size

Impact: The token here is not linked with the email it got generated for. Which allows the member to distribute to token with other people allow them to add themselves in the organization. Technically the Member user cannot add more people to the organization only Admin can (As there is no “invite-user” functionality in Member user panel). But through this vulnerability member user can indirectly add new users to the organization.

Remediation:

Invitation tokens should be properly linked with their respective users(email).
Invitation tokens must not be re-used.

Status of the vulnerability submission: Triaged

Moral of the day: Do never forget to check invitation tokens

I hope you guys liked reading this. :)

See ya soon!

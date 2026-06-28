---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-09_see-whether-a-hackercup-facebook-participant-allows-recruitment-contact.md
original_filename: 2020-07-09_see-whether-a-hackercup-facebook-participant-allows-recruitment-contact.md
title: See whether a Hackercup Facebook participant allows recruitment contact
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- business-logic
language: en
raw_sha256: ce3b9a38f4d72c3345ddd98d7bd6afd47ad9d1b7e1ae10e7ea4ca265a5e38c2b
text_sha256: 77c538dde351a183824bddeb04d10d414a570c1d40f8f1edcf6549eff4dde172
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# See whether a Hackercup Facebook participant allows recruitment contact

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-09_see-whether-a-hackercup-facebook-participant-allows-recruitment-contact.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `ce3b9a38f4d72c3345ddd98d7bd6afd47ad9d1b7e1ae10e7ea4ca265a5e38c2b`
- Text SHA256: `77c538dde351a183824bddeb04d10d414a570c1d40f8f1edcf6549eff4dde172`


## Content

---
title: "See whether a Hackercup Facebook participant allows recruitment contact"
page_title: "See whether a Hackercup Facebook participant allows recruitment contact - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/see-whether-a-hackercup-facebook-participant-allows-recruitment-contact/"
final_url: "https://philippeharewood.com/see-whether-a-hackercup-facebook-participant-allows-recruitment-contact/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2020-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4421
---

Posted on [July 9, 2020](https://philippeharewood.com/see-whether-a-hackercup-facebook-participant-allows-recruitment-contact/)

# See whether a Hackercup Facebook participant allows recruitment contact

Facebook launched a new portal for the Facebook Hackercup competition <https://www.facebook.com/codingcompetitions/>. At a user’s profile <https://www.facebook.com/codingcompetitions/profile> there seems to show the indication at “Private Contact Info” that any information (other than name, contests, submissions) will be private. However, the field for viewing whether the user allows recruitment contact is public to all.  
  
The impact is minor as it’s just a boolean field however Facebook isn’t keeping the privacy information here consistent by allowing this. Since a Hackercup participant links back to the Facebook user object, this can be used to pull all entrants per each competition all the back way back to 2011 and see the breakdown for who allows a recruiter to contact them.  
  
A participant object looks like the following,

`{"data":{"node":{"__typename":"CodingContestIndividualEntrant","entrant_personal_info":{"recruitment_preference":"ALLOW_RECRUITMENT_CONTACT","individual_entrant_user":{"id":"13608786"}}}},"extensions":{"is_final":true}}`

If the user changes his preference at <https://www.facebook.com/codingcompetitions/profile>, `DISALLOW_RECRUITMENT_CONTACT` will be shown instead.

**Impact** (A verbatim explanation of the bounty by Facebook):  
  
A Hackercup participant request to be contacted by FB recruiters is accessible publicly  
  
**Timeline**

Jul 9, 2020 – Report sent  
Jul 14, 2020 – Confirmation of submission by Facebook  
Jul 15, 2020 – Further investigation of submission by Facebook  
Jul 27, 2020 – Confirmation of patch by Facebook  
Aug 13, 2020 – Bounty awarded by Facebook

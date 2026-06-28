---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-28_page-admin-disclosure-via-an-upgraded-page-post.md
original_filename: 2020-02-28_page-admin-disclosure-via-an-upgraded-page-post.md
title: Page Admin Disclosure via an Upgraded Page Post
category: blogs
detected_topics:
- access-control
- command-injection
- information-disclosure
tags:
- imported
- blogs
- access-control
- command-injection
- information-disclosure
language: en
raw_sha256: 19a62cd76d5294c29e3c06eb0314d4bdf0f3a1918a5c072a1a37c01a4f8cb784
text_sha256: 7f8761a5bce320816b0af36031be7d0c225e763afb67efc5f69966924733a941
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Page Admin Disclosure via an Upgraded Page Post

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-28_page-admin-disclosure-via-an-upgraded-page-post.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `19a62cd76d5294c29e3c06eb0314d4bdf0f3a1918a5c072a1a37c01a4f8cb784`
- Text SHA256: `7f8761a5bce320816b0af36031be7d0c225e763afb67efc5f69966924733a941`


## Content

---
title: "Page Admin Disclosure via an Upgraded Page Post"
url: "https://medium.com/@timpaxerror/page-admin-disclosure-via-an-upgraded-page-post-57863fb02c50"
authors: ["Dan Fabro (@0x61_)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Information disclosure"]
bounty: "3,000"
publication_date: "2020-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4746
scraped_via: "browseros"
---

# Page Admin Disclosure via an Upgraded Page Post

Page Admin Disclosure via an Upgraded Page Post
Dan Fabro
3 min read
·
Feb 29, 2020

--

Press enter or click to view image in full size
src: https://www.askbuddie.com/blog/unauthorized-comments-on-facebook-live-stream/
Description

Soooo I was posting for a special event that happened in one of my organization’s pages. I upgraded that post through a prompt message, “It looks like something special happened. Want to make this post a life event?” when suddenly I noticed an unusual behavior; it disclosed myself as one of the page admins publicly, through my profile’s Life Events section by redirecting any Facebook user who visits my profile to such Page Post after clicking on it. Thus, implying I’m one of the page’s admins.

Steps to replicate
UserA = Account who manages a Facebook Page (page admin)
UserB = Stalker/Attacker
Using UserA, create a public post on the Page you are managing. Make sure that such post is congratulatory-worthy or something that would pop out the Life Event message enabling such post to be upgraded.

2. [Still UserA’s perspective] Once already posted, notice a prompt message on top of it saying: “It looks like something special happened. Want to make this post a life event?” which is then giving me two options, one is “No Thanks” which declines the post being upgraded and the other is “Upgrade Post” that enables such post to be upgraded. Click on the “Upgrade Post” button and supply the necessary details.

3. [Still UserA’s perspective] Go to your profile’s About Section Life Events [base url/username/about?section=year-overviews] and notice that the Life Event you posted via your page is listed there.

Or simply, go to your profile, scroll down to your Life Events section to verify.

4. [UserB’s perspective] UserB goes to UserA’s profile and clicks on any of UserA’s Life Events, it redirects UserB to the Page Post thereby validating/disclosing that UserA is an admin of that Page since it was linked to his or her personal account as a Life Event.

Impact

“This could have led to a page admin disclosure by upgrading a page post to a life event.” -Facebook

POC (Proof-of-Concept)
Timeline

December 19, 2019 :: Report Submitted

Get Dan Fabro’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

January 09, 2020 :: Triaged after several discussions

“Hi Dan, Thanks for your patience and for reporting this information to us. We are sending it to the appropriate product team for further investigation. We will keep you updated on our progress. Thanks”

February 06, 2020 :: Fixed the bug

February 07, 2020 :: Bounty awarded

Got myself listed on Facebook’s Whitehat Hacker Hall-of-Fame (2019)
Number 65: https://www.facebook.com/whitehat/thanks/

Acknowledgment

Would like to thank Ajay Gautam and AJ Dumanhug for creating writeups that inspired me to hunt similar security issues on Facebook.

Ajay Gautam : https://medium.com/bugbountywriteup/page-admin-disclosure-facebook-bug-bounty-2019-ee9920e768eb

AJ Dumanhug : https://medium.com/bugbountywriteup/disclosure-of-facebook-page-admin-due-to-insecure-tagging-behavior-24ff09de5c29

Takeaways
Be observant of the slightest, smallest details. I always keep a checklist whenever I hunt for security issues on a particular platform. You might want to do it too.
Understand the platform’s features if it is showing any unusual behavior, and/or if privacy has been bypassed, then find strong, supporting details with what you found and discuss with them (security team) why that’s happening and why that’s a security issue to deal with.

Thanks for reading!

Connect with me on LinkedIn!

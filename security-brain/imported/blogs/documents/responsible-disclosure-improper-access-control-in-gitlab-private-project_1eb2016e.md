---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-19_responsible-disclosure-improper-access-control-in-gitlab-private-project.md
original_filename: 2019-04-19_responsible-disclosure-improper-access-control-in-gitlab-private-project.md
title: 'Responsible disclosure: improper access control in Gitlab private project.'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 1eb2016e1769eb50bdb7fed57e0ae9d517d227b288a626b442be08f019355a91
text_sha256: 601368466bc7cac8ce654b088dc215342f040e7ba5bf601bc12404e34be3ebd2
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Responsible disclosure: improper access control in Gitlab private project.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-19_responsible-disclosure-improper-access-control-in-gitlab-private-project.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1eb2016e1769eb50bdb7fed57e0ae9d517d227b288a626b442be08f019355a91`
- Text SHA256: `601368466bc7cac8ce654b088dc215342f040e7ba5bf601bc12404e34be3ebd2`


## Content

---
title: "Responsible disclosure: improper access control in Gitlab private project."
url: "https://rpadovani.com/gitlab-responsible-disclosure"
final_url: "https://rpadovani.com/gitlab-responsible-disclosure"
authors: ["Riccardo Padovani (@rpadovani93)"]
programs: ["GitLab"]
bugs: ["Broken authorization"]
bounty: "2,000"
publication_date: "2019-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5301
---

# Responsible disclosure: improper access control in Gitlab private project.

As I said back in September regarding a responsible disclosure about Facebook, data access control isn’t easy. While it can sound elementary, it is very difficult, both on a theoretical side and on a practical side.

[ ![Profile picture of Riccardo Padovani](https://rpadovani.com/media/ptrpi1Gl1jueItEHEK7cAistnEI0oU5kLV14EQsL.png) Riccardo Padovani ](https://rpadovani.com/author/riccardo-padovani)

|  Published  Apr 19, 2019 

This issue was firstly reported on [HackerOne](https://hackerone.com/reports/310185) and was managed on the [Gitlab issues’ tracker](https://gitlab.com/gitlab-org/gitlab-ce/issues/42726). Both links are now publicly accessible.

## Summary of the issue

  * Rogue user is added to a private group with dozens of projects

  * The user’s role in some projects changes

  * Rogue is fired, and removed from the group: they still have access to projects where their role was changed

The second step could happen for a lot of different reasons:

  * _rogue_ is added as `master` \- knowing this vulnerability, they decrease their privileges to stay in some projects (this is the only **malicious** one)

  * _rogue_ is added as `developer`, but they become responsible for some projects, and are promoted to `master` role

  *  _rogue_ is added as `reporter`, and then they are promoted for a project, and so on.

When an admin removes a user from a private group, there is no indication that the user still has access to private projects, if their role was changed.

## Impact

User can still see all resources of a project of a secret group after they have been removed from the parent’s group.

## Timeline

  * **29 January 2018** : First disclosure to Gitlab

  * **9 February 2018** : Gitlab confirmed the issue and triaged it, assigning a **medium** priority

  * **25 February 2018** : I ask for a timeline

  * **27 February 2018** : They inform me they will update me with a timeline

  * **16 March 2018** : Almost two months are passed, I ask again for a timeline or suggest to go public since administrators of groups can easily check and avoid this vulnerability

  * **17 March 2018** : They inform me they will update me with a timeline, and ask to do not go public

  * **Somewhere around December 2018** : the team think the issue has been fixed, and close the internal issue - without communicating with me

  * **17 January 2019** : I ask for an update - they will never reply to this message

  * **25 January 2019** : the security team sees this is still an issue

  * **31 January 2019** : the fix is deployed in production and [publicly disclosed](https://about.gitlab.com/2019/01/31/security-release-gitlab-11-dot-7-dot-3-released/), without informing me

  * **5 March 2019** : I ask again for another update

  * **12 March 2019** : Gitlab says the issue has been fixed and awards me a bounty

## Bounty

Gitlab awarded me a $2000 bounty award for the disclosure.

If you follow my blog, you know I deeply love Gitlab: I contribute to it, I write blog posts, and I advocate for it any time I can. Still, I think this experience was _awful_ , to say the least. There was a total lack of communication by their side, they thought they fixed the issue the first time, but actually, it wasn’t fixed. If they had communicated with me, I would have double checked their work. After that, they deployed the fix and went public, without telling me. I was not interested in the bounty (for which I am grateful), I reported the issue because I care about Gitlab. Nonetheless, my love for Gitlab is still the same! I just hope they will improve this part of communication / contributing to Gitlab: in the last couple of years the [community around the project grew a lot](https://about.gitlab.com/2019/04/17/contributor-program-update/), and they are doing amazing with it, maybe the Community team should step in and help also the security community?

For any comment, feedback, critic, leave a comment below, or drop an email at `[[email protected]](/cdn-cgi/l/email-protection)`.

Regards,  
R.

[security](https://rpadovani.com/tag/security) [gitlab](https://rpadovani.com/tag/gitlab)

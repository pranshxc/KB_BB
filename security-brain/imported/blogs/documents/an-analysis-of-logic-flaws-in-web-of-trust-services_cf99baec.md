---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-13_an-analysis-of-logic-flaws-in-web-of-trust-services.md
original_filename: 2018-02-13_an-analysis-of-logic-flaws-in-web-of-trust-services.md
title: An analysis of logic flaws in web-of-trust services
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: cf99baecc2234918eb7ce39db4e3eca75e4e80103146d43b1c71f26151a5c3c3
text_sha256: a071e50c09330bc47731992875bb84fb7bee8c3c03a233fde7e01f44f178dfbc
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# An analysis of logic flaws in web-of-trust services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-13_an-analysis-of-logic-flaws-in-web-of-trust-services.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `cf99baecc2234918eb7ce39db4e3eca75e4e80103146d43b1c71f26151a5c3c3`
- Text SHA256: `a071e50c09330bc47731992875bb84fb7bee8c3c03a233fde7e01f44f178dfbc`


## Content

---
title: "An analysis of logic flaws in web-of-trust services"
page_title: "An analysis of logic flaws in web-of-trust services | EdOverflow"
url: "https://edoverflow.com/2018/logic-flaws-in-wot-services"
final_url: "https://edoverflow.com/2018/logic-flaws-in-wot-services/"
authors: ["EdOverflow (@EdOverflow)"]
programs: ["Keybase"]
bugs: ["Logic flaw"]
publication_date: "2018-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5976
---

Feb 13, 2018

# An analysis of logic flaws in web-of-trust services

## Abstract

Web-of-trust services (WOT) such as Keybase, Onename, and Blockstack promise to verify individuals’ identities on the web. Since many applications on the web are not consistent this often leads to unintended behaviour and therefore security vulnerabilities in web-of-trust services. This write-up analyses three attack vectors that I stumbled across while conducting research on the security of WOT services.

## The Technology Behind WOT Services

WOT services allow users to create tokens and place them on their personal pages (e.g. GitHub profile). The service will then look for the token using a scraper and if the token is valid, display that the user does in fact own that external page. The idea behind this method is so that users can display what pages on the web belong to them and then tie their WOT account to all of those external services. On top of that, since the verification tokens need to be publicly accessible, other users can verify that the proof is legitimate by visiting the page containing the token.

![TomNomNom’s Keybase profile](https://user-images.githubusercontent.com/18099289/36176220-cf811d06-1109-11e8-895f-8e8c4a350483.png)User TomNomNom cryptographically verifying their online identity on Keybase.

## Attack Vector One – Distribution Of Content On Timelines

On the web a lot of profile-based applications allow redistribution of content by sharing someone else’s entry on your personal timeline – on Twitter users can _retweet_ content and on GitHub people can _fork_ projects. Since some WOT services use a public entry or post to verify the user’s identity, I asked myself whether it would be possible to claim ownership of someone else’s account by having them share a token that was posted onto an attacker’s timeline. One particular service stood out for me, GitHub, where WOT applications such as Keybase require users to place the verification token into a GitHub gist file. The interesting behaviour that I noticed with GitHub is that when a user forks a gist, the gist is not only displayed on the user’s timeline, it replaces the original author’s username with the sharer’s username.

![](https://user-images.githubusercontent.com/18099289/36165627-1901716e-10e8-11e8-9def-a3349954851a.png)A forked GitHub gist — the original author is EdOverflow and the gist was forked by bayotop.

One vulnerable service was Keybase, where if an attacker could convince a victim to fork their GitHub gist, the attacker would be able to claim ownership of the victim’s GitHub username. On top of that, Keybase allowed modification of the verification snippet, allowing an attacker to hide the token in an HTML comment.

An example attack using this technique against Keybase could have unfolded as follows:

  1. The attacker requests a verification token from Keybase for the victim’s GitHub username;
  2. Keybase prompts the attacker to place the verification token in a `keybase.md` gist;
  3. The attacker creates a `keybase.md` gist hiding the verification token in an HTML comment;
  4. The victim forks the attacker’s GitHub gist;
  5. The attacker instructs Keybase to verify `/<victim>/keybase.md`.

As a result, the attacker’s Keybase account states that they own the victim’s account. To make matters worse, Keybase has a [browser extension](https://keybase.io/docs/extension) that allows users to browse to certain applications (e.g. GitHub, Twitter, Hacker News, etc.) and message the user on Keybase via the profile page – the extension adds a little messaging window on the user’s profile. Messages are sent to the account on Keybase that has verified ownership of the account. This means the extension will trick the user into thinking they are messaging the intended recipient, but all messages land in the attacker’s inbox since they control the victim’s username.

![](https://user-images.githubusercontent.com/18099289/36165628-1921e5ac-10e8-11e8-9fc5-e3ac95e98d1e.png)Hijacked GitHub username (@jackds1986) viewed in the Keybase browser extension. All messages are sent to a user called "totallynotjackds" on Keybase.

[Blockstack](https://blockstack.org/) and [fireblock.io](https://fireblock.io/) were also vulnerable to this attack vector. In most cases, the fix consisted of simply verifying whether the GitHub gist was a fork using GitHub’s gist API.

## Attack Vector Two – Namespace attacks

Some WoT services require placing the verification token in a specific filename. Keybase, for example, as mentioned in the previous section, require GitHub verification tokens to be placed in GitHub gists called _keybase.md_. On web assets, Keybase require the file to be named `keybase.txt` and either placed under the top-level directory or the `.well-known` path. The reason behind the `.well-known` proposal in [RFC5785](https://tools.ietf.org/html/rfc5785), is to prevent filename collisions and clogging up the root directory. The former is particularly interesting when it comes to WOT services since if an attacker can control the filename on a website, they could potentially claim ownership of the domain. One such case happened with liberapay.com and Keybase. Liberapay, an open-source donation platform, did not restrict username’s containing dots in them; therefore one could create usernames containing file extensions. This became apparent to me when I set up a profile page for the security.txt project (<https://liberapay.com/security.txt>). I created a user called `keybase.txt` and embedded the Keybase verification snippet in the profile’s description. This allowed me to claim ownership of liberapay.com. Keybase did not verify the content type of the keybase.txt file and did not even ensure that the token is not embedded into a page.

![](https://user-images.githubusercontent.com/18099289/35120564-d26274aa-fc98-11e7-884f-b972fdc44efe.png)Claiming ownership of liberapay.com by creating a user called keybase.txt and embedding the verification snippet into the profile's description.

## Attack Vector Three – Redirects

After claiming ownership of liberapay`.com` I noticed that liberapay`.org` redirects to liberapay`.com`. This next attack consisted of using a verification token generated for liberapay`.org` embedded on liberapay`.com` to claim ownership of liberapay`.org`. Keybase’s scraper would blindly follow the redirect and not validate the final endpoint to make sure it matches the target host. Keybase would request liberapay`.org/keybase.txt` which redirects to liberapay`.com/keybase.txt` where a valid `keybase.txt` file is located.

![](https://user-images.githubusercontent.com/18099289/36167048-659b30b0-10ec-11e8-8dbb-14b97337020a.png)Claiming ownership of liberapay.org via liberapay.com's keybase.txt file.

One particular plausible attack scenario that I could come up with was claiming branded URL-shorteners using this technique.

## Conclusion

All services affected by these attack vectors were notified and promptly resolved most of the reported issues. Keybase remain vulnerable to attack vectors 2 and 3 – as far as I can tell they do not plan on resolving those issues. I was thoroughly impressed by the response times of all the affected parties and I look forward to working with them again in the future. As a result of this research, I have become addicted to finding logic flaws.

* * *

Update (Friday, 16 February 2018): [@LewisBugBounty](https://twitter.com/LewisBugBounty) demonstrated that one can claim ownership of URL shorteners as I theorised above: [Tweet](https://twitter.com/LewisBugBounty/status/964561238956101632).

[![@LewisBugBounty’s
tweet](https://user-images.githubusercontent.com/18099289/36322389-fb99e1c4-1344-11e8-809f-aa4668017271.png)](https://twitter.com/LewisBugBounty/status/964561238956101632)

[bug bounty](https://edoverflow.com/tags/bug-bounty) [security](https://edoverflow.com/tags/security) [logic flaws](https://edoverflow.com/tags/logic-flaws) [Buy me a coffee ☕](https://www.buymeacoffee.com/edoverflow)[←Automating your reconnaissance workflow with 'meg'](https://edoverflow.com/2018/meg/) [The math behind bug bounties — A formula to calculate bounty amounts→](https://edoverflow.com/2017/the-math-behind-bug-bounties/)

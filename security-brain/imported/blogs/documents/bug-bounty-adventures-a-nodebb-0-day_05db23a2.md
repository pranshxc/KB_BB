---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-25_bug-bounty-adventures-a-nodebb-0-day.md
original_filename: 2022-03-25_bug-bounty-adventures-a-nodebb-0-day.md
title: 'Bug Bounty Adventures: A NodeBB 0-day'
category: documents
detected_topics:
- sso
- oauth
- saml
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- oauth
- saml
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: 05db23a2cd6eebf97f680d7289d5898dda9579e0356e3ac249d0a9a883ee393f
text_sha256: a80a24cb07009b8d6acad9f37e80143c0d781b0faba14a948b72ecf6734a842d
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty Adventures: A NodeBB 0-day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-25_bug-bounty-adventures-a-nodebb-0-day.md
- Source Type: markdown
- Detected Topics: sso, oauth, saml, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `05db23a2cd6eebf97f680d7289d5898dda9579e0356e3ac249d0a9a883ee393f`
- Text SHA256: `a80a24cb07009b8d6acad9f37e80143c0d781b0faba14a948b72ecf6734a842d`


## Content

---
title: "Bug Bounty Adventures: A NodeBB 0-day"
page_title: "Bug Bounty Adventures: A NodeBB 0-day | Opera Security"
url: "https://blogs.opera.com/security/2022/03/bug-bounty-adventures-a-nodebb-0-day/"
final_url: "https://blogs.opera.com/security/2022/03/bug-bounty-adventures-a-nodebb-0-day/"
authors: ["Marouane Mouhtadi (@Mar0_0uane)"]
programs: ["Opera"]
bugs: ["CSRF", "Account takeover", "SSO", "Broken authentication"]
publication_date: "2022-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2783
---

[Research](https://blogs.opera.com/security/category/research/)

# Bug Bounty Adventures: A NodeBB 0-day

Share

  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_facebook.da73949178f1431aa6845a440149477e.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2022%2F03%2Fbug-bounty-adventures-a-nodebb-0-day%2F)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_twitter.2d56c3ce28cf4b8b0c903daaa279cdec.svg)](https://twitter.com/intent/tweet?text=Bug%20Bounty%20Adventures:%20A%20NodeBB%200-day&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2022%2F03%2Fbug-bounty-adventures-a-nodebb-0-day%2F&via=wpvkp)
  * [![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_linkedin.6432d0e754bc197e2aeb64c38fcf2e23.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fblogs.opera.com%2Fsecurity%2F2022%2F03%2Fbug-bounty-adventures-a-nodebb-0-day%2F&title=Bug%20Bounty%20Adventures:%20A%20NodeBB%200-day)
  * ![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/share-article_copy-link.c83a9d420f922d3fde784398f6d5b79c.png)

![](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/img-placeholder.e3550a73cbe5432de9d7de613fbf1e1a.jpg)

March 25th, 2022

_Opera maintains both a[public bug bounty program](https://bugcrowd.com/opera), and a [private program](https://security.opera.com/bug-bounty/), where security researchers can submit security issues they have found in Opera’s products for cash rewards. We like to highlight some of the issues that have been submitted, to educate the community about the types of issues they should be on the look-out for. In this post, we outline a vulnerability that was submitted to us concerning a third-party-developed software – [NodeBB](https://nodebb.org/) – _which turned out to be a 0-day vulnerability.

In May 2021, we received a bug bounty submission from researcher [Mar0uane](https://twitter.com/Mar0_0uane), about a vulnerability in one of the forums we maintain, relating to an account-takeover vulnerability affecting the software’s single-sign-on module.

In the report, Mar0uane outlined that it was possible to create a single-sign-on authorization code for his own user, then trick a different user into associating their account with that auth-code, via a Cross-Site Request (a CSRF). The following instructions to reproduce the issue were given:

  1. Create two accounts; A (Attacker) and B (Victim).
  2. Sign into the attacker account, and begin the process of enabling Google SSO.
  3. Intercept the request, and retrieve the URI similar to: _https://forums.opera.com/auth/google/callback?code=XXXX_
  4. In a new browser, logged in with the victim account, navigate to the intercepted URI.

After step #4, the victim’s account is associated with the SSO account from the attacker’s account – with no user interaction needed. This also means that a foreign website can embed a frame to this URI, resulting in a logged-in user (such as an administrator) unsuspectingly being compromised, without their knowledge.

This type of vulnerability is not new, nor overly complicated. OWASP outlines this [type of issue](https://cheatsheetseries.owasp.org/cheatsheets/SAML_Security_Cheat_Sheet.html#unsolicited-response-ie-idp-initiated-sso-considerations-for-service-providers), which should be standard for many pentesters. However, what is somewhat interesting about this specific vulnerability, is that NodeBB is forum software used by thousands of users around the world. For many companies – and individuals – performing such basic tests against software may be seen as a waste of time, due to the assumption that _somebody_ , _somewhere_ , will have already tested for this sort of vulnerability.

According to NodeBB’s developer, this report was not the first they had heard about this issue. In June of 2018, it was reported via their [bug bounty program](https://nodebb.org/bounty/). However, the same issue was accidentally re-introduced when that part of the code was refactored in early 2021. Effectively, Mar0uane had reported a 0-day that to us that had been un-fixed just five months earlier – showing the power of the bug bounty system both via the original report in June of 2018, and in May 2021.

In the end the vulnerability was fixed. While we normally don’t pay-out for issues found in third-party code, an exception was made in this case, and both us and NodeBB, rewarded the reporter with some cash. Ultimately, this shows that when pentesting a website, it’s worth testing your assumptions.

[ ![](https://secure.gravatar.com/avatar/1bc5da9caf0d55cabcd2a1b02829c7e38d344f0eb5a29824736d5da7a2f71adb?s=120&d=mm&r=g) Opera Team ](https://blogs.opera.com/security/author/operateam/)

[bug bounty](https://blogs.opera.com/security/tag/bug-bounty/)

* * *

### User comments

![You deserve a</br>better browser](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/image-sidebar.829f600e58c0e4206501da0863c92aa1.png)

### You deserve abetter browser

Faster, safer and smarter than default browsers. Fully-featured for privacy, security, and so much more.

[ Download now ](https://www.opera.com/download)

* * *

[![How does Opera make money? An explainer on monetization](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/06/How-does-Opera-make-money-monetization-explainer.png)](https://blogs.opera.com/security/2026/06/how-does-opera-make-money-monetization-explainer/)

[Privacy](https://blogs.opera.com/security/category/privacy/)

##  [How does Opera make money? An explainer on monetization](https://blogs.opera.com/security/2026/06/how-does-opera-make-money-monetization-explainer/ "Permanent Link to How does Opera make money? An explainer on monetization")

June 22nd, 2026

[![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2023/06/Opera-Security-Updates-Green.png)](https://blogs.opera.com/security/2026/06/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-11645/)

[News, ](https://blogs.opera.com/security/category/news/)[Security](https://blogs.opera.com/security/category/security/)

##  [Update your browser: Security fix for Chrome zero-day CVE-2026-11645](https://blogs.opera.com/security/2026/06/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-11645/ "Permanent Link to Update your browser: Security fix for Chrome zero-day CVE-2026-11645")

June 11th, 2026

[![Is Opera's VPN safe?](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2024/09/opera-free-vpn-no-log-audit-wide.jpg)](https://blogs.opera.com/security/2026/05/opera-vpn-is-safe/)

[Security](https://blogs.opera.com/security/category/security/)

##  [Why browsing with Opera’s VPN is safer](https://blogs.opera.com/security/2026/05/opera-vpn-is-safe/ "Permanent Link to Why browsing with Opera’s VPN is safer")

May 29th, 2026

[![Inside the role of Opera's Head of Security](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/05/Opera-Head-of-Security.png)](https://blogs.opera.com/security/2026/05/meet-opera-head-of-security/)

[Security](https://blogs.opera.com/security/category/security/)

##  [How we keep Opera users and products safe: Inside the role of Head of Security](https://blogs.opera.com/security/2026/05/meet-opera-head-of-security/ "Permanent Link to How we keep Opera users and products safe: Inside the role of Head of Security")

May 8th, 2026

[![Opera Security team helps make the web safer through responsible disclosure](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2026/04/Opera-Security-responsible-disclosure.png)](https://blogs.opera.com/security/2026/04/opera-security-responsible-disclosure-osslsigncode-quill/)

[Security](https://blogs.opera.com/security/category/security/)

##  [How Opera’s Security team helps make the web safer through responsible disclosure](https://blogs.opera.com/security/2026/04/opera-security-responsible-disclosure-osslsigncode-quill/ "Permanent Link to How Opera’s Security team helps make the web safer through responsible disclosure")

April 17th, 2026

[![](https://www-static-blogs.operacdn.com/security/wp-content/uploads/sites/6/2023/06/Opera-Security-Updates-Green.png)](https://blogs.opera.com/security/2026/04/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-5281/)

[News, ](https://blogs.opera.com/security/category/news/)[Security](https://blogs.opera.com/security/category/security/)

##  [Update your browser: Security fix for Chrome zero-day CVE-2026-5281](https://blogs.opera.com/security/2026/04/update-your-browser-security-fix-for-chrome-zero-day-cve-2026-5281/ "Permanent Link to Update your browser: Security fix for Chrome zero-day CVE-2026-5281")

April 4th, 2026

![control](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/arrow-left.171ab59fa709a3915488a44fbe586dba.svg) ![control](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/arrow-right.22d48607ea14d7ce2603010ffc20d31d.svg)

* * *

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Sign up for our Newsletter and get the latest news from Opera

Join the mailing list for regular updates on AI and Opera

Your name

Your email

I agree to receive regular updates about Opera via electronic means (including email).

Sign up 

*Required fields

[Please check our Privacy Policy to see how we process data.](https://legal.opera.com/privacy/)

[ ![Opera](https://www-static-blogs.operacdn.com/security/wp-content/themes/opera-2022/static/img/logo.e807fcd39b532b698412c37cd8017781.png) ](https://www.opera.com/)

# You deserve a better browser

Opera's free VPN, Ad blocker, and Flow file sharing. Just a few of the must-have features built into Opera for faster, smoother and distraction-free browsing designed to improve your online experience.

[ Download now ](https://www.opera.com/download)

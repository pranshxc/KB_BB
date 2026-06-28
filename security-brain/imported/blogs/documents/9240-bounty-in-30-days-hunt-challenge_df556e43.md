---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-21_9240-bounty-in-30-days-hunt-challenge.md
original_filename: 2023-10-21_9240-bounty-in-30-days-hunt-challenge.md
title: $9240 Bounty in 30 days Hunt Challenge
category: documents
detected_topics:
- access-control
- xss
- mfa
- command-injection
- business-logic
- oauth
tags:
- imported
- documents
- access-control
- xss
- mfa
- command-injection
- business-logic
- oauth
language: en
raw_sha256: df556e43367926c40c74dc5f3a7cc9fbb0c22786d6283b8a75e42f56fffd3f0d
text_sha256: 949ab989b9f7683dd6d99983ea87f6ddf1302afbc78e6c5fa54a173cfbcff483
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# $9240 Bounty in 30 days Hunt Challenge

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-21_9240-bounty-in-30-days-hunt-challenge.md
- Source Type: markdown
- Detected Topics: access-control, xss, mfa, command-injection, business-logic, oauth
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `df556e43367926c40c74dc5f3a7cc9fbb0c22786d6283b8a75e42f56fffd3f0d`
- Text SHA256: `949ab989b9f7683dd6d99983ea87f6ddf1302afbc78e6c5fa54a173cfbcff483`


## Content

---
title: "$9240 Bounty in 30 days Hunt Challenge"
page_title: "$9240 Bounty in 30 days Hunt Challenge — Voorivex Team"
url: "https://blog.voorivex.team/9240-bounty-in-30-days-hunt-challenge"
final_url: "https://blog.voorivex.team/9240-bounty-in-30-days-hunt-challenge"
authors: ["0xrz (@omidxrz)"]
bugs: ["Information disclosure", "Reflected XSS", "Account takeover", "CORS misconfiguration", "Web cache deception", "Logic flaw", "CSV injection", "HTML injection", "Client-side enforcement of server-side security", "2FA / MFA bypass", "Broken Access Control", "Privilege escalation", "Pre-account takeover"]
bounty: "9,240"
publication_date: "2023-10-21"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 705
---

[All posts](/)

Bug Bounty · 21 Oct 2023 · $9,240 bounty

# $9240 Bounty in 30 days Hunt Challenge

Hello, I'm Omid, a 22-year-old enthusiast diving into the world of web application hacking for nearly a year and a half now. I'm currently hunting for the Voorivex team. Today, I'm sharing my journey as a full-time bug-bounty hunter over the past three months — disappointments, a mid-stride mindset reset, and a 30-day program-focused challenge that ended at $9,240. 

![](assets/avatars/omid-rezaei.png)

Written by [Omid Rezaei](/authors/omid-rezaei)

You can read my first write-up about command injection here: [Uncovering a Command Injection, $2400 Bounty](/uncovering-a-command-injection-2400-bounty). 

## Methodology

Year one was wide recon — DNS bruteforce, Nuclei runs, infrastructure mapping. Around $6k earned and a solid grasp of the wide-recon mindset. Year two: switching to narrow recon — targets with limited scope (`*.target.com` or just `target.com`), Burp + the application, deeply analysed auth and payment flows. 

## July, August

The tally after two months of part-time narrow-recon hunting across multiple targets:

![2-month report tally — 6 triaged, 8 duplicate, 4 informative, 7 N/A, $350 in bounties](assets/images/9240-bounty-in-30-days-hunt-challenge/01-2-months.png)

  * Triaged: 6 · Duplicate: 8 · Informative: 4 · N/A: 7 · All: 25 · Bounty: $350

A few of the more interesting findings from that stretch:

### PII Leakage

Sign-up flow. If the email already existed, the response leaked the user's PII.

![Sign-up response leaks PII when email already exists](assets/images/9240-bounty-in-30-days-hunt-challenge/02-pii-leakage.png)

### PII Leakage 2

The collaboration "suggest" endpoint returned not just name + email but addresses and phone numbers too: 

![Collaborator suggestion endpoint leaking address + phone](assets/images/9240-bounty-in-30-days-hunt-challenge/03-pii-leakage-2.png)

### Reflected XSS

On `admin.target.com`'s sign-up page, fuzzing JS variable names surfaced an `appURL` parameter reflected inside a script tag. `</script><script>alert(origin)</script>` popped: 

![appURL parameter reflected inside a script tag](assets/images/9240-bounty-in-30-days-hunt-challenge/04-reflected-xss.png)

### Reflected XSS → Admin ATO

Same XSS, weaponised into an authenticated request flow against `admin.target.com`:

![XSS-to-admin-ATO chain](assets/images/9240-bounty-in-30-days-hunt-challenge/05-xss-to-ato.png)

The program later marked three of these N/A claiming the asset wasn't theirs and went silent on the remaining triaged ones. After three months without payout I left BugCrowd, moved to HackerOne, and immediately ran into a wall of duplicates and N/A. 

## Self-Assessment & Debugging the Mindset

Two months of effort with nothing to show. Mental fatigue. I took a few days off, opened the laptop again, and instead of touching a target I started asking myself questions: 

  * Do I know enough for bug hunting?
  * Can the platform affect my success? If yes, why hasn't HackerOne fixed it?
  * Am I doing okay, or just unlucky?

I went hunting for answers. A few resources that helped:

  * Grzegorz Niedziela's [YouTube playlist](https://www.youtube.com/watch?v=mJI958rULdw&list=PLvxs_epf2X91YIlr3ze6gO3Zn_JhW38fG) on the pentest → bug bounty transition.
  * A tweet from [Hazem](https://x.com/H4cktus) showing his August results from a single program:

![Hazem's tweet — single-program focus paying off](assets/images/9240-bounty-in-30-days-hunt-challenge/06-hazem-tweet.png)

  * A direct message to Justin Gardner. He replied:

![Justin Gardner's reply on burnout and mindset](assets/images/9240-bounty-in-30-days-hunt-challenge/07-justin-reply.png)

  * And a chat with [Mohammad Zaheri](https://x.com/mzaherii) on goal-setting and avoiding burnout.

The takeaway:

  * Focus on a single program.
  * Set a clear goal.
  * Begin a specific challenge.
  * My knowledge might not be perfect, but it's sufficient to find things based on previous findings.
  * Sometimes it's just luck — but you can stack the odds.

## September

I picked one program based on bounty + response-time tables and started a 30-day challenge:

![Chosen program's bounty table and response-time stats](assets/images/9240-bounty-in-30-days-hunt-challenge/08-program-chosen.png)

Result of the 30-day challenge:

![30-day challenge tally — 9 triaged, 3 duplicate, 1 informative, 1 N/A, $9,240](assets/images/9240-bounty-in-30-days-hunt-challenge/09-30day-result.png)

  * Triaged: 9 · Duplicate: 3 · Informative: 1 · N/A: 1 · All: 14 · Bounty: $9,240

Quick sketch of each find:

  1. **CORS Misconfiguration.** Hosting let me register an arbitrary subdomain; an API on `api.target.com` trusted `*.arbitrary.targetsite.com` for CORS. Denied — Lax cookies + Firefox protection. 
  2. **Cache Deception.** `https://dashboard.target.com/my-profile/username/.css` was cached. 
  3. **Business Logic Error.** On `payment.target.com` the "domain already registered" check ran on the response side; manipulating the response let me invoice an already-taken domain. 
  4. **CSV Injection.** Contact-form messages exported by the admin as CSV; `=4+4` rendered as `8`. 
  5. **HTML Injection in Email.** Same contact form — sender name rendered as HTML in the admin's notification email. 
  6. **Weak Password-Protect Function.** The page builder offered password-protection that ran client-side; the data stayed reachable in the DOM. Reported as High; the program initially downgraded it, then accepted my argument: 

![Program's initial low-severity message](assets/images/9240-bounty-in-30-days-hunt-challenge/10-program-msg.png)

![My response arguing for higher severity](assets/images/9240-bounty-in-30-days-hunt-challenge/11-my-response.png)

![Program accepting the higher-severity classification](assets/images/9240-bounty-in-30-days-hunt-challenge/12-they-accepted.png)

  7. **Access to Unpublished Posts.** Direct request to a private post URL loaded the content; addresses were guessable. 
  8. **2FA Bypass via Authenticated Cookie.** The login flow ran through an anonymous → upgraded session converted to a JWT at a "converter" page. With 2FA the upgrade goes through `/login/key/<random>`. Swapping the 2FA-enabled victim's session ID for an attacker's converted anonymous session and refreshing produced a JWT for the victim. 
  9. **Pre-Account Takeover.** Sign-up didn't require email verification. Pre-creating an account for `[[email protected]](/cdn-cgi/l/email-protection)` let me wait until the victim signed up via Google OAuth — the previously-saved token then gave access. 
  10. **Reflected XSS → ATO.** Re-using parameters from `/login/key/<random>` on the previous page produced a tag break and a reflected XSS. Exploit code grabbed the JWT. 
  11. **ATO via Grant Access.** The "request access" feature emitted an auth token to the granting attacker that survived the victim revoking access. 
  12. **2FA Bypass via Grant Access.** Adding a dot to the email (`[[email protected]](/cdn-cgi/l/email-protection)`) made the backend treat it as a new user — the link bypassed the 2FA-prompt flow entirely. Exploitation needs the victim's mailbox, but it bypasses Google Authenticator on already-authed accounts. 

## Conclusion

Three months of bug bounty taught me it isn't just technical knowledge — mindset and the right kind of community matter just as much. Pick a program, set a goal, debug the mindset when output stalls, and ask people who've been there.

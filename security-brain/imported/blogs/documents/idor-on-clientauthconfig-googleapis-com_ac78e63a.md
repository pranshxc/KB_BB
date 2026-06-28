---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-08_idor-on-clientauthconfiggoogleapiscom.md
original_filename: 2021-07-08_idor-on-clientauthconfiggoogleapiscom.md
title: IDOR on clientauthconfig.googleapis.com
category: documents
detected_topics:
- access-control
- api-security
- oauth
- sso
- idor
- command-injection
tags:
- imported
- documents
- access-control
- api-security
- oauth
- sso
- idor
- command-injection
language: en
raw_sha256: ac78e63aad224df5c1c893fda791efd41b19d61e70955dc0ab9f4f77d9444dbf
text_sha256: 30a24b991b0db5d70c95e0a06d290716181c7925cfda1d27ad9695ed9118ba61
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# IDOR on clientauthconfig.googleapis.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-08_idor-on-clientauthconfiggoogleapiscom.md
- Source Type: markdown
- Detected Topics: access-control, api-security, oauth, sso, idor, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `ac78e63aad224df5c1c893fda791efd41b19d61e70955dc0ab9f4f77d9444dbf`
- Text SHA256: `30a24b991b0db5d70c95e0a06d290716181c7925cfda1d27ad9695ed9118ba61`


## Content

---
title: "IDOR on clientauthconfig.googleapis.com"
page_title: "[#0009] IDOR in Google Identity platform allows leaking limited OAuth client data | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0009"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0009"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2021-07-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3522
---

#0009  
Vendor: Google  
Status: wont-fix  
Reported: Apr 09, 2021  
Disclosed: Jul 08, 2021 (90 days) 

# IDOR in Google Identity platform allows leaking limited OAuth client data

**Summary:**

Using the `/v1/brands/lookupkey/brand/[brand_id]` endpoint on the `clientauthconfig.googleapis.com` API, its possible to request information about any brand, without any authentication.

Since the `brand_id` is normally the same as the `project_number`, only the `project_number` is needed to exploit this vulnerability. The `project_number` can leak from an API key when sending a request with the key to an API that’s not enabled on the key’s project.

The endpoint even returns `brand`s that are Google Workspace internal. (`"isOrgInternal": true`)

Normally, even if you have the `client_id`, trying to start an OAuth flow on a Workspace internal `brand` as an outsider only returns a `Error 403: org_internal This client is restricted to users within its organization.` error, and doesn’t leak any information about the `brand`’s name, or other details. So those details are clearly considered private, but this endpoint leaks them.

**Core Issue:**

There is no access control on the `/v1/brands/lookupkey/brand/[brand_id]` endpoint.  
It should require `read` permissions on the `brand`’s project. This is even stated in the API’s Discovery Document:
  
  
  Retrieve branding info given a brand_id.
  Requires read permission on the associated project.
  

**Steps to reproduce:**

  1. Create a GCP project, and note the project’s `project_number`
  2. Go to `https://console.cloud.google.com/apis/credentials/consent` and set up a consent screen (`brand`)
  3. Send this unauthenticated `GET` request (the API key is from Cloud Console):

  
  
  GET /v1/brands/lookupkey/brand/[project_number]?readMask=*&%24outputDefaults=true HTTP/1.1
  Host: clientauthconfig.googleapis.com
  Origin: https://console.cloud.google.com
  X-Goog-Api-Key=***REDACTED***
  
  
  

  4. See the `brand` object returned in the response

**Attack scenario:**

Any unauthenticated attacker who knows the target project’s `project_number`. As I stated above, the project_number can leak from a publicly exposed API key when sending a request with the key to an API that’s not enabled on the key’s project.

* * *

### Comments:

**Vendor - 2021-04-09 19:06**

_NOTE: This e-mail has been generated automatically._

Thanks for your report.

This email confirms we’ve received your message. We’ll investigate and get back to you once we’ve got an update. In the meantime, you might want to take a look at the [list of frequently asked questions about Google VRP](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq).

If you are reporting a security vulnerability and wish to appear in Google Security Hall of Fame, please [create a profile](https://bughunter.withgoogle.com/new_profile).

You appear automatically in our Honorable Mentions if we decide to file a security vulnerability based on your report, and you will also show up in our Hall of Fame if we issue a reward.

**Note that if you did not report a vulnerability, or a technical security problem in one of our products, we won’t be able to act on your report. This channel is not the right one if you wish to resolve a problem with your account, report non-security bugs, or suggest a new feature in our product.**

Cheers,  
Google Security Bot

[Follow us](https://twitter.com/googlevrp) on Twitter!

* * *

**Vendor - 2021-04-12 09:16**

_NOTE: This e-mail has been generated automatically._

Hey,

Just letting you know that your report was **triaged** and we’re currently looking into it.

You should receive a response in a couple of days, but it might take up to a week if we’re particularly busy. In the meantime, you might want to take a look at [the list of frequently asked questions about Google VRP](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq).

Thanks,  
Google Security Bot

* * *

**Vendor - 2021-04-13 16:53**

Hi,

🎉 **Nice catch!** I’ve filed a bug based on your report.

The panel will evaluate it at the next VRP panel meeting and we’ll update you once we’ve got more information. All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Security Team

* * *

**Vendor - 2021-04-22 21:20**

** NOTE: This is an automatically generated email **

Hello,

We have notified the team about this issue; they will review your report and decide whether they want to make a change or not. Thanks for letting us know.

Regarding our Vulnerability Reward Program, the panel decided this issue’s security impact does not meet the criteria to qualify for a reward in the program, so we won’t be issuing a reward at this time.

Regards, Google Security Bot

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Vendor - 2021-06-10 23:44**

_NOTE: This is an automatically generated email_

Hello,

Our systems show that the bug we created based on your report **has been closed without providing a fix**.

This may have happened for various reasons: the risk impact might be too small to warrant a fix, there might be other mitigating factors, or simply the product is not maintained anymore.

The exact status is **INTENDED_BEHAVIOR**. This decision has been made by the relevant product teams and does not affect your VRP reward amount or Hall of Fame position.

We can’t provide more details in this automated notification, but we’ll be happy to answer your questions regarding this decision.

Thanks,  
Google Security Bot

* * *

**Me - 2021-06-18 17:17**

Hi,

Just a heads up, this report will be disclosed in 20 days, on `2021-07-08`.

Is this really intended behaviour? I think the documentation states somewhere that org internal clients are not visible to anyone outside the org. Trying to log in to an org internal client with OAuth also throws an error without providing any information (like name, email address), but this bug leaks those details.

Thank you,  
David

* * *

**Vendor - 2021-06-21 22:14**

Hi,

The product team thinks that this information is public. The info is also available through other sources. If someone can construct the authorization URL using the client-id and redirect URI, they would be able to get part of this data on the consent screen (eg. app name, privacy policy, etc.).

Why do you think that the info should be private? If you can find it, can you give a link to the documentation that mentions that internal clients aren’t visible?

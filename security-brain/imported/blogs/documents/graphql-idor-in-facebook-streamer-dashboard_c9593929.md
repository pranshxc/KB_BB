---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-18_graphql-idor-in-facebook-streamer-dashboard.md
original_filename: 2020-11-18_graphql-idor-in-facebook-streamer-dashboard.md
title: GraphQL IDOR in Facebook streamer dashboard.
category: documents
detected_topics:
- idor
- command-injection
- graphql
tags:
- imported
- documents
- idor
- command-injection
- graphql
language: en
raw_sha256: c95939294607eaa947544d466b50a8a59f59f15a2fa96430760677e33df0c2f5
text_sha256: b899eef08a0b4089724a185747c373ab394cdb93a7ce4a730aa52f4acf152af0
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# GraphQL IDOR in Facebook streamer dashboard.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-18_graphql-idor-in-facebook-streamer-dashboard.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c95939294607eaa947544d466b50a8a59f59f15a2fa96430760677e33df0c2f5`
- Text SHA256: `b899eef08a0b4089724a185747c373ab394cdb93a7ce4a730aa52f4acf152af0`


## Content

---
title: "GraphQL IDOR in Facebook streamer dashboard."
page_title: "GraphQL IDOR in Facebook streamer dashboard. – Kailash"
url: "https://kailashbohara.com.np/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/"
final_url: "https://kailashbohara.com.np/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/"
authors: ["Kailash (@Corrupted_brain)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "GraphQL"]
bounty: "2,000"
publication_date: "2020-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4120
---

# [GraphQL IDOR in Facebook streamer dashboard.](https://corrupted-brain.github.io/blog/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/ "GraphQL IDOR in Facebook streamer dashboard.")

#### Description:

While viewing our stream dashboard data from creator studio, there is an endpoint from where we can see our dashboard status. There is parameter called _profile_id_ in GraphQl request which can be misused to access data of other pages by using facebook page_id.

#### Steps to Reproduce:

  1. Start burpsuite and intercept the request.
  2. Go to https://www.facebook.com/gaming/streamer and you will be redirected to creator studio.
  3. We will forward all the intercepted request since it’s difficult to spot the correct request which has vulnerable parameters in multiple requests.
  4. Meanwhile we will use find feature in burpsuite. we’ll search for _“GamesVideoStreamerDashboardProfileQuery”._ ![graphql-request](/images/posts/graphql-request.png)
  5. Once our search query matches we will forward that particular request to repeator and replace _profileID_ with desired game steaming pageID to see their stream stats. The response of the above request looks like as shown below. ![graphql-response](/images/posts/graphql-response.png) According to facebook only highlighted information i.e. _“l30_live_earnings”_ and _“supporter_count”_ are sensitive which should not be disclosed to a user which does not have any role in the page.

#### Conclusion:

After reviewing this issue, Facebook decided to award a bounty of $2000 and they fixed the issue by not displaying those information in the response to a users which does not have any role in page. ![facebook-reply](/images/posts/facebook-reply.png)

* * *

#### Share on

  * [__Twitter](https://twitter.com/intent/tweet?text=GraphQL IDOR in Facebook streamer dashboard. https://corrupted-brain.github.io/blog/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/ "Share on Twitter")
  * [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://corrupted-brain.github.io/blog/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/ "Share on Facebook")
  * [__Google+](https://plus.google.com/share?url=https://corrupted-brain.github.io/blog/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/ "Share on Google Plus")
  * [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://corrupted-brain.github.io/blog/blog/2020/11/18/GraphQL-IDOR-in-Facebook-streamer-dashboard/&title=GraphQL IDOR in Facebook streamer dashboard.&summary=While viewing our stream dashboard data from creator studio, there is an endpoint from where we can see our dashboard status. There is parameter called profile_id which can be misused to access data of other pages by using facebook page_id.&source=https://corrupted-brain.github.io/blog "Share on LinkedIn")

**GraphQL IDOR in Facebook streamer dashboard.** was published on November 18, 2020.

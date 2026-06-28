---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-24_instagram-github-token-with-public_scope-found-in-travis-ci-build-logs.md
original_filename: 2019-05-24_instagram-github-token-with-public_scope-found-in-travis-ci-build-logs.md
title: Instagram GitHub Token with public_scope found In Travis CI Build Logs
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: df359abf469a8614832e7575e8e50786a20bd4da1da463a58fe8a197cefcb88a
text_sha256: 079030cbacef0edd2f00f0e5b46626b5f68475bb7c961359c9f2b9383deb6eaf
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Instagram GitHub Token with public_scope found In Travis CI Build Logs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-24_instagram-github-token-with-public_scope-found-in-travis-ci-build-logs.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `df359abf469a8614832e7575e8e50786a20bd4da1da463a58fe8a197cefcb88a`
- Text SHA256: `079030cbacef0edd2f00f0e5b46626b5f68475bb7c961359c9f2b9383deb6eaf`


## Content

---
title: "Instagram GitHub Token with public_scope found In Travis CI Build Logs"
page_title: "Instagram GitHub Token with public_scope found In Travis CI Build Logs - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/instagram-github-token-with-public_scope-found-in-travis-ci-build-logs/"
final_url: "https://philippeharewood.com/instagram-github-token-with-public_scope-found-in-travis-ci-build-logs/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2019-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5247
---

Posted on [May 24, 2019](https://philippeharewood.com/instagram-github-token-with-public_scope-found-in-travis-ci-build-logs/)

# Instagram GitHub Token with public_scope found In Travis CI Build Logs

In https://travis-ci.org/Instagram/IGListKit/ lists a Github token with public_scope, since this user is a member of the Instagram organization this might have undesirable effects.

1\. Go to https://travis-ci.org/Instagram/IGListKit/jobs/JOBID

In there, is listed

`export DANGER_GITHUB_API_TOKEN=TOKEN`

2\. Check the scope for the token

`curl -H "Authorization: token TOKEN" https://api.github.com/rate_limit -v`

The response headers should present the following

`X-OAuth-Scopes: public_repo`

3\. Here is a slightly non-destructive call to star a repo,

`curl -X PUT -H "Content-Length:0" -H "Authorization: token TOKEN" https://api.github.com/user/starred/phwd/fbec`

4\. See the result at

https://github.com/iglistkit-bot?tab=stars

I also checked for any private membership after that I haven’t decided to test any other calls for risk of disturbing any workflows. According to https://danger.systems/guides/getting_started.html this seems like the recommended way to list tokens (with public_scope).

“We recommend giving the token the smallest scope possible. This means just public_repo, this scope is still ideally too much but this account shouldn’t have any access to other repos or organizations – so malicious use of the token is scoped to making new repos on it, or writing comments on other OSS projects. Because the token can be quite easily be extracted from the CI environment, this minimizes the chance for bad actors to cause chaos with it.”

Facebook’s response  
  
“This looks to be a deliberate tradeoff. https://github.com/facebook/facebook-instant-articles-sdk-php/pull/272 discusses the reasons why someone might provide a token like that in their repo, namely that they want to ensure that the token is available as part of pull requests (ie: to be able to have a bot that comments on a pull request).” -May 24, 2019  
  
“We are closing out your report. Note that just because this particular bot is broken or not active it doesn’t mean we can’t have other bots that are still active from whom you might be able to obtain a token with the same privileges. In such scenarios our previous explanation applies to these tokens as well.” -May 28, 2019

**Timeline**

May 22, 2019 – Report sent  
May 24, 2019 – Explanation by Facebook  
May 24, 2019 – Clarification sent  
May 28, 2019 – Closed as informative by Facebook

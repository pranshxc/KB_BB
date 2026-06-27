---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '212067'
original_report_id: '212067'
title: An “algobot”-s GitHub access token was leaked
weakness: Information Disclosure
team_handle: algolia
created_at: '2017-03-09T20:27:36.572Z'
disclosed_at: '2017-06-10T14:19:19.645Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# An “algobot”-s GitHub access token was leaked

## Metadata

- HackerOne Report ID: 212067
- Weakness: Information Disclosure
- Program: algolia
- Disclosed At: 2017-06-10T14:19:19.645Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

An access token of [algobot] account was first leaked 2015-12-02 in this [Travis CI job log] of [instantsearch.js] project due to incorrect handling of output from command `git clone` (or a `ghpages` module to be more specific.) Since then, the configuration of that project seems to have been changed not to perform this operation ([last build] with token found is from 2016-01-06), but the [docsearch] project still [uses it] and leaks algobot's token with every build of the master branch, here's for example [the latest one.]

This token has a `public_repo` scope, so it gives commit access to any public repositories its owner has access to. So both instantsearch.js and docsearch are affected.

You may want to verify that there were no suspicious changes since the first leak. Unfortunately I didn't find any way to check the token usage history, so cannot help with that.

Note that I did use this token to get its owner info (GET call to endpoint `https://api.github.com/user`) and repositories that belong to them (GET call to `https://api.github.com/user/repos`), but I didn't attempt to perform any other operations.

Also, please be sure to avoid disclosing this issue accidentally (e.g. in commit messages), as I'm still working with others that have similar leaks. Revoking/rotating tokens without explanation with simple “updating the token” should be fine though, generally nobody pays attention to them.

[algobot]: https://github.com/algobot
[instantsearch.js]: https://github.com/algolia/instantsearch.js
[docsearch]: https://github.com/algolia/docsearch
[uses it]: https://github.com/algolia/docsearch/blob/master/scripts/docs/gh-pages.js#L10
[Travis CI job log]: https://travis-ci.org/algolia/instantsearch.js/jobs/94408476/#L460
[last build]: https://travis-ci.org/algolia/instantsearch.js/jobs/100608422#L462
[the latest one.]: https://travis-ci.org/algolia/docsearch/builds/203760306#L419

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*

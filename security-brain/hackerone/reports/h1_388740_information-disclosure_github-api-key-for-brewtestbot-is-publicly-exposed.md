---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '388740'
original_report_id: '388740'
title: GitHub API Key for BrewTestBot is publicly exposed
weakness: Information Disclosure
team_handle: homebrew
created_at: '2018-07-31T05:47:18.646Z'
disclosed_at: '2018-08-11T13:57:57.996Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
tags:
- hackerone
- information-disclosure
---

# GitHub API Key for BrewTestBot is publicly exposed

## Metadata

- HackerOne Report ID: 388740
- Weakness: Information Disclosure
- Program: homebrew
- Disclosed At: 2018-08-11T13:57:57.996Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello!

While browsing through some old reports, I found that https://jenkins.brew.sh was publicly accessible. I got curious when I saw one of the [brew bottle builds](https://jenkins.brew.sh/job/Homebrew%20Bottles/33255/console) doing a `git push` to BrewTestBot/homebrew-core, and wondered if the credentials to make authenticated pushes were accessible.

Sure enough, you can view environment variables for the build on [this page](https://jenkins.brew.sh/job/Homebrew%20Bottles/33255/injectedEnvVars/), which includes a `HOMEBREW_GITHUB_API_TOKEN` environment variable.

This API token belongs to the [BrewTestBot](https://github.com/BrewTestBot) user on GitHub, and this API key allows me to commit to the `BrewTestBot/homebrew-core` repository:

```
$ export GITHUB_API_TOKEN=<github token from above>
$ curl https://api.github.com/repos/BrewTestBot/homebrew-core/git/blobs -u $GITHUB_API_TOKEN:x-oauth-basic -d '{"content":"test"}' -H "Content-Type: application/json"
{
  "sha": "30d74d258442c7c65512eafab474568dd706c430",
  "url": "https://api.github.com/repos/BrewTestBot/homebrew-core/git/blobs/30d74d258442c7c65512eafab474568dd706c430"
}
```

## Impact

Based on the purpose of `BrewTestBot`, this might be entirely intended, but if the GitHub access token has overly permissive scopes, it might be usable to perform other actions, aside from a `git push`. In that case, an SSH deploy key may be better, and less permissive.

If exposing this API key publicly is intended behavior, please feel free to close this.

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

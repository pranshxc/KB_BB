---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181212'
original_report_id: '181212'
title: Missing GIT tag/commit verification in Docker
team_handle: paragonie
created_at: '2016-11-09T23:19:24.673Z'
disclosed_at: '2016-11-09T23:45:20.349Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
---

# Missing GIT tag/commit verification in Docker

## Metadata

- HackerOne Report ID: 181212
- Weakness: 
- Program: paragonie
- Disclosed At: 2016-11-09T23:45:20.349Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

in:
https://github.com/paragonie/airship/blob/master/docker/Dockerfile.airship#L14-L16
```
RUN git clone https://github.com/jedisct1/libsodium.git /tmp/sodium
WORKDIR /tmp/sodium
RUN git checkout tags/1.0.10
```

The code is fetched from Github without one of:
1\. signature verification on relevant tag. (GPG)
2\. specific commit. (SHA checksum)
more information about this issue:
https://www.qubes-os.org/doc/verifying-signatures/#verifying-qubes-code

fix: (implement 1 and/or 2)

1. verify GPG signature 
	use:
		```
		git tag -v <tag name>
		```
	to ensure the tag is signed.
		
	Note: the tags in:
	https://github.com/jedisct1/libsodium/tags
	are signed, thus it's possible to implement this verification.

2. checkout known commit, such as:
```
git checkout fce6852d64339efa33c0ee4130b3107b888d6067
```
fce6852d64339efa33c0ee4130b3107b888d6067 is commit for tag 1.0.10 https://github.com/jedisct1/libsodium/commit/fce6852d64339efa33c0ee4130b3107b888d6067

Important note: The above operations need to be checked for errors (abort the script/don't proceed if error occurs)

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

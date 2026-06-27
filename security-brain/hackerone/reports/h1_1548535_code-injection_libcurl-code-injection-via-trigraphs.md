---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1548535'
original_report_id: '1548535'
title: --libcurl code injection via trigraphs
weakness: Code Injection
team_handle: curl
created_at: '2022-04-23T02:47:28.668Z'
disclosed_at: '2022-04-24T22:07:12.698Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 6
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- code-injection
---

# --libcurl code injection via trigraphs

## Metadata

- HackerOne Report ID: 1548535
- Weakness: Code Injection
- Program: curl
- Disclosed At: 2022-04-24T22:07:12.698Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:

curl command `--libcurl` option can be tricked to generate C code that when compiled contains arbitrary code execution.

## Steps To Reproduce:
  1. `curl --libcurl client.c --user-agent "??/\");char c[]={'i','d',' ','>','x',0},m[]={'r',0};fclose(popen(c,m));//" http://example.invalid`
  2. `gcc -trigraphs  client.c -lcurl -o client`
  3.  `./client`
  4. `ls -l x`

Note: In this PoC older compiler is simulated by passing `-trigraphs` option to gcc.

To remedy this issue `?` chars should be quoted to `\?` in the generated strings.

## Impact

Code injection to generated source code.

However, the impact of this vulnerability is minimal due to difficultly in finding scenarios where it would be practically exploitable. To be even remotely plausible curl command should somehow be hooked into a system that uses `--libcurl` to generate, compile and finally execute the compiled code *while* also accepting external user input for the curl command options. This seems extremely unlikely to happen in real life.

Trigraph support has also largely been disabled by now (gcc and clang have it disabled by default at least).

I don't really mind if this is found to be "not a vulnerability" (or only self-exploitable). In this case just close this H1 ticket and create a regular GitHub issue / or fix it direct.

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

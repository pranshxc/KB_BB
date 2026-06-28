---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-14_v1-instance-metadata-service-protections-bypass.md
original_filename: 2019-06-14_v1-instance-metadata-service-protections-bypass.md
title: v1 Instance Metadata Service protections bypass
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- cloud-security
- mobile-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- cloud-security
- mobile-security
language: en
raw_sha256: 2c06586ce8c2db00bcfe433018715824cc8764ec5b8eb8f65535f7c65ff17c7e
text_sha256: 644a62e1e98d662acbaa02b12799f53b4fd9116c3a727d0ca929a09cd862c799
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# v1 Instance Metadata Service protections bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-14_v1-instance-metadata-service-protections-bypass.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2c06586ce8c2db00bcfe433018715824cc8764ec5b8eb8f65535f7c65ff17c7e`
- Text SHA256: `644a62e1e98d662acbaa02b12799f53b4fd9116c3a727d0ca929a09cd862c799`


## Content

---
title: "v1 Instance Metadata Service protections bypass"
page_title: "v1 Instance Metadata Service protections bypass | Anthony Weems"
url: "https://lf.lc/vrp/135276622/"
final_url: "https://amlw.dev/vrp/135276622/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["SSRF"]
bounty: "5,000"
publication_date: "2019-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5217
---

#  v1 Instance Metadata Service protections bypass 

June 14, 2019

### Vulnerability Details#

The Instance Metadata Service has two mitigations to help protect applications that are vulnerable to SSRF. Namely, the `Metadata-Flavor: Google` header is required and requests with the `X-Forwarded-For` header are ignored. The three examples below describe methods for bypassing the first protection, which could expose customers to risk in specific scenarios.

Use any of the following commands to demonstrate issues with the metadata service protections:

  1. Bypass the `Metadata-Flavor: Google` requirement by including an extra ‘/’ in the URL:

  
  
  curl 'http://169.254.169.254/computeMetadata//v1/instance/name'
  

  2. Bypass the `Metadata-Flavor: Google` requirement by sending an HTTP/1.0 request, which (strangely) dumps all metadata content:

  
  
  printf "GET / HTTP/1.0\r\n\r\n" | nc 169.254.169.254 80
  

  3. In some scenarios, an attacker may not fully control a URL. They can use `;` in a URL to ignore all content following the semi-colon:

  
  
  curl -H 'Metadata-Flavor: Google' 'http://169.254.169.254/computeMetadata/v1/instance/name;extra/content'
  

### Attack Scenario#

_Actor: An attacker exploiting an SSRF vulnerability in an application running in GCP_

_Target: Service account credentials from metadata service_

_Outcome: Compromise of those credentials when the metadata service would normally protect them_

During a recent penetration test for a client using GCP, we discovered a specific SSRF vulnerability in that client’s application that allowed requests to an arbitrary host with a partially controlled URL (e.g. `http://xxx:xx/xxx/yyy`, where `x` is attacker-controlled and `y` is hardcoded). The URL `http://169.254.169.254/computeMetadata//v1/instance/name;yyy` allowed bypassing both the `Metadata-Flavor` requirement and, specific to our client’s vuln, the hardcoded data at the end of the URL. This was due to the way the Metadata Service handled both `//` and `;` sequences in URLs (as shown in #1 and #3 above).

During my research, I haven’t found a scenario where #2 would come up in practice, but it is another example of bypassing the `Metadata-Flavor` requirement.

### Timeline#

  * 2019-06-14: Issue reported to Google VRP
  * 2019-06-17: Issue triaged
  * 2019-06-19: Internal bug report filed
  * 2019-07-22: Issue fixed
  * 2019-07-23: VRP issued reward ($5000)

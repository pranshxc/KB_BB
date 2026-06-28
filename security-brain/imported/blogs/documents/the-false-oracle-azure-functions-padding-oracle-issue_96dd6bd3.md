---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-28_the-false-oracle-azure-functions-padding-oracle-issue.md
original_filename: 2021-04-28_the-false-oracle-azure-functions-padding-oracle-issue.md
title: The False Oracle — Azure Functions Padding Oracle Issue
category: documents
detected_topics:
- command-injection
- information-disclosure
- cloud-security
- access-control
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- information-disclosure
- cloud-security
- access-control
- otp
- automation-abuse
language: en
raw_sha256: 96dd6bd34ee89c0fe66a4ceee294dcb5d6e0e7c7a1761a37b86ace0049697267
text_sha256: b107576f9b0524161e1271f82bd07a7ebf7a07f13ce96ee5f04922dd49fb70f0
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# The False Oracle — Azure Functions Padding Oracle Issue

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-28_the-false-oracle-azure-functions-padding-oracle-issue.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, cloud-security, access-control, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `96dd6bd34ee89c0fe66a4ceee294dcb5d6e0e7c7a1761a37b86ace0049697267`
- Text SHA256: `b107576f9b0524161e1271f82bd07a7ebf7a07f13ce96ee5f04922dd49fb70f0`


## Content

---
title: "The False Oracle — Azure Functions Padding Oracle Issue"
url: "https://polarply.medium.com/the-false-oracle-azure-functions-padding-oracle-issue-2025e0e6b8a"
authors: ["polarply (@polarply)"]
programs: ["Microsoft"]
bugs: ["Padding oracle attack", "Privilege escalation"]
publication_date: "2021-04-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3697
scraped_via: "browseros"
---

# The False Oracle — Azure Functions Padding Oracle Issue

The False Oracle — Azure Functions Padding Oracle Issue
polarply
Follow
6 min read
·
Apr 28, 2021

56

1

Introduction

In this blog I present two vulnerabilities I found in the Azure Functions and another very interesting case of a padding oracle, available as an undocumented HTTP endpoint on every Function instance. Initially I was ecstatic about this finding as theoretically it would have allowed me to achieve remote code execution over arbitrary Azure Functions. However, in a twist of irony, an implementation bug in Microsoft’s Cryptography codebase made this oracle dysfunctional (a false oracle!) and I could not achieve RCE.

The first vulnerability allowed an attacker with code execution over a Function to escalate privileges by installing a permanent backdoor on the Function. The second bug allowed downloading encrypted Function configurations that did not belong to me. Chaining this bug with a padding oracle would’ve allowed me to decrypt configurations of other users and result in RCE however we shall see why this was not the case.

Both vulnerabilities were reported to MSRC and are now fixed, and the padding oracle issue was brought to Microsoft’s attention however as it wasn’t functioning they saw no need to fix it.

Overview

On my previous Function Docker Escape post published in Intezer’s website, I described how I set up Azure Function so I could investigate its environment. In a nutshell, I hosted a reverse shell over the Function environment. After publishing that research, I continued exploring the Function environment and I noticed interesting environment variables such as CONTAINER_START_CONTEXT_SAS_URI which linked to a file in the azcontainers blob storage belonging to wawstorageproddm1157 — a storage account belonging to Microsoft.

Press enter or click to view image in full size

There are two interesting things here:

An attacker with code execution on an Azure Function is able to escalate privileges using the SCM_RUN_FROM_PACKAGE environment variable. This URL redirected to the Azure Function package but its SAS token had a ‘write’ permission (marked in blue), meaning it can be used to overwrite the Azure Function package. This meant an would have been able to overwrite the Function code package with their own code (Escalation of Privileges). If done thoughtfully, the user would not have noticed this change and the attacker would have been able to plant a backdoor which would have run in every Function invocation. This is the first vulnerability.
The Azure Function had access to a storage blob belonging to ‘wasstorageproddm1157’ storage account, which belongs to Microsoft (marked in red).

Accessing this URL showed:

Press enter or click to view image in full size

This was an encrypted version of the configuration file used to initialize the Azure Function.

The CONTAINER_ENCRYPTION_KEY environment variable was used to decrypt this blob (using AES-256):

Press enter or click to view image in full size

The configuration held many interesting keys, such as SCM_RUN_FROM_PACKAGE that we saw earlier. Furthermore, the configuration file also contained Secrets related to the Function managed identity, allowing to spoof the Function identity outside of that Function.

I extracted the SAS token from the URL and using the Azure CLI, tried to query the azcontainers blob storage. To my surprise, I was able to list Azure Function’s configurations not belonging to me:

Press enter or click to view image in full size

Querying azcontainers, each “name” field is a different configuration file

The token also enabled me to download these configurations, however they were no use to us in their encrypted form so this had no practical impact.

However, recall that in the Azure Function Docker Escape blog, while reversing the Init Mesh binary we noticed the Mesh HTTP server was quite verbose. Interacting with this server required to pass an encrypted authentication token under the “x-ms-site-restricted-token” header, and would return a verbose error message when dealing with an invalid token. Specifically, it alerted if the token was malformed — specifically if it had incorrect padding. This behaviour is called a padding oracle, and with this single piece of information an attacker is able to completely decrypt passed encrypted messages.

Get polarply’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Furthermore, we found this HTTP server was accessible from outside the Function via a public endpoint:

Press enter or click to view image in full size
Azure Padding Oracle

If you are unfamiliar with Padding Oracle attacks, I suggest going over this video, as it is too bit a lengthy subject for this blog post. However, in a nutshell, a padding oracle enables an attacker to decrypt any encrypted message passed to it provided it was encrypted with the matching key in the oracle server.

Further reversing the Init Mesh binary showed the authentication code tried to decrypt this header using the CONTAINER_ENCRYPTION_KEY env variable, and would authorize the request only if the decryption succeeded.

So to recap: by downloading an encrypted configuration and finding its matching Azure Function URL, I should be able to achieve remote code execution over it. I would pass the whole encrypted config as x-ms-site-restricted-token and decrypt it bit by bit using the padding oracle. Once I had the configuration, I would use the SCM_RUN_FROM_PACKAGE field to take over the Function similarly as described in the EoP vulnerability, and I would now be in control.

With a plan at hand, I tried mounting this attack on our own controlled server but the oracle was non-cooperative! It reported no errors when it I passed it a token with invalid padding:

Press enter or click to view image in full size

We were expecting the server to reply “Padding is invalid”

I checked the Init Mesh binary to explain this behavior and to my dismay I discovered that the unpadding algorithm was flawed and was broken. Reasonably, I initially assumed the padding algorithm was working as intended, and did not spend time reverse engineering it.

To better understand why it wasn’t working I reconstructed the unpad code:

func init_server_pkg_encryption_pkcs7Unpad(data []byte) (byte[], error) {
  // Check that last byte isn’t zero
  if data[len(data)-1] != 0 {
  // Check that last byte is bigger than message total length
  data[len(data)-1] > len(data) {
  return nil
  }
  }
  return fmt.Errorf(“Padding is invalid”)
}

Compare this with a real unpad algorithm:

func Unpad(data []byte, blockSize uint) ([]byte, error) {
  if blockSize < 1 {
  return nil, fmt.Errorf(“Block size looks wrong”)
  }
  if uint(len(data))%blockSize != 0 {
  return nil, fmt.Errorf(“Data isn’t aligned to blockSize”)
  }
  if len(data) == 0 {
  return nil, fmt.Errorf(“Data is empty”)
  }
  paddingLength := int(data[len(data)-1])
  for _, el := range data[len(data)-paddingLength:] {
  if el != byte(paddingLength) {
  return nil, fmt.Errorf(“Padding had malformed entries. Have ‘%x’, expected ‘%x’”, paddingLength, el)
  }
  }
  return data[:len(data)-paddingLength], nil
}

Ironically, this bug rendered my exploit useless and I could not perform the attack. So in this case, two minuses made a plus.

Afterword

To summarize my findings, I discovered an escalation of privileges vulnerability in Linux Azure Function instances and information disclosure through being able to download arbitrary Functions’ encrypted configuration. I hoped to use the Padding Oracle to mount a crypto attack and decrypt this configuration, however I soon found out that the padding algorithm was flawed. The attack still required matching the oracle (the Function url) to its configuration which probably would have limited the impact of the attack should I have been successful.

These findings were reported to MSRC and they changed the scope of the SAS tokens so that apps cannot read encrypted configurations that do not belong to them. Furthermore, the permissive rw storage token (enabling EoP) was also restricted. As for the padding oracle, seeing as how the component was inoperative, the Azure security team decided not to make changes to it.

I hope you enjoyed the read!

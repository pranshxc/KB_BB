---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-28_redash-saml-authentication-bypass.md
original_filename: 2023-04-28_redash-saml-authentication-bypass.md
title: Redash SAML Authentication Bypass
category: documents
detected_topics:
- sso
- saml
- supply-chain
- oauth
- command-injection
- mfa
tags:
- imported
- documents
- sso
- saml
- supply-chain
- oauth
- command-injection
- mfa
language: en
raw_sha256: cbe2491eed7060dd2f972a65a712a898e302f0c5da76ef47db618bc63c83a7ce
text_sha256: 9041f3c2cfc212e4afcd026f1cda45ea1d5c75f1f5dc75249d1cbe6806ba24fc
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Redash SAML Authentication Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-28_redash-saml-authentication-bypass.md
- Source Type: markdown
- Detected Topics: sso, saml, supply-chain, oauth, command-injection, mfa
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `cbe2491eed7060dd2f972a65a712a898e302f0c5da76ef47db618bc63c83a7ce`
- Text SHA256: `9041f3c2cfc212e4afcd026f1cda45ea1d5c75f1f5dc75249d1cbe6806ba24fc`


## Content

---
title: "Redash SAML Authentication Bypass"
url: "https://blog.calif.io/p/redash-saml-authentication-bypass"
final_url: "https://blog.calif.io/p/redash-saml-authentication-bypass"
authors: ["An Trinh (@_tint0)", "Gia Bui (@yabeow)"]
programs: ["Redash"]
bugs: ["SAML", "Authentication bypass"]
publication_date: "2023-04-28"
added_date: "2023-04-28"
source: "pentester.land/writeups.json"
original_index: 1214
---

# Redash SAML Authentication Bypass

[![Calif's avatar](https://substackcdn.com/image/fetch/$s_!UZ0_!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F489bcdd2-8e9f-4bd1-92c4-09754a4aedd1_144x144.png)](https://substack.com/@calif)[![An Trinh's avatar](https://substackcdn.com/image/fetch/$s_!69J-!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd65e5532-7816-441d-bbeb-1c34723c5d03_72x72.webp)](https://substack.com/@atrinh)[![Gia Bui's avatar](https://substackcdn.com/image/fetch/$s_!JyH3!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6df7128-460f-4199-82b2-7afaba50deb2_144x144.png)](https://substack.com/profile/142936631-gia-bui)

[Calif](https://substack.com/@calif), [An Trinh](https://substack.com/@atrinh), and [Gia Bui](https://substack.com/profile/142936631-gia-bui)

Apr 28, 2023

3

Share

[Redash](https://redash.io/) is a popular data analysis and visualization tool. We recently reported a critical SAML authentication bypass vulnerability affecting its latest version (10.1.0).

The vulnerability could be exploited by anyone to gain highest possible privileges on the system. Its discovery led to an [important announcement](https://github.com/getredash/redash/discussions/5961) from the project’s maintainer.

# The Vulnerability

We encountered Redash in a recent engagement. This is not the first time we met this open-source software, so we decided to take a closer look.

Most of Redash's attack surface is put behind authentication. That’s why SAML was among the areas we audited first. We had a couple of findings, but the most critical by far is a SAML authentication bypass.

The vulnerability works as follows:

  * In the SAML flow, Redash acts as the Service Provider (SP), and popular providers like Okta or Google act as the Identity Provider (IdP).

  * SAML relies on digital signatures to authenticate users. The user logs into the IdP and gets redirected back to Redash with a signed SAML message containing the user’s information.

  * Redash uses the library _pysaml2_ 6.1.0 to implement SAML authentication at the two endpoints _/saml/login_ and _/saml/callback_. However, pysaml2 before version 6.5.0 is vulnerable to [CVE-2021-21239](https://github.com/IdentityPython/pysaml2/security/advisories/GHSA-5p3x-r448-pc62), which allows one to bypass signature verification on arbitrary SAML messages.

  * Specifically, the default backend of pysaml2, _CryptoBackendXmlSec1_ , uses the command line utility _[xmlsec1](https://github.com/lsh123/xmlsec)_ to verify signed SAML messages. However, xmlsec1 by default prefers the key embedded in the message over explicitly loaded keys (such as specified on the command line). This dangerous behaviour was first reported by Greg Vishnepolsky [in 2013](https://www.aleksey.com/pipermail/xmlsec/2013/009717.html).

# The Exploit

The vulnerability allows us to forge SAML messages from any identity providers. To exploit it against real-world Redash instances, we have to overcome a few small obstacles:

  * Obtaining SAML Entity ID: in the SAML world, each identity provider is uniquely identified by a SAML Entity ID. Redash will only accept SAML messages if this value is correct. Fortunately, most IdP uses SAML entity IDs that can be inferred from observing a SAML login session. For example, Google uses the pattern _https://accounts.google.com/o/saml2?idpid= <IDPID>_ as shown in the screenshot below.

[![](https://substackcdn.com/image/fetch/$s_!glqa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b34a0d5-ff4b-44fb-a4ec-9ef47fef08be_1600x393.png)](https://substackcdn.com/image/fetch/$s_!glqa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b34a0d5-ff4b-44fb-a4ec-9ef47fef08be_1600x393.png)

  * Signing in as administrator: when a user signs in to Redash over SAML with a non-existent email address, Redash automatically creates an account for that address. This is called Just In Time (JIT) provisioning. So we can sign in as test@victim.com, go to Settings → Users to obtain a list of all accounts on the Redash instance - like the screenshot below - and forge another SAML message to sign in as one of the admin accounts.

[![](https://substackcdn.com/image/fetch/$s_!wCS5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3b29169-e15e-4419-bca0-cc1aa8fb54ca_1600x609.png)](https://substackcdn.com/image/fetch/$s_!wCS5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3b29169-e15e-4419-bca0-cc1aa8fb54ca_1600x609.png)

Other than that, Redash allows unsolicited SAML responses, which means one does not have to go through the whole SP-initiated logon flow to craft a valid SAML response payload, simplifying the exploit.

# Remediation

Redash quickly acknowledged the vulnerability, but has not released a new version with the dependency fix. The [official advisory](https://github.com/getredash/redash/security/advisories/GHSA-rm5x-rgmf-qv5c) recommends upgrading pysaml2 to version >= 6.5.0.

As a defense-in-depth, consider:

  * switch to OAuth2 instead of SAML

  * update REDASH_COOKIE_SECRET to invalidate all existing sessions

# Impact

We reported the issue to multiple affected organizations. Considering the fix has to be applied manually, it’s impressive how they resolved this in a matter of days. Most classified the vulnerability as critical and rewarded generously for it.

# Timeline

  * Jan 16, 2023: Discovered the vulnerability

  * Mar 17, 2023: Reported to Redash

  * Mar 18, 2023: Redash confirmed the vulnerability

  * Apr 4, 2023: [GitHub advisory published](https://github.com/getredash/redash/security/advisories/GHSA-rm5x-rgmf-qv5c)

  * Apr 4, 2023: Reported to known affected organizations

  * Apr 28, 2023: Published this blog post

# Parting words

This vulnerability is unfortunate. Despite being very popular, Redash’s development has been halted since it was acquired by Databricks. This is probably why this issue has evaded detection for so long. Any automation tool could have caught it. In fact, GitHub’s dependapot submitted a [pull request](https://github.com/getredash/redash/pull/5363) to upgrade pysaml2 a while ago, but it was ignored.

On the bright side, we’re glad to see this work is driving positive changes. Redash made another announcement after the disclosure and decided to resurrect the project, as per [A New Chapter as a Community-Led Project](https://github.com/getredash/redash/discussions/5962).

As always, SAML is tricky to implement correctly and remains a large attack surface to explore.

Finally, props to the team for a great collaboration on this little research, especially to An for finding the vulnerability and Gia for doing all the heavy work.

* * *

[1] <https://github.com/getredash/redash/security/advisories/GHSA-rm5x-rgmf-qv5c>

[2] <https://github.com/IdentityPython/pysaml2/security/advisories/GHSA-5p3x-r448-pc62>

[3] <https://www.aleksey.com/pipermail/xmlsec/2013/009717.html>

[4] <https://github.com/getredash/redash/discussions/5961>

3

Share

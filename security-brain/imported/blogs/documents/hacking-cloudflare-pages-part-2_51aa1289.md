---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-23_hacking-cloudflare-pages-part-2.md
original_filename: 2023-12-23_hacking-cloudflare-pages-part-2.md
title: Hacking Cloudflare Pages part 2
category: documents
detected_topics:
- supply-chain
- jwt
- command-injection
- path-traversal
- mfa
tags:
- imported
- documents
- supply-chain
- jwt
- command-injection
- path-traversal
- mfa
language: en
raw_sha256: 51aa12897763d46c13070db47c2b5158203a926a7098b99dca6eb2fe5bddf07b
text_sha256: 0003f0cc2412cd68b75ab5f12f4e01af1d0f904d8d0c52343494779c7c70459a
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Cloudflare Pages part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-23_hacking-cloudflare-pages-part-2.md
- Source Type: markdown
- Detected Topics: supply-chain, jwt, command-injection, path-traversal, mfa
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `51aa12897763d46c13070db47c2b5158203a926a7098b99dca6eb2fe5bddf07b`
- Text SHA256: `0003f0cc2412cd68b75ab5f12f4e01af1d0f904d8d0c52343494779c7c70459a`


## Content

---
title: "Hacking Cloudflare Pages part 2"
page_title: "𖤐 ec0 :: tachibana systems division 𖤐"
url: "https://ec0.io/post/hacking-cloudflare-pages-part-2/"
final_url: "https://ec0.io/post/hacking-cloudflare-pages-part-2/"
authors: ["ec0"]
programs: ["Cloudflare"]
bugs: ["Path traversal", "RCE", "Arbitrary Code Execution"]
publication_date: "2023-12-23"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 596
---

[𖤐 ec0 :: tachibana systems division 𖤐](/)

  * :: 
  * [ ♥ blog ](/)
  * [ ♥ about ](/about/)

# Hacking Cloudflare Pages part 2 - Sat, Dec 23, 2023

これらの脆弱性について日本語で読みたい場合は、[こちら](https://blog.ryotak.me/post/cloudflare-pages-privesc-and-page-tampering/)から読むことができます

###  Background 

If you haven't read the writeup that myself and [Sean](https://twitter.com/seanyeoh) wrote when I was still at Assetnote on our initial adventures into Cloudflare Pages, you should check them out [here](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/)!

As a follow up to this, I had the opportunity to work with the wonderful & skilled [RyotaK](https://twitter.com/ryotkak) who contacted us with a new vector for dumping out files as the root user in the build system, so we all decided to collaborate and see what we could find if we picked apart Cloudflare page's build system again.

###  Regaining access 

We lost our previous method for dumping out the source code and various files in the filesystem when our previous reports were addressed, which meant we had not been able to review the current version of the build scripts and tools. RyotaK found a very clever way to abuse the functionality allowing users of Cloudflare Pages to set custom redirects or headers. Cloudflare pages allows users to set a file called [_redirects](https://developers.cloudflare.com/pages/platform/redirects/) or [_headers](https://developers.cloudflare.com/pages/platform/headers/) in their repository. The security flaw here, is that the Pages build system processes these files as root, and does not check to see if they are symlinks. So, as part of setting your build script up, you could (it has been fixed now) add a step similar to -
  
  
  ln -s /etc/shadow _redirects

…which will be executed during the build, and when redirects and headers are showing in the build results, you could exfiltrate files as root in the results panel. We used this to re-dump the source code for the build agent, so we could do some more code review. We were also about to dump the environment for the root user using the /proc/<pid>/environ trick to dump environment variables for system processes.

Using the dumped code, and the environment variables, we were able to find two more vulnerabilities which had good impact.

###  Internal API path traversal 

Internally, Cloudflare Pages uses an API which is not exposed to the Internet. It is used to pull and push data about the build environment and submit built results back to Pages. The API call look like this -
  
  
  https://api.pages.cloudflare.com/client/v4/accounts/d6fa5e8917ff81a61c1f92fc98b9f85d/storage/kv/namespaces/332a39fcd8a845d7909d2d5d753604d8/values/builds/5486590/logs

Normally, it is secured via an authenticating proxy to prevent you from accessing anything other than your own project and namespace. The UUIDs in the accounts and namespace parts of the URL must match the values encoded in the JWT. The user does not control these values nor can they change them, however, there was a path traversal vulnerability in the API allowing requests to be made outiside of the constraints of the user's regular account and namespace.

Issuing a request such as -
  
  
  https://api.pages.cloudflare.com/client/v4/accounts/d6fa5e8917ff81a61c1f92fc98b9f85d/storage/kv/namespaces/723ab79f47c549658d468156d47432f4/..%2F..%2f..%2f..%2f..%2f..%2Faccounts%2fd6fa5e8917ff81a61c1f92fc98b9f85d%2fstorage/kv/namespaces/332a39fcd8a845d7909d2d5d753604d8/keys

Would allow you to access sensitive data like keys used in other users' builds, build artifacts, for example. As one example of using this to further pivot your access, often there were keys allowing access to the GitHub account of another user.

###  Arbitrary code execution as root user 

In Cloudflare Pages' functions support, the wrangler npm package is installed during page build time to handle gathering of functions for deployment. Wrangler is a utility CLI for working with Cloudflare functions.

This tool is installed as part of the build in case the pages build registers any functions, a feature which was relatively new to Pages at the time this testing was performed. The version of wrangler could be controlled via the PAGES_WRANGLER_VERSION environment variable, which in turn was passed to npm in the below build tool step in /opt/pages/build_tool/steps/build_assets.py -
  
  
  version = [env_var['value'] for env_var in env_vars if env_var['key'] == 'PAGES_WRANGLER_VERSION'][0]
  <.. snip ...>
  subprocess.run(['npm', 'install', f'wrangler@{version}'], cwd=WRANGLER_DIR, check=True, capture_output=True)

As you can see from the above, we have control over the version variable, which is interpolated into the npm command after the package name and an @ symbol. We can use this to abuse an npm feature for installing a specific version of a package from either a git repository or fixed URL containing a tarball. For example, setting the PAGES_WRANGLER_VERSION environment variable in the build settings to /opt/buildhome/repo/wrangler-3.0.0.tgz, and including a malicious wrangler-3.0.0.tgz npm package with modified wrangler binary in the build repository. In our example, we modified the wrangler binary to execute a reverse shell back to a host we controlled. The modified wrangler2 binary was called as root previously with the user controlled version, so using our malicious wrangler package led to code execution as root.

###  Summary 

I hope this brief writeup is helpful for someone in their travels on the Internet. I'd also like to say thanks to Sean, RyotaK for their collaboration and skill, and the Cloudflare Pages security team for being a pleasure to work with in reporting these vulnerabilities.

* * *

[GPG](/gpg.txt) [Mail](mailto://james@ec0.io) [GitHub](https://github.com/devec0) [GitLab](https://gitlab.com/ec0) [Matrix](https://matrix.to/#/%40ec0%3aspooky.computer) [Fediverse](https://toot.spooky.computer/@ec0)

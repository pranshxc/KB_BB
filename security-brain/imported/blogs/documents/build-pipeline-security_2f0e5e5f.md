---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-18_build-pipeline-security.md
original_filename: 2021-02-18_build-pipeline-security.md
title: Build Pipeline Security
category: documents
detected_topics:
- command-injection
- cloud-security
- xss
- automation-abuse
- webhooks
- api-security
tags:
- imported
- documents
- command-injection
- cloud-security
- xss
- automation-abuse
- webhooks
- api-security
language: en
raw_sha256: 2f0e5e5f6faaff31598c94acaa788714c64a0c37fd94c4bd8b27a4dae56d4686
text_sha256: 2b9e6440d68f9f54ad08b9c54da4c8f088827f25f9fb1e3b50f0f3f54026b575
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Build Pipeline Security

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-18_build-pipeline-security.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, xss, automation-abuse, webhooks, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `2f0e5e5f6faaff31598c94acaa788714c64a0c37fd94c4bd8b27a4dae56d4686`
- Text SHA256: `2b9e6440d68f9f54ad08b9c54da4c8f088827f25f9fb1e3b50f0f3f54026b575`


## Content

---
title: "Build Pipeline Security"
url: "https://sprocketfox.io/xssfox/2021/02/18/pipeline/"
final_url: "https://sprocketfox.io/xssfox/2021/02/18/pipeline/"
authors: ["xssfox (@xssfox)"]
programs: ["AWS"]
bugs: ["RCE"]
publication_date: "2021-02-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3881
---

_This occurred on an AWS website (not a site hosted on AWS, but a site run by AWS). It shows that security is hard, even for a $51 billion business. This issue can occur not just on websites but even SDKs and libraries_

![Fox smelling the road](/xssfox/pipeline/erik-mclean-TNjdgCBRMeU-unsplash.jpg)

> 📸 Erik Mclean via unsplash

While developers have a keen nose for [code smells](https://en.wikipedia.org/wiki/Code_smell) us operations types have a keen nose for infrastructure smells. When I opened this git repository for first time it hit me. A `buildspec.yml` file.

### The humble `buildspec.yml`

For those unfamiliar, `buildspec.yml` is used by a service called [CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html) and basically defines the steps used to build a project, including running shell commands. It’s basically remote code execution as a service.

The presence of this file in a repository isn’t call for alarm, but when it’s in a public repository it certainly raises red flags. The usual concern is someones committed some secret credentials into this file. In this case the file was clean of credentials.

All good right? Not so fast.

![Fox sleeping](/xssfox/pipeline/lachlan-gowen-cWwqwN2uTo4-unsplash.jpg)

> 📸 Lachlan Gowen via unsplash

### _notices your`deploy.sh`_

The `buildspec.yml` referenced a `deploy.sh`. This is when I verbally said “oh no”. Like before no secrets committed. A good start. `deploy.sh` contains instructions to deploy out the project - like `aws s3 sync` and the like, so we can determine that when this gets run it has access to upload to the production site.

![Fox yelling](/xssfox/pipeline/nathan-anderson-3Lazy6QQR6c-unsplash.jpg)

> 📸 Nathan Anderson via unsplash

The issue here is that the `buildspec.yml` and `deploy.sh` could be modified by a malicious user.

### The pull request

However malicious user doesn’t have access to commit to the repository and an admin isn’t going to merge malicious code, so this is no big deal right? Let’s see what happens when we lodge a pull request.

Upon creation of the pull request GitHub triggers a CodeBuild job. This is a fairly common practice to make sure nothing in the pull request breaks the build. What prevents the pull request build from deploying to production? Lets check `deploy.sh`
  
  
  if [[ "$CODEBUILD_WEBHOOK_HEAD_REF" == "refs/heads/main" && ${CODEBUILD_SOURCE_VERSION:0:3} != "pr/" ]]; then
  

oh no.

So deployment is purely controlled by a script that can be changed in the pull request.

![Fox in grass](/xssfox/pipeline/scott-walsh-7LzKELgdzzI-unsplash.jpg)

> 📸 Scott Walsh via unsplash

### One last chance

At this stage we’ve got remote code execution into the pipeline. Apart from [mining some Bitcoin](https://www.vice.com/en/article/nzkxgm/bitcoin-mining-github-open-source-bots) this is pretty uneventful. What about the S3 sync we mentioned earlier? It’s possible that the role granted for pull requests is the same role used for deploying to production, so lets check it out.

I edited the shell script to have my code right at the start …
  
  
  echo "testing a security issue" > test.html
  aws s3 cp test.html s3://target_bucket/test.html
  aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_DIST_ID --paths "/*"
  exit 1
  

> `target_bucket` value was recovered from original `deploy.sh`

… and lodged a pull request. I checked the website and sure enough my file was there. 😮

![Fox licking lips](/xssfox/pipeline/nathan-anderson-XHK0JdmJxJc-unsplash.jpg)

> 📸 Nathan Anderson via unsplash

### It doesn’t end there

It’s quite possible that the role used for deployment might have access to lots of interesting things, a private subnet, IAM admin, CloudFormation. I didn’t check further than this and submitted a disclosure reported to the security team immediately.

### Prevention

If you still want pull requests to trigger builds on a public repository there a couple of things you can do to limit risk.

Place build scripts in a separate repo. Some build tools let you specify a separate repo to use for the build pipeline. Be careful though as this doesn’t guarantee that the project build can’t execute commands, depending on the programming language and build tools.

For services like CodeBuild you can utilize a separate IAM role for pull requests which is limited to just build requirements. Make sure the build agents for PRs aren’t within a a trusted network.

[pr](https://sprocketfox.io/xssfox/tags/pr/) [aws](https://sprocketfox.io/xssfox/tags/aws/) [security](https://sprocketfox.io/xssfox/tags/security/) [pull request](https://sprocketfox.io/xssfox/tags/pull-request/) [cicd](https://sprocketfox.io/xssfox/tags/cicd/) [codepipeline](https://sprocketfox.io/xssfox/tags/codepipeline/) [github](https://sprocketfox.io/xssfox/tags/github/) [git](https://sprocketfox.io/xssfox/tags/git/)

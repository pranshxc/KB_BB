---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-07_how-i-gained-commit-access-to-homebrew-in-30-minutes.md
original_filename: 2018-08-07_how-i-gained-commit-access-to-homebrew-in-30-minutes.md
title: How I gained commit access to Homebrew in 30 minutes
category: documents
detected_topics:
- supply-chain
- oauth
- command-injection
- otp
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- supply-chain
- oauth
- command-injection
- otp
- automation-abuse
- information-disclosure
language: en
raw_sha256: 056cc906218698ab00d99fc6a65fa0b112e050b270e412729f9adaf183decb99
text_sha256: ec274645e30390229c094e293713cd8b1a6fffe6d1c9fac43a39ed3c775850ee
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I gained commit access to Homebrew in 30 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-07_how-i-gained-commit-access-to-homebrew-in-30-minutes.md
- Source Type: markdown
- Detected Topics: supply-chain, oauth, command-injection, otp, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `056cc906218698ab00d99fc6a65fa0b112e050b270e412729f9adaf183decb99`
- Text SHA256: `ec274645e30390229c094e293713cd8b1a6fffe6d1c9fac43a39ed3c775850ee`


## Content

---
title: "How I gained commit access to Homebrew in 30 minutes"
url: "https://medium.com/@vesirin/how-i-gained-commit-access-to-homebrew-in-30-minutes-2ae314df03ab"
authors: ["Eric Holmes (@vesirin)"]
programs: ["Homebrew"]
bugs: ["Information disclosure"]
publication_date: "2018-08-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5767
scraped_via: "browseros"
---

# How I gained commit access to Homebrew in 30 minutes

Top highlight

1

How I gained commit access to Homebrew in 30 minutes
Eric Holmes
Follow
4 min read
·
Aug 7, 2018

10.9K

5

This issue was publicly disclosed on the Homebrew blog at https://brew.sh/2018/08/05/security-incident-disclosure/

Since the recent NPM, RubyGems, and Gentoo incidents, I’ve become increasingly interested, and concerned, with the potential for package managers to be used in supply chain attacks to distribute malicious software. Specifically with how the maintainers and infrastructure of these projects can be targeted as an attack vector.

On Jun 31st, I went in with the intention of seeing if I could gain access to Homebrew’s GitHub repositories. About 30 minutes later, I made my first commit to Homebrew/homebrew-core.

Let’s get leaky

My initial strategy going in was based on credential theft; find if there were any credentials leaked by members of the Homebrew GitHub org.

An OSSINT tool from Michael Henriksen called gitrob makes automating this search really easy. I ran it across the Homebrew organization, but ultimately didn’t come up with anything interesting.

Next, I took a look at previously disclosed issues on https://hackerone.com/Homebrew. From there, I found that Homebrew runs a Jenkins instance that’s (intentionally) publicly exposed at https://jenkins.brew.sh.

Get Eric Holmes’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some digging, I noticed something interesting; builds in the “Homebrew Bottles” project were making authenticated pushes to the BrewTestBot/homebrew-core repo:

Press enter or click to view image in full size

This got me thinking, “where are the credentials stored?”. I noticed the “Environment Variables” link on the left, which led to an exposed GitHub API token:

Press enter or click to view image in full size

I tested it locally to see what scopes the token had:

$ curl https://api.github.com/user/repos -u $GITHUB_API_TOKEN:x-oauth-basic | jq '.[] | {repo: .full_name, permissions: .permissions}'
{
  "repo": "BrewTestBot/homebrew-core",
  "permissions": {
  "admin": true,
  "push": true,
  "pull": true
  }
}
{
  "repo": "Homebrew/brew",
  "permissions": {
  "admin": false,
  "push": true,
  "pull": true
  }
}
{
  "repo": "Homebrew/formulae.brew.sh",
  "permissions": {
  "admin": false,
  "push": true,
  "pull": true
  }
}
{
  "repo": "Homebrew/homebrew-core",
  "permissions": {
  "admin": false,
  "push": true,
  "pull": true
  }
}

Which suggested that I had commit access to these core Homebrew repos:

Homebrew/brew
Homebrew/homebrew-core
Homebrew/formulae.brew.sh

Just to make sure, I tested this by creating a blob in the Homebrew/homebrew-core repo:

$ curl https://api.github.com/repos/Homebrew/homebrew-core/git/blobs -u $GITHUB_API_TOKEN:x-oauth-basic -d '{"content":"test"}' -H "Content-Type: application/json"
{
  "sha": "30d74d258442c7c65512eafab474568dd706c430",
  "url": "https://api.github.com/repos/Homebrew/homebrew-core/git/blobs/30d74d258442c7c65512eafab474568dd706c430"
}

And then subsequently reported the issue to the Homebrew maintainers.

What this means

Let me put this in perspective:

Hundreds of thousands of people use Homebrew, including employees at some of the biggest companies in Silicon Valley.
The most frequently installed package in the last 30 days is openssl, which was installed over 500k times: https://formulae.brew.sh/analytics/install/30d/
I had direct commit access to the Homebrew/homebrew-core repo. At the time, this repo did not have a protected master branch, meaning I would have been able to make a fast-forward change to refs/heads/master. Anyone that freshly installed Homebrew, or ran brew update would have my malicious formulae.

If I were a malicious actor, I could have made a small, likely unnoticed change to the openssl formulae, placing a backdoor on any machine that installed it.

If I can gain access to commit in 30 minutes, what could a nation state with dedicated resources achieve against a team of 17 volunteers? How many private company networks could be accessed? How many of these could be used to escalate to large scale data breaches? What other package management systems have similar weaknesses?

This is my growing concern, and it’s been proven time and time again that package managers, and credential leaks, are a weak point in the security of the internet, and that supply chain attacks are a real and persistent threat. This is not a weakness in Homebrew, but rather a systemic problem in the industry, and one where we need more security research.

What’s being done

Homebrew has publicly disclosed the issue on the blog at https://brew.sh/2018/08/05/security-incident-disclosure/. The Homebrew team worked with GitHub to audit and ensure that the given access token wasn’t used maliciously, and didn’t make any unexpected commits to the core Homebrew repos. I want to give special thanks to Mike McQuaid for his quick and professional handling of my report while on his paternity leave.

It’s clear that there’s a lot of work that could be done to improve the security of the Homebrew project. If you use Homebrew at your place of work, consider asking them to donate to the project. As an industry, we need to invest in the well being of core OSS software that we all use and depend on.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-05_4500-of-the-top-1-million-websites-leaked-source-code-secrets.md
original_filename: 2023-09-05_4500-of-the-top-1-million-websites-leaked-source-code-secrets.md
title: 4,500 of the Top 1 Million Websites Leaked Source Code, Secrets
category: documents
detected_topics:
- api-security
- supply-chain
- access-control
- cloud-security
- oauth
- command-injection
tags:
- imported
- documents
- api-security
- supply-chain
- access-control
- cloud-security
- oauth
- command-injection
language: en
raw_sha256: a19d4b8c5d36d13ce4df4491f5d196e7caa79b3f8efa27d9639b938940627b2e
text_sha256: 008b6240d28318064c998f3c30897b1edab229e8a6e502c9eaf8797b57fb6c3f
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# 4,500 of the Top 1 Million Websites Leaked Source Code, Secrets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-05_4500-of-the-top-1-million-websites-leaked-source-code-secrets.md
- Source Type: markdown
- Detected Topics: api-security, supply-chain, access-control, cloud-security, oauth, command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `a19d4b8c5d36d13ce4df4491f5d196e7caa79b3f8efa27d9639b938940627b2e`
- Text SHA256: `008b6240d28318064c998f3c30897b1edab229e8a6e502c9eaf8797b57fb6c3f`


## Content

---
title: "4,500 of the Top 1 Million Websites Leaked Source Code, Secrets"
page_title: "4,500 of the Top 1 Million Websites Leaked Source Code, Secrets ◆ Truffle Security Co."
url: "https://trufflesecurity.com/blog/4500-of-the-top-1-million-websites-leaked-source-code-secrets/"
final_url: "https://trufflesecurity.com/blog/4500-of-the-top-1-million-websites-leaked-source-code-secrets"
authors: ["Truffle Security (@trufflesec)", "Harsh Bothra (@harshbothra_)", "Luke Stephens (@hakluke)"]
bugs: ["Information disclosure"]
publication_date: "2023-09-05"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 806
---

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

TRUFFLEHOG

[CUSTOMERS](../customers)

COMPANY

RESOURCES

[LOG IN](https://trufflehog.org/)

[Contact Us](https://trufflesecurity.com/contact)

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

Joe Leon

### [The Dig](../blog)

September 5, 2023

# 4,500 of the Top 1 Million Websites Leaked Source Code, Secrets

# 4,500 of the Top 1 Million Websites Leaked Source Code, Secrets

Joe Leon

September 5, 2023

 _This research was done in collaboration with Harsh Bothra and Luke Stephens_ from [_Hackercontent_](http://hackercontent.com/) _._

#### We scanned the Alexa Top 1 Million Websites for leaked secrets. We found thousands of exposed source code repositories and hundreds of live API keys.

These are our top 5 takeaways:

##### 4,500 Heavily Visited Websites Publicly Exposed Source Code

Our research team discovered **4,500** of the most visited websites in the world publicly exposed their git directory (ie https://example.com/.git).

These git directories often contained the entire private source code for a given website. Attackers could use this inside knowledge to mount an attack against the victim’s web application or search the code for live credentials to third-party services like AWS.

##### AWS and GitHub Keys were the Most Frequently Leaked Secrets

  

![](https://framerusercontent.com/images/xF1LVP7VTsSr0aLVxExq0nimoU.png?width=1200&height=742)

 _Most Frequently Leaked Credentials_

  

AWS and GitHub keys accounted for 45% of all leaked credentials. 

You might be wondering why there are so many GitHub tokens. That’s because these tokens often land in the Git config file during remote repository cloning. (For more details see the Identifying Exposed Git Directories section below.)

Third-party email marketing services (like Mailgun, SendInBlue, Mailchimp, and Sendgrid) accounted for a large percentage of the leaked keys as well.

##### 67% of GitHub Credentials had Admin Access

TruffleHog verifies valid GitHub credentials by making a simple GET request to GitHub’s `/user` API endpoint. The response returns the permissions granted to that [Personal Access Token](https://docs.github.com/en/rest/orgs/personal-access-tokens?apiVersion=2022-11-28) (PAT) in the `X-OAuth-Scopes` header.

  

![](https://framerusercontent.com/images/9gQJVlpwKqPifthVZWIGZc3QI.png?width=1020&height=261)

_Many GitHub Tokens Contained Administrative Rights_

  

After reviewing the permissions granted to each valid GitHub PAT, we discovered the majority (67%) had admin-level privileges. All (100%) had `repo` permissions, which would enable an attacker to take arbitrary actions against all of the victim user’s repositories, including, but not limited to implanting malware in the code.

##### A Website Leaked their SSL Certificate Private Key

TruffleHog identified one private RSA key. We ran that key through [Driftwood](https://github.com/trufflesecurity/driftwood), [our new private key usage verification tool](https://trufflesecurity.com/blog/driftwood/), and discovered that the RSA key corresponded to that domain’s TLS certificate.

  

![](https://framerusercontent.com/images/a5W1ZhIjl35Qkk5TqUTSDItQo.png?width=1524&height=342)

_Verifying a Website’s Private TLS Key_

  

Attackers could have used this private key to conduct a man-in-the-middle attack, among other malicious actions against that domain.

##### Fluctuating Exposure of Git Directories Across Organizations

We conducted two rounds of research, one month apart, against the same list of 1 Million websites. The first round returned 255 leaked keys. The second round returned 97 leaked keys. Our research team attributes this discrepancy to the natural ebb and flow of vulnerabilities: some websites removed their .git directories, while others leaked new keys. 

If we repeated this study, we would undoubtedly get different results; however, at a minimum, we’d most likely identify a few hundred leaked keys.

We followed industry standards and attempted to notify all impacted organizations and individuals about their exposed data. While we don’t share which websites exposed their git directories (and secrets data), below we share our research approach.

## What is a .git Directory?

A .git directory is created when a Git repository is initialized. This directory generally contains code commits, commit messages, file paths, and other version control information. Essentially, git holds all the “plumbing” for a source code repository. Publicly exposing a .git directory enables an attacker to gain access to:

  * Source code: The entire source code of a project may be exposed, including proprietary algorithms, custom-built software, and trade secrets.

  * Configuration files: `.git/CONFIG` files often contain the password to the Git repo.

  * Commit history: The commit history of a repository can provide insight into an organization’s past mistakes, and internal service names.

  * Access credentials: If credentials are stored in git, a copy is also stored in the `/.git` directory. Attackers can use them to access systems and data. Often attackers will identify credentials from past commits.

## Identifying Exposed Git Directories

Discovering Git directories on a list of public websites seemed like a simple task. Unfortunately, we couldn’t just cURL an HTTP GET request to `/.git` and record all HTTP 200 responses. Many of the Alexa Top 1 Million websites used a Web Application Firewall (WAF), which returned unpredictable results. Additionally, some sites returned a HTTP 403 (Forbidden) response when querying the `/.git` path; however, we could access all subdirectories and files underneath the `/.git` folder.

Our research team reviewed Git’s official documentation and determined that identifying a `/.git/CONFIG` file would provide the most reliable determination that a website exposed a valid Git directory. We requested each site’s Git CONFIG file (ie: https://domain.com/.git/config) and then reviewed the first line of text to determine whether we retrieved a valid Git CONFIG file.

_Note: Git config files often house credentials. When running the following command, the git password will live inside the config file:_

  

  
  
  git

  

![](https://framerusercontent.com/images/dSmv61o9wUoOHuA7UG10kkimnQ.png?width=1252&height=474)

 _Example Git CONFIG File Storing Cleartext Credentials_

  

Here’s [a link to the type of Python script](https://gist.github.com/joeleonjr/98b5f3b629a049954ed7bac67a80451f) we used to conduct the CONFIG file testing.

## Reconstructing Project Source

Downloading a complete Git repository seemed like another simple task (just `git clone`, right?). Unfortunately, there were many edge-cases to consider, such as corrupted repos. To reconstruct the Git repositories and clone them to our local machine, we decided on the open-source tool [Goop](https://github.com/nyancrimew/goop). We found Goop to be mostly feature-complete and very efficient.

Running Goop is extremely simple; pass the URL as the only command-line argument.

**Command:** `./goop <url>`

  

![](https://framerusercontent.com/images/our3PAJrcr2qhhAzUoWBn9y4bw.png?width=1600&height=394)

_Running Goop Successfully_

  

If Goop can extract a Git repository, it will create a new folder titled with the target URL’s name and include all of the available project source code / version control information.

## Running TruffleHog to Find Exposed Secrets in Git

TruffleHog scans git repositories (and other sources) to identify sensitive data like keys, tokens, and passwords. When TruffleHog identifies a secret (we currently detect ~ 750 different types of secrets), it then attempts to authenticate using that credential. TruffleHog provides users with extremely high confidence that any secret reported as “verified” is live because it’s been used to authenticate.

Most of the time we recommend using the `git` subcommand on git repos, but some repositories were corrupted, so we used a combination of the `filesystem` and `git` commands. (_For a detailed discussion on when to use the Filesystem vs the Git command,_[_please see this post._](https://trufflesecurity.com/blog/trufflehog-commands-git-vs-filesystem/))

The following steps outline how to run TruffleHog against an exposed Git directory.

  1. Run TruffleHog’s `filesystem` (or `git`) command against the local Git directory. 

  

  

  2. If the scan returns exposed secrets, you’ll note all verified results are green and all unverified results are grey. A verified result means TruffleHog successfully authenticated to the target service using that credential. Importantly, an unverified result could still contain a live key, it just means that TruffleHog could not successfully authenticate against the relevant third-party service.

  

![](https://framerusercontent.com/images/IYaTp0digpkGQdDtpEg9nlkaQZE.png?width=1128&height=442)

_Verified and Unverified AWS Keys in TruffleHog_

  

  3. Re-run the above command with the `--only-verified` flag to see only “verified” secrets. 

  

  

![](https://framerusercontent.com/images/i6JnqVHrdEX6U506zFvcsRTkaQ.png?width=722&height=218)

 _Only Verified Keys in TruffleHog_

## Responsible Disclosure

After identifying a verified, exposed secret, our research team attempted to contact the impacted website owners. Truthfully, this was the most time-consuming part of our research. For most websites, we attempted the following 4 steps:

  1. Look for valid email addresses in git history. When you commit to git, your identity (including an email) attaches to the code changes. Unfortunately, as mentioned above, many of the sites served corrupted git repositories. This prevented us from reconstructing git history and easily identifying contacts at scale.

  2. Conduct a WHOIS lookup. Most organizations used private registration, so this wasn’t very helpful either.

  3. Guess role-based email addresses (ex: `security@domain`, `info@domain`). It’s not perfect, but most organizations have at least one role-based email address. We almost uniformly attempted `security@` and `info@`, unless we identified a reason to try another (such as `seguridad@` for a Spain-based website). 

  4. Rely on catch-all email configurations. Many email services implement a “catch-all” policy, where an email sent to a non-existent user gets redirected to a catch-all inbox. This is the least effective method, since this makes our message seem spammy. 

We attempted a minimum of 2 different email addresses for each website. Our notification emails looked like this: 

  

![](https://framerusercontent.com/images/pQ5Li7OpXKkDyYYQwIIxAbDcdI.png?width=747&height=674)

Our Disclosure Email

## Remediating an Exposed Git Directory

Given these website’s high traffic volume, we should assume web crawlers, and archivers (like archive.org), have already replicated and copied these keys. The only robust remediation solution is to invalidate, or rotate all exposed secrets. [Click here for a more detailed post on key rotation](https://trufflesecurity.com/blog/remediate-leaked-api-keys-with-key-rotation/).

## Preventing Data Exposure in a Git Directory

  1. Avoid committing sensitive data such as passwords, private keys, and other secrets to your repository. Use environment variables or other secure means to store this information instead..

  2. Implement pre-commit hooks, using tools like TruffleHog, to prevent sensitive data from committing to git. 

  3. Remove the .git directory from production servers and verify that the .git directory is not deployed along with an application.

  4. Use .gitignore to exclude sensitive files (like config files) from being tracked by Git.

  5. Implement access controls on the web server to restrict access to the .git directory. For example, using Nginx, you could implement the following configuration:

  

  
  location ~ /\.git

  

  6. Regularly scan your repositories and servers for vulnerabilities, including the presence of a .git directory.

## Conclusion

Our research team identified several thousand exposed .git directories on the Alexa Top 1 Million Websites. In addition to the risk that exposing source code presents for an organization, TruffleHog identified several hundred valid API keys and other secret information. Attackers can easily identify this information and use it for a variety of malicious purposes. We attempted to contact all organizations with exposed secrets; however, we could not reach everyone. Additionally, the Alexa Top 1 Million Websites list constantly changes, as does the website content hosted by these organizations. This means that recreating this research will lead to slightly different results; however, we’re confident that until all Git directories are removed from public viewing, secrets will continue to leak.

Our research was purposefully narrow in scope. We restricted our search for exposed git directories to the Alexa Top 1 Million Websites. There are millions and millions more websites to review. Also, it’s not uncommon for developers to expose a git directory outside of the web root directory (ex: https://domain.com/my-code/.git). We categorically excluded those types of git repositories from our research. Finally, we only reported verified live secrets, meaning we have extremely high confidence the secrets can be used by an attacker. There are many additional secret types that require users to verify them with an on-premise application/server. Out-of-the-box TruffleHog cannot verify these; however, we encourage users to author custom detectors for this purpose.

There’s a lot more research (and responsible disclosure) to be done to help organizations that inadvertently publicly expose a git directory and leak secrets.

_This research was done in collaboration with Harsh Bothra and Luke Stephens_ from [_Hackercontent_](http://hackercontent.com/) _._

#### We scanned the Alexa Top 1 Million Websites for leaked secrets. We found thousands of exposed source code repositories and hundreds of live API keys.

These are our top 5 takeaways:

##### 4,500 Heavily Visited Websites Publicly Exposed Source Code

Our research team discovered **4,500** of the most visited websites in the world publicly exposed their git directory (ie https://example.com/.git).

These git directories often contained the entire private source code for a given website. Attackers could use this inside knowledge to mount an attack against the victim’s web application or search the code for live credentials to third-party services like AWS.

##### AWS and GitHub Keys were the Most Frequently Leaked Secrets

  

![](https://framerusercontent.com/images/xF1LVP7VTsSr0aLVxExq0nimoU.png?width=1200&height=742)

 _Most Frequently Leaked Credentials_

  

AWS and GitHub keys accounted for 45% of all leaked credentials. 

You might be wondering why there are so many GitHub tokens. That’s because these tokens often land in the Git config file during remote repository cloning. (For more details see the Identifying Exposed Git Directories section below.)

Third-party email marketing services (like Mailgun, SendInBlue, Mailchimp, and Sendgrid) accounted for a large percentage of the leaked keys as well.

##### 67% of GitHub Credentials had Admin Access

TruffleHog verifies valid GitHub credentials by making a simple GET request to GitHub’s `/user` API endpoint. The response returns the permissions granted to that [Personal Access Token](https://docs.github.com/en/rest/orgs/personal-access-tokens?apiVersion=2022-11-28) (PAT) in the `X-OAuth-Scopes` header.

  

![](https://framerusercontent.com/images/9gQJVlpwKqPifthVZWIGZc3QI.png?width=1020&height=261)

_Many GitHub Tokens Contained Administrative Rights_

  

After reviewing the permissions granted to each valid GitHub PAT, we discovered the majority (67%) had admin-level privileges. All (100%) had `repo` permissions, which would enable an attacker to take arbitrary actions against all of the victim user’s repositories, including, but not limited to implanting malware in the code.

##### A Website Leaked their SSL Certificate Private Key

TruffleHog identified one private RSA key. We ran that key through [Driftwood](https://github.com/trufflesecurity/driftwood), [our new private key usage verification tool](https://trufflesecurity.com/blog/driftwood/), and discovered that the RSA key corresponded to that domain’s TLS certificate.

  

![](https://framerusercontent.com/images/a5W1ZhIjl35Qkk5TqUTSDItQo.png?width=1524&height=342)

_Verifying a Website’s Private TLS Key_

  

Attackers could have used this private key to conduct a man-in-the-middle attack, among other malicious actions against that domain.

##### Fluctuating Exposure of Git Directories Across Organizations

We conducted two rounds of research, one month apart, against the same list of 1 Million websites. The first round returned 255 leaked keys. The second round returned 97 leaked keys. Our research team attributes this discrepancy to the natural ebb and flow of vulnerabilities: some websites removed their .git directories, while others leaked new keys. 

If we repeated this study, we would undoubtedly get different results; however, at a minimum, we’d most likely identify a few hundred leaked keys.

We followed industry standards and attempted to notify all impacted organizations and individuals about their exposed data. While we don’t share which websites exposed their git directories (and secrets data), below we share our research approach.

## What is a .git Directory?

A .git directory is created when a Git repository is initialized. This directory generally contains code commits, commit messages, file paths, and other version control information. Essentially, git holds all the “plumbing” for a source code repository. Publicly exposing a .git directory enables an attacker to gain access to:

  * Source code: The entire source code of a project may be exposed, including proprietary algorithms, custom-built software, and trade secrets.

  * Configuration files: `.git/CONFIG` files often contain the password to the Git repo.

  * Commit history: The commit history of a repository can provide insight into an organization’s past mistakes, and internal service names.

  * Access credentials: If credentials are stored in git, a copy is also stored in the `/.git` directory. Attackers can use them to access systems and data. Often attackers will identify credentials from past commits.

## Identifying Exposed Git Directories

Discovering Git directories on a list of public websites seemed like a simple task. Unfortunately, we couldn’t just cURL an HTTP GET request to `/.git` and record all HTTP 200 responses. Many of the Alexa Top 1 Million websites used a Web Application Firewall (WAF), which returned unpredictable results. Additionally, some sites returned a HTTP 403 (Forbidden) response when querying the `/.git` path; however, we could access all subdirectories and files underneath the `/.git` folder.

Our research team reviewed Git’s official documentation and determined that identifying a `/.git/CONFIG` file would provide the most reliable determination that a website exposed a valid Git directory. We requested each site’s Git CONFIG file (ie: https://domain.com/.git/config) and then reviewed the first line of text to determine whether we retrieved a valid Git CONFIG file.

_Note: Git config files often house credentials. When running the following command, the git password will live inside the config file:_

  

  
  
  git

  

![](https://framerusercontent.com/images/dSmv61o9wUoOHuA7UG10kkimnQ.png?width=1252&height=474)

 _Example Git CONFIG File Storing Cleartext Credentials_

  

Here’s [a link to the type of Python script](https://gist.github.com/joeleonjr/98b5f3b629a049954ed7bac67a80451f) we used to conduct the CONFIG file testing.

## Reconstructing Project Source

Downloading a complete Git repository seemed like another simple task (just `git clone`, right?). Unfortunately, there were many edge-cases to consider, such as corrupted repos. To reconstruct the Git repositories and clone them to our local machine, we decided on the open-source tool [Goop](https://github.com/nyancrimew/goop). We found Goop to be mostly feature-complete and very efficient.

Running Goop is extremely simple; pass the URL as the only command-line argument.

**Command:** `./goop <url>`

  

![](https://framerusercontent.com/images/our3PAJrcr2qhhAzUoWBn9y4bw.png?width=1600&height=394)

_Running Goop Successfully_

  

If Goop can extract a Git repository, it will create a new folder titled with the target URL’s name and include all of the available project source code / version control information.

## Running TruffleHog to Find Exposed Secrets in Git

TruffleHog scans git repositories (and other sources) to identify sensitive data like keys, tokens, and passwords. When TruffleHog identifies a secret (we currently detect ~ 750 different types of secrets), it then attempts to authenticate using that credential. TruffleHog provides users with extremely high confidence that any secret reported as “verified” is live because it’s been used to authenticate.

Most of the time we recommend using the `git` subcommand on git repos, but some repositories were corrupted, so we used a combination of the `filesystem` and `git` commands. (_For a detailed discussion on when to use the Filesystem vs the Git command,_[_please see this post._](https://trufflesecurity.com/blog/trufflehog-commands-git-vs-filesystem/))

The following steps outline how to run TruffleHog against an exposed Git directory.

  1. Run TruffleHog’s `filesystem` (or `git`) command against the local Git directory. 

  

  

  2. If the scan returns exposed secrets, you’ll note all verified results are green and all unverified results are grey. A verified result means TruffleHog successfully authenticated to the target service using that credential. Importantly, an unverified result could still contain a live key, it just means that TruffleHog could not successfully authenticate against the relevant third-party service.

  

![](https://framerusercontent.com/images/IYaTp0digpkGQdDtpEg9nlkaQZE.png?width=1128&height=442)

_Verified and Unverified AWS Keys in TruffleHog_

  

  3. Re-run the above command with the `--only-verified` flag to see only “verified” secrets. 

  

  

![](https://framerusercontent.com/images/i6JnqVHrdEX6U506zFvcsRTkaQ.png?width=722&height=218)

 _Only Verified Keys in TruffleHog_

## Responsible Disclosure

After identifying a verified, exposed secret, our research team attempted to contact the impacted website owners. Truthfully, this was the most time-consuming part of our research. For most websites, we attempted the following 4 steps:

  1. Look for valid email addresses in git history. When you commit to git, your identity (including an email) attaches to the code changes. Unfortunately, as mentioned above, many of the sites served corrupted git repositories. This prevented us from reconstructing git history and easily identifying contacts at scale.

  2. Conduct a WHOIS lookup. Most organizations used private registration, so this wasn’t very helpful either.

  3. Guess role-based email addresses (ex: `security@domain`, `info@domain`). It’s not perfect, but most organizations have at least one role-based email address. We almost uniformly attempted `security@` and `info@`, unless we identified a reason to try another (such as `seguridad@` for a Spain-based website). 

  4. Rely on catch-all email configurations. Many email services implement a “catch-all” policy, where an email sent to a non-existent user gets redirected to a catch-all inbox. This is the least effective method, since this makes our message seem spammy. 

We attempted a minimum of 2 different email addresses for each website. Our notification emails looked like this: 

  

![](https://framerusercontent.com/images/pQ5Li7OpXKkDyYYQwIIxAbDcdI.png?width=747&height=674)

Our Disclosure Email

## Remediating an Exposed Git Directory

Given these website’s high traffic volume, we should assume web crawlers, and archivers (like archive.org), have already replicated and copied these keys. The only robust remediation solution is to invalidate, or rotate all exposed secrets. [Click here for a more detailed post on key rotation](https://trufflesecurity.com/blog/remediate-leaked-api-keys-with-key-rotation/).

## Preventing Data Exposure in a Git Directory

  1. Avoid committing sensitive data such as passwords, private keys, and other secrets to your repository. Use environment variables or other secure means to store this information instead..

  2. Implement pre-commit hooks, using tools like TruffleHog, to prevent sensitive data from committing to git. 

  3. Remove the .git directory from production servers and verify that the .git directory is not deployed along with an application.

  4. Use .gitignore to exclude sensitive files (like config files) from being tracked by Git.

  5. Implement access controls on the web server to restrict access to the .git directory. For example, using Nginx, you could implement the following configuration:

  

  
  location ~ /\.git

  

  6. Regularly scan your repositories and servers for vulnerabilities, including the presence of a .git directory.

## Conclusion

Our research team identified several thousand exposed .git directories on the Alexa Top 1 Million Websites. In addition to the risk that exposing source code presents for an organization, TruffleHog identified several hundred valid API keys and other secret information. Attackers can easily identify this information and use it for a variety of malicious purposes. We attempted to contact all organizations with exposed secrets; however, we could not reach everyone. Additionally, the Alexa Top 1 Million Websites list constantly changes, as does the website content hosted by these organizations. This means that recreating this research will lead to slightly different results; however, we’re confident that until all Git directories are removed from public viewing, secrets will continue to leak.

Our research was purposefully narrow in scope. We restricted our search for exposed git directories to the Alexa Top 1 Million Websites. There are millions and millions more websites to review. Also, it’s not uncommon for developers to expose a git directory outside of the web root directory (ex: https://domain.com/my-code/.git). We categorically excluded those types of git repositories from our research. Finally, we only reported verified live secrets, meaning we have extremely high confidence the secrets can be used by an attacker. There are many additional secret types that require users to verify them with an on-premise application/server. Out-of-the-box TruffleHog cannot verify these; however, we encourage users to author custom detectors for this purpose.

There’s a lot more research (and responsible disclosure) to be done to help organizations that inadvertently publicly expose a git directory and leak secrets.

## [More from THE DIG](../blog)

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)[![](https://framerusercontent.com/images/WeB35OGPgqrFpsRGCxRbRHAFRZE.png?width=1200&height=600)May 22, 2026CISA's Leaked Admin GitHub Token Remained Live 2 Days After Krebs Reported It Leaked](./cisa-leaked-admin-github-token-remained-live-2-days)

# [T](../blog)he Dig

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)

STAY STRONG

DIG DEEP

[](../)

TRUFFLEHOG

[Open-source](../trufflehog)

[Enterprise](../trufflehog-enterprise)

[Analyze](../trufflehog-analyze)

[GCP Analyze](../trufflehog-gcp-analyze)

NEW!

[Forager](../trufflehog-forager)

[Security](../security)

[Integrations](../integrations)

[Pricing](../pricing)

[CUSTOMERS](../customers)

COMPANY

[About](../about)

[Careers](../careers)

[Press](../press)

[FAQ](../faq)

[Partners](../partners)

NEW!

[Contact us](../contact)

RESOURCES

[Blog](../blog)

[Newsletter](../newsletter)

[Library](../library)

[Events](../events)

[Videos](../videos)

[GitHub](https://github.com/trufflesecurity)

[Enterprise docs](https://docs.trufflesecurity.com/)

[Open-source docs](https://github.com/trufflesecurity/trufflehog#trufflehog)

[How to rotate](https://howtorotate.com/)

[Brand assets](../branding)

NEW!

DOING IT THE RIGHT WAY

[SINCE 2021](../partners)

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

STAY STRONG

DIG DEEP

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

infra

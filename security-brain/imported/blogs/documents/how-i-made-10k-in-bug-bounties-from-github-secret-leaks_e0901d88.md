---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-10_how-i-made-10k-in-bug-bounties-from-github-secret-leaks.md
original_filename: 2020-05-10_how-i-made-10k-in-bug-bounties-from-github-secret-leaks.md
title: How I made $10K in bug bounties from GitHub secret leaks
category: documents
detected_topics:
- api-security
- sso
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- api-security
- sso
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: e0901d8861eea631c7fb81efdeceef9d1d1640020251873ebdc545cb45ba4443
text_sha256: 3d016ebe3cf475444123200084d3b8a9b8eb09fe520d1849aee7dd524d654431
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I made $10K in bug bounties from GitHub secret leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-10_how-i-made-10k-in-bug-bounties-from-github-secret-leaks.md
- Source Type: markdown
- Detected Topics: api-security, sso, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e0901d8861eea631c7fb81efdeceef9d1d1640020251873ebdc545cb45ba4443`
- Text SHA256: `3d016ebe3cf475444123200084d3b8a9b8eb09fe520d1849aee7dd524d654431`


## Content

---
title: "How I made $10K in bug bounties from GitHub secret leaks"
page_title: "How I made $15K in bug bounties from GitHub secret leaks"
url: "https://tillsongalloway.com/finding-sensitive-information-on-github/index.html"
final_url: "https://tillsongalloway.com/finding-sensitive-information-on-github/index.html"
authors: ["Tillson Galloway (tillson_)"]
bugs: ["Information disclosure"]
bounty: "10,000"
publication_date: "2020-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4596
---

10 May 2020 / [cybersecurity](../tag/cybersecurity/index.html)

# How I made $15k in bug bounties from GitHub secret leaks

API keys, passwords, and customer data are accidentally posted to GitHub every day. 

Hackers use these keys to login to servers, steal personal information, and rack up absurd AWS charges. GitHub leaks can cost a company thousands–or even millions–of dollars in damages. Open-source intelligence gathering on GitHub has become a powerful arrow in every security researcher's quiver: researchers from NC State even wrote an [academic paper](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04B-3_Meli_paper.pdf) on the subject. 

This article, written for both bug bounty hunters and enterprise infosec teams, demonstrates common types of sensitive information (secrets) that users post to public GitHub repositories as well as heuristics for finding them. The techniques in this article can be applied to [GitHub Gist](https://gist.github.com/) snippets, too.

In the last year, I've earned nearly $10,000 from bug bounty programs on [HackerOne](https://hackerone.com) without even visiting programs' websites thanks to these techniques. I've submitted over 30 Coordinated Disclosure reports to vulnerable corporations, including eight Fortune 500 companies. 

**I've also released[GitHound](https://github.com/tillson/git-hound), an open-source tool designed to automate the process of finding keys across GitHub.** GitHound isn't limited to a single user or organization: it sifts through all of GitHub, using Code Search queries as an entrypoint into repositories and then using context, regexes, and some other neat tricks to find secrets.

**New in 2025:** Don't want to download anything? You can now use [GitHound Explore](http://githoundexplore.com/) to scan for secrets in the cloud and to visualize search results in a slick web dashboard (for free!).

## GitHub Code Search

Before we get into the automated tools and bug bounty strategies, let's talk about Code Search. 

GitHub provides [rich code searching](https://github.com/search) that scans public GitHub repositories (some content is omitted, [like forks and non-default branches](https://help.github.com/en/github/searching-for-information-on-github/searching-code#considerations-for-code-search)). Queries can be simple like `uberinternal.com` or can contain multi-word strings like `"Authorization: Bearer"`. Searches can even target specific files (`filename: vim_settings.xml`) or specific languages (`language:SQL`). Searches can also contain certain [boolean qualifiers](https://help.github.com/en/github/searching-for-information-on-github/understanding-the-search-syntax) like `NOT` and `>`. 

Knowing the rules of GitHub code search enables us to craft search dorks: queries that are designed to find sensitive information. GitHub dorks can be found online, but the best dorks are the ones that you create yourself.

For example, `filename: vim_settings.xml` ([try it!](https://github.com/search?q=filename%3Avim_settings.xml&type=Code)) targets [IntelliJ settings files](https://www.jetbrains.com/help/idea/settings-tools-settings-repository.html). Interestingly, the `vim_settings.xml` file contains recent **copy-pasted strings encoded in Base64**. I recently made $2400 from a bug bounty with this dork: SaaS API keys and customer information were exposed in `vim_settings.xml`.

![](../content/images/2020/05/vim_settings.png)

`vim_settings.xml` only contains recently copy-pasted strings, but we can exploit the repository's commit history to find the **entire copy-paste history.** Just clone the repository and run [this 14-line script](https://gist.github.com/tillson/620e8ef87bc057f25b0a27c423433fda), and the user's activity will be at your fingertips. GitHound also finds and scans base64 encoded strings for secrets, even in commit history.

By the way: with [a GitHub commit search dork](https://github.com/search?q=%22vim_settings.xml%22&type=Commits), we can quickly scan all 500,000 of commits that edit `vim_settings.xml`.

![](../content/images/2020/05/commits.png)

## Search Heuristics for Bug Bounty Hunters

GitHub dorks broadly find sensitive information, but**what if we want to look for information about a specific company?** GitHub has millions of repositories and even more files, so we'll need some heuristics to narrow down the search space. 

To start finding sensitive information, identify a target. 

I've found that the best way to start is to **find domains or subdomains that identify corporate infrastructure.**

Searching for `company.com` probably won't provide useful results: many companies release audited open-source projects that aren't likely to contain secrets. Less-used domains and subdomains are more interesting. This includes specific hosts like `jira.company.com` as well as more general second-level and lower-level domains. It's more efficient to find a pattern than a single domain: `corp.somecompany.com`, `somecompany.net`, or `companycorp.com` are more likely to appear only in an employee's configuration files. 

The usual suspects for open-source intelligence and domain reconnaissance help here:

  * [Subbrute](https://github.com/TheRook/subbrute) \- Python tool for brute-forcing subdomains
  * [ThreatCrowd](https://www.threatcrowd.org/) \- Given a domain, find associated domains through multiple OSINT techniques
  * [Censys.io](https://censys.io/) \- Given a domain, find SSL certificates using it

GitHound can help with subdomain discovery too: add a custom regex `\.company\.com` and run GitHound with the `--regex-file` flag.

After finding a host or pattern to search, play around on GitHub search with it (I always do this before using automated tools). There are a few questions I like to ask myself here:

  1. **How many results came up?** If there are over 100 pages, I'll likely need to find a better query to start with (GitHub limits code search results to 100 pages).
  2. **What kind of results came up?** If the results are mostly (intentionally) open-source projects and people using public APIs, then I may be able to refine the search to eliminate those.
  3. **What happens if I change the language?** `language:Shell` and `language:SQL` may have interesting results.
  4. **Do these results reveal any other domains or hosts?** Results in the first few pages will often include a reference to another domain (e.g. searching for `jira.uber.com` may reveal the existence of another domain entirely, like `uberinternal.com`).

I spend most of my time in this step.

It's crucial that the search space is well-defined and accurate. Automated tools and manual searching will be faster and more accurate with the proper query.

Once I find results that seem interesting based on the criteria above, I run it through [GitHound](https://github.com/tillson/git-hound) with `--dig-files` and `--dig-commits` to look the entire repository and its history. 

`echo "uberinternal.com" | ./git-hound --dig-files --dig-commits`

`echo "uber.com" | ./git-hound --dig-files --language-file languages.txt --dig-commits`

`echo "uber.box.net" | ./git-hound --dig-files --dig-commits`

GitHound also locates interesting files that simply searching won't find, like `.zip` or `.xlsx` files. Importantly, I also manually go through results since automated tools often miss customer information, sensitive code, and username/password combinations. Oftentimes, this will reveal more subdomains or other interesting patterns that will give me ideas for more search queries. It's important to remember that open-source intelligence is a recursive process.

This process almost always finds results. Leaks usually fall into one of these categories (ranked from most to least impactful):

  1. **SaaS API keys** \- Companies rarely impose IP restrictions on APIs. AWS, Slack, Google, and other API keys are liquid gold. These are usually found in config files, bash history files, and scripts.
  2. **Server/database credentials** \- These are usually behind a firewall, so they're less impactful. Usually found in config files, bash history files, and scripts.
  3. **Customer/employee information** \- These hide in XLSX, CSV, and XML files and range from emails all the way to billing information and employee performance reviews.
  4. **Data science scripts** \- SQL queries, R scripts, and Jupyter projects can reveal sensitive information. These repos also tend to have "test data" files hanging around.
  5. **Hostnames/metadata** \- The most common result. Most companies don't consider this a vulnerability, but they can help refine future searches

## Workflow for Specific API Providers

Dorks can also be created to target specific API providers and their endpoints. This is especially useful for companies creating automated checks for their users' API keys. With knowledge of an API key's **context** and **syntax** , the search space can be significantly reduced. 

With knowledge of the specific API provider, we can obtain all of the keys that match the API provider's regex and are in an API call context and then we can check them for validity using an internal database or an API endpoint. 

![](../content/images/2020/05/graph.png)A workflow for finding secrets for a single API provider

For example, suppose a company (HalCorp) provides an API for users to read and write to their account. By making our own HalCorp account, we discover that API keys are in the form `[a-f]{4}-[a-f]{4}-[a-f]{4}`. 
  
  
  # Python
  import halapi
  api = halapi.API()
  api.authenticate_by_key('REDACTED')
  
  # REST API with curl
  curl -X POST -H "HALCorp-Key: REDACTED" https://api.halcorp.biz/userinfo
  

Armed with this information, we can compose our own GitHub dorks for HalCorp API responses: 
  
  
  # Python
  "authenticate_by_key" "halapi" language:python
  
  # REST API
  "HALCorp-Key"
  

With a tool like [GitHound](https://github.com/tillson/git-hound), we can use regex matching to find strings that match the API key's regex and output them to a file:

`echo "HALCorp-Key" | git-hound --dig-files --dig-commits --many-results --regex-file halcorp-api-keys.txt --results-only > api_tokens.txt `

Now that we have a file containing potential API tokens, and we can check these against a database for validity (**do not do this if you don't have written permission from the API provider**).

In the case of HalCorp, we can write a bash script that reads from stdin, checks the `api.halcorp.biz/userinfo` endpoint, and outputs the response.

`cat api_tokens.txt | bash checktoken.bash`

## Remediation

Although awareness of secret exposure on GitHub has increased, more and more sensitive data are published each day. 

Amazon Web Services have begun [notifying users if their API keys are posted online](https://aws.amazon.com/blogs/security/how-to-receive-notifications-when-your-aws-accounts-root-access-keys-are-used/). GitHub has added [security features](https://github.com/features/security) that scan public repositories for common keys. These solutions are merely bandaids, however. To limit secret leaks from source code, we must update API frameworks and DevOps methodologies to prevent API keys from being stored in Git/SVN repositories entirely. Software like [Vault](https://www.vaultproject.io/) safely stores production keys and some API providers, like Google Cloud Platform, have updated their libraries to force API keys to be stored in a file by default.

Fully eradicating exposure of sensitive information is a more difficult problem: how can customer information be fully detected? What if it's in a Word, Excel, or compiled file? More research must be conducted in this field to study the extent of the problem and its solution.

![Tillson Galloway](../content/images/2018/12/Zyq6A600_400x400.jpg)

#### [Tillson Galloway](../author/tillson/index.html)

Georgia Tech '22, iOS and Web developer, Information Security enthusiast 

[Read More](../author/tillson/index.html)

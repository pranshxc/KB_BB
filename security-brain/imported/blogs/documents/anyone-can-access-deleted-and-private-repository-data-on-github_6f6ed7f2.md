---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-24_anyone-can-access-deleted-and-private-repository-data-on-github.md
original_filename: 2024-07-24_anyone-can-access-deleted-and-private-repository-data-on-github.md
title: Anyone can Access Deleted and Private Repository Data on GitHub
category: documents
detected_topics:
- api-security
- idor
- cloud-security
- supply-chain
- command-injection
- otp
tags:
- imported
- documents
- api-security
- idor
- cloud-security
- supply-chain
- command-injection
- otp
language: en
raw_sha256: 6f6ed7f2040e6e99b6e8acb6a5fbcfe295a1d9132706612a4ea096ebd3e0d7f0
text_sha256: 6e311e59fb72602bfe99590a6ba7272e8ed95bde80e0bf1b3fa58c473d76c471
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Anyone can Access Deleted and Private Repository Data on GitHub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-24_anyone-can-access-deleted-and-private-repository-data-on-github.md
- Source Type: markdown
- Detected Topics: api-security, idor, cloud-security, supply-chain, command-injection, otp
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `6f6ed7f2040e6e99b6e8acb6a5fbcfe295a1d9132706612a4ea096ebd3e0d7f0`
- Text SHA256: `6e311e59fb72602bfe99590a6ba7272e8ed95bde80e0bf1b3fa58c473d76c471`


## Content

---
title: "Anyone can Access Deleted and Private Repository Data on GitHub"
page_title: "Anyone can Access Deleted and Private Repository Data on GitHub ◆ Truffle Security Co."
url: "https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github"
final_url: "https://trufflesecurity.com/blog/anyone-can-access-deleted-and-private-repo-data-github"
authors: ["Joe Leon (@JoeLeonJr)"]
programs: ["GitHub"]
bugs: ["Cross Fork Object Reference (CFOR)"]
publication_date: "2024-07-24"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 141
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

July 24, 2024

# Anyone can Access Deleted and Private Repository Data on GitHub

# Anyone can Access Deleted and Private Repository Data on GitHub

Joe Leon

July 24, 2024

 _Note: Open source TruffleHog can now discover all of these commits, see our follow-up post:_[_https://trufflesecurity.com/blog/trufflehog-now-finds-all-deleted-and-private-commits-on-github_](https://trufflesecurity.com/blog/trufflehog-now-finds-all-deleted-and-private-commits-on-github)

  

You can access data from _deleted forks_ , _deleted repositories_ and even _private repositories_ on GitHub. And it is available forever. This is known by GitHub, and intentionally designed that way. 

This is such an enormous attack vector for all organizations that use GitHub that we’re introducing a new term: **Cross Fork Object Reference (CFOR)**. A CFOR vulnerability occurs when one repository fork can access sensitive data from another fork (including data from private and deleted forks). Similar to an Insecure Direct Object Reference, in CFOR users supply commit hashes to directly access commit data that otherwise would not be visible to them. 

Let’s see a few examples.

## Accessing Deleted Fork Data

Consider this common workflow on GitHub: 

  1. You fork a public repository

  2. You commit code to your fork

  3. You delete your fork

![](https://framerusercontent.com/images/msknWhH1EkTt7PchLIRCt3npCI.png?width=2723&height=1646)

Is the code you committed to the fork still accessible? It shouldn’t be, right? You deleted it.

It is. And it’s accessible forever. Out of your control. 

In the video below, you’ll see us fork a repository, commit data to it, delete the fork, and then access the “deleted” commit data via the original repository.

  

  

**You might think you’re protected by needing to know the commit hash. You’re not. The hash is discoverable. More on that later.**

#### How often can we find data from deleted forks?

Pretty often. We surveyed a few (literally 3) commonly-forked public repositories from a large AI company and easily found 40 valid API keys from deleted forks. The user pattern seemed to be this:

  1. Fork the repo.

  2. Hard-code an API key into an example file. 

  3. <Do Work>

  4. Delete the fork.

  

![](https://framerusercontent.com/images/CIeHAgW971XDzRy61aiZjY8fBqE.png?width=2394&height=1102)

  

**But this gets worse, it works in reverse too:**

## Accessing Deleted Repo Data

Consider this scenario:

  1. You have a public repo on GitHub.

  2. A user forks your repo.

  3. You commit data after they fork it (and they never sync their fork with your updates).

  4. You delete the entire repo.

  

![](https://framerusercontent.com/images/A7rA45DJNYSMUEPCF6tj4wilVC0.png?width=2647&height=1590)

Is the code you committed after they forked your repo still accessible?

Yep.

GitHub stores repositories and forks in a [repository network](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks#about-visibility-of-forks), with the original “upstream” repository acting as the root node. [When a public “upstream” repository that has been forked is “deleted”, GitHub reassigns the root node role to one of the downstream forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility#deleting-a-public-repository). However, all of the commits from the “upstream” repository still exist and are accessible via any fork.

  

![](https://framerusercontent.com/images/jCEeyZLP33ugahiS5Oc3N9ms.png?width=3686&height=2324)

  

In the video below, we create a repo, fork it and then show how data not synced with the fork can still be accessed by the fork after the original repo is deleted.

  

  

This isn’t just some weird edge case scenario. This unfolded last week:

_I submitted a P1 vulnerability to a major tech company showing they accidentally committed a private key for an employee’s GitHub account that had significant access to their entire GitHub organization. They immediately deleted the repository, but since it had been forked, I could still access the commit containing the sensitive data via a fork, despite the fork never syncing with the original “upstream” repository._

The implication here is that any code committed to a public repository may be accessible _forever_ as long as there is at least one fork of that repository.

**It gets worse.**

## Accessing Private Repo Data

Consider this common workflow for open-sourcing a new tool on GitHub:

  1. You create a private repo that will eventually be made public.

  2. You create a private, internal version of that repo (via forking) and commit additional code for features that you’re not going to make public.

  3. You make your “upstream” repository public and keep your fork private.

![](https://framerusercontent.com/images/xImmfuPpiSy9ttCvAMC5G46bGSk.png?width=2481&height=1590)

Are your private features and related code (from step 2) viewable by the public?

Yes. Any code committed between the time you created an internal fork of your tool and when you open-sourced the tool, those commits are accessible on the public repository. 

Any commits made to your private fork _after_ you make the “upstream” repository public are not viewable. That’s because changing the visibility of a private “upstream” repository results in two repository networks - one for the private version, and one for the public version. 

  

![](https://framerusercontent.com/images/zOeORJBOu7eK4cx0y2qdgtXNW4.png?width=3921&height=2000)

In the video below, we demonstrate how organizations open-source new tools while maintaining private internal forks, and then show how someone could access commit data from the private internal version via the public one.

  

  

Unfortunately, this workflow is one of the most common approaches users and organizations take to developing open-source software. As a result, it’s possible that confidential data and secrets are inadvertently being exposed on an organization's public GitHub repositories.

  

## How do you actually access the data?

By directly accessing the commit.

Destructive actions in GitHub’s repository network (like the 3 scenarios mentioned above) remove references to commit data from the standard GitHub UI and normal git operations. However, this data still exists and is accessible (if you know the commit hash). This is the tie-in between CFOR and IDOR vulnerabilities - if you know the commit hash you can directly access data that is not intended for you.

Commit hashes are SHA-1 values.

  

![](https://framerusercontent.com/images/EoVCvCLjHvZJCuMrrZ0ZwQd3W8M.png?width=2322&height=602)

  

If a user knows the SHA-1 commit hash of a particular commit they want to see, they can directly navigate to that commit at the endpoint: https://github.com`/<user/org>/<repo>/commit/<commit_hash>`. They’ll see a yellow banner explaining that “[t]his commit does not belong to any branch of this repository, and may belong to a fork outside of the repository.”

  

![](https://framerusercontent.com/images/B0wRJU4mjHvmKdy7mpZ3Z3wRV8.png?width=2324&height=1410)

  

**Where do you get these hash values?**

Commit hashes can be brute forced through GitHub’s UI, particularly because the git protocol permits the use of [short SHA-1 values](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#:~:text=to%20any%20commit.-,Short%20SHA%2D1,-Git%20is%20smart) when referencing a commit. A short SHA-1 value is the minimum number of characters required to avoid a collision with another commit hash, with an absolute minimum of 4. The keyspace of all 4 character SHA-1 values is 65,536 (16^4). Brute forcing all possible values can be achieved relatively easily. 

For example, consider this commit in TruffleHog’s repository:

  

![](https://framerusercontent.com/images/yPbRdgv9LoasW1BXLK09dZNMSXs.png?width=2320&height=1098)

  

To access this commit, users typically visit the URL containing the full SHA-1 commit hash: <https://github.com/trufflesecurity/trufflehog/commit/07f01e8337c1073d2c45bb12d688170fcd44c637>

But users don’t need to know the entire 32 character SHA-1 value, they only need to correctly guess the Short SHA-1 value, which in this case is `07f01e`.

  

![](https://framerusercontent.com/images/jji5JQSyL5Bh0OJtpMQDB65DE.png?width=2326&height=1324)

<https://github.com/trufflesecurity/trufflehog/commit/07f01e>

But what’s more interesting; GitHub exposes a public events API endpoint. You can also query for commit hashes in the [events archive](https://www.gharchive.org/) which is managed by a 3rd party, and saves all GitHub events for the past decade outside of GitHub, even after the repos get deleted.

## GitHub’s Policies

We recently submitted our findings to GitHub via their VDP program. This was their response:

  

![](https://framerusercontent.com/images/G9xGKRx7gPHauxianQClKVxPE.png?width=1874&height=314)

  

After reviewing the documentation, it’s clear as day that GitHub designed repositories to work like this. 

  

![](https://framerusercontent.com/images/eE6IuZrodHY2R0pBWcGHKPNxI.png?width=2312&height=1270)

  

![](https://framerusercontent.com/images/UpywoiGAzxzDtqcMAzLxKeW6dwQ.png?width=2318&height=612)

<https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility>

We appreciate that GitHub is transparent about their architecture and has taken the time to clearly document what users should expect to happen in the instances documented above. 

Our issue is this:

The average user views the separation of private and public repositories as a security boundary, and understandably believes that any data located in a private repository cannot be accessed by public users. Unfortunately, as we documented above, that is not always true. Whatsmore, the act of deletion implies the destruction of data. As we saw above, deleting a repository or fork does not mean your commit data is actually deleted.

## Implications

We have a few takeaways from this:

  1. **As long as one fork exists, any commit to that repository network (ie: commits on the “upstream” repo or “downstream” forks) will exist forever.**

  1. This further cements our view that the only way to securely remediate a leaked key on a public GitHub repository is through key rotation. We’ve spent a lot of time documenting how to rotate keys for the most popularly leaked secret types - check our work out here: [howtorotate.com](https://howtorotate.com/docs/introduction/getting-started/).

  2. GitHub’s repository architecture necessitates these design flaws and unfortunately, the vast **majority of GitHub users will never understand how a repository network actually works and will be less secure** because of it.

  3. As secret scanning evolves, and we can hopefully scan all commits in a repository network, **we’ll be alerting on secrets that might not be our own** (ie: they might belong to someone who forked a repository). This will require more diligent triaging.

  

  4. While these three scenarios are shocking, that doesn’t even cover all of the ways GitHub could be storing deleted data from your repositories. Check out our [recent post](https://trufflesecurity.com/blog/trufflehog-scans-deleted-git-branches) (and related TruffleHog update) about how you also need to scan for secrets in deleted branches. 

Finally, while our research focused on GitHub, it’s important to note that some of these issues exist on other version control system products.

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

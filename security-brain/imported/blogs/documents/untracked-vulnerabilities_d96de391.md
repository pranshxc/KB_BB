---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-13_some-vulnerabilities-dont-have-a-name.md
original_filename: 2022-10-13_some-vulnerabilities-dont-have-a-name.md
title: '## Untracked Vulnerabilities'
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: d96de391e8241a6059669e8aef7da04f99d589a2bf375932b6b8c810666ce547
text_sha256: 0cb258e822f0d98d51bd9ecaccef98bd62ebff2346ba834aa9e69329592db9ea
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# ## Untracked Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-13_some-vulnerabilities-dont-have-a-name.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `d96de391e8241a6059669e8aef7da04f99d589a2bf375932b6b8c810666ce547`
- Text SHA256: `0cb258e822f0d98d51bd9ecaccef98bd62ebff2346ba834aa9e69329592db9ea`


## Content

---
title: "Some Vulnerabilities Don’t Have A Name"
page_title: "Some Vulnerabilities Dont Have a Name - Checkmarx.com"
url: "https://checkmarx.com/blog/some-vulnerabilities-dont-have-a-name/"
final_url: "https://checkmarx.com/blog/some-vulnerabilities-dont-have-a-name/"
authors: ["Mario Teixeira", "Bruno Dias"]
programs: ["Node.js third-party modules (debug)"]
bugs: ["ReDoS", "Memory leak"]
publication_date: "2022-10-13"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2046
---

## Untracked Vulnerabilities

There is a common assumption that all open-source vulnerabilities hold a [CVE](https://cve.org/ResourcesSupport/FAQs). Still, others believe that the National Vulnerability Database ([NVD](https://nvd.nist.gov/)) has the final word when deciding what is a vulnerability and what is not. However, can a vulnerability exist that isn’t tracked by a CVE, or is not in the NVD?

NVD is the top reference, that’s irrefutable. It’s why those of us on the Checkmarx SCA research team use NVD as our main source of vulnerability information. However, we’ve also [explained previously](https://checkmarx.com/blog/sca-behind-the-curtains/) how NVD’s data is often not enough. Moreover, NVD relies on various AppSec authorities and maintainers to maintain a comprehensive database of vulnerabilities.

In that sense, we must pursue other sources to increase the magnitude of the vulnerability coverage within our SCA solution. To every vulnerability that isn’t present in the NVD, and hence, doesn’t have a CVE, we call them an “Untracked Vulnerability.”

## Our Challenges

Tracked or not, an exploitable vulnerability in your code can become a gateway to your application being compromised. And like the dark side of the moon that we can’t see, we simply know it’s there. These two assumptions are where the real risk resides.

However, researching untracked vulnerabilities is a process that come with some challenges that we need to tackle. The most prominent are:

  * Untracked vulnerabilities usually have less information available than ones that are tracked. Which means it requires more difficult research to cover the vulnerability.
  * The fact that they aren’t validated by a trusted authority requires more work on our part to measure and validate the risk as well. Sometimes, we even need POCs (Proof of Concept) to prove that a vulnerability exists.

Both challenges are always present, yet a third challenge arises from time to time. It is common for Untracked Vulnerabilities to be unfixed and they may affect the latest versions of popular packages. So sometimes we must exhume vulnerabilities we’ve covered before and confirm if the research and information about them is still accurate.

Recently, we had to validate two of these vulnerabilities in the NPM package “debug.” The “debug” package is one of the most popular packages on NPM with hundreds of millions of weekly downloads—one more reason to perform our research as thoroughly as possible.

## Memory Leak in “debug”

**Confirming the vulnerability**

One of the vulnerabilities was a Memory Leak, and the starting point was [this issue](https://github.com/debug-js/debug/issues/678). It wasn’t mentioned anywhere else, and there was no CVE nor any info about this on NVD. So, we knew we would have to research this issue as an Untracked Vulnerability.

**Where could the issue lead us?**

When the information about an issue is limited, we must analyze everything from the beginning, and every crumb of information can add up to something. There are references to other issues, commits, etc., in addition to comments that might hold essential information. We must also look for leads on the old analysis that could indicate a misunderstanding or anything that went unnoticed.

A vigilant journey through the comments showed us how the vulnerability went from being exposed to fixed, and along the way, we gathered enough information to trust the validity of the vulnerability and its fix. There was proof in the comments (including answers from the maintainer) and a fix commit. Still, we analyzed the code thoroughly and ran our tools to confirm this.

But at this point, it wouldn’t suffice to completely trust the issue was fixed. We would have to reproduce the vulnerability and finally extinguish any doubt.

**Proof of Concept (POC)**

We know that a memory leak implies that memory that is no longer needed isn’t being freed correctly. In the cybersecurity jargon, it means that the memory will keep on accumulating until something crashes, thus, if intentional, leading to a Denial of Service (DoS).

That was precisely the situation here, and all it required was to instantiate “debug” in a loop.

That’s what we did using a public POC. One look at the CPU usage and the picture was clear. We could see the memory growing, bit by bit, and it was even clearer after running more instances of the POC. But we needed to make it better to showcase, so we made our own POC. Everything went the same, except that we made it easier to visualize the vulnerability and its results.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

The only thing that was left was to confirm our previous conclusions regarding the versions. So, we ran the POC for the latest vulnerable version and some of the older ones, only to confirm what we already knew. At last, running it for the first fixed versions and the latest one showed that the vulnerability was indeed fixed.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

## ReDoS in “debug”

**Confirming the vulnerability**

The other vulnerability was a Regular Expression Denial of Service, aka, ReDoS. We found it through [this issue](https://github.com/debug-js/debug/issues/737).  
  
We saw that the issue was open and there was no fix yet. And from the comments we confirmed it was indeed a vulnerability. Hum… an unfixed vulnerability? The person reporting the issue had neatly described the problem and affected code, and the maintainer agreed that it should be handled. However, it was planned to be fixed in a later version.

Nonetheless, we had to reproduce it and create proof that the vulnerability exists.

**Proof of Concept (POC)**

To begin with, the POC was also easy because we already had info about the affected components. We needed to call the `enable()` function and give it the regex. However, there was a challenge.

To summarize, a ReDoS happens when an application accepts regular expressions as input, but it does not validate catastrophic exponential-time regular expressions. Thus, we had to craft a specific malicious regex that would break it and cause the Denial of Service in the application. So that is what we did.

We used the regex `(a+)+`, which searches for the letter “a” and its repetition, and checks if the entire expression is repeating. If we then supplied something like `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX` as input, we could see the application hanging and running for an undetermined amount of time. This is because each “a” causes the regex function to check for the repetition of an additional expression, thus doubling the amount of processing time, and then, by having something other than an “a” in the end, it causes catastrophic backtracking. Mission accomplished!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Finally, we ran the POC for some earlier versions and for the latest released version, to confirm that the vulnerability was indeed not fixed – all the versions were vulnerable and could easily be exploited.

## Last words

As we’ve shown in this blog, Untracked Vulnerabilities are vulnerabilities nevertheless, and they must never be underestimated. We will keep working towards increasing our coverage of these Untracked Vulnerabilities since they are a surplus to our customers, and are as critical to security, if not sometimes more critical, than the tracked vulnerabilities.

The SCA research team continues to cover both tracked and untracked vulnerabilities with the same due care. You can learn more about Checkmarx SCA [here](https://checkmarx.com/cxsca-open-source-scanning/).

Tags:

Application Security Testing

AppSec

Article

Developer

English

Open-Source Security

SCA

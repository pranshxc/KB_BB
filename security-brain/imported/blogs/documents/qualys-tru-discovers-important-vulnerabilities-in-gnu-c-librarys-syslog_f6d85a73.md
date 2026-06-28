---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-30_qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog.md
original_filename: 2024-01-30_qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog.md
title: Qualys TRU Discovers Important Vulnerabilities in GNU C Library’s syslog()
category: documents
detected_topics:
- sso
- access-control
- command-injection
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- sso
- access-control
- command-injection
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: f6d85a739c33d47d7da63f89e337bb84c92d901e08112d95bd080db976e2040c
text_sha256: 1a23eb98fc293f2259957f84794b35071b5ed9e9b35029610ffe9dd5006e9aa1
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Qualys TRU Discovers Important Vulnerabilities in GNU C Library’s syslog()

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-30_qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `f6d85a739c33d47d7da63f89e337bb84c92d901e08112d95bd080db976e2040c`
- Text SHA256: `1a23eb98fc293f2259957f84794b35071b5ed9e9b35029610ffe9dd5006e9aa1`


## Content

---
title: "Qualys TRU Discovers Important Vulnerabilities in GNU C Library’s syslog()"
page_title: "Qualys TRU Discovers Important Vulnerabilities in GNU C Library’s syslog() | Qualys"
url: "https://blog.qualys.com/vulnerabilities-threat-research/2024/01/30/qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog"
final_url: "https://blog.qualys.com/vulnerabilities-threat-research/2024/01/30/qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog"
authors: ["Qualys Threat Research Unit (TRU)"]
programs: ["GNU C Library (glibc)"]
bugs: ["Memory corruption", "Integer overflow", "Heap buffer overflow", "Security code review"]
publication_date: "2024-01-30"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 481
---

# Qualys TRU Discovers Important Vulnerabilities in GNU C Library’s syslog()

![Saeed Abbasi](https://secure.gravatar.com/avatar/507a7837d5c29597d1f47426a71191e3459085683ce5074571c0de98f7c48aab?s=110&d=mm&r=g)

[Saeed Abbasi](https://blog.qualys.com/author/sabbasi), Director of Product, Head of Threat Research Unit (TRU), Qualys

[February 1, 2024](https://blog.qualys.com/vulnerabilities-threat-research/2024/01/30/qualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog) \- 8 min read 

Share

  * [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog "Share on LinkedIn")
  * [](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog "Share on Facebook")
  * [](https://twitter.com/share?url=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog&text=Qualys%20TRU%20Discovers%20Important%20Vulnerabilities%20in%20GNU%20C%20Library%E2%80%99s%20syslog%28%29&via=qualys "Share on X")
  * [](mailto:?body=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog&subject=Qualys%20TRU%20Discovers%20Important%20Vulnerabilities%20in%20GNU%20C%20Library%E2%80%99s%20syslog%28%29 "Send by email")

#### Table of Contents

  * Vulnerabilities in GNU C Library:
  * Heap-Based Buffer Overflow in __vsyslog_internal() Function (CVE-2023-6246):
  * Memory Corruption in qsort() Function:
  * Qualys QID Coverage:
  * Enhance Your Security Posture with Qualys Vulnerability Management, Detection, and Response (VMDR)
  * Discover Vulnerable Assets Using Qualys CyberSecurity Asset Management (CSAM)
  * Disclosure Timeline for CVE-2023-6246, CVE-2023-6779 and CVE-2023-6780
  * Disclosure Timeline for Out-of-bounds read & write in glibcs qsort()
  * Technical Details

The [Qualys Threat Research Unit (TRU)](https://www.qualys.com/tru/) has recently unearthed four significant vulnerabilities in the GNU C Library, a cornerstone for countless applications in the Linux environment.

Before diving into the specific details of the vulnerabilities discovered by the Qualys Threat Research Unit in the GNU C Library, it’s crucial to understand these findings’ broader impact and importance. The GNU C Library, or glibc, is an essential component of virtually every Linux-based system, serving as the core interface between applications and the Linux kernel. The recent discovery of these vulnerabilities is not just a technical concern but a matter of widespread security implications.

The vulnerabilities identified in glibc’s syslog and qsort functions highlight a critical aspect of software security: even the most foundational and trusted components are not immune to flaws. The ramifications of these vulnerabilities extend far beyond individual systems, affecting many applications and potentially millions of users worldwide. This article aims to shed light on the specific nature of these vulnerabilities, their potential impacts, and the steps taken to mitigate them.

For the first vulnerability (CVE-2023-6246), a significant security flaw has been identified in the GNU C Library’s __vsyslog_internal() function, affecting syslog() and vsyslog(). This heap-based buffer overflow vulnerability was inadvertently introduced in glibc 2.37 (August 2022) and subsequently backported to glibc 2.36 while addressing a different, less severe vulnerability (CVE-2022-39046). Major Linux distributions like Debian (versions 12 and 13), Ubuntu (23.04 and 23.10), and Fedora (37 to 39) are confirmed to be vulnerable. This flaw allows local privilege escalation, enabling an unprivileged user to gain full root access, as demonstrated in Fedora 38.

In our analysis of the same function affected by CVE-2023-6246, we identified two additional, albeit minor, vulnerabilities:

  1. CVE-2023-6779 (glibc): This vulnerability involves an off-by-one heap-based buffer overflow in the __vsyslog_internal() function.
  2. CVE-2023-6780 (glibc): This is an integer overflow issue in the __vsyslog_internal() function.

Based on our assessment, triggering these vulnerabilities appears more challenging than CVE-2023-6246. Additionally, exploiting them effectively is likely to be more complex.

Moving on to the last vulnerability, a memory corruption issue was found in the GNU C Library’s qsort () function, caused by missing bounds check. This vulnerability can be triggered when qsort() is used with a nontransitive comparison function (such as cmp(int a, int b) returning (a – b)) and a large number of elements controlled by an attacker, potentially leading to a malloc() failure.

## **Vulnerabilities in GNU C Library:**

The discovery of vulnerabilities in the GNU C Library’s syslog and qsort functions raises major security concerns. The syslog vulnerability, a heap-based buffer overflow, can allow local users to gain full root access, impacting major Linux distributions. Similarly, the qsort vulnerability, stemming from a missing bounds check, can lead to memory corruption and has affected all glibc versions since 1992. These flaws highlight the critical need for strict security measures in software development, especially for core libraries widely used across many systems and applications.

## **Heap-Based Buffer Overflow in __vsyslog_internal() Function (CVE-2023-6246):**

This vulnerability identified is a heap-based buffer overflow within the __vsyslog_internal() function of the GNU C Library, also known as glibc. This critical function underpins the widely-used syslog() and vsyslog() functions. The buffer overflow issue, traced back to the introduction of glibc version 2.37, poses a significant threat as it could allow local privilege escalation, enabling an unprivileged user to gain full root access through crafted inputs to applications that employ these logging functions. Although the vulnerability requires specific conditions to be exploited (such as an unusually long argv[0] or openlog() ident argument), its impact is significant due to the widespread use of the affected library. Interestingly, a similar issue was reported in December 1997 in an older Linux libc version.

## **Memory Corruption in qsort() Function:**

The second vulnerability involves a subtle yet dangerous flaw in glibc’s qsort() function. This issue arises from a missing bounds check, leading to memory corruption. For an application to be vulnerable, it must utilize the qsort() function with a specific set of criteria: a nontransitive comparison function (such as a simple cmp(int a, int b) returning (a – b)) and a substantial number of elements controlled by an attacker. This scenario could result in a malloc() failure within qsort(), opening the door for exploitation.

However, real-world examples of vulnerable programs have not been identified. This issue affects all versions of glibc from September 1992 (version 1.04) to the latest release (version 2.38). The glibc developers have already addressed this problem in a recent update, following an independent discovery during a refactoring of qsort(). The glibc security team clarified that the vulnerability arises from applications using non-transitive comparison functions, which are not compliant with POSIX and ISO C standards.

## **Qualys QID Coverage:**

We will share the details of the various QIDs associated with this vulnerability as soon as they become available. More details will be updated following its release.

QID| Title| Version| Supported On  
---|---|---|---  
379329| GNU C Library Multiple Vulnerabilities| VULNSIGS-2.5.972-3 | Scanner + Agent + CS Sensor  
6000458| Debian Security Update for glibc (DSA 5611-1)| VULNSIGS-2.5.973-2| Scanner + Agent + CS Sensor  
  
Additional QIDs will be released for these vulnerabilities as Linux distributions release their backported fixes. Please refer to the QID Knowledgebase for a complete list of coverage regarding this vulnerability.

## **Enhance Your Security Posture with Qualys Vulnerability Management, Detection, and Response (VMDR)**

[Qualys VMDR](https://www.qualys.com/apps/vulnerability-management-detection-response/) offers comprehensive coverage and visibility into vulnerabilities, empowering organizations to rapidly respond, prioritize, and mitigate the associated risks.

Leverage the power of Qualys VMDR alongside TruRisk and the Qualys Query Language (QQL) to efficiently identify and prioritize vulnerable assets, effectively addressing the vulnerabilities highlighted above.

Use this QQL statement:

vulnerabilities.vulnerability.cveIds:CVE-2023-6246

[![](https://ik.imagekit.io/qualys/wp-content/uploads/2024/01/vmdr-patch-1070x488.png)](https://ik.imagekit.io/qualys/wp-content/uploads/2024/01/vmdr-patch.png)

## **Discover Vulnerable Assets Using Qualys CyberSecurity Asset Management (CSAM)**

The initial and crucial step in managing this critical vulnerability and mitigating associated risks involves pinpointing all assets susceptible to this specific issue. Qualys VMDR facilitates the easy identification of these potentially affected assets. 

In the following example, we aim to identify all assets running the glibc:

Query: software:(name:”glibc”)

[![](https://ik.imagekit.io/qualys/wp-content/uploads/2024/01/Screenshot-2024-01-30-at-10.07.14-AM-1070x488.png)](https://ik.imagekit.io/qualys/wp-content/uploads/2024/01/Screenshot-2024-01-30-at-10.07.14-AM.png)

## **Disclosure Timeline for CVE-****2023-6246, CVE-2023-6779 and CVE-2023-6780**

  * 2023-11-07: We sent a preliminary draft of our advisory to Red Hat Product Security.
  * 2023-11-15: Red Hat Product Security acknowledged receipt of our email.
  * 2023-11-16: Red Hat Product Security asked us if we could share our exploit with them.
  * 2023-11-17: We sent our exploit to Red Hat Product Security.
  * 2023-11-21: Red Hat Product Security confirmed that our exploit worked, and assigned CVE-2023-6246 to this heap-based buffer overflow in __vsyslog_internal().
  * 2023-12-05: Red Hat Product Security sent us a patch for CVE-2023-6246 (written by the glibc developers), and asked us for our feedback.
  * 2023-12-07: While reviewing this patch, we discovered two more minor vulnerabilities in the same function (an off-by-one buffer overflow and an integer overflow). We immediately sent an analysis, proof of concept, and patch proposal to Red Hat Product Security, and suggested that we directly involve the glibc security team.
  * 2023-12-08: Red Hat Product Security acknowledged receipt of our email, and agreed that we should directly involve the glibc security team. We contacted them on the same day, and they immediately replied with very constructive comments.
  * 2023-12-11: The glibc security team suggested that we postpone the coordinated disclosure of all three vulnerabilities until January 2024 (because of the upcoming holiday season). We agreed.
  * 2023-12-13: Red Hat Product Security assigned CVE-2023-6779 to the off-by-one buffer overflow and CVE-2023-6780 to the integer overflow in __vsyslog_internal().
  * 2024-01-04: We suggested either January 23 or January 30 for the Coordinated Release Date of these vulnerabilities. The glibc developers agreed on January 30.
  * 2024-01-12: The glibc developers sent us an updated version of the patches for these vulnerabilities.
  * 2024-01-13: We reviewed these patches and sent our feedback to the glibc developers.
  * 2024-01-15: The glibc developers sent us the final version of the patches for these vulnerabilities.
  * 2024-01-16: We sent these patches and a draft of our advisory to the linux-distros@openwall. They immediately acknowledged receipt of our email.
  * 2024-01-30: Coordinated Release Date (18:00 UTC).

## **Disclosure Timeline for Out-of-bounds read & write in glibc’s qsort()**

  * 2023-12-12: We sent a draft of our advisory to the glibc security team. They immediately acknowledged receipt of our email.
  * 2023-12-19: The glibc security team decided to not treat this memory corruption in qsort() as a vulnerability in the glibc itself, as explained in the “Summary” of our advisory.
  * 2024-01-16: We backported commit b9390ba to all current and past stable versions of the glibc, and sent this patch and a draft of our advisory to the linux-distros@openwall (to piggyback on the glibc embargo for CVE-2023-6246). They immediately acknowledged receipt of our email.
  * 2024-01-30: Coordinated Release Date (18:00 UTC).

## **Technical Details**

You can find the technical details of these vulnerabilities at: 

<https://www.qualys.com/2024/01/30/syslog>  
<https://www.qualys.com/2024/01/30/qsort>

In conclusion, the recent discovery of these significant vulnerabilities in the GNU C Library highlights the security challenges in widely used software components. These vulnerabilities, affecting major Linux distributions, underscore the need for continuous vigilance and prompt updates in software security.

![Saeed Abbasi](https://secure.gravatar.com/avatar/507a7837d5c29597d1f47426a71191e3459085683ce5074571c0de98f7c48aab?s=180&d=mm&r=g)

Written by

[Saeed Abbasi](https://blog.qualys.com/author/sabbasi), Director of Product, Head of Threat Research Unit (TRU), Qualys

Write to Saeed at [sabbasi@qualys.com](mailto:sabbasi@qualys.com)

Like

Share

  * [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog "Share on LinkedIn")
  * [](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog "Share on Facebook")
  * [](https://twitter.com/share?url=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog&text=Qualys%20TRU%20Discovers%20Important%20Vulnerabilities%20in%20GNU%20C%20Library%E2%80%99s%20syslog%28%29&via=qualys "Share on X")
  * [](mailto:?body=https%3A%2F%2Fblog.qualys.com%2Fvulnerabilities-threat-research%2F2024%2F01%2F30%2Fqualys-tru-discovers-important-vulnerabilities-in-gnu-c-librarys-syslog&subject=Qualys%20TRU%20Discovers%20Important%20Vulnerabilities%20in%20GNU%20C%20Library%E2%80%99s%20syslog%28%29 "Send by email")

##### Related content

[CVE-2022-39046](https://blog.qualys.com/tag/cve-2022-39046), [CVE-2023-6246](https://blog.qualys.com/tag/cve-2023-6246), [CVE-2023-6779](https://blog.qualys.com/tag/cve-2023-6779), [CVE-2023-6780](https://blog.qualys.com/tag/cve-2023-6780)

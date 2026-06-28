---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-19_xs-searching-googles-bug-tracker-to-find-out-vulnerable-source-code.md
original_filename: 2018-11-19_xs-searching-googles-bug-tracker-to-find-out-vulnerable-source-code.md
title: XS-Searching Google’s bug tracker to find out vulnerable source code
category: documents
detected_topics:
- command-injection
- automation-abuse
- csrf
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- csrf
- information-disclosure
- api-security
language: en
raw_sha256: 1b07e97e1d24406d5f3fc0aed3d98ec0fcec2ce83734d4412539dc61191ed192
text_sha256: a1f86a8b5a8c7f8d284ebfb450da13891cea48b36314fc90d1e4fa7c3959f77b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XS-Searching Google’s bug tracker to find out vulnerable source code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-19_xs-searching-googles-bug-tracker-to-find-out-vulnerable-source-code.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, csrf, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1b07e97e1d24406d5f3fc0aed3d98ec0fcec2ce83734d4412539dc61191ed192`
- Text SHA256: `a1f86a8b5a8c7f8d284ebfb450da13891cea48b36314fc90d1e4fa7c3959f77b`


## Content

---
title: "XS-Searching Google’s bug tracker to find out vulnerable source code"
url: "https://medium.com/@luanherrera/xs-searching-googles-bug-tracker-to-find-out-vulnerable-source-code-50d8135b7549"
authors: ["Luan Herrera (@lbherrera_)"]
programs: ["Google"]
bugs: ["XS-Search", "Information disclosure"]
bounty: "9,400"
publication_date: "2018-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5573
scraped_via: "browseros"
---

# XS-Searching Google’s bug tracker to find out vulnerable source code

Top highlight

XS-Searching Google’s bug tracker to find out vulnerable source code
Or how side-channel timing attacks aren’t that impractical
Luan Herrera
Follow
6 min read
·
Nov 19, 2018

1.5K

1

Monorail is an open-source issue tracker used by many “Chromium-orbiting” projects, including Monorail itself. Other projects include Angle, PDFium, Gerrit, V8, and the Alliance for Open Media. It is also used by Project Zero, Google’s 0-day bug-finding team.

This article is a detailed explanation of how I could have exploited Google’s Monorail issue tracker to leak sensitive information (vulnerable source code files and line numbers) from private bug reports through a XS-Search attack.

Where to start?

One of the first functionalities I looked into when analyzing Monorail was the ability to download the result of a certain search query as a CSV.

It didn’t take me long to notice that it was vulnerable to a CSRF attack. In other words, it was possible to force an user to download a CSV containing the results of a search query if a malicious link was accessed.

Press enter or click to view image in full size
https://bugs.chromium.org/p/chromium/issues/csv?can=1&q=Restrict=View-SecurityTeam&colspec=ID

As seen in the image, there were no protections against CSRF attacks. So, for example, a request made with the “Restrict-View-SecurityTeam” tag would end up filtering the results to undisclosed security-related issues only. If a member of the Google security team or a high profile bug reporter were to access this link, they would download a CSV containing all undisclosed issues they have access to.

Duplicate and conquer

Another important discovery was that columns displayed in a search result could be duplicated, allowing us to arbitrarily increase the length of the generated CSV.

To illustrate, if we were to access the URL below:

https://bugs.chromium.org/p/chromium/issues/csv?can=1&q=id:51337&colspec=ID+Summary+Summary+Summary

The downloaded CSV would contain 3 repeated Summary columns, instead of only one.

Press enter or click to view image in full size
CSV generated from a query containing the “Summary” column 3 times.
Come again? A XS-Search attack?

Combining these two vulnerabilities we have all that is needed to perform a Cross-Site Search (XS-Search) attack:

Capacity to perform complex search queries.
Capacity to inflate the response of a search query.

The second point is particularly important. If the response of a search query matches a bug, we can make the CSV significantly bigger than a query that doesn’t.

Because of this big difference in response length, it’s possible to calculate the time each request takes to complete and then infer whether the query returned results or not. This way, we achieve the ability to ask cross-origin boolean questions.

The phrase “cross-origin boolean questions” sounds weird, but it essentially means we’re able to ask questions like “is there any private bug that matches the folder `src/third_party/pdfium/`?” and obtain the answer cross-origin. This involves several steps that will be described in the following section.

For now, the examples below demonstrate the core of the issue:

Press enter or click to view image in full size
1st case — CSV generated from query “Summary: This bug exists”.
Press enter or click to view image in full size
2nd case — CSV generated from query “Summary: This bug doesn’t exist”.
Press enter or click to view image in full size
3rd case — CSV generated from query ”Summary: This bug exists OR Summary: This bug doesn’t exist“.

As we can see, on the first and third case we would have an arbitrarily big CSV, because both queries match a bug with summary “This bug exists”. On the second case, the CSV would be empty (containing only the header), because the query didn’t match any bug with the Summary “This bug doesn’t exist”. Note that in the third case we are using the logic operator OR to query the first and second cases together.

To ask or not to ask?

One of the problems I had when trying to create a PoC was deciding what to search. Monorail’s search doesn’t allow us to query for specific letters in a report, only words. This meant that we couldn’t bruteforce the report char by char.

Get Luan Herrera’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After realizing this, I had to take a step back and search older bug reports looking for information that was relevant and could realistically be exfiltrated by the attack.

That’s when I learned that many Chromium bug reports indicate the file path and line number where the vulnerability can be found.

Press enter or click to view image in full size
Example from https://bugs.chromium.org/p/chromium/issues/detail?id=770148

That’s perfect for a XS-Search attack: since the folder structure of Chromium is public and Monorail treats slashes as words delimiters (a query for “path/to/dir” also includes results for bugs containing the string “path/to/dir/sub/dir”), we can easily generate the appropriate search queries.

So our attack would look something like this:

We find out if there’s any private bug report that mentions a file in Chromium’s source tree. We do this using https://cs.chromium.org/chromium/src/ as the base query.
We search for the first half of all the directories under src/ using the OR operator (e.g. src/blink OR src/build…).
We keep repeating step 2 using the binary search algorithm. If anything was found (i.e. a big CSV was generated), we restrict the search space to the first half. Otherwise (i.e., an empty CSV was generated), we restrict the search space to the second half.
After eliminating all directories but one, we restart step 2, but now adding the newly found directory to the end of the base query.

At the end of this process, the full URL will have been leaked and we can now (as an attacker) look into the corresponding file and try to find the vulnerability that was reported.

One request to rule them all

You might be wondering how we obtained the size of the CSV in step 3. Since the Same-Origin policy forbids us from accessing information across different origins, a naive response.length won’t work.

While we can’t know for sure the exact size of a response, we can measure the time each request takes to complete. Using the response-length inflation technique covered in previous sections, searches returning a bug would be a lot slower to finish than ones that do not.

However, to achieve a high degree of certainty, simply doing one request isn’t enough. We would need to request the same page many times and measure the average response time to obtain a reliable exploit.

That’s when the Cache API comes in handy, by only making one request and repeatedly calculating the duration that the response takes to be cached it’s possible to infer, with certainty, if the result of the search query returned bugs or not.

In other words, a small response takes less time to be cached than a bigger response. Given there are almost no limitations to the Cache API (and it being extremely fast), we can cache and measure the same response several times, and then compare it with the measurements of a known empty search query result, which allows us to easily differentiate a large response from a small/empty one, filtering out hardware and network variances, increasing the exploit’s speed and reliability.

For more information on how this can be implemented you can check the exploit’s code.

Aftermath

In total, I found three different places where this attack could be carried on, which resulted in CVE-2018–10099, CVE-2018–19334 and CVE-2018–19335.

I was also rewarded $3133,7 for each vulnerability, totaling over $9400.

Contact

If you have any questions, caught some typo or something that I missed, feel free to contact me on @lbherrera_

References

[1] Commit fixing the CSRF in Monorail’s CSV file download (https://chromium.googlesource.com/infra/infra/+/bdb78934b151ac75bf41711797bbf81130c5a502).

[2] Commit fixing the duplicated columns bug (https://chromium.googlesource.com/infra/infra/+/0ff6b6453b6192987bd9240c1e872a7de5fb1313).

[3] Commit disallowing double grid axes and Cc axis (https://chromium.googlesource.com/infra/infra/+/77ef00cb53d90c9d1f984eca434d828de5c167a5).

[4] Commit preventing request inflation through the groupby parameter (https://chromium.googlesource.com/infra/infra/+/e27936ef82d33a5f286e1f2f22817aa682f79e90).

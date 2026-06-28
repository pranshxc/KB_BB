---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-10_mindshare-when-mysql-cluster-encounters-taint-analysis.md
original_filename: 2022-02-10_mindshare-when-mysql-cluster-encounters-taint-analysis.md
title: 'Mindshare: When Mysql Cluster Encounters Taint Analysis'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: cbf893e79b44797d8275aa4090f9517bff3b12524c781e33ceea55d04f5d1074
text_sha256: ad5b05615d09c9e1f2f76c439742f142d6713d6299aa90006b82abc99debd218
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Mindshare: When Mysql Cluster Encounters Taint Analysis

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-10_mindshare-when-mysql-cluster-encounters-taint-analysis.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `cbf893e79b44797d8275aa4090f9517bff3b12524c781e33ceea55d04f5d1074`
- Text SHA256: `ad5b05615d09c9e1f2f76c439742f142d6713d6299aa90006b82abc99debd218`


## Content

---
title: "Mindshare: When Mysql Cluster Encounters Taint Analysis"
page_title: "Zero Day Initiative — MindShaRE: When MySQL Cluster Encounters Taint Analysis"
url: "https://www.zerodayinitiative.com/blog/2022/2/10/mindshare-when-mysql-cluster-encounters-taint-analysis"
final_url: "https://www.zerodayinitiative.com/blog/2022/2/10/mindshare-when-mysql-cluster-encounters-taint-analysis"
authors: ["Lucas Leong (@_wmliang_)"]
programs: ["Oracle (MySQL)"]
bugs: ["Memory corruption"]
publication_date: "2022-02-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2917
---

# Blog

#  MindShaRE: When MySQL Cluster Encounters Taint Analysis 

__ February 10, 2022

__ Lucas Leong

Recently, the ZDI received multiple submissions of vulnerabilities in [MySQL Cluster](https://www.mysql.com/products/cluster/). MySQL Cluster is a clustering solution providing linear scalability and high availability for the MySQL database management system. The common attack vector identified in these reports is the open port for the cluster management node and data nodes. Attackers can utilize the protocol and interact with nodes without authentication.

After investigating these submissions, I realized that the code is very buggy, and the pattern of the vulnerabilities is simple. However, the codebase is too large for a manual review. Therefore, the question becomes, “Is it possible to identify all low-hanging-fruit bugs automatically and quickly?” Fuzzing works, but it depends on coverage and cannot precisely focus on a specific type of bug. Taint analysis is probably the more suitable answer for this question.

Two tools are chosen for taint analysis: Clang Static Analyzer and CodeQL. Although they have their own pros and cons, both can lead to positive results. This blog looks at both methods and shows how they can be used for taint analysis against this and other programs.

**The Target**

Here is an example of the kind of low-hanging-fruit bug we are looking for:

The `Qmgr::execCM_REGREF` function is a registered signal of the QMGR [NDB kernel block](https://dev.mysql.com/doc/ndb-internals/en/ndb-internals-kernel-blocks.html). These registered signals can be invoked remotely. The `signal->getDataPtr()` at (1) returns a pointer to a buffer that contains untrusted input from the network. `TaddNodeno` at (2) is therefore a controlled 32-bit integer from the network, and it is subsequently used as an argument at (3). Finally, at (4) within `BitmaskImpl::set`, it is used as an array index. Since no validation has been performed on this value, this potentially produces an out-of-bounds (OOB) write.

MySQL Cluster registers around 1,400 signals (the number of calls to `addRecSignal()`) and around 6,500 accesses on untrusted input (the number of calls to `getDataPtr()` plus the number of calls to `getDataPtrSend()` plus the number of direct accesses of `theData`). Although the example above is not very challenging, the manual review is still very time consuming due to the required scale. It's time to introduce taint analysis.

There are 4 common terms used during taint analysis: SOURCE, SINK, PROPAGATION, and SANITIZER. SOURCE refers to where data originates. In the example above, `signal->getDataPtr()` at (1) is the SOURCE. SINK refers to where data ends. In the example above, the access of array index at (4) is a SINK. PROPAGATION refers to how the data flows. In our example, the assignment at (2) and the argument copy at (3) are considered PROPAGTIONs. SANITIZER indicates where data is either sanitized or validated. There is no SANITIZER on the above example, and that is the root cause of the bug. The task of taint analysis is to look for a flow from SOURCE to SINK where the flow did not meet SANITIZER during the PROPAGATION. By defining the suitable SOURCE, SINK, PROPAGATION, and SANITIZER, taint analysis should return the types of bugs we seek.

**The Process**

Two taint analysis tools were used to search for these types of bugs: Clang Static Analyzer and CodeQL. The scanning scope of source code is limited to `storage/ndb/src/kernel/` only. We will restrict our search to low-hanging-fruit, which we define as two bug types only: (1) buffer overflows in memcpy-like functions and (2) array index OOB accesses. The version of MySQL Cluster we are using for our examples in this blog is 8.0.25.

**Clang Static Analyzer**

[Clang Static Analyzer](https://clang-analyzer.llvm.org/) (CSA) has a checker, [GenericTaintChecker](https://clang.llvm.org/docs/analyzer/checkers.html#alpha-security-taint-taintpropagation-c-c), which provides the taint analysis feature. By default, it has a set of [pre-defined](https://github.com/llvm/llvm-project/blob/main/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp#L430) SOURCE and PROPAGATION values. The default SINK will [check](https://github.com/llvm/llvm-project/blob/main/clang/lib/StaticAnalyzer/Checkers/GenericTaintChecker.cpp#L639) some dangerous APIs and arguments, such as format string, command injection, buffer size in memcpy-like function, and so forth. GenericTaintChecker also shares tainted information with [ArrayBoundCheckerV2](https://clang.llvm.org/docs/analyzer/checkers.html#alpha-security-arrayboundv2-c) in order to recognize that the use of a value as an array index is a SINK. Users can also customize some simple SOURCE, SINK, PROPAGATION, and SANITIZER values by providing a [config file](https://github.com/llvm/llvm-project/blob/main/clang/test/Analysis/Inputs/taint-generic-config.yaml). If the config file cannot satisfy your requirement, such as for a more complicated semantic, you may have to write a new CSA checker in C++.

Using CSA for taint analysis, we first must let the checker know our SOURCE at (1). The config file cannot define an access to a variable, and writing a new checker would be an unwise expense of effort. Instead, I modified the code base to be analyzed, so that all the accesses of untrusted input have been replaced with something recognized as a pre-defined SOURCE. Some examples are shown as below:

Another untrusted SOURCE is the return of `SegmentedSectionPtr` in the `getSection()` function.

The default SINK missed some functions, which can easily be added to the config file as below:

Then, we can scan the project and get the reports using the following commands:

The `Makefile2` file specified the target scanning directory:

The reports can be viewed in a browser by running the `scan-view` command to start up a local web server.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/bd64ae32-afe3-4e43-b6e1-b6dfe0872046/Picture1.png)

There is some duplication in the output, where multiple reports flag the same line of code. Also, we are interested only in reports that show taints reaching memcpy-like functions and array indexes. In the end, I found approximately 100 interesting reports.

**CodeQL**

[CodeQL](https://securitylab.github.com/tools/codeql/) also supports taint analysis. It refers to it as [taint tracking](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-cpp/). There are no pre-defined SOURCEs or SINKs. Users define these with the [QL language](https://codeql.github.com/docs/ql-language-reference/). We defined our SOURCE and SINK as follows:

Once defined, we can scan the project with the following command line:

A quick cross-check of the scan results against the results from the Clang Static Analysis above showed that CodeQL was missing some bugs. After some investigation, the root cause was that PROPAGATION on some structure field accesses were not being recognized. A similar situation is discussed [here](https://msrc-blog.microsoft.com/2019/03/19/vulnerability-hunting-with-semmle-ql-part-2/), and I enhanced the PROPAGATION as follows:

The generated report became longer, but the number of bugs found was excessive. After reviewing the report, I found that in some cases, validation was being performed by `ptrCheckGuard()`, `arrGuard()`, or other bounds checking. SANITIZER can help here to reduce the number. The bounds checking is assumed when there is an `if` statement that includes `>`, `<`, data-preserve-html-node="true" `>=`, or `<=`. data-preserve-html-node="true" Make sure that your SANITIZER does not accidentally drop some real bugs before applying this modification.

We then scanned the project again. The scanning can also be done in Visual Studio Code with CodeQL extension. However, some complicated queries are too slow to process and may fail due to memory exhaustion.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/b677f5f8-3cd7-49ea-aff4-fe9e76d00379/Picture2.png)

Some reports are duplicated at the same line of code. After de-duplicating, the number of interesting reports is around 320. However, the number should be fewer since some of them are still similar or even identical.

Here is the [source](https://github.com/thezdi/PoC/blob/master/MySQL/example.ql) of the final CodeQL.

**The Results**

After reviewing all the reports, I generated Proof of Concept (POC) manually to confirm each bug. CSA found 28 bugs. A total of 18 of these bugs are array index OOB vulnerabilities and 10 are overflows on memcpy-like functions. CodeQL found 34 bugs. This tool found 21 array index OOB bugs and 13 overflows on memcpy-like functions. Using these methods, we discovered 37 unique bugs, with 25 of them being found by both tools. Only nine of 37 of these bugs overlapped from ZDI submissions, which means 28 are new for us. These numbers not only mean that the taint analysis is useful in this scenario, but also mean that MySQL Cluster has quite a few bugs to be discovered.

Each of these two tools has its pros and cons. By using both Clang Static Analyzer and CodeQL, we can learn from their different feedback and improve the output from each tool. These variances can be compared to the concept of differential testing. The taint propagation provided by either tool has its deficiencies, but can still yield useful results.

The power of these tools could be extended further by adding additional bug classes in SINK. I recommend applying taint analysis to loop counters and pointer dereferences.

**Conclusion**

Due to the large-scale codebase and simple bug pattern present in MySQL Cluster, taint analysis was quite useful. It identified low-hanging-fruit bugs automatically and quickly. Each tool discussed has its own pros and cons, and we recommend trying more than one tool to get the best results. The difference can be the feedback, which can be used to improve the overall results. Furthermore, we cannot blindly trust the output of either tool and must verify them carefully.

Also, thanks to my colleague [@RenoRobertr](https://twitter.com/renorobertr), who provided feedback and several contributions to this work. He will publish a write-up of additional work on MySQL Cluster soon with his advanced Binary Ninja skills. That blog should be available in a couple of days.

We are looking forward to seeing more submissions of this type in the future. Until then, you can find me on Twitter [@_wmliang_](https://twitter.com/_wmliang_), and follow the [team](https://twitter.com/thezdi) for the latest in exploit techniques and security patches.

  * [MindshaRE](/blog/tag/MindshaRE)
  * [MySQL](/blog/tag/MySQL)
  * [Taint Analysis](/blog/tag/Taint+Analysis)

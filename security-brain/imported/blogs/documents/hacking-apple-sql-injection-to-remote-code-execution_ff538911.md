---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-08_hacking-apple-sql-injection-to-remote-code-execution.md
original_filename: 2024-05-08_hacking-apple-sql-injection-to-remote-code-execution.md
title: Hacking Apple - SQL Injection to Remote Code Execution
category: documents
detected_topics:
- sqli
- command-injection
- password-reset
- mfa
- otp
- automation-abuse
tags:
- imported
- documents
- sqli
- command-injection
- password-reset
- mfa
- otp
- automation-abuse
language: en
raw_sha256: ff53891181f0bf0367b18e9f08f7988722fcaa0784ae164eaff86b4e207db658
text_sha256: afa005fce214167d15855f105c5c92286a5ce3e1a23d44c8b2487ac6b57c35c4
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Apple - SQL Injection to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-08_hacking-apple-sql-injection-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, password-reset, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `ff53891181f0bf0367b18e9f08f7988722fcaa0784ae164eaff86b4e207db658`
- Text SHA256: `afa005fce214167d15855f105c5c92286a5ce3e1a23d44c8b2487ac6b57c35c4`


## Content

---
title: "Hacking Apple - SQL Injection to Remote Code Execution"
page_title: "Hacking Apple - SQL Injection to Remote Code Execution — ProjectDiscovery Blog"
url: "https://blog.projectdiscovery.io/hacking-apple-with-sql-injection/"
final_url: "https://projectdiscovery.io/blog/hacking-apple-with-sql-injection"
authors: ["Harsh Jaiswal (@rootxharsh)", "Rahul Maini (@iamnoooob)"]
programs: ["Apple", "Mura CMS", "Masa CMS"]
bugs: ["SQL injection", "RCE", "Security code review"]
publication_date: "2024-05-08"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 296
---

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FBlog%20Header%20Background%20Image.07fydz4trtf5v.png&w=3840&q=75)

[Vulnerability Research](/blog/category/vulnerability-research/1)•

[Nuclei & Templates](/blog/category/nuclei-templates/1)

# Hacking Apple - SQL Injection to Remote Code Execution

By Harsh Jaiswal & Rahul Maini

May 8, 2024

7 min read

![Hacking Apple - SQL Injection to Remote Code Execution](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F05%2FBlog---Apple-SQL-Injection.png&w=828&q=75)

#### Table of Contents

  * Introduction 
  * Finding the sink
  * Tracing sink to source
  * Triggering & Exploiting SQL injection
  * Detection via Nuclei
  * Conclusion

#### Authors

[![Harsh Jaiswal](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F08%2F1585309233118.jpeg&w=96&q=75)Harsh Jaiswal](/blog/author/harsh/1)[![Rahul Maini](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F11%2FTKTMQH41W-U04DH0WJJLX-eec5b4b57170-512.jpeg&w=96&q=75)Rahul Maini](/blog/author/rahul/1)

#### Share

[](https://x.com/intent/post?url=)[](https://www.linkedin.com/shareArticle?mini=true&url=)

### Introduction 

In our [last blog post](https://projectdiscovery.io/blog/hello-lucee-let-us-hack-apple-again/), we delved into the inner workings of Lucee and took a look at the source code of Masa/Mura CMS, and the vastness of the potential attack surface struck us. It became evident that investing time in understanding the code could pay off. After dedicating a week to our exploration, we stumbled upon several entry points for exploitation, including a critical SQL injection flaw that we were able to exploit within Apple's Book Travel portal.

In this blog post, we aim to share our insights and experiences, detailing how we identified the vulnerability sink, linked it back to its source, and leveraged the SQL injection to achieve Remote Code Execution (RCE).

### Finding the sink

From playing around with the Masa/Mura CMS, we understood our attack surface - mainly the attack surface accessible on Apple's environment. Our primary focus was on JSON API, as it exposes some methods that are accessible within Apple's environment. Any potentially vulnerable sink we find should have its source in JSON API. 

We deliberated on optimising our approach to streamline our source code review process. We explored the availability of static analyzers or CFM parsers capable of traversing through code while disregarding sanitizers.

For instance, this is how a safe parameterised SQL query is written via tag-based CFM: 

cfml

Copy
  
  
  1<cfquery>
  2select * from table where column=<cfqueryparam cfsqltype="cf_sql_varchar" value="#arguments.user_input#">
  3</cfquery>

And this is how an unsafe SQL query is written:

cfml

Copy
  
  
  1<cfquery>
  2select * from table where column=#arguments.user_input#
  3</cfquery>

It would be great if we could parse and traverse through the code and only print `cfquery` tags that have unsanitized input regardless of having the `cfqueryparam` tag inside or not. We came across <https://github.com/foundeo/cfmlparser> which could let us do this.  
  
Here's how we targeted SQL injection sink detection:

  * Parse each CFM/CFC file.
  * Go through each statement, select the statement if it's a tag and its name is `cfquery` .
  * Strip all tags (like cfqueryparam) inside the code block of cfquery and if it still has `arguments` in the codeblock then the input is not parameterized and the query is susceptible to an SQL injection, given no other validation is in place.
  * Print this query.

cfml

Copy
  
  
  1<cfscript>
  2  targetDirectory = "../mura-cms/";
  3  files = DirectoryList(targetDirectory, true, "query");
  4
  5  for (file in files) {
  6  if (FindNoCase(".cfc", file.name) or FindNoCase(".cfm", file.name)) {
  7  fname = file.directory & "/" & file.name;
  8  if (file.name != "dbUtility.cfc" && file.name != "configBean.cfc" && !FindNoCase("admin", file.directory) && !FindNoCase("dbUpdates", file.directory)) {
  9  filez = new cfmlparser.File(fname);
  10  statements = filez.getStatements();
  11  info = [];
  12  for (s in statements) {
  13  if (s.isTag() && s.getName() == "cfquery" && FindNoCase("arguments", s.getStrippedInnerContent(true, true))) {
  14  WriteOutput("Filename: <b>#fname#</b>");
  15  WriteOutput("<br><br>" & s.getStrippedInnerContent(true, true));
  16  WriteOutput("<br><br><br><br>");
  17  }
  18  }
  19  }
  20  }
  21  }
  22</cfscript>

We started going through the result with a few things in mind, such as ignoring input like `siteid` because JSON API validates it in advance.  
  
One of the queries that had two other inputs was this:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F03%2Fimage-2.png&w=3840&q=75)

### Tracing sink to source

Looking at the function which had this query concluded that there's only one exploitable argument, that is, `ContentHistID`. The argument `columnid` is numeric and `siteid` is validated by default.

cfml

Copy
  
  
  1<cffunction name="getObjects" output="false">
  2	<cfargument name="columnID" required="yes" type="numeric" >
  3	<cfargument name="ContentHistID" required="yes" type="string" >
  4	<cfargument name="siteID" required="yes" type="string" >
  5
  6	<cfset var rsObjects=""/>
  7
  8	<cfquery attributeCollection="#variables.configBean.getReadOnlyQRYAttrs(name='rsObjects')#">
  9		select tcontentobjects.object,tcontentobjects.name,tcontentobjects.objectid, tcontentobjects.orderno, tcontentobjects.params, tplugindisplayobjects.configuratorInit from tcontentobjects
  10		inner join tcontent On(
  11		tcontentobjects.contenthistid=tcontent.contenthistid
  12		and tcontentobjects.siteid=tcontent.siteid)
  13		left join tplugindisplayobjects on (tcontentobjects.object='plugin'
  14  and tcontentobjects.objectID=tplugindisplayobjects.objectID)
  15		where tcontent.siteid='#arguments.siteid#'
  16		and tcontent.contenthistid ='#arguments.contentHistID#'
  17		and tcontentobjects.columnid=#arguments.columnID#
  18		order by tcontentobjects.orderno
  19	</cfquery>
  20
  21	<cfreturn rsObjects>
  22
  23</cffunction>

The function `getObjects` was called within the `dspObjects` function in the core/mura/content/contentRendererUtility.cfc component. 

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F03%2Fimage-5.png&w=3840&q=75)

The call stack was:  
  
JSON API -> processAsyncObject -> object case: displayregion -> dspobjects() -> getobjects().

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F03%2Fimage-6.png&w=3840&q=75)

### Triggering & Exploiting SQL injection

By default, Lucee escapes single quotes by adding a backslash before them when passed as input. This can be managed by using a backslash to escape one of the single quotes.

This should trigger the SQL injection:  
  
`/_api/json/v1/default/?method=processAsyncObject&object=displayregion&contenthistid=x%5c'`

However, it didn't. Upon revisiting the source code, we identified a crucial condition in the `dspObjects` function. Before calling `getObjects`, an `if` condition must be satisfied: the `isOnDisplay` property must be set to true in the Mura servlet event handler. Initially, we assumed that any property on the event handler could be set simply by passing the property name as a parameter, along with its value. This assumption was based on our debugging session within the codebase.

Our attempts to set the `isOnDisplay` property in this manner were unsuccessful. It appears that somewhere in the code, this property is being overwritten.

After conducting some grep searches, we stumbled upon the `standardSetIsOnDisplayHandler` function call within the `processAsyncObjects` of the JSON API.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F03%2Fimage-7.png&w=3840&q=75)

It appears that by simply passing the `previewID` parameter with any value, we can set the `previewID` property, which in turn will set the `isOnDisplay` property to true.

`/_api/json/v1/default/?method=processAsyncObject&object=displayregion&contenthistid=x%5c'&previewID=x`

And it worked:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F03%2Fimage-8.png&w=3840&q=75)

Since this was an error-based SQL injection, we could exploit it quite easily to achieve Remote Code Execution (RCE). Locally, we successfully performed RCE by following these steps:

  1. Reset an Admin user's password.
  2. Obtain the reset token and user ID via SQL injection.
  3. Use the password reset endpoint with exfiltrated info.
  4. Utilize plugin installation to upload CFM files.

However, on Apple's environment, we encountered only an Unhandled Exception error without any query-related information, turning this into a blind SQL injection. Fortunately, the token and user ID are UUIDs, making it relatively straightforward to exfiltrate them. With a bit of scripting, we were able to accomplish this task.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F05%2Fimage.png&w=3840&q=75)

We promptly submitted our report to Apple, including Proof of Concept (PoC) demonstrating logging into an account while theoretically providing them with RCE details.

### Detection via Nuclei

This SQL injection vulnerability can be identified by utilizing the below Nuclei template:

yaml

Copy
  
  
  1id: CVE-2024-32640
  2
  3info:
  4  name: Mura/Masa CMS - SQL Injection
  5  author: iamnoooob,rootxharsh,pdresearch
  6  severity: critical
  7  description: |
  8  The Mura/Masa CMS is vulnerable to SQL Injection.
  9  reference:
  10  - https://blog.projectdiscovery.io/mura-masa-cms-pre-auth-sql-injection/
  11  - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32640
  12  impact: |
  13  Successful exploitation could lead to unauthorized access to sensitive data.
  14  remediation: |
  15  Apply the vendor-supplied patch or update to a secure version.
  16  metadata:
  17  verified: true
  18  max-request: 3
  19  vendor: masacms
  20  product: masacms
  21  shodan-query: 'Generator: Masa CMS'
  22  tags: cve,cve2022,sqli,cms,masa,masacms
  23
  24http:
  25  - raw:
  26  - |
  27  POST /index.cfm/_api/json/v1/default/?method=processAsyncObject HTTP/1.1
  28  Host: {{Hostname}}
  29  Content-Type: application/x-www-form-urlencoded
  30
  31  object=displayregion&contenthistid=x\'&previewid=1
  32
  33  matchers:
  34  - type: dsl
  35  dsl:
  36  - 'status_code == 500'
  37  - 'contains(header, "application/json")'
  38  - 'contains_all(body, "Unhandled Exception")'
  39  - 'contains_all(header,"cfid","cftoken")'
  40  condition: and

We've also added template in [nuclei-templates GitHub project](https://github.com/projectdiscovery/nuclei-templates/pull/9721).

### Conclusion

In conclusion, our exploration of Masa/Mura CMS has been a rewarding journey, revealing critical vulnerabilities. The code review process begins by focusing on vulnerable SQL injection code patterns and then utilizing the [CFM/CFC parser](https://github.com/foundeo/cfmlparser) to search for specific patterns within the codebase, a similar approach to Semgrep. Once potential sinks were identified, we traced them back to the source, in this case, the JSON API of Mura/Masa CMS. 

We responsibly disclosed these findings to Apple and the respective Masa and Mura CMS teams.  
  
**Apple's Response:**

Apple responded and implemented a fix within 2 hours of the initial report, swiftly addressing the reported issue. As always, working with Apple has been a good collaboration.

**Masa CMS:**

Masa is an open-source fork of Mura CMS, they were quite transparent and released a new version of Masa CMS with fixes. The 7.4.6, 7.3.13 and 7.2.8 versions have the latest security patches including another critical pre-auth SQL injection which is assigned CVE ([CVE-2024-32640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32640)).  
  
**Mura CMS:**  
  
Despite numerous attempts to reach out to the Mura team regarding these vulnerabilities, we received no response across multiple communication channels. With the 90-day standard deadline elapsed, we are now releasing this blog post detailing the reported vulnerability.

* * *

By leveraging Nuclei and actively engaging with the open-source community, or by becoming a part of the ProjectDiscovery Cloud Platform, companies can enhance their security measures, proactively address emerging threats, and establish a more secure digital landscape. Security represents a shared endeavor, and by collaborating, we can consistently adapt and confront the ever-evolving challenges posed by cyber threats.

[Interested in ProjectDiscovery Cloud Platform? Learn more here...](https://projectdiscovery.io/platform)

## Related stories

Related stories

[View all](/blog/category/vulnerability-research/1)

[![Nuclei Templates - April 2026](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F05%2Fapril-month.png&w=828&q=75)](/blog/nuclei-templates-april-2026)

### [Nuclei Templates - April 2026Two releases shipped this cycle - v10.4.2 (April 15) and v10.4.3 (May 5) - delivering deep KEV coverage, a major push into AI/LLM attack surface, fresh Perforce visibility, and broad quality improvements across the template library. 🚀 April Stats Release New Templates CVEs Added First-time Contributors v10.4.2 121 61 15 v10.4.3 105 62 12 Total 226 123 27 * 226 new templates shipped across both releases * 123 CVEs covered, including ~10 actively exploited vulnerabilities ](/blog/nuclei-templates-april-2026)

[![Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FEveryone-is-finding-vulns.--The-hard-part-is-proving-them.--Blog-Thumbnail-.png&w=828&q=75)](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

### [Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.LLMs are a genuine leap forward for vulnerability discovery. Anthropic reported 500+ zero-days from Opus 4.6 and OpenAI's Codex Security discovered 14 CVEs across projects like OpenSSH and GnuTLS. If you've experimented with LLMs for security testing, you've probably been impressed too. The practical reality for a security team deploying AI is messier than the headlines or early POC results suggest. Noise compounds fast. Anthropic brought in external security researchers to help validate the vo](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

[![Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caught](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FInside-the-Benchmark--Blog-Thumbnail---Updated-.png&w=828&q=75)](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

### [Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caughtThis is Part 2 of our vibe coding security benchmark study. In Part 1, we compared how LLM-based security tools like ProjectDiscovery's Neo and Claude Code performed against traditional SAST and DAST scanners on AI-generated code. We found that LLM-based tools like Neo and Claude Code detected many high-value findings that traditional scanners missed. Between Neo and Claude Code, Neo produced more true positives and fewer false positives because it could validate hypotheses against a running app](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

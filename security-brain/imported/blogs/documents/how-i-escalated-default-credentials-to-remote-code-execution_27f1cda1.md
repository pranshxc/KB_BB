---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-26_how-i-escalated-default-credentials-to-remote-code-execution.md
original_filename: 2023-03-26_how-i-escalated-default-credentials-to-remote-code-execution.md
title: How I escalated default credentials to Remote Code Execution
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 27f1cda1f1e5670d31a92d42eaf9483921964d137f4e221b27d3af34f87ec5f1
text_sha256: f488d6ea0e7b6fdf8a339db80618904de2a6e06865d3179c5f0187c2fd9c6f3f
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# How I escalated default credentials to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-26_how-i-escalated-default-credentials-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `27f1cda1f1e5670d31a92d42eaf9483921964d137f4e221b27d3af34f87ec5f1`
- Text SHA256: `f488d6ea0e7b6fdf8a339db80618904de2a6e06865d3179c5f0187c2fd9c6f3f`


## Content

---
title: "How I escalated default credentials to Remote Code Execution"
url: "https://pawanchhabria.medium.com/how-i-escalated-default-credentials-to-remote-code-execution-1c34504be7a5"
authors: ["Pawan Chhabria (@heybenchmarkkk)"]
bugs: ["Default credentials", "RCE"]
publication_date: "2023-03-26"
added_date: "2023-03-28"
source: "pentester.land/writeups.json"
original_index: 1338
scraped_via: "browseros"
---

# How I escalated default credentials to Remote Code Execution

How I escalated default credentials to Remote Code Execution
Pawan Chhabria
Follow
3 min read
·
Mar 26, 2023

332

4

Hello All, We all know Recon is very important to get P1 bugs. Shodan and Censys are probably the best search engines. I have been testing a lot of application logic issues so thought of learning some recon as well.

Please note: The domain and other details have been masked for Confidentiality Purpose.

Recently, I came across an application which was using Tomcat. Lets take the domain as www.example.com. The first thing I did was brute forcing tomcat directories, but unfortunately, it did not work. I tried a couple of more things but it didn’t work, that’s where I decided to visit Shodan.

I took the domain name and pasted it on Shodan. I filtered out the results on the basis of port. That’s where I noticed something strange. I saw some application running on port 8082 and it was using tomcat. The IP address was x.x.x.x (Just an example).

Get Pawan Chhabria’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried accessing http://x.x.x.x:8082/manager and guess what, it was prompting me to enter username and password. I got some hope there.

Press enter or click to view image in full size

Boooommmm!!!!!, The username=tomcat and password=***REDACTED*** worked and the Tomcat Application Manager Console was accessible.

Technically, I should have stopped but I knew, I can get a remote code execution by uploading malicious war file. I needed a malicious .JSP file to make the war file. I took the JSP file from here, saved it with name index.jsp on desktop. Then, I created the war file using the commands in the below screenshot.

Once the war file was generated, I navigated to “Select WAR file to upload” section and uploaded it.

Press enter or click to view image in full size

After refreshing the page, I could see an application named “webshell” was added in the list of application.

Press enter or click to view image in full size

I quickly opened it on a new tab. The webshell was successfully uploaded and I was able to run a few commands on it.

Press enter or click to view image in full size
Press enter or click to view image in full size

Golden Tip: Always think the other way round while hunting. Old vulnerabilities never die, we have to be creative enough to find them.

That’s it for this writeup.

Happy Testing!

Make sure you say a “Hi” to me if I could be of some help!

Twitter: @heybenchmarkkk

LinkedIn: Pawan Chhabria

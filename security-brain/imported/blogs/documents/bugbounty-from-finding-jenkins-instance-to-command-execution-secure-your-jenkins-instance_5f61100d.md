---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-27_bugbounty-from-finding-jenkins-instance-to-command-executionsecure-your-jenkins-.md
original_filename: 2018-09-27_bugbounty-from-finding-jenkins-instance-to-command-executionsecure-your-jenkins-.md
title: '#BugBounty — From finding Jenkins instance to Command Execution.Secure your
  Jenkins Instance!'
category: documents
detected_topics:
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 5f61100d6c5da282413c9a2d7556e07006f3f9804c00b6f6c1bee755f72e1a96
text_sha256: f5667cd6f4982d24891f4b3cafd0f1e968b36aab3d59e8c06ab0d8b4bed8691f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-27_bugbounty-from-finding-jenkins-instance-to-command-executionsecure-your-jenkins-.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5f61100d6c5da282413c9a2d7556e07006f3f9804c00b6f6c1bee755f72e1a96`
- Text SHA256: `f5667cd6f4982d24891f4b3cafd0f1e968b36aab3d59e8c06ab0d8b4bed8691f`


## Content

---
title: "#BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance!"
page_title: "#BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance! | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-from-finding-jenkins-instance-to-command-execution-secure-your-jenkins-instance-9bd1e75c2288"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["RCE", "Exposed Jenkins instance"]
publication_date: "2018-09-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5677
scraped_via: "browseros"
---

# #BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance!

#BugBounty — From finding Jenkins instance to Command Execution.Secure your Jenkins Instance!
Avinash Jain (@logicbomb)
Follow
3 min read
·
Sep 27, 2018

788

6

Hi Guys,

This particular writeup is about how I was able to find a publically accessible Jenkin instance in a private bugbounty program and leverage it to perform Remote Code Execution (RCE).

Every hack, every pentesting starts with recon (information gathering) so this - finding subdomain, open ports/services, public server IPs are some parts of it. In order to find public server IPs, one of the tools I generally rely on is https://censys.io/.

Censys has a great ability of finding IP addresses and gathering information about them. Censys also come to help in order to discover internal tools and assets by analyzing the SSL certificate, ports open etc.

When I searched the targeted domain on the same (let's call it as redacted.com as it was a private program, the name can’t be disclosed), I found an instance running on 8080 port —

Press enter or click to view image in full size
Censys Result

As it can be seen, server name here was Jetty:8080 which gave me a glimpse that it might have Jenkins running on it (usually because it’s running on a standard port 80/443/8080/8443 on Jetty)- What is Jenkins- It is used as a CI-Continous Integration tool, used for automating the deployment of projects/applications in enterprises. I further checked the IP (X.X.X.X) for more details and it was indeed Jenkins running there —

Press enter or click to view image in full size
Jenkins running

I opened it and it was publically accessible and the worst part was it didn’t have any authentication set over it.

Press enter or click to view image in full size
Jenkins dashboard

As you can see, I was able to access Jenkins dashboard, getting access to Jenkins dashboard in itself is a security concern. An attacker can access AWS Access keys, sensitive API tokens, private keys, Server’s pem files, IP addresses, usernames and email address etc. How much disaster it can cause, read this!

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Having worked closely with the CI team, I was aware of plenty of stuff related to Jenkins like to view all the people having access of Jenkins Instance /asynchPeople/ provides that —

Press enter or click to view image in full size
Jenkins User Access

/credentials/ — it gives access to view credential ids, names.

/configure/ — it is a configuration management dashboard for Jenkins.

/configureSecurity/ — configuration management for security settings.

/script/ — script console to run commands.

Now it’s time to check the same here, without thinking much I tried to see whether I have sufficient permission to access /script/ or not and to all my luck, I had it —

Press enter or click to view image in full size
/script/ accessible leading to Remote Code Execution (local server image)

As it can be seen, I tried to read “/etc/passwd” and I was able to do so. Similarly, I could write any file, upload file etc.

Since Jenkins also has the availability to hook up Git plugin which enables running Git commands from the console itself.

Press enter or click to view image in full size
GitHub Plugin

So, the publicly accessible Jenkins console enabled me to view and modify the production code of the application also and that’s made it more dangerous!

And this is what all can happen when companies mistakenly make the Jenkins server accessible over the internet and don’t have proper authentication set over it thinking it’s an internal application.

Report details-

15-September-2018 — Bug reported to the concerned company.

15-September-2018 — Bug was marked fixed.

16-September-2018— Re-tested and confirmed the fix.

19-September-2018— Rewarded by the company.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )

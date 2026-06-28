---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-24_how-i-got-access-to-local-aws-info-via-jira.md
original_filename: 2018-06-24_how-i-got-access-to-local-aws-info-via-jira.md
title: How I got access to local AWS info via Jira
category: documents
detected_topics:
- ssrf
- cloud-security
- oauth
- sso
- idor
- xss
tags:
- imported
- documents
- ssrf
- cloud-security
- oauth
- sso
- idor
- xss
language: en
raw_sha256: d073f7f0cf37e04868d3d4be1becc722bbfe14b0bf8d837a4955af87be84089d
text_sha256: ccc5105b5e440d24d83d0015763f22545608db5c4b316d46b70c146cf562a668
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I got access to local AWS info via Jira

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-24_how-i-got-access-to-local-aws-info-via-jira.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, oauth, sso, idor, xss
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `d073f7f0cf37e04868d3d4be1becc722bbfe14b0bf8d837a4955af87be84089d`
- Text SHA256: `ccc5105b5e440d24d83d0015763f22545608db5c4b316d46b70c146cf562a668`


## Content

---
title: "How I got access to local AWS info via Jira"
url: "https://www.coengoedegebure.com/how-i-got-access-to-local-aws-info-via-jira/"
final_url: "https://www.coengoedegebure.com/how-i-got-access-to-local-aws-info-via-jira/"
authors: ["Coen Goedegebure (@CoenHimself)"]
bugs: ["SSRF"]
publication_date: "2018-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5828
---

[Security](/tag/security/)

# How I got access to local AWS info via Jira

This article will describe how I exploited an SSRF vulnerability in an Atlassian plugin and gained access to AWS instance metadata via a local endpoint, explaining the theory and techniques along the way

  * [ ![Coen Goedegebure](/content/images/size/w100/2021/01/IMG_20201110_083654.jpg) ](/author/coen/)

#### [Coen Goedegebure](/author/coen/)

24 Jun 2018 • 8 min read

![How I got access to local AWS info via Jira](/content/images/size/w2000/2018/06/title-5.jpg)

This article will describe how I exploited an SSRF vulnerability in an Atlassian plugin and gained access to AWS instance metadata via a local endpoint, explaining the theory and techniques along the way.

It has been a while since I disclosed these issues to the companies where I discovered the vulnerability. Amongst these companies were a US university, a large European private company and a big department of the US Government. Most of them have reported back that they have fixed the issue or will in an upcoming release and one provided a token of gratitude. Some have not replied or updated and remain vulnerable to this date.

This article consists of a few chapters:

  * Discovery \- How did I find this vulnerability?
  * The vulnerability and the code \- What exactly does this vulnerability do and what does the insecure source code of the plugin look like?
  * Exploitation \- Exploiting the SSRF vulnerability and accessing the AWS local endpoint.
  * How to fix \- How to fix the issue and final thoughts

# Discovery

In my spare time I like to read hacking writeups to learn from the methods and techniques used by other hackers. In one of these articles I stumbled upon vulnerability [CVE-2017-9506](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9506&ref=coengoedegebure.com). This entry in the dictionary of Common Vulnerabilities and Exposures (CVE) mentions a problem with the Atlassian OAuth Plugin which opens the [Atlassian](https://www.atlassian.com/?ref=coengoedegebure.com) products to a Server Side Request Forgery attack.

One example is Jira, a well known piece of software by Atlassian and used by many companies for issue / project tracking. If Jira would have this OAuth plugin installed, it would be vulnerable for SSRF. Since I use this software on a daily basis, I decided to explore the vulnerability and maybe help a few companies close their gaps before they were found and exploited by the bad guys.

Too bad the author of the writeup decided to remove it, otherwise I would have linked it here.

# The vulnerability and the code

Atlassian registered the vulnerability as issue [OAUTH-344](https://ecosystem.atlassian.net/browse/OAUTH-344?ref=coengoedegebure.com) in their publicly accessible bugtracking system (Jira obviously ;)) and have patched it, by writing, over a year ago!

Closely examining the links of this issue, it is clear that not only Jira, but the following list of Atlassian products and versions are affected:

  * Bamboo < 6.0.0
  * Confluence < 6.1.3
  * Jira < 7.3.5
  * Bitbucket < 4.14.4
  * Crowd < 2.11.2
  * Crucible < 4.3.2
  * Fisheye < 4.3.2

As mentioned in the discovery paragraph, the [CVE entry](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9506&ref=coengoedegebure.com) for this vulnerability states the following:

> The **IconUriServlet** of the Atlassian OAuth Plugin from version 1.3.0 before version 1.9.12 and from version 2.0.0 before version 2.0.4 allows remote attackers to access the content of internal network resources and/or perform an XSS attack via Server Side Request Forgery (**SSRF**).

In order to understand why this works like it does, let's first get a basic understanding of SSRF and see what this looks like in the source code of this plugin.

## Server Side Request Forgery

Simply put, SSRF is a way to have a server make a network request on your behalf somewhere you shouldn’t be able to. Web servers usually have access to more resources than an external agent (like a user browsing the website) and the level of trust inside the local network is most likely higher than what is coming from the outside world. In other words, the web server will typically have more privileges to do stuff on its environment than you. This situation is what typically enables this vulnerability.

### Why is this bad?

SSRF is usually used to target internal systems behind firewalls that are normally inaccessible to an attacker from the external network. Furthermore, it’s also possible for an attacker to leverage SSRF to access services from the same server that is listening on the loopback interface (127.0.0.1). If an attacker can access these internal systems or services, he may have the possibility to pivot deeper into the internal network.

## Secure coding

So, the cause of this problem lies in the **IconUriServlet** of the OAuth plugin. Since this plugin is open source, we can take a look at the Java code of the [commits](https://bitbucket.org/atlassian/atlassian-oauth/commits/cacd1a118fdc3dc7562d48110340b3de4f0b0af9?ref=coengoedegebure.com) that fixed this issue. The `doGet`-method of the IconUriServlet class is interesting from a secure coding perspective, so I included it here:

![atlassian_commit1](https://www.coengoedegebure.com/content/images/2018/06/atlassian_commit1.png)

As we can see in line 36, the `doGet`-method takes the `consumerUri`-parameter from the GET request. This value is then used to create another HTTP GET request in line 45, that is executed by the server in line 49. The response of this request is returned accross to the original request via the responsehandler created in line 44 by passing it as a parameter in line 49.

It is clear that no validation or white-listing is performed on the input parameter `consumerUri`. This allows an attacker to navigate to any URL as a request performed by the plugin, which is exacly what's happening. I'll just leave this here:

![alltheinputs](https://www.coengoedegebure.com/content/images/2018/06/alltheinputs.jpg)

In the same commit, in a different file, we can see the IconUriServlet can be found on the URI `/oauth/users/icon-uri`:

![atlassian_commit2](https://www.coengoedegebure.com/content/images/2018/06/atlassian_commit2.png)

The OAuth plugin's [documentation](https://developer.atlassian.com/server/jira/platform/oauth/?ref=coengoedegebure.com) states that the servlet can be found in the `/plugins/servlet/` path. Combined with the discovery in the source-code we now know the full URL of the IconUriServlet URL. For Jira this could be something like this:

`https://<JIRA_BASEPATH>/plugins/servlet/oauth/users/icon-uri?consumerUri=...`

I did my exploitation on Jira, but replace _< JIRA_BASEPATH>_ with any basepath from another vulnerable Atlassian product and it will work for that as well.

# Exploitation

Having found the URL of the IconUriServlet and the name of the parameter to use, finding out whether the Jira configuration is vulnerable to this attack is pretty straight forward. My first attempt I did by providing the Gmail URL as a parameter:

`https://<JIRA_BASEPATH>/plugins/servlet/oauth/users/icon-uri?consumerUri=http://www.gmail.com`

Which yielded the following result:

![1gmail-1](https://www.coengoedegebure.com/content/images/2018/06/1gmail-1.png)

This made the Gmail main page appear. Note that I did not need to login for this to work. The OAuth plugin made the connection to the Gmail URL on our behalf and returned the resulting page to our browser. The SSRF exploit succeeded and this in itself would be a reason to disclose the issue to the responsible company. However, I took it a bit further in order to demonstrate the severity of the problem by attempting to access the cloud instance information (if at all hosted on the cloud).

## Moving to the cloud

Many companies move their applications and tooling to the cloud, be it Microsoft's Azure, Amazon Web Services (AWS), Google or other platforms. Besides the advantages, this move comes with a risk. Securing your cloud configuration can be challenging to say the least and making a mistake can open your inner networks and data to unwanted visitors.

#### Example: HEMA cloud backup

A good example of when this movement to the cloud went wrong, is the USB key cloud storage of HEMA, a large Dutch retail chain. In 2015, the [RevSpace](https://revspace.nl/Main_Page?ref=coengoedegebure.com) Hacker group from The Hague found a '_[full Bingo card](https://revspace.nl/HEMA_USB?ref=coengoedegebure.com)_ ' of security issues in this HEMA USB key, including the cloud backup. SQL injections, accessing other users' data via path traversal, source code on the server, etc.  
The lack of understanding of the risks involved in the digital transformation to the cloud, is made clear by reading HEMA's product FAQ (back in 2015). As an answer to the question _"How safe is your online storage of data?"_ , they state: _"The storage of data is performed by a renowned hosting-organisation and meets high security demands."_. Hosting software on Amazon does not safeguard you from implementing the proper security defenses.

Ok, back to the issue at hand. What would Jira be able to access if it was hosted on Amazon AWS?  
![icon-cloud-aws-1](https://www.coengoedegebure.com/content/images/2018/06/icon-cloud-aws-1.png)

### AWS Instance Metadata

At runtime, software on AWS will have the possibility to access metadata and user data about the current runtime environment (instance), which can be used to configure or manage it. Accessing this information is done via a REST interface on a local endpoint to the instance:

`http://169.254.169.254/latest`

Scripts and applications can use this interface to access information like the hostname, IP- or MAC-addresses of the environment they're running on. It also provides information about the network interfaces, domain, security services, public keys, security tokens and any custom metadata configured by the administrator. Especially this last one can be tricky as admins may have a false sense of security and decide to include credentials as custom metadata.

### Metadata categories

To view all categories of instance metadata from within a running instance, the following URI can be used:

`http://169.254.169.254/latest/meta-data/`

If the vulnerable Jira dashboard was running on AWS, then passing this URI to the `consumerUri`-parameter of the OAuth plugin should provide us with this information. This works because the Jira application itself, as software running on the AWS instance, will have local access to the 169.254.169.254 IP address:

![2metadata](https://www.coengoedegebure.com/content/images/2018/06/2metadata.PNG)

The result is an enumeration of the categories available to this instance. The [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html?ref=coengoedegebure.com#instancedata-data-categories) has more information on the structure of the instance metadata categories and what they will contain.

## Access to the AWS instance

This metadata is valuable information for attackers as they may use this to access critical data or further pivot into the company's internal infrastructure.

The dynamic [instance identity document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html?ref=coengoedegebure.com) is a JSON file that describes an instance. This document is generated when the instance is launched and validates the attributes of the instances, such as the subscribed software, instance size, instance type, operating system, and the [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html?ref=coengoedegebure.com):

![3identity-document](https://www.coengoedegebure.com/content/images/2018/06/3identity-document.PNG)

An application on an AWS instance is granted the permissions for the actions and resources that are defined for a certain [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html?ref=coengoedegebure.com) through the security credentials associated with the role. To see which roles are defined we can access `/latest/meta-data/iam/security-credentials/`:

![4iam-security-credentials](https://www.coengoedegebure.com/content/images/2018/06/4iam-security-credentials.PNG)

Then per role we can find the secret access keys and tokens via `/latest/meta-data/iam/security-credentials/<rolename>`:  
![5iam-credentials-secret](https://www.coengoedegebure.com/content/images/2018/06/5iam-credentials-secret.PNG)

### Bitbucket source code repositories

I even encountered a company that had a Bitbucket server (hosting source-code repositories of their software) that was not accessible from the outside world. However, their Jira dashboard did have access to it:  
![6bitbucket](https://www.coengoedegebure.com/content/images/2018/06/6bitbucket.PNG)

# How to fix

To fix this issue, make sure you've upgraded your Atlassian product to a version larger than the ones mentioned in the Vulnerability paragraph and upgrade your Atlassian [OAuth plugin](https://marketplace.atlassian.com/search?query=oauth&ref=coengoedegebure.com) to a version >= 2.0.4.

In general, this article is yet another example of a common vulnerability category in the [OWASP Top10 of 2017](https://www.owasp.org/index.php/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities?ref=coengoedegebure.com): _Using components with known vulnerabilities_. This issue has been known for a while now and the vendor released a patch for it. Not keeping your software patched with the latest upgrades will weaken your security and may open doors for unwanted visitors.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-07_the-16000-dev-mistake.md
original_filename: 2022-05-07_the-16000-dev-mistake.md
title: The $16,000 Dev Mistake
category: documents
detected_topics:
- cloud-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 9cbf4cd66bceada1cdb1470204ae9f4938af0c694b15aacda9d41f3a912b696f
text_sha256: 1eb48d859ff0b5751a27f9172484ad69f93a0820ca95c781d3d03384461797eb
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# The $16,000 Dev Mistake

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-07_the-16000-dev-mistake.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `9cbf4cd66bceada1cdb1470204ae9f4938af0c694b15aacda9d41f3a912b696f`
- Text SHA256: `1eb48d859ff0b5751a27f9172484ad69f93a0820ca95c781d3d03384461797eb`


## Content

---
title: "The $16,000 Dev Mistake"
url: "https://medium.com/@masonhck357/the-16-000-dev-mistake-13e516e86be6"
authors: ["Daniel Marte (@Masonhck3571)"]
bugs: ["Information disclosure"]
bounty: "16,000"
publication_date: "2022-05-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2657
scraped_via: "browseros"
---

# The $16,000 Dev Mistake

Top highlight

The $16,000 Dev Mistake
Daniel Marte
Follow
6 min read
·
May 7, 2022

519

7

Hello all!

Its been a while since my last write up. As a-lot of you know, last year I joined the Bugcrowd team as an Application Security Engineer. Since then, my full-time hacking has taken quite the backseat as I transitioned into a full-time role with Bugcrowd. Towards the end of the year, I decided to put my focus onto 1 program only as every assets that they own was in scope!

So this is going to be a writeup on how I located some AWS keys with Recon, How I was able to leverage it to find out roles and permissions as well as digging deeper to different services to really solidify the impact.

Tools used:
Burp Suite Pro

2. JSminer Extension

3. DataExtractor Extension

4. FFUF

5. KiteRunner

6. Assetnote Wordlists

7. AWS cli

8. Shodan

Recon

As you know, any good vulnerability story starts with some solid recon. So I decided to go through Shodan and look for anything thats promising. So by making the query, “ssl:”{{Org name}}””, I was able to pull all scanned Assets belonging to the organization by making that query but I needed to start filtering it as there were MANY assets, so just like i used the query ssl:”{{Org name}}”, I started filtering out different assets by prepending a “-” on my queries.

So now I have ssl:”{{Org name}}” results and I want to remove the results of all assets belonging to example1.com My query will be the following:

ssl:”{{Org name}} -Ssl.cert.subject.CN:”example1.com”

I also wanted to remove any asset that was served by AkamaiGhost so I also added -AkamaiGhost†

Ok! now I see some interesting assets and IP addresses that I have never seen. I open up Burp and Firefox to start hitting the new assets. I discovered a Burp extension the day before called JSminer that runs through a list of regex and patterns and posts it as a severity.

[Post JSMiner screenshot]

I also have another tool made by Gwendolyn that also will pull data based on a list of regex that is user-suppled. Here is the link to the github repo. These 2 extensions both work via passive scanning, although JSMiner does have an active scan module to look for .map files.

Now that all tools are setup on a fresh new Burp Project. I started by extracting JS files from GAU and Wayback and saved them into a file called Jsurls.txt. Then by using TomNomNom Unfurl tool. I took that file, Extracted the list of hosts and put that in one file called Domains.txt. I then, extracted all the paths of the urls and saved it on another file called Jspaths.txt. As you know, some brute-forcing is coming your way but FIRST, I want to be a bit more thorough on how I am brute-forcing. So I decided to revisit my JSurls.txt file to extract the url up to the first subdirectory(without the js files) and put that into my Domains.txt file. I then pulled in URLs with 2nd level subdirectories, and then 3rd level subdirectories and added them to my Domains.txt file. From there it was time to utilize the FFUF tool to start the content discovery. I ran a simple FFUF one-liner to run all Javascript paths that I scraped from GAU/Wayback against all subdomains/subdirectories. From there, I had FFUF proxy the results returning ‘200’ to BURP. BURP will then start a live passive scan which will include utilizing JSMiner and DataExtractor extension.

Within a couple of minutes, I had several hits for an AWS key in a dev subdomain. It seems like adding 2nd level subdirectories was the key here. Final result for the Javascript file was https://tre-uat-euw1.redacted.com/assets/Javascript/config/config.js. The path “/Javascript/config/config.js” was the key path here. After pulling the AWS Access Key and AWS Secret Key. I dove straight to AWSCLI to see how we can ensure max impact.

Exploitation

AWS CLI is a tool that pulls all the AWS services together in one central console, giving you easy control of multiple AWS services with a single tool. The acronym stands for Amazon Web Services Command Line Interface because, as its name suggests, users operate it from the command line. Utilizing this tool, it allows us to take the keys we find and explore what services we have access too. So OFF we go:

First, we should create a profile using this one-liner:
aws configure — profile {whatevername}

Press enter or click to view image in full size

By creating this profile, we can call awscli commands utilizing the credentials located in the Javascript file. Now that the profile is created, its time to figure out exactly how permissive these keys really are.

Get Daniel Marte’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I ran the following command:

aws — profile {whatevername} sts get-caller-identity

This command gives you Userid, Account ID, and arn(which includes the username). By calling this command, it can provide you with crucial information, like the username, to pivot and continue exploring further. Although this information in sensitive in nature, this wouldn't be considered maximum impact. Sometimes, program owners need to know how impactful certain vulnerabilities can be. This can determine the difference between a 9.0 critical and a 10.0 critical(max pay) We can determine more impact with the following Awscli commands.

The command above will give you policy information associated with the username inputted into the command like. As you can see below, The policy name associated with the username located is AdministratorAccess.

aws iam list-attached-user-policies — profile {whatevername} — user-name {username}

Press enter or click to view image in full size

This command above will provide you with crucial information about the Policy that the user is under. A policy in AWS terms is a role or “group”. Which is essentially a permission set that allows a user to gain access to certain services with C.R.U.D permissions. Based on the screenshot above, we can assume that these keys have admin privileges. Now we need to find out what AWS services does this user have access too and if this user has full admin access to the services.

Finally, the last command I wanted to run to understand the full scope of the keys was to run the following command:

aws iam get-policy-version — profile redacted — policy-arn arn:aws:iam::aws:policy/AdministratorAccess — version-id v1

Press enter or click to view image in full size

This was exactly what I needed! This gave me two VERY important points of interest. As you can tell, there is a wildcard asterisk value next to the Action and Resource key. This indicates that I can perform ANY action with the AWS keys and I have access to all resources. What exactly does this mean?

IMPACT

To reiterate the impact, I have full access to all AWS services as an Admin with the ability to perform all actions. Meaning I can create, read, update and delete anything belonging to the company.

I had full access to all their EC2 snapshots
Press enter or click to view image in full size
Full access to their Lambda functions
Full access to all S3 buckets.

Once reported, this was taken down within 30 minutes and triaged by the program manager on a Saturday. Within a week, I received my first 5 digit payout at $16,000.

As the cool bounty hunters say: BOOM!

Takeaways:

Take time to understand a company and how they do things. Part of recon, besides gathering data, is trying to understand the pattern. Every program has a pattern, wether its the way they name their subdomains, to how they structure their directories.
Once you identify patterns, start getting creative.
Be thorough on your impact. I truly felt that if I submitted this vulnerability without digging deeper for more impact, it would not have been considered for a high bounty.

Thanks all for reading! If you have any questions, feel free to reach out on Twitter at https://twitter.com/Masonhck3571

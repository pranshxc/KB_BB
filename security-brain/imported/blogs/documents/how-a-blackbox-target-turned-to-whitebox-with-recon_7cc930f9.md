---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-27_how-a-blackbox-target-turned-to-whitebox-with-recon_2.md
original_filename: 2024-04-27_how-a-blackbox-target-turned-to-whitebox-with-recon_2.md
title: How A Blackbox Target Turned To Whitebox With Recon
category: documents
detected_topics:
- api-security
- sso
- idor
- access-control
- sqli
- command-injection
tags:
- imported
- documents
- api-security
- sso
- idor
- access-control
- sqli
- command-injection
language: en
raw_sha256: 7cc930f9bd473c6daba7b8f4aaf9bf46f081904208daabf81e23150c0ffb5cd0
text_sha256: d0286403ced7431505313e5c7da796e1fb4422528c537b280eb9abc828c9ab74
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# How A Blackbox Target Turned To Whitebox With Recon

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-27_how-a-blackbox-target-turned-to-whitebox-with-recon_2.md
- Source Type: markdown
- Detected Topics: api-security, sso, idor, access-control, sqli, command-injection
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `7cc930f9bd473c6daba7b8f4aaf9bf46f081904208daabf81e23150c0ffb5cd0`
- Text SHA256: `d0286403ced7431505313e5c7da796e1fb4422528c537b280eb9abc828c9ab74`


## Content

---
title: "How A Blackbox Target Turned To Whitebox With Recon"
url: "https://medium.com/@red.whisperer/how-a-blackbox-target-turned-to-whitebox-with-recon-e46536672702"
authors: ["Chux (@chux13786509)"]
bugs: ["Docker Registry"]
publication_date: "2024-04-27"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 317
scraped_via: "browseros"
---

# How A Blackbox Target Turned To Whitebox With Recon

How A Blackbox Target Turned To Whitebox With Recon
Chux
Follow
9 min read
·
Apr 27, 2024

178

I was invited to a private bug bounty program of a tech company, one of the biggest tech companies in its country. The scope was pretty much the entire company’s external infrastructure, that was big enough for a few days of only recon the attack surface.

I’m going to share some of my methodology for reconnaissance, that helped me a lot in many red team engagements and bug bounty programs. In order to keep this article not too long for reading, I will mention here the important parts of the recon that I find useful.

Recon is a very big part of offensive cyber, and there might be courses just for this topic alone. There is a baseline that most hackers follow, like port scanning and subdomain enumeration. And yet, highly trained and skilled hackers usually familiar with many different ways of recon, that include some OSINT, some enumeration and some useful tools that they adopted along the way or even build and customize for themselves.

When we attack a target that own many assets on the internet, it’s crucial to make sure that the recon process is thorough and we are not missing a blind spot that the target forgot to harden. For this reason, if you are in a red team, make sure that you have at least one team member that can be the expert for this topic.

For more content and hacking tips — follow me on X.

Press enter or click to view image in full size
Reconnaissance On The Target

So starting by recon, I was trying to focus on two main things:

Finding every internet asset of the target: IPs, domains & subdomains and even accounts related to the company on third party service (like slack)
OSINT investigation in order to understand better the services supplied by the target and also hoping to hunt some valid credentials (read more about 10 secrets for credentials harvesting)

For internet assets, I first tried to find every domain owned by the target. The first thing I was starting with is the target’s SSL certificate. SSL certificates are very interesting in terms of reconnaissance as they might hold a unique field that can be useful for finding more domains, subdomains and even IPs that use the same certificate. For example, by searching in crt.sh the content of the “Organization” field, we can find more domains of the target with completely different domain name.

Another example, is the Subject Alternative Name (SAN) field that as the name suggests, it holds more domains and subdomains related to the same certificate. Take a look at the certificate of Mercedes-Benz:

Mercedes-Benz Certificate’s SAN

As you can see, just by viewing the certificate of mercedez-benz.com, we can find more assets of the company:

More TLDs related to mercedes-benz
More domains of the company (benz.fr, media.daimler.com, mercedes-amg.com and more)

It’s important to mention that with big companies it’s necessary to view the certificates of many assets, because the company may be using a few. A good example is again with Mercedez-Benz. If we’ll view mercedes-benz.be certificate, we’ll find more domains of the company that were’nt in mercedes-benz.com cretificate:

Mercedes-benz.be Certificate’s SAN

After we enriched our target’s domains, it’s time for subdomain enumeration. There are many tools for this task: crh.sh, dnsdumpster, subdomainfinder, sublist3r and many more. My favorite one is Amass of OWASP, as it uses many resources to get a very good picture of the target.

While Amass is scanning for subdomains of the domains we gathered earlier in the recon process, I also used Shodan in order to find more assets, that sometimes don’t have any DNS record. This can be done by searching for the SSL certificates who hold our target name (filter: ssl.cert.subject.c: target.com) , or by searching for the target’s name in the HTTP headers.

Of course that if you have accounts for other online scanners, it’s recommended to do a similar process also with other tools that might scan different port ranges than Shodan:

Censys
Fofa
ZoomEye
Onyphe

These are all online and public scanners that already scan the target and we just have to query for the results, without having a direct contact with the target’s infrastructure. I know that many hackers like to also make active scans with tools like Masscan and Naabu. These are great tools and sometimes I use them too, but on large scale targets I usually find it more cost-effective to start with passive scans. Also in terms of stealth, scanners are noisy and you disclose your IP address that might get block by different firewalls and security products.

Now we have a list of a lot of domains and subdomains and also IP addresses that associated with the target. With the results of the online scanner (Shodan/Fofa/Censys) we also have a lot of open ports to check. So let’s put it all in a text file and feed httpx with it:

Press enter or click to view image in full size
httpx on the target

As you can see at the image above, there are some very useful features to httpx that can shed light about the web service behind the port. Eventually, based on the results of httpx I usually prioritize where I’m going to spend more time. By the end of this run, we will hold a good picture of the web services running in our attack surface.

Focusing on the results

Ok, so we have a final list of potential assets to test, after cleaning and filtering out some of the results, we ended up with around 100 IP addresses and domains/subdomains that looks interesting.

Get Chux’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s divide our efforts:

Starting vulnerability research on the main assets (like client’s panel, administration panels and so on)
Running a short fuzzing list at the background to check for “quick wins” on the 100 assets that we have

I started with the fuzzing task. When I meet with a long list of targets that I need to fuzz on, I usually use ffuf with a short custom wordlist that I made and contains only 100–150 words.

The custom list must be short and it holds words that if they I get status code 200 on one of them, it means automatically that I see a vulnerability in front of me, most of the time it’s a severe information disclosure. Here are some of the words in the list:

/config.json
/.git
/web.config
/server-status
/backup.zip
/.DS_Store
/v2/_catalog

While ffuf is running my list against 100 addresses, I started researching the main web application of the target. The first thing was to do API recon, just like I wrote about it here.

After some time I spent on API research, I wasn’t lucky to find a juicy vulnerability, maximum some parameters that I had to fuzz for with Arjun, but without permissions to use them. Every thing I tried was ended with invalid input error or an authorization problem. The app was definitely good with authorization validation.

So I went back to the ffuf that I ran earlier and found an interesting result: status code 200 on the address rg.target.com and the path /v2/_catalog. That means that we have a publicly open Docker Registry!

In order to confirm it, I used curl to send a GET request to https://rg.target.com/v2/_catalog. Immediately the response came back, full with a JSON containing all the docker images stored in this registry. Some of the docker images were with indicative name like “admin” or “frontend” and some were with names that I wasn’t familiar yet.

Time to enumerate and research. I sent requests to the docker registry server in order to get every tag of any docker image:

curl https://rg.target.com/v2/admin-REDACTED/tags/list

In response, I got the tags, which helps me to know better what is the latest docker image that was uploaded:

Example of docker registry enumeration for getting tag lists of an image

After a few more requests to some more docker images, I started looking at every image manifest in order to reveal some secrets:

curl https://rg.target.com/v2/admin-REDACTED/manifests/1.10

The results were very interesting, I was exposed to some data that was sensitive, but wasn’t really useful to exploit a vulnerability yet.

So I moved to pull the docker images in order to open them and search for code vulnerabilities. It’s important to know that analyzing a docker image is reading the code of the application you research. In fact, the docker image contains every piece of file that the program needs in order to run and function. So if to be explicit, accessing a docker registry of a target is just like accessing the target’s git.

For more details about docker registry, I wrote this article that is very relevant for this case too.

For pulling docker images from private registry we first need to create or edit the file in the following path: /etc/docker/daemon.json. We should add in a JSON format our new registry as an “insecure” registry that we can pull/push images from:

Allowing a private docker registry

So without waiting any longer, I started to pull some selected docker images that could be storing the source code of the main application’s backend server. I couldn’t just run the images as is because I was missing some dependencies in the entry point that I couldn’t guess. So for extracting the file system and the code files out of the docker images, I used the trick of running the image for the first 2 seconds and at the same time exporting the files to a tar file, like I explained here.

Exporting docker image file system to a file

And of course extracting the files from the tar file:

Press enter or click to view image in full size
The docker image’s file system extracted

And now we can dig into the directories, looking for the specific files containing the backend’s code. After a short view, I located the relevant directory under /home and started searching vulnerabilities and code secrets in its source code.

Remember the secured API I mentioned earlier? Now not only that I can see the exact mechanism, I also have some hardcoded valid API keys. By using these API keys, I could use every API with administrative privileges and in fact grab any user’s data and even altering user’s data.

With some more patient I tried to find more vulnerabilities inside the code, something like SQLi or even RCE. But the code was well secured and written with best practices so nothing came up.

I still wanted to find a way to get more even impact with this vulnerability. So one last thing I wanted to try before reporting my findings, is to check if except for read permissions to the docker registry, I also have write permissions. The meaning of pushing to a docker registry is that someone or something should pull my docker image and use it in order to affect the target. Docker registries tend to be a part of the CI/CD pipeline or part of the development process. At this point I still can’t tell what are the use cases of this registry, but I can assume three main use cases:

The application is based on a docker container so chances are that it managed by an orchestration utility like Kubernetes. It means that if I’ll push a new docker image to the registry with a “latest” tag, I may override the original docker image and replace it with my image that is replicated and contain a webshell.
The software engineers working on the backend use this docker registry in their development process, so at some point if I’ll replace the original docker image with my image with a “latest” tag, they might download my replicated image that could contain a script from me.
The least fun case, but still possible — this registry is just a backup registry and it gets only push requests, but never gets pull of the docker images. In this case, overriding current images would have no special effect on the target.

Anyway, I read again the rules of engagement and it says that any action that might harm or interrupt the company’s infrastructure in the production is completely out of scope (understandable). Hence, I decided to have a much more humble PoC and just validating that I have push permissions to the registry. So I took from DockerHub the latest image of NodeJS and pushed it to the target’s registry. As expected, it worked!

A full report was sent to the company and after more some explanations about the impact, they understood that it’s not only information disclosure vulnerability, it easily could be also a severe RCE vulnerability that could affect many different points of the company’s infrastructure.

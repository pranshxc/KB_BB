---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-30_old-rce-worth-3362.md
original_filename: 2022-10-30_old-rce-worth-3362.md
title: Old RCE worth $3362.
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 79b331b159d2abb9b4c51e9cf9cc42519fa8ac476e443fd6d51ba001afbf7e19
text_sha256: e504123d1b61c3f83de46c8315cf6b8a572a298b1ffa07f3c6815edfcf3ca840
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Old RCE worth $3362.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-30_old-rce-worth-3362.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `79b331b159d2abb9b4c51e9cf9cc42519fa8ac476e443fd6d51ba001afbf7e19`
- Text SHA256: `e504123d1b61c3f83de46c8315cf6b8a572a298b1ffa07f3c6815edfcf3ca840`


## Content

---
title: "Old RCE worth $3362."
page_title: "$3362 Reward for Finding a Critical RCE Vulnerability. | by nanwn | Medium"
url: "https://medium.com/@nanwinata/old-rce-worth-3362-1af0cd70c459"
authors: ["nanwn"]
bugs: ["RCE"]
bounty: "3,362"
publication_date: "2022-10-30"
added_date: "2022-10-31"
source: "pentester.land/writeups.json"
original_index: 1970
scraped_via: "browseros"
---

# Old RCE worth $3362.

$3362 Reward for Finding a Critical RCE Vulnerability.
nanwn
Follow
3 min read
·
Oct 30, 2022

133

1

Press enter or click to view image in full size

Have you come across the article “RCE via Symfony Secret Fragments”? If not, there are numerous articles available on Medium. I’m sure you already know this, but Shodan is a great tool for finding targets. However, the process doesn’t start with Shodan. It begins with a favicon hash. I used httpx from ProjectDiscovery to scan for random favicons.

During the scan, I stumbled upon a target.

https://retailersupport.redacted.com/favicon.ico [200] [Express,Node.js] [-2115385***]

Yes, the hash was obtained randomly from the subdomains of the target. I then searched for “hash:favicon:-2115385***” on Shodan and was lucky enough to find just one IP address. I continued to investigate this IP address because it was different from the “official” IP address listed on the Hackerone program page.

Next, I used dirsearch to gather more information about the IP. This tool helped me to dig deeper into the target.

python3 dirsearch -u 127.0.0.1

I discovered an endpoint at https://127.0.0.1/app_dev.php/.

After a quick Google search, I found that most of the articles were related to the Symfony framework. I then began to research more about the Symfony framework, specifically looking for information on exploiting it.

Searching for “Symfony Framework RCE” returned numerous articles and resources on the subject. It was quite surprising to see how many resources were available to help with exploiting the framework.

The endpoint at https://127.0.0.1/app_dev.php/ had a vulnerability in the Symfony framework where accessing the “phpinfo” endpoint without authentication would expose sensitive information.

To exploit this vulnerability, I navigated to https://127.0.0.1/app_dev.php/_profiler/phpinfo, and it worked successfully.

Configuration 2apache2handler 3Apache Version Apache/2.4.18 (Ubuntu) mod_fcgid/2.3.9 OpenSSL/1.0.2g 4Apache API Version 20120211 5Server Administrator info@dev.redacted.co.uk 6Hostname:Port dev.redacted.co.uk:0 7User/Group www-data(33)/33 8Max Requests Per Child: 0 — Keep Alive: off — Max Per Connection: 100 9Timeouts Connection: 30 — Keep-Alive: 10 10Virtual Server Yes 11Server Root /etc/apache2

After discovering the phpinfo endpoint, I wrote up a report detailing my findings. I initially believed that this was just an information disclosure vulnerability, so I didn’t check for any other weaknesses such as database credentials.

Get nanwn’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, after submitting the report, I received a response from the Hackerone triage team.

Hi @nanwn,

The reported asset is not in the scope of the program. Hence, I have sent a note to the Redacted Server Bug Bounty Program Team to check whether they are interested in receiving reports for this asset.

I will get back to you as soon as I hear back from them. Please bear with us in the meantime.

Thank you for your patience.

Cheers,

After researching and encountering multiple roadblocks, I finally stumbled upon a PDF file that listed the target domain. I added this information to my report and the program staff quickly changed the status to Triaged.

Upon further investigation, I discovered that the Symfony framework on the server was outdated and vulnerable to RCE.

I was shocked and quickly downloaded an exploit from a trusted resource to further my findings.

https://github.com/ambionics/symfony-exploits

I successfully achieved RCE on the server through my bash screen and Chrome browser. However, the staff had already fixed the vulnerability and deleted the /app_dev.php/ file by the time I realized it. Nevertheless, I was lucky enough to have taken a screenshot of the proof of concept (POC) beforehand.

https://redacted/_fragment?_path=_controller%3Dphpinfo%26what%3D-1&_hash=olvqWb%2FjUS%2F7Sk4L0fdQxJGmoHiEbLLV5C8S6%2BPzER2

https://redacted/_fragment?_path=cmd%3Did%26_controller%3Dshell_exec&_hash=c9KJ7TG5cvTbe5MDBjG8v7%2BQR2n9rcQ3eh49ardoYJs

Staff updated the severity from Critical to High (8.2)

Redacted Server Bug Bounty Program rewarded @nanwn with a $3,362 bounty.

Apr 23rd (6 months ago)

@nanwn — Thanks for the great finding. We look forward to future submissions from you. Happy Hunting!

Press enter or click to view image in full size

I am grateful to them not only for the bounty but also for the opportunity to review the target, even though it was not listed on the scope.

Big companies are often strict with the rules but forget about the impact on the organization. Whether a target is listed or not in the scope, it is worth reviewing.

Best of luck to everyone.

nan

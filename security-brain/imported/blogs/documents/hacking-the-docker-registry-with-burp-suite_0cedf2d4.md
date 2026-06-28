---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-14_hacking-the-docker-registry-with-burp-suite.md
original_filename: 2023-03-14_hacking-the-docker-registry-with-burp-suite.md
title: Hacking the Docker Registry with Burp Suite
category: documents
detected_topics:
- command-injection
- rate-limit
tags:
- imported
- documents
- command-injection
- rate-limit
language: en
raw_sha256: 0cedf2d4a3febf6ff6d4d6277434029914a12ce4e764e442d014244758889353
text_sha256: e68c747b3e0d0d2e6a827f4ea0cabc8b8a83c7fb337bb46e3e7f20307e6db2bf
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking the Docker Registry with Burp Suite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-14_hacking-the-docker-registry-with-burp-suite.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `0cedf2d4a3febf6ff6d4d6277434029914a12ce4e764e442d014244758889353`
- Text SHA256: `e68c747b3e0d0d2e6a827f4ea0cabc8b8a83c7fb337bb46e3e7f20307e6db2bf`


## Content

---
title: "Hacking the Docker Registry with Burp Suite"
url: "https://medium.com/@H1Xploit/hacking-the-docker-registry-with-burp-suite-18112cbfb6dd"
authors: ["H1Xploit (@H1Xploit)"]
bugs: ["Docker Registry"]
publication_date: "2023-03-14"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1382
scraped_via: "browseros"
---

# Hacking the Docker Registry with Burp Suite

Hacking the Docker Registry with Burp Suite
H1Xploit
Follow
3 min read
·
Mar 14, 2023

5

In this blog post, we will walk through the process of finding security bugs in a Docker registry by using Burp Suite with Intruder feature. Specifically, we will focus on how to brute-force directory names to find the repository file, and then demonstrate how to exploit the repository to get files.

Scenario: Our target domain is redacted.com, and we want to find any security vulnerabilities in their Docker registry. Let’s get started!

Step 1: Set up Burp Suite

First, we need to set up Burp Suite as our proxy for intercepting and manipulating web traffic. Open Burp Suite, and make sure that the proxy is running on the default port 8080. Next, configure your browser to use Burp Suite as a proxy by setting the HTTP proxy to “localhost” and the port to “8080”.

Step 2: Find the repository file

Now that we have Burp Suite set up, we can start brute-forcing directory names to find the repository file. To do this, we will use Burp Suite’s Intruder feature. First, we need to capture a request to the Docker registry by browsing to redacted.com in our browser. In Burp Suite, go to the “Proxy” tab and find the captured request in the history. Right-click on the request and select “Send to Intruder”.

In the Intruder tab, go to the “Positions” tab and select the “Add” button. This will allow us to define the payload positions in the request. Select the “Clear” button to clear any existing payload positions, and then highlight the path of the request (e.g., “/a/”) in the request editor. Click the “Add” button again to add the highlighted text as a payload position.

Press enter or click to view image in full size

Now, go to the “Payloads” tab and select the “Load” button. Choose the wordlist “directory-list-2.3-medium.txt” that you downloaded. This is a medium-sized wordlist of common directory names that we will use to brute-force the repository file.

Press enter or click to view image in full size

Finally, go to the “Start Attack” tab and click the “Start Attack” button. Burp Suite will now begin brute-forcing the directory names using the wordlist.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

Step 3: Get list of repository

Get H1Xploit’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now you can add the _catalog parameter to list the available repositories “ redacted.com/v2/_catalog “

Press enter or click to view image in full size

Step 4: Exploit the repository

Now that we have found the repository file, we can exploit it to get files. To do this, we will use the “docker pull” command to pull the contents of the repository onto our local machine.

First, copy the repository URL from the response in Burp Suite.

In our case, the repository URL is “redacted.com/v2/<repository-name>/manifests/<manifest-tag>”.

Replace “<repository-name>” and “<manifest-tag>” with the actual values from the response.

Next, open a terminal window and type the following command

docker pull <repository-url>

Replace “<repository-url>” with the actual URL that you copied from Burp Suite. This command will download the contents of the repository onto your local machine.

Congratulations! You have successfully found a security vulnerability in a Docker registry using Burp Suite with Intruder feature.

Reference : https://notsosecure.com/anatomy-of-a-hack-docker-registry

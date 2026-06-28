---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-31_exposed-docker-registries-server-as-critical-reminder-on-container-security.md
original_filename: 2023-03-31_exposed-docker-registries-server-as-critical-reminder-on-container-security.md
title: Exposed Docker Registries Server as Critical Reminder on Container Security
category: documents
detected_topics:
- oauth
- idor
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- oauth
- idor
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: 308e76acaa7697fafeecbe571bf19b73e967337642f59e0de9e8af489a5ed70f
text_sha256: 0161b974116827cc98fcc8185c0378fbc97b1de6c183663805d43b40364fa014
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# Exposed Docker Registries Server as Critical Reminder on Container Security

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-31_exposed-docker-registries-server-as-critical-reminder-on-container-security.md
- Source Type: markdown
- Detected Topics: oauth, idor, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `308e76acaa7697fafeecbe571bf19b73e967337642f59e0de9e8af489a5ed70f`
- Text SHA256: `0161b974116827cc98fcc8185c0378fbc97b1de6c183663805d43b40364fa014`


## Content

---
title: "Exposed Docker Registries Server as Critical Reminder on Container Security"
url: "https://emad0x90.medium.com/exposed-docker-registries-server-as-critical-reminder-on-container-security-a9bba13b403d"
authors: ["Emad Shawky"]
bugs: ["Docker Registry"]
publication_date: "2023-03-31"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1316
scraped_via: "browseros"
---

# Exposed Docker Registries Server as Critical Reminder on Container Security

Exposed Docker Registries Server as Critical Reminder on Container Security
Emad Shawky
Follow
5 min read
·
Mar 31, 2023

22

3

What is Docker?

Docker is a computer program that performs operating-system-level virtualization, also known as “containerization”.

The Docker Registry HTTP API is the protocol to facilitate the distribution of images to the docker engine. It interacts with instances of the docker registry, which is a service to manage information about docker images and enable their distribution.

Press enter or click to view image in full size
Description and what this vulnerability is all about?

A Docker registry is a storage and distribution system for named Docker images. The same image might have multiple different versions, identified by their tags.

A Docker registry is organized into Docker repositories, where a repository holds all the versions of a specific image. The registry allows Docker users to pull images locally, as well as push new images to the registry (given adequate access permissions when applicable).

Methodology:
I chose to automate the enumeration part of reconnaissance and found bugs using it with the following set of tools and also I created my own bash-script recon tool to automate running these tools ( Subfinder, httprobe , FFuF and Nuclei ) on VPS.
I used my experience in the field to enhance my recon methodology to find logical vulnerabilities and weak points.
How did I find this vulnerability?

1- As I normally do, I was using my recon scripts on a VPS to do my recon operation. My script shows my alert for an endpoint that looks like: https://XX.target.com/v2/catalog/ . in the beginning, I didn’t know or understand what the nature of this vulnerability was. So as usual, I open the description file for this vulnerability on the nuclei template to read about it. You can use the following link to check it out https://github.com/CharanRayudu/Custom-Nuclei-Templates/blob/main/docker-registry.yaml

2- After that, I started searching and poking around more to try to find how the logic behind it works. That is to get the highest powerful impact possible from this vulnerability.

3- To maximize what I can do or where I can go using this vulnerability:

I watched a bunch of tutorials about docker.
I researched and read a lot of reports about this vulnerability on HackerOne and other sources.
I read a lot of articles and writeups for similar vulnerabilities
Impact (Critical):
Docker Registry HTTP API v2 exposed in HTTP without authentication leads to docker images dumping and poisoning.
An attacker can use it to dump your docker images and poison them.
Proof of Concept:

# Step to PoC:

- Go to : https://XX.target.com

As mentioned, the Docker Registry exposes an API REST that can be queried via HTTP. If a Registry exposed to the internet is found, then it is possible to see all the Docker images uploaded there by acceding the following URL:

→ https:// XX.target.com /v2/_catalog/

Press enter or click to view image in full size

- It is also possible to see the tags for each image by making this request:

Get Emad Shawky’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

→ https:// XX.target.com /v2/overcast/db/tags/list

Press enter or click to view image in full size

- In the example above, you can observe that the Docker image “overcast/db” has only one tag named “latest”.

In the building process of every image, Docker creates a layer for each instruction (or step) that makes up the image. It is possible to get information about every layer by making the following request:

→ https:// XX.target.com /v2/overcast/db/manifests/1.3.40.49

Press enter or click to view image in full size

It will download a file that can then be opened with any text editor.

Each sha256 hash seen in the file represents a layer of the Docker image.

Once this information is known, then it is possible to download the contents of each layer with another request to the API. To do this, it is necessary to specify the sha256 of the image layer, as follows:

→ https:// XX.target.com /v2/overcast/db/blobs/sha256:73f64a17dcc090d65a83e07e7bd4a1**************b27a396b32af0

Press enter or click to view image in full size

It will download a file with a.tar.gz. extension.

Press enter or click to view image in full size

Once downloaded, it can be decompressed and its contents inspected. This will show the status of the Docker image’s filesystem in that specific layer.

Sometimes developers may enter passwords or other sensitive information during the build process, which is then removed in later layers. As a result, it is important to inspect each of the image layers, as they may contain sensitive information that is not presented in the final image.

So far only direct interaction with the Docker Registry API has been considered. However, it is possible to add the remote registry to a local Docker installation in order to interact with it using the Docker client. For that, the following information must be added inside the daemon.json file located at the /etc/docker path.

Press enter or click to view image in full size
Mitigation:
Version 2 of Docker Registry API supports multiple Token Based Authentications (i.e. bearer, OAuth, etc.) which should be implemented while deploying docker registry API.
Enable Content Trust to enforce client-side signing and verification of image tags.
Reference :
https://dreamlab.net/en/blog/post/abusing-exposed-docker-registry-apis/
https://hackerone.com/reports/924487?fbclid=IwAR2o4vsgjni1hZGp_zk***REDACTED-SUSPECT-TOKEN***https://www.acunetix.com/vulnerabilities/web/docker-registry-api-is-accessible-without-authentication/?fbclid=IwAR0wbSGL1kZY37aHM7FrB3gqs9Kmn5zGRduIQxa-SyYwyRUF5D_X-adEdZ0/
Summary:
As you can see, the impact of this vulnerability can be critical and super powerful on organizations and companies especially when the cybersecurity experts have a lot of knowledge about docker and how docker layers work.
My recommendation for anyone who wants to find similar vulnerabilities with such a high impact, is don’t just rely on automated enumeration tools for the recon process. Instead, take these tools as only the first step in your process as they can point out some paths you can take but it doesn’t lead you to the vulnerability directly.

My Linkedin: https://www.linkedin.com/in/emad0x90/

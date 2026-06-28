---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-18_how-i-manage-to-get-sensitive-informations-via-docker-image.md
original_filename: 2024-04-18_how-i-manage-to-get-sensitive-informations-via-docker-image.md
title: How i Manage to Get Sensitive Informations via docker image
category: documents
detected_topics:
- api-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- api-security
- command-injection
- information-disclosure
language: en
raw_sha256: 67f0f6eeb19ebc40ecc4cd000537fb7cdf7281e0c42122f62feaef20781a49fd
text_sha256: 54468217acce072989bbe4f69e8fb5a326571e0561c38f1d41894c8fcb592963
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# How i Manage to Get Sensitive Informations via docker image

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-18_how-i-manage-to-get-sensitive-informations-via-docker-image.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `67f0f6eeb19ebc40ecc4cd000537fb7cdf7281e0c42122f62feaef20781a49fd`
- Text SHA256: `54468217acce072989bbe4f69e8fb5a326571e0561c38f1d41894c8fcb592963`


## Content

---
title: "How i Manage to Get Sensitive Informations via docker image"
url: "https://ph-hitachi.medium.com/how-i-hacked-globe-gcash-services-and-manage-to-get-access-on-multiple-databases-including-ssh-9ca781348e8f"
authors: ["Ph.Hitachi"]
programs: ["Globe Telecom (Gcash)"]
bugs: ["Information disclosure", "Hardcoded credentials"]
publication_date: "2024-04-18"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 330
scraped_via: "browseros"
---

# How i Manage to Get Sensitive Informations via docker image

How i Manage to Get Sensitive Informations via docker image
Ph.Hitachi
Follow
5 min read
·
Apr 18, 2024

250

6

Hi guys,

Short Story:

after 2 years without doing bug bounty, someone message me on LinkedIn offering a Job on NCC Group as Bug Bounty Specialist (triager).

after the initial interview (screening) i don’t received any reply or status from them, on that point i disappointed to my self because i have many friends are already working on NCC.

i tried to refresh my knowledge and skills again by hunting on public program, but no luck, i found multiple valid bugs including criticals but it all marked as duplicate.

then i realize finding common vulnerabilities on these days is hard due to increasing researchers with limited programs even you found a bugs, there is a high chance that its duplicate.

so i find a new ways of attack path that are uncommon but can give you the most valuable information to the target, which is finding sensitive data that are accidentally exposed to the internet.

so on this article i will show you how to find sensitive information that accidentally exposed to internet as passive attack,

so passive attack is finding vulnerabilities without interacting to the services by only browsing & crawling on the internet, its an opposite of active attack like automated test that can trigger a security alerts on their end.

nowadays most of companies are using services where it can help them to automate their process and optimize resources like load balancing, seamless deployment such as CI/CD, containerization, etc.. and this we need to exploit.

Start:

first i search on Docker Hub to find public images

Press enter or click to view image in full size

after i search “gcash” there has 43 results, and the owner seems legitimate belongs to gcash, so let’s start to find sensitive informations here.

first choose a docker images, so i choose “gcashsupport/ms-login” because this more interesting than other images, this is most likely a gateway to other services.

Press enter or click to view image in full size
overview
Press enter or click to view image in full size
docker tags & image layer

after reviewing the tags & image layer i found out that the database productions was included, and this database is Amazon Relational Database Service (RDS).

so let’s pull the images on our local environment

Press enter or click to view image in full size

after i pulled it i run the container to access the image:

docker run -d gcashsupport/ms-login:1.0

Press enter or click to view image in full size
docker exec -it 17dc3eacc43b env

then i view the ENV on the container, but as you can see there are only DB_HOST are present on the env no username and password, but since the DB_HOST is in the docker images of course the credentials are also on the container, maybe on the source code?

Press enter or click to view image in full size

after checking the files on container i see this login.jar files which has (39614761 bytes), but the other are empty or default because it has only (4096 bytes), means the login.jar files are only uploaded to this image and theres no other files.

Press enter or click to view image in full size

after i run the login.jar file i confirm that this a Spring Boot

Get Ph.Hitachi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

i’m only using WSL i need to download the login.jar on my local machine to decompile so i downloaded it via docker command.

Press enter or click to view image in full size

then i decompile it using JD-GUI

Press enter or click to view image in full size

after i decompile it, we can see database credentials on:

src/main/resources/application.properties

after i hacked this container i look for the other docker images belongs to gcashsupport user and some of the image is actively managed, the last update was only a days ago:

Press enter or click to view image in full size

then i find out that all services that all publicly accessible image on gcashsupport, have configured database on images that could be exposed.

Press enter or click to view image in full size

also the other docker image has ssh keys so we can login to the server where this container has been deployed using this credentials we leaked, but this credentials are useless because it’s in docker container its isolated, accessing it on remote are similar to access the docker image that you pulled on your local machine.

Press enter or click to view image in full size
Gcash Master card & Gcash Gift card
Press enter or click to view image in full size

after i looked for another image i found out that “gcashsupport/lendingeligibilitytool” includes Gcash Master Card & Gift Card Database Credentials with gscore computation api endpoint.

Press enter or click to view image in full size

after refreshing my knowledge & practicing, i comeback with more knowledge!

Affected Images:

- gcashsupport/ackerman-tool:*
- gcashsupport/ms-biller-maintenance:*
- gcashsupport/ms-tl-pass:*
- gcashsupport/ms-jarvis:*
- gcashsupport/ms-powerpay-approval:*
- gcashsupport/ms-bank-maintenance :*
- gcashsupport/ms-login:*
- gcashsupport/ms-ipy-send:*
- gcashsupport/lendingeligibilitytool:*

Note: the services have dedicated database per image and also they use multiple database connection on some services like “gcashsupport/lendingeligibilitytool”.

The services is most likely a microservices (ms) for Globe Powerpay, Gcash Master card, Gcash Gift card, and some are internal tools like Inter-Peer Yield (ipy) and ackerman.

Press enter or click to view image in full size

This only takes me 2 days to uncover most critical bugs on gcash & globe telecom after the VDP has been annouced, including the first report i submited (still fixing).

even this not supports monetary reward, this experience rewared me a most valueble experience to hack the most big companies on local country.

if someone breach or compromised the database of gcash you can arrest these:
Leonel Obina
Christoper boyles
Herc Bandiola
Mark Rhogie Purok
John Lester Legaspi
John Albert Flores
Neil Harvey Miñano
JM Sanchez
Jayvee Garcia
Lex Santiago

just kidding these friends help me to back my skills by providing challenge where i can practice on & a resources that i can read.

linkedin: https://www.linkedin.com/in/jessdhoctor/

Timeline:

March 18, 2024 — Initial Report
March 25, 2024 — Triaged
April ?, 2024 — Initial Fixed (remove some public image)
April ?, 2024 — Fixed (public image again with new version/tags)
April 18, 2024 — Final Fixed (private all image repositories permanently)

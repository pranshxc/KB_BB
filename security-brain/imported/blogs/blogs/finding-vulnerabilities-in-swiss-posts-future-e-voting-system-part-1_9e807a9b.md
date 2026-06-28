---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-18_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-1.md
original_filename: 2022-01-18_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-1.md
title: Finding vulnerabilities in Swiss Post’s future e-voting system - Part 1
category: blogs
detected_topics:
- sso
- jwt
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- blogs
- sso
- jwt
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 9e807a9bfc50bdb4c61da643d3dd1f8d73bdfdf428a2b05c1aabea4deb626bb7
text_sha256: f1a2ec76c59714e92213e23a6a5aef8616b95dbbeaa58365c4ce6bb9a769ff80
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# Finding vulnerabilities in Swiss Post’s future e-voting system - Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-18_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-1.md
- Source Type: markdown
- Detected Topics: sso, jwt, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `9e807a9bfc50bdb4c61da643d3dd1f8d73bdfdf428a2b05c1aabea4deb626bb7`
- Text SHA256: `f1a2ec76c59714e92213e23a6a5aef8616b95dbbeaa58365c4ce6bb9a769ff80`


## Content

---
title: "Finding vulnerabilities in Swiss Post’s future e-voting system - Part 1"
url: "https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html"
final_url: "https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["Swiss Post"]
bugs: ["Insecure deserialization", "Cryptographic issues"]
publication_date: "2022-01-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2996
---

###  Finding vulnerabilities in Swiss Post’s future e-voting system - Part 1 

[ January 18, 2022  ](https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html "permanent link")

  

In September '21, I came across this story ["Swiss Post Offers up to €230,000 for Critical Vulnerabilities in e-Voting System"](https://www.securityweek.com/swiss-post-offers-%E2%82%AC230000-critical-vulnerabilities-e-voting-system) while catching up with the security news. 

The headline certainly caught my attention as it looked like an outlier from the regular bug bounty programs or well-known exploit contests, not only for the announced rewards but mainly because of the target. So essentially [Swiss Post](https://en.wikipedia.org/wiki/Swiss_Post), the national postal service of Switzerland, was opening to the general public a bug bounty program, using the [YesWeHack](https://yeswehack.com/programs/swiss-post-evoting) platform, intended to uncover vulnerabilities in its future e-voting system.

The first part of this blog post series will detail the approach used to analyze the Swiss Post e-voting system, as well as the first round of vulnerabilities that I reported during September/October '21.

#### Index

Introduction

Approach

Attack Surface

Vulnerabilities

1\. Insecure USB file handling during 'importOperation'

2\. Insecure 'ReturnCodeGenerationInput' signature generation allows vote manipulation

3\. Lack of consistency check allows an adversary to forge the verificationCardId in SecureLog entries

4\. Improper parsing of the request body when validating signatures for secure requests

###  

### Introduction

E-voting systems immediately raise concerns in a significant part of the security community. Not in vain, we are talking about systems that should be considered a critical infrastructure, as they are intended to support a democratic election process. Therefore, this kind of systems should provide the same guarantees regarding confidentiality, integrity and availability that current, let's oversimplify and say 'analog', election processes provide. However, security people usually don't trust computers and everyday we see examples that certainly do not facilitate changing your mind on this aspect. That said, we implicitly trust the outcome of safety-critical computer operations happening everyday in our life: from the state estimator that guarantees we have a stable power-grid, the train control systems providing a safe commute, or the avionics systems that keep you alive while flying. It doesn't mean those systems can't be hacked but supposedly they are being supported to keep up with the attacks they may face, while still successfully performing the tasks modern societies rely on. I know, it's not a perfect scenario but it's what it is.

Although e-voting may not be suitable for every country, Switzerland seems to have a long tradition on referendums, and actually, they have been already using e-voting for many years. However, when the Swiss Post e-voting platform was published, back in 2019, it faced some public scrutiny, mostly from the academic community. As a result, some significant [issues](https://www.zdnet.com/article/vulnerability-in-swiss-e-voting-system-could-have-led-to-vote-alterations/) were uncovered, so eventually Swiss Post [decided](https://www.evoting-blog.ch/en/pages/2019/swiss-post-temporarily-suspends-its-e-voting-system) to suspend the deployment of the system. The first version had been developed by [Scytl](https://en.wikipedia.org/wiki/Scytl), a spanish company specialized in electronic voting systems. After that fiasco, Swiss Post [changed](https://www.evoting-blog.ch/en/pages/2020/an-e-voting-system-for-switzerland-and-by-switzerland) their approach, acquiring the source code from Scytl and moving to a transparent, open-source focused, in-house development process, which is where they are at now.

### Approach

Swiss Post e-voting [platform](https://gitlab.com/swisspost-evoting/e-voting/e-voting) is a quite complex system, comprised of different technologies, whose codebase is approximately 150,000 lines of code, most of them Java but also Typescript for the front-end applications. Please note that a significant part of the code is dedicated to implement custom cryptographic protocols and operations. Despite this, code and component interactions are surprisingly easy to follow as everything is highly documented: cryptographic protocols, architecture, operations...The entire system seems to have been designed, defined and implemented in such a way that a 3rd party may properly audit it. Actually Swiss Post paid special attention to this aspect by requesting an external auditability [report](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/tree/master/Reports).

It's important to note that I'm not a cryptographer. As many in infosec I don't even have a degree so for me the hardest part to cover has been the highly specialized cryptography implemented in this system. At the same time I was looking for vulnerabilities I had to spend some time wrapping my head around schemes such as [Non-Interactive Zero Knowledge Proofs](https://en.wikipedia.org/wiki/Non-interactive_zero-knowledge_proof) or [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). For the reader in a similar situation, it is worth mentioning that TrailOfBits recently published a really useful initiative <https://www.zkdocs.com/> that breaks down all these concepts from a practical perspective, which facilitates the approach for non-academic security researchers.

Although Swiss Post provides the instructions to build a runnable version of the system I decided to follow a pure static analysis approach for various reasons:

  * The system is not fully implemented yet. As a result, you need to bear in mind the available source code but also the specification documents to discover and assess potential vulnerabilities. As a result, testing things against the running version does not actually guarantee that you found a real issue.
  * It's usually a pain to get everything working, so I'd rather spend 1 week looking at code than 1 week trying to build the system for no obvious advantage. Watch out, this does not mean the build instructions are either wrong or not accurate, I just didn't try.
  * Besides the code, the most interesting parts of the Swiss Post e-voting system, from the offensive perspective, are not the applications themselves, but the whole deployment (including hardened boxes, firewall rules, human operations...) which cannot be fully replicated obviously. 

Under my point of view, the following 4 documents should be used as a permanent reference to be able to properly analyze the source code. In such a complex system, with a very specific threat model and trust assumptions between components, you cannot just find something apparently bad and report it but you should be able to determine whether a potential issue is an actual vulnerability as well as its impact. 

  1. [Protocol of the Swiss Post Voting System](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/raw/master/Protocol/Swiss_Post_Voting_Protocol_Computational_proof.pdf)
  2. [System Specification](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/raw/master/System/System_Specification.pdf)
  3. [E-voting Architecture](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/blob/master/System/SwissPost_Voting_System_architecture_document.pdf)
  4. [Infrastructure white-paper](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/blob/master/Operations/Infrastructure%20whitepaper%20of%20the%20Swiss%20Post%20voting%20system.md)

### Attack Surface

The following diagram extracted from the documentation depicts a deployment overview of the system. On top of this I've added up to 5 points that represent, what I considered, the top priorities.

[![Deployment overview](https://blogger.googleusercontent.com/img/a/AVvXsEgKHSM0BU0TiyMyk9xaJDL96vqFHKzQmo_dxaR_PmTmD0oJfOtcJ94XuoCnhTh1I5z8ap5DObg42ybfWFjqmw1Qb050shT6-d7epBZEk_RR_LVsurBwhck4-K_1xYJptxioRPq1Qj_rMu-hSm7bWkg4hFncsPxswyNug6oapCBuftJeZetrYaQARbKYYg=w640-h252)](https://blogger.googleusercontent.com/img/a/AVvXsEgKHSM0BU0TiyMyk9xaJDL96vqFHKzQmo_dxaR_PmTmD0oJfOtcJ94XuoCnhTh1I5z8ap5DObg42ybfWFjqmw1Qb050shT6-d7epBZEk_RR_LVsurBwhck4-K_1xYJptxioRPq1Qj_rMu-hSm7bWkg4hFncsPxswyNug6oapCBuftJeZetrYaQARbKYYg=s1952)

  

Before elaborating them, we should talk a little bit about 'Trust assumptions', which is a key concept to understand the whole design of the system, as well as the plausible vulnerabilities that can be rewarded according to their Bug Bounty rules.

In addition to the extensive documentation, Swiss Post elaborates a little bit more about the trust assumptions [here](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/14)

  

[![Trustworthiness definition](https://blogger.googleusercontent.com/img/a/AVvXsEjU1GEW60zZh6WgOFSpt97SdEv0AMWCFO47NGzHpKVzZsWnmrIEk6J4O0BH67Yy6ImHfky3iBzxwzhkcsGCDFhwHGqA4TAY4aWZ9X46N-plLFV5t2-c6AIchpjMv_4o3Imk_2HrdfarZAxV5jfEdzvgIRsb_quh6N7g6cezP9_lhsDtfAdy8t9njp1yCQ=w640-h180)](https://blogger.googleusercontent.com/img/a/AVvXsEjU1GEW60zZh6WgOFSpt97SdEv0AMWCFO47NGzHpKVzZsWnmrIEk6J4O0BH67Yy6ImHfky3iBzxwzhkcsGCDFhwHGqA4TAY4aWZ9X46N-plLFV5t2-c6AIchpjMv_4o3Imk_2HrdfarZAxV5jfEdzvgIRsb_quh6N7g6cezP9_lhsDtfAdy8t9njp1yCQ=s1234)

Do not get me wrong, I understand that the trustworthiness concept is required to model the cryptographic protocols that support the entire system but we cannot forget either that in the real-world this means absolutely nothing. Malicious actors are not going to refrain from attacking a component because it has been labeled as 'trustworthy' so this situation slightly reminds me of the [spherical cow metaphor](https://en.wikipedia.org/wiki/Spherical_cow). Actually, one of the vulnerabilities herein described (ID#1) allows to fully compromise the SDM, a key trustworthy component. 

Anyway, these are the rules so we have to play with them. The following image shows the trust assumptions for all the components and humans involved in the election process. A more elaborated definition can be found in the [Protocol of the Swiss Post Voting System](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/raw/master/Protocol/Swiss_Post_Voting_Protocol_Computational_proof.pdf) (2.1 'Parties and Channels').

[![](https://blogger.googleusercontent.com/img/a/AVvXsEghbY-XKz5ipnOCEyw4Dnwr68sm9Wi66z6Gy_1VwUswPLUO9MXdusfk80PQpSeSaUX7nMXIwdF9igWWNVE_3R10BV0QaBIqb7RoVLbCl7koJXXRi12Ylef17BHelLKHjWWe1-hnHziShLh1mZbrYCFfrfl2xl0mGy6qVMeElmSHycbxApbyHUkK7-O-JQ=w640-h322)](https://blogger.googleusercontent.com/img/a/AVvXsEghbY-XKz5ipnOCEyw4Dnwr68sm9Wi66z6Gy_1VwUswPLUO9MXdusfk80PQpSeSaUX7nMXIwdF9igWWNVE_3R10BV0QaBIqb7RoVLbCl7koJXXRi12Ylef17BHelLKHjWWe1-hnHziShLh1mZbrYCFfrfl2xl0mGy6qVMeElmSHycbxApbyHUkK7-O-JQ=s1764)

  

Now we are in a position to dig deeper into the top 5 priorities for the attack surface (the order is not relevant) we just highlighted in the diagram above.

#### **1\. Air Gapped components connected using USB keys**

The system architecture document provides the following self-explanatory diagram. Please also note that according to the threat model, the administrators are considered 'untrustworthy' but the SDM is a key trustworthy element in the e-voting system. Basically we are mixing potentially malicious actors and USB keys so I don't think it is really needed to elaborate more on why this should be considered a priority.  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhYX9lLZbBRuXlQYjKCTVIA7SO1X4j_msWWu0mgaBS78b4prZXKvIMqTBltYuCdMCA-39V9VXJH4NkmBkWYDhhS6yKfI-Kn6BZ9kE2lvoXK-K-XRVU_pm76yu3A5ranUjHUBD5KaeB0GTAQ0wSCbJhHSYFqQklMV6yKwx5-nLPPa3QMWWCrKnVQf9D2uA=w640-h574)  
](https://blogger.googleusercontent.com/img/a/AVvXsEhYX9lLZbBRuXlQYjKCTVIA7SO1X4j_msWWu0mgaBS78b4prZXKvIMqTBltYuCdMCA-39V9VXJH4NkmBkWYDhhS6yKfI-Kn6BZ9kE2lvoXK-K-XRVU_pm76yu3A5ranUjHUBD5KaeB0GTAQ0wSCbJhHSYFqQklMV6yKwx5-nLPPa3QMWWCrKnVQf9D2uA=s1918)

  

**2\. SDM Online Instance**

The Secure Data Manager Online instance implements a significant part of the core functionality the election event relies on. In addition to this, it is communicating with trustworthy components through untrustworthy ones. I came up with the following diagram to illustrate these interactions. 

[![SDM interactions](https://blogger.googleusercontent.com/img/a/AVvXsEiLNmgJ3xSIuIsZEzjoHp6y71RhbUPnOtyCAYS4hmEEz8lSUfpYyXrriPEUpT_Up-bst8euUaIlMkd4VhteEo2Jia1yoAKstGRkHHDbJBJtdsSbjuo1mzYO3xUEmVunjYRacnma4GI6dG0LDwoj-ZzpxgmSqxlAu9eMlGaoQ5-o6DN-Z4cBVeDKZh6ieg=w640-h252)](https://blogger.googleusercontent.com/img/a/AVvXsEiLNmgJ3xSIuIsZEzjoHp6y71RhbUPnOtyCAYS4hmEEz8lSUfpYyXrriPEUpT_Up-bst8euUaIlMkd4VhteEo2Jia1yoAKstGRkHHDbJBJtdsSbjuo1mzYO3xUEmVunjYRacnma4GI6dG0LDwoj-ZzpxgmSqxlAu9eMlGaoQ5-o6DN-Z4cBVeDKZh6ieg=s1952)

  

#### **3\. Voting Server**

The Voting Server is the gateway to all the applications that need to perform voting process operations. It is comprised of different microservices, each of them is responsible for one part of the voting process, i.e., authentication, election information, vote verification, etc.The voting server also receives, processes, and stores the encrypted votes.

It is considered untrustworthy so it is assumed that can be compromised. Despite this, it is important to analyze the voting server, especially the Orchestrator, which handles interactions with trustworthy components so it plays an important role in the channel security implementation as I'm depicting in the following diagram.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh7qnslV8CcBBnNaTGYDB5GI_vUoP3dndHQm1z17NXzj0LtdmkgXbpo4r8zhpMg_vVG2kFAf7QipwXSzzRekje7KIiMqHkbTi3b87xAcifS_Nkw5jpIaTquLCY6Vq6bqLSF2qcjXIPD5lES6Re4hNzls3GLcUjLC3Lk0TQhHmbGKmvUsvR7fVaet_90PA=w640-h334)](https://blogger.googleusercontent.com/img/a/AVvXsEh7qnslV8CcBBnNaTGYDB5GI_vUoP3dndHQm1z17NXzj0LtdmkgXbpo4r8zhpMg_vVG2kFAf7QipwXSzzRekje7KIiMqHkbTi3b87xAcifS_Nkw5jpIaTquLCY6Vq6bqLSF2qcjXIPD5lES6Re4hNzls3GLcUjLC3Lk0TQhHmbGKmvUsvR7fVaet_90PA=s1764)

  

#### **4\. Control Components**

In the system architecture document (5.5 Control Components) we can find the following diagram

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj03fQHslQ7tpjva8C1zS6dQnjuYmDTXvv_Iv0M6Ai2W1-BV-PrajTmYWLVQIqXdMPUSA06ocREkEVk9qkfUkfd971FM_XRl1tbLnxcbAjLxQL-N8QfIopbC_ckbB5NMoqbVmEjY9gCiP33576cMXSD3yw8sGYVWK2BFByViV50LyuHJRUf55EnvDqlBQ=w640-h544)](https://blogger.googleusercontent.com/img/a/AVvXsEj03fQHslQ7tpjva8C1zS6dQnjuYmDTXvv_Iv0M6Ai2W1-BV-PrajTmYWLVQIqXdMPUSA06ocREkEVk9qkfUkfd971FM_XRl1tbLnxcbAjLxQL-N8QfIopbC_ckbB5NMoqbVmEjY9gCiP33576cMXSD3yw8sGYVWK2BFByViV50LyuHJRUf55EnvDqlBQ=s1868)

  

In addition to the SDM, the Control Components implement the most critical logic to guarantee the integrity of the election event. As a result, it is important to analyze both the interactions with the untrustworthy components (through the RabbitMQ cluster) and those parts of the underlying cryptographic protocol they sustain.

**5\. Voting Client**

The System Specification documents describe the Voting client. 

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiDdc2Nnr4878Il8jO683hUrbUw9FuiQ0D6upZ67pphMwEtxFxfXdt7kyXqmweKHvLsdEznez9r-JHk1viNzBih1JiqbulgDao60edumI7-87iEUb-qtFbx-GIK7qNXfXta5WPAbrH2WMiJW6Rd3Vy_56pO-us11Y0PPfX869WH6fZrgq9cjG4YcCZHHA=w640-h90)](https://blogger.googleusercontent.com/img/a/AVvXsEiDdc2Nnr4878Il8jO683hUrbUw9FuiQ0D6upZ67pphMwEtxFxfXdt7kyXqmweKHvLsdEznez9r-JHk1viNzBih1JiqbulgDao60edumI7-87iEUb-qtFbx-GIK7qNXfXta5WPAbrH2WMiJW6Rd3Vy_56pO-us11Y0PPfX869WH6fZrgq9cjG4YcCZHHA=s1772)

It is important to understand the implications of a potentially compromised voting client, although it is assumed, as well as the attack surface the voting server exposes to a malicious voting client.

### **Vulnerabilities**

The following table summarizes the first round of vulnerabilities that I reported to [Swiss Post](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/32) via the YesWeHack Bug Bounty Platform during September and October. A second blog post will cover the remaining bugs that are still being analyzed. Once all the reported vulnerabilities have been addressed by Swiss Post I will also be in a better position to draw some final conclusions. 

  

I'm only including those vulnerabilities that may contribute with something interesting for the reader, as vulnerabilities such as #4 are basically well-known issues (ObjectInputStream's readObject()).

  
ID| Title| Reward (€)| Attack Surface Areas*| CVSS  
---|---|---|---|---  
1| SDM - Insecure USB file handling during 'importOperation'| 15000| 1| 7.2 - High  
CVSS:3.0/AV:P/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H  
2| Insecure 'ReturnCodeGenerationInput' signature generation allows vote manipulation| 4000| 2 & 4| 5.4 - Medium  
CVSS:3.0/AV:A/AC:H/PR:H/UI:N/S:C/C:N/I:N/A:H  
3| Lack of anti-replay protection for Signed Request| 2000| 3| 3.1 - Low  
CVSS:3.0/AV:A/AC:H/PR:H/UI:N/S:U/C:N/I:L/A:L  
4| Insecure deserialization of untrusted input may lead to RCE in the 'Vote Verification' microservice.| 1200| 3| 4.2 - Medium  
CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:L/A:L/E:U/RC:U  
5| Lack of consistency check allows an adversary to forge the verificationCardId in SecureLog entries| 1000| 4| 3.8 - Low  
CVSS:3.0/AV:L/AC:H/PR:H/UI:N/S:U/C:N/I:H/A:N/E:U  
6| Uncaught exception in the Sanitize filter may prevent proper sanitization of a query string.| 200| 3| 3.7 - Low  
CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L  
7| Improper parsing of the request body when validating signatures for secure requests.| 100| 3| 2.6 - Low  
CVSS:3.0/AV:A/AC:H/PR:L/UI:N/S:U/C:N/I:L/A:N  
  
* The 'attack surface areas' column refers to the top 5 priorities we previously elaborated.

  

  

### #1 - SDM - Insecure USB file handling during 'importOperation'

**References**

[1] <https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/blob/master/Operations/Recommendation_Safety_Measures_SDM.md>

[2]<https://www.bk.admin.ch/dam/bk/en/dokumente/pore/OEV_draft%20for%20consultation%202021.pdf.download.pdf/OEV_draft%20for%20consultation%202021.pdf>

[3]<https://gitlab.com/swisspost-evoting/e-voting/e-voting/-/issues/5>

  

**  
**

**_Description_**

  

The communication between the online and the offline instances of the SDM is implemented via an import/export functionality using a USB stick. In the documentation provided there is no clear indication of the trust level defined for the USB key used in these operations. However, based on the documentation, the source code analyzed and the common threat model applied to the Swiss Post e-voting system it is reasonable to assume that the USB drive itself is not trustworthy(*). Therefore, as stated in the documentation, when malicious actors try to inject corrupted data that operation should be prevented by cryptographic means. 

  

Also, according to the 'System Specification' document Canton's Electoral Board Administrators accessing the SDM are considered untrustworthy. However, the attack herein explained does not inherently require a malicious administrator but merely a malicious USB drive, which may have been surreptitiously supplied to trustworthy staff. It is worth clarifying that the concept of a malicious USB drive described in this attack scenario is not related to external attacks such as a USB key posing as a HID device to inject keystrokes once connected to the computer or similar. The malicious USB drive concept assumed in this attack scenario is limited to a regular USB mass storage device loaded with specially crafted files and a custom directory structure.

  

Additionally, it is worth mentioning that the the attacker-controlled USB mass storage may have been programmed in such a way that the malicious content is only served when it detects certain file requests. For example, when the USB drive is regularly mounted and accessed it provides a specific file system, but when the USB mass storage device receives certain file requests (such as the one requested by the Import operation in the SDM) it will provide the specific malicious content, in order to not disclose the malicious payload when mounted in any computer different than the target. This kind of advanced scenarios are suitable for sophisticated malicious actors trying to undermine a nation-wide e-voting system.

  

The SDM Backend implements an endpoint for the front-end to perform an 'Import' operation in order to copy files from the USB to a local SDM directory. The vulnerability lies in the way this operation has been implemented, as there is no validation of the files that are copied, allowing to overwrite multiple files in the SDM directory, including the platform's Trusted CA. Among other things, this allows to bypass the subsequent signature verification of the imported files, overwrite key materials and run arbitrary commands through custom 'phase plugins' commands. As a result, this scenario allows malicious actors to fully compromise the SDM, thus having the ability to compromise the integrity of the election process.

  

* _Swiss Post indicated that the USB key and the SDM should be considered as a unit, thus implicitly granting the trustworthy consideration also to the USB key._

  

**_Technical Analysis_**

  

At line 255 the '_importData_ ' operation starts.

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/web-services/src/main/java/ch/post/it/evoting/sdm/ws/application/OperationsController.java
  
  
  242:  @PostMapping(value = "/import")
  243:  @ApiOperation(value = "Import operation service")
  244:  @ApiResponses(value = { @ApiResponse(code = 404, message = "Not Found"), @ApiResponse(code = 403, message = "Forbidden"),
  245:  @ApiResponse(code = 500, message = "Internal Server Error") })
  246:  public ResponseEntity<OperationResult> importOperation(
  247:  @RequestBody
  248:  final OperationsData request) {
  249: 
  250:  if (StringUtils.isEmpty(request.getPath())) {
  251:  return handleIncompleteRequest();
  252:  }
  253: 
  254:  try {
  255:  exportImportService.importData(request.getPath());
  256:  exportImportService.verifySignaturesOnImport();
  257:  exportImportService.importDatabase();
  258: 
  259:  } catch (IOException e) {
  260:  OperationsOutputCode code = OperationsOutputCode.ERROR_IO_OPERATIONS;
  261:  return handleException(e, code.value());
  262:  } catch (InvalidParameterException e) {
  263:  OperationsOutputCode code = OperationsOutputCode.MISSING_PARAMETER;
  264:  return handleInvalidParamException(e, code.value());
  265:  } catch (CMSException | SignatureException e) {
  266:  OperationsOutputCode code = OperationsOutputCode.SIGNATURE_VERIFICATION_FAILED;
  267:  return handleException(e, code.value());
  268:  } catch (GeneralCryptoLibException e) {
  269:  OperationsOutputCode code = OperationsOutputCode.CHAIN_VALIDATION_FAILED;
  270:  return handleException(e, code.value());
  271:  } catch (CertificateException e) {
  272:  OperationsOutputCode code = OperationsOutputCode.ERROR_CERTIFICATE_PARSING;
  273:  return handleException(e, code.value());
  274:  } catch (ConsistencyCheckException e) {
  275:  OperationsOutputCode code = OperationsOutputCode.CONSISTENCY_ERROR;
  276:  return handleException(e, code.value());
  277:  } catch (Exception e) {
  278:  OperationsOutputCode code = OperationsOutputCode.GENERAL_ERROR;
  279:  return handleException(e, code.value());
  280:  }
  281:  return new ResponseEntity<>(HttpStatus.OK);
  282:  }

  

At line 475 the '_usbFolder_ ' is generated based on the '_usbElectionPath_ '. It is worth pointing out that there is no check to validate whether the resulting '_usbFolder_ ' is actually pointing to a USB-based file system.

  

At line 478 the '_copyFolder_ ' method is invoked to copy the contents from the 'USB' to the SDM folder. The provided filter does not implement a whitelist of the files that should be copied. As a result, the entire USB drive will be replicated to the 'SDM' directory, creating directories if required (line 488), and overwriting files when they exist as the 'COPY_OPTIONS' used in line 503 are defined as '_COPY_OPTIONS = { StandardCopyOption.REPLACE_EXISTING, StandardCopyOption.COPY_ATTRIBUTES };_ '

  

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ExportImportService.java
  
  
  467:  /**
  468:  * Import all files from selected exported election event to user/sdm
  469:  *
  470:  * @param usbElectionPath path to selected exported election event
  471:  * @throws IOException
  472:  */
  473:  public void importData(String usbElectionPath) throws IOException {
  474:  Filter<Path> filter = file -> true;
  475:  Path usbFolder = absolutePathResolver.resolve(usbElectionPath);
  476:  Path sdmFolder = pathResolver.resolve(Constants.SDM_DIR_NAME);
  477: 
  478:  copyFolder(usbFolder, sdmFolder, filter, false);
  479:  }
  480: 
  481:  private void copyFolder(Path source, Path dest, Filter<Path> filter, boolean isExportingElectionInformationFolders) throws IOException {
  482:  if (!Files.exists(source)) {
  483:  return;
  484:  }
  485: 
  486:  if (Files.isDirectory(source)) {
  487:  if (!Files.exists(dest)) {
  488:  Files.createDirectories(dest);
  489:  LOGGER.info("Directory created from {} to {}", source, dest);
  490:  }
  491:  Filter<Path> electionInformationFilter = filter;
  492:  try (DirectoryStream<Path> stream = Files.newDirectoryStream(source, electionInformationFilter)) {
  493:  for (Path file : stream) {
  494:  if (isExportingElectionInformationFolders) {
  495:  electionInformationFilter = getElectionInformationFilter(file);
  496:  }
  497:  copyFolder(file, dest.resolve(file.getFileName()), electionInformationFilter, isExportingElectionInformationFolders);
  498:  }
  499:  }
  500:  } else {
  501:  try {
  502: 
  503:  copy(source, dest, COPY_OPTIONS);
  504: 
  505:  LOGGER.info("File copied from {} to {}", source, dest);
  506:  } catch (IOException e) {
  507:  LOGGER.error("Error copying files from {} to {}", source, dest, e);
  508:  }
  509:  }
  510:  }

  

At this point, the files have been copied from the 'USB' folder to the SDM directory, potentially overwriting any directory/file hanging from the '_c:\%USERS%\%USERNAME%\sdm_ ' directory structure.

  

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/web-services/src/main/java/ch/post/it/evoting/sdm/ws/application/OperationsController.java
  
  
  256:  exportImportService.verifySignaturesOnImport();
  257:  exportImportService.importDatabase();

'_OperationsController_ ' will then try to verify the signature of the expected imported files ('_db_dump.json_ ' and '_elections_config.json_ ') by calling '_verifySignaturesOnImport_ '

  

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ExportImportService.java
  
  
  658:  /**
  659:  * Verifies the signature of both db dump and elections config files.
  660:  *
  661:  * @throws IOException
  662:  * @throws CMSException
  663:  * @throws CertificateException
  664:  * @throws GeneralCryptoLibException
  665:  */
  666:  public void verifySignaturesOnImport() throws IOException, CMSException, CertificateException, GeneralCryptoLibException {
  667:  signaturesVerifierService.verifyPkcs7(getPathOfDumpDatabase(), getPathOfDumpDatabaseSignature());
  668:  signaturesVerifierService.verifyPkcs7(getPathOfElectionsConfig(), getPathOfElectionsConfigSignature());
  669:  }

  

However, this verification relies on the deployed 'Trusted CA' which could have been replaced by the previous USB copy operation as it is located at '_CONFIG_FILES_BASE_DIR_ ' (_public static final String CONFIG_FILES_BASE_DIR = SDM_DIR_NAME + "/config";_). As a result, now the trusted CA, used across the codebase to validate multiple cryptographic operations, is controlled by the attacker so '_signatureVerifier.verifyPkcs7_ ' can be effectively bypassed.

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/SignaturesVerifierServiceImpl.java
  
  
  66:  /**
  67:  * Verifies a P7 signature with the trusted chain of the SDM
  68:  *
  69:  * @param filePath
  70:  * @param signaturePath
  71:  * @return
  72:  * @throws IOException
  73:  * @throws CMSException
  74:  * @throws GeneralCryptoLibException
  75:  * @throws CertificateException
  76:  */
  77:  @Override
  78:  public Certificate[] verifyPkcs7(Path filePath, Path signaturePath)
  79:  throws IOException, CMSException, GeneralCryptoLibException, CertificateException {
  80:  Path trustedCAPath = pathResolver.resolve(Constants.CONFIG_FILES_BASE_DIR, Constants.CONFIG_FILE_NAME_TRUSTED_CA_PEM);
  81: 
  82:  return signatureVerifier.verifyPkcs7(filePath, signaturePath, trustedCAPath);
  83: 
  84:  }

  

The ability to overwrite arbitrary files in the 'SDM' directory allows to compromise the critical items and cryptographic materials required to properly run the election event.

  

Also, it is possible to overwrite/create custom 'phase' plugins to inject arbitrary commands, thus gaining code execution outside the JVM.

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/web-services/src/main/java/ch/post/it/evoting/sdm/ws/application/OperationsController.java
  
  
  284:  protected List<String> getCommands(PhaseName phaseName) throws IOException, JAXBException, SAXException, XMLStreamException {
  285: 
  286:  Path pluginXmlPath = pathResolver.resolve(Constants.SDM_DIR_NAME).resolve(PLUGIN_FILE_NAME);
  287:  if (!pluginXmlPath.toFile().exists()) {
  288:  pluginXmlPath = pathResolver.resolve(Constants.SDM_DIR_NAME).resolve(Constants.SDM_CONFIG_DIR_NAME).resolve(PLUGIN_FILE_NAME);
  289:  if (!pluginXmlPath.toFile().exists()) {
  290:  LOGGER.error("The plugin.xml file is not found");
  291:  return new ArrayList<>();
  292:  }
  293:  }
  294: 
  295:  Plugins plugins = XmlObjectsLoader.unmarshal(pluginXmlPath);
  296:  PluginSequenceResolver pluginSequence = new PluginSequenceResolver(plugins);
  297:  return pluginSequence.getActionsForPhase(phaseName);
  298:  }

  

### #2 - Insecure 'ReturnCodeGenerationInput' signature generation allows vote manipulation

####  _Description_

During the 'Configuration Phase' (Swiss Post Voting Protocol Computational Proof@11.1) the Setup Component generates the verification card key pair (Kid, kid) for each voter, as it is specified in '_GenVerDat_ ' (Swiss Post Voting Protocol Computational Proof@12.1.1.4). Kid, together with other materials, is then sent to the CCRs through the orchestrator (part of the voting server, which is defined untrustworthy by the threat model) to let the CCRj complete the '_GenEncLongCodeShares j_' functionality.

  

The payload, that includes the voters' Kid, sent from the Setup Component to the CCRj is signed by the Administrator Board (ABsk) as it is going through the orchestrator (untrustworthy) so the CCRj (at least 1 of them is trustworthy) can validate its signature before proceeding with the '_GenEncLongCodeShares_ ' logic. The vulnerability lies in the way this signature is generated and validated, which is based on '_ch.post.it.evoting.cryptoprimitives.hashing.Hashable_ ', since the list of '_ElGamalMultiRecipientPublicKey_ ' that holds the voters' Kid in the payload is not covered by the signature.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgqMsPE3rtuSD0qIFhmTMar-2BFSxN_jLfUOZDIrQRh26g_YkjnJ3EOVJWc49oyshYZWhwK0kPClqkLvx-mTIqVU9BG51QLDjXEtfPYaO5QuxGHNFm2j9mTHrZpb_ND6mpurtcfr037BsUZO7yJw50PDlvW7t5sGMwDfG8HrNuMUGA_GMhbwGW0qZ_29w=w640-h392)](https://blogger.googleusercontent.com/img/a/AVvXsEgqMsPE3rtuSD0qIFhmTMar-2BFSxN_jLfUOZDIrQRh26g_YkjnJ3EOVJWc49oyshYZWhwK0kPClqkLvx-mTIqVU9BG51QLDjXEtfPYaO5QuxGHNFm2j9mTHrZpb_ND6mpurtcfr037BsUZO7yJw50PDlvW7t5sGMwDfG8HrNuMUGA_GMhbwGW0qZ_29w=s1778)

  

As a result, a malicious voting server will be able to inject arbitrary public keys Kid (both during 'configuration phase' and 'voting phase') for arbitrary voters, which breaks a crucial safeguard against voting manipulation implemented in the form of Non-Interactive Zero-Knowledge Proofs (NIZKP from now on) during the 'Voting phase'. Let's see how:

  

We use the [Protocol of the Swiss Post Voting System](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/raw/master/Protocol/Swiss_Post_Voting_Protocol_Computational_proof.pdf) as the reference to consult how NIZKP have been implemented.

  

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg7ElXyss_KDRssyh3Iy7_0ZQ-ZpPwlrMLdBaCZUbnBOAwfVDLrViAQ6NYBUvp75CfsW9t0-8uM--dua4AfAqpV8pugmQRuMDJU-HIeneX_Z3iRl6iAzr3q5qgM4w_MlLrfIaVxzcHV0f0HOVVO9UoS6tK-23Hy24K38FFaCEAdYU2KlbnLB4Wu3PBmCg=w640-h274)](https://blogger.googleusercontent.com/img/a/AVvXsEg7ElXyss_KDRssyh3Iy7_0ZQ-ZpPwlrMLdBaCZUbnBOAwfVDLrViAQ6NYBUvp75CfsW9t0-8uM--dua4AfAqpV8pugmQRuMDJU-HIeneX_Z3iRl6iAzr3q5qgM4w_MlLrfIaVxzcHV0f0HOVVO9UoS6tK-23Hy24K38FFaCEAdYU2KlbnLB4Wu3PBmCg=s1762)

  

  

...

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj6iQSHJqe5jYNt5CVT7C9MXD7j6XkMIva1gcjNJ1QJ8zX94f9nxQ943owidZrLSV40Z84HQC2uuN7VBT4tCaCWHs0vs3a6GscyKLluVsDx0KzIzw3ccO-XdCxm1Xaha5oqJwLZakRpDtyUYirP5US1_lYeP2RiEVwqEP8WytGETQe8V6T0NIsoJHGudQ=w640-h384)](https://blogger.googleusercontent.com/img/a/AVvXsEj6iQSHJqe5jYNt5CVT7C9MXD7j6XkMIva1gcjNJ1QJ8zX94f9nxQ943owidZrLSV40Z84HQC2uuN7VBT4tCaCWHs0vs3a6GscyKLluVsDx0KzIzw3ccO-XdCxm1Xaha5oqJwLZakRpDtyUYirP5US1_lYeP2RiEVwqEP8WytGETQe8V6T0NIsoJHGudQ=s1700)

  

  1. We have that E1 = (c1,0,c1,1), the encrypted product of the selected voted options.
  2. We have that E1 is E1 exponentiated to the private key kid, E1=(ckid1,0, ckid1,1)
  3. We have an ElGamal Public Key Kid = gx
  4. We have VerifyExp(((p,q,g,E1),**(K id,E1)**),πExp, aux U {vcdid})

If the attacker is able to inject a malicious Public key K'id = g**x'** into the '_verificationCardPublicKeyExtendedRepository_ ', then a forged vote can be created in such a way that the bases (g, E1) will be exponentiated to the same arbitrary exponent x', instead of the original x private key for that specific vcdid key pair, but still satisfying **(K id, E1)** as Kid = g**x'** and E1 =(c**x'** 1,0, c**x'** 1,1).

  

The ability to inject arbitrary verification card public keys can be used to create especially crafted votes that satisfy the CCRj πballot(πExp, πEqEnc) NIZKP validation during the voting phase. A malicious voting client could then forge arbitrary votes using arbitrary ElGamal key pairs (Kid,kid) as long as they conform with the '_gparams_ ' (the established cyclic group Gq of order 'q' with generator 'g' for the current election event). 

  

The only safeguard that prevented this attack from being successful was the partial Choice Return Codes Allow List LpCC.  When this vulnerability was reported this safeguard was not implemented in the code yet but it was already defined by the specification.

  

#### _Technical Analysis_

At line 267 we can see how the vector of Kid generated during the '_GenVerDat_ ' is part of the payload, which is both persisted on the SDM and sent to the CCRj.

At line 279 '_signPayload_ ' is invoked.

At line 310 the hash of the payload is generated and then signed at line 311.

  

  
  
  File: e-voting-master/secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/GenerateVerificationData.java
  
  
  258:  private ReturnCodeGenerationRequestPayload createRequestPayload(final VerificationCardSet verificationCardSet, final int chunkId,
  259:  final GenVerDatOutput genVerDatOutput) throws PayloadSignatureException {
  260: 
  261:  // Create payload.
  262:  final List<ReturnCodeGenerationInput> returnCodeGenerationInputList = new ArrayList<>();
  263:  for (int j = 0; j < genVerDatOutput.size(); j++) {
  264:  final String verificationCardId = genVerDatOutput.getVerificationCardIds().get(j);
  265:  final ElGamalMultiRecipientCiphertext confirmationKey = genVerDatOutput.getEncryptedHashedConfirmationKeys().get(j);
  266:  final ElGamalMultiRecipientCiphertext partialChoiceCode = genVerDatOutput.getEncryptedHashedPartialChoiceReturnCodes().get(j);
  267:  final ElGamalMultiRecipientPublicKey verificationCardPublicKey = genVerDatOutput.getVerificationCardKeyPairs().get(j).getPublicKey();
  268: 
  269:  returnCodeGenerationInputList
  270:  .add(new ReturnCodeGenerationInput(verificationCardId, confirmationKey, partialChoiceCode, verificationCardPublicKey));
  271:  }
  272:  final ReturnCodeGenerationRequestPayload payload = new ReturnCodeGenerationRequestPayload(tenantId, verificationCardSet.getElectionEventId(),
  273:  verificationCardSet.getVerificationCardSetId(), chunkId, genVerDatOutput.getGroup(), returnCodeGenerationInputList,
  274:  new CombinedCorrectnessInformation(getBallot(verificationCardSet.getBallotBoxId(), verificationCardSet.getElectionEventId())));
  275: 
  276:  // Sign the payload.
  277:  LOGGER.debug("Signing payload for verificationCardSet {} and chunkId {}...", verificationCardSet.getVerificationCardSetId(), chunkId);
  278:  try {
  279:  signPayload(payload);
  280:  } catch (CertificateManagementException | PayloadSignatureException e) {
  281:  throw new PayloadSignatureException(e);
  282:  }
  283: 
  284:  LOGGER.debug("Payload successfully created and signed for verificationCardSet {} and chunkId {}.",
  285:  verificationCardSet.getVerificationCardSetId(), chunkId);
  286: 
  287:  return payload;
  288:  }
  289: 
  290:  /**
  291:  * Signs a return code generation request payload.
  292:  *
  293:  * @param payload the payload to sign
  294:  * @throws PayloadSignatureException  If an error occurs while getting the admin board's signing key.
  295:  * @throws CertificateManagementException If an error occurs while getting the admin board's certificate chain.
  296:  */
  297:  private void signPayload(final ReturnCodeGenerationRequestPayload payload) throws PayloadSignatureException, CertificateManagementException {
  298:  // Get the admin board's signing key.
  299:  final PrivateKey signingKey;
  300:  try {
  301:  signingKey = PemUtils.privateKeyFromPem(administrationBoardPrivateKeyPEM);
  302:  } catch (GeneralCryptoLibException e) {
  303:  throw new PayloadSignatureException(e);
  304:  }
  305: 
  306:  // Get the admin board's certificate chain.
  307:  final X509Certificate[] certificateChain = adminBoardService.getCertificateChain(adminBoardId);
  308: 
  309:  // Hash and sign the payload.
  310:  final byte[] payloadHash = hashService.recursiveHash(payload);
  311:  final CryptolibPayloadSignature signature = payloadSignatureService.sign(payloadHash, signingKey, certificateChain);
  312:  payload.setSignature(signature);
  313:  }

  

As we have seen above, '_hashService.recursiveHash_ ' is used to generate the hash of the payload. This method receives a list of '_Hashable_ ' objects, iterating over them recursively to generate the hash that will be signed.

  

  
  
  File: e-voting-master/crypto-primitives-master/src/main/java/ch/post/it/evoting/cryptoprimitives/hashing/HashService.java
  
  
  082:  public byte[] recursiveHash(final Hashable... values) {
  083:  checkNotNull(values);
  084:  checkArgument(Arrays.stream(values).allMatch(Objects::nonNull), "Values contain a null value which cannot be hashed.");
  085:  checkArgument(values.length != 0, "Cannot hash no values.");
  086: 
  087:  if (values.length > 1) {
  088:  final HashableList v = HashableList.from(ImmutableList.copyOf(values));
  089:  return recursiveHash(v);
  090:  } else {
  091:  final Hashable value = values[0];
  092: 
  093:  if (value instanceof HashableByteArray) {
  094:  final byte[] w = ((HashableByteArray) value).toHashableForm();
  095:  return this.hashFunction.apply(w);
  096:  } else if (value instanceof HashableString) {
  097:  final String w = ((HashableString) value).toHashableForm();
  098:  return this.hashFunction.apply(ConversionService.stringToByteArray(w));
  099:  } else if (value instanceof HashableBigInteger) {
  100:  final BigInteger w = ((HashableBigInteger) value).toHashableForm();
  101:  checkArgument(w.compareTo(BigInteger.ZERO) >= 0);
  102:  return this.hashFunction.apply(integerToByteArray(w));
  103:  } else if (value instanceof HashableList) {
  104:  final ImmutableList<? extends Hashable> w = ((HashableList) value).toHashableForm();
  105: 
  106:  checkArgument(!w.isEmpty(), "Cannot hash an empty list.");
  107: 
  108:  if (w.size() == 1) {
  109:  return recursiveHash(w.get(0));
  110:  }
  111: 
  112:  final byte[][] subHashes = w.stream()
  113:  .map(this::recursiveHash)
  114:  .toArray(byte[][]::new);
  115:  final byte[] concatenatedSubHashes = Bytes.concat(subHashes);
  116: 
  117:  return this.hashFunction.apply(concatenatedSubHashes);
  118:  } else {
  119:  throw new IllegalArgumentException(String.format("Object of type %s cannot be hashed.", value.getClass()));
  120:  }
  121:  }
  122:  }

  

However, if we look at line 105 in the '_toHashableForm_ ' implementation for the payload's class '_ReturnCodeGenerationInput_ ', we can see that all properties but '_verificationCardPublicKey_ ' are included. As a result, the vector of voters' public keys (Kid) is not actually computing for the hash so it can be manipulated.

  

  
  
  File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ReturnCodeGenerationInput.java
  
  
  001: /*
  002:  * (c) Copyright 2021 Swiss Post Ltd.
  003:  */
  004: package ch.post.it.evoting.domain.returncodes;
  005: 
  006: import static com.google.common.base.Preconditions.checkNotNull;
  007: 
  008: import java.util.Objects;
  009: 
  010: import com.fasterxml.jackson.annotation.JsonCreator;
  011: import com.fasterxml.jackson.annotation.JsonProperty;
  012: import com.fasterxml.jackson.annotation.JsonPropertyOrder;
  013: import com.google.common.collect.ImmutableList;
  014: 
  015: import ch.post.it.evoting.cryptoprimitives.elgamal.ElGamalMultiRecipientCiphertext;
  016: import ch.post.it.evoting.cryptoprimitives.elgamal.ElGamalMultiRecipientPublicKey;
  017: import ch.post.it.evoting.cryptoprimitives.hashing.Hashable;
  018: import ch.post.it.evoting.cryptoprimitives.hashing.HashableList;
  019: import ch.post.it.evoting.cryptoprimitives.hashing.HashableString;
  020: 
  021: @JsonPropertyOrder({ "verificationCardId", "encryptedHashedSquaredConfirmationKey", "encryptedHashedSquaredPartialChoiceReturnCodes" })
  022: public class ReturnCodeGenerationInput implements HashableList {
  023: 
  024:  @JsonProperty
  025:  private final String verificationCardId;
  026: 
  027:  @JsonProperty
  028:  private final ElGamalMultiRecipientCiphertext encryptedHashedSquaredConfirmationKey;
  029: 
  030:  @JsonProperty
  031:  private final ElGamalMultiRecipientCiphertext encryptedHashedSquaredPartialChoiceReturnCodes;
  032: 
  033:  @JsonProperty
  034:  private final ElGamalMultiRecipientPublicKey verificationCardPublicKey;
  035: 
  036:  /**
  037:  * Creates an object used as the input for return code (choice return codes and vote cast return codes) generation requests.
  038:  *
  039:  * @param verificationCardId  the verification card identifier.
  040:  * @param encryptedHashedSquaredConfirmationKey  the encrypted hashed squared confirmation key.
  041:  * @param encryptedHashedSquaredPartialChoiceReturnCodes the encrypted hashed squared partial choice return codes.
  042:  * @param verificationCardPublicKey  the verification card public key
  043:  */
  044:  @JsonCreator
  045:  public ReturnCodeGenerationInput(
  046:  @JsonProperty("verificationCardId")
  047:  final String verificationCardId,
  048:  @JsonProperty("encryptedHashedSquaredConfirmationKey")
  049:  final ElGamalMultiRecipientCiphertext encryptedHashedSquaredConfirmationKey,
  050:  @JsonProperty("encryptedHashedSquaredPartialChoiceReturnCodes")
  051:  final ElGamalMultiRecipientCiphertext encryptedHashedSquaredPartialChoiceReturnCodes,
  052:  @JsonProperty("verificationCardPublicKey")
  053:  final ElGamalMultiRecipientPublicKey verificationCardPublicKey) {
  054: 
  055:  checkNotNull(verificationCardId);
  056:  checkNotNull(encryptedHashedSquaredConfirmationKey);
  057:  checkNotNull(encryptedHashedSquaredPartialChoiceReturnCodes);
  058:  checkNotNull(verificationCardPublicKey);
  059: 
  060:  this.verificationCardId = verificationCardId;
  061:  this.encryptedHashedSquaredConfirmationKey = encryptedHashedSquaredConfirmationKey;
  062:  this.encryptedHashedSquaredPartialChoiceReturnCodes = encryptedHashedSquaredPartialChoiceReturnCodes;
  063:  this.verificationCardPublicKey = verificationCardPublicKey;
  064:  }
  065: 
  066:  public String getVerificationCardId() {
  067:  return verificationCardId;
  068:  }
  069: 
  070:  public ElGamalMultiRecipientCiphertext getEncryptedHashedSquaredConfirmationKey() {
  071:  return encryptedHashedSquaredConfirmationKey;
  072:  }
  073: 
  074:  public ElGamalMultiRecipientCiphertext getEncryptedHashedSquaredPartialChoiceReturnCodes() {
  075:  return encryptedHashedSquaredPartialChoiceReturnCodes;
  076:  }
  077: 
  078:  public ElGamalMultiRecipientPublicKey getVerificationCardPublicKey() {
  079:  return verificationCardPublicKey;
  080:  }
  081: 
  082:  @Override
  083:  public boolean equals(final Object o) {
  084:  if (this == o) {
  085:  return true;
  086:  }
  087:  if (o == null || getClass() != o.getClass()) {
  088:  return false;
  089:  }
  090:  final ReturnCodeGenerationInput that = (ReturnCodeGenerationInput) o;
  091:  return verificationCardId.equals(that.verificationCardId) && ***REDACTED-SUSPECT-TOKEN***  092:  .equals(that.encryptedHashedSquaredConfirmationKey) && encryp***REDACTED-SUSPECT-TOKEN***  093:  .equals(that.encryptedHashedSquaredPartialChoiceReturnCodes) && verificationCardPublicKey.equals(that.verificationCardPublicKey);
  094:  }
  095: 
  096:  @Override
  097:  public int hashCode() {
  098:  return Objects.hash(verificationCardId, encryptedHashedSquaredConfirmationKey, encryptedHashedSquaredPartialChoiceReturnCodes,
  099:  verificationCardPublicKey);
  100:  }
  101: 
  102:  @Override
  103:  public ImmutableList<Hashable> toHashableForm() {
  104:  return ImmutableList
  105:  .of(HashableString.from(verificationCardId), encryptedHashedSquaredConfirmationKey, encryptedHashedSquaredPartialChoiceReturnCodes);
  106:  }
  107: 
  108: }

Obviously, at the CCRj side, the inverse scenario is equally vulnerable.

  

At line 144 the payload's signature is set to be validated.

At line 266 the same logic applied to generate the hash is invoked, thus leaving the deserialized vector of public keys '_verificationCardPublicKey_ ' out of the hash computation.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/ReturnCodesGenerationConsumer.java
  
  
  131:  @RabbitListener(queues = "${generation.computation.request.queue}", autoStartup = "false")
  132:  public void onMessage(final Message message) throws IOException {
  133:  final byte[] messageBody = message.getBody();
  134:  final byte[] dtoBytes = new byte[messageBody.length - 1];
  135:  System.arraycopy(messageBody, 1, dtoBytes, 0, messageBody.length - 1);
  136: 
  137:  final ChoiceCodeGenerationDTO<ReturnCodeGenerationRequestPayload> choiceCodeGenerationDTO = objectMapper
  138:  .readValue(dtoBytes, new TypeReference<ChoiceCodeGenerationDTO<ReturnCodeGenerationRequestPayload>>() {
  139:  });
  140: 
  141:  final ReturnCodeGenerationRequestPayload payload = choiceCodeGenerationDTO.getPayload();
  142: 
  143:  try {
  144:  validateSignature(payload);
  
  ...
  
  253:  private void validateSignature(final ReturnCodeGenerationRequestPayload payload)
  254:  throws MissingSignatureException, InvalidSignatureException, PayloadVerificationException {
  255: 
  256:  final String payloadId = String.format("[electionEventId:%s, verificationCardSetId:%s, chunkID:%s]", payload.getElectionEventId(),
  257:  payload.getVerificationCardSetId(), payload.getChunkId());
  258: 
  259:  LOGGER.info("Checking the signature of payload {}...", payloadId);
  260: 
  261:  if (payload.getSignature() == null) {
  262:  LOGGER.warn("REJECTED payload {} because it is not signed", payloadId);
  263:  throw new MissingSignatureException(payloadId);
  264:  }
  265: 
  266:  final byte[] payloadHash = hashService.recursiveHash(payload);
  267:  final boolean isPayloadSignatureValid = payloadSignatureService
  268:  .verify(payload.getSignature(), returnCodesKeyRepository.getPlatformCACertificate(), payloadHash);

  

After successfully validating the signature, at line 153 '_genEncLongCodeShares_ ' is invoked.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/ReturnCodesGenerationConsumer.java
  
  
  131:  @RabbitListener(queues = "${generation.computation.request.queue}", autoStartup = "false")
  132:  public void onMessage(final Message message) throws IOException {
  133:  final byte[] messageBody = message.getBody();
  134:  final byte[] dtoBytes = new byte[messageBody.length - 1];
  135:  System.arraycopy(messageBody, 1, dtoBytes, 0, messageBody.length - 1);
  136: 
  137:  final ChoiceCodeGenerationDTO<ReturnCodeGenerationRequestPayload> choiceCodeGenerationDTO = objectMapper
  138:  .readValue(dtoBytes, new TypeReference<ChoiceCodeGenerationDTO<ReturnCodeGenerationRequestPayload>>() {
  139:  });
  140: 
  141:  final ReturnCodeGenerationRequestPayload payload = choiceCodeGenerationDTO.getPayload();
  142: 
  143:  try {
  144:  validateSignature(payload);
  145: 
  146:  final ElGamalPrivateKey ccrjReturnCodesGenerationSecretKey=***REDACTED***
  147:  payload.getVerificationCardSetId());
  148:  final ZpSubgroup group = ccrjReturnCodesGenerationSecretKey.getGroup();
  149:  gqGroup = new GqGroup(group.getP(), group.getQ(), group.getG());
  150:  electionEventId = payload.getElectionEventId();
  151:  verificationCardSetId = payload.getVerificationCardSetId();
  152: 
  153:  final List<ReturnCodeGenerationOutput> returnCodeGenerationOutputs = genEncLongCodeShares(ccrjReturnCodesGenerationSecretKey,
  154:  payload.getReturnCodeGenerationInputs());
  155: 

  

Inside '_genEncLongCodeShares_ ', at lines 245/246, the list of voter's public keys '_verificationCardPublicKeyExtendedRepository_ ' is created/updated, potentially containing attacker's malicious Kid
  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/ReturnCodesGenerationConsumer.java
  
  
  191:  @SuppressWarnings("java:S117")
  192:  private List<ReturnCodeGenerationOutput> genEncLongCodeShares(final ElGamalPrivateKey ccrjReturnCodesGenerationSecretKey,
  193:  final List<ReturnCodeGenerationInput> returnCodeGenerationInputs) throws GeneralCryptoLibException {
  194: 
  195:  checkNotNull(ccrjReturnCodesGenerationSecretKey);
  196:  checkNotNull(returnCodeGenerationInputs);
  197:  checkArgument(!returnCodeGenerationInputs.isEmpty(), "The list of inputs must not be empty.");
  198: 
  199:  final String ee = electionEventId;
  200:  final GqElement g = gqGroup.getGenerator();
  201:  final List<ReturnCodeGenerationOutput> returnCodeGenerationOutputs = new ArrayList<>();
  202: 
  203:  // Algorithm.
  204:  for (final ReturnCodeGenerationInput returnCodeGenerationInput : returnCodeGenerationInputs) {
  205:  final String vc_id = returnCodeGenerationInput.getVerificationCardId();
  206: 
  207:  final ZqElement k_j_id = deriveVoterChoiceReturnCodeGenerationSecretKey(returnCodeGenerationInput, ccrjReturnCodesGenerationSecretKey,
  208:  vc_id);
  209:  final GqElement K_j_id = g.exponentiate(k_j_id);
  210:  final ZqElement kc_j_id = deriveVoterVoteCastReturnCodeGenerationSecretKey(returnCodeGenerationInput, ccrjReturnCodesGenerationSecretKey,
  211:  vc_id);
  212:  final GqElement Kc_j_id = g.exponentiate(kc_j_id);
  213: 
  214:  // Compute c_expPCC_j_id.
  215:  final ElGamalMultiRecipientCiphertext c_pCC_id = returnCodeGenerationInput.getEncryptedHashedSquaredPartialChoiceReturnCodes();
  216:  final ElGamalMultiRecipientCiphertext c_expPCC_j_id = c_pCC_id.exponentiate(k_j_id);
  217: 
  218:  final List<String> i_aux = Arrays.asList(ee, vc_id, "GenEncLongCodeShares", String.valueOf(nodeID));
  219: 
  220:  // Compute pi_expPCC_j_id.
  221:  final GroupVector<GqElement, GqGroup> basesPCC = c_pCC_id.getPhi().prepend(c_pCC_id.getGamma()).prepend(g);
  222:  final GroupVector<GqElement, GqGroup> exponentiationsPCC = c_expPCC_j_id.getPhi().prepend(c_expPCC_j_id.getGamma()).prepend(K_j_id);
  223:  final ExponentiationProof pi_expPCC_j_id = zeroKnowledgeProofService.genExponentiationProof(basesPCC, k_j_id, exponentiationsPCC, i_aux);
  224: 
  225:  // Compute c_expCK_j_id.
  226:  final ElGamalMultiRecipientCiphertext c_ck_id = returnCodeGenerationInput.getEncryptedHashedSquaredConfirmationKey();
  227:  final ElGamalMultiRecipientCiphertext c_expCK_j_id = c_ck_id.exponentiate(kc_j_id);
  228: 
  229:  // Compute pi_expCK_j_id.
  230:  final GroupVector<GqElement, GqGroup> basesCK = c_ck_id.getPhi().prepend(c_ck_id.getGamma()).prepend(g);
  231:  final GroupVector<GqElement, GqGroup> exponentiationsCK = c_expCK_j_id.getPhi().prepend(c_expCK_j_id.getGamma()).prepend(Kc_j_id);
  232:  final ExponentiationProof pi_expCK_j_id = zeroKnowledgeProofService.genExponentiationProof(basesCK, kc_j_id, exponentiationsCK, i_aux);
  233: 
  234:  // Output.
  235:  final ReturnCodeGenerationOutput returnCodeGenerationOutput = new ReturnCodeGenerationOutput(vc_id,
  236:  new ElGamalMultiRecipientPublicKey(Collections.singletonList(K_j_id)),
  237:  new ElGamalMultiRecipientPublicKey(Collections.singletonList(Kc_j_id)), c_expPCC_j_id, pi_expPCC_j_id, c_expCK_j_id,
  238:  pi_expCK_j_id);
  239:  returnCodeGenerationOutputs.add(returnCodeGenerationOutput);
  240: 
  241:  // Secure log.
  242:  logEncryptedConfirmationKeySuccessfullyExponentiated(verificationCardSetId, vc_id);
  243:  logEncryptedPartialChoiceCodesSuccessfullyExponentiated(verificationCardSetId, vc_id);
  244: 
  245:  verificationCardPublicKeyExtendedRepository.save(new VerificationCardPublicKeyExtended(ee, vc_id, verificationCardSetId,
  246:  returnCodeGenerationInput.getVerificationCardPublicKey()));
  247: 
  248:  }
  249: 
  250:  return returnCodeGenerationOutputs;
  251:  }

  

Then, at line 165 the potentially malicious Kid is consumed to validate πExp
  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/VotingClientProofsValidator.java
  
  
  151:  private ValidationError validateExponentiationProof(ValidationError result, ZpSubgroup mathematicalGroup, Vote vote) {
  152:  try {
  153:  result.setValidationErrorType(ValidationErrorType.FAILED);
  154: 
  155:  List<ZpGroupElement> groupElements = new ArrayList<>();
  156:  String[] exponentiatedCiphertext = getCiphertextElementsFromEncryptedOptions(vote.getEncryptedOptions());
  157:  for (String elementValue : exponentiatedCiphertext) {
  158:  ZpGroupElement groupElement = new ZpGroupElement(new BigInteger(elementValue), mathematicalGroup);
  159:  groupElements.add(groupElement);
  160:  }
  161: 
  162:  // create a list of exponentiated elements consisting of the verification card public key and the exponentiated ciphertexts.
  163: 
  164:  final String verificationCardId = vote.getVerificationCardId();
  165:  final Optional<VerificationCardPublicKeyExtended> optionalVerificationCardPublicKeyExtended = ver***REDACTED-SUSPECT-TOKEN***  166:  .findById(verificationCardId);
  167: 
  168:  if (!optionalVerificationCardPublicKeyExtended.isPresent()) {
  169:  throw new MissingVerificationCardPublicKeyExtendedException(verificationCardId);
  170:  }
  171: 
  172:  final ElGamalPublicKey verificationCardPublicKey = CryptoAdapters
  173:  .convert(optionalVerificationCardPublicKeyExtended.get().getVerificationCardPublicKey());
  174: 
  175:  // There must be only one exponent in the verification card public key.
  176:  List<ZpGroupElement> verificationCardPublicKeyList = verificationCardPublicKey.getKeys();
  177:  if (verificationCardPublicKeyList.size() != 1) {
  178:  throw new IllegalArgumentException(
  179:  String.format("Unexpected number of keys: found %s but should be 1.", verificationCardPublicKeyList.size()));
  180:  }
  181: 
  182:  List<ZpGroupElement> exponentiatedElements = new ArrayList<>();
  183:  ZpGroupElement verificationCardPublicKeySingleElement = verificationCardPublicKeyList.get(0);
  184:  exponentiatedElements.add(verificationCardPublicKeySingleElement);
  185:  exponentiatedCiphertext = getCiphertextElementsFromEncryptedOptions(vote.getCipherTextExponentiations());
  186: 
  187:  for (String elementValue : exponentiatedCiphertext) {
  188:  ZpGroupElement exponentiatedElement = new ZpGroupElement(new BigInteger(elementValue), mathematicalGroup);
  189:  exponentiatedElements.add(exponentiatedElement);
  190:  }
  191: 
  192:  // create a list of base elements consisting of the encryption group's generator and the multiplied voting options ciphertext (E1).
  193:  List<ZpGroupElement> baseElements = new ArrayList<>();
  194: 
  195:  ZpGroupElement groupElementGenerator = new ZpGroupElement(mathematicalGroup.getG(), mathematicalGroup);
  196:  baseElements.add(groupElementGenerator);
  197:  baseElements.addAll(groupElements);
  198: 
  199:  if (proofsService.createProofVerifierAPI(mathematicalGroup)
  200:  .verifyExponentiationProof(exponentiatedElements, baseElements, Proof.fromJson(vote.getExponentiationProof()))) {
  201:  result.setValidationErrorType(ValidationErrorType.SUCCESS);
  202:  }
  203:  } catch (GeneralCryptoLibException | NumberFormatException e) {
  204:  LOGGER.error("The validation of the exponentiation proof failed.", e);
  205:  }
  206:  return result;
  207: 
  208:  }
  209: 

  

There are a couple of issues that aggravate this attack, thus enabling it to be performed multiple times, also during the 'Voting Phase':

  1. This payload's signature verification logic lacks any kind of anti-replay protection, so the injection of the public keys can be performed by the 'voting server' also at specific times during the 'Voting Phase'.
  2. '_verificationCardPublicKeyExtendedRawRepository_ ' is a Spring's CrudRepository, whose '_save_ ' method when invoked repeatedly over the same id ('_verificationCardId_ ') just updates its previously stored contents.

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/domain/VerificationCardPublicKeyExtendedRepository.java
  
  
  39:  public VerificationCardPublicKeyExtended save(final VerificationCardPublicKeyExtended verificationCardPublicKeyExtended) {
  40:  return toVerificationCardPublicKeyExtended(
  41:  verificationCardPublicKeyExtendedRawRepository.save(toVerificationCardPublicKeyExtendedRaw(verificationCardPublicKeyExtended)));
  42:  }
  43: 
  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/domain/VerificationCardPublicKeyExtendedRaw.java
  
  
  13: @Entity
  14: @Table(name = "CC_VERIFICATION_CARD_PUBLIC_KEY")
  15: class VerificationCardPublicKeyExtendedRaw {
  16: 
  17:  private String electionEventId;
  18:  @Id
  19:  private String verificationCardId;

<https://gitlab.com/swisspost-evoting/e-voting/e-voting/-/issues/4>

  

### #5 - Lack of consistency check allows an adversary to forge the 'verificationCardId' in SecureLog entries

####  _Description_

During the voting phase, the voter runs two protocols with the control components: '_SendVote_ ' and '_ConfirmVote_ '. For this phase, the trust model for the Swiss Post e-voting system considers that both the voting client and the voting server are untrustworthy, so the design assumes these components may be effectively operating under the attacker's control.

  

A vulnerability has been found in the implementation of the Return Codes Control Component's '_SendVote_ ' protocol, specifically during the '_PartialDecryptPCC_ ' at '_PartialChoiceReturnCodesDecryptionConsumer.java_ '. A missing consistency check of the '_VerificationCardId_ ' field in the '_ReturnCodeComputationDTO_ ' and its encapsulated '_Vote_ ' object allows a malicious voting server to insert bogus SecureLogs entries. This could lead to confusion if somebody would perform a deeper investigation of the SecureLogs or forensic analysis of the logs.

  

#### _Technical analysis_

The Return Codes Control Components communicate with the Voting server through a RabbitMQ cluster using the AMQP protocol. The following message handler is used to invoke the '_VerifyBallotCCRj_ ' (Swiss Post Voting Protocol Computation Proof@12.2.1.3) and '_PartialDecryptPCCj_ ' (Swiss Post Voting Protocol Computation Proof@12.2.1.4) functionalities on the Return Codes control components CCR. A malicious voting server is able to serialize a specific message and send it to this queue through the orchestrator.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/PartialChoiceReturnCodesDecryptionConsumer.java
  
  
  187:  @RabbitListener(queues = "${verification.decryption.request.queue}", autoStartup = "false")
  188:  public void onMessage(final Message message) throws SafeStreamDeserializationException {
  189: 
  190:  final StreamSerializableObjectReader<ReturnCodeComputationDTO<ReturnCodesInput>> reader = new StreamSerializableObjectReaderImpl<>();
  191:  final ReturnCodeComputationDTO<ReturnCodesInput> data = reader.read(message.getBody(), 1, message.getBody().length);
  192: 
  193:  validateParameters(data);
  194:  if (isValid(data)) {
  195:  decryptMessageAndSendToOutputQueue(data);
  196:  }
  197:  }

After the deserialization of the received message is performed we will have '_data_ ', from which '_verificationCardId_ ' can be accessed at two different places.

  

1.-The DTO, at line 39
  
  
  File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ReturnCodeComputationDTO.java
  
  
  32:  public ReturnCodeComputationDTO(UUID correlationId, String requestId, String electionEventId, String verificationCardSetId,
  33:  String verificationCardId, T payload) {
  34:  super(correlationId);
  35:  this.requestId = requestId;
  36:  this.payload = payload;
  37:  this.electionEventId = electionEventId;
  38:  this.verificationCardSetId = verificationCardSetId;
  39:  this.verificationCardId = verificationCardId;
  40:  }
  ...
  106:  @SuppressWarnings("unchecked")
  107:  @Override
  108:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  109:  try {
  110:  setCorrelationId(UUID.fromString(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker)));
  111:  this.electionEventId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  112:  this.verificationCardSetId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  113:  this.verificationCardId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);

  

2.-The encapsulated vote class in the DTO's payload ('_ReturnCodesInput_ ') At line 30 we see the declaration of '_PartialChoiceReturnCodesVerificationInput_ '. Its 'vote' variable will hold a json-serialized '_Vote.class_ ' object fully controllable by the attacker (line 123) 

  

  
  
  File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ReturnCodesInput.java
  
  
  24: public class ReturnCodesInput implements StreamSerializable {
  25: 
  26:  private List<BigInteger> returnCodesInputElements;
  27: 
  28:  private ConfirmationKeyVerificationInput confirmationKeyVerificationInput;
  29: 
  30:  private PartialChoiceReturnCodesVerificationInput partialChoiceReturnCodesVerificationInput;
  
  ...
  094:  @Override
  095:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  096:  try {
  097:  if (unpacker.tryUnpackNil()) {
  098:  this.returnCodesInputElements = null;
  099:  } else {
  100:  int listSize = unpacker.unpackArrayHeader();
  101:  returnCodesInputElements = new ArrayList<>(listSize);
  102:  for (int i = 0; i < listSize; i++) {
  103:  returnCodesInputElements.add(StreamSerializableUtil.retrieveBigIntegerValueWithNullCheck(unpacker));
  104:  }
  105:  }
  106: 
  107:  if (MessageFormat.NIL.equals(unpacker.getNextFormat())) {
  108:  confirmationKeyVerificationInput = null;
  109:  unpacker.unpackNil();
  110:  } else {
  111:  confirmationKeyVerificationInput = new ConfirmationKeyVerificationInput();
  112:  confirmationKeyVerificationInput.setConfirmationMessage(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  113:  confirmationKeyVerificationInput.setVotingCardId(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  114:  }
  115:  if (MessageFormat.NIL.equals(unpacker.getNextFormat())) {
  116:  partialChoiceReturnCodesVerificationInput = null;
  117:  unpacker.unpackNil();
  118:  } else {
  119:  partialChoiceReturnCodesVerificationInput = new PartialChoiceReturnCodesVerificationInput();
  120:  p***REDACTED-SUSPECT-TOKEN***  121:  .setVerificationCardSetDataJwt(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  122:  partialChoiceReturnCodesVerificationInput.setElectionPublicKeyJwt(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  123:  partialChoiceReturnCodesVerificationInput.setVote(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  124:  }
  125: 
  126:  certificates = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  127:  } catch (IOException e) {
  128:  throw new SafeStreamDeserializationException(e);
  129:  }
  130:  }

  

Looking at the Vote class definition we can see that '_verificationCardId_ ' is declared at line 110.

  

  
  
  File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/election/model/vote/Vote.java
  
  
  018: /**
  019:  * This class represents the vote in this context.
  020:  */
  021: @JsonIgnoreProperties(ignoreUnknown = true)
  022: public class Vote {
  023: 
  024:  // The identifier of the tenant.
  025:  @NotNull(groups = SyntaxErrorGroup.class)
  026:  @Pattern(regexp = Patterns.ID, groups = SemanticErrorGroup.class)
  027:  @Size(min = 1, max = Constants.COLUMN_LENGTH_100, groups = SemanticErrorGroup.class)
  028:  private String tenantId;
  029: 
  ...
  092:  /**
  093:  * The vote ciphertext that contains the exponentiated elements (C'0, C'1).
  094:  */
  095:  private String cipherTextExponentiations;
  096: 
  097:  /**
  098:  * The exponentiation proof.
  099:  */
  100:  private String exponentiationProof;
  101: 
  102:  /**
  103:  * The plaintext equality proof.
  104:  */
  105:  private String plaintextEqualityProof;
  106: 
  107:  /**
  108:  * The identifier of the verification card.
  109:  */
  110:  private String verificationCardId;
  111: 

  

The vulnerability lies in the lack of consistence as the underlying logic assumes that the '_verificationCardId_ ' value for both the serialized Vote and the DTO is the same. However, as we have seen, the attacker can serialize a specific message containing two different '_verificationCardId_ ' values:

  1. Consumed by the DTO
  2. Consumed when the deserialization of the encapsulated '_Vote_ ' is invoked.

Let's see how we can abuse the '_verificationCardId_ ' duality according to the specification.

  

At line 262 we can see a crucial validation, which checks whether the '_verificationCardId_ ' has already successfully completed a 'SendVote' protocol before. In this case the used '_verificationCardId_ ' value is DTO's (initialized at line 233). At line line 290 the NIZKP validator is invoked.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/PartialChoiceReturnCodesDecryptionConsumer.java
  
  
  226:  /**
  227:  * Checks if the input data is valid.
  228:  */
  229:  private boolean isValid(final ReturnCodeComputationDTO<ReturnCodesInput> data) {
  230: 
  231:  final String electionEventId = validateUUID(data.getElectionEventId());
  232:  final String verificationCardSetId = validateUUID(data.getVerificationCardSetId());
  233:  final String verificationCardId = validateUUID(data.getVerificationCardId());
  234: 
  235:  // Get the mathematicalGroup
  236:  final ZpSubgroup mathematicalGroup;
  237:  try {
  238:  mathematicalGroup = returnCodesKeyRepository.getMathematicalGroup(electionEventId, verificationCardSetId);
  239: 
  240:  if (mathematicalGroup == null) {
  241:  LOGGER.error("Unexpected scenario - encrypted partial Choice Return Codes' mathematicalGroup is null.");
  242:  return false;
  243:  }
  244: 
  245:  } catch (KeyManagementException e) {
  246:  LOGGER.error("Unexpected error getting the group for election event id {} and verification card set id {}.", electionEventId,
  247:  verificationCardSetId);
  248:  return false;
  249:  }
  250: 
  251:  if (!isPartialChoiceReturnCodesComputation(data)) {
  252:  LOGGER.error("Unexpected scenario - Necessary input to decrypt the encrypted partial Choice Return Codes is empty.");
  253:  return false;
  254:  }
  255: 
  256:  if (data.getPayload().getConfirmationKeyVerificationInput() != null) {
  257:  LOGGER.error("Unexpected scenario - Confirmation Key verification input must be empty.");
  258:  return false;
  259:  }
  260: 
  261:  // We abort the process if the control component already decrypted the partial Choice Return Codes for this verificationCardId
  262:  if (computedVerificationCardRepository.existsById(new ComputedVerificationCardPrimaryKey(electionEventId, verificationCardId))) {
  263:  LOGGER.error("Verification card has already been computed for electionEventId {} and verificationCardId {}", data.getElectionEventId(),
  264:  data.getVerificationCardId());
  265:  return false;
  266:  }
  267: 
  268:  LOGGER.info("Verification card is yet to be computed for electionEventId {} and verificationCardId {}", data.getElectionEventId(),
  269:  data.getVerificationCardId());
  270: 
  271:  if (!checkInputDataConsistency(data, mathematicalGroup)) {
  272:  return false;
  273:  }
  274: 
  275:  final PartialChoiceReturnCodesVerificationInput partialChoiceReturnCodesVerificationInput = data.getPayload()
  276:  .getPartialChoiceReturnCodesVerificationInput();
  277: 
  278:  // verify and obtain admin board public key
  279:  final PublicKey adminBoardPublicKey;
  280:  try {
  281:  adminBoardPublicKey = verifyChainAndGetAdminBoardPublicKey(data.getPayload().getCertificates());
  282:  } catch (GeneralCryptoLibException e) {
  283:  LOGGER.error("Could not read certificates from json.");
  284:  return false;
  285:  } catch (CertificateChainValidationException e) {
  286:  LOGGER.error("Invalid certificate chain: {}", String.join(" | ", certificateValidator.getErrors()));
  287:  return false;
  288:  }
  289: 
  290:  return votingClientProofsValidator.validateVoteAndProofs(mathematicalGroup, partialChoiceReturnCodesVerificationInput, adminBoardPublicKey);
  291:  }

  

As the following code shows, the NIZK proofs and valid votes checks are based on the Vote's '_verificationCardId_ ' not the DTO's (see how the vote object is deserialized at line 094). As a result, πballot = (πExp, πEqEnc) will be validated.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/VotingClientProofsValidator.java
  
  
  091:  public boolean validateVoteAndProofs(ZpSubgroup mathematicalGroup,
  092:  PartialChoiceReturnCodesVerificationInput partialChoiceReturnCodesVerificationInput, PublicKey adminBoardPublicKey) {
  093:  try {
  094:  Vote voteObject = ObjectMappers.fromJson(partialChoiceReturnCodesVerificationInput.getVote(), Vote.class);
  095: 
  096:  ElGamalPublicKey electionPublicKey = verifyAndGetElectionPublicKey(partialChoiceReturnCodesVerificationInput.getElectionPublicKeyJwt(),
  097:  adminBoardPublicKey);
  098: 
  099:  if (electionPublicKey == null) {
  100:  LOGGER.error("The election public key is null.");
  101:  return false;
  102:  }
  103: 
  104:  VerificationCardSetData verificationCardSetData = verifyAndGetVerificationCardSetData(
  105:  partialChoiceReturnCodesVerificationInput.getVerificationCardSetDataJwt(), adminBoardPublicKey);
  106: 
  107:  if (verificationCardSetData == null) {
  108:  LOGGER.error("The verification card set data is null.");
  109:  return false;
  110:  }
  111: 
  112:  if (!verifyVerificationCardPublicKey(verificationCardSetData.getVerificationCardSetIssuerCert(), voteObject)) {
  113:  LOGGER.error("The Verification Card Public Key could not be verified.");
  114:  return false;
  115:  }
  116: 
  117:  ValidationError exponentiationProofValidation = validateExponentiationProof(new ValidationError(), mathematicalGroup, voteObject);
  118:  boolean exponentiationProofValidationResult = !ValidationErrorType.FAILED.equals(exponentiationProofValidation.getValidationErrorType());
  119:  if (!exponentiationProofValidationResult) {
  120:  String errorArgs = StringUtils.join(exponentiationProofValidation.getErrorArgs());
  121:  LOGGER.error("Exponentiation proof not valid. {}", errorArgs);
  122:  }
  123: 
  124:  ValidationError plaintextEqualityProofValidation = validatePlaintextEqualityProof(new ValidationError(), mathematicalGroup, voteObject,
  125:  electionPublicKey, verificationCardSetData.getChoicesCodesEncryptionPublicKey());
  126:  boolean plaintextEqualityProofValidationResult = !ValidationErrorType.FAILED

  

See lines 164 and 165 for the πExp verification based on the Vote's '_verificationCardId_ ' value.
  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/VotingClientProofsValidator.java
  
  
  146:  * Validates an exponentiation zero-knowledge proof.
  147:  * <p>
  148:  * At this point, we already checked the group membership of all elements, via the class {@link ZpSubgroupProofVerifier} of CryptoLib.
  149:  * </p>
  150:  */
  151:  private ValidationError validateExponentiationProof(ValidationError result, ZpSubgroup mathematicalGroup, Vote vote) {
  152:  try {
  153:  result.setValidationErrorType(ValidationErrorType.FAILED);
  154: 
  155:  List<ZpGroupElement> groupElements = new ArrayList<>();
  156:  String[] exponentiatedCiphertext = getCiphertextElementsFromEncryptedOptions(vote.getEncryptedOptions());
  157:  for (String elementValue : exponentiatedCiphertext) {
  158:  ZpGroupElement groupElement = new ZpGroupElement(new BigInteger(elementValue), mathematicalGroup);
  159:  groupElements.add(groupElement);
  160:  }
  161: 
  162:  // create a list of exponentiated elements consisting of the verification card public key and the exponentiated ciphertexts.
  163: 
  164:  final String verificationCardId = vote.getVerificationCardId();
  165:  final Optional<VerificationCardPublicKeyExtended> optionalVerificationCardPublicKeyExtended = ver***REDACTED-SUSPECT-TOKEN***  166:  .findById(verificationCardId);
  167: 
  168:  if (!optionalVerificationCardPublicKeyExtended.isPresent()) {
  169:  throw new MissingVerificationCardPublicKeyExtendedException(verificationCardId);
  170:  }

  

As the vote is valid and the πballot proofs have been validated we will be reaching the final part '_decryptMessageAndSendToOutputQueue_ '

  

In this method is where we find a convenient way (from the attacker's perspective) to exploit the improper handling of this '_verificationCardId_ ' duality.

  

  * The DTO's '_verificationCardId_ ' value is used to update the list of partially decrypted PCC (line 488). This means the attacker can invoke the '_partialDecryptPCC_ ' multiple times, with arbitrary valid votes, as long as the malicious voting server uses a different, but valid, vcdid (in the same election context) for the serialized DTO. As this vcdid will be added to the List of already decrypted pCCs, the voter associated to that vcdid will be unable to complete the '_SendVote_ ' protocol (thus effectively preventing to cast a vote) even thou he/she never legitimately initiated that phase before.

  

  * The DTO's '_verificationCardId_ ' value is used at '_logPartialDecryptPccExponentiationProofSuccessfullyComputed_ ' (line 475) where the secure log that will be consumed by the trusted auditors is generated. The vcdid used to generate the secure log entry is different from the vcdid used to perform the exponentiation.

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/PartialChoiceReturnCodesDecryptionConsumer.java
  
  
  414:  private void decryptMessageAndSendToOutputQueue(final ReturnCodeComputationDTO<ReturnCodesInput> data) {
  415:  LOGGER.info("Decrypting the encrypted partial Choice Return Codes.");
  416: 
  417:  final String electionEventId = data.getElectionEventId();
  418:  final String verificationCardSetId = data.getVerificationCardSetId();
  419:  final String verificationCardId = data.getVerificationCardId();
  420: 
  421:  // This is the gamma element of the encrypted partial choice return codes.
  422:  final BigInteger gammaEncryptedPartialChoiceReturnCodesBigInteger = data.getPayload().getReturnCodesInputElements().get(0);
  423: 
  424:  final ElGamalPrivateKey ccrjChoiceReturnCodesEncryptionPrivateKey;
  425:  final ZpGroupElement gammaEncryptedPartialChoiceReturnCodes;
  426:  try {
  427:  ccrjChoiceReturnCodesEncryptionPrivateKey = returnCodesKeyRepository
  428:  .getCcrjChoiceReturnCodesEncryptionSecretKey(electionEventId, verificationCardSetId);
  429: 
  430:  gammaEncryptedPartialChoiceReturnCodes = new ZpGroupElement(gammaEncryptedPartialChoiceReturnCodesBigInteger,
  431:  ccrjChoiceReturnCodesEncryptionPrivateKey.getGroup());
  432:  } catch (GeneralCryptoLibException e) {
  433:  LOGGER.error(FAILED_TO_OBTAIN_THE_DECRYPTION_INPUT_PARAMETERS, e);
  434:  return;
  435:  } catch (KeyManagementException e) {
  436:  LOGGER.error(FAILED_FAILED_TO_GET_THE_CCR_J_CHOICE_RETURN_CODES_ENCRYPTION_PRIVATE_KEY_FROM_THE_KEY_REPOSITORY, e);
  437:  return;
  438:  }
  439: 
  440:  final List<Exponent> ccrjChoiceReturnCodesEncryptionPrivateKeyElements = ccrjChoiceReturnCodesEncryptionPrivateKey.getKeys();
  441:  if (ccrjChoiceReturnCodesEncryptionPrivateKeyElements.isEmpty()) {
  442:  LOGGER.error(CCR_J_CHOICE_RETURN_CODES_ENCRYPTION_PRIVATE_KEY_DID_NOT_CONTAIN_ANY_EXPONENT);
  443:  throw new IllegalStateException(CCR_J_CHOICE_RETURN_CODES_ENCRYPTION_PRIVATE_KEY_DID_NOT_CONTAIN_ANY_EXPONENT);
  444:  }
  445: 
  446:  // gamma element exponentiated to the CCR_j Choice Return Codes Encryption private key elements.
  447:  final List<ZpGroupElement> gammaExponentiatedToPrivateKeyElements = new ArrayList<>(ccrjChoiceReturnCodesEncryptionPrivateKeyElements.size());
  448: 
  449:  // gamma element exponentiated to the CCR_j Choice Return Codes Encryption private key elements as a JSON element.
  450:  final List<String> gammaExponentiatedToPrivateKeyElementsJson = new ArrayList<>(ccrjChoiceReturnCodesEncryptionPrivateKeyElements.size());
  451: 
  452:  try {
  453:  for (final Exponent exponent : ccrjChoiceReturnCodesEncryptionPrivateKeyElements) {
  454:  final ZpGroupElement exponentiated = gammaEncryptedPartialChoiceReturnCodes.exponentiate(exponent);
  455:  gammaExponentiatedToPrivateKeyElements.add(exponentiated);
  456:  gammaExponentiatedToPrivateKeyElementsJson.add(exponentiated.toJson());
  457:  }
  458:  } catch (GeneralCryptoLibException e) {
  459:  LOGGER.error(FAILED_TO_OBTAIN_THE_DECRYPTION_INPUT_PARAMETERS, e);
  460:  return;
  461:  }
  462: 
  463:  LOGGER.info(
  464:  "Partially decrypted the encrypted partial Choice Return Codes using the CCR_j Choice Return Codes encryption secret key for election event ID {}, verification card set ID {} and verification card ID{}",
  465:  electionEventId, verificationCardSetId, verificationCardId);
  466: 
  467:  final ElGamalPublicKey ccrjChoiceReturnCodesEncryptionPublicKey;
  468:  final Proof exponentiationProof;
  469:  try {
  470:  ccrjChoiceReturnCodesEncryptionPublicKey = returnCodesKeyRepository
  471:  .getCcrjChoiceReturnCodesEncryptionPublicKey(electionEventId, verificationCardSetId);
  472: 
  473:  exponentiationProof = calculateExponentiationProof(ccrjChoiceReturnCodesEncryptionPrivateKey, ccrjChoiceReturnCodesEncryptionPublicKey,
  474:  gammaEncryptedPartialChoiceReturnCodes, gammaExponentiatedToPrivateKeyElements);
  475:  logPartialDecryptPccExponentiationProofSuccessfullyComputed(data, gammaEncryptedPartialChoiceReturnCodes,
  476:  gammaExponentiatedToPrivateKeyElements, exponentiationProof);
  477: 
  478:  } catch (GeneralCryptoLibException e) {
  479:  LOGGER.error("Error while generating proof of knowledge of the CCR_j Choice Return Codes secret key.");
  480:  LOGGER.error(FAILED_TO_OBTAIN_THE_DECRYPTION_INPUT_PARAMETERS, e);
  481:  return;
  482:  } catch (KeyManagementException e) {
  483:  LOGGER.error(FAILED_FAILED_TO_GET_THE_CCR_J_CHOICE_RETURN_CODES_ENCRYPTION_PRIVATE_KEY_FROM_THE_KEY_REPOSITORY, e);
  484:  return;
  485:  }
  486: 
  487:  // Add the verification card id to the list of partial decrypted PCC
  488:  computedVerificationCardRepository.save(new ComputedVerificationCard(electionEventId, verificationCardId));
  489: 
  490:  final ChoiceCodesVerificationDecryptResPayload resultPayload = new ChoiceCodesVerificationDecryptResPayload();
  491: 
  492:  resultPayload.setDecryptContributionResult(gammaExponentiatedToPrivateKeyElementsJson);
  493:  try {
  494:  resultPayload.setExponentiationProofJson(exponentiationProof.toJson());
  495:  resultPayload.setPublicKeyJson(ccrjChoiceReturnCodesEncryptionPublicKey.toJson());
  496:  } catch (GeneralCryptoLibException e) {
  497:  LOGGER.error(FAILED_TO_OBTAIN_THE_DECRYPTION_INPUT_PARAMETERS, e);
  498:  return;
  499:  }
  500: 
  501:  try {
  502:  final PayloadSignature payloadSignature = payloadSigner.sign(resultPayload, keysManager.getElectionSigningPrivateKey(electionEventId),
  503:  keysManager.getElectionSigningCertificateChain(electionEventId));
  504:  resultPayload.setSignature(payloadSignature);
  505:  LOGGER.info("Partially decrypted partial Choice Return Codes and corresponding proofs correctly signed.");
  506:  } catch (KeyManagementException e) {
  507:  LOGGER.error(FAILED_FAILED_TO_GET_THE_CCR_J_CHOICE_RETURN_CODES_ENCRYPTION_PRIVATE_KEY_FROM_THE_KEY_REPOSITORY, e);
  508:  return;
  509:  } catch (PayloadSignatureException e) {
  510:  LOGGER.error(FAILED_TO_SIGN_PARTIAL_CHOICE_RETURN_CODES_DECRYPTION_RESULT, e);
  511:  return;
  512:  }
  513: 
  514:  final UUID correlationId = data.getCorrelationId();
  515:  final String requestId = data.getRequestId();
  516: 
  517:  final ReturnCodeComputationDTO<ChoiceCodesVerificationDecryptResPayload> returnCodeComputationDTO = new ReturnCodeComputationDTO<>(
  518:  correlationId, requestId, electionEventId, verificationCardSetId, verificationCardId, resultPayload);
  519: 
  520:  final Message amqpMessage = MessageSerialisation.getMessage(returnCodeComputationDTO);
  521: 
  522:  rabbitTemplate.send(decryptionOutputQueue, amqpMessage);
  523:  }

  

At line 570 - DTO's  _verificationCardId_ used in the secure logger, creating the anomaly as  _data.getVerificationCardId()_ !=  _Vote.getVerificationCardId()_

  

  
  
  File: e-voting-master/control-components/return-codes-service/src/main/java/ch/post/it/evoting/controlcomponents/returncodes/service/PartialChoiceReturnCodesDecryptionConsumer.java
  
  
  563:  private void logPartialDecryptPccExponentiationProofSuccessfullyComputed(final ReturnCodeComputationDTO<ReturnCodesInput> data,
  564:  final ZpGroupElement gammaEncryptedPartialChoiceReturnCodes, final List<ZpGroupElement> gammaExponentiatedToPrivateKeyElements,
  565:  final Proof exponentiationProof) {
  566: 
  567:  ControlComponentContext context = new ControlComponentContext(data.getElectionEventId(), data.getVerificationCardSetId(), controlComponentId);
  568: 
  569:  PartialDecryptPccExponentiationProof partialDecryptPccExponentiationProof = new PartialDecryptPccExponentiationProof(
  570:  data.getVerificationCardId(), gammaEncryptedPartialChoiceReturnCodes.getValue(), gammaExponentiatedToPrivateKeyElements,
  571:  exponentiationProof);
  572: 
  573:  final ReturnCodesMessage message = returnCodesMessageFactory
  574:  .buildPartialDecryptPccExponentiationProofLogMessage(context, partialDecryptPccExponentiationProof);
  575: 
  576:  SECURE_LOGGER.info(message);
  577:  }

  

  

  

### #7 - Improper parsing of the request body when validating signatures for secure requests

####  _Description_

I would like to clarify that this vulnerability is not that interesting in this e-voting context but I decided to include it in this blog post because it's useful to illustrate an interesting vulnerability pattern ( inconsistent encoding that breaks uniqueness requirements) that may end up creating serious security issues, such as this $2M Double Spending [bug](https://medium.com/immunefi/polygon-double-spend-bug-fix-postmortem-2m-bounty-5a1db09db7f1).

  

The verification of the signature for 'secure' requests within the Voting Server contains an inconsistent parsing logic between the signature generator (RestClientInterceptor) and the signature verifier (_SignedRequestFilter_) for the request body.

  

As a result, depending on the request body's contents, it is possible that the signature verifier fails to validate the received signature, thus preventing a potentially legitimate request to be processed.

#### _Technical analysis_

The signature is generated assuming a UTF-8 string body request, as the line 101 shows.

  

  
  
  File: e-voting-master/voting-server/commons/commons-infrastructure/src/main/java/ch/post/it/evoting/votingserver/commons/infrastructure/remote/client/RestClientInterceptor.java
  
  
  093:  private String getRequestBodyToString(final RequestBody request) {
  094:  final RequestBody copy = request;
  095:  try (final Buffer buffer = new Buffer()) {
  096:  if (copy != null) {
  097:  copy.writeTo(buffer);
  098:  } else {
  099:  return "";
  100:  }
  101:  return buffer.readUtf8();
  102:  } catch (final IOException e) {
  103:  final String errorMsg = "Exception occurred during process body to String";
  104:  LOGGER.error(errorMsg, e);
  105:  return "";
  106:  }
  107:  }

  

However, on the  _SignedRequestFilter_ side the request body is converted to a UTF-8 string using a different logic, which uses '_reader.readLine()_ ' (line 196). This method will remove any new-line character found in the request body from the resulting string. As this logic is different from the one implemented when the signature was created it may lead to a failure when the filter tries to validate the signature. 

  

  
  
  File: e-voting-master/voting-server/commons/commons-infrastructure/src/main/java/ch/post/it/evoting/votingserver/commons/infrastructure/remote/filter/SignedRequestFilter.java
  
  
  184:  /**
  185:  * Reads the request body from the request and returns it as a String.
  186:  *
  187:  * @param multiReadHttpServletRequest HttpServletRequest that contains the request body
  188:  * @return request body as a String or null
  189:  */
  190:  private String getRequestBodyToString(final MultiReadHttpServletRequest multiReadHttpServletRequest) {
  191:  try {
  192:  // Read from request
  193:  StringBuilder buffer = new StringBuilder();
  194:  BufferedReader reader = multiReadHttpServletRequest.getReader();
  195:  String line;
  196:  while ((line = reader.readLine()) != null) {
  197:  buffer.append(line);
  198:  }
  199:  return buffer.toString();
  200:  } catch (Exception e) {
  201:  LOGGER.error("Failed to read the request body from the request.", e);
  202:  }
  203:  return null;
  204:  }

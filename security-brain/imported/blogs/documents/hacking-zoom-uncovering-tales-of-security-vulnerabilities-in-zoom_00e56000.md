---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-08_hacking-zoom-uncovering-tales-of-security-vulnerabilities-in-zoom.md
original_filename: 2020-08-08_hacking-zoom-uncovering-tales-of-security-vulnerabilities-in-zoom.md
title: 'Hacking Zoom: Uncovering Tales of Security Vulnerabilities in Zoom'
category: documents
detected_topics:
- command-injection
- otp
- rate-limit
- automation-abuse
- idor
- ssrf
tags:
- imported
- documents
- command-injection
- otp
- rate-limit
- automation-abuse
- idor
- ssrf
language: en
raw_sha256: 00e560003c5b51e977d421b7dfed023b0c91ac95efa4ec14cedb9cd89cafd08d
text_sha256: 8148001ef2181d9133bfd6897e192edcab6db2fc0788b3ff055434852fe53025
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Zoom: Uncovering Tales of Security Vulnerabilities in Zoom

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-08_hacking-zoom-uncovering-tales-of-security-vulnerabilities-in-zoom.md
- Source Type: markdown
- Detected Topics: command-injection, otp, rate-limit, automation-abuse, idor, ssrf
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `00e560003c5b51e977d421b7dfed023b0c91ac95efa4ec14cedb9cd89cafd08d`
- Text SHA256: `8148001ef2181d9133bfd6897e192edcab6db2fc0788b3ff055434852fe53025`


## Content

---
title: "Hacking Zoom: Uncovering Tales of Security Vulnerabilities in Zoom"
page_title: "Hacking Zoom: Uncovering Tales of Security Vulnerabilities in Zoom · Mazin Ahmed"
url: "https://mazinahmed.net/blog/hacking-zoom/"
final_url: "https://mazinahmed.net/blog/hacking-zoom/"
authors: ["Mazin Ahmed (@mazen160)"]
programs: ["Zoom"]
bugs: ["Information disclosure", "RCE", "Memory leak"]
publication_date: "2020-08-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4339
---

# Hacking Zoom: Uncovering Tales of Security Vulnerabilities in Zoom

August 9, 2020·19 mins

* * *

# Hacking Zoom #

## Uncovering Tales of Security Vulnerabilities in Zoom #

This blog post discusses my experiments in testing and hacking Zoom.

Zoom has become one of the most high-performing tech companies of 2020. Zoom is a digital video conferencing software that went public in IPO last year[1](https://www.cnbc.com/2019/04/18/zoom-ipo-stock-begins-trading-on-nasdaq.html), a few months before the global pandemic.

Zoom grew rapidly over the past year, going from 10M active users in early 2019 to over 200M by mid-2020.

The popularity of Zoom has made it a high-profile target for hackers, nefarious actors, and the security community. Organizations worldwide are using Zoom to enable remote work. The UK government even used Zoom for cabinet meetings[2](https://www.infosecurity-magazine.com/news/uk-government-zoom-despite-mod/). We can see Zoom in every part of our lives today.

This post shares my research and experiments in testing and hacking Zoom.

# Executive Summary #

My research focused on identifying security vulnerabilities in Zoom. The research revealed several severe security vulnerabilities that affect the Zoom production and development infrastructure, the Zoom Linux app, and Zoom’s end-to-end encryption implementation.

My experience with Zoom’s security and VDP (vulnerability disclosure program) did not match what I had seen in the public media. I assume this is because Zoom focused on the security incidents that generated the most damaging public PR. This is also likely due to Zoom implementing a last-minute bug bounty program after its user base boomed during the global pandemic.

The first finding that I identified in April 2020 has not been patched. The first time I received a conclusive response regarding the finding was on July 14th, 2020, after four months of reporting the vulnerability and numerous follow-ups from my side.

When I submitted my CFP to DEFCON 2020, I conducted another round of experiments on Zoom, where I identified new security vulnerabilities that affected different Zoom products. All discovered vulnerabilities were responsibly disclosed to Zoom.

I would also like to note that all of my research was self-funded. I have also not received any bounty/reward for my efforts by Zoom.

## List of Identified Vulnerabilities #

  * Zoom Exposed Public Kerberos Authentication Server
  * Memory Leak on Zoom Production Server
  * Unexploitable RCE on Zoom Production Server
  * Shadow IT Issues on accessible Zoom servers
  * Zoom App for Linux:
  * Bad Design practice on TLS/SSL implementation
  * A Bad Design Practice on Zoom Launcher Implementation.
  * End-to-end encrypted messages between Zoom users are stored on disk in plain text.
  * Zoom Local Database accessible by all local users, including private end-to-end encrypted messages (stored in plain text) and access tokens.

The responsible disclosure section discusses the process I have been through in conducting a responsible disclosure with Zoom. It was a painful experience with a lack of communication from Zoom for most of the time. Many things could have been done to improve the Zoom VDP.

I can see that Zoom had difficulties building its bug bounty program. As a result, I’m also listing suggestions to help enhance the program at the end of the post.

# Who Am I? #

I’m a cyber security engineer who specializes in offensive security and AppSec. Read more about my previous work at <https://mazinahmed.net/>.

# Table of Contents #

  * Introduction
  * Identifying Attack Surface
  * Findings
  * Zoom Public Kerberos Authentication
  * Attacking Kerberos
  * Discovery of a Memory Leak on a Zoom Production Server
  * Automating the Exploitation
  * A Memory Leak is not the end
  * Zoom’s Prevention
  * Shadow IT & Zoom
  * Zoom App for Linux
  * Zoom TLS/SSL is Broken By Design on Linux
  * Zoom Launcher Implementation: What’s a badly designed application launcher? Zoom Launcher for Linux.
  * Zoom is End-to-End Encrypted? Not fully.
  * Zoom Local Database Implementation: Bad practice for Linux security.
  * Responsible Disclosure
  * Timeline
  * Zoom’s analysis & my response to the analysis.
  * Conclusion
  * Acknowledgment
  * References

* * *

## Recorded Conference Talk #

* * *

# Introduction #

I started my first round of tests on Zoom in April 2020. My goal was to find an impactful security vulnerability that affects Zoom infrastructure and users. I identified a memory leak vulnerability that affects an API belonging to Zoom production infrastructure - the details of the finding and other findings are discussed later in the article.

Once I confirmed the presence of the vulnerability, I reported it directly to [security@zoom.us](mailto:security@zoom.us) per their security page at zoom.us/security.

I expected to receive a quick, responsible confirmation, a patch, and a reward. Instead, I have been in a continuous circle of follow-ups with no response regarding my finding - the responsible disclosure.

I also contacted Luta Security, a Zoom contractor, to set up their VDP during Q1-Q2 2020. Still, there was no luck getting a fix or a detailed analysis for the responsible disclosure.

After all of the confusion about the attempts at responsible disclosure, I decided to take my research to DEFCON 2020. I submitted my CFP and notified Zoom regarding my intentions of disclosing my findings in Zoom on June 05th, 2020. I still haven’t received a conclusive response after that.

When my CFP was accepted, I conducted further security research on Zoom. I found new vulnerabilities affecting their infrastructure, the Zoom Linux app, and end-to-end encryption implementation.

I reported all the new findings to Zoom on July 11th, 2020, repeating my intentions of disclosing my research in DEFCON 2020. This was where I received the first conclusive response from Zoom.

# Identifying Attack Surface #

My first step when testing on targets is the attack surface identification. It’s a step where I do the reconnaissance phase to understand the running systems, exposed APIs, (un)maintained services and everything that can be interesting from an adversary point of view.

Before attacking Zoom, I wasn’t aware of the attack surface; I had to learn it during this research.

## Domains Discovery #

Luckily, I run [FullHunt.io](https://FullHunt.io), a vulnerability intelligence platform that aids in the attack surface discovery, monitoring, and automating security.

There is an internal FullHunt API that allows querying domains owned by organizations. I ran a query that returned more than 13 domains.

![](/uploads/assets/static/aa2beb87-a08b-4dcd-b1a3-6c24f4cde22b.png)

I added them to my FullHunt account to automate the discovery process. While I collected a tremendous amount of data, I didn’t have the time to test everything, as this research is a personal, non-funded experiment I was doing in my free time. I focused on a portion of the attack surface. I will be showcasing various findings I identified.

# Findings #

# Zoom Public Kerberos Authentication #

While port-scanning different assets, an asset grabbed my attention.

Targets: `ca01.idm.meetzoom.us`

![Nmap port scan on ca01.idm.meetzoom.us](/uploads/assets/static/bec0ea6b-1fee-43c2-9d68-edff0569089c.png)

I noticed a running Kerberos service that is externally accessible. Kerberos is a network authentication protocol designed to secure authentication for client/server applications.

The naming convention for the asset indicates that it’s running an identity management solution or a PKI (public-key infrastructure).

While checking what was running on port 80, I found that the host was running FreeIPA[3](https://www.freeipa.org/page/Main_Page). This is an open-source identity management solution developed by RedHat.

There are no known severe public vulnerabilities reported previously. Researching for a zero-day within FreeIPA is an option, but I didn’t have the time to focus on it. Another option was to review Zoom’s implementation of Kerberos and FreeIPA setup.

I also found another asset that runs the exact setup.

Target: `va01.idm.meetzoom.us`

Practically speaking, **Kerberos allows a significant size of attack surface once we have an authenticated account**. While not being within the internal network, the initial entry for Kerberos is more complicated.

The HTTP interface is quite verbose regarding error messages. However, these are the default responses in FreeIPA.

It’s possible to enumerate users from the [/IPA/session/login_password] API, as shown in the following screenshots: [2](https://www.infosecurity-magazine.com/news/uk-government-zoom-despite-mod/)

#### Invalid account #

![Invalid account](/uploads/assets/static/a63a1dd6-2f8a-4366-91b2-31e46f8db25c.png)

#### Valid account #

![Valid account](/uploads/assets/static/f6517f5b-aca4-402f-83a5-052e92592dbb.png)

However, there is a lockout policy within the HTTP API to lock accounts exceeding invalid authentication attempts.

After triggering the policy, I revisited the asset once the lockout period had timed out.

Attacking this functionality from the HTTP interface was the best idea. I moved my attack into the Kerberos service directly.

## Attacking Kerberos #

I tried enumerating users using the public Kerberos service on UDP/88.

One of the advantages of authenticating in UDP is the ability to craft packets with different source IPs. This can help a lot in evading IP blocklisting on the service level. I didn’t need to jump into that part, as no security controls were triggered within my tests on this service. Both user enumeration and user password brute-forcing were not blocked.

### Building Wordlists #

Based on my background knowledge of Zoom, I understood the email and account profile pattern on Zoom as follows: `{firstName}.{lastName}@zoom.us`. We can get started initializing the naming from the Zoom.us/team page:

![zoom.us/team page](/uploads/assets/static/d68240c3-d577-4931-97b4-6d1853458611.png)

I also enumerated email addresses using OSINT. This will be used to enumerate valid user accounts on the Kerberos service that is publicly accessible.

All of the generated names were not valid users on the Kerberos service - perhaps the two assets were Shadow IT assets mistakenly exposed publicly by Zoom.

User enumeration yielded me a single valid user, “admin”.

![Valid users](/uploads/assets/static/6e2be3cd-0ac6-4a8a-a3e1-9ace84e7d693.png)

I also brute-forced the account password, as there was no lockout policy for user accounts. It seemed like a dead-end for the timespan.

# Discovery of a Memory Leak on a Zoom Production Server #

Zoom allows uploading profile pictures on accounts. I’m always interested in image parsers as the attack surface on image parsers is wide and can open doors for different attack vectors.

I fuzzed the image parsing on Zoom with a range of techniques. Based on my analysis of what was happening in the background:

  1. A user uploads a profile image.
  2. Only JPEG, GIF, and PNG are allowed.
  3. If the image is PNG or GIF, it is converted to JPEG.
  4. Image conversion is not triggered if the image is in JPEG.
  5. The updating profile API aborts the process if the image contains an invalid image header.
  6. The check for validating images is done by checking the magic bytes [4](https://en.wikipedia.org/wiki/File_format#Magic_number). This means we can’t control the first bytes of the file.

Based on my fingerprinting, I assumed that Zoom is using ImageMagick as a backend to their image conversion on their server side. The typical pattern for deploying image conversion microservices is that they barely receive required updates and security controls once the microservice reaches a stable state. This happens as it is not as vital to the business as other functionalities within the infrastructure.

One famous vulnerability for ImageMagick is CVE-2016–3714, a remote code execution vulnerability.

I tested the functionality with the CVE-2016–3714, which seemed to be patched.

Another less popular vulnerability that ImageMagick was vulnerable to was a memory leak vulnerability that occurred because of the uninitialization of the memory space on the GIF parser of ImageMagick. As a result, we can leak portions of the memory in a “Heartbleed” approach.

All versions of ImageMagick builds before <https://github.com/ImageMagick/ImageMagick/commit/9fd10cf630832b36a588c1545d8736539b2f1fb5> are vulnerable.

The vulnerability is not commonly known. It also has a registered CVE of CVE-2017-15277.

I generated a payload using the exploit[5](https://github.com/neex/gifoeb) for the vulnerability. When uploading the payload, the converted images were rendered to indicate successful exploitation.

#### Original Payload #

![Payload](/uploads/assets/static/0e356db4-3354-4354-91fe-e3048949f352.png)

When rendered by Zoom APIs.

![Exploit](/uploads/assets/static/697b9388-39bb-419f-98b9-9e98fdf718fd.png)

I further confirmed that this is not a rendering bug on the ImageMagick implementation at Zoom by generating a typical black image by ImageMagick with the exact specs of the payload:
  
  
  $ convert -size 300x300 xc:black black.gif
  

##### Normal view #

![Normal view](/uploads/assets/static/62474d8f-fc8e-458c-87d9-29ca4b972200.png)

##### After Zoom renders a typical GIF image: Rendering an image. #

![](/uploads/assets/static/64174465-50a6-408c-b47d-4407626d3b52.png)

The result showed that this image is rendering normally when supplying a normal GIF image with the exact specifications of the payload, confirming the existence of the security vulnerability and illuminating the part where there is a rendering issue on the ImageMagick setup at Zoom.Us.

## Automating the Exploitation #

To plan the automation of the exploitation of the memory leak at Zoom, I need to:

  1. Generate a new unique payload
  2. Upload it to Zoom
  3. Download the rendered file.
  4. Extract the data from the corrupted file rendered by Zoom.
  5. Repeat and store leaked memory portions.

### Proof of Concept #

![](/uploads/assets/static/cb5f0502-5603-46fc-aefa-b2a315493822.png)

#### Video #

## A Memory Leak on Zoom production is not the end… #

After a week from the time of automating the exploit for the memory leak, I remembered that Tavis Ormandy had researched the GhostScript engine[6](https://bugs.chromium.org/p/project-zero/issues/detail?id=1640). GhostScript is an interpreter for the PostScript language and is also used in ImageMagick.

Tavis’s research disclosed a remote command execution on GhostScript. This research is vital to this functionality since if we can exploit GhostScript on the ImageMagick, we can achieve remote command execution.

I confirmed this vulnerability existed on Zoom’s build with the timeline of ImageMagick patches. In July 2017, the memory leak vulnerability was discovered and patched. In August 2018, GhostScript and ImageMagick patched the remote command execution vulnerability. This meant that if the memory leak was present at Zoom production, the GhostScript RCE was also present.

I replicated this vulnerability locally in my environment based on the environment of Zoom.

#### Proof of Concept Payload #

##### Proof of Concept Payload #

![Proof of Concept Payload](/uploads/assets/static/210bb2b8-2b02-4103-8b0d-bd525de8dd58.png)

##### Local replication of the RCE vulnerability #

![Local reproduction of the RCE vulnerability](/uploads/assets/static/f1674931-f60b-43aa-8ab2-2b27c37c47f8.png)

### Zoom’s Prevention #

There is a check on the magic bytes on uploaded images within the Zoom API [`/p/upload`]. Otherwise, full exploitation of the vulnerability is possible. If the microservice is called in other places, it may still be exploitable there.

# Shadow IT & Zoom #

Shadow IT is a pattern of public services at Zoom. Some instances don’t receive frequent updates and are publicly accessible. I found a development instance that has not been updated for at least ten months, and although I’m not sure, it was pushed to a Zoom customer. This meant that if a vulnerability was patched on production, it may be exploitable on these Shadow IT instances. I confirmed this because Zoom left a version build file on the instance.

![Instance age](/uploads/assets/static/ade2863a-8c6d-4795-9d1c-959f42968461.png)

This screenshot was taken on July 04th, 2020. The build time was September 10th, 2019.

Another addition to complete the hacking puzzle is: <https://bscdev.meetzoom.us/nginx_status>

![Nginx status on the ShadowIT asset](/uploads/assets/static/eb54c7a6-fdf2-4215-b4f4-e2b2e82287b0.png)

The Nginx status page is enabled due to a backend misconfiguration in the development instance, allowing me to have a confident guess that this instance is not heavily used and potentially has lesser logging triggers than the Zoom.us production web app.

It’s showing nine active connections on the instance, making it an excellent fit to test while not triggering alerts.

# Zoom App for Linux #

I also had a testing session on the Zoom App for Linux. The security community has not put a focus on the Zoom client for Linux in terms of security research. I thought of initiating this part.

## Zoom TLS/SSL is Broken By Design on Linux #

Whenever traffic is intercepted with a custom TLS/SSL certificate, Zoom prompts users with this message:

![Zoom: Untrusted Server certificate](/uploads/assets/static/e5148440-d78e-458e-b62e-194edc5caa10.png)

Once users click “Trust anyway”, the certificate is added to a local Zoom database with the fingerprints of the certificate. When the subsequent request occurs, the allowlisted certificate is permitted as expected.

The catch is that all TLS/SSL certificates can be directly “accepted” by malware to the local Zoom database without additional permissions. The custom implementation of the Zoom certificate database does not solely rely on the system CA certificate DB. System CA certificate DB requires root access in normal cases to allow a new SSL/TLS certificate.

I wrote a Proof of concept in Golang that injects TLS/SSL certificate fingerprints into the local Zoom database. Once this code is executed on a user machine, all injected certificates will be accepted without errors on Zoom.

Code:

![](/uploads/assets/static/443e885a-bafd-4c7d-9619-dd40d3d1a745.png)

# Zoom Launcher Implementation: What’s a bad design for an application launcher? Zoom Launcher for Linux #

#### Launching Zoom #

[`/usr/bin/zoom`] is a symlink of [`/opt/zoom/ZoomLauncher`]. When Zoom is called:
  
  
  $ zoom
  

The following occurs.

![Launching Zoom](/uploads/assets/static/0d628519-e589-473e-9dfd-187ab10cc02b.png)

This sounded interesting already.

Zoom is checking if there is a file on the `$PWD` directory that is for Zoom, and it executes it. Otherwise, it navigates to the Zoom installation directory and executes another binary, Zoom executable.

This doesn’t sound good already. But still, the next part is the surprising part. **If there is an executable called “zoom” on the $PWD directory, it will execute it as a child process for /usr/bin/zoom**.

#### Proof of Concept #

![](/uploads/assets/static/1f5041ba-8308-4cd5-951e-b46fd51ca1b4.png)

This breaks all of the protection of application allowlisting, allows malware to run as a subprocess of a trusted vendor (Zoom), and is a bad design/security practice.

I thought about why it was designed this way but didn’t find a good reason.

# Zoom Local Database Implementation: Bad practice for Linux security. #

I noticed another interesting issue in Zoom’s local database implementation. Zoom’s local database allows Zoom to store custom configurations and user data.

**Assuming there is access to the user machine, by any level of permissions, anyone can read and exfiltrate Zoom user data and configuration**.

![Zoomus.db local database permissions](/uploads/assets/static/7a465929-5406-4005-8701-ab4048827f99.png)

The customer data and main PII details are obfuscated, which is good. However, there is still data that is exposed and is essential.

# Zoom is End-to-End Encrypted? Not fully. #

Zoom announced that it now supports end-to-end encryption and has pushed additional security updates to protect users in May 2020[7](https://blog.zoom.us/end-to-end-encryption-update/). It has been everywhere in the news.

During my tests, I also tested Zoom Chat, a feature on Zoom that allows group chats. It will enable teams to collaborate, share files, and send messages.

I have noticed that the **chat logs of Zoom are stored on disk in plain text**. Combining this with the Linux file permissions bad practice means that any process can unrestrictedly access all of the Zoom chats.

### Video #

# Responsible Disclosure #

## Timeline #

  * [April 15th, 2020] Started the experiment.
  * [April 18th, 2020] I reported the Memory Leak at Zoom via [security@zoom.us](mailto:security@zoom.us).
  * [April 23rd, 2020] I Contacted Luta Security (the contractor for the Zoom VDP) via Twitter.
  * [April 26th, 2020] I followed up regarding the vulnerability disclosure. I haven’t received a response.
  * [May 05, 2020] Received: “[Request Closed] Memory Leak at zoom.us”
  * [May 06th, 2020] Tweeted about it: <https://twitter.com/mazen160/status/1257785071278477312>. Zoom support asked me to send it through Hackerone.
  * [May 06th, 2020] Forwarded the original report via Hackerone.
  * [May 06th, 2020] vulnerability triaged on Hackerone.
  * [May 06th, 2020 –> June 05th, 2020] Internal communication about running my automated exploit.
  * [June 05th, 2020] Informed Zoom that I plan to present my ongoing research at DEF CON.
  * [June 05th, 2020] Zoom can’t assess the issue, as no “sensitive data” was seen, despite the vulnerability’s reproducibility and the provided exploit.
  * [June 08th, 2020] Report closed as “Not Applicable”.
  * [July 11th, 2020] Sent my new research results, reporting seven new vulnerabilities and security issues to Zoom.
  * [July 14th, 2020] Acknowledgment about receiving the report and first conclusive response regarding the memory leak issue.
  * [July 24th, 2020] Further explanation from Zoom regarding the findings.

## Zoom’s Analysis & my response to the analysis #

> “Zoom Public Kerberos Authentication”
>
>> Zoom: These were development servers without access to production data. Moreover, authentication required 2FA, so brute forcing a password, though not demonstrated in your report, would have been insufficient to gain access to the system.

While I agree it may be a forgotten development server that was mistakenly exposed, I haven’t seen any references or indications of having 2FA implemented. In all cases, it’s down now, which is excellent.

> “Discovery of a Memory Leak on a Zoom Production Server”:
>
>> Zoom: After an internal investigation, we’ve concluded that the behavior you found was not a memory leak but just our image utility’s best effort at converting a malformed GIF into a JPEG.

This is the **exact** same behavior expected from valid exploitation of the CVE-2017-15277 as analyzed in the original report on ImageMagick [8](https://github.com/ImageMagick/ImageMagick/issues/592).

The observed behavior that occurs in ImageMagick is ImageMagick’s effort in converting a malformed gif, leaking a portion of the system memory when providing a malformed gif that has an uninitialized palette in the gif file; this is where the vulnerability is there.

From <https://github.com/ImageMagick/ImageMagick/issues/592>.

> GIF coder leaves the palette uninitialized if neither the global nor local palette is present in a gif file. If ImageMagick is used as a library loaded into a process that operates on interesting data, this can cause security consequences.

Having a malformed GIF rendered this way confirms the presence of the vulnerability.

> Zoom: We confirmed that ImageMagick is not used for image conversions here.

However, the same vulnerability is reproduced, a fork of ImageMagick. An image processing software that is vulnerable to the same CVE? In all cases, it’s clear that something is wrong.

> “Shadow IT & Zoom”
>
>> Zoom: These are non-sensitive information disclosures from a shared development environment. Information hygiene is important to us, and we appreciate you reporting this finding.

Great! FullHunt.io can help here. The best product out there for mitigating Shadow IT risks.

> “Zoom TLS/SSL is Broken By Design on Linux”
>
>> Zoom: This is per-user certificate pinning and intentionally allows the user to enable custom certificates. Users can write to their database, but no other non-root users can. It’s common best practice to have user applications run at their privilege level, as requiring Zoom to run as root would introduce unnecessary security risks to Zoom and our customers.

> “Zoom Launcher Implementation”
>
>> Zoom: This will be resolved in version 5.2.0 to be released on August 2nd. To exploit this finding, an attacker must have compromised the victim’s computer by other means, only if it ran the Linux operating system. Further, this attack only works if the victim runs Zoom for the first time.

> “Zoom local database implementation”
>
>> Zoom: This will be resolved in version 5.2.0 to be released on August 2nd. Note that, as you stated, to be able to read this data, the attacker would need to have already compromised the victim’s computer by other means, and only if that computer is running a Linux operating system.

I don’t know if the same vulnerability is also reproduced on macOS. It may be worth checking.

> “Zoom is End-to-End Encrypted?”
>
>> Zoom: We’re working on remediation for this finding. Note that an attacker must have already compromised the victim’s device by other means to read this data.

#### I appreciate the detailed analysis done by Zoom Security. #

### Zoom Linux App Update #

On August 03rd, 2020, Zoom 5.2.4 was released without mentioning the security patches. Zoom issued a silent fix to patch the reported security vulnerabilities without informing users about the fixes.

![Zoom release notes for Zoom 5.2.4](/uploads/assets/static/2db018c6-2228-44f6-b775-0f4733098f14.png)

# Conclusion #

Zoom stated that they plan to patch the reported vulnerabilities, and there will be a security fix for the Zoom Linux client on August 02nd.

Zoom has massively grown during the global pandemic. As with any company building its security program, there are many challenges that Zoom appears to be facing despite the large budget for security.

Coordinating the security disclosure has been a challenging experience from a security researcher’s perspective, despite Zoom’s effort to hire top-class security firms to aid in building the program. This is mainly happening because of the “last-minute” implementation of their vulnerability disclosure program. I would be surprised if I’m the only researcher with this experience.

I would also like to note that all of the research was self-funded. I have also not received a bounty/reward for my efforts by Zoom.

Building a security program takes work. There are many aspects to consider and processes to follow. A budget can “aid” in hiring great talents but cannot build the program alone. It’s always important to start building the security program from an early point; it takes time and effort from different teams within the organization. It has always been a challenging initiative to build a security program. A vulnerability disclosure program is only a single aspect in a larger cycle that should be there and done correctly.

I was also surprised that my experience with Zoom did not match my expectations. I have seen many great impressions about the Zoom vulnerability disclosure program in the media. However, what I have experienced was different. I hope this is not because my research was not media-focused with public media involvement.

# Acknowledgment #

I want to thank [Matt Suiche](https://twitter.com/msuiche) of Comae Technologies for his help in making this research available.

# References #

  1. <https://www.cnbc.com/2019/04/18/zoom-ipo-stock-begins-trading-on-nasdaq.html>

  2. <https://www.infosecurity-magazine.com/news/uk-government-zoom-despite-mod/>

  3. <https://www.freeipa.org/page/Main_Page>

  4. <https://en.wikipedia.org/wiki/File_format#Magic_number>

  5. <https://github.com/neex/gifoeb>

  6. <https://bugs.chromium.org/p/project-zero/issues/detail?id=1640>

  7. <https://blog.zoom.us/end-to-end-encryption-update/>

  8. <https://github.com/ImageMagick/ImageMagick/issues/592>

![Mazin Ahmed](/author.jpg)

Author

Mazin Ahmed

Thoughts of a hacker

[ ](/about/#contact)[ ](https://github.com/mazen160)[ ](https://x.com/mazen160)[](https://www.linkedin.com/in/infosecmazinahmed)

[ ](https://www.facebook.com/sharer/sharer.php?u=https://mazinahmed.net/blog/hacking-zoom/&quote=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Share on Facebook")[ ](https://x.com/intent/tweet/?url=https://mazinahmed.net/blog/hacking-zoom/&text=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Post on X")[ ](https://tootpick.org/#text=https://mazinahmed.net/blog/hacking-zoom/%20Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Toot on Mastodon")[ ](https://reddit.com/submit/?url=https://mazinahmed.net/blog/hacking-zoom/&resubmit=true&title=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Submit to Reddit")[ ](https://www.linkedin.com/shareArticle?mini=true&url=https://mazinahmed.net/blog/hacking-zoom/&title=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Share on LinkedIn")[ ](mailto:?body=https://mazinahmed.net/blog/hacking-zoom/&subject=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Send via email")[ ](https://telegram.me/share/url?text=https://mazinahmed.net/blog/hacking-zoom/&url=Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom "Share on Telegram")[](https://bsky.app/intent/compose?text=https://mazinahmed.net/blog/hacking-zoom/Hacking%20Zoom:%20Uncovering%20Tales%20of%20Security%20Vulnerabilities%20in%20Zoom)

* * *

[←→ Bad Marketing: COVID-19 and Cyber Security April 14, 2020 ](https://mazinahmed.net/blog/covid19-and-cybersecurity/)[Interview with Sectastic Podcast: How I started, What is FullHunt, and How are Security Startups in the GCC Region March 22, 2021 →←](https://mazinahmed.net/blog/interview-with-sectastic-podcast/)

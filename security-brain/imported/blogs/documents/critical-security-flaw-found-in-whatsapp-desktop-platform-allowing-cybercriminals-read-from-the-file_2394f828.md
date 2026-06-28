---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-04_critical-security-flaw-found-in-whatsapp-desktop-platform-allowing-cybercriminal.md
original_filename: 2020-02-04_critical-security-flaw-found-in-whatsapp-desktop-platform-allowing-cybercriminal.md
title: Critical Security Flaw Found in WhatsApp Desktop Platform Allowing Cybercriminals
  Read From The File System Access
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cloud-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cloud-security
- mobile-security
- supply-chain
language: en
raw_sha256: 2394f828e39c1bc21ea361ba74afcaa55db476b6b3222dd12dfe4ebfd77dfca1
text_sha256: 92dc1b5b946aa69259da74538b3cd42bd0ecfefcd9d7d8d7986b85ce1b97dd0d
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Critical Security Flaw Found in WhatsApp Desktop Platform Allowing Cybercriminals Read From The File System Access

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-04_critical-security-flaw-found-in-whatsapp-desktop-platform-allowing-cybercriminal.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cloud-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2394f828e39c1bc21ea361ba74afcaa55db476b6b3222dd12dfe4ebfd77dfca1`
- Text SHA256: `92dc1b5b946aa69259da74538b3cd42bd0ecfefcd9d7d8d7986b85ce1b97dd0d`


## Content

---
title: "Critical Security Flaw Found in WhatsApp Desktop Platform Allowing Cybercriminals Read From The File System Access"
page_title: "Blog | HUMAN Security"
url: "https://www.perimeterx.com/tech-blog/2020/whatsapp-fs-read-vuln-disclosure/"
final_url: "https://www.humansecurity.com/tech-engineering-blog/"
authors: ["Gal Weizman (@WeizmanGal)"]
programs: ["Meta / Facebook"]
bugs: ["Stored XSS", "CSP bypass", "Open redirect", "RCE"]
bounty: "12,500"
publication_date: "2020-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4793
---

# HUMAN Blog

HUMAN Insight and Research from our team

[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2024_RedisTechBlog-2.jpg&w=1921&q=100)Tech & Engineering BlogSeamlessly Scaling Redis: From Blue-Green Deployments to Persistent Data Clusters – Part 1READ NOW](/tech-engineering-blog/seamlessly-scaling-redis-from-blue-green-deployments-to-persistent-data-clusters-part-1/)

  * [![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_JavaScript-Library-2.jpg&w=1921&q=100)Tech & Engineering BlogBuilding a Core Edge Computing Library in TypeScriptREAD NOW](/tech-engineering-blog/building-a-core-edge-computing-library-in-typescript/)
  * [![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Kafka-Producer-Bl-2.jpg&w=1921&q=100)Tech & Engineering BlogOptimizing Kafka for ThroughputREAD NOW](/tech-engineering-blog/optimizing-kafka-for-throughput/)
  * [![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Autobots-Tech-Blog-2.jpg&w=1921&q=100)Tech & Engineering BlogAutobot Laws, Roll OutREAD NOW](/tech-engineering-blog/autobot-laws-roll-out/)

##### All Tech Engineering Blogs

CategoryBot FraudEngineeringMagecartResearch & DetectionRetailSecurityTechnology and Engineering

[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog_TypeScript-pt2.jpg&w=1921&q=100)Tech & Engineering BlogBuilding a Core Edge Computing Library in TypeScript, Part IIREAD NOW](/tech-engineering-blog/building-a-core-edge-computing-library-in-typescript-part-ii/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2024_RedisTechBlog-2.jpg&w=1921&q=100)Tech & Engineering BlogSeamlessly Scaling Redis: From Blue-Green Deployments to Persistent Data Clusters – Part 1READ NOW](/tech-engineering-blog/seamlessly-scaling-redis-from-blue-green-deployments-to-persistent-data-clusters-part-1/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_JavaScript-Library-2.jpg&w=1921&q=100)Tech & Engineering BlogBuilding a Core Edge Computing Library in TypeScriptREAD NOW](/tech-engineering-blog/building-a-core-edge-computing-library-in-typescript/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Kafka-Producer-Bl-2.jpg&w=1921&q=100)Tech & Engineering BlogOptimizing Kafka for ThroughputREAD NOW](/tech-engineering-blog/optimizing-kafka-for-throughput/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Autobots-Tech-Blog-2.jpg&w=1921&q=100)Tech & Engineering BlogAutobot Laws, Roll OutREAD NOW](/tech-engineering-blog/autobot-laws-roll-out/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_HC_ChatGPT_PCI-DSS_Magecart-2.jpg&w=1921&q=100)Tech & Engineering BlogMagecart and the PCI-DSS 4.0 Challenge: Is ChatGPT the Answer?READ NOW](/tech-engineering-blog/magecart-and-the-pci-dss-4-0-challenge-is-chatgpt-the-answer/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_HC_Katalina-2.jpg&w=1921&q=100)Tech & Engineering BlogKatalina: an open-source Android string deobfuscatorREAD NOW](/tech-engineering-blog/katalina-an-open-source-android-string-deobfuscator/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Go-Struction-2-2.jpg&w=1921&q=100)Tech & Engineering BlogFinding the Best Go Project Structure – Part 2READ NOW](/tech-engineering-blog/finding-the-best-go-project-structure-part-2/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Go-structure-2.jpg&w=1921&q=100)Tech & Engineering BlogFinding The Best Go Project Structure – Part 1READ NOW](/tech-engineering-blog/finding-the-best-go-project-structure-part-1/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Hackathon-2.jpg&w=1921&q=100)Tech & Engineering BlogThe best way to save on data storage? Only spend for what you useREAD NOW](/tech-engineering-blog/the-best-way-to-save-on-data-storage-only-spend-for-what-you-use/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Exposed-Repository-2.jpg&w=1921&q=100)Tech & Engineering BlogExposed Repository: Fixing the Accidental Public Repo BreachREAD NOW](/tech-engineering-blog/exposed-repository-fixing-the-accidental-public-repo-breach/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Power-Questions-for-Manager-2.jpg&w=1921&q=100)Tech & Engineering BlogPower Questions for ManagersREAD NOW](/tech-engineering-blog/power-questions-for-managers/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Integrated-Redux-with-Micro-Frontends-2.jpg&w=1921&q=100)Tech & Engineering BlogHow I’ve Integrated Redux with Micro-FrontendsREAD NOW](/tech-engineering-blog/how-ive-integrated-redux-with-micro-frontends/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Pulumi-Approaches-2.jpg&w=1921&q=100)Tech & Engineering BlogPulumi approaches: Micro stacks vs Monolithic stackREAD NOW](/tech-engineering-blog/pulumi-approaches-micro-stacks-vs-monolithic-stack/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Tech-Blog-images_2022-defeating-js-obfuscation-2.jpg&w=1921&q=100)Tech & Engineering BlogDefeating Javascript ObfuscationREAD NOW](/tech-engineering-blog/defeating-javascript-obfuscation/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Tech-Blog-images_2022-boosting-json-go-2.jpg&w=1921&q=100)Tech & Engineering BlogBoosting Up JSON Performance of Unstructured Structs in GoREAD NOW](/tech-engineering-blog/boosting-up-json-performance-of-unstructured-structs-in-go/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_Automating-Skimmer-Deobfuscation-2.jpg&w=1921&q=100)Tech & Engineering BlogAutomating Skimmer DeobfuscationREAD NOW](/tech-engineering-blog/automating-skimmer-deobfuscation/)[![](/_vercel/image?url=https:%2F%2Fhumanprod.wpenginepowered.com%2Fwp-content%2Fuploads%2F2025%2F01%2FHMN_Blog-images_2023_The-Far-Point-of-a-Static-Encounter-2.jpg&w=1921&q=100)Tech & Engineering BlogThe Far Point of a Static EncounterREAD NOW](/tech-engineering-blog/the-far-point-of-a-static-encounter/)

  *  * 1
  * 2
  * 3
  * 4
  * 5
  *

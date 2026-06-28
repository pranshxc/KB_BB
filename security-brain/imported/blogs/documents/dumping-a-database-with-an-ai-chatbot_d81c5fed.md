---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-30_dumping-a-database-with-an-ai-chatbot.md
original_filename: 2024-05-30_dumping-a-database-with-an-ai-chatbot.md
title: Dumping a Database with an AI Chatbot
category: documents
detected_topics:
- sso
- sqli
- command-injection
- mfa
- automation-abuse
- cloud-security
tags:
- imported
- documents
- sso
- sqli
- command-injection
- mfa
- automation-abuse
- cloud-security
language: en
raw_sha256: d81c5feda643cd59d3f76a08dbeac15c63932b5b56559683a3671ec3b2ca2c7e
text_sha256: 0d339f442a14cb941bf59f493b7715819e13c550486673afe4eaf8b93dab4f5e
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Dumping a Database with an AI Chatbot

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-30_dumping-a-database-with-an-ai-chatbot.md
- Source Type: markdown
- Detected Topics: sso, sqli, command-injection, mfa, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `d81c5feda643cd59d3f76a08dbeac15c63932b5b56559683a3671ec3b2ca2c7e`
- Text SHA256: `0d339f442a14cb941bf59f493b7715819e13c550486673afe4eaf8b93dab4f5e`


## Content

---
title: "Dumping a Database with an AI Chatbot"
page_title: "Dumping a Database with an AI Chatbot | Synack"
url: "https://www.synack.com/blog/dumping-a-database-with-an-ai-chatbot/"
final_url: "https://www.synack.com/exploits-explained/dumping-a-database-with-an-ai-chatbot/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["AI", "LLM", "Chatbot"]
publication_date: "2024-05-30"
added_date: "2024-06-05"
source: "pentester.land/writeups.json"
original_index: 270
---

[ Synack logo ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/icon/logo.svg) ](https://www.synack.com)

mobile menu button

search input label submit search button ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/icon/search-mobile.svg)

  * Go Back
  * Platform
  * Platform Tab Intro Section

AI and human powered pentesting platform

Synack unites the power of human expertise and AI technology to deliver continuous, trusted security testing at scale.

Platform Products

  * Platform Overview
  * Column 1
  * [The Synack PlatformAccess to on-demand researchers, vulnerability management, integration, and reporting](https://www.synack.com/platform/)
  * [On Demand Researchers (SRT)The Synack Red Team (SRT) unites over 1,500 of the world’s most skilled and trusted security researchers](/red-team/)
  * Column 2
  * [Sara AI PentestingSara, Synack Autonomous Red Agent identifies, validates, and prioritizes vulnerabilities across the enterprise attack surface](https://www.synack.com/platform/ai-pentesting/)
  * [Integrations](/partners/technology-partners/)
  * Products Overview
  * Column 1
  * [Penetration Testing](/products/penetration-testing-as-a-service/)
  * Gray Box
  * Column 1
  * [AI and LLM Pentesting](https://www.synack.com/products/ai-and-llm-pentesting/)
  * [API Penetration Testing](/products/api-penetration-testing/)
  * [Application Penetration Testing](/products/application-penetration-testing/)
  * Column 2
  * [Cloud Penetration Testing](/products/cloud-penetration-testing/)
  * [Compliance Penetration Testing](/products/pentesting-compliance/)
  * [Attack Surface Management](https://www.synack.com/products/attack-surface-management/)
  * [Vulnerability Disclosure Program](https://www.synack.com/products/vulnerability-disclosure-program/)
  * Solutions
  * Solutions Tab Intro Section

AI AND HUMAN POWERED PENTESTING

Synack combines agentic AI and human expertise to deliver pentesting solutions at scale.

SOLUTIONS INDUSTRIES

  * SOLUTIONS OVERVIEW
  * Column 1
  * [Penetration Testing Overview](/solutions/penetration-testing/)
  * [Third Party Testing](/solutions/pentesting-third-party-risk/)
  * [Scalable Security Talent](https://www.synack.com/solutions/cybersecurity-talent-shortage/)
  * [Beyond Bug Bounty](https://www.synack.com/solutions/go-beyond-bug-bounty/)
  * Column 2
  * [Active Offense](/solutions/active-offense/)
  * [Vulnerability Management](https://www.synack.com/solutions/vulnerability-management/)
  * [Social Engineering Testing](https://www.synack.com/solutions/social-engineering-penetration-testing/)
  * Industries Overview
  * Column 1
  * [Financial Services](/industries/financial-services/)
  * [Public Sector](/industries/public-sector/)
  * Column 2
  * [Retail / eCommerce](/industries/retail-ecommerce/)
  * [Technology](/industries/security-testing-for-technology/)
  * [Pricing](https://www.synack.com/pricing/)
  * [Why Synack](https://www.synack.com/why-synack/)
  * Company
  * Company Tab Intro Section

AI and human powered pentesting

Synack unites the power of human expertise and AI-driven technology to deliver continuous, trusted security testing at scale.

COMPANY

  * Company
  * Column 1
  * Company Info
  * [About](https://www.synack.com/about/)
  * [Careers](https://www.synack.com/careers/)
  * [Leadership](https://www.synack.com/leadership/)
  * [Contact](https://www.synack.com/contact/)
  * Column 2
  * Media
  * [Resource Hub](https://www.synack.com/resource-hub/)
  * [Press Releases](/resource-hub/?type=synack-press#js-scrollTo-pagination)
  * Column 3
  * [We’re Hiring](/careers/)
  * Open Positions Card

[ ![Synack Employees](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2025/11/synack-employees.jpg) Ready to make an impact? Discover career opportunities at Synack and join a team driving the future of cybersecurity. View Open Positions ](/careers/#jobs)

  * Partners
  * Partners Tab Intro Section

The Premier Security Testing Platform

Synack unites the power of human expertise and AI-driven technology to deliver continuous, trusted security testing at scale.

Partners

  * Partners
  * Column 1
  * PARTNERSHIP OVERVIEW
  * [Partnership Overview](https://www.synack.com/partners/)
  * [Solution ProvidersOur growing worldwide network of value-added resellers and distributors](https://www.synack.com/partners/solution-providers/)
  * Column 2
  * [Technology PartnersSynack’s pre-built integration modules with leading security vendors](https://www.synack.com/partners/technology-partners/)
  * [Strategic AlliancesOur partnerships with system integrators, SOC operators, consulting firms, and managed service providers](https://www.synack.com/partners/strategic-alliances/)
  * Column 3
  * BECOME A PARTNER
  * Partners Card

[ ![Synack](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2025/11/synack-logo-on-blue.png) Synack’s ecosystem of partners enhance our Premier Security Testing with their own offerings to reduce risk of breach for their customers. Become a Partner ](/partner-contact/)

  * Synack Red Team
  * [Synack Red Team Tab Intro Section](https://www.synack.com/red-team/)

SYNACK RED TEAM 

Meet the experts who power Synack’s strategic security testing platform. Our Synack Red Team unites over 1,500 of the world’s most skilled and trusted security researchers, who work with patented technology to deliver best-in-class offensive security testing on a continuous basis.

SYNACK RED TEAM

  * SYNACK RED TEAM
  * Column 1
  * SYNACK RED TEAM OVERVIEW
  * [Read about the SRT](https://www.synack.com/red-team/)
  * [Apply to SRT](https://boards.greenhouse.io/synacksrt/jobs/150860)
  * Column 2
  * PROGRAMS FOR SRT
  * [Acropolis Recognition](https://acropolis.synack.com/)
  * [Envoy](https://www.synack.com/red-team/envoy/)
  * [Pathways](https://www.synack.com/red-team/pathways/)
  * Resource Hub
  * Resource Intro Section

AI AND HUMAN POWERED PENTESTING

Synack combines agentic AI and human expertise to deliver pentesting solutions at scale.

RESOURCE HUB

  * Resource Hub
  * Column 1
  * RESOURCES OVERVIEW
  * [ResourcesBrowse all of our resources including videos, case studies, articles, podcasts and more.](https://www.synack.com/resource-hub/)
  * [BlogsStay up to date on the latest industry trends, company news and research.](https://www.synack.com/blog/)
  * [WE’RE IN! PodcastHear from newsmakers, hackers, and big thinkers around the world share their cybersecurity insights.](/were-in-podcast/)
  * [UnpluggedA video series with candid perspectives on cybersecurity topics that matter.](https://www.synack.com/unplugged/)
  * Column 2
  * [Demo SeriesCut to the Chase. A live demo series that gets the point without wasting your time.](https://www.synack.com/demo-cut-to-the-chase/)
  * [Exploits ExplainedA series featuring technical vulnerability insights from the elite security researchers on the Synack Red Team (SRT).](https://www.synack.com/exploits-explained/)
  * [Knowledge BaseLearn about cybersecurity industry terms and security testing solutions—what they do, why they’re important, and how they work.](https://www.synack.com/knowledge-base/)
  * [EventsJoin us for any in-person event, upcoming conference, or an online webinar.](https://www.synack.com/events/)
  * [ComparisonsCompare Synack side by side with other security testing platforms and vendors.](https://www.synack.com/comparisons/)
  * Column 3
  * FEATURED RESOURCE
  * Featured Resource Card

[ ![Synack 2026 research report cover titled “The State of Vulnerabilities in the AI Era,” featuring 11,000+ vulnerabilities analyzed, AI-era attack surface insights, and MTTR benchmarks.](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2026/06/Screenshot-2026-06-04-at-3.06.02-AM.png) 2026 State of Vulnerabilities Report: See what 11,000+ vulnerabilities reveal about the AI-era attack surface Get the Full Report ](https://go.synack.com/2026-state-of-vulnerabilities-report)

search button ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/icon/circle-search.svg)

  * [Pricing](https://www.synack.com/pricing/)
  * [Get Demo](/demo)

[ login button ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/icon/circle-login.svg) ](https://login.synack.com/)

Search 

search input label search button submit ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/icon/header-search.svg)

scroll it 

![synack-exploits-explained-blog-series-image-no-text](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/blazy.png)

#  Dumping a Database with an AI Chatbot 

Kuldeep Pandya 

0% read 

We’re seeing AI chatbots a lot these days. They’re everywhere from[ Notion](https://www.notion.so/) to[ AWS Docs](https://docs.aws.amazon.com/). Many companies have started implementing their AI chatbots either using OpenAI API or a custom AI model.

While making these AI chatbots is easy, the utmost care should be taken to secure them. Because with bad configurations, many critical vulnerabilities may arise.

For example, I’ll detail a vulnerability I found that allowed me full access to the database as well as the underlying filesystem.

In the blog, I’ll cover:

  * Discovery and authentication bypass
  * Enumerating permissions
  * Dumping the database

This is my first [LLM-related vulnerability](https://portswigger.net/web-security/llm-attacks), and I’m excited to share it with the hacker community.

## **Discovery and Authentication Bypass**

I was on boarded to a Synack Red Team host target. Even on host targets, I mostly probe for HTTP services on common HTTP ports and hunt on them.

I enumerated the HTTP services and ran[ aquatone](https://github.com/michenriksen/aquatone) to take screenshots. After taking the screenshots, I checked each host one by one.

Doing this, I discovered a host that showed a login page like this:

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/login.png)

Following my muscle memory, I entered “admin” into the username field, and to my surprise, I was logged into the application! There was an AI chatbot that I could access.

After doing a little more testing, I discovered that I can enter any random string into the username field and still get a valid authentication cookie. It seemed like there was no authentication at all.

## **Enumerating Permissions**

I had no idea what the chatbot was used for. To understand more, I genuinely asked the chatbot about its capabilities. I had no thoughts about security at this point.

When the AI chatbot replied, my eyes sparkled. It told me that I could query employee data using this chatbot. While this is sensitive enough, it told me that it can run **SQL Queries**.

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/capabilities.png)

Intrigued by the bot’s response, I asked how many departments existed in the organization. It ran an SQL query and gave me the output “**73”**.

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/departments.png)

I noticed that it executed an SQL query to answer the question, meaning it had access to the database.

I wanted to see if the bot would allow me to execute any arbitrary queries. So I asked it to execute the following query and provide the output:

`SELECT * FROM Department LIMIT 10;`

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/top-10-departments.png)

And the bot happily returned the top 10 departments.

## **Dumping the Database**

At this point, I could report this as is, but I wanted to confirm with a few more pieces of evidence.

To confirm, I asked it to show the current database user. This could be found with a query like this:

`SELECT CURRENT_USER;`

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/current-user-1.png)

The current user turned out to be **postgres**. 

To further enumerate the database, I asked the bot to list the tables that existed in the database. It listed several tables but the main table that stood out was the **person** table.

![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/uploads/2024/05/table-names.png)

As a proof of concept, I dumped 10 rows from the **person** table and reported the issue to Synack. This issue belongs to [OWASP-LLM02](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf). The Vulnerability Operations team was quick to accept the vulnerability and provide a reward.

After reporting the issue, I discovered that it was also possible for me to list and read local files using a query like this:

`SELECT pg_ls_dir('./');`

The main takeaway: Stay curious. If you have any questions/doubts, feel free to reach me over [Twitter](https://twitter.com/kuldeepdotexe), [Instagram](https://www.instagram.com/kuldeepdotexe) or [LinkedIn](https://www.linkedin.com/in/kuldeep-pandya-13a26a167/). Happy hacking!

_[Kuldeep Pandya](https://acropolis.synack.com/inductees/kuldeep-pandya?hsLang=en) is a member of the Synack Red Team_.

######  You may also like 

[ ![How Attackers Bypass 2FA with Response Tampering](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/blazy.png) How Attackers Bypass 2FA with Response Tampering  Exploit Explained  ](https://www.synack.com/exploits-explained/how-attackers-bypass-2fa-with-response-tampering/)

[ ![Turning Blind Error-Based SQL Injection into Exploitable Boolean One — Part 3: PostgreSQL](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/blazy.png) Turning Blind Error-Based SQL Injection into Exploitable Boolean One — Part 3: PostgreSQL  Exploit Explained  ](https://www.synack.com/exploits-explained/blind-sql-injection-postgresql-order-by/)

[ ![Beyond the Public PoC Deep Diving CVE 2025-54309](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/blazy.png) Beyond the Public PoC Deep Diving CVE 2025-54309  Exploit Explained  ](https://www.synack.com/exploits-explained/beyond-the-public-poc-deep-diving-cve-2025-54309/)

[ ![Client-side Authentication Bypass: 3 Real-World Pentesting Case Studies](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/blazy.png) Client-side Authentication Bypass: 3 Real-World Pentesting Case Studies  Exploit Explained  ](https://www.synack.com/exploits-explained/client-side-authentication-bypass-3-real-world-pentesting-case-studies/)

[ ![footer synack logo](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/logo.svg) ](https://www.synack.com)

[ facebook link  ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/fb.svg) ](https://www.facebook.com/synack)

[ linkedin link  ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/linkedin.svg) ](https://www.linkedin.com/company/synack-inc-/)

[ x link  ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/x.svg) ](https://x.com/synack)

[ instagram  ![](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/instagram.svg) ](https://www.instagram.com/synackofficial/)

TOP

[ Platform  ](https://www.synack.com/platform/)

  * [ The Platform ](https://www.synack.com/platform/)
?>
  * [ Agentic AI (Sara) ](https://www.synack.com/platform/ai-pentesting/)
  * [ FedRAMP ](https://www.synack.com/platform/fedramp/)
  * [ On Demand Researchers ](/red-team/)
  * [ Integrations ](/partners/technology-partners/)

Products 

  * [ Penetration Testing ](https://www.synack.com/products/penetration-testing-as-a-service/)
  * [ Attack Surface Management ](https://www.synack.com/products/attack-surface-management/)
  * [ Vulnerability Disclosure Program ](https://www.synack.com/products/vulnerability-disclosure-program/)

Solutions 

?>
  * [ Active Offense ](https://www.synack.com/solutions/active-offense/)
  * [ Social Engineering Testing ](https://www.synack.com/solutions/social-engineering-penetration-testing/)
  * [ Third Party Testing ](https://www.synack.com/solutions/pentesting-third-party-risk/)
  * [ Beyond Bug Bounty ](https://www.synack.com/solutions/go-beyond-bug-bounty/)
  * [ Vulnerability Management ](https://www.synack.com/solutions/vulnerability-management/)
  * [ Scalable Security Talent ](https://www.synack.com/solutions/cybersecurity-talent-shortage/)
  * [ Penetration Testing Solutions ](https://www.synack.com/solutions/penetration-testing/)

Industries 

?>
  * [ Pentesting Retail / eCommerce ](https://www.synack.com/industries/retail-ecommerce/)
  * [ Pentesting for Financial Services ](https://www.synack.com/industries/financial-services/)
  * [ Pentesting for Technology ](https://www.synack.com/industries/security-testing-for-technology/)
  * [ Pentesting for Public Sector ](https://www.synack.com/industries/public-sector/)

[ Partners  ](https://www.synack.com/partners/)

?>
  * [ ServiceNow and Synack ](https://www.synack.com/partners/servicenow/)
  * [ Solution Providers ](https://www.synack.com/partners/solution-providers/)
  * [ Strategic Alliances ](https://www.synack.com/partners/strategic-alliances/)
  * [ Synack and Accenture Federal Services ](https://www.synack.com/partners/accenture-federal-services/)
  * [ Synack and Microsoft ](https://www.synack.com/partners/microsoft-partnership/)
  * [ Synack Partners with Jira ](https://www.synack.com/partners/jira/)
  * [ Synack Partners with Palo Alto Networks ](https://www.synack.com/partners/synack-partners-with-palo-alto-networks/)
  * [ Synack Partners with Qualys ](https://www.synack.com/partners/synack-partners-with-qualys/)
  * [ Synack Partners with Splunk ](https://www.synack.com/partners/splunk-integration/)
  * [ Synack Partners with Tenable ](https://www.synack.com/partners/synack-partners-with-tenable/)

[ Resource Hub  ](https://www.synack.com/resource-hub/)

  * [ Blog ](/blog/)
  * [ Events ](https://www.synack.com/events/)
  * [ We’re In! Podcast ](/were-in-podcast/)
  * [ Demo Series ](/demo-cut-to-the-chase/)
  * [ Knowledge Base ](/knowledge-base/)

Company 

  * [ About ](https://www.synack.com/about/)
?>
  * [ Careers ](https://www.synack.com/careers/)
  * [ Leadership ](https://www.synack.com/leadership/)

[ Contact Us  ](https://www.synack.com/contact/)

[ Synack Red Team  ](https://www.synack.com/red-team/)

?>
  * [ Pathways ](https://www.synack.com/red-team/pathways/)
  * [ Envoy ](https://www.synack.com/red-team/envoy/)

[ Apply to Red Team  ](https://boards.greenhouse.io/synacksrt/jobs/150860)

© 2026 by Synack.com 

[ Privacy ](https://www.synack.com/privacy-policy/)

[ Terms ](https://www.synack.com/terms-of-use/)

[ Patent Info ](https://www.synack.com/patent/)

[ Disclosure Policy ](https://www.synack.com/disclosure-policy/)

[ Security ](https://www.synack.com/security/)

[ Cookies Policy ](https://www.synack.com/cookies-policy/)

[ Modern Slavery Statement ](/modern-slavery)

[ Sustainability ](https://www.synack.com/environmental-sustainability-policy/)

My Privacy Choices ![My Privacy Choices](https://cdn-ilehafm.nitrocdn.com/CEIcVhvPIRwjlbZfWoPvwdyDLoTdsmEr/assets/images/optimized/rev-ce9e3ba/www.synack.com/wp-content/themes/synack/webroot/images/footer/my-privacy-choices-check.webp)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-26_dns-analyzer-finding-dns-vulnerabilities-with-burp-suite.md
original_filename: 2023-06-26_dns-analyzer-finding-dns-vulnerabilities-with-burp-suite.md
title: DNS Analyzer - Finding DNS vulnerabilities with Burp Suite
category: documents
detected_topics:
- password-reset
- command-injection
- graphql
- api-security
tags:
- imported
- documents
- password-reset
- command-injection
- graphql
- api-security
language: en
raw_sha256: 2231423e4e31370312183f4c08e302a92d12fd38beb42f63003dc61d41d47797
text_sha256: 3956b00e136629277c96b4da48b7d9fb9e421eb068e22d8179f3b19d9f753803
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# DNS Analyzer - Finding DNS vulnerabilities with Burp Suite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-26_dns-analyzer-finding-dns-vulnerabilities-with-burp-suite.md
- Source Type: markdown
- Detected Topics: password-reset, command-injection, graphql, api-security
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `2231423e4e31370312183f4c08e302a92d12fd38beb42f63003dc61d41d47797`
- Text SHA256: `3956b00e136629277c96b4da48b7d9fb9e421eb068e22d8179f3b19d9f753803`


## Content

---
title: "DNS Analyzer - Finding DNS vulnerabilities with Burp Suite"
page_title: "DNS Analyzer - Finding DNS vulnerabilities with Burp Suite - SEC Consult"
url: "https://sec-consult.com/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/"
final_url: "https://sec-consult.com/blog/detail/dns-analyzer-finding-dns-vulnerabilities-with-burp-suite/"
authors: ["Timo Longin (@timolongin)"]
bugs: ["DNS"]
publication_date: "2023-06-26"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 1001
---

1. [ Home ](/)
  2. [ Blog ](/blog/)
  3. DNS Analyzer - Finding DNS vulnerabilities with Burp Suite

# DNS Analyzer - Finding DNS vulnerabilities with Burp Suite

26.06.2023  research news vulnerability 

A brand-new Burp Suite extension for discovering DNS vulnerabilities in web applications.

![Analyzing web applications via Burp Collaborator & DNS Analyzer](/fileadmin/_processed_/4/0/csm_sec-consult-h-Burp_Collaborater_c3b21dc5ea.png)

In our previous DNS blog posts researched by Timo Longin, ["Forgot password? Taking over user accounts Kaminsky style"](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/) and ["Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style"](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/), we've demonstrated how to identify DNS vulnerabilities in web applications and how to **compromise even fully-patched WordPress instances via DNS attacks.** However, finding DNS vulnerabilities isn't a trivial task. Hence Timo Longin, security expert at SEC Consult, has developed and introduced the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server), which allows fine-grained DNS analysis. Even though it's a great tool, it requires the setup of a dedicated domain, a server and so on. Therefore, we've been looking for a better solution and - oh boy - **we found it:_A brand-new Burp Suite extension for discovering DNS vulnerabilities in web applications!_**

[![Redirecting e-mails for password resets via DNS cache poisoning](/fileadmin/_processed_/f/4/csm_sec-consult-c-Web_app_DNS_resolver_97758f4660.png)](/fileadmin/_processed_/f/4/csm_sec-consult-c-Web_app_DNS_resolver_acb5a6802f.png) Redirecting e-mails for password resets via DNS cache poisoning 

## Back to the Basics

Before we get into the solution, let's take a step back for a second. **Why exactly would we analyze web applications for DNS vulnerabilities?** If you want a full run-down of all the little details, check out our previous blog posts [here](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/) and [here](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/), but essentially, it boils down to the following attack:

[![Analyzing web applications via DNS Analysis Server](/fileadmin/_processed_/b/1/csm_sec-consult-c-ADNS_analysis_example_2620174ce7.png)](/fileadmin/_processed_/b/1/csm_sec-consult-c-ADNS_analysis_example_eda80b8da1.png) Analyzing web applications via DNS Analysis Server 

By manipulating the DNS name resolution of a web application, the "Forgot password?" feature can be abused to take over user accounts via e-mail redirection. This attack vector was first mentioned by [Dan Kaminsky back in 2008](https://www.blackhat.com/presentations/bh-jp-08/bh-jp-08-Kaminsky/BlackHat-Japan-08-Kaminsky-DNS08-BlackOps.pdf), but haunts web applications even to this day.

So, how do we find vulnerable web applications and what exactly is the solution?

## The DNS Analyzer

To understand the DNS Analyzer, we must first understand where we came from - the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server). The [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server) allows to analyze the DNS name resolution of a web application as depicted below:

[![Analyzing web applications via Burp Collaborator & DNS Analyzer](/fileadmin/_processed_/f/0/csm_sec-consult-c-Burp_Collaborater_and_DNS_resolver_c7d3a7278b.png)](/fileadmin/_processed_/f/0/csm_sec-consult-c-Burp_Collaborater_and_DNS_resolver_9139845932.png) Analyzing web applications via Burp Collaborator & DNS Analyzer 

  1. In the first step, we force the web application to resolve a specific domain name. In this case, the web application must resolve **0100001337.analysis.example** so it can send a registration e-mail to **test@0100001337.analysis.example**.
  2. Therefore, a DNS query for the **MX record of 0100001337.analysis.example** is sent to the configured DNS resolver in the second step.
  3. The DNS resolver then tries to resolve the **MX record of 0100001337.analysis.example** by querying the authoritative DNS nameserver (ADNS) of **analysis.example**. This ADNS runs the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server), which **actively** and **passively** analyzes the DNS resolver for security issues. For example, it **actively** returns manipulated DNS responses to the DNS resolver and it **passively** logs security-relevant data such as used UDP source ports.
  4. After the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server) has analyzed enough DNS traffic, a log analyzer can be used to process and visualize the results.
  5. Based on the results, the tester can trigger further DNS resolutions via registration, password reset, newsletter, etc..

However, as mentioned before, this setup requires an analysis domain (e.g., "analysis.example"), an analysis server (e.g., EC2 instance) and some installation effort to get everything going. Now, **[Burp Collaborator](https://portswigger.net/burp/documentation/collaborator) and [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) **come into play!

With the capabilities of the [Burp Collaborator](https://portswigger.net/burp/documentation/collaborator) service, we can partially replace the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server) and do some **basic but important** DNS analysis directly in Burp.

![GIF showing Click "Copy to Clipboard" ](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-Copy_to_Clipboard.gif)

  1. In the first step, we again force the web application to resolve a specific domain name. However, in this case, we are using a collaborator domain **r6havapn933jvdt.oastify.com** which was generated by the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer).
  2. Like before, the web application tries to resolve this domain name and sends a DNS query to the configured DNS resolver.
  3. Now, the Burp Collaborator comes into play! The Collaborator server **passively** logs the query from the DNS resolver and returns - contrary to the [DNS Analysis Server](https://github.com/The-Login/DNS-Analysis-Server) \- a non-manipulated DNS response.
  4. The DNS interactions received by the Collaborator server can then be analyzed in the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) extension.
  5. Based on the results, the tester can trigger further DNS resolutions via registration, password reset, newsletter, etc..

With this solution, all that is required is a Burp Suite Professional license!

## DNS Analyzer - Howto

Now that we have a high-level overview of what's happening, how do we exactly use the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer)?

After installing the extension via the instructions on [GitHub](https://github.com/The-Login/DNS-Analyzer), navigate to the "DNS Analyzer" tab and follow the steps below:

1\. Click "Copy to Clipboard" to get a fresh Collaborator domain.

![GIF showing Trigger a DNS resolution](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-register.gif)

2\. Trigger a DNS resolution for this domain. For example, register a user called **test@[your Collaborator domain]** on the target web application.

![GIF showing Table Entries](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-Table_Entries.gif)

3\. Watch how the interaction table fills up more and more. If required, trigger even more DNS resolutions to reach the analysis threshold of 20 interactions.

![GIF showing Selecting Interactions](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-Selecting_Interactions.gif)

4\. Select at least 20 interactions which you want to analyze. The statistics and graphs can then be analyzed in the results pane.

[![Scatter Plots](/fileadmin/_processed_/d/6/csm_sec-consult-c-scatter_plots_9017a6fa77.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-scatter_plots.png) Random distribution of UDP source port and DNS ID values (Kaminsky Status: GREAT) 

#### At this point we have a Kaminsky status, some fancy numbers and scatter plots in front of us, but how do we know if a DNS resolver is vulnerable?

## DNS Analyzer - Interpreting Results

The goal and purpose of the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) is to be able to identify DNS resolvers that are vulnerable to [Kaminsky attacks](https://www.blackhat.com/presentations/bh-jp-08/bh-jp-08-Kaminsky/BlackHat-Japan-08-Kaminsky-DNS08-BlackOps.pdf). We're not going into detail on how the Kaminsky attack works in this blog post, since we've already done this in our previous blog posts ([here](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/) and [here](https://sec-consult.com/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/)) and a quick Google search/ChatGPT prompt will do the trick! However, we can talk about the major requirement for a Kaminsky attack! Essentially, a DNS resolver is most likely vulnerable to a Kaminsky attack, if the random portions of its DNS queries (UDP source port and DNS ID) are not sufficiently random or can be guessed/predicted by an attacker. The [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) allows us to analyze just that in the following three ways:

  * Kaminsky status
  * Scatter plots
  * Statistics

The **Kaminsky status** value gets automatically generated by the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) upon selecting 20+ Collaborator interactions. With its three possible states **POOR** , **GOOD** and **GREAT** it gives a first impression about the predictability of UDP source port and DNS ID values. The following metrics are used:

**Standard deviation:** Checks for a low standard deviation in source port and DNS ID distributions.

  * **POOR** : 0 - 296
  * **GOOD** : 296 - 3980
  * **GREAT** : 3980 - 20000+

**Direction Bias:** Checks if source port and DNS ID distributions are biased in an upward or downward direction.

  * **POOR** : 80% - 100%
  * **GOOD** : 50% - 80%
  * **GREAT** : 0% - 20%

**Port difference (bits):** Checks the differences of the lowest and the highest ports and DNS IDs in bits.

  * **POOR** : 0 - 10 bits
  * **GOOD** : 10 - 13.75 bits
  * **GREAT** : 13.75 - 16 bits

The metrics for these states are a mixture of the metrics from [DNS-OARC](https://www.dns-oarc.net/oarc/services/porttest) and the [Gibson Research Corporation (GRC)](https://www.grc.com/dns/dns.htm). Furthermore, the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) always chooses the worst/lowest metric for the Kaminsky status.

However, even though the Kaminsky status and corresponding statistics are great, sometimes the human eye can spot predictable values better than the machine! That's where the scatter plots come into play!

For example, when we look at the following two scatter plots, we can't see any predictable connections between source port or DNS ID values:

[![Scatter Plots](/fileadmin/_processed_/a/c/csm_sec-consult-c-scatter_plots_02_cf8284fb00.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-scatter_plots_02.png) Static distribution of UDP source port values and random distribution of DNS ID values (Kaminsky Status: POOR) 

But now for a vulnerable DNS resolver!

[![Scatter Plots](/fileadmin/_processed_/c/3/csm_sec-consult-c-scatter_plots_03_ccc5fb5204.png)](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-scatter_plots_03.png) Static distribution of every second UDP source port value and random distribution of DNS ID values (Kaminsky Status: GREAT) 

In this case, source ports are assigned statically, which is most likely attackable. Also, the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) correctly flagged this distribution as **POOR**.

Now for a trickier example:

![Static UDP source port values coming from one specific resolver IP](/fileadmin/user_upload/sec-consult/Dynamisch/Blogartikel/2023_06/sec-consult-c-results_sections.gif)

But wait! Why is the Kaminsky status **GREAT**? Shouldn't it be **POOR**?

Yes! However, due to the behavior of some DNS resolvers, it's hard to detect such distributions automatically without causing lots of false positives. Nevertheless, this distribution is vulnerable!

#### **Human: 1, Machine: 0**

In the above example it is important to mention that such distributions of source ports actually exist! Sometimes DNS resolvers can be very convoluted and individual DNS resolutions can take very different paths. This is why the results pane is separated into different sections based on the external resolver IP address. The first section "All Resolver IPs" includes DNS queries from all resolver IPs. After that each individual resolver IP address is listed.

[![Statistics and scatter plots of the Google public DNS resolver showing no signs of a vulnerability ](/fileadmin/_processed_/d/4/csm_sec-consult-c-scatter_plots_google_arrow_d83e807239.png)](/fileadmin/_processed_/d/4/csm_sec-consult-c-scatter_plots_google_arrow_1bf8562fbc.png) Statistics and scatter plots of the Google public DNS resolver showing no signs of a vulnerability (Kaminsky Status: GREAT) 

As the above animation shows, static source ports were only used by one specific resolver IP address!

Aside from the Kaminsky status and scatter plots, the statistics and general info sections can contain crucial information as well. For example, sometimes web applications are using large public DNS resolvers like [Google](https://developers.google.com/speed/public-dns), [Cloudflare](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1) or [Cisco](https://www.opendns.com/cisco-opendns/), which are generally more secure and most likely not vulnerable. If you seem to have found a vulnerability in one of them, it's most likely a false positive!

## Bug Bounty Considerations

Should you be looking for DNS vulnerabilities in bug bounty domains?  
**YES!** However, only report a DNS vulnerability if:

  1. infrastructure is in the scope of the bug bounty program
  2. you've confirmed the vulnerability via in-depth DNS analysis (e.g., via the [DNS-Analysis-Server](https://github.com/The-Login/DNS-Analysis-Server))

Essentially, **don't flood bug bounty programs with DNS vulnerability reports without doing proper research first!**

Also, if you've found a vulnerable web application, let us know on Twitter [@sec_consult](https://twitter.com/sec_consult).

## Backstory and Honorable Mentions

Back in 2021, when we published [our first DNS blog post](https://sec-consult.com/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/), Timo had chat with James Kettle ([@albinowax](https://twitter.com/albinowax)) about implementing a Burp extension that uses Burp Collaborator for DNS analysis (so basically what the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) is today). After some back and forth, this led to a [feature request](https://forum.portswigger.net/thread/providing-udp-source-ports-in-burp-collaborator-aadadf82) in the Portswigger forum. After promoting the feature request in one of my guest lectures at [FH Campus Wien](https://www.fh-campuswien.ac.at/), the feature request got some traction and was eventually implemented in [version 2022.12.4](https://portswigger.net/burp/releases/professional-community-2022-12-4) of Burp Suite.

So, in conclusion, a big **THANK YOU** goes out to:

  * **James Kettle** for his crucial initial input
  * **Portswigger** for honoring and implementing feature requests from the community
  * **The students of FH Campus Wien** for pushing the feature request

## Final Words

This sums up the most important facts about the [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer)!

The [DNS Analyzer](https://github.com/The-Login/DNS-Analyzer) was written by Timo Longin, aka Login. If there are any further questions you can reach out to him on Twitter ([@timolongin](https://twitter.com/timolongin)) or on Mastodon ([@login@infosec.exchange](https://infosec.exchange/@login)).

Also, the DNS Analyzer will hopefully soon be available via the [BApp Store](https://portswigger.net/bappstore)!

Happy hacking!

 _This research was done by Timo Longin and published on behalf of the[SEC Consult Vulnerability Lab](https://sec-consult.com/vulnerability-lab/)._

###  Are you interested in working at SEC Consult? 

SEC Consult is always searching for talented security professionals to work in our team. 

[ More Information ](/career/#c2854)

##  More On The Topic 

### [Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

[![](/fileadmin/_processed_/0/8/csm_sec-consult-h-iceberg_c4d1557faf.jpg)](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

06.10.2022 vulnerability

Hidden DNS resolvers and how to compromise your infrastructure 

[ Read more ](/blog/detail/melting-the-dns-iceberg-taking-over-your-infrastructure-kaminsky-style/ "Melting the DNS Iceberg: Taking over your infrastructure Kaminsky style")

### [Forgot password? Taking over user accounts Kaminsky style](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

[![](/fileadmin/_processed_/5/0/csm_sec-consult-h_pwd_dns_image_1_en_675bb23e07.png)](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

21.07.2021 

The "Forgot password?" feature and how DNS vulnerabilities may allow the takeover of user accounts. 

[ Read more ](/blog/detail/forgot-password-taking-over-user-accounts-kaminsky-style/ "Forgot password? Taking over user accounts Kaminsky style")

[ Back ](/blog/)

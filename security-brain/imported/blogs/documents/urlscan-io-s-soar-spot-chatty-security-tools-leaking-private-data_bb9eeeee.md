---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-01_urlscanios-soar-spot-chatty-security-tools-leaking-private-data.md
original_filename: 2022-11-01_urlscanios-soar-spot-chatty-security-tools-leaking-private-data.md
title: 'urlscan.io''s SOAR spot: Chatty security tools leaking private data'
category: documents
detected_topics:
- automation-abuse
- supply-chain
- oauth
- api-security
- sso
- command-injection
tags:
- imported
- documents
- automation-abuse
- supply-chain
- oauth
- api-security
- sso
- command-injection
language: en
raw_sha256: bb9eeeee2d7d00c2da5f81c7708fd7fb101daab54bdb15990bf2eaa6570c5a8e
text_sha256: 2e5ef1eceb5d1d7724b8d19bf1dbf13ae18625f443399effc717ab474bf22f2a
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# urlscan.io's SOAR spot: Chatty security tools leaking private data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-01_urlscanios-soar-spot-chatty-security-tools-leaking-private-data.md
- Source Type: markdown
- Detected Topics: automation-abuse, supply-chain, oauth, api-security, sso, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `bb9eeeee2d7d00c2da5f81c7708fd7fb101daab54bdb15990bf2eaa6570c5a8e`
- Text SHA256: `2e5ef1eceb5d1d7724b8d19bf1dbf13ae18625f443399effc717ab474bf22f2a`


## Content

---
title: "urlscan.io's SOAR spot: Chatty security tools leaking private data"
page_title: "urlscan.io's SOAR spot: Chatty security tools leaking private data | Positive Security"
url: "https://positive.security/blog/urlscan-data-leaks"
final_url: "https://positive.security/blog/urlscan-data-leaks"
authors: ["Fabian Bräunlein"]
bugs: ["Information disclosure"]
publication_date: "2022-11-01"
added_date: "2022-11-03"
source: "pentester.land/writeups.json"
original_index: 1964
---

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436cf0ef16e7ad_menu_icon_flipped.png)

[HOME](/)[About](/about)[Services](/services)[Blog](/blog)[Contact](/contact)

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c270016e798_purple.png)](/)

# urlscan.io's SOAR spot: Chatty security tools leaking private data

November 2, 2022

By 

[Fabian Bräunlein](mailto:fabian@positive.security)

![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6358304b4951324ae820a732_urlscan_mining_cover.png)

  * Sensitive URLs to shared documents, password reset pages, team invites, payment invoices and more are publicly listed and searchable on [urlscan.io](http://urlscan.io), a security tool used to analyze URLs
  * Part of the data has been leaked in an automated way by other security tools that accidentally made their scans public (as did GitHub earlier this year)
  * Users of such misconfigured Security Orchestration, Automation and Response (SOAR) tools have a high risk of their accounts being hijacked via manually triggered password resets
  * We are in no way affiliated with urlscan.io and just want to inform the public of its risk and potential in offensive security

Most of our readers probably know [Google Dorks](https://en.wikipedia.org/wiki/Google_hacking). Some may have also searched through data in public S3 buckets or implemented a scraper for Pastebin. But are you familiar with [urlscan.io](http://urlscan.io), and what kind of data you can find there that is arguably even more private?

\-- MARKDOWN --

# Table of Contents  
\- [Introduction: Github data leak](#introduction-github-data-leak)  
\- [What is urlscan.io?](#what-is-urlscan.io-)  
\- [Lots of data](#lots-of-data)  
\- [Lots of integrations](#lots-of-integrations)  
\- [What sensitive data can be mined?](#what-sensitive-data-can-be-mined-)  
\- [urlscan.io dorks](#urlscan-io-dorks)  
\- [Apple seems to have disappeared?](#apple-seems-to-have-disappeared-)  
\- [Where does the data come from?](#where-does-the-data-come-from-)  
\- [Contacting users](#contacting-users)  
\- [Contacting urlscan.io](#contacting-urlscan-io)  
\- [How exactly did the data end up there?](#so-how-exactly-did-the-data-end-up-there-)  
\- [Response](#response)  
\- [Multi-step account takeover](#multi-step-account-takeover)  
\- [Recommendations](#recommendations)  
\- [Conclusion](#conclusion)  
\- [Timeline](#timeline)  
\-- /MARKDOWN --

# Introduction: Github data leak

In February this year, GitHub sent an email to affected customers notifying them of a data breach. Specifically, users that enabled hosting via Github Pages for a private repository had the repository name leaked (together with their username).

There seems to be no public acknowledgement of this breach, and I was only made aware through a [Hacker News post](https://news.ycombinator.com/item?id=30348980), where the full email was posted.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b6105403d961685fb29861_hn.png)](https://positive.security/#zoom)

So, how did that happen?

From the mail:

> GitHub learned from an internal discovery by a GitHub employee, that GitHub Pages sites published from private repositories on GitHub were being sent to [urlscan.io](http://urlscan.io) for metadata analysis as part of an automated process

GitHub responded to the breach by “ _fixing the automated process that sends GitHub Pages sites for metadata analysis so that only public GitHub Pages sites are sent for analysis”_ as well as asking the 3rd-party to delete the data.

Seeing that GitHub can make the mistake of accidentally listing their internal urlscan.io scans publicly, I thought the site could contain potential for more data leaks.

As I hadn’t heard of the site before, I decided to check it out.

# What is urlscan.io?

[urlscan.io](http://urlscan.io/) describes itself as “a sandbox for the web”, where you can submit URLs which are then analyzed and scanned in various ways, mainly to detect malicious websites such as phishing sites. Besides analyzing the URLs submitted via the website, urlscan.io also scans URLs from public data sources and provides an API to integrate the check into other products. This last option is the one that lead to the systematic data leak of private repository URLs by GitHub.

## Lots of data

At the time of writing, the landing page listed 124k public, 76k unlisted and 436k private scans performed within the last 24 hours.

It also includes one of those “recent scan” views that is typical for that kind of security scanning sites (e.g. compare with <https://www.ssllabs.com/ssltest/>).

What is however more surprising is the option to search through all historical data (as an unauthenticated user) using the [extensive ElasticSearch Query String syntax](https://urlscan.io/docs/search/). This was also mentioned in GitHub’s notification mail:

> To view the name of the private repository on [urlscan.io](http://urlscan.io), you would need to have been looking at the front page of [urlscan.io](http://urlscan.io) within approximately 30 seconds of the analysis being performed **or have specifically searched using a query that would return the analysis in the search results.**

For every scan result, the service provides a lot of information:

  * The submitted URL (with all GET parameters)
  * The effective URL in case of a redirect
  * Any HTTP requests that were performed while scraping/scanning the URL
  * Information about the IPs and domains communicated with
  * A screenshot of the page taken at the time of the scan
  * The full HTML response of the site

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b61064cfc6234bb5a1e0f3_urlscan_info.png)](https://positive.security/#zoom)An OAuth2 redirect flow and other loaded resources captured on urlscan. The submitted URL also contains an UUID, which the web application might not expect to become public.

## Lots of integrations

[urlscan.io’s docs page](https://urlscan.io/docs/integrations/) lists 26 commercial security solutions by vendors such as Palo Alto, Splunk, Rapid7, FireEye and ArcSight that have integrated the service via its API. GitHub, which is directly using this API internally as part of their SaaS offering, is missing from this list however, as are probably many more enterprise customers.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62d092a9d38ec9048366c48a_urlscan_integrations.png)](https://positive.security/#zoom)urlscan is integrated in a multitude of commercial security tools

If any of those tools/API users are accidentally performing public URL scans, this could lead to systematic data leakage. As those advanced security tools are mostly installed in large corporations and government organizations, leaked information could be particularly sensitive.

Besides commercial products, the integration page also lists 22 open-source projects, some of which are information gathering tools, and others are simple library implementations for easier querying of the API.

# What sensitive data can be mined?

With the type of integration of this API (for example via a security tool that scans every incoming email and performs a urlscan on all links), and the amount of data in the database, there is a wide variety of sensitive data that can be searched for and retrieved by an anonymous user.

## urlscan.io dorks

Please find below a collection of clickable “urlscan.io dorks” and (redacted) example results (please note that after reporting our findings to urlscan.io, they have added deletion rules for many of the below dorks so you might need to get a bit creative with the queries yourself):

#### [Password reset links](https://urlscan.io/search/#page.url%3Apassword%20AND%20page.url%3Areset)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b611927d8adbebcdfde485_insta_pw_reset.png)](https://positive.security/#zoom)An Instagram password reset confirmation page that requests the user to enter the new password twice

#### [Account creation links](https://urlscan.io/search/#page.url%3Apassword%20AND%20page.url%3Acreate)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b6119f03d961040fb2bff1_zendesk_pw_reset.png)](https://positive.security/#zoom)The initial password setup page for an NBC News account on Zendesk (a customer support and sales SaaS)

#### [API keys](https://urlscan.io/search/#page.url%3Aapikey)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b612ca2f00918671eda8d5_virustotal_api_key.png)](https://positive.security/#zoom)A link containing a valid VirusTotal API key

#### [Telegram bots](https://urlscan.io/search/#page.domain%3Aapi.telegram.org)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b612d23d21d07a5068ed83_telegram_bot.png)](https://positive.security/#zoom)Telegram API URLs contain a long, secret identifier that can be used to call different [API methods](https://telegram-bot-sdk.readme.io/reference/getme) on the bot

#### [DocuSign signing requests](https://urlscan.io/search/#page.domain%3Adocusign.net%20AND%20page.url%3ASigning%20AND%20page.url%3Ati)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b612daf61e916316428b19_docusign.png)](https://positive.security/#zoom)DocuSign signing requests usually contain contractual documents with sensitive information

#### [Shared Google Drive documents](https://urlscan.io/search/#page.domain%3Adrive.google.com)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d8123f3172c645228b3f_gdrive_shared_folder.png)](https://positive.security/#zoom)

#### [Dropbox file transfers](https://urlscan.io/search/#page.domain%3Adropbox.com%20AND%20page.url%3Atransfer)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d82a7b0b187ba873363c_dropbox_police.png)](https://positive.security/#zoom)

#### [Sharepoint invites](https://urlscan.io/search/#page.url%3Ainvitation%20AND%20page.domain%3Asharepoint.com)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b616dc2f00917320edd77d_sharepoint_invite.png)](https://positive.security/#zoom)As SharePoint workspaces are tied to organizations, the subdomain already gives a clue what the invite is for (in this case the "Government of Ontario", as confirmed in the invite text)

#### [Discord invites](https://urlscan.io/search/#page.domain%3Adiscord.com%20AND%20page.url%3Ainvite)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b616e636589e583f5c13fc_discord_invite.png)](https://positive.security/#zoom)The search query returns over 7k Discord invite codes for various communities

#### [Government Zoom invites](https://urlscan.io/search/#page.domain%3Azoomgov.com)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b616f04cc86858e0ed75d0_zoomgov.png)](https://positive.security/#zoom)More sensitive than Discord invites might be Zoom invites, in particular to court hearings

#### [WebEx meeting recordings](https://urlscan.io/search/#page.url%3Arecordingservice)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d83ea445bc10312eae2f_webex_recording.png)](https://positive.security/#zoom)

#### [PayPal invoices](https://urlscan.io/search/#page.domain%3Apaypal.com%20AND%20page.url%3Ainvoice)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617023b830881c4a5cf81_paypal_invoice.png)](https://positive.security/#zoom)A PayPal-hosted invoice obviously contains all the (personal) information needed for a valid invoice and can be retrieved by anyone that knows its ID. Please not however that [those invoices are also used for spamming/scamming](https://krebsonsecurity.com/2022/08/paypal-phishing-scam-uses-invoices-sent-via-paypal/).

#### [Paypal money claim requests](https://urlscan.io/search/#page.url%3A%22transfer%2Fclaim-money%22)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617688f515005f60cc87d_paypal_claim.png)](https://positive.security/#zoom)PayPal money claim requests "only" prefill the target's email address (together with the amount and recipient), leaking a bit less information than the invoice

#### [Package tracking links](https://urlscan.io/search/#page.domain%3Adhl.de%20AND%20page.url%3Apiececode)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b61773fb58ea03b147bbb3_package_tracking.png)](https://positive.security/#zoom)Package tracking links for various postal services can be found as well. Interestingly, DHL seems to be aware of the risk of leaked tracking codes and asks for the recipient's ZIP code before showing their address. Note: With only 8k ZIP codes existing for locations in Germany, and the general area being known from the package trace, the code might be guessable

#### [Amazon gift delivery links](https://urlscan.io/search/#page.domain%3Aamazon.com%20AND%20page.url%3Agcx)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d8c70fc47522fd3595d1_amazon_gift.png)](https://positive.security/#zoom)Amazon gift delivery links leak the name of the giver and the gifted item.

#### [Unsubscribe links](https://urlscan.io/search/#page.url%3Aunsubscribe)

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b6179c3aaf473327441172_hibp_unsubscribe.png)](https://positive.security/#zoom)A HIBP unsbscribe link that would allow cancelling the breach notifications for a domain (Good: The domain itself is not shown on the page)[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617a738ce8f1cf2e795cc_paypal_unsubscribe.png)](https://positive.security/#zoom)On the PayPal unsubscribe page, the user's email address is fully shown. Some other services at least partially redact the email address on unsubscribe pages

## Apple seems to have disappeared?

Interestingly, when I performed my initial search back in February, I could find a lot of juicy URLs for Apple domains:

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62c4305f4a5b32a02cd8799b_apple_1.png)](https://positive.security/#zoom)An Apple Developer ID activation page that allows setting the new password (seemingly a developer related to a Cancer Center)[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617b9c338e074425f9900_apple_2.png)](https://positive.security/#zoom)An Apple ID finalization page that allows setting the password, seemingly for a Gamestop account[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d86eb0769527ed559f7f_apple_3.png)](https://positive.security/#zoom)A Family Sharing invite, which allows the use of other's purchased subscriptions and might even give access to the family's photos and device's locations[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617c6bbb02578fca9ef14_apple_4.png)](https://positive.security/#zoom)Invites for Enterprise-only online events[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617cce86364f6d215f120_apple_5.png)](https://positive.security/#zoom)iCloud of course also has the option to create public sharing links, which were leaked via urlscan.io[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/6318d88b73ba27346c0f193b_apple_6.png)](https://positive.security/#zoom)For iCloud Calendar invites, Apple seems to also create a link with all information

It seems like this information has in the meantime been hidden or deleted from the database:

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62b617dd2f00910b21ede53e_apple_deleted.png)](https://positive.security/#zoom)Searching for any scans for apple.com (and its subdomains) now only returns 2 results

However, when continuously monitoring the [above result page](https://urlscan.io/search/#page.domain%3Aapple.com), sometimes some fresh additional entries can be spotted, which disappear again within around 10 minutes.

We later found out that Apple has in the meantime requested an exclusion of their domains from the scan results, which is implemented via periodically deleting all scan results matching certain rules.

Overall, the urlscan.io service contains a trove of sensitive information of various kinds, that can be used by hackers, spammers, or cyber criminals for example to take over accounts, perform identity theft, or run believable phishing campaigns.

# Where does the data come from?

We can see from the details of a scan result whether a scan was submitted via the API, but we can not find out which application or integration submitted the scan request.

For this, we had two options:

  * **Contact affected users.** Send mails to users with leaked email address to inform them of the leak and inquire about any security tooling that might be the culprit.
  * **Contact urlscan.io.** Send a list of suspicious automated submissions and ask urlscan to investigate whether any integrations have the scan option accidentally set to public.

We decided to do both and started contacting users while also collecting a list of scan results to send to urlscan.io.

### Contacting users

We sent 23 mails to individuals whose email addresses were leaked in API-started scans (15 were from unsubscribe links, 5 from PayPal invoices, 2 from password reset links, and 1 from a PayPal claim).

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62c758a869abf940f19be8bd_notification_mail.png)](https://positive.security/#zoom)Example mail sent out with a link to the corresponding urlscan result page and a test link at the bottom

At the end of the notification mails were "bait links" with unique UUIDs to test whether any URLs will be auto-submitted to urlscan.io. If that was the case, the unique token would allow us to associate the scan request back to a mail recipient.

Out of the 23 test links that we sent out, 9 (~40%) were submitted via the API to urlscan.io (most of them immediately after the corresponding mail was sent):

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62c720af372331304b6e53cc_pingbacks.png)](https://positive.security/#zoom)Public results for the "private" test links included in the notification mails (please note that some URLs were scanned multiple times)

Without counting PayPal invoices (which might have actually [been created as part of a scam campaign](https://krebsonsecurity.com/2022/08/paypal-phishing-scam-uses-invoices-sent-via-paypal/)), the success rate is 9 out of 18 (50%).

The next day we sent out another 24 mails to email addresses from [leaked hubspot unsubscribe links ](https://urlscan.io/search/#page.domain%3Ahubspotemail.net%20AND%20page.url%3Aunsubscribe)with 12 of them (50% again) triggering a public scan.

Those "pingbacks" show us several things:

  * Our assumption of there being misconfigured security tools that submit any link received via mail as public scan to urlscan.io seems to be correct
  * Users of those misconfigured security tools are at a high risk of losing all of their online accounts (via a multi-step attack explained in the next section)
  * Seemingly low-severity urlscan.io findings (such as an email address from an unsubscribe link) can have critical impact

For organizations where we found multiple email addresses or systematic leakage, we also tried contacting the IT/security department directly.

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62d09f3c3a9c5f8fc30a0a76_Twitter_notification_2.png)](https://positive.security)When there was no answer or proper report contact, we also tried reaching out via Twitter

Unfortunately, neither did we receive any answer on any of the data leak notification mails to affected individuals nor could we get any feedback from organizations that seem to have a systematic problem.

With one exception: After sending one person a DocuSign link to their work contract, their employer reached out to us, started an investigation and awarded a bug bounty. They found the source of the leak to be "a misconfiguration of [their] Security Orchestration, Automation and Response playbook for integration with urlscan.io, which was in active development".

### Contacting urlscan.io

Without much feedback from affected users, we also explained the situation to urlscan.io.

In case the integration developers are following urlscan.io's docs (at least with regard to the following section), it should be quite easy for the urlscan.io team to identify the source software of the scan requests:

> ‍**Integrations** : Use a custom HTTP user-agent string for your library/integration. Include a software version if applicable.

We therefore asked, whether it would be possible for them to generate a list of user agents that triggered the scans related to the people we contacted, as well as for the scans of our own bait links, and if they would share that list with us - which they did!

In general, the urlscan.io team was very responsive and offered to investigate and work together with us to improve the current situation.

Reviewing the list of user agents revealed that many API integrations do not follow the above recommendation with more than half of the scans having been started with a generic "python-requests/2.X.Y" user agent.

The two solutions that could be easily identified via the user agents were:

  * [PaloAlto's XSOAR](https://www.paloaltonetworks.com/cortex/cortex-xsoar)
  * [Swimlane](https://swimlane.com/)

Further investigations on the API keys used to start scans with "python-requests" user agents revealed that many of them were also generated for PaloAlto's XSOAR (or "Demisto", its former name). Others were generated for:

  * [IBM Resilient (now "IBM Security QRadar SOAR")](https://www.ibm.com/products/qradar-soar)
  * [Splunk Phantom (now "Splunk SOAR")](https://docs.splunk.com/Documentation/Phantom/4.10.7/User/Intro)
  * [DimensionData's SOAR](https://www.dimensiondata.com/en-gb/solutions/intelligent-security/)

#### **So how exactly did the data end up there?**

\-- MARKDOWN --

Security Orchestration, Automation and Response (SOAR) platforms allow organizations to write their own playbooks to connect different data sources with security tools and services. To ease development, the platforms offer integrations with several 3rd-party services, e.g. via [this XSOAR urlscan.io pack](https://cortex.marketplace.pan.dev/marketplace/details/UrlScan/). With this pack installed, a playbook could extract URLs from incoming emails and submit them to urlscan with the command `!url url=https://example.com using="urlscan.io"` with optional parameters for e.g. the timeout and scan visibility.

The visibility of such a scan is then dependent on  
1\. the parameters submitted as part of the command,  
2\. the integration-wide configuration, and  
3\. the visibility settings of the associated urlscan.io account/team.

Therefore, a scan can be be wrongfully submitted as public  
1\. in case of a programming mistake in a playbook or a misconfiguration of the urlscan.io integration or account visibility settings, as has happened to the company that leaked their employee's work contract, or  
2\. in case the integration itself has a bug that does not respect the user-chosen visibility, as [has happened to the PaloAlto XSOAR urlscan.io pack](https://github.com/demisto/content/pull/18816) (fixed on May 1st of this year):

\-- /MARKDOWN --

> The argument [ ...] had been configured to have a default value of _public_ , and this argument overrides all other settings related to visibility. [...] Consequently, for all command invocations that did not explicitly provide a value for this newly introduced argument, all scans have since been executed with visibility public.

#### **Response**

As a result of our findings, urlscan.io reached out to customers who they identified as submitting a significant amount of public scans and started reviewing popular third-party integrations such as for SOAR tools to ensure they respect the user intent with regards to visibility.

Furthermore, they implemented the following changes:

  * Added deletion rules for dorks presented here to periodically delete scan results matching the search patterns
  * Highlighted the default visibility setting in the UI
  * Added an option to set a team-wide maximum visibility

urlscan.io also published [a blog post titled "Scan Visibility Best Practices"](https://urlscan.io/blog/2022/07/27/scan-visibility-best-practices/) that explains scan visibility settings, encourages users to frequently review their submissions and details urlscan's efforts to prevent such leaks.

In case sensitive data is still leaked, they offer the following options:

  * **Affected users** can report scan results with sensitive data via the "Report" button which immediately deactivates them
  * **Companies** that wish to have their domains or specific URL patterns excluded from scanning (or corresponding existing results deleted) can contact urlscan.io. This is also how the Apple results had disappeared
  * **Security researchers** that found systematic leakage are also asked to reach out to urlscan.io

# Multi-step account takeover

While passively searching through historical urlscan.io data already uncovers a trove of sensitive information, combining it with "active probing" can greatly increase the impact of any small leak.

As we have seen earlier, for around 50% of the users that have an unsubscribe link leaked in urlscan.io, any link in any incoming email will be immediately submitted to urlscan as a public scan.

We can find those misconfigured clients by scraping urlscan.io for email addresses (e.g. in unsubscribe pages or even just in the URL itself), sending them a "bait link" via mail and subsequently checking urlscan.io for the link.

By actively triggering password resets for the affected email addresses at various web services such as social media sites, other email providers or banks, and then checking for recent scan results for the corresponding domains in the urlscan database, we can exploit this behavior to take over those user's accounts. Searching additional data leaks e.g. using [HaveIBeenPwned](https://haveibeenpwned.com) for those email addresses might also provide hints which services the users are registered at.

For company email addresses, custom login portals and popular enterprise SaaS can be particularly interesting to find existing accounts at and trigger password resets for.

And even if no account exists yet at a specific service, just creating a new one with a corporate email address might [provide access to the company's internal data stored on that service](https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c).

The following graphic illustrates all the necessary steps to perform the account takeover attack:

[![](https://cdn.prod.website-files.com/5f6498c074436c349716e747/62c75134e3b100af89706a78_multi-step-account-takeover.png)](https://positive.security/#zoom)Combining a passive search with active probing for misconfigured clients and triggering of password resets can greatly increase the impact of any single urlscan.io leak

# Recommendations

**As owner of a web service** , you can make sure that you’re expiring password reset and similar links quickly and are not leaking unnecessary information to unauthenticated users via links that could become public. On an unsubscribe page, redact the user’s email address, and ask for additional authentication/information before showing PII (like many package tracking websites nowadays ask for a ZIP code before showing the full address). When implementing API authentication, do not accept API keys via GET parameters and instead require the usage of a separate HTTP header.

Furthermore, you can also search [urlscan.io](http://urlscan.io) as well as other services yourself for any data leaks regarding your own web service or organization, request deletions/exclusions and e.g. disable and rotate any leaked API keys of your users.

**urlscan.io users/security teams that integrate the service** should review their command, integration and account visibility settings, keep their integrations up to date, regularly review [their submitted scans](https://urlscan.io/search/#user%3Ame%20OR%20team%3Ame) and check the urlscan.io [blog post](https://urlscan.io/blog/2022/07/27/scan-visibility-best-practices/) for more information.

# Conclusion

We have shown that the service [urlscan.io](http://urlscan.io), which usually helps protect users, also stores sensitive information of those users, some of which is publicly available and can be searched through by attackers.

This information could be used by spammers to collect email addresses and other personal information. It could be used by cyber criminals to take over accounts and run believable phishing campaigns. And it could also be used by red teamers and security researchers to find hidden admin portals, gain a first foothold or find potential targets.

Similar to Google Dorking or the [search through public S3 buckets](https://buckets.grayhatwarfare.com/), “urlscan.io mining” reveals a lot of information that was not meant to be public. The difference is, that the information that can be found via Google or that is in a public S3 buckets actually is already public, while the URLs submitted to urlscan.io for public scanning might contain authentication tokens and originate from a private email to an individual, submitted by a security solution. It’s a case where the introduction of additional security tooling can actually degrade a system's security.

The docs do warn of personally identifiable information in the submitted URLs, but only suggest to mark those scans as _Unlisted_ (instead of _Private_):

> **TAKE CARE** to remove PII from URLs or submit these scans as _Unlisted_ , e.g. when there is an email address in the URL.

Those unlisted scans are at least still “visible to vetted security researchers and security companies in [the] urlscan Pro platform”. Furthermore, this warning does not address the risk of PII in the returned page instead of in the URL itself.

The [pricing and API quotas](https://urlscan.io/pricing/) also heavily favor the use of public scans and the service does not (effectively) proactively prevent the leakage of PII (e.g. a simple search for [page.url:@gmail.com](https://urlscan.io/search/#page.url%3A%40gmail.com) returns the maximum number of 10000 results).

However, the urlscan.io team has been very responsive to our report, supported the investigation, published a blog post to educate their users and implemented software and process changes to reduce the number of leaks.

# Timeline

\-- MARKDOWN --  
`2022-02-15`: Github notified affected users of the private repository name leak via email  
`2022-02-16`: Initial exploration of the urlscan.io service  
`2022-07-05`-`2022-07-15`: Continued analysis, scraped email addresses, sent notification mails  
`2022-07-15`: Reported findings to urlscan.io and shared blog post draft  
`2022-07-15`-`2022-07-20`: Discussed and investigated findings together with urlscan.io  
`2022-07-19`: urlscan.io released new version with improved scan visibility UI and team-wide maximum visibility setting  
`2022-07-27`: urlscan.io published blog post on [Scan Visibility Best Practices](https://urlscan.io/blog/2022/07/27/scan-visibility-best-practices/)  
`2022-11-02`: We are publishing this blog post

\-- /MARKDOWN --

‍

##### Follow us on Mastodon ([@positive_sec](https://infosec.exchange/@positive_sec)) to keep up to date with our posts.

‍

[![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f7ddb13deeceb266b162f8d_favicon-32x32_white.png)© 2025 Positive Security](/)[Legal disclosure](/contact#legal)

![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c6cbd16e799_top.png)![](https://cdn.prod.website-files.com/5f6498c074436c50c016e745/5f6498c074436c36af16e7a5_bottom.png)

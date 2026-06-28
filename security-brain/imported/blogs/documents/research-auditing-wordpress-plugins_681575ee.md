---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-20_research-auditing-wordpress-plugins.md
original_filename: 2022-05-20_research-auditing-wordpress-plugins.md
title: 'Research: Auditing WordPress Plugins'
category: documents
detected_topics:
- command-injection
- path-traversal
- automation-abuse
- sso
- xss
- sqli
tags:
- imported
- documents
- command-injection
- path-traversal
- automation-abuse
- sso
- xss
- sqli
language: en
raw_sha256: 681575ee0e8c0af1edc6aee5493fc7cb6206180395f9e8d425406e3c8cc677c5
text_sha256: 71ae59622a0dac95410595e1e239f822cbf99cb7e51689f6661ee009cfaed4ba
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Research: Auditing WordPress Plugins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-20_research-auditing-wordpress-plugins.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, automation-abuse, sso, xss, sqli
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `681575ee0e8c0af1edc6aee5493fc7cb6206180395f9e8d425406e3c8cc677c5`
- Text SHA256: `71ae59622a0dac95410595e1e239f822cbf99cb7e51689f6661ee009cfaed4ba`


## Content

---
title: "Research: Auditing WordPress Plugins"
page_title: "Auditing WordPress Plugins | cyllective's blog"
url: "https://cyllective.com/blog/posts/wordpress-audit-plugins"
final_url: "https://cyllective.com/blog/posts/wordpress-audit-plugins"
authors: ["cyllective (@cyllective)"]
bugs: ["SQL injection", "LFI", "XSS", "RCE"]
publication_date: "2022-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2626
---

# Auditing WordPress Plugins

20\. May 2022, [#web](https://cyllective.com/blog/tags/web) [#cms](https://cyllective.com/blog/tags/cms) [#cve](https://cyllective.com/blog/tags/cve) [#plugins](https://cyllective.com/blog/tags/plugins) [#wordpress](https://cyllective.com/blog/tags/wordpress)

> We at cyllective always strive to improve and expand our knowledge in our field of expertise. It was during a recent audit where we (once more) came into contact with WordPress. Even after the audit had passed, it did peak the interest of one of our security engineers ([@_cydave](https://twitter.com/_cydave)). As part of our work also involves giving back to the community, we decided to dedicate a fair amount of time into the research on WordPress plugins and we are pleased to present an insight into our research.

By now you’ve most likely heard about the pleasure of building a small website or cool blog, but it should be quickly and without hassle, oodles and oodles of beautiful designs, powerful features and the freedom to “build anything you want” - to most people, WordPress comes to mind.

But not everybody has heard about the associated security nightmares that the vast plugin and theme ecosystem entails. As the individual plugin maintainers usage of secure code practices highly varies.

Wether you’ve experienced the horrors of copy-pasta’d vulnerable components before (yes, we are looking at you [TimThumb ↗](https://www.exploit-db.com/exploits/17602) ;), [uploader ↗](https://www.exploit-db.com/exploits/38163) ;)) or had to explain to that one friend of yours, not to play Pokémon trainer with plugins and themes on the WordPress marketplace - we all have been touched by the grace of [WordPress ↗](https://wordpress.org/) in some shape or form.

![WordPress Plugin Market Place](/blog/posts/wordpress-audit-plugins/wordpress_marketplace.webp.pagespeed.ce.UyuJrpCdCt.webp)WordPress Plugin Market Place

This blog post summarizes our explorational WordPress plugin security research, which we’ve been working on for around three months. Our initial goals for this research were not set in stone, beyond getting in some practice for improving our secure code review / auditing routine and to learn more about WordPress plugins in the process.

## The First Step #

The first few hours of our research were spent reading through WordPress’s [Plugin Handbook ↗](https://developer.wordpress.org/plugins/) in order to get a basic understanding of their structure (hook all the things - [Actions ↗](https://developer.wordpress.org/plugins/hooks/actions/) and [Filters ↗](https://developer.wordpress.org/plugins/hooks/filters/)) and available security measures (`sanitize_*` and `esc_*` functions, nonce creation and validation, etc.).

Aside from the “official” resources, we dug around [exploit-db ↗](https://www.exploit-db.com) for additional insight into attacking / auditing WordPress plugins. The following papers provided us with valuable pointers:

  * [WordPress Plugin Analysis ↗](https://www.exploit-db.com/exploits/49776)
  * [Exploit WordPress Plugin vulnerability using static source code analysis techniques ↗](https://www.exploit-db.com/exploits/49289)
  * [How To: Find WordPress Plugin Vulns ↗](https://www.exploit-db.com/docs/49968)

Equipped with an ever growing scratchpad of notes, references and rabbit holes to chase, we decided to start digging.

## Plugins, Plugins everywhere #

The oodles and oodles of plugins, merely a few clicks away to get lost in reading, tracing function calls and keeping a keen eye out for sources and sinks - a sheer bottomless ball pit of good fun - we just couldn’t decide on where to start…

We had been scraping and indexing plugin metadata as well as the plugin’s files, version numbers, relative filepaths and checksums for quite a while. The data harvesting process was painfully slow, due to the transfer speeds of WordPress’ SVN server, but provided us with valuable information that we were then able to incorperated in our research in the form of our own database.

Initially, we started picking a fixed set of randomly selected plugins from our database, without any regards to the release date, popularity of the plugin or it’s use case. We also limited ourselves to a maximum of thirty minutes per plugin to audit, so we could expose ourselves to varying levels of code quality, structure and security awareness of the plugin developers.

After around one week of downloading, installing, auditing, uninstalling of random plugins, we uncovered an unauthenticated SQL injection vulnerability. We’ve also uncovered a series of local file inclusion and remote code execution vulnerabilities in severely outdated plugins, which just happened to be part of our random pool. The fact that we invested quite a bit of time in auditing plugins that had not received updates in the past 5 years didn’t sit well with us. We wouldn’t benefit all too much if we would continue on with our current plugin selection criteria. By auditing severly outdated plugins the WordPress ecosystem woulnd’t benefit that much either, as they weren’t relevant and supported anymore anyways.

Fortunately, we’ve been scraping plugin metadata for quite a while and could utilize the release- and last updated date fields to filter out severly outdated plugins. Out of curiosity, we plotted the number of plugins by the date they were last updated on and grouped them by year:

![Plugins last updated date grouped by year](/blog/posts/wordpress-audit-plugins/fig_last_updated_by_year.webp.pagespeed.ce.xrSnt5pGcC.webp)Plugins last updated date grouped by year

We decided to exclude plugins that did not receive updates in the last two years, so we wouldn’t be investing time in auditing “dead” software. This brought the capacity of our random pool down to roughly 20'000 plugins.

We continued auditing plugins left and right for a few more days and ended up finding two additional unauthenticated SQL injection vulnerabilities in two separate plugins. After having audited roughly **_one thousand_** plugins at this point, we developed a slight obsession (or hyper focus) on SQL injection vulnerabilities. Because SQL injection vulnerabilities are rather easy to spot, we began experimenting with a bunch of RegEx patterns, which would help us in discovering SQL injections more rapidly. But as expected, searching for vulnerabilities purely based on RegEx patterns, turned out to be suboptimal. Especially the time loss, caused by the high rate of false positives (and false negatives), motivated us to come up with a better approach.

## Optimizing Our Process #

Recalling that most plugins on the marketplace have a set of **tags** associated with them, inspired us to experiment with a similar approach, with the goal of finding more “relevant” plugins. Instead of using tags, which describe the plugin’s use cases, we chose to search the plugin’s source code for WordPress specific library calls and then enrich our database with this information in the form of tags.

Because we were mostly interested in finding SQL injection vulnerabilities (ideally, unauthenticated ones), we would look out for a combination of specific behavior:

  * Interaction with the WordPress database: references to `$wpdb->`
  * String interpolation in SQL-like strings:
  * `['"].+?\s(WHERE|where)\s*\w+\s*=\s*\$\w+.+?['"]`
  * `["'](SELECT|select|DELETE|delete)\s+.*?(FROM|from)\s+.+?(WHERE|where).+?(\$\w+).+(['"]|;)`
  * …
  * Optional: Security measures relating to sanitization attempts: `esc_sql`
  * Exposure of unauthenticated endpoints: references to `add_action("wp_ajax_nopriv_`

With our new approach in mind, some more RegEx patterns and yet another Python script at the ready, we re-lived the radical internet speeds of the 90s, by downloading all of the WordPress plugins via their SVN mirror once again. For each downloaded plugin we recursively grepped for specific patterns in the source code and once a match was found, we would attach a tag, describing the pattern that was used, to the plugin.

After days of downloading and grepping we ended up with **tagged** plugins:

![Excerpt of tagged plugins](/blog/posts/wordpress-audit-plugins/tagged_plugins.webp.pagespeed.ce.rE7kFp5UDa.webp)Excerpt of tagged plugins

Using the tags (stored in the “notes” column in the screenshot above) as an additional filter, we were able to reduce the pool of targets to audit down to roughly 5'000 plugins.

In the first few days of analysing a subset of the new targets, we encountered 2 more SQL injection vulnerabilities and as the audit-spree continued, we would occasionally find up to 4 or 5 vulnerabilities a day. To us, the fact that we were finding vulnerabilities more frequently, compared to our initial approach, felt like a clear indicator that we were on the right track. 😸

On each day that we discovered one or more vulnerabilities, we would responsibly disclose them with the help of the fine folks at WPScan (WPScan being [a CNA of WordPress CVE numbers ↗](https://wptavern.com/wpscan-can-now-assign-cve-numbers-for-wordpress-core-plugin-and-theme-vulnerabilities)). Instead of keeping track of all the back-and-forth communication across two or more parties (the plugin developers, the WordPress plugin team and a selected CNA) all while correctly timing, escalating and taking further steps by yourself, one can simply use [their vulnerability submission form ↗](https://wpscan.com/submit) and let the WPScan team take care of all the necessary steps for you.

_Thank you, WPScan and team, for providing us with such a smooth process!_ ❤️

## Findings & Conclusion #

Having exhausted the pool of 5'000 plugins after around two months, we decided to conclude our explorational research.

CVE| Plugin  
---|---  
[CVE-2022-0656 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0656)| [udraw ↗](https://wordpress.org/plugins/udraw)  
[CVE-2022-0657 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0657)| [5-stars-rating-funnel ↗](https://wordpress.org/plugins/5-stars-rating-funnel)  
[CVE-2022-0658 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0658)| [commonsbooking ↗](https://wordpress.org/plugins/commonsbooking)  
[CVE-2022-0679 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0679)| [narnoo-distributor ↗](https://wordpress.org/plugins/narnoo-distributor)  
[CVE-2022-0693 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0693)| [master-elements ↗](https://wordpress.org/plugins/master-elements)  
[CVE-2022-0694 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0694)| [advanced-booking-calendar ↗](https://wordpress.org/plugins/advanced-booking-calendar)  
[CVE-2022-0739 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0739)| [bookingpress-appointment-booking ↗](https://wordpress.org/plugins/bookingpress-appointment-booking)  
[CVE-2022-0747 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0747)| [infographic-and-list-builder-ilist ↗](https://wordpress.org/plugins/infographic-and-list-builder-ilist)  
[CVE-2022-0760 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0760)| [simple-link-directory ↗](https://wordpress.org/plugins/simple-link-directory)  
[CVE-2022-0769 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0769)| [users-ultra ↗](https://wordpress.org/plugins/users-ultra)  
[CVE-2022-0771 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0771)| [sitesupercharger ↗](https://wordpress.org/plugins/sitesupercharger)  
[CVE-2022-0773 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0773)| [documentor-lite ↗](https://wordpress.org/plugins/documentor-lite)  
[CVE-2022-0780 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0780)| [searchiq ↗](https://wordpress.org/plugins/searchiq)  
[CVE-2022-0781 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0781)| [nirweb-support ↗](https://wordpress.org/plugins/nirweb-support)  
[CVE-2022-0782 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0782)| [nd-donations ↗](https://wordpress.org/plugins/nd-donations)  
[CVE-2022-0783 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0783)| [multiple-shipping-address-woocommerce ↗](https://wordpress.org/plugins/multiple-shipping-address-woocommerce)  
[CVE-2022-0784 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0784)| [wp-experiments-free ↗](https://wordpress.org/plugins/wp-experiments-free)  
[CVE-2022-0785 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0785)| [daily-prayer-time-for-mosques ↗](https://wordpress.org/plugins/daily-prayer-time-for-mosques)  
[CVE-2022-0786 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0786)| [kivicare-clinic-management-system ↗](https://wordpress.org/plugins/kivicare-clinic-management-system)  
[CVE-2022-0787 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0787)| [wp-limit-failed-login-attempts ↗](https://wordpress.org/plugins/wp-limit-failed-login-attempts)  
[CVE-2022-0788 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0788)| [wp-fundraising-donation ↗](https://wordpress.org/plugins/wp-fundraising-donation)  
[CVE-2022-0814 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0814)| [ubigeo-peru ↗](https://wordpress.org/plugins/ubigeo-peru)  
[CVE-2022-0817 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0817)| [badgeos ↗](https://wordpress.org/plugins/badgeos)  
[CVE-2022-0818 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0818)| [woo-coupon-usage ↗](https://wordpress.org/plugins/woo-coupon-usage)  
[CVE-2022-0826 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0826)| [wp-video-gallery-free ↗](https://wordpress.org/plugins/wp-video-gallery-free)  
[CVE-2022-0827 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0827)| [bestbooks ↗](https://wordpress.org/plugins/bestbooks)  
[CVE-2022-0833 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0833)| [church-admin ↗](https://wordpress.org/plugins/church-admin)  
[CVE-2022-0836 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0836)| [sema-api ↗](https://wordpress.org/plugins/sema-api)  
[CVE-2022-0846 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0846)| [speakout ↗](https://wordpress.org/plugins/speakout)  
[CVE-2022-0867 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0867)| [arprice-responsive-pricing-table ↗](https://wordpress.org/plugins/arprice-responsive-pricing-table)  
[CVE-2022-0948 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0948)| [woc-order-alert ↗](https://wordpress.org/plugins/woc-order-alert)  
[CVE-2022-0949 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0949)| [stopbadbots ↗](https://wordpress.org/plugins/stopbadbots)  
[CVE-2022-0952 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0952)| [sitemap-by-click5 ↗](https://wordpress.org/plugins/sitemap-by-click5)  
[CVE-2022-1013 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1013)| [personal-dictionary ↗](https://wordpress.org/plugins/personal-dictionary)  
[CVE-2022-1014 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1014)| [wp-contacts-manager ↗](https://wordpress.org/plugins/wp-contacts-manager)  
[CVE-2022-1724 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1724)| [simple-membership ↗](https://wordpress.org/plugins/simple-membership)  
[CVE-2022-1903 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1903)| [armember-membership ↗](https://wordpress.org/plugins/armember-membership)  
[CVE-2022-1904 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1904)| [easy-pricing-tables ↗](https://wordpress.org/plugins/easy-pricing-tables)  
[CVE-2022-1905 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1905)| [events-made-easy ↗](https://wordpress.org/plugins/events-made-easy)  
[CVE-2022-1906 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1906)| [digiproveblog ↗](https://wordpress.org/plugins/digiproveblog)  
[CVE-2022-1910 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1910)| [auxin-elements ↗](https://wordpress.org/plugins/auxin-elements)  
[CVE-2022-1916 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1916)| [profit-products-tables-for-woocommerce ↗](https://wordpress.org/plugins/profit-products-tables-for-woocommerce)  
[CVE-2022-1932 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1932)| [rezgo ↗](https://wordpress.org/plugins/rezgo)  
[CVE-2022-1933 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1933)| [collect-and-deliver-interface-for-woocommerce ↗](https://wordpress.org/plugins/collect-and-deliver-interface-for-woocommerce)  
[CVE-2022-1937 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1937)| [awin-data-feed ↗](https://wordpress.org/plugins/awin-data-feed)  
[CVE-2022-1938 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1938)| [awin-data-feed ↗](https://wordpress.org/plugins/awin-data-feed)  
[CVE-2022-1946 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1946)| [gallery-album ↗](https://wordpress.org/plugins/gallery-album)  
[CVE-2022-1950 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1950)| [youzify ↗](https://wordpress.org/plugins/youzify)  
[CVE-2022-1951 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1951)| [kitestudio-core ↗](https://wordpress.org/plugins/kitestudio-core)  
[CVE-2022-1952 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1952)| [easync-booking ↗](https://wordpress.org/plugins/easync-booking)  
[CVE-2022-1953 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1953)| [product-configurator-for-woocommerce ↗](https://wordpress.org/plugins/product-configurator-for-woocommerce)  
[CVE-2022-2958 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2958)| [badgeos ↗](https://wordpress.org/plugins/badgeos)  
[CVE-2022-3254 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3254)| [another-wordpress-classifieds-plugin ↗](https://wordpress.org/plugins/another-wordpress-classifieds-plugin)  
[CVE-2022-3912 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3912)| [user-registration ↗](https://wordpress.org/plugins/user-registration)  
[CVE-2022-3915 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3915)| [dokan-lite ↗](https://wordpress.org/plugins/dokan-lite)  
[CVE-2022-3930 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3930)| [directorist ↗](https://wordpress.org/plugins/directorist)  
[CVE-2022-3933 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3933)| [essential-real-estate ↗](https://wordpress.org/plugins/essential-real-estate)  
[CVE-2022-3934 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3934)| [flatpm-wp ↗](https://wordpress.org/plugins/flatpm-wp)  
[CVE-2022-3982 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3982)| [booking-calendar ↗](https://wordpress.org/plugins/booking-calendar)  
[CVE-2022-3989 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3989)| [motors-car-dealership-classified-listings ↗](https://wordpress.org/plugins/motors-car-dealership-classified-listings)  
[CVE-2022-4024 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4024)| [pie-register ↗](https://wordpress.org/plugins/pie-register)  
[CVE-2022-4047 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4047)| [woo-refund-and-exchange-lite ↗](https://wordpress.org/plugins/woo-refund-and-exchange-lite)  
[CVE-2022-4049 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4049)| [wp-user ↗](https://wordpress.org/plugins/wp-user)  
[CVE-2022-4050 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4050)| [joomsport-sports-league-results-management ↗](https://wordpress.org/plugins/joomsport-sports-league-results-management)  
[CVE-2022-4059 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4059)| [cryptocurrency-widgets-pack ↗](https://wordpress.org/plugins/cryptocurrency-widgets-pack)  
[CVE-2022-4060 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4060)| [wp-upg ↗](https://wordpress.org/plugins/wp-upg)  
[CVE-2022-4061 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4061)| [jobboardwp ↗](https://wordpress.org/plugins/jobboardwp)  
[CVE-2022-4063 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4063)| [inpost-gallery ↗](https://wordpress.org/plugins/inpost-gallery)  
[CVE-2022-4099 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4099)| [joy-of-text ↗](https://wordpress.org/plugins/joy-of-text)  
[CVE-2022-4101 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4101)| [images-optimize-and-upload-cf7 ↗](https://wordpress.org/plugins/images-optimize-and-upload-cf7)  
[CVE-2022-4117 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4117)| [iws-geo-form-fields ↗](https://wordpress.org/plugins/iws-geo-form-fields)  
[CVE-2022-4118 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4118)| [woo-altcoin-payment-gateway ↗](https://wordpress.org/plugins/woo-altcoin-payment-gateway)  
[CVE-2022-4295 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4295)| [show-all-comments-in-one-page ↗](https://wordpress.org/plugins/show-all-comments-in-one-page)  
[CVE-2022-4297 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4297)| [wp-autosearch ↗](https://wordpress.org/plugins/wp-autosearch)  
[CVE-2022-4298 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4298)| [wholesale-market ↗](https://wordpress.org/plugins/wholesale-market)  
[CVE-2022-4301 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4301)| [sunshine-photo-cart ↗](https://wordpress.org/plugins/sunshine-photo-cart)  
[CVE-2022-4305 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4305)| [login-as-customer-or-user ↗](https://wordpress.org/plugins/login-as-customer-or-user)  
[CVE-2022-4306 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4306)| [panda-pods-repeater-field ↗](https://wordpress.org/plugins/panda-pods-repeater-field)  
[CVE-2022-4307 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4307)| [pardakht-delkhah ↗](https://wordpress.org/plugins/pardakht-delkhah)  
[CVE-2022-4320 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4320)| [connect-daily-web-calendar ↗](https://wordpress.org/plugins/connect-daily-web-calendar)  
[CVE-2022-4321 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4321)| [pdf-generator-for-wp ↗](https://wordpress.org/plugins/pdf-generator-for-wp)  
[CVE-2022-4325 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4325)| [post-status-notifier-lite ↗](https://wordpress.org/plugins/post-status-notifier-lite)  
[CVE-2022-4328 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4328)| [n-media-woocommerce-checkout-fields ↗](https://wordpress.org/plugins/n-media-woocommerce-checkout-fields)  
[CVE-2022-4329 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4329)| [gm-woo-product-list-widget ↗](https://wordpress.org/plugins/gm-woo-product-list-widget)  
[CVE-2022-4369 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4369)| [wp-lister-for-amazon ↗](https://wordpress.org/plugins/wp-lister-for-amazon)  
[CVE-2022-4374 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4374)| [bg-biblie-references ↗](https://wordpress.org/plugins/bg-biblie-references)  
[CVE-2022-4383 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4383)| [cbxpetition ↗](https://wordpress.org/plugins/cbxpetition)  
[CVE-2022-4395 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4395)| [membership-for-woocommerce ↗](https://wordpress.org/plugins/membership-for-woocommerce)  
[CVE-2022-4445 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4445)| [fl3r-feelbox ↗](https://wordpress.org/plugins/fl3r-feelbox)  
[CVE-2022-4447 ↗](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4447)| [fontsy ↗](https://wordpress.org/plugins/fontsy)  
  
**Further reading**

  * [A technique to semi-automatically discover new vulnerabilities in WordPress plugins ↗](https://kazet.cc/2022/02/03/fuzzing-wordpress-plugins.html) \- by Krzysztof Zając
  * [Thousands of WordPress Sites Hacked to Redirect Visitors to Scam Sites ↗](https://thehackernews.com/2022/05/thousands-of-wordpress-sites-hacked-to.html)

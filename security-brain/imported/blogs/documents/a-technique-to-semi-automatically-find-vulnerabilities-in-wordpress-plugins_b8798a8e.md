---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-03_a-technique-to-semi-automatically-find-vulnerabilities-in-wordpress-plugins.md
original_filename: 2022-02-03_a-technique-to-semi-automatically-find-vulnerabilities-in-wordpress-plugins.md
title: A technique to semi-automatically find vulnerabilities in WordPress plugins
category: documents
detected_topics:
- xss
- access-control
- rate-limit
- automation-abuse
- supply-chain
- sso
tags:
- imported
- documents
- xss
- access-control
- rate-limit
- automation-abuse
- supply-chain
- sso
language: en
raw_sha256: b8798a8e9072820e54f5cca3f194a98288d12616b463ec317f34b648144585fb
text_sha256: 9fb9643252227a7efd62c4d4d78d13446694db561fd16ac25b130d91271ec286
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# A technique to semi-automatically find vulnerabilities in WordPress plugins

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-03_a-technique-to-semi-automatically-find-vulnerabilities-in-wordpress-plugins.md
- Source Type: markdown
- Detected Topics: xss, access-control, rate-limit, automation-abuse, supply-chain, sso
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b8798a8e9072820e54f5cca3f194a98288d12616b463ec317f34b648144585fb`
- Text SHA256: `9fb9643252227a7efd62c4d4d78d13446694db561fd16ac25b130d91271ec286`


## Content

---
title: "A technique to semi-automatically find vulnerabilities in WordPress plugins"
page_title: "A technique to semi-automatically discover new vulnerabilities in WordPress plugins"
url: "https://kazet.cc/2022/02/03/fuzzing-wordpress-plugins.html"
final_url: "https://kazet.cc/2022/02/03/fuzzing-wordpress-plugins.html"
authors: ["kazet (@kazet1234)"]
bugs: ["XSS", "SQL injection", "Open redirect", "CSRF"]
publication_date: "2022-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2944
---

# A technique to semi-automatically discover new vulnerabilities in WordPress plugins

Feb 3, 2022 • Krzysztof Zając

![](/assets/2022-02-03-pies.jpg)

**Update (2022-02-26): the tool is now public:<https://github.com/kazet/wpgarlic>**

WordPress plugins expose a number of interfaces, such as:

  * AJAX endpoints (`/wp-admin/admin-ajax.php`)
  * Admin menu pages (`/wp-admin/admin.php?page=...`)
  * PHP files (in the `/wp-content/plugins/` directory),
  * Shortcodes
  * REST routes (`/wp-json/...`).

These interfaces have a consistent trust boundary: we know where the untrusted input goes and can detect what operations are executed on that input.

For instance, if you visit a `.php` file, provide appropriate parameters, and cause a file to be removed, you know that it is a vulnerability. You know what parameters you control and what ones you don’t – for example, you may redirect a logged-in admin to an admin menu page with arbitrary GET parameters, but you don’t control their cookies.

Therefore it is possible to semi-automatically scan for multiple classes of vulnerabilities in all WordPress plugins.

I have written a tool that:

  * executes each AJAX endpoint, menu page, REST route, or file multiple times,
  * injects payloads into the GET, POST, etc. arrays or REST parameters (more on how it’s done in the next section),
  * analyses the outputs with an ugly pile of regular expressions1 to detect: 
  * calls to WordPress functions (such as `wp_delete_post`),
  * crashes (“No such file or directory”, “You have an error in your SQL syntax”, …),
  * XSS (echoing a known payload containing " or <),
  * etc.

This method is transferable to other CMS plugin ecosystems but not directly e.g. to Python packages. If a Python package allows you to remove arbitrary files, it may or may not be a vulnerability depending on the package role and your particular setup.

## Injecting parameters

In PHP, the `_GET`, `_POST`, `_SERVER`, `_COOKIE`, and `_REQUEST` arrays contain various request parameters (e.g. GET and POST data, cookies, server configuration, and headers). I have replaced them with mock objects that allow access to any key - and with defined probability return a payload from a predefined payload list.

A simple mock `$_POST` array could be created using the following code:
  
  
  <?php
  
  class Mock implements ArrayAccess {
  function offsetGet($offset) {
  return "payload";
  }
  
  function offsetExists($offset) {
  return true;
  }
  
  function offsetSet($offset, $value) { }
  
  function offsetUnset($offset) { }
  }
  
  $_POST = new Mock();
  
  echo $_POST["parameter_name"];
  

The above snippet will print `payload`.

Let’s assume that the `$_REQUEST` array has been mocked in a way similar to the one described above and that an AJAX route is handled by the following function:
  
  
  public function delete_saved_block() {
  $block_id = (int) sanitize_text_field($_REQUEST['block_id']);
  $deleted_block = wp_delete_post($block_id);
  wp_send_json_success($deleted_block);
  }
  

When `$_REQUEST['block_id']` gets accessed, the mock will return a payload, thus allowing to detect that `wp_delete_post` was called on an attacker-controlled value.

**This approach allowed to easily inject payloads even if the parameter name was hard to guess – the tool didn’t distinguish between`id` and `secret_parameter_65e3c14a1d`.**

Some of the keys needed to be excluded manually (for example `$_SERVER['HTTP_AUTHORIZATION']` or `$_GET['doing_wp_cron']`) because their values were handled by WordPress, and providing them caused plugin code to not be reached.

Besides, with some probability, **a random type of array** was returned instead of a string payload:

  * a singleton array with a string payload,
  * recursively, an object that allows access to any key,
  * a singleton array: random payload → random payload.

## Detecting vulnerabilities

The tool contained checks to detect:

  * various kinds of crashes,
  * potentially dangerous operations,
  * information leaks.

Some of these checks led to a large number of CVEs (such as the XSS checks), some didn’t (e.g. the checks for syntax errors designed to catch `eval()` on untrusted code).

### XSS

To detect XSS, checks were implemented that detected payloads being echoed back (or echoed back with escaping that didn’t prevent XSS, such as prefixing `"` with `\`).

### Crashes

The following types of crashes were detected:

  * `fopen()` / `file_get_contents()` / `require()` / `require_once()` / `include()` / `include_once()` errors and “No such file or directory” or “failed to open stream” error messages,
  * `unlink()` error messages,
  * crashes related to `call_user_func()`,
  * SQL error messages,
  * `unserialize()` errors,
  * parse / syntax errors to detect `eval()` calls,
  * “command not found” error message,
  * `simplexml_load_string()` error messages2.

### Information leaks

The output was analysed to observe whether known user e-mails or file names are displayed.

### WordPress operations

WordPress has been instrumented to detect:

  * calls to `maybe_unserialize`,
  * calls to `update_option`/`update_site_option`/`delete_option`,
  * calls to `wp_insert_user`,
  * calls to `wp_insert_post`/`wp_update_post`/`wp_delete_post`,
  * calls to `wp_mail`,
  * calls to `query` (this one yielded an especially large number of false positives that needed additional filtering),
  * calls to `get_users` (this one has been added after accidentally discovering [CVE-2021-25110](https://wpscan.com/vulnerability/b655fc21-47a1-4786-8911-d78ab823c153) where an attacker can leak arbitrary user e-mails via a crafted user search query).

### Additional checks

After fuzzing, the admin panel, the homepage, and the post pages were crawled to find occurrences of known payloads. That allowed for instance to detect [CVE-2021-24975](https://wpscan.com/vulnerability/b99dae3d-8230-4427-adc5-4ef9cbfb8ba1) in `social-networks-auto-poster-facebook-twitter-g`.

Update (2022-02-26): additionally, any attempts to access uploaded files are logged, so that they may be checked manually.

## Changes to PHP

### Patched equality

**I have patched PHP so that equality comparison between any value and a known payload returned`true` with 1/3 probability. Forgive me about this one.**

With this patch, I was able to detect vulnerabilities such as:
  
  
  if ($_GET['action'] == 'please-remove-post') {
  wp_delete_post($_GET['id']);
  }
  

Unfortunately, this resulted in a large number of false positives as well. The false positives were e.g. in the form of:
  
  
  if (in_array($order, array("ASC", "DESC"), true)) {
  query("(...) ORDER BY $order");
  }
  

The only solution for this problem I have used was browsing through these false positives and cursing. Further research can lead to coming up with other solutions.

### Other changes

Besides, I have patched the PHP interpreter so that:

  * When `base64_decode` was performed on a known payload, this payload was returned again,
  * When `json_decode` was performed on a known payload, an object was returned that returns payloads when any key was accessed. These were the same objects that served as e.g. `$_GET` arrays,
  * when a redirect was performed, relevant information was displayed so that Open Redirect vulnerabilities could be detected.

## Testing

A test-driven approach was critical during development. Tests checked that the tool would find a known vulnerability. For example, I could write a test to check that:

> when fuzzing the `wp_ajax_heateor_sss_import_config` endpoint of the [sassy-social-share](https://pl.wordpress.org/plugins/sassy-social-share/) plugin in version 3.3.23, the tool should detect that `maybe_unserialize()` gets called on an attacker-controlled payload.

## False positives vs false negatives

This approach yielded a large number of false positives. It was a deliberate decision because I wanted to sort through multiple reports instead of missing vulnerabilities.

An alternative could be to write additional filtering logic. For example, there were multiple reports where an HTML payload was echoed back – but when checking them, I’ve observed that a correct JSON `Content-Type` header is added. This was one of the cases that could be checked automatically.

## Other

Fuzzing was performed inside Docker containers, re-created for every plugin.

It was important to disconnect the network, because a lot of plugins call other web services, and I wanted to avoid sending random payloads there.

I found it also helpful to separate plugin fuzzing and analysis of the outputs. Because the outputs were analyzed by a lot of regular expressions, bugs happened. Therefore a relatively quick rescan allowed to speed up development.

## Automating the fuzzing Added: 2022-02-16

Scanning thousands of plugins would not be possible without automating the job. Fortunately, WordPress plugins use consistent interfaces to integrate with WordPress, for example:

  * all REST routes are collected in a central registry, accessible via: `rest_get_server()->get_routes()`,
  * AJAX actions are created by adding a hook with a name starting with `wp_ajax_`,
  * there exists one registry with all admin menu pages.

Therefore all REST routes, AJAX actions, and menu actions can be enumerated in the same way regardless of which plugin is scanned. Of course, all PHP files can be easily listed as well.

All plugins can be installed in the same way: I have used [WP-CLI](https://wp-cli.org/) – a tool that allows to install, activate, deactivate or delete a plugin from the command-line. The list of plugins could be downloaded automatically from the WordPress plugin registry API.

All of the above techniques made it possible to create a tool that doesn’t require any plugin-specific code.

## Results Last updated: 2024-08-25

Because of time constraints, I have focused only on the most popular plugins. As of this moment, the following bugs found by the tool have already been fixed and published:

ID | Plugin | CVE | Number of active installations | Type | Link  
---|---|---|---|---|---  
1 | [litespeed-cache](https://wordpress.org/plugins/litespeed-cache/) | CVE-2024-3246 | 5,000,000 | CSRF stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/8036bd83-9af5-4b71-8974-9b0690ea6769)  
2 | [woocommerce](https://wordpress.org/plugins/woocommerce/) | CVE-2022-0775 | 5,000,000 | Arbitrary comment deletion | [WPScan](https://wpscan.com/vulnerability/b76dbf37-a0a2-48cf-bd85-3ebbc2f394dd)  
3 | [all-in-one-seo](https://wordpress.org/plugins/all-in-one-seo/) | CVE-2024-3554 | 3,000,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/28741ffc-4ff5-4e67-a183-bb5064b6752e)  
4 | [updraftplus](https://wordpress.org/plugins/updraftplus/) | CVE-2021-25022 | 3,000,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/1801c7ae-2b5c-493f-969d-4bb19a9feb15)  
5 | [complianz-gdpr](https://wordpress.org/plugins/complianz-gdpr/) | CVE-2024-1592 | 800,000 | CSRF deletion of “do not sell my personal data” requests | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/complianz-gdpr/complianz-gdprccpa-cookie-consent-656-cross-site-request-forgery-to-data-request-deletion)  
6 | [the-events-calendar](https://wordpress.org/plugins/the-events-calendar/) | CVE-2023-6203 | 700,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/229273e6-e849-447f-a95a-0730969ecdae/)  
7 | [code-snippets](https://wordpress.org/plugins/code-snippets/) | CVE-2021-25008 | 500,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/cb232354-f74d-48bb-b437-7bdddd1df42a)  
8 | [woocommerce-pdf-invoices-packing-slips](https://wordpress.org/plugins/woocommerce-pdf-invoices-packing-slips/) | CVE-2021-24991 | 300,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/88e706df-ae03-4665-94a3-db226e1f31a9)  
9 | [woocommerce-pdf-invoices-packing-slips](https://wordpress.org/plugins/woocommerce-pdf-invoices-packing-slips/) | CVE-2022-2537 | 300,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/ae613148-85d8-47a0-952d-49c29584676f)  
10 | [ad-inserter](https://wordpress.org/plugins/ad-inserter/) | CVE-2022-0288 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/27b64412-33a4-462c-bc45-f81697e4fe42)  
11 | [caldera-forms](https://wordpress.org/plugins/caldera-forms/) | CVE-2022-0879 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/c12f6087-1875-4edf-ac32-bec6f712968d)  
12 | [complianz-gdpr](https://wordpress.org/plugins/complianz-gdpr/) | CVE-2022-0193 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/30d1d328-9f19-4c4c-b90a-04937d617864)  
13 | [custom-facebook-feed](https://wordpress.org/plugins/custom-facebook-feed/) | CVE-2021-25065 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/ae1aab4e-b00a-458b-a176-85761655bdcc)  
14 | [favicon-by-realfavicongenerator](https://wordpress.org/plugins/favicon-by-realfavicongenerator/) | CVE-2022-0471 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/499bfee4-b481-4276-b6ad-0eead6680f66)  
15 | [gotmls](https://wordpress.org/plugins/gotmls/) | CVE-2022-2599 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/276a7fc5-3d0d-446d-92cf-20060aecd0ef)  
16 | [loginpress](https://wordpress.org/plugins/loginpress/) | CVE-2022-0347 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/a5084367-842b-496a-a23c-24dbebac1e8b)  
17 | [popup-builder](https://wordpress.org/plugins/popup-builder/) | CVE-2022-0479 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/0d2bbbaf-fbfd-4921-ba4e-684e2e77e816)  
18 | [royal-elementor-addons](https://wordpress.org/plugins/royal-elementor-addons/) | CVE-2023-5922 | 200,000 | Arbitrary post read (including drafts and password-protected posts) | [WPScan](https://wpscan.com/vulnerability/debd8498-5770-4270-9ee1-1503e675ef34/)  
19 | [templately](https://wordpress.org/plugins/templately/) | CVE-2023-5454 | 200,000 | Arbitrary post trashing | [WPScan](https://wpscan.com/vulnerability/1854f77f-e12a-4370-9c44-73d16d493685/)  
20 | [use-any-font](https://wordpress.org/plugins/use-any-font/) | CVE-2021-24977 | 200,000 | Arbitrary CSS append + stored XSS | [WPScan](https://wpscan.com/vulnerability/739831e3-cdfb-4a22-9abf-6c594d7e3d75)  
21 | [white-label-cms](https://wordpress.org/plugins/white-label-cms/) | CVE-2022-0422 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/429be4eb-8a6b-4531-9465-9ef0d35c12cc)  
22 | [white-label-cms](https://wordpress.org/plugins/white-label-cms/) | CVE-2024-4280 | 200,000 | Unauthorized plugin settings reset | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/13a206ea-0890-4535-9da7-54a7a45f0452)  
23 | [wp-cerber](https://wordpress.org/plugins/wp-cerber/) | CVE-2022-0429 | 200,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/d1b6f438-f737-4b18-89cf-161238a7421b)  
24 | [wp-gdpr-compliance](https://wordpress.org/plugins/wp-gdpr-compliance/) | CVE-2022-0147 | 200,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/2c735365-69c0-4652-b48e-c4a192dfe0d1)  
25 | [bdthemes-element-pack-lite](https://wordpress.org/plugins/bdthemes-element-pack-lite/) | CVE-2024-2966 | 100,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/bdthemes-element-pack-lite/element-pack-elementor-addons-header-footer-template-library-dynamic-grid-carousel-remote-arrows-556-sensitive-information-exposure-via-element-pack-ajax-search)  
26 | [capability-manager-enhanced](https://wordpress.org/plugins/capability-manager-enhanced/) | CVE-2021-25032 | 100,000 | Arbitrary settings update | [WPScan](https://wpscan.com/vulnerability/2f0f1a32-0c7a-48e6-8617-e0b2dcf62727)  
27 | [chaty](https://wordpress.org/plugins/chaty/) | CVE-2021-25016 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/b5035987-6227-4fc6-bc45-1e8016e5c4c0)  
28 | [cmp-coming-soon-maintenance](https://wordpress.org/plugins/cmp-coming-soon-maintenance/) | CVE-2022-0188 | 100,000 | Possibility to add arbitrary CSS | [WPScan](https://wpscan.com/vulnerability/50b6f770-6f53-41ef-b2f3-2a58e9afd332)  
29 | [download-manager](https://wordpress.org/plugins/download-manager/) | CVE-2021-24969 | 100,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/01144c50-54ca-44d9-9ce8-bf4f659114ee)  
30 | [download-manager](https://wordpress.org/plugins/download-manager/) | CVE-2021-25069 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/4ff5e638-1b89-41df-b65a-f821de8934e8)  
31 | [email-subscribers](https://wordpress.org/plugins/email-subscribers/) | CVE-2022-0439 | 100,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/729d3e67-d081-4a4e-ac1e-f6b0a184f095)  
32 | [email-subscribers](https://wordpress.org/plugins/email-subscribers/) | CVE-2022-3981 | 100,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/78054d08-0227-426c-903d-d146e0919028)  
33 | [intelly-related-posts](https://wordpress.org/plugins/intelly-related-posts/) | CVE-2023-6257 | 100,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/19a86448-8d7c-4f02-9290-d9f93810e6e1/)  
34 | [iubenda-cookie-law-solution](https://wordpress.org/plugins/iubenda-cookie-law-solution/) | CVE-2022-3911 | 100,000 | Privilege escalation | [WPScan](https://wpscan.com/vulnerability/c47fdca8-74ac-48a4-9780-556927fb4e52)  
35 | [learnpress](https://wordpress.org/plugins/learnpress/) | CVE-2022-0271 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/ad07d9cd-8a75-4f7c-bbbe-3b6b89b699f2)  
36 | [menu-image](https://wordpress.org/plugins/menu-image/) | CVE-2022-0450 | 100,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/612f9273-acc8-4be6-b372-33f1e687f54a)  
37 | [modern-events-calendar-lite](https://wordpress.org/plugins/modern-events-calendar-lite/) | CVE-2021-24925 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/82233588-6033-462d-b886-a8ef5ee9adb0)  
38 | [modern-events-calendar-lite](https://wordpress.org/plugins/modern-events-calendar-lite/) | CVE-2021-24946 | 100,000 | Blind SQL injection | [WPScan](https://wpscan.com/vulnerability/09871847-1d6a-4dfe-8a8c-f2f53ff87445)  
39 | [modern-events-calendar-lite](https://wordpress.org/plugins/modern-events-calendar-lite/) | CVE-2021-25046 | 100,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/19c2f456-a41e-4755-912d-13683719bae6)  
40 | [mystickymenu](https://wordpress.org/plugins/mystickymenu/) | CVE-2023-5509 | 100,000 | Missing authorization | [WPScan](https://wpscan.com/vulnerability/3b33c262-e7f0-4310-b26d-4727d7c25c9d/)  
41 | [paid-memberships-pro](https://wordpress.org/plugins/paid-memberships-pro/) | CVE-2021-25114 | 100,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/6c25a5f0-a137-4ea5-9422-8ae393d7b76b)  
42 | [relevanssi](https://wordpress.org/plugins/relevanssi/) | CVE-2023-7199 | 100,000 | Draft post read | [WPScan](https://wpscan.com/vulnerability/0c96a128-4473-41f5-82ce-94bba33ca4a3)  
43 | [relevanssi](https://wordpress.org/plugins/relevanssi/) | CVE-2024-1380 | 100,000 | Downloading full search history | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/7b2a3b17-0551-4e02-8e6a-ae8d46da0ef8)  
44 | [seo-simple-pack](https://wordpress.org/plugins/seo-simple-pack/) | CVE-2024-2795 | 100,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/seo-simple-pack/seo-simple-pack-321-information-exposure)  
45 | [squirrly-seo](https://wordpress.org/plugins/squirrly-seo/) | CVE-2021-25019 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/cea0ce4b-886a-47cc-8653-a297e9759d09)  
46 | [ti-woocommerce-wishlist](https://wordpress.org/plugins/ti-woocommerce-wishlist/) | CVE-2022-0412 | 100,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/e984ba11-abeb-4ed4-9dad-0bfd539a9682)  
47 | [vk-all-in-one-expansion-unit](https://wordpress.org/plugins/vk-all-in-one-expansion-unit/) | CVE-2024-2093 | 100,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/vk-all-in-one-expansion-unit/vk-all-in-one-expansion-unit-99501-information-exposure)  
48 | [webp-converter-for-media](https://wordpress.org/plugins/webp-converter-for-media/) | CVE-2021-25074 | 100,000 | Open redirect | [WPScan](https://wpscan.com/vulnerability/f3c0a155-9563-4533-97d4-03b9bac83164)  
49 | [woocommerce-mercadopago](https://wordpress.org/plugins/woocommerce-mercadopago/) | CVE-2024-3934 | 100,000 | Downloading arbitrary file (including wp-config.php) | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/1674e81e-6a75-436c-b219-8ec0a484a134)  
50 | [woocommerce-products-filter](https://wordpress.org/plugins/woocommerce-products-filter/) | CVE-2021-25085 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/b7dd81c6-6af1-4976-b928-421ca69bfa90)  
51 | [wpvivid-backuprestore](https://wordpress.org/plugins/wpvivid-backuprestore/) | CVE-2021-24994 | 100,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/ea74257a-f6b0-49e9-a81f-53c0eb81b1da)  
52 | [wpvivid-backuprestore](https://wordpress.org/plugins/wpvivid-backuprestore/) | CVE-2022-0531 | 100,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/ac5c2a5d-09b6-470b-a598-2972183413ca)  
53 | [advanced-cf7-db](https://wordpress.org/plugins/advanced-cf7-db/) | CVE-2021-24905 | 90,000 | Arbitrary file removal | [WPScan](https://wpscan.com/vulnerability/cf022415-6614-4b95-913b-802186766ae6)  
54 | [kingcomposer](https://wordpress.org/plugins/kingcomposer/) | CVE-2021-25048 | 90,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/5687e5db-d987-416d-a7f4-036cce4d56cb)  
55 | [kingcomposer](https://wordpress.org/plugins/kingcomposer/) | CVE-2022-0165 | 90,000 | Open redirect | [WPScan](https://wpscan.com/vulnerability/906d0c31-370e-46b4-af1f-e52fbddd00cb)  
56 | [masterslider](https://wordpress.org/plugins/masterslider/) | CVE-2024-4375 | 90,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/master-slider/master-slider-responsive-touch-slider-3910-authenticated-contributor-stored-cross-site-scripting-via-ms-layer-shortcode)  
57 | [social-networks-auto-poster-facebook-twitter-g](https://wordpress.org/plugins/social-networks-auto-poster-facebook-twitter-g/) | CVE-2021-24975 | 90,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/b99dae3d-8230-4427-adc5-4ef9cbfb8ba1)  
58 | [social-networks-auto-poster-facebook-twitter-g](https://wordpress.org/plugins/social-networks-auto-poster-facebook-twitter-g/) | CVE-2021-25072 | 90,000 | CSRF post removal | [WPScan](https://wpscan.com/vulnerability/53d2c61d-ce73-40e0-a113-9d76d8fecc91)  
59 | [tenweb-speed-optimizer](https://wordpress.org/plugins/tenweb-speed-optimizer/) | CVE-2023-5559 | 90,000 | DoS | [WPScan](https://wpscan.com/vulnerability/eba46f7d-e4db-400c-8032-015f21087bbf)  
60 | [embedpress](https://wordpress.org/plugins/embedpress/) | CVE-2023-5749 | 80,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/3931daac-3899-4169-8625-4c95fd2adafc/)  
61 | [official-mailerlite-sign-up-forms](https://wordpress.org/plugins/official-mailerlite-sign-up-forms/) | CVE-2024-2797 | 80,000 | Unauthorized settings change, allowing contributors to add and modify forms | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/a03b4c19-85fa-47ad-b9ae-b466f8e5ca96)  
62 | [themify-portfolio-post](https://wordpress.org/plugins/themify-portfolio-post/) | CVE-2022-0200 | 80,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/bbc0b812-7b30-4ab4-bac8-27c706b3f146)  
63 | [woo-product-feed-pro](https://wordpress.org/plugins/woo-product-feed-pro/) | CVE-2021-24974 | 80,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/8ed549fe-7d27-4a7a-b226-c20252964b29)  
64 | [woo-product-feed-pro](https://wordpress.org/plugins/woo-product-feed-pro/) | CVE-2022-0426 | 80,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/de69bcd1-b0b1-4b16-9655-776ee57ad90a)  
65 | [wp-google-map-plugin](https://wordpress.org/plugins/wp-google-map-plugin/) | CVE-2024-2386 | 80,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-google-map-plugin/wordpress-plugin-for-google-maps-wp-maps-461-authenticated-contributor-sql-injection)  
66 | [wp-hide-security-enhancer](https://wordpress.org/plugins/wp-hide-security-enhancer/) | CVE-2022-2538 | 80,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/afa1e159-30bc-42d2-b3f8-8c868b113d3e)  
67 | [boldgrid-easy-seo](https://wordpress.org/plugins/boldgrid-easy-seo/) | CVE-2024-2950 | 70,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/boldgrid-easy-seo/boldgrid-easy-seo-simple-and-effective-seo-1614-information-exposure)  
68 | [feed-them-social](https://wordpress.org/plugins/feed-them-social/) | CVE-2022-2532 | 70,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/07278b12-58e6-4230-b2fb-19237e9785d8)  
69 | [media-library-assistant](https://wordpress.org/plugins/media-library-assistant/) | CVE-2024-5605 | 70,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/3ba8a9f5-0633-4cf0-af27-5466d93e9020)  
70 | [stream](https://wordpress.org/plugins/stream/) | CVE-2022-4384 | 70,000 | Obtaining information about all users’ activity in the site | [WPScan](https://wpscan.com/vulnerability/2b506252-6f37-439e-8984-7316d5cca2e5)  
71 | [www-xml-sitemap-generator-org](https://wordpress.org/plugins/www-xml-sitemap-generator-org/) | CVE-2022-0346 | 70,000 | Reflected XSS and RCE | [WPScan](https://wpscan.com/vulnerability/4b339390-d71a-44e0-8682-51a12bd2bfe6)  
72 | [yith-woocommerce-ajax-search](https://wordpress.org/plugins/yith-woocommerce-ajax-search/) | CVE-2024-4455 | 70,000 | Unauthenticated Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/cf0f5fd4-cd06-4d11-9f22-1f417b546afb)  
73 | [blog2social](https://wordpress.org/plugins/blog2social/) | CVE-2024-3678 | 60,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/blog2social/blog2social-social-media-auto-post-scheduler-742-information-exposure)  
74 | [booking](https://wordpress.org/plugins/booking/) | CVE-2021-25040 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/3ed821a6-c3e2-4964-86f8-d14c4a54708a)  
75 | [contact-form-entries](https://wordpress.org/plugins/contact-form-entries/) | CVE-2024-2030. | 60,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/contact-form-plugin/contact-form-by-bestwebsoft-428-reflected-cross-site-scripting-via-cntctfrm-contact-subject)  
76 | [customer-reviews-woocommerce](https://wordpress.org/plugins/customer-reviews-woocommerce/) | CVE-2024-3731 | 60,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/c3489038-2833-4080-b802-5733afab5de8)  
77 | [interactive-3d-flipbook-powered-physics-engine](https://wordpress.org/plugins/interactive-3d-flipbook-powered-physics-engine/) | CVE-2022-0423 | 60,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/7dde0b9d-9b86-4961-b005-a11b6ffba952)  
78 | [mappress-google-maps-for-wordpress](https://wordpress.org/plugins/mappress-google-maps-for-wordpress/) | CVE-2022-0208 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/59a2abd0-4aee-47aa-ad3a-865f624fa0fc)  
79 | [permalink-manager](https://wordpress.org/plugins/permalink-manager/) | CVE-2022-0201 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/f274b0d8-74bf-43de-9051-29ce36d78ad4)  
80 | [post-grid](https://wordpress.org/plugins/post-grid/) | CVE-2022-0447 | 60,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/91ca2cc9-951e-4e96-96ff-3bf131209dbe)  
81 | [powerpack-lite-for-elementor](https://wordpress.org/plugins/powerpack-lite-for-elementor/) | CVE-2021-25027 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/48612c44-151d-4438-b91c-c27e96174270)  
82 | [print-invoices-packing-slip-labels-for-woocommerce](https://wordpress.org/plugins/print-invoices-packing-slip-labels-for-woocommerce/) | CVE-2024-3216 | 60,000 | Unauthorized plugin settings reset - removing invoicing configuration | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/aeac9c4a-0754-4fb1-bf11-0cd8483451b6)  
83 | [real-cookie-banner](https://wordpress.org/plugins/real-cookie-banner/) | CVE-2022-0445 | 60,000 | CSRF settings reset and deleting all GDPR consents | [WPScan](https://wpscan.com/vulnerability/d9f28255-0026-4c42-9e67-d17b618c2285)  
84 | [visual-portfolio](https://wordpress.org/plugins/visual-portfolio/) | CVE-2022-2543 | 60,000 | Arbitrary CSS injection | [WPScan](https://wpscan.com/vulnerability/5dc8b671-f2fa-47be-8664-9005c4fdbea8)  
85 | [visual-portfolio ](https://wordpress.org/plugins/visual-portfolio /) | CVE-2022-2597 | 60,000 | Arbitrary CSS injection | [WPScan](https://wpscan.com/vulnerability/3ffcee7c-1e03-448c-8006-a9405658cdb7)  
86 | [wd-instagram-feed](https://wordpress.org/plugins/wd-instagram-feed/) | CVE-2021-25047 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/d33241cc-17b6-491a-b836-dd9368652316)  
87 | [woocommerce-currency-switcher](https://wordpress.org/plugins/woocommerce-currency-switcher/) | CVE-2021-25043 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/8601bd21-becf-4809-8c11-d053d1121eae)  
88 | [woocommerce-currency-switcher](https://wordpress.org/plugins/woocommerce-currency-switcher/) | CVE-2022-0234 | 60,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/fd568a1f-bd51-41bb-960d-f8573b84527b)  
89 | [wp-letsencrypt-ssl](https://wordpress.org/plugins/wp-letsencrypt-ssl/) | CVE-2023-7046 | 60,000 | Exposed private keys | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-letsencrypt-ssl/wp-encryption-one-click-free-ssl-certificate-ssl-https-redirect-to-force-https-ssl-score-70-sensitive-information-exposure-via-insufficiently-protected-files)  
90 | [wp-responsive-menu](https://wordpress.org/plugins/wp-responsive-menu/) | CVE-2021-24971 | 60,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/661cb7e3-d7bd-4bc1-bf78-bdb4ba9610d7)  
91 | [wp-rss-aggregator](https://wordpress.org/plugins/wp-rss-aggregator/) | CVE-2021-24988 | 60,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/0742483b-6314-451b-a63a-536fd1e14845)  
92 | [wp-rss-aggregator](https://wordpress.org/plugins/wp-rss-aggregator/) | CVE-2022-0189 | 60,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/52a71bf1-b8bc-479e-b741-eb8fb9685014)  
93 | [ditty-news-ticker](https://wordpress.org/plugins/ditty-news-ticker/) | CVE-2022-0533 | 50,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/40f36692-c898-4441-ad24-2dc17856bd74)  
94 | [easy-digital-downloads](https://wordpress.org/plugins/easy-digital-downloads/) | CVE-2022-2389 | 50,000 | CSRF posts deletion | [WPScan](https://wpscan.com/vulnerability/db3c3c78-1724-4791-9ab6-ebb2e8a4c8b8)  
95 | [event-tickets](https://wordpress.org/plugins/event-tickets/) | CVE-2021-25028 | 50,000 | Open redirect | [WPScan](https://wpscan.com/vulnerability/80b0682e-2c3b-441b-9628-6462368e5fc7)  
96 | [getwid](https://wordpress.org/plugins/getwid/) | CVE-2023-6042 | 50,000 | Sending arbitrary e-mails to the admin | [WPScan](https://wpscan.com/vulnerability/56a1c050-67b5-43bc-b5b6-28d9a5a59eba)  
97 | [nimble-builder](https://wordpress.org/plugins/nimble-builder/) | CVE-2022-0314 | 50,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/17585f16-c62c-422d-ad9c-9138b6da97b7)  
98 | [post-grid](https://wordpress.org/plugins/post-grid/) | CVE-2024-0881 | 50,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/e460e926-6e9b-4e9f-b908-ba5c9c7fb290/)  
99 | [simple-membership](https://wordpress.org/plugins/simple-membership/) | CVE-2022-0328 | 50,000 | CSRF member deletion | [WPScan](https://wpscan.com/vulnerability/44532b7c-4d0d-4959-ada4-733f377d6ec9)  
100 | [social-networks-auto-poster-facebook-twitter-g](https://wordpress.org/plugins/social-networks-auto-poster-facebook-twitter-g/) | CVE-2024-1446 | 50,000 | CSRF post deletion | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/306b23ee-7dcb-4281-a218-21168998c4b9)  
101 | [social-pug](https://wordpress.org/plugins/social-pug/) | CVE-2024-1526 | 50,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/1664697e-0ea3-4d09-b2fd-153a104ec255/)  
102 | [super-socializer](https://wordpress.org/plugins/super-socializer/) | CVE-2021-24987 | 50,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/a14b668f-812f-46ee-827e-0996b378f7f0)  
103 | [bnfw](https://wordpress.org/plugins/bnfw/) | CVE-2022-0345 | 40,000 | E-mail leak | [WPScan](https://wpscan.com/vulnerability/b3b523b9-6c92-4091-837a-d34e3174eb19)  
104 | [theme: total](https://wordpress.org/plugins/theme: total/) | CVE-2024-1771 | 40,000 | Unauthorized settings change | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/total/total-2159-missing-authorization-to-authenticated-subscriber-sections-update)  
105 | [thirstyaffiliates](https://wordpress.org/plugins/thirstyaffiliates/) | CVE-2022-0398 | 40,000 | Arbitrary affiliate link creation | [WPScan](https://wpscan.com/vulnerability/21aec131-91ff-4300-ac7a-0bf31d6b2b24)  
106 | [tutor](https://wordpress.org/plugins/tutor/) | CVE-2021-25017 | 40,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/2d0c4872-a341-4974-926c-10b094a5d13c)  
107 | [ultimate-responsive-image-slider](https://wordpress.org/plugins/ultimate-responsive-image-slider/) | CVE-2023-6077 | 40,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/1afc0e4a-f712-47d4-bf29-7719ccbbbb1b/)  
108 | [wp-video-lightbox](https://wordpress.org/plugins/wp-video-lightbox/) | CVE-2024-4324 | 40,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/da2d8494-aea3-4a1e-9eca-946c0bd390cd)  
109 | [advanced-cron-manager](https://wordpress.org/plugins/advanced-cron-manager/) | CVE-2021-25084 | 30,000 | Arbitrary cron configuration change | [WPScan](https://wpscan.com/vulnerability/7c5c602f-499f-431b-80bc-507053984a06)  
110 | [ai-assistant-by-10web](https://wordpress.org/plugins/ai-assistant-by-10web/) | CVE-2023-6985 | 30,000 | Arbitrary plugin installation | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/229245a5-468d-47b9-8f26-d23d593e91da)  
111 | [ays-popup-box](https://wordpress.org/plugins/ays-popup-box/) | CVE-2024-3897 | 30,000 | Obtaining all users’ e-mails | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/e71e3624-ccda-4c9c-90e9-e557dd19b644)  
112 | [betterdocs](https://wordpress.org/plugins/betterdocs/) | CVE-2024-2845 | 30,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/2d113191-b550-4752-b536-644206ab56c1)  
113 | [block-options](https://wordpress.org/plugins/block-options/) | CVE-2024-2794 | 30,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/block-options/gutenberg-block-editor-toolkit-editorskit-1404-authenticated-contributor-stored-cross-site-scripting)  
114 | [contact-form-7-skins](https://wordpress.org/plugins/contact-form-7-skins/) | CVE-2021-25063 | 30,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/e2185887-3e53-4089-aa3f-981c944ee0bb)  
115 | [content-egg](https://wordpress.org/plugins/content-egg/) | CVE-2022-0428 | 30,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/071a2f69-9cd6-42a8-a56c-264a589784ab)  
116 | [download-plugins-dashboard](https://wordpress.org/plugins/download-plugins-dashboard/) | CVE-2024-7501 | 30,000 | CSRF download of all files | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/dcbfcaeb-2635-4b11-b426-ee04345d5f36)  
117 | [easy-paypal-donation](https://wordpress.org/plugins/easy-paypal-donation/) | CVE-2021-24989 | 30,000 | CSRF post removal | [WPScan](https://wpscan.com/vulnerability/82c2ead1-1d3c-442a-ae68-359a4748447f)  
118 | [futurio-extra](https://wordpress.org/plugins/futurio-extra/) | CVE-2021-25110 | 30,000 | E-mail leak | [WPScan](https://wpscan.com/vulnerability/b655fc21-47a1-4786-8911-d78ab823c153)  
119 | [google-pagespeed-insights](https://wordpress.org/plugins/google-pagespeed-insights/) | CVE-2022-0431 | 30,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/52bd94df-8816-48fd-8788-38d045eb57ca)  
120 | [html5-video-player](https://wordpress.org/plugins/html5-video-player/) | CVE-2023-6485 | 30,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/759b3866-c619-42cc-94a8-0af6d199cc81/)  
121 | [insight-core](https://wordpress.org/plugins/insight-core/) | CVE-2021-24950 | 30,000 | Stored XSS + object injection | [WPScan](https://wpscan.com/vulnerability/01d430ea-ef85-4529-9ae4-c1f70016bb75)  
122 | [lead-form-builder](https://wordpress.org/plugins/lead-form-builder/) | CVE-2021-24967 | 30,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/4e165122-4746-42de-952e-a3bf51393a74)  
123 | [master-addons](https://wordpress.org/plugins/master-addons/) | CVE-2022-0327 | 30,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/df38cc99-da3c-4cc0-b179-1e52e841b883)  
124 | [meks-easy-instagram-widget](https://wordpress.org/plugins/meks-easy-instagram-widget/) | CVE-2021-24958 | 30,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/011c2519-fd84-4c95-b8b8-23654af59d70)  
125 | [mp-timetable](https://wordpress.org/plugins/mp-timetable/) | CVE-2024-3342 | 30,000 | Contributor+ Blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/mp-timetable/timetable-and-event-schedule-by-motopress-2411-authenticated-contributor-sql-injection)  
126 | [my-calendar](https://wordpress.org/plugins/my-calendar/) | CVE-2021-24927 | 30,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/86f3acc7-8902-4215-bd75-6105d601524e)  
127 | [notificationx](https://wordpress.org/plugins/notificationx/) | CVE-2022-0349 | 30,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/1d0dd7be-29f3-4043-a9c6-67d02746463a)  
128 | [notificationx](https://wordpress.org/plugins/notificationx/) | CVE-2024-1698 | 30,000 | Blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/e110ea99-e2fa-4558-bcf3-942a35af0b91)  
129 | [photo-gallery](https://wordpress.org/plugins/photo-gallery/) | CVE-2022-0169 | 30,000 | SQL Injection | [WPScan](https://wpscan.com/vulnerability/0b4d870f-eab8-4544-91f8-9c5f0538709c)  
130 | [protect-wp-admin](https://wordpress.org/plugins/protect-wp-admin/) | CVE-2021-24906 | 30,000 | Disabling of plugin security features | [WPScan](https://wpscan.com/vulnerability/4204682b-f657-42e1-941c-bee7a245e9fd)  
131 | [pz-linkcard](https://wordpress.org/plugins/pz-linkcard/) | CVE-2021-25012 | 30,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/b126d2fc-6cc7-4c18-b95e-d32c2effcc4f)  
132 | [seriously-simple-podcasting](https://wordpress.org/plugins/seriously-simple-podcasting/) | CVE-2023-6444 | 30,000 | Admin e-mail leak | [WPScan](https://wpscan.com/vulnerability/061c59d6-f4a0-4cd1-b945-5e92b9c2b4aa)  
133 | [simple-social-buttons](https://wordpress.org/plugins/simple-social-buttons/) | CVE-2023-5845 | 30,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/d5b59e9e-85e5-4d26-aebe-64757c8495fa/)  
134 | [simply-schedule-appointments](https://wordpress.org/plugins/simply-schedule-appointments/) | CVE-2024-1760 | 30,000 | CSRF removing of all plugin data (appointments etc) | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simply-schedule-appointments/appointment-booking-calendar-simply-schedule-appointments-booking-plugin-16620-cross-site-request-forgery-to-plugin-data-reset)  
135 | [simply-schedule-appointments](https://wordpress.org/plugins/simply-schedule-appointments/) | CVE-2024-2341 | 30,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simply-schedule-appointments/appointment-booking-calendar-simply-schedule-appointments-booking-plugin-1677-authenticated-contributor-sql-injection-via-shortcode)  
136 | [simply-schedule-appointments](https://wordpress.org/plugins/simply-schedule-appointments/) | CVE-2024-2342 | 30,000 | SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simply-schedule-appointments/appointment-booking-calendar-simply-schedule-appointments-booking-plugin-1677-authenticated-subscriber-sql-injection)  
137 | [simply-schedule-appointments](https://wordpress.org/plugins/simply-schedule-appointments/) | CVE-2024-4288 | 30,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simply-schedule-appointments/appointment-booking-calendar-simply-schedule-appointments-booking-plugin-16714-authenticated-contributor-stored-cross-site-scripting)  
138 | [site-reviews](https://wordpress.org/plugins/site-reviews/) | CVE-2021-24973 | 30,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/0118f245-0e6f-44c1-9bdb-5b3a5d2403d6)  
139 | [social-warfare](https://wordpress.org/plugins/social-warfare/) | CVE-2024-1959 | 30,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/social-warfare/social-sharing-plugin-social-warfare-4461-authenticatedcontributor-stored-cross-site-scripting-via-shortcode)  
140 | [theme: responsive](https://wordpress.org/plugins/theme: responsive/) | CVE-2024-2848 | 30,000 | Injecting any HTML (without scripts) to the footer | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/dbe0cc57-a17d-4f91-887f-fe819b32f6b3)  
141 | [ultimate-faqs](https://wordpress.org/plugins/ultimate-faqs/) | CVE-2021-24968 | 30,000 | Possibility to add arbitrary FAQs | [WPScan](https://wpscan.com/vulnerability/f0a9e6cc-46cc-4ac2-927a-c006b8e8aa68)  
142 | [video-conferencing-with-zoom-api](https://wordpress.org/plugins/video-conferencing-with-zoom-api/) | CVE-2022-0384 | 30,000 | E-mail leak | [WPScan](https://wpscan.com/vulnerability/91c44c45-994b-4aed-b9f9-7db45924eeb4)  
143 | [visualizer](https://wordpress.org/plugins/visualizer/) | CVE-2024-3750 | 30,000 | Downloading arbitrary data from the database | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/6d27544c-97a5-42cd-ab07-358f819acbc4)  
144 | [woo-smart-wishlist](https://wordpress.org/plugins/woo-smart-wishlist/) | CVE-2022-0397 | 30,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/c8091254-1ced-4363-ab7f-5b880447713d)  
145 | [wp-user-frontend](https://wordpress.org/plugins/wp-user-frontend/) | CVE-2021-25076 | 30,000 | SQL injection in admin panel leading to reflected XSS | [WPScan](https://wpscan.com/vulnerability/6d3eeba6-5560-4380-a6e9-f008a9112ac6)  
146 | [xcloner-backup-and-restore](https://wordpress.org/plugins/xcloner-backup-and-restore/) | CVE-2022-0444 | 30,000 | Resetting settings, including encryption key | [WPScan](https://wpscan.com/vulnerability/9567d295-43c7-4e59-9283-c7726f16d40b)  
147 | [ad-invalid-click-protector](https://wordpress.org/plugins/ad-invalid-click-protector/) | CVE-2022-0190 | 20,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/ae322f11-d8b4-4b69-9efa-0fb87475fa44)  
148 | [ad-invalid-click-protector](https://wordpress.org/plugins/ad-invalid-click-protector/) | CVE-2022-0191 | 20,000 | CSRF ban removal | [WPScan](https://wpscan.com/vulnerability/d4c32a02-810f-43d8-946a-b7e18ac54f55)  
149 | [advanced-product-labels-for-woocommerce](https://wordpress.org/plugins/advanced-product-labels-for-woocommerce/) | CVE-2022-0399 | 20,000 | Reflected XSS (logged-in POST 3) | [WPScan](https://wpscan.com/vulnerability/5e5fdcf4-ec2b-4e73-8009-05606b2d5164)  
150 | [asgaros-forum](https://wordpress.org/plugins/asgaros-forum/) | CVE-2022-0411 | 20,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/35272197-c973-48ad-8405-538bfbafa172)  
151 | [bwp-google-xml-sitemaps](https://wordpress.org/plugins/bwp-google-xml-sitemaps/) | CVE-2022-0230 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/c73316d2-ae6a-42db-935b-b8b03a7e4363)  
152 | [crazy-bone](https://wordpress.org/plugins/crazy-bone/) | CVE-2022-0385 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/60067b8b-9fa5-40d1-817a-929779947891)  
153 | [custom-post-widget](https://wordpress.org/plugins/custom-post-widget/) | CVE-2024-3564 | 20,000 | Contributor+ LFI | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/c5a0b8fe-d284-4780-84b5-2e97fa96c99a)  
154 | [easy-appointments](https://wordpress.org/plugins/easy-appointments/) | CVE-2024-2842 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/easy-appointments/easy-appointments-31118-authenticated-contributor-stored-cross-site-scripting)  
155 | [easy-testimonials](https://wordpress.org/plugins/easy-testimonials/) | CVE-2024-2337 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/2c470cb0-5cbc-4ae1-b75a-384668d07215)  
156 | [ecwid-shopping-cart](https://wordpress.org/plugins/ecwid-shopping-cart/) | CVE-2023-6292 | 20,000 | Unauthorized settings change | [WPScan](https://wpscan.com/vulnerability/d4cf799e-2571-4b96-a303-78dcafbfcf40)  
157 | [ecwid-shopping-cart](https://wordpress.org/plugins/ecwid-shopping-cart/) | CVE-2024-2456 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/ecwid-shopping-cart/ecwid-ecommerce-shopping-cart-61210-authenticatedcontributor-stored-cross-site-scripting-via-shortcode)  
158 | [embed-form](https://wordpress.org/plugins/embed-form/) | CVE-2024-2542 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/embed-form/jotform-online-forms-131-authenticatedcontributor-stored-cross-site-scripting-via-shortcode)  
159 | [enhanced-e-commerce-for-woocommerce-store](https://wordpress.org/plugins/enhanced-e-commerce-for-woocommerce-store/) | CVE-2024-1203 | 20,000 | Blind SQL Injection (at least one woocommerce product must exist) | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/enhanced-e-commerce-for-woocommerce-store/conversios-google-analytics-4-ga4-meta-pixel-more-via-google-tag-manager-for-woocommerce-691-authenticated-subscriber-sql-injection)  
160 | [event-calendar-wd](https://wordpress.org/plugins/event-calendar-wd/) | CVE-2021-25024 | 20,000 | XSS | [WPScan](https://wpscan.com/vulnerability/08864b76-d898-4dfe-970d-d7cc1b1115a7)  
161 | [event-calendar-wd](https://wordpress.org/plugins/event-calendar-wd/) | CVE-2021-25025 | 20,000 | Possibility to add arbitrary events | [WPScan](https://wpscan.com/vulnerability/24fb4eb4-9fe1-4433-8844-8904eaf13c0e)  
162 | [favorites](https://wordpress.org/plugins/favorites/) | CVE-2024-2948 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/38a87046-9a46-40c2-b10d-d1a7d5ef8742)  
163 | [float-menu](https://wordpress.org/plugins/float-menu/) | CVE-2022-0313 | 20,000 | CSRF menu deletion | [WPScan](https://wpscan.com/vulnerability/1ce6c8f4-6f4b-4d56-8d11-43355ef32e8c)  
164 | [gmap-embed](https://wordpress.org/plugins/gmap-embed/) | CVE-2021-25011 | 20,000 | Arbitrary post removal, plugin settings update | [WPScan](https://wpscan.com/vulnerability/6639da0d-6d29-46c1-a3cc-5e5626305833)  
165 | [gmap-embed](https://wordpress.org/plugins/gmap-embed/) | CVE-2021-25081 | 20,000 | Arbitrary post removal, plugin settings update via CSRF | [WPScan](https://wpscan.com/vulnerability/f85cf258-1c2f-444e-91e5-b1fc55880f0e)  
166 | [image-hover-effects-ultimate](https://wordpress.org/plugins/image-hover-effects-ultimate/) | CVE-2021-25031 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/1fbcf5ec-498e-4d40-8577-84b8c7ac3201)  
167 | [leadconnector](https://wordpress.org/plugins/leadconnector/) | CVE-2024-1371 | 20,000 | Post removal | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/79e786ce-a3eb-40df-8dad-4c9c75243bec)  
168 | [material-design-for-contact-form-7](https://wordpress.org/plugins/material-design-for-contact-form-7/) | CVE-2022-0404 | 20,000 | DoS | [WPScan](https://wpscan.com/vulnerability/6d0932bb-d515-4432-b67b-16aba34bd285)  
169 | [miniorange-2-factor-authentication](https://wordpress.org/plugins/miniorange-2-factor-authentication/) | CVE-2022-0229 | 20,000 | DoS | [WPScan](https://wpscan.com/vulnerability/d70c5335-4c01-448d-85fc-f8e75b104351)  
170 | [mycred](https://wordpress.org/plugins/mycred/) | CVE-2021-25015 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/7608829d-2820-49e2-a10e-e93eb3005f68)  
171 | [mycred](https://wordpress.org/plugins/mycred/) | CVE-2022-0287 | 20,000 | E-mail leak | [WPScan](https://wpscan.com/vulnerability/6cd7cd6d-1cc1-472c-809b-b66389f149b0)  
172 | [mycred](https://wordpress.org/plugins/mycred/) | CVE-2022-0363 | 20,000 | Arbitrary post creation | [WPScan](https://wpscan.com/vulnerability/a438a951-497c-43cd-822f-1a48d4315191)  
173 | [mystickyelements](https://wordpress.org/plugins/mystickyelements/) | CVE-2022-0148 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/37665ee1-c57f-4445-9596-df4f7d72c8cd)  
174 | [navz-photo-gallery](https://wordpress.org/plugins/navz-photo-gallery/) | CVE-2021-24909 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/5855f1fe-28f6-4cd6-a83c-95c23d809b79)  
175 | [newstatpress](https://wordpress.org/plugins/newstatpress/) | CVE-2022-0206 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/ce12437a-d440-4c4a-9247-95a8f39d00b9)  
176 | [page-views-count](https://wordpress.org/plugins/page-views-count/) | CVE-2022-0434 | 20,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/be895016-7365-4ce4-a54f-f36d0ef2d6f1)  
177 | [quiz-maker](https://wordpress.org/plugins/quiz-maker/) | CVE-2023-6155 | 20,000 | Unauthorized obtaining of all users’ emails | [WPScan](https://wpscan.com/vulnerability/c62be802-e91a-4bcf-990d-8fd8ef7c9a28)  
178 | [related-posts-for-wp](https://wordpress.org/plugins/related-posts-for-wp/) | CVE-2024-0592 | 20,000 | Draft and password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/related-posts-for-wp/related-posts-for-wordpress-221-cross-site-request-forgery)  
179 | [restaurant-reservations](https://wordpress.org/plugins/restaurant-reservations/) | CVE-2021-24965 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/306ecf09-fdf0-449c-930c-9dfa58f0efc2)  
180 | [shapepress-dsgvo](https://wordpress.org/plugins/shapepress-dsgvo/) | CVE-2024-3201 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/shapepress-dsgvo/wp-dsgvo-tools-gdpr-3132-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
181 | [sharethis-share-buttons](https://wordpress.org/plugins/sharethis-share-buttons/) | CVE-2024-3648 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/03b37c90-4bb5-4003-a440-3fb57a5c1cae)  
182 | [simple-facebook-plugin](https://wordpress.org/plugins/simple-facebook-plugin/) | CVE-2024-3583 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/070f6820-e70c-4325-b5cb-d2010da34dce)  
183 | [simple-job-board](https://wordpress.org/plugins/simple-job-board/) | CVE-2024-0593 | 20,000 | Draft and password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simple-job-board/simple-job-board-2108-missing-authorization-to-unauthenticated-information-disclosure)  
184 | [smartcrawl-seo](https://wordpress.org/plugins/smartcrawl-seo/) | CVE-2023-5949 | 20,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/3cec27ca-f470-402d-ae3e-271cb59cf407)  
185 | [smartcrawl-seo](https://wordpress.org/plugins/smartcrawl-seo/) | CVE-2024-3287 | 20,000 | Adding arbitrary data to the ld+json description | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/9a77672b-340e-4f10-abe7-461c2db537b8)  
186 | [usc-e-shop](https://wordpress.org/plugins/usc-e-shop/) | CVE-2023-5952 | 20,000 | Object injection | [WPScan](https://wpscan.com/vulnerability/0acd613e-dbd6-42ae-9f3d-6d6e77a4c1b7/)  
187 | [video-conferencing-with-zoom-api](https://wordpress.org/plugins/video-conferencing-with-zoom-api/) | CVE-2024-2033 | 20,000 | Leak of all users’ e-mails | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/video-conferencing-with-zoom-api/video-conferencing-with-zoom-445-sensitive-information-exposure)  
188 | [video-conferencing-with-zoom-api](https://wordpress.org/plugins/video-conferencing-with-zoom-api/) | CVE-2024-2031 | 20,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/06e48355-6932-4401-8787-e6432444930f)  
189 | [website-article-monetization-by-magenet](https://wordpress.org/plugins/website-article-monetization-by-magenet/) | CVE-2024-1379 | 20,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/b8564dbb-6be8-4999-be65-d28609e05451)  
190 | [woo-product-slider](https://wordpress.org/plugins/woo-product-slider/) | CVE-2022-2382 | 20,000 | DoS | [WPScan](https://wpscan.com/vulnerability/777d4637-444b-4eda-bc21-95d3a3bf6cd3)  
191 | [woocommerce-product-addon](https://wordpress.org/plugins/woocommerce-product-addon/) | CVE-2021-25018 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/9e092aad-0b36-45a9-8987-8d904b34fbb2)  
192 | [wp-accessiblity-helper](https://wordpress.org/plugins/wp-accessiblity-helper/) | CVE-2022-0150 | 20,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/7142a538-7c3d-4dd0-bd2c-cbd2efaf53c5)  
193 | [wp-ecommerce-paypal](https://wordpress.org/plugins/wp-ecommerce-paypal/) | CVE-2024-1719 | 20,000 | CSRF | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/detail/easy-paypal-stripe-buy-now-button-183-cross-site-request-forgery-to-settings-update)  
194 | [wp-event-manager](https://wordpress.org/plugins/wp-event-manager/) | CVE-2024-2691 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/01a6dcf2-6f0b-494b-a18c-04bd9c44e0ce)  
195 | [wp-file-upload](https://wordpress.org/plugins/wp-file-upload/) | CVE-2024-2847 | 20,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-file-upload/wordpress-file-upload-4245-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
196 | [wp-meta-seo](https://wordpress.org/plugins/wp-meta-seo/) | CVE-2023-6962 | 20,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-meta-seo/wp-meta-seo-4512-information-exposure-via-meta-description)  
197 | [wp-meta-seo](https://wordpress.org/plugins/wp-meta-seo/) | CVE-2023-6961 | 20,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-meta-seo/wp-meta-seo-4512-unauthenticated-stored-cross-site-scripting-via-referer-header)  
198 | [wp-social](https://wordpress.org/plugins/wp-social/) | CVE-2024-1763 | 20,000 | Arbitrary login provider disabling | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/4f145c85-f3c6-46a7-b8ae-d486dd23087d)  
199 | [wp-stats-manager](https://wordpress.org/plugins/wp-stats-manager/) | CVE-2021-24750 | 20,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/7528aded-b8c9-4833-89d6-9cd7df3620de)  
200 | [wp-stats-manager](https://wordpress.org/plugins/wp-stats-manager/) | CVE-2021-25042 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/05b9e478-2d3b-4460-88c1-7f81d3a68ac4)  
201 | [wp-stats-manager](https://wordpress.org/plugins/wp-stats-manager/) | CVE-2022-0410 | 20,000 | Blind SQL Injection | [WPScan](https://wpscan.com/vulnerability/0d6b89f5-cf12-4ad4-831b-fed26763ba20)  
202 | [wp-useronline](https://wordpress.org/plugins/wp-useronline/) | CVE-2023-5560 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/55d23184-fc5a-4090-b079-142407b59b05/)  
203 | [wpforo](https://wordpress.org/plugins/wpforo/) | CVE-2024-3200 | 20,000 | Contributor+ Blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/f54cdad2-88db-4604-8064-fa6175176760)  
204 | [wplegalpages](https://wordpress.org/plugins/wplegalpages/) | CVE-2021-25106 | 20,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/47df802d-5200-484b-959c-9f569edf992e)  
205 | [addons-for-visual-composer](https://wordpress.org/plugins/addons-for-visual-composer/) | CVE-2024-2079 | 10,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/addons-for-visual-composer/wpbakery-page-builder-addons-by-livemesh-381-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
206 | [advanced-form-integration-log](https://wordpress.org/plugins/advanced-form-integration-log/) | CVE-2024-2387 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/advanced-form-integration/advanced-form-integration-connect-woocommerce-and-contact-form-7-to-google-sheets-and-other-platforms-1820-sql-injection-to-reflected-cross-site-scripting-via-integration-id)  
207 | [advanced-page-visit-counter](https://wordpress.org/plugins/advanced-page-visit-counter/) | CVE-2021-24957 | 10,000 | Blind SQL injection | [WPScan](https://wpscan.com/vulnerability/a282606f-6abf-4f75-99c9-dab0bea8cc96)  
208 | [advanced-page-visit-counter](https://wordpress.org/plugins/advanced-page-visit-counter/) | CVE-2021-25086 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/2cf9e517-d882-4af2-bd12-e700b75e7a11)  
209 | [advanced-post-blocks](https://wordpress.org/plugins/advanced-post-blocks/) | CVE-2024-0908 | 10,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/advanced-post-block/advanced-post-block-display-posts-pages-or-custom-posts-on-your-page-1131-missing-authorization-to-information-disclosure)  
210 | [affiliates-manager](https://wordpress.org/plugins/affiliates-manager/) | CVE-2021-25078 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/d4edb5f2-aa1b-4e2d-abb4-76c46def6c6e)  
211 | [akismet-privacy-policies](https://wordpress.org/plugins/akismet-privacy-policies/) | CVE-2021-25071 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/53085936-fa07-4f00-a7dc-bbe98c51320e)  
212 | [ari-fancy-lightbox](https://wordpress.org/plugins/ari-fancy-lightbox/) | CVE-2022-0161 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/6b37fa17-0dcb-47a7-b1eb-f9f6abb458c0)  
213 | [awesome-support](https://wordpress.org/plugins/awesome-support/) | CVE-2023-5352 | 10,000 | Arbitrary post content edit and removal | [WPScan](https://wpscan.com/vulnerability/d32b2136-d923-4f36-bd76-af4578deb23b/)  
214 | [awesome-support](https://wordpress.org/plugins/awesome-support/) | CVE-2024-0594 | 10,000 | SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/awesome-support/awesome-support-wordpress-helpdesk-support-plugin-617-authenticated-subscriber-sql-injection)  
215 | [awesome-support](https://wordpress.org/plugins/awesome-support/) | CVE-2024-0595 | 10,000 | User e-mail leak | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/awesome-support/awesome-support-wordpress-helpdesk-support-plugin-617-missing-authorization-via-wpas-get-users)  
216 | [awesome-support](https://wordpress.org/plugins/awesome-support/) | CVE-2024-0596 | 10,000 | Password-protected and draft post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/awesome-support/awesome-support-wordpress-helpdesk-support-plugin-617-missing-authorization-via-editor-html)  
217 | [ba-book-everything](https://wordpress.org/plugins/ba-book-everything/) | CVE-2024-3672 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/ba-book-everything/ba-book-everything-168-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
218 | [booster-extension](https://wordpress.org/plugins/booster-extension/) | CVE-2024-2109 | 10,000 | Leak of all users’ e-mails | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/89458095-2efe-4162-961a-7dc80852d312)  
219 | [buddypress-media](https://wordpress.org/plugins/buddypress-media/) | CVE-2023-5931 | 10,000 | RCE | [WPScan](https://wpscan.com/vulnerability/3d6889e3-a01b-4e7f-868f-af7cc8c7531a/)  
220 | [buddypress-media](https://wordpress.org/plugins/buddypress-media/) | CVE-2024-3293 | 10,000 | Contributor+ Blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/buddypress-media/rtmedia-for-wordpress-buddypress-and-bbpress-4618-authenticated-contributor-sql-injection-via-rtmedia-gallery-shortcode)  
221 | [business-directory-plugin](https://wordpress.org/plugins/business-directory-plugin/) | CVE-2024-4443 | 10,000 | Unauthenticated blind SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/982fb304-08d6-4195-97a3-f18e94295492)  
222 | [business-profile](https://wordpress.org/plugins/business-profile/) | CVE-2021-25060 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/9e1ac711-1f65-49fa-b007-66170a77b265)  
223 | [cardoza-facebook-like-box](https://wordpress.org/plugins/cardoza-facebook-like-box/) | CVE-2024-5224 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/cardoza-facebook-like-box/easy-social-like-box-popup-sidebar-widget-40-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
224 | [coming-soon-page](https://wordpress.org/plugins/coming-soon-page/) | CVE-2022-0164 | 10,000 | Sending any e-mail to all subscribers | [WPScan](https://wpscan.com/vulnerability/942535f9-73bf-4467-872a-20075f03bc51)  
225 | [coming-soon-page](https://wordpress.org/plugins/coming-soon-page/) | CVE-2022-0199 | 10,000 | Sending any e-mail to all subscribers via CSRF | [WPScan](https://wpscan.com/vulnerability/1ab1748f-c939-4953-83fc-9df878da7714)  
226 | [content-protector](https://wordpress.org/plugins/content-protector/) | CVE-2024-2026 | 10,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/content-protector/passster-4264-authenticated-contributor-stored-cross-site-scripting-via-content-protector-shortcode)  
227 | [conveythis-translate](https://wordpress.org/plugins/conveythis-translate/) | CVE-2023-6811 | 10,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/conveythis-translate/language-translate-widget-for-wordpress-conveythis-223-unauthenticated-stored-cross-site-scripting-via-api-key)  
228 | [custom-registration-form-builder-with-submission-manager](https://wordpress.org/plugins/custom-registration-form-builder-with-submission-manager/) | CVE-2024-1990 | 10,000 | Contributor+ blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/custom-registration-form-builder-with-submission-manager/registrationmagic-custom-registration-forms-user-registration-payment-and-user-login-5310-authenticated-contributor-sql-injection-via-shortcode)  
229 | [custom-registration-form-builder-with-submission-manager](https://wordpress.org/plugins/custom-registration-form-builder-with-submission-manager/) | CVE-2024-1991 | 10,000 | Promoting any user to administrator | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/766e3966-157a-4db3-9179-813032343f76)  
230 | [customer-area](https://wordpress.org/plugins/customer-area/) | CVE-2023-6824 | 10,000 | Obtaining other user’s address | [WPScan](https://wpscan.com/vulnerability/a224b984-770a-4534-b689-0701b582b388/)  
231 | [customer-area](https://wordpress.org/plugins/customer-area/) | CVE- 2023-6741 | 10,000 | Changing other user’s address | [WPScan](https://wpscan.com/vulnerability/9debe1ea-18ad-44c4-8078-68eb66d36c4a/)  
232 | [customer-area](https://wordpress.org/plugins/customer-area/) | CVE-2024-0665 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/customer-area/wp-customer-area-822-reflected-cross-site-scripting)  
233 | [demomentsomtres-wp-export](https://wordpress.org/plugins/demomentsomtres-wp-export/) | CVE-2023-5905 | 10,000 | Unauthorized data export (including user e-mails, post drafts, private posts) | [WPScan](https://wpscan.com/vulnerability/f94e91ef-1773-476c-9945-37e89ceefd3f)  
234 | [directorist](https://wordpress.org/plugins/directorist/) | CVE-2022-2376 | 10,000 | E-mail leak | [WPScan](https://wpscan.com/vulnerability/437c4330-376a-4392-86c6-c4c7ed9583ad)  
235 | [directorist](https://wordpress.org/plugins/directorist/) | CVE-2022-2377 | 10,000 | Sending arbitrary e-mails | [WPScan](https://wpscan.com/vulnerability/f4e606e9-0664-42fb-a59b-21de306eb530)  
236 | [download-attachments](https://wordpress.org/plugins/download-attachments/) | CVE-2024-3230 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/62475d8f-a0f6-45ab-abd0-ad24e1887c91)  
237 | [dropdown-menu-widget](https://wordpress.org/plugins/dropdown-menu-widget/) | CVE-2021-25113 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/7a5078db-e0d4-4076-9de9-5401c3ca0d65)  
238 | [duplicate-page-or-post](https://wordpress.org/plugins/duplicate-page-or-post/) | CVE-2021-25075 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/db5a0431-af4d-45b7-be4e-36b6c90a601b)  
239 | [easy-custom-auto-excerpt](https://wordpress.org/plugins/easy-custom-auto-excerpt/) | CVE-2024-3312 | 10,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/easy-custom-auto-excerpt/easy-custom-auto-excerpt-2412-sensitive-information-exposure)  
240 | [easy-pricing-tables](https://wordpress.org/plugins/easy-pricing-tables/) | CVE-2021-25098 | 10,000 | CSRF post removal | [WPScan](https://wpscan.com/vulnerability/960a634d-a88a-4d90-9ac3-7d24b1fe07fe)  
241 | [ecommerce-product-catalog](https://wordpress.org/plugins/ecommerce-product-catalog/) | CVE-2023-5979 | 10,000 | CSRF all product removal | [WPScan](https://wpscan.com/vulnerability/936934c3-5bfe-416e-b6aa-47bed4db05c4)  
242 | [english-wp-admin](https://wordpress.org/plugins/english-wp-admin/) | CVE-2021-25111 | 10,000 | Open redirect | [WPScan](https://wpscan.com/vulnerability/af548fab-96c2-4129-b609-e24aad0b1fc4)  
243 | [enjoy-instagram-instagram-responsive-images-gallery-and-carousel](https://wordpress.org/plugins/enjoy-instagram-instagram-responsive-images-gallery-and-carousel/) | CVE-2024-0779 | 10,000 | User account deletion | [WPScan](https://wpscan.com/vulnerability/ced134cf-82c5-401b-9476-b6456e1924e2/)  
244 | [eroom-zoom-meetings-webinar_](https://wordpress.org/plugins/eroom-zoom-meetings-webinar_/) | CVE-2024-3275 | 10,000 | Draft post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/eroom-zoom-meetings-webinar/eroom-zoom-meetings-webinar-1418-missing-authorization-to-information-exposure)  
245 | [essential-real-estate](https://wordpress.org/plugins/essential-real-estate/) | CVE-2023-6139 | 10,000 | DoS | [WPScan](https://wpscan.com/vulnerability/96396a22-f523-4c51-8b72-52be266988aa)  
246 | [essential-real-estate](https://wordpress.org/plugins/essential-real-estate/) | CVE-2023-6141 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/df12513b-9664-45be-8824-2924bfddf364)  
247 | [essential-real-estate](https://wordpress.org/plugins/essential-real-estate/) | CVE-2024-4273 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/c62ec31a-55e9-4404-b860-fa9a51ba3d3f)  
248 | [feedwordpress](https://wordpress.org/plugins/feedwordpress/) | CVE-2024-0839 | 10,000 | Draft post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/feedwordpress/feedwordpress-20220222-insecure-direct-object-referece)  
249 | [gamipress](https://wordpress.org/plugins/gamipress/) | CVE-2024-1799 | 10,000 | Contributor+ blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/gamipress/gamipress-the-1-gamification-plugin-to-reward-points-achievements-badges-ranks-in-wordpress-686-authenticated-contributor-sql-injection-via-shortcode)  
250 | [gamipress](https://wordpress.org/plugins/gamipress/) | CVE-2024-2783 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/gamipress/gamipress-the-1-gamification-plugin-to-reward-points-achievements-badges-ranks-in-wordpress-690-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
251 | [geodirectory](https://wordpress.org/plugins/geodirectory/) | CVE-2024-3732 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/geodirectory/geodirectory-wordpress-business-directory-plugin-or-classified-directory-2348-authenticated-contributor-stored-cross-site-scripting-via-gd-single-tabs-shortcode)  
252 | [ibtana-visual-editor](https://wordpress.org/plugins/ibtana-visual-editor/) | CVE-2021-25014 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/63c58d7f-8e0b-4aa5-b3c8-8726b4f19bf1)  
253 | [ip2location-country-blocker](https://wordpress.org/plugins/ip2location-country-blocker/) | CVE-2021-25095 | 10,000 | Banning arbitrary countries | [WPScan](https://wpscan.com/vulnerability/cbfa7211-ac1f-4cf2-bd79-ebce2fc4baa1)  
254 | [ip2location-country-blocker](https://wordpress.org/plugins/ip2location-country-blocker/) | CVE-2021-25096 | 10,000 | Ban circumvention | [WPScan](https://wpscan.com/vulnerability/e6dd140e-0c9d-41dc-821e-4910a13122c1)  
255 | [ip2location-country-blocker](https://wordpress.org/plugins/ip2location-country-blocker/) | CVE-2021-25108 | 10,000 | Banning countries via CSRF | [WPScan](https://wpscan.com/vulnerability/9d416ca3-bd02-4fcf-b3b8-f2f2280d02d2)  
256 | [job-postings](https://wordpress.org/plugins/job-postings/) | CVE-2024-2833 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/job-postings/jobs-for-wordpress-275-reflected-cross-site-scripting-via-job-search)  
257 | [leaflet-maps-marker](https://wordpress.org/plugins/leaflet-maps-marker/) | CVE-2024-3670 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/leaflet-maps-marker/leaflet-maps-marker-google-maps-openstreetmap-bing-maps-3128-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
258 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2021-25091 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/96204946-0b10-4a2c-8079-473883ff95b6)  
259 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2021-25092 | 10,000 | CSRF settings reset | [WPScan](https://wpscan.com/vulnerability/1cd30913-67c7-46c3-a2de-dcca0c332323)  
260 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2021-25093 | 10,000 | Arbitrary link removal | [WPScan](https://wpscan.com/vulnerability/7a7603ce-d76d-4c49-a886-67653bed8cd3)  
261 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2024-1559 | 10,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/407a5c69-cce0-4868-aef0-ffc88981e256)  
262 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2024-2325 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/link-library/link-library-766-reflected-cross-site-scripting)  
263 | [link-library](https://wordpress.org/plugins/link-library/) | CVE-2024-4281 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/30c9c4b9-6905-4d8a-bc55-5cd6f6201d25)  
264 | [login-logout-register-menu](https://wordpress.org/plugins/login-logout-register-menu/) | CVE-2024-3726 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/login-logout-register-menu/login-logout-register-menu-20-authenticated-contributor-stored-cross-site-scripting-via-llrmloginlogout-shortcode)  
265 | [masterstudy-lms-learning-management-system](https://wordpress.org/plugins/masterstudy-lms-learning-management-system/) | CVE-2024-1904 | 10,000 | Draft and password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/1be686d3-16b1-4ec7-b304-848ca4d7162c)  
266 | [meow-gallery](https://wordpress.org/plugins/meow-gallery/) | CVE-2024-4386 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/meow-gallery/gallery-block-meow-gallery-513-authenticated-contributor-stored-cross-site-scripting)  
267 | [modal-window](https://wordpress.org/plugins/modal-window/) | CVE-2021-25051 | 10,000 | CSRF RCE | [WPScan](https://wpscan.com/vulnerability/566ff8dc-f820-412b-b2d3-fa789bce528e)  
268 | [motopress-hotel-booking-lite](https://wordpress.org/plugins/motopress-hotel-booking-lite/) | CVE-2023-5991 | 10,000 | Arbitrary file download and removal | [WPScan](https://wpscan.com/vulnerability/e9d35e36-1e60-4483-b8b3-5cbf08fcd49e)  
269 | [opengraph](https://wordpress.org/plugins/opengraph/) | CVE-2024-5615 | 10,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/f57dc0fe-07f3-457e-8080-fe530f6a9f01)  
270 | [osm](https://wordpress.org/plugins/osm/) | CVE-2024-3603 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/osm/osm-openstreetmap-602-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
271 | [osm](https://wordpress.org/plugins/osm/) | CVE-2024-3604 | 10,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/osm/osm-openstreetmap-602-authenticated-contributor-sql-injection)  
272 | [page-builder-add](https://wordpress.org/plugins/page-builder-add/) | CVE-2021-25067 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/365007f0-61ac-4e81-8a3a-3a068f2c84bc)  
273 | [page-builder-sandwich](https://wordpress.org/plugins/page-builder-sandwich/) | CVE-2024-1285 | 10,000 | Arbitrary post content change | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/page-builder-sandwich/page-builder-sandwich-510-missing-authorization-to-authenticatedsubscriber-arbitrary-post-editing)  
274 | [page-builder-sandwich](https://wordpress.org/plugins/page-builder-sandwich/) | CVE-2024-1381 | 10,000 | Downloading arbitrary data from the database | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/page-builder-sandwich/page-builder-sandwich-front-end-wordpress-page-builder-plugin-510-sensitive-information-exposure)  
275 | [pearl-header-builder](https://wordpress.org/plugins/pearl-header-builder/) | CVE-2024-4000 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/c23bba83-35d2-4098-8104-8389bb2ff880)  
276 | [portfolio-wp](https://wordpress.org/plugins/portfolio-wp/) | CVE-2021-25090 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/32a4a2b5-ef65-4e29-af4a-f003dbd0809c)  
277 | [powerpack-addon-for-beaver-builder](https://wordpress.org/plugins/powerpack-addon-for-beaver-builder/) | CVE-2022-0176 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/564a66d5-7fab-4de0-868a-e19466a507af)  
278 | [print-o-matic](https://wordpress.org/plugins/print-o-matic/) | CVE-2024-3671 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/print-o-matic/print-o-matic-2110-authenticated-contributor-stored-cross-site-scripting-via-shortcode)  
279 | [qubely](https://wordpress.org/plugins/qubely/) | CVE-2021-25013 | 10,000 | Arbitrary post removal | [WPScan](https://wpscan.com/vulnerability/e88b7a70-ee71-439f-b3c6-0300adb980b0)  
280 | [rearrange-woocommerce-products](https://wordpress.org/plugins/rearrange-woocommerce-products/) | CVE-2021-24928 | 10,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/3762a77c-b8c9-428f-877c-bbfd7958e7be)  
281 | [registrations-for-the-events-calendar](https://wordpress.org/plugins/registrations-for-the-events-calendar/) | CVE-2021-24943 | 10,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/ba50c590-42ee-4523-8aa0-87ac644b77ed)  
282 | [registrations-for-the-events-calendar](https://wordpress.org/plugins/registrations-for-the-events-calendar/) | CVE-2021-25083 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/9b69544d-6a08-4757-901b-6ccf1cd00ecc)  
283 | [secure-copy-content-protection](https://wordpress.org/plugins/secure-copy-content-protection/) | CVE-2021-24931 | 10,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/1cd52d61-af75-43ed-9b99-b46c471c4231)  
284 | [send-pdf-for-contact-form-7](https://wordpress.org/plugins/send-pdf-for-contact-form-7/) | CVE-2024-3585 | 10,000 | Contact form data download | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/0646fcba-afe5-49a2-acd5-e15d009926c4)  
285 | [seraphinite-accelerator](https://wordpress.org/plugins/seraphinite-accelerator/) | CVE-2023-5609 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/aac4bcc8-b826-4165-aed3-f422dd178692)  
286 | [simple-basic-contact-form](https://wordpress.org/plugins/simple-basic-contact-form/) | CVE-2024-4150 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/simple-basic-contact-form/simple-basic-contact-form-20221201-reflected-cross-site-scripting)  
287 | [smart-forms](https://wordpress.org/plugins/smart-forms/) | CVE-2022-0163 | 10,000 | Downloading form data | [WPScan](https://wpscan.com/vulnerability/2b6b0731-4515-498a-82bd-d416f5885268)  
288 | [spider-event-calendar](https://wordpress.org/plugins/spider-event-calendar/) | CVE-2022-0212 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/15be2d2b-baa3-4845-82cf-3c351c695b47)  
289 | [ssl-zen](https://wordpress.org/plugins/ssl-zen/) | CVE-2024-1076 | 10,000 | SSL keys exposure | [WPScan](https://wpscan.com/vulnerability/9c3e9c72-3d6c-4e2c-bb8a-f4efce1371d5/)  
290 | [stopbadbots](https://wordpress.org/plugins/stopbadbots/) | CVE-2021-25070 | 10,000 | Blind SQL injection | [WPScan](https://wpscan.com/vulnerability/e00b2946-15e5-4458-9b13-2e272630a36f)  
291 | [swift-performance-lite](https://wordpress.org/plugins/swift-performance-lite/) | CVE-2023-6289 | 10,000 | Unauthorized configuration export | [WPScan](https://wpscan.com/vulnerability/8c83dd57-9291-4dfc-846d-5ad47534e2ad/)  
292 | [theme: graphene](https://wordpress.org/plugins/theme: graphene/) | CVE-2024-1984 | 10,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/graphene/graphene-29-missing-authorization)  
293 | [theme: newsmatic](https://wordpress.org/plugins/theme: newsmatic/) | CVE-2024-1587 | 10,000 | Draft post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/newsmatic/newsmatic-134-unauthenticated-information-exposure-via-newsmatic-filter-posts-load-tab-content)  
294 | [themify-shortcodes](https://wordpress.org/plugins/themify-shortcodes/) | CVE-2024-2732 | 10,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/themify-shortcodes/themify-shortcodes-208-authenticated-contributor-stored-cross-site-scripting)  
295 | [ultimate-product-catalogue](https://wordpress.org/plugins/ultimate-product-catalogue/) | CVE-2021-24993 | 10,000 | Possibility to add arbitrary products | [WPScan](https://wpscan.com/vulnerability/514416fa-d915-4953-bf1b-6dbf40b4d7e5)  
296 | [wa-sticky-buttons](https://wordpress.org/plugins/wa-sticky-buttons/) | CVE-2022-2375 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/caab1fca-cc6b-45bb-bd0d-f857edd8bb81)  
297 | [wassup](https://wordpress.org/plugins/wassup/) | CVE-2023-5653 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/76316621-1987-44ea-83e5-6ca884bdd1c0/)  
298 | [webpushr-web-push-notifications](https://wordpress.org/plugins/webpushr-web-push-notifications/) | CVE-2023-5620 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/a03330c2-3ae0-404d-a114-33b18cc47666/)  
299 | [whmcs-bridge](https://wordpress.org/plugins/whmcs-bridge/) | CVE-2021-25112 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/4aae2dd9-8d51-4633-91bc-ddb53ca3471c)  
300 | [wicked-folders](https://wordpress.org/plugins/wicked-folders/) | CVE-2021-24919 | 10,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/f472ec7d-765c-4266-ab9c-e2d06703ebb4)  
301 | [woo-orders-tracking](https://wordpress.org/plugins/woo-orders-tracking/) | CVE-2021-25062 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/dc9a5d36-7453-46a8-a17f-712449d7987d)  
302 | [woocommerce-exporter](https://wordpress.org/plugins/woocommerce-exporter/) | CVE-2022-0149 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/e47c288a-2ea3-4926-93cc-113867cbc77c)  
303 | [woocommerce-store-toolkit](https://wordpress.org/plugins/woocommerce-store-toolkit/) | CVE-2021-25077 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/53868650-aba0-4d07-89d2-a998bb0ee5f6)  
304 | [woostify-sites-library](https://wordpress.org/plugins/woostify-sites-library/) | CVE-2023-6279 | 10,000 | DoS | [WPScan](https://wpscan.com/vulnerability/626bbc7d-0d0f-4418-ac61-666278a1cbdb)  
305 | [word-balloon](https://wordpress.org/plugins/word-balloon/) | CVE-2023-5884 | 10,000 | CSRF avatar removal | [WPScan](https://wpscan.com/vulnerability/f4a7937c-6f4b-49dd-b88a-67ebe718ad19/)  
306 | [wp-booking-system](https://wordpress.org/plugins/wp-booking-system/) | CVE-2021-25061 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/bd9dc754-08a4-4bfc-8dda-3f5c0e070f7e)  
307 | [wp-coder](https://wordpress.org/plugins/wp-coder/) | CVE-2021-25053 | 10,000 | CSRF RCE | [WPScan](https://wpscan.com/vulnerability/a5448599-64de-43b0-b04d-c6492366eab1)  
308 | [wp-coder](https://wordpress.org/plugins/wp-coder/) | CVE-2022-2388 | 10,000 | CSRF code deletion | [WPScan](https://wpscan.com/vulnerability/50acd35f-eb31-4aba-bf32-b390e9514beb)  
309 | [wp-custom-widget-area](https://wordpress.org/plugins/wp-custom-widget-area/) | CVE-2023-6066 | 10,000 | Missing authorization | [WPScan](https://wpscan.com/vulnerability/f8f84d47-49aa-4258-a8a6-3de8e7342623)  
310 | [wp-marketing-automation](https://wordpress.org/plugins/wp-marketing-automation/) | CVE-2022-2387 | 10,000 | Adding automations | [WPScan](https://wpscan.com/vulnerability/e70f00b7-6251-476e-9297-60af509e6ad9)  
311 | [wp-photo-album-plus](https://wordpress.org/plugins/wp-photo-album-plus/) | CVE-2021-25115 | 10,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/dbc18c2c-7547-44fc-8a41-c819757e47a7)  
312 | [wp-popup-builder](https://wordpress.org/plugins/wp-popup-builder/) | CVE-2022-2404 | 10,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/0d889dde-b9d5-46cf-87d3-4f8a85cf9b98)  
313 | [wp-popup-builder](https://wordpress.org/plugins/wp-popup-builder/) | CVE-2022-2405 | 10,000 | Arbitrary popup deletion | [WPScan](https://wpscan.com/vulnerability/50037028-2790-47ee-aae1-faf0724eb917)  
314 | [wp-product-feed-manager](https://wordpress.org/plugins/wp-product-feed-manager/) | CVE-2024-3067 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-product-feed-manager/woocommerce-google-feed-manager-242-authenticated-admin-sql-injection-to-reflected-cross-site-scripting)  
315 | [wp125](https://wordpress.org/plugins/wp125/) | CVE-2021-25073 | 10,000 | CSRF ad deletion | [WPScan](https://wpscan.com/vulnerability/922a2037-9b5e-4c94-83d9-99efc494e9e2)  
316 | [wpcargo](https://wordpress.org/plugins/wpcargo/) | CVE-2021-25003 | 10,000 | RCE | [WPScan](https://wpscan.com/vulnerability/5c21ad35-b2fb-4a51-858f-8ffff685de4a)  
317 | [wpvr](https://wordpress.org/plugins/wpvr/) | CVE-2023-6529 | 10,000 | Plugin downgrade to Reflected/Stored XSS | [WPScan](https://wpscan.com/vulnerability/c36314c1-a2c0-4816-93c9-e61f9cf7f27a)  
318 | [yml-for-yandex-market](https://wordpress.org/plugins/yml-for-yandex-market/) | CVE-2024-1365 | 10,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/yml-for-yandex-market/yml-for-yandex-market-423-reflected-cross-site-scripting)  
319 | [analytics-insights](https://wordpress.org/plugins/analytics-insights/) | CVE-2024-0250 | 9,000 | Open Redirect | [WPScan](https://wpscan.com/vulnerability/321b07d1-692f-48e9-a8e5-a15b38efa979)  
320 | [cost-of-goods-for-woocommerce](https://wordpress.org/plugins/cost-of-goods-for-woocommerce/) | CVE-2024-0821 | 9,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/cost-of-goods-for-woocommerce/cost-of-goods-sold-cogs-cost-profit-calculator-for-woocommerce-328-reflected-cross-site-scripting)  
321 | [gdpr-cookie-consent](https://wordpress.org/plugins/gdpr-cookie-consent/) | CVE-2024-3599 | 9,000 | Unauthenticated arbitrary post deletion | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/gdpr-cookie-consent/wp-cookie-consent-for-gdpr-ccpa-eprivacy-302-missing-authorization-to-unauthenticated-arbitrary-post-deletion)  
322 | [gdpr-cookie-consent](https://wordpress.org/plugins/gdpr-cookie-consent/) | CVE-2024-4869 | 9,000 | Unauthenticated Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/507b2e65-987b-4d4a-8a99-5366048d925e)  
323 | [inline-google-spreadsheet-viewer](https://wordpress.org/plugins/inline-google-spreadsheet-viewer/) | CVE-2024-3674 | 9,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/523e80a5-dffa-4eb6-8f7a-e179e0dc4d28)  
324 | [media-library-plus](https://wordpress.org/plugins/media-library-plus/) | CVE-2024-3615 | 9,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/5f550bac-b047-4276-bde5-c15bfd4ceb49)  
325 | [motors-car-dealership-classified-listings.](https://wordpress.org/plugins/motors-car-dealership-classified-listings./) | CVE-2024-5545 | 9,000 | Hiding arbitrary posts from homepage | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/motors-car-dealership-classified-listings/motors-car-dealer-classifieds-listing-149-missing-authorization)  
326 | [rotatingtweets](https://wordpress.org/plugins/rotatingtweets/) | CVE-2024-5141 | 9,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/02cff893-4f41-4bb0-9fb0-344a3a8afa0b)  
327 | [slideshow-gallery](https://wordpress.org/plugins/slideshow-gallery/) | CVE-2024-5543 | 9,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/slideshow-gallery/slideshow-gallery-lite-181-authenticated-contributor-sql-injection)  
328 | [toolbar-extras](https://wordpress.org/plugins/toolbar-extras/) | CVE-2024-3611 | 9,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/50631f6c-de8b-408e-ab1f-ef74d3180e7f)  
329 | [videojs-html5-player](https://wordpress.org/plugins/videojs-html5-player/) | CVE-2024-5205 | 9,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/4ffd76a2-6700-4c2a-858d-4c7339a8d09a)  
330 | [woocommerce-catalog-enquiry](https://wordpress.org/plugins/woocommerce-catalog-enquiry/) | CVE-2023-5348 | 9,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/b37b09c1-1b53-471c-9b10-7d2d05ae11f1)  
331 | [wp-hotel-bookings](https://wordpress.org/plugins/wp-hotel-bookings/) | CVE-2023-5651 | 9,000 | Missing authorization | [WPScan](https://wpscan.com/vulnerability/a365c050-96ae-4266-aa87-850ee259ee2c/)  
332 | [wp-hotel-bookings](https://wordpress.org/plugins/wp-hotel-bookings/) | CVE-2023-5652 | 9,000 | SQL Injection | [WPScan](https://wpscan.com/vulnerability/8ea46b9a-5239-476b-949d-49546371eac1/)  
333 | [wp-hotel-bookings](https://wordpress.org/plugins/wp-hotel-bookings/) | CVE-2024-3605 | 9,000 | SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-hotel-booking/wp-hotel-booking-210-unauthenticated-sql-injection)  
334 | [wp-migration-duplicator](https://wordpress.org/plugins/wp-migration-duplicator/) | CVE-2024-3546 | 9,000 | Arbitrary .log file read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-migration-duplicator/wordpress-backup-migration-148-missing-authorization-to-directory-traversal)  
335 | [wp-sms](https://wordpress.org/plugins/wp-sms/) | CVE-2023-6980 | 9,000 | CSRF subscriber and group deletion | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-sms/wp-sms-65-cross-site-request-forgery-to-subscriber-deletion)  
336 | [wp-sms](https://wordpress.org/plugins/wp-sms/) | CVE-2023-6981 | 9,000 | SQL Injection leading to Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-sms/wp-sms-65-authenticated-admin-sql-injection-to-reflected-cross-site-scripting)  
337 | [erp](https://wordpress.org/plugins/erp/) | CVE-2024-0608 | 8,000 | SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/erp/wp-erp-complete-hr-solution-with-recruitment-job-listings-woocommerce-crm-accounting-1129-authenticated-subscriber-sql-injection)  
338 | [erp](https://wordpress.org/plugins/erp/) | CVE-2024-0609 | 8,000 | XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/erp/wp-erp-complete-hr-solution-with-recruitment-job-listings-woocommerce-crm-accounting-1129-unauthenticated-stored-cross-site-scripting)  
339 | [facebook-button-plugin](https://wordpress.org/plugins/facebook-button-plugin/) | CVE-2023-6250 | 8,000 | Password-protected post read | [WPScan](https://wpscan.com/vulnerability/6cad602b-7414-4867-8ae2-f0b846c4c8f0)  
340 | [icon-widget](https://wordpress.org/plugins/icon-widget/) | CVE-2024-1993 | 8,000 | Contributor+ stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/icon-widget/icon-widget-130-authenticatedcontributor-stored-cross-site-scripting-via-shortcode)  
341 | [json-content-importer](https://wordpress.org/plugins/json-content-importer/) | CVE-2023-6268 | 8,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/15b9ab48-c038-4f2e-b823-1e374baae985)  
342 | [kiwi-social-share](https://wordpress.org/plugins/kiwi-social-share/) | CVE-2024-3228 | 8,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/kiwi-social-share/social-sharing-plugin-kiwi-217-information-disclosure)  
343 | [mediavine-create](https://wordpress.org/plugins/mediavine-create/) | CVE-2024-1711 | 8,000 | SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/fcc78fa6-a5f0-4f29-ae19-8e783698b19e)  
344 | [stopbadbots](https://wordpress.org/plugins/stopbadbots/) | CVE-2024-4355 | 8,000 | Downloading request log (with IPs, user agents, …) | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/c77d94ae-528d-4525-b16d-96529bee08c0)  
345 | [wp-compress-image-optimizer](https://wordpress.org/plugins/wp-compress-image-optimizer/) | CVE-2023-6812 | 8,000 | Open Redirect | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-compress-image-optimizer/wp-compress-image-optimizer-all-in-one-62001-open-redirect-via-css)  
346 | [wp-compress-image-optimizer](https://wordpress.org/plugins/wp-compress-image-optimizer/) | CVE-2023-6699 | 8,000 | LFI | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-compress-image-optimizer/wp-compress-image-optimizer-all-in-one-61033-unauthenticated-directory-traversal-via-css)  
347 | [wp-migration-duplicator](https://wordpress.org/plugins/wp-migration-duplicator/) | CVE-2023-5738 | 8,000 | Stored XSS | [WPScan](https://wpscan.com/vulnerability/7f935916-9a1a-40c7-b6d8-efcc46eb8eaf/)  
348 | [wp-migration-duplicator](https://wordpress.org/plugins/wp-migration-duplicator/) | CVE-2023-5737 | 8,000 | Arbitrary settings update | [WPScan](https://wpscan.com/vulnerability/c761c67c-eab8-4e1b-a332-c9a45e22bb13/)  
349 | [wpc-composite-products](https://wordpress.org/plugins/wpc-composite-products/) | CVE-2024-2838 | 8,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wpc-composite-products/wpc-composite-products-for-woocommerce-727-authenticated-subscriber-stored-cross-site-scripting)  
350 | [armember-membership](https://wordpress.org/plugins/armember-membership/) | CVE-2024-4133 | 7,000 | Open Redirect | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/80d113aa-7401-4b58-a755-f64146d9fb08)  
351 | [calendar](https://wordpress.org/plugins/calendar/) | CVE-2024-2831 | 7,000 | Contributor+ SQL Injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/0886fa16-4292-4223-af01-9aa1f36490f7)  
352 | [estatik](https://wordpress.org/plugins/estatik/) | CVE-2023-6048 | 7,000 | DoS | [WPScan](https://wpscan.com/vulnerability/74cb07fe-fc82-472f-8c52-859c176d9e51)  
353 | [estatik](https://wordpress.org/plugins/estatik/) | CVE-2023-6049 | 7,000 | Object injection | [WPScan](https://wpscan.com/vulnerability/8cfd8c1f-2834-4a94-a3fa-c0cfbe78a8b7)  
354 | [events-made-easy](https://wordpress.org/plugins/events-made-easy/) | CVE-2021-25030 | 7,000 | SQL injection | [WPScan](https://wpscan.com/vulnerability/bc7058b1-ca93-4c45-9ced-7848c7ae4150)  
355 | [jm-twitter-cards](https://wordpress.org/plugins/jm-twitter-cards/) | CVE-2024-1769 | 7,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/jm-twitter-cards/jm-twitter-cards-12-information-exposure-via-meta-description)  
356 | [jquery-t-countdown-widget](https://wordpress.org/plugins/jquery-t-countdown-widget/) | CVE-2024-4783 | 7,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/jquery-t-countdown-widget/jquery-t-countdown-widget-2325-authenticated-contributor-stored-cross-site-scripting-via-tminus-shortcode)  
357 | [likebtn-like-button](https://wordpress.org/plugins/likebtn-like-button/) | CVE-2021-24945 | 7,000 | Sensitive data exposure | [WPScan](https://wpscan.com/vulnerability/d7618061-a7fa-4da4-9384-be19bc5e8548)  
358 | [likebtn-like-button](https://wordpress.org/plugins/likebtn-like-button/) | CVE-2022-0745 | 7,000 | Arbitrary e-mail sending | [WPScan](https://wpscan.com/vulnerability/180f8e87-1463-43bb-a901-80031127723a)  
359 | [list-categories](https://wordpress.org/plugins/list-categories/) | CVE-2024-4356 | 7,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/8e24306a-b741-4840-b238-e37138425bf8)  
360 | [mediavine-create](https://wordpress.org/plugins/mediavine-create/) | CVE-2024-5601 | 7,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/9d04d8c1-75c0-447c-a26a-c2724c0a6618)  
361 | [travelpayouts](https://wordpress.org/plugins/travelpayouts/) | CVE-2023-5932 | 7,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/16fbca64-cc35-455e-bfef-d1f28857f991/)  
362 | [woo-product-category-discount](https://wordpress.org/plugins/woo-product-category-discount/) | CVE-2024-0617 | 7,000 | arbitrary discount change | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/woo-product-category-discount/category-discount-woocommerce-412-missing-authorization-via-wpcd-save-discount)  
363 | [wp-email-users](https://wordpress.org/plugins/wp-email-users/) | CVE-2021-24959 | 7,000 | SQL injection + object injection | [WPScan](https://wpscan.com/vulnerability/0471d2e2-e759-468f-becd-0b062f00b435)  
364 | [wpupper-share-buttons](https://wordpress.org/plugins/wpupper-share-buttons/) | CVE-2024-4997 | 7,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wpupper-share-buttons/wpupper-share-buttons-343-missing-authorization)  
365 | [wpvivid-backup-mainwp](https://wordpress.org/plugins/wpvivid-backup-mainwp/) | CVE-2024-1383 | 7,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/2a8430ed-6aeb-46a3-8c42-59646845706e)  
366 | [country-state-city-auto-dropdown](https://wordpress.org/plugins/country-state-city-auto-dropdown/) | CVE-2024-3495 | 6,000 | Unauthenticated SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/17dcacaf-0e2a-4bef-b944-fb7e43d25777)  
367 | [easyjobs](https://wordpress.org/plugins/easyjobs/) | CVE-2023-6843 | 6,000 | Unauthorized settings change | [WPScan](https://wpscan.com/vulnerability/41508340-8caf-4dca-bd88-350b63b78ab0)  
368 | [export-wp-page-to-static-html](https://wordpress.org/plugins/export-wp-page-to-static-html/) | CVE-2024-3597 | 6,000 | Open Redirect | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/export-wp-page-to-static-html/export-wp-page-to-static-htmlcss-222-open-redirect)  
369 | [integrate-google-drive](https://wordpress.org/plugins/integrate-google-drive/) | CVE-2024-2086 | 6,000 | Missing authorization | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/integrate-google-drive/integrate-google-drive-138-missing-authorization-to-unauthenticated-settings-modification-and-export)  
370 | [order-delivery-date](https://wordpress.org/plugins/order-delivery-date/) | CVE-2024-0678 | 6,000 | Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/order-delivery-date/order-delivery-date-for-wp-e-commerce-12-unauthenticated-stored-cross-site-scripting)  
371 | [poll-maker](https://wordpress.org/plugins/poll-maker/) | CVE-2024-3600 | 6,000 | Unauthenticated Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/fec015e1-7f64-4917-a242-90bd1135f680)  
372 | [poll-maker](https://wordpress.org/plugins/poll-maker/) | CVE-2024-3601 | 6,000 | Obtaining all users’ e-mails | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/poll-maker/poll-maker-best-wordpress-poll-plugin-518-missing-authorization-to-unauthenticated-email-enumeration)  
373 | [responsive-vector-maps](https://wordpress.org/plugins/responsive-vector-maps/) | CVE-2021-24947 | 6,000 | Arbitrary file read | [WPScan](https://wpscan.com/vulnerability/c6bb12b1-6961-40bd-9110-edfa9ee41a18)  
374 | [theme: blossom-spa](https://wordpress.org/plugins/theme: blossom-spa/) | CVE-2024-2107 | 6,000 | Password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-themes/blossom-spa/blossom-spa-134-sensitive-information-exposure)  
375 | [travelpayouts](https://wordpress.org/plugins/travelpayouts/) | CVE-2024-0337 | 6,000 | Open Redirect | [WPScan](https://wpscan.com/vulnerability/2f17a274-8676-4f4e-989f-436030527890)  
376 | [woo-gift-cards-lite](https://wordpress.org/plugins/woo-gift-cards-lite/) | CVE-2024-1857 | 6,000 | Draft and password-protected post read | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/woo-gift-cards-lite/ultimate-gift-cards-for-woocommerce-create-redeem-manage-digital-gift-certificates-with-personalized-templates-266-missing-authorization-to-unauthenticated-information-exposure)  
377 | [wp-cafe](https://wordpress.org/plugins/wp-cafe/) | CVE-2024-5431 | 6,000 | Contributor+ LFI | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-cafe/wpcafe-online-food-ordering-restaurant-menu-delivery-and-reservations-for-woocommerce-2225-authenticated-contributor-file-inclusion-via-shortcode)  
378 | [wp-cafe](https://wordpress.org/plugins/wp-cafe/) | CVE-2024-5427 | 6,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-cafe/wpcafe-online-food-ordering-restaurant-menu-delivery-and-reservations-for-woocommerce-2224-authenticated-contributor-stored-cross-site-scripting-via-reservation-form-shortcode)  
379 | [advanced-schedule-posts](https://wordpress.org/plugins/advanced-schedule-posts/) | CVE-2024-0249 | 5,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/e7ee3e73-1086-421f-b586-d415a45a6c8e/)  
380 | [ari-cf7-connector](https://wordpress.org/plugins/ari-cf7-connector/) | CVE-2024-0239 | 5,000 | Reflected XSS | [WPScan](https://wpscan.com/vulnerability/b9a4a3e3-7cdd-4354-8541-4219bd41c854)  
381 | [auth0](https://wordpress.org/plugins/auth0/) | CVE-2023-6813 | 5,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/0c4e0d48-fde1-45dd-8e06-4582cf677579)  
382 | [button-generation](https://wordpress.org/plugins/button-generation/) | CVE-2021-25052 | 5,000 | CSRF RCE | [WPScan](https://wpscan.com/vulnerability/a01844a0-0c43-4d96-b738-57fe5bfbd67a)  
383 | [dashboard-widgets-suite](https://wordpress.org/plugins/dashboard-widgets-suite/) | CVE-2024-0979 | 5,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/cfe4d99c-9cbd-4255-8f90-f904313d46b4)  
384 | [easyazon](https://wordpress.org/plugins/easyazon/) | CVE-2023-6956 | 5,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/easyazon/easyazon-amazon-associates-affiliate-plugin-510-reflected-cross-site-scripting-via-easyazon-cloaking-locale)  
385 | [embedalbum-pro](https://wordpress.org/plugins/embedalbum-pro/) | CVE-2024-3984 | 5,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/6593b0de-db7a-4b7e-bd74-cc2b1e36ac60)  
386 | [testimonial-slider](https://wordpress.org/plugins/testimonial-slider/) | CVE-2024-4193 | 5,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/cd7ed687-4049-4957-86e9-b2f59621c747)  
387 | [ultimate-410](https://wordpress.org/plugins/ultimate-410/) | CVE-2024-3677 | 5,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/ultimate-410/ultimate-410-gone-status-code-114-authenticated-contributor-stored-cross-site-scripting)  
388 | [wp-e-commerce](https://wordpress.org/plugins/wp-e-commerce/) | CVE-2024-1516 | 5,000 | Unauthorized post insert | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-e-commerce/wp-ecommerce-3151-missing-authorization-to-unauthenticated-arbitrary-post-creation)  
389 | [wp-e-commerce](https://wordpress.org/plugins/wp-e-commerce/) | CVE-2024-1514 | 5,000 | SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-e-commerce/wp-ecommerce-3151-unauthenticated-sql-injection)  
390 | [wp-easycart](https://wordpress.org/plugins/wp-easycart/) | CVE-2024-3211 | 5,000 | Contributor+ Blind SQL injection | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-easycart/shopping-cart-ecommerce-store-563-authenticated-contributor-sql-injection)  
391 | [wp-job-manager-companies](https://wordpress.org/plugins/wp-job-manager-companies/) | CVE-2023-6978 | 5,000 | Reflected XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/e7a28382-facb-43a7-892a-8ca9e7f0f62b)  
392 | [wp-stateless](https://wordpress.org/plugins/wp-stateless/) | CVE-2024-1385 | 5,000 | DoS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/wp-stateless/wp-stateless-google-cloud-storage-340-missing-authorization-to-limited-arbitrary-options-update)  
393 | [wp-ultimate-post-grid](https://wordpress.org/plugins/wp-ultimate-post-grid/) | CVE-2024-4043 | 5,000 | Contributor+ Stored XSS | [Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/id/14e897f0-11e6-43b1-908c-be4ecdc7fd58)  
  
Not all of the vulnerabilities were found directly by the fuzzer. For example, [CVE-2021-25096](https://wpscan.com/vulnerability/e6dd140e-0c9d-41dc-821e-4910a13122c1) was found accidentally when writing a PoC for [CVE-2021-25095](https://wpscan.com/vulnerability/cbfa7211-ac1f-4cf2-bd79-ebce2fc4baa1). For some other vulnerabilities, the tool alerts were only part of the vulnerability information – for example, the tool notified that a WordPress option can get updated by any user - and finding the consequences (whether it can lead e.g. to stored XSS) required manual work.

## Findings worth mentioning

I won’t make fun of any particular plugin author, however, I think some findings are worth sharing.

### is_admin

The WordPress `is_admin()` function, as you may probably have guessed:

> Determines whether the current request is for an administrative interface page.

(from <https://developer.wordpress.org/reference/functions/is_admin/>)

The documentation warns as well, that it:

> Does not check if the user is an administrator; use `current_user_can()` for checking roles and capabilities.

As you may probably have guessed, it was a source of a couple of vulnerabilities in the form of:
  
  
  if (is_admin()) {
  /* dangerous action */
  }
  

### REST route URLs

Let’s consider the following code:
  
  
  register_rest_route((...), '/(...)/(?P<id>[\d]+)', array(
  array(
  'methods' => WP_REST_Server::READABLE,
  'callback' => array($this, 'callback'),
  'permission_callback' => '__return_true',
  ),
  ));
  
  /* ... */
  
  function callback($request) {
  $id = $request['id'];
  }
  

What ID values could be passed to the handler?

The correct answer is: all of them – just use `/?rest_route=/(...)/1&id=hehehe`.

### get_users()

Some plugins allow searching for users by providing a part of an e-mail address. That allows to leak any user’s e-mail using the following steps:

  * Bruteforcing the first letter of the domain name (searching for `@a`, `@b`, etc., and checking when the user’s name appears in search results).
  * Remembering the first letter and using it to guess the second letter. Let’s assume the user’s e-mail domain name starts with `g`. You can then brute force the second letter (`@ga`, `@gb`, …).
  * Repeating the above steps for the rest of the e-mail address.

Because of that, I have added a check that alerts when `get_users()` gets called. Unfortunately, besides finding vulnerabilities of this type, it led to numerous false positives as well.

### XSS protection

Don’t do the following:
  
  
  if (/* potential XSS in $parameter detected */) die('Invalid parameter: ' . $parameter);
  

Several XSS vulnerabilities were also caused by debugging helpers in the form of:
  
  
  echo "<!--";
  
  var_dump($_POST);
  
  echo "-->";
  

### CAPTCHA verification

Don’t do this:
  
  
  if (isset($_POST['captcha'])) {
  /* verify captcha */
  }
  
  /* do action that should be CAPTCHA-protected */
  

I have observed this pattern multiple times, both for CAPTCHAs and nonces.

## Conclusions

This was just a proof-of-concept to check whether automatic techniques are a viable method to find WordPress plugin bugs. I am sure it can be improved by e.g.:

  * adding checks to detect other types of dangerous operations,
  * attempting to decrease the number of false positives without a large loss of true positives. The percentage of false positives was one of the main obstacles in this project.

This technique can also be implemented for other plugin ecosystems.

Many of the vulnerabilities I found were easily preventable by modern software engineering practices. In many WordPress plugins, HTML is built using an error-prone pile of `echo` statements, instead of a template language. Similarly, AJAX endpoints are by default available for all logged-in users or all not logged-in users, instead of requiring the developer to provide a fixed allowlist of roles or permissions (so that they would have to explicitly mark a route as available to all logged-in users). Introducing techniques that make it harder to make mistakes and promoting their use is, unfortunately, something only the WordPress team, not plugin developers, can do.

## Footnotes

  1. In retrospect, using a pile of regular expressions to detect crashes in the output wasn’t the best idea. Now I would try to do this differently. ↩

  2. In retrospect, it is obvious that it doesn’t cover all ways to load XML. This should have been done differently. ↩

  3. This type of reflected XSS requires cookies to be sent with a POST request, therefore would be harder to exploit due to the SameSite-by-default behavior. ↩ ↩2 ↩3 ↩4 ↩5 ↩6 ↩7 ↩8

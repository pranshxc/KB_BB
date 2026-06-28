---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-21_playing-dominos-with-moodles-security-12.md
original_filename: 2023-08-21_playing-dominos-with-moodles-security-12.md
title: Playing Dominos with Moodle's Security (1/2)
category: documents
detected_topics:
- xss
- command-injection
- access-control
- ssrf
- path-traversal
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- access-control
- ssrf
- path-traversal
- automation-abuse
language: en
raw_sha256: 5d25d7fda7e9a88a19be19f16519d508fd30fde9438e65527c553981958c6f6c
text_sha256: af9c5d9f7e0b36dcd6d5021af89703e9ddcfba7885a8300bdb9bab01d787c247
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Playing Dominos with Moodle's Security (1/2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-21_playing-dominos-with-moodles-security-12.md
- Source Type: markdown
- Detected Topics: xss, command-injection, access-control, ssrf, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `5d25d7fda7e9a88a19be19f16519d508fd30fde9438e65527c553981958c6f6c`
- Text SHA256: `af9c5d9f7e0b36dcd6d5021af89703e9ddcfba7885a8300bdb9bab01d787c247`


## Content

---
title: "Playing Dominos with Moodle's Security (1/2)"
page_title: "Playing Dominos with Moodle's Security (1/2) | Sonar"
url: "https://www.sonarsource.com/blog/playing-dominos-with-moodles-security-1/"
final_url: "https://www.sonarsource.com/blog/playing-dominos-with-moodles-security-1/"
authors: ["Yaniv Nizry (@YNizry)"]
programs: ["Moodle"]
bugs: ["Stored XSS", "Arbitrary folder creation", "RCE", "Security code review"]
publication_date: "2023-08-21"
added_date: "2023-08-25"
source: "pentester.land/writeups.json"
original_index: 845
---

## TL;DR overview

  * Moodle versions before 4.1.3 and 4.2.0 contain an unauthenticated arbitrary folder creation vulnerability (CVE-2023-30943) that an attacker can leverage to trigger stored XSS in the administration panel.
  * The folder name created via the vulnerability is reflected unsanitized in the admin's HTML page, enabling JavaScript injection that executes when an admin visits the file type management page.
  * Because Moodle admins can install PHP plugins directly from the web interface, XSS in the admin context escalates immediately to arbitrary PHP code execution on the server—a full RCE chain from an unauthenticated starting point.
  * Moodle patched both CVEs promptly following responsible disclosure; the research illustrates how seemingly low-impact primitives become critical when combined with existing application features.

Moodle is an open-source learning management system (LMS) used to create and deliver online courses. It was first developed in 2002 by Martin Dougiamas and is now widely used by educators and institutions around the world, earning the trust of educational institutions worldwide, with its user base exceeding 350 million across 242 countries. 

  
Moodle provides a platform for teachers and trainers to create online courses and learning materials, manage course content, and interact with students through a range of communication tools such as discussion forums, messaging systems, and more.

Compromising a Moodle instance could considerably impact schools and universities. From simple grade cheating to infiltrating internal networks, shutting down a whole university, and more. An attacker can potentially cause significant harm to an educational institution.

This is the first blog in a two-part series where we will present our findings on a Moodle security audit we conducted. We were drawn to researching the security aspect of the framework due to its popularity, with the goal of contributing to a safer internet.  
  

In this first article, we demonstrate how an unauthenticated attacker can leverage a vulnerability with a supposedly low impact to gain full control over the Moodle instance.

## Impact

Moodle versions 4.1.x before 4.1.3 and 4.2.x before 4.2.0 are susceptible to an unauthenticated arbitrary folder creation, tracked as CVE-2023-30943. An attacker can leverage the creation of arbitrary folders to carry out a Stored Cross-Site Scripting (XSS) attack on the administration panel, resulting in arbitrary code execution on the server as soon as an administrator visits the panel.

## Technical Details

In this section, we discuss the origin of the vulnerability and how an attacker can turn an arbitrary folder creation into a Stored Cross-Site Scripting vulnerability and then execute arbitrary commands.

### Background

Like many other applications, Moodle has its own permission/authorization levels, using roles such as students, teachers, managers, etc. An administrator account can install arbitrary plugins (PHP code). This feature allows an administrator to execute code on the server by design.

By default, the register feature is disabled on Moodle: this is mainly because schools usually don't want random people to register and login into their Moodle, but only their students. For example, only after a student is accepted by a university, they will manually create a Moodle user and provide the student with their login credentials. 

### From arbitrary folder creation to RCE (CVE-2023-30943)

Although the attack surface for an unauthenticated attacker is minimal, we found two interesting endpoints that do not require authentication.

Both of the following endpoints take a `RAW` typed input from the `rev` parameter and generate a custom path that includes the provided `rev` parameter in the middle. Later, a folder will be created on this path if it doesn't exist. Since the parameter type is `RAW` (no modification or sanitization by Moodle) and its value is inserted in the middle of the path string, an attacker can create arbitrary folders on the server by using path traversal sequences. Without control over any files (names, paths, nor data) the impact of this weird bug is questionable at first glance. 

  * `lib/editor/tiny/lang.php`

Copy to clipboard
  
  
  $rev  = min_optional_param('rev', 0, 'RAW');
  $lang = min_optional_param('lang', 'standard', 'SAFEDIR');
  //...
  $this->candidatefile = "{$CFG->localcachedir}/editor_tiny/{$this->rev}/lang/{$this->lang}/lang.json";
  //...
  @mkdir(dirname($this->candidatefile), $CFG->directorypermissions, true);
  //...

  * `lib/editor/tiny/loader.php`

Copy to clipboard
  
  
  $this->rev  = min_optional_param('rev', 0, 'RAW');
  $this->filepath = min_optional_param('filepath', 'standard', 'SAFEPATH');
  //...
  $this->candidatefile = "{$CFG->localcachedir}/editor_tiny/{$this->rev}/{$filepathhash}";
  //...
  @mkdir(dirname($this->candidatefile), $CFG->directorypermissions, true);
  //...

In order to determine ways, how this could be exploited, we can assume that any folder name on the server is equivalent to an attacker’s input. From here we can go over all PHP code, that interacts with folders/files and consider them as sources. 

  
Some of the PHP functions, which should be considered for example:

  * `glob`
  * `*dir (scandir/opendir/readdir/closedir)`
  * `realpath`
  * `…`

Using this approach, we encountered an interesting code flow. When an admin visits the site administration page the following code is executed:  
`lib/adminlib.php`

Copy to clipboard
  
  
  foreach (glob($CFG->dirroot.'/'.$CFG->admin.'/settings/*.php') as $file) {
  if ($file == $CFG->dirroot.'/'.$CFG->admin.'/settings/top.php') {
  continue;
  }
  if ($file == $CFG->dirroot.'/'.$CFG->admin.'/settings/plugins.php') {
  // plugins are loaded last - they may insert pages anywhere
  continue;
  }
  require($file);
  }

The loop iterates over every file that ends with `.php` in the `admin/settings` and tries to `require` it. An attacker can simply add a folder that ends with`.php` at `/var/www/html/admin/settings/*.php` and crash all administration pages. 

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6973b581-e1d4-4c72-ac59-8ba624786c9e/moodle-admin-dashboard-dos.png)

This attack on the admin panel is limited to a Denial of Service (DoS), but we were curious, if attackers may even gain RCE.

#### XSS from arbitrary folder creation

Moodle offers methods for teachers and students to share learning materials and submissions, which could be in the form of files like word-processed documents or slideshow presentations. By default, Moodle supports a number of file types. An administrator can [add](https://docs.moodle.org/402/en/Working_with_files#Adding_a_new_file_type) other file types to their Moodle instance. Doing so requires choosing a corresponding icon that will represent the file type. 

  
The code at `admin/tool/filetypes/classes/utils.php` lists the available icons by iterating over the files (**including folders**) that end with `.svg`/`.gif`/`.png` in a dedicated path: 

Copy to clipboard
  
  
  public static function get_icons_from_path($path) {
  $icons = array();
  if ($handle = @opendir($path)) {
  while (($file = readdir($handle)) !== false) {
  $matches = array();
  if (preg_match('~(.+?)(?:-24|-32|-48|-64|-72|-80|-96|-128|-256)?\.(?:svg|gif|png)$~',
  $file, $matches)) {
  $key = $matches[1];
  $icons[$key] = $key;
  }
  }
  closedir($handle);
  }
  ksort($icons);
  return $icons;
  }

The name of the files/folders are displayed on the page without sanitization (`admin/tool/filetypes/edit_form.php`):

Copy to clipboard
  
  
  $fileicons = \tool_filetypes\utils::get_file_icons();
  $mform->addElement('select', 'icon', get_string('icon', 'tool_filetypes'), $fileicons);

In order to inject malicious JavaScript code, an attacker can create the following folder:

`var/www/html/pix/f/<input><img src=x onerror=alert(1)>.png `

When an admin tries to add a new filetype from the server settings page ([http://moodle-domain/admin/tool/filetypes/edit.php?name=add](http://localhost/admin/tool/filetypes/edit.php?name=add)), the folder name is reflected on the HTML page, and the JavaScript payload is executed in the context of the admin account. Because the folder name is reflected inside a `select` tag the attacker needs an `input` tag first to [break out](https://html.spec.whatwg.org/#parsing-main-inselect), causing the `img` to render and JavaScript to run. This vulnerability can be exploited in a Cross-Site Scripting (XSS) attack against an admin user to achieve remote code execution on the server, as [demonstrated](https://cube01.io/blog/Moodle-DOM-Stored-XSS-to-RCE.html) before via plugin installation. 

[Plugins](https://docs.moodle.org/402/en/Installing_plugins) in Moodle are additional PHP code made to provide custom features and functionalities. Using Moodle’s web interface, admins can conveniently install user [shared](https://moodle.org/plugins/) plugins, or install their own from a local zip. Since plugins are simply PHP code, an attacker-controlled plugin is equivalent to arbitrary code execution.

There are probably other ways to exploit this vulnerability, but this XSS on the “new filetype” page demonstrates how an unauthenticated attacker can execute arbitrary code on the Moodle server by installing a malicious plugin.

### Patch

The vulnerability was [fixed](https://github.com/moodle/moodle/commit/59d42e1ed23f916dcb47d53c745bef18a116d800) in versions 4.1.3 and 4.2.0 by casting the `$rev` parameter to integers in both files:

Copy to clipboard
  
  
  [$rev, $lang] = explode('/', $slashargument, 2);
  -  $rev  = min_clean_param($rev, 'RAW');
  +  $rev  = min_clean_param($rev, 'INT');
  $lang = min_clean_param($lang, 'SAFEDIR');
  } else {
  -  $rev  = min_optional_param('rev', 0, 'RAW');
  +  $rev  = min_optional_param('rev', 0, 'INT');
  $lang = min_optional_param('lang', 'standard', 'SAFEDIR');
  }

Copy to clipboard
  
  
  [$rev, $filepath] = explode('/', $slashargument, 2);
  -  $this->rev  = min_clean_param($rev, 'RAW');
  +  $this->rev  = min_clean_param($rev, 'INT');
  $this->filepath = min_clean_param($filepath, 'SAFEPATH');
  } else {
  -  $this->rev  = min_optional_param('rev', 0, 'RAW');
  +  $this->rev  = min_optional_param('rev', 0, 'INT');
  $this->filepath = min_optional_param('filepath', 'standard', 'SAFEPATH');
  }

Now, an attacker cannot control the name of a folder nor traverse back directories in order to create arbitrary folders on the server.

## Timeline

**Date**| **Action**  
---|---  
2023-03-22| We report all issues to Vendor  
2023-04-19| Vendor patched the vulnerability  
2023-05-01| Vendor released security advisory and CVE-2023-30943 was assigned  
  
## Summary

In this article, we showed how an unauthenticated actor could create an arbitrary folder on a Moodle server, an apparently innocuous action, to then trigger a Cross-Site Scripting vulnerability on the administration panel. With existing features of Moodle, this primitive can be turned into Remote Code Execution, ultimately granting an unauthenticated attacker arbitrary code execution on the server. 

In the second article coming on August 29th, we will dive into how attackers could take over accounts by chaining minor vulnerabilities.

We would also like to thank Moodle for their responsiveness and great communication.

## Related Blog Posts

  * [WordPress 5.8.2 Stored XSS Vulnerability](https://www.sonarsource.com/blog/wordpress-stored-xss-vulnerability/)
  * [Magento 2.3.1: Unauthenticated Stored XSS to RCE](https://www.sonarsource.com/blog/magento-rce-via-xss/)
  * [SmartStoreNET - Malicious Message leading to E-Commerce Takeover](https://www.sonarsource.com/blog/smartstorenet-malicious-message-leading-to-e-commerce-takeover/)
  * [Odoo: Get your Content Type right, or else!](https://www.sonarsource.com/blog/odoo-get-your-content-type-right-or-else/)

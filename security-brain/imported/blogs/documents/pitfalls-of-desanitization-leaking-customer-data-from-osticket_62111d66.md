---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-06_pitfalls-of-desanitization-leaking-customer-data-from-osticket.md
original_filename: 2024-02-06_pitfalls-of-desanitization-leaking-customer-data-from-osticket.md
title: 'Pitfalls of Desanitization: Leaking Customer Data from osTicket'
category: documents
detected_topics:
- xss
- sqli
- command-injection
- password-reset
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- command-injection
- password-reset
- otp
- automation-abuse
language: en
raw_sha256: 62111d66c2b79b3e6d019d56b3433a43ec89c522d7040968a6800ff95c7da334
text_sha256: f09d0fd8c420ff096346fd8b08b705589d1135ffd262ed76948c36e23e0a4a7a
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Pitfalls of Desanitization: Leaking Customer Data from osTicket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-06_pitfalls-of-desanitization-leaking-customer-data-from-osticket.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, password-reset, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `62111d66c2b79b3e6d019d56b3433a43ec89c522d7040968a6800ff95c7da334`
- Text SHA256: `f09d0fd8c420ff096346fd8b08b705589d1135ffd262ed76948c36e23e0a4a7a`


## Content

---
title: "Pitfalls of Desanitization: Leaking Customer Data from osTicket"
page_title: "Pitfalls of Desanitization: Leaking Customer Data from osTicket | Sonar"
url: "https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/"
final_url: "https://www.sonarsource.com/blog/pitfalls-of-desanitization-leaking-customer-data-from-osticket/"
authors: ["Oskar Zeino-Mahmalat"]
programs: ["Enhancesoft (osTicket)"]
bugs: ["Stored XSS", "Security code review"]
publication_date: "2024-02-06"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 448
---

## TL;DR overview

  * osTicket leaks customer data through a desanitization vulnerability: the server sanitizes HTML input correctly, but then re-processes the sanitized output in a way that re-introduces XSS vectors before they reach the browser.
  * Desanitization occurs when code modifies a sanitizer's output—applying HTML entity decoding, template substitution, or string manipulation—that inadvertently restores dangerous characters the sanitizer had neutralized.
  * The resulting XSS allows attackers to steal support ticket data, impersonate agents, or take over customer accounts by injecting script that executes in the victim's browser session.
  * Developers should treat sanitizer output as immutable: any transformation applied after sanitization must be analyzed to confirm it does not re-introduce injection vectors.

As part of our continuous effort to improve our Code Quality technology and the security of the open-source ecosystem, our R&D team is always on the lookout for new 0-day security vulnerabilities in prominent software.

During our research, we repeatedly come across a dangerous coding pattern we call _Desanitization_ : An issue where potentially dangerous user input is sanitized, and then changed afterward in a way that negates the sanitization, making the input dangerous again. The pattern led to numerous impactful XSS vulnerabilities we uncovered, e.g. a [WordPress RCE bug chain](https://www.sonarsource.com/blog/wordpress-csrf-to-rce/).

We found the issue again in osTicket, where it led to a Cross-Site Scripting (XSS) vulnerability. [osTicket](https://osticket.com/) is an open-source helpdesk software that companies can use to provide solutions to customers seeking help. By default, anyone can create a ticket about a problem without needing an account. Employees with staff member accounts can then view and answer tickets. osTicket can be an interesting target for attackers, as customers or staff members might write about sensitive data like credentials or personal identifiable information.

In this blog post, we first explain the theory of the common Desanitization pattern. We then showcase what the pattern looks like in practice using the XSS vulnerability we found in osTicket which could be used to leak customer data.

## Impact

**osTicket v1.18 and osTicket before v1.17.4** contain a **Stored** **Cross-Site Scripting (XSS)** vulnerability ([CVE-2023-46967](https://nvd.nist.gov/vuln/detail/CVE-2023-46967)).

  
An unauthenticated attacker can create a malicious ticket with an XSS payload. When an authenticated staff member of the osTicket instance views the ticket, the payload executes. The attacker can use this to **leak tickets** of other customers potentially containing **sensitive data**. Additionally, the attacker can **fully** **take over the staff member's account** with a password reset email sent to the attacker's email address, allowing them to impersonate the victim. A support system compromise can have serious consequences for customers: Think of the [Okta hack last year](https://techcrunch.com/2023/10/20/okta-says-hackers-stole-customer-access-tokens-from-support-unit/) that rippled out to [Cloudflare and 1Password](https://techcrunch.com/2023/10/24/oktas-latest-hack-fallout-hits-cloudflare-1password/) because of leaked access tokens.

The vulnerability is **fixed** in osTicket versions [**v1.18.1**](https://github.com/osTicket/osTicket/releases/tag/v1.18.1) and [**v1.17.5**](https://github.com/osTicket/osTicket/releases/tag/v1.17.5).

## The Desanitization pattern

Before looking at the XSS vulnerability in osTicket and how to exploit it to leak customers' tickets, we want to explain the common and dangerous coding pattern that led to the XSS vulnerability: _Desanitization_.

XSS vulnerabilities are injection vulnerabilities: user input has to end up in a dangerous sink that renders HTML without sufficient encoding or sanitization. An abstract way of protecting against injection vulnerabilities looks like this: The `userInput` is processed and modified in some way, then sanitized, and finally used.

Copy to clipboard
  
  
  data = modify(userInput);
  data = sanitize(data);
  use(data);

A concrete example of this pattern is protecting against client-side XSS using DOMPurify:

Copy to clipboard
  
  
  userInput = '<div class="foo"><img src onerror=alert(1)>';
  
  // (1) modify
  data = data.replace(/class=".*?"/, 'class="custom-class" ');
  // <div class="custom-class"><img src onerror=alert(1)>
  
  // (2) sanitize
  data = DOMPurify.sanitize(userInput);
  // <div class="custom-class"><img src=""></div>
  
  // (3) use
  document.body.innerHTML = data; // safe

This approach is only safe as long as the order of operations stays like this. Swapping the order to sanitize and then modify results in the dangerous Desanitization pattern.

Copy to clipboard
  
  
  data = sanitize(userInput);
  data = modify(data);
  use(data);

Why is this dangerous? Because the modifications can break the assumptions of the sanitizer and reintroduce injection payloads into a context where they are executed. This desanitizes the data. Let's illustrate this again with a toy XSS example.

Copy to clipboard
  
  
  userInput = 'class=" <div id="<img src onerror=alert(1)>">';
  
  // (1) sanitize
  data = DOMPurify.sanitize(userInput);
  // class=" <div id="<img src onerror=alert(1)>"></div>
  
  // (2) modify
  data = data.replace(/class=".*?"/, 'class="custom-class" ');
  // class="custom-class"<img src onerror=alert(1)>"></div>
  
  // (3) use
  document.body.innerHTML = data; // triggers alert(1)

DOMPurify sees a harmless `<div>` tag with an `id` attribute and leaves it intact after sanitization. The modification afterward naively removes the opening `<div` tag. In doing so, the context of the malicious `<img>` is changed from an attribute to a tag. This breaks the assumption of the sanitizer about the attribute context being harmless, as the payload is moved out of the attribute context. In the end, an alert is triggered.

Desanitization happens because of a false assumption: "I have already sanitized my data, now I am safe and can implement features." But unfortunately, the order of operations matters. As a rule of thumb, modifying a sanitizer’s output should be avoided and considered dangerous, regardless of how benign the modification might be. It can always lead to Desanitization in unexpected and subtle ways. To avoid Desanitization, we recommend making sure that sanitization is the very last step before data is used. 

This issue also goes beyond XSS: it can show up anytime when data is sanitized, modified, and then interpreted by another component that reparses the data. For example, think of SQL Injection (SQLi): An old way to protect against it was escaping single quotes and other special characters in the user input. Modifying the escaped data afterward could mess with the escaping and lead to SQLi. While SQLi can be avoided by fixing the order of operations, the best way to do it is to avoid reparsing altogether with parameterized queries. 

We found Desanitization to be a common cause of vulnerabilities. The pattern was part of a [Wordpress RCE bugchain](https://www.sonarsource.com/blog/wordpress-csrf-to-rce/) we discovered, it allowed us to potentially steal emails from [Proton Mail](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/), [Zimbra](https://www.sonarsource.com/blog/zimbra-webmail-compromise-via-email/), [Tutanota](https://www.sonarsource.com/blog/remote-code-execution-in-tutanota-desktop-due-to-code-flaw/), and [more](https://www.sonarsource.com/blog/magento-rce-via-xss/). We showcased multiple of these vulnerabilities in the talk [A Common Bypass Pattern To Exploit Modern Web Apps](https://www.youtube.com/watch?v=V-DdcKADnFk) at Insomni'hack 2022. 

In the next section, we go from theory to practice by looking at a Desanitization vulnerability in osTicket. We explain how a small modification after the sanitization of user-submitted HTML leads to XSS in multiple locations of osTicket.

## Desanitization in osTicket's Format::sanitize function leads to XSS (CVE-2023-46967)

osTicket is a typical support software written in core PHP. It allows customers to create support tickets asking for help and staff members to view and reply to those tickets. Users can submit tickets on the website or directly via email with rich text formatting enabled.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/b755ce77-81ad-4e97-8289-221f88713045/Screenshot%202024-02-06%20at%2016-02-09%20Ticket%20%23750539.png)

Rich text benefits clear communication between the users seeking help and staff members but also comes at the risk of XSS. As such, it cleans up the user's HTML tickets on the server by sending all HTML user input through a sanitizer function `Format::sanitize()`. This server-side HTML sanitizer is used in many different places in osTicket where user-controlled HTML is rendered.

This function passes the user input from the `$text` parameter into `Format::safe_html()` for sanitization. `Format::safe_html()` is a wrapper around the [htmLawed library](https://www.bioinformatics.org/phplabware/internal_utilities/htmLawed/). This library claims to clean up broken HTML and filter against XSS attacks. `Format::localizeInlineImages()` takes the now safe HTML string and transforms the `src` attribute of all images to a different format. After that, the transformed HTML is returned to be rendered by the browser. 

Copy to clipboard
  
  
  static function sanitize($text, $striptags=false, $spec=false) {
  // (1) sanitize
  $text = Format::safe_html($text, array('spec' => $spec));
  // (2) modify
  $text = self::localizeInlineImages($text);
  // ...
  return $text;
  }

Looking at this code, the Desanitization pattern immediately jumps out, as the sanitization and modification are in the wrong order and directly next to each other. So we went through both steps to search for bugs in the sanitization itself and Desanitization bugs. After investigating the htmLawed library and how it was configured, we could not find issues in the sanitization. So we assumed that it was safe and proceeded with the rest of `Format::sanitize()`.

What is `Format::localizeInlineImages()` doing exactly with the sanitized input? Looking at its code, we find a regex that replaces specifically formatted `http(s):` URLs inside `src` attributes with `cid:` URLs. Content ID URLs (`cid:`) usually represent inline images in emails, but osTicket also uses them to map attachments to tickets internally.

Copy to clipboard
  
  
  static function localizeInlineImages($text) {
  return preg_replace(
  '`src="(?:https?:/)?(?:/[^/"]+)*?/file\\.php\\?(?:\w+=[^&]+&(?:amp;)?)*?key=([^&]+)[^"]*`',
  'src="cid:$1', $text);
  }

The regex tries to match a `src` attribute containing a URL with a `/file.php` path and a `key` query parameter. For example, the following input matches the regex and gets replaced by the string below:

Copy to clipboard
  
  
  src="/file.php?param=value&key=cid-value
  
  src="cid:cid-value

The attribute parsing performed by this regex is, unfortunately, flawed. The regex contains a negative character class that can match unlimited characters that are not ampersands (`&`). This includes the double quote character `"`, which is used to mark the end of the `src` attribute. It also includes the angle brackets `<` and `>`.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c0855ca2-d2f0-4507-aa21-04ebe03cea22/osTicket%20-%20regex.png)

The characters matched by this character class are not part of the replacement and are deleted. This can lead to plain text outside of an HTML element becoming an attribute of the element when the closing bracket `>` of the element is deleted by the regex replace. This violates the assumptions of the htmLawed sanitizer, which does not clean up plain text. This makes the transformation a classic case of Desanitization because special characters could be removed in an unbalanced way, unintentionally changing the structure of the HTML.

### Exploitation

How can this be abused? In this example, everything after `>` is considered plain text and not changed by the sanitization. The marked part is matched by the negative character class from before. In the replacement, this removes the `>`. All the plain text after `&key=cid-value"`, including `onerror=alert(1)`, is now part of the `<img>` element. Browsers ignore that the closing angle bracket of `<img>` is now missing and still renders the element, leading to XSS.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/b0f3e36d-d63b-4482-b918-8c17dac303d4/osTicket%20-%20regex%20replace.png)

The above example is not enough to trigger the XSS vulnerability. This is because other parts of the osTicket codebase transform the HTML even further. The `src` attributes of images are converted from `cid:` back to `https:`, and images without valid `src` attributes are deleted afterward. But the vulnerable regex modification includes `src=` at the start, so we do not need to use an `<img>` tag. Any element that can have a `src` attribute works. We cannot use any random element, as htmLawed checks if attributes are expected on an element or not. For example, a `src` attribute on a `<div>` element is removed.

Going through the htmLawed's mapping of HTML elements to attributes, we discovered the `<track>` element. `<track>` elements are usually used inside of `<video>` or `<audio>` to attach a subtitle track. A `src` attribute is used for this, just what we need. Normally, htmLawed would remove `<track>` if it is outside of the expected `<video>` or `<audio>` element, but osTicket disabled this check in the htmLawed configuration. 

Unfortunately, a simple `onerror` does not work for `<track>`. It only tries to load its `src` \- which can fail and trigger `onerror` \- when it is inside `<audio>` or `<video>`. And both of these are blocked by htmLawed! Remember, we can only add bad attributes to valid tags that passed sanitization, not arbitrary ones.

XSS connoisseurs might know that there are other juicy event handlers out there than just `onerror`. [Portswigger's XSS cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet) is an excellent resource for exploring and filtering them for your conditions. With this, we found `onanimationstart`. This event handler fires whenever an animation on the element starts. We can add an existing animation from osTicket's stylesheets to the `<track>` element inside a `style` attribute, which is allowed by the sanitizer. Here is our final working payload before and after being desanitized.

Copy to clipboard
  
  
  <track style="animation-name:progress-bar-stripes;" src="/file.php?param=value"> &key=foo" onanimationstart="alert(origin)" text
  
  <track style="animation-name:progress-bar-stripes" src="cid:foo" onanimationstart="alert(origin)" text

An attacker can submit a payload like this as a ticket to an osTicket instance to leak other tickets with sensitive customer data as soon as a staff member looks at the ticket. The attacker can also take over the staff member's account by changing their email address to an attacker-controlled one and requesting a password reset. An attacker with staff member access can abuse the same vulnerability in other locations on internal pages to target administrative users, who might not look at tickets. They could also use the gained staff member access to trick users seeking help into installing remote access software to run malicious commands on the user's computer. 

### Patch

The osTicket maintainer Enhancesoft chose to follow our recommendation for protecting against Desanitization: Never modify data after sanitization. They swapped the order of the modifying ``Format::localizeInlineImages()` and the sanitizing `Format::safe_html()` calls. They additionally hardened the regex that replaces URLs so that it only matches `<img>` tags.

Copy to clipboard
  
  
  static function sanitize($text, $striptags=false, $spec=false) {
  +  // Localize inline images before sanitizing content
  +  $text = self::localizeInlineImages($text);
  
  //balance and neutralize unsafe tags.
  $text = Format::safe_html($text, array('spec' => $spec));
  
  -  $text = self::localizeInlineImages($text);
  -
  //If requested - strip tags with decoding disabled.
  return $striptags?Format::striptags($text, false):$text;
  }

## Timeline

**Date**| **Action**  
---|---  
2023-07-31| We reported all issues to Enhancesoft  
2023-07-31| Enhancesoft acknowledged the report  
2023-08-07| Enhancesoft replicated the issue and suggested a patch  
2023-10-25| Enhancesoft released patched versions v1.18.1 and v1.17.5  
  
## Summary

This blog post introduced the concept of the dangerous Desanitization pattern: data is modified after sanitization, desanitizing it and making it dangerous again. We showed that the pattern often leads to critical vulnerabilities and gave an in-depth example of that with the XSS vulnerability in osTicket. Kudos to the maintainer Enhancesoft for the pleasant communication during disclosure! 

To protect your code against Desanitization, you can follow the Intentionality attribute of Code Quality: You intend to only use sanitized data for rendering HTML, so you sanitize last after modifications, keeping the data clean.

## Related Blog Posts

  * [WordPress 5.1 CSRF to Remote Code Execution](https://www.sonarsource.com/blog/wordpress-csrf-to-rce/)
  * [Code Vulnerabilities Put Proton Mails at Risk](https://www.sonarsource.com/blog/code-vulnerabilities-leak-emails-in-proton-mail/)
  * [Zimbra 8.8.15 - Webmail Compromise via Email](https://www.sonarsource.com/blog/zimbra-webmail-compromise-via-email/)
  * [Magento 2.3.1: Unauthenticated Stored XSS to RCE](https://www.sonarsource.com/blog/magento-rce-via-xss/)
  * [Remote Code Execution in Tutanota Desktop due to Code Flaw](https://www.sonarsource.com/blog/remote-code-execution-in-tutanota-desktop-due-to-code-flaw/)

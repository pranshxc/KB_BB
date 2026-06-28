---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-27_pre-auth-rce-in-moodle-part-i-php-object-injection-in-shibboleth.md
original_filename: 2021-07-27_pre-auth-rce-in-moodle-part-i-php-object-injection-in-shibboleth.md
title: Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth
category: documents
detected_topics:
- command-injection
- sso
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- supply-chain
language: en
raw_sha256: 6b491a8f6501a45101f8035a11b64b9d03e80df5a8a8a9aa1447f8b7fa990b05
text_sha256: c3b1739f1d147060e4477e5153559648d27e54f0d8a60ba46db4cfa41839395a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-27_pre-auth-rce-in-moodle-part-i-php-object-injection-in-shibboleth.md
- Source Type: markdown
- Detected Topics: command-injection, sso, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6b491a8f6501a45101f8035a11b64b9d03e80df5a8a8a9aa1447f8b7fa990b05`
- Text SHA256: `c3b1739f1d147060e4477e5153559648d27e54f0d8a60ba46db4cfa41839395a`


## Content

---
title: "Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth"
page_title: "Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth Module · Haxolot.com"
url: "https://haxolot.com/posts/2021/moodle_pre_auth_shibboleth_rce_part1/"
final_url: "https://haxolot.com/posts/2021/moodle_pre_auth_shibboleth_rce_part1/"
authors: ["Johannes Moritz", "Robin Peraglie"]
programs: ["Moodle"]
bugs: ["RCE", "PHP object injection"]
publication_date: "2021-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3471
---

# Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth Module

__ July 27, 2021  __5-minute read

__[Robin Peraglie](/authors/robin-peraglie/) • [Johannes Moritz](/authors/johannes-moritz/)

__[Pre-Auth](/tags/pre-auth/) • [Moodle](/tags/moodle/) • [RCE](/tags/rce/) • [Shibboleth](/tags/shibboleth/) • [POI](/tags/poi/)

Title

Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth Module 

Product

Moodle 

Vulnerable Version

3.11, 3.10 to 3.10.4, 3.9 to 3.9.7 and earlier unsupported versions 

Fixed Version

>= 3.11.1, 3.10.5 and 3.9.8 

Impact

Critical 

CVE Number

[CVE-2021-36394](https://nvd.nist.gov/vuln/detail/CVE-2021-36394)

It was found that the Shibboleth authentication module of Moodle suffers from a beautiful Remote Code Execution vulnerability from the unauthenticated perspective. This is widely used among universities to allow students from one university to authenticate against other universities allowing them to attend external courses and have fiddling fun with others.

A similar joy is sparked by the Remote Code Execution vulnerability that is actually located within the Logout functionality that can be invoked via SOAP. The function `LogoutNotification` invalidates sessions in different ways, depending on the deployed session manager used by Moodle:
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  function LogoutNotification($spsessionid) {
  $sessionclass = \core\session\manager::get_handler_class();
  switch ($sessionclass) {
  case '\core\session\file':
  return \auth_shibboleth\helper::logout_file_session($spsessionid);
  
  
---|---  
  
If the sessions are - as per default config - stored on the filesystem (via `\core\session\file`) every session will be stored in an individual file on the fileystem. We will now see how a Remote Code Execution can be utilized with the help of this session manager via a PHP Object Injection vulnerability.

## PHP Object Injection via File Sessions

First lets inspect the Remote Code Execution vulnerability by diving into the respective logout handler implemented in the `logout_file_session` function:
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  29
  30
  31
  

| 
  
  
  public static function logout_file_session($spsessionid) {
  global $CFG;
  
  if (!empty($CFG->session_file_save_path)) {
  $dir = $CFG->session_file_save_path;
  } else {
  $dir = $CFG->dataroot . '/sessions';
  }
  
  if (is_dir($dir)) {
  if ($dh = opendir($dir)) {
  // Read all session files.
  while (($file = readdir($dh)) !== false) {
  // Check if it is a file.
  if (is_file($dir.'/'.$file)) {
  // Read session file data.
  $data = file($dir.'/'.$file);
  if (isset($data[0])) {
  $usersession = self::unserializesession($data[0]);
  // Check if we have found session that shall be deleted.
  if (isset($usersession['SESSION']) && 
  isset($usersession['SESSION']->shibboleth_session_id)) {
  // If there is a match, delete file.
  if ($usersession['SESSION']->shibboleth_session_id == $spsessionid) {
  // Delete session file.
  if (!unlink($dir.'/'.$file)) {
  return new SoapFault('LogoutError', 
  'Could not delete Moodle session file.');
  }
  [...]
  }
  
  
---|---  
  
It can be observed that the file handler traverses all session files. Each session file holds a single serialized session object. The handler copes for that, by reading every file and deserializing its contents with the `unserializesession` function. Once a matching session ID was found in a session object it’s related file is `unlink`‘ed resulting in a logged out session.

PHPs default internal serialization format for storing sessions looks slightly different than the intuitive `serialize($_SESSION)`. Due to legacy reasons, it is a sequence of the session objects keys glued to their associated serialized values with pipe `|` character.

To give an example: a session object `$_SESSION = array('key1'=>'value1', 'key2' => 'value2)` would have the session-serialized form `key1|s:6:"value1";key2|s:6:"value2";`.

Diving deeper into the `unserializesession` function one can observe the underlying problem that is located in the parsing of such a session-serialized session object. The handler intends to process it by splitting up the serialized session string on every vertical pipe character `|` available extracting the key and `unserialize()`‘ing the serialized value.
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  

| 
  
  
  private static function unserializesession($serializedstring) {
  $variables = array();
  $a = preg_split("/(\w+)\|/", $serializedstring, -1, PREG_SPLIT_NO_EMPTY
  | PREG_SPLIT_DELIM_CAPTURE);
  $counta = count($a);
  for ($i = 0; $i < $counta; $i = $i + 2) {
  $variables[$a[$i]] = unserialize($a[$i + 1]);
  }
  return $variables;
  }
  
  
---|---  
  
However, this algorithm fails to properly parse the serialized value of a session key if it contains an unexpected Pipe `|` character due to the intrinsics of `preg_split`. This induces the risk of the parser misinterpreting the beginning and end of a serialized value within the session object, leading to the deserialization of potentially user-controlled input.

This means that any gadget in the code that allows us to write the pipe character anywhere into the value part of the `$_SESSION` array will grant us potential to leverage a PHP Object injection. The file `grade/report/grader/index.php` allows us to do exactly that: supply the ProofOfConcept string `xxx|O:8:"Evil":0:{}` that will be stored as a value in the `$_SESSION` object of an unauthenticated guest user.

This will be serialized by the session handler and stored on the filesystem in the form

`USER|O:8:"stdClass":…:{…}SESSION|O:8:"stdClass":…:{…s:…:"filterfirstname";s:19:"xxx|O:8:"Evil":0:{}";…}`.

The colors indicate how PHPs internal sessionhandler would see the string when correctly deserializing the session and its key value pairs iteratively. In contrast, the `unserializesession` function of moodle that uses `preg_split` would erroneously parse an additional session key:

`USER|O:8:"stdClass":…:{…}SESSION|O:8:"stdClass":…:{…s:…:"filterfirstname";s:19:"xxx|O:8:"Evil":0:{}";…}`

The `unserializesession()` function will detect the `xxx|` string as a new sessionkey although it belongts to the serialized value of another session key. This prematurely cuts off the serialized value mid-parsing and results in a broken deserialization. The logic then iterates to our evil serialized payload and deserializes it.

From this point on, the dangers are known and documented by PHP and the Remote Code Execution is only a matter of technical skill via PHP’s magic functions. We will leave the exact exploitation technique as practice to the reader.

## Patch

It is therefore recommended to mitigate this vulnerability by not relying on `unserialize` in combination with regular expressions to decode the session objects. Instead, keys stored within the session object could hold information about the sessions validity or refer back to the file where this session can be found. When logging out - which should only be possible with an active valid session- the session file of the currently active `$_SESSION` variable can be removed.

Alternatively, the second parameter of `unserialize` could be used to only allow the standard class `stdClass` to be unserialized. This is exactly the path that Moodle has chosen to fix this issue within their recent commit. This would prevent any POI Gadget chains that leverage the POI into more severe vulnerabilities by abusing the magic methods of specific app classes.

However, this mitigation has the drawback of still allowing potential memory corruption bugs that reside in `unserialize()`. They became much rarer especially with only `stdClass` objects, but there have been plenty of them in the past.

## Timeline

Date | Action  
---|---  
2021-02-21 | Submitted Bug via Bugcrowd  
2021-06-16 | Bugcrowd triaged our report with P1  
2021-07-10 | Patch released on GitHub

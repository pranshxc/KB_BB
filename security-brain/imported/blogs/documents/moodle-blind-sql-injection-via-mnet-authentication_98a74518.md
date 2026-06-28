---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-23_moodle-blind-sql-injection-via-mnet-authentication.md
original_filename: 2021-11-23_moodle-blind-sql-injection-via-mnet-authentication.md
title: Moodle Blind SQL injection via MNet authentication
category: documents
detected_topics:
- idor
- sqli
- command-injection
tags:
- imported
- documents
- idor
- sqli
- command-injection
language: en
raw_sha256: 98a7451830f13823f2b7f8150e5523283f1f7b06fc7ca3ea9166fc09d7ac2279
text_sha256: e072dee8d6d47a0d4d526929f64b6339d3e6a1e90d7eb9c4e2abd17cef64a8ae
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Moodle Blind SQL injection via MNet authentication

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-23_moodle-blind-sql-injection-via-mnet-authentication.md
- Source Type: markdown
- Detected Topics: idor, sqli, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `98a7451830f13823f2b7f8150e5523283f1f7b06fc7ca3ea9166fc09d7ac2279`
- Text SHA256: `e072dee8d6d47a0d4d526929f64b6339d3e6a1e90d7eb9c4e2abd17cef64a8ae`


## Content

---
title: "Moodle Blind SQL injection via MNet authentication"
page_title: "r0 · Moodle Blind SQL injection via MNet authentication"
url: "https://r0.haxors.org/posts?id=26"
final_url: "https://r0.xyz/posts/moodle-blind-sql-injection-via-mnet-authentication"
authors: ["rekter0 (@rekter0)"]
programs: ["Moodle"]
bugs: ["SQL injection"]
publication_date: "2021-11-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3147
---

Moodle is an opensource learning management system, popular in universities and workplaces largely used to manage courses, activities and learning content, with about 200 million users
  

|  
---|---  
**Versions affected** | 3.10 to 3.10.3, 3.9 to 3.9.6, 3.8 to 3.8.8, 3.5 to 3.5.17  
**CVE identifier** | CVE-2021-32474  
  
## Summary

> What is Mnet?  
>  The Moodle network feature allows a Moodle administrator to establish a link with another Moodle or a Mahara site and to share some resources with the users of that Moodle. Official documentation: <https://docs.moodle.org/310/en/MNet>
> 
> How ?  
>  Mnet communicate with peers through xmlrpc, and uses encrypted and signed messages with RSA 2048
> 
> So what ?  
>  `auth/mnet/auth.php/keepalive_server` xmlrpc method used to pass unsanitized user supplied parameters to SQL query => SQL injection
> 
> Attack scenario ?  
>  1- You compromised one moodle instance, and use it to launch attack on its peers  
>  2- An evil moodle instance decides to attack its peers  
>  3- For one reason or another some mnet instance keypairs are leaked

## Vulnerability analysis

Moodle uses singed and encrypted xmlrpc messages to communicate via MNet protocol

`/mnet/xmlrpc/client.php`
  
  
  function send($mnet_peer) {
  global $CFG, $DB;
  
  
  if (!$this->permission_to_call($mnet_peer)) {
  mnet_debug("tried and wasn't allowed to call a method on $mnet_peer->wwwroot");
  return false;
  }
  
  $this->requesttext = xmlrpc_encode_request($this->method, $this->params, array("encoding" => "utf-8", "escaping" => "markup"));
  $this->signedrequest = mnet_sign_message($this->requesttext);
  $this->encryptedrequest = mnet_encrypt_message($this->signedrequest, $mnet_peer->public_key);
  
  $httprequest = $this->prepare_http_request($mnet_peer);
  curl_setopt($httprequest, CURLOPT_POSTFIELDS, $this->encryptedrequest);

xmlrpc message is first singed using private key

`/mnet/lib.php`
  
  
  function mnet_sign_message($message, $privatekey = null) {
  global $CFG;
  $digest = sha1($message);
  
  $mnet = get_mnet_environment();
  // If the user hasn't supplied a private key (for example, one of our older,
  //  expired private keys, we get the current default private key and use that.
  if ($privatekey == null) {
  $privatekey = $mnet->get_private_key();
  }
  
  // The '$sig' value below is returned by reference.
  // We initialize it first to stop my IDE from complaining.
  $sig  = '';
  $bool = openssl_sign($message, $sig, $privatekey); // TODO: On failure?
  
  $message = '<?xml version="1.0" encoding="iso-8859-1"?>
  <signedMessage>
  <Signature Id="MoodleSignature" xmlns="http://www.w3.org/2000/09/xmldsig#">
  <SignedInfo>
  <CanonicalizationMethod Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"/>
  <SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
  <Reference URI="#XMLRPC-MSG">
  <DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
  <DigestValue>'.$digest.'</DigestValue>
  </Reference>
  </SignedInfo>
  <SignatureValue>'.base64_encode($sig).'</SignatureValue>
  <KeyInfo>
  <RetrievalMethod URI="'.$CFG->wwwroot.'/mnet/publickey.php"/>
  </KeyInfo>
  </Signature>
  <object ID="XMLRPC-MSG">'.base64_encode($message).'</object>
  <wwwroot>'.$mnet->wwwroot.'</wwwroot>
  <timestamp>'.time().'</timestamp>
  </signedMessage>';
  return $message;
  }

The xml envelope along signature is then encrypted

`/mnet/lib.php`
  
  
  function mnet_encrypt_message($message, $remote_certificate) {
  $mnet = get_mnet_environment();
  
  // Generate a key resource from the remote_certificate text string
  $publickey = openssl_get_publickey($remote_certificate);
  
  if ( gettype($publickey) != 'resource' ) {
  // Remote certificate is faulty.
  return false;
  }
  
  // Initialize vars
  $encryptedstring = '';
  $symmetric_keys = array();
  
  //  passed by ref ->  &$encryptedstring &$symmetric_keys
  $bool = openssl_seal($message, $encryptedstring, $symmetric_keys, array($publickey));
  $message = $encryptedstring;
  $symmetrickey = array_pop($symmetric_keys);
  
  $message = '<?xml version="1.0" encoding="iso-8859-1"?>
  <encryptedMessage>
  <EncryptedData Id="ED" xmlns="http://www.w3.org/2001/04/xmlenc#">
  <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#arcfour"/>
  <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
  <ds:RetrievalMethod URI="#EK" Type="http://www.w3.org/2001/04/xmlenc#EncryptedKey"/>
  <ds:KeyName>XMLENC</ds:KeyName>
  </ds:KeyInfo>
  <CipherData>
  <CipherValue>'.base64_encode($message).'</CipherValue>
  </CipherData>
  </EncryptedData>
  <EncryptedKey Id="EK" xmlns="http://www.w3.org/2001/04/xmlenc#">
  <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-1_5"/>
  <ds:KeyInfo xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
  <ds:KeyName>SSLKEY</ds:KeyName>
  </ds:KeyInfo>
  <CipherData>
  <CipherValue>'.base64_encode($symmetrickey).'</CipherValue>
  </CipherData>
  <ReferenceList>
  <DataReference URI="#ED"/>
  </ReferenceList>
  <CarriedKeyName>XMLENC</CarriedKeyName>
  </EncryptedKey>
  <wwwroot>'.$mnet->wwwroot.'</wwwroot>
  </encryptedMessage>';
  return $message;
  }

On the other side the server receives the xmlrpc request and processes it via verifying signature then decrypting the envelope

`/mnet/xmlrpc/server.php`
  
  
  try {
  $plaintextmessage = mnet_server_strip_encryption($rawpostdata);
  $xmlrpcrequest = mnet_server_strip_signature($plaintextmessage);
  } catch (Exception $e) {
  mnet_debug('encryption strip exception thrown: ' . $e->getMessage());
  exit(mnet_server_fault($e->getCode(), $e->getMessage(), $e->a));
  }
  [...]
  [...]
  // Have a peek at what the request would be if we were to process it
  $params = xmlrpc_decode_request($xmlrpcrequest, $method);
  mnet_debug("incoming mnet request $method");
  [...]
  [...]
  if ((($remoteclient->request_was_encrypted == true) && ($remoteclient->signatureok == true))
  || (($method == 'system.keyswap') || ($method == 'system/keyswap'))
  || (($remoteclient->signatureok == true) && ($remoteclient->plaintext_is_ok() == true))) {
  try {
  // main dispatch call.  will echo the response directly
  mnet_server_dispatch($xmlrpcrequest);
  mnet_debug('exiting cleanly');
  exit;
  } catch (Exception $e) {
  mnet_debug('dispatch exception thrown: ' . $e->getMessage());
  exit(mnet_server_fault($e->getCode(), $e->getMessage(), $e->a));
  }
  }

Then moodle dispatch xmlrequest method to the appropriate functions.

**Blind SQL Injection**  
`keepalive_server` method used to pass client supplied parameters to SQL query unsanitized

`/auth/mnet/auth.php`
  
  
  function keepalive_server($array) {
  global $CFG, $DB;
  $remoteclient = get_mnet_remote_client();
  
  // We don't want to output anything to the client machine
  $start = ob_start();
  
  // We'll get session records in batches of 30
  $superArray = array_chunk($array, 30);
  
  $returnString = '';
  
  foreach($superArray as $subArray) {
  $subArray = array_values($subArray);
  $instring = "('".implode("', '",$subArray)."')";
  $query = "select id, session_id, username from {mnet_session} where username in $instring";
  
  $results = $DB->get_records_sql($query);
  
  if ($results == false) {
  // We seem to have a username that breaks our query:
  // TODO: Handle this error appropriately
  $returnString .= "We failed to refresh the session for the following usernames: \n".implode("\n", $subArray)."\n\n";
  } else {
  foreach($results as $emigrant) {
  \core\session\manager::touch_session($emigrant->session_id);
  }
  }
  }
  
  $end = ob_end_clean();
  
  if (empty($returnString)) return array('code' => 0, 'message' => 'All ok', 'last log id' => $remoteclient->last_log_id);
  return array('code' => 1, 'message' => $returnString, 'last log id' => $remoteclient->last_log_id);
  }

array parameters for `keepalive_server` used to be processed via `implode` and concatinated into the SQL query leading to blind SQL injection risks.

## Impact

Blind SQL injection risks in `keepalive_server` xmlrpc method for MNet Authentication, Successful exploitation could have led to compromising the targeted moodle instance with RCE possibility.

## Timeline

24-01-2021 - Reported  
05-02-2021 - Vendor confirmed  
17-05-2021 - Fixed in new release

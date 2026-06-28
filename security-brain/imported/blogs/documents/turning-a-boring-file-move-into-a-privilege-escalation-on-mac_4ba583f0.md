---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-28_turning-a-boring-file-move-into-a-privilege-escalation-on-mac.md
original_filename: 2023-10-28_turning-a-boring-file-move-into-a-privilege-escalation-on-mac.md
title: Turning a boring file move into a privilege escalation on Mac
category: documents
detected_topics:
- access-control
- command-injection
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- supply-chain
language: en
raw_sha256: 4ba583f09b7b8596b9c1b33ffaf7e1a58583ede556170c2b1cca5f82ed47bb47
text_sha256: e90e20cbeed5437daf983532b6a3259156efe880e47387af99d817bc6db2e6d8
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: true
---

# Turning a boring file move into a privilege escalation on Mac

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-28_turning-a-boring-file-move-into-a-privilege-escalation-on-mac.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: True
- Raw SHA256: `4ba583f09b7b8596b9c1b33ffaf7e1a58583ede556170c2b1cca5f82ed47bb47`
- Text SHA256: `e90e20cbeed5437daf983532b6a3259156efe880e47387af99d817bc6db2e6d8`


## Content

---
title: "Turning a boring file move into a privilege escalation on Mac"
page_title: "Turning a boring file move into a privilege escalation on Mac | pwn.win"
url: "https://pwn.win/2023/10/28/file-move-privesc-mac.html"
final_url: "https://pwn.win/2023/10/28/file-move-privesc-mac.html"
authors: ["kn32"]
programs: ["Parallels"]
bugs: ["Local Privilege Escalation", "MacOS"]
publication_date: "2023-10-28"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 694
---

# Turning a boring file move into a privilege escalation on Mac

Oct 28, 2023 

While poking around [Parallels Desktop](https://www.parallels.com/products/desktop/) I found a script which is invoked by a setuid-root binary, which has the following snippet:
  
  
  local prl_dir="${usr_home}/Library/Parallels"
  if [ -e "$prl_dir" -a ! -d "$prl_dir" ]; then
  log warning "'${prl_dir}' is not a directory. Renaming it."
  mv -f "$prl_dir"{,~}
  continue
  fi
  

Here `${usr_home}` represents the home directory of the user for which Parallels Desktop is installed. The code says if `~/Library/Parallels` exists and is not a directory then move it to `~/Library/Parallels~`, presumably to back it up before creating this path as a directory.

However, given this is our home directory, we (a low privileged user) can create `~/Library/Parallels~` beforehand, and make it a symlink to another directory, for example. This would mean the code actually moves `~/Library/Parallels` _into_ the directory pointed to by the symlink. Additionally, we can fully control the `~/Library/Parallels` file, it can have whatever content we want, or it could even be a symlink to some other file.

Great, so now we can move a file of controlled content, or a symlink, into an arbitrary directory. How can we use this to escalate our privileges to root?

Digging around the filesystem, some ways which came to mind:

  * `/etc/periodic/{daily,monthly,weekly}`
  * Files must be owned by root, which our file isn’t
  * Besides, I don’t want to wait days for this privesc
  * `/etc/pam.d/`
  * Files must be owned by root, which our file isn’t
  * Filenames are important, we can’t use the `Parallels` filename for this
  * `/etc/ssh/sshd_config.d/`
  * Could use something like `AuthorizedKeysCommand` and `AuthorizedKeysCommandUser` to execute a command as root
  * Would need a reboot or some other way to force sshd to reload its config
  * sshd would need to be running in the first place, which it’s not by default
  * `/etc/sudoers.d/`
  * Files must be owned by root, which our file isn’t
  * Files must not be world writeable

Of these, the hurdles which seemed easiest to overcome were those of `/etc/sudoers.d`. So I started digging for files which are owned by root, are not world-writeable, and we can partially control. With some searching I found `/var/log/install.log`.
  
  
  -rw-r--r--@ 1 root  admin  637109 23 Jun 12:00 /var/log/install.log
  

It turns out we can write to this log using the `logger` utility, specifying the `install.error` priority. Like so:
  
  
  logger -p install.error "Hello, World!"
  

![Log file entry](/assets/file-move-privesc-mac/install_log1.png)

Even better, we can get our content onto a new line using a carriage return, which is replaced with a newline, like so:
  
  
  logger -p install.error $(echo -e "\rHello, World!")
  

![Log file newline injection](/assets/file-move-privesc-mac/install_log2.png)

We can use this to insert a line of sudo config:
  
  
  logger -p install.error $(echo -e "\r$USER ALL=(ALL) NOPASSWD=***REDACTED***)
  

![Log file sudo config](/assets/file-move-privesc-mac/install_log3.png)

So now we have a log file with a bunch of invalid sudo config lines (i.e. normal log entries), with one line of valid sudo config, which says that our current user can use sudo with no password, allowing us to escalate our privileges.

Now we can make `~/Library/Parallels` a symlink pointing to `/var/log/install.log` and `~/Library/Parallels~` a symlink pointing to `/etc/sudoers.d/`. When we invoke the vulnerable script, which runs as root, it will move our symlink, pointing to the log file, into `/etc/sudoers.d/`.

After that we can run `sudo su`, which will follow the symlink, parse the log file, spitting out pages of errors about the invalid syntax of the log entries in the process (but kindly continuing processing) until it reaches a line of valid syntax which we’ve injected, and eventually we’ll be dropped into a root shell.

Hopefully other people find this trick useful, beyond just Parallels. You can find the code for this exploit [on my GitHub](https://github.com/kn32/parallels-file-move-privesc).

## Timeline

  * **2023-05-19** \- ZDI submission, assigned ZDI-CAN-21227
  * **2023-06-21** \- reported to vendor
  * **2023-07-06** \- fix released in version 18.3.2
  * **2023-12-19** \- public release of advisory, CVE-2023-50226

[](/2023/10/28/file-move-privesc-mac.html)

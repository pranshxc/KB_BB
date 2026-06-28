---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-02_filezilla-untrusted-search-path.md
original_filename: 2019-04-02_filezilla-untrusted-search-path.md
title: FileZilla Untrusted Search Path
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 9a378fce14873501a3d228751352c72f99a88addf606cdf7c7652de684bb9437
text_sha256: ba4eff23d4b296f8c885dc3fac759186d4b9090f07fca2cda91d78629b5ea6f8
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# FileZilla Untrusted Search Path

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-02_filezilla-untrusted-search-path.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9a378fce14873501a3d228751352c72f99a88addf606cdf7c7652de684bb9437`
- Text SHA256: `ba4eff23d4b296f8c885dc3fac759186d4b9090f07fca2cda91d78629b5ea6f8`


## Content

---
title: "FileZilla Untrusted Search Path"
url: "https://medium.com/tenable-techblog/filezilla-untrusted-search-path-bc3a7b3ae51e"
authors: ["Chris Lyne (@lynerc)"]
programs: ["FileZilla (EU-FOSSA 2)"]
bugs: ["RCE"]
publication_date: "2019-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5334
scraped_via: "browseros"
---

# FileZilla Untrusted Search Path

FileZilla Untrusted Search Path
Chris Lyne
Follow
3 min read
·
Apr 2, 2019

411

Targeting the user with a rogue binary

Summary

I found a vulnerability in FileZilla 3.40.0 that could allow a remote attacker to execute arbitrary code. FileZilla depends on a specific executable to handle its SFTP operations, but it will happily load the binary from several locations. By tricking a victim user into downloading a rogue binary, the attacker is able to leverage this bug to execute code in the context of the current user.

Press enter or click to view image in full size
Calculator popped

Before I talk about the attack scenario, I’ll discuss how I found the vulnerability.

Discovery Process

I found this bug while performing some basic dynamic analysis. During a system call trace (‘strace’), the following calls were observed (current user name is ‘osboxes’):

10327 getcwd("/home/osboxes", 1024) = 14
10327 stat("/home/osboxes/fzsftp", 0x7ffd184b2cd0) = -1 ENOENT (No such file or directory)
10327 stat("/home/osboxes/bin/fzsftp", 0x7ffd184b2cd0) = -1 ENOENT (No such file or directory)
10327 stat("/home/osboxes/src/putty/fzsftp", 0x7ffd184b2cd0) = -1 ENOENT (No such file or directory)
10327 stat("/home/osboxes/putty/fzsftp", 0x7ffd184b2cd0) = -1 ENOENT (No such file or directory)
10327 stat("/usr/bin/fzsftp", {st_mode=S_IFREG|0755, st_size=568928, …}) = 0

FileZilla is searching for the “fzsftp” binary. Notice the home directory is searched before /usr/bin/. But what is fzsftp needed for?

A search for fzsftp in the code base led me to src/engine/sftp/connect.cpp:

int CSftpConnectOpData::Send()
{
  switch (opState)
  {
  case connect_init:
  {
  auto executable = fz::to_native(engine_.GetOptions().GetOption(OPTION_FZSFTP_EXECUTABLE));
  if (executable.empty()) {
  executable = fzT("fzsftp");
  }
  LogMessage(MessageType::Debug_Verbose, L"Going to execute %s", executable);
  // snip
  if (!controlSocket_.process_->spawn(executable, args)) {
  LogMessage(MessageType::Debug_Warning, L"Could not create process");
  return FZ_REPLY_ERROR | FZ_REPLY_DISCONNECTED;;
  }
// snip

Based on the CSftpConnectOpData::Send() function (note the “sftp”), the “fzsftp” executable will be passed to a spawn() function. This function is defined in libfilezilla/lib/process.cpp. The gist is that the spawn function creates a new process. In the case of Linux, there is a call to fork(), and shortly after there is a call to execv(), thereby launching fzsftp.

execv(cmd.c_str(), argV.get()); // noreturn on success

These pieces of information tell us two important things. First, the FileZilla application checks in multiple locations to find the fzsftp binary. The first place it looks is in the current user’s home directory. Secondly, the fzsftp binary will be executed when an SFTP connection is initiated. As a side note: fzsftp is a custom version of Putty’s “psftp” — used to perform SFTP operations.

Get Chris Lyne’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s take a look at how to exploit this vulnerability.

Exploitation

In order to exploit this bug, an attacker would have to drop a malicious binary named “fzsftp” into any of the directories shown in the strace output. But how can the attacker accomplish this?

I mentioned earlier that user interaction is required. However, FileZilla makes the attacker’s life simple. When FileZilla loads, the default “local site” is the user’s home directory. This is where downloads will be stored.

Press enter or click to view image in full size
Local site is user’s home directory

With this in mind, an attacker needs to simply convince the FileZilla user to download a crafted fzsftp binary from his or her server. After FileZilla is restarted, any new SFTP connection will launch the rogue binary. Below is a video showing what exploitation looks like.

In this case, I popped a calculator. Creating the payload was pretty simple. Add an include and a call to execl() in src/putty/psftp.c, and recompile (it will be built as “fzsftp”). As long as the call is beneath the first call to fzprintf() in psftp_main(), everything will work.

fzprintf(sftpReply, "fzSftp started, protocol_version=%d", FZSFTP_PROTOCOL_VERSION);
execl("/snap/bin/gnome-calculator", "gnome-calculator", "-e", "Tenable", (char *) NULL);
Conclusion

As you can see, an untrusted path vulnerability can give an attacker a simple attack vector. They don’t need any complicated shell code or payload delivery mechanisms. With a small amount of social engineering, they can easily exploit this bug.

Patch details can be found at revision 9112 of the FileZilla SVN repository. This case represents positive strides in making open source software more secure. FileZilla is one of many open source projects to join the EU-funded bug bounty program. Thanks to the EU and HackerOne for making the disclosure process quick and painless.

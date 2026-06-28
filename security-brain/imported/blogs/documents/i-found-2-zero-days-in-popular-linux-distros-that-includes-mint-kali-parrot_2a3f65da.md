---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-17_i-found-2-zero-days-in-popular-linux-distros-that-includes-mint-kali-parrot.md
original_filename: 2024-01-17_i-found-2-zero-days-in-popular-linux-distros-that-includes-mint-kali-parrot.md
title: I found 2 Zero-Days in popular Linux distros that includes Mint, Kali, Parrot
category: documents
detected_topics:
- command-injection
- path-traversal
- file-upload
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- path-traversal
- file-upload
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 2a3f65dad9d883e458f4a823110fa3f3b2d6ffcacf654b79efec206b5edc1271
text_sha256: 641becf9d421f6ffde71611f896ad42001393ca3f0e1a862400077f30e944ded
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# I found 2 Zero-Days in popular Linux distros that includes Mint, Kali, Parrot

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-17_i-found-2-zero-days-in-popular-linux-distros-that-includes-mint-kali-parrot.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, file-upload, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `2a3f65dad9d883e458f4a823110fa3f3b2d6ffcacf654b79efec206b5edc1271`
- Text SHA256: `641becf9d421f6ffde71611f896ad42001393ca3f0e1a862400077f30e944ded`


## Content

---
title: "I found 2 Zero-Days in popular Linux distros that includes Mint, Kali, Parrot"
url: "https://febinj.medium.com/i-found-2-zero-days-in-popular-linux-distros-that-includes-mint-kali-parrot-04e1cee800bd"
authors: ["Febin Mon Saji"]
programs: ["Linux Mint (Xreader)", "MATE Desktop (Atril)"]
bugs: ["RCE", "Argument injection", "Path traversal", "Arbitrary file write"]
publication_date: "2024-01-17"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 531
scraped_via: "browseros"
---

# I found 2 Zero-Days in popular Linux distros that includes Mint, Kali, Parrot

I found 2 Zero-Days in popular Linux distros that includes Mint, Kali, Parrot
Febin
Follow
10 min read
·
Jan 17, 2024

135

This is the story on how I found 2 Zero-Day Vulnerabilities (4 CVEs). The flaws affected a list popular Linux Desktop distros that inlcudes:

Linux Mint
Kali Linux (Popular OS among Security professionals, researchers)
Parrot OS (Popular OS among Security professionals, researchers)
Ubuntu-Mate
Xubuntu
Fedora Cinnamon
Fedora Mate
Manjaro Mate
Manjaro Cinnamon
Ubuntu Kylin (Official Chinese Ubuntu)
Kylin OS V10 ( OS said to be used in the Chinese Government Sectors )

CVEs:

CVE-2023–44451, CVE-2023–52076 - EPUB File Parsing Directory Traversal RCE Vulnerability

CVE-2023–44452, CVE-2023–51698: CBT File Parsing Argument Injection RCE

Let’s Jump in on to the vulnerabilities,

1. EPUB File Parsing Directory Traversal RCE

My 8th and 10th CVEs

Slippy-book: EPUB File Parsing Directory Traversal Remote Code Execution

CVE-2023–44451 (Xreader), CVE-2023–52076(Atril)(Reserved):

RCE Vulnerability affected popular Linux Distros including Mint, Kali, Parrot, Manjaro etc. EPUB File Parsing Directory Traversal Remote Code Execution

A Critical Path traversal and Arbitrary file write vulnerability has been discovered in the default document viewer software of Linux’s MATE/ and Linux Mint affecting popular operating systems such as Kali Linux, Parrot Security OS, Ubuntu-Mate, Linux Mint, Xubuntu, and all the other Operating Systems that use MATE or Atril/Xreader as default doc viewer.

The vulnerability exists in Atril Document Viewer and Xreader Document Viewer which are the default document viewers of the MATE environment and Linux Mint respectively. Atril is the default document reader for Kali Linux, Ubuntu-Mate, Parrot Security OS, and Xubuntu, and Xreader is the default document reader for Linux Mint.

This vulnerability is capable of writing arbitrary files anywhere on the filesystem to which the user opening a crafted document has access, the only limitation is that this vulnerability cannot be exploited to overwrite existing files but that doesn’t stop an attacker from achieving Remote Command Execution on the target system.

I named this vulnerability “Slippy-Book“

Severity: CRITICAL

Impact: Remote Command Execution, System compromise

This can be used particularly against security researchers who mostly use Kali and Parrot OS and also desktop users who use Linux Mint.

Remote Command Execution can be achieved in many ways:

The most efficient way to achieve RCE is by placing a malicious .desktop entry under $HOME/.config/autostart/ directory, and the .desktop will execute when the user logs out and logs back in, the autostart/ directory acts as the startup folder in Windows, and it will execute all the .desktop entries that are present inside at startup. We can place an infinite number of .desktop files with random names under autostart/ directory to achieve RCE, no need to overwrite any file.
By writing the authorized_keys file under the .ssh/ directory inside the user’s home, in this way, an attacker can immediately achieve Command Execution via SSH if the target system has SSH enabled.
RCE can be achieved in another way just by writing files like .bash_profile, .bash_login, .zshrc, .cshrc, .vimrc, .xsession under the user’s home directory. Many of these files might be missing in operating systems, it depends on the OS. In Ubuntu-mate and Linux Mint, .bash_profile, and .bash_login files won’t be present, and placing those files with malicious commands written inside under the user’s home directory will result in RCE if the user logs in to the system without GUI mode, like SSH login.
Another way to achieve control over the target system is by writing files in places like ~/.local/bin, ~/.local/lib/python3.9/site-packages/, ~/.local/lib/python3.10/site-packages/, ~/.local/lib/python3.11/site-packages/, ~/.local/share/applications/, /var/www/html/, /var/www/ and so on.

[+] Finding the Vulnerability:

I was researching archive file formats such as Zip, Tar, Rar, etc., and the software that works with archives, then I got the idea to get into the Ebook file format (.epub) because .epub files are really Zip archives with some XML, HTML and other files packed inside. Even though Epub files are just zip files, epub format has its own standards.

[*] How did I find the vulnerability?

People have been exploiting Archives since the early 2000s, researchers are constantly looking into Archives and archiving software for vulnerabilities and Zero-day acquisition companies like Zerodium are willing to pay million-dollar bounties for zero-days in archives and archivers. So, I thought to give it a try. I am not a binary ninja or kernel exploitation specialist to pull off a highly complicated exploit chain that could give me a code execution or elevation of privilege. My approach was, “What is the dumbest thing that could possibly work”.

Path traversal is one of the most common vulnerabilities that affect Archives and software that deals with archives, Zip Slip is one such vulnerability that leads to arbitrary file overwrite and Code execution that was disclosed on the 5th of June 2018 by the Snyk Security team, Zip Slip was a widespread vulnerability affected many software and libraries that handle Zip archives. Path traversal in zip archives was an ancient bug in the wild even before that was disclosed by the Snyk Security team. It is still present in many software including some Android file managers.
Another such vulnerability was discovered in WinRar with the CVE Id CVE-2018–20250, in which a potential path traversal can be exploited to achieve RCE.

Archives were developed in a period when people not much cared about security, and that’s where all the problems began.

Knowing that Path traversals can be a problem in the archive, I started testing it out on EPUB. I started off by downloading a sample .epub file from the internet and started playing with it. Then I did something really interesting, I added my own files into the .epub file by using the “zip -u” command.

$ zip -u sample1.epub hello.txt

And then when I listed the contents of the EPUB archive using “unzip -l”, I was able to see my hello.txt was present inside the EPUB. Perfect! So what’s next? As I said above, my approach was, “What is the dumbest thing that could possibly work” so what I did next was add a bunch of Path Traversal gadgets (../../) at the beginning of my filename hello.txt.

I was using Kali Linux and logged in as root during the research on archives.
Then, I navigated to the directory graphically and clicked on the EPUB document, the document opened up and nothing happened but after that, I noticed something really interesting, the hello.txt file was present under my Kali Linux’s root (/). I tried overwriting existing files but that didn’t work.

Then, I tried changing the filename to something like ../../../../tmp/test.txt and that worked too, a file named test.txt was successfully created under /tmp upon opening the epub document. First I thought it was a vulnerability in Kali Linux and downloaded the latest ISO of Kali from their official site and built a VM to test it out. Guess what? It worked on the latest version of Kali too. The software responsible for opening epub files in Kali is Atril, I then went to Google to read more about Atril Document Viewer and found out that it is the default Document reader for MATE desktop environment. After knowing that, I immediately switched to my Parrot OS VM to reproduce the same vulnerability, and that worked in Parrot OS as well. I also tested it out on Ubuntu’s MATE variant called Ubuntu-MATE and found that it was also vulnerable. The MATE desktop environment itself is vulnerable.

I also tried to reproduce this on various other Linux distros with other Desktop Environments and found out that Linux Mint is also vulnerable.

[+] Achieving Remote Command Execution:

This vulnerability can’t be exploited to overwrite existing files, it can only create new files under any specified locations, but that doesn’t stop us from achieving RCE. I tried out using the vulnerability to write a .desktop entry under $HOME/.config/autostart and then I logged out and logged back in, the malicious .desktop entry got triggered and I got Remote Command Execution. I also tried placing an authorized_keys file under .ssh/ directory and achieved RCE via SSH. Note: If a directory is not present it will create the directory automatically.

Who knows about the Ebook format? Hasn’t everyone switched to PDF?

The answer is no, EPUB is still a popular and powerful document format, but many people prefer PDF. Most of them are familiar with PDFs. So, I was trying to maximize this vulnerability impact. Another Interesting thing I noticed was, when renaming the .epub document to something.pdf, the vulnerable Document Viewer (Atril/Xreader) tries to open the something.pdf file and reads it as an EPUB document because it is responsible for reading both EPUB and PDF, it also supports many other document formats as well. In other words, we can rename our crafted something.epub to something.pdf and then send it to the target to achieve RCE on the target.

So everything is good, we could create an exploit that’ll craft an epub/pdf pair to write malicious .desktop entries under /home//.config/autostart/ directory. But there’s a small problem, the target user’s username is required for successful exploitation of this bug. What if we don’t know the username? No Easy RCE? Needs to guess Username? Needs to try random common usernames? Let’s see what I got..

Upon further analysis, I found out that we can use the /proc/self/cwd to access the user’s home directory if he downloads the crafted document and opens it somewhere inside his home directory such as the ~/Downloads/, ~/Documents/ directory. So we can exploit the path traversal bug to achieve RCE just by using the gadget ../../../../../proc/self/cwd/../.config/autostart/exploit.desktop.

I have created a fully working exploit for this vulnerability (exploit_rce.sh) and a script to write and include custom files for path traversal (exploit_file_write.sh).

Demo: (Linux Mint)

Opens Calculator app as a PoC
Press enter or click to view image in full size

https://raw.githubusercontent.com/febinrev/slippy-book-exploit/main/Slippy-exploit1.mp4

Exploit: https://github.com/febinrev/slippy-book-exploit.git

Zero Day Initiative Advisory: https://www.zerodayinitiative.com/advisories/ZDI-23-1835/

Get Febin’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s move on to the next bug,

2. CBT File Parsing Argument Injection

This bug is even dangerous as a URL/Link is the only thing that’s needed to trigger RCE on the target. In other words, if a victim user visits a URL/Link will trigger the RCE immediately and you’ll get a shell.

A Critical One-Click RCE/Command Injection Vulnerability Affecting Popular Linux Operating Systems with MATE, Cinnamon, and some Xfce desktop Environments.

My 9th and 11th CVEs

Vulnerability Summary:

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Mint Xreader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file.

The specific flaw exists within the parsing of CBT files. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the current user.

This vulnerability is due to a bad code segment in Atril and Xreader responsible for handling comic book documents (.cbr, .cbz, .cbt, .cb7). Comic book documents are just archives that contain images in it. The vulnerability here can be exploited using a maliciously crafted CBT document which is a TAR archive.

Root Cause — Vulnerable Code segment in both doc viewers (comics-document.c):

static const ComicBookDecompressCommand command_usage_def[] = {

/* RARLABS unrar */

{"%s p -c- -ierr --", "%s vb -c- -- %s", NULL , FALSE, NO_OFFSET},

/* GNA! unrar */

{NULL , "%s t %s" , "%s -xf %s %s" , FALSE, NO_OFFSET},

/* unzip */

{"%s -p -C --" , "%s %s" , NULL , TRUE , OFFSET_ZIP},

/* 7zip */

{NULL , "%s l -- %s" , "%s x -y %s -o%s", FALSE, OFFSET_7Z},

/* tar */

{"%s -xOf" , "%s -tf %s" , NULL , FALSE, NO_OFFSET},

/* UNARCHIVER */

{"unar -o -" , "%s %s" , NULL , FALSE, NO_OFFSET}

};

By looking at the above code, we can see that there are shell commands used for decompression. Look at the /* tar */ section, it actually calls the following shell command, “tar -xOf -tf“. This is to view/load each image inside the CBT document. This behavior can be exploited by using an option of tar program ‘–checkpoint-action’ to execute arbitrary commands on the target by naming one of the images inside the CBT document to something like ‘–checkpoint-action=EXEC=bash -c “whoami>/tmp/who.txt”;.jpg’.

This vulnerability was already found in Evince Document viewer (the default Doc reader of GNOME) back in 2017. Since Atril and Xreader are forks of Evince, this vulnerability was present in both Atril and Xreader. Atril’s team fixed the vulnerability at that time by adding a piece of code that quits Atril’s process if the CBT file with “–checkpoint-action=” in its name. The following was the patch (comics-document.c) (line — 983):

extract_argv (EvDocument *document, gint page)

{

ComicsDocument *comics_document = COMICS_DOCUMENT (document);

char **argv;

char *command_line, *quoted_archive, *quoted_filename;

GError *err = NULL;

if (g_strrstr (comics_document->page_names->pdata[page], "--checkpoint-action="))

{

g_warning ("File unsupported\n");

gtk_main_quit ();

}

As you can see, it throws a “File Unsupported” message to the console and quits when it sees “–checkpoint-action=” in a page/filename. I noticed that this only works with an empty file or a really small image file, and if we provide a larger file with more bytes, the “gtk_main_quit ();” function fails, so it continues to run, thus executing the injected arbitrary command.

In the MATE desktop environment, many XFCE and lightweight desktop environments (including OS like Kali, Parrot, Xubuntu, Ubuntu Mate, Kylin, Fedora Mate, Manjaro Mate), this vulnerability can be exploited just by sending a link/URL because these Operating Systems/Environments has Atril and Atril has an additional component called atril-previewer that will trigger the exploit without even opening or clicking on the document. An attacker can craft a webpage that instantly downloads the crafted CBT file onto the target system when the target user visits the webpage and the latest Firefox browser nowadays downloads automatically by default without user confirmation, when the user navigates to his Downloads directory the payload will be executed, gives the attacker the shell.

In Linux Mint (Cinnamon Desktop Environment), the target user must open the document to trigger the payload because Linux Mint uses Xreader and Xreader doesn’t have a previewer.

Demo:

In the demo video, the following is the scenario:

Attacker Machine — Kali Linux
Victim Machine — Kali Linux latest edition (2023.3)
Victim visits the malicious URL/Link generated by my exploit script

https://user-images.githubusercontent.com/52229330/292667942-3f8f8959-74a9-445e-a33c-11c539caaffd.mp4

Exploit: https://github.com/febinrev/atril_cbt-inject-exploit.git

Exploit Dependencies: poppler-utils
Please install poppler-utils before running the exploit script on your Linux machine (Kali preferred). Installation: apt install poppler-utils.

Github Advisory on MATE Atril: https://github.com/mate-desktop/atril/security/advisories/GHSA-34rr-j8v9-v4p2

Zero Day Initiative Advisory on Mint Xreader: https://www.zerodayinitiative.com/advisories/ZDI-23-1836/

Update the Document Viewers to the latest version on your Distros!

Thanks for Reading.

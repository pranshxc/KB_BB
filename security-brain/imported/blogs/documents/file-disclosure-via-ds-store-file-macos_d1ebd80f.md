---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-23_file-disclosure-via-ds_store-file-macos.md
original_filename: 2018-01-23_file-disclosure-via-ds_store-file-macos.md
title: File Disclosure via .DS_Store file (macOS)
category: documents
detected_topics:
- command-injection
- information-disclosure
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- mobile-security
- supply-chain
language: en
raw_sha256: d1ebd80f00d89d8895ce1bc30b7dd10b551cfbaf14c66f0f5f710070d227c066
text_sha256: 3394b786909edc1ee39ea938a42e958597ca450a063479ea7369bf275924b6bc
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# File Disclosure via .DS_Store file (macOS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-23_file-disclosure-via-ds_store-file-macos.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `d1ebd80f00d89d8895ce1bc30b7dd10b551cfbaf14c66f0f5f710070d227c066`
- Text SHA256: `3394b786909edc1ee39ea938a42e958597ca450a063479ea7369bf275924b6bc`


## Content

---
title: "File Disclosure via .DS_Store file (macOS)"
page_title: "FACEBOOK N/A – FILE DISCLOSURE VIA .DS_STORE FILE (MACOS) – @omespino"
url: "http://omespino.com/write-up-file-disclosure-via-ds_store-file-macos"
final_url: "https://omespino.com/write-up-file-disclosure-via-ds_store-file-macos/"
authors: ["Omar Espino (@omespino)"]
programs: ["Meta / Facebook"]
bugs: ["Directory listing"]
publication_date: "2018-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6002
---

WEBN/A[January 2018](/write-up-file-disclosure-via-ds_store-file-macos/)

# FACEBOOK N/A – FILE DISCLOSURE VIA .DS_STORE FILE (MACOS)

**Introduction:**  
Hi everyone, this is another Facebook Whitehat Report write up (Facebook marked the report as N/A, but some another programs accept this bug as a valid bug bounty, per ex. Twitter so this might be can be useful in some scenarios), well, there you go: 

Title Directory Listing Disclosure via .DS_Store file (macOS)  
Product / URL: https://live.oculus.com/

Description and Impact  
Apple Macintosh OS X / macOS .DS_Store Directory Listing Disclosure Vulnerability

In the Apple macOS operating system, .DS_Store is a file that stores custom attributes of its containing folder, such as the position of icons or the choice of a background image. BUT ALSO LIST THE WHOLE FILES ON DIRECTORY THAT HAS BEEN CREATED AS HIDDEN FILE, AUTOMATICALLY BY MACOS.

Critical ISSUE! A remote attacker may read obtain web directory content information by submitting a URL to the vulnerable host’s web service of the following form:

http://www.example.com/target_directory/.DS_store.

This information could provide an attacker with sensitive information including system configuration, installed applications, etc. Properly exploited, this information could allow an attacker to further compromise the security of the host.

But how do .DS_Store files get on a web server? This can happen in several ways:

A user copies an entire folder of files to a web server via FTP. In this case, the .DS_Store file contained in that folder (or multiple .DS_Store files contained in sub-folders) gets copied to the webserver. (Note that some FTP clients do not copy .DS_Store files by default.)

A user copies the entire contents of a folder via FTP to a web server by selecting all the files in a folder. In normal usage, the .DS_Store file will not be copied, but, if invisible files are displayed in the user’s FTP client, and the user simply selects all files in the folder and copies them to the webserver directory, the .DS_Store file – and any other invisible file – will be copied to the server.  
Reproduction Instructions / Proof of Concept

• OS: macOS  
• You need to have python2.7, pip for python2.7, ds_store and tqdm pip modules installed:  
brew install python && sudo pip install ds_store && sudo pip install tqdm  
** Only for .DS_Store parsing to make the content file “human-readable”  
• Navigate to https://live.oculus.com/assets/.DS_Store and the “.DS_Store” file, downloads automatically.  
• Save the code bellow this is small “.DS_Store” files parser as “dsstore.py” in the same “.DS_Store” file directory :

* NOTE: this script was borrowed from some part of internet but i could not find the source anymore, if somebody knows the author, just let me know to give the properly credits to him/her.  
<
  
  
  #!/usr/bin/env python
  # Begin Small .DS_Store Parser
  # -*- encoding: utf-8 -*-
  from ds_store import DSStore
  from tqdm import tqdm
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--path", help="Path to the DS_Store file", required=True)
  parser.add_argument("-t", "--type", help="Type : Iloc, bwsp, lsvp, lsvP, icvp", default='Iloc')
  args = parser.parse_args()
  dsstore = DSStore.open(args.path, 'r+')
  for data in tqdm(dsstore):
  data = str(data)
  entry = data.translate(None, "<>")
  entry = entry.split(' ')
  if(entry[1] == args.type):
  print(entry[0])
  # Ends Small .DS_Store Parser
  

• Run the script and see the output
  
  
  localhost:~ds_store_py$ python dsstore.py -p .DS_Store
  0%|
  fonts
  images
  logos
  nux_bg_web.mp4
  oculus-health.pdf

• Then the files are listed (human-readable), well let’s see what happens with the other directories, for example, “images”, navigate to https://live.oculus.com/assets/images/.DS_Store and the “.DS_Store” file, again downloads automatically.

• RE-Run the script for the .DS_Store from images and see the output
  
  
  localhost:~ds_store_py$ python dsstore.py -p .DS_Store
  0%|
  24_sprite.png
  24_sprite2x.png
  _temp-cesbg.jpg
  _temp-ceslogo.png
  _temp-e3bg.jpg
  _temp-e3logo.png
  bg-event-generic.jpg
  bg-experiences.jpg
  bg-home.jpg
  bg-search.jpg
  bg-search2.jpg
  black-dot@2x.png
  black-pin1@2x.png
  black-pin2@2x.png
  black-pin3@2x.png
  black-pin4@2x.png
  black-pin@2x.png
  blue-dot@2x.png
  blue-pin1@2x.png
  blue-pin2@2x.png
  blue-pin3@2x.png
  blue-pin4@2x.png
  blue-pin@2x.png
  confirmation-bg.jpg
  event_e3_feature.jpg
  event_tour_feature.jpg
  facebook_og.jpg
  facebook_share.jpg
  favicon.png
  new-reality-1.jpg
  new-reality-3.jpg
  oculus-ready.png
  twitter_card.jpg
  

[![](/assets/images/2018/01/live.oculus.com-directory-listing-by-DS_Store.webp)](/assets/images/2018/01/live.oculus.com-directory-listing-by-DS_Store.webp)

• Then Confirm vía browser the accessibility for any file listed for example “_temp-e3logo.png” , go to https://live.oculus.com/assets/images/_temp-e3logo.png via any browser and see the file.

• Repeat in whole Directory “Three”, if you can access to any “.DS_Store” you can see the Directory Listing

• “.DS_Store” files founded on https://live.oculus.com/ :

https://live.oculus.com/assets/.DS_Store  
https://live.oculus.com/assets/images/.DS_Store  
https://live.oculus.com/assets/logos/.DS_Store

• How can the attacker get the file? Easy, with a simple google/bing dork for example “site:live.oculus.com filetype(.DS_Store OR DS_Store)” or maybe with a manual test on assets or image directories adding .DS_Store at the end of the URL ex: “https://live.oculus.com/assets/” + “.DS_Store”, because is a common error upload the DS_Store file when you zip the folder in your macOS and upload the folder to the server), the DS_Store file is not a security issue by itself, I think the security issue is that you have that kind of file published in your web app that let the attacker list the whole directory.

This time was in the inoffensive folder but think about the impact if you accidentally upload a .DS_Store in the wrong public folder on the server.

Anyway, you should erase any .DS_Store on any web application public servers to prevent this behavior.

• Solution / Fix :  
Erase any .DS_Store files on any application server published on the internet.

Timeline:  
03 Jun 2017: Initial report  
06 Jun 2017: Security team member Kurt asking for help to understand and reproduce the bug  
06 Jun 2017: My reply with more detailed information.  
07 Jun 2017: Security team asking how the “attacker” gains access to the mentioned file (.DS_Store)  
08 Jun 2017: Report triaged  
07 Jun 2017: Bug acknowledged and Neal said that fix is in the progress  
12 Jun 2017: Vic informed me that bug has been mitigated.  
12 Jun 2017: I replied confirming that the bug was patched  
21 jun 2017: Report marked as “Not Applicable”, with the next resolution “The committee met to analyze the issue and we concluded that it doesn’t qualify for a bounty because no sensitive data was exposed”

Simliar bug that was marked as valid report and bug bounty (Twitter):  
<https://hackerone.com/reports/142549>

well, that’s it if you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/intent/user?screen_name=omespino), read you later.

[](/facebook-bug-bounty-getting-access-to-prompt-debug-dialog-and-serialized-tool-on-main-website-facebook-com/)

[](/write-up-ctf-eset-latinoamerica-challenge-36/)

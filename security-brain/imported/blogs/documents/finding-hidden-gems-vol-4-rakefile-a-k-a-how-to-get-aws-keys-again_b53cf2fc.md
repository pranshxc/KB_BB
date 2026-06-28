---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-03_finding-hidden-gems-vol-4-rakefile-aka-how-to-get-aws-keys-again.md
original_filename: 2019-07-03_finding-hidden-gems-vol-4-rakefile-aka-how-to-get-aws-keys-again.md
title: 'Finding hidden gems vol. 4: Rakefile a.k.a. how to get AWS keys again'
category: documents
detected_topics:
- supply-chain
- oauth
- sso
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- supply-chain
- oauth
- sso
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: b53cf2fcc5434a7a276aefc60f9ec4e23fd833f9970ef9b682f0827bd97c6aaf
text_sha256: 9aee95358440d8f08e87d745da13fa547deb5e323a5476cbcfa05115694d0712
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Finding hidden gems vol. 4: Rakefile a.k.a. how to get AWS keys again

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-03_finding-hidden-gems-vol-4-rakefile-aka-how-to-get-aws-keys-again.md
- Source Type: markdown
- Detected Topics: supply-chain, oauth, sso, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `b53cf2fcc5434a7a276aefc60f9ec4e23fd833f9970ef9b682f0827bd97c6aaf`
- Text SHA256: `9aee95358440d8f08e87d745da13fa547deb5e323a5476cbcfa05115694d0712`


## Content

---
title: "Finding hidden gems vol. 4: Rakefile a.k.a. how to get AWS keys again"
url: "https://medium.com/@mateusz.olejarka/finding-hidden-gems-vol-4-rakefile-a-k-a-how-to-get-aws-keys-again-ed0d840e0ec"
authors: ["Mateusz Olejarka (@molejarka)"]
bugs: ["Information disclosure"]
publication_date: "2019-07-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5169
scraped_via: "browseros"
---

# Finding hidden gems vol. 4: Rakefile a.k.a. how to get AWS keys again

Finding hidden gems vol. 4: Rakefile a.k.a. how to get AWS keys again
Mateusz Olejarka
Follow
2 min read
·
Jul 3, 2019

20

1

Long time no see. I will improve I promise. Maybe. NVM.

S
taying in application development area as in previous post.
Some time ago I was interested in applications created in Ruby. I did some review of trending GitHub repositories and I noticed that some of them contain a Rakefile file. To quote the docs:

Rake is a Make-like program implemented in Ruby. Tasks and dependencies are specified in standard Ruby syntax.
Rake has the following features:
* Rakefiles (rake’s version of Makefiles) are completely defined in standard Ruby syntax. No XML files to edit. No quirky Makefile syntax to worry about (is that a tab or a space?)
* Users can specify tasks with prerequisites.
* Rake supports rule patterns to synthesize implicit tasks.
* Flexible FileLists that act like arrays but know about manipulating file names and paths.
* A library of prepackaged tasks to make building rakefiles easier. For example, tasks for building tarballs. (Formerly tasks for building RDoc, Gems and publishing to FTP were included in rake but they’re now available in RDoc, RubyGems and respectively.)
* Supports parallel execution of tasks.

S
ounds cool, maybe some juicy information is hiding there. As in previous story I used simple multi-threaded Python code to check my domain list to see if there are any such files available.

Get Mateusz Olejarka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found several of those files and one interesting in particular:

require ‘rubygems’
require ‘bundler/setup’
require ‘rake’
require ‘rspec/core’
require ‘rspec/core/rake_task’
[ — CUT — ]
path = “conf/deployment.yml”
[ — CUT — ]
task :spec => :build
task :default => :build

O.o a deployment.yml is a configuration file or so it seems. Probably accessing it will result in 403 response code but still it is worth to check I think.
Surprise surprise — it was accessible! Inside it were AWS keys.

production:
[--CUT--]
aws_key: AKIA[--CUT--]AR
***REDACTED-AWS-KEY***: vx[--CUT--]nIst
 
development:
[--CUT--]

This is it, another P1.

Lessons learned
For myself - further extend my list of application development related files
Bug hunters - search for Rakefile, Makefile, Dockerfile… (there is much more of those)
Developers - make sure you do not have any additional content in an application web root folder, which is not necessary and, of course, set proper permissions to the configuration folder.

If you enjoyed this story go and read three previous parts:

Finding hidden gems vol. 1: forging OAuth tokens using discovered client id and client secret
Finding hidden gems vol. 2: REAMDE.md, the story of a bit too helpful readme file
Finding hidden gems vol. 3: quick win with .sh file

If you have any questions feel free to use comments ore find me on Twitter.

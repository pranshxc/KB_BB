---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-09_setting-up-gitrob-and-using-it-to-find-leaking-repository-of-an-employee-in-a-ha.md
original_filename: 2019-02-09_setting-up-gitrob-and-using-it-to-find-leaking-repository-of-an-employee-in-a-ha.md
title: Setting Up Gitrob and using it to find Leaking Repository of an Employee in
  a hackerone private program.
category: documents
detected_topics:
- sso
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 5c2454406557dfcc0b5c7339efab4dff106fbde5caaa31bf0f658b74eca6691c
text_sha256: ca420c9b08d2a84d8e55484e335afd9e900247aca8215cda326e9a6fd83f8460
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Setting Up Gitrob and using it to find Leaking Repository of an Employee in a hackerone private program.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-09_setting-up-gitrob-and-using-it-to-find-leaking-repository-of-an-employee-in-a-ha.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `5c2454406557dfcc0b5c7339efab4dff106fbde5caaa31bf0f658b74eca6691c`
- Text SHA256: `ca420c9b08d2a84d8e55484e335afd9e900247aca8215cda326e9a6fd83f8460`


## Content

---
title: "Setting Up Gitrob and using it to find Leaking Repository of an Employee in a hackerone private program."
url: "https://medium.com/@pig.wig45/setting-up-gitrob-and-using-it-to-find-leaking-repository-of-an-employee-in-a-hackerone-private-e4c40da1bc85"
authors: ["Sahil Tikoo (@viperbluff)"]
bugs: ["Information disclosure"]
publication_date: "2019-02-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5424
scraped_via: "browseros"
---

# Setting Up Gitrob and using it to find Leaking Repository of an Employee in a hackerone private program.

Setting Up Gitrob and using it to find Leaking Repository of an Employee in a hackerone private program.
Sahil Tikoo
Follow
4 min read
·
Feb 9, 2019

127

1

Press enter or click to view image in full size
Gitrob

The only reason I am blogging about this finding is to help guys who are facing difficulty in setting up Gitrob since it has been rewritten in Go and not many people out there are familiar with go.So, lets begin:

Few days back I got a private invite on hackerone and started with some reconnaissance, lets assume it as abc.com.So I started to manually lookup repositories linked to it by performing a general search on github.com as you can see below:-

Press enter or click to view image in full size
Searching Github[OSINT]

Next thing I thought was to give my task some touch of automation.The only tool that I could think about at that moment was none other than Gitrob.So I quickly went to https://golang.org/doc/install?download=go1.11.5.linux-amd64.tar.gz from where I was able to download the GO package for my linux machine.

Press enter or click to view image in full size
Go package for Linux

After Downloading it I extracted it in the /usr/local folder of my machine’s root directory.

tar -C /usr/local -xvzf go1.11.5.linux-amd64.tar.gz

Now the final step left was to setup environment variable for GO so that I could easily run commands like go get and go run from anywhere on my bash terminal.

To do this I had to make sure that my /usr/local/go/bin directory that contained my go executable is present in the $PATH environment variable which contains the list of directories where the system searches for executable programs, scripts, or files when you want to run a command directly from your shell.

Most of the time people directly set their executable’s path in $PATH by running export PATH=$PATH:/../../../path/to/executable in their shell but this doesn’t work if u open a new shell.

So to make sure that you have a persistant system wide installation of GO for all users follow below steps:-

1. cd /etc

2. nano profile

3. Add export PATH=$PATH:/usr/local/go/bin at the end of the file

4. ctrl+x the save the changes.

As of now I was ready to run go from my command line as you can see below:

Press enter or click to view image in full size
Running Go in bash

It was the time to fetch michenriksen’s repository so that I could now run gitrob on my machine

One thing to remember here is the `GOPATH` which is nothing but the default working directory of go.So, Once you install go this path will be automatically set to your $HOME/go directory for versions 1.7–1.11.

In case the above doesn’t work you can always follow the below steps:

Get Sahil Tikoo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Create a folder to store all programs written in Go and use go get to fetch Gitrob’s repository and get started with it.

1. mkdir $HOME/go

2.cd ~/go

3. mkdir bin src

4.nano /etc/profile

5. export GOPATH=$HOME/go

6. export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

7. Save changes made to the profile with source /etc/profile

8. go get github.com/michenriksen/gitrob

Now you have the Gitrob’s repository cloned in your go directory , checkout the final steps shown in the image below:-

Press enter or click to view image in full size

Now I just ran go run main.go -github-access-token 1234 abc

Replace 1234 with your github access token and where abc is the name we gave to our private program.You can go through this link[https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/] and find out how to generate your github access token.

After few minutes I got a lot of findings in which one of them got my attention , it’s shown in the image below:-

Press enter or click to view image in full size
shell config file

So, First I confirmed that whether the author was the company’s employee or not?I searched the author’s name on Linkedin and found that the person was a software developer in that company.Next step was to parse the .zshrc file for some sensitive data.

Once I opened Up that .zshrc file in the dotfiles folder I found multiple Psql commands that contained the names of some aws instances and One Okta Api key using which I could get a SSO to all the accounts of that person which included abc as well[thought so].BINGO!!!

Okta Api Key can be seen in the Image below:-

Press enter or click to view image in full size
Okta Api Key Leakage

Postgresql Commands for Aws instances can be seen below:-

Press enter or click to view image in full size
Psql commands in shell config file

At last I reported this issue to the private program, they took down the repository but it wasn’t eligible for a bounty , you can find the reason mentioned in the below image:-

Press enter or click to view image in full size
Hackerone response

Happy Hacking !!!

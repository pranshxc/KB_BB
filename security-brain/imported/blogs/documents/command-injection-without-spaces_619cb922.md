---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-10-02_command-injection-without-spaces.md
original_filename: 2016-10-02_command-injection-without-spaces.md
title: Command Injection Without Spaces
category: documents
detected_topics:
- command-injection
- otp
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- api-security
- supply-chain
language: en
raw_sha256: 619cb9226ec50b7dd91cedbe17dc487775da45813631698f9e303a47743133fe
text_sha256: b9633290b96f3cbe3aa263fe919bfafb656e3c8f092dcd6908a8f649c3cceb15
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Command Injection Without Spaces

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-10-02_command-injection-without-spaces.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `619cb9226ec50b7dd91cedbe17dc487775da45813631698f9e303a47743133fe`
- Text SHA256: `b9633290b96f3cbe3aa263fe919bfafb656e3c8f092dcd6908a8f649c3cceb15`


## Content

---
title: "Command Injection Without Spaces"
url: "https://www.betterhacker.com/2016/10/command-injection-without-spaces.html"
final_url: "https://www.betterhacker.com/2016/10/command-injection-without-spaces.html"
authors: ["Fyoorer (@ƒyoorer)"]
bugs: ["OS command injection"]
publication_date: "2016-10-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6252
---

###  Command Injection Without Spaces 

[ October 02, 2016  ](https://www.betterhacker.com/2016/10/command-injection-without-spaces.html "permanent link")

I came across a nice little command injection vulnerability while doing a bug bounty recently. The only catch was that I couldn't use any spaces in the commands. Let me go into the details...  
  
Note: I can't post any details about the application as it was a private bounty program.  
  
It all began with the page providing an input box for doing 'nslookup' of a domain or IP entered by the user.  
A page like this always excites a bug bounty hunter as the application has to pass user's input to underlying system command to perform nslookup and present the output of that command in the browser. If the developer has made any mistake in validating and sanitizing the input, they inadvertently open the doors to attackers misusing this feature to execute arbitrary commands on the server.  
  
So, when I saw the input box I started to explore and try to force the application in executing arbitrary commands.  
I began with simple input google.com  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvTPsYHnNVlST1Vz6_M9uxo40mJzP9LM1Vza3UvDRNE4fieuhBXkkRqNnteUhcl5QncXtPtASfBCUi700UKp5PSlsjzlP_Ifn-q84nXg8UK3v1QYm0xZIelBsY3o29yeJ-mVKiMQZ9iHc/s640/blog-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvTPsYHnNVlST1Vz6_M9uxo40mJzP9LM1Vza3UvDRNE4fieuhBXkkRqNnteUhcl5QncXtPtASfBCUi700UKp5PSlsjzlP_Ifn-q84nXg8UK3v1QYm0xZIelBsY3o29yeJ-mVKiMQZ9iHc/s1600/blog-1.png)

  
My next automatic try was to input google.com && ls  
This returned same output as above, meaning the application ignored additional command provided by me. The same story continued for all my tries such as google.com || ls  
When I tried input google.com>/tmp/test.txt the output window came blank which was strange. This suggested maybe the application is filtering spaces so I tried the same commands but without spaces and...  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvpZ5wTtxI_hcaq5ucaSUv6xlxwDYlyKkMbZXrl7V4Rbfj5CrkU5VrhGE3nnKIZVUc4CPkwFNO7stplp-iHWQqCKLoTsBoXhn4wMQosonWuOjYjWWVlPq7YLcW6ctIGJKwLVZyNZVPbWw/s640/blog-2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhvpZ5wTtxI_hcaq5ucaSUv6xlxwDYlyKkMbZXrl7V4Rbfj5CrkU5VrhGE3nnKIZVUc4CPkwFNO7stplp-iHWQqCKLoTsBoXhn4wMQosonWuOjYjWWVlPq7YLcW6ctIGJKwLVZyNZVPbWw/s1600/blog-2.png)  
---  
Success!  
But the problem with spaces was still not solved. For the input google.com&&cat /etc/passwd the application again ignored anything after the space.  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOSuwjqSP1M1zITTynHFIHZOxOj8PpQJPtpW58JJgddH8FlcigBIvaaQqw2GHMUX1XfOpuWulURlDbgBOcUxilFwV3ioRt1vjbqDp1gNoF4eKxXbx1JnMehxdHPlBH2K-LgMRcpmZ-p5M/s640/blog-3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOSuwjqSP1M1zITTynHFIHZOxOj8PpQJPtpW58JJgddH8FlcigBIvaaQqw2GHMUX1XfOpuWulURlDbgBOcUxilFwV3ioRt1vjbqDp1gNoF4eKxXbx1JnMehxdHPlBH2K-LgMRcpmZ-p5M/s1600/blog-3.png)  
---  
:(  
  
Then my next obvious move was to search on Google for this issue because if I am facing this issue, somebody must have already faced similar situation. Needless to say, Google didn't disappoint.  

  

Enter "[Bash Brace Expansion](https://jon.oberheide.org/blog/2008/09/04/bash-brace-expansion-cleverness/)". 

According to this, if you provide input like following on the bash terminal: {echo,hello,world} it will execute the command echo hello world  

That was neat and TIL moment for me.

I tried it in my application but that didn't succeed. Maybe because the application I was targeting was an embedded device and the shell was a busybox shell. On more Googling, my doubt was [confirmed](http://lists.busybox.net/pipermail/busybox/2011-July/076170.html).

  
So I was again back to Google looking for different solution. Then I came across this thread - <http://seclists.org/pauldotcom/2012/q2/200>

According to this, you can execute commands without spaces like this: CMD=$'\x20a\x20b\x20c';echo$CMD

  

Look at the cleverness of that! More TIL!

Here, CMD is an environment variable containing encoded spaces. On running that we get echo a b c

  

Now, I tried that in my application with little modification CMD=$'\x20a\x20b\x20c'&&echo$CMD

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgth_vX2lVoRUlxOH5utvgooRePwkdnzcJ5xaWaiNLHNBpe1odtHwC2uPPTTqPjLi6m-Uq1yIIhjTPQmnoj0bu6j_Y9G1lJo3pTZ-tCOsaYd1_WSqk0ZUMNhdLmZj7vEuUqiCxGBwZ0B7w/s640/blog-4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgth_vX2lVoRUlxOH5utvgooRePwkdnzcJ5xaWaiNLHNBpe1odtHwC2uPPTTqPjLi6m-Uq1yIIhjTPQmnoj0bu6j_Y9G1lJo3pTZ-tCOsaYd1_WSqk0ZUMNhdLmZj7vEuUqiCxGBwZ0B7w/s1600/blog-4.png)  
---  
Bingo!  
  
  

From here, executing arbitrary commands was a cakewalk. Input google.com&&CMD=$'\x20/etc/passwd'&&cat$CMD  

  
  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX6ZotpC-lVwNvfm-C1CVfl4Mw7lfWV6EXhlgEcqVKo35qlzHsm8DKvw9BlOr8wF_Wx8mMzWY4AZhSKn76UsKUsRUWKdBmU3GvNMXimlsLU1mZytaGzCD-fDcLwScGArtViHMwDp6ryTo/s640/blog-5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX6ZotpC-lVwNvfm-C1CVfl4Mw7lfWV6EXhlgEcqVKo35qlzHsm8DKvw9BlOr8wF_Wx8mMzWY4AZhSKn76UsKUsRUWKdBmU3GvNMXimlsLU1mZytaGzCD-fDcLwScGArtViHMwDp6ryTo/s1600/blog-5.png)  
---  
/etc/passwd  
  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[brace expansion](https://www.betterhacker.com/search/label/brace%20expansion) [bugbounty](https://www.betterhacker.com/search/label/bugbounty) [busybox](https://www.betterhacker.com/search/label/busybox) [command execution](https://www.betterhacker.com/search/label/command%20execution) [os command injection](https://www.betterhacker.com/search/label/os%20command%20injection) [trick](https://www.betterhacker.com/search/label/trick)

Labels: [brace expansion](https://www.betterhacker.com/search/label/brace%20expansion) [bugbounty](https://www.betterhacker.com/search/label/bugbounty) [busybox](https://www.betterhacker.com/search/label/busybox) [command execution](https://www.betterhacker.com/search/label/command%20execution) [os command injection](https://www.betterhacker.com/search/label/os%20command%20injection) [trick](https://www.betterhacker.com/search/label/trick)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[October 17, 2016 at 12:27 PM](https://www.betterhacker.com/2016/10/command-injection-without-spaces.html?showComment=1476687447535#c675389712869549914)

may I ask if this qualified for a bounty/reward? Thanks

Reply[Delete](https://www.blogger.com/comment/delete/4538251661335272060/675389712869549914)

Replies

Reply

  2. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[October 17, 2016 at 12:28 PM](https://www.betterhacker.com/2016/10/command-injection-without-spaces.html?showComment=1476687480732#c249618630270901422)

may I know if this qualified for bounty under Google VRP? Thanks

Reply[Delete](https://www.blogger.com/comment/delete/4538251661335272060/249618630270901422)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[[write me an essay online](http://www.huffingtonpost.com/ursula-nwobu/write-my-essay-the-new-bu_1_b_11451790.html)](https://www.blogger.com/profile/14269657111903821428)[September 15, 2017 at 5:35 PM](https://www.betterhacker.com/2016/10/command-injection-without-spaces.html?showComment=1505477122852#c6473900957475390940)

nice

Reply[Delete](https://www.blogger.com/comment/delete/4538251661335272060/6473900957475390940)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/4538251661335272060?po=4421149241472102893&hl=en&saa=85391&origin=https://www.betterhacker.com&skin=notable)

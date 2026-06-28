---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-29_bugbounty-how-i-was-able-to-bypass-firewall-to-get-rce-and-then-went-from-server.md
original_filename: 2018-04-29_bugbounty-how-i-was-able-to-bypass-firewall-to-get-rce-and-then-went-from-server.md
title: '#BugBounty — How I was able to bypass firewall to get RCE and then went from
  server shell to get root user account!'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: a1518e0463e38cde92cfbd6d1fb7bd382d6fbfe60d549e8ef598d34c3eb917ad
text_sha256: ecd3ef71b5202d2078337bfa1d98c9cd58ea0763dfe67e899164c78d33154aac
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — How I was able to bypass firewall to get RCE and then went from server shell to get root user account!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-29_bugbounty-how-i-was-able-to-bypass-firewall-to-get-rce-and-then-went-from-server.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `a1518e0463e38cde92cfbd6d1fb7bd382d6fbfe60d549e8ef598d34c3eb917ad`
- Text SHA256: `ecd3ef71b5202d2078337bfa1d98c9cd58ea0763dfe67e899164c78d33154aac`


## Content

---
title: "#BugBounty — How I was able to bypass firewall to get RCE and then went from server shell to get root user account!"
page_title: "#BugBounty — How I was able to bypass firewall to get RCE and then went from server shell to get root user account! | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-how-i-was-able-to-bypass-firewall-to-get-rce-and-then-went-from-server-shell-to-get-783f71131b94"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["RCE"]
publication_date: "2018-04-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5895
scraped_via: "browseros"
---

# #BugBounty — How I was able to bypass firewall to get RCE and then went from server shell to get root user account!

#BugBounty — How I was able to bypass firewall to get RCE and then went from server shell to get root user account!
Avinash Jain (@logicbomb)
Follow
5 min read
·
Apr 29, 2018

977

6

Hi Guys,

This vulnerability blog is about when Apache struts2 CVE-2013–2251 went viral and was getting highly exploited because of the impact of vulnerability which was leading to execution of remote commands. In short it was — A vulnerability introduced by manipulating parameters prefixed with “action:”/”redirect:”/”redirectAction:” allows remote command execution in the java web application using < Struts 2.3.15 as a framework.

Now when this loophole went viral, major application firewall companies started updating their rule engines and detection technique in order to prevent it from happening which was a pretty obvious and responsible thing. But I was not only able to bypass the firewall and get the remote code execution but also able to get the shell of the server and that too as root user by exploiting kernel CVE. :)

Let’s see what was the complete hack —

This comes when I was testing for a travel booking website. As it was very clear in order to find whether the application is running over vulnerable Apache Struts framework , you have to simply check for the following vulnerable parameters — “action, redirect,redirectAction” and for the right payload, I google’d a little (as for this, I have to construct an OGNL expression) and this helped me a lot-http://blog.opensecurityresearch.com/2014/02/attacking-struts-with-cve-2013-2251.html , below is the payload used to run the command “ifconfig”

redirect:${#a=(new java.lang.ProcessBuilder(new java.lang.String[]{‘ ifconfig’})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#matt=#context.get(‘com.opensymphony.xwork2.dispatcher.HttpServletResponse’),#matt.getWriter().println(#e),#matt.getWriter().flush(),#matt.getWriter().close()}

Press enter or click to view image in full size
OGNL Expression to run command

but as expected , it was blocked by the application firewall , and redirected me to a bots page-

Press enter or click to view image in full size
Blocked by Application Firewall- Redirected to Bots page

and when anything like this happens to me, I always return to the basics. So as pointed out earlier, I knew that which all parameters were vulnerable and one of them was “redirect” which I used in the above request. “Redirect” , yes you felt it right , let’s try for some redirection here and I simply put redirect:http://www.goal.com -

Press enter or click to view image in full size
redirect request

and as you can see I got 302 redirection to location”http://www.goal.com :) and so my earlier “ifconfig” payload got blocked and this redirection worked , this gave an idea to bypass the firewall and so , I combined both the above payload-

redirect:http://www.goal.com/${#a=(new java.lang.ProcessBuilder(new java.lang.String[]{‘ ifconfig’})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[50000],#d.read(#e),#matt=#context.get(‘com.opensymphony.xwork2.dispatcher.HttpServletResponse’),#matt.getWriter().println(#e),#matt.getWriter().flush(),#matt.getWriter().close()}

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

and fired the request-

Press enter or click to view image in full size

Time for some cheer as I was able to bypass the firewall and got the “ifconfig” command output running :)

Press enter or click to view image in full size
ifconfig command output

Now the next target was to get the remote shell of the server and I tried it using reverse ssh tunneling and public key authentication which allow SSH users to login in without entering passwords. For this I had to put my attacker server ssh public key in the victim server’s authorization list~/.ssh/authorized_keys. in order to prove the identity and as this going to be a reverse ssh tunnel , I had to add id_rsa.pub key of the victim ssh server as well. In order to define the concept of above 2 keywords in short and understand the concept of public key authentication—

id_rsa.pub is a public key that you add to other hosts' authorized_keys files to allow you to log in as that user. authorized_keys is a list of public keys that are allowed to log into that specific account on that specific server.

1st Step- Cat the id_rsa.pub file of the victim server using RCE

Press enter or click to view image in full size
id_rsa.pub file

2nd Step- Copy the authorized_keys from victim server to attacker server

Press enter or click to view image in full size
Copy the authorized_keys from victim server to attacker server

3rd Step- Copy back the modified authorized_keys from attacker server to victim which I got by reading id_rsa.pub

Press enter or click to view image in full size
Copy back the modified authorized_keys from attacker server to victim

Now the final step — SSH using the reverse tunnel on attacker machine so I ran the command-

Press enter or click to view image in full size
SSH using reverse tunnel

Pheww! Able to reach to the remote shell of server. :) but I was not logged in as a root that means I could have only limited right and access to files and commands. Now in order to logged in as root user, firstly I found out what was the current kernel version running on victim machine and it was -

Press enter or click to view image in full size
kernel version

So the kernel version found to be 2.6.32 which I google’d in order to find if there was any open CVE against this and to my luck, I found that it was vulnerable to privilege escalation and exploit was over github too — https://github.com/realtalk/cve-2013-2094 . Without wasting much time, I ran the exploit.

Press enter or click to view image in full size
Running the exploit

and finally I was able to get privilege escalation to the root user! :) and this is how the chain to get the remote shell of the server as a root user by exploiting apache strut 2 vulnerability and kernel version exploit ends. Thanks to Kunal Aggarwal for all the mutual efforts!

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )

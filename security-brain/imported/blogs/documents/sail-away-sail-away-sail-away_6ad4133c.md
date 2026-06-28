---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-21_sail-away-sail-away-sail-away.md
original_filename: 2022-10-21_sail-away-sail-away-sail-away.md
title: Sail away, sail away, sail away
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 6ad4133c502388bcf84372480fd0dfdd801d1b87d57f91123dc2c7e07dfc925e
text_sha256: 8888b612c3343c0e5fd5d4e67bc150c1bf26d274d7fb0c3ba7c3996d1f24cd4b
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Sail away, sail away, sail away

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-21_sail-away-sail-away-sail-away.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `6ad4133c502388bcf84372480fd0dfdd801d1b87d57f91123dc2c7e07dfc925e`
- Text SHA256: `8888b612c3343c0e5fd5d4e67bc150c1bf26d274d7fb0c3ba7c3996d1f24cd4b`


## Content

---
title: "Sail away, sail away, sail away"
page_title: "SensePost | Sail away, sail away, sail away"
url: "https://sensepost.com/blog/2022/sail-away-sail-away-sail-away/"
final_url: "https://sensepost.com/blog/2022/sail-away-sail-away-sail-away/"
authors: ["Reino Mostert"]
bugs: ["RCE", "Privilege escalation"]
publication_date: "2022-10-21"
added_date: "2022-10-22"
source: "pentester.land/writeups.json"
original_index: 2007
---

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/69ba0de8f95b1350afa2e9cd152a1dd6.jpg)](/img/pages/blog/2022/sail-away-sail-away-sail-away/bf35e7e6d4d23eff4965c3c0053a11ed.jpg)

A while back, after some live music and drinks at Railways, I made my way to another city for pleasant weather, some dubious food, the ever-wakeful seagulls, and ultimately – an assessment.

After playing around for a few days, Jason and I had obtained access to a system which contained cleartext credentials, namely **ihsadmin:ihsadmin**.

Using these credentials, we were also able to SSH into a management server of sorts. While this was great, there were still several other servers in-scope that we had no access to. After scanning the network for a bit, I found out that a couple of these servers ran HTTP services on port 80, 8008 and 9080.

When I accessed the service on port 8008 on one of these servers using Firefox, I was greeted with a basic HTTP auth box, asking for credentials to “IBM Administration Server”.

As luck would have it, the **ihsadmin:ihsadmin** credentials worked. However, instead of logging me into an a nice graphical administrative portal, it showed an error message on a somewhat bland page:

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/ad62397271499861b5fafcaebb39d378.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/ad62397271499861b5fafcaebb39d378.png)

After decoding this error message for a while, I realized a couple of things:

  * I had successfully authenticated to some administrative endpoint. 
  * The administrative endpoint was implemented by the **mod_ibm_admin** module.
  * I had not provided all the required headers. Specifically, the **Command** and **Arguments** headers were missing.
  * I was dealing with some system/implementation called **SAIL**.

I searched for the error message, the words **SAIL** , **IBM Administration Server** and **mod_ibm_admin** to get more information, even going as far as to check page 2 of the Google results. This didn’t really reveal a lot, but I learned that:

  * I was dealing with an IBM HTTP Server (IHS), which seems to be IBM’s fork of Apache.
  * The main use of IHS is to serve static HTML or do load balancing.
  * IHS is different from IBM **WebSphere** , which is instead used to serve dynamic Java web applications.
  * The administrative interface that runs on port 8008 is used to manage the IBM HTTP Server, however it has no graphical interface.
  * Instead, admins were supposed to use the administrative console of a **WebSphere** instance to manage the IBM HTTP Server via its administrative interface.

This was a bit vexing, as I didn’t have a copy of IBM’s **WebSphere** laying around, so I couldn’t use it to manage the IBM HTTP Servers, even though I had valid credentials. 

I tried for quite a while to guess the **Command** and **Arguments** headers that IHS’ administrative interface wanted, without any success.

However, as luck would have it , the server that we had already compromised had a copy of IHS installed, including the **mod_ibm_admin.so** module that implemented the administrative interface.

I copied this file off, and opened it up in **Ghidra and IDA,** with the hope that I would be able to reverse engineer it a bit. Specifically, I wanted to know what **headers** it needed to work, what commands I could run, and what **arguments** I needed to provide.

Some time later, I found the code responsible for processing incoming HTTP requests. It contained references to two headers, **SAILCmd** and **SAILArgs** :

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/23b648f10c3fa581b6ac4a3bd5167d2f.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/23b648f10c3fa581b6ac4a3bd5167d2f.png)

Looking around a bit more, I found which commands the interface supported.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/d91154195b01cce15984995a29c1b3b4.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/d91154195b01cce15984995a29c1b3b4.png)

Some more digging in IDA around revealed what these commands did:

  * ReadFile – Allows you to read a file on the web server.
  * WriteFile – Allows you to write a file to the web server.
  * ServerControl – Allows you to stop, start, restart and query the status of the IHS process.
  * NumberOfLines – Allows you to determine how many lines there are in a file. Useful for an argument in the ReadFile function, I guess?
  * ExpandMachine – Seems to be an empty command that doesn’t do anything. I might be wrong.

The next thing I needed to know was how the arguments worked for the different commands. I first focused on the **ReadFile** command, whose argument structure seemed to be similar to URL parameters, with a key (parameter) followed by an = sign and the value. Different parameters were separated by an &. The **src** parameter seemed to refer to the path of file that should be read, while the **linestart** and **lineend** parameters specified which lines should be read. The line parameters seemed optional.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/575f476f46e8d748623ae9160fbc1724.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/575f476f46e8d748623ae9160fbc1724.png)

Having put these puzzle pieces together, I sent off a command to read the **/etc/passwd** file on the remote IHS web server. The sever sent back the file’s contents.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/4d4abf5f3123e41e039f7cc2ffe7f9f2.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/4d4abf5f3123e41e039f7cc2ffe7f9f2.png)

Having tasted success, I tried invoking the rest of the commands. 

For the **NumberOfLines** command to work, you simply needed to specify the filename within the **SAILArgs** header. It simply returned the number of lines a file had.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/5cf3b95a8877655c26804f07c84c0cf4.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/5cf3b95a8877655c26804f07c84c0cf4.png)

The WriteFile command was a bit more interesting. For this command to work, you needed to specify the path of file you want to write to in the **SAILArgs** header. The data you wanted to put in the file was simply put in the body of the request. Strangely this needed to be a GET request. 

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/b6d4918c2a1d315d488e56cacb9b2ed6.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/b6d4918c2a1d315d488e56cacb9b2ed6.png)

Having gained the ability to write files, I wanted to upload a web shell to take over the web server. IHS however mostly serves static HTML content, so my JSP/PHP webshell wouldn’t work. Luckily, IHS still supports CGI. After a couple of attempts, I uploaded a working CGI web shell. I had to overwrite an exiting CGI script, so that the file would have the execution bit set, else it wouldn’t run.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/eeda8671200484abeeaf372f59687eae.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/eeda8671200484abeeaf372f59687eae.png)

Executing **id** with the CGI web shell revealed that I was executing as the **nobody** user, which by design doesn’t have much access.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/997274a0abdb3f0af884fa03ce8a0a1e.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/997274a0abdb3f0af884fa03ce8a0a1e.png)

At this point I wanted to escalate my access a bit. A task listing showed that some of the IHS services were running as root, so I have a further look at the administrative interface, specifically the last command **ServerControl**. 

IDA revealed that this administrative interface originally runs as root, which we will refer to as the root process for now. The root process starts a unprivileged process, which is in charge of receiving and processing the commands, like **WriteFile** , **ReadFile** and **ServerControl**.

The **ServerControl** command, however needs to do things as the root user, such as restarting the IHS process. To facilitate this, the root process creates a socket to which the unprivileged process can write to. When the unprivileged process gets a **ServerControl** command, it writes to socket. The root process then reads from the socket, and runs the required command.

IDA also revealed that the **SAILArgs** header for **ServerControl** command could be set to either **stop** , **start** , **restart** or **status**.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/30da4ea118ea4fad86db9a9b0de42b25.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/30da4ea118ea4fad86db9a9b0de42b25.png)

The **ServerControl** command also required two extra headers, **InstallRoot** and **CfgFile** , which were set to the path of the installation root folder of the IHS server, and its configuration file.

This gave me an idea – perhaps I could write a new configuration file which would specify that the IHS server should run as the root user, instead of the nobody user. This would provide my CGI web shell with root access. To make sure the new configuration file takes effect, I would restart the IHS server using the **ServerControl** command.

Below I used the **WriteFile** command to upload the modified config file:

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/1eda826c69b354d37790970ca36da15e.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/1eda826c69b354d37790970ca36da15e.png)

I then used the SeverControl command to stop the IHS server.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/19eecfed4ff7ead6f7e2fcd8ba12c589.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/19eecfed4ff7ead6f7e2fcd8ba12c589.png)

Unfortunately, the server did not want to start again. After a moment of stress, I changed the configuration file again to rather start as the user who owned the IHS’ directory and files. We will refer to this user as **bob** , which was created by the customer, and isn’t default. 

This time the **ServerControl** command worked, and IHS started as the **bob** user. As a result, the CGI web shell now ran as **bob**.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/a52d9ebe15ee984516e6a5f622a861a4.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/a52d9ebe15ee984516e6a5f622a861a4.png)

This was nice, but it wasn’t root. Using the CGI web shell, I uploaded my SSH key to the server so that I could login as **bob** via SSH.

While looking at the **ServerControl** command in IDA, I noticed that the root process was actually calling the Unix **apachectl** command to stop, start and restart IHS. As luck would have it, the **bob** user owned the **apachectl** command.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/061b351f65ff7012ed68f155dc2a7778.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/061b351f65ff7012ed68f155dc2a7778.png)

Using my SSH shell, I swapped out the **apachectl** command with a shell script that would grant the **bob** user, root access via sudo.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/87ec5fc7e9afe88d4ab190561a6d8263.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/87ec5fc7e9afe88d4ab190561a6d8263.png)

I then called the **ServerControl** command again, which would execute the new **apachectl** command as root.

Following on this, I was able gain root access via sudo.

[![](/img/pages/blog/2022/sail-away-sail-away-sail-away/6543d3cbdb042f010e424831996d3bc6.png)](/img/pages/blog/2022/sail-away-sail-away-sail-away/6543d3cbdb042f010e424831996d3bc6.png)

I’m still looking in IDA to see if there are any vulnerabilities that would allow me to get root in another way. In any case, if you ever encounter IHS servers in the wild, try using this approach to get root.

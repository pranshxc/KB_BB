---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-24_vocera-report-server-pwnage.md
original_filename: 2023-04-24_vocera-report-server-pwnage.md
title: Vocera Report Server Pwnage
category: documents
detected_topics:
- command-injection
- file-upload
- path-traversal
- sso
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- path-traversal
- sso
- api-security
language: en
raw_sha256: 55ce476c5ffea490c8440a09b443466cbdeb025a46b1f28836ae28ef60beaf01
text_sha256: 3ba98a712802c31945bece4cdc566d23e0d8f5ec84a113a5f6a8c18b33383e0f
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Vocera Report Server Pwnage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-24_vocera-report-server-pwnage.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, path-traversal, sso, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `55ce476c5ffea490c8440a09b443466cbdeb025a46b1f28836ae28ef60beaf01`
- Text SHA256: `3ba98a712802c31945bece4cdc566d23e0d8f5ec84a113a5f6a8c18b33383e0f`


## Content

---
title: "Vocera Report Server Pwnage"
page_title: "Vocera Report Server Pwnage – Securifera"
url: "https://www.securifera.com/blog/2023/04/24/vocera_report_server_pwnage/"
final_url: "https://www.securifera.com/blog/2023/04/24/vocera_report_server_pwnage/"
authors: ["b0yd (@rwincey)"]
programs: ["Stryker"]
bugs: ["RCE", "Arbitrary file upload", "Path traversal", "Zip Slip attack"]
publication_date: "2023-04-24"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1227
---

Vocera Report Server Pwnage

![](https://www.securifera.com/wp-content/uploads/2023/04/vocera.png)

### **This article is in no way affiliated, sponsored, or endorsed with/by Vocera Communications or Stryker Corporation. All graphics are being displayed under fair use for the purposes of this article.**

## **Quest for RCE**

### Last year during a routine penetration test, our team came across a interesting target called Vocera Report Server while reviewing web endpoint screenshots.

![](https://www.securifera.com/wp-content/uploads/2023/04/vocera-1.png)

### A little research revealed that the “[Vocera Report Server software and the associated report console interface provide administrators, managers, and decision makers the ability to monitor system performance and generate reports for analysis](https://www.vocera.com/resource/data-sheets/vocera-report-server)” for the Vocera Communication System. When we click on the “Vocera Report Console” link we are greeted with the following login page.

![](https://www.securifera.com/wp-content/uploads/2023/04/report_console.png)

### Step 1: head over to Google to see if we can find any documentation that might list default credentials for the application. As luck would have it, this [page](https://pubs.vocera.com/vrs/vrs_5.2.2/docs/ReportGuide.pdf) comes up and kindly tells us what the default password would be.

![](https://www.securifera.com/wp-content/uploads/2023/04/login_pw.png)

### Fortunately the system owner didn’t change the password and we log right in. Once inside we start perusing the various endpoints to get a feel for what the application is used for. Right off, the first thing that stands out is the menu that is named “Task Scheduler”. Clicking on the menu brings up a panel that appears to let you create tasks that will be executed.

![](https://www.securifera.com/wp-content/uploads/2023/04/task_scheduler.png)

### After tinkering with the various tasks, it appears we can only edit existing tasks. We also can’t seem to get arbitrary command execution or injection by modifying the existing entries. At this point we decided it would likely be more fruitful to move on to a white box approach and see what the code is actually doing. We reached out to a colleague to get us access to the server using some credentials they had cracked after pulling the hash with Responder.

### Since the application is written in Java, we open up the class files in [JD-GUI](http://java-decompiler.github.io/) to begin analyzing the function responsible for executing tasks. The first issue we notice is that the function that parses the user-controlled task execFileName attempts to retrieve the filename portion of the path by searching for the last occurrence of a backslash. Unfortunately in Java, forward slashes are automatically normalized into directory separators in a file path. This means we can traverse out of the intended directory.

![](https://www.securifera.com/wp-content/uploads/2023/04/exec_task.png)

### While the path to the executable task is controllable, a check is performed that ensures that the file contains the word “java” before executing. This means if we can control the contents of a file on disk, we can execute arbitrary commands.

![](https://www.securifera.com/wp-content/uploads/2023/04/java_check.png)

### How then do we get a file on disk that we control? What if we can affect the log file? It looks like if an exception happens when executing the task, a log entry is created.

![](https://www.securifera.com/wp-content/uploads/2023/04/vocera_log.png)

### Sure enough, if we specify a task execfilename that doesn’t exist, an entry is created in the log file that also includes the task parameters that we can inject arbitrary data. With a little creativity, we are able to inject arbitrary commands and then point to the log file using the directory traversal to achieve remote code execution.

![](https://www.securifera.com/wp-content/uploads/2023/04/code_exec.png)

## **Can we do better?**

### With a path to execute arbitrary commands identified, we shifted our focus to finding a way to accomplish the same thing but without having to authenticate first. While investigating the task execution code in the previous exercise, we noticed there is a websocket interface that the web server communicates with when executing a task. After some testing it was determined that this interface was unauthenticated. In addition to the “runTaskPage” function mentioned above, there are a few other operations that appear to be related to database management functions that are worth investigating.

![](https://www.securifera.com/wp-content/uploads/2023/04/ws_funcs.png)

### If we look at the code for the restoreSqlData operation we see that it executes a bat file that in turn executes another Java JAR. Inside that JAR, the function that handles the restoreSqlData operation parses the “uploadFile” parameter and appends it to the local “backupDir”. This instance is also vulnerable to directory traversal like the one mentioned previously.

![](https://www.securifera.com/wp-content/uploads/2023/04/sql_dirtrav.png)

### The specified file is expected to be a zip file that is then programmatically unzipped and written to disk. The problem, as you could probably guess, is the unzip function is vulnerable to directory traversal which could lead to an arbitrary file write. If the unzip succeeds, a particular file is read from the archive that is then used to completely overwrite the database. **DANGER: THIS OPERATION OVERWRITES THE DATABASE SO ADDITIONAL MEASURES NEED TO BE TAKEN TO PREVENT THIS.**

![](https://www.securifera.com/wp-content/uploads/2023/04/unzip.png)

### Since this server hosts a web server and is running as SYSTEM, an arbitrary file write can be used to achieve remote code execution by writing a webshell in the webroot. To summarize, in this instance we have found an unauthenticated endpoint that allows for a privileged file write if we can place an arbitrary file somewhere on the file system. We lack one more primitive to pull off this exploit. Back to the code!

### Given the specific requirement for a file write, we search for any references to “write” and work our way back to any web endpoints that would reach that code. This concept is often referred to as **_source_ **to _**sink** _data flow analysis. After some time we find a class called _**MultipartRequest**_. This class is instantiated from an incoming **_multipart/form-data_** request. If the requests contains any parameters that are named _**filename**_ , the data is read and written to a file in a temp folder.

![](https://www.securifera.com/wp-content/uploads/2023/04/multipart.png)

### If we search for references of RequestContainer, the class responsible for creating MultipartRequest instances, we see it is created by the BaseController class on the handling of each HTTP request. Since BaseController is an abstract class, we search for any child classes and find ReportController. This is perfect since ReportController is the primary endpoint for the application. This means if we send an HTTP request with _**Content-Type**_ multipart/form-data to the ReportController endpoint, the contents of any parameters with a _**Content-Disposition**_ that contains a filename will be written to disk in a temp directory. This best part is this is all unauthenticated (another bug)!

![](https://www.securifera.com/wp-content/uploads/2023/04/arb_upload.png)

### Now we have all the pieces necessary to construct an exploit chain to gain unauthenticated remote code execution on the Vocera Report Server. First we construct a malicious zip file with a webshell embedded with a directory traversal path. Next we upload a zip file to the temp directory with a multipart request. Finally we send a websocket request with the restoreSqlData operation with a directory traversal path to our uploaded zip file.

## **WAIT!!! HOW DO I NOT CLOBBER THE DATABASE?!?!**

### As much as any customer likes red teamers proving exploitation, nuking an application’s database is probably not a reasonable loss to prove code execution. That means we needed to put in a little more effort into the exploit to avoid this. If we look at the SQL restore function, we can see that if a ZipException is thrown (that is not a version issue), the function will bail out.

![](https://www.securifera.com/wp-content/uploads/2023/04/zip_error.png)

### How then do we cause a ZipException while also successfully executing our arbitrary file write? If we look at the [JDK source code for ZipInputStream](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/zip/ZipInputStream.java#L522) we can see a simple way to cause a ZipException to be thrown from a specific ZipEntry. If we set the first bit of the flag field in the ZipEntry a ZipException will be thrown since encryption is not supported.

![](https://www.securifera.com/wp-content/uploads/2023/04/zip_stream.png)

### If we lookup the offset for [LOCFLG](https://github.com/openjdk/jdk/blob/0deb648985b018653ccdaf193dc13b3cf21c088a/src/jdk.zipfs/share/classes/jdk/nio/zipfs/ZipConstants.java#L81) we see it is at index 6 in the ZipEntry header. We can code up some python to modify the zip entry contents after we zip up our payload as shown below.

Copy to Clipboard

Syntax Highlighter# This function intentional adds a second entry that is marked as encrypted # so the zip loop will throw an exception after the Zip slip exploit def build_zip(wsh_endpoint, file_contents): f = BytesIO() z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED) z.writestr( '/../../tomcat/webapps/ROOT/%s' % wsh_endpoint, # outfile file_contents) # contents z.writestr( 'exception.txt', # outfile '') # contents z.close() # Zip contents zip_contents = f.getvalue() idx = zip_contents.find(b'\x50\x4B\x03\x04', 4) flag_idx = idx+6 zip_array = bytearray(zip_contents) zip_array[flag_idx] = 1 zip_contents = bytes(zip_array) return zip_contents

## **Vendor Disclosure & Patch**

### I reported these issues through the [Stryker vulnerability disclosure program](https://www.stryker.com/us/en/about/governance/cyber-security.html) and can say everything went smoothly and they worked with us to get the issues fixed and patched in a reasonable time frame. Given the severity of these findings, we strongly encourage anyone that has Vocera Report Server deployed to update to the latest version immediately. For tracking purposes, the vulnerabilities discussed here represent CVE-2022-46898, CVE-2022-46899, CVE-2022-46900, CVE-2022-46901, and CVE-2022-46902.

By [b0yd](https://www.securifera.com/blog/author/b0yd/)|2024-04-15T14:25:43+00:00April 24th, 2023|[BUG BOUNTY](https://www.securifera.com/blog/category/bug-bounty/), [EXPLOITS](https://www.securifera.com/blog/category/exploits/), [PENTESTING](https://www.securifera.com/blog/category/pentesting/)|[0 Comments](https://www.securifera.com/blog/2023/04/24/vocera_report_server_pwnage/#respond)

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&t=Vocera%20Report%20Server%20Pwnage "Facebook")[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&text=Vocera%20Report%20Server%20Pwnage "X")[Reddit](https://reddit.com/submit?url=https://www.securifera.com/blog/2023/04/24/vocera_report_server_pwnage/&title=Vocera%20Report%20Server%20Pwnage "Reddit")[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&title=Vocera%20Report%20Server%20Pwnage&summary=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Vocera%20Communications%20or%20Stryker%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0AQuest%20for%20RCE%20%0D%0ALast%20year%20during%20a%20routine%20penetration "LinkedIn")[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&name=Vocera%20Report%20Server%20Pwnage&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Vocera%20Communications%20or%20Stryker%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0AQuest%20for%20RCE%20%0D%0ALast%20year%20during%20a%20routine%20penetration%20test%2C%20our%20team%20came%20across%20a%20interesting%20target%20called "Tumblr")[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Vocera%20Communications%20or%20Stryker%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0AQuest%20for%20RCE%20%0D%0ALast%20year%20during%20a%20routine%20penetration%20test%2C%20our%20team%20came%20across%20a%20interesting%20target%20called&media=https%3A%2F%2Fwww.securifera.com%2Fwp-content%2Fuploads%2F2023%2F04%2Fvocera.png "Pinterest")[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F04%2F24%2Fvocera_report_server_pwnage%2F&title=Vocera%20Report%20Server%20Pwnage&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Vocera%20Communications%20or%20Stryker%20Corporation.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0AQuest%20for%20RCE%20%0D%0ALast%20year%20during%20a%20routine%20penetration%20test%2C%20our%20team%20came%20across%20a%20interesting%20target%20called "Vk")[Email](mailto:?body=https://www.securifera.com/blog/2023/04/24/vocera_report_server_pwnage/&subject=Vocera%20Report%20Server%20Pwnage "Email")

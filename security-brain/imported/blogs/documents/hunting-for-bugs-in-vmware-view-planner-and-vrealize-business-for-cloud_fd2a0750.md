---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-15_hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud.md
original_filename: 2022-02-15_hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud.md
title: 'Hunting for bugs in VMware: View Planner and vRealize Business for Cloud'
category: documents
detected_topics:
- command-injection
- ssrf
- path-traversal
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- ssrf
- path-traversal
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: fd2a075097e89f906d594d15a7233cf95f77cdf9c0faee4f900a1b76fc9d0f8e
text_sha256: dc84341cf53a68e2dbeefa3041dbf1a4b89df09b2f5cd034a49de0e6235a7cb3
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting for bugs in VMware: View Planner and vRealize Business for Cloud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-15_hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, path-traversal, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `fd2a075097e89f906d594d15a7233cf95f77cdf9c0faee4f900a1b76fc9d0f8e`
- Text SHA256: `dc84341cf53a68e2dbeefa3041dbf1a4b89df09b2f5cd034a49de0e6235a7cb3`


## Content

---
title: "Hunting for bugs in VMware: View Planner and vRealize Business for Cloud"
page_title: "Hunting for bugs in VMware: View Planner and vRealize Business for Cloud – PT SWARM"
url: "https://swarm.ptsecurity.com/hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud/"
final_url: "https://swarm.ptsecurity.com/hunting-for-bugs-in-vmware-view-planner-and-vrealize-business-for-cloud/"
authors: ["Mikhail Klyuchnikov (@__Mn1__)", "Egor Dimitrenko (@elk0kc)"]
programs: ["VMware"]
bugs: ["RCE"]
publication_date: "2022-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2903
---

# Hunting for bugs in VMware: View Planner and vRealize Business for Cloud

Written by [Mikhail Klyuchnikov](https://swarm.ptsecurity.com/author/mikhail-klyuchnikov/ "Posts by Mikhail Klyuchnikov") and [Egor Dimitrenko](https://swarm.ptsecurity.com/author/egor-dimitrenko/ "Posts by Egor Dimitrenko") on February 15, 2022

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/image_2022-02-15_18-01-38.png)

## Authors

![](https://swarm.ptsecurity.com/wp-content/uploads/2020/06/image_2020-06-09_16-40-50.jpg)

[Mikhail Klyuchnikov](https://swarm.ptsecurity.com/author/mikhail-klyuchnikov/ "Posts by Mikhail Klyuchnikov")

Web Application Security Expert 

[m1ke_n1](https://twitter.com/m1ke_n1 "Visit Mikhail Klyuchnikov’s Twitter")

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/Egor_Dimitrenko-1-150x150.png)

[Egor Dimitrenko](https://swarm.ptsecurity.com/author/egor-dimitrenko/ "Posts by Egor Dimitrenko")

Penetration Tester 

[elk0kc](https://twitter.com/elk0kc "Visit Egor Dimitrenko’s Twitter")

Last year we found a lot of exciting vulnerabilities in VMware products. They were disclosed to the vendor, responsibly and have been patched. It’ll be a couple of articles, that disclose the details of the most critical flaws. This article covers unauthenticated RCEs in VMware View Planner (CVE-2021-21978) and in VMware vRealize Business for Cloud (CVE-2021-21984).

We want to thank VMware and their security response center for responsible cooperation. During the collaboration and communication, we figured out, that the main goal of their approach to take care of their customers and users.

## VMware View Planner

> VMware View Planner is the first comprehensive standard methodology for comparing virtual desktop deployment platforms. Using the patented technology, View Planner generates a realistic measure of client-side desktop performance for all desktops being measured on the virtual desktop platform. View Planner uses a rich set of commonly used applications as the desktop workload.
> 
> [VMware View Planner Documentation](https://docs.vmware.com/en/VMware-View-Planner/index.html)

After deploying this system, users access the web management interface at ports 80 and 443.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_1.png)Web panel

We started our investigation using the `netstat -pltn` command to identify the process assigned to port TCP/443. As shown below, we found this to be the docker’s process:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_2.png)List of open ports

To get a list of all the docker containers and the ports each one forwarded to the host machine we ran the `docker ps` command:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_3.png)List of Docker containers

Ports 80 and 443 was forwarded from the `appacheServer` container. Next, we attempted to get a shell inside of the container in order to find out the exact application that handles the HTTP requests. As shown below this turned out to be the httpd server:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_4.png)List of open ports in Docker container

The configuration file for the httpd server `httpd.conf` was located in the directory `/etc/httpd/conf/`. An extract of the configuration file is show below:
  
  
  <Directory "/etc/httpd/cgi-bin">
  AllowOverride None
  Options None
  Require all granted
  </Directory>
  
  # WSGI configuration for log uplaod
  WSGIScriptAlias /logupload /etc/httpd/html/wsgi_log_upload/log_upload_wsgi.py
  
  <IfModule headers_module>
  #
  # Avoid passing HTTP_PROXY environment to CGI's on this or any proxied
  # backend servers which have lingering "httpoxy" defects.
  # 'Proxy' request header is undefined by the IETF, not listed by IANA
  #
  RequestHeader unset Proxy early
  </IfModule>

The line with the `WSGIScriptAlias` directive caught our attention. That directive points to the python script `log_upload_wsgl.py` which responsible for handling requests to the `/logupload` URL. Significantly, authentication is not required in order to execute this request.

We determined:

  1. VMware View Planner handles a request to the `/logupload` URL made to the 443/TCP port.
  2. The request is redirected from the host into the `appacheServer` docker container.
  3. The Apache HTTP Server’ service (httpd) handles the requests to the mentioned URL inside the container by executing the `log_upload_wsgl.py` python script.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_5.png)Request handling workflow

We immediately started analysis of the `log_upload_wsgi.py` script. The script is very small and lightweight. A summary of this script’s functions:

  1. The script handles HTTP POST requests.
  2. The script parses a data from request.
  3. The script creates a file with the pathname based on the unsanitized data from the request and static prefix.
  4. Finally, the script writes the POST content into that file.

  
  
  #...
  if environ['REQUEST_METHOD'] == 'POST':
  #...
  resultBasePath = "/etc/httpd/html/vpresults"
  try:
  filedata = post["logfile"]
  metaData = post["logMetaData"]
  
  if metaData.value:
  logFileJson = LogFileJson.from_json(metaData.value)
  
  if not os.path.exists(os.path.join(resultBasePath, logFileJson.itrLogPath)):
  os.makedirs(os.path.join(resultBasePath, logFileJson.itrLogPath))
  
  if filedata.file:
  if (logFileJson.logFileType == agentlogFileType.WORKLOAD_ZIP_LOG):
  filePath = os.path.join(resultBasePath, logFileJson.itrLogPath, WORKLOAD_LOG_ZIP_ARCHIVE_FILE_NAME.format(str(logFileJson.workloadID)))
  else:
  filePath = os.path.join(resultBasePath, logFileJson.itrLogPath, logFileJson.logFileType)
  with open(filePath, 'wb') as output_file:
  while True:
  data = filedata.file.read(1024)
  # End of file
  if not data:
  break
  output_file.write(data)
  
  #...

We were surprised at user data wasn’t filtering. This means we could create arbitrary file with arbitrary content using a Path Traversal or uncommon feature of the `os.path.join` function.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_6.png)_How`os.path.join` works_

We want to draw attention to the unsafe use of `os.path.join` function in some cases. Even if the user input has been sanitized and the “`..`” strings would be stripped to prevent the Path Traversal, it’s possible to use the absolute path to the desired directory in the second argument.

Often even if there are possibilities to upload a malicious file for getting an arbitrary remote code execution python web app needs to be restarted entirely to pick up this new code. Unfortunately for VMware, this time, the `WSGIScriptAlias` alias in the httpd’s config meant that the script would not be cached and would be loaded into memory and executed each time users request the `/logupload` URL.

With this in mind, we decided to overwrite the original `log_upload_wsgi.py` script with our own malicious code. We had only one attempt to upload a valid python script otherwise we would break the web app. We created a WSGI web shell in the python language and tried to upload it to the `/etc/httpd/html/wsgi_log_upload/` folder with `log_upload_wsgi.py` filename.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_7.png)_Uploading web shell_

The attempt was successful and we uploaded the file. For the PoC we executed the `whoami` command sending an HTTP request to `/logupload` path with GET parameter `cmd`. Finally, we got the current system user in the server’s response, it was `apache` user.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic_8.png)_Executing`whoami` command_

## **VMware vRealize Business for Cloud**

> VMware vRealize Business for Cloud automates cloud costing analysis, consumption metering, cloud comparison and planning, delivering the cost visibility and business insights you need to run your cloud more efficiently.
> 
> [VMware vRealize Business for Cloud Documentation](https://docs.vmware.com/en/vRealize-Business-for-Cloud/index.html)

The second vulnerability in this article affects software, which works alongside with the cloud services. During the assessment, we discovered the application update mechanism is accessible without any authentication. Exploiting this feature resulted in arbitrary code execution on the target system.

It is no secret that if the attacker gets access to software update functionality and can affect the installation process, that would lead to critical consequences for the system. In this case, the update mechanism allowed for the setting up of custom repositories for the package sources. Although this method gives more flexibility to the administrator as they can choose the package location themselves, it exploitation easier for attackers.

At first, we looked closely at the script `upgradeVrb.py` located in the directory `/opt/vmware/share/htdocs/service/administration/` and responsible for the upgrade functionality. It was found that it is available without authentication, and also accepts the `repository_url` parameter.

The fragment of the vulnerable code `upgradeVrb.py`:
  
  
  app = Router()
  @app.route('/service/administration/upgradeVrb.py/updatesFromSource', methods=['PUT'], content_type="text/plain")
  def va_upgrade():
  repository_type = routing.get_query_parameter('repository_type')  # default, cdrom, url
  # default is when no provider-runtime.xml is supplied
  try:
  os.unlink("/opt/vmware/var/lib/vami/update/provider/provider-runtime.xml")
  except:
  pass
  
  url = ''
  if repository_type == 'cdrom':
  url = 'cdrom://'
  elif repository_type == 'url':
  url = routing.get_query_parameter('repository_url')
  if not url:
  cgiutil.error('repository_url is needed')
  elif repository_type == 'default':
  url = 'https://vapp-updates.vmware.com/vai-catalog/valm/vmw/a1ba78af-ec67-4333-8e25-a4be022f97c7/latest'
  

By specifying the address of the remote server controlled by us in the `repository_url` parameter, we noticed in logs, that the application requested the `manifest-latest.xml` file.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_1.png)_Setting custom repository as a source_ ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_2.png)_Web-server logs on our remote server_

So, after spending a little time in documentation we figured out that file `manifest-latest.xml` is a protagonist in repository. The custom repository consists of packages, additional resources and the manifest. The manifest file is a core component for each repository, and it describes the exact steps of the updating process. The repository can be located on any web server as a set of files and folders, but it must meet the specification.

At the next step an example of the correct manifest file for this software was found.
  
  
  <?xml version="1.0"?>
  <update xmlns:vadk="http://www.vmware.com/schema/vadk" xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:vmw="http://www.vmware.com/schema/ovf">
  <product>vRealize Business for Cloud</product>
  <version>7.6.0.28529</version>
  <fullVersion>7.6.0.28529 Build 13134973</fullVersion>
  <vendor>VMware</vendor>
  <vendorUUID>706ee0c0-b51c-11de-8a39-0800200c9a66</vendorUUID>
  <productRID>a1ba78af-ec67-4333-8e25-a4be022f97c7</productRID>
  <vendorURL/>
  <productURL/>
  <supportURL/>
  <releaseDate>20190403115019.000000+000</releaseDate>
  <description>vRealize Business for Cloud</description>
  <EULAList showPolicy="" introducedVersion=""/>
  <UpdateInfoList>
  <UpdateInfo introduced-version="7.8" category="feature" severity="important" affected-versions="" description="" reference-type="vendor" reference-id="" reference-url=""/>
  </UpdateInfoList>
  <preInstallScript>
  #!/bin/sh
  exit 0
  </preInstallScript>
  <postInstallScript>
  #!/bin/sh
  exit 0
  </postInstallScript>
  <Network protocols="IPv4,IPv6"/>
  </update>
  

While examining the manifest file, the document elements called `preInstallScript` and `postInstallScript` caught our attention:
  
  
  <preInstallScript>
  #!/bin/sh
  exit 0
  </preInstallScript>
  <postInstallScript>
  #!/bin/sh
  exit 0
  </postInstallScript>

The content of these elements hints that they are responsible for the OS command that would be executed before and after the update, the perfect place to inject the malicious code.

The updating procedure consists of three steps:

  1. Setting up the location of the remote repository
  2. Version comparison between the installed version and the version in the repository
  3. Remote installation procedure

We changed the version number in our repository and added the payload – the `cat /etc/shadow > /opt/vmware/share/htdocs/shadow` command that will end up with a sensitive file being written to the publicly available directory:
  
  
  <?xml version="1.0"?>
  <update xmlns:vadk="http://www.vmware.com/schema/vadk" xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:vmw="http://www.vmware.com/schema/ovf">
  <product>vRealize Business for Cloud</product>
  <version>7.8.4.28529</version>
  <fullVersion>7.8.4.28529 Build 13134973</fullVersion>
  <vendor>VMware</vendor>
  ….
  <preInstallScript>
  #!/bin/sh
  cat /etc/shadow > /opt/vmware/share/htdocs/shadow
  exit 0
  </preInstallScript>
  <postInstallScript>
  #!/bin/sh
  exit 0
  </postInstallScript>
  <Network protocols="IPv4,IPv6"/>
  </update>
  

As it turned out, there is integrity checks on the system. VMware product checks the manifest-latest.xml.sig file that should contain the digital signature of the package. And that is why our first attempt failed:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_3.png)_Application attempting to extract signature from repository_

So, this attempt was unsuccessful. But a quick search on the Internet reveals that this step is not mandatory and can be skipped by setting the `validateSignature` property to `False` in the `provider-runtime.xml`, which stores repository url. To do that, we would need another hack. Let’s look again how the `upgradeVrb.py` generates the `provider-runtime.xml`.
  
  
  elif repository_type == 'url':
  url = routing.get_query_parameter('repository_url')
  if not url:
  cgiutil.error('repository_url is needed')
  elif repository_type == 'default':
  url = 'https://vapp-updates.vmware.com/vai-catalog/valm/vmw/a1ba78af-ec67-4333-8e25-a4be022f97c7/latest'
  
  if url:
  with open("/opt/vmware/var/lib/vami/update/provider/provider-runtime.xml", 'w') as provider_file:
  provider_file.write("""
  <service>
  <properties>
  <property name="localRepositoryAddress" value="%s" />
  <property name="localRepositoryPasswordFormat" value="base64" />
  </properties>
  </service>
  """ % url)
  

As you can see, the `repository_url` parameter is taken from the user input without sanitization. That means we can inject the `validateSignature` XML tag via user-controlled parameter, which should disable the integrity checks:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/image_2022-02-16_13-03-21.png)_With XML injection, we add`validateSignature` property in the `provider-runtime.xml`_ ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/image_2022-02-16_13-03-36.png)R _esult of our attack: modified XML file with additional element_

With the integrity check disabled, we attempted our attack again using the update process.

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_6.png)_HTTP request that checks update’s availability_ ![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_7.png)_HTTP request that triggers the installation process_

The update functionality abuse is successful and we are able to get a copy of the `/etc/shadow` file available from the web directory without any authentication:

![](https://swarm.ptsecurity.com/wp-content/uploads/2022/02/pic2_8.png) Demo

## To be continued

Don’t worry, it’s not over yet. In the next article, we will talk about the SSRF to RCE vulnerability chain and a misconfiguration in a fancy proxy server that led to a severe consequence. Stay tuned!

[Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)

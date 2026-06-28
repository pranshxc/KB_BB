---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-02_stealing-chat-session-id-with-cors-and-execute-csrf-attack.md
original_filename: 2021-02-02_stealing-chat-session-id-with-cors-and-execute-csrf-attack.md
title: Stealing Chat session ID with CORS and execute CSRF attack
category: documents
detected_topics:
- command-injection
- cors
- csrf
tags:
- imported
- documents
- command-injection
- cors
- csrf
language: en
raw_sha256: 0786fb16ced92166a7d9a1bbb4fa4cd29581fb7be06b797f7f9f7ae51e45a847
text_sha256: 84fa96588a39f6a2a4f9888b8c814ffa35a80f631a98daec6632f4c8018b6f06
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Chat session ID with CORS and execute CSRF attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-02_stealing-chat-session-id-with-cors-and-execute-csrf-attack.md
- Source Type: markdown
- Detected Topics: command-injection, cors, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `0786fb16ced92166a7d9a1bbb4fa4cd29581fb7be06b797f7f9f7ae51e45a847`
- Text SHA256: `84fa96588a39f6a2a4f9888b8c814ffa35a80f631a98daec6632f4c8018b6f06`


## Content

---
title: "Stealing Chat session ID with CORS and execute CSRF attack"
url: "https://sunilyedla.medium.com/stealing-chat-session-id-with-cors-and-execute-csrf-attack-f9f7ea229db1"
authors: ["Sunil Yedla (@sunilyedla2)"]
bugs: ["CSRF", "CORS misconfiguration"]
publication_date: "2021-02-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3942
scraped_via: "browseros"
---

# Stealing Chat session ID with CORS and execute CSRF attack

Stealing Chat session ID with CORS and execute CSRF attack
Sunil Yedla
Follow
2 min read
·
Feb 2, 2021

334

2

Hello Everyone, Hope you all are healthy and safe. Today’s writeup is my recent find on Bugcrowd private program. This writeup explains how I was able to chain CORS with CSRF attack to steal chat session Id of victim user and send messages on behalf of victim. Without wasting time let’s get into details of the vulnerability.

In 2nd week of January, while exploring the <redacted> domain. I found that the target domain has in built chat feature. For sending a new message, system will send a POST request like this:

POST /ha/chat/<Chat_Session_ID> HTTP/1.1
Host: <redacted>
User-Agent: XXXXX
Accept: application/json, text/plain, /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
Host-Site: XXX
Content-Length: 75
Origin: XXXXX
Connection: close
Referer: XXXXXXX

{“content”:”HI”,”event”:”MESSAGE”,”clientSideSequence”:4,”role”:”CUSTOMER”}

Get Sunil Yedla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On further investigation, I found that this POST request is vulnerable to CSRF attack. So YAY! Attackers can send messages on behalf of Victim user.

But Wait!! If you observe carefully the end-point includes victim’s chat session_id **/ha/chat/<Chat_Session_ID>** and it has format like this: XXXXXX-CHAT_XXXXXXXXXX–XXXX-XXXX-XXXX-XXXXXXXXXXXX

: (

Now I came so close and don’t want to give up on this. At this moment, I have the complete clarity, all I need to do is find a way to steal that chat session ID of victim user. So continued exploring and came across an end-point which helps me create chat session_ID of the victim user. **https://<redacted>/ha/chat/create** and in addition to this, end-point does not have CORS and CSRF protection. So quickly created a CORS POC code and verified that this end-point is vulnerable to CORS : )

Press enter or click to view image in full size

CORS POC code example: [Change values accordingly]

<html>
<script>
var req = new XMLHttpRequest(); req.onload = reqListener; req.open(‘GET/POST’,’<Vulnerable URL>’,true); req.withCredentials = true;
req.send(‘{}’); function reqListener() { alert(this.responseText); };
</script>
</html>

Conclusion

So to create an impact, attacker will first steal Chat session Id of victim user and then execute CSRF attack to send messages as victim users. After getting the complete clarity, quickly raised a report on Bugcrowd on Jan/12/2021. Bugcrowd Triage team Triaged this report with severity P3 on Jan/26/2021

Press enter or click to view image in full size

I hope you like my explanation. You can ping me on twitter: https://twitter.com/sunilyedla2 if you have any queries. Good Day and spread positivity!

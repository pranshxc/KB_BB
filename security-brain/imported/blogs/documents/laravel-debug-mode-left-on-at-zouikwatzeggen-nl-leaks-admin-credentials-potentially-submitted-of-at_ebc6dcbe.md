---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-30_laravel-debug-mode-left-on-at-zouikwatzeggennl-leaks-admin-credentials-potential.md
original_filename: 2023-06-30_laravel-debug-mode-left-on-at-zouikwatzeggennl-leaks-admin-credentials-potential.md
title: Laravel debug mode left on at Zouikwatzeggen.nl leaks admin credentials & potentially
  submitted reports of improper behaviour at Amsterdam University Medical Centers
category: documents
detected_topics:
- command-injection
- information-disclosure
- supply-chain
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- command-injection
- information-disclosure
- supply-chain
- otp
- automation-abuse
- csrf
language: en
raw_sha256: ebc6dcbef276644fc6b4f43941c1d53de9b1b0c6cdfbc55f2fe764ea2357924e
text_sha256: fb1695aadb4099096299a83f4d3dd2b5e8806e20cde1c716cd81a389bab67624
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# Laravel debug mode left on at Zouikwatzeggen.nl leaks admin credentials & potentially submitted reports of improper behaviour at Amsterdam University Medical Centers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-30_laravel-debug-mode-left-on-at-zouikwatzeggennl-leaks-admin-credentials-potential.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, supply-chain, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `ebc6dcbef276644fc6b4f43941c1d53de9b1b0c6cdfbc55f2fe764ea2357924e`
- Text SHA256: `fb1695aadb4099096299a83f4d3dd2b5e8806e20cde1c716cd81a389bab67624`


## Content

---
title: "Laravel debug mode left on at Zouikwatzeggen.nl leaks admin credentials & potentially submitted reports of improper behaviour at Amsterdam University Medical Centers"
url: "https://medium.com/@jonathanbouman/laravel-debug-mode-left-on-at-zouikwatzeggen-nl-948a7365409f"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["AmsterdamUMC"]
bugs: ["Debug mode enabled", "Android", "Email spoofing", "Information disclosure"]
publication_date: "2023-06-30"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 988
scraped_via: "browseros"
---

# Laravel debug mode left on at Zouikwatzeggen.nl leaks admin credentials & potentially submitted reports of improper behaviour at Amsterdam University Medical Centers

Laravel debug mode left on at Zouikwatzeggen.nl leaks admin credentials & potentially submitted reports of improper behaviour at Amsterdam University Medical Centers
Jonathan Bouman
Follow
12 min read
·
Jun 30, 2023

122

Background
It’s already 11 years ago when Benjamin & I published the article “There’s a medical app for that” in the BMJ Careers. It helps the reader to ask the right questions to estimate if an app could be safely used in healthcare. Our focus during that time was on patient safety, but today the focus will be on the safety of the actual people working in healthcare themselves.

Let's have a closer look at the app that allows one to report improper behaviour at work; the #zouikwatzeggen-app (translated: ‘#wouldIsaysomething-app’). Is that app safe to use?

Press enter or click to view image in full size
The release announcement of the app “#zouikwatzeggen”, now available to all 15k employees.

The app raises awareness about improper behaviour and shows how to make it discussable. There is also a report button to easily report (anonymously) undesirable behaviour directly to the right person. The app is part of a larger package of e-learning about preventing undesirable behaviour and workshops on the subject.

Undesirable behaviour in the workplace occurs in many ways: gossiping, bullying, exclusion, intimidation, verbal and physical aggression, discrimination, conflicts and sexual remarks or acts.

At the end of the day I think everyone agrees it’s a good thing to do reduce undesirable behaviour. An app might help, but we need to be sure that the app itself is as safe as possible as it handles highly sensitive data.

Recon, how does the app exactly work?
As security researchers we are triggered by the functionality of ‘sending reports using the app’. How does that work? Some form that relays data to an email? What parameters? Where is the code supporting this functionality hosted and is this server properly secured?

Let’s start with the android app, as we could easily download the app and patch the code in order to be able to intercept the traffic made by the app.

Nowadays all apps use HTTPS for communication, and by patching it we disable those security checks. After the patch we could route the traffic of the app through Burp Suite and inspect / manipulate it.

There are multiple ways to obtain the APK installation file of the app.
Method 1 — Install the app on your android phone from the Google Play store and use the method described here; https://stackoverflow.com/questions/4032960/how-do-i-get-an-apk-file-from-an-android-device
Method 2 — Trust a third party download website and download the APK; see this deeplink on https://apkpure.com/

Intercept the app its traffic
After we have obtained the APK we use APK-MITM to patch our APK so it does not check the HTTPS certificates anymore; it needs to accept our Burp enforced HTTPS certificate.

When we have apk-mitm installed we could runapk-mitm \#Zouikwatzeggen_2.2.2_Apkpure.apkin order to patch it.

Patching the APK file using apk-mitm so we can intercept the internet traffic

After that we could install the app on the mobile using ADB (see this page for instruction). Pro tip: use scrcpy to capture the screen of your mobile on your desktop, really handy if you want to be able to capture both screens at the same time like the video below.

Install the patched APK on our test device.

Prepare your phone so it could work together with Burp Suite. See for example this tutorial. Still problems intercepting the traffic with Burp? You can inject the Burp Suite certificate directly into the patched APK using this command apk-mitm \#Zouikwatzeggen_2.2.2_Apkpure.apk --certificate cacert.pem . The cacert.pem file is created by running this command:curl --proxy http://127.0.0.1:8080 -o cacert.der http://burp/cert && openssl x509 -inform DER -in cacert.der -out cacert.pem.

Interception of the app traffic works after injecting the Burp Certificate in the APK. On the left you see the request made by the app.

We are now able to intercept the traffic between the app and its backend systems. For example when we submit a new report we are able to intercept the request made:

Press enter or click to view image in full size
Request send to the server when submitting a new report. It returns an error message including a stack trace.

Stack trace error message?
This is odd. The functionality of submitting a report is broken and the app gives back an error. By a quick look at the request we see: "recipient”: “null" . The developer forgot to set the email when sending the form…

Furthermore the error we get back is extremely detailed. It reflects the exact source code file and line of code triggering the error. This smells like someone forgot to properly test all the functionality before the app was published, and forgot to turn of debug messages.

However first lets dig deeper and lets try to fix the request by injecting our own email address as recipient.

POST /formData HTTP/1.1
Host: api.zouikwatzeggen.nl
Cookie: XSRF-TOKEN=eyJpdiI6Ijh6ODVJYTZrQ1lsOHlpbXVCWm51dkE9PSIsInZhbHVlIjoiRnBabGd6U0pCSGw0Y0hyYXlPa1IzcGVoS1BLZkYyeVR6WEtoZlV5N2xUVERpbnd2eGdVSVdPUzQxdjJtTFlLcm9ZNy9pVWR0Rk1CWFlwSlAvQjNmcVdNKzc4czBwZXJSa016YnpJdlVnMjhkTEtSS0c5M1hjOGxYSzdSQ3YvMUUiLCJtYWMiOiI4MzVjZmU1MDVmOTQ1MTliNmY5YTMyOGI4NzliYjM4NWQwMmJkOTFjNGVlN2JlODViY2MzOTQ1NWFkNWI3ZGQ2In0%3D; zouikwatzeggen_fritz_api_v2_session=eyJpdiI6IkMya3ZIcEozV2RpdUg0NkRqUU14V2c9PSIsInZhbHVlIjoiVGo2eGJFaElHek5jREhXL3RGM093R0xZRXlZbm41UldvT3hsMXRRRWV3VktIMVZBL215NTV2TExUQmlGT3Irc1dkT0lEYmFJNWYrQU1KaU9aUmJ6TGt5cVhnSFFPUDhRVkFER1oyTzRnaC83a2x3WUNsbVhKV2s4MmJkTkJRcFIiLCJtYWMiOiI0YWUyZmVlZjk1ZTA1NmVkMjU1MTljMDE0MWYxMDM5Njk0M2I2YjljOWU1ODUzMTRlNmIyNDQ0ODUzOTM0OWVlIn0%3D
Accept: application/json, text/plain, */*
Content-Type: application/json;charset=utf-8
Content-Length: 112
Accept-Encoding: gzip, deflate
User-Agent: okhttp/3.14.9
Connection: close

{"message":"https://test.nl <h1>test</h1>","type":"ContactViaAnonymousEmail","recipient":"pentest@protozoan.nl"}
Press enter or click to view image in full size
Injecting our own email as the recipient.

A few seconds later we receive this email:

Press enter or click to view image in full size
Bug 1: Being able to send emails from the #zouikwatzeggen-app to anyone

We found our first bug: Email spoofing.

Although the impact is limited; one could use the app to send emails with a custom text to anyone. Handy to for phishing campaigns, or just to spam users on the internet.

Now let’s have a closer look at the headers returned when submitting the email form submit:

HTTP/1.1 200 OK
Date: Mon, 12 Sep 2022 17:50:06 GMT
Server: Apache/2.4.41 (Ubuntu)
Cache-Control: no-cache, private
phpdebugbar-id: ***REDACTED-SUSPECT-TOKEN***Set-Cookie: XSRF-TOKEN=eyJpdiI6Ik9ROW14ckUrbU0xVjdXQzZWMko0R2c9PSIsInZhbHVlIjoiUnFIQW1YZlBSbXVmaEhkREpjeHUyYTRXbUZhY3pyK1JLbmhKaFU0QXQvOUR4YXF1MUJMallOUUZyR05NOVV4S2wyYTZDc2lERTJZU0IxL2RyTzcrZVFhd25ndFpRWXd4WVJtNHFLUVVWdEZ2OTd2MWJBTURGd1Z2VjJIUStHZmIiLCJtYWMiOiI1ZDE3Y2IxZDEyODFkZGRlNWEwMjBkODJjZWUyN2M1ODkxZThjM2Q5OTQ1YTcyNzk2MWEwZmVmNGZmOWYwMmE1In0%3D; expires=Mon, 12-Sep-2022 19:50:06 GMT; Max-Age=7200; path=/; samesite=lax
Set-Cookie: zouikwatzeggen_fritz_api_v2_session=eyJpdiI6Im1hMWpreFZ6VjIwRSsySmtjcjBCbUE9PSIsInZhbHVlIjoiVzRiSy9nZ1F6c0pTZDNLUjE1bUNqR0FTSUM4UDFweG4rVjNsRUVzTGtSdFpSeXFrUnZSOHJUZnhzQU0yalZWMzJKQmhkK2ZSRHVaVjBmNGFzemVXSWNYak9FdHRYa0tmYnlpdnpxTlhOZlZsaVpSd0hwNDVJWVVSRzBBeXpkalkiLCJtYWMiOiI3OGU0Yzk1NTQ1NTRkZDNiYjJlMzQ4ZjkyYWMwNTI3OGVhZTQwNTFlMmJlMDZkMGIyOTY3ODZhOGI5NjI2NDVkIn0%3D; expires=Mon, 12-Sep-2022 19:50:06 GMT; Max-Age=7200; path=/; httponly; samesite=lax
Content-Length: 17
Connection: close
Content-Type: application/json

{"status":"sent"}

PHP Debug bar
If you look carefully you notice phpdebugbar-id ; a tool (2) used by PHP developers to easily debug problems on deployed applications. This might explains why we got those extensive error messages back. The debug mode of the application was left on, and it includes a php debug bar.

Let’s see if we can find a way to trigger the user interface of the debug bar on our desktop. An easy way is to just trigger an error by visiting one of the endpoints used by the app.

We randomly pick one the urls from our Burp History and open it in our browser.

https://api.zouikwatzeggen.nl/getToKnowYou?domain=1&model=App%5CCms%5CModels%5CAfterIntroBeforeQuestionsHolxder (notice the Holxder piece which is a typo that triggers an error).

Press enter or click to view image in full size
We got access to the debugbar!

Here we have bug number 2: php debug bar exposure. Please see https://github.com/barryvdh/laravel-debugbar to learn more about all the features it has.

This bug gives us insights in the code behind the app, its settings and active user sessions and their data. As we all understand this is a problem. But we need a proof of concept everyone at the organization is able to understand, what is the impact on the 15k employees at the AmsterdamUMC? How are they affected? If I tell the board “PHP Debug Bar is left on!” they will shrug their shoulders.

Whenever possible we should provide a proof of concept that everyone could understand and at the same time limit damage done doing that. For example: can we now leak one of our own submitted reports on inappropriate behaviour by using this debug bar?

On the left our mobile phone that just sent a report, on the right the exposed debugbar. In grey Burp Suite used to search for the leakage of our just sent report. In blue we mark the actual leak.

Ok. This is serious; we can leak submitted reports.

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The debug bar allows one to list the latest requests of all visitors to the server. This includes the submission of inappropriate behaviour reports. In the Debug bar UI it does not reflect the exact details of those reports. However when one intercepts the Debug bar traffic (use Burp Browser) it will reflect all the report details.

The above proof of concept video might go a bit fast, so let's have a closer look.

Step 1: open the Request modal.

Press enter or click to view image in full size
Press the Folder icon to open the model of active sessions

Step 2: Open the incoming POST request from the App.

Press enter or click to view image in full size
Open the request /formData

Step 3: Intercept the request made by the PHP Debug Bar about this request, inspect the response in Burp and search for the string Serieuze to see if we could find a piece of our report (and confirming the leak).

Press enter or click to view image in full size
Bug 2: The response contains the inappropriate behaviour report message

In other words, one could monitor this endpoint https://api.zouikwatzeggen.nl/_debugbar/open?op=get, no authentication needed, every few seconds and store the output. This allows one to capture all the reports sent by employees in near real time.

We now have proved the bug leaks report details, however is there more?

After digging a little bit deeper, we discover that in the past the debug bar could be abused to achieve remote code execution (RCE), see this bug. Luckily this Laravel was properly patched and I could not find a way to bypass the bugfix.

Anything else we could do to achieve RCE using this debug bar?

Leaking the administrator password
What if the system administrator uses the same web application to access the administration panel? Will we be able to leak the password?

Lets monitor the incoming requests on this server for a few hours and see if we’re lucky to monitor the administrator logging in:

Press enter or click to view image in full size
Captured server request, someone trying to login.

Hurray! As we can see the path /cm/login is requested by another user. Let’s look at the credentials used for this login.

Press enter or click to view image in full size
Bug 3: The administrator username & password is leaked (blurred in the above picture)

We now demonstrated this bug gives us the credentials needed to access the administrator dashboard.

Time to stop our research and share all our insights with the CERT.

Discussion, Do no harm — Primum non nocere
One of the ground principles of modern (and old) medicine is that we need to be sure our intervention really helps to solve the problem, and not actually make it more worse.

What if the highly sensitive data of the submitter is leaked, or the details of a report on an unaware potential subject of improper behaviour? What would it do with our overall trust in a system?

An interesting perspective is that especially this ‘Do no harm’-rule made us create proper (transparent) procedures in medicine before we could even research medical interventions on humans. When you want to research a new intervention you would need approval from the Research Ethics Committee. What are the risks of something going wrong, what is the impact if it goes wrong? Does it potentially harm? Furthermore you’re enforced to report back adverse events, so research can shutdown or new participants can be informed upfront.

As always I try to share my insights of what we could learn from medicine when we try to make the digital world safer, and the other way around.

Implementing Threat Modeling
What needs to be done before one should publish an app like this? It’s a hard question, let me share you my thoughts. However I’m happy to learn from you, so change my mind and leave your comments below!

My advice is to perform a proper pentest upfront, fix the found bugs and after that perform a systematic way of threat modelling like includesnodirt.com (invite a hacker, developer, privacy officer, end user and CERT member).

After this is done present the results to a small committee just like the ones we have in medicine known as Research Ethics Committees (so if possible include ethicists) and decide if the risk is worth the potential benefit. This sounds like a lot of hassle for a ‘simple app’. However employee/customer trust is at stake, one mistake could severely impact the trust on other (properly working) apps. So ‘do no harm’ and try to proof if your app really solves the problem, if it doesn’t, shut it down (I love to see more evidence based policy in healthcare).

Possible improvements
If deemed necessary to publish an app like this I would recommend a few things to limit the blast radius if something goes wrong. A good start would be to implement client side encryption of the most sensitive data.

What we could use is OpenPGP, which is an open source, battle proof, encryption protocol that allows one to encrypt the message before it leaves the device. See the OpenPGP documentation for examples that work on the client side.

At this moment the message in the app is send to the external vendor its webserver, from the webserver to the external vendors internal mail server and relayed to the email server of the AmsterdamUMC (or one of the other hospitals using the app). As email is not encrypted by default this might create a risk if any of the involved servers is compromised.

Whenever one implements OpenPGP encryption the impact would be ‘leaked encrypted emails’, which is less impactful compared to the current situation. The receiver of the emails needs to implement OpenPGP in order to decrypt the contents using a secret private key (only known to the people who should be able to view the reports).

The risks that are left over are a supply chain attack (someone replacing the code of the app and sniff the reports), phishing (someone releasing a rogue app imitating the original one and sniff the reports) or when the email box of the receiver gets compromised. Last but not least when the email box of the receiver fails because of whatever reason and the email is send back to the actual sender, which is webmaster@<app-developer-name>.nl (see screenshot of Bug 1), the contents would be leaked to the person who has access to the webmaster@<app-developer-name>.nl account (not likely to happen, but something to take into account).

Transparency is trust
The fact I could publish this blog without any problems is really important. Thanks to the Cordinated Vulnerability Disclosure (CVD) policy.

Keeping bugs like these quiet is not the way forward. As in medicine, we all learn from mistakes made by others. It’s not about shaming someone making this mistake, it’s about learning from it and creating a safer environment for everyone tomorrow.

A great example of properly working CVD
After I hit the SEND button of my bug report it took literally 10 minutes to get back a reply from the involved CERT. It was 20:30 local time, but they confirmed the bug and took action to inform the vendor.

After supplying more information on the additional impact (leaked administrator credentials) I had the same experience; a quick reply with proper actions.

The app was hosted by an external vendor, this report demonstrates the challenges you have when not all infrastructure is under your control. Does the vendor has the same level of security as your self-hosted applications? And more important do they also support CVD?

However, this report is a great example of how CVD can help your organisation in getting everything more secure. Act fast and kill the bugs!

Disclaimer
As some of you know I work at the affected hospital myself, however this research was done in my spare time. As being part of SCIRT (SURF Community van Incident Response Teams) I’m happy to share my insights and increase awareness whenever needed.

Timeline
17–06–2021 First announcement of the availability of the app; students only
07–09–2022 Announcement of the availability of the app; all 15k employees
12–09–2022 Discovered the email spoof bug, reported it to CERT
12–09–2022 Discovered the PHP debug bar bug, reported it to CERT
12–09–2022 CERT replied within 10 minutes confirming the bug
13–09–2022 Discovered the administrator credentials, reported it to CERT
13–09–2022 CERT confirmed the compromise and ordered vendor to shutdown server. CERT reported the data leak.

23–03–2023 Got an invite to share the details of the bug during the SURF Security & Privacy conferentie
29–05–2023 Wrote the first draft of this blog and shared it with the AmsterdamUMC CISO to coordinate the disclosure.
20–06–2023 AmsterdamUMC gives permission to disclose the bug
29–06–2023 Presentation of the above research, release of the blog
29–06–2023 Got the “Thank You!” keychain award from the AmsterdamUMC

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-30_how-i-get-1000-bounty-for-discovering-account-takeover-in-android-application.md
original_filename: 2023-06-30_how-i-get-1000-bounty-for-discovering-account-takeover-in-android-application.md
title: How I get 1000$ bounty for Discovering Account Takeover in Android Application
category: documents
detected_topics:
- sso
- command-injection
- otp
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- api-security
- mobile-security
language: en
raw_sha256: c0f37d110a9544125f76ea71c5e5fb07ace60d412f4c69eaf768b83caa93c7c2
text_sha256: 64f80ef91f06f6712f68e1021c87a49f7c0a3c8fa91d40c46481528470e2c681
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# How I get 1000$ bounty for Discovering Account Takeover in Android Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-30_how-i-get-1000-bounty-for-discovering-account-takeover-in-android-application.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `c0f37d110a9544125f76ea71c5e5fb07ace60d412f4c69eaf768b83caa93c7c2`
- Text SHA256: `64f80ef91f06f6712f68e1021c87a49f7c0a3c8fa91d40c46481528470e2c681`


## Content

---
title: "How I get 1000$ bounty for Discovering Account Takeover in Android Application"
url: "https://medium.com/@amolbhavar/how-i-get-1000-bounty-for-discovering-account-takeover-in-android-application-3c4f54fbde39"
authors: ["Amol Bhavar"]
bugs: ["Account takeover", "Android", "Client-side enforcement of server-side security", "OTP bypass"]
bounty: "1,000"
publication_date: "2023-06-30"
added_date: "2023-07-03"
source: "pentester.land/writeups.json"
original_index: 989
scraped_via: "browseros"
---

# How I get 1000$ bounty for Discovering Account Takeover in Android Application

Top highlight

How I get 1000$ bounty for Discovering Account Takeover in Android Application
Amol Bhavar
Follow
4 min read
·
Jun 29, 2023

403

9

In this blog post, I will share my experience of discovering a critical account takeover vulnerability in an Android application which has 100Mn+ downloads on Play Store. Through a combination of reverse engineering, runtime analysis, and the use of powerful tools like Frida, Objection, Burp Suite, and Brida, I successfully identified the vulnerability and responsibly disclosed it to the application’s developers, earning a $1000 bug bounty.

While attempting to log into the application using a temporary phone number, I encountered an issue where the OTP was not being sent to the provided number. So I decided to take a look into it to better understand the application’s inner workings.

First I fired up Burp and start capturing requests. After a while I came across an encrypted message in a particularly interesting network request. Decrypting the message revealed login session details but did not provide the necessary OTP for login.

Press enter or click to view image in full size

I send it to Burp Decoder tab and decrypt it , what was I saw is this request contains some login session but not giving me any OTP for login. I tried response manipulation but it also didn’t work. I spend some more time with Burp but end up finding nothing interesting.

At this point I decided to to reverse engineer the application and analyze its source code. I used jadx tool to convert APK files into readable Java code. However, the converted code turned out to be quite lengthy and difficult to navigate. Additionally the code was obfuscated as expected.

Get Amol Bhavar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I decided to do runtime analysis and best tool for it is Frida. By attaching application to Frida, I was able to gain deeper visibility into its runtime behavior. With the help of Frida and Objection, I quickly identified the activity responsible for the login functionality within the Android application. This provided me with a starting point to explore further.

Press enter or click to view image in full size

I use below command to start objection and search for current activity:

# objection -g com.appname.test explore

# android hooking get current activity

Activity: com.testapp.activity.setup.phoneLogin.PhoneLoginActivity

Once I got the current activity then I decided to listed down all the class methods that were loaded during the identified login activity. This step allowed me to narrow down my focus and concentrate on methods relevant to OTP generation and verification.

android hooking list class_methods com.appname.test.testActivity
Press enter or click to view image in full size

Boom!!! It gave me all the loaded class methods. I began intercepting and analyzing the methods associated with OTP handling. After spending couple of time I found some interesting methods which I think can be responsible for sending OTP or checking the inserted OTP is valid or not. But then hooking each method and checking what they do is also time consuming and I also need to write manual script for each method.

At this point I decided to use Brida. Brida is a Burp Suite Extension that, working as a bridge between Burp Suite and Frida. To enhance my analysis and backtrack the OTP generation process, I integrated Burp Suite with the Brida extension. This combination provided me with greater visibility into network traffic and allowed for more comprehensive testing.

Press enter or click to view image in full size
This is how Brida looks like

I spawn application with Brida and this time decided to use Graphical Analysis option. Here I have option of load all the methods from specific class and I can inspect that method with backtarce also. So I inspect all the methods which I found interesting at same time and check if they return any value or not. And I am suprised to see that one of method is returing the OTP code itself.

Press enter or click to view image in full size

Cool at this point inspecting some class methods I can easily get the OTP code. With the combined power of Frida, Objection, Burp Suite, and Brida I traced back the method responsible for OTP generation. But I realized that the OTP was being generated at the application level itself, without relying on the user’s phone number, this flaw posed a severe risk to user security and privacy, enabling account takeover without access to the phone number.

Understanding the importance of responsible disclosure, I reported this vulnerability & They acknowledged the issue, swiftly addressed it, and awarded me a $1000 bug bounty for my responsible disclosure and contribution to their application’s security !!!

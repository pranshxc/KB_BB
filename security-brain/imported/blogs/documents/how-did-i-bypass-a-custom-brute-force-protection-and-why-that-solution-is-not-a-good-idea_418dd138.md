---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-25_how-did-i-bypass-a-custom-brute-force-protection-and-why-that-solution-is-not-a-.md
original_filename: 2019-05-25_how-did-i-bypass-a-custom-brute-force-protection-and-why-that-solution-is-not-a-.md
title: How did I bypass a Custom Brute Force protection and why that solution is not
  a good idea?
category: documents
detected_topics:
- mobile-security
- rate-limit
- ssrf
- command-injection
- otp
- csrf
tags:
- imported
- documents
- mobile-security
- rate-limit
- ssrf
- command-injection
- otp
- csrf
language: en
raw_sha256: 418dd1386dddc1715e2ab18e3478f8d1b23dd32754e45c9dea3e84505a1f0cda
text_sha256: 562b583f93b2d6d5df4bd8619fbcd066976deb5fd98997265da9a67ccb117912
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How did I bypass a Custom Brute Force protection and why that solution is not a good idea?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-25_how-did-i-bypass-a-custom-brute-force-protection-and-why-that-solution-is-not-a-.md
- Source Type: markdown
- Detected Topics: mobile-security, rate-limit, ssrf, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `418dd1386dddc1715e2ab18e3478f8d1b23dd32754e45c9dea3e84505a1f0cda`
- Text SHA256: `562b583f93b2d6d5df4bd8619fbcd066976deb5fd98997265da9a67ccb117912`


## Content

---
title: "How did I bypass a Custom Brute Force protection and why that solution is not a good idea?"
page_title: "Bypassing custom rate-limit protection in Mobile App | by INMUNE7 | Medium"
url: "https://medium.com/@dortz/how-did-i-bypass-a-custom-brute-force-protection-and-why-that-solution-is-not-a-good-idea-4bec705004f9"
authors: ["dortz"]
bugs: ["Bruteforce", "Broken authentication"]
publication_date: "2019-05-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5242
scraped_via: "browseros"
---

# How did I bypass a Custom Brute Force protection and why that solution is not a good idea?

Bypassing custom rate-limit protection in Mobile App
INMUNE7
Follow
8 min read
·
May 26, 2019

36

Introduction

In this article, I am going to talk about how I bypass rate-limit protection of the ACME corporation (a hypothetical name to maintain the non-disclosure agreement) with a custom implementation in native code for token generation. Later I will mention why this is not the best solution and I will recommend a better one.

Prelude

Brute force is one of the simple (also noisy) way to guess a password or something you want to know. Basically, in a brute force attack, an attacker tries a combination of passwords, strings, hex values, stack cookies, what you want to find.

In this case, the ACME company implemented a custom solution to “stop” brute force attacks based in tokens using native code (.so library ) in an Android application.

My client said:

No one can read the library to generate a token because is compiled and is not readable.

I say to myself :

That’s not true, some one can decompile the source code of the library and read the assembler code to understand what the library does.

So let’s get started.

About the app

The application is built for Android and it uses its own token implementation to prevent brute force attacks.

Press enter or click to view image in full size
Figure 1. Token validation process

In Figure 1. We can see how the server handles the token, if the token is valid, the server returns 200, but if the token is invalid, the server returns 401.

This token is put in the header and is validate per request.

Press enter or click to view image in full size
Figure 2. Request example

In Figure 2 we can see an example of a request. In the X-ACME-Token header the application place the generated token. This token is used during the login process.

The research

Due to the kind of test, I perform this research without access to the source code or any information about the application, this is what we call “black-box testing”.

I downloaded the APK of the application and opened it with JADX, after a lot of source code review I found the SEC class. This class defines a static segment to load the library with native code. Also is important to note that the application doesn’t obfuscate the code so was easy to JADX decompile the source code and show me in a readable format.

Press enter or click to view image in full size
Figure 3. Sec class ACME example

Second … At this point, I know what is the name of the library so I extract the .so file using the ADB command from the Android emulated device.

adb pull /data/data/com.acme.app/lib/libacme-lib.so .

In this link I was talk about Genymotion and how prepare an Android lab if you are interested.

This is the fun part. I need to do binary research if I want to understand what the file does because I don’t have the source code of the library.

Let’s begin with the basic, I used xxd and file command to know more about the file.

Press enter or click to view image in full size
Figure 4. Basic research in a binary file

At this point I know what the file is, the ELF header and the output of the file command confirm that the file is a shared library. The next thing I always do is open the file using the string command.

Figure 5. Strings output command.

…. very interesting method I found here.

Java_com_acme_account_Sec_token

Let’s open the library in IDA and examine that method.

Figure 6. Library opened with IDA

After a couple of hours reading assembler code to try to understand what the library does I decide to move forward with another option (more simplistic and cheaper for my client) maybe if I find some vulnerability in the Login process I can generate my own token… But wait …. something comes to my mind and it was like a.

WOW!! … yes, it could works !!

Me after a revelation of God
FRIDA to the rescue

This is an awesome tool, according to the website is:

it’s a dynamic code instrumentation toolkit. It lets you inject snippets of JavaScript or your own library into native apps on Windows, macOS, GNU/Linux, iOS, Android, and QNX. Frida also provides you with some simple tools built on top of the Frida API. These can be used as-is, tweaked to your needs, or serve as examples of how to use the API.

What is my plan from now?

In theory, according to the definition, I could inject snippets of JavaScript into the native apps in this case Java. So I need to find in the code where the SEC class is used and try to understand how the token is generated (reading Java code, not assembler) and maybe generate my own token.

My steps:

Give me six hours to chop down a tree and I will spend the first four sharpening the ax. Abraham Lincoln

Before diving into the code I spent a couple of hours understanding the FRIDA API. This is a very important step because it allows to me get a better idea of how FRIDA works and the limitations it has.

Get INMUNE7’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After a while, I felt confident. I opened the APK file again, read some classes, and found what I was looking for … YES !!

Press enter or click to view image in full size
Figure 7. create a client example class

Again, the lack of code obfuscation makes me work easily.

In the newBuilder.addHeader() instruction we can see how the X-ACME-Token Header is added and how Sec.access is called. According to the code, three parameters are needed, the first is a Context object, the second is a unique ID, and the last one is an URL.

At this point, we can use FRIDA.

The POC

FRIDA uses python code to enable frida-tools, in this article I explain how is the installation of frida-tools. So I create a basic skeleton of code in python.

Figure 8. Python wrapper code

The next step is to create a JavaScript snippet.

Press enter or click to view image in full size
Figure 9. Example of JavaScript snippet

There is a lot of more code in Figure 9 to show, however, I am interested in to show you the function used to generate the token.

In this code we hook to the Environment class and create a new instance of it, call the setter method, and define a new value using a random string. The next part is the getValidToken function.

Press enter or click to view image in full size
Figure 10. getValidToken() method

In this code, we overload the token function of com.acme.account.Sec. With this function overloaded we can create our acmeID and pass as an argument to the function which generates the token.

Press enter or click to view image in full size
Figure 11. Token generation

Yeah, it worked … in Figure 11 you can see a list of token generated with FRIDA.

I configure Burpsuite Intruder with my list of tokens and then I tried to brute force a valid user of ACME…

Press enter or click to view image in full size
Figure 12. Burpsuite intruder

Oh no!!!!! After 54 requests the server return code 500 (which means server error) the status code 400 is for an invalid password but after a series of request the server detect my brute force attack… Nooooo!!! :(

The exploit

I never give up, so, after resting, I came to the battle again and found this…

Press enter or click to view image in full size
Figure 13. Context information

The Context … if I remember one of the parameters of the token.access function is a Context object, so what happens if I overload the token function again and define it with 3 strings parameters?

Press enter or click to view image in full size
Figure 14. Token method overload

I overload the function and configure my payload with my list of the token.

…come on this has to work !!

Figure 15. Payload configuration

And DAWN men it worked…. Yeahhhh !!!

Figure 16. Brute force attack success using Intruder

After 303 requests the server still returns 400 code indicating that the password is invalid… Yeah !!!!

What happened here?

With FRIDA, we overload the function of Token.access so at run-time when I executed my python script which inside uses my JavaScript snippets and lunch an instance of com.acme.app in my emulated android device, the method definition is overloaded, so when I called the method getValidToken(), I am not calling the default method (token), I am calling the overloaded method passing 3 strings as arguments, so I don’t need to pass a context object. I have control of the three arguments and can pass random values to the token function.

I use these valid tokens to launch the attack…basically in the backend each request appears valid and the server doesn’t detect my brute force attack.

Yeah !!!!

…But how we can fix this?

The “solution”

I found a better way around token-based implementation to prevent brute force attacks using SafetyNET reCAPTCHA API. Figure 17 is a detailed definition.

Press enter or click to view image in full size
Figure 17. SafetyNET definition

This is a basic diagram of how SafetyNET reCAPTCHA does work. In Figure 18 you can see 3 actors (Android app, SafetyNET, and Android Server). The Android app has a Site Key (something like a Public key) which is used to communicate with the SafetyNET server. Then SafetyNET server returns the captcha challenge to the user and then sends the token to the server for validation. The server has the secret key and validates the token against SafetyNET, then SafetyNET server validates this token using its own analyst engine. The response is sent to the server and the server handles the token depending if it is valid or invalid.

Press enter or click to view image in full size
Figure 18. SafetyNET basic architecture
What about ACME ?

At the end of this journey, I made my report including a detailed explanation about the vulnerability and how to fix it.

Of course, adding SafetyNET to an application in production is not a trivial step, requires planning and in some case, it needs to validate against product team because adding a CAPTCHA affect the user experience using the application.

I didn’t exploit any vulnerability like Buffer Overflow, CSRF, SSRF, or something similar, in this case, the vulnerability is the token implementation by itself. Some times you need to spend time in order to understand the application to find this kind of bugs.

Please let me know how if you implement SafetyNET reCAPTCHA API and how was the experience.

Bye-bye …

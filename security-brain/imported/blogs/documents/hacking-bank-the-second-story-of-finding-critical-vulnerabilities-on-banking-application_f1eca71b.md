---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-26_hacking-bank-the-second-story-of-finding-critical-vulnerabilities-on-banking-app.md
original_filename: 2022-11-26_hacking-bank-the-second-story-of-finding-critical-vulnerabilities-on-banking-app.md
title: '[Hacking Bank] The Second Story of Finding Critical Vulnerabilities on Banking
  Application'
category: documents
detected_topics:
- otp
- mobile-security
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- otp
- mobile-security
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: f1eca71b87c7eb46c7bb0b285fc3d5a64c204296ab7e9970941161d12c4967ca
text_sha256: edf56d012996d9184c1c49b9ae4625de6b5d13bf6bebd4e03babc2ac80ed7d61
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# [Hacking Bank] The Second Story of Finding Critical Vulnerabilities on Banking Application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-26_hacking-bank-the-second-story-of-finding-critical-vulnerabilities-on-banking-app.md
- Source Type: markdown
- Detected Topics: otp, mobile-security, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `f1eca71b87c7eb46c7bb0b285fc3d5a64c204296ab7e9970941161d12c4967ca`
- Text SHA256: `edf56d012996d9184c1c49b9ae4625de6b5d13bf6bebd4e03babc2ac80ed7d61`


## Content

---
title: "[Hacking Bank] The Second Story of Finding Critical Vulnerabilities on Banking Application"
url: "https://medium.com/@protostar0/hacking-bank-the-second-story-of-finding-critical-vulnerabilities-on-banking-application-ac20cd8f3dad"
authors: ["Abdelhak Kharroubi"]
bugs: ["Android", "Hardcoded credentials", "IDOR"]
publication_date: "2022-11-26"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1855
scraped_via: "browseros"
---

# [Hacking Bank] The Second Story of Finding Critical Vulnerabilities on Banking Application

[Hacking Bank] The Second Story of Finding Critical Vulnerabilities on Banking Application
Abdelhak Kharroubi
Follow
5 min read
·
Nov 27, 2022

208

This is new post about reversing a banking application that uses the “Xamarin” platform, bypassing the integrity of the requests and finding critical vulnerabilities that allow attackers to access the internal platform, obtain full user information (passwords, account balance, transaction list) even to send money just with the victim’s phone number.

1- Getting around the application:

First, I start checking the requests of the application in Burp; we need to run Frida server in the background and start the banking application in a rooted device.
I used frida_multiple_unpinning.js to disable the SSL pinning and intercept all requests between the app and the API.

Press enter or click to view image in full size

Changing anything in the request with Burp Repeater will result in this error.

Press enter or click to view image in full size

The “ONB-CS header” looks to be the signature used to verify the request’s integrity.

Moving to the JADX-GUI to see how this header was generated — but there’s nothing interesting inside the JAVA source code. I tried searching for the header name and found nothing.

Press enter or click to view image in full size

I started searching in source code of the app and googling to check for which platform is used in developing this application and I found Xamarin SDK and DLL files in Resources > assemblies

What is Xamarin?

.NET is a developer platform made up of tools, programming languages, and libraries for building many different types of applications. Xamarin extends the .NET developer platform with tools and libraries specifically for building apps for Android, iOS, tvOS, watchOS, macOS, and Windows.

So, it’s a platform for developing Android and iOS apps using.NET and C#, which explains why dll files are used in Android apps.

I kept looking for a way to reverse this dll until I came across the tool ILSpy, which is an open-source .NET assembly browser and decompiler.

I used the tool to decompile the dll files and saved it as C# code clear text so that I could open it in Sublime Text.

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I located the function responsible for the signature by searching for “ONB-CS” on all C# files, using Sublime Feature.

Press enter or click to view image in full size

This hashes the request body using HMACSHA256 with ClientSecret as the key. By searching for the next keyword “***BankClientSecret”,I discovered critical information disclosed on the app settings that leads to access to an internal platform that allows fetching of all users data (First Vulnerability).

Press enter or click to view image in full size
2-Testing the API:

To automate the test, I write the signature function in Python that does the same thing (HMACSHA256 with ***BankClientSecret as key ).

Press enter or click to view image in full size

The login function in Python should be like this:

Press enter or click to view image in full size

And I received a valid response after running the script.

Press enter or click to view image in full size

PS: I used Proxychains to chain the Python requests to the Burp Suite, so I can view the requests on Burps History as well.

Press enter or click to view image in full size

I noticed that the login request doesn’t really return any session tokens on the response, which is weird. I checked the next API call “GetAccountFullInfo” , which takes only the account number as input.

Press enter or click to view image in full size

I need another account number to test IDOR, I could have tried to brute force the account number but it would take time and I might be blocked.

So I continue checking the app’s other features and discovered that the create OTP request returns critical data like: hashed password, hashed pin, account number and it simply requires the phone number.(Vulnerability 2)

Press enter or click to view image in full size

I utilized LinkedIn to find someone who worked at the bank in order to obtain his phone number, then I used the Python script to validate the signature check and I sent the request.

Now I have all of his details!!

Press enter or click to view image in full size

Returning to the GetAccountFullInfo API, i can test the IDOR Vulnerability with the victim’s account number. and it’s Vulnerable!!

Press enter or click to view image in full size

I test the other API calls like Get Statement ,Sending Money …., and it worked !!(Vulnerability 3).

Press enter or click to view image in full size
3- Exploitation:

I wrote a Python script that requires only the victim’s phone number to gather all of the user’s information from the bank’s API.

Press enter or click to view image in full size
Conclusion:
The signature check “ONB-CS HEADER” appears to be the only security check in the Backend of this API.
DO NOT RELY ON FRONT-END SECURITY ONLY !!!!!!!!!!!!!!!!!!!!!!

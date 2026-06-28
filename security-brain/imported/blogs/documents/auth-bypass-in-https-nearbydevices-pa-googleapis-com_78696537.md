---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-16_auth-bypass-in-httpsnearbydevices-pagoogleapiscom.md
original_filename: 2021-05-16_auth-bypass-in-httpsnearbydevices-pagoogleapiscom.md
title: Auth Bypass in https://nearbydevices-pa.googleapis.com
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 78696537a283ccfc5a1a474cd0c727b816855af217affe8d3f071f98a31dee2d
text_sha256: fc6e697742f013f00a70a675e733a69538646fcfb65b977f649f23e7eee51194
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# Auth Bypass in https://nearbydevices-pa.googleapis.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-16_auth-bypass-in-httpsnearbydevices-pagoogleapiscom.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `78696537a283ccfc5a1a474cd0c727b816855af217affe8d3f071f98a31dee2d`
- Text SHA256: `fc6e697742f013f00a70a675e733a69538646fcfb65b977f649f23e7eee51194`


## Content

---
title: "Auth Bypass in https://nearbydevices-pa.googleapis.com"
page_title: "[#0004] Complete takeover of any Google Fast Pair headphones vendor settings & secrets | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0004"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0004"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Broken Access Control"]
bounty: "5,000"
publication_date: "2021-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3650
---

#0004  
Vendor: Google  
Status: fixed  
Reported: Feb 15, 2021  
Disclosed: May 16, 2021 (90 days) 

# Complete takeover of any Google Fast Pair headphones vendor settings & secrets

**Summary:**

I think this is pretty bad. Using this issue, a malicious attacker could have **full CRUD (Create, Read Update, Delete) access to all Google[Fast Pair devices](https://developers.google.com/nearby/fast-pair/spec)**. The attacker could even steal the secret Anti-Spoofing Private Key for any device, which would allow the attacker to **spoof the given device’s identity** and/or to **perform MITM attacks against any new Fast Pair Bluetooth connection established with that device**.

**Core issue:**

The API `nearbydevices-pa.googleapis.com` **doesn’t seem to perform any kind of access control**. Thus, a normal authenticated user can access/modify/delete any resource, including resources the user doesn’t own. This allows full CRUD access to all Fast Pair devices.

**Steps to reproduce:**

  1. Create 2 users: `Attacker` and `Victim`
  2. With both users, visit `https://developers.google.com/nearby/devices/`, log in, and create one GCP project when prompted
  3. With both users, in new tabs, go to `https://console.cloud.google.com/`, and note both new project’s `Project number`s
  4. [`Victim`] Go to `Add Device`, and create a new device. (Choose `Fast Pair` -> `Headphones` for the least required fields & You must upload an 512x512 image)
  5. [`Attacker`] Start proxying the traffic with Burp
  6. [`Attacker`] In Burp, go to `Proxy` -> `Options` -> `Match and Replace` and click `Add`
  7. [`Attacker`] Set the type to `Request body`, set `Match` to `Attacker`’s `Project number`, set `Replace` to `Victim`’s `Project number` from `Step 3`, and click `OK`
  8. [`Attacker`] Click on the `Devices` button, and see a list of `Victim's` devices
  9. [`Attacker`] Click on the device created in `Step 4` and see that you can access its secret Anti-Spoofing Private Key, add a new firmware revision, edit the device, view analytics, delete the device, and more. Basically attacker now has full access to all of `Victim`’s resources, just by changing the project number.

**A real-world attack:**

For the above POC, an attacker needs to know the project ID of the targeted device.  
Thats not bad, but we can do better.

Here is a theoretical real world MITM attack against all second generation Google Pixel Buds devices:

  1. Attacker would like to MITM Bluetooth connections between Pixel Buds devices and victims. For this, Attacker would need to obtain the Pixel Buds’s Anti-Spoofing Private Key. This key is (hopefully) [stored in the secure enclave](https://developers.google.com/nearby/fast-pair/spec#antispoofing) of every manufactured Pixel Buds device. So it is hidden from the Attacker.
  2. Attacker buys a Pixel Buds, and proxies her phone’s traffic while pairing the device.
  3. From the proxy logs, attacker finds the gRPC request her phone made to `nearbydevices-pa.googleapis.com/location.nearby.v1.NearbyDevicesService/GetObservedDevice`, and extract’s the Pixel Buds’s `Model ID` and `Project Number` from the response protobuf
  4. Attacker now has all of the necessary information to access the Pixel Buds’s Anti-Spoofing Private Key
  5. Attacker sends this request, which returns the Anti-Spoofing Private Key:

  
  
  GET /v1/projects/[pixel's_project_number]/devices/[prixel's_model_id_in_decimal]?key=AIzaSyBbXGPRxbh6-U8pujg5-lABDGuThIjtn38 HTTP/1.1
  Host: nearbydevices-pa.googleapis.com
  Authorization: Bearer [attacker's_nearby_dashboard_access_token]
  

  6. Attacker now can [MITM any new Fast Pair Bluetooth connection](https://developers.google.com/nearby/fast-pair/spec#ProcedureExamples) between any second generation Pixel Buds and any victitm.

_I performed this attack until`Step 4.` to confirm that the gRPC response leaks the `Project Number`. By this, I found that the second generation Pixel Buds’s has a `Model ID` of `9616317` (`0x92BBBD` in hex), and a `Project Number` of `88849360756`._

Or, you know, if an attacker want’s to be just pure destructive, she could just **delete the Pixel Buds device** , so Fast Pair Seekers don’t recognize it anymore. Or, she could **change the Pixel Buds’s name/image to something inappropriate**. Or, do anything, basically.

**[!!] Because of this, if previous malicious access to this API can’t be confidently refuted, consider ALL already-generated Anti-Spoofing Private Keys on the Fast Pair platform COMPROMISED.**

**Extras / The horror-story of decoding the protobuf:**

  * I wanted to make sure that the `GetObservedDevice` gRPC method returns the device’s `Project Number`, so I wanted to decode the binary protobuf. I spent basically a day trying to decode that protobuf without success. Every tool I tried (`protoc`, `blackboxprotobuf`, …) failed to decode the response, not sure why. I found out how gRPC prefixed the proto payload, but even after removing the prefix, every tool failed. I even tried programmatically cutting out bytes from the beginning/end, without success.
  * I was forced to use the protobuf response, since the same REST endpoint, `/v1/device/[device-id]`, for some reason only returned the ID you gave to it, without doing anything.
  * After quite a few hours and almost loosing all hope, I added `$outputDefaults=1` to the REST endpoint, and it returned every field, but of course, they were all empty.
  * I knew that if I change the `Content-Type` to `application/json+protobuf`, the response will include the field IDs of the protobuf. I used this, and `$outputDefaults=1` to correlate the `id` and `projectNumber` to the protobuf field ID `1` and `2`, because the ordering of the fields looked the same in both cases.
  * After checking where the strings were the binary protobuf, I concluded that it’s thankfully in the same exact order as in the REST responses. So I only need to decode the first 2 fields in the protobuf, and simply ignore everything else.
  * Since all tools failed on me, I took the last road. I had to [hand-decode](https://developers.google.com/protocol-buffers/docs/encoding#structure) the protobuf. It was _very epic_ :

  
  
  0a -> 00001010 -> 00001 010 -> length-delimited:2 ID:1
  lenght:
  ca 07 -> 11001010 00000111
  -> 10010100000111
  -> len = 9479 ?! (I just noticed that this is incorrect. I din't swap the bytes)
  
  08 -> 1000 -> varint:0 ID:1 ("id")
  bd f7 ca 04 -> 10111101 11110111 11001010 00000100
  ->  0111101  1110111  1001010  0000100
  -> 0000100 1001010 1110111 0111101
  -> 0000100100101011101110111101
  -> device ID: 9616317 0x92BBBD (pixel buds) omg, this is correct!!
  
  10 -> 10000 -> varint:0 ID:2 ("projectNumber" !!)
  f4 ce d6 fe ca 02 -> 11110100 11001110 11010110 11111110 11001010 00000010
  ->  1110100  1001110  1010110  1111110  1001010  0000010
  -> 0000010 1001010 1111110 1010110 1001110 1110100
  -> 00***REDACTED-SUSPECT-TOKEN***  -> project ID: 88849360756
  

**[Disclosure Warning]:**

**This issue is subject to a 90 day disclosure deadline.** On `2021-05-16` this issue will be publicly disclosed. If you would like to redact additional information or if for some reason the issue can’t be fixed until the deadline, let me know in a comment.

Thank you!

* * *

### Comments:

**Vendor - 2021-02-15 17:21**

_NOTE: This e-mail has been generated automatically._

Thanks for your report.

This email confirms we’ve received your message. We’ll investigate and get back to you once we’ve got an update. In the meantime, you might want to take a look at the [list of frequently asked questions about Google VRP](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq).

If you are reporting a security vulnerability and wish to appear in Google Security Hall of Fame, please [create a profile](https://bughunter.withgoogle.com/new_profile).

You appear automatically in our Honorable Mentions if we decide to file a security vulnerability based on your report, and you will also show up in our Hall of Fame if we issue a reward.

**Note that if you did not report a vulnerability, or a technical security problem in one of our products, we won’t be able to act on your report. This channel is not the right one if you wish to resolve a problem with your account, report non-security bugs, or suggest a new feature in our product.**

Cheers,  
Google Security Bot

[Follow us](https://twitter.com/googlevrp) on Twitter!

* * *

**Vendor - 2021-02-16 22:19**

_NOTE: This e-mail has been generated automatically._

Hey,

Just letting you know that your report was **triaged** and we’re currently looking into it.

You should receive a response in a couple of days, but it might take up to a week if we’re particularly busy. In the meantime, you might want to take a look at [the list of frequently asked questions about Google VRP](https://sites.google.com/site/bughunteruniversity/behind-the-scenes/faq).

Thanks,  
Google Security Bot

* * *

**Vendor - 2021-02-24 13:45**

Hi,

🎉 **Nice catch!** I’ve filed a bug based on your report.

The panel will evaluate it at the next VRP panel meeting and we’ll update you once we’ve got more information. All you need to do now is wait. If you don’t hear back from us in 2-3 weeks or have additional information about the vulnerability, let us know!

Regards,  
[redacted], Google Security Team

* * *

**Vendor - 2021-03-04 21:20**

** NOTE: This is an automatically generated email **

Hello,

Thank you for reporting this bug. As part of Google’s Vulnerability Reward Program, the panel has decided to issue a reward of $5000.00.

Important: if you aren’t registered with Google as a supplier, p2p-vrp@google.com will reach out to you. If you have registered in the past, no need to do it again - sit back and relax, and we will process the payment soon.

If you have any payment related requests, please direct them to p2p-vrp@google.com. Please remember to include the subject of this email and the email address that the report was sent from. Regards,

Google Security Bot

If you’d like your name added to our Hall of Fame:
  
  
  https://bughunter.withgoogle.com/
  

Just create a profile here: https://bughunter.withgoogle.com/new_profile

In addition, we encourage you to signup for our Vulnerability Research Grants program, where we issue monetary payments to VRP researchers, even when no vulnerabilities are found. To read more about the program visit: https://www.google.com/about/appsecurity/research-grants/

– How did we do? Please fill out a short anonymous survey (https://goo.gl/IR3KRH).

* * *

**Me - 2021-04-26 17:51**

Hi,

This bug will be publicly disclosed in 20 days, on `2021-05-16`.

Can you please confirm that the issue has been fixed and that no `Anti-Spoofing Private Key` was compromised using this attack?

Thank you,  
David

* * *

**Vendor - 2021-04-30 20:24**

hi!

the team is currently working on the fix, there’s two steps for the fix, and the first step is almost done, but the second one has been taking some time to complete.

* * *

**Me - 2021-05-06 12:44**

Hi,

The 90 day deadline will expire in 10 days, on `2021-05-16`. Will a fix be rolled out by then?

If a fix is scheduled to fully roll out in the next 14 days after the deadline, let me know, and the disclosure will be delayed by 2 weeks, as described in Google Project Zero’s “Grace period”.

Can you please confirm that (after the issue has been fixed) no `Anti-Spoofing Private Key` was compromised using this attack?  
Since as far as I know, once compromised, these keys can not be changed on the devices already manufactured. Users should be aware if their model’s key is compromised, thus allowing MITM attacks.

Thank you,  
David

* * *

**Vendor - 2021-05-07 22:26**

Thanks David!

We have been making several changes, so you probably wont be able to exploit this anymore, but we are still working on making more changes, and the last of those changes probably won’t land until June 16.

The keys are updatable through firmware updates, but some devices dont get firmware updates :). That said, those that do, also probably store the key in the clear anyway.

Maybe it’s worth noting that the keys we are talking about here are on the devices that the customers buy (so you can get them from there too in most cases by just dumping the firmware), so they may allow for impersonation of an “original device”, but otherwise shouldn’t have significant security consequences. Also, fastpair doesn’t allow for most bluetooth profiles, so besides being a music sink and a few other things, it should not be too serious for users. All devices require user confirmation/etc.

I suggest you look at the difference with Fastpair with a key you own, and a key you take from another device (if you didn’t keep any keys from when the bug was working, maybe find the firmware of some device with fastpair and extract the key from there).

* * *

**Me - 2021-05-16 23:38**

Hi,

Thank you for the response.

So, my conclusion is that this means that users _should not_ rely on any security protection this “secret” `Anti-Spoofing Private Key` provides, especially they _should not_ rely on MITM protection, and consider all their Bluetooth traffic sniffable by a malicious party.

Thats a bit sad, because it would be a very nice feature of Fast Pair, but I guess it would be hard (or even impossible) to push out a secret key in consumer devices in a way that the owners can’t ever access it.

(Hopefully, at least the Pixel Buds follows the spec, and uses a Secure Element to store the key.. 😬)

Thank you,  
David

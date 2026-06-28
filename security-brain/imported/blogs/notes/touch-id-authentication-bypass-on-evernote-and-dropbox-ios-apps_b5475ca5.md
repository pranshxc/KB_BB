---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-03_touch-id-authentication-bypass-on-evernote-and-dropbox-ios-apps_2.md
original_filename: 2020-04-03_touch-id-authentication-bypass-on-evernote-and-dropbox-ios-apps_2.md
title: Touch ID Authentication Bypass on Evernote and Dropbox IOS Apps
category: notes
detected_topics:
- command-injection
- automation-abuse
- mobile-security
tags:
- imported
- notes
- command-injection
- automation-abuse
- mobile-security
language: en
raw_sha256: b5475ca5234d3e8e269850dbf42444f130cdca0cde775d9bc8714a3cee8b540f
text_sha256: 886e91273743676f8828ec2f5f7777a0458324fa91573ac49d2597d4ee60b741
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Touch ID Authentication Bypass on Evernote and Dropbox IOS Apps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-03_touch-id-authentication-bypass-on-evernote-and-dropbox-ios-apps_2.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b5475ca5234d3e8e269850dbf42444f130cdca0cde775d9bc8714a3cee8b540f`
- Text SHA256: `886e91273743676f8828ec2f5f7777a0458324fa91573ac49d2597d4ee60b741`


## Content

---
title: "Touch ID Authentication Bypass on Evernote and Dropbox IOS Apps"
url: "https://medium.com/@pig.wig45/touch-id-authentication-bypass-on-evernote-and-dropbox-ios-apps-7985219767b2"
authors: ["Sahil Tikoo (@viperbluff)"]
programs: ["Evernote", "Dropbox"]
bugs: ["Authentication bypass", "iOS"]
publication_date: "2020-04-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4669
scraped_via: "browseros"
---

# Touch ID Authentication Bypass on Evernote and Dropbox IOS Apps

Touch ID Authentication Bypass on Evernote and Dropbox IOS Apps
Sahil Tikoo
Follow
6 min read
·
Apr 3, 2020

54

2

This blog will walk you through the technique that I used to bypass Touch ID authentication feature implemented on the Login Page in Evernote and Dropbox IOS apps.

Just Before Getting Started, I will list down the tools that were used in this process:

Iphone 6S with ios 13.3.1
Checkra1n executable for semi tethered Jailbreaking
Frida on PC & frida server on device
Objection on PC

Lets get started folks!!

Prologue

Jailbreaking ios 13.3.1: First and foremost install checkra1n executable on your PC in my case I had mac OS , you can install the dmg from here https://checkra.in/#release and continue with the entire process of jailbreaking until your device reboots , finally you will be presented with a checkra1n IPA through which cydia and other custom apps can be installed.

Jailbroken Iphone 6S with ios 13.3.1

You can refer this blog for the entire Jailbreak process: https://www.redmondpie.com/jailbreak-ios-13.3.1-using-checkra1n-heres-how-guide/.

Once you have a jailbroken device the next step in the process is to install frida server through cydia(a store to download all the apps).

Frida server on Iphone 6S

Finally Install frida and objection on Your PC in my case I had mac OS, you can install Objection from https://github.com/sensepost/objection/wiki and frida will get automatically installed , you just need to have python3 installed.

Methodology

Once you have all the tools necessary to test Touch ID feature implemented in the apps , the roadmap is clear and pretty straightforward.Install Evernote and Dropbox apps from the App store and interact with these apps through frida server and objection.Finally Bypass authentication by utilizing commands available in objection.

Pre Configuration before Attack

Install Evernote and Dropbox apps from the app store , once installed also check if frida and objection are working perfectly or not on your PC .Let us enable TouchID’s for both the apps now.

Setting up Touch ID in Evernote

Steps:

Go to your profile
Go to settings
Click on passcode Lock
Click `Turn Passcode On`
Setup the passcode and once its done TouchID will be automatically enabled.
Evernote Touch ID enabled

Setting up Touch ID in Dropbox

Steps:

Go to your profile
Click on the settings logo on the top left corner
Click `Turn Passcode On`
Setup the passcode and once its done slide the TouchID button.
Dropbox Touch ID enabled
Understanding the Attack

Let us confirm whether TouchID’s are working or not, after configuring Touch ID for both the apps , close the apps and open them again, if you are presented with a banner like Touch ID for “Evernote” or Touch ID for “Dropbox” then you are good to go.

Get Sahil Tikoo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But…. Before we begin the actual attack Lets Understand the bypass first.

Note: I will just briefly give you an idea about how it was actually bypassed and then we begin with the practical demo.

Basically when a User puts his/her fingerprint for the TouchID auth then a class LAContextis invoked in the application code which in turn calls the evaluatePolicy method , inside this method fingerprint data in the form of a mathematical expression is checked against the fingerprint data stored in Secure Enclave of the device.Depending on the success or failure of the authentication itself, a reply block is invoked that includes a boolean indicating if it was successful or not.

So if the auth was successful we get a boolean true else a boolean false return value.We use a command ios ui biometrics_bypass in objection tool for bypassing this boolean value check , after using this command, objection starts interacting with frida server on the device.Frida server during runtime, changes the false value to true , gives heads up to objection and bang we get access.

Note: Checkout the entire description about this command and how it works https://github.com/sensepost/objection/wiki/Understanding-the-iOS-Biometrics-Bypass in this post.

Final Attack

Lets Begin the demo for bypass now.We will go step by step so its easy to understand.The bypassing techniques used in both Dropbox and Evernote are same as described above.So, the steps would remain the same, i will be just adding two different Image POC’s to make it clear that bypass is present on both the apps.

Steps:

Connect your Iphone with the PC
First we need to identify under what names apps are running on the phone.
Run frida-ps -U on your PC terminal
Press enter or click to view image in full size
Frida command on PC terminal

4. The apps are usually running by their own names “Evernote” and “Dropbox” as you can see in the above Image.

5. Open the Evernote App

6. Next step is to run objection with the commands like:

objection -g Evernote explore

Press enter or click to view image in full size
Objection command Evernote

7. Now use ios ui biometrics_bypass command as shown below along with that you can also observe a localized reason in the Image was identified by the agent or we can say frida server, Sometimes frida server or the agent isn’t able to identify the touchID pop up while opening the app and you won’t see the localized reason message in objection so make sure to lock the phone without closing the app and again unlock it quickly to observe that the code was hooked properly.

Press enter or click to view image in full size
biometric bypass command [Evernote]

8. As you can see below wrong fingerprint attempts were made on the Touch ID , it might sometimes take three attempts to bypass , make sure while making the attempts objection is running in terminal and device is connected with a USB cable.

Evernote fingerprint wrong attempts

9. So finally during the 3rd wrong attempt , below are the results on both objection terminal and app GUI as well:

Press enter or click to view image in full size
Bypass Complete on Evernote app

10. As you can see in the image below , Evernote dashboard accessed by bypassing the fingerprint auth mechanism.

Evernote dashboard accessible

Similarly for Dropbox as well follow all the steps from step5 to step9.Finally during the 3rd wrong attempt in the case of dropbox as well , below are the results observed on both objection terminal and app GUI :

Press enter or click to view image in full size
Bypass Complete on Dropbox app

Dropbox dashboard also accessible after bypassing the fingerprint auth mechanism.

Dropbox dashboard accessible

Note:Just let me know through DM on my twitter handle https://twitter.com/viperbluff how this Vulnerability can be patched :-)

Hope u guys liked it !!

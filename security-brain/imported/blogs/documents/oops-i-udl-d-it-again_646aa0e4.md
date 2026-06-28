---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-15_oops-i-udld-it-again.md
original_filename: 2024-08-15_oops-i-udld-it-again.md
title: Oops I UDL'd it Again
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 646aa0e4497c5db8c97d5cc0d53c9e92be30cbd604cb11a6982fc7c6f3490928
text_sha256: e813c6ff25eb5ff4533e982437d08da17f6cf9c965b2d300086fec0ca4012be5
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Oops I UDL'd it Again

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-15_oops-i-udld-it-again.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `646aa0e4497c5db8c97d5cc0d53c9e92be30cbd604cb11a6982fc7c6f3490928`
- Text SHA256: `e813c6ff25eb5ff4533e982437d08da17f6cf9c965b2d300086fec0ca4012be5`


## Content

---
title: "Oops I UDL'd it Again"
page_title: "TrustedSec | Oops I UDL'd it Again"
url: "https://trustedsec.com/blog/oops-i-udld-it-again"
final_url: "https://trustedsec.com/blog/oops-i-udld-it-again"
authors: ["Oddvar Moe (@Oddvarmoe)"]
bugs: ["Phishing"]
publication_date: "2024-08-15"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 68
---

* [Blog](https://trustedsec.com/blog)
  * [Oops I UDL'd it Again](https://trustedsec.com/blog/oops-i-udld-it-again)

August 15, 2024

# Oops I UDL'd it Again

Written by Oddvar Moe 

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OopsUDLAgain_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767063731&s=d311396a9f92870559d43ab8108504da)

Table of contents

  * Introduction
  * The Discovery
  * Details about Universal Data Link Configuration (UDL) files
  * Using UDL Files for Phishing
  * Conclusion

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#231c505641494640571e604b4640480611134c5657061113574b4a500611134251574a404f4606111345514c4e0611137751565057464770464006111205424e5318414c475a1e6c4c53500611136a06111376676f061114470611134a570611136244424a4d0610620611134b57575350061062061165061165575156505746475046400d404c4e061165414f4c440611654c4c53500e4a0e56474f470e4a570e4244424a4d "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Oops%20I%20UDL%27d%20it%20Again%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again&mini=true "Share on LinkedIn")

## Introduction

Phishing. We all love phishing. This post is about a new phishing technique based on some legacy knowledge I had that can be used to get past email filters and such. I would expect that after publication, this method will be identified and addressed by most vendors.

## The Discovery

As usual, the discovery was made during an engagement where I actually did something completely different. I was in a scenario where I needed to find the databases servers through a locked down Citrix session. Based on some old notes I had from 2017, I knew that there is a native way to enumerate database servers in Windows environments by simply creating an empty file with the .udl extension. Once that file is created, you can open it and you will be presented with a GUI that looks like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig1_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121713&s=2a6df94cb8cac112a077bad9c96a3ec3)

The interesting part for this scenario is that you can press the down arrow on the top line (1. Select or enter server name), then it will broadcast the network for available SQL servers and list them right below the down arrow. This gave me what I needed at the time; however, I could not stop thinking about the struggles I had early in the engagement with getting any phish into the mailboxes. Out of curiosity, I decided I would simply send this to my own mailbox from a test account I had and see if the attachment would come through. To my big surprise, it did! It was not even blocked by Outlook and that is a great thing.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig2_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121714&s=b6909a39c3d3b8dd973c39941d7c48a1)

This is when I started to research if I could abuse this in a phishing scenario, and, you guessed right, you can.

## Details about Universal Data Link Configuration (UDL) files

The main purpose of UDL files is to be able to test connections towards a database server. The UDL file supports various providers, and this also depends somewhat on what is installed on the host. However, there are a few standard providers that are most likely to be present. For instance, the Microsoft OLE DB Provider for SQL Server, which is also the default chosen for new UDL files.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig3_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121715&s=5178c83ded7aa3c212a88e306224ca34)

The Connection tab is the default shown when you open a UDL file, and these fields change based on the provider that has been chosen. Looking at the 'Connection' tab when using the default provider, we can see that you can fill out a server name, choose between integrated security, and choose to enter username and password. You can also choose to select a database on the server or attach a database file as a database name.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig4_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121717&s=73e2ca9ee94a2b738b3cc0920d7b61de)

I will leave the rest of the tabs up to you to explore, however no adjustment of settings on these are necessary for this to work. since it is not really that interesting. Let’s enter a server name. set it to use windows integrated security, and press OK to store it.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig5_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121718&s=c86f1f6538a38fe944779859a7ce49c5)

Now, lets take a look at what a UDL file actually looks like by opening it in Notepad (The best editor next to Nano).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig6_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121720&s=d69207c3fbf4b956802756209e5bf243)

That’s it. That’s the entire file. It is just a text file. Based on some experimentation, the commented line needs to be present for it to work as a UDL file. You also might be wondering what happens when you press the 'test connection' button. Well, that is where things get interesting, because it will attempt to connect to the server defined in the server name field on port 1433. Upon successful connection, it will then use Integrated Security to authenticate as the user. If you choose to fill in a specific username and password however, it will send that as part of the authentication. And I am assuming you can seewhere this is heading in terms of phishing. We need to send this to a user with a pretext that gets the user to either press 'test connection' or fill in their username and password before hitting it. Now that you have some details, let’s see if we can use this in a phishing scenario.

## Using UDL Files for Phishing

Let’s first see if we can capture a hash with this technique. First, fire off a Responder instance on a public IP address (Just add the public IP address to the server name) and see what happens when you press 'test connection'. As you can see, you now have a NetNTLMv2 hash (As shown in the screenshot below).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig7_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121721&s=eb678756c04e9708458227ad7910bcee)

On the client side, you will get an error message like the one shown below, so take that into account when creating the actual pretext.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig8_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121723&s=d4b59cbb3ace8c51b59388761b72b04e)

When using the option to let the user fill the username and password, the flow will look like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig9_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121724&s=0577ae87efe1ac348034d57122f7ae2a)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig10_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121724&s=e5afceaa393f05d3f5529a67734c9b30)

One thing to note on filling username and password, is that you can prefill the username before you send it to the user, making the pretext more believable.

This is cool and all, but in most cases , based on my experience, port 1433 will be blocked outbound from the customer, making this technique somewhat useless. You can take a gamble on that it will be open, of course, but let’s see if we can make things little more exciting. Let's change the port to a more friendly one, for instance, port 80. The trick is that you can simply change the port in the server name field by adding a comma between the name and ip and the port like this: **servername_or_ip,80**. It should look like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig11_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121725&s=d9330052beced0eef14910431eb02f7e)

The only problem is that if you press 'test connection' now, Responder will not understand what to do since this is a MSSQL connection and not a standard HTTP connection. For this to work, we need to adjust Responder a bit. I will walk you through the minor changes we need to adjust, so no need to worry.

Firstly, you will need to change the responder.conf file and turn off the HTTP server. I recommend using nano since it is the superior editor (Yes, this is a running joke in TS).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig12_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121726&s=4bd23431fa1af8ad452f9b997b1e6c34)

Next, we need to change the port in the code so that the Responder SQL server will listen on port 80. Change the 1433 in line [370](https://github.com/lgandx/Responder/blob/4947ae6e52df031b591049f8e2e904f2454bd96c/Responder.py#L370) inside the Responder.py script to 80, as shown below:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig13_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121729&s=0216ea7fc5186dae9ea2bbea441acf21)

Save the file and refire Responder, then try and hit test connection with it pointing to port 80, and you should get a hash. You are now ready to create a pretext and ship this bad boy of a payload out the door. In terms of pretext, I will leave that up to you to find a good one. If you want to use one file per user that you are sending to with the username prefilled, I have a Powershell script that [you can find here](https://github.com/api0cradle/RedTeamScripts/blob/main/generate-udl.ps1) that you can use.

## Conclusion

As you can see, diving into older knowledge can certainly be a great thing when you are up against Modern Defenses, and Windows sure has a lot of historical file formats and legacy things. Who would have known that this file format could be used for phishing? My prediction is that after posting this blog, Microsoft will start to default block the UDL file format in Outlook, since this technique is now know.

If you want to learn more about the UDL file format you can [visit this link](https://learn.microsoft.com/en-us/sql/connect/oledb/help-topics/data-link-pages?view=sql-server-ver16).

Hope you found this post interesting, learned something new, and got inspired.

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#b08fc3c5d2dad5d3c48df3d8d5d3db958280dfc5c4958280c4d8d9c3958280d1c2c4d9d3dcd5958280d6c2dfdd958280e4c2c5c3c4d5d4e3d5d395828196d1ddc08bd2dfd4c98dffdfc0c3958280f9958280e5f4fc958287d4958280d9c4958280f1d7d1d9de9583f1958280d8c4c4c0c39583f19582f69582f6c4c2c5c3c4d5d4c3d5d39ed3dfdd9582f6d2dcdfd79582f6dfdfc0c39dd99dc5d4dcd49dd9c49dd1d7d1d9de "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Oops%20I%20UDL%27d%20it%20Again%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again&mini=true "Share on LinkedIn")

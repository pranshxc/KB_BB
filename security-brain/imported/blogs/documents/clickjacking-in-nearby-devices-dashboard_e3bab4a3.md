---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-17_clickjacking-in-nearby-devices-dashboard.md
original_filename: 2021-05-17_clickjacking-in-nearby-devices-dashboard.md
title: Clickjacking in Nearby Devices Dashboard
category: documents
detected_topics:
- command-injection
- clickjacking
- cloud-security
tags:
- imported
- documents
- command-injection
- clickjacking
- cloud-security
language: en
raw_sha256: e3bab4a36292488c3ccf6b2c2700d23d5d1d3a0cdb5ef3e127dd73c01a00cbc8
text_sha256: 1dde7f56a05f44a0e3402e1b75d9bbed10934d6b34c6e7b517988ede214d6dce
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Clickjacking in Nearby Devices Dashboard

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-17_clickjacking-in-nearby-devices-dashboard.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `e3bab4a36292488c3ccf6b2c2700d23d5d1d3a0cdb5ef3e127dd73c01a00cbc8`
- Text SHA256: `1dde7f56a05f44a0e3402e1b75d9bbed10934d6b34c6e7b517988ede214d6dce`


## Content

---
title: "Clickjacking in Nearby Devices Dashboard"
page_title: "[#0005] Clickjacking in Google Fast Pair Vendor Dashboard | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0005"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0005"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Google"]
bugs: ["Clickjacking"]
publication_date: "2021-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3647
---

#0005  
Vendor: Google  
Status: fixed  
Reported: Feb 16, 2021  
Disclosed: May 17, 2021 (90 days) 

# Clickjacking in Google Fast Pair Vendor Dashboard

**Summary:**

Clickjacking is possible on the Nearby Devices Dashboard. Using this, (among other things) an attacker could create a malicious webpage which can trick a victim into deleting his/her own device.

**POC Video:**

<https://youtu.be/kqfsgEJjgEM> (`00:15`) (`music`)

**Core Issue:**

The Nearby Devices Dashboard page on `https://developers.google.com/nearby/devices/` actually embeds `https://developers-dot-devsite-v2-prod.appspot.com/nearby/devices/index_c4c5649698417947f28fa2ba0f3267ae10a9a13b3b687a720a65984cfff9e812.frame`, which displays the Dashboard. This host behaves just like `developers.google.com`, but looks like an AppEngine App.

The host `developers-dot-devsite-v2-prod.appspot.com` doesn’t have any framing protections.

When a victim uses the Nearby Devices Dashboard, she has to log in. When she logs in, since the whole Dashboard is in an iframe, the login cookies get set on `developers-dot-devsite-v2-prod.appspot.com`.

So, its possible to embed `developers-dot-devsite-v2-prod.appspot.com`, and a victim will have valid cookies, so the embedded frame will be logged in.

**Steps to reproduce:**

  1. Create/log into a Google account
  2. Go to `https://developers.google.com/nearby/devices/`, log in, and create a GCP project when prompted
  3. Go to `Add Device`, and create a new device. (Choose `Fast Pair` -> `Headphones` for the least required fields & You must upload an 512x512 image)
  4. Convert the new device’s `Model ID` from hex to decimal (e.g. for the Pixel Buds: `0x92BBBD` -> `9616317`)
  5. Open the POC HTML file from below, and add the ID after the `#` sign in the URL (e.g. `poc.html#9616317`)
  6. When the POC loads, see that the device management page got embedded, and clicking the `Click here for cat pics!!` deletes the victim’s device

**POC Code:**
  
  
  <html>
  <body>
  <button id="button" style="pointer-events: none;z-index:1;left:460px;position:relative;top:-330px;background-color: greenyellow;"><b>Click here for<br/>cat pics!!</b></button>
  <iframe id="iframe" width=500px height=500px style="opacity: 0.1;"></iframe>
  </body>
  <script>
  document.getElementById("iframe").src = "https://developers-dot-devsite-v2-prod.appspot.com/nearby/devices/index_c4c5649698417947f28fa2ba0f3267ae10a9a13b3b687a720a65984cfff9e812.frame#/devices/view/" + window.location.hash.substring(1);
  
  window.addEventListener("blur", function(){
  var elem = document.createElement('iframe');
  elem.style.cssText = 'position:absolute;width:50%;height:50%;z-index:100';
  elem.src = "https://www.youtube.com/embed/5wOXc03RwVA?autoplay=1"
  document.body.appendChild(elem);
  });
  </script>
  </html>
  

**Real-world Attack:**

_Attacker wants to delete the second generation Pixel Buds device, to cause a DOS for users who want to pair with it._

  1. Attacker buys a Pixel Buds
  2. [From the BLE advertisements](https://developers.google.com/nearby/fast-pair/spec#advertising_payload_fast_pair_model_id_data), Attacker notes that the Pixel Buds has a `Model ID` of `0x92BBBD`
  3. Attacker converts this ID to decimal `0x92BBBD` -> `9616317`
  4. Attacker sets up the POC, and sends the malicious link (`poc.html#9616317`) to a Google Engineer who is logged into the Nearby Devices Dashboard and has access to the Pixel Buds device
  5. If the Google Engineer clicks `Click here for cat pics!!`, the Pixel Buds device gets deleted, probably causing a DOS/other issues for users who want to pair with their Pixel Buds

**[Disclosure Warning]:**

**This issue is subject to a 90 day disclosure deadline.** On `2021-05-17` this issue will be publicly disclosed. If you would like to redact additional information or if for some reason the issue can’t be fixed until the deadline, let me know in a comment.

Thank you!

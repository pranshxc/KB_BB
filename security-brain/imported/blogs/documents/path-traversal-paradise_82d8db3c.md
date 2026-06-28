---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-23_path-traversal-paradise.md
original_filename: 2022-01-23_path-traversal-paradise.md
title: Path Traversal Paradise
category: documents
detected_topics:
- path-traversal
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- path-traversal
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 82d8db3ce41d1033c0979c22f3c40bd4d35b2768af6f4c8512e8f4934616a529
text_sha256: 7b2bb350d780ba08d8c998c9e17e6bd438f1534732f833a3843ed73341aa7215
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Path Traversal Paradise

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-23_path-traversal-paradise.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `82d8db3ce41d1033c0979c22f3c40bd4d35b2768af6f4c8512e8f4934616a529`
- Text SHA256: `7b2bb350d780ba08d8c998c9e17e6bd438f1534732f833a3843ed73341aa7215`


## Content

---
title: "Path Traversal Paradise"
page_title: "Path Traversal Paradise :: kuldeepdotexe's blog"
url: "https://kuldeep.io/posts/path-traversal-paradise/"
final_url: "https://kuldeep.io/posts/path-traversal-paradise/"
authors: ["Kuldeep Pandya (@kuldeepdotexe)"]
bugs: ["Path traversal", "LFI"]
publication_date: "2022-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2988
---

Hi, guys!

This blog will be about all the different kinds of Path Traversals and Local File Inclusion vulnerabilities that I have found in Synack Red Team.

After hacking on Synack Red Team for approximately 9 months, I came to realise that Path Traversal and LFI like vulnerabilities are very common. I reported few authenticated vulnerabilities and few unauthenticated. However, I will try to cover both kinds of vulnerabilities.

Before moving forward, I’d like to list all my Path Traversal/LFI submissions.

### Submissions⌗

Submission | Status  
---|---  
[Path Traversal Vulnerability Leads To Source Code Disclosure](/posts/path-traversal-paradise/#path-traversal-vulnerability-leads-to-source-code-disclosure) | Accepted  
[Local File Inclusion in VMWare VCenter running at [REDACTED]](/posts/path-traversal-paradise/#local-file-inclusion-in-vmware-vcenter-running-at-redacted) | Accepted  
[Spring Boot Path Traversal - CVE-2020-5410](/posts/path-traversal-paradise/#spring-boot-path-traversal---cve-2020-5410) | Accepted  
[Local File Inclusion In download.php](/posts/path-traversal-paradise/#local-file-inclusion-in-downloadphp) | Accepted  
[Local File Inclusion In download.php](/posts/path-traversal-paradise/#local-file-inclusion-in-downloadphp) | Rejected (Duplicated my previous report)  
[Local File Inclusion In download.php](/posts/path-traversal-paradise/#local-file-inclusion-in-downloadphp) | Rejected (Duplicated in quality period)  
[Path Traversal Allows To Download Licence Keys](/posts/path-traversal-paradise/#path-traversal-allows-to-download-licence-keys) | Accepted  
  
### Descriptions⌗

#### Path Traversal Vulnerability Leads To Source Code Disclosure⌗

This was the very first Path Traversal vulnerability that I had found in Synack Red Team. Also, even though I was pretty new to the platform and to the whole bug bounty thing in general, this report won the quality round so I am very proud of this particular report.

After logging into the application, the application provided a bunch of sections like manage vendors, manage inventory, etc with a bunch of functionalities.

Upon further inspecting these sections, I came across an interesting functionality that involved importing the data. The file was named `DataImport.view`.

![DataImport.view](/DataImport.png)

I tried getting RCE by uploading a web shell and it actually worked! However, that’s a different story. We want to discuss Path Traversals here and not RCEs.

So, after successfully uploading a file, we were given the functionality to read the file.

![ReadFile](/ReadFile.png)

After clicking the “**ReadFile** ” button, it filled the file name field to the current uploaded filename by default. However, we had the ability to change the file name.

Now, I just had to provide a valid file name. For this, I used the `Auth.aspx` to which the login request was sent. I could be sure that this exists because a login request was sent to this file and it resided in the webroot.

So, I tried to do path traversal using payloads like `../Auth.aspx` and `../../Auth.aspx` etc.

And, after three `../` sequences, the file was actually returned!

![Auth.aspx](/Auth.png)

The response looked like this:

![AuthResponse](/AuthResponse.png)

The file was broken because some sort of XML parsing was done on it. I still went ahead and reported it because it was still a path traversal issue and disclosed source code contents.

I could do more creative things here like pulling more sensitive files but I stopped here because very limited time was left in the quality round. I initially did not care much for this vulnerability as I had already reported an RCE there but then quickly made a report in under 15 minutes putting together all my PoCs and I still won the quality round.

#### Local File Inclusion in VMWare VCenter running at [REDACTED]⌗

This was the classic VMWare VCenter `/eam/vib` LFI vulnerability.

The `/eam/vib` endpoint in VMWare VCenter instances takes a parameter named `id` in the GET request. The value to this `id` parameter is a file name that will be retrieved by the VCenter instance and will be given back in the response.

There are already many resources regarding this particular vulnerability and I do not think much is to be said about it in this particular article.

I used the following payload to retrieve the `hosts` file off the remote server:
  
  
  https://[REDACTED]/eam/vib?id=C:/WINDOWS/System32/drivers/etc/hosts
  

There were some IP to host mappings in the `hosts` file which I thought was enough for impact but with creativity, more could have been achieved.

I reported the issue during the quality round and this also won the QR.

#### Spring Boot Path Traversal - CVE-2020-5410⌗

This was a known vulnerability in Spring Boot Cloud Config server. For PoC, I referred to this article here: <http://www.jrasp.com/case/CVE-2020-5410.html>

That article talks in detail about the vulnerability and also explains the source code.

I did not read that much and simply took the PoC from there and used it on the target that I had for testing. And the exploit worked!

I used the same payload as in the PoC which is:
  
  
  https://[REDACTED]/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%252Fpasswd%23foo/development
  

The above payload retrieves the `/etc/passwd` file.

However, this was Java and one odd thing about Java Path Traversals/LFIs is that if you specify a directory instead of a file for opening, it will actually list the content of that directory.

So, for example, if I did not know what files were in the `/etc` directory, I would simply use the following payload to list all the files:
  
  
  https://[REDACTED]/..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252F..%252Fetc%23foo/development
  

This is just the previous payload with the trailing `/passwd` removed. Now, we are just listing the contents of the `/etc` directory.

I used this feature to list the contents of the root directory in the affected Linux server. In the root directory, I found a file named `application.jar` which was potentially the source code of the currently running Spring Boot Cloud Config server.

Also, the root directory had a file `.dockerenv` so I was quite sure that I was in a docker container.

However, Synack Red Team has the stop-and-report policy according to which, we are not supposed to do post-exploitation.

I reported the issue during the 8 hours long quality period. And nobody had checked for this particular vulnerability and mine was the only report in QR.

#### Local File Inclusion In download.php⌗

I have already discussed this vulnerability in my previous article and you can find it here: [Local File Inclusion In download.php](/posts/120-days-of-high-frequency-hunting/#local-file-inclusion-in-downloadphp)

#### Path Traversal Allows To Download Licence Keys⌗

This path traversal was also very interesting. This was in a custom-built application and it did not require any authentication.

When we visited the webroot, the web application redirected us to the login page.

The login page was custom built and there was a brand logo along with the login page so I cannot show you the screenshots.

Upon visiting the login page, a request to the `/web/product_logo` endpoint was sent. The request contained a GET parameter named `logo`.

Overall, the request URL looked like this:
  
  
  https://[REDACTED]/web/product_logo?logo=logo.png
  

The parameter `logo` took a file name as the input and returned that particular file in the response. In this case, it was `logo.png`.

Now, as this is functionality to read files, there may be a potential LFI/Path Traversal here. So, I changed the file name to `index` with different extensions. However, none of them worked.

So, I ran `ffuf` hoping to discover more files but it was a failure. I used the `raft-small-files-lowercase.txt` provided in the [SecLists](https://github.com/danielmiessler/SecLists).

I did not know the underlying technology which is used so it was quite painful to enumerate files.

However, I knew it was a Windows box because of the case-insensitive directory structure. What it basically means is that, in Windows, `WinDows` and `Windows` are the same directories/files as it is not case sensitive. And when I was doing my recon, I received the same response when I did `/web` or `/Web` so I was quite sure it was a Windows box.

There are other ways to determine this too but I decided to assume it was Windows.

Same as my past submissions, I decided to read the `C:/WINDOWS/System32/drivers/etc/hosts` file of the remote server.

So, I used a path traversal payload and the final URL looked like this:
  
  
  https://[REDACTED]/web/product_logo?logo=../WINDOWS/System32/drivers/etc/hosts
  

However, one `../` sequence did not work. So I kept increasing the `../` sequences.

Finally after 10 `../` sequences, I finally hit the `hosts` file and the server retrieved it for us.

The final payload looked like this:
  
  
  https://[REDACTED]/web/product_logo?logo=../../../../../../../../../../WINDOWS/System32/drivers/etc/hosts
  

Although this was enough for PoC, I decided to dig deeper with this path traversal.

When I was fuzzing the application, I encountered an error that disclosed the full path to the webroot.

I ran `ffuf` again but now in the webroot of the server using the path traversal that I had found. This way, I was able to enumerate a file named `LICENSE` that had license keys of the application.

I reported the issue with all my findings and the report won the QR.

Thanks for the read. :)

You can reach out to me at [@kuldeepdotexe](https://twitter.com/kuldeepdotexe).

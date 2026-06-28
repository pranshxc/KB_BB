---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-25_revisiting-an-old-bug-file-upload-to-code-execution.md
original_filename: 2023-10-25_revisiting-an-old-bug-file-upload-to-code-execution.md
title: 'Revisiting an Old Bug: File Upload to Code Execution'
category: documents
detected_topics:
- command-injection
- sso
- file-upload
- rate-limit
- automation-abuse
- graphql
tags:
- imported
- documents
- command-injection
- sso
- file-upload
- rate-limit
- automation-abuse
- graphql
language: en
raw_sha256: 42fd33de3ffa26d4a6488a0c880eb8c2c4e07536ecb96e0e7cb64ef4d3993dd0
text_sha256: 24b707e6823f74944ae00833f599b1c80c6db6afd8251f66673c13bf029bf7ad
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Revisiting an Old Bug: File Upload to Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-25_revisiting-an-old-bug-file-upload-to-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, sso, file-upload, rate-limit, automation-abuse, graphql
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `42fd33de3ffa26d4a6488a0c880eb8c2c4e07536ecb96e0e7cb64ef4d3993dd0`
- Text SHA256: `24b707e6823f74944ae00833f599b1c80c6db6afd8251f66673c13bf029bf7ad`


## Content

---
title: "Revisiting an Old Bug: File Upload to Code Execution"
page_title: "CVE-2021-27198 – Securifera"
url: "https://www.securifera.com/blog/2023/10/25/cve-2021-27198/"
final_url: "https://www.securifera.com/blog/2023/10/25/cve-2021-27198/"
authors: ["b0yd (@rwincey)"]
programs: ["Visualware"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2023-10-25"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 698
---

CVE-2021-27198

![](https://www.securifera.com/wp-content/uploads/2023/10/file_upload.jpg)

### **This article is in no way affiliated, sponsored, or endorsed with/by Visualware, Inc. All graphics are being displayed under fair use for the purposes of this article.**

## **Revisiting an Old Bug: File Upload to Code Execution**

### A colleague recently contacted me about a [bug](https://www.securifera.com/advisories/cve-2021-27198/) I discovered a couple of years ago (CVE-2021-27198). The vulnerability was an unauthenticated arbitrary file upload issue in version 11.0 to 11.0b of the [Visualware MyConnection Server](https://myconnectionserver.visualware.com/download) software. At the time I hadn’t actually proven remote code execution even though I rated it as critical. So when my colleague asked me how I exploited it, I felt like I had to show it was possible. This endeavor proved to be both challenging and enlightening so I thought I’d share the experience.

### The MyConnection Server software is coded in Java and intended to work seamlessly across different platforms. In this case, the arbitrary file write was privileged, granting the file server elevated permissions, with SYSTEM on Windows and root on Linux. With a privileged file write, achieving code execution is often straightforward. This [post](https://blog.doyensec.com/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html) by Doyensec outlines the most common approaches, which can be broadly categorized into two groups: web application-specific and operating system-specific. Web application-specific methods involve seeking ways to initiate execution within the web server process. Examples include uploading web framework configuration files or web application source code. On the other hand, operating system-specific techniques involve finding execution triggers controlled by the operating system itself, such as services, scheduled tasks, cron jobs, and so on.

### Regrettably, in the case of this particular bug, I cannot directly target the web server itself since it’s a pure Java implementation, as opposed to using a web server framework like Apache or Nginx. As a result, our focus will primarily shift towards exploring operating system-specific possibilities or more innovative approaches.

## **Windows RCE**

### With this in mind, I began researching possible techniques for achieving code execution solely through a file write. In the Windows environment, my usual strategy would involve targeting vulnerable applications susceptible to traditional DLL hijacking or [phantom DLL hijacking](https://www.crowdstrike.com/blog/4-ways-adversaries-hijack-dlls/), leveraging the privilege granted by such writes.

### I opened up [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) Procmon tool and began looking for “NAME NOT FOUND” or “PATH NOT FOUND” results for CreateFile. I usually look for instances of executables or DLLs. While looking through the results, I noticed that every minute the MCS java process is attempting to open several “rtaplugin” JAR files, some of which do not exist.

![](https://www.securifera.com/wp-content/uploads/2023/10/prcomon2.png)

### Based on the output, it looks like the server is dynamically loading these JARs from disk into the java process. If this is the case, I may be able to get arbitrary code execution by simply placing a custom JAR file in a specific place on the file system. I decided to open up the MCS JAR in [JD-GUI](http://java-decompiler.github.io/) to investigate.

### When I searched for “rtaplugin”, I found a class named RTAPlugin that has a function that appears to load a file from disk, create a custom ClassLoader, loads a class from the file, and then creates a new instance of the class. This is exactly what I need!

![](https://www.securifera.com/wp-content/uploads/2023/10/load_jar.png)

### To confirm execution, I created a simple POC that executes calc.exe when an instance of the class is created.

![](https://www.securifera.com/wp-content/uploads/2023/10/payload1.png)

### I then just manually copied the JAR into the appropriate directory to see if it was loaded. I was thrilled to see that it worked! Now I just needed to test it using the file upload vulnerability.

![](https://www.securifera.com/wp-content/uploads/2023/10/calc.png)

### I loaded up Burp and pasted in the JAR file as the body of the file upload request. Unfortunately when I sent it over, I didn’t see calc.exe in the process list.

![](https://www.securifera.com/wp-content/uploads/2023/10/burp_req.png)

### When I opened up the log file for the MyConnection server, I found the following exception was thrown when attempting to unzip the JAR.

![](https://www.securifera.com/wp-content/uploads/2023/10/crc.jpg)

### I took the original JAR payload and diff-ed it against the one that was uploaded into the rtaplugin directory. I found that certain bytes were getting corrupted. I opened up JD-GUI again to take a closer look at the code that performed the file write.

![](https://www.securifera.com/wp-content/uploads/2023/10/file_write.jpg)

### What wasn’t immediately obvious (at least to me) was that there was an implied encoding/decoding that was happening with the calls to String.valueOf and String.getBytes. As a result, certain ranges of bytes were getting corrupted. On Windows I found that bytes between 0x80 and 0x9f were being replaced with other values. This meant I had to do some bit fiddling to get the payload to work.

### After doing a little bit of googling, I found a [CTF writeup](https://hackmd.io/@ptr-yudai/S1LWYdOm9) by Yudai Fujiwara that faced a similar encoding problem. The writeup provided code for generating a zip file that only contained bytes in the ASCII range, 0x0 – 0x7f. The script primarily focused on two structures in the zip protocol that needed to be free of non-ascii bytes, the CRC for zipped files, and any length fields.

### The script brute-forces a valid ASCII value for the CRC field by iteratively modifying the inner file. In the CTF challenge, the zip contained an ASCII script, whereas a JAR contains a binary class file. I updated the algorithm to perform a similar modification to the Java source, and then recompile the Java class file on each iteration to make the CRC update.

Copy to Clipboard

Syntax Highlighterwhile True: cmd = ['/opt/jdk1.7.0_80/bin/javac','-cp','/opt/mcs/java.jar', '/opt/mcs/error.java'] output = subprocess.check_output(cmd) class_file_contents = '' with open("/opt/mcs/error.class", "rb") as f: class_file_contents = f.read() class_file_len = len(class_file_contents) if class_file_len > 0: crc32 = binascii.crc32(class_file_contents) logger.info("CRC: " + hex(crc32)) if all([(crc32 >> i) & 0xff < 0x80 for i in range(0, 32, 8)]): if all([(class_file_len >> i) & 0xff < 0x80 for i in range(0, 32, 8)]): break else: new_needle = needle + random.choice(string.ascii_letters)*0x2 else: new_needle = needle + random.choice(string.ascii_letters) # Add more data to the src with open("/opt/mcs/error.java", "r") as f: y = f.read() new_data= y.replace(needle, new_needle) with open("/opt/mcs/error.java", "w") as f: f.write(new_data) # Update needle needle = new_needle

### After creating the ascii-zip payload, I uploaded it using the vulnerable endpoint. As hoped, it was loaded and executed as SYSTEM on the target server. To keep from having to recompile a JAR to execute different commands, I generated a JAR that would execute a script at a known location. I could then separately upload that script with a new command whenever I wanted command execute. I added the “setExecutable” directive to ensure it worked on Linux as well.

![](https://www.securifera.com/wp-content/uploads/2023/10/payload2.jpg)

## **Linux RCE**

### When dealing with Linux-based operating systems, one of the primary challenges when exploiting arbitrary file write vulnerabilities is ensuring that file permissions are correctly configured. Even if a file is executed, it won’t function if it isn’t marked as executable. To overcome this obstacle, I am targeting files that already have the execute bit set.

### As I had anticipated, demonstrating exploitation on Linux turned out to be quite straightforward by simply overwriting scripts within the /etc/cron.* directories. On Red Hat distributions, you can achieve relatively timely execution by overwriting the /etc/cron.hourly/0anacron script. The drawback to targeting cron jobs is there is no guarantee specific scripts exist, and overwriting them can cause system instability.

### 

![](https://www.securifera.com/wp-content/uploads/2023/10/0anacron.png)

### Assuming outbound network connectivity isn’t blocked, a[ simple reverse shell](https://book.hacktricks.xyz/generic-methodologies-and-resources/shells/linux) is likely the simplest payload to put in the cron job. If that doesn’t work, the cron job can be modified to contain a base64 encoded copy of the unmodified rtaplugin JAR that is then copied to the correct directory. The same technique as described above can then be used to get repeated code execution by uploading different versions of the script to _**/tmp/b.bat**_.

### 

## **No License, No Wurk!**

### After all the effort put in to develop the rtaplugin exploit, I was disappointed to find out that rtaplugins (and the associated thread that loads them periodically) are only active when the web server has a valid license. I wasn’t aware of this because my test instance was still within its trial phase. I decided to take another look and see if our privileged file write vulnerability (CVE-2021-27198) can be used once again, but this time to trick the server into thinking it is licensed. The hope here is to find a file or database entry that can modified with our file upload exploit to bypass licensing. **I want to be sure to clarify here, nothing I will describe here can be used to subvert or crack the license for this software on a fully patched system. The goal is to use our already privileged file system access to bypass any license checks.**

### When you navigate to the web application home page, you’ll see a menu on the left that contains a link to “Licensing”. It’s safe to assume this is the right place to look.

![](https://www.securifera.com/wp-content/uploads/2023/10/license.png)

### Sadly, when you click on it, you’re presented with the login page. If you’re fortunate and the password for the admin user hasn’t been changed, the next page you’ll encounter is shown below.

![](https://www.securifera.com/wp-content/uploads/2023/10/login.jpg)

### If you’ve made it this far, or happen to guess some credentials, you will have sufficient permissions to access the server licensing endpoint. There’s not much to go on in regards to the format of the expected key other than the hint that it starts with MCS.

![](https://www.securifera.com/wp-content/uploads/2023/10/licensing.png)

### I opened up the JAR again and tracked down the code responsible for handling the license activation. The handler performs a series of checks and transforms before making a web request to a visualware domain to verify the license.

![](https://www.securifera.com/wp-content/uploads/2023/10/http_verify2.jpg)

### If that fails (by exception), the server then attempts to validate the license by sending a specially crafted DNS request.

![](https://www.securifera.com/wp-content/uploads/2023/10/dns_verify.jpg)

### Leveraging the privileged file write capability of CVE-2021-27198, there are several methods at my disposal for circumventing the licensing without having to decipher the licensing key directly. As the software initiates a network request to validate the entered key, it can be rerouted to a server under my control to authenticate the supplied key.

### The most straightforward method to achieve this is by modifying the hosts file, a file which contains mappings of IP addresses to hostnames, and is typically the first location an operating system checks when resolving a hostname’s IP address. On Windows systems, you can find this file at _**C:\Windows\System32\drivers\etc\hosts**_ , and on *nix systems, it’s located at _**/etc/hosts**_. To manipulate the license verification process, I can simply insert a new entry into the hosts file, directing the license server domain to the IP address of a server under my control.

![](https://www.securifera.com/wp-content/uploads/2023/10/hosts.png)

### An alternative approach, specific to *nix systems, involves altering the /etc/resolv.conf file, which specifies the DNS server’s IP address used for domain resolution. By changing the DNS server address to a server that I manage, I can ensure that any DNS requests for the license server are resolved to my fake license server’s IP address.

### **WARNING: It should be noted that overwriting the /etc/hosts or /etc/resolv.conf file can cause system instability if certain configurations are expected to properly resolve custom DNS entries or resolvers.**

### My next step is to trace back the activate function to the web endpoint that can trigger it. Unfortunately, it appears the key entered into the web form is not the same format as what is sent to the license server. After performing a couple string-based checks, a validate function is called on the provided license key. If you look at the function closely, it may look familiar. It appears to be implementing a handcrafted version of RSA.

![](https://www.securifera.com/wp-content/uploads/2023/10/rsa.png)

### From a security standpoint, the rationale behind requiring an encrypted license key as the input into the web application doesn’t make sense. First and foremost, since the unencrypted license key is subsequently transmitted over the network, unencrypted, it can easily be captured with a tool like Wireshark. Secondly, the actual license key is verified on the vendor’s server so deducing how the license key is generated is impractical. Unfortunately for me however, this has introduced a minor obstacle in reaching the network activation function detailed in the previous section.

### The astute reader may have already noticed an interesting detail about the RSA parameters. That public key looks awful small. Just barely over 256 bits. It appears our CTF challenge continues… (oh wait this is real software).

![](https://www.securifera.com/wp-content/uploads/2023/10/pub.jpg)

### For those imposters in the infosec community that claim playing CTF doesn’t provide real world experience, I can confidently say you’ve never hunted real bugs. All too often I come across exploit chains that appear as if someone neatly setup each primitive for me to uncover. I personally don’t spend a ton of time attempting crypto challenges when playing CTFs, mostly because I’m not smart enough. Luckily for me, this example would fit nicely into the baby’s first category. With such a small public key, I should be able to find a CTF writeup that guides me through the process of breaking it down into its two prime numbers. A few searches later I found an [article](https://yurichev.com/news/20220210_RSA/) by Dennis Yurichev that demonstrates using a tool called [CADO-NFS](https://cado-nfs.gitlabpages.inria.fr/) to do just that. After about 5 mins I was presented with the answer.

![](https://www.securifera.com/wp-content/uploads/2023/10/cado.png)

### With the two prime numbers in hand, I attempted to reconstruct the private key using the script provided in Yurichev’s post. Unfortunately, the RSA crypto libraries in python didn’t play well with the provided primes. Namely because the block size rounded up to 257 bits and it complained about truncation. I also discovered that the server’s custom RSA implementation didn’t implement padding. To get around these issues I wrote code to perform the calculations manually rather than using a crypto library.

Copy to Clipboard

Syntax Highlighterfrom Crypto.Util.number import bytes_to_long from Crypto.Util.number import inverse def encrypt_with_private_key_raw(data): p = 624106295606602100995951586143562696483 q = 264089186086669371634156709929132346711 e = 17 n = p * q phi = (p - 1) * (q - 1) d = inverse(e, phi) # Convert data to an integer and perform raw RSA encryption m = bytes_to_long(data) ciphertext = pow(m, d, n) return ciphertext

### I used my script to generate an encrypted blob with the derived RSA private key and fired off a web request with a finished license key. Keep in mind, since I’ve already overwritten the hosts file, I only need to pass the decryption checks as the key will not be transmitted to the vendor’s server for verification. To my delight, it works!

![](https://www.securifera.com/wp-content/uploads/2023/10/activated.jpg)

## **Conclusion**

### My journey to developing a working exploit for CVE-2021-27198 finally comes to an end. What started as a simple exercise turned into quite an endeavor. For anyone interested, I’ve uploaded my exploit [here](https://github.com/rwincey/CVE-2021-27198).

By [b0yd](https://www.securifera.com/blog/author/b0yd/)|2024-04-15T14:25:43+00:00October 25th, 2023|[Uncategorized](https://www.securifera.com/blog/category/uncategorized/)|[0 Comments](https://www.securifera.com/blog/2023/10/25/cve-2021-27198/#respond)

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&t=CVE-2021-27198 "Facebook")[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&text=CVE-2021-27198 "X")[Reddit](https://reddit.com/submit?url=https://www.securifera.com/blog/2023/10/25/cve-2021-27198/&title=CVE-2021-27198 "Reddit")[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&title=CVE-2021-27198&summary=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Visualware%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0ARevisiting%20an%20Old%20Bug%3A%20File%20Upload%20to%20Code%20Execution%20%0D%0AA%20colleague%20recently%20contact "LinkedIn")[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&name=CVE-2021-27198&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Visualware%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0ARevisiting%20an%20Old%20Bug%3A%20File%20Upload%20to%20Code%20Execution%20%0D%0AA%20colleague%20recently%20contacted%20me%20about%20a%20bug%20I%20discovered%20a "Tumblr")[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Visualware%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0ARevisiting%20an%20Old%20Bug%3A%20File%20Upload%20to%20Code%20Execution%20%0D%0AA%20colleague%20recently%20contacted%20me%20about%20a%20bug%20I%20discovered%20a&media=https%3A%2F%2Fwww.securifera.com%2Fwp-content%2Fuploads%2F2023%2F10%2Ffile_upload.jpg "Pinterest")[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.securifera.com%2Fblog%2F2023%2F10%2F25%2Fcve-2021-27198%2F&title=CVE-2021-27198&description=This%20article%20is%20in%20no%20way%20affiliated%2C%20sponsored%2C%20or%20endorsed%20with%2Fby%20Visualware%2C%20Inc.%20All%20graphics%20are%20being%20displayed%20under%20fair%20use%20for%20the%20purposes%20of%20this%20article.%20%20%0D%0A%0D%0ARevisiting%20an%20Old%20Bug%3A%20File%20Upload%20to%20Code%20Execution%20%0D%0AA%20colleague%20recently%20contacted%20me%20about%20a%20bug%20I%20discovered%20a "Vk")[Email](mailto:?body=https://www.securifera.com/blog/2023/10/25/cve-2021-27198/&subject=CVE-2021-27198 "Email")

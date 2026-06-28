---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-03_story-of-youtubes-unfixable-ads-bypass.md
original_filename: 2022-01-03_story-of-youtubes-unfixable-ads-bypass.md
title: Story of YouTube’s Unfixable Ads Bypass
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 0f4a2337521718a54b8bad81f24cd54d2c50d61a0ad010c0975a744cdc84ad34
text_sha256: 8b66b59eb64c55e6f0b19eb052e641b73efeb421108ab2035e27760aa7d692c6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Story of YouTube’s Unfixable Ads Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-03_story-of-youtubes-unfixable-ads-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `0f4a2337521718a54b8bad81f24cd54d2c50d61a0ad010c0975a744cdc84ad34`
- Text SHA256: `8b66b59eb64c55e6f0b19eb052e641b73efeb421108ab2035e27760aa7d692c6`


## Content

---
title: "Story of YouTube’s Unfixable Ads Bypass"
url: "https://medium.com/@mrmax4o4/story-of-youtubes-unfixable-ads-bypass-b3bb7016c14e"
authors: ["MrMax4o4"]
programs: ["Google"]
bugs: ["Logic flaw"]
publication_date: "2022-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3037
scraped_via: "browseros"
---

# Story of YouTube’s Unfixable Ads Bypass

Story of YouTube’s Unfixable Ads Bypass
MrMax4o4
Follow
4 min read
·
Jan 3, 2022

197

1

Hello there!
I hope everything is going well with you; today I will talk about my YouTube Ads bypass.

Story time:

On 10th September 2021 I was watching some videos on YouTube and by mistake I double-clicked a couple of times on my mouse right click button, the “Show Controls” option caught my eyes

I clicked it and found this timeline bar showed up

Press enter or click to view image in full size

I couldn’t use it because it’s under the main timeline bar so I had to remove the main timeline to use it, I used the Inspector and removed the main timeline bar

Press enter or click to view image in full size

It’s a basic timeline bar with its basic functions no more! before I refresh the page to get the YouTube main timeline again I was curious to know if I can use this bar while there is an Ad, I picked a random video and found some Ad, used the “Show Controls” option and surprise! I was able to control the Ad timeline (before the 5 seconds to skip) like a normal video!

Now I have 2 problems,

It’s hard to exploit.
The “Show Controls” bar disappears after every use.

To solve these problems and to make it as easy as possible I decided to make a browser extension.

How To make a browser extension (Firefox/Chrome):

I made a directory and created 2 files

manifest.json: Contains the extension configurations.

{

“manifest_version”: 2,
“name”: “Manual Ad Skip”,
“version”: “1.0”,

“content_scripts”: [
{
“matches”: [“https://www.youtube.com/*"],
“js”: [“poc.js”]
}
]

}

The first three keys: manifest_version, name, and version, are mandatory and contain basic metadata for the extension.
content_scripts: Tells Firefox to load a script into Web pages whose URL matches a specific pattern. In this case, I am matching the YouTube URL, when the pattern is found the browser will call the poc.js script

2. poc.js: The script that will be executed when the YouTube URL is matched, the purpose of this file are two things:

Remove the YouTube’s main timeline bar
Show the “Show Controls” bar and Solve the problem that it disappears after every use.
#To remove the YouTube bar
var el = document.getElementsByClassName("ytp-chrome-bottom");
el[0].remove();
# To show the "show controls" bar and repeat this every 100 milliseconds
setInterval(function(){
 document.getElementsByClassName("video-stream html5-main-video")[0].setAttribute("controls","true");
}, 100);

Main timeline bar: I found its Class-name is ytp-chrome-bottom so I used the remove() function to remove it with all its components.

Get MrMax4o4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“Show Controls” timeline bar: I found its Class-name is video-stream html5-main-video and to enable the timeline bar the controls attribute must be true so I used the setAttribute() and finally to show the bar always I used the setInterval method.

It’s time to test the extension,

Firefox: navigate to Add-ons and items > Tools for all add-ons > Debug add-ons > Load Temporary add-ons and select the mainifest.json file.
Chrome/Chromium: navigate to More Tools > Extensions > Enable the developer mode > Load unpacked and select the extension directory.

The extension works very well!

I was like

Before reporting to to Google I decided to write another extension to automate the whole bypass process ( to avoid using the mouse).

While trying to automate the process I noticed that I can click the skip button to skip the Ads before the five seconds are up, I used this point to skip all the Ads

# remove the YouTube's main timeline bar
var el=document.getElementsByClassName("ytp-chrome-bottom");el[0].remove();
### Since the "Skip" button is only available when the Ad is played, I am checking if the button is found on the source code.
 var text="ytp-ad-skip-button ytp-button";
 setInterval(function(){
if (document.body.innerHTML.includes(text))
{
### if the button is found, click it to skip the ad
document.getElementsByClassName("ytp-ad-skip-button ytp-button")[0].click();
document.getElementsByClassName("video-stream html5-main-video")[0].setAttribute("controls","true");
  
}else{
### If not, Show our second timeline bar to skip any Ads in the middle of the video
  document.getElementsByClassName("video-stream html5-main-video")[0].setAttribute("controls","true");
  }
},100);

Finally it’s all ready now, I reported it and after a few days it was triaged and accepted (priority: P2 - severity: S2)

On 7th October 2021 Google closed the report

After some questions

At least I have YouTube without Ads now :)

Thanks for reading and wait for more 😉

Feel free to contact me ;)

Twitter — LinkedIn

Have a good day 😁

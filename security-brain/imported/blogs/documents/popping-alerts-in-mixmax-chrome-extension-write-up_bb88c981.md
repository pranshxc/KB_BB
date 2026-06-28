---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-06_popping-alerts-in-mixmax-chrome-extension-write-up.md
original_filename: 2020-02-06_popping-alerts-in-mixmax-chrome-extension-write-up.md
title: Popping Alerts in Mixmax Chrome Extension (Write Up)
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
raw_sha256: bb88c98184fb4cc6cc823bc0a595b535bdd3a3c64f927d25f7f4f4e9ed219a7f
text_sha256: 5a87838ed28dc83d418cf5691af51340c0f861dce18f7c8b7c751baf07e085de
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Popping Alerts in Mixmax Chrome Extension (Write Up)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-06_popping-alerts-in-mixmax-chrome-extension-write-up.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `bb88c98184fb4cc6cc823bc0a595b535bdd3a3c64f927d25f7f4f4e9ed219a7f`
- Text SHA256: `5a87838ed28dc83d418cf5691af51340c0f861dce18f7c8b7c751baf07e085de`


## Content

---
title: "Popping Alerts in Mixmax Chrome Extension (Write Up)"
page_title: "Evan Ricafort | Blog: Popping Alerts in Mixmax Chrome Extension (Write Up)"
url: "https://blog.evanricafort.com/2020/02/popping-alerts-in-mixmax-chrome.html"
final_url: "https://blog.evanricafort.com/2020/02/popping-alerts-in-mixmax-chrome.html"
authors: ["Evan Ricafort (@evanricafort)"]
programs: ["Mixmax"]
bugs: ["XSS"]
publication_date: "2020-02-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4783
---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifbPQs_DjNYd6poG_YYUyVBHOazQ4CFqbO4JX2j4AFqwGQZqeHl6Bg3wUAytSHw2Kgvhpwj65z92vBu78bvZK2zLqtfxuMnNTPhhuCZiQpfT1dY50y9s5oXtwTjm-ribxUCulMwxAk/s1600/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifbPQs_DjNYd6poG_YYUyVBHOazQ4CFqbO4JX2j4AFqwGQZqeHl6Bg3wUAytSHw2Kgvhpwj65z92vBu78bvZK2zLqtfxuMnNTPhhuCZiQpfT1dY50y9s5oXtwTjm-ribxUCulMwxAk/s1600/Screenshot_1.png)

  
  
  
Howdy!  
  
  
Back in 2017, I reported this simple XSS vulnerability that affects Mixmax Chrome Extension. The vulnerability was due to a feature called insert link/URL. This vulnerability didn't trigger on other user since the payload was filtered after it was push to the victim so ends up into self-XSS but Mixmax issued a fix and rewarded me a Mixmax swag that until now didn't arrive. (I don't know why). This vulnerability was reported to Mixmax via [Hackerone](https://hackerone.com/).  
  
  
**_\--Proof of Concept--_**  
**_  
_**  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiu9c5tZnIRvc-Pb11N4xlbE5oitxylfYrTu1V2Dv_AYvDuv-Na0LdSpHrr_mejWrHsCR-yfW06oort8kYZf_nNR687T3_oWkNkCJj3eFYlewCKMRjHT-uZ4GMUI-pyG5C2qVH4x5Xg/s640/2017-10-31_20-58-48.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiu9c5tZnIRvc-Pb11N4xlbE5oitxylfYrTu1V2Dv_AYvDuv-Na0LdSpHrr_mejWrHsCR-yfW06oort8kYZf_nNR687T3_oWkNkCJj3eFYlewCKMRjHT-uZ4GMUI-pyG5C2qVH4x5Xg/s1600/2017-10-31_20-58-48.gif)

**_  
_**_PS: Don't mind my inbox, nothing sensitive in there._  
_  
_**_\--Report Timeline--_**  
**_  
_****Report Title** : XSS in Mixmax Chrome Extension  
**Reported** : 2017-10-31 13:00:48 +0000  
**Triaged** : 2018-01-08 19:45:25 +0000  

> _We'll fix, thanks!_

**Fixed** : 2018-02-10 03:50:44 +0000  
**Reward** : Mixmax Swag  
  
I hope you enjoy this write up! stay tune for more contents like this in the future.  
  
Have a great day,  
Evan  
  

_**“To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.”**_

_― Ralph Waldo Emerson_

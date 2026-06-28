---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-10_how-i-got-500-with-open-redirect.md
original_filename: 2021-10-10_how-i-got-500-with-open-redirect.md
title: How I got $500 with Open redirect
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 5922ee53fc7de8ceaa9dddb541f442b935a53e284a5e87bb32a60eb45bac61d8
text_sha256: 387f75512ebd7ff5ebc38a92547476c086cf4d56a8bb59de9df80943913daf6d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $500 with Open redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-10_how-i-got-500-with-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `5922ee53fc7de8ceaa9dddb541f442b935a53e284a5e87bb32a60eb45bac61d8`
- Text SHA256: `387f75512ebd7ff5ebc38a92547476c086cf4d56a8bb59de9df80943913daf6d`


## Content

---
title: "How I got $500 with Open redirect"
url: "https://medium.com/@mamunwhh/how-i-got-500-with-open-redirect-48fd80c82631"
authors: ["khan mamun (@mamunwhh)"]
bugs: ["Open redirect"]
bounty: "500"
publication_date: "2021-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3250
scraped_via: "browseros"
---

# How I got $500 with Open redirect

How I got $500 with Open redirect
khan mamun
Follow
2 min read
·
Oct 10, 2021

225

7

Hei Everyone:) Hope you are fine.Today i will gonna share you How i find open redirect Bug on example.com website.I think everyone can get this bug out.so why i share? okk..Only when you read the text you will understand.

Ok Ready Boys;)

Site is example.com.First of all, i use nuclei tool for find Bug.But I did not get any bug. Because everyone runs nuclei tool so the chances of getting bug are less. Although it is more likely to be duplicate. Anyway, let’s hope it works, so when I didn’t get any bugs and no open redirect. Usually if there is any open redirect bug in the website, it can be found by nuclei tool.But this did not happen to me. I don’t know,why can’t find open redirect bug I bought from Nuclei. I think there was a missing any path .So, when I didn’t find any bugs, I opened the subdomain one by one and started looking for all the bugs along with open redirect. The Interesting thing is that,my first try is a success.yes it’s open redirect.

My first try is https://subdomain.site.com/////bing.com

https://subdomain.site.com//bing.com---fail:(

https://subdomain.site.com///bing.com---success:)[i report it]

i find open redirect bug in many subdomain on this site.But reported only 3 subdomain.

Press enter or click to view image in full size

Apparently there are many hackers who do not manually hunt these bugs depending on the nuclei tool.

Get khan mamun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Note: My sole purpose in writing this write up was to try the bugs manually without relying only on the nuclei tool.

Tips or say whatever, I can recommend you please don’t just rely on any tool.

— — — — — — — — — — — — —

I’m human, I could be wrong, please forgive me goes any wrong and please pray for me.

Thanks everyone☺

my Twitter : https://twitter.com/mamunwhh

If you have time check my Yt:

https://m.youtube.com/channel/UCwFn0AfyutumdIDWCUyR21Q

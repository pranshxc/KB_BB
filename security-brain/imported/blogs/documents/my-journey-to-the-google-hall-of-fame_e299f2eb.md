---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-25_my-journey-to-the-google-hall-of-fame.md
original_filename: 2018-11-25_my-journey-to-the-google-hall-of-fame.md
title: My Journey To The Google Hall Of Fame
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: e299f2ebf5eba9421ff6c69d5ad46b4b650d50f59e77c7052ac5a15b99bd25da
text_sha256: dedb350ef528525128ffabf44a45ab9ccebe1dcebe7099b99f85f00ccd34a1c1
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# My Journey To The Google Hall Of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-25_my-journey-to-the-google-hall-of-fame.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e299f2ebf5eba9421ff6c69d5ad46b4b650d50f59e77c7052ac5a15b99bd25da`
- Text SHA256: `dedb350ef528525128ffabf44a45ab9ccebe1dcebe7099b99f85f00ccd34a1c1`


## Content

---
title: "My Journey To The Google Hall Of Fame"
url: "https://www.secjuice.com/google-hall-of-fame/"
final_url: "https://www.secjuice.com/google-hall-of-fame/"
authors: ["Abartan Dhakal (@imhaxormad)"]
programs: ["Google"]
bugs: ["Open redirect", "XSS"]
publication_date: "2018-11-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5566
---

[TECHNICAL](/tag/technical/)

# My Journey To The Google Hall Of Fame

This is the story of the how Abartan Dhakal managed to get into the Google Hall of Fame, along a path strewn with failure and invalid vulnerabilities.

  * [ ![Abartan Dhakal](/content/images/size/w100/2018/12/profile.jpg) ](/author/abartan/)

#### [Abartan Dhakal](/author/abartan/)

Nov 25, 2018

[Tip Writer](https://ko-fi.com/abartandhakal)

![My Journey To The Google Hall Of Fame](/content/images/size/w2000/2018/11/slack_hammer_gif-1.gif)

In this article I tell the story of the success I have had finding Google vulnerabilities, a success that is underpinned by LOTS of failure. This is the story of of how I turned my invalids into valid vulnerabilities and got into the Google Hall of Fame and hopefully will help you out during penetration test or during bugbounty hunting. 

I have been trying to earn a seat in Google's Hall of Fame by finding at least one valid security vulnerability for a long time. I tried whenever I had free time at night (I have studies and work to do so don't ever get enough time for hacking). 

After seven months of trying and getting my reports tagged as "intended behaviour of the application" or "won't fix", one incredible evening I was able to get my name into Google's "honorable mentions" and their "reward hall of fame". 

This story is all about how Google themselves helped me find the vulnerability. 

_**Note:** This is not a super hack, merely a small Cross Site Scripting (XSS) vulnerability which was gained by exploiting open redirection._

### Story Begins

I have been trying to find a valid vulnerability in the "Google" and "Youtube" domains with the hope of discovering some low hanging fruit. I had reported a few authentication related vulnerabilities with the hope of one being valid, but all those reports were invalid because the issues were 'intended' and did not poses any risk. 

Then two months ago I thought to look into the acquisitions and I came across a new vulnerability, but sadly the report from Google also came back as invalid. 

It was all a bit disheartening, after searching for so long I had found nothing but invalid vulnerabilities, so I had to stop, take a break and start learning a bit more. 

So one fine day I was checking all the available proof of concepts that were there for Google's reports. At the same time, I found a site[ Sidewalk Labs ](https://sidewalklabs.com/?ref=secjuice.com). I first checkout out the application flow and at the same time was enumerating the subdomains. 

Then as I was doing my recon, I thought of giving a Google dork shot to find some files and gain more attack surface, whenI came across this dork "site:*.sidewalklabs.com" and mistakenly pressed enter. I found a site "https://replicaexplorer.sidewalklabs.com" where there was a redirection parameter and checked that once you log in, you will be redirected to any website. 

This was a sad moment because as per [Google's VRP](https://www.google.com/about/appsecurity/reward-program/?ref=secjuice.com) Open redirection is out of scope and therefore would not be rewarded. I then started checking for the available POC where Open Redirection could bring a big issue and I had completely forgotten about XSS till this phase. 

Then I came across a post from google where a hacker had chained 3 Open redirections to get an XSS and hence Google had rewarded him a bounty. Then I started to find similar websites which might have open redirection. 

But then suddenly, I came across a POC where Open Redirection was easily chained with "javascript:alert(document.domain);" to get XSS and without any time wasting, I tried this payload (had very less faith that it's gonna work because its "GOOGLE") and got amazed that it actually executed and gave me a sweet little Popup. I quickly made a report and within 13hrs they responded with a "Nice Catch!" response and within another 12days, I got rewarded. 

![](https://secjuice.com/content/images/2018/11/Screenshot-from-2018-11-01-16-36-42.png)My Sweet Little PopUp 

Quick Tips: If you want to hunt down big corps, try with their acquisions and never think if it's a very big corp then it won't have small vulnerabilities. Also even if you are hunting down Google, use help of google ;) (Google Dorking).

That was all. You can now find me on both hall of fames of Google [here](https://www.google.com/about/appsecurity/hall-of-fame/archive/?ref=secjuice.com). 

![](https://secjuice.com/content/images/2018/11/slack_hammer_gif.gif)The awesome images used to head this article is called Colorful Bang and was created by [Henrique Barone](https://dribbble.com/henrique_barone?ref=secjuice.com).

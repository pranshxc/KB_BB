---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-04_bypassing-amazon-kids-parental-controls.md
original_filename: 2023-04-04_bypassing-amazon-kids-parental-controls.md
title: Bypassing Amazon Kids+ Parental Controls
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: 44c04cab1784ab5dd69e0632a66a730e1fbb3a7804a60e30bc60204dae364956
text_sha256: cf822bc7cde895f3cf147928150edecccda30fad12d319ec59aceb6b15a64750
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Amazon Kids+ Parental Controls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-04_bypassing-amazon-kids-parental-controls.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `44c04cab1784ab5dd69e0632a66a730e1fbb3a7804a60e30bc60204dae364956`
- Text SHA256: `cf822bc7cde895f3cf147928150edecccda30fad12d319ec59aceb6b15a64750`


## Content

---
title: "Bypassing Amazon Kids+ Parental Controls"
page_title: "Bypassing Amazon Kids+ Parental Controls – n00py Blog"
url: "https://www.n00py.io/2023/01/bypassing-amazon-kids-parental-controls/"
final_url: "https://www.n00py.io/2023/04/bypassing-amazon-kids-parental-controls/"
authors: ["n00py (@n00py1)"]
programs: ["Amazon"]
bugs: ["Logic flaw"]
publication_date: "2023-04-04"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1302
---

Recently for Christmas my 4 year old daughter got an Amazon Kids tablet. So far the tablet has been great and Kids+ seems like a pretty decent value for what you get. I’m very wary of the types of content available on the internet, and as a parent it’s my duty to ensure that my child stays safe online. I was happy to see that this new tablet came with robust controls that I could use to filter the type of content that my child has access to.

Being a hacker however, I couldn’t help but ponder _“Could these controls be bypassed?”_ I had locked down the tablet as best I could, but after about 5 minutes of effort, I was able to access adult content on the device, and bypass all the tools in place to monitor this type of activity.

The story starts with **My Baby Unicorn – Amazon Kids+ Edition**. I chose this app as it was my daughter’s favorite, so I figured it was a logical place to start.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105617.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105617.png)

All apps on the App store are rated by Amazon for age appropriate content. You can select your child’s age within their profile. As long as the application is approved for Kids+, the child can download it without needing to request permission. Other applications do require the parent to approve them.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105951.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105951.png)

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110014.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110014.png)

You can also control settings for web browsing. You can set controls around the web browser, limit content, and review your child’s web activity.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110031.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110031.png)

When it comes to the web browser, your two main options are hand-selected websites and videos, and filtered websites and videos. Hand-selected is a much stronger control, as filtered is unlikely to stop a determined child, and Amazon only makes the claim to _**help**_ filter out inappropriate content. I did not want my child accessing the web browser at all, so I chose to disable the web access completely.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110106-1.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110106-1.png)Now, back to **My Baby Unicorn**. Upon launching the application, the first thing I noticed was the link to the privacy policy, so I clicked it.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105331.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105331.png)

This did indeed display the privacy policy, but it became quickly apparent to me that I was viewing this content through a web browser embedded within the application.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105340.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105340.png)

After scrolling down for a bit I looked through the other areas of the policy looking for any hyperlinks.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105349.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105349.png)

While the policy contained many hyperlinks, the most notable was the link to the Google privacy policy.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105358.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105331.png)

After getting to the privacy policy, I clicked The menu icon to access additional parts of Google, namely Google search.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105405.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105405.png)

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105415.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105415.png)

After getting to Google, I could then query anything on the internet that is indexed by Google.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105457.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105457.png)

I verified that searching for adult content was possible, and clicking the links to the content was possible and the web pages displayed the content.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105509.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105509.png)

I then went back to my Parent Dashboard to see if any of this web activity was logged. It was not. All content controls are specific to the the Amazon web browser application, and do not apply to any other app that is on the device.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110042.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-110042.png)

I had considered disabling the internet entirely, and instead having my child use the tablet exclusively in offline only mode. Most apps seem to work fine offline, however some apps do not and of course you can not stream any videos.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105749.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105749.png)

Ultimately however you have little control over this, as a child profile can access the control center. They cannot access the network manager, but they can re-enable the WiFi, and if the tablet had ever connected to any network in range, it should automatically connect and restore internet access.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105758.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230103-105758.png)

I showed this to my wife, and she was surprised to see how simple it was, but felt it was an issue with **My Baby Unicorn**. I disagreed, and was sure that within 5 minutes I could do it again in a completely separate application by a separate development studio, and after a little trial and error I was again successful in less than 5 minutes.

This time, I chose **Dr. Panda Candy Factory.**

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151311.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151311.png)

Upon launching the game, I clicked on the control center icon in the upper right.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151320.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151320.png)

From here, I clicked T _erms & Services_.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151327.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151327.png)

In _Terms and Services_ , both buttons opened an embedded web browser.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151333.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151333.png)

Scrolling down the terms off service led me to a few social media links in the footer of the web page.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-112138.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-112138.png)

From there I could gain access to YouTube, and of course Google’s privacy policy and subsequently Google Search just as before.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151418.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-151418.png)

I did not continue to test each and every application I had installed for my child, but I found that it was common enough that it was a pervasive issue on child friendly pre-approved applications.

Ultimately I believe the issue is Amazon’s trust model. Once an application is cleared for Kids+, it is no longer subject to scrutiny. Instead, I would like to see any outbound communication from the applications able to be filtered and audited, just like what is possible for the web browser. I know that apps often need access to web content to function, and these endpoints can and will change with frequency, so it’s not super easy to tell exactly what they need.

With that said, I did try to replicate these attacks against an Apple iOS device, and was not successful. On iPhone, **My Baby Unicorn** also contains an embedded browser, but the hyperlinks do not work, and thus I could not navigate away to any third party sites. I believe this may have been an intentional control put in place to prevent these types of exploits. For**Dr. Panda Candy Factory** on iOS, it opened the policy webpage using Safari instead of an embedded browser, which may have been because of separate codebases resulting in minor differences in functionality.

When testing iOS, I also observed that when I did find a working embedded browser, it was subject to the web-based content controls, unlike what I observed on the Amazon device.

Ideally, I think the fix needed is for content controls to monitor/restrict the outbound traffic of the apps themselves, or perhaps modify the review process for these kind of escapes and establish a policy prohibiting embedded browsers in apps approved for Kids+. I did encounter some apps that acted properly, and would pass hyperlinks over to the default web browser, which were then subsequently blocked per my configuration.

[![](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-120659.png)](https://www.n00py.io/wp-content/uploads/2023/01/Screenshot_20230104-120659.png)

### Disclosure timeline:

January 4th, 2023 – Contacted Amazon about the issue. Indicated that I will not be using the HackerOne platform and would like to disclose the security issue through an alternative channel.

January 4th, 2023 – Amazon responds, requests details and requests withholding disclosure until a fix is put in place.

January 4th, 2023 – Details provided via email.

March 8th, 2023 – Amazon requests additional time to implement a fix.

March 8th, 2023 – I notice **My Baby Unicorn** has been removed from my device and unpublished from the app store.

March 8th, 2023 – Amazon proposes a publish date of March 31st.

March 19th, 2023 – I request details on the fix.

March 29th, 2023 – Amazon provides remediation details. Remediation is removal of the applications identified in this blog post from the app store as well as guidance on how to use existing content controls.

I noticed that in addition to **My Baby Unicorn** and **Dr. Panda Candy Factory** being removed, it appears that their respective publishers ([TutuTOONS](https://tutotoons.com/), [Dr. Panda](https://drpanda.com/)) have also updated or removed all of their other games to remove this bypass.

While I don’t think it is likely that this entire class of vulnerability has been removed from the platform, I do not have knowledge of any undisclosed bypasses. I have not audited but a small fraction of the Amazon Kids+ app store, so it may be possible other bypasses exist in other applications. I ultimately consider the response a “won’t fix”, though I do appreciate that they made an effort to remove known vulnerable apps.

For now, my best advice for parents is to follow a model that works and has always worked: supervise their activities as they happen. While I would still advocate for enabling all available content controls and disabling network access if you can, there is no substitute for being present when your child is using their device.

# Bonus Content: Apple iOS Comparison

Lets look at Apple privacy controls and see how. they compare. First, lets set up some content controls.

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9429-1.png)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9429-1.png)For now, I’m leaving the web content to “** _Unrestricted_** ” however we will address that later. Otherwise, this is set up to only allow for child friendly content. Let’s try to Download TikTok.

**Blocked.** Nice, just what I like to see.

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9430.jpg)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9430.jpg)Ok, what about something a little more child friendly, like KidzBOP? (pop songs edited for content and sang by kids)

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9680.jpg)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9680.jpg)This is rated age 4+, so not a problem at all. The child is free to download it. As I’m sure you have already guessed, this app has an extremely trivial bypass due to an embedded browser. I won’t document the steps, but I’m not joking when I say a child could figure it out, I found it in sub-60 seconds.

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9681.jpg)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9681.jpg)So now back to the web content settings. As I showed earlier, they were not locked down. It’s entirely possible some parents might simply disable Safari (iOS’s built-in browser) and not consider this control relevant. Ok, so what if we change it?

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9677.png)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9677.png)I can tell you right now, “ _**Limit Adult Websites**_ ” isn’t nearly as useful as it sounds. In fact, the screenshot above was taken with this option turned on. There is an unlimited supply of adult content on the internet, and even seemingly vanilla websites like Twitter and Reddit allow for hardcore porn. They do have controls to limit this, but as you might guess, they too pretty much do next to nothing. One good thing however, is that when you select this option the browser cannot go into “private mode” and the browsing history cannot be deleted.

Ok, so now we get to the final option, **“Allowed Websites”:**

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9676.png)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9676.png)Fantastic, it ACTUALLY works! Unlike Amazon Kids+, browsers embedded within apps are still subject to the iOS content controls.

[![](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9679.jpg)](https://www.n00py.io/wp-content/uploads/2023/04/IMG_9679.jpg)

This makes iOS significantly safer, assuming you understand the risks and opt to go for the most strict control.

[Tweet](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.n00py.io%2F2023%2F04%2Fbypassing-amazon-kids-parental-controls%2F&via=n00py1)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-02_hacking-always-check-out-the-images.md
original_filename: 2020-12-02_hacking-always-check-out-the-images.md
title: Hacking — Always check out the Images
category: documents
detected_topics:
- command-injection
- information-disclosure
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- information-disclosure
- mobile-security
- supply-chain
language: en
raw_sha256: a1588596a7d8bc8cd853638fc7482f3c7d9a6bec787c4fe1df334eff97802f89
text_sha256: 1c212a2b9194370b48c791c8da1f38b91ada09390f349cd62a238e3a9d6b86fb
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking — Always check out the Images

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-02_hacking-always-check-out-the-images.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `a1588596a7d8bc8cd853638fc7482f3c7d9a6bec787c4fe1df334eff97802f89`
- Text SHA256: `1c212a2b9194370b48c791c8da1f38b91ada09390f349cd62a238e3a9d6b86fb`


## Content

---
title: "Hacking — Always check out the Images"
url: "https://medium.com/the-volatile-triad/hacking-always-check-out-the-images-99217e6cea"
authors: ["Jack"]
programs: ["GitLab"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2020-12-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4096
scraped_via: "browseros"
---

# Hacking — Always check out the Images

Hacking — Always check out the Images
Jack
Follow
3 min read
·
Dec 2, 2020

41

1

Concise tip: Always check for Exif metadata, particularly latitudinal/longitudinal metadata, on profile pictures/anywhere that images can be publicly shared on websites.

My report: https://hackerone.com/reports/446238

Full story: Exif metadata is a tool that can be utilized primarily on JPEG images to store information about the photo such as camera model, date and time of the photo being taken, copyright information, and even the latitude/longitude of the location where the photo was taken. Many modern smartphones actually attach this latitudinal and longitudinal data by default to images taken through their native camera apps unless otherwise specified by the user in settings.

This creates quite the privacy risk if a website does not properly handle the metadata; that is, if a website has a way to publicly share images via profile pictures, forum posts, etc. and they do not strip that Exif metadata from images shared on that platform. When you couple that lack of stripping metadata with the fact that most smartphone users do not realize that they are sharing the location data for that photo, it can lead to different scenarios disclosing the uploader’s exact home location or other data that they may not want to share such as phone model, etc.

Get Jack’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When you’re testing on websites that have public profile pages with images on them or, better yet, forums, you should prepare a JPEG image with Exif longitudinal/latitudinal data attached to it and upload it to those different spots. If you can redownload it from that website and it still contains that Exif metadata, you’ve likely found a vulnerability. There are a couple exceptions, however:

The site strips latitude/longitude but not other data. This is somewhat common as the copyright data may need to be preserved for legal reasons and no other data beyond latitude/longitude really gives away any possibly sensitive information.
The original image with metadata is only accessible to the uploader. When redownloading, always attempt to do so when unauthenticated/authenticated on a different account to see if it is reproducible without being authenticated on the uploader’s account.

If neither of the above scenarios apply, congratulations! You’ve likely found yourself a vulnerability. One scenario that can also increase the severity is if the location where images are uploaded is obviously a place for images of the home. For example, maybe they have a forum topic that is home decor images. This would increase the chances of the latitudinal/longitudinal data being the home locations of the photo uploaders therefore increasing the amount of sensitive information disclosed.

Finally, a few tips. Be sure to check images attached to reviews, although some of these may not qualify due to the image host/review integration being third-party. Also if you don’t initially see the metadata, ensure that you’re viewing the original image. For example, if you right click and open the profile picture in a new tab, oftentimes there will be URL parameters or other modifiers changing the size/quality, etc. Try removing all of these modifiers and downloading that image.

Although the patch took a while, Gitlab eventually rolled it out and they were a great team to work with. Thank you to the whole Gitlab team and Hackerone triagers for a smooth reporting process. As Gitlab has specified in the summary, they are aware of tricks to bypass EXIF metadata stripping and are working to remediate these, but they do not consider this impactful enough for a valid report. This is likely due to the nature of this information disclosure coming from the uploader’s end therefore it would make no sense for an uploader to bypass and leak their own information.

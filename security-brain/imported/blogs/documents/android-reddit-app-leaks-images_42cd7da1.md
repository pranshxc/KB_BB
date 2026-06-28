---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-29_android-reddit-app-leaks-images.md
original_filename: 2019-10-29_android-reddit-app-leaks-images.md
title: Android Reddit App leaks images
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- cloud-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- cloud-security
- mobile-security
- supply-chain
language: en
raw_sha256: 42cd7da177536d7d1f4bb103b3ecc1f9ddf58cbe3fb0f864cc0b1886059a0096
text_sha256: bfcdca82ed708dbe63981b99763ef08b589746a4c8aea91b7ff5b8a63d774cae
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Android Reddit App leaks images

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-29_android-reddit-app-leaks-images.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, cloud-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `42cd7da177536d7d1f4bb103b3ecc1f9ddf58cbe3fb0f864cc0b1886059a0096`
- Text SHA256: `bfcdca82ed708dbe63981b99763ef08b589746a4c8aea91b7ff5b8a63d774cae`


## Content

---
title: "Android Reddit App leaks images"
url: "http://www.hydrogen18.com/blog/reddit-android-app-leaks-images.html"
final_url: "https://www.hydrogen18.com/blog/reddit-android-app-leaks-images.html"
authors: ["Eric Urban"]
programs: ["Reddit"]
bugs: ["Information disclosure"]
publication_date: "2019-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4970
---

# [Android Reddit App leaks images](https://www.hydrogen18.com/blog/reddit-android-app-leaks-images.html "Android Reddit App leaks images")

  * Tuesday October 29 2019
  * [android](tags.html#android) [jpg](tags.html#jpg)

I recently was browsing Reddit when I came upon [a really pecuilar image](https://old.reddit.com/r/Justrolledintotheshop/comments/dmh9cd/6_head_gaskets_1_cup_of_coffee/) that was uploaded by another user from his smart phone.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_lossless_mid.png)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_lossless.png)

This image is a JPEG, which often contains many artifacts from the lossy compression used. However, the quality of this image is particularly atrocious. It's almost like a base image with just a bunch of noise layered on top of it. This lead me to eventually notice that I wasn't looking at artifacts from compression. JPEG compression artifacts usually look like this

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/texas_state_capitol_lq_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/texas_state_capitol_lq.jpg)

Highly compressed JPEG. Original image courtesy of LoneStarMike via Wikipedia

This example here shows a clear loss of color quality and the practical resolution of the image is very low, no matter how many pixels make up the image. However, all of the components somehow correspond to a single image even if the overall quality is poor. For example, the pedestrian path in front of the building is certainly not green but the coloration is uniform across the visible portion in the photograph.

## Initial investigation

Looking at the image more, something really jumped out at me. Other Reddit users noticed this as well.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_highlighted_mid.png)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_highlighted.png)

This is obviously not just random noise or loss of quality due to JPEG compression. You can clearly make out the logo of [CRC Industries](https://www.crcindustries.com/). You can also see a product name "Brakleen". It looks like JPEG artifacts, but it is actually an image. So far I am calling this the "ghost". Here is the same region cropped.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_cropped_mid.png)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_cropped.png)

So I reached out to the user and got this story

  1. He took a few photos of his work area
  2. He used the Reddit app. on his Pixel 3 to upload one of the images
  3. The image with the "ghost" is what got shared on Reddit

He was also kind enough to supply to me the original images taken by his phone at that time

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102255_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102255.jpg)

The original image which was intended to be shared

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102242_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102242.jpg)

The other image taken by the user not intended to be shared

Both of these images are JPEGs and neither have any obvious issues. If you look at the other image, the "ghost" is clearly formed from the image of the can of Brakleen sitting on the bench. There is way this is the expected behavior of the image copmression used by the Reddit app. Why is information from the other image somehow encoded into the first one?

I didn't know much about the Reddit Android application, so I downloaded and installed it on my personal smart phone. It is pretty simple. You can upload a single image at a time when making a post to subreddit. There are no options to adjust image size, quality, etc. All of the images get uploaded to the "i.redd.it" domain. You can actually browse Reddit by domain, so I checked [the page for that domain](https://old.reddit.com/domain/i.redd.it/) (warning: maybe NSFW). I found plenty of images that were obviously taken with someone's smartphone. But did not find any other images with the same issue. My guess is the Reddit application sometimes recompresses very high quality images to a lower quality on the phone. Then it uploads them. Reddit probably doesn't want to host ultra high quality images and this makes the upload from the phone take less time.

At this point I decided to do some more investigation and found the application [JPEGSnoop](https://github.com/ImpulseAdventure/JPEGsnoop). It runs under Wine just fine if you use Ubuntu like me. I was able to use it to see what sections made up the JPEG image. This turns out to be a progressive JPEG. Progressive JPEGs are an optimized form of content delivery that permits the image to be displayed before the entire image is downloaded by the client. Without going too much into how this works, the image is basically delivered in a bunch of layers. Each layer provides more definition to the image to produce a clearer view.

Once I knew this image was progressive, I wanted to view the image as each layer became available. So I wrote a simple Python script that could take the original image and create a copy that was lacking the later layers. There apparently is no answer as to the optimal number of layers, this particular image consists of 10. With each image split out I was able to basically thumb through the layers. After looking at it for a while, I realized that up to layer 3 everything looks normal.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_prog3_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_prog3.jpg)

Displaying progressive layers 1-4 the image is clear

This image isn't great quality, but it does look fine. As soon as you view the image with layer 4 present, the "ghost" is visible

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_prog4_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_prog4.jpg)

Displaying progressive layers 1-5 the "ghost" is visible again

So at this point I was thoroughly confused. It seems that the image compression was going fine and suddenly just started compressing parts of the other image into this file. This is an extremely far fetched explanation that I wanted to find some evidence to back up.

I located an APK of the Reddit app. and managed to decompile it to Java bytecode using a bunch of utilites. The Reddit application does contain the library [Fresco](https://github.com/facebook/fresco) and [JCodec](https://github.com/jcodec). The Fresco library is actually optimized towards displaying progressive JPEGs on Android handsets. It does contain a complete copy of [libjpeg-turbo](https://libjpeg-turbo.org/). This library is capable of producing progressive JPEGs. There are some Java wrappers around JPEG transcoding, but it doesn't appear those functions would produce progressive JPEGs. The actual Java bytecode of the Reddit Application is obfuscated, making it very difficult to identify what code would be responsible for compression before the upload. Ultimately, I gave up on this path of investigation.

## Conclusion

But going back to the layers, I decided to see what happen if I constructed an image using only those after layer 4. The resulting file is not really a sensible JPEG, but every tool I tried is able to display it. This strange looking image is what I was able to produce. I then filtered it using GIMP to make the features easier to see

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_fractional_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_fractional.jpg)

Displaying layers 5-10 just shows the ghosts

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_fractional_inverted_mid.png)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_fractional_inverted.png)

The ghosts highlighted using GIMP

Comparing what I could see, I realized _all_ of the visible features in the later layers are actually just information from the other image. Here, I've indicated the features visible in the later layers that are from the second image.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102242_highlighted_mid.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/IMG_20191024_102242_highlighted.jpg)

The source of the ghosts in the shared image

So what I finally realized, is **I am looking at two JPEG files just spliced together at some arbitrary point**. As it would turn out, the JPEG image format is fairly robust. Most parsers simply ignore anything they don't understand and display the parts they do. Somehow it appears the Reddit application was actually compressing both images. This process presumably happens in a background thread. I cannot explain how it happened, but the application appears to have the upploaded first half of compressing the original image and the second half of compressing the other image. This produces what appears as the "ghost" in the resulting output. This is probably not the fault of the image compression library and more likely somehow **buffers are reused in the application improperly**. This explanation is also extremely simple compared to anything else I could come up with.

To prove this out, I took two of my own images and converted them into progressive JPEGs. Afterwards I took the first half of one file and combined it with the second half of another. This joining process was done without any image editing software, instead I simply took half the bytes from the first image and half the bytes from the last image.

[![](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/cut_together_prog_thumb.jpg)](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/cut_together_prog.jpg)

Click to see the ghosts

It is difficult to observe, but if you click on the image to view it in fullscreen you can see faint "ghosts" that are red and green and wind their way across the image. This is the same effect that I see in the image that was uploaded to Reddit. If this had happened with a normal JPEG, it would just produce a garbage image. Due to the way progressive JPEGs are constructed, the image is still recognizable.

If you consider it, this has some huge security implications. In this case, the application uploaded parts of another image that the user never wanted shared. Thankfully, it wasn't anything sensitive. I personally use my smartphone to photograph all sorts of personal information and notes that are never meant to be shared with anyone. I suspect I am not alone in this habit. This bug in the Reddit application could lead to unintentional sharing of private information in the form of these "ghosts" on the image.

If someone else would like to investigate this issue and try and come up with a more complete explanation, you can download the original JPEGs plus the ones I created during my investigation in a zip file below.

[ reddit_app_bug_original_material.zip 2.3 MB](https://h18blog.s3.us-east-1.amazonaws.com/blog/reddit-app-image-leaking/reddit_app_bug_original_material.zip)

This original images plus the ones I created while investigating this

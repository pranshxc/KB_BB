---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-11_all-your-parcel-are-belong-to-us-talk-at-troopers-2023.md
original_filename: 2023-07-11_all-your-parcel-are-belong-to-us-talk-at-troopers-2023.md
title: All your parcel are belong to us – Talk at Troopers 2023
category: documents
detected_topics:
- rate-limit
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- rate-limit
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: c01cc7c3f261cab65464fe8bcf3d37db05df745ab2b5ff13f66ed4db46121b21
text_sha256: 9c8c01a6c0d578fe719a4f14ad3605044a5d3502f5482411dbbacf59c09cb8fa
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# All your parcel are belong to us – Talk at Troopers 2023

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-11_all-your-parcel-are-belong-to-us-talk-at-troopers-2023.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, automation-abuse, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `c01cc7c3f261cab65464fe8bcf3d37db05df745ab2b5ff13f66ed4db46121b21`
- Text SHA256: `9c8c01a6c0d578fe719a4f14ad3605044a5d3502f5482411dbbacf59c09cb8fa`


## Content

---
title: "All your parcel are belong to us – Talk at Troopers 2023"
page_title: "All your parcel are belong to us – Talk at Troopers 2023 – Insinuator.net"
url: "https://insinuator.net/2023/07/all-your-parcel-are-belong-to-us-talk-at-troopers-2023/"
final_url: "https://insinuator.net/2023/07/all-your-parcel-are-belong-to-us-talk-at-troopers-2023/"
authors: ["Dennis Kniel", "Florian Bausch"]
programs: ["DHL"]
bugs: ["Privacy issue", "Cryptographic issues"]
publication_date: "2023-07-11"
added_date: "2023-07-17"
source: "pentester.land/writeups.json"
original_index: 942
---

[ Back ](https://insinuator.net/#post-14312)

[Breaking](https://insinuator.net/category/breaking/)

[July 11, 2023](https://insinuator.net/2023/07/all-your-parcel-are-belong-to-us-talk-at-troopers-2023/) by [Florian Bausch](https://insinuator.net/author/fbausch/)

# All your parcel are belong to us – Talk at Troopers 2023

[Florian Bausch](https://insinuator.net/author/fbausch/ "Florian Bausch")

At Troopers 2023, we gave a talk on how to attack DHL parcel tracking information based on OSINT. Since we previously had an exemplary disclosure process about this attack with DHL, Mr. Kiehne (from DHL) joined us to provide interesting background information and insights on how they addressed our findings.

We want to thank DHL and especially Mr. Kiehne for sharing those insights with us at Troopers 2023. It is the ideal case, but still not common that organizations talk openly about their actions and views on a disclosure process.

You can find the video recording on [Youtube](https://www.youtube.com/watch?v=bZd8Ls4VqQs) and the slide decks on [troopers.de](https://troopers.de/troopers23/talks/mtgrsz/).

In the following you find a description of what we found out and how the disclosure went:

Some time ago we ordered multiple bottles of wine from a winery. Since they were supposed to be tasted by us and our colleagues during an online team event, we decided to ship everyone’s bottles directly to them. The winery was nice enough to give us a tracking number for every parcel. When we looked over the numbers, something interesting came to our eyes. The tracking numbers were all really similar. Maybe it is possible to identify a pattern and to have fun with tracking numbers?

They all were 12 digits long and the first 9 digits were identical. Here are the numbers with the identical digits censored:

  * XXXXXXXXX344
  * XXXXXXXXX350
  * XXXXXXXXX366
  * XXXXXXXXX372
  * XXXXXXXXX388
  * XXXXXXXXX394
  * XXXXXXXXX401
  * XXXXXXXXX417
  * XXXXXXXXX423

The 10th and 11th seemed like they were counting upwards and the 12th seemed random at first. We tried iterating the numbers in between but only the ones we had seemed to be valid. After a short research, we found out that [the last digit is a checksum](https://www.paketda.de/firmenkunden/paket-pruefziffern.html). For 12-digit tracking numbers the checksum is calculated by multiplying numbers on odd positions with 4 and on even positions with 9. Then all the results are added up. Afterwards, the sum is subtracted from its next multiple of 10. If it is a multiple of 10 already, the checksum is 0, otherwise it is the result of said subtraction. As an example let’s try it for the tracking number `140318792527`. First, multiply the first 11 digits with 4 and 9 alternately:
  
  
  1  4  0  3  1  8  7  9  2  5  2
  x 4  9  4  9  4  9  4  9  4  9  4
  _____________________________________
  4  36 0  27 4  72 28 81 8  45 8

Now the sum has to be built:
  
  
  4 + 36 + 0 + 27 + 4 + 72 + 28 + 81 + 8 + 45 + 8 = 313

And last, subtract it from the next multiple of 10:
  
  
  320 - 313 = 7

So the numbers we got from the winery were really just counting up. We were unsure if this was the case because they were just bought in a batch or if they are somehow connected to the business that bought them. So we asked the winery owner if he could provide us with some more tracking numbers – and he did. Thank you, [Weingut Kohl](https://weingut-kohl-bockenheim.de). It turned out that the next batch of numbers also just counted up and they started where the last batch ended. Since tracking numbers seem to become invalid after some time, we iterated the ones we had until we hit valid numbers again. Then we checked the parcel center of origin (more on that later) and they (almost) all matched the one we would expect from the business, whose numbers we were testing with. Also, we were able to gather lots of valid tracking numbers by just iterating from a number we got when we bought a parcel label without a DHL account.

Buying two labels around 30 minutes apart resulted in tracking numbers approximately 750 numbers apart (ignoring the checksum of course). Also, the parcel centers of origin were spread all across the country, as you might expect, if the labels created without an account share a common prefix and just count up. Seems like we can now iterate over all the tracking numbers created by this business and by random people. But what can we do with those tracking numbers? Well, the answer is obvious. We can **track parcels**!

## Making Use of Tracking Numbers

When entering a tracking number on the DHL website you get some information about it’s tracking history. The following screenshot shows, what we saw:

![](https://insinuator.net/wp-content/uploads/2022/08/Screenshot-from-2022-08-25-11-18-44.png)

So we have some timestamps and the origin and destination parcel center (which are the same in this case). To get more information, you need to enter the recipient’s postal code, which we do not know (yet). We could now just brute-force every 5 digit combination, leaving you with 10⁵ combinations. According to DHL, there were [28.278 postal codes in use in 2018](https://www.dpdhl.com/de/presse/pressemitteilungen/2018/25-jahre-fuenfstellige-postleitzahlen-in-deutschland.html), which is still a lot. Maybe we can make this a bit more efficient. Here we can use the information we already got with just the tracking number, since it contains the destination parcel center (Speyer in our case).

There are already [lists](https://www.paketda.de/paketdepot-dhl.html) with [all existing parcel centers](https://de.wikipedia.org/wiki/Paketzentrum_\(Deutsche_Post_DHL\)) available. paketda.de also lets you find the responsible one for each postal code. Now all we have to do is to catch a list of all postal codes and find the responsible parcel center for each one. Also, not all 28.000 postal codes are for delivery districts. [Some](https://de.wikipedia.org/wiki/Postleitzahl_\(Deutschland\)#Postleitzahlenarten) are for PO boxes, some for larger business customers and some for delivery districts. According to the list of all delivery district postal codes, there are [8170](https://downloads.suche-postleitzahl.org/v2/public/plz_einwohner.csv). Since there are 37 parcel centers listed on Wikipedia, we can already strip the 8170 postal codes down to 221 for an average parcel center, which could already be guessed by hand if someone has enough time and dedication. We could already just automate the guessing here but we can improve this approach a bit more.

We found available information for the population of each postal code’s area [from 2011](https://www.suche-postleitzahl.org/downloads). If we start with the high population ones and work our way down to the low population ones (assuming more people order more parcels), we can speed things up even more. As an example, take the parcel center Speyer. It serves 128 postal codes (a lot less than the average of 227 and also a nice number in general), which have a combined population of 1.632.699. Half of those are already covered in the 30 most populated postal codes. A simulation showed that on average 50 tries are needed to get the correct postal code of 50% of the parcels across all parcel centers. We do not consider parcels to areas where a lot of parcels go but few people live, like industrial areas but you get the picture. By going from high to low population postal codes we can guess the one for our package with 37 tries.

## The Impact

Let us take a look at what information we get, when we have the correct postal code of the recipient.

![](https://insinuator.net/wp-content/uploads/2022/08/Screenshot-from-2022-08-25-10-06-20-443x1024.png)

It depends a bit on the stage of the delivery but the most information is available during live tracking, which we see in the screenshot. We now also have the name of the sender and the Recipient. The map gives us a somewhat precise location of the driver and the delivery address. As you might be able to guess, the coordinates for this position can be taken out of the response here.

![](https://insinuator.net/wp-content/uploads/2022/08/Screenshot-from-2022-08-25-11-33-56.png)

When looking the coordinates up, you quickly find the address oft the recipient.

![](https://insinuator.net/wp-content/uploads/2022/08/Screenshot-from-2022-08-25-11-35-45-e1661420497918.png)

Saw the “Not at home?” menu point in the tracking? Guessing the postal code also gave us the power to use it. We can now do things like selecting a drop-off location, changing the delivery day or refusing the acceptance.

![](https://insinuator.net/wp-content/uploads/2022/08/358940230582_delivery_options-e1661420371460-300x152.png)

The amount of options presented depends on the progress of the parcel.

## What Could Possibly Go Wrong?

After finding this issue, we thought about things that can go wrong and ways this could be abused. Following is a list of things that came to our minds.

### Reoccurring Parcels

If someone receives parcels in a regular manner from a certain sender, this might allow for some conclusions. Imagine someone ordering from a pharmacy every two weeks. Or from a nursing supply shop every month. Or from a winery ever week. It might be possible to get hints on hobbies, medications, household members in need of care, alcohol consumption etc..

### Senders of Interest

In some cases it might be interesting to see, who receives parcels from special businesses. Think of shops for things that might be used to discredit someone like a shop for hidden cameras.

### Theft

Since you are able to know when exactly parcels arrive you can enumerate parcels from expensive vendors and if one is scheduled for delivery close to you, you can try to intercept the driver before they ring the doorbell. Or even easier, use the DHL website to select a drop-off location. Interestingly enough, even the sender can select drop-off locations, since they know the receiver’s postal code.

### Trolling

You can change delivery options or refuse acceptances of other people’s parcels. In case the parcel contains some perishable items or are needed urgently, this might cause additional issues.

### Estimating Sales

By enumerating a companies tracking numbers you can try to estimate their sales numbers.

### Stalking Delivery Drivers

Depending on the accuracy of the live tracking, it might be possible to track delivery drivers during their workdays.

### Mining Customer Lists

Enumerating parcels of a business allows you to build a customer list.

### Metadata Mining

Why not mine everything you can get and think about what you can do with it afterwards?

## The Underlying Issue

The process does not rely on proper secrets, as the tracking numbers can be iterated and the postal codes can be guessed. To guess this postal code hints are given. It is recommended to implement a proper secret. This secret should only be known to the recipient.

## Limitations and Assumptions

It was not tested with a broad range of businesses, whether all their tracking numbers have a fixed suffix and just count up. To do this, we would have had to brute force a lot of tracking numbers, gaining access to a lot of sensitive information.

DHL uses some kind of Akamai Anti-Bot Framework which is a blackbox for now. Using Selenium with an undetected chrome driver got rid of this problem but slowed down the process quite a bit.

As mentioned earlier, in our quick calculation on the needed guesses we ignored PO boxes, companies with their own postal codes and areas with low population but potentially high parcel flow.

## DHL’s Reaction

After some initial issues, DHL reacted quite well to our findings. First, they referred to technical measures that should prevent the abuse of the flaws, which probably referred to the bot detection. After we got a chance to proof the validity of our findings, they implemented the first measures in just a week. Since then the DHL parcel tracking site does not show the origin and destination parcel center name anymore.

Therefore, our approach to limiting the number of potential ZIP codes does not work anymore. It still does in an edge case. (If sender and recipient are in the same parcel center’s region, you can determine this by looking at the number of “hops” a parcel took – even if the names of the parcel centers are hidden to us.)

Another measure, which was implemented shortly before our talk at Troopers, is a rate limit on parcels. As soon as we do three wrong guesses for the postal code of a parcel, we are locked out for 20 minutes. This is not based on our client but on the tracking number. This slows us down significantly.  
Later, they also implemented even more measures. However, they did not tell us all the details.

The implemented measures slow down the attacks significantly, but, while this was not tested by us yet, leave potential for the collection of parcel information using a parallelized process as after three guesses other tracking numbers may be tried while waiting for the lock to terminate.

On an organizational level DHL introduced a [security.txt](https://www.dhl.de/.well-known/security.txt) and started a bug bounty program.

## Trivia

When researching stuff like postal codes you sometimes stumble upon interesting pieces of information. This might also be attributed to the fact that people who write for Wikipedia seem to like trivia. Did you know that there have been 6 postal code festivals in Germany? For example, the people of 24613 Aukrug celebrated theirs on the 24th of June 2013 (see why?) and formed the supposedly [largest human postal code in Schleswig-Holstein](https://de.wikipedia.org/wiki/Postleitzahl_\(Deutschland\)#Postleitzahlenfeste). Also, when the postal codes were assigned, an area nearly the size of Frankfurt (Main) with a population of 2 was forgotten. This lead to those two people having constant issues with the delivery of packages up until 2015, where [the issue was partially resolved](https://de.wikipedia.org/wiki/Postleitzahl_\(Deutschland\)#Kuriosa). Also check [this](https://www.youtube.com/watch?v=S9y9H0EB4jE) out.

## Disclosure Timeline

24.08.2022 – start of 90-day disclosure period of the vulnerability by ERNW to DHL

18.10.2023 – DHL refers to “IT-security measures”, which are supposed to mitigate the issue

27.02.2023 – Demo of proof-of-concept tool created by ERNW in a meeting with DHL

05.03.2023 – First fixes implemented and rolled out to production

28.06.2023 – Talk at Troopers 2023

(Big thanks to Fabian Ullrich who managed the disclosure process from ERNW-side.)

## Outlook

We will have a talk at the [Heise DevSec in September 2023](https://heise-devsec.de/veranstaltung-20712-0-physical-traceroute---oder-warum-bot-erkennungen-nicht-helfen.html) about the parcel tracking number issues (not only at DHL) – Stay tuned.

Cheers,  
Dennis Kniel & Florian Bausch

[Florian Bausch](https://insinuator.net/author/fbausch/ "Florian Bausch")

[ Back ](https://insinuator.net/#post-14312)

[DHL](https://insinuator.net/tag/dhl/)[Parcels](https://insinuator.net/tag/parcels/)[talk](https://insinuator.net/tag/talk/)[TROOPERS](https://insinuator.net/tag/troopers/)

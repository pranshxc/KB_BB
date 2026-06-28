---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-30_how-i-could-have-promoted-any-facebook-page-for-free.md
original_filename: 2018-03-30_how-i-could-have-promoted-any-facebook-page-for-free.md
title: How I Could Have Promoted Any Facebook Page For Free.
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 22ff5e8fd278c6d6304160d376316608c74220e160008f8bde170f27fee77ee2
text_sha256: 07cf9fba62c5bd88c92fdfb94dab911f50c5d4449493de00e2f636ac4734cfa8
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# How I Could Have Promoted Any Facebook Page For Free.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-30_how-i-could-have-promoted-any-facebook-page-for-free.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `22ff5e8fd278c6d6304160d376316608c74220e160008f8bde170f27fee77ee2`
- Text SHA256: `07cf9fba62c5bd88c92fdfb94dab911f50c5d4449493de00e2f636ac4734cfa8`


## Content

---
title: "How I Could Have Promoted Any Facebook Page For Free."
url: "https://medium.com/bugbountywriteup/how-i-could-have-promoted-any-facebook-page-for-free-70b0f4fc0feb"
authors: ["Anees Khan (@AneesEthical)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
publication_date: "2018-03-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5939
scraped_via: "browseros"
---

# How I Could Have Promoted Any Facebook Page For Free.

How I Could Have Promoted Any Facebook Page For Free.
AneesKhan
Follow
5 min read
·
Mar 30, 2018

303

2

Greetings Everyone!

This Blog Post is about How I was able to promote my Facebook Page Free of cost.

What is Facebook Promotion:

Press enter or click to view image in full size

How Does it Work:

Press enter or click to view image in full size

Here’s the Link, If you wanna read more about Promotions:
https://www.facebook.com/business/help/1189028774466371

So Lets start Hacking this Mechanism :)

I created a Fresh facebook page and Uploaded some Images to it. There was an Option called “Boost Post” below Every Image.

When I clicked on Boost Post, I was returned to a new page something like:

Press enter or click to view image in full size

Now here we have to set the amount and for how many days do have have to run our ad. So I filled up the form and clicked on Boost. And facebook asked me to add a Valid Card for the transaction.

NOTE: I only had 4 to 5 US Dollars in my Card but I started an ad for 100000 PKR which is almost 1000 USD.

I added my Card details and clicked on Continue. And it said that the Post is Under Review:

I was thinking that Facebook Might have a Manual check or review and I might be Blocked after this .But After a Couple Of Minutes I recieved a Notification Saying that You ad has been approved.

Press enter or click to view image in full size

I was Like:

But I was not sure that the ad will run completely or not. So I waited for a couple of hours and when I checked it again. I was as shocked as before.

My Post Reached 34,792 people and got 7.1k Likes.

My Reactions:

But All of a sudden my ad stoppped. I was not sure why is it stopped and what next steps do I have to take. But after reading there blogs and other stuff I sorted out that its some kind of functionality by facebook.

So How Does it Work.

Get AneesKhan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When we Boost a Post in Facebook then at that time it doesn’t charge the money from our card but instead it saves the money in our account that we need to pay later and it is named as “Threshold Amount”. But the threshold has got its limit. So when Our boosted post reaches the limit of 2500 pkr (20–25 Dollars), then the ad will be automatically stopped and it will be started again after paying that amount. So we can just Promote ads for 2500pkr.

Amount I have to Pay:

Threshold Limit:

I tried to change the threshold limit but it didn’t happen :(
I tried lots of different methods to bypass this protection but all in vain. So I left it.
But after a couple of days an Idea Came into my Mind. I thought what If we change the ownership of the page?
So what ? I went ahead and changed the admin of that page and removed the previous admin.

And Boom!!!

No Amount Due was shown this time So by doing the same process again I could have boosted up as many posts as I could.

Steps to Reproduce:

Create a Facebook Page and Boost a Post.
Add a Valid card which has at least 2–3 dollars in it.
The Ad will be started and it will run untill it reaches its threshold limit.
You can check the summary of your ads and amout spent by going to the following url:
https://www.facebook.com/ads/manager
Once the ad reaches its threshold limit, change the admin of the page and remove the previous admin.
Now start the whole process once again by boosting other or the same posts :)

I didn’t waste much more time and reported it to facebook but at first they were not able to reproduce it. So I provided them as much information as I could. Actually the issue with facebook was that it wasn’t validating the amount in the card. So after having a chit chat for a couple of days they Finally reproduced it and they Amused me by their Outstanding Reply:

Ok So they were already aware of the issue But were unable to reproduce it when I first reported it to them :P (Only Leets Can understand what I mean.)
I said Not a problem if you don’t wanna take it seriously.

NOTE: There’s something Notable in their reply which is “This behavior will eventually get caught by our fraud detection.”

I said why not challenging my self to see If I get caught or not. So I made a Brand New page and uploaded a video and some images and boosted them using the same process again and again.

Here are the results:

This was not just Limited to Posts but the Facebook Pages could’ve also been Promoted as well.

Got 2,514 Page Likes + Followers within a day :)

I showed these images to facebook and they’ve now implemented some fixes but Unfortunatley “Every Fix has a Bypass ” :D

I wasn’t awarded anything as they were already aware of the issue.

I Hope You Enjoyed this Write-Up.

Best Regards,
Anees Khan

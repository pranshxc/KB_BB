---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-14_hacking-intotinders-premium-model.md
original_filename: 2019-07-14_hacking-intotinders-premium-model.md
title: Hacking intoTinder’s Premium Model
category: documents
detected_topics:
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: dc5f0bbe2d691217c531ed2925981a13e12e772b3c760b710421c1606a534748
text_sha256: a00018c184dd18ef14a351105e9adcd5a2e48b9abb43ac338cdc3b80c0895931
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking intoTinder’s Premium Model

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-14_hacking-intotinders-premium-model.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `dc5f0bbe2d691217c531ed2925981a13e12e772b3c760b710421c1606a534748`
- Text SHA256: `a00018c184dd18ef14a351105e9adcd5a2e48b9abb43ac338cdc3b80c0895931`


## Content

---
title: "Hacking intoTinder’s Premium Model"
page_title: "Hacking into Tinder’s Premium Model | by Sanskar Jethi | Medium"
url: "https://medium.com/@sansyrox/hacking-tinders-premium-model-43f9f699d44"
authors: ["Sanskar Jethi (@sansyrox)"]
programs: ["Tinder"]
bugs: ["Broken authorization"]
publication_date: "2019-07-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5153
scraped_via: "browseros"
---

# Hacking intoTinder’s Premium Model

Hacking into Tinder’s Premium Model
Sanskar Jethi
Follow
4 min read
·
Jul 14, 2019

987

19

1

In this blog, I’ll be talking about how we can bypass the tinder’s premium service and convert likes into matches through a vulnerability in their API.

Reason for this post:

So, I reported this bug to Tinder’s bug bounty team and they gave me the following response:

“We are aware of this behavior and we choose to not take any action for the same”.

Which meant either of these two things:

Tinder team were just being d*cks and denied me my bounty
or
This is actually the way they want their API to work

Whatever the case may be, the world needed to know! xD

The Good Stuff:

Tinder has a system of Likes and Matches.
When a person swipes right to you, you get a like and when swipe right back to him/her its a match.

But unless you are a premium subscriber, you can’t see the liker’s profile/photo. All you get is a blurred photo and the option to buy the premium service.

Press enter or click to view image in full size

So, when I was reverse-engineering their API, I happen to find that, tinder blurs the image on the client-side and sends a complete image as a response.

https://api.gotinder.com/v2/fast-match/preview

So, the API requires a few request headers which can be obtained through an easy process.

Step 1: Get your Request Headers.

Login to your Tinder account in a browser, open the developer console and search for the following request.

Press enter or click to view image in full size
Step 2: Make a Request to The Endpoint and Access the Photo
Press enter or click to view image in full size

and save through the following process.

Press enter or click to view image in full size

and voila! You have your desired image.

The only dynamic parameter is the X-Auth-Token which needs to be updated after every week or when the call fails.

We make a simple request and voila.

On further investigation, I found out that Tinder’s LIKE system follows a Queue or FIFO system, where to get the image of every person who likes you on Tinder, you have to match to the one present at the front of the queue, i.e. the response image which was received.

Now you search through your recommendations and just swipe right :)

Some BONUS Content

And tinder’s recommendation system follows a circular queue system, i.e. a recommendation rejected by you is likely to show up again as your recommendation until a new image is added in the queue which happens once in 24 hours or when you change your physical location.

Also, tinder applies a profile boost when you travel to a different state/country and basically fetches you double the number of likes that you are likely to get.

Get Sanskar Jethi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, this endpoint fetches you the image and user id of your recent suggestion.

https://api.gotinder.com/user/recs

fetches you the following response

{
“status”: 200,
“results”: [{
“distance_mi”: 2,
“common_like_count”: 0,
“common_friend_count”: 0,
“common_likes”: [],
“common_friends”: [],
“_id”: “518d666a2a00df0e490000b9”,
“bio”: “”,
“birth_date”: “1986–05–17T00:00:00.000Z”,
“gender”: 1,
“name”: “Elen”,
“ping_time”: “2014–04–08T11:59:18.494Z”,
“photos”: [{
“id”: “fea4f480–7ce0–4143-a310-a03c2b2cdbc6”,
“main”: true,
“crop”: “source”,
“fileName”: “fea4f480–7ce0–4143-a310-a03c2b2cdbc6.jpg”,
“extension”: “jpg”,
“processedFiles”: [{
“width”: 640,
“height”: 640,
“url”: “http://images.gotinder.com/518d666a2a00df0e490000b9/640x640_fea4f480-7ce0-4143-a310-a03c2b2cdbc6.jpg"
}
}

And using some OpenCV magic (to check whether the photos match) and some more requests, you can automate your searching process and make your lives much simpler.

All you have to do is make GET requests using the same request headers as above.

To like the matched photo:

https://api.gotinder.com/like/{id}

And to reject the rest:

https://api.gotinder.com/pass/{id}

If the above is too complex for you, you can just swipe your way through.

I don’t have the time to code program for this, but if someone wants to create one, I’ll happy to collaborate.

Happy Matching!

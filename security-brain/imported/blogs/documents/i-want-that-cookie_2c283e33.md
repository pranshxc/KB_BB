---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-27_i-want-that-cookie-.md
original_filename: 2020-03-27_i-want-that-cookie-.md
title: I Want that Cookie !!!
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
raw_sha256: 2c283e336935e92fddc441502b9477f4e9c33911366332826533f4aaa97341a7
text_sha256: 25e6c722af65ed54110d052515bc9f75260aeaab438b42a00c73e49aace4df69
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# I Want that Cookie !!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-27_i-want-that-cookie-.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2c283e336935e92fddc441502b9477f4e9c33911366332826533f4aaa97341a7`
- Text SHA256: `25e6c722af65ed54110d052515bc9f75260aeaab438b42a00c73e49aace4df69`


## Content

---
title: "I Want that Cookie !!!"
url: "https://medium.com/@adnanmalikinfo110/i-want-that-cookie-8d2daab242ac"
authors: ["Adnan Malik (@infoadnanmalik)"]
bugs: ["Logic flaw"]
publication_date: "2020-03-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4686
scraped_via: "browseros"
---

# I Want that Cookie !!!

I Want that Cookie !!!
Adnan Malik
Follow
3 min read
·
Mar 27, 2020

74

1

Press enter or click to view image in full size

Hi hunters! This is the story of simple bug I found. I got a private invitation from a company (name it XYZ) on Hackerone. Checked out the VDP/scope and fastened my seat belt to hack. It was an e-commerce store selling some apps and softwares. I was checking it out and trying to understand the flow of the target. Went for some low hanging fruits but grapes were sour. What I noticed was, there was no user account system. All you need is to choose the object you want to purchase, add to cart and give your bank card credentials. That’s it. Very simple? Right.

While testing I came across a feature which was named a loyalty discount and I am pretty sure, all e-commerce have this. Loyalty discount is something given to loyal customers who made regular purchases with that particular store. As they are regular customers, they are given high discounts sometimes. But something which grabbed my attention was, how XYZ is going to know that I have made purchases with them previously or not as there is no user account ? Of Course they have an authentication system for it. You need to put your email, they will verify it. If you have made some regular previous purchases with them , they will directly apply the discount coupon. After verification, all you need is, pick an object, add to cart and give your credit card credentials. And you will see the 50% off in your final total at checkout. That’s it.

But wait a minute !!!! Where have they kept the coupon after verifying the email address for previous purchases? Either they have to keep it in my session storage or either in cookies. But there is no account system in this store. Well, quite clear then, they keep that coupon in the cookies.

“ I badly want that cookie “. I said to myself

Get Adnan Malik’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But to get that cookie, I need someone email who had previous purchases with XYZ store. Time for reconnaissance. I went to find their employee email. For sure they would have purchased those products (Free or paid; Not my headache) . LinkedIn was there to do the job. Spent an hour and finally found one ( not of internee :p ) . Now went straight to the loyalty discount verification feature. Put any random email and catch the request. The request is like this.

Send it to repeater and replace the random email with the one having previous purchases. Check out the ‘set-cookie’ in http response header and game over.

Now as the cookie has been updated with the coupon, I choose an object, added to the card and saw the 50% off in the final total. And that’s how can everybody get 50% off on their purchases without being a loyal customer. The coupon value can be check from the storage portion of inspect element.

Sometimes the target is as simple as this. All we need is an eye with a focus to see and observe what others can’t.

Impact: The regular customers sometimes get high discounts from online stores. But as the store was having no user account system to store coupons in their session cookies, they could be gotten by anyone. Anyone could get that high discount, without having previous purchases. I have found another security flaw using the same methodology but that was marked as duplicate to this as the source of flaw was the same.

Happy Hacking !!!

GET in touch here:

https://www.twitter.com/infoadnanmalik

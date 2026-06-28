---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-28_one-more-parameter-manipulation-bug-.md
original_filename: 2019-06-28_one-more-parameter-manipulation-bug-.md
title: One more Parameter manipulation bug (🤑)
category: documents
detected_topics:
- sso
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 1e8a01fadfb18533feeba72f7c1c4da32ffda568d5c502f85d4ef3c164b7d675
text_sha256: fffb313d4ea8e815faa40aad5a24ed19ee801a84e697a7bae250ee55c7921329
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# One more Parameter manipulation bug (🤑)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-28_one-more-parameter-manipulation-bug-.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1e8a01fadfb18533feeba72f7c1c4da32ffda568d5c502f85d4ef3c164b7d675`
- Text SHA256: `fffb313d4ea8e815faa40aad5a24ed19ee801a84e697a7bae250ee55c7921329`


## Content

---
title: "One more Parameter manipulation bug (🤑)"
url: "https://medium.com/@kanchansinghyadav/one-more-parameter-manipulation-bug-7fa0551a6021"
authors: ["Kanchan Singh Yadav (@KanchanSingh0)"]
bugs: ["Parameter tampering"]
publication_date: "2019-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5176
scraped_via: "browseros"
---

# One more Parameter manipulation bug (🤑)

One more Parameter manipulation bug (🤑)
Kanchan Singh Yadav
Follow
5 min read
·
Jun 28, 2019

160

1

Hey everyone,
I am back again with one more post and it is about parameter manipulation .
So what the heck is that?

Here is the official definition by OWASP

The Web Parameter Tampering attack is based on the manipulation of parameters exchanged between client and server in order to modify application data, such as user credentials and permissions, price and quantity of products, etc. Usually, this information is stored in cookies, hidden form fields, or URL
Query Strings, and is used to increase application functionality and control.

Or simply put, you tamper/alter the parameters to check how the application reacts to the changes.
The title is enough to tell you what we will be dealing with today, yeah right Money part or technically price and quantity parameter manipulation.

money!!

Price or quantity parameter manipulation is self-explanatory but let me put it in simple English, “A hacker try to change the parameter value as to reduce the price of a product or order more than 1 product with price equal to single product or even in some cases get a product on a price of other product(which is obviously cheaper than the original price of the product) or all”.

Price manipulation is one of the attractive topics in ethical hacking and almost all organizations dealt with it long back, so most authors and hackers say that it is a thing of past and it is rarely possible to find one. I believed the same but this website had something else for me.

Website Developer!

So one day after finding a parameter manipulation on a website, I checked a similar website for the same vulnerability(Parameter manipulation).
This website was selling shoes and other wearables.

First, I was just checking the normal workflow. Everything was normal, working like charm without any problem.
Now bring in the guns, Burp Suite.

burp

I was just looking for parameter manipulation that’s why I was not paying attention to other things.
After selecting the product, you need to select the right size(normal working) and then add to cart. Burp suite was sending this when I clicked add to cart,

request to server

Sweet, I can change the price as simple as that and I am done

Press enter or click to view image in full size
yes!!

but…..

even after changing price it was not reflected which means the website is using the product id to fetch the price, cool so there is no point of changing the product id as that will change the price as well.

So what next…
we do have one more parameter with which we can play i.e quantity, So I Changed it to negative(-1) AND the price is negative,

good!

which means that the company will pay me that amount and give me the product as well so it’s a win-win situation.

Get Kanchan Singh Yadav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Killing two birds with one stone

but…
As I clicked on checkout I was welcomed by this

Surprise !!

so again I am in the middle of nowhere

No!!

So what I can do?
I tried other things, got nothing but during the process I got to know that the cart id can be changed as there is no check on the cart id i.e I can create new carts without any problem. Prior to that every time I add, delete or change anything I have to manually reverse the steps or have to clear cookies or open up a private window which was slowing me down to get a new cart. Now I just need to add a random value to cart id and I got an empty cart.

but what to do next?
After thinking for a while an idea came to my mind,

idea!!!

so I added a product normally and one more product having less price than the first price but quantity is changed to negative(-1) and it worked. Total price is equal to their difference.

Press enter or click to view image in full size

Simple, let’s do some maths to understand it easily

the total price is as follows:

total=pof-pos _______________(equation 1)*condition

where pof=price of first product, pos=price of the second product

*condition:- equation 1 will only hold true when the total is greater than 0 (total>0) because if your total price is negative(total<0) the process will fail.

so where was the problem,
the problem was in the way the website was handling the user inputted data, they were taking the data directly and multiplying it with product price.

total_price=price*quantity

they do check the total if it is negative or positive before payment section but that can be abused to reduce the price of the product.

Lesson learnt

Even if there is rarest of the rarest possibility for something, do check it as it may have 0.01% probability for all but if you got it then you converted that 0.01% to 100%.

Do give your feedback!!

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-28_this-popular-facebook-app-publicly-exposed-your-data-for-years.md
original_filename: 2018-06-28_this-popular-facebook-app-publicly-exposed-your-data-for-years.md
title: This popular Facebook app publicly exposed your data for years
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- information-disclosure
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- information-disclosure
- supply-chain
language: en
raw_sha256: 74eaa20bf6c0bb6008608f60effd1c4a2144b3934a6deb83408f34973cb3103b
text_sha256: 006841fbdfcbc8433465ad1785affd679e0d1ce0a3f3744678dad31494b259da
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# This popular Facebook app publicly exposed your data for years

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-28_this-popular-facebook-app-publicly-exposed-your-data-for-years.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `74eaa20bf6c0bb6008608f60effd1c4a2144b3934a6deb83408f34973cb3103b`
- Text SHA256: `006841fbdfcbc8433465ad1785affd679e0d1ce0a3f3744678dad31494b259da`


## Content

---
title: "This popular Facebook app publicly exposed your data for years"
url: "https://medium.com/@intideceukelaire/this-popular-facebook-app-publicly-exposed-your-data-for-years-12483418eff8"
authors: ["Inti De Ceukelaire (@securinti)"]
programs: ["Meta / Facebook", "Nametests.com"]
bugs: ["Information disclosure", "Broken authorization"]
bounty: "4,000"
publication_date: "2018-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5823
scraped_via: "browseros"
---

# This popular Facebook app publicly exposed your data for years

This popular Facebook app publicly exposed your data for years
Inti De Ceukelaire
Follow
7 min read
·
Jun 28, 2018

966

3

Ever took a personality test on Facebook? For years, anyone could have accessed your private information, friends, posts and photos.

Press enter or click to view image in full size

Nametests.com, the website behind the quizzes, recently fixed a flaw that publicly exposed information of their more than 120 million monthly users — even after they deleted the app. At my request, Facebook donated $8,000 to the Freedom of the Press Foundation as part of their Data Abuse Bounty Program.

In the light of the Cambridge Analytica scandal, Facebook tried to clean up its act by launching their data abuse bounty program. Being a participant in their Bug Bounty Program, I got triggered and decided to give it a shot. I scrolled through my timeline and noted down all apps my friends were using. Fitness trackers and Facebook Quizzes topped my list. The latter have been heavily criticised for their massive data harvesting and data-greedy permissions, so for the first time in my life, I took a Facebook Quiz:

Press enter or click to view image in full size
According to nametests.com, if I were a Disney Princess, I would be Jasmine.

Upon closer investigation, I noticed something strange.

While loading a test, the website would fetch my personal information and display it on the webpage. Here’s where it got my personal information from:

http://nametests.com/appconfig_user

Press enter or click to view image in full size
In theory, every website could have requested this data. Note that the data also includes a ‘token’ which gives access to all data the user authorised the application to access, such as photos, posts and friends.

I was shocked to see that this data was publicly available to any third-party that requested it.

In a normal situation, other websites would not be able to access this information. Web browsers have mechanisms in place to prevent that from happening. In this case however, the data was wrapped in something called javascript, which is an exception to this rule.

One of the basic principles of javascript is that it can be shared with other websites. Since NameTests displayed their user’s personal data in javascript file, virtually any website could access it when they would request it.

Press enter or click to view image in full size
NameTests wants to know who you are so they ask nametests.com/appconfig_user, but any other website could do that as well.

To verify it would actually be that easy to steal someone’s information, I set up a website that would connect to NameTests and get some information about my visitor. NameTests would also provide a secret key called an access token, which, depending on the permissions granted, could be used to gain access to a visitor’s posts, photos and friends. It would only take one visit to our website to gain access to someone’s personal information for up to two months.

Video proof:

An unauthorised website getting access to my Facebook information

As you can see in the video, NameTests would still reveal your identity even after deleting the app. In order to prevent this from happening, the user would have had to manually delete the cookies on their device, since NameTests.com does not offer a log out functionality.

I would imagine you wouldn’t want any website to know who you are, let alone steal your information or photos. Abusing this flaw, advertisers could have targeted (political) ads based on your Facebook posts and friends. More explicit websites could have abused this flaw to blackmail their visitors, threatening to leak your sneaky search history to your friends.

Timeline of events:

On April, 22nd, I reported this to Facebook’s Data Abuse program.

On April 30th, I received an initial response from Facebook, stating that they’re looking still looking into it.

On May 14th, I sent a follow-up mail, asking whether they already reached out to the app developers.

On May 22th, Facebook said that it could take three to six months to investigate the issue (as mentioned in their initial automated reply) and that they would keep me in the loop. At this time, the NameTests quizzes were still up and running.

On June, 25th I noticed NameTests had changed the way they process data. Third-parties could no longer access its users personal information. I contacted them about the fix, told them about this blogpost and asked them to donate the bounty to Freedom of the Press Foundation.

Get Inti De Ceukelaire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On June, 26th, I reached out to NameTest’s Digital Protection Officer to answer some questions regarding the vulnerability and the disclosure process by Facebook.

On June, 27th, Facebook informed me they donated $8,000 ($4,000 bounty, doubled because I chose to donate it to charity) to the Freedom of the Press foundation as part of their data abuse bounty program:

Press enter or click to view image in full size

I also got a response from NameTests. The public relations team claims that, according to the data and knowledge they have, they found no evidence of abuse by a third party. They also state that they have implemented additional tests to find such bugs and avoid them in the future. As soon as I get permission to publish our conversation, I will post it here for the sake of completeness.

On June, 28, I published this blog post. In response to this, Facebook issued a public statement on their Facebook page: https://www.facebook.com/BugBounty/posts/2117617158252499

I have mixed feelings about this one. I am glad both Facebook and NameTests cooperated and resolved the issue. On the other hand, we cannot accept that the information of hundreds of millions of users could have been leaked out so easily. We can and must do better.

Follow me on Twitter for more updates: https://twitter.com/securinti

FAQ
How many users were affected?

According to Facebook, NameTests has more than 120 million active monthly users. I have no insights in how many users have given their data to the app since their launch early 2015. It is important to note that if this flaw was ever abused, only the users that actually visited the attacker’s website would have their data leaked to the attacker.

To get more grip on the reach of these quizzes, I made a list of their NameTest’s localised Facebook pages pages with more than one million likes. Pretty scary numbers, considering the fact you don’t even have to like their Facebook page to take a quiz. Their potential reach is immense:

Press enter or click to view image in full size
There are so many NameTests pages that I only published the ones with +1M likes.
How long did this flaw exist?

Looking at archive.org, the flaw has been there at least since the end of 2016.
NameTests said they introduced the script on the 24th of January, 2017.

Did NameTests know about this?

I have no evidence to claim that. It could have been a rookie programming mistake, but given the fact that this went unnoticed since 2016, it raises some serious questions about the way they handle the security of their hundreds of millions of users. Their terms of service are pretty clear on this:

NO CLAIMS OR PROMISES ABOUT THE QUALITY, ACCURACY, OR RELIABILITY OF THE SITE, ITS SAFETY OR SECURITY, OR THE SITE CONTENT. ACCORDINGLY, THE PROVIDER’S ENTITIES ARE NOT LIABLE TO YOU FOR ANY LOSS OR DAMAGE THAT MIGHT ARISE, FOR EXAMPLE, FROM THE SITE’S INOPERABILITY, UNAVAILABILITY OR SECURITY VULNERABILITIES OR FROM YOUR RELIANCE ON THE QUALITY, ACCURACY, OR RELIABILITY OF THE CONTENT, BUSINESS LISTINGS, RATINGS, REVIEWS, METRICS, OR REVIEW FILTER FOUND ON, USED ON, OR MADE AVAILABLE THROUGH THE SITE.

Their Digital Protection Officer did let me know that they take data security very seriously, though.

Was this flaw ever discovered by someone else?

It’s hard to tell. I can only say that it was really easy to spot, and I would be surprised if nobody else found this earlier, given the website claims to generate more than 3 billion page views every month, most of which had references to the leaky javascript. NameTests does state that, according to the data and knowledge they have, they did not find any evidence of abuse.

What data could have been leaked?

Depending on what quizzes you took, the javascript could leak your facebook ID, first name, last name, language, gender, date of birth, profile picture, cover photo, currency, devices you use, when your information was last updated, your posts and statuses, your photos and your friends.

What data could have been leaked after the app was deleted?

If you ever took a quiz and removed the app afterwards, external websites would still be able to read your facebook id, first name, last name, language, gender, date of birth. You could have only prevented this from happening if you manually deleted your cookies, as the website does not offer a logout functionality.

How can I protect myself from against these kind of leaks?

Delete any apps that you’re currently not using, be wary when giving new apps access to your data and delete your cookies on a regular basis.

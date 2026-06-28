---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-15_a-facebook-bug-that-exposes-emailphone-number-to-your-friends.md
original_filename: 2021-09-15_a-facebook-bug-that-exposes-emailphone-number-to-your-friends.md
title: A Facebook bug that exposes email/phone number to your friends
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: 3a02bc8e1f88e18cc139a5e34698a9b64bf9c40ac3670234d49e7b7c3d2a3676
text_sha256: fcbfa14e5464e8377e25c098f045ef66a9037ecf974cb63c6e8d8bce11659476
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# A Facebook bug that exposes email/phone number to your friends

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-15_a-facebook-bug-that-exposes-emailphone-number-to-your-friends.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `3a02bc8e1f88e18cc139a5e34698a9b64bf9c40ac3670234d49e7b7c3d2a3676`
- Text SHA256: `fcbfa14e5464e8377e25c098f045ef66a9037ecf974cb63c6e8d8bce11659476`


## Content

---
title: "A Facebook bug that exposes email/phone number to your friends"
url: "https://iamsaugat.medium.com/a-facebook-bug-that-exposes-email-phone-number-to-your-friends-a980d24e5ea8"
authors: ["Saugat Pokharel (@saugatscript)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Logic flaw"]
bounty: "19,250"
publication_date: "2021-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3313
scraped_via: "browseros"
---

# A Facebook bug that exposes email/phone number to your friends

Saugat Pokharel
 highlighted

A Facebook bug that exposes email/phone number to your friends
Saugat Pokharel
Follow
6 min read
·
Sep 15, 2021

577

2

Hi, I am Saugat Pokharel from Kathmandu, Nepal. Today, I am going to explain my other quick and easy finding on Facebook. This bug could have caused a Facebook user to expose email/phone number to their friends. Let me explain in detail.

On April 3, 2021, I saw the news on the internet with the title “533 Million Facebook users’ phone/email leaked online”. Being an active Facebook user, the news was very concerning for me. But later Facebook clarified that those data were not collected through hacking but through public scrapping by abusing a feature called “Contact Importer”. Also, FB said that those were old data from 2019.

I checked whether my data was there on the list or not. And luckily, I didn’t find my data over there. However, I wanted to change my email as a precautionary measure. So, I went to Facebook > Settings > Account Settings and changed my email.

While adding a new email, I read the prompt very carefully. It was written that, “Only you will see your email on your profile.” This means the new email should have privacy “Only Me”.

Press enter or click to view image in full size

I added a new email and confirmed that email. After confirming, I went to my profile and found out that the email privacy defaulted to “Friends” instead of “Only Me”. I came to the prompt and read the text carefully again. It was clearly saying that the email should be visible to only me. Many Facebook users could have read the prompt and fairly believe that the expected privacy will be applied. Although users could change the privacy of their email later on, but not everyone will repeatedly check the privacy of their email after confirming. I became pretty hopeful that it was a bug. So, I quickly reported the issue to Facebook Security.

After sending the report, I went to dig further. I wanted to see if this happens with the phone numbers as well or not. To confirm, I went to: https://www.facebook.com/settings?tab=account&section=phone.

Press enter or click to view image in full size

I added and confirmed my number. And as expected, the privacy defaulted to “Friends” here as well. So, I quickly mentioned the issue in the same report. For my better Hacker Plus Count, I asked the security team if I can file a different report on this phone number issue. I got a reply “Sure, you can create a different report.”

The email issue was acknowledged by the security team and got fixed 3 days after triage. The Facebook team said, “We will decide bounty once we fix this phone number issue as well.”

Since the email issue was fixed, I tried to bypass the original fix. For this, I gave a try to disavow flow this time.

What is Disavow Flow?

This is a feature from Facebook where it is possible to regain access to the account directly from an email if in case the account is compromised or hacked. If any hacker accessed the account and changed the password/email/phone, then a notification will be sent to the previously removed email to confirm whether you did this or not. And the victim can disavow the action by clicking “Secure your account”.

Press enter or click to view image in full size
Email notification from where disavow flow can be initiated

So I clicked on “secure your account”, and then added a new email. After adding a new email, I also saw an option to change my email address. I changed the email address with some random email from temp mail. Then again after confirming the email, its privacy defaulted to “Friends” instead of “Only Me”.

Press enter or click to view image in full size

With this, I was able to confirm that the patch was not sufficient. So, I replied in the initial report along with the bypass steps and a video POC demonstrating the issue. Again, I created a new report for this disavow flow bypass after getting approval from the security team.

I began to look for more bypasses and found that there were so many endpoints where the email defaulted to privacy “Friends”. I sent a few more bypasses again and again until I got the response as shown below.

Press enter or click to view image in full size
Press enter or click to view image in full size

Since I was suggested not to spend time looking for bypasses, I stopped searching for more vulnerable endpoints.

Get Saugat Pokharel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I began to wait patiently for the fixed message. I was quite sure that I will be getting a good reward for this issue. I made this assumption based on the previous FB payout guidelines on similar reports.

And after waiting patiently for 4 months, I got a fixed message and a reward from Facebook. All three reports had the same reward. The total reward was $18250. ($5000×3 + Bonus $3250)

My finding was also featured on a blog post by Facebook Bug Bounty Page as one of the interesting bugs related to contact point, on the same day when I got the bounty.

Click here to read the blog post.

Facebook said that they fixed the issue and corrected the settings for people whose visibility configuration they believe was impacted. This means all FB users who added their email later on and had privacy “Friends” were changed to “Only Me”. Also, FB said they didn’t find any evidence of abuse (scraping of those data).

Previously, when we create a new FB account, the default privacy used to be “Friends”, but the privacy from now onwards will be “Only Me”. While checking the fix, I found all endpoints were correctly identified and fixed.

The bounty also took me to rank #11 globally on Facebook Whitehat Thanks Page.

Press enter or click to view image in full size

Also, I reached Platinum league in Facebook Hacker Plus League. Researchers in this league will get an invitation to attend Vegas DEFCON (all sponsored by Facebook).

Press enter or click to view image in full size

Also, I received a great message from one of my favorite security engineers at Facebook.

Press enter or click to view image in full size

Fun Fact: While verifying the email issue, I encountered another issue. One of my emails was not being removed from my account using mobile devices. I intercepted the android app traffic and tried to delete that specific email. But, there was always an exception blocking the deletion. The issue was acknowledged and fixed by Facebook. I was rewarded $1000 for finding that issue.

Press enter or click to view image in full size
Undeletable email address

Timeline of the report:

Initial email issue sent: April 17, 2021
Initial phone issue sent: April 17, 2021
Triaged: April 21, 2021
Email issue fixed: April 24, 2021
Bypass sent: May 7, 2021
Phone number issue fixed: September 2, 2021
Bypass fixed: September 2, 2021
Bounty Rewarded: September 2, 2021

Press enter or click to view image in full size
Bounty message from one of the three spitted reports

Video POC: https://youtu.be/wkGQL2jNabU

I am very thankful to Ajay Gautam, Sameer Rao, Kassem, and Bassem Bazzoun for their constant motivation and guidance in the recent years/months.

I do have a YouTube channel where I have been sharing bug bounty tips/tricks and my experience in Nepali language. You may visit my channel if you are from Nepal or understand Nepali language.

Link to my channel: https://www.youtube.com/c/saugatpokharel

Thank you for taking the time to read my article. Have a great day!

You can follow me on Facebook or Twitter if you would like to stay connected with me.

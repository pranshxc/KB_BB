---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-14_deleted-data-stored-permanently-on-instagram-facebook-bug-bounty-2020.md
original_filename: 2020-08-14_deleted-data-stored-permanently-on-instagram-facebook-bug-bounty-2020.md
title: Deleted data stored permanently on Instagram? Facebook Bug Bounty 2020
category: documents
detected_topics:
- command-injection
- automation-abuse
- business-logic
tags:
- imported
- documents
- command-injection
- automation-abuse
- business-logic
language: en
raw_sha256: 2fa0d7fa67f459fbb58d9d6f2a96f39aa764476a404e9bfc018e1ea464677967
text_sha256: 09a9c6f8e5eeea05e83cd76b9277844c4ff99271d358cf1ed0472886d849a68a
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Deleted data stored permanently on Instagram? Facebook Bug Bounty 2020

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-14_deleted-data-stored-permanently-on-instagram-facebook-bug-bounty-2020.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `2fa0d7fa67f459fbb58d9d6f2a96f39aa764476a404e9bfc018e1ea464677967`
- Text SHA256: `09a9c6f8e5eeea05e83cd76b9277844c4ff99271d358cf1ed0472886d849a68a`


## Content

---
title: "Deleted data stored permanently on Instagram? Facebook Bug Bounty 2020"
url: "https://medium.com/nassec-cybersecurity-writeups/deleted-data-stored-permanently-on-instagram-facebook-bug-bounty-2020-26074c229955"
authors: ["Saugat Pokharel (@saugatscript)"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Privacy issue"]
bounty: "6,000"
publication_date: "2020-08-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4323
scraped_via: "browseros"
---

# Deleted data stored permanently on Instagram? Facebook Bug Bounty 2020

Deleted data stored permanently on Instagram? Facebook Bug Bounty 2020
Saugat Pokharel
Follow
8 min read
·
Aug 14, 2020

954

5

Hello, I am Saugat from Kathmandu, Nepal. Today I am going to explain one of the coolest and easiest bugs which I accidentally found on Instagram a few months ago.

One day, I was not looking for a bug, I was just browsing my Instagram profile. I thought I should take a backup of my Instagram data so that I could save all of my photos at once. Data on Instagram generally refers to everything; Login details, followers and following, likes, conversations, photos, search history, checkout, etc.

I went to Instagram settings > Accounts >Privacy and Security.

I clicked on View Account Data and requested for the backup by entering the necessary credentials. Then it said I would receive the backup file within a few hours. In about 2 hours, I got the mail saying, “Your Instagram Data.” I clicked on it, and then I was redirected to the Instagram login page. I entered my password for verification then a zipped file containing my account data was downloaded.

I unzipped the file and began to view all the files and folders one after another. To my surprise, I noticed a very unusual thing. The backup files had few photos which I deleted back in 2013. I was shocked and thrilled. How could that happen? I still remember one of my photos which I deleted within a minute of uploading back in 2013. But, I could clearly view that photo in the backup folder. How could that be possible?

Or is this intended? I read somewhere earlier that raw images can be accessed from Facebook CDN even after deleting the images. But, for 6 years? I was not convinced myself since that was a very long period of time. I thought this should not have actually happened.

Digging up even further, I found that the conversations that were deleted long ago were still viewable in the Message.json folder. There were URL links for the photos in the conversation files which when copied and pasted into the browser would generate valid signature URL and loads up respective photos/attachments which were sent and deleted 4–5 years back.

After analyzing for a few minutes, I decided to report this issue to Facebook. I went to facebook.com/whitehat/report and wrote a quick report as follows.

They replied:

Hi Saugat,

Thank you for your report. We are unsure at this time that this is a privacy or security issue; as such, it might not qualify as a part of the bounty program. Could you please clarify how this bug is able to compromise the integrity of Facebook user data, circumvent the privacy protections of Facebook user data, or enable access to a system within Facebook’s infrastructure?

Thanks,

Ed Kurson
Security

I replied back with the following message.

It affects the privacy and integrity of the user as the backup data reveals all the deleted photos and conversations. When a user deletes the chat history and photo, it should not appear in backed up data. If the deleted photo can be viewed again through the backup, what is the meaning of deleting? This also shows that our data is kept safe permanently even if chats and photos are permanently deleted from our side. This is a very big compromise to user privacy. Instagram should not store my photos and chats permanently when I delete them.

Conversation continued.

Hi Saugat,

Thank you for the additional context! To help us understand better, do you know what the timeline for all these actions were? For instance, did the backup happen quickly after the conversations were deleted?

Thanks,

Ed Kurson
Security

I answered:

The conversations were deleted two weeks ago and back up was requested 10–12 days after the conversation was deleted. But, the backed up data was provided after 7–8 hours of the request. The folder contained all conversations from the beginning no matter when it was deleted. It also contained photos that were deleted 5–6 years back.

Conversation continued.

Hi Saugat,

Thank you for that context! I have found a little more information regarding what you are seeing.

When you choose to delete something from our platform (a profile picture in this example), it is immediately removed from public view. You are still able to access that entity if you have a direct link to it. Our Content Distribution Network (CDN) is a complex and highly distributed network of servers. As per our policies, full deletion (including from backups) can take up to 90 days. You can read more on our data retention policy at the following URL:

https://www.facebook.com/policy/

Thanks,

Ed Kurson
Security

I felt very sad to see my report being closed as informative. The reply from the security team did not clear up my confusion. They were saying that deleted data will take up to 90 days to get deleted from their server (CDN). But, I was able to view the photos that were deleted more than 5 years ago. I was thinking to reply to them with additional details. But, I got the reply the next day with the following message.

Hi Saugat,

I’m Megan from the Security team. I wanted to apologize for the confusion and let you know that we are taking another look at your report.

I will keep you updated on our progress.

Thanks,

Megan
Security

I was very happy to see that message. As the security team re-opened my case, I was quite hopeful that this would qualify for the bug bounty program.

So, I replied with a smile in a face.

Okay, thank you for taking a close look at my report. I believe that it will qualify for the bounty program.

Conversation continued.

Hi Saugat,

No problem. Could you please let us know the affected Instagram username(s)?

Thanks,

Megan
Security

I replied:

The affected username is: (redacted)

Thank you.

I was asked again:

Hi Saugat,

Thanks for providing the username. We require further info to investigate, so could you please confirm the last time you made a backup request, and if possible, could you request a new backup?

Thanks,

Get Saugat Pokharel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Megan
Security

I answered with the following.

I requested the data on Oct 5, at around 4 PM (approx) and I got the backup link at exactly 7:36 PM the same day into my Gmail account. Sure, I will request for the new backup as well. Should I request for the new data and check either this issue exists or not?

Just In: I requested the new backup and found that the deleted messages and photos can be seen as before. So, I am sure that the issue still persists.

Conversation continued.

Hi Saugat,

Thanks for providing us with this info. I’m having a hard time locating your backup request so I wanted to check what kind of email you received. If possible, could you provide us with a screenshot and/or copy of the email received from Instagram with the backup?

Thanks,

Megan
Security

I answered:

I had requested for backup on October 24. I got the below-attached mail into my Gmail on the same day saying that the requested data has been provided.

I clicked on the button (DOWNLOAD DATA) which redirected me to login page. Once I logged in, it gets me into the download page and I took a backup from there. The download page link was:
https://www.instagram.com/download/confirm/nGzKfDA8PX/

I hope this helps. Thank you.

Again the conversation continued.

Hi Saugat,

Much appreciated, thanks.

To give you an update here — I’m in conversation with the Instagram team and actively investigating. I was wondering if you could provide one or both of the following to help us further:

- a photo that you deleted but still shows up in the backup zip file
- the username of a user that you chatted with, and deleted the chat, but still shows up in the backup zip file

I’ll let you know if I have further updates from our end.

Thanks,

Megan
Security

I wrote a reply as follows.

Thank you Megan for the reply.

Below is the deleted photo which appears in the backed up zip file.

The username of a user that I chatted with, and deleted the chat, but still shows up in the backup zip file is: (redacted)

Existing link of the deleted photo: (redacted)

Hope it helps.
Thank you

The conversation continued.

Hi Saugat,

Thanks for the info. I’ve passed your report to our Instagram Security & Privacy team for further analysis and will let you know when I’ve got an update.

Thanks,

Megan
Security

I took a backup of my other account and found that it contained photos and information that were deleted more than a year ago. So, I wrote the next day with the following message.

Okay sure. I am waiting for the update.

I took the backup an Instagram account today and found that it contained few photos which were deleted more than a year ago. I hope this will be fixed very soon. Thank you.

The active conversation came to an end as the issue was sent to the appropriate team and fix was being deployed. I pinged them continuously asking for the update.

After 3 months of no response, the security team replied on January 10, 2020 as follows.

Hi Saugat,

Apologies for the delay. The team is working on a complete fix. We’ll help provide an update when there is new information to share.

Thank you for your patience,
Zane

I was happy to see the response and realized that this issue needed a long term fix. Then I thought not to disturb asking for the update every time.

After a month of the last reply, on February 7, 2020; I got another reply from Facebook regarding the same issue. I was not asking for an update, why did they reply? I thought, maybe the fix is complete and they are now asking me for confirmation of the fix. I tapped on the notification and BOOM! It was a BOUNTY DECISION.

Bounty decision without a fix? Hmm, it was written at the end not to disclose the issue until the issue is fully resolved. The bounty was much beyond what I expected. I was thrilled and excited. In fact, Super EXCITED.

Press enter or click to view image in full size
From Informative to critical Bug

Along with the bounty, there was additional information saying that a framework change of the back-end was going on.

I asked them an additional question about when is the fix expected to complete. They replied, we do not have a solid time frame but it could take until March.

But, sadly the Coronavirus Pandemic broke out globally and affected the United States the most. So the fix was much delayed. It took until July 7, 2020 when I got the message for the confirmation of the fix.

Timeline of the Report:

October 13, 2019: Initial Report Sent
October 15, 2019: Report marked as Informative and Closed
October 22, 2019: Report re-opened by Facebook Security Team
November 4, 2019: Report Triaged
February 7, 2020: $6000 Bounty rewarded without the fix
July 7, 2020: Confirmation of Fix

Thank you for taking time to read my article. Have a great day!

You can follow me on Facebook or Twitter if you would like to stay connected with me.

Below is the coverage from the press regarding this issue.

Instagram kept deleted photos and messages on its servers for more than a year
A security researcher found that Instagram was keeping copies of photos and direct messages he'd deleted from his…

www.theverge.com

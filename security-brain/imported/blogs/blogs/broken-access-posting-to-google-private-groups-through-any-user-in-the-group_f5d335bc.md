---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-27_broken-access-posting-to-google-private-groups-through-any-user-in-the-group.md
original_filename: 2019-04-27_broken-access-posting-to-google-private-groups-through-any-user-in-the-group.md
title: 'Broken Access: Posting to Google private groups through any user in the group'
category: blogs
detected_topics:
- access-control
- command-injection
- mfa
tags:
- imported
- blogs
- access-control
- command-injection
- mfa
language: en
raw_sha256: f5d335bc704689a66cffa960369b469ce101e40eed6d4327532c7a510e8680e4
text_sha256: f26cdf771bbe6bc8063d96d8f6b328f446807e0b7b164de53044a52c411db714
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Broken Access: Posting to Google private groups through any user in the group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-27_broken-access-posting-to-google-private-groups-through-any-user-in-the-group.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f5d335bc704689a66cffa960369b469ce101e40eed6d4327532c7a510e8680e4`
- Text SHA256: `f26cdf771bbe6bc8063d96d8f6b328f446807e0b7b164de53044a52c411db714`


## Content

---
title: "Broken Access: Posting to Google private groups through any user in the group"
url: "https://medium.com/@elberandre/broken-access-posting-to-google-private-groups-through-any-user-in-the-group-3becfa818894"
authors: ["Elber Andre (@Elber333)"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2019-04-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5281
scraped_via: "browseros"
---

# Broken Access: Posting to Google private groups through any user in the group

Broken Access: Posting to Google private groups through any user in the group
Elber Andre
Follow
4 min read
·
Apr 28, 2019

134

(My main goal in this post is to show tricks for bug hunters, today I’m showing Email Spoofing)

These days I reported a bug in Google Groups to Google, but received the following response:

“Thanks for reporting! We think the issue might not be severe enough for us to track it as a security bug.”

So I decided to share this trick with you, I think it can be useful for some people.

*Remembering that the “Bug” has not been fixed.

Google Groups:

Google Groups allows you to create and participate in online forums and email-based groups with a rich experience for community conversations.

To create a group we need to fill in some information.
1- Group Name (Ex: testpocgoogle)
2- Email of the group (Ex: testpocgoogle@googlegroups.com)
3- Description of the group
And also some basic permissions (Ex: Only members of the group can post something [Standard])

Press enter or click to view image in full size

When posting something in the group, all users receive feedback in the email, containing the content of the post,
in this email we also found some kind of “help” from Google groups.

Press enter or click to view image in full size

Among them “To post to this group, send email to testpocgoogle@googlegroups.com.”

Get Elber Andre’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So we can: Post to the group just by sending an email to testpocgoogle@googlegroups.com
or stop receiving notifications by sending an email to testpocgoogle+unsubscribe@googlegroups.com.

Unauthorized posts:

Let’s cite as an example the user “elbtests acc - elbtestsacc@gmail.com”, he is in the group, so he can make and comment posts.
Hacker knows that this user is in the group but does not have access to his account (Acc elbtestsacc@gmail.com).
Knowing that posts can be made via email, the hacker decides to try Email Spoofing.

Spoofing Email

Email spoofing is the creation of email messages with a forged sender address.

To perform this “Attack” I used the site emkei.cz.

Press enter or click to view image in full size

By filling in the correct information and submitting the request, the group admin will receive the post marked
as if it had been made by the actual user of the group, but with those settings I saw that she was falling into Spam.

Bypass the spam filter.

To make the post fall directly into the group, I used an SMTP server of my own with some more settings that they should not have on the site I used.
(like SPF and dkim with 2048 key, since 1024 usually went to spam in some tests)

[Video Demoted at the beginning of the post]

Now we can see that the email was not marked as spam, and was posted directly in the group by my user, and for this I just needed the email, no passwords or 2FA bypass.

And the email with the content of the post was sent to the email of the users that follow that group.

(in the video we can see a notification in the tab of gmail after the POST in the form has been sent.)

Press enter or click to view image in full size
Additional Information:

In addition to posting, the hacker can also unsubscribe from the user in that group.
The posting made by the hacker stays in the victim’s logs if she logs in to your profile and sees your “Recent Activities” post that she did not do
will be there.
If the Admin sees the email in the Spam tab, or in the group itself and clicks ban user, the user “victim” will be banned without doing anything.
Google hides users’ email, but they can be found in your gmail when you receive feedback from posts.

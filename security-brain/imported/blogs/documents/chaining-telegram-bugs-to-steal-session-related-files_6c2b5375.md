---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-25_chaining-telegram-bugs-to-steal-session-related-files.md
original_filename: 2022-08-25_chaining-telegram-bugs-to-steal-session-related-files.md
title: Chaining Telegram bugs to steal session-related files.
category: documents
detected_topics:
- command-injection
- path-traversal
- mobile-security
tags:
- imported
- documents
- command-injection
- path-traversal
- mobile-security
language: en
raw_sha256: 6c2b5375b616ca25217d3b687bcf2da7e655a8520d085af4836fe55a4ecaa28a
text_sha256: eae028db7bc51e7115a2d1d28ca255d548c758320b3a1fd93075206c645df1f0
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Telegram bugs to steal session-related files.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-25_chaining-telegram-bugs-to-steal-session-related-files.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, mobile-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `6c2b5375b616ca25217d3b687bcf2da7e655a8520d085af4836fe55a4ecaa28a`
- Text SHA256: `eae028db7bc51e7115a2d1d28ca255d548c758320b3a1fd93075206c645df1f0`


## Content

---
title: "Chaining Telegram bugs to steal session-related files."
url: "https://dphoeniixx.medium.com/chaining-telegram-bugs-to-steal-session-related-files-c90eac4749bd"
authors: ["Sayed Abdelhafiz (@dPhoeniixx)"]
programs: ["Telegram"]
bugs: ["Arbitrary file read", "Android"]
publication_date: "2022-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2263
scraped_via: "browseros"
---

# Chaining Telegram bugs to steal session-related files.

Chaining Telegram bugs to steal session-related files.
Sayed Abdelhafiz
Follow
4 min read
·
Aug 25, 2022

130

1

We will discuss the chaining of two bugs on the telegram android application, which can make malicious applications steal internal telegram files, including the session.

Sharing Activity

Almost all messengers have an activity that can receive any type of content like images, videos, text, etc.. and forward that content to chat or a thread on the application.

For example, Open the gallery on your phone, select a photo, and click on “Share it” or “Open With”, and you will see a popup with some of the applications on your device, those applications appear because all of them have a sharing activity that can receive images, exactly like a telegram:

As we can see in <intent-filter>, LaunchActivity in telegram can handle data with mimeType: video/*, image/*, text/plain, */*

Turn feature into security bug

Before diving into how this feature can go on the wrong way, we have to figure out the intent that is being sent when sharing an image to the application or what happens on your gallery application when you chose to share an image, here is an example for that intent:

The above code shows you what exactly is being sent to any shared activity, it sends the Uri of the file, but not the file content, and when LaunchActivity in telegram receives that Uri the file will be opened in the telegram’s context and will show the user a chats list activity to let the user select a chat to send the file to.

Now, It is a nice idea to trick the telegram application, and instead of sending a Uri of file in the sd card, we will send a path of an internal file on telegram.

Can you bypass it?

the above code, orders the telegram application to share /data/data/org.telegram.messenger/shared_prefs/userconfing.xml file to chat, but when running this code, telegram shows a toast with a message: Unsupported content.

it seems I’m that telegram check if the Uri refers to internal file by AndroidUtilities.isInternalUri Method:

I was trying to bypass this method for a week, without any results. Hmmm, sit back to see the big picture and relax, we don’t have to bypass that method to complete the attack!

Get Sayed Abdelhafiz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How telegram actually opens the file from the Uri did we send it? actually, after the Uri pass isInternalUri method will forward to copyFileToCache method, its name is clear, and it will copy the file to the cache, but how?

It opens the Uri by openInputStream, and it means that it can open Uri refers to the provider, it gives us the option to send the provider Uri instead of a file scheme Uri.

I checked the telegram providers and found a provider that can refer to an internal telegram file and pass the isInternalUri check.

the openFile is method in the provider takes the file path from final_path parameter and returns ParcelFileDescriptor of that file.

the following Provider Uri content://org.telegram.messenger.notification_image_provider/msg_media_raw/1/test.txt?final_path=/data/data/org.telegram.messenger/shared_prefs/userconfing.xml refers to /data/data/org.telegram.messenger/shared_prefs/userconfing.xml

And it passes the isInternalUri method!

The above code will force the telegram to open an internal file and share it to a chat, but to which chat? It still requires a heavy interaction which forces the user to select the attacker chat. Impossible.

A new feature, but a bad implementation.

ChooserTargetService is a new feature that came to Android API 7 years ago. In the popup that shows you all applications you can send your file to, something new came to that list which is a list of specific people on the. specific applications, you can send them the file directly by clicking on their pictures.

To implement this feature in your application, you will implement a new service that extends ChooserTargetService and it will be used to tell the os about the items or people to list on that popup:

And In the Sharing activity, you will have to handle a new extra, and this extra will be that chat id or thread id to send the content directly to it.

But this implementation lacks security. How the SharingActivity knows if the direct share intent was populated or not? If any application sends a sharing intent to the activity and set the extra that carries the target chat id to any chat id, the application will send the file directly to that chat without user interaction!

Telegram had the same issue, by sending dialogId extra with any chat id to the telegram application, it will send the message or file directly to that chat without any more user interaction.

Final Exploit

The above code will exploit the two bugs and send /data/data/org.telegram.messenger/shared_prefs/userconfing.xml file to 100000000 chat id directly without user interaction, to reproduce the full exploit, downgrade your telegram to 5.4.0.

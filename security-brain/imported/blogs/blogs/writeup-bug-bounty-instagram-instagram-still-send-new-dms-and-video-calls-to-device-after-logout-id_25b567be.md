---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-16_writeupbug-bountyinstagram-instagram-still-send-new-dms-and-video-calls-to-devic.md
original_filename: 2020-04-16_writeupbug-bountyinstagram-instagram-still-send-new-dms-and-video-calls-to-devic.md
title: '[Writeup][Bug Bounty][Instagram] Instagram Still Send New DMs and Video Calls
  to Device After Logout [ID][EN]'
category: blogs
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- blogs
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 25b567be04ba0c42e301f70e947fce4ba7349f2c09f9a92eaf1465bbdac3d3c4
text_sha256: 5c33b4e104692a9e77c872a55ec3335317d73868433b037b426302e103408823
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# [Writeup][Bug Bounty][Instagram] Instagram Still Send New DMs and Video Calls to Device After Logout [ID][EN]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-16_writeupbug-bountyinstagram-instagram-still-send-new-dms-and-video-calls-to-devic.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `25b567be04ba0c42e301f70e947fce4ba7349f2c09f9a92eaf1465bbdac3d3c4`
- Text SHA256: `5c33b4e104692a9e77c872a55ec3335317d73868433b037b426302e103408823`


## Content

---
title: "[Writeup][Bug Bounty][Instagram] Instagram Still Send New DMs and Video Calls to Device After Logout [ID][EN]"
page_title: "[Writeup][Bug Bounty][Instagram] Instagram Still Send New DMs and Video Calls to Device After Logout [ID][EN] | Home"
url: "https://fadhilthomas.github.io/post/facebook-white-hat-01/"
final_url: "https://fadhilthomas.github.io/post/facebook-white-hat-01/"
authors: ["Muhammad Thomas Fadhila Yahya (@fadhilthomas)"]
programs: ["Meta / Facebook"]
bugs: ["Session management issue"]
bounty: "750"
publication_date: "2020-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4651
---

[Home](https://fadhilthomas.github.io/) » [Posts](https://fadhilthomas.github.io/post/)

# [Writeup][Bug Bounty][Instagram] Instagram Still Send New DMs and Video Calls to Device After Logout [ID][EN]

April 16, 2020 · 2 min · fadhilthomas

Table of Contents

  * Impact
  * Steps to Reproduce
  * Timeline

![alt text](/facebook01/instagram_logo.png)

Setelah pengguna melakukan _logout_ akunnya, _session_ seharusnya di _invalidate_ untuk menghentikan aksi yang membutuhkan otentikasi seperti menerima notifikasi pesan yang masuk. Pada postingan ini membahas tentang Instagram yang menampilkan notifikasi pesan masuk walaupun pengguna telah mengakhiri _session_ akunnya.

> _After the user logs out of his account, the session should be invalidated to stop actions that require authentication such as receiving notifications of incoming messages. This post is about Instagram, which shows incoming message notifications even though the user has ended his account session._

* * *

## Impact#

_Attacker_ masih bisa mendapatkan notifikasi pesan yang masuk ke akun korban walaupun _session_ nya sudah diakhiri.

> _The attacker can still get notification of messages that go to the victim’s account even though the session has ended._

* * *

## Steps to Reproduce#

  * _Attacker_ berhasil masuk ke akun korban.

> _The attacker has succeeded log in into the victim’s account._

  * Korban mengetahui bahawa ada orang lain yang telah masuk ke akunnya.

> _The victim knows that someone else has entered her account._

  * Korban ingin mengakhiri session dari _attacker_ dengan cara membuka pengaturan Aktifitas Login pada Pengaturan.

> _The victim wants to end the session from the attacker by opening the Login Activity setting in Settings._

  * _Session attacker_ berhasil diakhiri.

> _The attacker’s session has successfully ended._

  * Walaupun _attacker_ sudah berhasil keluar dari akun korban, tetapi apabila ada pesan yang masuk ke akun korban, perangkat _attacker_ masih mendapatkan notifikasi pesan yang masuk.

> _Although the attacker has logged out from the victim’s account, if there is a message that enters the victim’s account, the attacker’s device still gets a notification of the incoming message._

  * Mungkin hal ini terjadi karena, token FCM dari _device attacker_ masih terdaftar sehingga _device attacker_ masih menerima notifikasi pesan baru.

> _Maybe this happened because FCM tokens from the device attacker were still registered so that the device attacker was still receiving new message notifications._

![alt text](/facebook01/facebook_bounty_01.png)

* * *

## Timeline#

  * 15 Nov 2019 : Melaporkan ke Facebook.
  * 19 Nov 2019 : Facebook menerima laporan dan meminta informasi lebih detil.
  * 27 Jan 2020 : Facebook menyatakan laporan valid dan memberikan hadiah $750.

  * [bugbounty](https://fadhilthomas.github.io/tags/bugbounty/)
  * [instagram](https://fadhilthomas.github.io/tags/instagram/)
  * [writeup](https://fadhilthomas.github.io/tags/writeup/)
  * [facebook](https://fadhilthomas.github.io/tags/facebook/)

[« Prev Page  
[Writeup][Bug Bounty][Tokopedia] Manipulate Other User’s Cart and Wishlist on Tokopedia [EN]](https://fadhilthomas.github.io/post/bug-bounty-tokopedia-03/) [Next Page »  
[Writeup][Bug Bounty][Tokopedia] Information Disclosure of Sensitive Information pada Verification Login Page [ID]](https://fadhilthomas.github.io/post/bug-bounty-tokopedia-02/)

[](https://twitter.com/intent/tweet/?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f&hashtags=bugbounty%2cinstagram%2cwriteup%2cfacebook)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f&title=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d&summary=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d&source=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f)[](https://reddit.com/submit?url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f&title=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d)[](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f)[](https://api.whatsapp.com/send?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d%20-%20https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f)[](https://telegram.me/share/url?text=%5bWriteup%5d%5bBug%20Bounty%5d%5bInstagram%5d%20Instagram%20Still%20Send%20New%20DMs%20and%20Video%20Calls%20to%20Device%20After%20Logout%20%5bID%5d%5bEN%5d&url=https%3a%2f%2ffadhilthomas.github.io%2fpost%2ffacebook-white-hat-01%2f)

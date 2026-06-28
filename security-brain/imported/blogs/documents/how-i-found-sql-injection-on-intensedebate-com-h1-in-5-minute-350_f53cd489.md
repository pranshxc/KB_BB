---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-05_how-i-found-sql-injection-on-intensedebatecom-h1-in-5-minute-350.md
original_filename: 2021-05-05_how-i-found-sql-injection-on-intensedebatecom-h1-in-5-minute-350.md
title: How I Found Sql Injection on intensedebate.com (h1) in 5 minute $350
category: documents
detected_topics:
- sqli
- command-injection
tags:
- imported
- documents
- sqli
- command-injection
language: en
raw_sha256: f53cd4896e5f58ac16a0d208a7276a5663ff689cfb84d10da461ee8d8df476e2
text_sha256: ccd256db795d76471eee330dc91f59c2e69a2a55669f684064a8417464e6cd2c
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found Sql Injection on intensedebate.com (h1) in 5 minute $350

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-05_how-i-found-sql-injection-on-intensedebatecom-h1-in-5-minute-350.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `f53cd4896e5f58ac16a0d208a7276a5663ff689cfb84d10da461ee8d8df476e2`
- Text SHA256: `ccd256db795d76471eee330dc91f59c2e69a2a55669f684064a8417464e6cd2c`


## Content

---
title: "How I Found Sql Injection on intensedebate.com (h1) in 5 minute $350"
url: "https://ahmadaabdulla.medium.com/how-i-found-sql-injection-on-intensedebate-com-h1-in-5-minute-350-a36c2890882d"
authors: ["Ahmad A Abdulla (@lu3ky13)"]
programs: ["Automattic"]
bugs: ["SQL injection"]
bounty: "350"
publication_date: "2021-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3675
scraped_via: "browseros"
---

# How I Found Sql Injection on intensedebate.com (h1) in 5 minute $350

Ahmad A Abdulla
 highlighted

How I Found Sql Injection on intensedebate.com (h1) in 5 minute $350
Ahmad A Abdulla
Follow
2 min read
·
May 4, 2021

490

2

If you want to learn bug bounty in an easy and affordable way, visit our website. The course is taught in English.

https://www.cybershield.krd/Courses/Course/28

I’m here to tell you how I found SQL injection on this website at HackerOne just in 5 minutes and I got 350$ without any tools to recon

just I used my mind and google search after 2 or 3 minutes I found a zip on a website like https://intensedebate.com/intensedebate.zip I downloaded this zip I saw source code of some file PHP like this

Press enter or click to view image in full size

<img src=”http://intensedebate
.com/midimages/<?php echo get_usermeta($user_ID, ‘id_userID’);?>” alt=”[Avatar]” class=”idwp-avatar” />
<h3 class=”idwp-floatnone”><?php printf(__(‘Synchronizing as %s’, ‘intensedebate
‘), ‘<a href=”http://www.intensedebate
.com/people/'.get_usermeta($user_ID, ‘id_username’).’”>’.get_usermeta($user_ID, ‘id_username’).’</a>’); ?></h3>
<p class=”idwp-floatnone”><a href=”http://www.intensedebate
.com/userDash"><?php _e(‘Dashboard’, ‘intensedebate
‘); ?></a> | <a href=”http://www.intensedebate
.com/editprofile”><?php _e(‘Edit profile’, ‘intensedebate
‘); ?></a></p>
<p><a href=”options-general.php?id_settings_action=user_disconnect” id=”id_user_disconnect”><?php _e(‘Disconnect from IntenseDebate
‘) ?></a></p>
<span class=”idwp-clear”></span>
<p class=”idwp-nomargin”><?php _e(‘All WordPress comments are now synchronized with the IntenseDebate
account above. <a href=”http://www.intensedebate
.com/wordpress#userSync”>Read more here</a>.’, ‘intensedebate
‘); ?></p>
<p></p>

Get Ahmad A Abdulla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

after I read source code PHP I saw too many errors on the URL and source code and I found this URL

https://www.intensedebate.com/js/importStatus.php?acctid=1

and I used sqlmap to dump the database i saw it’s done soo nice

Press enter or click to view image in full size

my report https://hackerone.com/reports/1069561

lu3ky13 is on @buymeacoffee! 🎉

You can support by buying a coffee ☕️ here —
https://www.buymeacoffee.com/lu3ky13

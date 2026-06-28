---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-01_you-can-add-extra-zeroes-xss-bypass-on-a-private-bug-bounty-program.md
original_filename: 2023-10-01_you-can-add-extra-zeroes-xss-bypass-on-a-private-bug-bounty-program.md
title: You can add extra zeroes. XSS bypass on a private bug bounty program
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 4ce0081cafc6c3f9b327e5b249b9e96814e821fbe20231973b8e3a0d48202cd7
text_sha256: c79867ebf6eecbe2cec9bed177e6ab5a33aa7015df0847c133b45e5ec551c595
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# You can add extra zeroes. XSS bypass on a private bug bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-01_you-can-add-extra-zeroes-xss-bypass-on-a-private-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `4ce0081cafc6c3f9b327e5b249b9e96814e821fbe20231973b8e3a0d48202cd7`
- Text SHA256: `c79867ebf6eecbe2cec9bed177e6ab5a33aa7015df0847c133b45e5ec551c595`


## Content

---
title: "You can add extra zeroes. XSS bypass on a private bug bounty program"
url: "https://medium.com/@snoopy101/you-can-add-extra-zeroes-xss-bypass-on-a-private-bug-bounty-program-77440495e448"
authors: ["snoopy (@snoopy101101)"]
bugs: ["Reflected XSS"]
bounty: "500"
publication_date: "2023-10-01"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 734
scraped_via: "browseros"
---

# You can add extra zeroes. XSS bypass on a private bug bounty program

Top highlight

You can add extra zeroes. XSS bypass on a private bug bounty program
snoopy
Follow
2 min read
·
Oct 1, 2023

509

10

Hi incredible hackers. I got a private invite, and got curious about the program, so I signed up into the main website and started clicking around and using all functions.

I found this endpoint in which the value of “name” parameter was reflecting inside the “iframe” tag.

Press enter or click to view image in full size
Press enter or click to view image in full size

Fortunately the " character wasn’t being encoded, so I was able to get out of the src.

Problem

( and ` characters were not allowed and causing a 403 error.

test" onload=alert(origin) --> 403
test" onload=print`` --> 403
test" onload=alert origin) --> 200

I played with it for a few minutes, but I couldn’t exploit it.

Cure

I texted my buddy 0xrz who is a true monster when it comes to hacking.

Get snoopy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I sent him the endpoint and…

Press enter or click to view image in full size
savage

Payload:

" onload=alert&#0000000040origin) value="

He told me what is going on here, and I’m writing it down here.

JS accepts decimal Unicode characters, so we can write &#40 instead of (. Check it: http://www.endmemo.com/unicode/ascii.php.

But this payload was giving us a 403 page again, and it wasn’t a bypass in this case.

You can add extra zeroes after &# and it will be treated as &#40 which is (. Isn’t JS amazing?
Report & Bounty:
Press enter or click to view image in full size
Make sure that you follow 0xrz:
JavaScript is not available.
Edit description

twitter.com

Reach me at:

LinkedIn:

https://www.linkedin.com/in/ali-imani-2a896a266/

Twitter:

https://twitter.com/snoopy101101

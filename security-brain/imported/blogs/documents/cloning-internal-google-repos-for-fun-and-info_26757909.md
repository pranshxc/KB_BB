---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-16_cloning-internal-google-repos-for-fun-and-info_2.md
original_filename: 2022-09-16_cloning-internal-google-repos-for-fun-and-info_2.md
title: Cloning internal Google repos for fun and… info?
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 26757909acb80493de2692f5608c6be9798a5e0ef4904f15b36181e733995510
text_sha256: dfc9580e0f8886c69b3027e57d23c8aba6c163a0a4655d4cbf286fdfe0dffa47
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Cloning internal Google repos for fun and… info?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-16_cloning-internal-google-repos-for-fun-and-info_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `26757909acb80493de2692f5608c6be9798a5e0ef4904f15b36181e733995510`
- Text SHA256: `dfc9580e0f8886c69b3027e57d23c8aba6c163a0a4655d4cbf286fdfe0dffa47`


## Content

---
title: "Cloning internal Google repos for fun and… info?"
url: "https://medium.com/@lukeberner/cloning-internal-google-repos-for-fun-and-info-bf2c83d0ae00"
authors: ["Luke Berner"]
programs: ["Google"]
bugs: ["Broken authorization"]
publication_date: "2022-09-16"
added_date: "2022-09-19"
source: "pentester.land/writeups.json"
original_index: 2160
scraped_via: "browseros"
---

# Cloning internal Google repos for fun and… info?

Cloning internal Google repos for fun and… info?
Luke Berner
Follow
5 min read
·
Sep 16, 2022

112

3

This is a vulnerability I reported back in May, 2021

As a normal bug-bounty exercise, I was checking Google subdomains to see if I could find anything interesting. One of them caught my attention: googlesource.com

As the name suggests, it hosts Google code. That's ok, mostly their open source projects or forked ones. I proceeded to list all subdomains to see if I could spot anything interesting; for example, when looking for Google stuff, the word 'corp' always catches my attention, because it may refer to their *.corp.google.com world.

Quickly checked the subdomains gathered (Tomnomnom's assetfinder is a great resource for this), and unfortunately found no 'corp'. However, I found one that seemed interesting:

Press enter or click to view image in full size
Anything with the word ‘internal’ should at least be given a shot, right?

So here is when I started learning about googlesource.com and how it works. It's divided into two:

project_name.googlesource.com, where all repos are listed (as you can see in android.googlesource.com/),
project_name-review.googlesource.com, where Gerrit comes into play.

Gerrit is Google’s code review and project management tool for Git based projects. To every project_name.googlesource.com, I learnt that you can add a -review to access the Gerrit version. Continuing with Android's example, its Gerrit URL is https://android-review.googlesource.com/

Press enter or click to view image in full size
As any code review / git tool, you can see changes, comments, commits, etc.

When opening chrome-internal.googlesource.com, I was greeted with a PERMISSION_DENIED error page. Makes sense, right? Like it or not, its URL says it's internal related.

Press enter or click to view image in full size

But when doing bug-bounty, you have to be curious and follow every lead. So naturally I followed my instinct and pressed Sign In. For a moment I was shocked that it didn't mandate a @google.com account in the Login form (as many other internal Google services do). So I selected my personal @gmail.com email and boom, I was in.

Press enter or click to view image in full size
List of repos listed in chrome-internal.googlesource.com

Lots of things here, but still I wasn't sure if it was really internal or not. Next I went to its Gerrit version (chrome-internal-review) and was able to access project's groups information, containing data about internal mail-lists and also Googlers (full name, photo, @google.com email).

Press enter or click to view image in full size
Information about chrome-internal groups & Googlers

To be fair, at this point I thought this could be something. What I normally do in these cases is: report it, and continue poking to see if I can escalate it even more (or until I get the famous “Nice catch!”).

Two things also hinted me it could be really internal:

Some links (e.g: “Report a bug”), asked for a @google.com email to continue,
According to gerrit-guide, this subdomain is intended for Googlers only: "Go to http://google.com/ and verify you are logged into your @google.com account."

So I went ahead and filed a security vulnerability report before continuing.

Press enter or click to view image in full size
Yep, 33 replies. You see where this is going.

As you can read in the above report, I was already trying to access changes or get more information. Endpoints hinted I had no read access to changes, but they were there.

At the moment I was not able to see anything change-related in Gerrit, but was able to visit all repos. Some of them instantly seemed interesting, listing internal *.corp.google.com subdomains and read-only credentials as well:

Press enter or click to view image in full size

I wanted to have a way to search for certain keywords (passwords, internal IPs, apikeys, corp.google.com subdomains, etc) through all code, quick.

Get Luke Berner’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So after I submitted this new info and waited for an answer, I coded a quick script to clone all repos and branches. But not just for this subdomain, for all *.googlesource.com subdomains. My guess was that, if this subdomain had internal/sensitive info, then there might be others as well.

To give a few examples, I was also able to grep for buckets (storage.googleapis.com) URLs which led me to terraform files for GKE internal services.

Interesting thing about these buckets is that, even though they are private, if you have a full link to a file you can download it without any auth ;)

Press enter or click to view image in full size
Private bucket’s files

Was able to get lots of internal information as you can see below:

*.corp.google.com subdomains (internal and external ones),
internal IPs (10.0.0.0/8, 172.16.0.0/12),
files hosted in Google private buckets,
config files with staging & prod credentials,
deploy scripts, containing build steps and credentials (found in private buckets),
deploy templates containing credentials as well (found in private buckets)
Press enter or click to view image in full size
Had to remove a bit of sensitive content

Without hesitation I re-submitted this extra info and waited. I felt like this might have been enough.

After some back and forth providing all the evidence found, got the long-awaited "Nice catch!" message:

Press enter or click to view image in full size
feelsgood.jpg

Got a few learnings from this report. One of them is that Google Security team receives lots of reports per day, and they have a limited time to spend (I remember reading something like 8 mins?) per report. So it's best to send all information organized and not many messages containing part of the information. Also, like the ones posted above, a picture may be worth a thousand words ;)

In addition, if you see a PERMISSION_DENIED or Login screen, make sure the authentication is well placed (maybe they allow any auth or even yourself to register).

Another thing this vulnerability helped me learn was a lot about how *.googlesource.com and Gerrit work. As a matter of fact a year after this vulnerability, I reported another one related to Gerrit; waiting on Google's OK to post write-up :)

Timeline:

16.05.2021: Vulnerability reported.
17.05.2021: Report triaged.
20.05.2021: Sent more information
01.06.2021: Received "Nice catch!"
01.06.2021: VRP reward received
07.06.2021: Sent extra info about private buckets' files exposed on other googlesource.com subdomains
22.06.2021: VRP reward #2 received
11.04.2022: Google confirms all bugs have been fixed

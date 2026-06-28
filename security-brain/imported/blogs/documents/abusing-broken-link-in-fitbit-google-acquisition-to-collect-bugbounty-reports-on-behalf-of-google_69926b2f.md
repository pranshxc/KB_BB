---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-16_abusing-broken-link-in-fitbit-google-acquisitionto-collect-bugbounty-reports-on-.md
original_filename: 2022-09-16_abusing-broken-link-in-fitbit-google-acquisitionto-collect-bugbounty-reports-on-.md
title: Abusing Broken Link In Fitbit (Google Acquisition)To Collect BugBounty Reports
  On Behalf Of Google !
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 69926b2f74d031fbb203ba60076b6dd1dd7cd309ca31bdae56474f6a0d5edf5b
text_sha256: 4cd0d0043d5f279fe967a8af4709dd14a79cb99398a40d7a2f0cdf58044bb384
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Broken Link In Fitbit (Google Acquisition)To Collect BugBounty Reports On Behalf Of Google !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-16_abusing-broken-link-in-fitbit-google-acquisitionto-collect-bugbounty-reports-on-.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `69926b2f74d031fbb203ba60076b6dd1dd7cd309ca31bdae56474f6a0d5edf5b`
- Text SHA256: `4cd0d0043d5f279fe967a8af4709dd14a79cb99398a40d7a2f0cdf58044bb384`


## Content

---
title: "Abusing Broken Link In Fitbit (Google Acquisition)To Collect BugBounty Reports On Behalf Of Google !"
url: "https://infosecwriteups.com/abusing-broken-link-in-fitbit-google-acquisition-to-collect-bugbounty-reports-on-behalf-of-google-5885a556eb7c"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Google"]
bugs: ["Broken link hijacking"]
publication_date: "2022-09-16"
added_date: "2022-09-17"
source: "pentester.land/writeups.json"
original_index: 2162
scraped_via: "browseros"
---

# Abusing Broken Link In Fitbit (Google Acquisition)To Collect BugBounty Reports On Behalf Of Google !

Abusing Broken Link In Fitbit (Google Acquisition)To Collect BugBounty Reports On Behalf Of Google !
Jayateertha Guruprasad
Follow
2 min read
·
Sep 16, 2022

64

Press enter or click to view image in full size
Pic of Me tracking all acquisitions of Google regularly 🤑

I usually track acquisitions of websites for which I am hunting bugs regularly.

I knew that Fitbit acquisition has been completed by Google and is eligible for bounty in GoogleVRP platform.

But, I previously remember that, Fitbit was also part of some other bugbounty platform before Google’s acquisition, So wanted to make sure that I am reporting to correct platform.

Hence, I made a simple Google search and found this broken link in official website of Fitbit in the 1st page of Google result.

Now, as the reported vulnerability is fixed, you can visit the archive to see how it was, when I reported.

It means that, although the acquisition is fully complete by Google, The website mentions that vulnerabilities found in Fitbit should be reported through — Bugcrowd.

Although Bugcrowd may not host a malicious page at this broken link and start collecting Bugbounty reports from security researchers, By following zero trust for better security — It’s suggested not to trust any entity blindly whether internal or external !

Impact:

Attacker might create a new company in bugcrowd with that url and may take vulnerability reports from actual reported and exploit.

Bugcrowd platform itself may exploit this. (Although they might not, there is still a possibility)

Hence, created a nice report and submitted via GoogleVRP platform, This was triaged to Trust & Safety team, as the reported issue was identified as an Abuse Risk.

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was hoping for a good bounty, but unfortunately I was awarded with only honorable mentions, But as I am already in Google’s Hall Of Fame (Leaderboard), This wouldn’t be much beneficial for me.

As this is my first abuse risk report not a usual vulnerability report, I asked the team how the severity was assessed and evaluated to learn more.

Press enter or click to view image in full size

Timeline:

Reported — Aug 10 2022

Triaged — Aug 11 2022

Accepted — Aug 16 2022

Fixed — Sep 9 2022

Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.
From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!

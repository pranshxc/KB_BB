---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-11_biological-inspiration.md
original_filename: 2022-08-11_biological-inspiration.md
title: Biological Inspiration
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: f6568373edf688b2835ee15447353cd38fba94dda829eaeb0c028e6a3e43dfa0
text_sha256: 74e9fedb7a8a548360faa1d44547b08b6bea82673f858fc99dca5990b11cc60a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Biological Inspiration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-11_biological-inspiration.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `f6568373edf688b2835ee15447353cd38fba94dda829eaeb0c028e6a3e43dfa0`
- Text SHA256: `74e9fedb7a8a548360faa1d44547b08b6bea82673f858fc99dca5990b11cc60a`


## Content

---
title: "Biological Inspiration"
page_title: "Bahruz Jabiyev - Biological Inspiration"
url: "https://bahruz.me/posts/biological-inspiration"
final_url: "https://bahruz.me/posts/biological-inspiration"
authors: ["Bahruz Jabiyev (@BahruzJabiyev)", "Steven Sprecher (@StevenSprecher)", "Anthony Gavazzi", "Tommaso Innocenti (@innotommy)", "Kaan Onarlioglu", "Engin Kirda"]
bugs: ["HTTP request smuggling", "DoS"]
publication_date: "2022-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2330
---

![Site avatar](https://spaces-cdn.owlstown.com/blobs/07l9q8hcx8scw9a2pf9v5xr9qzj9)

Bahruz Jabiyev

PhD in Cybersecurity

* * *

jabiyev.bahruz@gmail.com 

* * *

[Twitter](https://twitter.com/bahruzjabiyev)

[Github](https://github.com/bahruzjabiyev)

[Google Scholar](https://scholar.google.com/citations?user=ql33eqkAAAAJ)

[LinkedIn](https://www.linkedin.com/in/bahruz-jabiyev/)

* * *

# Biological Inspiration

* * *

September 08, 2022 

* * *

Couple of weeks ago, I presented a [paper](https://bahruz.me/publications/11844.pdf) in USENIX Security conference. The paper was about HTTP/2-to-HTTP/1 conversion anomalies and their security implications. When we started the project, the idea was to fuzz and confuse HTTP/2 reverse proxies, in order to have them make abnormal conversions. For the mutation part, we did not want to constrain ourselves to string mutations on the frame contents and had the idea of stream-level mutations in the mind all along. To develop an approach for stream-level mutations, we took inspiration from living cells.

To give some context here, when a cell decides to synthesize a protein, the relevant fragment is cut from the DNA of the cell. The fragment is brought to a ribosome to have it turned into a chain of amino acids. For example, when a ribosome receives a nucleotide sequence of _GAGGAGGAG_ (_A_ is adenine, _G_ is guanine), it reads and converts three nucleotides at a time (e.g., _GAG_ to glutamate) and produces three glutamates.

💡 

GAGGAGGAG --> GAG-GAG-GAG --> glutamate-glutamate-glutamate

However, if the source DNA sequence has a nucleotide inserted by a mutation, this changes the reading frame. For example, an extra _G_ after the first _GAG_ would cause a different set of amino acids to be produced.

💡 

GAG**[G]** GAGGAG --> GAG-GGA-GGA-G --> glutamate-glycine-glycine

Biologists call this kind of mutation a "frameshift mutation" and it is known to be at the root of various disorders.

The frameshift mutations inspired us in three ways: 1) using healthy (i.e., syntactically and semantically valid) frame sequences as the base, 2) adding only healthy (i.e., syntactically valid) frames in mutations 3) inserting all available types of frames in sequences including terminating frames (e.g., GOAWAY, RST_STREAM), similar to how some amino acid insertions terminate reading earlier. These biologically inspired principles laid the foundation of our mutation strategy and we named our fuzzing tool in honor of frameshift mutations: **Frameshifter**. It is available on [Github](https://github.com/bahruzjabiyev/frameshifter).

When we used Frameshifter to test popular reverse proxies including popular CDN servers, we found that many of them are affected by abnormal conversions and attacks. We reported all the findings to the affected vendors and helped them reproduce the attacks. Some of the vendors assigned CVEs, such as Golang team at Google (for the Query-of-Death attack) and Apache Traffic Server team (for the Request Blackholing attack). Some other vendors confirmed the findings and shared their plan for action.

* * *

Share 

  * [ ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fbahruz.me%2Fposts%2Fbiological-inspiration&text=Bahruz+Jabiyev+-+Biological+Inspiration "Twitter")
  * [ ](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fbahruz.me%2Fposts%2Fbiological-inspiration&t=Bahruz+Jabiyev+-+Biological+Inspiration "Facebook")
  * [ ](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fbahruz.me%2Fposts%2Fbiological-inspiration&title=Bahruz+Jabiyev+-+Biological+Inspiration "LinkedIn")
  * [ ](mailto:?body=https%3A%2F%2Fbahruz.me%2Fposts%2Fbiological-inspiration&subject=Bahruz+Jabiyev+-+Biological+Inspiration "Email")

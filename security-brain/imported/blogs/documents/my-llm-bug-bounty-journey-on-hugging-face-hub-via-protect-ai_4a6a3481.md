---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-11_my-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai.md
original_filename: 2024-05-11_my-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai.md
title: My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI
category: documents
detected_topics:
- supply-chain
- command-injection
tags:
- imported
- documents
- supply-chain
- command-injection
language: en
raw_sha256: 4a6a34817b30c8340ce40945beffca0ce5d93d02f0e113ac0dca931538d061ea
text_sha256: 4e955cc9c10ae0f8e5afdc76726b59c6ac04515506b6034f52017cbbe88ad2aa
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-11_my-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `4a6a34817b30c8340ce40945beffca0ce5d93d02f0e113ac0dca931538d061ea`
- Text SHA256: `4e955cc9c10ae0f8e5afdc76726b59c6ac04515506b6034f52017cbbe88ad2aa`


## Content

---
title: "My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI"
url: "https://medium.com/@zpbrent/my-llm-bug-bounty-journey-on-hugging-face-hub-via-protect-ai-9f3a1bc72c2e"
authors: ["Peng Zhou"]
programs: ["Hugging Face", "Protect AI"]
bugs: ["LLM", "Insecure deserialization", "RCE"]
bounty: "3,250"
publication_date: "2024-05-11"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 289
scraped_via: "browseros"
---

# My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI

Member-only story

My LLM Bug Bounty Journey on Hugging Face Hub via Protect AI
From Informative Rejection to Black Hat Briefing
Peng Zhou
Follow
8 min read
·
May 11, 2024

80

Press enter or click to view image in full size

I am writing this article to share my bug-bounty experiences for LLM/AI security, specifically for the LLM supply chain vulnerabilities I have disclosed across the third-party LLM libraries integrated into the Hugging Face hub (HF in short), which include the huggingface/transformers, PaddlePaddle/PaddleNLP, facebookresearch/mbrl-lib, and DLR-RM/stable-baselines3. The root cause of these vulnerabilities is the abuse of the risky pickle.loads functions that can be exploited from the Hugging Face’s demo codes. I have reported my findings to respective maintainers, some of which are disclosed via Protect AI (huntr.com), and have successfully rewarded $3250 bounties with 2 CVEs. I have also presented this class of bugs as a briefing at Black Hat Asia 2024. Despite the final results seeming encouraging, I will tell you the way to success is narrow and difficult.

The First Blood

Originally, my LLM bug bounty journey started from an AI Bug Bounty champion held by Protect AI (huntr.com) in August-September 2023. The target of this champion is huggingface/transformers. To participate in this champion, I first searched lots of risky Python function calls across the source code of the target and found that…

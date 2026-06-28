---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-17_adding-a-malicious-notebook-to-be-treated-like-a-trusted-notebook-in-google-cola.md
original_filename: 2020-01-17_adding-a-malicious-notebook-to-be-treated-like-a-trusted-notebook-in-google-cola.md
title: Adding a malicious notebook to be treated like a trusted notebook in Google
  Colab — 1337$
category: notes
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- notes
- access-control
- command-injection
- business-logic
language: en
raw_sha256: e72c2a3ec284c69591f020efaed20972c82f8d6020242ea3b0e184c11c687ad5
text_sha256: 4fbdc3abd26d75bede708e939843221ba7e7f659bbc3b81715908ed6e01fd467
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Adding a malicious notebook to be treated like a trusted notebook in Google Colab — 1337$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-17_adding-a-malicious-notebook-to-be-treated-like-a-trusted-notebook-in-google-cola.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e72c2a3ec284c69591f020efaed20972c82f8d6020242ea3b0e184c11c687ad5`
- Text SHA256: `4fbdc3abd26d75bede708e939843221ba7e7f659bbc3b81715908ed6e01fd467`


## Content

---
title: "Adding a malicious notebook to be treated like a trusted notebook in Google Colab — 1337$"
url: "https://medium.com/@raushanraj_65039/adding-a-malicious-notebook-to-be-treated-like-a-trusted-notebook-in-google-colab-1337-b84353a9f77"
authors: ["Raushan Raj (@raushan_rajj)"]
programs: ["Google"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "1,337"
publication_date: "2020-01-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4826
scraped_via: "browseros"
---

# Adding a malicious notebook to be treated like a trusted notebook in Google Colab — 1337$

Adding a malicious notebook to be treated like a trusted notebook in Google Colab — 1337$
Raushan Raj
Follow
2 min read
·
Jan 17, 2020

89

1

Introduction

When we try to execute any Google Colab notebook from GitHub repo like https://colab.research.google.com/github/raushanraj/poc_likethat/blob/master/test_simple_camera.ipynb

Google collab doesn't allow us to run any third party GitHub notebook directly, instead, it gives a warning.

Warning: This notebook was not authored by Google.
This notebook is being loaded from GitHub. It may request access to your data stored with Google, or read data and credentials from other sessions. Please review the source code before executing this notebook.

The colab.research.google.com allows notebooks from google trusted repository like “https://github.com/googlecolab” to run without any warning. Eg. https://colab.research.google.com/github/googlecolab/colabtools/blob/master/tests/simple.ipynb

Get Raushan Raj’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Also, When we execute a notebook from the drive, whenever there is a critical functionality like accessing the camera, voice, etc then google colab add a warning prompt, once accepted then only notebook can access the same after execution. Hence, there is the relevance of warning prompt here as it is a parameter to disable and enable some attributes.

Bypass

The bypass is to execute the notebook from any Github repository without any warning. So, by clicking open in the colab, the notebook got executed without prompt.

1. Create a new file in the public repository https://github.com/googlecolab/colabtools and generate a pull request.

https://github.com/googlecolab/colabtools/blob/219f1771d8c22fd6bec00926a9d07f7d66e724ac/notebooks/test_simple_camera.ipynb

2. Open the public notebook below https://colab.research.google.com/github/googlecolab/colabtools/blob/219f1771d8c22fd6bec00926a9d07f7d66e724ac/notebooks/test_simple_camera.ipynb

and execute the code, no warning will be prompted for the user as the repository(googlecolab) is trusted instead the code is malicious

Browser/OS:
Chrome/Firefox/Linux

Attack scenario:
1. Presenting a malicious notebook to the victim (as a trusted google notebook) with no warning message.
2. The code I have used in POC can capture victims' media like cameras, voices, etc if previously saved in the browser.

Reported on 2 Jan 2020
Fixed on 16 Jan 2020
Bounty Awarded on 17 Jan 2020

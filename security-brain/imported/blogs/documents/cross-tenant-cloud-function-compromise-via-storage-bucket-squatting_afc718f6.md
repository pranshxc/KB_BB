---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-20_cross-tenant-cloud-function-compromise-via-storage-bucket-squatting.md
original_filename: 2020-09-20_cross-tenant-cloud-function-compromise-via-storage-bucket-squatting.md
title: Cross-tenant Cloud Function compromise via storage bucket squatting
category: documents
detected_topics:
- command-injection
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- cloud-security
- supply-chain
language: en
raw_sha256: afc718f6c7865243aa09b1f10b2f17ba42f34da8f2a2b45a8bf7836e05739f07
text_sha256: 0a84bd26bf276cbadb4d73e70aa7651e6476066025bdf6ea2082067d9a5d6f5b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Cross-tenant Cloud Function compromise via storage bucket squatting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-20_cross-tenant-cloud-function-compromise-via-storage-bucket-squatting.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `afc718f6c7865243aa09b1f10b2f17ba42f34da8f2a2b45a8bf7836e05739f07`
- Text SHA256: `0a84bd26bf276cbadb4d73e70aa7651e6476066025bdf6ea2082067d9a5d6f5b`


## Content

---
title: "Cross-tenant Cloud Function compromise via storage bucket squatting"
page_title: "Cross-tenant Cloud Function compromise via storage bucket squatting | Anthony Weems"
url: "https://lf.lc/vrp/168991979/"
final_url: "https://amlw.dev/vrp/168991979/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["Cross-tenant vulnerability"]
bounty: "3,133.70"
publication_date: "2020-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4251
---

#  Cross-tenant Cloud Function compromise via storage bucket squatting 

September 20, 2020

### Vulnerability Details#

Google Cloud Functions accept code from users and build this code into a deployable container via Cloud Build. Before building, the code is uploaded to a cloud storage bucket whose name matches the format `gcf-sources-<numeric-project-id>-<location>` (e.g. `gcf-sources-928967777810-us-central1`).

When uploading user provided code to the gcf-sources bucket, the backend does not verify that the bucket owner matches the current project. As the bucket name is not a domain, nor does it contain the word Google, an attacker can register these scratch buckets for any target accounts.

### Attack Scenario#

An attacker can effectively “squat” bucket names for projects they expect might use Cloud Functions at some point in the future. Requirements for the attack:

  1. attacker must know the project ID of their victim
  2. victim must have no cloud functions in the target region
  3. attacker must create a bucket matching `gcf-sources-<numeric-project-id>-<location>`
  4. attacker must grant access to the bucket (e.g. grant allUsers the storage.buckets.list, storage.objects.get, storage.objects.list, and storage.objects.create permissions)

When the victim creates a Cloud Function, the backend will upload their code archive to the attacker-controlled bucket. The attacker can then download and view code from the victim account. Additionally, their Cloud Function will proceed with creation and work as expected.

Finally, the attacker can modify the victim’s function-source.zip archive and edit the code of the victim’s cloud function. This will not be deployed unless the victim performs a new deployment through the UI and does not notice the modification. In larger Cloud Functions, this should be trivial by injecting code either a malicious dependency or a snippet into a large file.

#### Attacker setup#

Create bucket matching victim numeric project ID:
  
  
  gsutil mb gs://gcf-sources-928967777810-us-central1
  gsutil iam ch "allUsers:admin" gs://gcf-sources-928967777810-us-central1
  

Wait until victim uploads code. Upload backdoor’d version of victim’s code to attacker bucket.

#### Victim setup#

Deploy any Cloud Function.

**Screenshot of the victim Cloud Function correctly deployed:** ![Screenshot of the victim Cloud Function correctly deployed](/assets/vrp/168991979-victim-setup.png)

#### Result#

**Screenshot of the attacker bucket showing source code from the victim:** ![Screenshot of the attacker bucket showing source code from the victim](/assets/vrp/168991979-source-exfil.png)

**Screenshot of the victim’s edit view after the attacker “backdoors” the function-source.zip file:** ![Screenshot of the victim&rsquo;s edit view after the attacker &ldquo;backdoors&rdquo; the function-source.zip file](/assets/vrp/168991979-victim-edit.png)

**Screenshot showing simple shell as a result of backdoor’d function:** ![Screenshot showing simple shell as a result of backdoor&rsquo;d function](/assets/vrp/168991979-shell.png)

### Timeline#

  * 2020-09-20: Issue reported to Google VRP
  * 2020-09-22: Issue triaged
  * 2020-09-22: Internal bug report filed
  * 2020-09-29: VRP issued reward ($3133.70)

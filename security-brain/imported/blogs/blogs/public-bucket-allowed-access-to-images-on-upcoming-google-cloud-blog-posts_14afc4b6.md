---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-29_public-bucket-allowed-access-to-images-on-upcoming-google-cloud-blog-posts.md
original_filename: 2020-09-29_public-bucket-allowed-access-to-images-on-upcoming-google-cloud-blog-posts.md
title: Public Bucket Allowed Access to Images on Upcoming Google Cloud Blog Posts
category: blogs
detected_topics:
- cloud-security
- command-injection
- information-disclosure
tags:
- imported
- blogs
- cloud-security
- command-injection
- information-disclosure
language: en
raw_sha256: 14afc4b6cd6c7a5d3426e42f4cb24c14169b24fd04eff88087594c3a74af3353
text_sha256: 8ba183fce3e2c5bdb34747e6349caf7e7032fe294aeeb24a2a99e185b044560b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Public Bucket Allowed Access to Images on Upcoming Google Cloud Blog Posts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-29_public-bucket-allowed-access-to-images-on-upcoming-google-cloud-blog-posts.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `14afc4b6cd6c7a5d3426e42f4cb24c14169b24fd04eff88087594c3a74af3353`
- Text SHA256: `8ba183fce3e2c5bdb34747e6349caf7e7032fe294aeeb24a2a99e185b044560b`


## Content

---
title: "Public Bucket Allowed Access to Images on Upcoming Google Cloud Blog Posts"
page_title: "Public bucket allowed access to images on upcoming Google Cloud blog posts - Web Security Blog"
url: "https://websecblog.com/vulns/public-google-cloud-blog-bucket/"
final_url: "https://websecblog.com/vulns/public-google-cloud-blog-bucket/"
authors: ["Thomas Orlita (@ThomasOrlita)"]
programs: ["Google"]
bugs: ["GCP bucket misconfiguration", "Information disclosure", "Cloud"]
publication_date: "2020-09-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4231
---

# Public bucket allowed access to images on upcoming Google Cloud blog posts

[![](https://secure.gravatar.com/avatar/7f8a61ba947af5eb2a9b491c4dacb5f1b6952c86727d08f85d3b10e901d8e253?s=24&d=mm&r=g)](https://websecblog.com/author/admin/)by [Thomas Orlita](https://websecblog.com/author/admin/)[Vulnerabilities](https://websecblog.com/category/vulns/)[September 29, 2020June 11, 2026](https://websecblog.com/vulns/public-google-cloud-blog-bucket/)

Google has multiple different official blogs (for example [blog.google](https://blog.google/), [firebase.googleblog.com](https://firebase.googleblog.com/), or [cloud.google.com/blog](https://cloud.google.com/blog)).

Blogs on *.googleblog.com are hosted on blogspot.com and uploaded images are hosted on Blogspot’s CDN. However, The Keyword (blog.google) and Google Cloud blog use a custom platform for their blogs.

Images on these blogs are stored in Google Cloud Storage buckets:
  
  
  https://storage.googleapis.com/gweb-uniblog-publish-prod/

and
  
  
  https://storage.googleapis.com/gweb-cloudblog-publish/

respectively.

**Google Cloud Storage** is an IaaS file storage service on the Google Cloud Platform and can allow us to access the resources via an URL on the web. 

## Accessing the buckets

We can access the bucket in the browser using one of these URLs: 

  * `https://storage.googleapis.com/_< bucket name>_/`
  * `https://__< bucket name>__.storage.googleapis.com/`
  * `https://storage.cloud.google.com/__< bucket name>__/`
  * `https://sandbox.google.com/storage/__< bucket name>__/`

and adding the filename at the end of the URL.

### The Keyword Blog

However, if we try to access the first Cloud Bucket in the browser, it shows that we don’t have permission to list the uploaded items.
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <Error>
  <Code>AccessDenied</Code>
  <Message>Access denied.</Message>
  <Details>Anonymous caller does not have storage.objects.list access to the Google Cloud Storage bucket.</Details>
  </Error>

That’s because public listing of uploaded items is disabled by default.

### Google Cloud Blog

But if we try to access the second bucket, it returns the list of _all uploaded items_ in the bucket.
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <ListBucketResult xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <Name>gweb-cloudblog-publish</Name>
  <Prefix />
  <Marker />
  <NextMarker>images/100-announcements-12_T3T5Cv5.max-300x300.png</NextMarker>
  <IsTruncated>true</IsTruncated>
  <Contents>
  <Key>images/-02-MAIN-Dublin.2e16d0ba.fill-1000x347.jpg</Key>
  <Generation>1529607698661849</Generation>
  <MetaGeneration>1</MetaGeneration>
  <LastModified>2018-06-21T19:01:38.661Z</LastModified>
  <ETag>"fbce0d28ed561e2248946ca8763de8ad"</ETag>
  <Size>156772</Size>
  </Contents>
  <Contents>
  <Key>images/-02-MAIN-Dublin.2e16d0ba.fill-1000x563.jpg</Key>
  <Generation>1529607698725002</Generation>
  <MetaGeneration>1</MetaGeneration>
  <LastModified>2018-06-21T19:01:38.724Z</LastModified>
  <ETag>"a22b9d844cb2ade708ce4166f7d4797e"</ETag>
  <Size>259746</Size>
  </Contents>
  <Contents>
  <Key>images/-02-MAIN-Dublin.2e16d0ba.fill-100x100.jpg</Key>
  <Generation>1529607698808132</Generation>
  <MetaGeneration>1</MetaGeneration>
  <LastModified>2018-06-21T19:01:38.807Z</LastModified>
  <ETag>"ec3c2c4d8bff33d050e251a40a7ee52d"</ETag>
  <Size>7264</Size>
  </Contents>
  …
  </ListBucketResult>

Why did this happen? This bucket had public view permissions added for everyone.

![](https://websecblog.com/wp-content/uploads/public_access.png)

Since the _Storage Object Viewer (`roles/storage.objectViewer`)_ permission (or _`roles/storage.legacyBucketReader`_) has been added for _allUsers_ , it allowed anyone to view and list items stored in the bucket.

> **Storage Object Viewer**
> 
> Grants access to view objects and their metadata, excluding ACLs.  
> Can also list the objects in a bucket.

## Impact

The bucket was accessible to the public and included all uploaded images on the Google Cloud Blog, including images in draft blog posts.

![](https://websecblog.com/wp-content/uploads/image-56.png)

Getting access to images that have not been published yet could have resulted in a leak of confidential information, for example, upcoming Google Cloud products or features.

* * *

Timeline|  
---|---  
2019-04-10| Vulnerability reported  
2019-04-10| Priority changed to P2  
2019-04-10| Looking into it  
2019-04-12| Filed a bug  
2019-04-16| Reward issued  
2019-04-24| Marked as fixed  
  
Written by [Thomas Orlita](https://thomasorlita.com/)
  *[IaaS]: Infrastructure as a service

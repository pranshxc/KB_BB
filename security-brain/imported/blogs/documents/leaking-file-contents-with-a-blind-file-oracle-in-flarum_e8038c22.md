---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-28_leaking-file-contents-with-a-blind-file-oracle-in-flarum.md
original_filename: 2023-08-28_leaking-file-contents-with-a-blind-file-oracle-in-flarum.md
title: Leaking File Contents with a Blind File Oracle in Flarum
category: documents
detected_topics:
- api-security
- idor
- ssrf
- command-injection
- file-upload
- path-traversal
tags:
- imported
- documents
- api-security
- idor
- ssrf
- command-injection
- file-upload
- path-traversal
language: en
raw_sha256: e8038c229a19bbc1b37c66ff78f1e7915ef013a3e5962ae87b8d1c9ebb7b67a6
text_sha256: 6cb664f7922f6d4cea338fe7692d43864622c43bc3e2342456aa5419e93685e6
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking File Contents with a Blind File Oracle in Flarum

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-28_leaking-file-contents-with-a-blind-file-oracle-in-flarum.md
- Source Type: markdown
- Detected Topics: api-security, idor, ssrf, command-injection, file-upload, path-traversal
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `e8038c229a19bbc1b37c66ff78f1e7915ef013a3e5962ae87b8d1c9ebb7b67a6`
- Text SHA256: `6cb664f7922f6d4cea338fe7692d43864622c43bc3e2342456aa5419e93685e6`


## Content

---
title: "Leaking File Contents with a Blind File Oracle in Flarum"
url: "https://blog.assetnote.io/2023/08/28/leaking-file-contents-with-a-blind-file-oracle-in-flarum/"
final_url: "https://www.assetnote.io/resources/research/leaking-file-contents-with-a-blind-file-oracle-in-flarum"
authors: ["Adam Kues (@hash_kitten)"]
programs: ["Flarum"]
bugs: ["PHP filter chain", "Arbitrary file read", "LFI", "Security code review"]
publication_date: "2023-08-28"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 829
---

[Research Notes](/resources/research)

Security Research

August 28, 2023

# Leaking File Contents with a Blind File Oracle in Flarum

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

## Introduction

Flarum is a free, open source PHP-based forum software used for everything from gaming hobbyist sites to cryptocurrency discussion. A quick survey on Shodan suggests there are over 1200 installs exposed to the internet.

Through our research we were able to leak the contents of arbitrary local files in Flarum through a blind oracle, and conduct blind SSRF attacks with only a basic user account.

_We continue to perform original security research in an effort to alert our customers to zero-day vulnerabilities in their attack surface. As users of our_[ _Attack Surface Management_](https://assetnote.io/) _platform, our customers are the first to know when they are affected by new vulnerabilities._

## Understanding the Flarum Software

Since Flarum is open source software, there was no need for reverse engineering. We quickly realised that the vast majority of code for a Flarum installation comes from the <span class="code_single-line">flarum/framework</span> repository, which is available [on Github](https://github.com/flarum/framework). The first step in analysing the application was to figure out which routes were accessible. Unlike many other software applications we assess at Assetnote, due to Flarum’s nature as forum software, the majority of installations typically permit users to create their own accounts. This means that authenticated routes are also interesting, as long as they don’t require administrative permissions.

We quickly figured out that files called <span class="code_single-line">routes.php</span> in different directories provided routing for most of the application, and in particular that <span class="code_single-line">framework/core/src/Api/routes.php</span> listed a lot of interesting routes:
  
  
  use Flarum\Api\Controller;
  use Flarum\Http\RouteCollection;
  use Flarum\Http\RouteHandlerFactory;
  
  return function (RouteCollection $map, RouteHandlerFactory $route) {
  // Get forum information
  $map->get(
  '/',
  'forum.show',
  $route->toController(Controller\ShowForumController::class)
  );
  
  ... 
  
  // Send test mail post
  $map->post(
  '/mail/test',
  'mailTest',
  $route->toController(Controller\SendTestMailController::class)
  );
  };
  
  

We quickly ruled out a lot of otherwise interesting routes that required admin permissions, such as <span class="code_single-line">/mail/test</span>. After a while of looking through the code route by route, we identified a potentially interesting API endpoint that allowed users to update their forum avatar:
  
  
  // Upload avatar
  $map->post(
  '/users/{id}/avatar',
  'users.avatar.upload',
  $route->toController(Controller\UploadAvatarController::class)
  );
  
  

We then dived into the <span class="code_single-line">UploadAvatarController</span> for a closer look.

## Looking at the Upload Functionality

The code of the <span class="code_single-line">UploadAvatarController</span> is very straightforward:
  
  
  protected function data(ServerRequestInterface $request, Document $document)
  {
  $id = Arr::get($request->getQueryParams(), 'id');
  $actor = RequestUtil::getActor($request);
  $file = Arr::get($request->getUploadedFiles(), 'avatar');
  
  return $this->bus->dispatch(
  new UploadAvatar($id, $file, $actor)
  );
  }
  
  

The route takes a user <span class="code_single-line">id</span> in the query parameter, and a file upload named <span class="code_single-line">avatar</span>, and dispatches an <span class="code_single-line">UploadAvatar</span> action to the bus. This is then handled in the <span class="code_single-line">UploadAvatarHandler</span> class in <span class="code_single-line">framework/core/src/User/Command/UploadAvatarHandler.php</span>:
  
  
  class UploadAvatarHandler
  {
  use DispatchEventsTrait;
  
  ...
  
  /**
  * @var ImageManager
  */
  protected $imageManager;
  
  ...
  
  public function handle(UploadAvatar $command)
  {
  $actor = $command->actor;
  
  $user = $this->users->findOrFail($command->userId);
  
  if ($actor->id !== $user->id) {
  $actor->assertCan('edit', $user);
  }
  
  $this->validator->assertValid(['avatar' => $command->file]);
  
  $image = $this->imageManager->make($command->file->getStream());
  
  $this->events->dispatch(
  new AvatarSaving($user, $actor, $image)
  );
  
  $this->uploader->upload($user, $image);
  
  $user->save();
  
  $this->dispatchEventsFor($user, $actor);
  
  return $user;
  }
  }
  
  

Here the function checks we have access to change the avatar of the user with that ID, which prevents a trivial IDOR. However, we are more interested in the behavior of the <span class="code_single-line">imageManager->make</span> function. The <span class="code_single-line">ImageManager</span> is sourced from the Intervention Image library. What is that?

## When Library Code is Dangerous by Default

Intervention Image [is a PHP image handling and manipulation library](https://image.intervention.io/v2) that provides a simple interface to load, store, and edit images. Let’s start by looking at the documentation for the ImageManager’s make method:
  
  
  Universal factory method to create a new image instance from source. The method is highly variable to read all the input types listed below.
  
  

The library then lists a bunch of methods you can use to supply an image:
  
  
  string - Path of the image in filesystem.
  string - URL of an image (allow_url_fopen must be enabled).
  string - Binary image data.
  string - Data-URL encoded image data.
  string - Base64 encoded image data.
  resource - PHP resource of type gd. (when using GD driver)
  object - Imagick instance (when using Imagick driver)
  object - Intervention\Image\Image instance
  object - SplFileInfo instance (To handle Laravel file uploads via Symfony\Component\HttpFoundation\File\UploadedFile)
  
  

This immediately raises alarm bells. We are providing a string to this method (not exactly, but an object with a <span class="code_single-line">__toString()</span> magic method) and have full control. In the happy path, this just ‘works’ since one of the options is binary image data. But what happens if we upload a file containing a URL?

To understand the impact, let’s dive into the sources of the image library:
  
  
  namespace Intervention\Image;
  
  abstract class AbstractDecoder
  {
  // ...
  
  public function init($data)
  {
  $this->data = $data;
  
  switch (true) {
  
  case $this->isGdResource():
  return $this->initFromGdResource($this->data);
  
  case $this->isImagick():
  return $this->initFromImagick($this->data);
  
  case $this->isInterventionImage():
  return $this->initFromInterventionImage($this->data);
  
  case $this->isSplFileInfo():
  return $this->initFromPath($this->data->getRealPath());
  
  case $this->isBinary():
  return $this->initFromBinary($this->data);
  
  case $this->isUrl():
  return $this->initFromUrl($this->data);
  
  case $this->isStream():
  return $this->initFromStream($this->data);
  
  case $this->isDataUrl():
  return $this->initFromBinary($this->decodeDataUrl($this->data));
  
  case $this->isFilePath():
  return $this->initFromPath($this->data);
  
  // isBase64 has to be after isFilePath to prevent false positives
  case $this->isBase64():
  return $this->initFromBinary(base64_decode($this->data));
  
  default:
  throw new NotReadableException("Image source not readable");
  }
  }
  }
  
  

We are interested in particular in the functionality when the string supplied is a URL, so let’s see what checks are done:
  
  
  public function isUrl()
  {
  return (bool) filter_var($this->data, FILTER_VALIDATE_URL);
  }
  
  // ...
  
  public function initFromUrl($url)
  {
  
  $options = [
  'http' => [
  'method'=>"GET",
  'protocol_version'=>1.1, // force use HTTP 1.1 for service mesh environment with envoy
  'header'=>"Accept-language: en\r\n".
  "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36\r\n"
  ]
  ];
  
  $context  = stream_context_create($options);
  
  
  if ($data = @file_get_contents($url, false, $context)) {
  return $this->initFromBinary($data);
  }
  
  throw new NotReadableException(
  "Unable to init from given url (".$url.")."
  );
  }
  
  

Our user input gets passed into <span class="code_single-line">file_get_contents</span> without any validation, except that it must ‘look like’ a URL! This is known to be incredibly dangerous. The one limitation is that the content to leak must be a valid image, otherwise an error is thrown when the library parses the contents. We can start to brainstorm ways we can abuse this functionality:

  * We could pass an internal URL such as <span class="code_single-line">http://localhost:8100/favicon.ico</span>, and possibly leak that image if it exists.
  * We could pass an internal URL such as <span class="code_single-line">http://localhost:9001/do/evil/action?param=foo</span>, and conduct a blind SSRF attack.
  * More worryingly, despite the stream context, PHP is happy to accept a file URI, so an input like <span class="code_single-line">file:///home/foo/secret.png</span> could possibly reveal the contents of an image on the local filesystem.

While these definitely are vulnerabilities, they are context-dependent and are not so impactful. Can we do better? It turns out, using blind file oracle, we can!

## Blind File Oracles 101

First revealed in the DownUnderCTF 2022, there is a technique for leaking the contents of arbitrary files using the <span class="code_single-line">php://</span> wrapper even if the output of the file read is not given to the user. In our case, the files we want to read are most likely not going to form valid images, so this is a perfect application of this technique. In summary, this attack hinges on two features of the <span class="code_single-line">php://filter</span> wrapper.

The first is that the filter wrapper supports converting between two different charsets using the <span class="code_single-line">convert.iconv</span> function. For instance, the request <span class="code_single-line">php://filter/convert.iconv.latin1.UTF-32/resource=/etc/passwd</span> would take the contents of <span class="code_single-line">/etc/passwd</span> and convert it from the latin1 charset to UTF-32. In this case, the file content gets mapped to something like this:

latin1: root:x: 

UTF-32: r\0\0\0o\0\0\0o\0\0\0t\0\0\0:\0\0\0x\0\0\0:\0\0\0

Note how the output blows up 4x in size, because each latin1 char is encoded in a fixed 4 bytes of UTF-32. If we repeat this process, the string will blow up to 16x, 64x, 256x size, and so on, and eventually the string will grow so large it will exceed the memory limit and cause the PHP process to stop and return 500. However, if the file we point to is empty or does not exist, no 500 error will be generated. This forms an oracle we can use to test for emptiness.

On its own this is not so useful, but PHP has another interesting ‘feature’ - the <span class="code_single-line">dechunk</span> filter. The <span class="code_single-line">dechunk</span> filter was intended for parsing HTTP chunks, but its behavior on arbitrary strings are as follows:

  * If the string is a single line and begins with one of <span class="code_single-line">0-9a-fA-F</span>, the whole line is removed;
  * Otherwise, the string remains untouched.

We can now leak information from a file as follows:

  * Base64 encode the file using the <span class="code_single-line">convert.base64-encode</span> function;
  * Apply the dechunk filter;
  * Blow up the string multiple times using a latin1 - UTF32 conversion.

If we don’t get a 500, we know that the file contents in base64 must have started with one of <span class="code_single-line">0-9a-fA-F</span>. Otherwise, if we do get a 500, we know it can’t have started with those characters (so it must be in <span class="code_single-line">g-zG-Z+/</span>)

The full file leak is more complicated and uses multiple iconv conversions to swap other characters to the front and precisely determine which character is at the front. The gory details are explained in the original challenge’s [solution script](https://github.com/DownUnderCTF/Challenges_2022_Public/blob/main/web/minimal-php/solve/solution.py) and in a [blog post written by Synacktiv](https://www.synacktiv.com/en/publications/php-filter-chains-file-read-from-error-based-oracle).

Summarising, with a simple modification to the above script we are able to use the technique to leak the contents of any file on the server.

## Remediation

Flarum fixed this vulnerability promptly and versions <span class="code_single-line">>= 1.8.0</span> are no longer vulnerable. Their advisory is available [here](https://github.com/flarum/framework/security/advisories/GHSA-67c6-q4j4-hccg). The vulnerability was assigned CVE-2023-40033.

We have tried reaching out to the developers of <span class="code_single-line">Intervention/Image</span> several times with some suggestions to make the library less vulnerable by default, but have got no response. If you are using this library, the best way to ensure you are not vulnerable is by never passing user data directly into the constructor; if you are wanting to turn an upload into an image, pass the file path to the uploaded tempfile instead.

## Conclusion

In this blog post, we have seen that a small error in how a library for image manipulation was used resulted in the ability to leak the contents of any file on disk. We have also shown that the PHP blind file oracle which originated in a CTF challenge has real-world applicability and should be kept in mind when auditing PHP source code.

As always, customers of our Attack Surface Management platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities in their attack surface.

Written by:

Adam Kues

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)

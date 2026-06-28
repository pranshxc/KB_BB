---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-14_craftcms-rce.md
original_filename: 2023-09-14_craftcms-rce.md
title: CraftCMS RCE
category: documents
detected_topics:
- command-injection
- access-control
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- access-control
- api-security
- cloud-security
language: en
raw_sha256: 28867df630e292e913af9b3736a85811bac99b33cec6754277023d3355540def
text_sha256: e6de4c03a085962bcbdcac0b928f70be3a403f3f60a4d1bcb394bbb595e30dad
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# CraftCMS RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-14_craftcms-rce.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `28867df630e292e913af9b3736a85811bac99b33cec6754277023d3355540def`
- Text SHA256: `e6de4c03a085962bcbdcac0b928f70be3a403f3f60a4d1bcb394bbb595e30dad`


## Content

---
title: "CraftCMS RCE"
page_title: "CraftCMS RCE - by Thanh - Calif"
url: "https://blog.calif.io/p/craftcms-rce"
final_url: "https://blog.calif.io/p/craftcms-rce"
authors: ["Thanh"]
programs: ["Craft CMS"]
bugs: ["RCE", "Code injection", "Security code review"]
publication_date: "2023-09-14"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 779
---

# CraftCMS RCE

[![Thanh's avatar](https://substackcdn.com/image/fetch/$s_!zMDC!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6425f7d-0fd0-44d7-a5d0-6a74d07e3689_144x144.png)](https://substack.com/@thanhc)

[Thanh](https://substack.com/@thanhc)

Sep 14, 2023

12

Share

> Craft is a flexible, user-friendly CMS for creating custom digital experiences on the web—and beyond.
> 
> You have a ton of options when it comes to choosing a CMS. Craft is uniquely equipped to deliver high-quality, content-driven experiences to your clients and their audiences, in large part due to its blank-slate approach to content modeling.

We recently encountered a target running CraftCMS in an engagement, and discovered a Remote Code Execution vulnerability (CVE-2023-41892) that allowed us to compromise the target. While the patch [is now available](https://github.com/advisories/GHSA-4w8r-3xrw-v25g), all CraftCMS users are strongly encouraged to apply the additional mitigation at the end of this post to keep your instance secure.

# The vulnerability

Like other content management systems, the pre-auth attack surface of CraftCMS is relatively limited. However, the `\craft\controllers\ConditionsController` class quickly got our attention because its `beforeAction` method seems to do something with object creation. 
  
  
  public function beforeAction($action): bool
  {
  $baseConfig = Json::decodeIfJson($this->request->getBodyParam('config'));
  $config = $this->request->getBodyParam($baseConfig['name']);
  $newRuleType = ArrayHelper::remove($config, 'new-rule-type');
  $conditionsService = Craft::$app->getConditions();
  $this->_condition = $conditionsService->createCondition($config);
  **Craft::configure($this- >_condition, $baseConfig);**
  ...
  
  
  \yii\BaseYii::configure
  \yii\base\Component::__set
  \yii\BaseYii::createObject
  ...

After spending some time understanding the code, we confirmed that the endpoint gave us the ability to create an arbitrary object.

The codebase of CraftCMS and its dependencies contains several gadgets that can be used to escalate the object creation into something meaningful, like limitedly calling some methods:

> \GuzzleHttp\Psr7\FnStream
  
  
  public function __destruct()
  {
  if (isset($this->_fn_close)) {
  **call_user_func($this- >_fn_close);**
  }
  }

Or including arbitrary files:
  
  
  \yii\base\BaseObject::__construct
  \yii\rbac\PhpManager::init
  \yii\rbac\PhpManager::load
  \yii\rbac\PhpManager::loadFromFile
  
  
  protected function loadFromFile($file)
  {
  if (is_file($file)) {
  **return require $file;**
  }
  
  
  return [];
  }

The latter seemed to be a quick win for us, as we could inject some PHP code into the [CraftCMS’s log file](https://craftcms.com/docs/4.x/logging.html) and then include it, just like in a CTF challenge (and we can even use the `@storage` variable to locate the log file in case it is placed somewhere other than the default location, which makes the exploit easier). 

Unfortunately, in the case of our target, no log files are available on the server. We could leverage a PHP behavior to create temporary files, but we didn’t know the exact filename to include (the `FindFirstFile` / `<` trick could not be applied here since we were dealing with a Linux server). On the other hand, including a remote file was also not possible.

That’s when we remembered [an excellent research](https://swarm.ptsecurity.com/exploiting-arbitrary-object-instantiations/) from Arseniy Sharoglazov, because the described vulnerability is identical to what we were working on. In his post, Arseniy revealed that creating an `Imagick` object with the `VID` scheme would result in an arbitrary file write, and the beauty of the `VID` scheme is its ability to reference a file without knowing the filename. That’s all we needed.

The rest of the work was straightforward, and after some testing, we got an exploit that worked perfectly on the target environment and achieved RCE.

# Recommendations

Besides applying [the patch](https://github.com/craftcms/cms/releases/tag/4.4.15), we highly recommend all CraftCMS users to rotate the `CRAFT_SECURITY_KEY` immediately. We have confirmed that knowing the key will lead to an unauthenticated RCE on a widely used CraftCMS plugin, and there may be more.

12

Share

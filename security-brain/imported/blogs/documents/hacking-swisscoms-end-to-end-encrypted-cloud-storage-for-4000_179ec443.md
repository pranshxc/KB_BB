---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-08_hacking-swisscoms-end-to-end-encrypted-cloud-storage-for-4000.md
original_filename: 2024-04-08_hacking-swisscoms-end-to-end-encrypted-cloud-storage-for-4000.md
title: Hacking Swisscom’s End-to-End Encrypted Cloud Storage for $4,000
category: documents
detected_topics:
- password-reset
- automation-abuse
- sso
- idor
- xss
- command-injection
tags:
- imported
- documents
- password-reset
- automation-abuse
- sso
- idor
- xss
- command-injection
language: en
raw_sha256: 179ec4438a894dbca21879673830287dac96f18c7bf042c4272d9bb0e28fbc97
text_sha256: 66652206182c4132ec2fa5a5f4df729514d415e1527330c517eedbd88e2b9d45
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Swisscom’s End-to-End Encrypted Cloud Storage for $4,000

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-08_hacking-swisscoms-end-to-end-encrypted-cloud-storage-for-4000.md
- Source Type: markdown
- Detected Topics: password-reset, automation-abuse, sso, idor, xss, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `179ec4438a894dbca21879673830287dac96f18c7bf042c4272d9bb0e28fbc97`
- Text SHA256: `66652206182c4132ec2fa5a5f4df729514d415e1527330c517eedbd88e2b9d45`


## Content

---
title: "Hacking Swisscom’s End-to-End Encrypted Cloud Storage for $4,000"
page_title: "Discovering Logic Vulnerabilities in Swisscom's End-to-End Encrypted Cloud Storage | Thomas Houhou"
url: "https://www.thomashouhou.com/post/logic-vulnerabilities-swisscom-e2ee-cloud-storage"
final_url: "https://www.thomashouhou.com/post/logic-vulnerabilities-swisscom-e2ee-cloud-storage/"
authors: ["Thomas Houhou (@Th0h0)"]
programs: ["Swisscom"]
bugs: ["Password reset", "Security code review"]
bounty: "4,000"
publication_date: "2024-04-08"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 349
---

![Discovering Logic Vulnerabilities in Swisscom's End-to-End Encrypted Cloud Storage](/resources/mycloud-illustration.png)

APRIL 08, 2024

# Discovering Logic Vulnerabilities in Swisscom's End-to-End Encrypted Cloud Storage

## Table of Contents

  1. The Story
  2. Understanding MyCloud Safe: Generating and Securely Storing Asymmetric Keys, Recovery Codes, and Recovery Keys
  3. Vulnerability 1 (CHF 750 Bounty)
  4. Vulnerability 2 (CHF 3000 Bounty)
  5. Conclusion / Takeaway

### The Story

On October 17, 2022, Swisscom sent an email inviting 15 selected hunters to test the security of a newly released feature within their cloud storage solution, MyCloud. This new service, called MyCloud Safe, introduces end-to-end encryption to MyCloud by employing client-side encryption. In this context, users own two asymmetric key pairs: one for file encryption and another for request signing. The file encryption key pair consists of a public key responsible for encrypting files before upload and a private key allowing to decrypt them back for read or update. Since this service is protected by an additional password, it must preserve an additional layer of authenticity as well, which is the purpose of the second key pair: the private key signs each HTTP request and the public key allows server-side signature verification.

![MyCloud Safe Initialization Page](/images/posts/logic-vulnerabilities-swisscom-e2ee-cloud-storage/mycloud-init.png)

MyCloud Safe Initialization Page

### Understanding MyCloud Safe: Generating and Securely Storing Asymmetric Keys, Recovery Codes, and Recovery Keys

As described in the first section, end-to-end encryption makes it so that the user is responsible for encrypting and decrypting their own data. The very first step of the service initialization phase would then be to generate the required personal asymmetric key pairs, including the request-signing one. Given that MyCloud Safe is exclusively deployed on web, expecting the user to indefinitely store the keys in the same unique browser, without ever using other devices, would be very inconvenient — if not impractical. Thus, MyCloud Safe's server is required to keep state or store information about the client's private keys somehow. The challenge and complexity of such a service is then to accomplish this while preserving the implications of end-to-end encryption, i.e., no access to protected data or keys should be given to Swisscom, which is considered a third party in this context. Ultimately, MyCloud Safe must provide enough information for the client to retrieve the private keys without being able to access them itself.

Let's describe step-by-step how MyCloud Safe implements this:

_Note: As most of these insights were inferred by diving into MyCloud Safe's JavaScript files, I will sometimes refer to the code. When not explicitly invited to look at it, you're not required to do so in order to understand the two upcoming vulnerabilities. It might, of course, always be useful for your own curiosity or if you want to start hacking on MyCloud Safe :) (the service is now public; feel free to contact me if you want more details about it — I took quite extensive notes)._

#### 1\. Setting a secret passphrase

The UI prompts the user to define a secret passphrase. Although this passphrase does not directly serve as a private key, it plays a significant role, which will be explored later.

![Setting a secret passphrase](/images/posts/logic-vulnerabilities-swisscom-e2ee-cloud-storage/setting-passphrase.png)

#### 2\. Generation of recovery code

After setting a password and clicking on _Continue,_ client-side javascript generates 10 recovery codes. The second vulnerability will be directly related to those.

![Recovery code generation](/images/posts/logic-vulnerabilities-swisscom-e2ee-cloud-storage/recovery-code.png)

The responsible code is the below:
  
  
  o.recoveryCodeList = [],
  o.recoveryCodePayloads = [];
  try {
  const e = await cryptoService.Safe.generateRecoveryCodes(10); // generating the 10 codes
  o.recoveryCodePassphrase = e.passphrase, // recovery passphrase?
  o.recoveryCodeList = e.codes,
  o.recoveryCodePayloads = e.codesPayload, // recovery code payloads?
  o.filename('myCloud_safe_recoveryCodes_{0}.txt'.storage_format((new Date).storage_toCustomizedString('dd.MM.yyyy HH:mm'))),
  o.downloadCodesValue('data:application/octet-stream,' + [...] o.recoveryCodeList.join('%0A')) // recovery codes are downloaded by the user as a .txt file
  

The above code calls the function _generateRecoveryCodes_ on line 4. Let's inspect it as well:
  
  
  generateRecoveryCodes: function(e) {
  return new Promise(async (t, i) => {
  const n = window.crypto.getRandomValues(new Uint8Array(32)),
  o = [],
  r = [];
  for(let t = 0; t < e; t++) {
  const e = await cryptoService.recoveryCode.generateCode(n);
  r.push(e.codeHex),
  o.push(e.payload)
  }
  t({
  passphrase: n,
  codes: r,
  codesPayload: o
  })
  })
  }
  

Analyzing these two code snippets reveals interesting insights. In addition to generating the 10 recovery codes (line 6 of the first snippet; line 13 of the second snippet), the process also generates another passphrase (line 5 of the first snippet; line 12 of the second snippet) and recovery code payloads (line 7 of the first snippet; line 14 of the second snippet). These two additional elements provide specific clues to how recovery codes are used under the hood and will later guide us to the discovery of the second vulnerability.

#### 3\. Generating the asymmetric keys and securing them

##### 3.1. Keys generation

With the initialization of MyCloud Safe nearly done, the necessary keys can finally be generated:
  
  
  o.createSafeAccount = async
  function() {
  storageUIService.Loader.Show(!0);
  const e = await cryptoService.Safe.generateUserKeys(o.repeatPasswordValue, o.recoveryCodePassphrase);
  

This effectively creates the two asymmetric key pairs, respectively dedicated to request signature and file encryption.
  
  
  userSigningKey: await cryptoService.keys.generateSigningKey(!0), // request-signature key pair
  userEncryptionKey: await cryptoService.keys.generateEncryptionKey(!0) // file-encryption key pair
  

The functions _generateSigningKey_ and _generateEncryptionKey_ ultimately rely on the native Web Crypto API by calling _window.crypto.subtle.generateKey_ with the key generation algorithm specified as argument.

##### 3.2. Passphrase gets involved

Here finally comes to play the passphrase previously set by the user.

Rather than being straightforwardly used as a weak private key, this secret passphrase actually serves as a Key-Encryption-Key (KEK) or wrapping key, whose purpose is to encrypt (or wrap) the generated private keys. This, thus, allows MyCloud Safe to exclusively and securely store the encrypted versions of the user's private keys instead of the plain ones. Although bringing additional complexity, this adopted strategy successfully addresses the previously described challenge of preventing access to third parties (Swisscom itself) while not expecting users to permanently store their private keys. In such a setup, the user will be able to request their encrypted private keys from the server and decrypt them using their passphrase, making the keys readily available for use.

The below three lines of code are associated with this key wrapping process:
  
  
  a = await cryptoService.helpers.getImportKey(passphrase),
  

_getImportKey function is used to derive a proper key in the right format from the passphrase string._
  
  
  signingKey: await cryptoService.helpers.getKeyPayload(u.userSigningKey, a, i, r, h),
  userKey: await cryptoService.helpers.getKeyPayload(u.userEncryptionKey, a, i, o, d)
  

_getKeyPayload is responsible for wrapping the keys with the one derived from the passphrase._

##### 3.3. Recovery data

Now is the perfect time to discuss what happens with the recovery codes. As we previously observed, in addition to generating the 10 recovery codes, another passphrase and code payloads are also generated. These additional pieces allow for the construction and securing of wrapped keys in a manner very similar to the regular process discussed in sub-section 3.2. The generated extra passphrase, which is randomly generated, then acts as another key-encryption-key (KEK) or wrapping key for the private keys.

_But what about the recovery codes and the recovery payloads?_

As the complexity of MyCloud Safe never stops growing, recovery codes themselves are actually used as key-encryption-keys. Their role is to encrypt or wrap the recovery passphrase, which, if you remember, is itself a key-encryption-key for the private keys... In this context, the recovery payloads are the encrypted versions of the recovery passphrase, where the encryption key involved is an associated recovery code. Each recovery code then maps to one recovery code payload.

This newly added complexity in the recovery data generation could be attributed to efficiency reasons. Hiding the private key behind or mapping the private key to the passphrase, which is a much smaller structure, results in a smaller ciphertext compared to what would have been generated if the entire high-entropy private keys were used. Since the user regularly fetches the wrapped private keys already, the former would only need to fetch the encrypted recovery passphrase (i.e., the recovery code payload) during a recovery process. This approach makes the process lighter in terms of bandwidth and storage for both the server and the end-user.

#### 4\. Sending the relevant (non-revealing) data to MyCloud Safe's server

In this final step, the client completes the MyCloud Safe setup and initialization by sending an HTTP POST request to the server at the endpoint _https://mycloud.swisscom.ch/safe_. The POST body consists of:

  * The wrapped or encrypted private keys (for signature and encryption, both for the regular and the recovery cases, totaling to four private keys)
  * The associated public keys (which do not need to be protected by wrapping/encryption by definition)
  * The ten recovery code payloads (the same recovery passphrase encrypted by the ten different recovery codes)

Once the POST request is sent, most of the data from the post body (excluding the recovery-related data) populates the same endpoint (_/safe_) for a GET request. The HTTP response for the latter is the below:
  
  
  {
  "keys":{
  "signingKey":{
  "id":"0140c60f-d416-6986-0e2d-34346b95c350",
  "pub":{
  "d":"eyJrdHkiOiJFQyIsImNydiI6Il[...]vTmFxMTc2MmJpZk5zcmUtV3pCdDZ0ZCJ9"
  },
  "pri":{
  "d":"DQMlWZr14sNI8R/OvKfPuRoalEKRUBq2/[....]BLlHygfJ/E=",
  "iv":"zVDQ+5Vc+QnuQw7L"
  }
  },
  "userKey":{
  "id":"6f8abf14-0930-6aae-8120-d7a58bfa8f62",
  "pub":{
  "d":"eyJrdHkiOiJSU0E[...]Wm1zTTM2YyJ9"
  },
  "pri":{
  "d":"4VfhC1sva[....]Qw1q+Pspm4CMAiXXh",
  "iv":"A4O7TmAcH6WfS/rp"
  }
  },
  "keyDerivationInfo":{
  "salt":"K3VsCEYkCcGVH5C1DzpgTg",
  "iterationCount":300000,
  "algo":"PBKDF2"
  }
  },
  "remainingRecoveryCodes":10
  }
  

The client login process for MyCloud Safe then proceeds as follows:

  1. Client-side javascript initiates a GET request to the _/safe_ endpoint to retrieve the wrapped private keys dedicated to encryption and signature.
  2. The user enters their secret passphrase.
  3. The secret passphrase is transformed into a key, which is then used to decrypt the wrapped private keys.
  4. The plain private keys get stored in the user's browser.

With these steps completed, MyCloud Safe can now be fully and freely accessed by the authenticated user.

### Vulnerability 1 (CHF 750 Bounty)

Given the above insights into how MyCloud Safe works under the hood, we can finally discuss the first vulnerability!

MyCloud Safe offers a passphrase reset feature that can be triggered in two ways:

  1. Via a recovery code, if the passphrase is forgotten
  2. Via the authenticated MyCloud Safe panel, assuming the user remembers the passphrase but might want to change it due to compromise concerns

When fetching the endpoint _mycloud.swisscom.ch/safe_ and comparing the returned JSON data before and after a passphrase reset (feel free to refer to the objects and attributes of the returned JSON in the previous snippet), it can be noticed that in the `pri` objects, which are supposed to represent the private key, the `d` attribute (supposedly consisting of the private key's value) does indeed change. It could then be appropriately assumed that the reset proceeded as intended. However, from the insights gained in the previous sections, we can actually discover that the naming in this returned JSON is misleading. In fact, in line with the POST request responsible for finalizing the MyCloud Safe initialization/setup, while the `d` attribute of the `pub` object (from `signingKey` and `userKey`) does consist of the plain value of the public key, the `d` attribute of the `pri` object represents the value of the wrapped/encrypted private key, not the plain version!

Therefore, the change in the `d` attribute of `pri` after a reset could actually be the consequence of two separate behaviors:

  1. Both the plain private keys and the key-encryption-key (i.e., the passphrase) were affected by the reset and changed.
  2. The plain private keys were not affected by the reset, and only the passphrase was changed.

While the first behavior is secure, the second is not.

Still looking at the JSON response from the `/safe` endpoint, one element reveals the approach followed by the developers: the public key. It can be observed that the `d` attribute of the public key objects remains the same across resets. Given that the public key is always derived from the private key, a non-changing public key implies a static private key.

Such an implementation implies that, in the case of an initial MyCloud Safe compromise where the private keys become known to an attacker, no passphrase reset would ever have the capability to remove access to the latter. The access becomes persistent, and the passphrase reset turns out to not behave as the user would expect.

### Vulnerability 2 (CHF 3000 Bounty)

In the situation where a user forgets their secret passphrase, recovery codes can be used to reset it and regain access to the MyCloud Safe files. This reset action consists of a multi-step process, and it's where the second vulnerability was identified.

This process follows the below flow:

  1. The user enters their recovery code

![Forgot Password screen](/images/posts/logic-vulnerabilities-swisscom-e2ee-cloud-storage/forgot-password.png)

  2. As soon as the user clicks on 'Continue', a body-less POST request is asynchronously sent to the following endpoint:
  
  https://safe-backend.prod.mdl.swisscom.ch/safe/recovery-package/[HASH_OF_RECOVERY_CODE]
  

This POST request leads to an HTTP response with a JSON body of the following form:
  
  {
  "passphrase_protected_keys":{
  "signingKey":{
  "id":"0140c60f-d416-6986-0e2d-34346b95c350",
  "pub":{
  "d":"eyJrdHkiOiJFQyIsImNydiI6Il[...]vTmFxMTc2MmJpZk5zcmUtV3pCdDZ0ZCJ9"
  },
  "pri":{
  "d":"3yVO04ASwgstHGBw[...]ik7nozcISpwO72bR8+O9Ws=",
  "iv":"FbZsFnZCmSSQFkUx"
  }
  },
  "userKey":{
  "id":"6f8abf14-0930-6aae-8120-d7a58bfa8f62",
  "pub":{
  "d":"eyJrdHkiOiJSU0E[...]Xk0Wm1zTTM2YyJ9"
  },
  "pri":{
  "d":"bbRzDBhltDE7t[...]XQJrzk0q0nRyYzLU4f/y5V3YOzFw1nufVY2ZcZUnXhZ+tiqT",
  "iv":"ud72bkPNyxJOMyn3"
  }
  },
  "keyDerivationInfo":{
  "salt":"tTrZFYZ2HR+j42yofZKKTQ==",
  "iterationCount":300000,
  "algo":"PBKDF2"
  }
  },
  "recovery_code":{
  "keyDerivationInfo":{
  "salt":"wujxdmx6EfPJgIEu26Sl1A==",
  "iterationCount":300000,
  "algo":"PBKDF2"
  },
  "hash":"[HASH_OF_RECOVERY_CODE]",
  "passphrase":{
  "d":"JwIdjRCYwvtaVy2ekZ3toLG9/wRWlSYcsVGkMOm9VfJacwN6R62PjgqHaU+wH5fM",
  "iv":"4LsBSiiZVRtVjABm"
  }
  }
  }
  

  3. If the previous HTTP response indicates success, meaning the recovery code's hash is correctly recognized, the user is prompted to enter a new passphrase.

  4. Once the user enters the new desired password and clicks on 'Continue', a final HTTP request is sent:
  
  PATCH /safe HTTP/1.1
  Host: safe-backend.prod.mdl.swisscom.ch
  Cookie:[...]
  [...Headers]
  Content-Type: application/json;
  
  {
  "type":"pw_change_with_recovery",
  "diff":{
  "keyDerivationInfo":{
  "algo":"PBKDF2",
  "iterationCount":300000,
  "salt":"bgZkT5NSoBovAF1JBRXRwQ=="
  },
  "signingKey":{
  "id":"0140c60f-d416-6986-0e2d-34346b95c350",
  "pub":{
  "d":"eyJhbGci[...]nQ2dGQifQ=="
  },
  "pri":{
  "d":"oU9Ukd7A54Ef[...]xmkwKk2I=",
  "iv":"LYkqQcCOapFKKMQP"
  }
  },
  "userKey":{
  "id":"6f8abf14-0930-6aae-8120-d7a58bfa8f62",
  "pub":{
  "d":"eyJhbGciOiJ[...]0zNmMifQ=="
  },
  "pri":{
  "d":"APicSIKJTy[...]e+tE+P2LZnNcUGx",
  "iv":"8ANrh21eTsOLfAeh"
  }
  },
  "recoveryCodeHash":"[HASH_OF_RECOVERY_CODE]"
  }
  }
  

After the above step (and only after this step!!), the recovery code is consumed and cannot be reused anymore, and the user is assigned a new passphrase.

At this point, if you well understood from previous sections how recovery codes work in MyCloud Safe, and pay attention to the last sentence, you may have already spotted the issue. If not, feel free to try guessing now what could be wrong in this described multi-step process.

The security issue is described below:

The issue in this process lies in the fact that, even though the recovery code is only consumed at the last step (4.), the server's HTTP response from step 2 already provides all the necessary and sufficient information to access the user's private key. This entire multi-step process can thus be shortcut in a way that would make resetting the passphrase irrelevant, and that, without the recovery code getting consumed.

In fact, as stated in a previous section, the recovery code is nothing more than a key-encryption-key for a randomly generated recovery passphrase, which is different from the one set by the user. This recovery passphrase itself is a key-encryption-key for the private keys. Thus, as we observe that the wrapped/encrypted recovery passphrase is returned in the JSON response from step 2 on line 37 (note that the naming is once again misleading by calling it 'passphrase', even though it is actually the wrapped passphrase), we can recover the recovery passphrase by unwrapping the returned value with our recovery code. The plain passphrase can then ultimately be used to unwrap the wrapped private keys, effectively leading to their plain versions.

It's important to note that all these unwrapping operations can be done purely client-side without making the server aware of anything further. The multi-step process must be followed through to the end of step 2, but can then be freely aborted.

As a result of Swisscom's fix, the recovery code is now directly consumed at step 2.

### Conclusion / Takeaway

After going through these two vulnerabilities, it could be reasonably thought that making sense of the entire MyCloud Safe implementation actually was the most difficult part. It is by understanding how the passphrase was used in relation to private keys that diving into the passphrase reset feature looked promising. Similarly, it is by understanding how recovery codes are involved in the account recovery that spotting a shortcut in the associated process happened quite naturally.

That being said, one could wonder how to develop this understanding of a system. It turns out that an effective way for that is to interact with the application as a regular user would in the first place and question things extensively in the process. When testing MyCloud Safe for the first time, the very first thing that struck me was that the password/passphrase submission didn't trigger any HTTP request. The endpoint `/safe` would have been previously fetched, and after that: nothing. Since I wasn't expecting this behavior, this made me directly curious about it and led me to start inspecting the responsible client-side javascript files.

Coming back to "questioning everything", what I mean is that as you go through the application, you would want to minimize the amount of obscure and misunderstood points, which could consist of specific parameters, cookies, or headers; the role of a request in a long multi-step process; a whole feature, etc. Proceeding so is particularly relevant for finding generally more impactful and complex vulnerabilities. To bring light to darkness, doing the following could prove to be very helpful:

  1. Reading JavaScript files, particularly for apps with heavy client-side logic.
  2. Reading documentation (or the _Help_ section) when available.
  3. Asking LLMs (Claude 3 / GPT 4 at the time this post is written — it may happily become outdated soon :D).
  4. Fuzzing / providing unexpected inputs.

Note that some classes of bugs might be less concerned about the need to deeply understand an app — I'm thinking about most basic XSS where a hunter's identification strategy would be to spray payloads everywhere, or IDORs if one's strategy is to swap IDs without questioning that much what's happening, etc. It's still very dependent on the tester's methodology, and it's surely the case that a mindful hacker would still manage to identify some instances of these bug classes while all others missed them. I'm particularly thinking here about researchers like [Youssef Sammouda](https://twitter.com/samm0uda) consistently finding XSS and escalating them to account takeover on Meta, or ZWink (not on social media anymore), who at a time found $150K worth of IDORs in Pinterest.

One last thing I want to share here, also with the purpose of making me think about it more often: people shouldn't be afraid of hacking on complex applications/systems!

There are two reasons for that:

  1. The more difficult and complex something looks, the higher the chances that the developers and designers got it wrong. The more features, different ways of interaction, roles, and permissions, the more room for errors and creative bugs. Really!
  2. As complexity brings a higher barrier to entry, there inherently is less competition there. Other hackers could either not trust their skills enough or not be in the right mental state to fully commit and focus on one particular thing — preferring quick wins. Hackers relying a lot on automation or semi-automation could also find it harder to deploy there. We can greatly benefit from all of this!

I guess that's all I had to say.

Thanks for reading! <3

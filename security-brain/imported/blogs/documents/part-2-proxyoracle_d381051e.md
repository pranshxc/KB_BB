---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-18_part-2-proxyoracle.md
original_filename: 2021-08-18_part-2-proxyoracle.md
title: Part 2 - ProxyOracle!
category: documents
detected_topics:
- access-control
- xss
- ssrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- xss
- ssrf
- command-injection
- otp
- api-security
language: en
raw_sha256: d381051e556fb66fdb4eb65ddffa241b5b7a99dd91968cf2bfb12a97e9e5609c
text_sha256: 84a2503ff3079784f03fdddbab60216385be7e42eadab96898ee0a837ab9bbb6
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Part 2 - ProxyOracle!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-18_part-2-proxyoracle.md
- Source Type: markdown
- Detected Topics: access-control, xss, ssrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d381051e556fb66fdb4eb65ddffa241b5b7a99dd91968cf2bfb12a97e9e5609c`
- Text SHA256: `84a2503ff3079784f03fdddbab60216385be7e42eadab96898ee0a837ab9bbb6`


## Content

---
title: "Part 2 - ProxyOracle!"
page_title: "A New Attack Surface on MS Exchange Part 2 - ProxyOracle! | DEVCORE"
url: "https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-2-ProxyOracle/"
final_url: "https://devco.re/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-2-ProxyOracle/"
authors: ["Orange Tsai (@orange_8361)"]
programs: ["Microsoft"]
bugs: ["RCE", "Privilege escalation"]
bounty: "200,000"
publication_date: "2021-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3409
---

[Tech Editorials](/en/blog/category/Tech Editorials) [#Advisory](/en/blog/tag/Advisory/) [#CVE](/en/blog/tag/CVE/) [#RCE](/en/blog/tag/RCE/) [#Exchange](/en/blog/tag/Exchange/)

#  A New Attack Surface on MS Exchange Part 2 - ProxyOracle! 

[ __ ](/en/blog/author/orange) [Orange Tsai](/en/blog/author/orange) 2021-08-06

![](https://devco.re/assets/img/blog/20210806/2/cover.png)

* * *

Hi, this is the part 2 of the New MS Exchange Attack Surface. Because this article refers to several architecture introductions and attack surface concepts in the previous article, you could find the first piece here:

  * [A New Attack Surface on MS Exchange Part 1 - ProxyLogon!](/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/)

This time, we will be introducing ProxyOracle. Compared with ProxyLogon, ProxyOracle is an interesting exploit with a different approach. By simply leading a user to visit a malicious link, ProxyOracle allows an attacker to recover the user’s password in plaintext format completely. ProxyOracle consists of two vulnerabilities:

  * [CVE-2021-31195](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31195) \- Reflected Cross-Site Scripting
  * [CVE-2021-31196](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31196) \- Padding Oracle Attack on Exchange Cookies Parsing

# Where is ProxyOracle

So where is ProxyOracle? Based on the CAS architecture we introduced before, the Frontend of CAS will first serialize the User Identity to a string and put it in the header of `X-CommonAccessToken`. The header will be merged into the client’s HTTP request and sent to the Backend later. Once the Backend receives, it deserializes the header back to the original User Identity in Frontend.

We now know how the Frontend and Backend synchronize the User Identity. The next is to explain how the Frontend knows who you are and processes your credentials. The Outlook Web Access (OWA) uses a fancy interface to handle the whole login mechanism, which is called Form-Based Authentication (FBA). The FBA is a special IIS module that inherits the `ProxyModule` and is responsible for executing the transformation between the credentials and cookies before entering the proxy logic.

![](/assets/img/blog/20210806/2/1.png)

# The FBA Mechanism

HTTP is a stateless protocol. To keep your login state, FBA saves the username and password in cookies. Every time you visit the OWA, Exchange will parse the cookies, retrieve the credential and try to log in with that. If the login succeed, Exchange will serialize your User Identity into a string, put it into the header of `X-CommonAccessToken`, and forward it to the Backend

**HttpProxy\FbaModule.cs**
  
  
  protected override void OnBeginRequestInternal(HttpApplication httpApplication) {
  
  httpApplication.Context.Items["AuthType"] = "FBA";
  if (!this.HandleFbaAuthFormPost(httpApplication)) {
  try {
  this.ParseCadataCookies(httpApplication);
  } catch (MissingSslCertificateException) {
  NameValueCollection nameValueCollection = new NameValueCollection();
  nameValueCollection.Add("CafeError", ErrorFE.FEErrorCodes.SSLCertificateProblem.ToString());
  throw new HttpException(302, AspNetHelper.GetCafeErrorPageRedirectUrl(httpApplication.Context, nameValueCollection));
  }
  }
  base.OnBeginRequestInternal(httpApplication);
  }
  

All the cookies are encrypted to ensure even if an attacker can hijack the HTTP request, he/she still couldn’t get your credential in plaintext format. FBA leverages 5 special cookies to accomplish the whole de/encryption process:

  * `cadata` \- The encrypted username and password
  * `cadataTTL` \- The Time-To-Live timestamp
  * `cadataKey` \- The KEY for encryption
  * `cadataIV` \- The IV for encryption
  * `cadataSig` \- The signature to prevent tampering

![](/assets/img/blog/20210806/2/2.png)

The encryption logic will first generate two 16 bytes random strings as the IV and KEY for the current session. The username and password will then be encoded with Base64, encrypted by the algorithm AES and sent back to the client within cookies. Meanwhile, the IV and KEY will be sent to the user, too. To prevent the client from decrypting the credential by the known IV and KEY directly, Exchange will once again use the algorithm RSA to encrypt the IV and KEY via its SSL certificate private key before sending out!

Here is a Pseudo Code for the encryption logic:
  
  
  @key = GetServerSSLCert().GetPrivateKey()
  cadataSig = RSA(@key).Encrypt("Fba Rocks!")
  cadataIV  = RSA(@key).Encrypt(GetRandomBytes(16))
  cadataKey = RSA(@key).Encrypt(GetRandomBytes(16))
  
  @timestamp = GetCurrentTimestamp()
  cadataTTL  = AES_CBC(cadataKey, cadataIV).Encrypt(@timestamp)
  
  @blob  = "Basic " + ToBase64String(UserName + ":" + Password)
  cadata = AES_CBC(cadataKey, cadataIV).Encrypt(@blob)
  

The Exchange takes CBC as its padding mode. If you are familiar with Cryptography, you might be wondering whether the CBC mode here is vulnerable to the Padding Oracle Attack? Bingo! As a matter of fact, Padding Oracle Attack is still existing in such essential software like Exchange in 2021!

![](/assets/img/blog/20210806/2/3.gif)

# CVE-2021-31196 - The Padding Oracle

When there is something wrong with the FBA, Exchange attaches an error code and redirects the HTTP request back to the original login page. So where is the Oracle? In the cookie decryption, Exchange uses an exception to catch the Padding Error, and because of the exception, the program returned immediately so that error code number is `0`, which means `None`:

> Location: /OWA/logon.aspx?url=…&reason=0

In contrast with the Padding Error, if the decryption is good, Exchange will continue the authentication process and try to login with the corrupted username and password. At this moment, the result must be a failure and the error code number is `2`, which represents `InvalidCredntials`:

> Location: /OWA/logon.aspx?url=…&reason=2

The diagram looks like:

![](/assets/img/blog/20210806/2/4.png)

With the difference, we now have an Oracle to identify whether the decryption process is successful or not.

**HttpProxy\FbaModule.cs**
  
  
  private void ParseCadataCookies(HttpApplication httpApplication)
  {
  HttpContext context = httpApplication.Context;
  HttpRequest request = context.Request;
  HttpResponse response = context.Response;
  
  string text = request.Cookies["cadata"].Value;  
  string text2 = request.Cookies["cadataKey"].Value;  
  string text3 = request.Cookies["cadataIV"].Value;  
  string text4 = request.Cookies["cadataSig"].Value;  
  string text5 = request.Cookies["cadataTTL"].Value;
  
  // ...
  RSACryptoServiceProvider rsacryptoServiceProvider = (x509Certificate.PrivateKey as RSACryptoServiceProvider);
  
  byte[] array = null;
  byte[] array2 = null;
  byte[] rgb2 = Convert.FromBase64String(text2);
  byte[] rgb3 = Convert.FromBase64String(text3);
  array = rsacryptoServiceProvider.Decrypt(rgb2, true);
  array2 = rsacryptoServiceProvider.Decrypt(rgb3, true);
  
  // ...
  
  using (AesCryptoServiceProvider aesCryptoServiceProvider = new AesCryptoServiceProvider()) {
  aesCryptoServiceProvider.Key = array;
  aesCryptoServiceProvider.IV = array2;
  
  using (ICryptoTransform cryptoTransform2 = aesCryptoServiceProvider.CreateDecryptor()) {
  byte[] bytes2 = null;
  try {
  byte[] array5 = Convert.FromBase64String(text);
  bytes2 = cryptoTransform2.TransformFinalBlock(array5, 0, array5.Length);
  } catch (CryptographicException ex8) {
  if (ExTraceGlobals.VerboseTracer.IsTraceEnabled(1)) {
  ExTraceGlobals.VerboseTracer.TraceDebug<CryptographicException>((long)this.GetHashCode(), "[FbaModule::ParseCadataCookies] Received CryptographicException {0} transforming auth", ex8);
  }
  httpApplication.Response.AppendToLog("&CryptoError=PossibleSSLCertrolloverMismatch");
  return;
  } catch (FormatException ex9) {
  if (ExTraceGlobals.VerboseTracer.IsTraceEnabled(1)) {
  ExTraceGlobals.VerboseTracer.TraceDebug<FormatException>((long)this.GetHashCode(), "[FbaModule::ParseCadataCookies] Received FormatException {0} decoding caData auth", ex9);
  }
  httpApplication.Response.AppendToLog("&DecodeError=InvalidCaDataAuthCookie");
  return;
  }
  string @string = Encoding.Unicode.GetString(bytes2);
  request.Headers["Authorization"] = @string;
  }
  }
  }
  

It should be noted that since the IV is encrypted with the SSL certificate private key, we can’t recover the first block of the ciphertext through XOR. But it wouldn’t cause any problem for us because the C# internally processes the strings as UTF-16, so the first 12 bytes of the ciphertext must be `B\x00a\x00s\x00i\x00c\x00 \x00`. With one more Base64 encoding applied, we will only lose the first 1.5 bytes in the username field.

> (16−6×2) ÷ 2 × (3/4) = 1.5

# The Exploit

As of now, we have a Padding Oracle that allows us to decrypt any user’s cookie. BUT, how can we get the client cookies? Here we find another vulnerability to chain them together.

## XSS to Steal Client Cookies

We discover an XSS (CVE-2021-31195) in the CAS Frontend (Yeah, CAS again) to chain together, the root cause of this XSS is relatively easy: Exchange forgets to sanitize the data before printing it out so that we can use the `\` to escape from the JSON format and inject arbitrary JavaScript code.
  
  
  https://exchange/owa/auth/frowny.aspx
  ?app=people
  &et=ServerError
  &esrc=MasterPage
  &te=\
  &refurl=}}};alert(document.domain)//
  

![](/assets/img/blog/20210806/2/5.png)

But here comes another question: all the sensitive cookies are protected by the HttpOnly flag, which makes us unable to access the cookies by JavaScript. WHAT SHOULD WE DO?

## Bypass the HttpOnly

As we could execute arbitrary JavaScript on browsers, why don’t we just insert the SSRF cookie we used in ProxyLogon? Once we add this cookie and assign the Backend target value as our malicious server, Exchange will become a proxy between the victims and us. We can then take over all the client’s HTTP static resources and get the protected HttpOnly cookies!

![](/assets/img/blog/20210806/2/6.png)

By chaining bugs together, we have an elegant exploit that can steal any user’s cookies by just sending him/her a malicious link. What’s noteworthy is that the XSS here is only helping us to steal the cookie, which means all the decryption processes wouldn’t require any authentication and user interaction. Even if the user closes the browser, it wouldn’t affect our Padding Oracle Attack!

Here is the [demonstration video](https://www.youtube.com/watch?v=VuJvmJZxogc) showing how we recover the victim’s password:

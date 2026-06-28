---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-17_mtls-when-certificate-authentication-is-done-wrong.md
original_filename: 2023-08-17_mtls-when-certificate-authentication-is-done-wrong.md
title: 'mTLS: When certificate authentication is done wrong'
category: documents
detected_topics:
- oauth
- jwt
- access-control
- command-injection
- supply-chain
- saml
tags:
- imported
- documents
- oauth
- jwt
- access-control
- command-injection
- supply-chain
- saml
language: en
raw_sha256: 03213795e7d494aa26eab67157fc8a2db997303a1f39f8df6ba262bedadb5811
text_sha256: 5122072ec0f5db4b3270a5c587902c707a386050cd42c408228069c08897fe72
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: true
---

# mTLS: When certificate authentication is done wrong

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-17_mtls-when-certificate-authentication-is-done-wrong.md
- Source Type: markdown
- Detected Topics: oauth, jwt, access-control, command-injection, supply-chain, saml
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: True
- Raw SHA256: `03213795e7d494aa26eab67157fc8a2db997303a1f39f8df6ba262bedadb5811`
- Text SHA256: `5122072ec0f5db4b3270a5c587902c707a386050cd42c408228069c08897fe72`


## Content

---
title: "mTLS: When certificate authentication is done wrong"
page_title: "mTLS: When certificate authentication is done wrong - The GitHub Blog"
url: "https://github.blog/2023-08-17-mtls-when-certificate-authentication-is-done-wrong/"
final_url: "https://github.blog/security/vulnerability-research/mtls-when-certificate-authentication-is-done-wrong/"
authors: ["Michael Stepankin (@artsploit)"]
programs: ["Keycloak", "Bouncy Castle", "Apereo CAS"]
bugs: ["mTLS", "Improper Certificate Validation", "LDAP injection", "SSRF"]
publication_date: "2023-08-17"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 851
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# mTLS: When certificate authentication is done wrong

In this post, we’ll deep dive into some interesting attacks on mTLS authentication. We’ll have a look at implementation vulnerabilities and how developers can make their mTLS systems vulnerable to user impersonation, privilege escalation, and information leakages.

![](https://github.blog/wp-content/uploads/2023/04/1200.630-Global@2x-1.png?resize=1200%2C630)

[Michael Stepankin](https://github.blog/author/artsploit/ "Posts by Michael Stepankin")·[@artsploit](https://github.com/artsploit)

August 17, 2023 

| 15 minutes 

  * Share: 
  * [ ](https://x.com/share?text=mTLS%3A%20When%20certificate%20authentication%20is%20done%20wrong&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fmtls-when-certificate-authentication-is-done-wrong%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=mTLS%3A%20When%20certificate%20authentication%20is%20done%20wrong&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fmtls-when-certificate-authentication-is-done-wrong%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=mTLS%3A%20When%20certificate%20authentication%20is%20done%20wrong&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fmtls-when-certificate-authentication-is-done-wrong%2F)

Although [X.509](https://en.wikipedia.org/wiki/X.509) certificates have been here for a while, they have become more popular for client authentication in zero-trust networks in recent years. Mutual TLS, or authentication based on X.509 certificates in general, brings advantages compared to passwords or tokens, but you get increased complexity in return.

In this post, I’ll deep dive into some interesting attacks on mTLS authentication. We won’t bother you with heavy crypto stuff, but instead we’ll have a look at implementation vulnerabilities and how developers can make their mTLS systems vulnerable to user impersonation, privilege escalation, and information leakages.

We will present some CVEs we found in popular open-source identity servers and ways to exploit them. Finally, we’ll explain how these vulnerabilities can be spotted in source code and how to fix them.

This blog post is based on work that I recently presented at [Black Hat USA](https://www.blackhat.com/us-23/briefings/schedule/#mtls-when-certificate-authentication-is-done-wrong-33203) and [DEF CON](https://media.defcon.org/DEF%20CON%2031/DEF%20CON%2031%20presentations/Michael%20Stepankin%20-%20mTLS%20when%20certificate%20authentication%20done%20wrong.pdf).

## Introduction: What is mutual TLS?

Website certificates are a very widely recognized technology, even to people who don’t work in the tech industry, thanks to the padlock icon used by web browsers. Whenever we connect to Gmail or GitHub, our browser checks the certificate provided by the server to make sure it’s truly the service we want to talk to. Fewer people know that the same technology can be used to authenticate clients: the TLS protocol is also designed to be able to verify the client using public and private key cryptography.

It happens on the handshake level, even before any application data is transmitted:

![Excerpt from RFC 5246: "Figure 1. Message flow for a full handshake"](https://github.blog/wp-content/uploads/2023/08/mtls-1.png?w=1024&resize=1024%2C597)

If configured to do so, a server can ask a client to provide a security certificate in the X.509 format. This certificate is just a blob of binary data that contain information about the client, such as its name, public key, issuer, and other fields:
  
  
  $ openssl x509 -text -in client.crt
  Certificate:
  Data:
  Version: 1 (0x0)
  Serial Number:
  d6:2a:25:e3:89:22:4d:1b
  Signature Algorithm: sha256WithRSAEncryption
  Issuer: CN=localhost  //used to locate issuers certificate
  Validity
  Not Before: Jun 13 14:34:28 2023 GMT
  Not After : Jul 13 14:34:28 2023 GMT
  Subject: CN=client  //aka "user name"
  Subject Public Key Info:
  Public Key Algorithm: rsaEncryption
  RSA Public-Key: (2048 bit)
  Modulus:
  00:9c:7c:b4:e5:e9:3d:c1:70:9c:9d:18:2f:e8:a0:
  

The server checks that this certificate is signed by one of the trusted authorities. This is a bit similar to checking the signature of a JWT token. Next, the client sends a “Certificate verify” message encrypted with the private key, so that the server can verify that the client actually has the private key.

### How certificates are validated

“Certificate validation” commonly refers to the PKIX certificate validation process defined in [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280).

In short, in order to validate the certificate, the server constructs a certification path (also known as a certificate chain) from the target certificate to a trust anchor. The trust anchor is a self-signed root certificate that is inherently trusted by the validator. The end entity certificate is often signed by an intermediate CA, which is also signed by another intermediate certificate or directly by a trust anchor.

![Diagram of certificate chain with three links: Client certificate, Intermediate CA, Root Certificate Authority](https://github.blog/wp-content/uploads/2023/08/mtls-2.png?w=1024&resize=1024%2C518)

Then, for each certificate in the chain, the validator checks the signature, validity period, allowed algorithms and key lengths, key usage, and other properties. There are also a number of optional certificate extensions: if they are included in the certificate, they can be checked as well. This process is quite complicated, so every language or library implements it differently.

Note: in my research I mostly looked at how mTLS is implemented in applications written in Java, but it is likely that the ideas and attacks below apply to other languages as well.

### mTLS in a Java web application, an example

Let’s see how to use mTLS in a Java web application. The bare minimum configuration is to enable it in the application settings and specify the location of all trusted root certificates, like this:
  
  
  $ cat application.properties
  
  …
  server.ssl.client-auth=need
  server.ssl.trust-store=/etc/spring/server-truststore.p12
  server.ssl.trust-store-password=***REDACTED***
  

From the client, such as curl, you need to specify which certificate is sent to the server. The rest of the application code, such as request mappings, is exactly the same as for a normal web application.
  
  
  $ curl -k -v –cert client.pem http://localhost/hello
  

This setup works for very simple mTLS configurations, when there is only a single root certificate, and all client certificates are signed by it. You can find this example in various articles on the web and it’s quite secure due to its simplicity. Let’s quickly break down its pros and cons.

#### Pros:

  * Speed: Authorization happens only during TLS handshake, all subsequent “keep-alive” HTTP requests are considered authenticated, saving CPU time.
  * Storage: Similar to JWT, the server does not store all client certificates, only the root certificate.

#### Cons:

  * No granular control: if mTLS is enabled, all requests have to be authenticated, even to `/static/style.css`.
  * Any certificate signed by a trusted CA can be used to access this HTTP service. Even if the certificate is issued for another purpose, it still can potentially be used for TLS authentication.
  * No host verification by default: client certificates can be accepted from any IP.
  * Certificate issuance process needs to be implemented separately.
  * Certificates expire, so need to be rotated frequently.

As you can see, this approach brings some advantages and disadvantages compared to traditional authentication methods, such as password or tokens.

### Previous attacks

Before we dive into the attack section, I’ll briefly mention some previous well-known attacks on certificate parsing and validation:

  * Obviously, the security of the authentication system depends on the strength of the signature. If we can somehow forge the content of the certificate, but keep the same signature, we can completely break the authentication process. 
  * Since the X.509 format is quite complex, just parsing these data structures can lead to buffer and heap overflows. 
  * Lack of basic constraints checking. The end-entity certificates should not be used to sign additional certificates.

### My approach

In Java, most of these attacks are already mitigated in APIs provided by the JDK. Weak algorithms are intentionally not allowed. Fuzzing of certificate parsing in Java also did not look productive to me, as the vast majority of PKIX code is implemented in memory-safe Java, instead of using native libraries. I had to take a different approach, so I decided to have a deep look at how mTLS is used from the source code perspective. Since the certificate validation process is quite complex, I suspected that someone might implement it in a weird way. After several weeks, it yielded me some interesting vulnerabilities in popular open source projects.

So, let’s move on to the attack’s section.

## Chapter 1: Improper certificate extraction

In real-life applications, developers often need to access the certificate presented during the TLS handshake. For example, they might need it for authorization purposes, such as checking the current username. In Java, there are two common ways how to access it:
  
  
  X509Certificate[] certificates = sslSession.getPeerCertificates();  
  
  // another way
  X509Certificate[] certificates = request.getAttribute("javax.servlet.request.X509Certificate");
  

Interestingly, this API returns an array of certificates presented by the client, not a single one. Why? Perhaps because TLS specification defines that clients may send a full chain of certificates, from end-entity to the root CA.

So, I decided to take a look at how different applications use this API. The most common approach I’ve seen is to take only the first certificate from the array and consider it as the client certificate. This is correct, as mTLS RFC explicitly says that the sender’s certificate MUST come first in the list.
  
  
  //way 1 is good
  String user = certificates[0].getSubjectX500Principal().getName();
  

At the same time, I discovered some rare cases when applications disregard this rule and iterate over the array trying to find a certificate that matches some criteria.
  
  
  //way 2 is dangerous
  for (X509Certificate cert : certificates) {
  if (isClientCertificate(cert)) {
  user = cert.getSubjectX500Principal().getName();
  }
  }
  

This is dangerous, as the underlying TLS library in Java only verifies the first certificate in the list. Moreover, it does not require the chain to be sent in a strict order.

### Example: CVE-2023-2422 improper certificate validation in KeyCloak

One of these examples was a vulnerability I discovered in Keycloak. Keycloak is a popular authorization server that supports OAuth, SAML, and other authorization methods, as well as mutual TLS.

Keycloak iterates over all certificates in the array, searching for the one that matches the client_id form parameter. As soon as it finds a matching certificate, it implicitly trusts it, assuming that its signature has already been checked during the TLS handshake:
  
  
  X509Certificate[] certs = null;
  ClientModel client = null;
  try { 
  certs = provider.getCertificateChain(context.getHttpRequest());
  String client_id = null;
  ...
  if (formData != null) {
  client_id = formData.getFirst(OAuth2Constants.CLIENT_ID);
  }
  …
  matchedCertificate = Arrays.stream(certs)
  .map(certificate -> certificate.getSubjectDN().getName())
  .filter(subjectdn -> subjectDNPattern.matcher(subjectdn).matches())
  .findFirst();
  

In reality, a client can send as many certificates as they want, and the server only verifies the first one.

A potential attacker can exploit this behavior to authenticate under a different username. It is possible to send a list of certificates, where the first one contains one username and is properly chained to a root CA. But the last certificate in the array might be self signed and belong to a different user. The client does not even need to provide a valid private key for it.

![Diagram of a certificate list in which the first client certificate is signed by a CA, but the second is self-signed.](https://github.blog/wp-content/uploads/2023/08/mtls-3.png?w=1024&resize=1024%2C582)

Speaking about the exploitation, there are a number of endpoints in Keycloak that support mTLS authentication, but we need one that does not require any additional factors, such as tokens or secrets. “client-management/register-node” is a good example, as it mutates the user’s data. We can normally use this api with mTLS in the following way:
  
  
  $ cat client1.crt client1.key > chain1.pem
  $ curl --tlsv1.2 --tls-max 1.2 --cert chain1.pem -v -i -s -k "https://127.0.0.1:8443/realms/master/clients-managements/register-node?client_id=client1" -d "client_cluster_host=http://127.0.0.1:1213/"
  

To demonstrate the vulnerability, we generate a new self signed certificate using openssl and add it to the end of the array.
  
  
  $ openssl req -newkey rsa:2048 -nodes -x509 -subj /CN=client2 -out client2-fake.crt
  $ cat client1.crt client1.key client2-fake.crt client1.key > chain2.pem
  $ curl --tlsv1.2 --tls-max 1.2 --cert chain2.pem -v -i -s -k "https://127.0.0.1:8443/realms/master/clients-managements/register-node?client_id=client2" -d "client_cluster_host=http://127.0.0.1:1213/"
  

When we send the second curl request, Keycloak performs this action on behalf of the user specified in `client2-fake.crt`, instead of `client1.crt`. Therefore, we can mutate data on the server for any client that supports mTLS.

How to fix that? Easy: just use the first certificate from the array. That’s exactly how Keycloak patched this vulnerability. This CVE is a good example of how developers provide methods and interfaces that can be misunderstood or used incorrectly.

### Passing certificate as a header

Another common scenario for mTLS deployments is when the TLS connection is terminated on a reverse proxy. In this case, the reverse proxy often checks the certificate and forwards it to a backend server as an additional header. Here is a typical nginx configuration to enable mTLS:
  
  
  $ cat nginx.conf
  
  http {
  server {
  server_name example.com;
  listen 443 ssl;
  …
  ssl_client_certificate /etc/nginx/ca.pem;
  ssl_verify_client on;
  
  location / {
  proxy_pass http://host.internal:80;
  proxy_set_header ssl-client-cert $ssl_client_cert;
  }
  }
  

I’ve seen a number of systems like that, and in most cases the backend servers behind nginx do not perform additional validation, just trusting the reverse proxy. This behavior is not directly exploitable, but it’s not ideal either. Why? Well, first of all, it means that any server in the local network can make a request with this header, so this network segment needs to be carefully isolated from any traffic coming from outside. Additionally, if the backend or reverse proxy is affected by request smuggling or header injection, its exploitation becomes trivial. Over the past few years, we’ve seen a lot of request and header smuggling vulnerabilities, including the latest CVEs in [Netty](https://github.com/netty/netty/security/advisories/GHSA-wm47-8v5p-wjpj) and [Nodejs](https://github.com/advisories/GHSA-cggh-pq45-6h9x). Be careful when implementing these scenarios and check the certificate’s signature on all servers if possible.

## Chapter 2: “Follow the chain, where does it lead you?”

![Excerpt from RFC 4158: "Figure 1 - Sample Hierarchical PKI"](https://github.blog/wp-content/uploads/2023/08/mtls-4.png?w=1024&resize=1024%2C744)

In large systems, servers may not store all root and intermediate certificates locally, but use external storage instead. [RFC 4387](https://datatracker.ietf.org/doc/html/rfc4387) explains the concept of a certificate store: an interface you can use to lazily access certificates during chain validation. These stores are implemented over different protocols, such as HTTP, LDAP, FTP, or SQL queries.

[RFC 3280 defines](https://www.rfc-editor.org/rfc/rfc3280.html#section-5.2) some X.509 certificate extensions that can contain information about where to find the issuer and CA certificates. For instance, the Authority Information Access (AIA) extension contains a URL pointing to the Issuer’s certificate. If this extension is used for validation, there is a high chance that you can exploit it to perform an SSRF attack. Also, Subject, Issuer, Serial, and their alternative names can be used to construct SQL or LDAP queries, creating opportunities for injection attacks.

![Client certificate with an AIA extension, containing a link to http://example.com](https://github.blog/wp-content/uploads/2023/08/mtls-5.png?w=1024&resize=1024%2C729)

When certificate stores are in use, you should think of these values as “untrusted user input” or “Insertion points,” similar to those we have in Burp Suite’s Intruder. And what attackers will really love is that all of these values can be used in queries _before_ the signature is checked.

### Example: CVE-2023-33201 LDAP injection in Bouncy Castle

To demonstrate an example of this vulnerability, we’ll use [LDAPCertStore](https://github.com/bcgit/bc-java/blob/main/prov/src/main/java/org/bouncycastle/jce/provider/X509LDAPCertStoreSpi.java) from the Bouncy Castle library. Bouncy Castle is one of the most popular libraries for certificate validation in Java. Here is an example of how you can use this store to build and validate a certificate chain.
  
  
  PKIXBuilderParameters pkixParams = new PKIXBuilderParameters(keystore, selector);
  
  //setup additional LDAP store
  X509LDAPCertStoreParameters CertStoreParameters = new X509LDAPCertStoreParameters.Builder("ldap://127.0.0.1:1389", "CN=certificates").build();
  CertStore certStore = CertStore.getInstance("LDAP", CertStoreParameters, "BC");
  pkixParams.addCertStore(certStore);
  
  // Build and verify the certification chain
  try {
  CertPathBuilder builder = CertPathBuilder.getInstance("PKIX", "BC");
  PKIXCertPathBuilderResult result =
  (PKIXCertPathBuilderResult) builder.build(pkixParams);
  

Under the hood, Bouncy Castle uses the Subject field from the certificate to build an LDAP query. The Subject field is inserted in the filter, without—you guessed it—any escaping.

![Client certificate containing the text "Subject: CN=Client*\)\(userPassword=***REDACTED***](https://github.blog/wp-content/uploads/2023/08/mtls-6.png?w=1024&resize=1024%2C470)

So, if the Subject contains any special characters, it can change the syntax of the query. In most cases, this can be exploited as a blind ldap query injection. Therefore, it might be possible to use this vulnerability to extract other fields from the LDAP directory. The exploitability depends on many factors, including whether the application exposes any errors or not, and it also depends on the structure of the LDAP directory.

In general, whenever you incorporate user-supplied data into an LDAP query, special characters should be properly filtered. That’s exactly how this CVE has been patched in the Bouncy Castle code.

## Chapter 3: Certificate revocation and its unintended uses

Similar to Json web tokens, the beauty of certificate chains is that they can be trusted just based on their signature. But what happens if we need to revoke a certificate, so it can no longer be used?

The PKIX specification ([RFC 4387](https://www.rfc-editor.org/rfc/rfc4387.html)) addresses this problem by proposing a special store for revoked certificates, accessible via HTTP or LDAP protocols. Many developers believe that revocation checking is absolutely necessary, whereas others urge to avoid it for performance reasons or only use offline revocation lists.

Generally speaking, the store location can be hardcoded into the application or taken from the certificate itself. There are two certificate extensions used for that: Authority Information Access OSCP URL and CRL Distribution points.

![Client certificate containing URLs in its AIA OSCL and CRL Distribution points.](https://github.blog/wp-content/uploads/2023/08/mtls-7.png?w=816&resize=816%2C500)

Looking at it from the hackers point of view, I think it’s _incredible_ that the location of the revocation server can be taken from the certificate. So, if the application takes URLs relying on AIA or CRLDP extension to make a revocation check, it can be abused for SSRF attacks.

Sadly for attackers, this normally happens after the signature checks, but in some cases it’s still exploitable.

Moreover, LDAP is also supported, at least in Java. You probably heard that, in Java, unmarshaling an LDAP lookup response can lead to a remote code execution. A few years back, [Moritz Bechler](https://github.com/mbechler) reported this problem and remote code execution via revocation has since been patched in the JDK. You can check out [his blog post](https://mbechler.github.io/2018/01/20/Java-CVE-2018-2633/) for more details.

In my research, I decided to check if the Bouncy Castle library is also affected. It turns out that Bouncy Castle can be configured to use the CRLDP extension and make calls to an LDAP server. At the same time, Bouncy Castle only fetches a specific attribute from the LDAP response and does not support references. So, remote code execution is not possible there. HTTP SSRF is still viable though.
  
  
  private static Collection getCrlsFromLDAP(CertificateFactory certFact, URI distributionPoint) throws IOException, CRLException
  {
  Map<String, String> env = new Hashtable<String, String>();
  
  env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
  env.put(Context.PROVIDER_URL, distributionPoint.toString());
  
  byte[] val = null;
  try
  {
  DirContext ctx = new InitialDirContext((Hashtable)env);
  Attributes avals = ctx.getAttributes("");
  Attribute aval = avals.get("certificateRevocationList;binary");
  val = (byte[])aval.get();
  }
  

### Example: CVE-2023-28857 credentials leak in Apereo CAS

I also had a quick look at open source projects that support mTLS and perform revocation checking. One of these projects was Apereo CAS. It’s another popular authentication server that is highly configurable. Administrators of Apereo CAS can enable the revocation check using an external LDAP server by specifying its address and password in the settings:
  
  
  cas.authn.x509.crl-fetcher=ldap
  cas.authn.x509.ldap.ldap-url=ldap://example.com:1389/
  cas.authn.x509.ldap.bind-dn=admin
  cas.authn.x509.ldap.bind-credential=s3cr3taaaaa
  

If these settings are applied, Apereo CAS performs the revocation check for the certificate, fetching the address from the certificate’s CRLDP extension.
  
  
  /**
  * Validate the X509Certificate received.
  *
  * @param cert the cert
  * @throws GeneralSecurityException the general security exception
  */
  private void validate(final X509Certificate cert) throws GeneralSecurityException {
  cert.checkValidity();
  this.revocationChecker.check(cert);
  
  val pathLength = cert.getBasicConstraints();
  if (pathLength < 0) {
  if (!isCertificateAllowed(cert)) {
  val msg = "Certificate subject does not match pattern " + this.regExSubjectDnPattern.pattern();
  LOGGER.error(msg);
  

I was afraid that this could lead to remote code execution, but it turns out that Apereo CAS uses a custom library for LDAP connection, which does not support external codebases or object factories needed for RCE.

When I tested this in Apereo CAS, I noticed one interesting behavior. The server prefers the LDAP URL located **inside the certificate** , instead of the one that is configured in settings. At the same time, Apereo CAS still sends the password from the settings. I quickly set up a testing environment and sent a self-signed certificate in the header. My self-signed certificate had a CRLDP extension with the LDAP URL pointing to a netcat listener. After sending this request to Apereo CAS, I received a request to my netcat listener with the username and password leaked.

![Pair of screenshots: the first contains a POST request to Apereo CAS and the second is a terminal running netcat.](https://github.blog/wp-content/uploads/2023/08/mtls-8.png?w=1024&resize=1024%2C673)

After reporting this vulnerability, the application developers issued a fix within just one day. They patched it by clearing the login and password used for LDAP connection if the URL is taken from the CRLDP. Therefore, the password leak is no longer possible. Nevertheless, I would say that using URLs from the CRLDP extension is still dangerous, as it broadens the attack surface.

## Summary

If you’re developing an mTLS system or performing a security assessment, I suggest:

  1. Pay attention when extracting usernames from the mTLS chain, as the servers only verify the first certificate in the chain.
  2. Use Certificate Stores with caution, as it can lead to LDAP and SQL injections.
  3. Certificate revocation can lead to SSRF or even to RCE in the worst case. So, do the revocation check only after all other checks and do not rely on URLs taken from the certificate extensions.

* * *

## Tags:

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

##  Written by 

![Michael Stepankin](https://avatars.githubusercontent.com/u/44605151?v=4&s=200)

###  [Michael Stepankin](https://github.blog/author/artsploit/)

[@artsploit](https://github.com/artsploit)

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

## More on [GitHub Security Lab](https://github.blog/tag/github-security-lab/)

### [Hack the AI agent: Build agentic AI security skills with the GitHub Secure Code Game](https://github.blog/security/hack-the-ai-agent-build-agentic-ai-security-skills-with-the-github-secure-code-game/)

Learn to find and exploit real-world agentic AI vulnerabilities through five progressive challenges in this free, open source game that over 10,000 developers have already used to sharpen their security skills.

[Joseph Katsioloudes](https://github.blog/author/jkcso/ "Posts by Joseph Katsioloudes")

### [Securing the open source supply chain across GitHub](https://github.blog/security/supply-chain-security/securing-the-open-source-supply-chain-across-github/)

Recent attacks on open source focus on exfiltrating secrets; here are the prevention steps you can take today, plus a look at the security capabilities GitHub is working on.

[Zachary Steindler](https://github.blog/author/steiza/ "Posts by Zachary Steindler")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![GitHub Universe 2023](https://github.blog/wp-content/uploads/2023/08/Icon-Circle.svg)

###  GitHub Universe 2023 

Get free virtual tickets to the global developer event for AI, security, and DevEx.

[ Get free tickets ](https://githubuniverse.com/)

![GitHub Actions](https://github.blog/wp-content/uploads/2022/05/actions.svg)

###  GitHub Actions 

Native CI/CD alongside code hosted in GitHub.

[ Learn more ](https://github.com/features/actions)

![Enterprise content](https://github.blog/wp-content/uploads/2022/05/careers.svg)

###  Enterprise content 

Executive insights, curated just for you

[ Get started ](https://github.com/solutions/executive-insights)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe

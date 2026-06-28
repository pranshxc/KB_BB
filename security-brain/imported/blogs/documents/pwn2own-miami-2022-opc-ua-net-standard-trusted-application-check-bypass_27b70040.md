---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass.md
original_filename: 2022-07-19_pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass.md
title: 'Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass'
category: documents
detected_topics:
- command-injection
- automation-abuse
- access-control
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- access-control
- cloud-security
- supply-chain
language: en
raw_sha256: 27b70040d07b3f00613ae17748f51b5a0c040b4074a5e9b89d655800a05ef00e
text_sha256: d044899c4ce116783446559108a33fede5cc7656bc3b9c890cf5b8c90d5db93e
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, access-control, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `27b70040d07b3f00613ae17748f51b5a0c040b4074a5e9b89d655800a05ef00e`
- Text SHA256: `d044899c4ce116783446559108a33fede5cc7656bc3b9c890cf5b8c90d5db93e`


## Content

---
title: "Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass"
page_title: "Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2022-07-opc-ua-net-standard-trusted-application-check-bypass/"
final_url: "https://defion.security/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["OPC Foundation"]
bugs: ["Local Privilege Escalation"]
bounty: "40,000"
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2431
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass

Pwn2Own 19 July 2022 · 14 min read

# Pwn2Own Miami 2022: OPC UA .NET Standard Trusted Application Check Bypass

This write-up is part 1 of a series of write-ups about the 5 vulnerabilities we demonstrated last April at Pwn2Own Miami. This is the write-up for the Trusted Application Check Bypass in the OPC Foundation's OPC UA .NET Standard (CVE-2022-29865).

> [](https://twitter.com/thezdi/status/1516844610353565696)

OPC UA is a communication protocol used in the ICS world. It is an open standard developed by the OPC Foundation. Because it is implemented by many vendors, it is often the preferred protocol for setting up communication between systems from different vendors in an ICS network.

The security for OPC UA connections can be configured in three different ways: without any security, only signing and signing and encryption. In the latter two cases, both endpoints authenticate to each other using X.509 certificates. While these are the same type of certificates as used in TLS, the encryption protocol itself is custom and not based on TLS.

At Pwn2Own Miami 2022, four OPC UA servers were in scope, with three different "payload" options:

  * **Denial-of-Service.** Availability is everything in an ICS network, so being able to crash an OPC UA server can have significant impact.
  * **Remote code execution.** Being able to take over the server.
  * **Bypass Trusted Application Check.** Setting up a trusted connection to a server without having a valid certificate.

Of course, with a pre-authentication RCE it would be possible to modify the configuration of the server to change the security level and bypass the trusted application check that way, but this was not allowed.

## OPC UA .NET Standard

We looked at potential trusted certificate bypasses in all four servers in scope, we only found one in the server OPC UA .NET Standard. This server is used as a reference implementation for OPC UA in C# and is open source, meaning that this bypass could affect many ICS products that incorporate it as a library.

The core of the issue is in the function `InternalValidate` in [CertificateValidator.cs](https://github.com/OPCFoundation/UA-.NETStandard/blob/7072fe07717dc143a77c3cc71426904f661c55c8/Stack/Opc.Ua.Core/Security/Certificates/CertificateValidator.cs). The logic for verifying a certificate here is quite complicated, which likely contributed to a bug like this to be missed.

What we heard from the OPC Foundation is that the reason this check is so complicated is that they do not want to use the built-in certificate store of Windows. Instead, the certificates of the application can be managed by placing the certificate files in a specific directory on the server. The OPC UA specification has such a high level of detail that it even [suggests how to store those certificates](https://reference.opcfoundation.org/GDS/docs/F.1/).

The core issue here is that two different certificate chains are built without verifying that they are equal. By crafting a chain in a very specific way, it is possible to make the server accept it, even though it is not signed by a trusted root.
  
  
  protected virtual async Task InternalValidate(X509Certificate2Collection certificates, ConfiguredEndpoint endpoint)
  {
  X509Certificate2 certificate = certificates[0];
  
  // check for previously validated certificate.
  X509Certificate2 certificate2 = null;
  
  if (m_validatedCertificates.TryGetValue(certificate.Thumbprint, out certificate2))
  {
  if (Utils.IsEqual(certificate2.RawData, certificate.RawData))
  {
  return;
  }
  }
  
  CertificateIdentifier trustedCertificate = await GetTrustedCertificate(certificate).ConfigureAwait(false);
  
  // get the issuers (checks the revocation lists if using directory stores).
  List<CertificateIdentifier> issuers = new List<CertificateIdentifier>();
  Dictionary<X509Certificate2, ServiceResultException> validationErrors = new Dictionary<X509Certificate2, ServiceResultException>();
  
  bool isIssuerTrusted = await GetIssuersNoExceptionsOnGetIssuer(certificates, issuers, validationErrors).ConfigureAwait(false);
  
  ServiceResult sresult = PopulateSresultWithValidationErrors(validationErrors);
  
  // setup policy chain
  X509ChainPolicy policy = new X509ChainPolicy();
  policy.RevocationFlag = X509RevocationFlag.EntireChain;
  policy.RevocationMode = X509RevocationMode.NoCheck;
  policy.VerificationFlags = X509VerificationFlags.NoFlag;
  
  foreach (CertificateIdentifier issuer in issuers)
  {
  if ((issuer.ValidationOptions & CertificateValidationOptions.SuppressRevocationStatusUnknown) != 0)
  {
  policy.VerificationFlags |= X509VerificationFlags.IgnoreCertificateAuthorityRevocationUnknown;
  policy.VerificationFlags |= X509VerificationFlags.IgnoreCtlSignerRevocationUnknown;
  policy.VerificationFlags |= X509VerificationFlags.IgnoreEndRevocationUnknown;
  policy.VerificationFlags |= X509VerificationFlags.IgnoreRootRevocationUnknown;
  }
  
  // we did the revocation check in the GetIssuers call. No need here.
  policy.RevocationMode = X509RevocationMode.NoCheck;
  policy.ExtraStore.Add(issuer.Certificate);
  }
  
  // build chain.
  using (X509Chain chain = new X509Chain())
  {
  chain.ChainPolicy = policy;
  chain.Build(certificate);
  
  // check the chain results.
  CertificateIdentifier target = trustedCertificate;
  
  if (target == null)
  {
  target = new CertificateIdentifier(certificate);
  }
  
  for (int ii = 0; ii < chain.ChainElements.Count; ii++)
  {
  X509ChainElement element = chain.ChainElements[ii];
  
  CertificateIdentifier issuer = null;
  
  if (ii < issuers.Count)
  {
  issuer = issuers[ii];
  }
  
  // check for chain status errors.
  if (element.ChainElementStatus.Length > 0)
  {
  foreach (X509ChainStatus status in element.ChainElementStatus)
  {
  ServiceResult result = CheckChainStatus(status, target, issuer, (ii != 0));
  if (ServiceResult.IsBad(result))
  {
  sresult = new ServiceResult(result, sresult);
  }
  }
  }
  
  if (issuer != null)
  {
  target = issuer;
  }
  }
  }
  [...]

First, on line 883, [`GetIssuersNoExceptionsOnGetIssuer`](https://github.com/OPCFoundation/UA-.NETStandard/blob/7072fe07717dc143a77c3cc71426904f661c55c8/Stack/Opc.Ua.Core/Security/Certificates/CertificateValidator.cs#L620) is used to construct a certificate chain for the to be validated certificate (the out variable `issuers`). This function works in a loop. In each iteration, it attempts to find the issuer of the current certificate. For this it consults the following locations:

  1. The list of trusted certificates stored on the server. If it is found in this list, the function will return `true`.
  2. The list of issuer certificates stored on the server. These certificates are not explicitly trusted, but can be used to construct a chain to a trusted root.
  3. The list of additional certificates sent by the client. Just like in TLS, it is possible to include additional certificates in the OPC UA handshake.

If an issuer is found, it becomes the current certificate and the loop will continue until the current certificate is self-signed or an issuer can not be found.

To find the issuer of a certificate, the function [`Match`](https://github.com/OPCFoundation/UA-.NETStandard/blob/7072fe07717dc143a77c3cc71426904f661c55c8/Stack/Opc.Ua.Core/Security/Certificates/CertificateValidator.cs#L568) is used. This function compares the issuer name of the certificate with the subject name of each potential issuer. Additionally, the serial number or the subject key identifier must match. Note that the cryptographic signature is not yet considered at this stage, the match is therefore only based on forgeable certificate metadata.

The comparison of the names in `Match` is implemented in [`CompareDistinguishedName`](https://github.com/OPCFoundation/UA-.NETStandard/blob/7072fe07717dc143a77c3cc71426904f661c55c8/Stack/Opc.Ua.Core/Security/Certificates/X509Utils.cs#L237), but this implementation is unusual. This function decomposes the name into components and then does a _case-insensitive_ match on each component. This is not how most implementations compare X.509 names.

Next up, on line 912 an `X509Chain` object is used. The intent here appears to be to verify that the chain built using `GetIssuersNoExceptionsOnGetIssuer` is cryptographically valid. However, because it is not configured with the root certificates used by the application, it will often result in errors. Thus, on line 938, the function [`CheckChainStatus`](https://github.com/OPCFoundation/UA-.NETStandard/blob/7072fe07717dc143a77c3cc71426904f661c55c8/Stack/Opc.Ua.Core/Security/Certificates/CertificateValidator.cs#L1173) is used to ignore certain types of errors. For example, an `UntrustedRoot` error is ignored if it occurred for the certificate at the root.

The vulnerability that we found is that there is no verification that the certificate chain built by `GetIssuersNoExceptionsOnGetIssuer` and the one built by `X509Chain.Build` are equal. By abusing the unusual name comparison it is possible to construct a certificate such that both functions will result in a different chain. By making sure that the errors in the second chain only occur where `CheckChainStatus` ignores them, it is possible for this certificate to get accepted by the server.

The only prerequisite for this attack is that we know the subject name of one of the trusted root certificates and either its serial number or subject key identifier. Because certificates are not secret, these values should be easy to obtain in practice. During the demonstration, we ran the attack against a server which itself has a certificate issued by a trusted root certificate. That certificate gives us the metadata we need. In practice this should work quite often.

### Example

#### Certificates

Suppose the server is configured to trust a certificate with the following details:
  
  
  Certificate:
  Data:
  Version: 3 (0x2)
  Serial Number: 9891791597891487306 (0x8946b40ca084064a)
  Signature Algorithm: sha1WithRSAEncryption
  Issuer: CN=Root
  Validity
  Not Before: Feb 24 09:35:53 2022 GMT
  Not After : Feb 24 09:35:53 2023 GMT
  Subject: CN=Root
  Subject Public Key Info:
  Public Key Algorithm: rsaEncryption
  Public-Key: (2048 bit)
  Modulus:
  [...]
  Exponent: 65537 (0x10001)
  X509v3 extensions:
  X509v3 Authority Key Identifier:
  DirName:/CN=Root
  serial:89:46:B4:0C:A0:84:06:4A
  
  X509v3 Basic Constraints:
  CA:TRUE
  X509v3 Key Usage:
  Certificate Sign, CRL Sign
  Signature Algorithm: sha1WithRSAEncryption
  [...]

And suppose that the OPC server itself is configured with the following certificate, issued from this root:
  
  
  Certificate:
  Data:
  Version: 3 (0x2)
  Serial Number:
  35:b3:1d:0a:27:cf:e3:94:25:b1:46:b8:35:47:07:1c:3a:54:0a:e8
  Signature Algorithm: sha1WithRSAEncryption
  Issuer: CN=Root
  Validity
  Not Before: Feb 24 09:35:53 2022 GMT
  Not After : Mar 26 09:35:53 2022 GMT
  Subject: CN=Quickstart Reference Server, C=US, ST=Arizona, O=OPC Foundation, DC=opcserver
  Subject Public Key Info:
  Public Key Algorithm: rsaEncryption
  Public-Key: (2048 bit)
  Modulus:
  [...]
  Exponent: 65537 (0x10001)
  X509v3 extensions:
  X509v3 Authority Key Identifier:
  DirName:/CN=Root
  serial:89:46:B4:0C:A0:84:06:4A
  
  X509v3 Basic Constraints:
  CA:FALSE
  X509v3 Key Usage:
  Digital Signature, Key Encipherment, Data Encipherment, Key Agreement
  X509v3 Subject Alternative Name:
  DNS:opcserver, URI:URI:urn:opcserver
  Signature Algorithm: sha1WithRSAEncryption
  [...]

Then the attacker can connect to the server to obtain this certificate and use the data in the Issuer and X509v3 Authority Key Identifier fields to craft two new certificates.

First of all, the attacker generates a new root certificate which uses the same common name as the trusted root certificate, but where each letter is flipped in case (i.e.: upper case to lower case and lower case to upper case). This certificate is self-signed and must contain the CA=TRUE basic constraint. The attacker makes this certificate available for download as a PEM file over HTTP on a webserver at the URL `http://attacker/root.pem`.
  
  
  Certificate:
  Data:
  Version: 3 (0x2)
  Serial Number:
  18:c6:c2:36:a6:97:b1:a8:10:4b:07:7c:4b:20:5e:f2:d0:8b:e0:a2
  Signature Algorithm: sha256WithRSAEncryption
  Issuer: CN=rOOT
  Validity
  Not Before: Feb 17 10:40:24 2022 GMT
  Not After : May 25 10:40:24 2022 GMT
  Subject: CN=rOOT
  Subject Public Key Info:
  Public Key Algorithm: rsaEncryption
  Public-Key: (3072 bit)
  Modulus:
  [...]
  Exponent: 65537 (0x10001)
  X509v3 extensions:
  X509v3 Basic Constraints:
  CA:TRUE
  X509v3 Key Usage:
  Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement, Certificate Sign, CRL Sign
  Signature Algorithm: sha256WithRSAEncryption
  [...]

Secondly, the attacker generates a new leaf certificate, signed using the previously created root. The following fields are added to this certificate:

  * The issuer contains the subject name of the _fake_ root.
  * The X509v3 Authority Key Identifier extension contains a directory name of the _fake_ root and a serial number of the _real_ trusted root.
  * The certificate contains an Authority Information Access extension containing a CA Issuers field containing the URL where the fake root certificate PEM file can be downloaded.

All other fields, like the Subject and Subject Alternative Name fields, can contain any data the attacker may choose. To pass all further checks in `InternalValidate`, the validity time should contain the current time and the `keyUsage` field should contain Data Encipherment. A Subject Alternative Name extension could be added if the domain is checked.
  
  
  Certificate:
  Data:
  Version: 3 (0x2)
  Serial Number:
  0e:4f:b8:ff:bd:d9:3a:fe:e7:0a:b2:eb:64:32:59:5e:ad:08:01:39
  Signature Algorithm: sha256WithRSAEncryption
  Issuer: CN=rOOT
  Validity
  Not Before: Feb 17 10:40:24 2022 GMT
  Not After : May 25 10:40:24 2022 GMT
  Subject: CN=FakeCert
  Subject Public Key Info:
  Public Key Algorithm: rsaEncryption
  Public-Key: (3072 bit)
  Modulus:
  [...]
  Exponent: 65537 (0x10001)
  X509v3 extensions:
  X509v3 Authority Key Identifier:
  DirName:/CN=rOOT
  serial:89:46:B4:0C:A0:84:06:4A
  
  X509v3 Basic Constraints:
  CA:FALSE
  Authority Information Access:
  CA Issuers - URI:http://attacker/root.pem
  
  X509v3 Key Usage:
  Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment, Key Agreement, Certificate Sign, CRL Sign
  Signature Algorithm: sha256WithRSAEncryption
  [...]

#### Verification

When the attacker connects with this `CN=FakeCert` certificate, the following will happen:

`GetIssuersNoExceptionsOnGetIssuer` will look in its trusted certificate store for the issuer of this certificate. To do this, it compares the Issuer name of the received certificate with the Subject name of the certificates in the store.

It does this check by decomposing the distinguished name, sorting the components, and then doing a case-insensitive match on each component.

So, it compares the common name of the issuer from the certificate:
  
  
  CN=rOOT

with the common name of the subject of the trusted certificate:
  
  
  CN=Root

In addition, it will compare the serial number of the root certificate with the serial number of the authority key identifier extension, which are equal:
  
  
  Serial Number: 9891791597891487306 (0x8946b40ca084064a)
  
  
  X509v3 Authority Key Identifier:
  DirName:/CN=rOOT
  serial:89:46:B4:0C:A0:84:06:4A

This function will therefore consider the `CN=Root` certificate a match. The signature could show that it is not correctly signed, but this is not checked yet. It will obtain a chain with one issuer and `isIssuerTrusted` will be true.

Then, it creates an `X509Chain` object and calls `chain.Build(certificate)`. The result code of this call is ignored, and the global status of the result too. Only the statuses of the individual chain elements are checked.

As `chain.Build` does a literal comparison on the subject of the trusted root with the issuer of `FakeCert`, it will not consider the `CN=Root` certificate to be the issuer of `FakeCert` (because it looks for `CN=rOOT`). While the serial number from the Authority Key Identifier extension matches, this is not sufficient for a match.

Because it can't find the issuer certificate in its trust store, it will use the CA Issuers URL from the Authority Information Access extension to download the certificate from the webserver. With that, the result of the `chain.Build()` call will be a chain of two certificates, where the second one indicates the error `UntrustedRoot`. The function `CheckChainStatus` ignores this error code because it incorrectly assumes that the corresponding certificate was one of its trusted certificates, but it will in fact be the `CN=rOOT` certificate.

The remainder of the checks in `InternalValidate` will now succeed, because `issuedByCA` is true and `isIssuerTrusted` is true. The key usage, endpoint domain, use of SHA1 and minimum key size checks can be passed because the attacker has full control over the contents of `FakeCert`.

Our exploit can been seen in action in the video below:

Your browser does not support the video tag. 

## Impact

With this vulnerability we could bypass the Trusted Application Check against the reference server that is included in the OPC UA .NET Standard repository. It would also be possible to bypass the check at the client side to impersonate a server.

In addition, OPC UA also has what is known as "User Authentication", which happens after the Trusted Application Check to establish a session. One of the options for User Authentication is by using an X.509 certificate, which could be bypassed in the same way too.

In most places in practice the OPC UA server would not be exposed to the public internet, so to exploit this issue an attacker would need to already have access to an internal ICS network. However, in rare cases where exposing an OPC UA server to the public internet would be unavoidable, enabling certificate authentication would be the most effective method for securing it. In that case, this check could be bypassed and it would be possible to gain access to the communication.

Once connected to an OPC UA server, the attacker would be able to read and write data, which could be used to disrupt the ICS processes that use this server.

## The fix

The issues we found were fixed in the commit [51549f5ed846c8ac060add509c76ff4c0470f24d](https://github.com/OPCFoundation/UA-.NETStandard/commit/51549f5ed846c8ac060add509c76ff4c0470f24d) and assigned [CVE-2022-29865](https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-29865.pdf). Names are now compared in the same manner as other X.509 implementations, by not doing a case-insensitive check and no resorting of name components. In addition, defensive checks were added to make sure that the two certificate chains that are used are equal.

## Thoughts

Certificate validation is tricky, as we have also demonstrated before in our [post about the Dutch Corona-check app](/en/research-labs/coronacheck-app-tls-certificate-vulnerabilities/). These vulnerabilities actually bear some similarity, as both used a check for issuers based only on forgeable data. In this case, the cause is the desire to not use the Windows certificate store. We are unsure if this is truly the only way to implement this in .NET, as the [`CustomTrustStore`](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509chainpolicy.customtruststore?view=net-6.0) property and [`TrustMode=CustomRootTrust`](https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.x509chaintrustmode?view=net-6.0) setting on an `X509ChainPolicy` object appear to offer the required functionality without a dependence on the Windows certificate store.

[The level of detail in the OPC UA specification](https://reference.opcfoundation.org/v104/Core/docs/Part4/6.1.3/) regarding certificate validation is admirable. For example, it specifies clearly what errors should be used in what situations and there is even a [chapter that suggests how to store the certificates on the server](https://reference.opcfoundation.org/GDS/docs/F.1/). However, there is a risk that over-specification of how a process like this should work leads to complex and non-idiomatic code. If the normal .NET API can no longer be applied directly as certain parts need to be re-implemented, this could create a large potential source for vulnerabilities.

## Conclusion

We demonstrated a Trusted Application Check Bypass in OPC Foundation OPC UA .NET Standard. This can be used to set up a trusted connection to an OPC UA server. The cause of this vulnerability was the modification of the certificate validation procedure to use trusted roots stored in a custom location instead of the Windows certificate store and an unusual name comparison. This made it possible to made our certificate appear to be signed by one of the trusted roots.

We thank Zero Day Initiative for organizing this years edition of Pwn2Own Miami, we hope to return to a later edition!

You can find the other four write-ups here:

  * [Inductive Automation Remote Code Execution](/en/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/)
  * [AVEVA Edge Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/)
  * [Unified Automation C++ Demo Server DoS](/en/research-labs/pwn2own-miami-2022-unified-automation-c-demo-server-dos/)
  * [ICONICS GENESIS64 Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution/)

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Red Teaming →](/en/pentesting-services/red-teaming-service/)

[← Back to Research Labs](/en/research-labs/)

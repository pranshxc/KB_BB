---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-15_how-to-bypass-golang-ssl-verification.md
original_filename: 2024-07-15_how-to-bypass-golang-ssl-verification.md
title: How to Bypass Golang SSL Verification
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 7b22b497358d92f1241fde02f3860eb6df111eb5f5b8def12718b4f5ef512219
text_sha256: 2416680f826516a8b927da5237a9566d431a12ff3fa9ae21247f75f777d998a5
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# How to Bypass Golang SSL Verification

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-15_how-to-bypass-golang-ssl-verification.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `7b22b497358d92f1241fde02f3860eb6df111eb5f5b8def12718b4f5ef512219`
- Text SHA256: `2416680f826516a8b927da5237a9566d431a12ff3fa9ae21247f75f777d998a5`


## Content

---
title: "How to Bypass Golang SSL Verification"
url: "https://www.cyberark.com/resources/threat-research-blog/how-to-bypass-golang-ssl-verification"
final_url: "https://www.cyberark.com/resources/threat-research-blog/how-to-bypass-golang-ssl-verification"
authors: ["Michael Pasternak"]
bugs: ["SSL verification bypass", "Security code review"]
publication_date: "2024-07-15"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 164
---

# How to Bypass Golang SSL Verification

July 15, 2024 Michael Pasternak

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fhow-to-bypass-golang-ssl-verification)
  * [Twitter](https://twitter.com/share?text=How%20to%20Bypass%20Golang%20SSL%20Verification&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fhow-to-bypass-golang-ssl-verification&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#eed19d9b8c848b8d9ad3ad81809a8b809acbdcde889c8183cbdcde8397cbdcdea69b8ccbdcdfc88f839ed58c818a97d3ad868b8d85cbdcde819b9acbdcde99868f9acbdcd99dcbdcde868f9e9e8b80878089cbdcde8f9acbdcdead978c8b9caf9c85cbdcdfcbdeafcbdeafa68199cbdcde9a81cbdcdeac979e8f9d9dcbdcdea981828f8089cbdcdebdbda2cbdcdeb88b9c8788878d8f9a878180cbdeafa981828f8089cbdcde8f9e9e82878d8f9a8781809dcbdcde9a868f9acbdcde9b9d8bcbdcdea6bababebdcbdcde9c8b9f9b8b9d9a9dcbdcde868f988bcbdcde8fcbdcde8c9b87829ac38780cbdcdebdbda2cbdcde988b9c8788878d8f9a878180cbdcde888b8f9a9b9c8bcbdcde8b808f8c828b8acbdcde8c97cbdcde8a8b888f9b829ac0cbdcdea780cbdcde819b9ccbdcde99819c85cbdcadcbdcde998bcbdcde81889a8b80cbdcde8b808d819b809a8b9ccbdcde8f80cbdcde8f9e9e82878d8f9a878180cbdcde9a868f9acbdcde9b9d8b9dcbdcdea981828f8089cbdcdea6bababebdcbdcde9c8b9f9b8b9d9a9dcbdcadcbdcde8f808acbdcde998bcbdcde868f988bc0c0c0cbdeafcbdeaf869a9a9e9dcbddafcbdca8cbdca8999999c08d978c8b9c8f9c85c08d8183cbdca89c8b9d819b9c8d8b9dcbdca89a869c8b8f9ac39c8b9d8b8f9c8d86c38c828189cbdca8868199c39a81c38c979e8f9d9dc38981828f8089c39d9d82c3988b9c8788878d8f9a878180)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fhow-to-bypass-golang-ssl-verification&title=How%20to%20Bypass%20Golang%20SSL%20Verification&summary=Golang%20applications%20that%20use%20HTTPS%20requests%20have%20a%20built-in%20SSL%20verification%20feature%20enabled%20by%20default.%20In%20our%20work%2C%20we%20often%20encounter%20an%20application%20that%20uses%20Golang%20HTTPS%20requests%2C%20and%20we%20have...)

![Safe Encrypted Connection on Internet](https://www.cyberark.com/wp-content/uploads/2024/07/bypass-golang.jpg)

Golang applications that use HTTPS requests have a built-in SSL verification feature enabled by default. In our work, we often encounter an application that uses Golang HTTPS requests, and we have to examine the requests in plain text to find security flaws and bugs.

Usually, we lack the application’s source code, and without debug symbols, it becomes much more complex to change the binary to allow us to intercept the HTTP requests.

In this blog post, we will explore the Golang core net/http library more deeply to understand how to remove the SSL verification manually or using a short Python script.

## TL;DR

We will get into Golang SSL verification and explore simple patching methods to bypass it.

## How Did It All Start?

We begin with a Golang application, which examines HTTPS requests in plain text.

We tried using a tool like “Burp Suite” (or any other preferred proxy tool) by setting the HTTPS_PROXY environment variable. However, we encountered an error when trying this method:

![Trying to proxy an app](https://www.cyberark.com/wp-content/uploads/2024/07/proxy-an-app.jpg)

**Figure 1:****Trying to****proxy an app**

We pondered the situation and considered adding the Burp certificate to our computer’s CA store, assuming it would resolve the “unknown authority” certificate error.

However, adding the burp suite cert into the computer CA didn’t work because Golang does not rely on the computer’s CA store and verifies every certificate itself.

We thought about performing MITM (man in the middle) attacks on the Golang apps and concluded that it would be difficult because of the self-verification.

Usually, in network libraries and HTTP handling, the programmer can disable SSL verification by changing the config or adding flags in the HTTP handler. We thought that might be the case here, too.

To disable SSL verification, we found a parameter in the config called “ _InsecureSkipVerify_ ” with the default value set to false. To disable SSL Verification, you can add the code below (code snippet 1) to the app. However, in our case, we worked on a compiled app and needed to modify it on the disk since it had already been built.

Method 1:
  
  
  
  
  http.DefaultTransport.(*http.Transport).TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
  _, err := http.Get("https://golang.org/")
  
  
  

Method 2:
  
  
  
  
  tr := &http.Transport{
  TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
  }
  client := &http.Client{Transport: tr}
  _, err := client.Get("https://golang.org/")
  

Although the “ _InsecureSkipVerify_ ” flag is precisely what we need, we faced a challenge because our application was pre-compiled, and we couldn’t access the source code. It cannot be recompiled with the flag enabled, so we needed a different approach to tackle this problem.

## Deep Into Golang Source Code

Our next objective was to find where in the program binary the flag “ _InsecureSkipVerify”_ was being used and patch it.

Although we could attempt to understand the application’s binary format and assembly code, this was unnecessary. Instead, we referred to the _net/http_ source code.

By searching through the Golang codebase for the _“InsecureSkipVerify”_ flag, we discovered it was used in the file “[crypto/tls/handshake_client.go](https://github.com/golang/go/blob/master/src/crypto/tls/handshake_client.go).”
  
  
  
  
  func (c *Conn) verifyServerCertificate(certificates [][]byte) error {
  activeHandles := make([]*activeCert, len(certificates))
  certs := make([]*x509.Certificate, len(certificates))
  for i, asn1Data := range certificates {
  cert, err := globalCertCache.newCert(asn1Data)
  if err != nil {
  c.sendAlert(alertBadCertificate)
  return errors.New("tls: failed to parse certificate from server: " + err.Error())
  }
  activeHandles[i] = cert
  certs[i] = cert.cert
  }
  
  if !c.config.InsecureSkipVerify {
  opts := x509.VerifyOptions{
  Roots:  c.config.RootCAs,
  CurrentTime:  c.config.time(),
  DNSName:  c.config.ServerName,
  Intermediates: x509.NewCertPool(),
  }
  
  for _, cert := range certs[1:] {
  opts.Intermediates.AddCert(cert)
  }
  var err error
  c.verifiedChains, err = certs[0].Verify(opts)
  if err != nil {
  c.sendAlert(alertBadCertificate)
  return &CertificateVerificationError{UnverifiedCertificates: certs, Err: err}
  }
  }
  
  

In this file, we found a function called “verifyServerCertificate” (code snippet 3). After examining it, it became evident that if the flag is set to true, the server certificate verification is bypassed. Therefore, we can bypass the check certificate part by merely patching the “if” statement or the assembly opcode.

## Demo App

To demonstrate what we found, we wrote a simple Golang code that creates a GET request to ipinfo.io and prints the output.
  
  
  
  
  package main
  
  import (
  "io/ioutil"
  "log"
  "net/http"
  )
  
  func main() {
  resp, err := http.Get("https://ipinfo.io/")
  if err != nil {
  log.Fatalln(err)
  }
  
  //We Read the response body on the line below.
  body, err := ioutil.ReadAll(resp.Body)
  if err != nil {
  log.Fatalln(err)
  }
  
  //Convert the body to type string
  sb := string(body)
  log.Printf(sb)
  }
  
  
  

Usually, programmers choose to strip their apps from debug symbols to remove unnecessary information about their apps, such as strings and function names.

As you can see in the code (Code snippet 3), we didn’t configure any “special” flags or settings and relied on Golang’s default configuration.

For the sake of this blog, we won’t strip the binary, making reverse engineering the app easier.

## Reversing the App

Before we examine the assembly code, let’s look at the source code of “ _verifyServerCertificate._ ”

![verifyServerCertificate](https://www.cyberark.com/wp-content/uploads/2024/07/verifyservercertificate.jpg)

**Figure 2: Source code of verifyServerCertificate**

As you can see in Figure 2, we can divide the code into three sections by their flow:

Red. Checks if the server is in the cache

Green. Checks if the _InsecureSkipVerify_ is set

Blue. Checks public key verifications and Peer Certificate

The second part is of interest because of the usage of the flag _InsecureSkipVerify_ _._

Let’s search the function by name because we didn’t remove the debug symbols from the binary:

![IDA function search](https://www.cyberark.com/wp-content/uploads/2024/07/function-search.jpg)

**Figure 3: IDA function search**

Let’s see how the “graph view” (Figure 4) looks:

![IDA graph view](https://www.cyberark.com/wp-content/uploads/2024/07/graph-view.jpg)

**Figure 4: IDA graph view**

As we examine the IDA graph (Figure 4) and look at the loops inside the binary (light blue arrows), we can see that it looks similar to the source code (Figure 2). Now, we can divide the source code into three sections.

We can that entering the second section is affected by the flag “ _InsecureSkipVerify_ _.”_

Figure 4 shows the margin area between the red and green sections, where the OPCODEs are responsible for checking whether we are following the flow or jumping straight to the blue section.

![IDA graph view ](https://www.cyberark.com/wp-content/uploads/2024/07/statement.jpg)

**Figure 5: IDA graph view of the if statement**

From our analysis, we can deduce that the “if” statement involves the two OP-CODEs, cmp and jnz.

## Patching the Program

Based on our findings, it can be assumed that the **jnz** opcode controls whether or not the program enters the second section of the code. We wanted to reverse the condition to “bypass” the if statement and then jump straight into the third (Figure 5).

![X86 opcodes](https://www.cyberark.com/wp-content/uploads/2024/07/x86-opcodes.jpg)

**Figure 6: X86 opcodes**

Referring to the opcode table, we determined that only one byte needs to be changed, specifically from **85** to **84**. This alteration will transform the opcode from **jnz** to **jz** , which represents “jump if zero.”

![Bytes before the patch](https://www.cyberark.com/wp-content/uploads/2024/07/bytes-before-the-patch.jpg)

**Figure 7: Bytes before the patch**

To patch the program, we can right-click and select “edit.” Then, we can modify the byte at position 85 to become 84.

![Bytes after the patch](https://www.cyberark.com/wp-content/uploads/2024/07/bytes-after-the-patch.jpg)

**Figure 8: Bytes after the patch**

Afterward, right-click again and choose “Apply changes.” Consequently, the program changes from**jnz** to **jz**.

![Graph view after the patch](https://www.cyberark.com/wp-content/uploads/2024/07/graph-view-after-the-patch.png)

**Figure 9: Graph view after the patch**

To apply the patches to the input program, navigate to the toolbar, click on “Edit,” select “Patch program,” and click “Apply patches to input file…” When prompted, you can choose to preserve an original copy of the program.

![IDA patching menu](https://www.cyberark.com/wp-content/uploads/2024/07/patching-menu.jpg)

**Figure 10: IDA patching menu**

That’s it! Your program no longer has SSL verification. Let’s verify this.

![Pathed Program Output](https://www.cyberark.com/wp-content/uploads/2024/07/pathed-program-output.jpg)

**Figure 11: Pathed program output**

Now, let’s examine our Burp Suite proxy.

![Burp view of the proxied HTTPS request](https://www.cyberark.com/wp-content/uploads/2024/07/burp-view.jpg)

**Figure 12: Burp view of the proxied HTTPS request**

We are victorious! We can observe the request successfully passing through.

## Patching by Python Script

For convenience, we created a Python script that searches for the cmp and jnz instructions and replaces them with jz instructions. Here is the code of the script:
  
  
  
  
  #!/usr/bin/env python3
  import subprocess
  import argparse
  
  supported_versions_to_bytes = {
  '11': [b"\x00\x0F\x85\xB3\x04\x00\x00", b"\x00\x0F\x84\xB3\x04\x00\x00"],
  '12': [b"\x00\x00\x0F\x85\x43\x05\x00\x00", b"\x00\x00\x0F\x84\x43\x05\x00\x00"],
  '13': [b"\x00\x00\x0F\x85\x32\x05\x00\x00", b"\x00\x00\x0F\x84\x32\x05\x00\x00"],
  '14': [b"\x00\x00\x0F\x85\x48\x05\x00\x00", b"\x00\x00\x0F\x84\x48\x05\x00\x00"],
  '15': [b"\x00\x00\x0F\x85\x3A\x06\x00\x00", b"\x00\x00\x0F\x84\x3A\x06\x00\x00"],
  '16': [b"\x00\x00\x0F\x85\x5A\x06\x00\x00", b"\x00\x00\x0F\x84\x5A\x06\x00\x00"],
  '17': [b"\x00\x00\x0F\x85\x7F\x01\x00\x00", b"\x00\x00\x0F\x84\x7F\x01\x00\x00"],
  '18': [b"\x00\x00\x0F\x85\x7C\x01\x00\x00", b"\x00\x00\x0f\x84\x7C\x01\x00\x00"],
  '19': [b"\x00\x00\x0F\x85\x7B\x01\x00\x00", b"\x00\x00\x0f\x84\x7B\x01\x00\x00"],
  '20': [b"\x00\x00\x0F\x85\x84\x01\x00\x00", b"\x00\x00\x0F\x84\x84\x01\x00\x00"],
  '21': [b"\x00\x00\x0F\x85\x82\x01\x00\x00", b"\x00\x00\x0F\x84\x82\x01\x00\x00"]
  }
  
  
  def replace_file_bytes(file_path, old_bytes, new_bytes):
  with open(file_path, 'rb') as f:
  data = f.read()
  position = data.find(old_bytes)
  
  if(-1 == position):
  raise Exception("cannot find bytes, maybe the program is already patched?")
  
  with open(file_path, 'rb+') as file:
  file.seek(position)
  existing_bytes = file.read(len(old_bytes))
  
  if existing_bytes == old_bytes:
  file.seek(position)
  file.write(new_bytes)
  
  def run_command(command):
  result = subprocess.run(command, shell=True, capture_output=True, text=True)
  return result.stdout.strip()
  
  def get_go_bin_version(filename):
  output = run_command(f"strings {filename} | grep '^go1' | head -n 1")
  if "" == output:
  output = run_command(f"strings {filename} | grep 'Go cmd/compile'  | head -n 1 | cut -d' ' -f 3")
  if "" == output:
  output = run_command(f"strings {filename} | grep -Eo 'go[0-9]+\.[0-9]+(\.[0-9]+)?' | head -n 1")
  return output
  
  def get_args():
  parser = argparse.ArgumentParser(description='Get a filename and patches it ssl verification check')
  parser.add_argument("-f", "--filename", help='File to patch', required=True)
  parser.add_argument("-v", "--version", help='Input version of Golang app')
  parser.add_argument("-g", "--get-version", help='tries to get the app Golang version', action='store_true')
  return parser.parse_args()
  
  def main():
  args = get_args()
  version = get_go_bin_version(args.filename).split('.')[1]
  if args.get_version:
  print("Assuming that the Golang version is: %s" % version)
  return
  if args.version:
  version = args.version
  old_bytes = supported_versions_to_bytes[version][0]
  new_bytes = supported_versions_to_bytes[version][1]
  replace_file_bytes(args.filename, old_bytes, new_bytes)
  
  if "__main__" == __name__:
  main()
  

## Understanding Source Code to Patch Vulnerabilities

Our goal was to remove the SSL verification from the pre-compiled Golang so that we could check for vulnerabilities in the code. We did this by understanding the source code and flow of the net/http library in Golang and analyzing it to better understand where we needed to patch the binary. This doesn’t require you to be proficient with low-level programming; it only requires common sense.

We could also apply this method to bypasses in other apps/languages and get more comfortable patching other binaries for fun.

_Michael Pasternak is a cyber research team leader at CyberArk Labs._

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_authomize-discovers-passbleed-password-stealing-and-impersonation-risks-in-okta.md
original_filename: 2022-07-19_authomize-discovers-passbleed-password-stealing-and-impersonation-risks-in-okta.md
title: Authomize Discovers PassBleed Password Stealing and Impersonation Risks in
  Okta
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
- information-disclosure
- api-security
language: en
raw_sha256: 6f7656c39cb37198f18a6bb72726fc606e2da35d44d00df10caa732bcbe57d66
text_sha256: f214b6a4ae0438258479b9233f58c81f1d5646443e2f7a590e2a27449b258312
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Authomize Discovers PassBleed Password Stealing and Impersonation Risks in Okta

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_authomize-discovers-passbleed-password-stealing-and-impersonation-risks-in-okta.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `6f7656c39cb37198f18a6bb72726fc606e2da35d44d00df10caa732bcbe57d66`
- Text SHA256: `f214b6a4ae0438258479b9233f58c81f1d5646443e2f7a590e2a27449b258312`


## Content

---
title: "Authomize Discovers PassBleed Password Stealing and Impersonation Risks in Okta"
page_title: "What is Secure Shell (SSH)? | Delinea"
url: "https://www.authomize.com/blog/authomize-discovers-password-stealing-and-impersonation-risks-to-in-okta/"
final_url: "https://delinea.com/what-is/secure-shell-ssh"
authors: ["Authomize (@Authomize)"]
programs: ["Okta"]
bugs: ["Sensitive data sent over an unencrypted channel", "Broken authorization", "Information disclosure"]
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2432
---

# Secure Shell (SSH)

## What is Secure Shell?

Secure Shell (SSH) is a network protocol that enables secure communication between two devices over an unsecured network. Specifically, SSH allows for remote login, command execution, and file transfer between a client and server.

The SSH protocol relies on strong encryption to authenticate users and prevent eavesdropping and data tampering. Common applications include:

  * Securely accessing a remote server
  * Managing infrastructure
  * Transferring files

SSH originated as a more secure replacement for insecure remote access protocols like Telnet and FTP. The first version of SSH appeared in 1995, while SSH-2, the current standard version, was adopted in 2006.

## How SSH works

Public-key authentication is common in SSH. It relies on key pairs that can be generated through ssh-keygen. Once authenticated, the client and server negotiate temporary session keys using symmetric encryption algorithms like AES to encrypt data in transit.

SSH also supports certificate-based authentication for enhanced security. Certificate-based authentication was introduced in OpenSSH 5.4. It offers more security than plain public keys because certificates can expire and be managed centrally. To use SSH certificates, a certificate authority signs and issues user/host certificates that are then used to authenticate sessions.

After successful authentication, users can securely execute commands or transfer files as if locally connected.

Under the hood, SSH is implemented on top of TCP/IP and standard network protocols. It typically listens on port 22 for connections. SSH can also forward or "tunnel" traffic from other applications over its encrypted channels.

## Benefits of SSH

Encryption: SSH encrypts all traffic between the client and server. This protects sensitive data in transit.

Remote access: SSH enables secure remote login to servers and devices for administration, file transfers, command execution, etc. This is very useful for managing infrastructure.

Authentication: SSH supports authentication to verify user and host identities. This prevents unauthorized access.

Integrity checking: The protocol uses hashing algorithms to ensure the integrity of transmitted data. This prevents tampering or manipulation of data.

Wide adoption: SSH is widely adopted across operating systems like Linux, Unix, and Windows and is used to manage servers, routers, firewalls, etc.

## Challenges of SSH

While SSH offers crucial encryption and remote access capabilities, organizations must be aware of management challenges and potential attack vectors and have appropriate controls to secure SSH usage.

Complex key and certificate management: Managing a large number of SSH keys and certificates across an organization can be operationally challenging.

Security vulnerabilities: Issues like brute force attacks, session hijacking, and poor key management can compromise SSH security.

Tunneling risks: SSH port forwarding can be misused to bypass firewall policies and access restricted networks.

Compliance and auditing: Tracking SSH activities to meet compliance requirements can be difficult without proper logging and monitoring.

### How to securely manage SSH keys and certificates 

A credential vault like [Delinea’s Secret Server](/products/secret-server) handles SSH key discovery, protection, access, rotation, and audit.  
Learn more [best practices for SSH key management](/blog/ssh-key-management).

Within a DevOps workflow for rapid development, you can securely issue and manage SSH certificates, and enable automated certificate signing and distribution.  
Learn about [DevOps Secrets Vault](/products/devops-secrets-management-vault) for managing SSH keys and certificates.

### More SSH Resources:

Blogs  
[SSH proxies vs. jump hosts: How to save time and spend less](/blog/rdp-ssh-proxies-jump-hosts-and-pam)  
[SSH key management best practices: Beyond SSH Keys](/blog/ssh-key-management)  
  
Products  
[Secret Server Feature: SSH Key Management](/products/secret-server/features/ssh-key-management)  
[Secret Server Feature: Unix Protection](/products/secret-server/features/unix-linux-protection-add-on-ssh)

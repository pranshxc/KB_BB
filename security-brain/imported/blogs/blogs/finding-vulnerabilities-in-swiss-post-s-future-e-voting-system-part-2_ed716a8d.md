---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-22_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-2.md
original_filename: 2022-05-22_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-2.md
title: Finding vulnerabilities in Swiss Post's future e-voting system - Part 2
category: blogs
detected_topics:
- otp
- sso
- command-injection
- path-traversal
- automation-abuse
- graphql
tags:
- imported
- blogs
- otp
- sso
- command-injection
- path-traversal
- automation-abuse
- graphql
language: en
raw_sha256: ed716a8d86b4ef6b418676b0e5c043541527d13a59a4336cb0b1c762e17ce63c
text_sha256: a40a210a0a1b0225b04412c7a71903361023185e112e8039fed9084ae9f29262
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# Finding vulnerabilities in Swiss Post's future e-voting system - Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-22_finding-vulnerabilities-in-swiss-posts-future-e-voting-system-part-2.md
- Source Type: markdown
- Detected Topics: otp, sso, command-injection, path-traversal, automation-abuse, graphql
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `ed716a8d86b4ef6b418676b0e5c043541527d13a59a4336cb0b1c762e17ce63c`
- Text SHA256: `a40a210a0a1b0225b04412c7a71903361023185e112e8039fed9084ae9f29262`


## Content

---
title: "Finding vulnerabilities in Swiss Post's future e-voting system - Part 2"
url: "https://www.reversemode.com/2022/05/finding-vulnerabilities-in-swiss-posts.html"
final_url: "https://www.reversemode.com/2022/05/finding-vulnerabilities-in-swiss-posts.html"
authors: ["Ruben Santamarta (@reversemode)"]
bugs: ["Insecure deserialization", "Cryptographic issues"]
publication_date: "2022-05-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2616
---

###  Finding vulnerabilities in Swiss Post's future e-voting system - Part 2 

[ May 22, 2022  ](https://www.reversemode.com/2022/05/finding-vulnerabilities-in-swiss-posts.html "permanent link")

  

Earlier this year I published the [Part I](https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html) of this series of blog posts on vulnerabilities in Swiss Post's future e-voting system. That publication comprehensively explains the context, methodology and attack surface for the Swiss Post e-voting system, so it is highly recommended to go through it before reading this post, if you're really interested in getting the whole picture.

This second round of [bugs](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/35) (reported during December '21 and January '22 ) includes multiple cryptographic vulnerabilities and a deserialization issue. 

For me, the most interesting issue is '#YWH-PGM2323-65', not only because it would have prevented ballot boxes from being decrypted during the tally phase, but also due to the potential design weaknesses that I'm coming across as a result of its analysis. 

Let's briefly discuss the reported issues before going into detail:

ID| Title| Reward (€)| Attack Surface Areas*| CVSS  
---|---|---|---|---  
#YWH-PGM2323-53| Multiple unchecked length values during SafeStreamDeserialization may crash Control Components| 3500| 3 & 4| 5.4 - Medium  
CVSS:3.0/AV:A/AC:H/PR:H/UI:N/S:C/C:N/I:N/A:H  
#YWH-PGM2323-64| Verifier does not properly verify the signature of NodeContributions| 5000| 2 & 3| 5.1 - Medium  
CVSS:3.0/AV:A/AC:H/PR:H/UI:R/S:C/C:N/I:H/A:N  
#YWH-PGM2323-65| Generation of 'Choice Return Codes encryption' Public Key and 'Election' Public Key may be influenced by a malicious voting server.| 4500| 3| 5.4 - Medium  
CVSS:3.0/AV:A/AC:H/PR:H/UI:N/S:C/C:N/I:N/A:H  
#YWH-PGM2323-{59,60,61}| Multiple improper signature verification issues.| N/A (Duplicated)| 2 & 3 & 4| 7.3 - High  
CVSS:3.0/AV:A/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:H  
  
* The 'attack surface areas' column refers to the top 5 priorities previously elaborated on 'Finding vulnerabilities in Swiss Post's future e-voting system - Part I '.

_1.____Multiple unchecked length values during SafeStreamDeserialization may crash Control Components_

As it was explained in the Part I, the orchestrator service, part of the untrusted Voting Server, communicates with the Control Components using [AMQP](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol) messages through a RabbitMQ cluster.

The control components implement a specific deserialization logic for some of those messages. A lack of proper length validation during the deserialization of potentially attacker-controlled messages can force an out of memory error, thus crashing the affected component

 _2\. 'Verifier' does not properly verify the signature of NodeContributions_

This vulnerability targets the [Verifier](https://gitlab.com/swisspost-evoting/verifier/verifier), a component that is not a priority yet as it is still missing part of its functionality, but nonetheless a key component intended to facilitate auditors (including 3rd parties) the task of validating an election event.

When checking the Node Contributions resulting from the '_GenEncLongCodeShares_ ', the verifier uses data, coming from the Control Components, that has not been yet verified in order to set up the own verification logic, which usually is a bad thing to do. Additionally, it does not properly verify the consistency of these contributions, however consistence checks are still being developed so that may be considered a known-issue.

_3\. Generation of 'Choice Return Codes encryption' Public Key and 'Election' Public Key may be influenced by a malicious voting server._

This vulnerability involves a malicious voting server (note that the system specification considers the voting server untrustworthy and potentially compromised) providing a specific combination of Control Components public keys to the SDM, so that when 'Choice Return Codes' and the 'Election' Public Keys are generated, they will not comply with the actual contributions from the four different Control Components.

When targeting the 'Election' Public key (ELpk), this attack would have prevented the ballot boxes from being decrypted during the tally phase, which renders the election event basically useless as votes cannot be decrypted.

If we were talking about a regular election, this issue would be similar to be directly voting into a paper shredding machine.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5mi_HcoBYoiBvNpl2PQDL-tjKM3LBXQ-_d0BhluETe6UjG2FyW0KvipxaZfln-7ng4_ObEyTq_Rx0dpzoMXH7rdmhuwaFgy7nFt-vkuupLxrKnkRMXeMPF2bwhW6RGeRcgLPZSW1WJUh1NUTBUVjR8x0g_f7keEazRRXinxqwMnjKYUiCb6ZmZLSmww/w400-h270/evoting.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5mi_HcoBYoiBvNpl2PQDL-tjKM3LBXQ-_d0BhluETe6UjG2FyW0KvipxaZfln-7ng4_ObEyTq_Rx0dpzoMXH7rdmhuwaFgy7nFt-vkuupLxrKnkRMXeMPF2bwhW6RGeRcgLPZSW1WJUh1NUTBUVjR8x0g_f7keEazRRXinxqwMnjKYUiCb6ZmZLSmww/s1166/evoting.png)

To be honest, I don't completely agree with the assessment Swiss Post has performed on this vulnerability due to the following reasons:

\- Swiss Post narrows down the impact of this vulnerability to the availability of the system, while I consider there is also an impact on its integrity. 

\- They didn't consider this attack may qualify for the '[Vote Corruption](https://yeswehack.com/programs/swiss-post-evoting)' [domain-specific](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/33) scenario, because it targets all votes instead of individual votes, which, from my perspective, may be questionable at least.

\- They acknowledge that the mitigation adduced for this attack, which is the ability of the cantons to decrypt 'test ballot boxes' using the same cryptographic materials than in the real election event (so they would see votes are not being decrypted), is not currently part of the system specification, neither had been documented anywhere when the attack was reported. In addition to this, I think that ability presents a high risk attack vector but as that functionality has not been formally described nor implemented, so far there is little to add.

\- Swiss Post states that attacks against availability do not violate their security objectives, which is a concern. Actually they acknowledge the system design and specification are vulnerable by default to this kind of attack: for instance, if a malicious Control Component destroys (3 of 4 Control Components are assumed to be malicious) its election private key. 

Just to put things into context, Ransomware is essentially an attack against availability. I see a troubled future for e-voting if the election results depend on whether the election authorities are willing to pay in order to receive the keys that would allow to decrypt votes. 

 _4\. Multiple improper signature verification issues._

The signature validation for payloads sent back and forth between the SDM and Control Components (through the Voting Server's Orchestrator) was broken due to an improper validation of the certificate chain. Basically, the signature validation algorithm was just checking whether the payload was properly signed, but not who really signed it. As there were different certificate chains hanging from the same Platform Root CA, untrustworthy components would be able to leverage their intermediate certificates to impersonate others. 

My reports were accepted but discarded as 'Duplicated'. It turned out these, and similar, issues had been previously uncovered by [Thomas Haines](https://gitlab.anu.edu.au/u1113289/thomas-public-paper/-/raw/a5f1c738d7e034c360dc5fccddf49ea9555a42b1/SwissPostSigningMarch2021.pdf), [Vanessa Tiague and Oliver Pereira](https://gitlab.com/swisspost-evoting/e-voting/e-voting/-/issues/1): the experts who have reported most of the serious cryptographic vulnerabilities in the system. 

Although there is a little difference: in Thomas' paper he mentions a malicious Control Component is required to perform this kind of attack but I found a malicious Voting Server is enough, due to the Voting Server's 'Election Information 100' certificate chain.

## Vulnerabilities

###  _#YWH-PGM2323-53_ \- Multiple unchecked length values during SafeStreamDeserialization may crash Control Components

 _Description_

The Orchestrator service, part of the untrusted Voting Server, communicates with the Control Components using AMQP messages through a RabbitMQ cluster.

The control components implement specific deserialization logic for some of those messages. A lack of proper length validation during the deserialization of potentially attacker-controlled messages can force an out of memory error, thus crashing the affected component.

_Technical Details_

The 'unpackArrayHeader()' (or similar unpack* functions) is used multiple times without enforcing any bounds checking (see lines 156, 101, 115, 129, 100 in the following files). As a result, an overly large signed integer value is used to initialize lists and allocate arrays, which may result in a '_java.lang.OutOfMemoryError: Java heap space_ ' error, thus crashing the affecting component.

(Version: 0.12.0.0)

File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/KeyCreationDTO.java
  
  
  144:  @Override
  145:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  146:  try {
  147:  setCorrelationId(UUID.fromString(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker)));
  148:  this.requestId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  149:  this.signature = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  150:  this.resourceId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  151:  this.encryptionParameters = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  152:  this.electionEventId = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  153:  this.from = StreamSerializableUtil.retrieveDateValueWithNullCheck(unpacker);
  154:  this.to = StreamSerializableUtil.retrieveDateValueWithNullCheck(unpacker);
  155:  if (!unpacker.tryUnpackNil()) {
  156:  int listSize = unpacker.unpackArrayHeader();
  157:  this.publicKeys = new ArrayList<>(listSize);
  158:  for (int i = 0; i < listSize; i++) {
  159:  CCPublicKey key = new CCPublicKey();
  160:  key.deserialize(unpacker);
  161:  publicKeys.add(key);
  162:  }
  163:  } else {
  164:  publicKeys = null;
  165:  }
  166:  } catch (IOException e) {
  167:  throw new SafeStreamDeserializationException(e);
  168:  }
  169:  }

File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ChoiceCodesVerificationDecryptResPayload.java
  
  
  096:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  097:  try {
  098:  if (unpacker.tryUnpackNil()) {
  099:  decryptContributionResult = null;
  100:  } else {
  101:  int listSize = unpacker.unpackArrayHeader();
  102:  decryptContributionResult = new ArrayList<>(listSize);
  103:  for (int i = 0; i < listSize; i++) {
  104:  decryptContributionResult.add(StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker));
  105:  }
  106:  }
  107:  exponentiationProofJson = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  108:  publicKeyJson = StreamSerializableUtil.retrieveStringValueWithNullCheck(unpacker);
  109:  if (unpacker.tryUnpackNil()) {
  110:  this.signature = null;
  111:  } else {
  112:  int arraySize = unpacker.unpackArrayHeader();
  113:  X509Certificate[] certs = new X509Certificate[arraySize];

File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ReturnCodesExponentiationResponsePayload.java
  
  
  110:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  111:  try {
  112:  if (unpacker.tryUnpackNil()) {
  113:  pccOrCkToLongReturnCodeShare = null;
  114:  } else {
  115:  int mapSize = unpacker.unpackMapHeader();
  116:  pccOrCkToLongReturnCodeShare = new LinkedHashMap<>(mapSize);
  117:  for (int i = 0; i < mapSize; i++) {
  118:  BigInteger key = retrieveBigIntegerValueWithNullCheck(unpacker);
  119:  BigInteger value = retrieveBigIntegerValueWithNullCheck(unpacker);
  120:  pccOrCkToLongReturnCodeShare.put(key, value);
  121:  }
  122:  }
  123:  exponentiationProofJson = retrieveStringValueWithNullCheck(unpacker);
  124:  voterChoiceReturnCodeGenerationPublicKeyJson = retrieveStringValueWithNullCheck(unpacker);
  125:  voterVoteCastReturnCodeGenerationPublicKeyJson = retrieveStringValueWithNullCheck(unpacker);
  126:  if (unpacker.tryUnpackNil()) {
  127:  this.signature = null;
  128:  } else {
  129:  int arraySize = unpacker.unpackArrayHeader();
  130:  X509Certificate[] certs = new X509Certificate[arraySize];

File: e-voting-master/domain/src/main/java/ch/post/it/evoting/domain/returncodes/ReturnCodesInput.java
  
  
  095:  public void deserialize(MessageUnpacker unpacker) throws SafeStreamDeserializationException {
  096:  try {
  097:  if (unpacker.tryUnpackNil()) {
  098:  this.returnCodesInputElements = null;
  099:  } else {
  100:  int listSize = unpacker.unpackArrayHeader();
  101:  returnCodesInputElements = new ArrayList<>(listSize);
  102:  for (int i = 0; i < listSize; i++) {
  103:  returnCodesInputElements.add(StreamSerializableUtil.retrieveBigIntegerValueWithNullCheck(unpacker));
  104:  }
  105:  }

The deserialization of the received messages relies on the open-source '_msgpack_ ' code, the _{unpack*Header}_ functions end up invoking '_getInt_ ', so there is no safeguard either at that component level.

<https://github.com/msgpack/msgpack-java/blob/651a2a02fd5f269d91183cf70e162dea7a5d9caa/msgpack-core/src/main/java/org/msgpack/core/buffer/MessageBuffer.java#L459>
  
  
  public int getInt(int index)
  {
  // Reading little-endian value
  int i = unsafe.getInt(base, address + index);
  // Reversing the endian
  return Integer.reverseBytes(i);
  }

The RabbitMQ message size limit mitigation is also out of the scope of this issue. We're not sending an overly large [RabbitMQ](https://www.rabbitmq.com/) message, we are sending a especially crafted serialized message, that once deserialized by _[MessagePack](https://msgpack.org/index.html)_ provides the large integer values that are consumed by the e-voting code but the actual RabbitMQ message may be just several KBs. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSobaeAUQXZr77HBCs790PUYiQtP_AlQI4FhhpTQ64nFe3X2mh_vT-TXP0BRJAiZM1HGw8Iviiazaaab00ElQCrIue55-TIwuGq3R4RbLTqLSYy-TugoU8CUTm0GDSxdhSHm2TK6_5yIKMavstAMlpkQbuW5UQMezYWcjhjfZDR9_fly8R0Kl1_nFhMA/w640-h308/dos_deserialize.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSobaeAUQXZr77HBCs790PUYiQtP_AlQI4FhhpTQ64nFe3X2mh_vT-TXP0BRJAiZM1HGw8Iviiazaaab00ElQCrIue55-TIwuGq3R4RbLTqLSYy-TugoU8CUTm0GDSxdhSHm2TK6_5yIKMavstAMlpkQbuW5UQMezYWcjhjfZDR9_fly8R0Kl1_nFhMA/s1846/dos_deserialize.png)

  

###  _#YWH-PGM2323-64_ \- Verifier does not properly verify the signature of NodeContributions

 _Description_

The verifier is using potentially malicious data to dynamically adjust the values that will determine whether a successful verification has been performed.

When checking the Node Contributions resulting from the '_GenEncLongCodeShares_ ', the verifier uses data, coming from the Control Components, that has not been yet verified in order to set up its own verification logic.

_Technical Details_

(v 0.12.3)

At line 165 the _NodeContributions_ are persisted by the SDM, once they have been collected from the Orchestrator.

File: e-voting-master/secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/VotingCardSetService.java
  
  
  133:  /**
  134:  * Download the computed values for a votingCardSet
  135:  *
  136:  * @throws InvalidStatusTransitionException if the original status does not allow the download
  137:  */
  138:  public void download(String votingCardSetId, String electionEventId)
  139:  throws ResourceNotFoundException, InvalidStatusTransitionException, IOException {
  140: 
  141:  if (!idleStatusService.getIdLock(votingCardSetId)) {
  142:  return;
  143:  }
  144: 
  145:  try {
  146:  Status fromStatus = Status.COMPUTED;
  147:  Status toStatus = Status.VCS_DOWNLOADED;
  148: 
  149:  checkVotingCardSetStatusTransition(electionEventId, votingCardSetId, fromStatus, toStatus);
  150: 
  151:  JsonObject votingCardSetJson = votingCardSetRepository.getVotingCardSetJson(electionEventId, votingCardSetId);
  152:  String verificationCardSetId = getVerificationCardSetId(votingCardSetJson);
  153: 
  154:  deleteNodeContributions(electionEventId, verificationCardSetId);
  155: 
  156:  int chunkCount;
  157:  try {
  158:  chunkCount = returnCodeGenerationRequestPayloadRepository.getCount(electionEventId, verificationCardSetId);
  159:  } catch (PayloadStorageException e) {
  160:  throw new IllegalStateException("Failed to get the chunk count.", e);
  161:  }
  162: 
  163:  for (int i = 0; i < chunkCount; i++) {
  164:  try (InputStream contributions = votingCardSetChoiceCodesService.download(electionEventId, verificationCardSetId, i)) {
  165:  writeNodeContributions(electionEventId, verificationCardSetId, i, contributions);
  166:  }
  167:  }
  168: 
  169:  configurationEntityStatusService.update(toStatus.name(), votingCardSetId, votingCardSetRepository);
  170: 
  171:  } finally {
  172:  idleStatusService.freeIdLock(votingCardSetId);
  173:  }
  174: 
  175:  }

During verification, the persisted Node contributions are then loaded, deserialized and verified. However, at line 190 we can see that the verifier use '_payload.getNodeId()_ ', a value belonging to a payload for which its signature has not been yet validated, to choose the CCN CA that will be used to validate the certificate chain of the signature. This can be used by an attacker to trick the verifier into using a certificate chain, which may belong to a malicious Control Component, to validate a tampered contribution of the honest Control Component.

File: verifier-master/verifier-block1/src/main/java/ch/post/it/evoting/verifier/block/block1/verifications/CheckSigNodeContributions.java
  
  
  172:  // Data class that represent node contributions signature to verify
  173:  static class NodeOutputSignature {
  174:  private final byte[] signature;
  175:  private final byte[] payloadHash;
  176:  private final X509Certificate signingCertificate;
  177:  private final List<X509Certificate> intermediateCertificates;
  178:  private final X509Certificate rootCertificate;
  179: 
  180:  // Massage the data to get it into the expected format for the verification algorithm
  181:  NodeOutputSignature(final ReturnCodeGenerationResponsePayload payload, final NodeCertificates nodeCertificates, HashService hashService,
  182:  CertificateLoader certificateLoader) {
  183:  // Signature
  184:  this.signature = payload.getSignature().getSignatureContents();
  185:  this.payloadHash = hashService.recursiveHash(payload);
  186: 
  187:  // Certificates chain
  188:  this.signingCertificate = payload.getSignature().getCertificateChain()[0];
  189:  final List<Path> filteredCertificates = nodeCertificates.nodeCertificatesPaths.stream()
  190:  .filter(ccPath -> ccPath.getFileName().toString().equals("cc" + payload.getNodeId() + "_CA.pem"))
  191:  .collect(Collectors.toList());
  192:  this.intermediateCertificates = Collections.singletonList(certificateLoader.loadCertificate(filteredCertificates.get(0)));
  193:  this.rootCertificate = nodeCertificates.rootCertificate;
  194:  }
  195:  }

The verifier should limit the use of potentially attacker-controlled data while performing the different verifications. Before verification, the data to be validated should not be part of the values involved in the own validation. Otherwise, there is a risk to validate data that may have been tampered in the component that persisted that data, thus populating any potential issue abused in a component providing inputs to the verifier into the own verifier.

In this specific case, if we are expecting to verify contributions from 4 nodes, for which their CCN CA are known, the verifier should check whether the node Id _n_ (without using the _nodeId_ from the not yet verified payload) is actually using the CCN CA _n_ , but also that all the contributions come from four different nodes, and that the same node _Id_ has not been used to sign another node's contribution.

### _#YWH-PGM2323-65_ \- Generation of 'Choice Return Codes encryption' Public Key and 'Election' Public Key may be influenced by a malicious voting server

 _Description_

ELpk and pkCCR are generated by combining the public key contributions of the CCM and CCR nodes. These contributions are collected from the Control Components by the Voting Server and sent to the Setup Component, as can be seen in the 'System Specification' document.

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglPSSnmxuLO64s5YwIf1CppZGe-REpdidTHkmu6rnLktyXP7L9aftGk8y7AYdYeA5W2MzVUDdRB__og63xDj7k9f2eAnpsOJEEdbGtpIbR3bwbKS2xQ4PVWFRaRz7NsTumeopEZQnIeu971VaqqD8Et4G_2ZRVthYlLt7nRFjsLCOc7TOyXSHx12L6oA/w640-h212/setuptallyebvoting.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglPSSnmxuLO64s5YwIf1CppZGe-REpdidTHkmu6rnLktyXP7L9aftGk8y7AYdYeA5W2MzVUDdRB__og63xDj7k9f2eAnpsOJEEdbGtpIbR3bwbKS2xQ4PVWFRaRz7NsTumeopEZQnIeu971VaqqD8Et4G_2ZRVthYlLt7nRFjsLCOc7TOyXSHx12L6oA/s1856/setuptallyebvoting.png)

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx6pLDwL0iHkmccPfmrVPDulnhg-roP3h91ICvrT9IS1Bq4yMm4dRwaJetdD98gHPcKU-en188o8TSC3k9psGEqW43LG6KmJN5En0FY7H8mHcYPhzw8AmN_adi2Ra5j8dQymagM7EtA4c1nQqd4ee--HVm7mH-e06UFYZXUaBm-8dw8yesn1AeK8D43w/w640-h150/genccrkeys.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjx6pLDwL0iHkmccPfmrVPDulnhg-roP3h91ICvrT9IS1Bq4yMm4dRwaJetdD98gHPcKU-en188o8TSC3k9psGEqW43LG6KmJN5En0FY7H8mHcYPhzw8AmN_adi2Ra5j8dQymagM7EtA4c1nQqd4ee--HVm7mH-e06UFYZXUaBm-8dw8yesn1AeK8D43w/s1864/genccrkeys.png)

  

  

These public keys are individually signed by the corresponding CCR/CCM Signing certificate, which later on are verified by the Setup Component before combining them to generate the final public keys. However, the Setup Component does not validate the number of public keys that have been received from the Voting Server matches the amount of public keys defined in the protocol specification. Thus, a malicious voting server can just return to the Setup Component an arbitrary number of properly signed public keys, that will be validated by the Setup Component and then combined.

As a result, this combination of an arbitrary number of public keys can be abused to maliciously influence the resulting ELpk and pkCCR keys, in such a way that it may compromise the ability to decrypt all votes in an election event.

It's important to note that this attack does not rely on being able to bypass the implemented signature logic, but it is based on the ability to increase the number of valid public keys that are used during the generation of ELpk and pkCCR

 _Technical Details_

The following Runnable lambda '_serializePublicKey_ ' triggers the logic that generates the ELpk

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ElectoralAuthorityService.java
  
  
  305:  public void writeShare(final String electionEventId, final String electoralAuthorityId, final Integer shareNumber, final String pin)
  306:  throws IOException, GeneralCryptoLibException, SharesException, ResourceNotFoundException {
  307: 
  308:  CreateSharesHandler createSharesHandlerElGamal = getHandler(electoralAuthorityId);
  309: 
  310:  JsonObject electoralAuthority = getElectoralAuthorityJsonObject(electoralAuthorityId);
  311:  JsonArray electoralAuthorityMembers = electoralAuthority.getJsonArray(Constants.ELECTORAL_BOARD_LABEL);
  312: 
  313:  Runnable serializePublicKey = () -> {
  314: 
  315:  try {
  316:  JsonArray mixingKeysJsonArray = controlComponentKeysAccessorService.downloadMixingKeys(electoralAuthorityId);
  317: 
  318:  controlComponentKeysAccessorService.writeMixingKeys(electionEventId, electoralAuthorityId, mixingKeysJsonArray);
  319: 
  320:  serializePublicKeysAndVerifyThatTheyWereWritten(electionEventId, electoralAuthorityId, createSharesHandlerElGamal);
  321: 
  322:  updateElectoralAuthorityStatus(electoralAuthorityId, electoralAuthority);
  323: 
  324:  createSharesHandlerElGamalMap.remove(electionEventId);
  325:  } catch (ResourceNotFoundException | SharesException | IOException e) {
  326:  throw new LambdaException(e);
  327:  }
  328:  };
  329: 

It will be executed by '_processShare_ ' when the last share for the EBsk has been written (line 308)

File: secure-data-manager/config-generator/config-shares/src/main/java/ch/post/it/evoting/sdm/config/shares/handler/CreateSharesHandler.java
  
  
  294:  private void processShare(final int i, final String name, final String oldPinPuk, final String newPinPuk,
  295:  final PrivateKey privateKeyToBeUsedToSign, Runnable finalOperation) throws SharesException {
  296: 
  297:  Share share = shares.get(i);
  298: 
  299:  try {
  300:  smartcardService.write(share, name, oldPinPuk, newPinPuk, privateKeyToBeUsedToSign);
  301:  } catch (SmartcardException e) {
  302:  throw new SharesException("An error occured while trying to write a share", e);
  303:  }
  304: 
  305:  numSharesWritten++;
  306: 
  307:  if (numSharesWritten == shares.size()) {
  308:  finalOperation.run();
  309:  wipeAllSharesFromMemory();
  310:  }
  311:  }

At line 320 from the previous '_serializePublicKey_ ' lambda, we can see how the CCMj  election keys are going to be verified, combined and persisted at '_serializePublicKeysAndVerifyThatTheyWereWritten_ '

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ElectoralAuthorityService.java
  
  
  512:  private void serializePublicKeysAndVerifyThatTheyWereWritten(final String electionEventId, final String electoralAuthorityId,
  513:  final CreateSharesHandler createSharesHandler) throws SharesException, ResourceNotFoundException {
  514: 
  515:  CreateElectoralBoardKeyPairInput createEbKeyPairInput = el***REDACTED-SUSPECT-TOKEN***  516:  .generate(electoralAuthorityId, electionEventId);
  517:  Path outputFolder = pathResolver.resolve(createEbKeyPairInput.getOutputFolder());
  518: 
  519:  final ElGamalPublicKey electoralAuthorityPublicKey = getElectoralAuthorityPublicKey(createSharesHandler);
  520: 
  521:  JsonArray mixingKeysJsonArray = controlComponentKeysAccessorService.downloadMixingKeys(electoralAuthorityId);
  522: 
  523:  final List<ElGamalPublicKey> mixingPublicKeys = getMixingElGamalPublicKeys(electionEventId, electoralAuthorityId, mixingKeysJsonArray);
  524: 
  525:  ElGamalPublicKey electionPublicKey = combineUsingCompression(electoralAuthorityPublicKey, mixingPublicKeys);
  526: 
  527:  boolean areElectoralAuthorityKeysSerialized = createEBKeysSerializer
  528:  .serializeElectionPublicKeys(outputFolder, electoralAuthorityId, electionPublicKey, electoralAuthorityPublicKey);
  529:  if (!areElectoralAuthorityKeysSerialized) {
  530:  throw new IllegalStateException(
  531:  "The serialization of the Electoral Authority public keys failed. They might not be written to file. Stopping the process.");
  532:  }
  533: 
  534:  }
  535: 

At line 523 '_getMixingElGamalPublicKeys_ ' is invoked, which basically iterates over all the existent '_publicKey_ ' objects, without following the specification of '_SetupTallyEB_ ' which clearly defines the number of nodes that should contribute to this operation.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPtnW48dcglSUKjWnJ4sn8BIAVJFhUgv1XKQyR7ZwcR42ZYAlItxT8cI9d9ghPjSlsCbfTLfXSX1pVymxadzDpoAQkQihvlsYQ4yQM59xeB9HB-UmOVc-ueWiXL9egf45DrrocPrWUvKpkPNiBCmRrkzxa_0XuRGk1K4eXRzr7DyWHP6gVUXepnEEoSQ/w640-h392/setuptallyeb.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhPtnW48dcglSUKjWnJ4sn8BIAVJFhUgv1XKQyR7ZwcR42ZYAlItxT8cI9d9ghPjSlsCbfTLfXSX1pVymxadzDpoAQkQihvlsYQ4yQM59xeB9HB-UmOVc-ueWiXL9egf45DrrocPrWUvKpkPNiBCmRrkzxa_0XuRGk1K4eXRzr7DyWHP6gVUXepnEEoSQ/s1844/setuptallyeb.png)

  

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ElectoralAuthorityService.java

  

  
  
  548:  private List<ElGamalPublicKey> getMixingElGamalPublicKeys(String electionEventId, String electoralAuthorityId, JsonArray mixingKeysJsonArray) {
  549:  List<ElGamalPublicKey> mixingPublicKeys = new ArrayList<>();
  550:  try {
  551:  X509Certificate rootCACertificate = platformRootCAService.load();
  552:  for (JsonObject jsonObject : jsonArrayToJsonObjects(mixingKeysJsonArray)) {
  553:  ElGamalPublicKey publicKey = ElGamalPublicKey.fromJson(jsonObject.get("publicKey").toString());
  554:  byte[] signature = Base64.getDecoder().decode(jsonObject.getString("signature"));
  555:  X509Certificate signingCertificate = (X509Certificate) PemUtils.certificateFromPem(jsonObject.getString("signerCertificate"));
  556:  X509Certificate nodeCACertificate = (X509Certificate) PemUtils.certificateFromPem(jsonObject.getString("nodeCACertificate"));
  557:  X509Certificate[] chain = { signingCertificate, nodeCACertificate, rootCACertificate };
  558:  keySignatureValidator.checkMixingKeySignature(signature, chain, publicKey, electionEventId, electoralAuthorityId);
  559:  mixingPublicKeys.add(publicKey);
  560:  }
  561:  } catch (SignatureException | GeneralCryptoLibException | CertificateManagementException e) {
  562:  throw new IllegalStateException("Failed to get mixing ElGamal public keys", e);
  563:  }
  564:  return mixingPublicKeys;
  565:  }

  

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ElectoralAuthorityService.java

  

  
  
  567:  private List<JsonObject> jsonArrayToJsonObjects(JsonArray array) {
  568:  List<JsonObject> jsonObjects = new ArrayList<>(array.size());
  569:  for (int i = 0; i < array.size(); i++) {
  570:  jsonObjects.add(array.getJsonObject(i));
  571:  }
  572:  return jsonObjects;
  573:  }

  

Then '_combineUsingCompression_ ' is invoked to combine the EBsk with the CCMj public keys, thus yielding the final ELpk

  

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/application/service/ElectoralAuthorityService.java

  

  
  
  536:  public ElGamalPublicKey combineUsingCompression(ElGamalPublicKey electoralAuthorityPublicKey, List<ElGamalPublicKey> mixingPublicKeys) {
  537: 
  538:  ElGamalPublicKey combinedPublicKey;
  539:  try {
  540:  combinedPublicKey = new ElGamalPublicKeyCombinerWithCompression().combine(electoralAuthorityPublicKey, mixingPublicKeys);
  541:  } catch (GeneralCryptoLibException e) {
  542:  throw new ElectoralAuthorityServiceException("Exception when trying to combine public keys: " + e.getMessage(), e);
  543:  }
  544: 
  545:  return combinedPublicKey;
  546:  }

  

We can see how '_combine_ ' doesn't check the number of contributions either, iterating over the entire list of public keys.

  

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/domain/service/utils/ElGamalPublicKeyCombinerWithCompression.java
  
  
  40:  public ElGamalPublicKey combine(ElGamalPublicKey primaryElGamalPublicKey, List<ElGamalPublicKey> keysToBeCombined)
  41:  throws GeneralCryptoLibException {
  42: 
  43:  validateInputs(primaryElGamalPublicKey, keysToBeCombined);
  44: 
  45:  int numRequiredElements = primaryElGamalPublicKey.getKeys().size();
  46: 
  47:  ElGamalPublicKey combinedKey = primaryElGamalPublicKey;
  48: 
  49:  GroupElementsCompressor<ZpGroupElement> compressor = new GroupElementsCompressor<>();
  50: 
  51:  for (ElGamalPublicKey key : keysToBeCombined) {
  52: 
  53:  List<ZpGroupElement> subkeys = key.getKeys();
  54: 
  55:  if (subkeys.size() > numRequiredElements) {
  56: 
  57:  List<ZpGroupElement> compressedList = compressor.buildListWithCompressedFinalElement(numRequiredElements, subkeys);
  58: 
  59:  key = new ElGamalPublicKey(compressedList, key.getGroup());
  60:  }
  61: 
  62:  combinedKey = combinedKey.multiply(key);
  63:  }
  64: 
  65:  return combinedKey;
  66:  }

  

We find a similar scenario during the generation of pkCCR based on the CCMj Choice Return Codes encryption keys

  

The number of contributions is not validated as specified in '_GenVerCardSetKeys_ '

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1a0WUlEKUzMPn77G1MelJMIiVRw6SsECfkGtyh7t14tg_w98gWeXYBaE5kPW-gH3ci1jFLAZj-8YwF_2y5SJApKQcRyGq5Ck6rYsmjDKdn9Txt_VBW2NGJ32a_lGJ2TxYhnUJ24TYczHP0BPWQnl0ai--I2L364XwJ0tJPm3LibBlSS6Hz2_XO93fwA/w640-h436/genvercardkeys.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1a0WUlEKUzMPn77G1MelJMIiVRw6SsECfkGtyh7t14tg_w98gWeXYBaE5kPW-gH3ci1jFLAZj-8YwF_2y5SJApKQcRyGq5Ck6rYsmjDKdn9Txt_VBW2NGJ32a_lGJ2TxYhnUJ24TYczHP0BPWQnl0ai--I2L364XwJ0tJPm3LibBlSS6Hz2_XO93fwA/s1782/genvercardkeys.png)

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/domain/service/impl/VotingCardSetDataGeneratorServiceImpl.java
  
  
  276:  private void validateChoiceCodesEncryptionKey(String electionEventId, String verificationCardId, List<String> keys) {
  277:  try {
  278:  X509Certificate rootCACertificate = platformRootCAService.load();
  279:  Decoder decoder = Base64.getDecoder();
  280:  for (String string : keys) {
  281:  JsonObject object = JsonUtils.getJsonObject(string);
  282:  ElGamalPublicKey key = ElGamalPublicKey.fromJson(object.get("publicKey").toString());
  283:  byte[] signature = decoder.decode(object.getString("signature"));
  284:  X509Certificate signingCertificate = (X509Certificate) PemUtils.certificateFromPem(object.getString("signerCertificate"));
  285:  X509Certificate nodeCACertificate = (X509Certificate) PemUtils.certificateFromPem(object.getString("nodeCACertificate"));
  286:  X509Certificate[] chain = { signingCertificate, nodeCACertificate, rootCACertificate };
  287:  keySignatureValidator.checkChoiceCodesEncryptionKeySignature(signature, chain, key, electionEventId, verificationCardId);
  288:  }
  289:  } catch (SignatureException | GeneralCryptoLibException | CertificateManagementException e) {
  290:  throw new IllegalStateException("Invalid choice codes encryption keys.", e);
  291:  }
  292:  }

Then at line 199 the List of pkCCRj,i keys is assigned as a parameter for the upcoming job task.

File: secure-data-manager/secure-data-manager-backend/services/src/main/java/ch/post/it/evoting/sdm/domain/service/impl/VotingCardSetDataGeneratorServiceImpl.java
  
  
  List<String> choiceCodeEncryptionKey = getChoiceCodesEncryptionKey(choiceCodeKeysJsonArray);
  176:  validateChoiceCodesEncryptionKey(electionEventId, verificationCardSetId, choiceCodeEncryptionKey);
  177: 
  178:  controlComponentKeysAccessorService.writeChoiceCodeKeys(electionEventId, verificationCardSetId, choiceCodeKeysJsonArray);
  179: 
  180:  CreateVotingCardSetInput createVotingCardSetInput = new CreateVotingCardSetInput();
  181:  createVotingCardSetInput.setStart(ballotBox.getString(JsonConstants.DATE_FROM));
  182:  createVotingCardSetInput.setElectoralAuthorityID(electoralAuthorityId);
  183:  createVotingCardSetInput.setEnd(ballotBox.getString(JsonConstants.DATE_TO));
  184:  createVotingCardSetInput
  185:  .setValidityPeriod(electionEvent.getJsonObject(JsonConstants.SETTINGS).getInt(JsonConstants.CERTIFICATES_VALIDITY_PERIOD));
  186:  createVotingCardSetInput.setBasePath(configElectionEventPath.toString());
  187:  createVotingCardSetInput.setBallotBoxID(ballotBoxId);
  188:  createVotingCardSetInput.setBallotID(ballotId);
  189:  createVotingCardSetInput.setBallotPath(destinationBallotFilePath.toString());
  190:  createVotingCardSetInput.setEeID(electionEventId);
  191:  createVotingCardSetInput.setNumberVotingCards(votingCardSet.getInt(JSON_PARAM_NAME_NR_OF_VC_TO_GENERATE));
  192:  createVotingCardSetInput.setVerificationCardSetID(verificationCardSetId);
  193:  createVotingCardSetInput.setVotingCardSetID(id);
  194: 
  195:  // INCLUDE ALIAS INSIDE THE OBJECT...
  196:  createVotingCardSetInput.setVotingCardSetAlias(votingCardSet.getString(JsonConstants.ALIAS, ""));
  197: 
  198:  createVotingCardSetInput.setKeyForProtectingKeystorePassword(getPublicKeyForProtectingKeystorePassword());
  199:  createVotingCardSetInput.setChoiceCodesEncryptionKey(choiceCodeEncryptionKey);
  200: 
  201:  createVotingCardSetInput.setPlatformRootCACertificate(PemUtils.certificateToPem(platformRootCAService.load()));
  202: 
  203:  createVotingCardSetInput.setCreateVotingCardSetCertificateProperties(getCertificateProperties());
  204: 
  205:  final ResponseEntity<StartVotingCardGenerationJobResponse> startJobResponse;
  206:  try {
  207:  startJobResponse = sendStartJobRequest(tenantId, electionEventId, createVotingCardSetInput);

Eventually, the list of pkCCRj,i is combined without checking the allowed number of contributions.

File: secure-data-manager/config-generator/config-engine/src/main/java/ch/post/it/evoting/sdm/config/commands/voters/datapacks/generators/VerificationCardSetCredentialDataPackGenerator.java
  
  
  103:  combinedChoiceCodesEncryptionPublicKey = choiceCodesEncryptionPublicKey;
  104:  for (int i = 1; i < choiceCodesEncryptionKeys.length; i++) {
  105:  jsonNode = mapper.readTree(choiceCodesEncryptionKeys[i]);
  106:  choiceCodesEncryptionPublicKeyJson = jsonNode.get("publicKey").toString();
  107:  choiceCodesEncryptionPublicKey = ElGamalPublicKey.fromJson(choiceCodesEncryptionPublicKeyJson);
  108:  nonCombinedChoiceCodesEncryptionPublicKeys[i] = choiceCodesEncryptionPublicKey;
  109:  combinedChoiceCodesEncryptionPublicKey = combinedChoiceCodesEncryptionPublicKey.multiply(choiceCodesEncryptionPublicKey);
  110:  }
  111: 
  112:  LOGGER.info(ConfigGeneratorLogEvents.GENVCD_SUCCESS_GENERATING_CHOICES_CODES_KEYPAIR.getInfo(), inputDataPack.getEeid(),
  113:  Constants.ADMIN_ID, Constants.VERIFCS_ID, verificationCardSetID);
  114: 
  115:  } catch (Exception e) {
  116: 
  117:  LOGGER.error(ConfigGeneratorLogEvents.GENVCD_ERROR_GENERATING_CHOICES_CODES_KEYPAIR.getInfo(), inputDataPack.getEeid(),
  118:  Constants.ADMIN_ID, Constants.VERIFCS_ID, verificationCardSetID, Constants.ERR_DESC, e.getMessage());
  119: 
  120:  throw new CreateVotingCardSetException("An error occurred while trying to set the choices codes ElGamal public key", e);
  121:  }
  122: 
  123:  dataPack.setChoiceCodesEncryptionPublicKey(combinedChoiceCodesEncryptionPublicKey);

  

### _#YWH-PGM2323-59,60,61_ \- Multiple improper signature verification issues.

As these issues have been marked as 'Duplicated' I will just include one of the examples (#60, affecting 'MixDecOnline') to illustrate the problem.

_Description_

The MixNet 'initial' payload sent from the Voting Server to the first Control Component is signed using a private key belonging to the 'Election Information' certificate chain, made available in a keystore (by design) to the Voting Server. The subsequent 'shuffle' payloads generated by the different Control Components are then signed using a signing key belonging to each of the CCN certificate chains.

However, it's important to note that both certificate chains share the same trusted cert as shown in the image.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpgqMnDkXBvZRjr9j7luVC5oE6nN7FRR1c1S0DsLm09EDMqDAWLMPQqYeH3fWkfVKIU371wFKUuCWW2-6TkCg8RMiF_G00i3IxI3ORehjjLWFn5IWfvutLeATQ4MoIM7eH9YIxgZRcfjD9WljgxnKFS5gzilkJv_N2sPJ7wsphfhucUSyhVr3NnveMeQ/w640-h284/mix3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpgqMnDkXBvZRjr9j7luVC5oE6nN7FRR1c1S0DsLm09EDMqDAWLMPQqYeH3fWkfVKIU371wFKUuCWW2-6TkCg8RMiF_G00i3IxI3ORehjjLWFn5IWfvutLeATQ4MoIM7eH9YIxgZRcfjD9WljgxnKFS5gzilkJv_N2sPJ7wsphfhucUSyhVr3NnveMeQ/s1936/mix3.png)

  

The vulnerability can be found in how the signature validation of these payloads ('initial' and 'shuffle') has been implemented in the CCN's '_MixDecryptMessageConsumer_ ', as the signature for both kinds of payloads is validated using the same logic, which only relies on checking whether the certificate chain is validated by the trusted certificate (Platform Root CA).

As a result, a malicious Voting Server can modify any '_shuffle_ ' payload that will be accepted by a honest control component. In addition to this, as the signature validation logic is the same in '_ReturnCodesGenerationConsumer_ ' the voting server's '_Election Information_ ' certificate chain can be used to perform the impersonation attack without even requiring the collusion of a malicious Control Component.

_Technical Details_

 _  
_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0kVtVt3ISNFdIy_zazOyBm-eyMTt5_7EomdVmFQCGHSzPAIxQ_jbzP5zGk-pkkqa_ZIP_NxwJrL8mx4PwB-8ScQOY4FHYEwHwAMD-bUHcQXAVN4QwQaiE_rLHRWxwCRZ7ABGW9e1_oGWfG3BumDjdqcSfidosfl4GDgRgRfzpFxPTEnb0YMAKZnFyw/w640-h226/mix1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl0kVtVt3ISNFdIy_zazOyBm-eyMTt5_7EomdVmFQCGHSzPAIxQ_jbzP5zGk-pkkqa_ZIP_NxwJrL8mx4PwB-8ScQOY4FHYEwHwAMD-bUHcQXAVN4QwQaiE_rLHRWxwCRZ7ABGW9e1_oGWfG3BumDjdqcSfidosfl4GDgRgRfzpFxPTEnb0YMAKZnFyw/s1976/mix1.png)

  
_  
_

The online Mixing control components CCM shuffle (and re-encrypt) the previous control component’s ciphertexts and perform partial decryption. The payload of the input list of ciphertexts c dec,j-1 corresponds to the cleansed encrypted votes cdec,0 and the other input, the remaining election public key ELpk,j-1 equals the election public key ELpk.

The initial mixnet payload created after the 'Cleansing' process is signed (line 175) by the Voting Server using the Election Information Signing key. The Certificate chain (line 158) is set to the 'Election Information' as shown in the above diagram.

  

  
  
  File: e-voting-master/voting-server/election-information/src/main/java/ch/post/it/evoting/votingserver/electioninformation/services/domain/service/ballotbox/CleansedBallotBoxServiceImpl.java
  110:  @Override
  111:  public MixnetInitialPayload getMixnetInitialPayload(final BallotBoxId ballotBoxId)
  112:  throws ResourceNotFoundException, CleansedBallotBoxServiceException {
  113: 
  114:  checkNotNull(ballotBoxId);
  115: 
  116:  // Find out how many vote sets fit the ballot box.
  117:  final int voteCount;
  118:  try {
  119:  voteCount = cleansedBallotBoxRepository.count(ballotBoxId);
  120:  } catch (CleansedBallotBoxRepositoryException e) {
  121:  throw new CleansedBallotBoxServiceException(String.format("Failed to count votes for ballot box %s.", ballotBoxId), e);
  122:  }
  123: 
  124:  // Get the encryption parameters from the ballot box information.
  125:  final JsonObject ballotBoxInformation = getBallotBoxInformationJson(ballotBoxId);
  126:  final JsonObject encryptionParametersJson = ballotBoxInformation.getJsonObject(ENCRYPTION_PARAMETERS_JSON_FIELD);
  127: 
  128:  final BigInteger p = new BigInteger(encryptionParametersJson.getString(P_JSON_FIELD));
  129:  final BigInteger q = new BigInteger(encryptionParametersJson.getString(Q_JSON_FIELD));
  130:  final BigInteger g = new BigInteger(encryptionParametersJson.getString(G_JSON_FIELD));
  131:  final GqGroup encryptionParameters = new GqGroup(p, q, g);
  132: 
  133:  // Convert the EncryptedVotes to ElGamalMultiRecipientCiphertext.
  134:  final List<ElGamalMultiRecipientCiphertext> encryptedVotes = cleansedBallotBoxRepository.getVoteSet(ballotBoxId, 0, voteCount)
  135:  .map(vote -> ElGamalMultiRecipientCiphertext.create(GqElement.create(vote.getGamma(), encryptionParameters),
  136:  vote.getPhis().stream().map(bi -> GqElement.create(bi, encryptionParameters)).collect(Collectors.toList())))
  137:  .collect(Collectors.toList());
  138: 
  139:  // Get the election public key.
  140:  final ElGamalMultiRecipientPublicKey electionPublicKey;
  141:  try {
  142:  // Get the electoral authority identifier.
  143:  final String electoralAuthorityId = ballotBoxInformation.getString(ELECTORAL_AUTHORITY_ID_JSON_FIELD);
  144: 
  145:  // Get the vote encryption key, which at this stage is the electoral authority public key.
  146:  final ElGamalPublicKey voteEncryptionKey = getVoteEncryptionKey(TENANT_ID, ballotBoxId.getElectionEventId(), electoralAuthorityId);
  147:  final List<ZpGroupElement> keys = voteEncryptionKey.getKeys();
  148: 
  149:  // Convert cryptolib public key to crypto-primitives public key.
  150:  electionPublicKey = keys.stream().map(k -> GqElement.create(k.getValue(), encryptionParameters))
  151:  .collect(Collectors.collectingAndThen(Collectors.toList(), ElGamalMultiRecipientPublicKey::new));
  152:  } catch (GeneralCryptoLibException | IOException e) {
  153:  throw new CleansedBallotBoxServiceException("Failed to retrieve election public key.");
  154:  }
  155: 
  156:  // Get the certificate chain for the election information public key.
  157:  LOGGER.info("Finding the validation key certificate chain for ballot box {}...", ballotBoxId);
  158:  final X509Certificate[] fullCertificateChain = eiTenantSystemKeys.getSigningCertificateChain(TENANT_ID);
  159:  if (null == fullCertificateChain) {
  160:  throw new CleansedBallotBoxServiceException("No certificate chain was found for tenant " + TENANT_ID);
  161:  }
  162:  final X509Certificate[] certificateChain = new X509Certificate[fullCertificateChain.length - 1];
  163:  System.arraycopy(fullCertificateChain, 0, certificateChain, 0, fullCertificateChain.length - 1);
  164:  LOGGER.info("Obtained the validation key certificate for tenant {} with {} elements", TENANT_ID, certificateChain.length);
  165: 
  166:  // Create the initial payload to send.
  167:  final MixnetInitialPayload mixnetInitialPayload = new MixnetInitialPayload(encryptionParameters, encryptedVotes, electionPublicKey);
  168: 
  169:  // Hash the payload.
  170:  final byte[] payloadHash = hashService
  171:  .recursiveHash(mixnetInitialPayload.getEncryptionGroup(), HashableList.from(mixnetInitialPayload.getEncryptedVotes()),
  172:  mixnetInitialPayload.getElectionPublicKey());
  173: 
  174:  // Get the election information system key to sign the payload.
  175:  final PrivateKey signingKey = eiTenantSystemKeys.getSigningPrivateKey(TENANT_ID);
  176:  LOGGER.info("Obtained the signing key for tenant {}, signing the initial payload...", TENANT_ID);
  177: 
  178:  // Sign the payload hash.
  179:  byte[] signature;
  180:  try {
  181:  signature = asymmetricService.sign(signingKey, payloadHash);
  182:  } catch (GeneralCryptoLibException e) {
  183:  throw new CleansedBallotBoxServiceException("Failed to sign the initial payload.", e);
  184:  }
  185:  final CryptoPrimitivesPayloadSignature payloadSignature = new CryptoPrimitivesPayloadSignature(signature, certificateChain);
  186:  mixnetInitialPayload.setSignature(payloadSignature);
  187:  LOGGER.info("Initial payload signed successfully.");
  188: 
  189:  return mixnetInitialPayload;
  190:  }

The '_mixnetInitialPayload_ ' is sent through the Orchestrator to be consumed by the Control Components

File: e-voting-master/control-components/distributed-mixing-service/src/main/java/ch/post/it/evoting/controlcomponents/mixing/service/MixDecryptMessageConsumer.java
  
  
  122:  @RabbitListener(queues = "${partialMixingDecryptionRequestQueue}", autoStartup = "false")
  123:  public void onMessage(Message message) throws IOException, KeyManagementException, PayloadSignatureException {
  124:  byte[] messageBody = message.getBody();
  125:  byte[] mixnetStateBytes = new byte[messageBody.length - 1];
  126:  System.arraycopy(messageBody, 1, mixnetStateBytes, 0, messageBody.length - 1);
  127: 
  128:  MixnetState mixnetState = objectMapper.readValue(mixnetStateBytes, MixnetState.class);
  129: 
  130:  List<String> validationErrors = validateData(mixnetState);
  131:  if (!validationErrors.isEmpty()) {
  132:  sendWithError(mixnetState, "The following fields present validation errors: " + validationErrors);
  133:  return;
  134:  }

'_ValidateData_ ' extracts the payload and verifies its signature by using '_CryptolibPayloadSignatureService_ ' (line 216) in the same vulnerable way.

File: e-voting-master/control-components/distributed-mixing-service/src/main/java/ch/post/it/evoting/controlcomponents/mixing/service/MixDecryptMessageConsumer.java
  
  
  192:  private List<String> validateData(final MixnetState mixnetState) {
  193:  List<String> errors = new ArrayList<>();
  194: 
  195:  final MixnetPayload payload = mixnetState.getPayload();
  196: 
  197:  if (mixnetState.getNodeToVisit() != nodeID) {
  198:  String errorMessage = String.format("Node to visit is expected to be %d, but was %d", nodeID, mixnetState.getNodeToVisit());
  199:  errors.add(errorMessage);
  200:  LOGGER.error(errorMessage);
  201:  }
  202:  if (payload == null) {
  203:  String errorMessage = "No payload provided";
  204:  errors.add(errorMessage);
  205:  LOGGER.error(errorMessage);
  206:  } else if (containsNullFields(payload)) {
  207:  String errorMessage = "The payload contains null objects.";
  208:  errors.add(errorMessage);
  209:  LOGGER.error(errorMessage);
  210:  } else {
  211:  LOGGER.info("Verifying signature...");
  212:  final CryptoPrimitivesPayloadSignature signature = payload.getSignature();
  213:  final byte[] payloadHash = hashPayload(payload);
  214: 
  215:  try {
  216:  final boolean validSignature = signatureService.verify(signature, ccmjKeyRepository.getPlatformCACertificate(), payloadHash);
  217: 
  218:  if (!validSignature) {
  219:  String errorMessage = "Invalid signature.";
  220:  errors.add(errorMessage);
  221:  LOGGER.error(errorMessage);
  222:  } else {
  223:  LOGGER.info("The signature is valid.");
  224:  }
  225:  } catch (PayloadVerificationException e) {
  226:  String errorMessage = "Signature verification failed.";
  227:  errors.add(errorMessage);
  228:  LOGGER.error(errorMessage);
  229:  }
  230:  }

As a result, the Voting Server's 'Election Information' certificate chain can be abused to impersonate the 'SetupComponent' during the configuration phase.

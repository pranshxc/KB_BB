---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-17_finding-vulnerabilities-in-swiss-posts-e-voting-system-part-3.md
original_filename: 2024-01-17_finding-vulnerabilities-in-swiss-posts-e-voting-system-part-3.md
title: 'Finding vulnerabilities in Swiss Post''s e-voting system: part 3'
category: blogs
detected_topics:
- sso
- xss
- command-injection
- mfa
- otp
- automation-abuse
tags:
- imported
- blogs
- sso
- xss
- command-injection
- mfa
- otp
- automation-abuse
language: en
raw_sha256: 82c18184dba97a02cf4049ed7b5d3f6e8cdae83b33bac3601fc7ecd1dd8b812c
text_sha256: b99e5d5a8985ab00ab64ae627610507786cce55e759e51da952516ca250990ce
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Finding vulnerabilities in Swiss Post's e-voting system: part 3

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-17_finding-vulnerabilities-in-swiss-posts-e-voting-system-part-3.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `82c18184dba97a02cf4049ed7b5d3f6e8cdae83b33bac3601fc7ecd1dd8b812c`
- Text SHA256: `b99e5d5a8985ab00ab64ae627610507786cce55e759e51da952516ca250990ce`


## Content

---
title: "Finding vulnerabilities in Swiss Post's e-voting system: part 3"
url: "https://www.reversemode.com/2024/01/finding-vulnerabilities-in-swiss-posts.html"
final_url: "https://www.reversemode.com/2024/01/finding-vulnerabilities-in-swiss-posts.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["Swiss E-Voting"]
bugs: ["Cryptographic issues", "Security code review"]
publication_date: "2024-01-17"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 538
---

###  Finding vulnerabilities in Swiss Post's e-voting system: part 3 

[ January 17, 2024  ](https://www.reversemode.com/2024/01/finding-vulnerabilities-in-swiss-posts.html "permanent link")

  

Exactly two years ago I brought my blog back to life, after many years of hiatus, with "[Finding vulnerabilities in Swiss Post’s future e-voting system - Part 1](https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html)". That was the first of [a series of blog posts](https://www.reversemode.com/search/label/e-voting) covering that system. During these two years I've been periodically assessing the security posture of this e-voting solution, as part of their [Bug Bounty program](https://yeswehack.com/programs/swiss-post-evoting), which I personally recommend. 

Since the first time I reviewed their codebase a lot of things have changed, for good, as many areas have been dramatically improved. To be honest, from a security perspective the codebase back then was kind of a mess. 

When the first Swiss Post e-voting platform was published, back in 2019, it faced some public scrutiny, mostly from the academic community. As a result, some significant issues were [uncovered](https://www.zdnet.com/article/vulnerability-in-swiss-e-voting-system-could-have-led-to-vote-alterations/), so eventually Swiss Post decided to suspend the [deployment](https://www.evoting-blog.ch/en/pages/2019/swiss-post-temporarily-suspends-its-e-voting-system) of the system. That first version had been developed by [Scytl](https://en.wikipedia.org/wiki/Scytl), Spanish company specialized in electronic voting systems. After that fiasco, Swiss Post [changed](https://www.evoting-blog.ch/en/pages/2020/an-e-voting-system-for-switzerland-and-by-switzerland) their approach, thus acquiring the source code from Scytl and moving to a transparent, open-source focused, in-house development process, which is where they are at now.

I've already [expressed](https://www.reversemode.com/2023/10/some-thoughts-on-e-voting.html) my thoughts about e-voting, which is a thorny issue for many in the security community. Obviously, bearing in mind what is at stake, all kind of concerns are expected, understandable, and actually, needed. That said, I think that it is also our, we security people, responsibility to properly raise legitimate concerns, while keeping a technically accurate position. For me, this means properly understanding the scope, extent and context for both the e-voting solution and the threats it may face.

This can be achieved by carefully studying the '[Protocol of the Swiss Post Voting System](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/raw/master/Protocol/Swiss_Post_Voting_Protocol_Computational_proof.pdf)' document, which includes their threat model. 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgQWGmXnoYa1KWiM8WKng_QvdnchDvnUMfEaKG-4UNeSyEvxCZvi43Wva9R9JEXDpgthtT5uUl-wjuiY4ktHlvuF8nSR3e3tVnWB3a93p24tbc7SjuwYdp9WykrBPf5KzS6omeGek4pCzJSW5VuQhTLoh-uJasvrdk3VogZeuwtPYWC1cSYNChF9I4z_2JQ=w640-h276)](https://blogger.googleusercontent.com/img/a/AVvXsEgQWGmXnoYa1KWiM8WKng_QvdnchDvnUMfEaKG-4UNeSyEvxCZvi43Wva9R9JEXDpgthtT5uUl-wjuiY4ktHlvuF8nSR3e3tVnWB3a93p24tbc7SjuwYdp9WykrBPf5KzS6omeGek4pCzJSW5VuQhTLoh-uJasvrdk3VogZeuwtPYWC1cSYNChF9I4z_2JQ)

  
The trust assumptions are a key concept to understanding Swiss Post's e-voting system.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgjmmhzqsg_hhKp_J4ccUp9lEM4sqlAuqjqsajfwkDAKscXNhZiFJT8C3yATAB_JU4M4aVbjWpczchMhEK_kZ8PubsssqqVGT-nM5a10loMoG8ovoDKOju83-cZSTM1B68CBI9JxFBvjdXtNox6avEtKnqLD_Ab9sQLypWDZaWQIK4dPzTW4itfAM63az6c=w640-h294)](https://blogger.googleusercontent.com/img/a/AVvXsEgjmmhzqsg_hhKp_J4ccUp9lEM4sqlAuqjqsajfwkDAKscXNhZiFJT8C3yATAB_JU4M4aVbjWpczchMhEK_kZ8PubsssqqVGT-nM5a10loMoG8ovoDKOju83-cZSTM1B68CBI9JxFBvjdXtNox6avEtKnqLD_Ab9sQLypWDZaWQIK4dPzTW4itfAM63az6c)

There are three things we should note about this model:

1\. The system is designed to be resilient in a pretty extreme environment, where a significant part of their assets and participants are assumed to be hostile and/or compromised.

2\. This is possible because of the specific cryptography that has been implemented. The availability, integrity and confidentiality of the system is relying on the different cryptographic schemes that sustain the core functionality.

3\. Swiss Post e-voting system is not an EDR, it's not an anti-virus, it's not a security solution for the user device.

Before claiming e-voting is useless and insecure in general terms, I would first review these three points and try to confront any alleged vulnerability or attack scenario against them.

However, we should also note that in the real-world, malicious actors are not going to refrain from attacking a component because it has been considered as 'trustworthy' in a threat model. There are also inherent issues in terms of availability, due to the fact that untrustworthy components can simply refuse to cooperate.

### The human factor

Social engineering will always be a menace for any computer-based system that requires a human interaction and a human-based decision making process. This basically means that any e-voting solution requires an additional effort to educate the voter on how to use the system and what are the expected interactions, similar to what most banking applications do nowadays. However, there are also some additional limitations for e-voting solutions with regards to the range of elements available for out-of-band communications. While we happily accept a 2FA request in our mobile phone for confirming a transfer of funds when using a banking app, any similar functionality would be totally barred for e-voting solutions.

We should differentiate between malware-based social engineering attacks and vulnerabilities. E-voting solutions can only aspire to mitigate, up to a certain level, social engineering scenarios posed by compromised user devices (voting client) trying to lure the victim into behaving in a specific way. E-voting solutions are not EDRs, once the user device has been compromised there is an endless string of malware-based social engineering attacks that can be launched. Under my point of view, these do not represent vulnerabilities, unless they can break (or weaken) individual verifiability in a deterministic way, without requiring social engineering. 

### Vulnerabilities

Now, let's move to the technical part. This time I'm covering three different vulnerabilities that will be [addressed](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/58) in the next version of the Swiss Post e-voting system (1.4). A brief introduction:

_#YWH-PGM2323-192 - Incomplete verifiability of the Election Encryption Parameters_

One month after reporting this issue, Filippo Valsorda, a well-known cryptography engineer unveiled an interesting initiative "[Announcing the $12k nist elliptic curves seeds bounty](https://words.filippo.io/dispatches/seeds-bounty/)". 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjfy5kFiHwFiBXHsz8HsrE6fnJV95OC3nyY0508zS0YLM8A-So5hs-HH1Ef0wntvKJxVOpdYSyFwhZLh9lhSx_3hrb8QtcMaa6-DaBhekgwi_ylBE10Ddxfqdz0GMk9NdktOdlilwQ675YKvPfaGufVfd0UfaljRC-OHkpBIWzJJR4EHxS8xV28MwQ0k6qw=w640-h206)](https://blogger.googleusercontent.com/img/a/AVvXsEjfy5kFiHwFiBXHsz8HsrE6fnJV95OC3nyY0508zS0YLM8A-So5hs-HH1Ef0wntvKJxVOpdYSyFwhZLh9lhSx_3hrb8QtcMaa6-DaBhekgwi_ylBE10Ddxfqdz0GMk9NdktOdlilwQ675YKvPfaGufVfd0UfaljRC-OHkpBIWzJJR4EHxS8xV28MwQ0k6qw)

  

The Swiss Post e-voting system is not alien to this question. So basically, the underlying idea in both cases is whether we should trust the seeds used to generate the public parameters.

  

Although initially, the system specification stated that the seed was verifiably generated, I discovered that the seed was never checked neither by the verifier nor in any other component. As a result, assuming a malicious actor is able to control the seed, I elaborate the feasibility of the different scenarios that could be derived from this issue.

_#YWH-PGM2323-195 - [Verifier] Potential Vote Corruption due to inconsistent handling of truncated Write-Ins_

The way the verifier handles write-ins differs from the tally control component. This situation could have ended up in the ability of a malicious voter to invalidate an entire ballot box. Fortunately, there was something that prevented this worst-case scenario.

_#YWH-PGM2323-196 - Improper validation of Write-Ins_

Write-Ins have been a 'polemic' part of the e-voting system. I spent some time understanding the implementation behind this logic, how malicious voters could forge malformed write-ins and the implications of such a scenario.

  

1\.  _#YWH-PGM2323-192-__Incomplete verifiability of the Election Encryption Parameters_

### Description

The '[Crypto Primitives Specification](https://gitlab.com/swisspost-evoting/crypto-primitives/crypto-primitives/-/blob/master/Crypto-Primitives-Specification.pdf?ref_type=heads)' document states the following:

  

__

_[![](https://blogger.googleusercontent.com/img/a/AVvXsEhk3dzxBeYXBtpWtgNR6gTdU1taxQJemezHQprenqUJwZicw8HroA4b42_2vPksPh_Mx3lXSomibmEb6wY0i2HV7K4-r5raKlPQXdHEVLi-_OCwVMzDPBAyoAxSzWWFs7wr-gRvKJHWbikJIz8KhJgyPW-cWEsCEAAbrhXUmMqWq918TzPy54n3tx1kQbHu=w640-h276)](https://blogger.googleusercontent.com/img/a/AVvXsEhk3dzxBeYXBtpWtgNR6gTdU1taxQJemezHQprenqUJwZicw8HroA4b42_2vPksPh_Mx3lXSomibmEb6wY0i2HV7K4-r5raKlPQXdHEVLi-_OCwVMzDPBAyoAxSzWWFs7wr-gRvKJHWbikJIz8KhJgyPW-cWEsCEAAbrhXUmMqWq918TzPy54n3tx1kQbHu)_

_  
_

However, the analysis of the system reveals that the 'seed' is never checked to verify that it actually matches the election name belonging to the election event context in which the Encryption Parameters are being used. The verifier also misses this check.

### Technical Details

The administrator, under the four-eye principle (Electoral Board), provides the 'seed.txt' file to the 'config-cryptographic-parameters-tool'. According to the system specification none of these individuals are considered trustworthy, although the Electoral Board is assumed to be trustworthy under regular conditions.

The 'Election Name' is defined by the eCH standard in its eCH-0155 document. Internally, the swiss-post evoting configuration uses the 'contestIdentification' to represent this field. 'contestIdentification' must comply with a specific pattern, as we can see below

File: e-voting-libraries-master/e-voting-libraries-xml/src/main/resources/xsd/evoting-config-5-0.xsd
  
  
  12:  <xs:simpleType name="identifierType">
  13:  <xs:restriction base="xs:token">
  14:  <xs:maxLength value="50"/>
  15:  <xs:minLength value="1"/>
  16:  <xs:pattern value="[\w\-_]{1,50}"/>
  17:  </xs:restriction>
  18:  </xs:simpleType>

However, the 'config-cryptographic-parameters-tool' does not implement this logic to filter the contents imported from the 'seed.txt' file.

File: tools/config-cryptographic-parameters-tool/src/main/java/ch/post/it/evoting/config/commands/encryptionparametersandprimes/EncryptionParametersAndPrimesGenerator.java
  
  
  56:  public EncryptionParametersPayload generate(final Path seedPath, final Path keystoreLocationConfigPath,
  57:  final Path keystorePasswordLocationConfigPath) {
  58:  checkNotNull(seedPath);
  59:  checkNotNull(keystoreLocationConfigPath);
  60:  checkNotNull(keystorePasswordLocationConfigPath);
  61: 
  62:  final String seed = readSeedFromFile(seedPath);
  
  ...
  
  81:  private String readSeedFromFile(final Path seedPath) {
  82:  final List<String> lines;
  83:  try {
  84:  lines = Files.readAllLines(seedPath);
  85:  } catch (IOException e) {
  86:  throw new UncheckedIOException(String.format("Failed to read seed located at: %s", seedPath), e);
  87:  }
  88: 
  89:  final String seed = lines.stream().reduce("", (s1, s2) -> s1 + s2.trim());
  90:  if (seed.isEmpty()) {
  91:  throw new IllegalArgumentException("The seed must not be an empty string.");
  92:  }
  93: 
  94:  return seed;
  95:  }

There are two actions that change the original input: At line 84 '_readAllLines_ ' is used, which will strip 'newline' control characters from the input, as well as s2.trim() at line 89, removing 'space' characters.

This logic implies that different 'seed.txt' files (see example below) will provide the same 'seed', which may have security implications.

File: Seed.txt

"ElectionNameLegit"

File: BadSeed.txt

"E\nlecti\n on N\n ame\nLegit"

Also, under the four-eye principle, the administrator may trick the Electoral Board members into thinking that the 'seed.txt' file corresponds to the actual election name, by using a combination of 'newline' and 'space' characters carefully inserted after the original Election Name, thus hiding additional content in a common text editor (assuming the Electoral Board may request the administrator to open 'seed.txt').

Once the 'encryptionParametersPayload.json' file has been generated and imported during the pre-configuration phase, the 'seed' value will never be checked against the configured Election Name (represented by different fields such _ContestIdentification_ or _ElectionName_ Alias)

File: e-voting-libraries-master/e-voting-libraries-domain/src/main/java/ch/post/it/evoting/evotinglibraries/domain/mixnet/EncryptionParametersPayload.java
  
  
  40: @JsonDeserialize(using = EncryptionParametersPayloadDeserializer.class)
  41: @JsonPropertyOrder({ "encryptionGroup", "seed", "smallPrimes", "signature" })
  42: public class EncryptionParametersPayload implements SignedPayload {
  43:  @JsonProperty
  44:  private final GqGroup encryptionGroup;
  45:  @JsonProperty
  46:  private final String seed;
  47:  @JsonProperty
  48:  private final GroupVector<PrimeGqElement, GqGroup> smallPrimes;
  49:  @JsonProperty
  50:  private CryptoPrimitivesSignature signature;

The Verifier also misses any cross-check between the '_seed_ ' and the '_ContestIdentification_ ':

1.- The 'encryption Group' consistency check leaves the '_seed_ ' out of the logic

File: verifier-master/verifier-backend/src/main/java/ch/post/it/evoting/verifier/backend/verifications/setup/consistency/VerifyEncryptionGroupConsistency.java
  
  
  86:  private boolean validateEncryptionParameters(final Path inputDirectoryPath, final EncryptionGroupParametersDataExtractor.DataExtraction encryptionGroupParametersDataExtraction) {
  87:  return encryptionGroupParametersDataExtraction.equals(extractionService.getFromEncryptionParameters(inputDirectoryPath));
  88:  }

2.- The 'evidence' check for the Encryption Parameters just verifies whether the received seed generates the public parameters, but fails to validate whether that 'seed' actually corresponds to the election name.

File: verifier-master/verifier-backend/src/main/java/ch/post/it/evoting/verifier/backend/verifications/setup/evidence/VerifyEncryptionParameters.java
  
  
  69:  @Override
  70:  public VerificationResult verify(final Path inputDirectoryPath) {
  71:  // Deserialize file.
  72:  final EncryptionParametersPayload encryptionParametersPayload = extractionService.getEncryptionParametersPayload(inputDirectoryPath);
  73:  final GqGroup encryptionGroup = encryptionParametersPayload.getEncryptionGroup();
  74: 
  75:  // Extract parameters.
  76:  final BigInteger p_hat = encryptionGroup.getP();
  77:  final BigInteger q_hat = encryptionGroup.getQ();
  78:  final GqElement g_hat = encryptionGroup.getGenerator();
  79:  final String seed = encryptionParametersPayload.getSeed();
  80: 
  81:  final VerificationResult verificationResult;
  82:  if (!verifyEncryptionParametersAlgorithm.verifyEncryptionParameters(p_hat, q_hat, g_hat, seed)) {
  83:  verificationResult = VerificationResult.failure(getVerificationDefinition(),
  84:  TranslationHelper.getFromResourceBundle(SetupVerificationSuite.RESOURCE_BUNDLE_NAME, "setup.verification500.nok.message"));
  85:  } else {
  86:  verificationResult = VerificationResult.success(getVerificationDefinition());
  87:  LOGGER.info("Successfully verified the encryption parameters p, q, g. [p: {}, q: {}, g: {}]", p_hat, q_hat, g_hat);
  88:  }
  89: 
  90:  return verificationResult;
  91:  }
  92: 

### Risk 

The intended verifiability for the encryption parameters described in the system specification is not actually enforced. As a result, the following statement, presented in the the system specification, is not completely backed by the implementation.

_"We pick all the group parameters verifiably to demonstrate that they are devoid of hidden properties or back doors_."

It should be noted that this doesn't imply that the ability to generate encryption parameters with arbitrary 'seeds' may result in a practical attack against the Swiss Post system. However, these missing checks would potentially enable that possibility. Now let's analyze the feasibility of the different scenarios.

### 1\. Primality testing

The ability to inject composite numbers instead of prime ones into the public parameters would be devastating for the integrity of the whole system. A malicious seed switches the paradigm of the primality testing from 'random' to adversarial. This really great research ["Prime and Prejudice: Primality Testing Under Adversarial Conditions"](https://eprint.iacr.org/2018/749) provides real-world examples of well-known codebases falling for this attack. 

Fortunately for Swiss Post, they implemented a robust primality testing logic. So, even with a malicious seed it is not possible to end up with composite numbers. It is documented in the '[Crypto Primitives specification](https://gitlab.com/swisspost-evoting/crypto-primitives/crypto-primitives/-/blob/master/Crypto-Primitives-Specification.pdf?ref_type=heads)' 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgm4pO1CPg7RYPUh1QcK93VAKfGLHLA2XKf71COGi457RdHcK5NB4IAjbKEiDjCVH_I9KBGrr3zfmWO4GAMULicspjB-FhXlr8TcXUUpzkPxdaVkv6QJKdGCSBWMG19eMW0vK9riFegJIuGM8aKAzx55Rs7AET0Uo_oWNACHXqsT84KSiwbv_TQrIi6Odbt=w640-h328)](https://blogger.googleusercontent.com/img/a/AVvXsEgm4pO1CPg7RYPUh1QcK93VAKfGLHLA2XKf71COGi457RdHcK5NB4IAjbKEiDjCVH_I9KBGrr3zfmWO4GAMULicspjB-FhXlr8TcXUUpzkPxdaVkv6QJKdGCSBWMG19eMW0vK9riFegJIuGM8aKAzx55Rs7AET0Uo_oWNACHXqsT84KSiwbv_TQrIi6Odbt)

  
If you are curious how this was implemented, here you can see the code.

File: crypto-primitives-master/src/main/java/ch/post/it/evoting/cryptoprimitives/internal/elgamal/EncryptionParameters.java
  
  
  072:  @SuppressWarnings("java:S117")
  073:  public GqGroup getEncryptionParameters(final String seed, final List<Integer> smallPrimes) {
  074:  checkNotNull(seed);
  075:  checkNotNull(smallPrimes);
  076:  smallPrimes.forEach(prime -> checkArgument(PrimesInternal.isSmallPrime(prime), "The given number is not a prime. [Number: %s]", prime));
  077: 
  078:  final int certaintyLevel = lambda.getSecurityLevelBits();
  079:  final ArrayList<BigInteger> sp = smallPrimes.stream().map(BigInteger::valueOf)
  080:  .collect(Collectors.toCollection(ArrayList::new));
  081:  final int l = smallPrimes.size();
  082:  final int pBitLength = lambda.getPBitLength();
  083: 
  084:  final byte[] q_b_hat = shake128(stringToByteArray(seed), pBitLength / 8);
  085:  final byte[] q_b = Bytes.concat(new byte[] { 0x02 }, q_b_hat);
  086:  final BigInteger q_prime = byteArrayToInteger(q_b).shiftRight(3);
  087:  BigInteger q = q_prime.subtract(q_prime.mod(SIX)).add(FIVE);
  088:  final ArrayList<BigInteger> r = new ArrayList<>(l);
  089:  for (int i = 0; i < l; i++) {
  090:  r.add(i, q.mod(sp.get(i)));
  091:  }
  092:  final BigInteger jump = SIX;
  093:  BigInteger delta = ZERO;
  094:  do {
  095:  delta = delta.add(jump);
  096:  int i = 0;
  097:  while (i < l) {
  098:  if ((r.get(i).add(delta).mod(sp.get(i)).equals(ZERO)) || (TWO.multiply(r.get(i).add(delta)).add(ONE).mod(sp.get(i)).equals(ZERO))) {
  099:  delta = delta.add(jump);
  100:  i = 0;
  101:  } else {
  102:  i = i + 1;
  103:  }
  104:  }
  105:  } while (!(q.add(delta).isProbablePrime(certaintyLevel)) || !(TWO.multiply(q.add(delta)).add(ONE).isProbablePrime(certaintyLevel)));
  106:  q = q.add(delta);
  107:  final BigInteger p = TWO.multiply(q).add(ONE);
  108: 
  109:  final BigInteger g;
  110:  if (isGroupMember(TWO, p)) {
  111:  g = TWO;
  112:  } else {
  113:  g = THREE;
  114:  }
  115: 
  116:  if (!millerRabin(q, 64) || !millerRabin(p, 64)) {
  117:  throw new IllegalStateException("p and q must both pass the Miller-Rabin test");
  118:  }
  119: 
  120:  return new GqGroup(p, q, g);
  121:  }

### 2\. Trapdoors

Now things get more interesting. In general terms, the idea is to build a [trapdoor](https://arxiv.org/abs/1610.02874) in the public parameters so malicious actors can turn a problem known to be hard, such as breaking the Discrete Logarithm Problem (e.g., ElGamal), into a 'less hard' situation, ideally allowing to break it.

There are different algorithms ([Pohlig-Hellman](https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm), [Shanks'](https://en.wikipedia.org/wiki/Baby-step_giant-step), [Pollard's rho](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms)...) that have been developed to solve DLP, under very specific circumstances, with a complexity that makes this problem tractable. However, even with a malicious seed, this is a dead-end due to the way the public parameters are generated. This paragraph, in addition to the previous code, provides the reason. Let's see why:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhbzwhss9hZ3nAzPz-kk7edzakocCHfgWHznNlP3qUgKNESaUvQllnYPX7L1JmFqVXPQXBYainHm-KTMM4Wk_BQJ2Ovp3Tist4Ye92mpC9528OGSXPcphr-UwsEea8qgJUgZJFJ0jYg9qUrl8HRM3GHyz6DLqbrHx1_ZqF5k0euEn-8QBVSxdAMQWMvLcjK=w640-h118)](https://blogger.googleusercontent.com/img/a/AVvXsEhbzwhss9hZ3nAzPz-kk7edzakocCHfgWHznNlP3qUgKNESaUvQllnYPX7L1JmFqVXPQXBYainHm-KTMM4Wk_BQJ2Ovp3Tist4Ye92mpC9528OGSXPcphr-UwsEea8qgJUgZJFJ0jYg9qUrl8HRM3GHyz6DLqbrHx1_ZqF5k0euEn-8QBVSxdAMQWMvLcjK)

  

In the Swiss Post e-voting solution, the ElGamal encryption scheme is instantiated over a cyclic group (𝔾q) with a prime order. In addition to this, _q_ is also a [safe prime](https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes) as we can see in the following code. 
  
  
  107:  final BigInteger p = TWO.multiply(q).add(ONE);
  
  
  116:  if (!millerRabin(q, 64) || !millerRabin(p, 64)) {
  117:  throw new IllegalStateException("p and q must both pass the Miller-Rabin test");
  118:  }

  

Also, Swiss Post enforces the 'extended' bit length of the public parameters.

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg2P-RyidPrmkCu90-NqqP0n7EdhmD8sz4WjC7Q1qywMOym7TbSXn_5lnDcj_vQ2A_24iPxYeIGW4uQIdMgwwGvMIX-ygieQn5IQH0LzbMGT5Wg6UTNaslexjZ0x_D-_iQHBPix8WIO3QKqCOY1HJ_2a9SqLTRLnvPE9Ra9VqxeVdL_8QsrbIW9GvOeFptU=w640-h372)](https://blogger.googleusercontent.com/img/a/AVvXsEg2P-RyidPrmkCu90-NqqP0n7EdhmD8sz4WjC7Q1qywMOym7TbSXn_5lnDcj_vQ2A_24iPxYeIGW4uQIdMgwwGvMIX-ygieQn5IQH0LzbMGT5Wg6UTNaslexjZ0x_D-_iQHBPix8WIO3QKqCOY1HJ_2a9SqLTRLnvPE9Ra9VqxeVdL_8QsrbIW9GvOeFptU)

  
These properties effectively leave most of the DLP-solving algorithms out of play.

The only potential available option left would be an approach based on [Number Field Sieve](https://en.wikipedia.org/wiki/Function_field_sieve) algorithms, an extremely complex area. I'm neither a mathematician nor a cryptographer so I'm far from being in a position to provide a sound statement about the feasibility of NFS-based trapdoors. From what I've been studying, it doesn't seem really plausible. We should bear in mind that the seed goes first through a SHAKE128 hash algorithm, which means the malicious actors would need a pre-image attack or significant brute-forcing capabilities (and a little bit of luck I guess).
  
  
  084:  final byte[] q_b_hat = shake128(stringToByteArray(seed), pBitLength / 8);

There is still a specific scenario for the Swiss Post e-voting solution, also for similar e-voting solutions, due to the way voting options are encoded in the ElGamal encryption scheme. 

[Pierre Gaudry](https://members.loria.fr/PGaudry/), from LORIA, elaborates this scenario on his paper "[About the Subgroup Generated By Small Primes](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/blob/master/Protocol/sgsp.pdf)" 

Swiss Posts also asked Pierre Gaudry to assess the feasibility of trapdoors due to this vulnerability. 

"_To summarize, even if an attacker can force a seed, whatever its length, whatever its structure, they won't be able to gain any advantage in breaking the discrete logarithm, nor in breaking SGSP in the corresponding group._ "

  

_2\. #YWH-PGM2323-195 - [Verifier] Potential Vote Corruption due to inconsistent handling of truncated Write-Ins_

### Description

The logic implemented in the Verifier to verify the Write-Ins does not check the maximum allowed length of the Write-Ins, so the Write-Ins decoded in the verifier are not truncated. On the other hand, when the votes are persisted during the Tally phase, the Write-Ins decoded by the Tally Control Component are truncated if they exceed the allowed length (500).

The Verifier then compares the truncated Write-Ins, obtained from these Tally CC persisted files, with the non-truncated Write-Ins directly decoded by the verifier from the persisted votes, which can potentially result in a failed verification due to a 'false positive'.

However, according to the current bit length of the current ElGamal public parameters, it's not possible to encode Write-Ins higher than 430 characters, so this issue does not seem exploitable. This may change in the future.

A group of malicious voting clients (voters) may leverage this inconsistent logic to trick the verifier into detecting an (inexistent) vote corruption.

### Technical Details

The '_ProcessPlaintexts_ ' algorithm in the Tally CC will persist the decoded Write-Ins, truncating them when the lengths are higher than MAXIMUM_WRITE_IN_OPTION_LENGTH (500)

File: e-voting-master/secure-data-manager/backend/src/main/java/ch/post/it/evoting/securedatamanager/sdmtally/tally/mixoffline/ProcessPlaintextsService.java
  
  
  122:  private TallyComponentVotesPayload createTallyComponentVotesPayload(final String electionEventId, final String ballotId, final String ballotBoxId,
  123:  final GqGroup encryptionGroup, final GroupVector<GroupVector<PrimeGqElement, GqGroup>, GqGroup> encodedSelectedVotingOptions,
  124:  final List<List<String>> actualSelectedVotingOptions, final List<List<String>> decodedWriteInVotes) {
  125: 
  126:  final List<List<String>> sanitizedDecodedWriteInVotes = decodedWriteInVotes.stream()
  127:  .map(decodedWriteInVote -> decodedWriteInVote.stream()
  128:  .map(decodedWriteIn -> {
  129:  if (decodedWriteIn.length() > MAXIMUM_WRITE_IN_OPTION_LENGTH) {
  130:  LOGGER.warn("Write-in voting option with length exceeding maximum. "
  131:  + "It has been truncated to maximum supported size. [maximum: {}, write-in's length: {}]",
  132:  MAXIMUM_WRITE_IN_OPTION_LENGTH, decodedWriteIn.length());
  133:  return decodedWriteIn.substring(0, MAXIMUM_WRITE_IN_OPTION_LENGTH);
  134:  }
  135:  return decodedWriteIn;
  136:  })
  137:  .toList())
  138:  .toList();

Then, the Verifier performs its own decoding of the Write-Ins directly from the persisted votes, but without truncating them, and then compares the results with 'L_writeIns' (at line 138), that contains the persisted, and potentially truncated, Write-Ins previously decoded by the Tally CC.

File: e-voting-master/verifier-master/verifier-backend/src/main/java/ch/post/it/evoting/verifier/backend/verifications/tally/evidence/VerifyProcessPlaintextsAlgorithm.java
  
  
  
  106:  // Equivalent stream to the for-loop.
  107:  final List<FactorizedDecodedVotes> factorizedDecodedVotes = m.stream()
  108:  .filter(m_i -> !m_i.equals(one_vector))
  109:  .map(m_i -> {
  110:  final GqElement phi_i_0 = m_i.get(0);
  111:  final GroupVector<PrimeGqElement, GqGroup> p_k_hat_prime = factorizeAlgorithm.factorize(phi_i_0,
  112:  getEncodedVotingOptionsAlgorithm.getEncodedVotingOptions(pTable, List.of()), psi);
  113: 
  114:  final List<String> v_k_hat_prime = getActualVotingOptionsAlgorithm.getActualVotingOptions(pTable, p_k_hat_prime);
  115: 
  116:  final GroupVector<GqElement, GqGroup> w_k_prime = m_i.getElements().subVector(1, l);
  117: 
  118:  final List<String> s_k_hat_prime = decodeWriteInsAlgorithm.decodeWriteIns(new DecodeWriteInsAlgorithmInput.Builder()
  119:  .setWriteInVotingOptions(p_w_tilde)
  120:  .setSelectedEncodedVotingOptions(p_k_hat_prime)
  121:  .setEncodedWriteIns(w_k_prime)
  122:  .build());
  123: 
  124:  return new FactorizedDecodedVotes(p_k_hat_prime, v_k_hat_prime, s_k_hat_prime);
  125:  })
  126:  .toList();
  127: 
  128:  final GroupVector<GroupVector<PrimeGqElement, GqGroup>, GqGroup> p_hat_prime = factorizedDecodedVotes.stream()
  129:  .map(FactorizedDecodedVotes::factorized)
  130:  .collect(GroupVector.toGroupVector());
  131:  final List<List<String>> v_hat_prime = factorizedDecodedVotes.stream()
  132:  .map(FactorizedDecodedVotes::decoded)
  133:  .toList();
  134:  final List<List<String>> s_hat_prime = factorizedDecodedVotes.stream()
  135:  .map(FactorizedDecodedVotes::decodedWriteInVotes)
  136:  .toList();
  137: 
  138:  return p_hat_prime.equals(L_votes) && v_hat_prime.equals(L_decodedVotes) && s_hat_prime.equals(L_writeIns);

Assuming an encoded Write-In longer than 500 characters (the size of WRITE_IN_ALPHABET is 142), this logic would result in a failed verification. However, this doesn't seem possible, as a|s| would need to be higher than the current _q_.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiJDPTeU86_79hDaZv5tLvPEEF_QiXZb_cYkETFu6Be5U3TtwZfnkaZj6YHoFukwqSfalqtpxirc2M7Q9h_cVxe1tM7Up3wXOCkpKM2zJb86tJq8m5x9-wQSKssBvVlu0uzJ50qllAtW3r7ruMDeumvN1Y38MMBNG8pR8DxZCngfdpvLDOrI_7egQrpuBr9=w640-h166)](https://blogger.googleusercontent.com/img/a/AVvXsEiJDPTeU86_79hDaZv5tLvPEEF_QiXZb_cYkETFu6Be5U3TtwZfnkaZj6YHoFukwqSfalqtpxirc2M7Q9h_cVxe1tM7Up3wXOCkpKM2zJb86tJq8m5x9-wQSKssBvVlu0uzJ50qllAtW3r7ruMDeumvN1Y38MMBNG8pR8DxZCngfdpvLDOrI_7egQrpuBr9)

  
  

### Risk

If a malicious voting client can, somehow, encode a Write-In longer than 500 characters, the verifier will fail to validate the ballot box where the vote has been deposited. A coordinated attack can generate multiple vote corruption 'alerts' received by the auditors. This scenario could affect the ability to verify an election in a timely manner, thus impacting the overall election process, potentially undermining the public trust.

  

3._#YWH-PGM2323-196 - Improper validation of Write-Ins_

### Description

The implementation (and specification) of the logic that handles the Write-Ins, on the server side (Tally CC), does not properly validate their values.

The documentation does not seem to fully describe the extent of the Write-Ins logic but the specification mentions the following:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhsnpq3prsVUvov-LaCnQhOxm7lUvSe-EpY84DVRF_BDfBN5EEHuV4hvQcLmVntqNg2sn5SfDi-_B8OF4AFCJFQ4uKymk4SKHRptO6bbbSeORtCzBXS3mE_lgKRmv2LHGA5MM-kIDT7W1StXUzMPAQ7JvnotnUixWR3IMHftUvqPxfyKZBEGU3l9iuzwJzg=w640-h96)](https://blogger.googleusercontent.com/img/a/AVvXsEhsnpq3prsVUvov-LaCnQhOxm7lUvSe-EpY84DVRF_BDfBN5EEHuV4hvQcLmVntqNg2sn5SfDi-_B8OF4AFCJFQ4uKymk4SKHRptO6bbbSeORtCzBXS3mE_lgKRmv2LHGA5MM-kIDT7W1StXUzMPAQ7JvnotnUixWR3IMHftUvqPxfyKZBEGU3l9iuzwJzg)

The analysis reveals that this validation is just enforced on the client-side (Voting-portal/Voting-Client). In addition to this, the Write-In decoding assumes a valid input, when in fact it can be controlled by a malicious voter.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrGYFbt1Qr4qglt7EGsLVJwa2os4hOZlAxgLQ_r1TZtiUTfrswzCicWFTx_OXpi1Xz_ZX78-svcVdeMbWRzK8-IrLchY9uIVnYcccYR6on7d4aspGVT0lX5nzUo365b6ReVCC6wX6MSsZoN9rMJT8K2dTGnwCwUmTZ4rIyTG7ldkHvYIMFfzY-UB-Fw17G=w640-h174)](https://blogger.googleusercontent.com/img/a/AVvXsEjrGYFbt1Qr4qglt7EGsLVJwa2os4hOZlAxgLQ_r1TZtiUTfrswzCicWFTx_OXpi1Xz_ZX78-svcVdeMbWRzK8-IrLchY9uIVnYcccYR6on7d4aspGVT0lX5nzUo365b6ReVCC6wX6MSsZoN9rMJT8K2dTGnwCwUmTZ4rIyTG7ldkHvYIMFfzY-UB-Fw17G)

These issues allow a malicious voter to forge Write-Ins that do no comply with the specification.

### Technical details

The client-side validation that prevents a voter from entering '#' characters (in addition to a specific format) in the write-in fields is implemented, client-side, by the Voting Client.

At line 53 we can see how the first character in the Write-in alphabet ('#') is removed from the regexp that controls the accepted characters.

File: voter-portal/libs/candidate/src/lib/candidate-write-in/candidate-write-in.component.ts
  
  
  33:  private get writeInValidator(): ValidatorFn {
  34:  return (control: AbstractControl): ValidationErrors | null => {
  35:  // Control value length is checked to prevent regex DoS attack
  36:  const writeInFormat = /^.+\s.+$/;
  37:  if (!control.value || control.value.length > this.writeInMaxLength || !writeInFormat.test(control.value)) {
  38:  return {incorrectFormat: true};
  39:  }
  40: 
  41:  if (this.writeInAlphabet && !this.writeInAlphabet.test(control.value)) {
  42:  return {incorrectCharacters: true};
  43:  }
  44: 
  45:  return null;
  46:  }
  47:  }
  48: 
  49:  ngOnInit() {
  50:  this.alphabetSubscription = this.store.pipe(
  51:  getDefinedWriteInAlphabet
  52:  ).subscribe(alphabet => {
  53:  this.writeInAlphabet = new RegExp(`^[${alphabet.substring(1)}]+$`);
  54:  });
  55: 
  56:  this.initialWriteIn = this.writeInControl.value;
  57: 
  58:  this.writeInControl.setValidators([this.writeInValidator, Validators.maxLength(this.writeInMaxLength)]);
  59:  setTimeout(() => {
  60:  this.writeInControl.updateValueAndValidity();
  61:  this.writeInInput?.nativeElement.focus();
  62:  });
  63:  }
  64: 

The final representation of the Write-In value entered by the voter is built according to the format "primeId +'#'+ write-in", as we can see at line 125.

File: voter-portal/libs/backend/src/lib/representation-builder/representation-builder.service.ts
  
  
  118:  contestUserData.candidates.forEach(({candidateId, writeIn}, i) => {
  119:  let candidate = contest.getCandidate(candidateId);
  120:  if (!candidate) {
  121:  candidate = contest.blankCandidates ? contest.blankCandidates[i] : null;
  122:  } else if (candidate.isWriteIn) {
  123:  candidate = contest.writeInCandidates ? contest.writeInCandidates[i] : null;
  124:  writeIns.push(
  125:  `${candidate?.prime}${this.writeInsSeparator}${writeIn}`
  126:  );
  127:  }

This Write-In value is then encoded during the '_CreateVote_ ' logic by the '_writeInToQuadraticResidue_ ' algorithm, which first maps the write-in to ℤq (writeInToInteger, line 45) and finally to 𝔾q by squaring it (line 47)

File: voting-client-js/src/write-ins/write-in-to-quadratic-residue-algorithm.js
  
  
  27:  function writeInToQuadraticResidue(
  28:  context,
  29:  characterString
  30:  ) {
  31:  checkNotNull(context);
  32:  const encryptionGroup = checkNotNull(context.encryptionGroup);
  33:  const s = checkNotNull(characterString);
  34: 
  35:  const a = ImmutableBigInteger.fromNumber(WRITE_IN_ALPHABET.length);
  36:  const s_length = ImmutableBigInteger.fromNumber(s.length);
  37: 
  38:  // Require.
  39:  checkArgument(writeInToIntegerAlgorithm.checkExpLength(a, s_length, encryptionGroup),
  40:  'The exponential form of a to s_length must be smaller than q.');
  41:  checkArgument(s_length > 0, 'The character string length must be greater than 0.');
  42:  checkArgument(s.charAt(0) !== WRITE_IN_ALPHABET[0], 'The character string must not start with rank 0 character.');
  43: 
  44:  // Operation.
  45:  const x = writeInToIntegerAlgorithm.writeInToInteger({encryptionGroup: encryptionGroup}, s);
  46: 
  47:  return GqElement.fromSquareRoot(x.value, encryptionGroup);
  48:  }
  49: 
  50:  return {
  51:  writeInToQuadraticResidue: writeInToQuadraticResidue
  52:  }
  53: })();

Then, during the decoding at the Tally Control Component, we can see how the algorithm assumes the previous encoding (the quadratic Residue ∈ 𝔾q and ∉ ℙ), which may not be true.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiH1n1y_SSEBMq-tvzE3k0a8tRwDTBVuNPUBqVtmO0JTG_RnDt5mD3_0wcnfmXP0AvJYuNihcjbi28IOr97bdMS7RrUt1PnQf-DFh3eB2cjQxk4tu-iIdGKRJUkkZIuNs2_q4TlNVpocbJ8ss9oAbCNRiuru3yxp-B8aop08uee6cxZ7R-CxiG7jNXiFVF_=w640-h178)](https://blogger.googleusercontent.com/img/a/AVvXsEiH1n1y_SSEBMq-tvzE3k0a8tRwDTBVuNPUBqVtmO0JTG_RnDt5mD3_0wcnfmXP0AvJYuNihcjbi28IOr97bdMS7RrUt1PnQf-DFh3eB2cjQxk4tu-iIdGKRJUkkZIuNs2_q4TlNVpocbJ8ss9oAbCNRiuru3yxp-B8aop08uee6cxZ7R-CxiG7jNXiFVF_)

  

As a result, a malicious voter could encode any 𝑦 ∈ 𝔾q ∩ ℙ, so at line 57, instead of calculating the expected square root due to the [quadratic reciprocity](https://en.wikipedia.org/wiki/Quadratic_reciprocity), the algorithm would actually be exponentiating it. The resulting Write-In will depend on the election public parameters (p, q).

File: e-voting-libraries-master/e-voting-libraries-protocol-algorithms/src/main/java/ch/post/it/evoting/evotinglibraries/protocol/algorithms/preliminaries/writeins/QuadraticResidueToWriteInAlgorithm.java
  
  
  38:  /**
  39:  * Maps a quadratic residue to a write-in string.
  40:  *
  41:  * @param quadraticResidue y, the quadratic residue as a {@link GqElement}. Must be non-null.
  42:  * @return the corresponding write-in string.
  43:  * @throws NullPointerException if the input is null.
  44:  */
  45:  public String quadraticResidueToWriteIn(final GqElement quadraticResidue) {
  46:  checkNotNull(quadraticResidue);
  47: 
  48:  final GqGroup gqGroup = quadraticResidue.getGroup();
  49:  final ZqGroup zqGroup = ZqGroup.sameOrderAs(gqGroup);
  50:  final BigInteger p = gqGroup.getP();
  51:  final BigInteger q = gqGroup.getQ();
  52: 
  53:  // Input.
  54:  final BigInteger y = quadraticResidue.getValue();
  55: 
  56:  // Operation.
  57:  BigInteger x = y.modPow(p.add(BigInteger.ONE).divide(BigInteger.valueOf(4)), p);
  58:  if (x.compareTo(q) > 0) {
  59:  x = p.subtract(x);
  60:  }
  61: 
  62:  return integerToWriteInAlgorithm.integerToWriteIn(ZqElement.create(x, zqGroup));
  63:  }

This also reveals the lack of any kind of validation: the resulting Write-In is not checked against the expected format enforced by the voting client. As a result, a malicious voting-client can encode arbitrary Write-Ins that do not comply with the specification.

File: e-voting-libraries-master/e-voting-libraries-domain/src/main/java/ch/post/it/evoting/evotinglibraries/domain/tally/TallyComponentVotesPayload.java
  
  
  134:  final Predicate<String> isInAlphabet = element -> element.chars()
  135:  .mapToObj(Character::toString)
  136:  .allMatch(character -> WriteInAlphabet.WRITE_IN_ALPHABET.stream().anyMatch(el -> el.equals(character)));
  137: 
  138:  checkArgument(this.decodedWriteInVotes.stream()
  139:  .flatMap(Collection::stream)
  140:  .allMatch(isInAlphabet),
  141:  "The write-in voting options characters must be in the defined alphabet.");

Eventually, the decoded write-in votes are populated from the persisted 'tallyComponentVotesPayload' file to the tally output files (eCh-0110, eCh-0155 and evoting-decrypt)

File: e-voting-libraries-master/e-voting-libraries-xml/src/main/java/ch/post/it/evoting/evotinglibraries/xml/mapper/ResultDeliveryMapper.java
  
  
  161:  IntStream.range(0, tallyComponentVotesPayload.getActualSelectedVotingOptions().size())
  162:  .forEach(i -> updateBallotTypeWithSelectedVotingOptions(
  163:  contestType,
  164:  ballotBoxType,
  165:  tallyComponentVotesPayload.getActualSelectedVotingOptions().get(i),
  166:  tallyComponentVotesPayload.getDecodedWriteInVotes().get(i)));

As we can see at line 263, the '#' separator character is expected.

File: e-voting-libraries-xml/src/main/java/ch/post/it/evoting/evotinglibraries/xml/mapper/ResultDeliveryMapper.java
  
  
  255:  case WRITE_INS_CANDIDATE_VALUE -> {
  256:  BallotElectionType ballotElectionType = ballotElectionTypes.get(answerAdditionalInformation.identificationIds());
  257:  if (ballotElectionType == null) {
  258:  ballotElectionType = new BallotElectionType();
  259:  ballotElectionTypes.put(answerAdditionalInformation.identificationIds(), ballotElectionType);
  260:  }
  261:  // It is assumed all dummy values across elections are at the end.
  262:  final String decodedWriteIn = listOfDecodedWriteInsPerVoter.get(currentWriteInIndex++);
  263:  ballotElectionType.getChosenWriteInsCandidateValue().add(decodedWriteIn.substring(decodedWriteIn.indexOf("#") + 1));
  264:  }

### Risk 

Malicious voters (or compromised voting clients) can forge Write-Ins that do not comply with the specification. However, Swiss Post stated that even malformed Write-Ins cannot render a vote invalid.

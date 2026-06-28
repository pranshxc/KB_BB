---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-31_beware-of-javas-stringgetbytes.md
original_filename: 2023-03-31_beware-of-javas-stringgetbytes.md
title: Beware of Java's String.getBytes
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: cde921159c55b8952e4d46a8860ca0c74e3114277fc94a4be61be23204a5ec0f
text_sha256: ed84c2fbeb0089aa31d3507ce15d0b2055d35194e719d62ebf3c21306c7bb02a
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Beware of Java's String.getBytes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-31_beware-of-javas-stringgetbytes.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `cde921159c55b8952e4d46a8860ca0c74e3114277fc94a4be61be23204a5ec0f`
- Text SHA256: `ed84c2fbeb0089aa31d3507ce15d0b2055d35194e719d62ebf3c21306c7bb02a`


## Content

---
title: "Beware of Java's String.getBytes"
url: "https://www.reversemode.com/2023/03/beware-of-javas-stringgetbytes.html"
final_url: "https://www.reversemode.com/2023/03/beware-of-javas-stringgetbytes.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["Swiss E-Voting"]
bugs: ["Hash collision", "Cryptographic issues", "Security code review"]
publication_date: "2023-03-31"
added_date: "2023-04-06"
source: "pentester.land/writeups.json"
original_index: 1313
---

###  Beware of Java's String.getBytes 

[ March 31, 2023  ](https://www.reversemode.com/2023/03/beware-of-javas-stringgetbytes.html "permanent link")

  

Sometimes there are subtle bugs whose origin can be found in some quirks from the underlying language used to build the software. This blog post describes one of those cases in order to let both fellow security researchers and developers, who didn't know about it, become aware of this potential vulnerable pattern. In fact, I'm pretty sure that similar bugs to the one herein described likely affect a bunch of products/codebases out there.

  

  

In [previous](https://www.reversemode.com/2022/01/finding-vulnerabilities-in-swiss-posts.html) [posts](https://www.reversemode.com/2022/05/finding-vulnerabilities-in-swiss-posts.html), I've already described some bugs in the Swiss Post's future E-voting system. While reading their [Crypto-Primitives specification](https://gitlab.com/swisspost-evoting/crypto-primitives/crypto-primitives/-/blob/master/Crypto-Primitives-Specification.pdf), which among other things describes the custom Hashing algorithm Swiss Post implemented, I noticed something potentially interesting.

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio3_3wRZzQQ98PR498jjutyWMOTkYpz_gcmLhi8T5FHklHuniB-D8sgLwV2_iLtbuFJwzhU6tqSFtrmUpTtdwsv-SGIZwFucfX110PSEpaGk_l6uXClJZvZk7QQnboI4PmgC35hq6jT4wGKez7xdhVHdK58LxizExW7K6SkA5iW8Th9HV00qNubt2rsg/w354-h400/Recursive_hash2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio3_3wRZzQQ98PR498jjutyWMOTkYpz_gcmLhi8T5FHklHuniB-D8sgLwV2_iLtbuFJwzhU6tqSFtrmUpTtdwsv-SGIZwFucfX110PSEpaGk_l6uXClJZvZk7QQnboI4PmgC35hq6jT4wGKez7xdhVHdK58LxizExW7K6SkA5iW8Th9HV00qNubt2rsg/s1466/Recursive_hash2.png)

  

  

Basically, there are 4 different types that are supported: byte arrays, strings, integers and vectors. Before being hashed, strings are converted to a byte array via the '_StringToByteArray_ ' algorithm.

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjtaSgW-OZOd7UpXdzGNZddBO4CYdwWWvCI2cArepdnSbShNSaYsa3df38kePGRsBjykc7cjjYshJ8UU21RVVbatr7s4bDP0FD9xsG7cTY_R3qkLHUf1dwlxRq4wIsYWprsISr-17tBp6EUd10bKNcoSkrUh69JSsmqzGpOznHcN4_sf0o-phBaE9j4Ow=w400-h338)](https://blogger.googleusercontent.com/img/a/AVvXsEjtaSgW-OZOd7UpXdzGNZddBO4CYdwWWvCI2cArepdnSbShNSaYsa3df38kePGRsBjykc7cjjYshJ8UU21RVVbatr7s4bDP0FD9xsG7cTY_R3qkLHUf1dwlxRq4wIsYWprsISr-17tBp6EUd10bKNcoSkrUh69JSsmqzGpOznHcN4_sf0o-phBaE9j4Ow)

  
However, by comparing '_StringToByteArray_ ' and '_ByteArrayToString_ ' we can find a significant difference: invalid UTF-8 sequences are only considered in the latter. Let's see how this was implemented in the code:

  

File: crypto-primitives-master/src/main/java/ch/post/it/evoting/cryptoprimitives/internal/utils/ConversionsInternal.java
  
  
  079:  /**
  080:  * See {@link ch.post.it.evoting.cryptoprimitives.utils.Conversions#stringToByteArray}
  081:  */
  082:  public static byte[] stringToByteArray(final String s) {
  083:  checkNotNull(s);
  084: 
  085:  // Corresponds to UTF-8(S)
  086:  return s.getBytes(StandardCharsets.UTF_8);
  087:  }
  088: 
  089:  /**
  090:  * See {@link ch.post.it.evoting.cryptoprimitives.utils.Conversions#byteArrayToString}
  091:  */
  092:  public static String byteArrayToString(final byte[] b) {
  093:  checkNotNull(b);
  094:  checkArgument(b.length > 0, "The length of the byte array must be strictly positive.");
  095: 
  096:  CharsetDecoder decoder = StandardCharsets.UTF_8.newDecoder();
  097:  // The try-catch clause implements the pseudo-code's if statement
  098:  try {
  099:  // Corresponds to UTF-8^-1(B)
  100:  return decoder.decode(ByteBuffer.wrap(b)).toString();
  101:  } catch (CharacterCodingException ex) {
  102:  throw new IllegalArgumentException("The byte array does not correspond to a valid sequence of UTF-8 encoding.");
  103:  }
  104:  }

  

As expected, at line 100, '_byteArrayToString_ ' tries to decode the input to detect invalid UTF-8 sequences. On the other hand, at line 86, '_StringToByteArray'_ directly uses '_getBytes'._

  

Internally, 'getBytes' will encode the string before returning the bytes. Let's see Java's implementation:

  

File: java/lang/String.java
  
  
  /**
  * Encodes this {@code String} into a sequence of bytes using the given
  * {@linkplain java.nio.charset.Charset charset}, storing the result into a
  * new byte array.
  *
  * <p> This method always replaces malformed-input and unmappable-character
  * sequences with this charset's default replacement byte array.  The
  * {@link java.nio.charset.CharsetEncoder} class should be used when more
  * control over the encoding process is required.
  *
  * @param  charset
  *  The {@linkplain java.nio.charset.Charset} to be used to encode
  *  the {@code String}
  *
  * @return  The resultant byte array
  *
  * @since  1.6
  */
  public byte[] getBytes(Charset charset) {
  if (charset == null) throw new NullPointerException();
  return encode(charset, coder(), value);
  }

  

  

As the description of the method clearly states, any invalid character sequence will be replaced (_onMalformedInput(CodingErrorAction.REPLACE).onUnmappableCharacter(CodingErrorAction.REPLACE_) with the default "replacement byte array", it doesn't trigger any exception.

  

In Java, the replacement byte array for a default Charset provider is one of the Unicode specials, the replacement character (0xFFFD). However, for some reason Java's UTF-8 Charset Encoder uses '?' (63d).

  

File: 'sun.nio.cs.UTF_8'

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj4gCDuBBkwmJKgDlj735Kb5Skscr62iz3p2tq2-bySpSa6WqaiBcpmkUPle-e9Jee9Xel70thQdkgg77d7D9a6G0wuHnZsFVVotkEoEketepZUCDdNEjjnyul2ZCo5EIf_fT7_hpKPLUx8bx3XBVqMAWsAnbkn3QRRFETA5e9GwqTUTtx619kDaEz9kA=w640-h150)](https://blogger.googleusercontent.com/img/a/AVvXsEj4gCDuBBkwmJKgDlj735Kb5Skscr62iz3p2tq2-bySpSa6WqaiBcpmkUPle-e9Jee9Xel70thQdkgg77d7D9a6G0wuHnZsFVVotkEoEketepZUCDdNEjjnyul2ZCo5EIf_fT7_hpKPLUx8bx3XBVqMAWsAnbkn3QRRFETA5e9GwqTUTtx619kDaEz9kA)

  
This behavior does not seem to comply with the Unicode's security [recommendations](https://unicode.org/reports/tr36/).

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrh6bjt18wnZ6Vw2f74OOVAXZPfgF_1aHOXUd8TvAHrkSq44NKqWJH1FA35r5QrDfykJZWW4IJD8rdUnaExREh5M0HauspGT_dS_krrc7WMtMAuSf_N1EpMg-q35aBK0jDr8AneKecJe1zfLFPsJy_hB_NK9I9UzTW2bUo27v3bpAd_1KLn5OdJrslAw=w640-h78)](https://blogger.googleusercontent.com/img/a/AVvXsEjrh6bjt18wnZ6Vw2f74OOVAXZPfgF_1aHOXUd8TvAHrkSq44NKqWJH1FA35r5QrDfykJZWW4IJD8rdUnaExREh5M0HauspGT_dS_krrc7WMtMAuSf_N1EpMg-q35aBK0jDr8AneKecJe1zfLFPsJy_hB_NK9I9UzTW2bUo27v3bpAd_1KLn5OdJrslAw)

  

It also differs from other languages, such as C#, which follows the best-practice and replaces (_Encoding.UTF8.GetBytes_) the malformed character sequence with the UTF-8 encoded version (0xEF 0xBF 0xBD) of the replacement character. 

### Impact

This specific pattern may result in different attack scenarios, depending on the logic where the vulnerable pattern has been identified.

#### _Swiss Post E-Voting_

In this specific case, what we end up with is a hash collision vulnerability.

This silly PoC elaborates how two different strings are not injectively encoded, thus leading to a potential hash collision according to the 'RecursiveHash' algorithm.

  

  

  
  
  import java.nio.charset.StandardCharsets;
  import java.nio.ByteBuffer;
  import java.nio.CharBuffer;
  import java.util.Arrays;
  import java.util.stream.Collectors;
  import java.nio.charset.CharsetEncoder;
  import java.nio.charset.CodingErrorAction;
  import java.nio.ByteBuffer;
  import java.nio.charset.CharacterCodingException;
  import java.nio.CharBuffer;
  
  public class poc {
  
  public static void encode(String string)
  throws CharacterCodingException {
  CharsetEncoder encoder = StandardCharsets.UTF_8.newEncoder();
  
  System.out.println("\nEncoding");
  
  ByteBuffer encoded = encoder.encode(CharBuffer.wrap(string.toCharArray()));
  
  System.out.println("\nEncoding end");
  
  }
  
  public  static void printhex(byte []ars) {
  
  for(int i=0;i<ars.length;i++){  
  System.out.print(String.format("\\x%04X",(short)ars[i]));  
  }
  
  System.out.print("\n");
  return;
  }
  
  public static byte[] stringToByteArray(final String s) {
  
  return s.getBytes(StandardCharsets.UTF_8);
  }
  
  public static String  buildCustomString(String dat) {
  
  String badString = Arrays.stream(dat.split("\\+U"))
  .filter(s -> ! s.isEmpty()) 
  .map(s -> {
  try {
  return Integer.parseInt(s, 16);
  } catch (NumberFormatException e) { 
  System.out.println("Error parsing int");
  }
  return null; 
  })
  .map(i -> Character.toString(i)) 
  .collect(Collectors.joining());
  
  return badString;
  }
  
  public static String DumpInfo(String inf)
  {
  String badString;
  
  System.out.println("=>> Original string (custom format): \"" + inf+"\""); 
  System.out.println("[+] Building String");
  badString = buildCustomString(inf);
  
  System.out.println("[+] String badString => \""+ badString+"\"");
  System.out.print("[+] badString.toCharArray() =>\t\t"); 
  char[] hash3 = badString.toCharArray();
  
  for(int i=0;i<hash3.length;i++){  
  System.out.print(String.format("\\x%04X",(short)hash3[i]));  
  }  
  
  System.out.print("\n");
  
  System.out.print("[+] stringToByteArray(badString) =>  "); 
  printhex(stringToByteArray(badString));
  
  return badString;
  }
  
  public static void main(String args[]) {
  
  String badString1,badString2;
  
  String base = "Question_1?";
  
  // +UD8AF is illegal so it will be mapped to '?' after UTF8 encoding.
  String data1 = "+U0051+U0075+U0065+U0073+U0074+U0069+U006f+U006E+U005f+U0031+UD8AF";
  
  badString1 = DumpInfo(data1);
  
  System.out.println("[+] badString after UTF-8 encoding: \""+ badString1 + "\"");
  System.out.print("[+] stringToByteArray(base) =>  \t"); 
  printhex(stringToByteArray(base));
  
  if(!badString1.equals(base)){
  System.out.println("[+] 'badString' and 'base' are not equal");
  }
  
  try {
  //This will trigger an exception
  encode(badString1);
  
  }
  catch (Exception e) {
  e.printStackTrace();
  }
  
  System.out.print("\n");
  
  }
  
  }

  

In the PoC there are two strings '_base_ ' and '_badString_ '. The first one is a valid UTF-8 string that contains "_Question_1?_ ", while the latter contains "_Question_1_ " plus a malformed UTF-8 sequence ('\uD8AF').

  

When '_stringToByteArray_ ' is invoked on '_badString_ ', its illegal sequence will be substituted by '?' resulting in the same hash that would be generated for the 'base' string. However, those strings, before being encoded, are different, as can be checked in the '_toCharArray()_ ' and '_equals_ ' comparisons. This is important to be able to potentially bypass certain checks, as '_equals_ ' operates at the char array level

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEifgqehXp35WBfk6jqCA5K0PaBEcXrsRgYX7LGzB9mOZQGyGuG-gy6epgQIKkKoHeflKWgkeKdYg5DWDfOATMtuyqSW2cky3DOnOf-lkDDBUdmM0a0zHCYj9dYdsdUeIspMfoViCX1V1QD6dZ5DUFElnfOZSiobOSe2lQWPDqCo58JRd9fN_tfvHuiuHw=w400-h368)](https://blogger.googleusercontent.com/img/a/AVvXsEifgqehXp35WBfk6jqCA5K0PaBEcXrsRgYX7LGzB9mOZQGyGuG-gy6epgQIKkKoHeflKWgkeKdYg5DWDfOATMtuyqSW2cky3DOnOf-lkDDBUdmM0a0zHCYj9dYdsdUeIspMfoViCX1V1QD6dZ5DUFElnfOZSiobOSe2lQWPDqCo58JRd9fN_tfvHuiuHw)

#### The output of the PoC is as follows

#### 

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgo_qtkSqX_qHNupqcIdk4bNhRNOxl1jXkaYdsHCMC_EduABPphAZdzDvtuf622340ZwRQJGHX16L_NupeZ9lyRn0pb6TfhKhssh0FgzqLpCZBiBSxJY3RGpGizkvZiwWYfSHOT33Eeen6esD8olmyyD7oJLVyQFqdbKUbdMl62vb5ykNz-9-NaR5liHw=w640-h208)](https://blogger.googleusercontent.com/img/a/AVvXsEgo_qtkSqX_qHNupqcIdk4bNhRNOxl1jXkaYdsHCMC_EduABPphAZdzDvtuf622340ZwRQJGHX16L_NupeZ9lyRn0pb6TfhKhssh0FgzqLpCZBiBSxJY3RGpGizkvZiwWYfSHOT33Eeen6esD8olmyyD7oJLVyQFqdbKUbdMl62vb5ykNz-9-NaR5liHw)

[Swiss Post](https://www.post.ch/en) confirmed the bug ( [#YWH-PGM232-122](https://gitlab.com/swisspost-evoting/e-voting/e-voting-documentation/-/issues/46) ), which has been patched in version 1.3.0

####  _Other products_

The fact that Java's UTF-8 Encoder is replacing a malformed character sequence with a valid one, '?', which in turn plays an important role in URLs makes me think that probably, in addition to the potential cryptographic issues we have already seen, this vulnerable pattern might be used to bypass certain security-related logic.

  

As long as the attacker can control the string, for instance after deserializing an attacker controlled JSON by using [Jackson](https://github.com/FasterXML/jackson), there will be a chance to abuse the Java's UTF-8 'getBytes' replacement logic.

  

  
  
  ObjectMapper objectMapper = new ObjectMapper();
  String json = "{ \"badString\" : \"Question_1\\uD84F\" }";
  JsonNode jsonNode = objectMapper.readTree(json);
  String badString = objectMapper.readValue(jsonNode.get("badString").toString(), String.class);

  

If you happen to stumble upon a product with such a vulnerability, I would love to hear about it.

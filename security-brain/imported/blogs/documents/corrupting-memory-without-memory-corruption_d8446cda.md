---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-27_corrupting-memory-without-memory-corruption.md
original_filename: 2022-07-27_corrupting-memory-without-memory-corruption.md
title: Corrupting memory without memory corruption
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: d8446cda283e6522113911ed58912184307dc7761b2aa035443ac7f8fee7620d
text_sha256: 5e1b732a34cfff6500048075536d40141aabdcf79deb68c03c9c53f37b77fc3e
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Corrupting memory without memory corruption

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-27_corrupting-memory-without-memory-corruption.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `d8446cda283e6522113911ed58912184307dc7761b2aa035443ac7f8fee7620d`
- Text SHA256: `5e1b732a34cfff6500048075536d40141aabdcf79deb68c03c9c53f37b77fc3e`


## Content

---
title: "Corrupting memory without memory corruption"
page_title: "Corrupting memory without memory corruption - The GitHub Blog"
url: "https://github.blog/2022-07-27-corrupting-memory-without-memory-corruption/"
final_url: "https://github.blog/security/vulnerability-research/corrupting-memory-without-memory-corruption/"
authors: ["Man Yue Mo (@mmolgtm)"]
programs: ["Google"]
bugs: ["Memory corruption"]
publication_date: "2022-07-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2388
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# Corrupting memory without memory corruption

In this post I’ll exploit CVE-2022-20186, a vulnerability in the Arm Mali GPU kernel driver and use it to gain arbitrary kernel memory access from an untrusted app on a Pixel 6. This then allows me to gain root and disable SELinux. This vulnerability highlights the strong primitives that an attacker may gain by exploiting errors in the memory management code of GPU drivers.

![](https://github.blog/wp-content/uploads/2021/12/github-security_orange-banner.png?resize=1200%2C630)

[Man Yue Mo](https://github.blog/author/mymo/ "Posts by Man Yue Mo")·[@m-y-mo](https://github.com/m-y-mo)

July 27, 2022  | Updated August 1, 2022 

| 29 minutes 

  * Share: 
  * [ ](https://x.com/share?text=Corrupting%20memory%20without%20memory%20corruption&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fcorrupting-memory-without-memory-corruption%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=Corrupting%20memory%20without%20memory%20corruption&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fcorrupting-memory-without-memory-corruption%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=Corrupting%20memory%20without%20memory%20corruption&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fcorrupting-memory-without-memory-corruption%2F)

In this post I’ll cover the details of CVE-2022-20186, a vulnerability in the Arm Mali GPU that I reported to the Android security team, which was fixed in the [June update for Pixel](https://source.android.com/security/bulletin/pixel/2022-06-01). This bug exists in the memory management code of the Arm Mali GPU kernel driver, which is exploitable to map arbitrary physical pages to the GPU memory with both read and write access. This gives a very strong primitive that allows me to gain arbitrary kernel code execution and root on a Pixel 6 with ease.

As explained in my [previous post](https://github.blog/2022-06-16-the-android-kernel-mitigations-obstacle-race/), the GPU driver on Android is a very attractive target for an attacker, due to the following reasons:

  1. On all Android devices, the GPU driver can be accessed from the untrusted app domain, so any compromised or malicious app can launch an attack on the kernel.
  2. Most Android devices use either Qualcomm’s Adreno GPU (which was covered in the [previous post](https://github.blog/2022-06-16-the-android-kernel-mitigations-obstacle-race/)), or the Arm Mali GPU. So by just attacking two GPU drivers, it is possible to gain universal root on all Android devices with relatively few bugs.
  3. As we’ll see in this post, a large part of the GPU driver is responsible for creating shared memory between the GPU and user applications, and to achieve this, GPU drivers often contain fairly elaborate memory management code that is complex and error prone. Errors in the GPU driver can often lead to bugs that are undetectable as memory corruptions and also immune to existing mitigations, such as the bug in this post.

In fact, of the seven Android 0-days that were detected as exploited in the wild in 2021, five targeted GPU drivers. As of the date of writing, another bug that was exploited in the wild — [CVE-2021-39793](https://source.android.com/security/bulletin/pixel/2022-03-01), disclosed in March 2022 — also targeted the GPU driver. Together, of these six exploited in-the-wild bugs that targeted Android GPU, three bugs targeted the Qualcomm GPU, while the other three targeted the Arm Mali GPU.

## The Arm Mali GPU

The Arm Mali GPU can be integrated in different chipsets (for example, see “Implementations” in the [Mali(GPU) Wikipedia entry](https://en.wikipedia.org/wiki/Mali_\(GPU\)) for a list of chipsets that have the Mali GPU) and is used on Android devices. For example, all of the international versions of the Samsung S series phones up to the S21 use the Mali GPU, as well as Pixel 6 and Pixel 6 Pro.

There are many good articles about the architecture of the Mali GPU (for example, [“The Mali GPU: An abstract machine”](https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/the-mali-gpu-an-abstract-machine-part-1---frame-pipelining) series by Peter Harris, and [“Arm’s new Mali-G77 & Valhall gpu architecture: a major leap”](https://www.anandtech.com/show/14385/arm-announces-malig77-gpu/2) by Andrei Frumusanu).

The names of the Mali GPU architectures are inspired by Norse mythology, starting from “Utgard”, “Midgard”, “Bifrost” to the most recent “Valhall”. Most modern Android phones are running either “Valhall” or “Bifrost” architecture and their kernel drivers share much of the code. As these newer architectures are based largely on the “Midgard” architecture, there are sometimes macros in the “Valhall” or “Bifrost” driver with the “MIDGARD” prefix (e.g. `MIDGARD_MMU_LEVEL`). These macros may still be in active use in the newer drivers and the “MIDGARD” prefix merely reflects their historic origin.

The Mali GPU driver consists of two different parts. The kernel driver is open source and new versions are released regularly on the [Arm Developer page](https://developer.arm.com/downloads/-/mali-drivers/valhall-kernel). Apart from the open source kernel driver, there is also a proprietary user space driver responsible for compiling programs written in shading languages (e.g. OpenGL) into instruction sets of the Mali GPU. This post will only cover the open source kernel driver and will simply call it the Mali driver.

In order to use the Mali driver, a `[kbase_context](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#1747)` first has to be created by calling a sequence of `ioctl` calls. The `kbase_context` defines an execution environment for the user space application to interact with the GPU. Each device file that interacts with the GPU has a separate `kbase_context`. Amongst other things, the `kbase_context` defines its own GPU address space and manages user space and GPU memory sharing.

## Memory management in the Mali kernel driver

There are different ways to share memory between the GPU and user space process, but for the purpose of this post, I’ll only cover the case where the shared memory is managed by the driver. In this case, the user first calls the `[KBASE_IOCTL_MEM_ALLOC](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_linux.c#292)` `ioctl` to allocate pages from the `kbase_context`. These pages are allocated from a per-context memory pool in the `kbase_context` (`[mem_pools](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#1811)`) and do not get mapped to the GPU nor to the user space immediately. The `ioctl` returns a cookie to the user, which is then used as the `offset` to `mmap` the device file and map these pages to the GPU and to user space. The backing page is then recycled back to the `mem_pools` when the memory is unmapped with `munmap`.

The `KBASE_IOCTL_MEM_ALLOC` `ioctl` is implemented in `[kbase_mem_alloc](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_linux.c#292)`. This function creates a `[kbase_va_region](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem.h#322)` object to store data relevant to the memory region:
  
  
  struct kbase_va_region *kbase_mem_alloc(struct kbase_context *kctx,
  u64 va_pages, u64 commit_pages,
  u64 extension, u64 *flags, u64 *gpu_va)
  {
  ...
  struct kbase_va_region *reg;
  ...
  reg = kbase_alloc_free_region(rbtree, PFN_DOWN(*gpu_va),
  va_pages, zone);
  ...
  

It also allocates backing pages for the memory region from `mem_pools` of the `kbase_context` by calling `[kbase_alloc_phy_pages](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem.c#2139)`.

When calling from a 64 bit process, the created region is stored in the `[pending_regions](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#1802)` of `kbase_context`, instead of mapping it immediately:
  
  
  if (*flags & BASE_MEM_SAME_VA) {
  ...
  kctx->pending_regions[cookie_nr] = reg;
  
  /* relocate to correct base */
  cookie = cookie_nr + PFN_DOWN(BASE_MEM_COOKIE_BASE);
  cookie <<= PAGE_SHIFT;
  
  *gpu_va = (u64) cookie;
  }...
  

The `cookie` from the above is then returned to the user, which can then be used as the `offset` parameter in `mmap` to map this memory.

### **Mapping pages to user space**

Although I’ll not be accessing the memory region through the user space mapping, when exploiting the vulnerability, it is important to understand how the virtual addresses are assigned when `mmap` is called to map the region, so I’ll go through the user space mapping here briefly. When `mmap` is called, `[kbase_context_get_unmapped_area](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/thirdparty/mali_kbase_mmap.c#237)` is used to find a free region for the mapping:
  
  
  unsigned long kbase_context_get_unmapped_area(struct kbase_context *const kctx,
  const unsigned long addr, const unsigned long len,
  const unsigned long pgoff, const unsigned long flags)
  {
  ...
  ret = kbase_unmapped_area_topdown(&info, is_shader_code,
  is_same_4gb_page);
  ...
  return ret;
  }
  

This function does not allow mapping the region to a fixed virtual address with the `MAP_FIXED` flag . Instead, it uses `kbase_unmapped_area_topdown` to look for a free region large enough to fit the requested memory and returns its address. As its name suggests, `kbase_unmapped_area_topdown` returns the highest available address. The mapped address is then stored as the `[start_pfn](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem.h#326)` field in the `kbase_va_region`. In particular, this means that relative addresses of consecutively mmapped regions are predictable:
  
  
  int fd = open("/dev/mali0", O_RDWR);
  union kbase_ioctl_mem_alloc alloc;
  union kbase_ioctl_mem_alloc alloc2;
  ...
  ioctl(fd, KBASE_IOCTL_MEM_ALLOC, alloc);
  ioctl(fd, KBASE_IOCTL_MEM_ALLOC, alloc2);
  void* region1 = mmap(NULL, 0x1000, prot, MAP_SHARED, fd, alloc.out.gpu_va);
  void* region2 = mmap(NULL, 0x1000, prot, MAP_SHARED, fd, alloc2.out.gpu_va);
  

In the above, the `region2` will be `region1 - 0x1000` because of how `kbase_unmapped_area_topdown` works.

### **Mapping pages to the GPU**

The GPU mapping is the more interesting part. Each `kbase_context` maintains its own GPU address space and also manages its own GPU page table. Each `kbase_context` maintains a four-level page table that is used for translating the GPU address to the backing physical page. It has a `[mmut](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#1751)` field that stores the top level [page table global directory (PGD)](https://www.kernel.org/doc/gorman/html/understand/understand006.html) as the `[pgd](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#293)` field. The implementation is standard, with `mmut->pgd` being a page interpreted as a 512 element `int64_t` array whose entries point to the page frames that store the next level PGD, until it reaches the bottom level, where the page table entries (PTE) store the backing physical page (as well as page permissions) instead.

As most of the addresses are unused, the various PGD and PTE of the page table are only created when they are needed for an access:
  
  
  static int mmu_get_next_pgd(struct kbase_device *kbdev,
  struct kbase_mmu_table *mmut,
  phys_addr_t *pgd, u64 vpfn, int level)
  {
  ...
  p = pfn_to_page(PFN_DOWN(*pgd));
  page = kmap(p);
  ...
  target_pgd = kbdev->mmu_mode->pte_to_phy_addr(page[vpfn]);  //<------- 1.
  
  if (!target_pgd) {
  target_pgd = kbase_mmu_alloc_pgd(kbdev, mmut);  //<------- 2.
  ...
  kbdev->mmu_mode->entry_set_pte(&page[vpfn], target_pgd); //<------- 3.
  

When an access requires a certain PGD, it’ll look for the entry from the previous level PGD (1 in the above). As all entries of a PGD are initialized to a magic value that indicates the entry is invalid, if the entry had not been accessed before, then 1 will return a `NULL` pointer, which would lead to `target_pgd` being allocated (2 in the above). The address of `target_pgd` is then added as an entry in the previous PGD (3 in the above). The page frame that is backing `target_pgd` is allocated via the `mem_pools` of the global `[kbase_device](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_defs.h#969)` `kbdev`, which is a global memory pool shared by all contexts.

When mapping memory to GPU, `[kbase_gpu_mmap](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem.c#1461)` will call `kbase_mmu_insert_pages` to add the backing pages to the GPU page table:
  
  
  int kbase_gpu_mmap(struct kbase_context *kctx, struct kbase_va_region *reg, u64 addr, size_t nr_pages, size_t align)
  {
  ...
  alloc = reg->gpu_alloc;
  ...
  if (reg->gpu_alloc->type == KBASE_MEM_TYPE_ALIAS) {
  ...
  } else {
  err = kbase_mmu_insert_pages(kctx->kbdev,
  &kctx->mmu,
  reg->start_pfn,  //<------ virtual address
  kbase_get_gpu_phy_pages(reg),  //<------ backing pages
  kbase_reg_current_backed_size(reg),  
  reg->flags & gwt_mask,
  kctx->as_nr,
  group_id);
  ...
  }
  ...
  }
  

This will insert the backing pages at the address specified by `reg->start_pfn`, which is also the address of the memory region in the user space (see Mapping pages to user space).

### Memory alias

The `KBASE_IOCTL_MEM_ALIAS` is an interesting `ioctl` that allows multiple memory regions to share the same underlying backing pages. It is implemented in `[kbase_mem_alias](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_linux.c#1710)`. It accepts a `stride` parameter, as well as an array of `[base_mem_aliasing_info](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/common/include/uapi/gpu/arm/midgard/mali_base_kernel.h#206)` to specify the memory regions that back the alias region:
  
  
  union kbase_ioctl_mem_alias alias = {0};
  alias.in.flags = BASE_MEM_PROT_CPU_RD | BASE_MEM_PROT_GPU_RD | BASE_MEM_PROT_CPU_WR | BASE_MEM_PROT_GPU_WR;
  alias.in.stride = 4;
  alias.in.nents = 2;
  struct base_mem_aliasing_info ai[2];
  ai[0].handle.basep.handle = region1;
  ai[1].handle.basep.handle = region2;
  ai[0].length = 0x3;
  ai[1].length = 0x3;
  ai[0].offset = 0;
  ai[1].offset = 0;
  alias.in.aliasing_info = (uint64_t)(&(ai[0]));
  ioctl(mali_fd, KBASE_IOCTL_MEM_ALIAS, &alias);
  

In the above, an alias region backed by `region1` and `region2` (both are regions that are already mapped to the GPU) is created by passing the addresses of these regions as `base_mem_aliasing_info::handle::basep::handle`. The stride parameter indicates the gap between these two alias regions (in pages) and `nents` is the number of backing regions. The resulting region that is created is of size `stride * nents` pages:

![](https://github.blog/wp-content/uploads/2022/07/blog-1.png?resize=585%2C435)

The orange region indicates the entire alias region, which is of `2 * 4 = 8` pages. Only six pages are actually mapped and are backed by the pages of `region1` and `region2` respectively. If the starting address of the alias region is `alias_start`, then the addresses between `alias_start` and `alias_start + 0x3000` (three pages) are aliased with `region1`, while `region2` is aliased with the addresses between `alias_start + stride * 0x1000` and `alias_start + (stride + 3) * 0x1000`. This leaves some gaps in the alias region unmapped. This can be seen from the handling of a `KBASE_MEM_TYPE_ALIAS` memory region in `kbase_gpu_mmap`:
  
  
  if (reg->gpu_alloc->type == KBASE_MEM_TYPE_ALIAS) {
  u64 const stride = alloc->imported.alias.stride;
  
  KBASE_DEBUG_ASSERT(alloc->imported.alias.aliased);
  for (i = 0; i < alloc->imported.alias.nents; i++) {
  if (alloc->imported.alias.aliased[i].alloc) {
  err = kbase_mmu_insert_pages(kctx->kbdev,
  &kctx->mmu,
  reg->start_pfn + (i * stride),  //<------ each region maps at reg->start_pfn + (i * stride)
  alloc->imported.alias.aliased[i].alloc->pages + alloc->imported.alias.aliased[i].offset,
  alloc->imported.alias.aliased[i].length,
  reg->flags & gwt_mask,
  kctx->as_nr,
  group_id);
  ...
  }
  ...
  }
  

From the above code, we can see that page table entries are inserted at `reg->start_pfn + (i * stride)`, where `reg->start_pfn` is the starting address of the alias region.

## **The vulnerability**

As explained in the previous section, the size of an alias region is `stride * nents`, which can be seen from `kbase_mem_alias`:
  
  
  u64 kbase_mem_alias(struct kbase_context *kctx, u64 *flags, u64 stride,
  u64 nents, struct base_mem_aliasing_info *ai,
  u64 *num_pages)
  {
  ...
  if ((nents * stride) > (U64_MAX / PAGE_SIZE))
  /* 64-bit address range is the max */
  goto bad_size;
  
  /* calculate the number of pages this alias will cover */
  *num_pages = nents * stride;  //<---- size of region
  

Although there is a check to make sure `nents * stride` is within a limit, there is no integer overflow check which means a large `stride` can be used to overflow `nents * stride`. This means that the resulting alias region may be smaller than its backing region. Let’s see what it means in practice. First allocate and map three three-page regions (`region1`, `region2` and `region3`) to the GPU and denote their start addresses as `region1_start`, `region2_start` and `region3_start`. Then create and map an alias region with `stride = 2 ** 63 + 1` and `nents = 2`. Then because of the integer overflow, the size of the alias region becomes `2` (pages). In particular, the starting address of the alias region, `alias_start` will be `region3_start - 0x2000`, where `0x2000` is the size of the alias region, so the virtual addresses of the alias region and `region3` are contiguous. However, when the alias region is mapped to GPU, `kbase_gpu_mmap` will insert three pages at `alias_start` (which is the size of the backing region (`region1`)):
  
  
  if (reg->gpu_alloc->type == KBASE_MEM_TYPE_ALIAS) {
  u64 const stride = alloc->imported.alias.stride;
  
  KBASE_DEBUG_ASSERT(alloc->imported.alias.aliased);
  for (i = 0; i < alloc->imported.alias.nents; i++) {
  if (alloc->imported.alias.aliased[i].alloc) {
  err = kbase_mmu_insert_pages(kctx->kbdev,
  &kctx->mmu,
  reg->start_pfn + (i * stride),  //<------- insert pages at reg->start_pfn, which is alias_start
  alloc->imported.alias.aliased[i].alloc->pages + alloc->imported.alias.aliased[i].offset,
  alloc->imported.alias.aliased[i].length, //<------- length is the length of the alias region, which is 3
  reg->flags & gwt_mask,
  kctx->as_nr,
  group_id);
  ...
  }
  ...
  }
  

This, in particular, means that the address `region3_start = alias_start + 0x2000` gets remapped and is now backed by a page in `region1`:

![](https://github.blog/wp-content/uploads/2022/07/blog-2.png?resize=758%2C323)

The red rectangle in the right hand side of the figure indicates a page that is backing both `region1_start + 0x2000` and `region3_start` after remapping took place. This is interesting because the backing page marked in red is “owned” by `region1` and the alias region jointly, in the sense that if both regions are unmapped, then the page will get freed and recycled to the memory pool. So if I now unmap both regions, the GPU address corresponding to `region3_start` will be backed by a free’d page, meaning that the GPU can still access this free’d page by accessing the address at `region3_start`.

While this allows free’d pages to be accessed, it is not entirely clear how this may lead to security problems at this point. Recall that backing pages for a memory region are allocated from the `mem_pools` of the `kbase_context` that is associated with the device file. This means that when a page is free’d, it’ll go back to the `mem_pools` and only be used again as a backing page for another region in the same `kbase_context`, which is only used by the calling process. So at this point, it is not totally clear what an attacker can gain from this vulnerability.

## Breaking out of the context

To understand how this bug can be exploited, we need to take a look at how `kbase_mem_pool` works in more detail. To begin with, let’s take a look at how `kbase_mem_pool` allocates and free pages. The function `[kbase_mem_pool_alloc_pages](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_pool.c#529)` is used to allocate pages from a `kbase_mem_pool`:
  
  
  int kbase_mem_pool_alloc_pages(struct kbase_mem_pool *pool, size_t nr_4k_pages,
  struct tagged_addr *pages, bool partial_allowed)
  {
  ...
  /* Get pages from this pool */
  while (nr_from_pool--) {
  p = kbase_mem_pool_remove_locked(pool);  //<------- 1.
  ...
  }
  ...
  if (i != nr_4k_pages && pool->next_pool) {
  /* Allocate via next pool */
  err = kbase_mem_pool_alloc_pages(pool->next_pool,  //<----- 2.
  nr_4k_pages - i, pages + i, partial_allowed);
  ...
  } else {
  /* Get any remaining pages from kernel */
  while (i != nr_4k_pages) {
  p = kbase_mem_alloc_page(pool);  //<------- 3.
  ...
  }
  ...
  }
  ...
  }
  

As the comments suggest, the allocation is actually done in tiers. First the pages will be allocated from the current `kbase_mem_pool` using `[kbase_mem_pool_remove_locked](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_pool.c#96)` (1 in the above). If there is not enough capacity in the current `kbase_mem_pool` to meet the request, then `pool->next_pool`, is used to allocate the pages (2 in the above). If even `pool->next_pool` does not have the capacity, then `[kbase_mem_alloc_page](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_pool.c#153)` is used to allocate pages directly from the kernel via the buddy allocator (the page allocator in the kernel).

When freeing a page, the opposite happens: `[kbase_mem_pool_free_pages](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_pool.c#738)` first tries to return the pages to the current `kbase_mem_pool` (1. in the below), if the current pool is full, it’ll try to return the remaining pages to `pool->next_pool`. If the next pool is also full, then the remaining pages are returned to the kernel by freeing them via the buddy allocator.
  
  
  void kbase_mem_pool_free_pages(struct kbase_mem_pool *pool, size_t nr_pages,
  struct tagged_addr *pages, bool dirty, bool reclaimed)
  {
  struct kbase_mem_pool *next_pool = pool->next_pool;
  ...
  if (!reclaimed) {
  /* Add to this pool */
  ...
  kbase_mem_pool_add_array(pool, nr_to_pool, pages, false, dirty);  //<------- 1.
  ...
  if (i != nr_pages && next_pool) {
  /* Spill to next pool (may overspill) */
  ...
  kbase_mem_pool_add_array(next_pool, nr_to_pool,  //<------ 2.
  pages + i, true, dirty);
  ...
  }
  }
  /* Free any remaining pages to kernel */
  for (; i < nr_pages; i++) {
  ...
  kbase_mem_pool_free_page(pool, p);  //<------ 3.
  ...
  }
  ...
  }
  

So it seems that, by freeing a large number of pages to fill out both the `kbase_mem_pool` and `next_pool`, it is possible to return a page allocated from the per context `kbase_mem_pool` back to kernel memory. Then by using the bug, and some heap feng shui in the buddy allocator, I should be able to access kernel memory via the GPU. As we shall see, to exploit the bug, I only need to return a page to `next_pool` instead of the kernel. So in what follows, I’ll aim to find a reliable way to return a free’d page to `next_pool`.

First, let’s find out what is `next_pool` for the per context `kbase_mem_pool`. The `mem_pools` in a `kbase_context` is initialized in `[kbase_context_mem_pool_group_init](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/context/mali_kbase_context.c#318)`:
  
  
  int kbase_context_mem_pool_group_init(struct kbase_context *kctx)
  {
  return kbase_mem_pool_group_init(&kctx->mem_pools,
  kctx->kbdev,
  &kctx->kbdev->mem_pool_defaults,
  &kctx->kbdev->mem_pools);  //<----- becomes next_pool
  }
  

The last argument, `kctx->kbdev->mem_pools` passed to `[kbase_mem_pool_group_init](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/tags/android-12.0.0_r0.42/mali_kbase/mali_kbase_mem_pool_group.c#46)` becomes the `next_pool` of `kctx->mem_pools`. This is the global `mem_pools` of the `kbase_device` memory pool that is also used for allocating the GPU page table global directories in section Mapping pages to the GPU. This means that, by freeing the doubly mapped page caused by the bug to `next_pool`, it is possible to have the page reused as a PGD. Then by modifying it from the GPU, I can install arbitrary backing pages to the PGD, which would allow arbitrary memory access. This is the path that I’m going to take to exploit the bug. In order to free a page into `next_pool`, I first need to know the capacity of the memory pools.

On a Pixel 6, the capacity of the memory pool can be found using the `debugfs` `/sys/module/mali_kbase/drivers/platform\:mali/1c500000.mali/mempool/max_size` (file name may differ slightly depending on devices). This can be read from a rooted phone and gives the capacity of the memory pool:
  
  
  oriole:/ # cat /sys/module/mali_kbase/drivers/platform\:mali/1c500000.mali/mempool/max_size
  16384
  

This is the capacity of the memory pool configured for the device. As explained before, a `kbase_mem_pool` is empty when it is first created. This means when pages are first allocated from the memory pool, they are allocated from `next_pool`, but when those pages are freed, they are returned to the `kbase_mem_pool`, (which is empty).

![](https://github.blog/wp-content/uploads/2022/07/blog-3.png?resize=864%2C482)

In the above, the gray boxes indicate the full capacities of the memory pools and green regions indicate available pages in the pool. A memory pool is full when the available pages reach its capacity (no gray region left).

While the per context memory pool is used by my process only and I can control its size precisely, the same cannot be said of the device memory pool (`next_pool`). At any time, I must assume there is an unknown number of pages available in the memory pool. It is, however, not difficult to drain the device memory pool and to manipulate its layout.

  1. From an empty per context memory pool, such as when it is first created, allocate a page that I want to place in the device memory pool. As the context memory pool is empty, this page will either be allocated from the device memory pool (`next_pool`) or from kernel (if the device memory pool is full). After this, the context memory pool will still be empty.
  2. Allocate `16384` (capacity of the memory pool) pages from the context memory pool. As the context memory pool is empty, these pages will be allocated from the device memory pool. As the device memory pool has at most 16384 free pages, it will become empty after the allocation.
  3. At this point, both the context memory pool and the device memory pool are empty. If I now free the 16384 pages allocated in step two, the context memory pool will be full and none of the pages is returned to the device memory pool. So after this, the context memory pool is full and the device memory pool is empty.
  4. Free the page created in step one and it’ll be returned to an empty device memory pool.

![](https://github.blog/wp-content/uploads/2022/07/blog-4.png?resize=960%2C540)

In the figure, green regions indicate free pages in the memory pool, while red regions indicate pages that are taken by the allocation.

After these steps, the device memory pool will only contain the page that I just freed. In particular, I can use the bug to hold on to a page, and then follow these steps so that it becomes the only page in the otherwise empty device memory pool. This means that when a GPU PGD is next allocated, the page that I freed and am still able to access will be used for the allocation and I’ll be able to write to this PGD.

To cause an allocation of a PGD, recall that the entries in the GPU page table are allocated lazily and when mapping pages to the GPU, the driver will allocate addresses in a continuous and descending manner (See Mapping pages to user space). As each PGD contains 512 entries, by mapping 512 pages, I can guarantee to reach addresses that require the allocation of a new PGD.

![](https://github.blog/wp-content/uploads/2022/07/blog-5.png?resize=591%2C495)

In the figure, the gray boxes indicate PGDs in different levels of the page table with arrows showing the indices at each level for the address of the same color. The indices in level 0 and level 1 PGD are the same for all the addresses shown (computed as `((addresses >> 12) >> (3 - level)) & 0x1FF`), but addresses separated by 512 pages, such as the orange address and the black address, are guaranteed to be in a different level 3 PGD. So by allocating 512 pages, a new level 3 PGD is needed. Moreover, as the context memory pool is now full, these new 512 pages allocated are taken from the context memory pool, without affecting the device memory pool. (These 512 pages can also be allocated in advance and only map to the GPU at this stage, which will still create a new PGD, so these pages do not actually need to be allocated at this stage). This means that the new PGD entry will be allocated using the page that I still have access to because of the bug. I can then rewrite this PGD entry and map GPU addresses to arbitrary physical pages. This allows me to read and write arbitrary kernel memory.

To recap, the exploit involves the following steps:

  1. Allocate and map three three-page memory regions (`region1`, `region2` and `region3`), and an alias region with `stride` `2 ** 63 + 1` and `nents` 2 backed by `region1` and `region2`.
  2. Allocate 16384 pages to drain the device memory pool.
  3. Free 16384 pages to fill up the context memory pool.
  4. Then unmap both `region1` and the alias region. This will put three pages in the device memory pool as the context memory pool is full. As explained in the section “The vulnerability” one of these pages is still used as the backing page in `region3` and can be accessed from the GPU.
  5. Allocate and map `512 * 3 = 1536` pages to ensure three new PGDs are created. (In fact only two new PGDs are sufficient, which is what is used in the actual exploit). One of these PGDs will use the page that I can access via GPU addresses in `region3`.

## Writing to GPU memory

The question now is: how do I access memory using the GPU? While this is certainly achievable by compiling a shader program and running it on the GPU, it seems rather overkill for the task and it would be good if I could use the kernel driver to do it directly.

The `ioctl` for running GPU instructions is the `KBASE_IOCTL_JOB_SUBMIT`. I can use this `ioctl` to submit a “job chain” to the GPU for processing. Each job chain is basically a list of jobs, which are opaque data structures that contain job headers, followed by payloads that contain the specific instructions. Although ARM never releases any details about the format of these data structures, nor of the GPU instruction sets, there is an extensive amount of research on reverse-engineering the Mali GPU — mostly for creating an open source Mali user space driver, [Panfrost](https://gitlab.freedesktop.org/panfrost). In particular, the instruction sets for the Bifrost and Midgard architectures were reversed by [Connor Abbott](https://github.com/cwabbott0/mali-isa-docs) and the Valhall instruction set was reversed by [Alyssa Rosenzweig](https://www.collabora.com/news-and-blog/news-and-events/reverse-engineering-the-mali-g78.html). Their work, as well as the Panfrost driver, was indispensable to this current work.

Within the Panfrost driver, the `[pandecode-standalone](https://gitlab.freedesktop.org/panfrost/pandecode-standalone)` project is a tool that can be used to decode the jobs that have been submitted to the GPU. In particular, the project contains the data format for GPU jobs that can be used with the `KBASE_IOCTL_JOB_SUBMIT`. Each job contains a header and a payload, and the type of the job is specified in the header. The structure of the payload differs depending on the type of the job, and the following types of jobs are available:
  
  
  enum mali_job_type {
  MALI_JOB_TYPE_NOT_STARTED  =  0,
  MALI_JOB_TYPE_NULL  =  1,
  MALI_JOB_TYPE_WRITE_VALUE  =  2,
  MALI_JOB_TYPE_CACHE_FLUSH  =  3,
  MALI_JOB_TYPE_COMPUTE  =  4,
  MALI_JOB_TYPE_VERTEX  =  5,
  MALI_JOB_TYPE_GEOMETRY  =  6,
  MALI_JOB_TYPE_TILER  =  7,
  MALI_JOB_TYPE_FUSED  =  8,
  MALI_JOB_TYPE_FRAGMENT  =  9,
  };
  

Many of these jobs are related to specific types of shaders, but the `MALI_JOB_TYPE_WRITE_VALUE` provides a simple way to write to a GPU address without the need to write any GPU assembly. The payload of this job type has the following structure:
  
  
  struct MALI_WRITE_VALUE_JOB_PAYLOAD {
  uint64_t  address;
  enum mali_write_value_type  type;
  uint64_t  immediate_value;
  };
  

The fields are fairly self explanatory: The `address` field is the GPU address to write to, `immediate_value` is the value to write, and `type` specifies the size of the write:
  
  
  enum mali_write_value_type {
  MALI_WRITE_VALUE_TYPE_CYCLE_COUNTER  =  1,
  MALI_WRITE_VALUE_TYPE_SYSTEM_TIMESTAMP =  2,
  MALI_WRITE_VALUE_TYPE_ZERO  =  3,
  MALI_WRITE_VALUE_TYPE_IMMEDIATE_8  =  4,
  MALI_WRITE_VALUE_TYPE_IMMEDIATE_16  =  5,
  MALI_WRITE_VALUE_TYPE_IMMEDIATE_32  =  6,
  MALI_WRITE_VALUE_TYPE_IMMEDIATE_64  =  7,
  };
  

with `MALI_WRITE_VALUE_TYPE_IMMEDIATE_8` writing 8 bits to the address, for example. Note that the memory layout and padding of the structure used by the GPU are not always the same as their representation in `C`, and a simple packing/unpacking is needed to convert the job struct in `C` to data that can be consumed by the GPU. This packing/unpacking code is also available in `pandecode-standalone`.

## Arbitrary kernel code execution

At this point, it is fairly easy to achieve arbitrary kernel code execution. As page tables specify the backing page using their page frame, which is a simple shift of the physical address, I can simply write a page frame to the GPU PGD that I control to gain write access to any physical address. On non -Samsung devices, physical addresses in the kernel image are fixed and depend on the firmware only, so having arbitrary physical address write allows me to overwrite any kernel function with my own shell code. I can then use this to disable SELinux and overwrite the credentials of my own process to become root. On Samsung devices, I can follow the steps from my [previous post](https://github.blog/2022-06-16-the-android-kernel-mitigations-obstacle-race/) to disable SELinux and then hijack a `kworker` to gain root.

The exploit for Pixel 6 can be found [here](https://github.com/github/securitylab/tree/main/SecurityExploits/Android/Mali/CVE_2022_20186) with some setup notes.

## Conclusions

In this post I exploited CVE-2022-20186 in the Mali GPU driver. What is interesting about this bug is that the exploit abuses the memory management logic in the GPU to achieve arbitrary physical memory access, and because of this, there is no control flow hijacking involved in exploiting this bug, which renders mitigations such as [kernel control flow integrity](https://source.android.com/devices/tech/debug/kcfi) ineffective.

What is perhaps more important and unusual is that this bug does not involve the usual type of memory corruption that is associated with memory safety. During the exploit, objects are corrupted in the following places:

  1. When a different backing page is rewritten to an existing page table entry by mapping the alias region.
  2. When the above backing page is freed and then reused as a page table entry.

As the first point above involves only overwriting the page table entry using existing kernel functions and there is no invalid memory access or type confusion, it could happen even if the code is written in a memory safe language. Similarly, while point two can be considered a use-after-free, there is no unsafe dereferencing of pointer addresses involved, but rather, a stale physical address is used, and access to the address is done via the GPU. As such, these problems could very well happen even if the code is written in a memory safe language or when mitigations targeting memory safety (such as [Memory Tagging Extension (MTE)](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/enhancing-memory-safety)) are enabled. When dealing with code that is responsible for accessing physical memory directly, the margin of error is very small and strong attack primitives can often be gained without exploiting memory corruptions, as both this and previous vulnerabilities in the GPU drivers have shown.

## Patching time and patch gapping

The bug was reported to the Android security team on January 15, 2022 and was fixed in the June update for Pixel, which was released on June 6, 2022. The time it took is similar to that for fixing issues in the Qualcomm GPU (see, for example the section “Disclosure practices, patching time and patch gapping” in my [previous article](https://github.blog/2022-06-16-the-android-kernel-mitigations-obstacle-race/)), though is past the 90 day disclosure standard set by Google’s Project Zero team. It is not clear to me on the cause of such delays, although this kind of disclosure time frame is not uncommon for Android kernel drivers.

Just like the Qualcomm GPU bug in my previous post, the patch for this bug was publicly visible before an official release. I first noticed the `[patch](https://android.googlesource.com/kernel/google-modules/gpu/+/86e5f385e9d8d83c040c7104df0fc7046c713323%5E%21/#F0)` appearing in the `[android-gs-raviole-5.10-s-qpr3-beta-3](https://android.googlesource.com/kernel/google-modules/gpu/+/refs/heads/android-gs-raviole-5.10-s-qpr3-beta-3)` branch on May 24, 2022. Unfortunately, I hadn’t checked this branch before so I cannot verify when the patch was first made visible. (Although the commit date was March 18, 2022, that is unlikely to be the date when the patch was first publicly visible). At the very least, this leaves a two week gap between the patch being visible and the official release. Once again, this highlights the complexity of the branching system in the Android kernel and the potential of exploiting one day vulnerabilities via patch gapping.

_**August 1, 2022 Update:** Shortly after the initial publication of this blog post, we were informed by Vitaly Nikolenko and Jann Horne that a different CVE ID, [CVE-2022-28348](https://github.com/advisories/GHSA-r85c-7543-8wq6) may have been used by Arm in their [vulnerability list](https://developer.arm.com/Arm%20Security%20Center/Mali%20GPU%20Driver%20Vulnerabilities). Judging from the affected software version, release date and patch analysis, it seems likely that [CVE-2022-28348](https://github.com/advisories/GHSA-r85c-7543-8wq6) and [CVE-2022-20186](https://github.com/advisories/GHSA-f396-p774-5c2p) do indeed refer to the same bug. It is unclear to me why a separate CVE ID was assigned. Judging from the date on Arm’s website, they may well have released a public patch for the bug in April 2022, while the Pixel devices were only patched in June (I have tested that the May patch level of Pixel 6 was still vulnerable to the bug). However, since the only CVE ID that the vendor communicated to me is [CVE-2022-20186](https://github.com/advisories/GHSA-f396-p774-5c2p), this is the only CVE ID that I’m certain of that is associated to this bug and as such, I decided to keep using this CVE ID throughout the post and in our [advisory](https://securitylab.github.com/advisories/GHSL-2022-053_Arm_Mali/)._

* * *

* * *

## Tags:

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

##  Written by 

![Man Yue Mo](https://avatars.githubusercontent.com/u/15773368?v=4&s=200)

###  [Man Yue Mo](https://github.blog/author/mymo/)

[@m-y-mo](https://github.com/m-y-mo)

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

## More on [GitHub Security Lab](https://github.blog/tag/github-security-lab/)

### [Hack the AI agent: Build agentic AI security skills with the GitHub Secure Code Game](https://github.blog/security/hack-the-ai-agent-build-agentic-ai-security-skills-with-the-github-secure-code-game/)

Learn to find and exploit real-world agentic AI vulnerabilities through five progressive challenges in this free, open source game that over 10,000 developers have already used to sharpen their security skills.

[Joseph Katsioloudes](https://github.blog/author/jkcso/ "Posts by Joseph Katsioloudes")

### [Securing the open source supply chain across GitHub](https://github.blog/security/supply-chain-security/securing-the-open-source-supply-chain-across-github/)

Recent attacks on open source focus on exfiltrating secrets; here are the prevention steps you can take today, plus a look at the security capabilities GitHub is working on.

[Zachary Steindler](https://github.blog/author/steiza/ "Posts by Zachary Steindler")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![The ReadME Project](https://github.blog/wp-content/uploads/2022/05/readme.svg)

###  The ReadME Project 

Stories and voices from the developer community.

[ Learn more ](https://github.com/readme)

![GitHub Actions](https://github.blog/wp-content/uploads/2022/05/actions.svg)

###  GitHub Actions 

Native CI/CD alongside code hosted in GitHub.

[ Learn more ](https://github.com/features/actions)

![Enterprise content](https://github.blog/wp-content/uploads/2022/05/careers.svg)

###  Enterprise content 

Executive insights, curated just for you

[ Get started ](https://github.com/solutions/executive-insights)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe

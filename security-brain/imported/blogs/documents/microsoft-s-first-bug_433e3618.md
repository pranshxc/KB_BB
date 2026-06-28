---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-30_microsofts-first-bug.md
original_filename: 2020-05-30_microsofts-first-bug.md
title: Microsoft's first bug
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
language: en
raw_sha256: 433e36183d32b67ec47a31c923462e76deecf5a6ef53b396aa334d1d038006d5
text_sha256: e7365d05da505cc4ff89947e6646a2b8316c642925afb3beb5de211853745900
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft's first bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-30_microsofts-first-bug.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `433e36183d32b67ec47a31c923462e76deecf5a6ef53b396aa334d1d038006d5`
- Text SHA256: `e7365d05da505cc4ff89947e6646a2b8316c642925afb3beb5de211853745900`


## Content

---
title: "Microsoft's first bug"
page_title: "linhlhq's blog: Microsoft's first bug"
url: "https://ezqelusia.blogspot.com/2020/05/microsofts-first-bug.html"
final_url: "https://ezqelusia.blogspot.com/2020/05/microsofts-first-bug.html"
authors: ["Lê Hữu Quang Linh (@linhlhq)"]
programs: ["Microsoft"]
bugs: ["Memory corruption", "File format vulnerability"]
publication_date: "2020-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4546
---

Continuing the series on fuzzing, this section I will share how I find attack surfaces on windows to fuzz. On windows handling a lot of file formats, learn and fuzz these file formats are a common way to find bugs on windows today. The approach and fuzz are exactly the same as finding fault in Irfanview I mentioned in the previous section.

  

Perhaps there are many people who wonder how to find an attack surface? It simply looks like this when you study something long enough, deep enough that you see the possible directions to attack on it. It sounds hard to put this situation in most beginners because not everyone is so good and excellent. But the interesting thing here is that there are so many good researchers who are willing to share everything they research and the bugs they find to the community. Google Project Zero (P0) [1] is an example, I see and track the bugs published on it (including bugs long ago). From there I learned about the types of bugs, surface attacks, components that often cause bugs on different platforms, etc. Or simply monthly I keep track of patches from Microsoft [2] and see if the bugs are patched. What's interesting and suitable for my fuzzing direction or not.

  

**Introduction**

  

Back to talking about fuzz file formats on windows, as we know on windows there are many DLLs, each DLL will have a separate task. For me, for the time being, I will focus on the DLLs that handle file formats. Some common file formats such as media: audio, video, image,... or some other file formats such as XML, XPS, PDF, registry,... These DLLs will export to APIs for developers to use to build the Windows applications, and Windows built-in components also use these APIs.

  

Microsoft itself has provided us MSDN [3], which is a repository for us to read and learn about using those APIs. Not only has the API document, but Microsoft is also generous in giving us a lot of sample code. I usually refer to the Microsoft GitHub repo [4]. It helps us a lot in building harness to fuzz file formats on windows.

  

**Microsoft Font Subsetting**

  

Windows fonts are a file format that I find very diverse, since the kernel-mode count user-mode has a font processing component. P0 public talks about fuzzing fonts of windows [5] [6], all of them are very clear and quality. In the font-related errors that P0 finds, I pay attention to the fontsub.dll library.

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgw01LjPzQ0ZcAIA8d8DZDIM9xaQ9YbaxulqYueQjf5Ba5Dy4TFKtUGg8DI9js7-oikpCemNy-7JFLuSWJge2elI9J_gRdudtIm9F3wgyWvsbKUcSq5qKSHAJo5MQR5q253e12A_KJZhjM/s1600/Screen+Shot+2020-05-27+at+8.27.37+PM.png)

  

Up to the time of P0 public bugs of this library, no one has previously tried fuzz into the fontsub.dll library.

  

The Microsoft Font Subsetting DLL (fontsub.dll) is a default Windows helper library for subsetting TTF fonts; i.e. converting fonts to their more compact versions based on the specific glyphs used in the document where the fonts are embedded. It is used by Windows GDI and Direct2D.

  

The DLL exports two API functions: CreateFontPackage [7] and MergeFontPackage [8].

  

unsigned long CreateFontPackage( const unsigned char *puchSrcBuffer, const unsigned long ulSrcBufferSize, unsigned char **ppuchFontPackageBuffer, unsigned long *pulFontPackageBufferSize, unsigned long *pulBytesWritten, const unsigned short usFlag, const unsigned short usTTCIndex, const unsigned short usSubsetFormat, const unsigned short usSubsetLanguage, const unsigned short usSubsetPlatform, const unsigned short usSubsetEncoding, const unsigned short *pusSubsetKeepList, const unsigned short usSubsetListCount, CFP_ALLOCPROC lpfnAllocate, CFP_REALLOCPROC lpfnReAllocate, CFP_FREEPROC lpfnFree, void *lpvReserved ); |  unsigned long MergeFontPackage( const unsigned char *puchMergeFontBuffer, const unsigned long ulMergeFontBufferSize, const unsigned char *puchFontPackageBuffer, const unsigned long ulFontPackageBufferSize, unsigned char **ppuchDestBuffer, unsigned long *pulDestBufferSize, unsigned long *pulBytesWritten, const unsigned short usMode, CFP_ALLOCPROC lpfnAllocate, CFP_REALLOCPROC lpfnReAllocate, CFP_FREEPROC lpfnFree, void *lpvReserved );  
---|---  
  
  

P0 also publishes the harness they built [9], it's very good, covers all the parameters passed to these two functions. I use that harness to fuzz.

  

In addition to harness, P0 has a public tool that supports TTF/OTF [10] mutate files, this is a tool that I think is the key to help P0 find many bugs with such fonts.

  

Based on these, I began to find and create copus:

1\. Corpus from P0 public with previously published bugs + download on the internet

2\. Mutate these corpus based on the tool of P0

3\. Use winafl-cmin to reduce the number of corpus

4\. Check coverage

5\. Return to step 2

  

I do this task over and over again until the coverage I achieve with fontsub.dll is as follows:

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTnoeyT6ojKb5lV3i7aEAvFLdCYXaYpbQybsDDFqD4xG8NVURkJFRXZD3kuEv54D0wD-JoNzzDpTYZDqRm0Kq0IGhF-rZY5dasIbC0P3aXR6KVQyfxb4RPBr70NI4OGgDiwfMHcuHRxzs/s1600/Screen+Shot+2020-05-27+at+8.14.35+PM.png)

  

With a test case, I can mutate 53.22% on DLL fontsub.dll, 81.08% for CreateFontPackage and 76.40% for MergeFontPackage. I think this is enough to start fuzz.

  

I used Winafl to run with 1 master and 7 slaves, after a few hours I started seeing the first crashes. After a few days, I went back and started checking for those crashes.

  

Most of them are stack overflow errors (0xc00000fd):

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg071kx_cNnvPQJebtniy50Ei8c3lDUk3uhL6lu0sDsNN_1uHZyq9-QSzIlLaY79EI7MQFjbSBu9JC771BgNCJZQjk2E3A1KAdnjI-tm5UtgO6ByNL8nFAi0APpQ7L6vxDbm5Xd1h_HtEU/s1600/Screen+Shot+2020-05-27+at+8.37.58+PM.png)

  

There are 2 errors that P0 reported earlier that Microsoft did not fix [11] [12]. 

And there is also a crash which, in my opinion, is quite similar to an error that P0 report earlier that Microsoft has fixed [13].

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhkkQL_CvsubBoAVrDlyBmU5Ojv-zMofHSOqAp7SwCxo3FAGfX5KtSEKGIADrf6H_N_t3NR9Li4-Fe1guTJablJvMlawU7Rl05cwMFHOwG48_6UfTXQhVhNyFHCgIYPd89isPawHLIl7A/s1600/Screen+Shot+2020-05-27+at+8.39.53+PM.png)

  

I report and Microsoft has accepted to fix this. It seems that this is a variant with a bug that Microsoft has fixed before. The bug was fixed in the T4/2020 patch (CVE-2020-0687), this is the root cause analysis of this error I wrote, everyone can read it [14], (In the article you should only pay attention to this error analysis, the impact is not written by me, of course, with errors like this, in fact, can not have a full exploit). 

  

According to the google timeline, the bug fix was fixed in August 2019, but I did fuzz it and the bug persisted until January 2020 (the moment I reported it to Microsoft).

  

I am not surprised that Microsoft has not completely fixed the bug, but this P0 public project has not been used by anyone to find bugs.

  

**Conclusion**

  

This bug is not hard to find, everything is available in front of you but no one jumped into it. You can see that the steps I showed are clearly presented in the previous article, all the basic knowledge that you do not have to use reverse much to write harness. Microsoft's documentation is very complete, please read it, learn it, and try it out. If I just stopped reading the blog then I think it will not bring much results.

  

Error when fuzz file format of windows appears less and less. Because this way is quite a lot of users, it requires you to spend a lot of time researching for new surface attacks, file formats that have not been studied in order to be able to spot bugs.

  

The following blog will talk about a file format bug that Microsoft rewarded me with max bounty in Windows Insider Preview Bounty. Maybe I'll publish it after Microsoft's T6/2020 patch is released or longer.

  

[1] <https://googleprojectzero.blogspot.com/>

[2] <https://portal.msrc.microsoft.com/en-us/security-guidance/acknowledgments>

[3] <https://docs.microsoft.com/en-us/>

[4] <https://github.com/microsoft/Windows-classic-samples>

[5] <https://googleprojectzero.blogspot.com/2016/06/a-year-of-windows-kernel-font-fuzzing-1_27.html>

[6] <https://googleprojectzero.blogspot.com/2016/07/a-year-of-windows-kernel-font-fuzzing-2.html>

[7] <https://docs.microsoft.com/en-us/windows/win32/api/fontsub/nf-fontsub-createfontpackage>

[8] <https://docs.microsoft.com/en-us/windows/win32/api/fontsub/nf-fontsub-mergefontpackage>

[9] <https://github.com/googleprojectzero/BrokenType/tree/master/ttf-fontsub-loader>

[10] <https://github.com/googleprojectzero/BrokenType/tree/master/ttf-otf-mutator>

[11] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1863>

[12] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1866>

[13] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1868>

[14] <https://blog.vincss.net/2020/04/cve44-microsoft-font-subsetting-dll-heap-corruption-in-ReadTableIntoStructure-cve-2020-0687.html>

  

\-------

  

**Vietnamese version**

  

Tiếp tục seri về fuzzing, phần này tôi sẽ chia sẻ cách tôi tìm kiếm attack surface trên windows để fuzz. Trên windows xử lý rất nhiều định dạng file, tìm hiểu và fuzz các định dạng file này là một hướng phổ biến để tìm được bug trên windows hiện nay. Cách tiếp cận và fuzz hoàn toàn giống như tìm lỗi ở Irfanview tôi đã trình bày ở phần trước.

  

Có lẽ sẽ có nhiều người tự nhủ làm thế nào mà có thể tìm được attack surface? Đơn giản sẽ như thế này khi bạn nghiên cứu một cái gì đó đủ lâu, đủ sâu bạn sẽ thấy được những hướng có thể tấn công vào nó. Nghe thì thật khó khi đặt tình huống này vào phần lớn người mới bắt đầu vì không phải ai cũng giỏi và xuất sắc như thế. Tuy nhiên có một điều thú vị ở đây là có rất nhiều nhà nghiên cứu giỏi họ sẵn sàng chia sẻ mọi thứ mà họ nghiên cứu cũng như bug họ tìm được cho cộng đồng. Google Project Zero (P0) [1] là một ví dụ, tôi xem và theo dõi các bug được public trên đó (kể cả những bug cách đây rất lâu). Từ đó tôi biết được các loại bug, các attack surface, các thành phần thường gây ra lỗi trên các nền tảng khác nhau,… Hoặc đơn giản hơn hàng tháng tôi vẫn theo dõi các bản vá từ Microsoft [2] và xem các bug được vá có gì thú vị và phù hợp với hướng fuzzing của tôi hay không.

  

**Introduction**

  

Quay trở lại nói về fuzz các định dạng file trên windows, như chúng ta biết trên windows có rất nhiều dll, mỗi dll sẽ có một nhiệm vụ riêng biệt. Đối với tôi, hiện tại tôi sẽ chỉ tập trung vào những DLL có nhiệm vụ xử lý các định dạng file. Một số định dạng file phổ biến như media: audio, video, ảnh,… hoặc một số định dạng file khác như XML, XPS, PDF, registry… Các DLL này sẽ export ra các API cho các developer sử dụng để xây dựng các ứng dụng trên windows, và các thành phần built in của Windows cũng sử dụng những API này.

  

Bản thân Microsoft đã cung cấp cho chúng ta MSDN [3], đó là một kho tài liệu để ta có thể đọc, tìm hiểu về cách sử dụng các API đó. Không những có document về API mà Microsoft còn hào phóng cho chúng ta rất nhiều code mẫu. Tôi thường tham khảo tại repo github của Microsoft [4]. Nó giúp chúng ta rất nhiều trong việc xây dựng harness để fuzz các định dạng file trên windows.

  

**Microsoft Font Subsetting**

  

Phông chữ của windows là một định dạng file tôi thấy rất đa dạng, từ usermode đếm kernelmode đều có thành phần xử lý phông chữ. P0 public rất nhiều bài nói về fuzzing phông chữ của windows [5] [6], những bài đó đều rất rõ ràng và chất lượng. Trong các lỗi liên quan đến phông chữ mà P0 tìm ra, tôi chú ý đến thư viện fontsub.dll.

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigFaoDkxWFXa0WhTC7gorgixLRP4dE66LvfMFCV_9TaSKtiNqCzMwFA-RUOU_ybiIbnsAfDYd0Xd8mS2O2jt9CivqX2bXu2loZdBohUMpvw-zHw62vf45yUTNPx10PWRe5EOoz_MbqCSY/s1600/Screen+Shot+2020-05-27+at+8.27.37+PM.png)

  

Tính tới thời điểm P0 public các lỗi của thư viện này thì trước đó chưa có ai thử fuzz vào thư viện fontsub.dll. 

  

Fontub.dll là một thư viện tạo, gom nhóm các phông chữ TTF, nó có thể chuyển đổi phông chữ thành các phiên bản nhỏ gọn hơn dựa trên các glyph và được sử dụng trong các file tài liệu như docx, ppt, pdf,… có phông chữ được nhúng. Nó cũng được Windows GDI và Direct2D sử dụng.

  

DLL export hai hàm API: CreateFontPackage [7] và MergeFontPackage [8].

  

unsigned long CreateFontPackage( const unsigned char *puchSrcBuffer, const unsigned long ulSrcBufferSize, unsigned char **ppuchFontPackageBuffer, unsigned long *pulFontPackageBufferSize, unsigned long *pulBytesWritten, const unsigned short usFlag, const unsigned short usTTCIndex, const unsigned short usSubsetFormat, const unsigned short usSubsetLanguage, const unsigned short usSubsetPlatform, const unsigned short usSubsetEncoding, const unsigned short *pusSubsetKeepList, const unsigned short usSubsetListCount, CFP_ALLOCPROC lpfnAllocate, CFP_REALLOCPROC lpfnReAllocate, CFP_FREEPROC lpfnFree, void *lpvReserved ); |  unsigned long MergeFontPackage( const unsigned char *puchMergeFontBuffer, const unsigned long ulMergeFontBufferSize, const unsigned char *puchFontPackageBuffer, const unsigned long ulFontPackageBufferSize, unsigned char **ppuchDestBuffer, unsigned long *pulDestBufferSize, unsigned long *pulBytesWritten, const unsigned short usMode, CFP_ALLOCPROC lpfnAllocate, CFP_REALLOCPROC lpfnReAllocate, CFP_FREEPROC lpfnFree, void *lpvReserved );  
---|---  
  
  

P0 cũng public cả harness mà họ xây dựng [9], nó rất tốt, cover được hết tất cả các tham số được truyền vào 2 hàm này. Tôi sử dụng harness đó để fuzz.

Ngoài harness, P0 còn public tool hỗ trợ mutate file TTF/OTF [10], đây là một tool tôi nghĩ nó là chìa khóa giúp P0 có thể tìm được nhiều lỗi với phông chữ như thế.

Dựa vào những thứ đó, tôi bắt đầu tìm và tạo copus:

1\. Corpus từ P0 public kèm các lỗi đã public từ trước + download trên internet

2. Mutate các corpus này dựa theo tool của P0

3. Dùng winafl-cmin để giảm số lượng corpus xuống

4. Kiểm tra coverage

5. Quay lại bước 2

Tôi làm công việc này lặp đi lặp lại đến khi coverage tôi đạt được với fontsub.dll như say:

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxrmW5efXDHHYdryxvQdRWYQMK_lJJlyiuNfqoRwuEh8ux-tvqM3U7Za8gF5_JytGP09GiKM82xpxXx9b5WGilYlb_151VCGyXyor6nF4oTSUTJ4spq61ChrsA3zgaX2XvxFOKSs4yAOA/s1600/Screen+Shot+2020-05-27+at+8.14.35+PM.png)

  

Với 1 testcase tôi mutate ra có thể đạt 53.22% trên DLL fontsub.dll, 81.08% đối với hàm CreateFontPackage và 76.40% đối với hàm MergeFontPackage. Tôi nghĩ thế này là đủ để có thể bắt đầu fuzz.

Tôi sử dụng winafl chạy với 1 master và 7 slave, sau một vài tiếng tôi bắt đầu thấy các crash đầu tiên. Sau một vài ngày tôi quay lại và bắt đầu kiểm tra các crash đó.

Phần lớn đều là lỗi stack overflow (0xc00000fd):

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiKmKwiDINIDl8Z-h0y0nBrKexok766apZn_QYAo04_XVi9WGgE6JdFsmEWGKyC5vcnb3idR9JGtIAWKbpLlWgaI6p5WKbYQTR70Y1gGRAd0snd-cUxH4YP1lJWGDl4XHAhwK7TVk9nNPI/s1600/Screen+Shot+2020-05-27+at+8.37.58+PM.png)

  

Xuất hiện 2 lỗi mà P0 report trước đó mà Microsoft không fix [11][12].

Và còn xuất hiện 1 crash mà theo tôi thấy thì khá giống với một lỗi mà P0 report trước đó mà Microsoft đã fix [13].

  

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtFk_k2YiEFG1cn2Tugu93njaJc95mIW2m2WLneZ5IY6IpWphtLO7cMjC4sg0NL4UPCL8_zItfQeWBzUefs10gy00KqKphLI1L6UZtIEkzbSj4_Ok4ZI8VcPpvLYxGmsI8PNn5hBkdMYs/s1600/Screen+Shot+2020-05-27+at+8.39.53+PM.png)

  

Tôi report và Microsoft đã chấp nhận sửa lỗi này. Có vẻ đây là một biến thể với lỗi mà Microsoft đã fix trước đó. Lỗi được sửa trong bản vá T4/2020 (CVE-2020-0687), đây là bài phân tích root cause của lỗi này tôi viết, mọi người có thể đọc thử [14] (trong bài viết bạn chỉ nên chú ý phần phân tích lỗi này, phần impact không phải do tôi tự viết, tất nhiên với những lỗi như thế này trong thực tế không thể có 1 full exploit).

Theo timeline google đưa ra bug này đã được fix vào tháng 8/2019, tuy nhiên tôi đã fuzz bản vá đó và lỗi đó vẫn tồn tại đến tận T1/2020 (thời điểm tôi report cho Microsoft).

Tôi không bất ngờ về việc Microsoft fix không hết bug, mà P0 public project này từ rất lâu rồi mà không hề có ai đó thử sử dụng để tìm bug.

**Conclusion**

Bug này không phải là khó tìm, mọi thứ đều ở sẵn trước mặt nhưng lại không có ai nhảy vào làm. Bạn có thể thấy các bước tôi làm đều trình bày rõ ở trong bài viết trước, đều là các kiến thức cơ bản bạn chưa phải sử dụng reverse nhiều để có thể viết được harness. Document của Microsoft rất đầy đủ, hãy chịu khó đọc, tìm hiểu và bắt tay vào làm thử. Nếu chỉ dừng lại ở việc đọc blog thì tôi nghĩ sẽ không mang lại nhiều kết quả.

Các lỗi khi fuzz định dạng file của windows xuất hiện càng ngày càng ít. Do cách này khá nhiều người sử dụng, đòi hỏi bạn phải bỏ nhiều thời gian để nghiên cứu tìm các attack surface mới, các định dạng file chưa ai nghiên cứu thì mới có thể ra được bug.

Blog sau tôi sẽ nói về bug của một định dạng file mà Microsoft đã thưởng cho tôi max bounty ở Windows Insider Preview Bounty. Có lẽ tôi sẽ public nó sau khi bản vá T6/2020 của Microsoft được release hoặc lâu hơn nữa.

  

[1] <https://googleprojectzero.blogspot.com/>

[2] <https://portal.msrc.microsoft.com/en-us/security-guidance/acknowledgments>

[3] <https://docs.microsoft.com/en-us/>

[4] <https://github.com/microsoft/Windows-classic-samples>

[5] <https://googleprojectzero.blogspot.com/2016/06/a-year-of-windows-kernel-font-fuzzing-1_27.html>

[6] <https://googleprojectzero.blogspot.com/2016/07/a-year-of-windows-kernel-font-fuzzing-2.html>

[7] <https://docs.microsoft.com/en-us/windows/win32/api/fontsub/nf-fontsub-createfontpackage>

[8] <https://docs.microsoft.com/en-us/windows/win32/api/fontsub/nf-fontsub-mergefontpackage>

[9] <https://github.com/googleprojectzero/BrokenType/tree/master/ttf-fontsub-loader>

[10] <https://github.com/googleprojectzero/BrokenType/tree/master/ttf-otf-mutator>

[11] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1863>

[12] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1866>

[13] <https://bugs.chromium.org/p/project-zero/issues/detail?id=1868>

[14] <https://blog.vincss.net/2020/04/cve44-microsoft-font-subsetting-dll-heap-corruption-in-ReadTableIntoStructure-cve-2020-0687.html>

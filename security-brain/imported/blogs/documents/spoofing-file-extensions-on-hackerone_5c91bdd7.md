---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-16_spoofing-file-extensions-on-hackerone.md
original_filename: 2018-11-16_spoofing-file-extensions-on-hackerone.md
title: Spoofing file extensions on HackerOne
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 5c91bdd74954f056d3edc6d6011e0f2b817b8f53980f85afab7917d3d0aff20d
text_sha256: 1842d2385737529294f60adfdb0b17ebb93e1886c03b6bb0764db0b5ab36495a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Spoofing file extensions on HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-16_spoofing-file-extensions-on-hackerone.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `5c91bdd74954f056d3edc6d6011e0f2b817b8f53980f85afab7917d3d0aff20d`
- Text SHA256: `1842d2385737529294f60adfdb0b17ebb93e1886c03b6bb0764db0b5ab36495a`


## Content

---
title: "Spoofing file extensions on HackerOne"
page_title: "Advance Programs and Tricks in Java: Spoofing file extensions on HackerOne"
url: "https://cooltrickshome.blogspot.com/2018/11/spoofing-file-extensions-on-hackerone.html"
final_url: "https://cooltrickshome.blogspot.com/2018/11/spoofing-file-extensions-on-hackerone.html"
authors: ["Anurag Jain (@csanuragjain)"]
programs: ["HackerOne"]
bugs: ["Unrestricted file upload"]
publication_date: "2018-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5585
---

While testing HackerOne, I observed an issue with the file upload functionality. It seems that on File upload, the uploader uses the content within the file for determining the content type of file instead of filetype .  
  
Although this does not pose much of a risk since the changed extensions would be visible at download time but wanted to blog about this.  
  
This raises below 2 scenario:  
  
**Scenario 1**  
  

  * Open any of your Hackerone report 
  * Upload the batch.cmd from <https://github.com/csanuragjain/roughProj/blob/master/batch.cmd?raw=true> in comment and post the comment

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8ahiYwmMCdVbhfw0i_-BJoRqK6U1Cy3rPf00rFh8OEZhI3DYoH0xpWyC677RQVS6c5cRXPkONmj2_u8aOADRq4zOXfZCZZ64awa4sd6ZGWLgwxpeQafbrOvfnwS8yO8PaqnaUgXI_A7zm/s640/S1_File_uploaded.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8ahiYwmMCdVbhfw0i_-BJoRqK6U1Cy3rPf00rFh8OEZhI3DYoH0xpWyC677RQVS6c5cRXPkONmj2_u8aOADRq4zOXfZCZZ64awa4sd6ZGWLgwxpeQafbrOvfnwS8yO8PaqnaUgXI_A7zm/s1600/S1_File_uploaded.png)

  

  * Open the batch.cmd on the posted comment
  * Observe an image gets represented and their is no warning from HackerOne

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLzqMk76ZWAJxKVO1u-FLIKM7PUhdK2hl-UpBk5ahlDSQ8ysRbzyqUSmocw-EZWjS806-EVvDU_C3e4-l8rXXXxG_ibJGGSFrEX4ldzoxhOqn8YBTGLBpuhBamX955U7kEHWCO04FE3rZJ/s640/S1_Image_shown_on_opening_cmd_with_no_warning.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLzqMk76ZWAJxKVO1u-FLIKM7PUhdK2hl-UpBk5ahlDSQ8ysRbzyqUSmocw-EZWjS806-EVvDU_C3e4-l8rXXXxG_ibJGGSFrEX4ldzoxhOqn8YBTGLBpuhBamX955U7kEHWCO04FE3rZJ/s1600/S1_Image_shown_on_opening_cmd_with_no_warning.png)

  

  * User downloads the file, thinking of it as an image file 
  * if the user accidentally ignores the downloaded file extensions opens it then malicious batch file gets executed

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyrwxXl_LToHrYC134ZEcl9lj5fnXoOXq0iKtuAQhONu59DLtFphcjPgY9mvv3VM0zfqMyR3_oqKORLREobxgUAuUv8aUFRAR45YdVcnjFMeRTXNLmk2NsQGhnLZMJs7KP5Xzm3PU22cot/s640/S1_On_opening_ran_system_commands_on_Safari.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyrwxXl_LToHrYC134ZEcl9lj5fnXoOXq0iKtuAQhONu59DLtFphcjPgY9mvv3VM0zfqMyR3_oqKORLREobxgUAuUv8aUFRAR45YdVcnjFMeRTXNLmk2NsQGhnLZMJs7KP5Xzm3PU22cot/s1600/S1_On_opening_ran_system_commands_on_Safari.png)

  

  
  
**Scenario 2**  
  

  * Open any of your Hackerone report
  * Upload the myFile.txt from <https://raw.githubusercontent.com/csanuragjain/roughProj/master/myFile.txt> in comment and post the comment

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdVO1yMX8lHS7tyWIeG4IZb_deA7j7R1GsMtCdcUDoIKLnZgvdayU9Bw-cNvnoF8YGl9ixBM1GO9FLTKVD4pyf9O5tIOtunmEs_4EScCsPGocFlWZxWF7P1r-Ogl6j8eW1YM1FY1bJVD-c/s640/S2_File_uploaded.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdVO1yMX8lHS7tyWIeG4IZb_deA7j7R1GsMtCdcUDoIKLnZgvdayU9Bw-cNvnoF8YGl9ixBM1GO9FLTKVD4pyf9O5tIOtunmEs_4EScCsPGocFlWZxWF7P1r-Ogl6j8eW1YM1FY1bJVD-c/s1600/S2_File_uploaded.png)

  

  * Open the myFile.txt on the posted comment
  * You will see a warning from Hackerone, but since the file is txt file so user might just go ahead 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-vR47Ok8JGx2o4m1bEFICfge9Xih82o8k6wMGE1Cv7RFb30FdGtRLtPqKyoKKwbYaA3cfYTEZchZHVPuztpzr4mwF9I5LbQOCwurvimNNMIXWsYEEUPs1QY9DwDkNWsQl7YK95rhTZ52-/s640/S2_warning_comes_but_since_its_txt_file_so_ignored.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-vR47Ok8JGx2o4m1bEFICfge9Xih82o8k6wMGE1Cv7RFb30FdGtRLtPqKyoKKwbYaA3cfYTEZchZHVPuztpzr4mwF9I5LbQOCwurvimNNMIXWsYEEUPs1QY9DwDkNWsQl7YK95rhTZ52-/s1600/S2_warning_comes_but_since_its_txt_file_so_ignored.png)

  

  * User downloads the file, thinking of it as an text file

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOaj0Cf0PKdwYj5cypzgbZjShqHvmW-wspRNATtmtgzeKf4gTZnrm_Qb1ozh2tiMqBLg37fMDAosNsuRLAKZ7oPHXWDZ8bUjNqpbAoIwrk6wy2PmSy5C8wfcEHBq0peuyGQ8upsE8xNWYj/s400/S2_Downloaded_as_html_file_instead_of_txt.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgOaj0Cf0PKdwYj5cypzgbZjShqHvmW-wspRNATtmtgzeKf4gTZnrm_Qb1ozh2tiMqBLg37fMDAosNsuRLAKZ7oPHXWDZ8bUjNqpbAoIwrk6wy2PmSy5C8wfcEHBq0peuyGQ8upsE8xNWYj/s1600/S2_Downloaded_as_html_file_instead_of_txt.png)

  

  * if the user accidentally ignores the downloaded file extensions opens it then malicious HTML scripts execute

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-0CTFeex8YMUI9GTHAXvH0-vqAdr4xck7oCOpfmM8L2159hTcf2T99ubkWmtEQpjcsWTMq9lBd6UUxa03ecr5R3icO7rcJwR9XzqrzpCo9b_hOrUsudG9IQWoIU_R-ov03xQzeW5pMKn9/s400/S2_malicious_script_on_opening_downloaded_txt.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-0CTFeex8YMUI9GTHAXvH0-vqAdr4xck7oCOpfmM8L2159hTcf2T99ubkWmtEQpjcsWTMq9lBd6UUxa03ecr5R3icO7rcJwR9XzqrzpCo9b_hOrUsudG9IQWoIU_R-ov03xQzeW5pMKn9/s1600/S2_malicious_script_on_opening_downloaded_txt.png)

  

  
**Reason:**  
  

  1. Content-Disposition: attachment; filename="" in response from hackerone-attachments.s3.amazonaws.com does not contain filename, forcing browser to decide the naming convention. 
  2. Since the Content type got decided on basis of file content header instead of extension by HackerOne so few browser would simply save it on user computer with incorrect extension, which caused the above Scenarios 1 and 2

**HackerOne Report:**

<https://hackerone.com/reports/268123> (Closed as Informative)

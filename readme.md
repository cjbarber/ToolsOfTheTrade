# Hacker News Tools of the Trade [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f3/media/badge.svg)](https://github.com/sindresorhus/awesome)

> Tools of The Trade, from [Hacker News](https://news.ycombinator.com).

##### Background

In 2010, Joshua Schachter, the founder of Delicious, [posted the following](https://news.ycombinator.com/item?id=1769910) on Hacker News:

> When I first started delicious, we had to host most of the services ourselves. CVS, mail, mailing lists, etc etc etc.
>
> These days, lots of that stuff is available as SaaS. What are the tools and services people use instead of hosting their own?
>
> (I'm not talking about actual production services like EC2 and Heroku and whatnot. We can go over this in another thread.)

In 2013, Sharjeel Qureshi, [posted the following](https://news.ycombinator.com/item?id=5235137):

> Few years ago, Joshua Schachter started this thread on HN for discussing hosted useful services: https://news.ycombinator.com/item?id=1769910
>
> The contribution in thread introduced many interesting SaaS services which can immensely help in deploying services as well as development.
>
> It's been three years since then. What do we have today?

Many thanks to the big contributors to the previous threads, including garrettdimon, espeed, netshade, and cmadan, and many more that I haven't named.

##### Now

I've collected more data from Hacker News, AngelList and Quora, to make the 2015 and beyond version. This list also includes self-hosted as well as hosted services.

It's on GitHub for a reason! Please submit pull requests.

## Supported with ❤️ by [Instabug](https://instabug.com/android/sdk?utm_source=toolsofthetrade&utm_medium=spon&utm_content=header)
### Understand How Your App is Doing with Real-Time Contextual Insights From Your Users
[![instabug-github](https://user-images.githubusercontent.com/10850625/65512691-fd45f280-ded9-11e9-8921-3528b98c30a7.png)](https://instabug.com/android/sdk?utm_source=toolsofthetrade&utm_medium=spon&utm_content=banner)
>Instabug helps Android developers easily collect bugs and feedback from beta testers and users to iterate faster and ship quality apps. Instabug automatically attaches screenshots, device details, network logs, repro steps, and tons of other critical insights needed to resolve issues and prioritize product backlogs.
> Mobile teams accelerate their workflows by seamlessly integrating with third-party tools like Github, Jira, Slack, Zendesk and much more. [Instabug is offering Tools of the Trade community an exclusive 15% discount on all paid plans. Get Started!](https://instabug.com/android/sdk/?utm_source=toolsofthetrade&utm_medium=spon&utm_content=get-started)
>[![](https://instabug-ga.appspot.com/UA-41982088-6/github/ToolsOfTheTrade?pixel)](https://instabug.com)

## Contents
* Business
  * Payments
    * [Payments, Billing & Downloads](#payments-billing--downloads)
    * [Accounting/Invoicing](#accountinginvoicing)
    * [Billing & Payment Processing](#billing--payment-processing)
    * [Payroll](#payroll)
  * Marketing
    * [Remote Collaboration](#remote-collaboration)
    * [Remote Workers](#remote-workers)
    * [SEO Tools](#seo-tools)
    * [Social Media Marketing](#social-media-marketing)
    * [Email Marketing](#email-marketing)
    * [Sources of Clicks/Ad Platforms](#sources-of-clicksad-platforms)
    * [Transactional Email](#transactional-email)
  * Productivity
    * [Group Communication/Chat Tools](#group-communicationchat-tools)
    * [Knowledge Tracking/Wiki](#knowledge-trackingwiki)
    * [Password Management](#password-management)
    * [Personal Productivity](#personal-productivity)
    * [Planning & Project Management](#planning--project-management)
    * [Time Tracking](#time-tracking)
  * For Founders
    * [Naming](#naming)
    * [Presentations / Slides](#presentations--slides)
    * [Privacy Policy, Terms & Conditions, Legal Documents](#privacy-policy-terms--conditions-legal-documents)
    * [Space Rental](#space-rental)
  * Business Tracking & Analytics
    * [Dashboards](#dashboards)
    * [Business & Traffic Analytics](#business--traffic-analytics)
    * [Income Analytics](#income-analytics)
  * Design
    * [Business Cards and Print Material](#business-cards-and-print-material)
    * [Content Creation/Infographics](#content-creationinfographics)
    * [Design Collaboration](#design-collaboration)
    * [Designers](#designers)
    * [Prototyping/Mockups](#prototypingmockups)
  * UX
    * [Conversion Optimization & A/B Testing](#conversion-optimization--ab-testing)
    * [User Feedback](#user-feedback)
    * [User Management](#user-management)
    * [User Testing](#user-testing)
    * [Customer Feedback](#customer-feedback)
    * [Forms / Surveys](#forms--surveys)
  * Others
    * [CRM/Sales Tools](#crmsales-tools)
    * [Customer Support/Help Desks](#customer-supporthelp-desks)
    * [Community Tools](#community-tools)
    * [HR](#hr)
    * [Phone/PBX/SMS](#phonepbxsms)
    * [Shipping](#shipping)

* Tech
  * Data
    * [Database-aaS](#database-aas)
    * [Database](#database)
  * Programming Productivity
    * [Documentation](#documentation)
    * [Notes](#notes)
  * API
    * [API Builder](#api-builder)
    * [Other APIs](#other-apis)
  * Testing & Monitoring
    * [Browser/Email Testing](#browseremail-testing)
    * [Load Testing](#load-testing)
    * [Server Monitoring](#server-monitoring)
    * [System Monitoring](#system-monitoring)
    * [Log Monitoring](#log-monitoring)
    * [Status Blogs/User Alerts](#status-blogsuser-alerts)
    * [Ops Alerts and Scheduling](#ops-alerts-and-scheduling)
  * As a Service
    * [Backend-aaS](#backend-aas)
    * [Database-aaS](#database-aas)
    * [PaaS](#paas)
    * [WebSockets-aaS](#websockets-aas)
  * DevSecOps
    * [App Developer Tools](#app-developer-tools)
    * [Application Performance](#application-performance)
    * [Continuous Integration/Code Quality](#continuous-integrationcode-quality)
    * [Feature Flags](#feature-flags)
    * [Ops Alerts and Scheduling](#ops-alerts-and-scheduling)
    * [Security](#security)
    * [Bug/Issue Tracking](#bugissue-tracking)
    * [Source Code Hosting](#source-code-hosting)
  * Simple
    * [Email Collection/Landing Page Apps](#email-collectionlanding-page-apps)
    * [Boilerplates](#boilerplates)
  * Hosting
    * [AWS Tools](#aws-tools)
    * [Heroku Tools](#heroku-tools)
    * [Video Hosting](#video-hosting)
    * [Source Code Hosting](#source-code-hosting)
  * Others
    * [Application Distribution](#application-distribution)
    * [Deployment](#deployment)
    * [DNS](#dns)
    * [Error/Exception Handling](#errorexception-handling)
    * [Geocoding](#geocoding)
    * [Identity Verification](#identity-verification)
    * [Localization & Internationalization](#localization--internationalization)
    * [Offsite Backups](#offsite-backups)
    * [Personal Machine Backups](#personal-machine-backups)
    * [Search](#search)
    * [Site Search](#site-search)
    * [Task Scheduling](#task-scheduling)
    * [VPS](#vps)

## Identity Verification

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Cognito](https://cognitohq.com) | [@getcognito](https://twitter.com/getcognito) | - | Identity verification and compliance checks (ID documents, screening, phone-based identity) for onboarding. `Hosted` |
| [Onfido](https://onfido.com) | [@Onfido](https://twitter.com/Onfido) | $2/verification | Individual ID verifications, Document Checks and Facial recognition. |

## Browser/Email Testing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [BrowserStack](https://www.browserstack.com) | [@browserstack](https://twitter.com/browserstack) | $29/mo - $199/mo | Live, web-based browser testing. |
| [Litmus](https://www.litmus.com) | [@litmusapp](https://twitter.com/litmusapp) | $79/mo - $159/mo | Preview and test email campaigns across email clients and devices. `Hosted` |
| [Sauce Labs](https://saucelabs.com) | [@saucelabs](https://twitter.com/saucelabs) | $19/mo - $298/mo | Cloud service for running web and mobile tests on real browsers and devices. `Hosted` |
| [EmailOnAcid](https://www.emailonacid.com) | [@emailonacid](https://twitter.com/EmailonAcid) | $44/mo - $260/mo | Test how emails render across email clients before sending. `Hosted` |
| [Rainforest QA](https://www.rainforestqa.com) | [@rainforestqa](https://twitter.com/rainforestqa) | $500/mo - $2000/mo | Crowd-sourced and automated end-to-end testing for web apps. `Hosted` |
| [DebugMail](https://debugmail.io) | - | Free | Easy to use fake mail (SMTP) server for developers. |
| [Mailosaur](https://mailosaur.com) | [@mailosaur](https://twitter.com/mailosaur) | $19/mo - $199/mo | Email, SMS and spam testing using virtual SMTP servers. `Hosted` |
| [Mailtrap](https://mailtrap.io) | [@Mailtrap](https://twitter.com/Mailtrap) | Free - $299.99/mo | A fake SMTP server for development and staging environments along with a REST API for testing. |
| [testmail.app](https://testmail.app) | [@testmailapp](https://twitter.com/testmailapp) | Free - $29/mo | Automate end-to-end email tests with unlimited mailboxes and a GraphQL API. |
| [Polypane](https://polypane.rocks) | [@polypane](https://twitter.com/polypane) | Free trial - $12+/mo | A browser built from the ground up to create and test websites and apps. |

## Bug/Issue Tracking

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Bitbucket](https://bitbucket.org) | [@bitbucket](https://twitter.com/bitbucket) | Free - $6/user/mo | Git repository hosting with pull requests and built-in CI pipelines, from Atlassian. `Hosted` |
| [BugHerd](https://bugherd.com) | [@bugherd](https://twitter.com/bugherd) | $29/mo - $180/mo | Collects visual feedback on websites and turns it into tasks on a board. `Hosted` |
| [GitHub](https://github.com) | [@GitHub](https://twitter.com/GitHub) | Free - $4/user/mo | Git hosting with pull requests, issues, Actions CI and code security. `Hosted` |
| [GitLab](https://about.gitlab.com) | [@gitlab](https://twitter.com/gitlab) | Free - $29/user/mo | Git hosting with issue tracking and CI/CD, on GitLab.com or self-managed. `Hosted` |
| [Jira](https://www.atlassian.com/software/jira) | [@JIRA](https://twitter.com/JIRA) | - | Issue and project tracking for software teams, from Atlassian. `Hosted` |
| [Lighthouse](https://lighthouseapp.com/) | [@lighthouseapp](https://twitter.com/lighthouseapp) | $25/mo - $100/mo | Whether you're a large company or a small bootstrapped team, Lighthouse is the perfect ticket tracking solution. Collaborate effortlessly on projects. Whether you’re a team of 5 or studio of 50, Lighthouse will help you keep track of your project development with ease. |
| [Sifter](https://sifterapp.com) | [@sifterapp](https://twitter.com/sifterapp) | $29/mo - $149/mo | Less configuring. More doing. We've put in the time researching bug tracking to help create the simplest possible workflow for you to get work done. From time-to-time we even blog about some of our ideas around this optimal bug tracking process… |
| [Usersnap](https://usersnap.com) | [@usersnap](https://twitter.com/usersnap) | $19/mo - $99/mo | Visual bug reports for web projects, with browser details attached to each report. `Hosted` |
| [Instabug](https://instabug.com) | [@instabug](https://twitter.com/instabug) | $49/mo - $349/mo | In-app bug reporting and feedback SDK for mobile apps. `Hosted` |

## Planning & Project Management

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Aha!](https://www.aha.io) | [@aha_io](https://twitter.com/aha_io) | $69/mo, Ask about startup plan | Product roadmap and strategy software for planning features and goals. `Hosted` |
| [Sprintly](https://sprint.ly) | [@sprintly](https://twitter.com/sprintly) | $49/mo- $399/mo | Don't ask how projects are going. Watch how they're going in real-time. Use our elegant interface to prioritize, tag, manage, estimate, and measure your software developers' progress in real-time. |
| [Podio](https://podio.com) | [@Podio](https://twitter.com/Podio) | Free | Low-code workspace for organising team work, projects and custom apps. `Hosted` |
| [Flow](https://www.getflow.com) | [@flowapp](https://twitter.com/flowapp) | $19/mo - $249/mo | Task and project management for teams, with recurring tasks and timelines. `Hosted` |
| [Basecamp](https://basecamp.com) | [@basecamp](https://twitter.com/basecamp) | $20/mo - $150/mo | Project management with to-dos, message boards and schedules for teams. `Hosted` |
| [Apollo](https://www.apollohq.com) | [@applicomhq](https://twitter.com/applicomhq) | $23/mo - $148/mo | Integrated Project and Contact Management Done Right Apollo is project and contact management done right. Using Apollo, you will realise that it's built to help you get things done, quickly and efficiently. With Apollo, you will always know where your projects, your contacts and your life are at and you will feel on top of everything, regardless of how hectic your schedule is. |
| [Asana](https://asana.com) | [@asana](https://twitter.com/asana) | $50/mo - $800/mo | Work management for planning projects, tracking tasks and coordinating teams. `Hosted` |
| [WeekPlan](https://weekplan.net) | [@weekplan](https://twitter.com/weekplan) | $7/mo - $19/mo | Time management inspired by the "7 habits of highly effective people" Features: goals of the week, week view and quadrant matrix, pomodoro timer, shared workspaces, etc... |
| [Trello](https://trello.com) | [@trello](https://twitter.com/trello) | Free - $5/user/mo | Kanban boards for organising tasks and projects, owned by Atlassian. `Hosted` |
| [Blossom](https://www.blossom.co) | [@blossom](https://twitter.com/blossom) | $19/mo - $149/mo | Agile Project Management. Blossom gives each member of the team clear overview about who’s doing what & why and at the same time it helps you to focus on what matters most. With Blossom you can efficiently manage your whole development process in one place, built with simplicity in mind. Blossom is based on the principles ofKanban, a way of working that emphasizes iterative delivery cycles and continuously improves the workflow of your team or organization. |
| [Redmine](https://www.redmine.org) | - | - | Flexible project management web application. Written using Ruby on Rails framework, it is cross-platform and cross-database. |
| [Tom's Planner](https://www.tomsplanner.com) | [@tomsplanner](https://twitter.com/tomsplanner) | $9/mo - $19/mo | Browser-based Gantt chart software for planning and sharing project schedules. `Hosted` |
| [Breeze](https://www.breeze.pm) | [@BreezeTeam](https://twitter.com/BreezeTeam) | $29/mo - $129/mo | Organize and track everything. Breeze shows you what's being worked on, who's working on what, where things are in the workflow and how much time it took. |
| [Cushion](https://cushionapp.com/) | [@cushionapp](https://twitter.com/cushionapp) | $8/mo - $48/mo | Piece of mind for freelancers. We built Cushion as a team of freelancers who always had trouble planning and managing our year, constantly taking on too much work and never thinking to take a break. |
| [ClickUp](https://clickup.com) | [@clickup_app](https://twitter.com/clickup_app) | Free - $7/user/mo | Project management with tasks, docs and goals in one workspace. `Hosted` |
| [Ora](https://ora.pm) | [@oratask](https://twitter.com/oratask) | $0 - $8/mo | Intuitive project management and team collaboration, Ora is your team’s command center! A place to track projects. Tasks. Time. Commits. Status Reports. Your entire product or business! |
| [Slate](https://heyslate.com/) | [@_heyslate](https://twitter.com/_heyslate) | $15/mo | Slate is a planning tool for freelance designers & developers who want to organise their schedule, projects and finances in one place. |

## Time Tracking

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Toggl Track](https://toggl.com/track/) | [@toggl](https://twitter.com/toggl) | Free - $20/user/mo | Time tracking for individuals and teams, with reports and integrations. `Hosted` |
| [Clockify](https://clockify.me) | [@clockify](https://twitter.com/clockify) | Free - $9/user/mo | Time tracking with timesheets, reports and team features. `Hosted` |
| [Hubstaff](https://hubstaff.com) | [@hubstaff](https://twitter.com/Hubstaff) | Free - $20/user/mo | Time tracking for remote teams, with timesheets, payroll and invoicing. `Hosted` |
| [Tickspot](https://www.tickspot.com/) | [@tickspot](https://twitter.com/tickspot) | Free - $149/mo | Time tracking and invoicing for client work, with Basecamp, Asana and Trello integrations. `Hosted` |
| [Kimai](https://www.kimai.org/) | [@kimai_org](https://twitter.com/kimai_org) | self-hosted | Kimai is a Free open source timetracker. It tracks work time and prints out a summary of your activities on demand. Yearly, monthly, daily, by customer, by project, by action, etc. |
| [OfficeClip](https://www.officeclip.com/web/timesheet) | @OfficeClip | Free - $12/user/mo| Time tracking software designed for small business. Free for unlimited user and unlimited time. Available as boh Hosted and Self-Hosted |

## App Developer Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [App Figures](https://appfigures.com) | [@appfigures](https://twitter.com/appfigures) | $9/mo | Sales and download tracking for iOS and Android app developers. `Hosted` |

## Localization & Internationalization

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Localize.js](https://localizejs.com) | - | $25/mo - $150/mo | Website translation with just a few lines of code. |
| [Gengo](https://gengo.com) | [@GengoIt](https://twitter.com/gengoit) | From $0.06/word | Human translation API. `Hosted` |

## Business & Traffic Analytics

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Amplitude](https://amplitude.com) | [@Amplitude_HQ](https://twitter.com/Amplitude_HQ) | Free - custom | Product analytics for web and mobile apps, with funnels, retention and experiments. `Hosted` |
| [Chartbeat](https://chartbeat.com) | [@chartbeat](https://twitter.com/chartbeat) | - | Real-time audience and traffic analytics for websites and publishers. `Hosted` |
| [Clicky](https://clicky.com) | [@clicky](https://twitter.com/clicky) | $9.99/mo - $19.99/mo | Real Time Web Analytics. Clicky lets you see every visitor and every action they take on your web site, with the option to attach custom data to visitors, such as usernames or email addresses. Analyze each visitor individually and see their full history. |
| [Fathom Analytics](https://usefathom.com/) | [@usefathom](https://twitter.com/usefathom) | $0-79/mo | Privacy-focused website analytics that does not track or store personal data. `Hosted` |
| [GoatCounter](https://www.goatcounter.com) | [@arp242_martin](https://twitter.com/arp242_martin) | Free for personal use or self hosted | Simple web statistics. No tracking of personal data. [Open source](https://github.com/zgoat/goatcounter) |
| [GoSquared](https://www.gosquared.com) | [@gosquared](https://twitter.com/GoSquared) | £21.60 - £396/mo | Easy to use real-time web analytics. |
| [Google Analytics](https://marketingplatform.google.com/about/analytics/) | [@GMktgPlatform](https://twitter.com/GMktgPlatform) | Free - custom (360) | Web and app analytics for measuring traffic and user behaviour. `Hosted` |
| [Heap](https://www.heap.io) | - | 0 - $599+ | Product analytics that captures web and iOS events automatically. Owned by Contentsquare. `Hosted` |
| [Improvely](https://www.improvely.com) | [@improvelycom](https://twitter.com/improvelycom) | $29 - $899/mo | Conversion tracking and click fraud monitoring platform. The easiest way to track the performance of marketing campaigns and monitor them for click fraud. |
| [Kissmetrics](https://www.kissmetrics.io) | [@kissmetrics](https://twitter.com/kissmetrics) | $150/mo - $500/mo | Customer analytics that ties activity to individual people across devices and sessions. `Hosted` |
| [Keen IO](https://keen.io) | [@keen_io](https://twitter.com/keen_io) | $0 - $2000+/mo | Custom analytics shouldn't be a pain in the backend. Keen IO's powerful APIs do the heavy lifting for you, so you can gather all the data you want and start getting the answers you need. |
| [Localytics](https://www.localytics.com) | [@localytics](https://twitter.com/localytics) | Free up to 10k MAUs, $200/mo - $2700/mo above that | Mobile app analytics and push and in-app messaging, owned by Upland Software. `Hosted` |
| [Matomo](https://matomo.org) | [@matomo_org](https://twitter.com/matomo_org) | Free self-hosted, paid cloud | Open source web analytics that can be self-hosted or run as a hosted service. `Self-hosted` |
| [Mixpanel](https://mixpanel.com) | [@mixpanel](https://twitter.com/mixpanel) | Free - custom | Product analytics that tracks user actions, funnels and retention in apps. `Hosted` |
| [Segment](https://segment.com) | [@segment](https://twitter.com/segment) | Free - custom | Customer data platform that collects events and routes them to analytics and marketing tools. Owned by Twilio. `Hosted` |
| [Snowplow](https://snowplowanalytics.com) | [@SnowPlowData](https://twitter.com/SnowPlowData) | - | Open source event data pipeline for collecting behavioural data from websites and apps. `Self-hosted` |
| [Inspectlet](https://inspectlet.com) | - | $0/mo - $499/mo | Session recordings and heatmaps for websites. `Hosted` |
| [Plausible](https://plausible.io) | - | Free self-hosted, from $9/mo hosted | Privacy-friendly website analytics, available hosted or self-hosted. `Self-hosted` |

## Conversion Optimization & A/B Testing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Optimizely](https://www.optimizely.com) | [@optimizely](https://twitter.com/optimizely) | $17/mo - $359/mo | Experimentation platform for A/B tests and feature experiments on websites and apps. `Hosted` |
| [VWO](https://vwo.com) | [@VWO](https://twitter.com/VWO) | $49/mo - $129/mo | A/B testing and personalisation for websites and landing pages. `Hosted` |
| [EyeQuant](https://www.eyequant.com) | [@eyequant](https://twitter.com/eyequant) | $199/mo - $999/mo | Predicts where visitors will look on a page design before it goes live. `Hosted` |

## Feature Flags

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [LaunchDarkly](https://launchdarkly.com) | [@LaunchDarkly](https://twitter.com/launchdarkly) | Free trial, then custom | Feature flag platform with user targeting, gradual rollouts and experimentation. `Hosted` |
| [Unleash](https://www.getunleash.io) | [@getunleash](https://twitter.com/getunleash) | Free self-hosted, from $80/mo cloud | Open source feature flag platform with gradual rollouts and user targeting. Can be self-hosted or used as a hosted service. `Self-hosted` |

## User Management

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Okta](https://www.okta.com) | [@OktaDev](https://twitter.com/OktaDev) | Free - custom | Identity and access management for sign-in, SSO and user management. `Hosted` |
| [Auth0](https://auth0.com) | [@auth0](https://twitter.com/auth0) | - | Hosted authentication and authorization service for web and mobile apps, owned by Okta. `Hosted` |
| [Connect2id](https://c2id.net) | [@Connect2id](https://twitter.com/connect2id) | €299/mo - €999/mo | Hosted Connect2id server, a flexible, secure and certified OpenID Connect/OAuth 2.0 identity provider. |
| [Cerbos Hub](https://www.cerbos.dev/product-cerbos-hub) | [@Cerbos](https://twitter.com/cerbosdev) | Free up to 100 monthly active principals | Console for writing, testing and deploying authorization policies for Cerbos. `Hosted` |


## User Testing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Hotjar](https://www.hotjar.com) | [@hotjar](https://twitter.com/hotjar) | Free - $32/mo+ | Heatmaps, session recordings and feedback polls for websites. `Hosted` |
| [Wisdom](https://getWisdom.io) | [@wisdomCRM](https://twitter.com/WisdomCRM) | Free - $2000+/mo | Session Replay. Wisdom is the most accurate live visitor session recorder service available. Focusing only on session replay, Wisdom reconstructs a virtual desktop screen for every visitor, across all tabs, to capture the true feel of every visitor's experience. |
| [LiveSession](https://livesession.io) | [@LiveSessionHQ](https://twitter.com/LiveSessionHQ) | $44+/mo | Session replay and funnel analytics for websites and web apps. `Hosted` |

## HR

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Workday](https://www.workday.com) | [@workday](https://twitter.com/workday) | - | Enterprise HR, payroll and finance software for large organisations. `Hosted` |
| [Lever](https://www.lever.co) | [@lever](https://twitter.com/lever) | - | Applicant tracking and recruiting software for hiring teams. `Hosted` |
| [Zenefits](https://www.zenefits.com) | [@zenefits](https://twitter.com/zenefits) | $8+/mo/employee | HR, payroll, benefits and compliance software for small and mid-sized employers. `Hosted` |
| [TestDome](https://www.testdome.com/) | [@TestDome](https://twitter.com/TestDome) | $8/candidate - $20/candidate | Automated testing of programming skills, ask candidates to write real code before calling them for an interview. |
| [HackerRank](https://www.hackerrank.com/) | [@hackerrank](https://twitter.com/hackerrank) | - | Technical skills assessments and recruiting platform for hiring engineers. `Hosted` |
| [PeopleDoc](https://www.people-doc.com/) | [@PeopleDoc_Inc](https://twitter.com/PeopleDoc_Inc) | - | HR Service delivery platform designed to simplify complex HR operations, compliance and can easily serve employees anytime, anywhere. |
| [BambooHR](https://www.bamboohr.com/) | [@bamboohr](https://twitter.com/bamboohr) | - | HR software for small and mid-sized companies, covering employee records, time off and onboarding. `Hosted` |

## Payroll

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Wagepoint](https://wagepoint.com) | [@wagepoint](https://twitter.com/wagepoint) | $20 + $2/mo/employee | Payroll, tax remittances and T4 filing for small businesses in Canada. `Hosted` |

## Continuous Integration/Code Quality

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Travis](https://travis-ci.com) | [@travisci](https://twitter.com/travisci) | Free - $489/mo | Hi I’m Travis CI, a hosted continuous integration service for open source and private projects: [travis-ci.com](https://travis-ci.com/) System status updates: [@traviscistatus](https://twitter.com/traviscistatus) |
| [AppVeyor](https://www.appveyor.com) | [@appveyor](https://twitter.com/appveyor) | - | AppVeyor automates building, testing and deployment of .NET applications, helping your team to focus on delivering great apps. |
| [CircleCI](https://circleci.com) | [@circleci](https://twitter.com/circleci) | Free - custom | Hosted CI/CD for building, testing and deploying code. `Hosted` |
| [Hound](https://houndci.com) | [@houndci](https://twitter.com/houndci) | Free, $49/mo - $249/mo | Automated Code Review. Take care of pesky code reviews with a trusty Hound |
| [Code Climate](https://codeclimate.com) | [@codeclimate](https://twitter.com/codeclimate) | $0/mo - $399/mo | Automated maintainability grades and static analysis for code quality. `Hosted` |
| [Codacy](https://www.codacy.com) | [@codacy](https://twitter.com/codacy) | Free - $15/user/mo | Automated code review and static analysis, with security scanning and coverage tracking. `Hosted` |
| [Codecov](https://codecov.io) | [@codecov](https://twitter.com/codecov) | $0 - $5/mo | Code coverage reports on pull requests, free for open source. `Hosted` |
| [Semaphore](https://semaphore.io) | [@semaphoreci](https://twitter.com/semaphoreci) | Free - usage-based | Hosted CI/CD pipelines for GitHub and other Git hosts, with self-hosted agents. `Hosted` |
| [Jenkins](https://jenkins.io) | [@jenkinsci](https://twitter.com/jenkinsci) | Free | Open source automation server for building, testing and deploying software. `Self-hosted` |
| [Bamboo](https://www.atlassian.com/software/bamboo) | [@atlassian](https://twitter.com/atlassian) | $10/mo - $1000/mo | Bamboo does more than just run builds and tests. It connects issues, commits, test results, and deploys so the whole picture is available to your entire product team, from project managers, to devs and testers, to sys admins. |
| [Buildkite](https://buildkite.com) | [@buildkite](https://twitter.com/buildkite) | Free - $30/user/mo | CI/CD pipelines that run on your own agents and infrastructure. `Self-hosted` |
| [Crucible](https://www.atlassian.com/software/crucible) | [@atlassian](https://twitter.com/atlassian) | $10/mo - $8000/mo | Code review system. Review code, discuss changes, share knowledge, and identify defects with Crucible's flexible review workflow. It's code review made easy for Git, Subversion, CVS, Perforce, and more. |
| [Coveralls](https://coveralls.io) | [@coverallsapp](https://twitter.com/coverallsapp) | $0/mo - $50/mo | Coveralls works with your continuous integration server to give you test coverage history and statistics. It integrates with any language and is Free for open source. |
| [Monkey Test It](https://monkeytest.it) | [@monkeytestit](https://twitter.com/monkeytestit) | $0/mo - $199/mo | Automated website checking tool to catch bugs on your website (broken links, missing images, JS errors, etc) before your users do. Integrates with Slack, most CI systems, webooks, and supports built-in scheduling. |
| [Concourse](https://concourse-ci.org) | [@concourseci](https://twitter.com/concourseci) | Free | Open source CI/CD system where pipelines are built from resources, tasks and jobs. `Self-hosted` |
| [PullRequest](https://www.pullrequest.com) | [@pullrequestinc](https://twitter.com/pullrequestinc) | $33+/10 min | Code review as a service by vetted, professional reviewers backed by static analysis  |
| [GitLab](https://about.gitlab.com/product/continuous-integration/) | [@GitLab](https://twitter.com/gitlab) | $0 [Community Edition](https://about.gitlab.com/pricing/) / Paid Premium | GitLab is an open-source version control platform with exquisite CI/CD integrations. |


## Dashboards

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Geckoboard](https://www.geckoboard.com) | [@geckoboard](https://twitter.com/geckoboard) | $17/mo - $899/mo | Hosted KPI dashboards that pull data from many services into one screen. `Hosted` |
| [TelemetryTV](https://www.telemetrytv.com) | [@telemetrytv](https://twitter.com/telemetrytv) | $9/mo - $749/mo | Dashboards for TVs, desktops and mobile, fed by a REST API. `Hosted` |
| [Klipfolio](https://www.klipfolio.com) | [@klipfolio](https://twitter.com/klipfolio) | $5/user/mo - $20/user/mo | Hosted business dashboards that combine data from many services and share them with a team. `Hosted` |
| [Grafana](https://grafana.com) | [@grafana](https://twitter.com/grafana) | $0 - $90/mo (+9/user/mo) | Open source dashboards and alerting for metrics, logs and traces. `Self-hosted` |
| [Redash](https://redash.io) | [@getredash](https://twitter.com/getredash) | Self-hosted or $49/mo - 450/mo | "Redash has support for querying multiple databases, including: Redshift, Google BigQuery, PostgreSQL, MySQL, Graphite, Presto, Google Spreadsheets, Cloudera Impala, Hive and custom scripts." |
| [Cyfe](https://www.cyfe.com) | [@cyfe](https://twitter.com/Cyfe) | $0 - $29/mo | Cyfe offers all-in-one web dashboards for your clients to help them monitor and analyze data scattered across all their online services like Google Analytics, Salesforce, AdSense, MailChimp, Amazon, Facebook, WordPress, Twitter and more from one single location in real-time. |
| [Two Minute Reports](https://twominutereports.com/) | - | Free - $9/mo | Two Minute Reports helps Marketing Agencies automate reports and save billable hours. It works with both Google Sheets and Looker Studio. It helps automate data from different sources like Facebook Ads, Google Ads, Instagram, LinkedIN Ads, HubSpot, Google Analytics 4, Shopify, Amazon Seller/Ads, etc. |

## Error/Exception Handling

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [CabinJS](https://cabinjs.com) | [@niftylettuce](https://twitter.com/niftylettuce) | Free and Open-Source | Cabin is a drop-in replacement and alternative JavaScript logging service to Sentry, Timber, Bugsnag, and more. It is security, privacy, and business cost-saving focused. Full support across all Node versions and IE 10+ support. |
| [CatchJS](https://catchjs.com) | - | $49 - $499 | JavaScript error reporting for web apps. Can take screenshots and collect click trails, so reproducing bugs becomes easy. |
| [Firebase Crashlytics](https://firebase.google.com/products/crashlytics) | [@crashlytics](https://twitter.com/crashlytics) | Free | Crash reporting for iOS, Android and Flutter apps, part of Firebase. `Hosted` |
| [Sentry](https://sentry.io/) | [@getsentry](https://twitter.com/getsentry) | Open Source & $24/mo - $199/mo | Error tracking and performance monitoring for applications. `Hosted` |
| [Honeybadger](https://www.honeybadger.io) | [@honeybadgerapp](https://twitter.com/honeybadgerapp) | $39/mo - $249/mo | Error tracking, uptime checks and performance monitoring for many languages. `Hosted` |
| [BugSnag](https://www.bugsnag.com) | [@bugsnag](https://twitter.com/bugsnag) | $29/mo - $249/mo | Automatic, full-stack error monitoring. Web app monitoring for Rails, PHP, Node.js, Java, and every other leading platform. |
| [Raygun](https://raygun.com) | [@raygunio](https://twitter.com/raygunio) | $14/mo - $199/mo | Hosted error and crash tracking that groups errors by root cause. `Hosted` |
| [Airbrake](https://airbrake.io) | [@airbrake](https://twitter.com/airbrake) | $49 - $249/mo | Hosted exception tracking for many languages and frameworks. `Hosted` |
| [Rollbar](https://rollbar.com) | [@rollbar](https://twitter.com/rollbar) | $12/mo - $1249/mo | Hosted error tracking with SDKs for Ruby, Python, PHP, Node.js, JavaScript, Android and iOS. `Hosted` |
| [Errbit](https://errbit.com) | - | OSS | The open source error catcher that's Airbrake API compliant. |

## Application Distribution

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Setapp](https://setapp.com) | [@setapp](https://twitter.com/setapp) | $9.99/mo | Setapp is a single subscription with a huge collection of quality apps for macOS. |

## Log Monitoring

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Fluentd](https://www.fluentd.org) | [@fluentd](https://twitter.com/fluentd) | - | Open source data collector that routes logs and events to storage and analytics tools. `Self-hosted` |
| [Graylog](https://www.graylog.org) | [@graylog2](https://twitter.com/graylog2) | - | Open source log management with search, dashboards and alerts. `Self-hosted` |
| [Mezmo](https://www.mezmo.com) | [@LogDNA](https://twitter.com/LogDNA) | free - $3/gb | Hosted log management and observability pipeline, formerly LogDNA. `Hosted` |
| [Logit.io](https://logit.io) | [@logit_io](https://twitter.com/logit_io) | from $74/mo | Logit.io provides log and metrics management built on hosted ELK, Open Distro & Grafana. |
| [Loggly](https://www.loggly.com) | [@loggly](https://twitter.com/loggly) | $49/mo - $349/mo | Hosted log management and search. `Hosted` |
| [Logstash](https://www.elastic.co/products/logstash) | [@logstash](https://twitter.com/logstash) | - | Open source pipeline that ingests, parses and forwards logs and events to Elasticsearch and other outputs. `Self-hosted` |
| [Papertrail](https://papertrailapp.com) | [@papertrailapp](https://twitter.com/papertrailapp) | $7/mo - $230/mo | Hosted log search, live tail and alerts for servers and apps. `Hosted` |
| [statsd](https://github.com/statsd/statsd) | - | Free, open source | Network daemon that collects metrics over UDP or TCP and forwards them to backends such as Graphite. `Self-hosted` |
| [Sumo Logic](https://www.sumologic.com) | [@SumoLogic](https://twitter.com/SumoLogic) | - | Hosted log management and analytics platform. `Hosted` |

## Application Performance

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [AppNeta](https://www.appneta.com) | [@AppNeta](https://twitter.com/AppNeta) | Free to $119 / mo | Full-stack application monitoring for web apps. Get visibility into code, network, and end user, especially for polyglot and service-oriented applications, by looking at transactions, errors, browser metrics, host metrics, and more. |
| [New Relic](https://newrelic.com) | [@NewRelic](https://twitter.com/NewRelic) | Free tier, then usage-based | Hosted observability platform for application performance, infrastructure and logs. `Hosted` |
| [AppSignal](https://appsignal.com) | [@AppSignal](https://twitter.com/AppSignal) | $49/mo - $259/mo | Hosted application performance monitoring and error tracking for Ruby, Elixir and Node.js. `Hosted` |
| [Instrumental](https://instrumentalapp.com) | [@instrumental](https://twitter.com/instrumental) | $150/mo - $750/mo | Monitor Your App in Realtime. Instrumental’s made to monitor metrics at a ridiculously high scale. At rates of 500,000 metrics per second and higher, it doesn’t even break a sweat |
| [Atatus](https://www.atatus.com) | [@atatusapp](https://twitter.com/atatusapp) | $12/mo - $159/mo | Simple JavaScript Error Tracking. Atatus is a simple error tracking and uptime monitoring system. Add two lines of code and get alerted on any errors that occurs in your application in realtime. |
| [Scout APM](https://www.scoutapm.com) | [@ScoutAPM](https://twitter.com/ScoutAPM) | - | Application monitoring with errors, logs and traces for Ruby, Python, Node.js, PHP and Elixir apps. `Hosted` |

## Load Testing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Bees with Machine Guns!](https://github.com/newsapps/beeswithmachineguns) | - | - | - |
| [Flood.io](https://flood.io) | [@flood_io](https://twitter.com/flood_io) | Free to $399/mo | Auto setup and results summaries/graphs of JMeter and Gatling load tests. Can easily scale to 100K+ reqs/min. |
| [Neustar Website Load Testing](https://www.security.neustar/digital-performance/web-performance-management) | [@Neustar](https://twitter.com/Neustar) | $80/mo | Tackle performance problems such as bandwidth limitations, error rates exceeding thresholds, server PU limitations and much more. |
| [Loader.io](https://loader.io) | [@loaderio](https://twitter.com/loaderio) | Free to 100.00$/mo | Loader.io is a Free load testing service that allows you to stress test your web-apps/apis with thousands of concurrent connections. |
| [Locust.io](https://locust.io) | [@locustio](https://twitter.com/locustio) | Open Source | Self-hosted load testing tool written in Python, with the tests themselves written in Python code |
| [k6](https://k6.io) | [@k6_io](https://twitter.com/k6_io) | Free, Open Source | Open source load testing tool with tests written in JavaScript. `Self-hosted` |
| [Grafana Cloud k6](https://grafana.com/products/cloud/k6/) | [@k6_io](https://twitter.com/k6_io) | Free tier, then usage-based | Hosted load testing built on the open source k6 project (formerly Load Impact). `Hosted` |

## Server Monitoring

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Datadog](https://www.datadoghq.com) | [@datadoghq](https://twitter.com/datadoghq) | $0/mo - $15/host/mo | Hosted monitoring for infrastructure, applications and logs. `Hosted` |
| [Circonus](https://www.circonus.com) | [@circonus](https://twitter.com/circonus) | $15/host/mo - $25/host/mo | Circonus combines multiple monitoring, alerting, event reporting, and analytical tools into one unified solution. Use any data, in any application, from any system, and visualize it in real-time. |
| [Prometheus](https://prometheus.io) | [@PrometheusIO](https://twitter.com/PrometheusIO) | Free | Open source monitoring system and time series database. `Self-hosted` |
| [Site24x7](https://www.site24x7.com) | [@site24x7](https://twitter.com/Site24x7) | $9/mo starter - $225/enterprise | Website, server and application monitoring. `Hosted` |
| [Uptime Robot](https://uptimerobot.com) | [@uptimerobot](https://twitter.com/uptimerobot) | - | Free basic HTTP/HTTPS website monitoring |
| [BinaryCanary](https://www.binarycanary.com) | - | - | - |

## Customer Support/Help Desks

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Help Scout](https://www.helpscout.com/) | [@helpscout](https://twitter.com/helpscout) | $15/mo | Shared inbox and help desk for customer email, with a knowledge base. `Hosted` |
| [Zendesk](https://www.zendesk.com) | [@zendesk](https://twitter.com/zendesk) | $1/mo - $195/mo | Hosted help desk for email, chat and phone support. `Hosted` |
| [Groove](https://www.groovehq.com) | [@groove](https://twitter.com/groove) | $15/mo | Everything you need to deliver awesome, personal support to every customer. Your customers will never know that you’re using a helpdesk. To them, your messages look like regular emails. It feels like personal support, and it helps you build deeper relationships with your customers. |
| [Intercom](https://www.intercom.com) | [@intercom](https://twitter.com/intercom) | $49/mo - $449/mo | Hosted customer messaging with live chat, help center and support inbox. `Hosted` |
| [Tender](https://tenderapp.com/) | [@tenderapp](https://twitter.com/tenderapp) | $9/mo - $99/mo | Better, Simpler, Customer Support Software. Support your customers in the open! With public forums, you can offer a public space to your users to discuss common issues and get feedback, while still keeping certain categories private (billing, orders, ...). Power users can subscribe to categories and new discussions, and help out other customers. |
| [Enchant](https://www.enchant.com) | [@enchant](https://twitter.com/enchant) | $9/mo | It's like gmail on steroids! Enchant is a powerful helpdesk that helps your team deliver awesome support to each and every customer. To your customers, it's just email. They will never see a ticket number and will never have to log into anything! |
| [Freshdesk](https://freshdesk.com) | [@freshdesk](https://twitter.com/freshdesk) | $16/mo - $70/mo | Hosted help desk for ticket-based customer support, part of Freshworks. `Hosted` |
| [UserDeck](https://userdeck.com) | [@user_deck](https://twitter.com/user_deck) | $0 - $25/mo | Customer support software that embeds into your existing website. |
| [Sirportly](https://sirportly.com) | [@sirportly](https://twitter.com/sirportly) | £0 - £15/mo | Grow your business and provide world class customer support. Simply setup your helpdesk in less than a few minutes. Integrate with your other software tools and take advantage of the automated rules and macros to scale your customer support to a new level, become more professional and customer focused and turn your customers into raving fans with Sirportly. |
| [Olark](https://www.olark.com/) | [@olark](https://twitter.com/olark) | - | - |
| [SnapEngage](https://snapengage.com/) | [@snapengage](https://twitter.com/snapengage) | Custom pricing per integration, or from $81/month | Highly customised live chat integrations |
| [Reamaze](https://www.reamaze.com) | [@reamaze](https://twitter.com/reamaze) | $15/mo | Hosted help desk with email, chat and social channels. `Hosted` |
| [Jitbit Helpdesk](https://www.jitbit.com/helpdesk/) | [@jitbithelpdesk](https://twitter.com/jitbithelpdesk) | $29/mo - $199/mo | A help desk app that actually makes your work easier, not harder. Comes in both hosted and on-premise versions. Very well designed and easy to use. Has all the must-have features and doesn't get in your way. |
| [Drift](https://www.drift.com) | [@drift](https://twitter.com/drift) |Paid from $49/mo | Stop wasting your website traffic. Sales-oriented live chat and in-app messaging, with chatbot automation. |
| [Zammad](https://zammad.com/) | [@zammadhq](https://twitter.com/zammadhq) | $0/mo - $24/mo | Open source help desk for email, phone, chat and social channels. `Self-hosted` |
| [Support Hero](https://www.supporthero.io) | [@supportheroapp](https://twitter.com/supportheroapp) | $49/mo - $199/mo | Knowledge base and tutorial management platform with smart analytics. Support Hero is a self-service knowledge base that helps companies educate their clients. Helping them to create and deliver a game-changing user education experience that increases retention and engagement, while reducing customer relationship costs. |
| [Atlasmic](https://atlasmic.com) | [@atlasmichq](https://twitter.com/atlasmichq) | Free - €20/mo | Live chat, business messenger, sales, inbound marketing and analytics. `Hosted` |

## Transactional Email

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Postmark](https://postmarkapp.com) | [@postmarkapp](https://twitter.com/postmarkapp) | $1.50 | Hosted transactional email API for application emails. `Hosted` |
| [Mailgun](https://www.mailgun.com) | [@Mail_Gun](https://twitter.com/Mail_Gun) | $20.00 | Hosted email sending API for developers, with SMTP and HTTP interfaces. `Hosted` |
| [Amazon Simple Email Service](https://aws.amazon.com/ses/) | [@AWSSupport](https://twitter.com/AWSSupport) | $0.10 per 1,000 emails | Hosted email sending and receiving API from AWS. `Hosted` |
| [SendGrid](https://sendgrid.com) | [@SendGrid](https://twitter.com/SendGrid) | $9.95/mo - $399.95 | Hosted email API for transactional and marketing email, owned by Twilio. `Hosted` |
| [CritSend](https://www.critsend.com) | [@critsend](https://twitter.com/critsend) | $50/mo - $3000/mo | The Best SMTP Relay for Developers. Use the most reliable infrastructure for your transactional and bulk emails. It only takes 5 minutes to setup Critsend and start enjoying fast delivery time and automatic scalability. |
| [Postage](https://postageapp.com) | [@postagebird](https://twitter.com/postagebird) | $9/mo - $399/mo | The easier way to send email from web apps. Postage app helps design, send, and analyze emails within minutes. |
| [Dyspatch](https://www.dyspatch.io) | [@sendwithus](https://twitter.com/send_with_us) | - | Hosted email template and transactional email platform, formerly Sendwithus. `Hosted` |
| [SparkPost](https://sparkpost.com) | [@SparkPost](https://twitter.com/SparkPost) | Free - $474/mo | Hosted email delivery API for transactional and bulk email. `Hosted` |

## Other APIs

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Exchange Rate API](https://www.exchangerate-api.com) | - | Free | A simple API for fetching currency exchange rates maintained since 2010. Free tier with no signup or request limits. |
| [Filestack](https://www.filestack.com) | [@FileStack](https://twitter.com/FileStack) | $0/mo - $49/mo | Hosted file upload, storage and processing API. `Hosted` |
| [Open Exchange Rates](https://openexchangerates.org) | - | $12/mo - $97/mo | Hosted JSON API for currency exchange rates. `Hosted` |
| [FormAPI](https://formapi.io) | [@form_api](https://twitter.com/form_api) | $49/mo - $249/mo | Hosted API that fills PDF templates with data. `Hosted` |
| [Abstract APIs](https://www.abstractapi.com) | [@abstractapi](https://twitter.com/abstractapi) | Free - $249/mo | Suite of APIs for everyday needs (email validation, VAT calculation, IP geolocation, and more). |

## Site Search

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Elasticsearch](https://www.elastic.co/products/elasticsearch) | [@elastic](https://twitter.com/elastic) | - | Distributed search and analytics engine built on Apache Lucene. `Self-hosted` |
| [Algolia](https://www.algolia.com) | [@Algolia](https://twitter.com/Algolia) | $49/mo - $449/mo | Hosted search API for websites and apps. `Hosted` |
| [Apache Solr](https://lucene.apache.org/solr/) | - | - | An open source search platform, based and co-released with Apache Lucene. |

## Email Marketing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [QuickChart](https://quickchart.io/) | | Open source, self-hosted. Free hosted tier, paid from $40/mo | Add chart and graph images to your emails. Supports Chart.js and Google Image Charts formats. |
| [MailCharts](https://www.mailcharts.com) | [@mailcharts](https://twitter.com/mailcharts) | $30/mo | Track & understand how your competitors use email marketing. MailCharts tracks over a thousand companies, bringing you actionable insights to help you improve your email marketing strategy, make data-driven decisions and gain design and content inspiration. |
| [Customer.io](https://customer.io) | [@CustomerIO](https://twitter.com/CustomerIO) | $50/mo - $1250/mo | Hosted messaging for email, SMS and push, triggered by user behavior. `Hosted` |
| [Vero](https://www.getvero.com) | [@getvero](https://twitter.com/getvero) | $99/mo | Send emails based on what your customers do. Vero makes it easy to create segments of customers based on the attributes you capture (e.g. age, location, gender) and the actions your customers take (e.g. logged in, used feature x, checked out, etc.). |
| [Mailchimp](https://mailchimp.com) | [@Mailchimp](https://twitter.com/Mailchimp) | Free tier, then paid plans | Hosted email marketing and automation, owned by Intuit. `Hosted` |
| [Campaign Monitor](https://www.campaignmonitor.com) | [@CampaignMonitor](https://twitter.com/CampaignMonitor) | $9/mo - $699/mo | Hosted email marketing for newsletters and automated campaigns. `Hosted` |
| [Sendy](https://sendy.co) | [@getsendy](https://twitter.com/getSendy) | $59 one time fee | Self-hosted newsletter app that sends through Amazon SES. `Self-hosted` |
| [Image-Charts](https://www.image-charts.com/) | [@imagecharts](https://twitter.com/imagecharts) | Free - $49/mo, self-hosted plan available | Include animated charts as image into emails, no server-side rendering, 1 URL = 1 chart, compatible with Google Image Charts. |
| [Drip](https://www.drip.com) | [@getdrip](https://twitter.com/getdrip) | Paid plans from $49/mo | Hosted email marketing automation with workflows and drip campaigns. `Hosted` |
| [MailerLite](https://www.mailerlite.com) | [@mailerlite](https://twitter.com/mailerlite) | Free - $140/mo | Hosted email newsletters and automation with a free plan. `Hosted` |
| [EmailOctopus](https://emailoctopus.com) | [@emailoctopus](https://twitter.com/emailoctopus) | Free up to 2,500 subscribers, paid plans from $19/mo | Low cost email marketing using Amazon SES. |
| [Buttondown](https://buttondown.email/) | [@buttondownemail](https://twitter.com/buttondownemail) | Free tier, then paid | Hosted newsletter service that uses Markdown for writing. `Hosted` |

## Email Collection/Landing Page Apps

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Launchrock](https://www.launchrock.com) | [@launchrock](https://twitter.com/launchrock) | $49/mo - $199/mo | Even if you know how to code a web page with HTML, you'll love how much faster it is with our landing page builder. Load up your logo and graphic assets, set up a few base colors from your brand palette and publish away. |
| [Unbounce](https://unbounce.com) | [@unbounce](https://twitter.com/unbounce) | $49/mo - $199/mo | Hosted landing page builder for marketing campaigns. `Hosted` |
| [Leadpages](https://www.leadpages.com) | [@Leadpages](https://twitter.com/Leadpages) | $25/mo - $199/mo | Hosted landing page builder with lead capture tools. `Hosted` |
| [Instapage](https://instapage.com/) | [@Instapage](https://twitter.com/Instapage) | $29/mo - $127/mo | Hosted landing page builder with A/B testing for ad campaigns. `Hosted` |
| [KickoffLabs](https://kickofflabs.com) | [@kickofflabs](https://twitter.com/kickofflabs) | $29/mo - $99/mo | Stop building landing pages. Start building smarter campaigns. Send customers to a tailored page that speaks to them. Keep them engaged with signup-forms, newsletters and, best of all, a very cool, unique REWARD system for customer referrals. |
| [Prefinery](https://www.prefinery.com) | [@prefinery](https://twitter.com/prefinery) | $19/mo- $399/mo | Stress-Free Beta Invitation and Management. Prefinery is beta invitations & management for serious product launches. You need more than just a landing page -- outsource your beta to Prefinery! |

## CRM/Sales Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Salesforce](https://www.salesforce.com) | [@salesforce](https://twitter.com/salesforce) | - | Cloud CRM and software for sales, service, marketing and commerce. `Hosted` |
| [SugarCRM](https://www.sugarcrm.com) | [@sugarcrm](https://twitter.com/sugarcrm) | - | CRM software for sales, marketing and customer support. `Hosted` |
| [Insightly](https://www.insightly.com) | [@insightly](https://twitter.com/insightly) | $7/mo | CRM for small businesses to manage contacts, organizations, projects and opportunities. `Hosted` |
| [Close](https://close.com) | [@closeio](https://twitter.com/closeio) | - | Sales CRM with built-in calling, email and SMS. `Hosted` |
| [Streak](https://www.streak.com) | [@streak](https://twitter.com/streak) | - | CRM and pipelines inside Gmail. `Hosted` |
| [Pipedrive](https://www.pipedrive.com) | [@pipedrive](https://twitter.com/pipedrive) | - | Sales pipeline CRM for tracking deals and activities. `Hosted` |

## Social Media Marketing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Buffer](https://buffer.com) | [@buffer](https://twitter.com/buffer) | Free - $5/channel/mo | Schedules and publishes posts to social media accounts. `Hosted` |
| [HootSuite](https://hootsuite.com) | [@HootSuite](https://twitter.com/HootSuite) | $99/mo - $399/mo | Social media scheduling, monitoring and analytics for teams. `Hosted` |
| [Exacttarget Marketing Cloud/Buddy Media](https://www.salesforce.com/products/marketing-cloud/overview/) | [@marketingcloud](https://twitter.com/marketingcloud) | - | Bringing you closer to your social customers with an integrated social content solution. Run integrated campaigns across Facebook, Twitter, YouTube and your websites Increase fans, followers and advocates. Publish engaging and interactive social apps. Easily create landing pages and microsites and extend social to your websites. Understand engagement trends, demographics, conversions and business metrics with powerful analytics. |
| [Sprout Social](https://sproutsocial.com) | [@sproutsocial](https://twitter.com/sproutsocial) | - | Social media publishing, engagement and analytics for teams. `Hosted` |
| [F5Bot](https://f5bot.com) | - | Free | F5Bot is Free social media keyword monitoring. F5Bot will send you an email when your startup, your product, or your competitors are mentioned on Hacker News or Reddit. |
| [Syften](https://syften.com) | [@syften_com](https://twitter.com/syften_com) | $29.95/mo - $119.95/mo | Monitors Reddit, Hacker News and forums for keywords and sends alerts. `Hosted` |

## Naming

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Trademarkia](https://www.trademarkia.com) | [@trademarkia](https://twitter.com/trademarkia) | - | Trademark search database and filing service. `Hosted` |
| [NameRobot](https://www.namerobot.com) | [@namerobotEN](https://twitter.com/namerobotEN) | 0$ - 300$/mo | Find, create and check the name for your project. NameRobot offers everything you need to create suitable naming ideas in a short time. |
| [DomainTools Whois Lookup](https://whois.domaintools.com/) | [@DomainTools](https://twitter.com/DomainTools) | Free - $99/mo | Whois and domain ownership lookup with history and related records. `Hosted` |
| [Startup Name Check](https://startupnamecheck.com/) | - | Free | Name validator tool for dozens of domain-names and social media networks. |
| [Word Safety](https://naming-tools.com/word-safety) | - | Free | Word Safety tool to check for second meanings in other languages or other forms of writing. |

## Space Rental

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [LiquidSpace](https://liquidspace.com) | [@LiquidSpace](https://twitter.com/LiquidSpace) | - | Marketplace for booking desks, meeting rooms and offices in coworking spaces. `Hosted` |

## Community Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Discourse](https://www.discourse.org) | [@discourse](https://twitter.com/discourse) | - | Open source forum and discussion software. `Self-hosted` |
| [Scoold](https://scoold.com) | [@getscoold](https://twitter.com/getscoold) | Free / Pro €299 | Stack Overflow in a JAR. An enterprise-ready Q&A platform with full-text search, SAML, LDAP integration and social login support. |
| [Flarum](https://flarum.org) | [@flarum](https://twitter.com/flarum) | Free | Well designed forum software. |

## Personal Productivity

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [RescueTime](https://www.rescuetime.com) | [@rescuetime](https://twitter.com/rescuetime) | Free - $9/mo | RescueTime gives you an accurate picture of how you spend your time to help you become more productive every day. |
| [Qbserve](https://qotoqot.com/qbserve/) | [@Qbserve](https://twitter.com/Qbserve) | $40 one-time | Qbserve is a time tracker for Mac that does whatever RescueTime can but also tracks project time automatically, generates invoices, and stores tracked data locally. |
| [Timing](https://timingapp.com) | [@TimingApp](https://twitter.com/TimingApp) | $10/mo - $168/yr | Automatic time tracking for Mac that builds timesheets from app and website activity. |
| [fman](https://fman.io) | [@m_herrmann](https://twitter.com/m_herrmann) | $14.00 | Manage and transfer your files with ease. For Windows, Mac and Linux. |
| [WakaTime](https://wakatime.com) | [@WakaTime](https://twitter.com/WakaTime) | Free - $9/mo | Automatic productivity metrics using text editor plugins. Goals, leaderboards, GitHub integration, automatic project/language/branch detection. |
| [deprocrastination](https://www.deprocrastination.co) | [@deprocrastinate](https://twitter.com/deprocrastinate) | Free - $3.99/mo | Browser extension to train yourself to procrastinate less. |


## Prototyping/Mockups

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Creately](https://creately.com) | [@creately](https://twitter.com/creately) | Free - $750/mo | Web-based diagramming tool with real-time collaboration. `Hosted` |
| [Keynote](https://www.apple.com/keynote/) | - | Free | Presentation app for Mac, iPad, iPhone and iCloud. `Hosted` |
| [OmniGraffle](https://www.omnigroup.com/omnigraffle) | [@omniGraffle](https://twitter.com/omniGraffle) | $99.99 | Mac diagramming app for flowcharts, org charts and layouts. |
| [moqups](https://moqups.com) | [@moqups](https://twitter.com/moqups) | $9/mo - $39/mo | Browser-based tool for wireframes, diagrams and interactive prototypes. `Hosted` |
| [Balsamiq](https://balsamiq.com) | [@balsamiq](https://twitter.com/balsamiq) | $16/editor/mo - $35/editor/mo | Wireframing tool for quick, sketch-style mockups. `Hosted` |
| [Proto.io](https://proto.io) | [@protoio](https://twitter.com/protoio) | $24/mo - $199/mo | Browser-based prototyping tool for interactive mobile app prototypes. `Hosted` |
| [Sketch](https://www.sketch.com) | [@sketchapp](https://twitter.com/sketchapp) | $12/editor/mo - $44/editor/mo | Mac design tool for interface design and prototyping. |
| [Figma](https://www.figma.com) | [@figmadesign](https://twitter.com/figmadesign) | Free - $16/editor/mo | Browser-based design and prototyping tool with real-time collaboration. `Hosted` |
| [Anima](https://www.animaapp.com) | [@animaapp](https://twitter.com/animaapp) | $0 - $39/mo | Converts Figma, Sketch and Adobe XD designs into HTML, CSS and React code. `Hosted` |
| [Framer](https://www.framer.com) | [@framer](https://twitter.com/framer) | Free - $30/mo | Design tool for building responsive websites and interactive prototypes. `Hosted` |
| [UXPin](https://www.uxpin.com/) | [@uxpin](https://twitter.com/uxpin) | $0 - $23+/mo | The full-stack UX design platform: design systems, prototyping, and documentation in one place. |

## Content Creation/Infographics

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [AudienceOps](https://audienceops.com) | [@AudienceOps](https://twitter.com/AudienceOps) | $850/mo - $1700/mo | AudienceOps handles your entire content strategy so you can focus on your product. |
| [Visual.ly](https://visual.ly) | [@Visually](https://twitter.com/Visually) | $195/mo - $994/mo | ORIGINAL VISUAL CONTENT FOR BRANDS. We only work with the best creative talent available. Thousands of designers, journalists, animators and developers are standing by to help you achieve your goals and take your project to the next level. |
| [Canva](https://www.canva.com) | [@canva](https://twitter.com/canva) | Free - $144/yr | Browser-based design tool for social graphics, presentations and documents, with templates. `Hosted` |

## Customer Feedback

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [PickFu](https://www.pickfu.com) | [@pickfu](https://twitter.com/pickfu) | $50/mo - $299/mo | Paid polling of consumers on design, copy and product choices. `Hosted` |
| [Raaft.io](https://www.raaft.io/) | [@RaaftRetain](https://twitter.com/RaaftRetain) | $79/mo - $229/mo| Instantly get feedback from every canceling customer. Make retention offers to reduce churn. |
| [ProsperStack](https://prosperstack.com/) | [@prosperstack](https://twitter.com/prosperstack) | Free - $149+| Collect cancellation feedback from customers and prevent churn automatically. |

## Database

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Citus](https://www.citusdata.com) | [@citusdata](https://twitter.com/citusdata) | - | Open source PostgreSQL extension that shards tables across servers. `Self-hosted` |
| [Datomic](https://www.datomic.com) | [@datomic_team](https://twitter.com/datomic_team) | - | Immutable, transactional database with Datalog queries, on AWS or self-hosted. `Self-hosted` |
| [Tinkerpop](https://tinkerpop.apache.org/) | - | - | Open source software products in the graph space. |
| [Vertabelo](https://www.vertabelo.com) | [@Vertabelo](https://twitter.com/Vertabelo) | - | Web-based database design tool that generates SQL and ORM code. `Hosted` |
| [TablePlus](https://tableplus.com) | [@TablePlus](https://twitter.com/TablePlus) | $79 - $129 one-time | Native GUI client for MySQL, PostgreSQL, SQLite, SQL Server and other databases. |
| [DBngin](https://dbngin.com) | [@DBngin](https://twitter.com/dbngin) | Free | An all-in-one tool for database version management. It allows you to set up a local database server of any versions within a click. |


## Accounting/Invoicing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Harvest](https://www.getharvest.com) | [@harvest](https://twitter.com/harvest) | Free - $14/seat/mo | Time tracking, invoicing and expense tracking for teams. `Hosted` |
| [Ballpark](https://www.getballpark.com) | [@ballparkapp](https://twitter.com/ballparkapp) | $12/mo - $99/mo | Stop sending your clients ugly paper invoices. Go paperless today, with Ballpark. Our beautiful, web-based invoices and estimates make it easier than ever to get paid and discuss projects with your clients and colleagues. |
| [PaySimple](https://paysimple.com) | [@PaySimple](https://twitter.com/PaySimple) | - | Card and ACH payments, recurring billing and invoicing for service businesses. `Hosted` |
| [FreshBooks](https://www.freshbooks.com) | [@freshbooks](https://twitter.com/freshbooks) | $23/mo - $70/mo | Invoicing, expenses and time tracking for small businesses and freelancers. `Hosted` |
| [FreeAgent](https://www.freeagent.com) | [@Freeagent](https://twitter.com/Freeagent) | - | Accounting for small businesses and freelancers, with bank feeds and invoicing. `Hosted` |
| [Blinksale](https://www.blinksale.com) | [@blinksale](https://twitter.com/blinksale) | $15.00 | Online invoicing with payment links and reminders for freelancers and small businesses. `Hosted` |
| [Cashboard](https://cashboardapp.com/) | [@cashboard](https://twitter.com/cashboard) | $8.25/mo - $250/mo | FreeLANCE TIME TRACKING & INVOICE SOFTWARE TRUSTED BY THOUSANDS, WORLDWIDE. Cashboard is the tool we designed to remedy that situation. It works for our software consultancy and we think it’ll work for you too. We launched Cashboard in Spring of 2007after many sleepless nights of hard work. It was the first solution to combine estimates, invoices, time tracking, and online payments into one tool. |
| [Paydirt](https://paydirtapp.com) | [@paydirtapp](https://twitter.com/paydirtapp) | $8/mo - $149/mo | Smart Time Tracking Easier Invoicing Online Payments. In Paydirt, you can start a timer from any page in one click. No fiddly menus. No navigating around. Just a start button for each task. |
| [inDinero](https://www.indinero.com) | [@indinero](https://twitter.com/indinero) | - | - |
| [QuickBooks Online](https://quickbooks.intuit.com/online/) | - | - | Cloud accounting for small businesses, with invoicing, bank feeds and payroll add-ons. `Hosted` |
| [Xero](https://www.xero.com) | [@Xero](https://twitter.com/xero) | - | Cloud accounting for small businesses, with bank feeds, invoicing and payroll. `Hosted` |
| [Wave](https://www.waveapps.com) | [@WaveHQ](https://twitter.com/WaveHQ) | Free (payments and payroll fees extra) | Free accounting and invoicing for small businesses. `Hosted` |
| [Invoice Ninja](https://www.invoiceninja.com) | [@invoiceninja](https://twitter.com/invoiceninja) | Free self-hosted, paid hosted plans | Open source invoicing and billing app. `Self-hosted` |
| [Bonsai](https://www.hellobonsai.com/) | [@bonsaiinc](https://twitter.com/bonsaiinc) | Free, $19, $29 | Online invoicing, proposals, contracts and expense tracking for freelancers and agencies. `Hosted` |

## Privacy Policy, Terms & Conditions, Legal Documents

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [iubenda](https://www.iubenda.com) | [@iubenda](https://twitter.com/iubenda) | Free - from $5.99/mo | Hosts and updates privacy policies, cookie policies and terms. `Hosted` |
| [Choose a license](https://choosealicense.com/licenses/) | [@ChooseALicense](https://twitter.com/ChooseALicense) | Free | Compares open source and other license options for software, data and media. `Hosted` |

## Income Analytics

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Baremetrics](https://baremetrics.com) | [@Baremetrics](https://twitter.com/Baremetrics) | $79/mo - $249/mo | Subscription revenue metrics from Stripe and other billing providers. `Hosted` |

## Payments, Billing & Downloads

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [PayPal](https://www.paypal.com) | [@PayPal](https://twitter.com/PayPal) | - | Online payments and money transfers for individuals and businesses. `Hosted` |
| [Gumroad](https://gumroad.com) | [@gumroad](https://twitter.com/gumroad) | 10% + $0.50/sale | Sells digital downloads, memberships and subscriptions directly to customers. `Hosted` |
| [FetchApp](https://www.fetchapp.com) | [@fetchapp](https://twitter.com/fetchapp) | $5/mo - $500/mo | Delivers digital downloads and license keys to customers. `Hosted` |
| [Maxio Chargify](https://www.maxio.com/chargify) | [@chargify](https://twitter.com/chargify) | - | Subscription billing and invoicing for recurring revenue businesses. `Hosted` |
| [Recurly](https://recurly.com) | [@Recurly](https://twitter.com/Recurly) | $99/mo - $259/mo | Subscription billing and recurring payments management. `Hosted` |
| [ChargeOver](https://chargeover.com) | [@ChargeOver](https://twitter.com/chargeover) | $65/mo- $549/mo | ChargeOver is a full featured invoicing platform supporting payment plans, recurring billing, one-time billing, and all the major gateway backends. |
| [Chargebee](https://www.chargebee.com) | [@chargebee](https://twitter.com/chargebee) | Free (Starter) - custom | Subscription billing and revenue operations for SaaS businesses. `Hosted` |

## Billing & Payment Processing

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Braintree](https://www.braintreepayments.com) | [@braintree](https://twitter.com/braintree) | - | PayPal-owned payments API and SDKs for cards, PayPal and Venmo. `Hosted` |
| [Dwolla](https://www.dwolla.com) | [@dwolla](https://twitter.com/dwolla) | 25¢/transaction | ACH bank transfer API for moving money between accounts. `Hosted` |
| [Stripe](https://stripe.com) | [@stripe](https://twitter.com/stripe) | 2.9% + 30¢/successful charge (US cards) | Payments API for accepting cards and other payment methods online. `Hosted` |
| [Pin](https://pinpayments.com) | [@PinPayments](https://twitter.com/PinPayments) | 2.9% + 30¢/successful charge. | Payments, Rebooted. Accepting credit card payments from a global audience typically requires a merchant account. The process of establishing a merchant account for each currency can be too difficult and costly for small businesses. |
| [Spreedly](https://www.spreedly.com) | [@spreedly](https://twitter.com/spreedly) | $150/mo - $1500/mo | Payment vault and API that connects to many payment gateways through one integration. `Hosted` |
| [Paddle](https://paddle.com) | [@PaddleHQ](https://twitter.com/PaddleHQ) | 5% + 50¢/transaction. | Payment processing and fulfillment, specialized for desktop apps and SaaS subscription services. Handles VAT and invoicing for you, so your accounting becomes easier. |
| [Fattmerchant](https://fattmerchant.com/) | [@Fattmerchant](https://twitter.com/fattmerchant) | 0% + interchange + $99+/mo | Payments unified. Integrate your app, website, software, or hardware with the Fattmerchant API to seamlessly accept all major credit cards, ACH payments, and more! Ideal for both in-person and online transactions. |

## Boilerplates

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Lad](https://lad.js.org) | [@niftylettuce](https://twitter.com/niftylettuce) | Free | Lad scaffolds a Koa webapp and API framework for Node.js. It also includes a job scheduler, automatic email previewing and templates, and much more. |
| [Yeoman](https://yeoman.io/) | [@yeoman](https://twitter.com/yeoman) | Free | The web scaffolding tool for modern web apps |
| [JHipster](https://www.jhipster.tech/) | [@jhipster](https://twitter.com/jhipster) | Free | Hipster stack for Java developers. Spring Boot + Angular/React in one handy generator. |
| [Divjoy](https://divjoy.com/) | [@divjoy](https://twitter.com/divjoy) | $59 | The React codebase generator. |
| [WPPB](https://wppb.me/) | - | Free | WordPress Plugin Boilerplate Generator |

## Phone/PBX/SMS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Plivo](https://www.plivo.com) | [@plivo](https://twitter.com/plivo) | - | Cloud voice and SMS API for sending messages and making calls from code. `Hosted` |
| [Twilio](https://www.twilio.com) | [@twilio](https://twitter.com/twilio) | - | Cloud APIs for SMS, voice, email and verification. `Hosted` |
| [PhoneBooth](https://www.phonebooth.com/) | - | - | - |
| [Talkdesk](https://www.talkdesk.com) | [@Talkdesk](https://twitter.com/talkdesk) | - | Cloud contact center software for phone, chat and email support. `Hosted` |
| [Dropbox Fax](https://fax.dropbox.com) | - | - | Send and receive faxes online (formerly HelloFax). `Hosted` |
| [Dialpad](https://www.dialpad.com) | [@DialpadHQ](https://twitter.com/dialpadHQ) | $15/user/mo | Cloud business phone system with calling, meetings and contact center features. `Hosted` |


## System Monitoring

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [AppNeta (Tracelytics)](https://www.appneta.com/) | [@AppNeta](https://twitter.com/Appneta) | - | - |
| [Riemann](https://riemann.io) | - | - | Open source event stream processor for monitoring metrics and alerts. `Self-hosted` |
| [Pingdom](https://www.pingdom.com) | [@pingdom](https://twitter.com/pingdom) | - | Website uptime and performance monitoring, part of SolarWinds. `Hosted` |
| [UptimeRobot](https://uptimerobot.com) | [@uptimerobot](https://twitter.com/uptimerobot) | Free - paid plans | Website and server uptime monitoring with alerts. `Hosted` |
| [Where's It Up?](https://wheresitup.com/) | - | - | - |
| [Nagios](https://www.nagios.org) | [@nagiosinc](https://twitter.com/nagiosinc) | - | Open source server and network monitoring with alerting. `Self-hosted` |
| [Smokeping](https://oss.oetiker.ch/smokeping/) | - | - | - |

## Search

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Bonsai](https://bonsai.io/) | [@bonsaisearch](https://twitter.com/bonsaisearch) | - | - |
| [WebSolr](https://www.websolr.com) | [@websolr](https://twitter.com/websolr) | - | - |
| [Searchify](https://www.searchify.com/) | [@getsearchify](https://twitter.com/getsearchify) | - | - |
| [SearchBlox](https://www.searchblox.com) | [@searchblox](https://twitter.com/searchblox) | - | - |

## Security

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Foil](https://usefoil.com) | [@usefoil](https://twitter.com/usefoil) | - | Detect AI agents, bots and malicious devices with a drop-in SDK for web, iOS and Android |
| [Burp](https://portswigger.net/burp) | [@Burp_Suite](https://twitter.com/Burp_Suite) | - | - |
| [DuoSecurity](https://duo.com/) | [@duosec](https://twitter.com/duosec) | - | - |
| [Authy](https://authy.com/) | [@Authy](https://twitter.com/Authy) | - | - |
| [Hotspot Shield](https://www.hotspotshield.com/) | [@HotspotShield](https://twitter.com/hotspotshield) | - | - |
| [Betterleaks](https://github.com/betterleaks/betterleaks) | - | Free | Finds leaked secrets such as passwords, API keys and tokens in Git repositories and files. Successor to Gitleaks, by the same author. `Self-hosted` |

## Shipping

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Shipwire](https://www.shipwire.com) | [@shipwire](https://twitter.com/shipwire) | - | - |
| [Whiplash](https://sales.getwhiplash.com/) | - | - | - |

## User Feedback

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Uservoice](https://www.uservoice.com/) | [@UserVoice](https://twitter.com/uservoice) | $499/mo - $999+/mo | Collect, understand and respond to user feedback. |
| [Userecho](https://userecho.com/) | [@userecho](https://twitter.com/userecho) | - | - |

## Designers

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Dribbble](https://dribbble.com) | [@dribbble](https://twitter.com/dribbble) | - | - |
| [Sortfolio](https://sortfolio.com) | [@Sortfolio](https://twitter.com/Sortfolio) | - | - |
| [Behance](https://www.behance.net) | [@Behance](https://twitter.com/Behance) | - | - |

## Notes

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Google Docs](https://www.google.com/docs/about/) | [@googledocs](https://twitter.com/googledocs) | - | - |
| [Evernote](https://evernote.com/) | [@evernote](https://twitter.com/evernote) | - | - |
| [Google Keep](https://www.google.com/keep/) | - | - | - |
| [Workflowy](https://workflowy.com/) | [@WorkFlowy](https://twitter.com/workflowy) | - | - |
| [Quip](https://quip.com/) | [@quip](https://twitter.com/quip) | - | - |
| [Etherpad](https://etherpad.org/) | [@EtherpadOrg](https://twitter.com/EtherpadOrg) | - | - |
| [Kami](https://www.kamiapp.com/) | [@usekamiapp](https://twitter.com/usekamiapp) | - | View, edit, annotate, and collaborate on documents on your browser |
| [OneNote](https://www.onenote.com/) | [@msonenote](https://twitter.com/msonenote) | Free | The digital note-taking app for your devices |
| [Taskade](https://www.taskade.com) | [@taskade](https://twitter.com/taskade) | Free | Real-time collaborative notes, checklists, and outlines for teams. |
| [Dynalist](https://dynalist.io/) | [@dynalisthq](https://twitter.com/dynalisthq) | Free - $8/mo | Outliner, note-taking app, checklists. |
| [Notion](https://www.notion.so/) | [@notionhq](https://twitter.com/notionhq) | Free - $10/user/mo | All-in-one workspace for notes, docs and project tracking. `Hosted` |
| [Inkdrop](https://inkdrop.app/) | [@inkdrop_app](https://twitter.com/inkdrop_app) | $4.99/mo | The Note-Taking App for Markdown Lovers. |

## Group Communication/Chat Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Viva Engage](https://www.microsoft.com/microsoft-viva/engage) | [@Yammer](https://twitter.com/yammer) | - | Enterprise social network, formerly Yammer. `Hosted` |
| [Slack](https://slack.com/) | [@SlackHQ](https://twitter.com/slackhq) | Free - $15/user/mo | Team messaging with channels, webhooks and app integrations. `Hosted` |
| [GoToMeeting](https://www.gotomeeting.com) | [@GoToMeeting](https://twitter.com/gotomeeting) | - | - |
| [IRCCloud](https://www.irccloud.com/) | - | - | - |
| [Gitter](https://gitter.im) | [@gitchat](https://twitter.com/gitchat) | - | Chat for open-source and private development teams, with strong Github integration features |
| [Whereby](https://whereby.com) | [@whereby](https://twitter.com/whereby) | - | One-click video meetings in the browser, no download needed (formerly appear.in). `Hosted` |
| [Convo](https://www.convo.com/) | [@convo](https://twitter.com/convo) | - | - |
| [Zoom](https://www.zoom.us/) | [@zoom_us](https://twitter.com/zoom_us) | - | - |
| [Telegram](https://telegram.org/) | [@telegram](https://twitter.com/telegram) | - | - |
| [Matrix](https://matrix.org/) | [@matrixdotorg](https://twitter.com/matrixdotorg) | - | Decentralised Open Source chat protocol with [bridges to everywhere](https://matrix.org/docs/projects/try-matrix-now.html#application-services) |


## Remote Collaboration

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [TeamViewer](https://www.teamviewer.com) | [@TeamViewer](https://twitter.com/teamviewer) | - | - |

## DNS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Forward Email](https://forwardemail.net) | [@niftylettuce](https://twitter.com/niftylettuce) | Free | Email forwarding for custom domains, with aliases, catch-all and wildcard addresses. `Hosted` |
| [Cloudflare](https://www.cloudflare.com/) | [@Cloudflare](https://twitter.com/Cloudflare) | - | - |
| [Amazon Route 53](https://aws.amazon.com/route53/) | - | - | - |
| [DNSimple](https://dnsimple.com/) | [@dnsimple](https://twitter.com/dnsimple) | - | - |
| [ClouDNS](https://www.cloudns.net/) | [@ClouDNS](https://twitter.com/ClouDNS) | - | - |
| [FreeDNS](https://freedns.afraid.org) | - | - | - |
| [Noip](https://noip.com) | [@NoIPcom](https://twitter.com/NoIPcom) | Free | Quickly get free hostnames, and keep DNS resolving if your IP isn't static. |
| [ImprovMX](https://improvmx.com) | [@nicoschmidt](https://twitter.com/nicoschmidt) | Free - $9/mo | Email forwarding for custom domains. Free plan includes up to 25 aliases per domain with unlimited forwarding. `Hosted` |

## Status Blogs/User Alerts

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [API Status Check](https://apistatuscheck.com) | - | Free | Real-time status monitoring dashboard aggregating 50+ major API and cloud service status pages. Tracks AWS, Stripe, Twilio, GitHub, and more in one view with email alerts. |
| [StatusPage.io](https://www.statuspage.io/) | [@Statuspage](https://twitter.com/Statuspage) | - | - |
| [Tumblr](https://www.tumblr.com/) | [@tumblr](https://twitter.com/tumblr) | - | - |
| [HelloBar](https://www.hellobar.com) | - | - | - |
| [Status.io](https://status.io) | [@statusio](https://twitter.com/statusio) | - | Hosted system status pages |

## Forms / Surveys

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Wufoo](https://www.wufoo.com) | [@Wufoo](https://twitter.com/Wufoo) | - | - |
| [Google Forms](https://www.google.com/forms/about/) | [@googledocs](https://twitter.com/googledocs) | Free | Surveys and forms that collect responses in Google Sheets. `Hosted` |
| [Typeform](https://www.typeform.com) | [@typeform](https://twitter.com/typeform) | Free - $39/mo | Online forms and surveys with conversational question flows and built-in response analysis. `Hosted` |
| [Qualaroo](https://qualaroo.com) | [@Qualaroo](https://twitter.com/Qualaroo) | $63/mo - 499/mo | Qualaroo website surveys uncover customer insights that lead to better business results. |
| [Formcarry](https://formcarry.com) | - | $0/mo - $99/mo | Handle forms without a single line of back-end code. |
| [FormKeep](https://formkeep.com) | [@formkeep](https://twitter.com/formkeep) | $59/mo - $199/mo | Premium Forms Backend service with built in spam protection, data integrations to over a 1000 services, data retention policies and more. |
| [Formcake](https://formcake.com) | - | free - $19.99/mo | Form backend built for devs. Integrate with Zapier, trigger webhooks, emails, and other actions. |

## Source Code Hosting

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [BitBucket](https://bitbucket.org/) | [@Bitbucket](https://twitter.com/bitbucket) | - | - |
| [Codebase](https://www.codebasehq.com/) | - | - | - |
| [GitHub](https://github.com/) | [@github](https://twitter.com/github) | - | - |
| [Unfuddle](https://unfuddle.com/) | [@unfuddle](https://twitter.com/unfuddle) | - | - |
| [GitLab](https://about.gitlab.com/) | [@gitlab](https://twitter.com/gitlab) | - | - |
| [Launchpad](https://launchpad.net/) | - | - | - |
| [TuxFamily](https://www.tuxfamily.org) | - | - | - |
| [Assembla](https://www.assembla.com/) | [@assembla](https://twitter.com/assembla) | From $11.50/user/mo | Git and SVN hosting with integrated project management and ticketing. `Hosted` |
| [Source Hut](https://sourcehut.org) | - | - | Open source git, mailing list and CI hosting. `Hosted` |

## Design Collaboration

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [ConceptShare](https://www.conceptshare.com) | [@conceptshare](https://twitter.com/conceptshare) | - | - |
| [Helio](https://helio.zurb.com) | [@ZURB](https://twitter.com/zurb) | - | Prototype and design testing with real users. `Hosted` |

## PaaS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Heroku](https://www.heroku.com) | [@heroku](https://twitter.com/heroku) | From $5/mo | Platform for deploying and scaling web apps. `Hosted` |
| [Cloud Foundry](https://www.cloudfoundry.org) | [@cloudfoundry](https://twitter.com/cloudfoundry) | - | Open source platform for deploying apps, on your own infrastructure or a provider's. `Self-hosted` |
| [Clever Cloud](https://www.clever-cloud.com) | [@clever_cloud](https://twitter.com/clever_cloud) | - | French platform for deploying and scaling apps. `Hosted` |
| [Google App Engine](https://cloud.google.com/appengine/docs/) | - | - | Google Cloud's managed platform for running web apps. `Hosted` |
| [OpenShift](https://www.openshift.com) | [@openshift](https://twitter.com/openshift) | - | Red Hat's Kubernetes application platform. `Self-hosted` |
| [Engine Yard](https://www.engineyard.com) | [@engineyard](https://twitter.com/engineyard) | - | - |
| [CloudBees](https://www.cloudbees.com) | [@CloudBees](https://twitter.com/cloudbees) | - | - |
| [Microsoft Azure](https://azure.microsoft.com) | [@Azure](https://twitter.com/azure) | - | Microsoft's cloud platform for compute, storage, databases and app hosting. `Hosted` |
| [Amazon Web Services](https://aws.amazon.com/elasticbeanstalk/) | [@awscloud](https://twitter.com/awscloud) | - | Like Azure, it's more known for IaaS |
| [AKS](https://azure.microsoft.com/en-us/services/kubernetes-service/) | [@Azure](https://twitter.com/azure) | - | - |
| [Scalingo](https://scalingo.com) | [@ScalingoHQ](https://twitter.com/ScalingoHQ) | - | Platform as a service for deploying apps, hosted in Europe. `Hosted` |

## VPS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Linode](https://www.linode.com/) | [@linode](https://twitter.com/linode) | - | - |
| [Ramnode](https://www.ramnode.com/) | [@RamNode](https://twitter.com/ramnode) | - | - |
| [DigitalOcean](https://www.digitalocean.com/) | [@digitalocean](https://twitter.com/digitalocean) | - | - |
| [Vultr](https://www.vultr.com/) | [@Vultr](https://twitter.com/vultr/) | - | - |
| [OVH](https://www.ovh.com) | [@OVHcloud](https://twitter.com/OVHcloud) | - | - |
| [Scaleway](https://www.scaleway.com/) | [@Scaleway](https://twitter.com/scaleway/) | - | European cloud provider with VPS, bare metal and managed services. `Hosted` |


## Geocoding

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [OpenCage Geocoder](https://opencagedata.com/) | [@OpenCageData](https://twitter.com/opencagedata) | $0-1000/month | Forward and reverse geocoding API built on open data, with worldwide coverage. `Hosted` |
| [Google Maps](https://developers.google.com/maps/documentation/geocoding/intro) | - | Pay per request | Geocoding API from Google. Requires a billing account at sign up. `Hosted` |
| [Pelias](https://pelias.io) | [@pelias_geocoder](https://twitter.com/pelias_geocoder) | Free | Open source geocoder built on Elasticsearch. `Self-hosted` |


## Heroku Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Hirefire](https://hirefire.io/) | - | $25 - $50/mo per app | Autoscaler for Heroku worker and web dynos. `Hosted` |

## AWS Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Skeddly](https://www.skeddly.com) | [@skeddly](https://twitter.com/skeddly) | - | - |

## Database-aaS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [HumongouS.io](https://www.humongous.io) | - | - | HumongouS.io is a web-based user interface (GUI) for MongoDB. |
| [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) | [@MongoDB](https://twitter.com/MongoDB) | Free - $1000+/mo | MongoDB's official hosted service |
| [Redis Cloud](https://redis.io/cloud/) | [@RedisLabs](https://twitter.com/RedisLabs) | Free - $338+/mo | Managed Redis hosting from Redis, formerly RedisLabs. `Hosted` |

## Backend-aaS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Firebase](https://firebase.google.com) | [@Firebase](https://twitter.com/Firebase) | - | Google's backend platform with realtime database, auth, hosting and functions. `Hosted` |
| [LoopBack](https://loopback.io/) | - | - | Node.js and TypeScript framework for building REST APIs. `Self-hosted` |
| [Para](https://paraio.com) | [@Para_IO](https://twitter.com/para_io) | Free - $99/mo | A flexible and affordable backend API for busy developers. |

## WebSockets-aaS

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Pusher](https://pusher.com) | [@pusher](https://twitter.com/pusher) | - | Hosted WebSocket channels and pub/sub API for realtime features. `Hosted` |
| [ScaleDrone](https://www.scaledrone.com) | [@scaledrone](https://twitter.com/scaledrone) | - | - |

## Ops Alerts and Scheduling

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [PagerDuty](https://www.pagerduty.com/) | [@pagerduty](https://twitter.com/pagerduty) | - | Incident response and on-call alerting platform. `Hosted` |
| [Splunk On-Call](https://www.splunk.com/en_us/products/on-call.html) | [@VictorOps](https://twitter.com/VictorOps/) | $9 - $49 user/month | On-call alerting and incident response, formerly VictorOps. `Hosted` |

## Video Hosting

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Wistia](https://wistia.com) | [@wistia](https://twitter.com/wistia) | - | Video hosting, player and analytics for businesses. `Hosted` |
| [JW Player](https://developer.jwplayer.com) | - | - | Video hosting and player APIs for web and mobile. `Hosted` |

## Knowledge Tracking/Wiki

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Confluence](https://www.atlassian.com/software/confluence) | [@Confluence](https://twitter.com/Confluence) | - | Team wiki and knowledge base from Atlassian. `Hosted` |
| [Confluence Questions (Q&A for your team)](https://www.atlassian.com/software/confluence/questions) | - | - | - |
| [Bitbucket Wiki](https://support.atlassian.com/bitbucket-cloud/docs/create-a-wiki/) | - | - | Comes with each repo, written in Markdown or Creole, much lighter than Confluence. |
| [SlimWiki](https://slimwiki.com) | [@slimwiki](https://twitter.com/slimwiki) | - | - |
| [Documize](https://www.documize.com/) | - | - | - |
| [Notion](https://www.notion.so/) | [@NotionHQ](https://twitter.com/NotionHQ) | Free, $10 - $20/member/mo | Docs, wikis, databases and project planning in one workspace. `Hosted` |
| [Slite](https://slite.com/) | [@sliteHQ](https://twitter.com/sliteHQ) | From $8/user/mo | Team knowledge base for docs, handbooks and meeting notes. `Hosted` |

## Offsite Backups

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Tarsnap](https://www.tarsnap.com/) | - | Pay per use | Encrypted command-line backup service that charges for storage and bandwidth. `Hosted` |
| [Rsync.net](https://www.rsync.net/) | [@rsyncnet](https://twitter.com/rsyncnet) | - | SSH and rsync-accessible cloud storage for backups. `Hosted` |
| [SpiderOak](https://spideroak.com) | [@spideroak](https://twitter.com/spideroak) | First 2gb Free - $100/100gb/year (check [twitter](https://twitter.com/spideroak) for deals) | Store. Sync. Share. Privately. |

## Personal Machine Backups

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Crashplan](https://www.crashplan.com) | [@CrashPlanSMB](https://twitter.com/crashplansmb) | - | - |
| [Arq Backup](https://www.arqbackup.com/) | - | - | Client-side encrypted backups to your own S3, Glacier or other storage. `Self-hosted` |

## Remote Workers

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Upwork](https://www.upwork.com) | [@Upwork](https://twitter.com/Upwork) | - | Marketplace for hiring freelancers and contractors. `Hosted` |
| [Freelancer](https://www.Freelancer.com/) | [@freelancer](https://twitter.com/freelancer) | - | - |
| [TaskArmy](https://taskarmy.com) | [@taskarmy](https://twitter.com/taskarmy) | - | - |
| [99designs](https://99designs.com/) | [@99designs](https://twitter.com/99designs) | - | Marketplace for hiring designers for logos, branding and web work. `Hosted` |
| [Fiverr](https://www.fiverr.com) | [@fiverr](https://twitter.com/fiverr) | - | Marketplace for hiring freelancers for fixed-price tasks. `Hosted` |

## Deployment

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Chef](https://www.chef.io) | [@chef](https://twitter.com/chef) | - | Configuration management that describes server state in code. `Self-hosted` |
| [Fabric](https://www.fabfile.org) | - | - | Python library for running commands over SSH. `Self-hosted` |
| [Puppet](https://puppet.com) | [@puppetize](https://twitter.com/puppetize) | - | Configuration management for servers and infrastructure. `Self-hosted` |
| [Ansible](https://www.ansible.com) | [@ansible](https://twitter.com/ansible) | - | Agentless automation for configuration, deployment and orchestration. `Self-hosted` |
| [Vagrant](https://www.vagrantup.com) | - | - | Tool for building and managing reproducible development virtual machines. `Self-hosted` |
| [Salt](https://saltproject.io) | [@SaltStack](https://twitter.com/SaltStack) | - | Event-driven configuration management and remote execution. `Self-hosted` |
| [Ngrok](https://ngrok.com) | - | - | Secure tunnels that expose local servers to the internet. `Hosted` |

## SEO Tools

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [AccuRanker](https://www.accuranker.com/) | - | - | Rank tracking for keywords across search engines. `Hosted` |
| [Ahrefs](https://ahrefs.com) | [@ahrefs](https://twitter.com/ahrefs) | From $129/mo | Backlink analysis, keyword research and rank tracking. `Hosted` |
| [SerpBook](https://serpbook.com) | - | - | - |
| [WooRank](https://www.woorank.com) | [@woorank](https://twitter.com/woorank) | Free - $49/mo | WooRank analyzes your website for optimization best practices and shows how it ranks against your competition. Its real-time brandable reports, consisting of over 150 data-points, help you to instantly spot critical issues that impact traffic, usability and conversions. Sync your analytics, social accounts and keywords for even more robust tracking. |
| [Moz](https://moz.com) | [@moz](https://twitter.com/moz) | $49 - $299/mo | SEO toolset for keyword research, link analysis and rank tracking. `Hosted` |
| [RatedWithAI](https://ratedwithai.com) | - | Free - $29/mo | AI-powered web accessibility scanner. Checks WCAG 2.2 compliance, detects issues, and provides fix guidance. Accessibility impacts SEO, Google uses Core Web Vitals and accessibility signals in rankings. |
| [KWFinder](https://kwfinder.com/) | [@mangools_com](https://twitter.com/mangools_com) | $30+/mo | Keyword research tool |
| [Animalz - Revive](https://revive.animalz.co/) | [@AnimalzCo](https://twitter.com/AnimalzCo) | Free | Provides a list of posts that should be refreshed. |

## API Builder

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Postman](https://www.postman.com/) | [@postmanclient](https://twitter.com/postmanclient) | Free, from $9/mo | API platform for designing, testing and documenting APIs. `Hosted` |
| [Apiary](https://apiary.io) | [@apiary](https://twitter.com/apiaryio) | Free - $99/mo | Powerful API Design Stack. Built for Developers. Work together to quickly design, prototype, document and test APIs. |
| [Hoppscotch](https://hoppscotch.io) | [@liyasthomas](https://twitter.com/liyasthomas) | Free (OSS) | Open source API development tool. `Hosted` |

## Password Management

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Lastpass](https://www.lastpass.com) | [@LastPass](https://twitter.com/LastPass) | Free - $7.5/user/mo | - |
| [1Password](https://1password.com) | [@1Password](https://twitter.com/1Password) | $2.99 - $7.99/user/mo | Password manager with shared vaults for individuals and teams. `Hosted` |
| [Passpack](https://www.passpack.com) | [@passpack](https://twitter.com/passpack) | $18 - $480/year | - |
| [KeePassXC](https://keepassxc.org/) | [@KeePassXC](https://twitter.com/KeePassXC) | Free | Cross-platform open source password manager that stores its database in a local file. `Self-hosted` |
| [Enpass](https://www.enpass.io) | [@EnpassApp](https://twitter.com/EnpassApp) | - | Password manager with a local encrypted vault and optional sync through your own cloud storage. `Self-hosted` |
| [Dashlane](https://www.dashlane.com) | [@dashlane](https://twitter.com/dashlane) | $5/user/mo - $8/user/mo | Password manager with autofill, password health checks and team sharing. `Hosted` |
| [Bitwarden](https://bitwarden.com/) | [@bitwarden](https://twitter.com/bitwarden) | Free, from $1.65/mo | Open source password manager, hosted or self-hosted. `Hosted` `Self-hosted` |

## Sources of Clicks/Ad Platforms

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [NeoReach](https://neoreach.com/) | [@NeoReach](https://twitter.com/NeoReach) | - | - |
| [Microsoft Advertising](https://ads.microsoft.com) | - | - | Search ads on Bing, Yahoo and partner sites. `Hosted` |
| [Taboola](https://www.taboola.com/) | [@taboola](https://twitter.com/taboola) | - | Content recommendation and native ad network. `Hosted` |
| [Outbrain](https://www.outbrain.com/) | [@Outbrain](https://twitter.com/outbrain) | - | Content recommendation and native ad network. `Hosted` |
| [Google Ads](https://ads.google.com) | [@GoogleAds](https://twitter.com/googleads) | Pay per click | Search and display advertising from Google. `Hosted` |
| [Meta Ads](https://www.facebook.com/business/) | - | - | Paid ads across Facebook, Instagram and Messenger. `Hosted` |

## Task Scheduling

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [EasyCron](https://www.easycron.com) | - | - | - |
| [IFTTT](https://ifttt.com) | [@IFTTT](https://twitter.com/ifttt) | - | Automations that connect apps and devices with if-this-then-that rules. `Hosted` |
| [Zapier](https://zapier.com) | [@Zapier](https://twitter.com/zapier) | Free, from $19.99/mo | No-code automation that connects apps with multi-step workflows. `Hosted` |
| [Make](https://www.make.com) | [@integromat](https://twitter.com/integromat) | Free, from $9/mo | Visual no-code automation builder that connects apps in scenarios. `Hosted` |
| [Dead Man's Snitch](https://deadmanssnitch.com) | [@DeadMansSnitch](https://twitter.com/deadmanssnitch) | Free - $49/mo | Monitoring for scheduled tasks (like cron) and service heartbeats. Makes it easy to know when and why a particular job failed. |
| [Healthchecks.io](https://healthchecks.io) | [@healthchecks_io](https://twitter.com/healthchecks_io) | Free - $80/mo | Cron job and scheduled task monitoring. |

## Documentation

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Dash](https://kapeli.com/dash) | [@kapeli](https://twitter.com/kapeli) | - | Offline API documentation browser. `Self-hosted` |
| [Zeal](https://zealdocs.org) | [@zealdocs](https://twitter.com/zealdocs) | Free | Offline documentation browser |
| [DevDocs](https://devdocs.io/) | [@DevDocs](https://twitter.com/DevDocs) | Free | Searchable, offline-capable API documentation for many languages and frameworks. `Hosted` |

## Business Cards and Print Material

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Moo](https://www.moo.com) | [@MOO](https://twitter.com/MOO) | - | Online printer for business cards and marketing print. `Hosted` |
| [PSPrint](https://www.psprint.com) | [@PsPrint](https://twitter.com/psprint) | - | Online printer for business cards, flyers and marketing print. `Hosted` |
| [Vistaprint](https://vistaprint.com) | [@Vistaprint](https://twitter.com/vistaprint) | - | Online printer for business cards, flyers and marketing print. `Hosted` |

## Presentations / Slides

| Service | Twitter | Pricing | Description |
|:--------|:--------|:--------|:------------|
| [Prezi](https://prezi.com/) | [@prezi](https://twitter.com/prezi) | - | Cloud presentation editor with zooming canvas layouts. `Hosted` |
| [markpress](https://github.com/gamell/markpress) | - | - | HTML presentations from Markdown files |
| [Reveal.js](https://github.com/hakimel/reveal.js) | - | Free | HTML presentation framework for building slides in the browser. `Self-hosted` |
| [Impress.js](https://github.com/impress/impress.js/)| - | - | Presentation framework based on CSS3 transforms and transitions inspired by Prezi |
| [Slides](https://slides.com/) | - | Free - $20/mo | Online editor built with Reveal.js that includes a graphical interface |
| [SlideShare](https://www.slideshare.net/) | [@slideshare](https://twitter.com/SlideShare) | Free | Hosts and shares public slide decks and documents. `Hosted` |

## Use

The best ways to use this list are:

- By browsing the [contents](#contents).
- By using <kbd>command</kbd> + <kbd>F</kbd> to search the contents.

This list also uses tags to help when searching the contents:

- **Hosted?** `Hosted`, `Self-hosted`

## Also

* [Awesome Online IDEs](https://github.com/styfle/awesome-online-ide) - A list of awesome online development environments.

## Credits

- [Chris Barber](https://www.chrisbarber.co)
- [Craig Davison](https://davison.io)
and contributors!

If you'd like to contribute, feel free to submit a pull request following the [contributing guidelines](https://github.com/cjbarber/ToolsOfTheTrade/blob/master/contributing.md).

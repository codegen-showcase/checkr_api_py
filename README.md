
# Checkr.com API Docs Python SDK

## Overview
 # Introduction

Checkr is a modern, [RESTful](https://en.wikipedia.org/wiki/Representational_state_transfer) API-driven background screening service. The Checkr API uses resource-oriented URLs, supports HTTPS authentication and HTTPS verbs, and leverages [JSON](http://www.json.org/) in all responses passed back to customers.

Checkr is used by over 10,000 customers in a wide variety of industries, and supports a range of screening products and candidate workflows. For a full list of our screenings, please see the Checkr [Screenings section](#tag/SSN-Trace) below or read the Checkr Help Center articles on [Screening Types](https://help.checkr.com/hc/en-us/sections/203637147-Screening-Types).

This Programming Guide is designed to help customers get up-and-running with Checkr's background screening services, both by providing the necessary context to understand the background screening industry and its regulations, and by giving technical guidance on how to work with the Checkr API.

**Note:** The cURL command is used for all examples in the Checkr API documentation.

### Other resources

For information about using the Checkr Dashboard, and [compliance](https://help.checkr.com/hc/en-us/sections/203637107-Compliance) and regulatory aspects of background checks, visit the [Checkr Help Center](https://help.checkr.com).

For a more targeted set of Checkr Dashboard learning paths for talent sourcing roles like Recruiters, Adjudicators, or Program Administrators, please see the [Checkr Learning Center](https://learn.checkr.com).

## Understand the screening process

Checkr follows a standardized screening process:

1. Customer requests a background check.
2. Candidate is presented with and signs the necessary disclosures and authorizations, and submits the requested Personally Identifiable Information (PII).
  -   With the Checkr-Hosted Apply Flow, the candidate signs disclosures and authorizations and enters their own PII.
  -   With a custom self-hosted flow, the Checkr customer collects the required authorizations, and passes Checkr candidate PII using the Checkr API.
3. Checkr conducts an SSN Trace, and collects associated addresses.
4. Checkr runs searches or verifications based on the screening Packages requested.
5. Checkr applies appropriate compliance filters based on the customer’s settings and candidate’s provided residence to determine which records to show, and returns a finalized report to the customer.
6. If there is a record on the report, the customer Engages or Adverse Actions the Candidate, based on an individualized assessment of the candidate's report.

### 1. Request a background check

To initiate a background check, a customer provides Checkr their candidate's email address (for a Checkr-Hosted Apply Flow) or the candidate's PII (for a self-hosted flow). For more information on ways to achieve this, please see [Designing your workflow](#section/Introduction/Designing-your-workflow).

### 2. Candidate signs disclosures and authorizations

Under the U.S. Fair Credit Reporting Act (FCRA), customers are obligated to collect consent from their candidates when running background checks through Checkr or any other Consumer Reporting Agency (CRA).

The Checkr-Hosted Apply Flow presents candidates with fields in which the requested PII may be entered, and collects candidate information on behalf of the customer. Checkr will also present disclosures and authorizations to the candidate, and enable eSignature to capture consent, on behalf of customers using this flow with the Checkr Dashboard or email invitation flow.

Custom self-hosted flows collect candidate PII, and pass the information to Checkr using the Checkr API. Customers creating a self-hosted flow will receive guidance from the Checkr team on setting up a similar process as required.

### 3. Checkr runs an SSN Trace

Checkr runs an SSN Trace to match the candidate’s provided PII with existing credit header data mapped to the SSN. This process yields a list of names and addresses associated with the entered SSN, which can be used to supplement the background check process.

At this point Checkr also conducts some initial data comparisons to check that critical pieces of information, like a candidate's submitted Date of Birth (DOB) and SSN, align with information held on file by the credit bureaus. If there is information that looks out of place, Checkr may reach out directly to the candidate, through their email address, to gain further confirmation or data from the individual.

Once the candidate's information has been confirmed and an address history developed, the background check screening process begins.

### 4. Checkr runs the requested Screenings

Checkr then runs the customer's requested Screenings. Based on the results of the SSN Trace, Checkr may expand the search for the requested Screenings to include counties where the candidate may have lived in the past.

### 5. Completed Report is returned

Once a report has been completed, customers receive a report result update of **Clear** or **Consider** through their selected method of API webhooks, email, or Checkr Dashboard notifications.

**Clear** and **Consider** are the default results. A Clear result can be interpreted as that report having no items listed on the candidate’s record that require consideration. A report with a result of Consider indicates that there are items on the candidate’s report that require your review. With both Clear and Consider reports, customers must decide whether or not to engage a candidate. Checkr does not make this determination on the customer’s behalf.

### 6. Customer evaluates the Report

After the Report is completed and returned, the customer must evaluate the report, and make a final hiring determination. In maintaining a process compliant with per FCRA legislation and EEOC guidelines, Checkr does not make this determination on the customer's behalf.

## Get credentialed

Before gaining a Checkr staging or production account, you must first work with a Checkr Account Executive or Customer Success representative to create and credential your account.

### Credentialing and authorizing your account

The background screening industry in the United States is heavily regulated by federal, state, and local levels of government, and primarily by the [Fair Credit Reporting Act (FCRA)](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/fair-credit-reporting-act). Checkr complies with these laws, and helps its customers comply, through multiple Checkr product features.

Two key processes in the account authorization process also enable compliance: establishing permissible purpose, and confirming a compliant user interface workflow.

### Establishing permissible purpose

One of the main provisions of FCRA is the requirement to establish a legitimate "permissible purpose" for running a background screen on an individual. These permissible purposes include running background screens for employment purposes (that is, making hiring decisions), making a decision to extend credit to an individual, or for what the law calls a "legitimate business purpose".

Checkr establishes a customer's permissible purpose by collecting and confirming a number of key details about the business entity running a background screen, including:

- Legal business name (associated with Employer Identification Number)
- State of incorporation
- Articles of incorporation
- Employer Identification Number

Some permissible purposes may impose additional legal requirements on the business entity running a background screen. For example, purposes involving checking a candidate's credit history require [an onsite inspection of the entity's business premises](https://www.transunion.com/data-reporting/getting-started).

### Confirming a compliant user interface (UI) workflow

When building a candidate user experience that includes the capture of information necessary to run a background check, there are a number of essential components that must be included to send a compliant request to Checkr. For more information on these requirements and best practices, please see [Building your candidate experience](#section/Introduction/Designing-your-workflow/Building-your-candidate-experience).

Before a Checkr account is credentialed and authorized for production API access, the Checkr Customer Success team confirms that your UI/UX flow meets our requirements and that all necessary information is being appropriately captured. More details about these requirements are included below and throughout the Checkr customer account onboarding process.

## API keys

Checkr authenticates your API requests using your account's API keys. If you do not include your key when making an API request, Checkr will return an authentication error.

Go to <b>Account Settings > Developer Settings </b>in the Checkr Dashboard to create both Secret and Publishable keys for your account. Use the Secret Key within your staging and production environments.

Resources like Candidates, Reports, and Packages will not transfer from your Staging environment to your Live environment. For more information, please see [Requesting a Staging Account](#section/Getting-Started/Request-a-Staging-Account) in Getting Started.

There are two types of API keys: secret and publishable.

- **Secret API keys** should be kept confidential and stored only on your own servers. Your account's secret API key can perform any API request to Checkr without restriction.
- **Publishable API keys** are for use only with [Checkr's JS API](https://github.com/checkr/checkr-js), and are meant solely to identify your account with Checkr. They aren't secret, and can therefore safely be published in your site's JavaScript code, or in an Android or iPhone app.

### Using your API keys

Once your Checkr account has been created, your API keys will be available in the Checkr Dashboard, in the Account Settings > [Developer Settings](https://help.checkr.com/hc/en-us/articles/360010450474-Account-Settings#developer) page.

<b>Note: </b>To prevent unexpected charges for production background checks, do not use your production Publishable API key for testing or development.

**Keeping your keys safe**

Access to your API keys should be granted only to those that need them. Your secret API key can be used to make any API call on behalf of your account, such as creating Candidates, requesting and upgrading Screenings, and creating Geos. Your publishable API key can only create Candidates in the Checkr system, and may be used to publish app or site builds.

To further protect your keys, ensure that they are not included in any version control system that you may be using.

**Expiring keys**

If an API key is compromised, expire the key in the [Checkr Dashboard](https://help.checkr.com/hc/en-us/articles/360010450474-Account-Settings#developer) to block it. Click **Expire key** to set an expiration date for the selected key, and **Create new key** to create a new one to replace it.

![](images/AccountSettingsDevsKeys.png)

## Designing your workflow

Checkr's API is flexible enough to support a range of workflows for integrating background screening into your candidate onboarding process. At a high-level there are three options, each with unique benefits and disadvantages.

| Option | Benefits | Disadvantages |
|:--|:--|:--|
| Checkr Dashboard experience | <ul><li>No developer investment needed to get up-and-running</li></ul> | <ul><li>Least control over user experience</li><li>Least amount of flexibility around automated workflows</li></ul>  |
| Checkr-hosted candidate experience | <ul><li>Easy to implement and get up-and-running</li><li>Checkr hosts and maintains compliance language</li></ul> | <ul><li>Less control over user experience</li><li>Less flexibility around API-specific automated workflows</li></ul> |
| Self-hosted candidate experience | <ul><li>Seamless, customizable user experience</li><li>Potential for higher candidate conversion rates</li><li>Ability to measure conversion at each stage</li></ul> | <ul><li>Requires greater engineering resources</li><li>Customer is responsible for presenting and capturing all legal disclosure and consent forms and maintaining ongoing compliance with FCRA and state/locality regulations</li><li>Customer must have adequate legal resources to provide ongoing review of compliance</li></ul> |


### Checkr Dashboard experience

The Checkr Dashboard allows customers to initiate a background check through either the Checkr-Hosted Apply Flow or through a Manual flow.

* Selecting Invite Candidates allows customers to enter an email address for their candidates. Checkr will then issue an invitation to the selected candidate which includes a Checkr-provided link. Clicking the link launches the Checkr-Hosted Apply Flow, which will walk them through the next steps in the process.

* Selecting Manual Order requires customers to enter their candidate's PII, and confirm that they have collected the necessary authorizations on their candidate's behalf.

For more information, see [Order a Report](https://help.checkr.com/hc/en-us/articles/217084017-Order-a-Report) in the Checkr Help Center.

### Checkr-hosted candidate experience

The Checkr-hosted candidate experience enables Checkr customers to easily set up a modern, compliant candidate background screening process in their onboarding flow with limited development effort. The Checkr-hosted candidate experience has the full set of features and functionality of the Checkr product, and is built on top of the Checkr API, making it an easy and powerful option for customers looking to begin using Checkr as quickly as possible.

The Checkr-Hosted Apply Flow, by which invitations are issued to candidates to participate in their background check, forms the basis of the Checkr-hosted candidate experience. Use the [Invitations](#tag/Invitations) resource to build this automated process into your application.

The Checkr-hosted experience can be initiated in two ways:

**Candidate invitations triggered by API:** Customers can choose to build a programmatic trigger into their site or product to order reports and send candidates invitations to participate in the background check process. In this case, a customer passes Checkr a candidate email address through the API, which triggers an email to that address to collect the candidate's information and present the necessary compliance forms and disclosures. This option requires developer time to build a Checkr backend integration into the customer's product, but does present benefits for automation and programmatic ordering.

**Candidate invitations triggered through the Checkr Dashboard:** Customers can log into the Checkr Dashboard and issue an invitation to participate in the background check process to a candidate's email address. This option requires no developer time to build any Checkr integration, but lacks any automation or programmatic ordering, making it difficult to scale for high volume environments.

Customers may also use the Checkr Dashboard to submit a Manual Order. Selecting this option requires them to collect the candidate’s authorization and consent to a background screening “offline”. This means that the customer will collect the candidate’s Personally Identifiable Information (PII), present the necessary authorizations and disclosures, and collect and store necessary signatures through separate means. Customers must then submit their candidate's PII to Checkr through the Checkr Dashboard, and certify that proper consent was obtained from their candidate.

**Note:** When using candidate invitations and the Checkr-Hosted Apply Flow, understand that Checkr is facilitating your obligations with regard to applicable consumer reporting laws. Before using either method of candidate invitations, you should fully review the template copies of disclosure(s) and authorization language to ensure your business needs are met.

<!--#### What it looks like

![](images/CheckrHostedFlowEmail.gif)

![](images/MobileCheckrInvite.gif)-->


### Self-hosted candidate experience

The self-hosted candidate experience enables Checkr customers to completely control the user onboarding experience, from the look and feel of the candidate's UX, to the specific API calls made during the process, to the flexibility in timing and ordering of those calls. Some unique Checkr functionality, like programmatic report upgrades, are also available only to those customers hosting their own candidate experience.

While the self-hosted flow offers more control over the background check experience, this needs to be weighed against the burden of having to be responsible for maintaining compliance when presenting the background check disclosure and consent forms, which is not a trivial undertaking.  Typically, the self-hosted flow works best for our larger customers that have a dedicated legal department that can provide ongoing monitoring of the changing compliance landscape for background checks.  Please see the [Creating a fully custom apply flow](#section/Advanced-Features/Creating-a-fully-custom-apply-flow) section for more detail on this.

**Building your candidate experience**

To help customers meet the regulatory demands of the background screening industry, Checkr has defined the following UX requirements for customers building their own candidate onboarding experience:

- **Collect candidate PII:** Collect candidate Personally Identifiable Information (PII), with additional requirements around the data captured and its formatting. This screen may be presented and the information collected at any point in the signup flow
- **Present consumer rights summary, and collect acknowledgement:** Present a summary of consumer rights under the Fair Credit Reporting Act (FCRA) and candidate’s acknowledgement of receipt. This screen may be presented on the same page as the collection of PII.
- **Present disclosures and collect acknowledgement:** Present a disclosure form and candidate’s acknowledgement of receipt. This disclosure form MUST be on its own page with no extraneous information.
- **Present state-specific disclosures and collect acknowledgement** (if necessary): Present any state-specific disclosure forms and candidate’s acknowledgement of receipt. For example: California requires its own disclosure separate from the general background check disclosure. Washington State DMV requires a release of liability for accessing Motor Vehicle Records for employment.
- **Present authorization form and collect consent:** Present an authorization form and collection of consent to a background screening. Present a signature of authorization form, compliant with the [ESIGN Act](https://en.wikipedia.org/wiki/Electronic_Signatures_in_Global_and_National_Commerce_Act).
- **Upload authorization:** upload authorization to Checkr using the Documents endpoint https://api.checkr.com/v1/candidates/{candidate_id}/documents  with the type of "consent"

Checkr can provide you with copy templates for each of these documents. Checkr routinely has these documents reviewed for general compliance and best practice in the industry, but you should always consult your own legal counsel when using templates and ensure they work for your business. Please work with your Checkr Account Executive or Customer Success Manager to receive Checkr’s set of templates. These templates, the documents they include, and other requirements will be explained throughout the Checkr customer account onboarding process.

**Note:** Requirements differ for customers running background screening programs limited to running a Motor Vehicle Record (MVR) on candidates for a non-employment or contractor purpose. The requirements for running an MVR in order to provide a service such as a car or scooter rental are far less onerous than the requirements for other uses of the MVR, and require only one or two screens of necessary consent and disclosure. Please contact your Checkr Account Executive or Customer Success Manager if you'd like to learn more about these streamlined requirements.

**Compliance and eSignature**

Collecting proof of authorization from your candidates is one of your most important responsibilities before performing a background screen through Checkr or any other Consumer Reporting Agency. Under the FCRA, Checkr cannot provide you with a report unless you certify that you have obtained proper authorization. Maintaining proof of this process is essential in the event that either you or Checkr is audited, or a candidate threatens you with litigation.

Checkr recommends two means of collecting and storing this eSignature during the consent and authorization flow:

- Store generated PDFs
    -   Identify the candidate by username and password
    -   Have the candidate type their name in a signature box
    -   Upon submission of authorization, generate a PDF of the authorization form, including the date, time, and IP address
- Store data to generate PDF on demand
    -   Enable on-demand generation of PDFs
    -   Identify the candidate by username and password
    -   Have the candidate type their name in signature box
    -   Upon submission of authorization, store the date, timestamp, IP address, and signed name
    -   Have the ability to reproduce a PDF copy of the authorization form on demand, including the date and timestamp, IP address, and signed name

## The Checkr Dashboard

The Checkr Dashboard allows Checkr customers to begin using the Checkr platform immediately and with no developer effort. The Checkr Dashboard includes the full feature and functionality set as the Checkr API interface, with a few key limitations.

For more information, please see the [Checkr Dashboard User Guide](https://help.checkr.com/hc/en-us/sections/360002119753-Checkr-Dashboard-User-Guide) in the Checkr Help Center.

# Getting Started

The following sections will walk you through the steps necessary to get started
running background checks with the Checkr API:

- [Get credentialed](#section/Getting-Started/Get-credentialed)
- [Request a Staging Account](#section/Getting-Started/Request-a-Staging-Account)
- [Get your API key](#section/Getting-Started/Get-your-API-key)
- [Authenticate with Checkr](#section/Getting-Started/Authenticate-with-Checkr)
- [Create a Candidate](#section/Getting-Started/Create-a-Candidate)
- [Create an Invitation](#section/Getting-Started/Create-an-Invitation)
- [Retrieve the Report](#section/Getting-Started/Retrieve-the-Report)
- [Parse the results](#section/Getting-Started/Parse-the-results)

<div class="alert alert-info">
  <b>Note: </b>Please reach out to <a href="mailto:clients@checkr.com">clients@checkr.com</a> before you start integrating with our API to learn about our approval process for production.
</div>

## Get credentialed

Before gaining access to the Checkr APIs and Dashboard, you must be properly credentialed to request background checks. Work with your Customer Support Representative to provide the required documentation, and complete the credentialing process.

For more information, see [Getting credentialed](#section/Introduction/Get-credentialed) above.

## Request a Staging Account

Checkr provides customers with the option of a “staging account” that can be used to test your integration and use the Checkr Dashboard prior to deploying your integration to your production account. The staging account can be set up to match the settings from your production account and allows for submission of background check orders without incurring any billable events. To accomplish this, Checkr uses candidate “mocked” data setups that result in predefined background check results, mimicking the most common outcomes you will encounter in your production account.

Once your staging account has been created, Checkr will provide you with a document containing this mocked candidate data.

### Request a staging account

Use our [Submit a request form](https://help.checkr.com/hc/en-us/requests/new?ticket_form_id=360004180714) to request a staging account. Enter the following information:

1. <b>How can we help?: </b>select "I need assistance configuring my account", then select "Other".

2. <b>Topic: </b>enter "Staging account setup request"

3. <b>Description: </b>Please enter the following information:

    - Admin user for staging: <i>Provide the email address to be used as the initial Admin account for this requested staging account.</i>

    - Checkr production Admin: <i>Provide the email address for one of the Admin users of your Checkr Dashboard account.</i>

New staging accounts are typically created within 1-2 business days of a submitted request.

### Configure your staging account

Upon successful creation of the staging account, the email address specified in the [staging account request submission](https://help.checkr.com/hc/en-us/requests/new?ticket_form_id=360004180714) will receive an email from Checkr providing a temporary password to the account and allowing the recipient to create a permanent password. This initial user will have an Admin user role which allows them to invite other users to the account as they see fit.

Once you have Admin access to the staging account, go to <b>Account Settings > Developer Settings</b>. On this page, in the “API keys” section click <b>Create Key</b> and choose <b>Secret</b>. Use the resulting API key to authenticate all of your API calls to this staging account.

To enable webhooks for the account, from the <b>Account Settings > Developer Settings </b> page scroll down to <b>New Webhook</b>. Enter a URL and click <b>Add </b>to create a new webhook. You may also use this page to select the webhook notifications you wish to receive from Checkr.

![](images/AccountSettingsDevelopersWebhooks.png)

The staging account’s API calls, responses, and webhooks follow the same pattern and response structure as those of the production environment.

<b>Note: </b>The staging account uses the API host URL: https://api.checkr-staging.com/v1 for all calls.

#### Testing Checkr's functions and features

To facilitate building with the Checkr API, Checkr staging accounts support a number of mocked candidate profiles that will return predictable results. This allows you to test a number of different report outcomes and other workflows before moving your integration to your production account. To ensure the desired outcome, you must enter the candidate data exactly as provided in this mocked candidate data document or the resulting report will remain in `pending` status indefinitely.

Reports created in the staging account will typically complete within minutes of submission, though this can vary depending upon the relative load on the staging environment servers.

<b>Note: </b>Checkr’s product and development teams also use the staging environment to test new functionality. It is therefore possible that one or more of the mocked candidate records may not return the expected results. If you encounter unexpected returns for a mock data candidate, please test a different candidate from the mocked data document with a similar predefined outcome. If the problem persists, reach out to your Checkr Customer Support Manager to troubleshoot the issue.

### Uses and limitations of the staging account

The staging account is built to mimic the production environment and allow developers to build without running production background screenings and incurring a charge. Staging account uses mocked candidate data, and does not support the following functionality available in the production environment:

- Post adverse action is not supported
- Invitations do not expire
- Invoices are not created
- Analytics are not available

Please reach out to your Checkr Account Executive or Customer Success Manager if you require additional status, report, or state test cases.

## Get your API key

Once you have access set up to log into Checkr, go to [Developer Settings](https://dashboard.checkr.com/account/developer_settings) in the Checkr Dashboard. Click <b>Create Key > Secret </b>to generate a new Secret Key for your staging environment.

Your production API key is also available from this [Developer Settings](https://dashboard.checkr.com/account/developer_settings) page. Note that your production key will not be enabled for Reports until you contact clients@checkr.com and request that your account be enabled for live requests.

For more information on using Checkr's Staging environment, see the [Requesting a Staging Account](#section/Getting-Started/Request-a-Staging-Account) section below.

## Set up a local API client

Checkr provides support for several API clients, allowing you to explore the Checkr APIs. Download and install [Postman](https://www.postman.com/downloads/) or [Insomnia](https://docs.insomnia.rest/), then click the buttons below to install the Checkr APIs. Or use our [OAS3 API spec](https://api.redocly.com/registry/bundle/checkr/Checkr%20Public%20API/v1/openapi.yaml) to work with the tooling of your choice.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/17709267-82bc3552-fc3c-4cf0-a11a-071ba6beb5bd?action=collection%2Ffork&collection-url=entityId%3D17709267-82bc3552-fc3c-4cf0-a11a-071ba6beb5bd%26entityType%3Dcollection%26workspaceId%3D46c6cc7f-9630-4414-bd15-0b2cfc79b7b9)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Checkr&uri=https%3A%2F%2Fapi.redocly.com%2Fregistry%2Fbundle%2Fcheckr%2FCheckr%2520Public%2520API%2Fv1%2Fopenapi.yaml)

### Configure your API client

Configure your API client using the API key from the [Developer Settings](https://dashboard.checkr.com/account/developer_settings) page in your Checkr Dashboard. Then use your local client to execute any Checkr API requests. We provide sample parameters and payloads throughout these developer guides to help you in your journey.

<b>Note: </b>Checkr APIs are updated frequently. Use your selected method to reimport our APIs to evaluate our most recent versions.

Checkr API host URLs:
  * Production: https://api.checkr.com/v1
  * Staging (if you have been given access): https://api.checkr-staging.com/v1

## Authenticate with Checkr

<PullRight>

##### Example authentication

```sh
$ curl https://api.checkr.com \
    -u YOUR_SECRET_API_KEY:
```
</PullRight>

Use HTTP Basic authentication to authenticate with Checkr, with your API key as the username and an empty password. When using `curl`, use the `-u` option to specify your API key. (Note the colon following the API key in the examples. It tells cURL to send an empty password.)

Note that staging environment requests are free and return fake data. Once you are production-ready, please email clients@checkr.com and we will enable live requests.

## Create a Candidate

<PullRight>

##### Create a Test Candidate

```sh
$ curl -X POST https://api.checkr.com/v1/candidates \
    -u [YOUR_API_KEY]: \
    -d first_name=Michael \
    -d middle_name=Gary \
    -d last_name=Scott \
    -d email=michael.scott@dundermifflin.com \
    -d phone=2035408926 \
    -d zipcode=06831 \
    -d dob=1964-03-15 \
    -d ssn=111-11-2001 \
    -d driver_license_number=981736076 \
    -d driver_license_state=CT \
    -d copy_requested=true \
    -d 'work_locations[][country]=US'
```
</PullRight>

Create a Candidate by passing the required PII to Checkr.

Remember to replace `"YOUR_SECRET_API_KEY"` with <b>your </b> Secret API key in the cURL example on the right.
See [Candidates](#tag/Candidates) for more details on creating Candidates.

**Notes:**

- The Candidate object represents the candidate to be screened.
- The `copy_requested` boolean captures whether or not the candidate has requested a copy of their background check upon completion. If `true`, Checkr will automatically send a copy of the background check to the passed email address on your behalf.
- If using a [Checkr-hosted candidate experience](#section/Introduction/Checkr-hosted-candidate-experience), the only strictly required parameter for creating a Candidate in Checkr is `email`. We recommend that the candidate's phone number also be provided when creating the Candidate object, as it will be required to authenticate the candidate when they log into the Candidate Portal.
- If using a [custom self-hosted flow](#section/Introduction/Self-hosted-candidate-experience), the required attributes include `first_name`, `middle_name` or `no_middle_name`, `last_name`, and `dob`.
- If the Report's package includes any criminal check, `ssn` and `zipcode` are required attributes.
- If requesting a Motor Vehicle Report, Checkr requires `driver_license_number` and `driver_license_state`.
- Other Candidate-specific parameters are defined in the [Candidate resource](#operation/createCandidate) below.

### Candidate creation response

<PullRight>

##### Test Candidate creation response

```json
{
  "id":"551564b7865af96a28b13f36",
  "object":"candidate",
  "uri":"/v1/candidates/551564b7865af96a28b13f36",
  "created_at":"2018-08-17T01:08:18Z",
  "first_name":"Michael",
  "last_name":"Scott",
  "middle_name":"Gary",
  "mother_maiden_name":null,
  "dob":"1964-03-15",
  "ssn":"XXX-XX-2001",
  "email":"michael.scott@dundermifflin.com",
  "zipcode":"06831",
  "phone":"2035408926",
  "driver_license_state":"CT",
  "driver_license_number":"981736076",
  "copy_requested":true,
  "previous_driver_license_state":null,
  "previous_driver_license_number":null,
  "adjudication":null,
  "custom_id":null,
  "no_middle_name":false,
  "report_ids":[],
  "geo_ids":[]
}
```
</PullRight>

Checkr responds immediately with the resulting Candidate object, which includes the ID of the Candidate and a URI that points to the new Candidate object. Store the ID for this new Candidate object, which you'll need when creating a Report in the next step.

<!--<RedocResponse pointer={"#/components/responses/CandidateCreated"} />-->

## Create an Invitation

<PullRight>

##### Create a Test Invitation

```sh
$ curl -X POST https://api.checkr.com/v1/invitations \
      -u [YOUR_API_KEY]: \
      -d candidate_id=551564b7865af96a28b13f36 \
      -d package=dunder_mifflin_executive \
      -d node=CHLD_e7c3ab7bf4ad \   // only if nodes exist on the account
      -d work_locations[][state]=CA \   // state required, city optional
      -d work_locations[][city]=San+Francisco
```

</PullRight>

Use the [Invitations](#tag/Invitations) resource to order a background check using the Checkr-Hosted Apply Flow. Checkr will send an email to the candidate, inviting them to provide their information and consent. Once the invitation is completed a Report is automatically created. The invitation is valid for 7 days, during which Checkr will send a follow-up notice every 24 hours, reminding the candidate to complete their invitation. If 7 days pass and the candidate has not yet completed the invitation, the invitation will expire and you must create a new invitation to proceed with the candidate.

Parameters required to [Create an invitation](#operation/createInvitation):

*   `candidate_id`: the ID of the candidate for whom the Invitation is created.
*   `package`: the Package to use for the background check.
*   `work_locations`: the candidate's work location, described using country, state, and city. (ISO-3166 alpha-2 format country code, two letter state code, and the name of the city)
*   `node` (optional): the `custom_id` of the node associated with the background check. Required if any nodes exist on the account.

The `work_location` parameter is used by Checkr to determine compliance requirements for background check reports ordered through the Checkr Hosted Apply Flow. Checkr uses the candidate work location to apply the appropriate state- and city-based fair hiring laws, disclosures, and adverse action procedures. If a city is not provided, Checkr uses the state-based regulation.

### Invitation creation response

<PullRight>

##### Test Invitation creation response

```json
{
    "id": "551564b7865af96a28b13f36",
    "object": "invitation",
    "uri": "/v1/invitations/551564b7865af96a28b13f36",
    "invitation_url":
"https://apply.checkr.com/invite/try-checkr/290f9d6d6e46/test",
    "status": "pending",
    "created_at": "2015-05-14T17:45:34Z",
    "expires_at": "2015-05-21T17:45:34Z",
    "completed_at": null,
    "deleted_at": null,
    "package": "dunder_mifflin_executive",
    "candidate_id": "551564b7865af96a28b13f36",
    "report_id": null
    "tags": []
}
```

</PullRight>

Use the Checkr Candidate ID you have retrieved from [Create a Candidate](#section/Getting-Started/Create-a-Candidate), the Package “slug” (as selected in step [Selecting Packages](#tag/Working-with-Packages)), and the candidate’s work location to create an Invitation.

<b>Note: </b>Checkr requires Candidates to provide only information that is required for the screenings contained in the Package (such as SSN for criminal screenings, driver license number and state for MVR).


Store the resulting Report ID and any of the requested Screening IDs. The ID for this new Report object is required to retrieve the Report. (Checkr will return IDs for all Screenings included in the requested Package. All other Screening IDs will be returned `null`.)

## Listen for webhooks

<PullRight>

##### Test webhook response

```json
{
  "id": "507f1f77bcf86cd799439011",
  "object": "event",
  "type": "report.completed",
  "created_at": "2014-01-18T12:34:00Z",
  "data": {
    "object": {
      "id": "4722c07dd9a10c3985ae432a",
      "object": "report",
      "uri": "/v1/reports/532e71cfe88a1d4e8d00000d",
      "created_at": "2014-01-18T12:34:00Z",
      "received_at": "2014-01-18T12:34:00Z",
      "status": "complete",
      "result": "clear",
      "package": "driver_pro",
      "source": "api",
      "candidate_id": "e44aa283528e6fde7d542194",
      "ssn_trace_id": "539fd88c101897f7cd000001",
      "sex_offender_search_id": "539fd88c101897f7cd000008",
      "national_criminal_search_id": "539fd88c101897f7cd000006",
      "county_criminal_search_ids": [
        "539fdcf335644a0ef4000001",
        "532e71cfe88a1d4e8d00000c"
      ],
      "state_criminal_search_ids": [
        "539fdcf335644a0ef4000003",
        "532e71cfe88a1d4e8d000004"
      ],
      "motor_vehicle_report_id": "539fd88c101897f7cd000007"
    }
  },
  "account_id": "8e122cc56b8fa82d33c6118a"
}
```
</PullRight>

If webhooks are enabled, Checkr pushes a status change webhook event to the customer account's webhook URL with the structure shown in the Test Webhook Response to the right.

Use the resulting Report status (or other data elements) to execute subsequent workflows in your application or program.

Subscribing to webhooks is the recommended approach for accessing the report information and status, since it provides near real-time updates and frees the customer from having to poll our API for this information.

## Retrieve a Report

<PullRight>

##### Retrieve a Report

```sh
$ curl -X GET https://api.checkr.com/v1/reports/a13f4827d8711ddc75abc56ct
```
</PullRight>

While Checkr recommends listening to the **report.completed** webhook to retrieve the results of a report, you can also retrieve the same information by performing a GET request to the specific URL of the report.

Retrieve the Report created in the previous step by using your Secret API key and Report ID into the cURL command shown to the right.

### Retrieve Report response

<PullRight>

##### Retrieve Report response

```JSON
{
  "id": "a13f4827d8711ddc75abc56ct",
  "object": "report",
  "uri": "/v1/reports/a13f4827d8711ddc75abc56ct",
  "status": "complete",
  "result": "clear",
  "created_at": "2018-08-17T01:10:21Z",
  "completed_at": "2018-08-17T01:12:26Z",
  "revised_at": null,
  "upgraded_at": null,
  "turnaround_time": 52,
  "package": "dunder_mifflin_executive",
  "tags": [],
  "adjudication": null,
  "assessment": null,
  "source": "api",
  "candidate_id": "551564b7865af96a28b13f36",
  "county_criminal_search_ids": [],
  "municipal_criminal_search_ids": [],
  "document_ids": [],
  "drug_alcohol_clearinghouse_id": "5b64c62b67abb4002d3ec763",
  "federal_criminal_search_id": "5b64c62b67abb4002d3ec763",
  "global_watchlist_search_id": "5b64c5cf67abb400353ec6f7",
  "national_criminal_search_id": "5b64c5cf67abb400353ec6f5",
  "personal_reference_verification_ids": [],
  "professional_reference_verification_ids": [],
  "sex_offender_search_id": "5b64c5cf67abb400353ec6f6",
  "ssn_trace_id": "5b64c5cf67abb400353ec6f3",
  "state_criminal_search_ids": [],
  "terrorist_watchlist_search_id": "5b64c5cf67abb400353ec6f7",
  "facis_search_id": null,
  "arrest_search_id": null,
  "motor_vehicle_report_id": null,
  "self_disclosure_ids": []
}
```
</PullRight>

Note that the Report is now a full Report with a status of `clear`, indicating that no violations or criminal background have come up for this Report.

See [Embedding Resources](#section/Reference/Embedding-Resources) if you wish to embed the full contents of individual screenings (SSN Trace, Sex Offender Registry Search, Global Watchlist Search) in the server response. You can also retrieve those resources using the IDs provided in the server response.

## Parse the results

Webhook responses and completed Reports both contain the same information about the results of a criminal screening: the `status` of the report which can be `complete`, the `result` of the report which can be `null`, `clear`, or `consider`, and the assessment of the report, which can be `null`, `eligible`, `review`, or `escalated`.

A completed report with result of `clear` can be interpreted as that report having no items listed on the candidate's record that must be reviewed. A result of `consider` indicates that there are items on the candidate's record that may require consideration.

A report contains an `assessment` if the account has Assess enabled. The assessment is returned as `eligible`, `review`, or `escalated`, according to the customer rules defined in Assess. For more information, see [Assess](https://help.checkr.com/hc/en-us/articles/360051026954-Assess) in the Checkr User Guides.

In maintaining a compliant process as per FCRA legislation and EEOC guidelines, Checkr does not make any eligibility or hiring decisions (adjudicate) on our customers' behalf.

# Webhooks

<PullRight>

##### Generic webhook payload examples

_`include_object` is ON_

```json
{
  "id": "1002d6bca6acdfcbb8442178",
  "object": "event",
  "type": "object.event",
  "created_at": "2018-08-17T01:12:43Z",
  "webhook_url": "https://notify.company.com/checkr",
  "data": {
    "object": {
      "id": "a13f4827d8711ddc75abc56ct",
      "object": "object",
      "uri": "/v1/objects/a13f4827d8711ddc75abc56ct",
      "created_at": "2018-08-17T01:10:21Z",
      "completed_at": "2018-08-17T01:12:26Z",
      // [...] full object included
    }
  }
}
```
</PullRight>

Use webhooks to receive updates on objects created with the API and to kick off additional workflows based on these events. Each time an event that you subscribed to occurs, Checkr submits a POST request to the designated webhook URL with information about the event. When the `include_object` option is ON, it also includes the related object.

The User-Agent for the requests will have the prefix `Checkr-Webhook/`.

To receive webhooks, use the Checkr Dashboard to configure a Webhook URL in the [Developer Settings](https://dashboard.checkr.com/account/developer_settings).  A maximum of two webhook URLs may be configured. For more information about setting up webhooks, see the [Account Settings article](https://help.checkr.com/hc/en-us/articles/360010450474-Account-Settings#developer) in the Checkr Help Center.

<div class="alert alert-warning">
<b>Note: </b>Any webhook URL that fails to accept with a 2XX status code at least one request over a period of 60 days will be removed automatically - e.g. webhooks failing for 100% of the requests during 60 or more days. However if no requests have reached into a webhook URL, over the same period of time, it won't be removed.
</div>

## Attributes

<PullRight>

_`include_object` is OFF_


```json
{
  "id": "1002d6bca6acdfcbb8442178",
  "object": "event",
  "type": "object.event",
  "created_at": "2018-08-17T01:12:43Z",
  "webhook_url": "https://notify.company.com/checkr",
  "data": {
    "object": {
      "id": "a13f4827d8711ddc75abc56ct",
      "object": "object",
      "uri": "/v1/objects/a13f4827d8711ddc75abc56ct"
    }
  }
}
```
</PullRight>

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | ID of the event. |
| `object` | string | Defines the object type: `event`. |
| `type` | string | The type of event. Values include: `candidate.created`, `report.completed`. |
| `created_at` | timestamp iso 8601 format | Timestamp for the event. |
| `webhook_url` | string | Webhook URL. |
| `data` | hash | Object associated with the event. |
| `include_object` | boolean | Should the related object be attached to webhook payload. |

## Supported webhook URLs

| Type | Format | Description |
|------|--------|-------------|
| `HTTPS` | `https://(<user>:<password>@)<hostname>/<path>`<br>E.g.: `https://notify.company.com/checkr` | **Notes:** The endpoint to be reached must be public.<br>Webhook URLs must be HTTPS.<br>Basic Auth is supported by adding `username:password@` in front of the hostname, credentials must be URL escaped. |
| `SNS` | `sns://<key_id>:<access_key>@<region>/<topic_owner>/<topic_name>`<br>E.g.: `sns://AKI95AMUAD5K:a2n66fVKX7%2BYJKid3@us-east-1/12048/checkr` | AWS Simple Notification System (SNS)<br>**Notes:** Access Key must have <b>only </b>the Publish to SNS right in IAM.<br>Credentials must be URL escaped. |

## Responding to webhooks

Your endpoint should respond to webhooks as quickly as possible. To acknowledge receipt of a webhook, your endpoint must return a `2xx` HTTP status code. This status code should only indicate receipt of the message, not acknowledgment that it was successfully processed by your system. Any other information returned in the response headers or response body is ignored.

If a webhook is not successfully received for any reason, Checkr will continue trying to send it every minute for 10 minutes, then every hour for 24 hours.

Webhook logs can be found on the dashboard: https://dashboard.checkr.com/webhook_logs


## Order of events

Checkr does not guarantee the delivery of events in the order in which they are generated. For example, a report with a `result` of `consider` might generate the follow events:

```
report.completed
report.engaged
```

Your integration should not expect the delivery of these events to be in this order and should handle this accordingly. For example, you can fetch the report object, and look at `report.assessment` if you happen to receive the `report.completed` event later.

## Securing webhooks

For greater security, verify that the requests you receive come from Checkr.

We pass along a hash signature with each request in the header X-Checkr-Signature. The hash signature is generated with the HMAC algorithm, using your API key as a key and SHA256 digest mode. When you receive a request, you can compute a hash and ensure that the one from Checkr matches.

**Note:** Accounts without an API key will have X-Checkr-Signature set to "Please create an API key to check the authenticity of our webhooks."

**Example hash signature computation:**

`printf "$compact_json" | openssl sha256 -hmac "$PARTNER_APP_CLIENT_SECRET"`

In this example, `$compact_json` is the “non-pretty print” version of a JSON object. For example, you can get the compact version of a json file with the `jq` tool with: `compact_json=$(jq -c < example_response.json)`.

Code examples on how to do this can be found [here](https://github.com/checkr/webhook-verification-examples/).

## Guarding against duplicate and missed report notifications

While webhooks are helpful for updates, they are not foolproof. In some cases, report updates can be sent in rapid succession based on multiple events within the Checkr environment, and may be "mis-heard". For robust webhook handling, we recommend that you account for the following:

- Duplicate reports (idempotency)
- Webhook misses

As a best practice, Checkr recommends that you build a safety net to account for duplicate reports. One option might be to build in a function ahead of the status tracker, which copies only one `report.completed` update per Candidate or Report. This works well with an additional time threshold assigned. (For example, a report is only considered a duplicate if it's within 60 minutes of a previous iteration of that report.)

To address missed webhook updates, you may also consider adding a function to send an alert if no `report.completed` update is sent within a certain number of days.

## Candidate events

<PullRight>

##### Example Candidate event webhook payload

```json
{
  "id": "58f8e550d991bb000db04005",
  "object": "event",
  "type": "candidate.created",
  "created_at": "2017-04-20T16:44:00Z",
  "webhook_url": "https://yourcompany.com/checkr/incoming",
  "data": {
    "object": {
      "id": "c373384e71a9a02098cb7421",
      "object": "candidate",
      "uri": "/v1/candidates/e44aa283528e6fde7d542194",
      "created_at": "2017-04-18T18:37:34Z",
      "first_name": "John",
      "last_name": "Smith",
      "middle_name": "Alfred",
      "mother_maiden_name": null,
      "dob": "1990-10-31",
      "ssn": "XXX-XX-1111",
      "email": "john.smith@example.org",
      "zipcode": "48071",
      "phone": "5555555555",
      "driver_license_state": "CA",
      "driver_license_number": "F111111",
      "copy_requested": true,
      "previous_driver_license_state": null,
      "previous_driver_license_number": null,
      "adjudication": "engaged",
      "custom_id": null,
      "no_middle_name": false,
      "report_ids": [
        "4722c07dd9a10c3985ae432a"
      ],
      "geo_ids": [],
      "metadata": {
        "custom_key": "custom_value"
      }
    }
  },
  "account_id": "e9b18321a51bdab376045be8"
}
```
</PullRight>

| Event | Description |
|-------|-------------|
| `candidate.created` | A new Candidate has been created. |
| `candidate.id_required` | An exception has been raised requiring a copy of the Candidate's identification. |
| `candidate.driver_license_required` | An exception has been raised requiring a copy of the Candidate's driver license. |
| `candidate.updated` | A Candidate has been updated. |
| `candidate.pre_adverse_action` | An Adverse Action has been initiated on the Candidate. |
| `candidate.post_adverse_action` | An Adverse Action has been completed on the Candidate. |

## Invitation events

<PullRight>

##### Example Invitation event webhook payload

```json
{
  "id": "1002d6bca6acdfcbb8442178",
  "object": "event",
  "type": "invitation.expired",
  "created_at": "2017-04-20T16:44:00Z",
  "webhook_url": "https://yourcompany.com/checkr/incoming",
  "data": {
    "object": {
      "id": "16241770f7f7be1c57c85176",
      "status": "expired",
      "uri": "/v1/invitations/16241770f7f7be1c57c85176",
      "invitation_url": "https://apply.checkr.com/invite/yourcompany/7499b8c558a6",
      "completed_at": null,
      "deleted_at": null,
      "expires_at": "2017-05-21T17:45:34Z",
      "package": "tasker_pro",
      "object": "invitation",
      "created_at": "2017-05-14T17:45:34Z",
      "candidate_id": "fcb0084f6cb2423c069a35b3",
      "report_id": null
    }
  },
  "account_id": "e9b18321a51bdab376045be8"
}
```
</PullRight>

| Event | Description |
|-------|-------------|
| `invitation.created` | An Invitation has been created. |
| `invitation.completed` | An Invitation has been completed. |
| `invitation.expired` | An Invitation has expired. |
| `invitation.deleted` | An Invitation has been canceled. |

## Verification events

<PullRight>

##### Example Verification event webhook payload

```json
{
  "id": "id",
  "object": "event",
  "type": "verification.processed",
  "created_at": "2018-07-12T00:06:40Z",
  "data": {
    "object": {
      "id": "verification_id",
      "object": "verification",
      "uri": "/v1/reports/report_id/verifications/verification_id",
      "created_at": "2018-07-12T00:06:39Z",
      "completed_at": "2018-07-12T00:17:02Z",
      "processed_at": "2018-07-12T00:17:04Z",
      "verification_type": "ssn_confirmation",
      "verification_url": "https://verifications.checkr.com/verifications/verification_id",
      "report_id": "report_id"
    }
  },
  "account_id": "account_id"
}
```
</PullRight>

Verification events are issued during the [Exception](https://help.checkr.com/hc/en-us/articles/217114247-Exceptions-Addressing-data-discrepancies-in-reports) process when a candidate is issued or has responded to a request to verify submitted PII.

Verification events are issued for exceptions which occur to ask candidates to confirm their Social Security Number, Driver License information, or Education and Employment Verification information.

The list of possible verification types that are in the webhook payload (verification_type inside the data object) can be found [here](#section/Reference/Verification-Types).

**Note:** When verifications are automatically processed, and do not require manual input, the `verification.processed` webhook is sent immediately after the `verification.completed` webhook. These two webhooks may not arrive “in order”.

| Event | Description |
|-------|-------------|
| `verification.created` | A verification is created and a request to upload a document or enter the data is forwarded to the candidate. |
| `verification.completed` | A document is uploaded or data is entered by the candidate. |
| `verification.processed` | The data gathered by the verification is processed manually or automatically and a decision is made for the continuation of the background check. |

## Report events

<PullRight>

##### Example Report event webhook payload

```json
{
  "id": "507f1f77bcf86cd799439011",
  "object": "event",
  "type": "report.completed",
  "created_at": "2014-01-18T12:34:00Z",
  "webhook_url": "https://yourcompany.com/checkr/incoming",
  "data": {
    "object": {
      "id": "4722c07dd9a10c3985ae432a",
      "object": "report",
      "uri": "/v1/reports/532e71cfe88a1d4e8d00000d",
      "created_at": "2014-01-18T12:34:00Z",
      "received_at": "2014-01-18T12:34:00Z",
      "status": "complete",
      "result": "clear",
      "package": "driver_pro",
      "candidate_id": "e44aa283528e6fde7d542194",
      "ssn_trace_id": "539fd88c101897f7cd000001",
      "sex_offender_search_id": "539fd88c101897f7cd000008",
      "national_criminal_search_id": "539fd88c101897f7cd000006",
      "county_criminal_search_ids": [
        "539fdcf335644a0ef4000001",
        "532e71cfe88a1d4e8d00000c"
      ],
      "state_criminal_search_ids": [
        "539fdcf335644a0ef4000003",
        "532e71cfe88a1d4e8d000004"
      ],
      "motor_vehicle_report_id": "539fd88c101897f7cd000007"
    }
  },
  "account_id": "e9b18321a51bdab376045be8"
}
```
</PullRight>

| Event | Description |
|-------|-------------|
| `report.created` | A new Report has been created. |
| `report.updated` | A Report has been updated while the background check is run. This event is triggered on select update events, which include: <ul><li>Report Estimated Completion Time changed</li><li>Drug Screening update status event created</li></ul> |
| `report.canceled` | A Report has been canceled. |
| `report.upgraded` | A Report has been upgraded. Upgrades can be triggered either from an API call or from the Dashboard ("Upgrade" button). This is useful if you want to run a package (such as an MVR) and then upgrade it on completion (for example: add a County Criminal Search). |
| `report.completed` | A Report has been completed. |
| `report.suspended` | A Report has been suspended. Checkr is waiting for the candidate to provide additional documentation. |
| `report.resumed` | A Report has resumed. (The candidate has provided documentation to a previously "suspended" Report.) |
| `report.disputed` | A Report has been disputed by a candidate. Once a dispute has been completed, Checkr will trigger the `report.completed` webhook again with the appropriate Report status. |
| `report.pre_adverse_action` | The Pre-Adverse Action notice has been sent to the candidate of that report. |
| `report.post_adverse_action` | The Post-Adverse Action notice has been sent to the candidate of that report. |
| `report.engaged` | A Report has been adjudicated as "engaged". Use this event to track either all candidates you have officially engaged, or simply those candidates with a "consider" background check report that you have engaged. This can be triggered either from an API call or from the dashboard ("Engage" button). |

## Adverse Action events

<PullRight>

##### Example Adverse Action event webhook payload

```json
{
  "id": "5c4fee84d5abd60049eaa4fe",
  "object": "event",
  "type": "adverse_action.notice_not_delivered",
  "created_at": "2019-01-29T06:11:16Z",
  "data": {
    "object": {
      "id": "5c4f46eb805e59e228baacdd",
      "object": "adverse_action",
      "uri": "/v1/adverse_actions/5c4f46eb805e59e228baacdd",
      "status": "pending",
      "created_at": "2019-01-28T18:16:11Z",
      "canceled_at": null,
      "post_notice_scheduled_at": null,
      "post_notice_ready_at": "2019-02-04T18:16:11Z",
      "delivery": {
        "state": "error",
        "updated_at": "2019-01-29T06:11:15Z",
        "reason": "No MX for bad-email-domain-client.com"
      },
      "individualized_assessment_engaged": false,
      "report_id": "report_id",
      "adverse_items": [
        {
          "id": "62532b9f6dd2279acc5eb3574bad5bc085892ecc",
          "object": "adverse_item",
          "text": "** ACCIDENT **"
        },
        {
          "id": "418759b62961971c0ce8d7a6858b6c6f457400d5",
          "object": "adverse_item",
          "text": "** ACCIDENT **"
        },
        {
          "id": "e911042a437d735bbcbb6a98ab500bc62fc2b88e",
          "object": "adverse_item",
          "text": "FAILURE TO WEAR SEAT BELT"
        },
        {
          "id": "09d83492f6a15b41e3e5c48a970df3a4f53e660c",
          "object": "adverse_item",
          "text": "OBSTRUCTING PASSAGE OF OTHER VEHIC"
        }
      ]
    }
  },
  "account_id": "account_id"
}
```
</PullRight>

| Event | Description |
|-------|-------------|
| `adverse_action.notice_not_delivered` | The Adverse Action notice is confirmed to be undeliverable to the candidate of that report. User action is required. |

## Package events

<PullRight>

##### Example Package event webhook payload

```json
{
  "id": "1002d6bca6acdfcbb8442178",
  "object": "event",
  "type": "package.created",
  "created_at": "2017-04-20T16:44:00Z",
  "webhook_url": "https://yourcompany.com/checkr/incoming",
  "data": {
    "object": {
      "id": "e44aa283528e6fde7d542194",
      "object": "package",
      "uri": "/v1/packages/e44aa283528e6fde7d542194",
      "apply_url": "https://apply.checkr.com/apply/customer-services-inc/532c20ea819b",
      "created_at": "2014-01-18T12:34:00Z",
      "deleted_at": null,
      "name": "Driver Pro",
      "slug": "driver_pro",
      "price": 6500,
      "screenings": [
        {
          "type": "ssn_trace",
          "subtype": null
        },
        {
          "type": "county_criminal_search",
          "subtype": "7years"
        },
        {
          "type": "national_criminal_search",
          "subtype": "standard"
        },
        {
          "type": "sex_offender_search",
          "subtype": null
        },
        {
          "type": "global_watchlist_search",
          "subtype": null
        },
        {
          "type": "motor_vehicle_report",
          "subtype": null
        }
      ]
    }
  }
}
```
</PullRight>

| Event | Description |
|-------|-------------|
| `package.created` | A Package has been created. |
| `package.updated` | A Package has been updated. |
| `package.deleted` | A Package has been deleted. |

## Continuous Check events

<PullRight>

##### Example Continuous Check event webhook payload

```json
{
  "id": "6164822db059440001101d93",
  "object": "event",
  "type": "continuous_check.confirmation_required",
  "created_at": "2021-10-11T18:27:57Z",
  "data": {
    "object": {
      "object": "continuous_check",
      "id": "d56cdf24dca36bd1cb65aebe",
      "candidate_id": "7c445ec8dd78d534436c6ead",
      "created_at": "2021-09-02T17:22:17Z",
      "node": "zpy8orej4r614ize",
      "type": "mvr",
      "work_locations": [
        {
          "country": "US",
          "state": "CA",
          "city": "San Francisco"
        }
      ]
    }
  },
  "account_id": "57f79ea983381984e6a6e61a"
}
```

</PullRight>

| Event | Description |
|-------|-------------|
| `continuous_check.subscription_error` | An error occurred when attempting to enroll a Candidate in Continuous MVR. |
| `continuous_check.confirmation_required` | A Candidate has been unenrolled from Continuous MVR due to stale or invalid PII. The Candidate sumbitted updated information through the Checkr exception process. Action is required to re-enroll the Candidate. |

## Form I-9 events

<PullRight>

##### Example I9 Verification event webhook payload

```json
{
  "id": "58f8e550d991bb000db04005",
  "object": "event",
  "type": "formI9.updated",
  "created_at": "2023-11-20T16:44:00Z",
  "data": {
    "object": {
      "id": "c373384e71a9a02098cb7421",
      "object": "formI9",
      "uri": "/v1/i9/forms_i9/e44aa283528e6fde7d542194",
      "candidate_id": "3ae7e278beb24d14a3785e2dd02cca49",
      "event_timestamp": "2023-11-20T16:44:00Z",
      "status": "section_1_completed"
    },
  },
}
```

</PullRight>

| Event | Description |
|-------|-------------|
| `form_i9.created` | A new Form I9 has been created. |
| `form_i9.updated` | A in progress Form I9 has received an update. This update will usually mean a change in the section of the report e.g section 1 is signed by a candidate or employee. It can also mean, for those forms created with a worksite that has E-Verify enabled, a change in the E-Verify status. <br/><br/> You can find information about Form I-9 statuses in [the Form I-9 reference section](#section/Reference/Form-I-9-definitions-lessBETAgreater) |
| `form_i9.completed` | A Form I9 has been completed. |
| `form_i9.deleted`   | A Form I9 has been deleted. |

# Checkr Partners

Checkr partners with leading Staffing, On-Demand, Applicant Tracking Systems, and HR Systems to bring background checks to your customers. As a Checkr Partner, you can leverage the Checkr API to seamlessly connect your customers' Checkr accounts and integrate the background check process into your applications. Checkr's self-serve sign-up flow is fast, easy, and allows your customers to start running background checks within minutes after their account is credentialed.

If you are interested in partnering with Checkr, submit our <a href="https://checkr.com/become-a-partner" target="_blank">Checkr Partner Application form</a> to connect with our Business Development team.

## Checkr Partner Developer Guides

Please see our <a href="https://docs.checkr.com/partners/" target="_blank">Checkr Partner Developer Guides</a> for more complete information on building your partner integration with Checkr, and allowing your customers to use Checkr functionality from within your app.

# Advanced Features

The Checkr API offers significant flexibility and opportunity for developers to build a unique background screening program tailored to their product or business needs. This section describes additional features and capabilities that our customers find valuable.

## Creating a fully custom apply flow

Checkr allows customers to create fully custom application flows for their candidates, using the [Reports](https://docs.checkr.com/#tag/Reports) resource to build a self-hosted flow.

In this flow, you must collect and store both the candidate’s information and their consent within your application. You must also provide candidates the appropriate state- and city-specific disclosures for each screening type. Once obtained, you must store your candidates’ consent to the background check, both to maintain proof that consent was granted, and to provide proof of consent for Checkr’s ongoing evaluation of customer compliance (annual compliance audits).

Once all required information is present on the Candidate resource, creating a Report will initiate the background check.

For more information on your obligations under FCRA, and Checkr’s responsibilities as a Consumer Reporting Agency (CRA), check out our [Compliance resources](https://help.checkr.com/hc/en-us/sections/203637107-Compliance) in the Help Center, particularly our articles about [obligations under FCRA](https://help.checkr.com/hc/en-us/articles/216557368-What-is-the-Fair-Credit-Reporting-Act-FCRA-) and [disclosures and authorizations](https://help.checkr.com/hc/en-us/articles/360000144867-Disclosure-and-authorization).

<b>Note: </b>Some screening types are not supported with the Reports flow, such as credit checks and complex occupational health screenings. Other screening types, like employment and education verifications, are supported but not recommended with this flow, as they require significant data entry. For more information, see [Reports](/#tag/Reports) below.

<PullRight>

##### Create a Report

```sh
$ curl -X POST https://api.checkr.com/v1/reports \
    -u [YOUR_API_KEY]: \
    -d package=dunder_mifflin_executive \
    -d candidate_id=551564b7865af96a28b13f36
```
</PullRight>

Create a Report for an existing Candidate object. Use your API key and Candidate ID in the cURL command shown to the right.

**Notes:**

 - The Report object represents a background check report.
 - Depending on the selected Package, a Report may include any number of requested Screenings.
 - Validation for inclusion of Candidate attributes (such as driver license number or SSN) is performed when you request a Report.
 - Information requirements depend strictly on the Package requested. (For more information, see [Packages](#tag/Packages), below.)
 - This object includes your certification to Checkr that appropriate disclosures and authorization (such as consent) have been obtained from your candidate.

### Report Creation response

<PullRight>

##### Test Report creation response

```json
{
  "id": "a13f4827d8711ddc75abc56ct",
  "object": "test_report",
  "uri": "/v1/reports/a13f4827d8711ddc75abc56ct",
  "status": "pending",
  "result": null,
  "created_at": "2018-08-17T01:10:21Z",
  "completed_at": null,
  "revised_at": null,
  "upgraded_at": null,
  "turnaround_time": null,
  "package": "dunder_mifflin_executive",
  "tags": [],
  "adjudication": null,
  "assessment": null,
  "candidate_id": "551564b7865af96a28b13f36",
  "county_criminal_search_ids": null,
  "document_ids": [
    "865de4344ac6d05209c83ef5"
  ],
  "federal_criminal_search_id": "5b64c62b67abb4002d3ec763",
  "global_watchlist_search_id": "5b64c5cf67abb400353ec6f7",
  "national_criminal_search_id": "5b64c5cf67abb400353ec6f5",
  "personal_reference_verification_ids": [],
  "professional_reference_verification_ids": [],
  "sex_offender_search_id": "5b64c5cf67abb400353ec6f6",
  "ssn_trace_id": "5b64c5cf67abb400353ec6f3",
  "state_criminal_search_ids": [],
  "terrorist_watchlist_search_id": "5b64c5cf67abb400353ec6f7",
  "facis_search_id": null,
  "arrest_search_id": null,
  "motor_vehicle_report_id": null
}
```
</PullRight>

Checkr responds immediately with the full Report object, which includes the ID of the Report and a URI that points to the new Report object.

Store the resulting Report ID and any of the requested Screening IDs. The ID for this new Report object is required to retrieve the Report. (Checkr will return IDs for all Screenings included in the requested Package. All other Screening IDs will be returned `null`.)

## Ordering Subscriptions or Continuous Check services

In addition to offering "point-in-time" background checks, Checkr offers ongoing check services through our Subscription and Continuous Check products.

A Subscription enables customers to order a repeating background check on a candidate on a user-defined time interval. Candidates must first complete an initial background check, after which customers may create a Subscription to repeat that background check on a user-defined interval. Subscriptions can be created, modified, or deleted both through the Checkr Dashboard and the Checkr API.

For more information, see [Subscriptions: Run recurring background checks](https://help.checkr.com/hc/en-us/articles/227394707-Subscriptions-Run-recurring-background-checks) in the Checkr Help Center, or the [Subscription](#tag/Subscriptions) resource below.

Continuous Checks allow customers to monitor their candidates' records. Continuous Check monitors real-time data sources, and looks for changes in a candidate's record. If Checkr identifies a change in the candidate's history, Continuous Check will automatically kick off follow-up searches in the appropriate jurisdictions and generate a new background check report.

For more information, see [Continuous Check: The new standard of safety](https://help.checkr.com/hc/en-us/articles/360016337054-Continuous-Check-The-new-standard-of-safety) in the Checkr Help Center, or the [Continuous Checks](#tag/Continuous-Checks) resource below. For information on using the Checkr Dashboard to order a Continuous Check package on a candidate, see [Continuous checks](https://help.checkr.com/hc/en-us/articles/4411414294167) in the Checkr Help Center.

While both Continuous Check and Subscriptions allow you to monitor your candidates' record, they should not be understood as equivalent to one another. Subscriptions generate a new report according to your defined cadence. Continuous Check continuously monitors multiple data sources, and generates a new report only if a change in your candidate's record is found. If you have additional questions about what makes the most sense for your business, please reach out to your Checkr Account Executive or Customer Success Manager.


## Upgrading a report

Checkr also offers the ability to "upgrade" a report based on a prior set of screening results. The most common use case for this feature is to order a Package that includes both a Motor Vehicle Record (MVR) and a County Criminal Search. The report can be "upgraded" to run the County Criminal Search only after the MVR returns with a result. Checkr facilitates the following workflow:

1.  Customer submits API request to Checkr for a candidate MVR
2.  Checkr fulfills MVR, submits webhook response to customer with screening results
3.  Customer determines if candidate passes or does not pass MVR requirements
4.  If candidate passes MVR requirements:
    - Customer submits second API request for Checkr to "upgrade" the MVR report to a full criminal screening report, submitting a `POST` request to Checkr's `/reports/{id}` endpoint with the same Report ID and the new Package to request
    - Checkr conducts the criminal screening as described in [Overview of API calls and callbacks](#api-calls)
5.  If the candidate does not pass MVR requirements:
    - Customer does not submit second API request to Checkr

For more information on upgrading a Report, please see [Update an existing Report](#operation/updateReport) below.

Please note: Only reports which include a Candidate SSN may be upgraded, and only within 30 days of Report creation. Attempts to upgrade a report which does not include an SSN will return a 400 error: "Candidate must have SSN to upgrade report." Requests to upgrade an older report will result in a 400 error, "Report too old to upgrade."

## Configuring encryption for the SSN resource

To use the [Candidate SSN endpoint](#operation/getCandidateSsn), you must generate an RSA key-pair for your account, and share the public key with Checkr. Checkr will use this public key to encrypt the SSN and securely share it with your integration.

### Generating a Key Pair

Run the following command in a bash session to generate a private key. This will generate a file named private.pem containing your private key.


`openssl genrsa -out private.pem -aes256 4096`


**Note:** if you generate your RSA key via an alternative method, we require a key size of at least 4096 bits for access to production SSN data.


Once your private key is generated, run the following command. This will generate a file named public.pem containing your public key.


`openssl rsa -in private.pem -out public.pem -outform PEM -pubout`


With both keys generated, send your **public key** to your Customer Success Manager. **Do not share your private key. If your private key is exposed let us know as soon as possible so that we can secure your candidates' information.**

# Reference

## Content-Type

<PullRight>

##### Example request
```sh
$ curl -X POST https://api.checkr.com/v1/candidates \
    -H "Content-Type: application/json" \
    -u 83ebeabdec09f6670863766f792ead24d61fe3f9: \
    -d '{"first_name": "John", "middle_name": "Alfred", "last_name": "Smith", "email": "john.smith@gmail.com"}'
```
</PullRight>
The `Content-Type` entity header is used to describe the media type of a resource. In requests, a `Content-Type` header tells the server what type of data is being sent. In responses, it tells the client what type of data the returned content actually is.

Our default is to accept data as **application/x-www-form-urlencoded** (which is typical for most websites you interact with), but you are free to send other data types, like **application/json**, as it suits you. Simply specify the `Content-Type` in the header of the request.

## Embedding Resources

<PullRight>

##### Example request

```sh
$ curl -X GET https://api.checkr.com/v1/reports/59b650f567e1dd0f01422b92\
    ?include=candidate,ssn_trace,county_criminal_searches \
    -u 83ebeabdec09f6670863766f792ead24d61fe3f9:
```
</PullRight>
By default, an API response contains the requested resource, and provides the IDs of related resources. You can also request related resources to be embedded in the initial response.

The `include` parameter specifies the names of resources that should be embedded in the response. Resources to embed must be comma-separated.

## Pagination

<PullRight>

##### Example paginated request

```sh
$ curl -X GET https://api.checkr.com/v1/candidates?page=2&per_page=25 \
    -u 83ebeabdec09f6670863766f792ead24d61fe3f9:
```

##### Example paginated payload
```json
{
  "data": [
    {
      "id": "e44aa283528e6fde7d542194",
      "object": "candidate",
      "uri": "/v1/candidates/e44aa283528e6fde7d542194",
      "created_at": "2014-01-18T12:34:00Z",
      "first_name": "John",
      "middle_name": "Alfred",
      "no_middle_name": false,
      "last_name": "Smith",
      "mother_maiden_name": null,
      "email": "john.smith@gmail.com",
      "phone": "5555555555",
      "zipcode": "90401",
      "dob": "1970-01-22",
      "ssn": "XXX-XX-4645",
      "driver_license_number": null,
      "driver_license_state": null,
      "previous_driver_license_number": null,
      "previous_driver_license_state": null,
      "copy_requested": false,
      "custom_id": null,
      "report_ids": []
    },
    {
      "id": "8b6eb2bf554ebbef7b6f885a",
      "object": "candidate",
      "uri": "/v1/candidates/8b6eb2bf554ebbef7b6f885a",
      "created_at": "2014-01-18T12:34:00Z",
      "first_name": "Michael",
      "middle_name": null,
      "no_middle_name": true,
      "last_name": "Johnson",
      "mother_maiden_name": null,
      "email": "michael.johnson@gmail.com",
      "phone": "5555555555",
      "zipcode": "94407",
      "dob": "1970-01-22",
      "ssn": "XXX-XX-8605",
      "driver_license_number": null,
      "driver_license_state": null,
      "previous_driver_license_number": null,
      "previous_driver_license_state": null,
      "copy_requested": false,
      "custom_id": null,
      "report_ids": []
    }
  ],
  "object": "list",
  "next_href": null,
  "previous_href": "http://api.checkr.com/v1/candidates?page=1&per_page=25",
  "count": 27
}
```

</PullRight>

Pagination is enabled for endpoints that return a list of records.

There are two parameters that control pagination: `page`, which specifies the page number to retrieve, and `per_page`, which indicates how many records each page should contain. The default value of `per_page` is 25 records.

| Parameters      | Description      |
| --------------- | ---------------- |
| `page`      | **integer** <br> greater than or equal to 1 |
| `per_page` | **integer** <br> between 0 and 100 |

Paginated responses include the following attributes:

| Attributes      | Description      |
| --------------- | ---------------- |
| `count`      | **integer** <br> the total number of items |
| `data` | **array** <br> list of objects |
| `next_href`      | **string** <br> URI to fetch the next page of results |
| `object`      | **string** <br> "list" |
| `previous_href`      | **string** <br> URI to fetch the previous page of results |

## Rate limiting

<PullRight>

##### Example rate limiting request

```sh
$ curl -I -X GET https://api.checkr.com/v1/reports/59b650f567e1dd0f01422b92 \
    -u 83ebeabdec09f6670863766f792ead24d61fe3f9:

< X-Ratelimit-Limit: 1200
< X-Ratelimit-Remaining: 9
< X-Ratelimit-Reset: 2018-02-02T16:39:00Z
```
</PullRight>
In order to provide a high-quality of service for all customers, our API is rate limited. The current limit is 1200 requests per minute across all endpoints. We reserve the right to adjust the rate limit for given endpoints.

If the rate limit is exceeded, the API responds with a `HTTP 429 "Too Many Requests"` status code. The response has a `X-Ratelimit-Reset` header that tells you when the rate limit count will reset.

Here are the headers related to rate limiting that our API returns for any requests:

| Header      | Description      |
| ----------- | ---------------- |
| `X-Ratelimit-Limit` | Number of requests allowed per minute |
| `X-Ratelimit-Remaining`      | Remaining number of requests allowed for the current minute |
| `X-Ratelimit-Reset`      | Time at which the rate limit count resets |

### Staying under the limit

Here are some recommendations to stay under the limit:

* Subscribe to Checkr webhooks to get updates about a report's activity instead of polling.
* If you do anticipate situations where you could exceed the limit, we recommend using an exponential backoff (wait 2 seconds, then 5, then 10, then 30, etc.) and retrying the API call.

## Idempotency support

<PullRight>

##### Example idempotent report creation request

```sh
$ curl -v -X POST https://api.checkr.com/v1/reports \
  -u 83ebeabdec09f6670863766f792ead24d61fe3f9: \
  -H 'Idempotency-Key: 40b23921-c005-4ec7-832a-3ae023dbbc11' \
  -d package=driver_pro \
  -d candidate_id=be529e5d8cc5ad26e655ce89
```
</PullRight>

The Checkr API supports idempotency in POST requests. Use this feature to safely repeat POST requests without accidentally creating the same reports or candidates multiple times.

First, provide an `Idempotency-Key: <key>` header to the POST request. This header value will be used server side to recognize retries of the same request.

The client side must then generate a unique value for every POST request, and re-use the same header value in any subsequent retry attempts. We recommend the use of V4 UUIDs to avoid collisions.

When serving the request with a new idempotency key, Checkr service will save the response (including status code, headers, body) for the first request if it is successful (2xx status), and return the saved response for later requests with the same idempotency key.

<b>Note: </b>The idempotency key expires after 24 hours. Retries with an expired idempotency key will be handled as new requests.

`409` HTTP status code will be received when another request with the same idempotency key is still being processed. Wait for the other request to complete before making a new request with the same idempotency key.


## Supported characters

The Checkr API supports alphanumeric character input, as well as accented characters and some punctuation marks.

Corresponding regex character ranges: `[a-zA-Z0-9ªµºÀ-ÖØ-öø-ÿ\-'., ]`

### Supported accented characters


ª|µ|º|À|Á|Â|Ã|Ä|Å|Æ
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Ç|È|É|Ê|Ë|Ì|Í|Î|Ï|Ð
Ñ|Ò|Ó|Ô|Ö|Ø|Ù|Ú|Û|Ü
Ý|Þ|ß|à|á|â|ã|ä|å|æ
ç|è|é|ê|ë|ì|í|î|ï|ð
ñ|ò|ó|ô|õ|ö|ø|ù|ú|û
ü|ý|þ|ÿ|'|.|,|-|


## Driver License validation

Checkr has compiled the following table of valid driver license number input per state. To avoid errors, we suggest that you implement driver license number validation for both the Candidates and Driver Licenses endpoints.

<table>
  <tr>
   <td><strong>State</strong>
   </td>
   <td><strong>Validation Criteria</strong>
   </td>
   <td><strong>Regex</strong>
   </td>
  </tr>
  <tr>
   <td>AL
   </td>
   <td>7-8 Numeric
   </td>
   <td>/\A\d{7,8}\z/
   </td>
  </tr>
  <tr>
   <td>AK
   </td>
   <td>7 Numeric
   </td>
   <td>/\A\d{7}\z/
   </td>
  </tr>
  <tr>
   <td>AZ
   </td>
   <td>(1 Alpha + 8 Numeric) OR 9 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{8}\z/ OR /\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>AR
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>CA
   </td>
   <td>1 Alpha + 7 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{7}\z/
   </td>
  </tr>
  <tr>
   <td>CO
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>CT
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>DE
   </td>
   <td>2-7 Numeric
   </td>
   <td>/\A\d{2,7}\z/
   </td>
  </tr>
  <tr>
   <td>DC
   </td>
   <td>7-9 Numeric
   </td>
   <td>/\A\d{7,9}\z/
   </td>
  </tr>
  <tr>
   <td>FL
   </td>
   <td>1 Alpha + 12 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{12}\z/
   </td>
  </tr>
  <tr>
   <td>GA
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>HI
   </td>
   <td>("H" + 8 Numeric) or 9 Numeric
   </td>
   <td>/\AH\d{8}\z/ OR /\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>ID
   </td>
   <td>(2 Alpha + 6 Numeric + 1 Alpha) or 9 Numeric
   </td>
   <td>/\A[A-Z]{2}\d{6}[A-Z]{1}\z/ OR /\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>IL
   </td>
   <td>1 Alpha + 11-12 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{11,12}\z/
   </td>
  </tr>
  <tr>
   <td>IN
   </td>
   <td>10 Numeric
   </td>
   <td>/\A\d{10}\z/
   </td>
  </tr>
  <tr>
   <td>IA
   </td>
   <td>9 Numeric or (3 Numeric + 2 Alpha + 4 Numeric)
   </td>
   <td>/(\A\d{9}\z)/ OR /(\A\d{3}[A-Z]{2}\d{4}\z)/
   </td>
  </tr>
  <tr>
   <td>KS
   </td>
   <td>"K" + 8 Numeric
   </td>
   <td>/\A[K]{1}\d{8}\z/
   </td>
  </tr>
  <tr>
   <td>KY
   </td>
   <td>1 Alpha + 8 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{8}\z/
   </td>
  </tr>
  <tr>
   <td>LA
   </td>
   <td>("0" + 7 Numeric) OR ("0" + 8 Numeric) OR 7 Numeric or 8 Numeric
   </td>
   <td>/\A[0]{0,1}\d{7,8}\z/
   </td>
  </tr>
  <tr>
   <td>ME
   </td>
   <td>7 Numeric
   </td>
   <td>/\A\d{7}\z/
   </td>
  </tr>
  <tr>
   <td>MD
   </td>
   <td>(1 Alpha + 12 Numeric) OR ("MD" + 11 Numeric)
   </td>
   <td>/\A[A-Z]{1}\d{12}\z/ OR /\AMD\d{11}\z/
   </td>
  </tr>
  <tr>
   <td>MA
   </td>
   <td>("SA" + 7 Numeric) OR ("S" + 8 Numeric) OR 9 Numeric
   </td>
   <td>\ASA\d{7}\z OR \AS\d{8}\z OR \A\d{9}\z
   </td>
  </tr>
  <tr>
   <td>MI
   </td>
   <td>1 Alpha + 12 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{12}\z/
   </td>
  </tr>
  <tr>
   <td>MN
   </td>
   <td>1 Alpha + 12 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{12}\z/
   </td>
  </tr>
  <tr>
   <td>MS
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>MO
   </td>
   <td>9 Numeric OR (1 Alpha + 5-9 Numeric) OR (3 Numeric + 1 Alpha + 6 Numeric)
   </td>
   <td>/(\A\d{9}\z)/ OR /(\A[A-Z]{1}\d{5,9}\z)/ OR /(\A\d{3}[A-Z]{1}\d{6}\z)/
   </td>
  </tr>
  <tr>
   <td>MT
   </td>
   <td>13 Numeric or 9 Alpha-Numeric or (3 Alpha + 10 Numeric)
   </td>
   <td>/(\A\d{13}\z)/ OR
<p>
/(\A(\d|[A-Z]){9}\z)/ OR \
/(\A[A-Z]{3}\d{10}\z)/
   </td>
  </tr>
  <tr>
   <td>NE
   </td>
   <td>1 Alpha + 3-8 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{3,8}\z/
   </td>
  </tr>
  <tr>
   <td>NV
   </td>
   <td>10 Numeric
   </td>
   <td>/\A\d{10}\z/
   </td>
  </tr>
  <tr>
   <td>NH
   </td>
   <td>(2 Numeric + 3 Alpha + 5 Numeric) OR ("NHL" + 8 Numeric)
   </td>
   <td>/(\A\d{2}[A-Z]{3}\d{5}\z)/ OR /(\ANHL\d{8}\z)/
   </td>
  </tr>
  <tr>
   <td>NJ
   </td>
   <td>1 Alpha + 14 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{14}\z/
   </td>
  </tr>
  <tr>
   <td>NM
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>NY
   </td>
   <td>9 Numeric OR 1 Alpha + 18 Numeric
   </td>
   <td>/(\A\d{9}\z)/ OR /(\A[A-Z]{1}\d{18}\z)/
   </td>
  </tr>
  <tr>
   <td>NC
   </td>
   <td>1-12 Numeric
   </td>
   <td>/\A\d{1,12}\z/
   </td>
  </tr>
  <tr>
   <td>ND
   </td>
   <td>9 Alpha-Numeric
   </td>
   <td>/\A(\d|[A-Z]){9}\z/
   </td>
  </tr>
  <tr>
   <td>OH
   </td>
   <td>2 Alpha + 6 Numeric OR 8 Numeric
   </td>
   <td>/\A[A-Z]{2}\d{6}\z/ OR /(\A\d{8}\z)/
   </td>
  </tr>
  <tr>
   <td>OK
   </td>
   <td>(1 Alpha + 9 Numeric) or 9 Numeric
   </td>
   <td>/(\A[A-Z]{1}\d{9}\z)/ OR /(\A\d{9}\z)/
   </td>
  </tr>
  <tr>
   <td>OR
   </td>
   <td>5-7 Numeric OR (1 Alpha + 6 Numeric)
   </td>
   <td>/(\A\d{5,7}\z)/ OR /(\A[A-Z]{1}\d{6}\z)/
   </td>
  </tr>
  <tr>
   <td>PA
   </td>
   <td>8 Numeric
   </td>
   <td>/\A\d{8}\z/
   </td>
  </tr>
  <tr>
   <td>PR
   </td>
   <td>5-7 Numeric OR 9 Numeric
   </td>
   <td>/\A\d{5,7}\z/ OR /\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>RI
   </td>
   <td>7-8 Numeric OR ("V" + 6 Numeric)
   </td>
   <td>/(\A\d{7,8}\z)/ OR /(\AV\d{6}\z)/
   </td>
  </tr>
  <tr>
   <td>SC
   </td>
   <td>3-10 Numeric
   </td>
   <td>/\A\d{3,10}\z/
   </td>
  </tr>
  <tr>
   <td>SD
   </td>
   <td>6-9 Numeric
   </td>
   <td>/\A\d{6,9}\z/
   </td>
  </tr>
  <tr>
   <td>TN
   </td>
   <td>7-9 Numeric
   </td>
   <td>/\A\d{7,9}\z/
   </td>
  </tr>
  <tr>
   <td>TX
   </td>
   <td>7-8 Numeric
   </td>
   <td>/\A\d{7,8}\z/
   </td>
  </tr>
  <tr>
   <td>UT
   </td>
   <td>4-10 Numeric
   </td>
   <td>/\A\d{4,10}\z/
   </td>
  </tr>
  <tr>
   <td>VT
   </td>
   <td>8 Numeric or (7 Numeric + "A")
   </td>
   <td>/(\A\d{8}\z)/ OR /(\A\d{7}A\z)/
   </td>
  </tr>
  <tr>
   <td>VA
   </td>
   <td>(1 Alpha + 8 Numeric) OR 9 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{8}\z/ OR /\A\d{9}\z/
   </td>
  </tr>
  <tr>
   <td>WA
   </td>
   <td>(4-8 Alpha + 2-3 Numeric + 2 Alpha-Numeric) OR ("WDL" + 9 Alpha-Numeric)
   </td>
   <td>/\A[A-Z*]{4,8}\d{2,3}(\d|[A-Z]){2}\z/ OR /\AWDL([A-Z]|\d){9}\z/
   </td>
  </tr>
  <tr>
   <td>WV
   </td>
   <td>7 Alpha-Numeric
   </td>
   <td>/\A([A-Z]|\d){7}\z/
   </td>
  </tr>
  <tr>
   <td>WI
   </td>
   <td>1 Alpha + 13 Numeric
   </td>
   <td>/\A[A-Z]{1}\d{13}\z/
   </td>
  </tr>
  <tr>
   <td>WY
   </td>
   <td>9 Numeric
   </td>
   <td>/\A\d{9}\z/
   </td>
  </tr>
</table>

## Email address validation

The Checkr API validates submitted email addresses using the industry standard [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322). The string length must be <=255, and the domain must be valid and configured to accept email. (For example: gmail.com is a valid domain, while gmeil.con is not.)

To avoid errors, we suggest that you validate emails used in your candidate creation requests.

## Form I-9 definitions


##### Workflow types

Workflow types are high-level flows the employee can select at the moment of creating an I9 form, it affects what will be the filling experience is from a candidate’s perspective.


| Workflow Type     | Description      |
| ----------- | ---------------- |
| `remote_section_1_only` | Employee will complete Section 1 on their own. Then Employer help them complete Section 2 on-site. |
| `employer_appointment`      | Employee will complete Section 1 on their own. Then Employer authorize a representative to help them complete Section 2. |
| `employee_appointment`      | Employee will complete Section 1 on their own. Then Employer authorize an employee-designated representative to help them complete Section 2. |

##### Form I9 Order Progress

Represents the current status of the I-9/e-Verify process.

| Status     | Description      |
| ----------- | ---------------- |
| `section_1_incomplete` | Indicates that the employee must complete Section 1. |
| `section_2_incomplete`    | Indicates that the employer/customer or the Authorized Representative (when applicable) must complete Section 2. |
| `awaiting_approval`     | Indicates that the Authorized Representative has completed Section 2 and the employer/customer must review and approve the I-9. |
| `everify_pending` | Indicates that the e-Verify process is in progress. |
| `everify_tnc_issued`    | Indicates a Tentative Non-Confirmation (TNC) e-Verify status, which requires action from the employer/customer. |
| `i9_complete`  | Indicates that the I-9/e-Verify process is complete. |


##### Form I9 Open Tasks

Represents tasks that must be completed by the employer/customer.

| Status     | Description      |
| ----------- | ---------------- |
| `no_action` | Indicates that there is no action to be taken by the employer/customer. |
| `complete_section_2`    | Indicates that the employer/customer must complete Section 2. |
| `appoint_section_2_representative`     | Indicates that the employer/customer must appoint an Authorized Representative to complete Section 2. |
| `accept_reject_i9` | Indicates that the employer/customer must accept or reject the I-9 after the Authorized Representative has completed Section 2.  |
| `check_user_email`    | Indicates that the employer/customer must check the employee's email address as a follow-up action to an e-Verify Tentative Non-Confirmation (TNC) case. |


## SSN validation

Checkr's product incorporates SSN field controls designed to not accept SSNs with the following characteristics:

* SSNs without exactly 9 numeric characters
* SSNs that start with 666 (666-34-3768)
* SSNs that start with 9 (967-65-4325)
* SSNs that are a single digit (111-11-1111)
* SSNs that are sequential digits (123-45-6789)

## Error codes

Checkr's API offers a number of error codes to facilitate your building and troubleshooting. Some common error codes include:

| Status Code | Response |
| ----------- | -------- |
| 400 | SSN is invalid |
| 400 | Zipcode is invalid |
| 400 | Email is not a valid email address |
| 400 | First name must only contain letters, numbers, spaces, hyphens, apostrophes, periods, and commas |
| 400 | Last name must only contain letters, numbers, spaces, hyphens, apostrophes, periods, and commas |
| 400 | Report is too old to upgrade |
| 400 | New package does not add any screenings |
| 400 | Candidate must have a driver license number and a driver license state for the package mvr |
| 400 | Report has a pre-existing adverse action. See https://docs.checkr.com/#operation/updateReport |
| 400 | SSN is invalid. TIN was provided. |
| 400 | SSN has already been taken |
| 400 | First name must only contain letters, numbers, spaces, hyphens, apostrophes, periods, and commas", "Last name must only contain letters, numbers, spaces, hyphens, apostrophes, periods, and commas |
| 400 | Candidate must_not have middle name when no_middle_name flag is set to true for the candidate report_id= |
| 400 | Report driver license state not supported or not enabled for account |
| 400 | Candidate must be at least 16 years old |
| 400 | Candidate must be at least 18 years old |
| 400 | Candidate must have SSN for the package driver_premium |
| 400 | Candidate has reached the limit of Reports allowed |
| 400 | Middle name must only contain letters, numbers, spaces, hyphens, apostrophes, periods, and commas. |
| 400 | Number Driver license number must only contain letters, numbers, spaces, hyphens, and asterisks |
| 400 | Candidate must have middle name when no_middle_name flag is set for the candidate report_id= |
| 400 | Number can't be blank, State can't be blank, State is not a valid US state |
| 400 | No middle name can not be updated, No middle name must have middle name when no_middle_name flag is set to false for the candidate candidate_id= |
| 403 | Forbidden |
| 403 | Sorry, your account is not approved for production |
| 403 | Candidate has requested that their PII be removed |
| 409 | Duplicate geo, name: peninsulasw_wa, state: WA already exists |
| 409 | Duplicate report detected. No more than 3 reports per candidate can be created within a 24 hour period |
| 409 | Duplicate candidate detected. No more than 2 duplicate candidates can be created within a 24 hour period |

## Cancellation Reasons

Screenings can be canceled due to various scenarios. Here is a list of the current cancellation reasons and their descriptions.

| Reason | Description |
| ------ | ----------- |
| candidate_missing_consent | Candidate consent not provided |
| candidate_pii_updated_customer_requested | Customer updated candidate PII prior to screening completion |
| exception_ssn_trace | SSN Trace completed with an exception prior to screening completion |
| source_inaccessible_closed_court | Court closed or has limited access to court records |
| complete_now_customer_requested | Customer requested Complete Now prior to screening completion |
| missing_required_information | Required information not received |
| vendor_unable_to_complete | Vendor unable to complete screening |
| vendor_account_deauthorized | Vendor deauthorized account |
| international_entry_not_supported | Screening does not support international entries |
| no_history_required_information | Candidate declared no history |
| profile_on_hold_customer_requested | Customer requested candidate profile on hold |
| candidate_withdrew_consent | Candidate withdrew consent |
| minors_package_not_enabled | Package not configured to allow candidates under age 18 |
| candidate_below_minimum_age | Candidate is below the minimum age for a background check |
| exception_mvr | MVR canceled with an exception |
| customer_account_deauthorized | Customer account was deauthorized |
| adverse_action_completed | Adverse Action completed prior to screening completion |
| adverse_action_suspended_report_timer_customer_requested | Customer configured the Adverse Action on Suspended Reports feature and its timer expired prior to screening completion |
| unable_to_fulfill_mvr | Unable to fulfill MVR request as data is not available |
| identity_verification_unverified | Identity Verification completed with an Unverified Result and action was taken to cancel the Report |
| request_withdrawn | Request withdrawn |

## Verification Types

Verification type values that indicate additional information or actions requested from a candidate.
These types are shown inside of [webhooks](#section/Webhooks/Verification-events) and from the [API](#operation/getVerification) for verifications.
For more information about verifications please visit the links for the webhook events or the api.

| Type |
| ----------------- |
| candidate_employment_history |
| driver_license |
| driver_license_history |
| education |
| id |
| id_document |
| license_document |
| passport_document |
| previous_license_document |
| ssn_confirmation |
| ssn_document |
| matrix |
| consent |

[dev-settings]: https://dashboard.checkr.com/account/developer_settings


#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
```

## Module Documentation and Snippets

### [account](checkr_api_py/resources/account/README.md)

* [list](checkr_api_py/resources/account/README.md#list) - Retrieve authenticated account details

### [accounts](checkr_api_py/resources/accounts/README.md)

* [create](checkr_api_py/resources/accounts/README.md#create) - Create a new Account

### [adverse_actions](checkr_api_py/resources/adverse_actions/README.md)

* [delete](checkr_api_py/resources/adverse_actions/README.md#delete) - Cancel an existing Adverse Action
* [get](checkr_api_py/resources/adverse_actions/README.md#get) - Retrieve an existing Adverse Action

### [candidate_stories](checkr_api_py/resources/candidate_stories/README.md)

* [delete](checkr_api_py/resources/candidate_stories/README.md#delete) - Delete a Candidate Story
* [get](checkr_api_py/resources/candidate_stories/README.md#get) - Retrieve a Candidate Story

### [candidates](checkr_api_py/resources/candidates/README.md)

* [create](checkr_api_py/resources/candidates/README.md#create) - Create a new Candidate
* [get](checkr_api_py/resources/candidates/README.md#get) - Retrieve an existing Candidate
* [list](checkr_api_py/resources/candidates/README.md#list) - List existing Candidates
* [update](checkr_api_py/resources/candidates/README.md#update) - Update an existing Candidate

### [candidates.continuous_checks](checkr_api_py/resources/candidates/continuous_checks/README.md)

* [create](checkr_api_py/resources/candidates/continuous_checks/README.md#create) - Create a new Continuous Check
* [list](checkr_api_py/resources/candidates/continuous_checks/README.md#list) - List existing Continuous Checks

### [candidates.documents](checkr_api_py/resources/candidates/documents/README.md)

* [create](checkr_api_py/resources/candidates/documents/README.md#create) - Upload a new Candidate Document
* [list](checkr_api_py/resources/candidates/documents/README.md#list) - List a Candidate's Documents

### [candidates.driver_licenses](checkr_api_py/resources/candidates/driver_licenses/README.md)

* [create](checkr_api_py/resources/candidates/driver_licenses/README.md#create) - Create a new Driver License
* [delete](checkr_api_py/resources/candidates/driver_licenses/README.md#delete) - Delete an existing Driver License
* [get](checkr_api_py/resources/candidates/driver_licenses/README.md#get) - Retrieve an existing Driver License
* [list](checkr_api_py/resources/candidates/driver_licenses/README.md#list) - List existing Driver Licenses
* [update](checkr_api_py/resources/candidates/driver_licenses/README.md#update) - Update an existing Driver License

### [candidates.employers](checkr_api_py/resources/candidates/employers/README.md)

* [create](checkr_api_py/resources/candidates/employers/README.md#create) - Create a new Employer
* [delete](checkr_api_py/resources/candidates/employers/README.md#delete) - Delete an existing Employer
* [get](checkr_api_py/resources/candidates/employers/README.md#get) - Retrieve an existing Employer
* [list](checkr_api_py/resources/candidates/employers/README.md#list) - List existing Employers

### [candidates.pii](checkr_api_py/resources/candidates/pii/README.md)

* [delete](checkr_api_py/resources/candidates/pii/README.md#delete) - Request PII removal for a Candidate

### [candidates.postal_address](checkr_api_py/resources/candidates/postal_address/README.md)

* [create](checkr_api_py/resources/candidates/postal_address/README.md#create) - Create a new Postal Address
* [list](checkr_api_py/resources/candidates/postal_address/README.md#list) - Get the Candidate's Postal Addresses

### [candidates.professional_licenses](checkr_api_py/resources/candidates/professional_licenses/README.md)

* [create](checkr_api_py/resources/candidates/professional_licenses/README.md#create) - Create a new Professional License
* [delete](checkr_api_py/resources/candidates/professional_licenses/README.md#delete) - Delete an existing Professional License
* [list](checkr_api_py/resources/candidates/professional_licenses/README.md#list) - List existing Professional Licenses

### [candidates.schools](checkr_api_py/resources/candidates/schools/README.md)

* [create](checkr_api_py/resources/candidates/schools/README.md#create) - Create a new School
* [delete](checkr_api_py/resources/candidates/schools/README.md#delete) - Delete an existing School
* [get](checkr_api_py/resources/candidates/schools/README.md#get) - Retrieve an existing School
* [list](checkr_api_py/resources/candidates/schools/README.md#list) - List existing Schools

### [candidates.ssn](checkr_api_py/resources/candidates/ssn/README.md)

* [list](checkr_api_py/resources/candidates/ssn/README.md#list) - Get a candidate's encrypted SSN

### [continuous_checks](checkr_api_py/resources/continuous_checks/README.md)

* [create](checkr_api_py/resources/continuous_checks/README.md#create) - Update an existing Continuous Check
* [delete](checkr_api_py/resources/continuous_checks/README.md#delete) - Cancel an existing Continuous Check
* [get](checkr_api_py/resources/continuous_checks/README.md#get) - Retrieve an existing Continuous Check

### [counties](checkr_api_py/resources/counties/README.md)

* [list](checkr_api_py/resources/counties/README.md#list) - Get Counties by State(s)

### [county_criminal_searches](checkr_api_py/resources/county_criminal_searches/README.md)

* [get](checkr_api_py/resources/county_criminal_searches/README.md#get) - Retrieve an existing County Criminal Search

### [documents](checkr_api_py/resources/documents/README.md)

* [get](checkr_api_py/resources/documents/README.md#get) - Retrieve a Document

### [drug_alcohol_clearinghouse_searches](checkr_api_py/resources/drug_alcohol_clearinghouse_searches/README.md)

* [get](checkr_api_py/resources/drug_alcohol_clearinghouse_searches/README.md#get) - Retrieve an existing Drug & Alcohol Clearinghouse Search

### [education_verifications](checkr_api_py/resources/education_verifications/README.md)

* [get](checkr_api_py/resources/education_verifications/README.md#get) - Retrieve an existing Education Verification

### [employment_verifications](checkr_api_py/resources/employment_verifications/README.md)

* [get](checkr_api_py/resources/employment_verifications/README.md#get) - Retrieve an existing Employment Verification

### [facis_searches](checkr_api_py/resources/facis_searches/README.md)

* [get](checkr_api_py/resources/facis_searches/README.md#get) - Retrieve an existing FACIS Search

### [federal_civil_district_searches](checkr_api_py/resources/federal_civil_district_searches/README.md)

* [get](checkr_api_py/resources/federal_civil_district_searches/README.md#get) - Retrieve an existing Federal District Civil Search

### [federal_civil_searches](checkr_api_py/resources/federal_civil_searches/README.md)

* [get](checkr_api_py/resources/federal_civil_searches/README.md#get) - Retrieve an existing Federal Civil Search

### [federal_criminal_searches](checkr_api_py/resources/federal_criminal_searches/README.md)

* [get](checkr_api_py/resources/federal_criminal_searches/README.md#get) - Retrieve an existing Federal Criminal Search

### [federal_district_criminal_searches](checkr_api_py/resources/federal_district_criminal_searches/README.md)

* [get](checkr_api_py/resources/federal_district_criminal_searches/README.md#get) - Retrieve an existing Federal District  Criminal Search

### [geos](checkr_api_py/resources/geos/README.md)

* [create](checkr_api_py/resources/geos/README.md#create) - Create a new Geo
* [get](checkr_api_py/resources/geos/README.md#get) - Retrieve an existing Geo
* [list](checkr_api_py/resources/geos/README.md#list) - List existing Geos
* [update](checkr_api_py/resources/geos/README.md#update) - Update an existing Geo

### [global_watchlist_searches](checkr_api_py/resources/global_watchlist_searches/README.md)

* [get](checkr_api_py/resources/global_watchlist_searches/README.md#get) - Retrieve an existing Global Watchlist Search

### [hierarchy](checkr_api_py/resources/hierarchy/README.md)

* [create](checkr_api_py/resources/hierarchy/README.md#create) - Create Hierarchy
* [list](checkr_api_py/resources/hierarchy/README.md#list) - Retrieve Hierarchy (Deprecated)

### [hierarchy.nodes](checkr_api_py/resources/hierarchy/nodes/README.md)

* [create](checkr_api_py/resources/hierarchy/nodes/README.md#create) - Add nodes to a hierarchy

### [hierarchy.status](checkr_api_py/resources/hierarchy/status/README.md)

* [list](checkr_api_py/resources/hierarchy/status/README.md#list) - Retrieve Hierarchy update status

### [i9.forms_i9](checkr_api_py/resources/i9/forms_i9/README.md)

* [create](checkr_api_py/resources/i9/forms_i9/README.md#create) - Create a new Form I-9
* [get](checkr_api_py/resources/i9/forms_i9/README.md#get) - Retrieve a Form I-9
* [list](checkr_api_py/resources/i9/forms_i9/README.md#list) - List existing Form I-9s

### [i9.forms_i9.pdf](checkr_api_py/resources/i9/forms_i9/pdf/README.md)

* [list](checkr_api_py/resources/i9/forms_i9/pdf/README.md#list) - Retrieve Form I-9 PDF file

### [i9.worksites](checkr_api_py/resources/i9/worksites/README.md)

* [create](checkr_api_py/resources/i9/worksites/README.md#create) - Create new Worksite
* [delete](checkr_api_py/resources/i9/worksites/README.md#delete) - Delete a Worksite
* [get](checkr_api_py/resources/i9/worksites/README.md#get) - Retrieve a Worksite
* [list](checkr_api_py/resources/i9/worksites/README.md#list) - List existing Worksites
* [update](checkr_api_py/resources/i9/worksites/README.md#update) - Update Worksite information

### [international_adverse_media_searches](checkr_api_py/resources/international_adverse_media_searches/README.md)

* [get](checkr_api_py/resources/international_adverse_media_searches/README.md#get) - Retrieve an existing International Adverse Media Search

### [international_criminal_searches](checkr_api_py/resources/international_criminal_searches/README.md)

* [get](checkr_api_py/resources/international_criminal_searches/README.md#get) - Retrieve an existing International Criminal Search

### [international_education_verifications](checkr_api_py/resources/international_education_verifications/README.md)

* [get](checkr_api_py/resources/international_education_verifications/README.md#get) - Retrieve an existing International Education Verificaiton

### [international_employment_verifications](checkr_api_py/resources/international_employment_verifications/README.md)

* [get](checkr_api_py/resources/international_employment_verifications/README.md#get) - Retrieve an existing International Employment Verification

### [international_global_watchlist_searches](checkr_api_py/resources/international_global_watchlist_searches/README.md)

* [get](checkr_api_py/resources/international_global_watchlist_searches/README.md#get) - Retrieve an existing International Global Watchlist Search

### [international_identity_document_validation](checkr_api_py/resources/international_identity_document_validation/README.md)

* [get](checkr_api_py/resources/international_identity_document_validation/README.md#get) - Retrieve an existing International Identity Document Validation

### [international_motor_vehicle_reports](checkr_api_py/resources/international_motor_vehicle_reports/README.md)

* [get](checkr_api_py/resources/international_motor_vehicle_reports/README.md#get) - Retrieve an existing International Motor Vehicle Report

### [invitations](checkr_api_py/resources/invitations/README.md)

* [create](checkr_api_py/resources/invitations/README.md#create) - Create a new Invitation
* [delete](checkr_api_py/resources/invitations/README.md#delete) - Cancel an existing Invitation
* [get](checkr_api_py/resources/invitations/README.md#get) - Retrieve an existing Invitation
* [list](checkr_api_py/resources/invitations/README.md#list) - List existing Invitations

### [motor_vehicle_reports](checkr_api_py/resources/motor_vehicle_reports/README.md)

* [get](checkr_api_py/resources/motor_vehicle_reports/README.md#get) - Retrieve an existing Motor Vehicle Report

### [national_criminal_searches](checkr_api_py/resources/national_criminal_searches/README.md)

* [get](checkr_api_py/resources/national_criminal_searches/README.md#get) - Retrieve an existing National Criminal Search

### [nodes](checkr_api_py/resources/nodes/README.md)

* [delete](checkr_api_py/resources/nodes/README.md#delete) - Delete an existing node
* [get](checkr_api_py/resources/nodes/README.md#get) - Retrieve an existing node
* [list](checkr_api_py/resources/nodes/README.md#list) - List existing Nodes
* [patch](checkr_api_py/resources/nodes/README.md#patch) - Update an existing node

### [packages](checkr_api_py/resources/packages/README.md)

* [delete](checkr_api_py/resources/packages/README.md#delete) - Delete an existing Package
* [get](checkr_api_py/resources/packages/README.md#get) - Retrieve an existing Package
* [list](checkr_api_py/resources/packages/README.md#list) - List existing Packages

### [personal_reference_verifications](checkr_api_py/resources/personal_reference_verifications/README.md)

* [get](checkr_api_py/resources/personal_reference_verifications/README.md#get) - Retrieve an existing Personal Reference Verification

### [professional_license_verifications](checkr_api_py/resources/professional_license_verifications/README.md)

* [get](checkr_api_py/resources/professional_license_verifications/README.md#get) - Retrieve an existing Professional License Verification

### [professional_reference_verifications](checkr_api_py/resources/professional_reference_verifications/README.md)

* [get](checkr_api_py/resources/professional_reference_verifications/README.md#get) - Retrieve an existing Professional Reference Verification

### [programs](checkr_api_py/resources/programs/README.md)

* [get](checkr_api_py/resources/programs/README.md#get) - Retrieve an existing Program
* [list](checkr_api_py/resources/programs/README.md#list) - List existing Programs

### [reports](checkr_api_py/resources/reports/README.md)

* [create](checkr_api_py/resources/reports/README.md#create) - Create a new Report
* [get](checkr_api_py/resources/reports/README.md#get) - Retrieve an existing Report
* [update](checkr_api_py/resources/reports/README.md#update) - Update an existing Report

### [reports.addresses](checkr_api_py/resources/reports/addresses/README.md)

* [list](checkr_api_py/resources/reports/addresses/README.md#list) - List existing Report addresses

### [reports.adverse_actions](checkr_api_py/resources/reports/adverse_actions/README.md)

* [create](checkr_api_py/resources/reports/adverse_actions/README.md#create) - Create a new Adverse Action

### [reports.adverse_items](checkr_api_py/resources/reports/adverse_items/README.md)

* [list](checkr_api_py/resources/reports/adverse_items/README.md#list) - List existing Adverse Items

### [reports.assessments](checkr_api_py/resources/reports/assessments/README.md)

* [list](checkr_api_py/resources/reports/assessments/README.md#list) - List existing Assessments

### [reports.candidate_stories](checkr_api_py/resources/reports/candidate_stories/README.md)

* [create](checkr_api_py/resources/reports/candidate_stories/README.md#create) - Create a new Candidate Story

### [reports.complete](checkr_api_py/resources/reports/complete/README.md)

* [create](checkr_api_py/resources/reports/complete/README.md#create) - Complete an existing Report

### [reports.eta](checkr_api_py/resources/reports/eta/README.md)

* [list](checkr_api_py/resources/reports/eta/README.md#list) - Retrieve a Report's ETA

### [reports.tags](checkr_api_py/resources/reports/tags/README.md)

* [create](checkr_api_py/resources/reports/tags/README.md#create) - Add a tag to a Report
* [delete](checkr_api_py/resources/reports/tags/README.md#delete) - Delete a tag from a Report
* [list](checkr_api_py/resources/reports/tags/README.md#list) - Retrieve tags for a Report
* [update](checkr_api_py/resources/reports/tags/README.md#update) - Update tags for a Report

### [reports.verifications](checkr_api_py/resources/reports/verifications/README.md)

* [list](checkr_api_py/resources/reports/verifications/README.md#list) - List existing Verifications

### [sex_offender_searches](checkr_api_py/resources/sex_offender_searches/README.md)

* [get](checkr_api_py/resources/sex_offender_searches/README.md#get) - Retrieve an existing Sex Offender Registry Search

### [ssn_traces](checkr_api_py/resources/ssn_traces/README.md)

* [get](checkr_api_py/resources/ssn_traces/README.md#get) - Retrieve an existing SSN Trace

### [state_criminal_searches](checkr_api_py/resources/state_criminal_searches/README.md)

* [get](checkr_api_py/resources/state_criminal_searches/README.md#get) - Retrieve an existing State Criminal Search

### [subscriptions](checkr_api_py/resources/subscriptions/README.md)

* [create](checkr_api_py/resources/subscriptions/README.md#create) - Create a new Subscription
* [delete](checkr_api_py/resources/subscriptions/README.md#delete) - Cancel an existing Subscription
* [get](checkr_api_py/resources/subscriptions/README.md#get) - Retrieve an existing Subscription
* [list](checkr_api_py/resources/subscriptions/README.md#list) - List existing Subscriptions
* [update](checkr_api_py/resources/subscriptions/README.md#update) - Update a Subscription

### [users](checkr_api_py/resources/users/README.md)

* [list](checkr_api_py/resources/users/README.md#list) - List existing Users

### [verifications](checkr_api_py/resources/verifications/README.md)

* [get](checkr_api_py/resources/verifications/README.md#get) - Retrieve a Verification

### [webhooks](checkr_api_py/resources/webhooks/README.md)

* [create](checkr_api_py/resources/webhooks/README.md#create) - Create a new Webhook
* [delete](checkr_api_py/resources/webhooks/README.md#delete) - Delete a Webhook
* [get](checkr_api_py/resources/webhooks/README.md#get) - Retrieve a Webhook
* [list](checkr_api_py/resources/webhooks/README.md#list) - List existing Webhooks

<!-- MODULE DOCS END -->

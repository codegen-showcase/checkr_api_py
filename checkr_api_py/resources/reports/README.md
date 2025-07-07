
### Retrieve an existing Report <a name="get"></a>

Returns an existing Report with the input ID.


**API Endpoint**: `GET /reports/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |
| `include` | ✗ | Comma delimited string specifying the resources to be embedded in the returned Report object. See [Embedding Resources](#section/Reference/Embedding-Resources). | `"candidate"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.get(id="string", include="candidate")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.get(id="string", include="candidate")

```

#### Response

##### Type
[Report](/checkr_api_py/types/models/report.py)

##### Example
`{"adjudication": "engaged", "archived": False, "arrest_search_id": "539fd88c101897f7cd000001", "assessment": "eligible", "candidate_id": "e44aa283528e6fde7d542194", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "drug_alcohol_clearinghouse_id": "539fd88c101897f7cd000001", "drug_screening_id": "539fd88c101897f7cd000001", "estimated_completion_time": "2019-07-31T00:00:00Z", "facis_search_id": "539fd88c101897f7cd000001", "federal_civil_search_id": "539fd88c101897f7cd000001", "federal_criminal_search_id": "539fd88c101897f7cd000001", "federal_district_civil_search_id": "539fd88c101897f7cd000001", "federal_district_criminal_search_id": "539fd88c101897f7cd000001", "global_watchlist_search_id": "539fd88c101897f7cd000001", "id": "e44aa283528e6fde7d542194", "includes_canceled": False, "international_education_verification_id": "41007c751c9a15c892c0981a040004", "international_employment_verification_id": "41007c751c9a15c892c0981a040015", "international_global_watchlist_search_id": "41007c751c9a15c892c0981a0400f3", "international_identity_document_validation_id": "41007c751c9a15c892c0981a040026", "motor_vehicle_report_id": "539fd88c101897f7cd000007", "national_criminal_search_id": "539fd88c101897f7cd000006", "occupational_health_screening_id": "539fdcf335644a0ef4000003", "package": "driver_pro", "program_id": "00166f9ff39ec7b453adfaec", "result": "clear", "sex_offender_search_id": "539fd88c101897f7cd000008", "source": "api", "ssn_trace_id": "539fd88c101897f7cd000001", "status": "complete", "turnaround_time": 90, "uri": "/v1/reports/4722c07dd9a10c3985ae432a"}`

### Create a new Report <a name="create"></a>

Creates a new Report resource.

<b>Notes: </b>
- This resource does not support the creation of reports which include international Packages. Use the [`/invitations` API](#tag/invitations) to order these reports.
- Employment Verifications, Education Verifications, and Credit Checks may not be initiated using the `/reports` API. Please use the [`/invitations` API](#tag/invitations) to initiate the [Checkr-Hosted Apply Flow](/#section/Getting-Started/Create-an-Invitation) when ordering background checks that include any of these screening types.
- Creating a Report which includes an Occupational Health or Drug
Check will automatically issue an email invitation to the candidate to schedule their appointment at a clinic of their choice.


**API Endpoint**: `POST /reports`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | ID of the Candidate screened. | `"e44aa283528e6fde7d542194"` |
| `package` | ✓ | `slug` of the associated package. Example: `driver_pro`  | `"string"` |
| `node` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  `custom_id` of the associated node.  | `"string"` |
| `self_disclosures` | ✗ | Array of SelfDisclosures  **Note:** Self Disclosures may not be added, updated, or deleted after a Report has been created. The information provided in a Self Disclosure will not be included in the completed Report, and may be retrieved using [GET](#operation/getReport) `/v1/reports/{id}?include=documents`. See the [Documents](#tag/Documents) resource for more information.  Removing the requirement for the description, date, and location parameters greatly reduces the value of Self Disclosures. If your system mandates that these parameters be optional, work with your Checkr Customer Success Manager to disable the requirement.  | `[{"date": "2019-11-01", "description": "I made a mistake and grew from this experience.", "location": {"country": "US", "county": "BOULDER", "state": "CO"}, "offense_category": "Insurance Fraud", "offense_level": "Misdemeanor", "sentence": "24 months probation", "time_served": "20 months probation"}]` |
| `tags` | ✗ | Array of tags for the Report. | `["string"]` |
| `work_locations` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.create(candidate_id="e44aa283528e6fde7d542194", package="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.create(
    candidate_id="e44aa283528e6fde7d542194", package="string"
)

```

#### Response

##### Type
[Report](/checkr_api_py/types/models/report.py)

##### Example
`{"adjudication": "engaged", "archived": False, "arrest_search_id": "539fd88c101897f7cd000001", "assessment": "eligible", "candidate_id": "e44aa283528e6fde7d542194", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "drug_alcohol_clearinghouse_id": "539fd88c101897f7cd000001", "drug_screening_id": "539fd88c101897f7cd000001", "estimated_completion_time": "2019-07-31T00:00:00Z", "facis_search_id": "539fd88c101897f7cd000001", "federal_civil_search_id": "539fd88c101897f7cd000001", "federal_criminal_search_id": "539fd88c101897f7cd000001", "federal_district_civil_search_id": "539fd88c101897f7cd000001", "federal_district_criminal_search_id": "539fd88c101897f7cd000001", "global_watchlist_search_id": "539fd88c101897f7cd000001", "id": "e44aa283528e6fde7d542194", "includes_canceled": False, "international_education_verification_id": "41007c751c9a15c892c0981a040004", "international_employment_verification_id": "41007c751c9a15c892c0981a040015", "international_global_watchlist_search_id": "41007c751c9a15c892c0981a0400f3", "international_identity_document_validation_id": "41007c751c9a15c892c0981a040026", "motor_vehicle_report_id": "539fd88c101897f7cd000007", "national_criminal_search_id": "539fd88c101897f7cd000006", "occupational_health_screening_id": "539fdcf335644a0ef4000003", "package": "driver_pro", "program_id": "00166f9ff39ec7b453adfaec", "result": "clear", "sex_offender_search_id": "539fd88c101897f7cd000008", "source": "api", "ssn_trace_id": "539fd88c101897f7cd000001", "status": "complete", "turnaround_time": 90, "uri": "/v1/reports/4722c07dd9a10c3985ae432a"}`

### Update an existing Report <a name="update"></a>

Updates the `package` or `adjudication` for an existing Report resource.

Use this endpoint to update reports which include the candidate's Social Security Number. To update a Report which does not include an SSN, first use the [update Candidate](#operation/updateCandidate) request to add the candidate’s SSN before updating the report.

Either `package` or `adjudication` is required.

<b>Note: </b>This endpoint may also be used to update international reports for candidates which do not include an SSN.
<div class="alert alert-info">

  **Note**: The Package of a Report cannot be updated if it has an Adverse Action with the status: `complete` or `dispute`. To proceed, cancel the Adverse Action or create a new Report.

</div>


**API Endpoint**: `POST /reports/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |
| `adjudication` | ✗ |  | `"engaged"` |
| `package` | ✗ | Slug of the Package.  | `"driver_pro"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.update(id="string", adjudication="engaged", package="driver_pro")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.update(
    id="string", adjudication="engaged", package="driver_pro"
)

```

#### Response

##### Type
[Report](/checkr_api_py/types/models/report.py)

##### Example
`{"adjudication": "engaged", "archived": False, "arrest_search_id": "539fd88c101897f7cd000001", "assessment": "eligible", "candidate_id": "e44aa283528e6fde7d542194", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "drug_alcohol_clearinghouse_id": "539fd88c101897f7cd000001", "drug_screening_id": "539fd88c101897f7cd000001", "estimated_completion_time": "2019-07-31T00:00:00Z", "facis_search_id": "539fd88c101897f7cd000001", "federal_civil_search_id": "539fd88c101897f7cd000001", "federal_criminal_search_id": "539fd88c101897f7cd000001", "federal_district_civil_search_id": "539fd88c101897f7cd000001", "federal_district_criminal_search_id": "539fd88c101897f7cd000001", "global_watchlist_search_id": "539fd88c101897f7cd000001", "id": "e44aa283528e6fde7d542194", "includes_canceled": False, "international_education_verification_id": "41007c751c9a15c892c0981a040004", "international_employment_verification_id": "41007c751c9a15c892c0981a040015", "international_global_watchlist_search_id": "41007c751c9a15c892c0981a0400f3", "international_identity_document_validation_id": "41007c751c9a15c892c0981a040026", "motor_vehicle_report_id": "539fd88c101897f7cd000007", "national_criminal_search_id": "539fd88c101897f7cd000006", "occupational_health_screening_id": "539fdcf335644a0ef4000003", "package": "driver_pro", "program_id": "00166f9ff39ec7b453adfaec", "result": "clear", "sex_offender_search_id": "539fd88c101897f7cd000008", "source": "api", "ssn_trace_id": "539fd88c101897f7cd000001", "status": "complete", "turnaround_time": 90, "uri": "/v1/reports/4722c07dd9a10c3985ae432a"}`

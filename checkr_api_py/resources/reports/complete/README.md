
### Complete an existing Report <a name="create"></a>

Cancels all pending or suspended screenings and completes the report.

Use this endpoint to complete reports which include pending or suspended screenings. If a report is completed with pending or suspended screenings, the following events will be triggered:

  - The `status` for all in-progress screenings within the report will be updated to `canceled`.
  - A cancellation reason and the reason’s description will be added to each canceled screening.
  - Checkr will issue webhooks upon report completion.
    - If all screenings are canceled, a `report.canceled` webhook will be issued.
    - If at least one screening has a result before the report is completed, Checkr will issue two webhooks: first, `report.updated`, followed by `report.complete`.


**API Endpoint**: `POST /reports/{id}/complete`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.complete.create(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.complete.create(id="string")

```

#### Response

##### Type
[Report](/checkr_api_py/types/models/report.py)

##### Example
`{"adjudication": "engaged", "archived": False, "arrest_search_id": "539fd88c101897f7cd000001", "assessment": "eligible", "candidate_id": "e44aa283528e6fde7d542194", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "drug_alcohol_clearinghouse_id": "539fd88c101897f7cd000001", "drug_screening_id": "539fd88c101897f7cd000001", "estimated_completion_time": "2019-07-31T00:00:00Z", "facis_search_id": "539fd88c101897f7cd000001", "federal_civil_search_id": "539fd88c101897f7cd000001", "federal_criminal_search_id": "539fd88c101897f7cd000001", "federal_district_civil_search_id": "539fd88c101897f7cd000001", "federal_district_criminal_search_id": "539fd88c101897f7cd000001", "global_watchlist_search_id": "539fd88c101897f7cd000001", "id": "e44aa283528e6fde7d542194", "includes_canceled": False, "international_education_verification_id": "41007c751c9a15c892c0981a040004", "international_employment_verification_id": "41007c751c9a15c892c0981a040015", "international_global_watchlist_search_id": "41007c751c9a15c892c0981a0400f3", "international_identity_document_validation_id": "41007c751c9a15c892c0981a040026", "motor_vehicle_report_id": "539fd88c101897f7cd000007", "national_criminal_search_id": "539fd88c101897f7cd000006", "occupational_health_screening_id": "539fdcf335644a0ef4000003", "package": "driver_pro", "program_id": "00166f9ff39ec7b453adfaec", "result": "clear", "sex_offender_search_id": "539fd88c101897f7cd000008", "source": "api", "ssn_trace_id": "539fd88c101897f7cd000001", "status": "complete", "turnaround_time": 90, "uri": "/v1/reports/4722c07dd9a10c3985ae432a"}`

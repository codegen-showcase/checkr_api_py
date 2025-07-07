
### List existing Assessments <a name="list"></a>

Returns Assessments for an existing Report.


**API Endpoint**: `GET /reports/{report_id}/assessments`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `report_id` | ✓ | The ID of the associated Report. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.assessments.list(report_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.assessments.list(report_id="string")

```

#### Response

##### Type
[ReportsAssessmentsListResponse](/checkr_api_py/types/models/reports_assessments_list_response.py)

##### Example
`{"count": 1}`

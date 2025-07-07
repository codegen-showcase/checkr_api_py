
### List existing Verifications <a name="list"></a>

Returns a list of existing Verifications for the input `report_id`.


**API Endpoint**: `GET /reports/{report_id}/verifications`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `report_id` | ✓ | Returns the list of verifications for the input `report_id`. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.verifications.list(report_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.verifications.list(report_id="string")

```

#### Response

##### Type
[ReportsVerificationsListResponse](/checkr_api_py/types/models/reports_verifications_list_response.py)

##### Example
`{"count": 2}`

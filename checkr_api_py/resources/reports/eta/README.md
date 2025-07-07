
### Retrieve a Report's ETA <a name="list"></a>

Returns an existing Report ETA for the input Report ID.


**API Endpoint**: `GET /reports/{id}/eta`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Report for which the ETA was generated. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.eta.list(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.eta.list(id="string")

```

#### Response

##### Type
[ReportEta](/checkr_api_py/types/models/report_eta.py)

##### Example
`{"estimate_generated_at": "2014-01-18T12:34:00Z", "estimated_completion_time": "2019-07-31T00:00:00Z"}`

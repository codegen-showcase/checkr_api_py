
### List existing Adverse Items <a name="list"></a>

Returns a list of existing Adverse Items with the input `report_id`.

<b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.

Returns 400 if the Report's status is not Consider or the Report already has an active (non-cancelled) Adverse Action.


**API Endpoint**: `GET /reports/{report_id}/adverse_items`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `report_id` | ✓ | The ID of the associated Report. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.adverse_items.list(report_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.adverse_items.list(report_id="string")

```

#### Response

##### Type
[ReportsAdverseItemsListResponse](/checkr_api_py/types/models/reports_adverse_items_list_response.py)

##### Example
`{"count": 1}`

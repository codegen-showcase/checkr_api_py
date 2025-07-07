
### List existing Report addresses <a name="list"></a>

This request is used to retrieve addresses for a given Report.

**API Endpoint**: `GET /reports/{report_id}/addresses`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `report_id` | ✓ | Returns the list of Report addresses for the input `report_id`. | `"string"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.addresses.list(report_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.addresses.list(report_id="string")

```

#### Response

##### Type
[ReportsAddressesListResponse](/checkr_api_py/types/models/reports_addresses_list_response.py)

##### Example
`{"count": 1}`

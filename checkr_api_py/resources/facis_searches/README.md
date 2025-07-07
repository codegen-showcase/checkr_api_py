
### Retrieve an existing FACIS Search <a name="get"></a>

Returns an existing FACIS Search with the input ID.


**API Endpoint**: `GET /facis_searches/${id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Facis Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.facis_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.facis_searches.get(id="string")

```

#### Response

##### Type
[FacisSearch](/checkr_api_py/types/models/facis_search.py)

##### Example
`{"cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": 345600}`

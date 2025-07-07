
### Retrieve an existing State Criminal Search <a name="get"></a>

Returns an existing State Criminal Search with the input ID.


**API Endpoint**: `GET /state_criminal_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the State Criminal Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.state_criminal_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.state_criminal_searches.get(id="string")

```

#### Response

##### Type
[StateCriminalSearch](/checkr_api_py/types/models/state_criminal_search.py)

##### Example
`{"assessment": "eligible", "cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything", "estimated_completion_time": "2014-01-18T12:34:00Z", "state": "CA"}`


### Retrieve an existing County Criminal Search <a name="get"></a>

Returns an existing County Criminal Search with the input ID.


**API Endpoint**: `GET /county_criminal_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the County Criminal Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.county_criminal_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.county_criminal_searches.get(id="string")

```

#### Response

##### Type
[CountyCriminalSearch](/checkr_api_py/types/models/county_criminal_search.py)

##### Example
`{"assessment": "eligible", "cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything", "county": "SAN FRANCISCO", "estimated_completion_date": "2019-03-13", "estimated_completion_time": "2019-03-13T16:31:07Z", "state": "CA"}`

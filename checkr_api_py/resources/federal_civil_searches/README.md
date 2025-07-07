
### Retrieve an existing Federal Civil Search <a name="get"></a>

Returns an existing Federal Civil Search with the input ID.


**API Endpoint**: `GET /federal_civil_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Federal Civil Search to retrieve. | `"string"` |
| `exclude` | ✗ | Indicates whether to return district screenings in pointer search payload | `"district"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.federal_civil_searches.get(id="string", exclude="district")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.federal_civil_searches.get(id="string", exclude="district")

```

#### Response

##### Type
[FederalCivilSearch](/checkr_api_py/types/models/federal_civil_search.py)

##### Example
`{"completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything"}`

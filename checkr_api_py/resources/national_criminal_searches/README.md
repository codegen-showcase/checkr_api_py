
### Retrieve an existing National Criminal Search <a name="get"></a>

Returns an existing National Criminal Search with the input ID.


**API Endpoint**: `GET /national_criminal_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the National Criminal Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.national_criminal_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.national_criminal_searches.get(id="string")

```

#### Response

##### Type
[NationalCriminalSearch](/checkr_api_py/types/models/national_criminal_search.py)

##### Example
`{"completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything"}`

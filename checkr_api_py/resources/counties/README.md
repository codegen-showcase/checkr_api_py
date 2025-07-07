
### Get Counties by State(s) <a name="list"></a>

Returns a list of all counties for the input state(s). If no state is provided with the query, returns a list of all counties in the United States.


**API Endpoint**: `GET /counties`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `states` | ✗ | A comma-separated list of states' Federal Information Processing Series (FIPS) values to query. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.counties.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.counties.list()

```

#### Response

##### Type
[CountiesListResponse](/checkr_api_py/types/models/counties_list_response.py)

##### Example
`{}`

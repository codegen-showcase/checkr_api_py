
### Retrieve an existing SSN Trace <a name="get"></a>

Returns an existing SSN Trace with the input ID.


**API Endpoint**: `GET /ssn_traces/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the SSN Trace to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.ssn_traces.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.ssn_traces.get(id="string")

```

#### Response

##### Type
[SsnTrace](/checkr_api_py/types/models/ssn_trace.py)

##### Example
`{"completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything", "issued_state": "CA", "issued_year": 1993, "ssn": "XXX-XX-4645"}`

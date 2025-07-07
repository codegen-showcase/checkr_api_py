
### Retrieve Hierarchy update status <a name="list"></a>

Returns the status of the latest Hierarchy ingestion request.

This call requires no input, and is provided as a means to determine the progress of an
asynchronous `POST /hierarchy` request.


**API Endpoint**: `GET /hierarchy/status`

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.hierarchy.status.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.hierarchy.status.list()

```

#### Response

##### Type
[HierarchyStatusListResponse](/checkr_api_py/types/models/hierarchy_status_list_response.py)

##### Example
`{"hierarchy_pending": False, "hierarchy_present": True}`

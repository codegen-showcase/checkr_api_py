
### Retrieve an existing International Criminal Search <a name="get"></a>

Returns an existing International Criminal Search with the input ID.


**API Endpoint**: `GET /international_criminal_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the International Criminal Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.international_criminal_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.international_criminal_searches.get(id="string")

```

#### Response

##### Type
[InternationalCriminalSearch](/checkr_api_py/types/models/international_criminal_search.py)

##### Example
`{"cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "could be anything", "result": "clear", "status": "complete", "turnaround_time": 90, "uri": "could be anything", "country": "FR", "pdf_url": "https://eu-west-1-checkr-staging.s3.eu-west-1.amazonaws.com/document.pdf"}`

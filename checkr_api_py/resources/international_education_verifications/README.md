
### Retrieve an existing International Education Verificaiton <a name="get"></a>

Returns an existing International Education Verificaiton with the input ID.


**API Endpoint**: `GET /international_education_verifications/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the International Education Verificaiton to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.international_education_verifications.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.international_education_verifications.get(id="string")

```

#### Response

##### Type
[InternationalEducationVerification](/checkr_api_py/types/models/international_education_verification.py)

##### Example
`{"cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "could be anything", "result": "clear", "status": "complete", "turnaround_time": "could be anything", "uri": "could be anything"}`


### Retrieve an existing Professional Reference Verification <a name="get"></a>

Returns an existing Professional Reference Verification with the input ID.


**API Endpoint**: `GET /professional_reference_verifications/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Professional Reference Verification to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.professional_reference_verifications.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.professional_reference_verifications.get(id="string")

```

#### Response

##### Type
[ProfessionalReferenceVerification](/checkr_api_py/types/models/professional_reference_verification.py)

##### Example
`{"assessment": "eligible", "cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "could be anything", "turnaround_time": "could be anything", "uri": "could be anything", "email": "john.smith@gmail.com", "name": "John Smith", "phone": "5555555555", "relationship": "Manager"}`

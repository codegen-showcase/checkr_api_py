
### Retrieve a Verification <a name="get"></a>

Returns an existing Verification with the input ID


**API Endpoint**: `GET /verifications/{verification_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `verification_id` | ✓ |  | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.verifications.get(verification_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.verifications.get(verification_id="string")

```

#### Response

##### Type
[Verification](/checkr_api_py/types/models/verification.py)

##### Example
`{"created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "report_id": "4722c07dd9a10c3985ae432a", "uri": "/v1/verifications/db313e73383710d4fa2f18fd", "verification_type": "id", "verification_url": "http://verifications.checkr.com/db313e73383710d4fa2f18fd"}`

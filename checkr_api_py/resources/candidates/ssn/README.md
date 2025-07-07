
### Get a candidate's encrypted SSN <a name="list"></a>

Returns an encrypted SSN for the input `candidate_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/ssn`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The candidate's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.ssn.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.ssn.list(candidate_id="string")

```

#### Response

##### Type
[Ssn](/checkr_api_py/types/models/ssn.py)

##### Example
`{"encrypted_ssn": "hyYMhDje9dVUEPKU9myy7OFJ7R27pj0pmlegFlka99I="}`

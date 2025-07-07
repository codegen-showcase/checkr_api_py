
### Get the Candidate's Postal Addresses <a name="list"></a>

Returns the Postal Address of a given candidate.


**API Endpoint**: `GET /candidates/{candidate_id}/postal_address`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The candidate's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.postal_address.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.postal_address.list(candidate_id="string")

```

#### Response

##### Type
[CandidatePostalAddress](/checkr_api_py/types/models/candidate_postal_address.py)

##### Example
`{"candidate_id": "e44aa283528e6fde7d542194", "city": "Santa Monica", "id": "e44aa283528e6fde7d542194", "name": "John Alfred Smith", "state": "CA", "street": "123 Main St", "street2": "Apt A", "uri": "/v1/candidate/e44aa283528e6fde7d542194/postal_address", "zipcode": "90401"}`

### Create a new Postal Address <a name="create"></a>

Creates a new Postal Address for a given candidate.


**API Endpoint**: `POST /candidates/{candidate_id}/postal_address`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The candidate's ID. | `"string"` |
| `data` | ✗ |  | `{"city": "Santa Monica", "name": "John Smith", "state": "CA", "street": "123 Main St", "street2": "Apt A", "zipcode": "90401"}` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.postal_address.create(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.postal_address.create(candidate_id="string")

```

#### Response

##### Type
[CandidatePostalAddress](/checkr_api_py/types/models/candidate_postal_address.py)

##### Example
`{"candidate_id": "e44aa283528e6fde7d542194", "city": "Santa Monica", "id": "e44aa283528e6fde7d542194", "name": "John Alfred Smith", "state": "CA", "street": "123 Main St", "street2": "Apt A", "uri": "/v1/candidate/e44aa283528e6fde7d542194/postal_address", "zipcode": "90401"}`


### List existing Continuous Checks <a name="list"></a>

Returns a list of existing Continuous Checks.


**API Endpoint**: `GET /candidates/{candidate_id}/continuous_checks`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.continuous_checks.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.continuous_checks.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesContinuousChecksListResponse](/checkr_api_py/types/models/candidates_continuous_checks_list_response.py)

##### Example
`{"count": 1}`

### Create a new Continuous Check <a name="create"></a>

Creates a new Continuous Check resource.


**API Endpoint**: `POST /candidates/{candidate_id}/continuous_checks`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `type` | ✓ | Defines the screening type(s) for this Continuous Check. | `"criminal"` |
| `node` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts with Nodes.  `custom_id` of the associated node.  | `"string"` |
| `work_locations` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.continuous_checks.create(
    candidate_id="string", type_="criminal"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.continuous_checks.create(
    candidate_id="string", type_="criminal"
)

```

#### Response

##### Type
[ContinuousCheck](/checkr_api_py/types/models/continuous_check.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "id": "e44aa283528e6fde7d542194", "node": "zpy8orej4r614ize", "type_": "criminal"}`

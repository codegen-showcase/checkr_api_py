
### Cancel an existing Continuous Check <a name="delete"></a>

Cancels an existing Continuous Check.


**API Endpoint**: `DELETE /continuous_checks/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Continuous Check's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.continuous_checks.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.continuous_checks.delete(id="string")

```

#### Response

##### Type
[ContinuousCheck](/checkr_api_py/types/models/continuous_check.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "id": "e44aa283528e6fde7d542194", "node": "zpy8orej4r614ize", "type_": "criminal"}`

### Retrieve an existing Continuous Check <a name="get"></a>

Returns an existing Continuous Check with the input ID.


**API Endpoint**: `GET /continuous_checks/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Continuous Check's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.continuous_checks.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.continuous_checks.get(id="string")

```

#### Response

##### Type
[ContinuousCheck](/checkr_api_py/types/models/continuous_check.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "id": "e44aa283528e6fde7d542194", "node": "zpy8orej4r614ize", "type_": "criminal"}`

### Update an existing Continuous Check <a name="create"></a>

Updates the node and/or work locations of an existing Continuous Check.


**API Endpoint**: `POST /continuous_checks/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Continuous Check's ID. | `"string"` |
| `node` | ✗ | `custom_id` of the associated node.  | `"string"` |
| `work_locations` | ✗ | Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.continuous_checks.create(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.continuous_checks.create(id="string")

```

#### Response

##### Type
[ContinuousCheck](/checkr_api_py/types/models/continuous_check.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "id": "e44aa283528e6fde7d542194", "node": "zpy8orej4r614ize", "type_": "criminal"}`

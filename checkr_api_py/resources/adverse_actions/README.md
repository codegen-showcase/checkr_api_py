
### Cancel an existing Adverse Action <a name="delete"></a>

Cancels an existing Adverse Action.


**API Endpoint**: `DELETE /adverse_actions/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Adverse Action. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.adverse_actions.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.adverse_actions.delete(id="string")

```

#### Response

##### Type
[AdverseAction](/checkr_api_py/types/models/adverse_action.py)

##### Example
`{"created_at": "2016-09-29T17:39:49Z", "id": "e44aa283528e6fde7d542194", "post_notice_ready_at": "2016-10-06T17:39:48Z", "post_notice_scheduled_at": "2016-10-07T12:34:00Z", "report_id": "b861a56db1b1b89692dd6118", "status": "pending", "uri": "/v1/adverse_actions/57ed51e57619e8002a6683f2"}`

### Retrieve an existing Adverse Action <a name="get"></a>

Returns an existing Adverse Action with the input ID.


**API Endpoint**: `GET /adverse_actions/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Adverse Action. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.adverse_actions.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.adverse_actions.get(id="string")

```

#### Response

##### Type
[AdverseAction](/checkr_api_py/types/models/adverse_action.py)

##### Example
`{"created_at": "2016-09-29T17:39:49Z", "id": "e44aa283528e6fde7d542194", "post_notice_ready_at": "2016-10-06T17:39:48Z", "post_notice_scheduled_at": "2016-10-07T12:34:00Z", "report_id": "b861a56db1b1b89692dd6118", "status": "pending", "uri": "/v1/adverse_actions/57ed51e57619e8002a6683f2"}`

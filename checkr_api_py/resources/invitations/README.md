
### Cancel an existing Invitation <a name="delete"></a>

Cancels an existing Invitation.


**API Endpoint**: `DELETE /invitations/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Invitation's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.invitations.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.invitations.delete(id="string")

```

#### Response

##### Type
[Invitation](/checkr_api_py/types/models/invitation.py)

##### Example
`{"archived": False, "candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "expires_at": "2015-05-21T17:45:34Z", "id": "e44aa283528e6fde7d542194", "invitation_url": "https://apply.checkr.com/invite/try-checkr/290f9d6d6e46/test", "package": "driver_pro", "status": "pending", "uri": "/v1/invitations/e44aa283528e6fde7d542194"}`

### List existing Invitations <a name="list"></a>

Returns a list of existing Invitations with the input `status` or `candidate_id`.

* If no parameters are passed, returns all Invitations.

* If `candidate_id` or `status` is passed, returns Invitations that match the input parameter.

* If both `candidate_id` and `status` are passed, return Invitations that match both parameters.

Returns 400 if the (optional) `status` parameter is not `pending`, `expired`, or `completed`.
<b>Note: </b>This call will not return invitations with non-US `work_locations`. Use [GET /invitations/{id}](#operation/getInvitation) to retrieve candidates outside the US.


**API Endpoint**: `GET /invitations`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✗ | ID of the candidate to whom the invitation was issued. | `"string"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |
| `status` | ✗ | Status of the Invitation. | `"completed"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.invitations.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.invitations.list()

```

#### Response

##### Type
[InvitationsListResponse](/checkr_api_py/types/models/invitations_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Invitation <a name="get"></a>

Returns an existing Invitation with the input ID.


**API Endpoint**: `GET /invitations/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Invitation's ID. | `"string"` |
| `include_deleted` | ✗ | Retrieve an invitation that has been deleted | `True` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.invitations.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.invitations.get(id="string")

```

#### Response

##### Type
[Invitation](/checkr_api_py/types/models/invitation.py)

##### Example
`{"archived": False, "candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "expires_at": "2015-05-21T17:45:34Z", "id": "e44aa283528e6fde7d542194", "invitation_url": "https://apply.checkr.com/invite/try-checkr/290f9d6d6e46/test", "package": "driver_pro", "status": "pending", "uri": "/v1/invitations/e44aa283528e6fde7d542194"}`

### Create a new Invitation <a name="create"></a>

Creates a new Invitation resource.


**API Endpoint**: `POST /invitations`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | ID of the Candidate for whom the Invitation is created. | `"551564b7865af96a28b13f36"` |
| `package` | ✓ | `slug` of the associated package.  | `"driver_pro"` |
| `node` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  `custom_id` of the associated node.  | `"string"` |
| `tags` | ✗ | Array of tags for the Report. | `["string"]` |
| `work_locations` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.invitations.create(
    candidate_id="551564b7865af96a28b13f36", package="driver_pro"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.invitations.create(
    candidate_id="551564b7865af96a28b13f36", package="driver_pro"
)

```

#### Response

##### Type
[Invitation](/checkr_api_py/types/models/invitation.py)

##### Example
`{"archived": False, "candidate_id": "551564b7865af96a28b13f36", "created_at": "2015-05-14T17:45:34Z", "expires_at": "2015-05-21T17:45:34Z", "id": "e44aa283528e6fde7d542194", "invitation_url": "https://apply.checkr.com/invite/try-checkr/290f9d6d6e46/test", "package": "driver_pro", "status": "pending", "uri": "/v1/invitations/e44aa283528e6fde7d542194"}`

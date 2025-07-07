
### List existing Users <a name="list"></a>

Returns a list of all existing Users.


**API Endpoint**: `GET /users`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.users.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.users.list()

```

#### Response

##### Type
[UsersListResponse](/checkr_api_py/types/models/users_list_response.py)

##### Example
`{"count": 2}`

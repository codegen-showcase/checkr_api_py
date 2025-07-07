
### List existing Programs <a name="list"></a>

Returns a list of existing Programs with the input `name`.


**API Endpoint**: `GET /programs`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✗ | Returns Programs with the input `name`. | `"string"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.programs.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.programs.list()

```

#### Response

##### Type
[ProgramsListResponse](/checkr_api_py/types/models/programs_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Program <a name="get"></a>

Returns an existing Program with the input ID.


**API Endpoint**: `GET /programs/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Program to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.programs.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.programs.get(id="string")

```

#### Response

##### Type
[Program](/checkr_api_py/types/models/program.py)

##### Example
`{"created_at": "2017-08-07T16:51:09Z", "id": "e44aa283528e6fde7d542194", "name": "Program A"}`

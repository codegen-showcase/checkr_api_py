
### List existing Geos <a name="list"></a>

Returns a list of existing Geos with the input `name` or `state`.


**API Endpoint**: `GET /geos`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✗ | Returns all Geos with the input `name`. | `"string"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |
| `state` | ✗ | Returns all Geos with the input state. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.geos.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.geos.list()

```

#### Response

##### Type
[GeosListResponse](/checkr_api_py/types/models/geos_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Geo <a name="get"></a>

Returns an existing Geo with the input ID.


**API Endpoint**: `GET /geos/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Geo. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.geos.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.geos.get(id="string")

```

#### Response

##### Type
[Geo](/checkr_api_py/types/models/geo.py)

##### Example
`{"city": "San Francisco", "created_at": "2015-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "name": "SF CA", "state": "CA", "uri": "/v1/geos/e44aa283528e6fde7d542194"}`

### Create a new Geo <a name="create"></a>

Creates a new Geo resource.

**Note**: Attempting to create a new Geo with the same name/state combination will result in an
409 error


**API Endpoint**: `POST /geos`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ | Human-readable name of the Geo. | `"San Francisco"` |
| `state` | ✓ | US state for the Geo. | `"CA"` |
| `city` | ✗ | A major city within the input state. | `"San Francisco"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.geos.create(name="San Francisco", state="CA", city="San Francisco")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.geos.create(name="San Francisco", state="CA", city="San Francisco")

```

#### Response

##### Type
[Geo](/checkr_api_py/types/models/geo.py)

##### Example
`{"city": "San Francisco", "created_at": "2015-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "name": "SF CA", "state": "CA", "uri": "/v1/geos/e44aa283528e6fde7d542194"}`

### Update an existing Geo <a name="update"></a>

Updates an existing Geo resource with the input `city`.
`city` can only be added once.


**API Endpoint**: `POST /geos/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Geo. | `"string"` |
| `city` | ✗ | Updates the Geo with the input city. | `"San Francisco"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.geos.update(id="string", city="San Francisco")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.geos.update(id="string", city="San Francisco")

```

#### Response

##### Type
[Geo](/checkr_api_py/types/models/geo.py)

##### Example
`{"city": "San Francisco", "created_at": "2015-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "name": "SF CA", "state": "CA", "uri": "/v1/geos/e44aa283528e6fde7d542194"}`

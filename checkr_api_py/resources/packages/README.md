
### Delete an existing Package <a name="delete"></a>

Deletes an existing Package.


**API Endpoint**: `DELETE /packages/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Package to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.packages.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.packages.delete(id="string")

```

#### Response

##### Type
[Package](/checkr_api_py/types/models/package.py)

##### Example
`{"apply_url": "https://apply.checkr.com/apply/customer-services-inc/532c20ea819b", "created_at": "2014-01-18T12:34:00Z", "deleted_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "name": "Criminal Pro", "price": 6500, "slug": "criminal_pro", "uri": "/v1/packages/e44aa283528e6fde7d542194"}`

### List existing Packages <a name="list"></a>

Returns a list of all existing Packages.


**API Endpoint**: `GET /packages`

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
res = client.packages.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.packages.list()

```

#### Response

##### Type
[PackagesListResponse](/checkr_api_py/types/models/packages_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Package <a name="get"></a>

Returns an existing Package with the input ID.


**API Endpoint**: `GET /packages/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Package to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.packages.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.packages.get(id="string")

```

#### Response

##### Type
[Package](/checkr_api_py/types/models/package.py)

##### Example
`{"apply_url": "https://apply.checkr.com/apply/customer-services-inc/532c20ea819b", "created_at": "2014-01-18T12:34:00Z", "deleted_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "name": "Criminal Pro", "price": 6500, "slug": "criminal_pro", "uri": "/v1/packages/e44aa283528e6fde7d542194"}`

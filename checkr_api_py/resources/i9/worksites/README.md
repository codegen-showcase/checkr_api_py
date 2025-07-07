
### Delete a Worksite <a name="delete"></a>

Deletes specified Worksite. If there are at least one Form I-9 associated
with a Worksite, this Worksite cannot be deleted.


**API Endpoint**: `DELETE /i9/worksites/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Worksite resource Id | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.worksites.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.worksites.delete(id="string")

```

### List existing Worksites <a name="list"></a>

Returns a list with all existing Worksites for the authenticated Checkr account.


**API Endpoint**: `GET /i9/worksites`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `order` | ✗ | Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.  | `"desc"` |
| `order_by` | ✗ | Returns records ordered by `field`.  If neither is specified, records will not be ordered.  | `"street_line1"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.worksites.list(order="desc", order_by="street_line1")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.worksites.list(order="desc", order_by="street_line1")

```

#### Response

##### Type
[I9WorksitesListResponse](/checkr_api_py/types/models/i9_worksites_list_response.py)

##### Example
`{"count": 1}`

### Retrieve a Worksite <a name="get"></a>

Returns a specified Worksite for the authenticated Checkr account.

**API Endpoint**: `GET /i9/worksites/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Worksite resource Id | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.worksites.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.worksites.get(id="string")

```

#### Response

##### Type
[WorksiteDetailed](/checkr_api_py/types/models/worksite_detailed.py)

##### Example
`{"id": "8046067e32ad6b25a9078735", "city": "San Francisco", "name": "Head Office", "state": "CA", "street_line1": "Some Rd", "street_line2": "Some Rd 2", "zip_code": "66554", "everify_status": "not_determined"}`

### Create new Worksite <a name="create"></a>

Create new Worksites for the authenticated account.


**API Endpoint**: `POST /i9/worksites`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `city` | ✗ | City of Worksite. | `"San Francisco"` |
| `name` | ✗ | Worksite name. | `"Head Office"` |
| `state` | ✗ | State of Worksite. | `"CA"` |
| `street_line1` | ✗ | Line one of Worksite address. | `"Some Rd"` |
| `street_line2` | ✗ | Line two of Worksite address. | `"Some Rd 2"` |
| `zip_code` | ✗ | ZIP Code of Worksite. | `"66554"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.worksites.create(
    city="San Francisco",
    name="Head Office",
    state="CA",
    street_line1="Some Rd",
    street_line2="Some Rd 2",
    zip_code="66554",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.worksites.create(
    city="San Francisco",
    name="Head Office",
    state="CA",
    street_line1="Some Rd",
    street_line2="Some Rd 2",
    zip_code="66554",
)

```

#### Response

##### Type
[WorksiteDetailed](/checkr_api_py/types/models/worksite_detailed.py)

##### Example
`{"id": "8046067e32ad6b25a9078735", "city": "San Francisco", "name": "Head Office", "state": "CA", "street_line1": "Some Rd", "street_line2": "Some Rd 2", "zip_code": "66554", "everify_status": "not_determined"}`

### Update Worksite information <a name="update"></a>

Update Worksite information


**API Endpoint**: `PUT /i9/worksites/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Worksite resource Id | `"string"` |
| `city` | ✗ | City of Worksite. | `"San Francisco"` |
| `everify_status` | ✗ | Worksite E-Verify Status. | `"inactive"` |
| `name` | ✗ | Worksite name. | `"Head Office"` |
| `state` | ✗ | State of Worksite. | `"CA"` |
| `street_line1` | ✗ | Line one of Worksite address. | `"Some Rd"` |
| `street_line2` | ✗ | Line two of Worksite address. | `"Some Rd 2"` |
| `zip_code` | ✗ | ZIP Code of Worksite. | `"66554"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.worksites.update(
    id="string",
    city="San Francisco",
    everify_status="inactive",
    name="Head Office",
    state="CA",
    street_line1="Some Rd",
    street_line2="Some Rd 2",
    zip_code="66554",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.worksites.update(
    id="string",
    city="San Francisco",
    everify_status="inactive",
    name="Head Office",
    state="CA",
    street_line1="Some Rd",
    street_line2="Some Rd 2",
    zip_code="66554",
)

```

#### Response

##### Type
[I9WorksitesUpdateResponse](/checkr_api_py/types/models/i9_worksites_update_response.py)

##### Example
`{"id": "79265751d363a140106fec15", "city": "San Francisco", "name": "Updated Worksite", "state": "California", "street_line1": "Some Rd first", "street_line2": "Some Rd second", "zip_code": "66554", "everify_status": "inactive"}`


### Delete an existing node <a name="delete"></a>

Deletes an existing node by custom_id.

Parent nodes and nodes assigned to continuous check subscriptions or legacy
subscriptions cannot be deleted.


**API Endpoint**: `DELETE /nodes/{custom_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `custom_id` | ✓ | custom_id of the Node. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.nodes.delete(custom_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.nodes.delete(custom_id="string")

```

#### Response

##### Type
[HierarchyNode](/checkr_api_py/types/models/hierarchy_node.py)

##### Example
`{"custom_id": "zpy8orej4r614ize", "name": "Acme Staffing", "packages": ["driver_pro", "tasker_pro"], "parent_custom_id": "parent custom id", "tier": "department"}`

### List existing Nodes <a name="list"></a>

Returns a list of existing Nodes that make up the current Account Hierarchy.

* If `include=packages` is passed, each Node object in the response will include a "packages" field. This will be an array of strings representing the slugs of the account Packages that are assigned (directly or indirectly) to the given Node. This field can be used to build UIs that truncate the list of Packages displayed to a requester, or to display only the nodes that are relevant to the requester.

* If `include=packages` is not passed, no package information will be included in the response.

This endpoint uses pagination; please see the corresponding [reference page](#section/Reference/Pagination) for details.


**API Endpoint**: `GET /nodes`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `include` | ✗ | Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors. | `"packages"` |
| `order` | ✗ | Returns records arranged in order as specified by the `order_by` parameter. If neither is specified, records will be listed in ascending order. | `"desc"` |
| `order_by` | ✗ | Returns records sorted by custom_id or created_at. If neither is specified, records will be sorted by created_at. | `"custom_id"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.nodes.list(include="packages", order="desc", order_by="custom_id")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.nodes.list(include="packages", order="desc", order_by="custom_id")

```

#### Response

##### Type
[NodesListResponse](/checkr_api_py/types/models/nodes_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing node <a name="get"></a>

Returns an existing node by custom_id.


* If `include=packages` is passed, the response will include a "packages" field.
This will be an array of strings representing the slugs of the account
Packages that are assigned (directly or indirectly) to the given Node. This field can be
used to build UIs that truncate the list of Packages displayed to a requester, or to
display only the nodes that are relevant to the requester.


* If `include=packages` is not passed, no package information will be included in the response.


**API Endpoint**: `GET /nodes/{custom_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `custom_id` | ✓ | custom_id of the Node. | `"string"` |
| `include` | ✗ | Includes a "packages" array with each Node object, containing a list of slugs for packages that are assigned to that node or its ancestors. | `"packages"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.nodes.get(custom_id="string", include="packages")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.nodes.get(custom_id="string", include="packages")

```

#### Response

##### Type
[HierarchyNode](/checkr_api_py/types/models/hierarchy_node.py)

##### Example
`{"custom_id": "zpy8orej4r614ize", "name": "Acme Staffing", "packages": ["driver_pro", "tasker_pro"], "parent_custom_id": "parent custom id", "tier": "department"}`

### Update an existing node <a name="patch"></a>

Updates the name and tier on an existing node by custom_id.


**API Endpoint**: `PATCH /nodes/{custom_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `custom_id` | ✓ | custom_id of the Node. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.nodes.patch(custom_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.nodes.patch(custom_id="string")

```

#### Response

##### Type
[HierarchyNode](/checkr_api_py/types/models/hierarchy_node.py)

##### Example
`{"custom_id": "zpy8orej4r614ize", "name": "Acme Staffing", "packages": ["driver_pro", "tasker_pro"], "parent_custom_id": "parent custom id", "tier": "department"}`

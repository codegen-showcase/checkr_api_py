
### Retrieve Hierarchy (Deprecated) <a name="list"></a>

**Note:** This endpoint is _deprecated_ and will no longer be supported. Please use the new [List existing Nodes](#operation/nodesList) endpoint instead.

Retrieves the current Hierarchy for the Account.

Returns the account hierarchy in its entirety, or from a specific node to its children. The returned JSON object will include the Packages assigned to each node in the dashboard. This is useful for building UIs that truncate the list of Packages displayed to a requester, or display only the nodes that are relevant to the requester.

Output is arranged hierarchically, with child nodes accessible through the parent node. Customers without large hierarchy mode enabled who do not specify pagination parameters will be returned the entire hierarchy. Customers with large hierarchy mode enabled and pagination parameters specified in this request will be returned the given page and number of results per page. If pagination parameters are not included, only the first page of the hierarchy will be returned.

**Note:** Customers with large hierarchy mode enabled will see a different response. Please reach out to clients@checkr.com if you have any questions.


**API Endpoint**: `GET /hierarchy`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `node_custom_ids` | ✗ | An array of `custom_ids` for the nodes to return. Returns the portion(s) of the Account Hierarchy matching the input nodes and their descendants. | `["string"]` |
| `page` | ✗ | Specifies the page to retrieve. The default page is 1. | `123.0` |
| `per_page` | ✗ | Indicates how many nodes each page should contain. The default per_page value is 20. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.hierarchy.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.hierarchy.list()

```

#### Response

##### Type
[HierarchyListResponse](/checkr_api_py/types/models/hierarchy_list_response.py)

##### Example
`{"sync_id": "account-da78fa2cd1e6ebee4b5975aa", "time": "2020-01-01T08:00:00Z"}`

### Create Hierarchy <a name="create"></a>

Creates a new or replaces an existing Account Hierarchy.

The Hierarchy endpoint performs ingestion asynchronously. Check the status
of the ingestion by calling `GET /v1/hierarchy/status`. Once ingested, use the Checkr Dashboard to assign your nodes to Packages, PAMs, and Users.


**API Endpoint**: `POST /hierarchy`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `nodes` | ✓ |  | `[{"custom_id": "zpy8orej4r614ize", "name": "Acme Staffing", "packages": ["driver_pro", "tasker_pro"], "parent_custom_id": "parent custom id", "tier": "department"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.hierarchy.create(
    nodes=[
        {
            "custom_id": "zpy8orej4r614ize",
            "name": "Acme Staffing",
            "packages": ["driver_pro", "tasker_pro"],
            "parent_custom_id": "parent custom id",
            "tier": "department",
        }
    ]
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.hierarchy.create(
    nodes=[
        {
            "custom_id": "zpy8orej4r614ize",
            "name": "Acme Staffing",
            "packages": ["driver_pro", "tasker_pro"],
            "parent_custom_id": "parent custom id",
            "tier": "department",
        }
    ]
)

```

#### Response

##### Type
[HierarchyCreateResponse](/checkr_api_py/types/models/hierarchy_create_response.py)

##### Example
`{"sync_id": "account-da78fa2cd1e6ebee4b5975aa", "time": "2020-02-11T00:27:14Z"}`

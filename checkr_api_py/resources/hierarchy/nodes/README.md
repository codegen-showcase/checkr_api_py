
### Add nodes to a hierarchy <a name="create"></a>

Adds new nodes to an existing Account Hierarchy.

This endpoint creates the nodes synchronously.


**API Endpoint**: `POST /hierarchy/nodes`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `nodes` | ✓ |  | `[{"custom_id": "zpy8orej4r614ize", "name": "Acme Staffing", "packages": ["driver_pro", "tasker_pro"], "parent_custom_id": "parent custom id", "tier": "department"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.hierarchy.nodes.create(
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
res = await client.hierarchy.nodes.create(
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


### Create a new Adverse Action <a name="create"></a>

Creates a new Adverse Action.

<b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.


**API Endpoint**: `POST /reports/{report_id}/adverse_actions`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `adverse_item_ids` | ✓ | IDs of Adverse Items selected for the Adverse Action. | `["string"]` |
| `report_id` | ✓ | The ID of the Report for which the Adverse Action will be created. | `"string"` |
| `medium` | ✗ | The medium through which the Adverse Action notification should be sent.  | `{}` |
| `post_notice_scheduled_at` | ✗ | Time at which the Post-Adverse Action notification will be sent. Default is 7 days after creation. | `"2016-10-07T12:34:00Z"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.adverse_actions.create(
    adverse_item_ids=["string"],
    report_id="string",
    post_notice_scheduled_at="2016-10-07T12:34:00Z",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.adverse_actions.create(
    adverse_item_ids=["string"],
    report_id="string",
    post_notice_scheduled_at="2016-10-07T12:34:00Z",
)

```

#### Response

##### Type
[AdverseAction](/checkr_api_py/types/models/adverse_action.py)

##### Example
`{"created_at": "2016-09-29T17:39:49Z", "id": "e44aa283528e6fde7d542194", "post_notice_ready_at": "2016-10-06T17:39:48Z", "post_notice_scheduled_at": "2016-10-07T12:34:00Z", "report_id": "b861a56db1b1b89692dd6118", "status": "pending", "uri": "/v1/adverse_actions/57ed51e57619e8002a6683f2"}`

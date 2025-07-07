
### Delete a tag from a Report <a name="delete"></a>

This request is used to delete a tag from a Report.


**API Endpoint**: `DELETE /reports/{id}/tags`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |
| `tag` | ✓ |  | `"West Coast"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.tags.delete(id="string", tag="West Coast")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.tags.delete(id="string", tag="West Coast")

```

#### Response

##### Type
[ReportsTagsDeleteResponse](/checkr_api_py/types/models/reports_tags_delete_response.py)

##### Example
`{"count": 1.0, "data": [{"name": "To Review"}], "object": "list"}`

### Retrieve tags for a Report <a name="list"></a>

Retrieves tags for the input Report.


**API Endpoint**: `GET /reports/{id}/tags`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.tags.list(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.tags.list(id="string")

```

#### Response

##### Type
[ReportTags](/checkr_api_py/types/models/report_tags.py)

##### Example
`{"count": 2.0, "data": [{"name": "EIN-234234234"}, {"name": "api-generated"}], "object": "list"}`

### Add a tag to a Report <a name="create"></a>

This request is used to add a tag to a Report.
<p><b>Note: </b>The <code>tag</code> value passed to <code>POST /v1/reports/{id}/tags</code> will match the <code>name</code> field in the response.</p>


**API Endpoint**: `POST /reports/{id}/tags`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |
| `tag` | ✓ |  | `"To Review"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.tags.create(id="string", tag="To Review")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.tags.create(id="string", tag="To Review")

```

#### Response

##### Type
[ReportsTagsCreateResponse](/checkr_api_py/types/models/reports_tags_create_response.py)

##### Example
`{"count": 3.0, "data": [{"name": "EIN-234234234"}, {"name": "api-generated"}, {"name": "In Progress"}], "object": "list"}`

### Update tags for a Report <a name="update"></a>

This request is used to define all tags for a Report.


**API Endpoint**: `PUT /reports/{id}/tags`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Report's ID. | `"string"` |
| `tags` | ✓ |  | `["To Review"]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.tags.update(id="string", tags=["To Review"])

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.tags.update(id="string", tags=["To Review"])

```

#### Response

##### Type
[ReportsTagsUpdateResponse](/checkr_api_py/types/models/reports_tags_update_response.py)

##### Example
`{"count": 2.0, "data": [{"name": "West Coast"}, {"name": "To Review"}], "object": "list"}`


### Cancel an existing Subscription <a name="delete"></a>

Cancels an existing Subscription.


**API Endpoint**: `DELETE /subscriptions/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Subscription. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.subscriptions.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.subscriptions.delete(id="string")

```

#### Response

##### Type
[SubscriptionCanceled](/checkr_api_py/types/models/subscription_canceled.py)

##### Example
`{"canceled_at": "2014-01-30T12:34:00Z", "candidate_id": "e44aa283528e6fde7d542194", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "interval_count": 1, "interval_unit": "month", "package": "driver_pro", "start_date": "2014-06-10", "status": "active", "uri": "/v1/subscriptions/4722c07dd9a10c3985ae432a"}`

### List existing Subscriptions <a name="list"></a>

Lists existing Subscriptions with the input parameters.

**API Endpoint**: `GET /subscriptions`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✗ | ID of the candidate to search for subscriptions. | `"string"` |
| `created_after` | ✗ | Returns subscriptions created after the input date. | `"1970-01-01T00:00:00"` |
| `created_before` | ✗ | Returns subscriptions created before the input date. | `"1970-01-01T00:00:00"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |
| `status` | ✗ | Returns subscriptions with the input status. | `"active"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.subscriptions.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.subscriptions.list()

```

#### Response

##### Type
[SubscriptionsListResponse](/checkr_api_py/types/models/subscriptions_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Subscription <a name="get"></a>

Retrieves an existing Subscription.


**API Endpoint**: `GET /subscriptions/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Subscription. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.subscriptions.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.subscriptions.get(id="string")

```

#### Response

##### Type
[Subscription](/checkr_api_py/types/models/subscription.py)

##### Example
`{"candidate_id": "4722c07dd9a10c3985ae432a", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "interval_count": 1, "interval_unit": "month", "next_occurrence_date": "2014-07-10", "node": "zpy8orej4r614ize", "package": "driver_pro", "start_date": "2014-06-10", "status": "active", "uri": "/v1/subscriptions/e44aa283528e6fde7d542194"}`

### Create a new Subscription <a name="create"></a>

Creates a new Subscription.

<b>Notes for International Customers: </b>Subscriptions are not available for reports which include international packages. 
If your candidate is located outside the US, you may not create a Subscription for them.


**API Endpoint**: `POST /subscriptions`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | ID of the candidate being screened. | `"string"` |
| `package` | ✓ | `slug` of the associated package.  | `"string"` |
| `start_date` | ✓ | Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run. | `"1970-01-01"` |
| `interval_count` | ✗ | The number of intervals between each recurrent background check. | `123` |
| `interval_unit` | ✗ | Interval at which the subscription will repeat. | `"day"` |
| `node` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts.  `custom_id` of the associated node.  | `"string"` |
| `work_locations` | ✗ | <font color="red">Required</font> for hierarchy-enabled accounts. Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.subscriptions.create(
    candidate_id="string", package="string", start_date="1970-01-01"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.subscriptions.create(
    candidate_id="string", package="string", start_date="1970-01-01"
)

```

#### Response

##### Type
[Subscription](/checkr_api_py/types/models/subscription.py)

##### Example
`{"candidate_id": "4722c07dd9a10c3985ae432a", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "interval_count": 1, "interval_unit": "month", "next_occurrence_date": "2014-07-10", "node": "zpy8orej4r614ize", "package": "driver_pro", "start_date": "2014-06-10", "status": "active", "uri": "/v1/subscriptions/e44aa283528e6fde7d542194"}`

### Update a Subscription <a name="update"></a>

Updates a Subscription. Specify only those parameters you wish to change.


**API Endpoint**: `POST /subscriptions/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Subscription. | `"string"` |
| `candidate_id` | ✗ | ID of the candidate being screened. | `"string"` |
| `interval_count` | ✗ | The number of intervals between each recurrent background check. | `123` |
| `interval_unit` | ✗ | Interval at which the subscription will repeat. | `"day"` |
| `node` | ✗ | `custom_id` of the associated node.  | `"string"` |
| `package` | ✗ | Package to run for the Report. | `"string"` |
| `start_date` | ✗ | Start date for the subscription. This is the date on which the subscription will begin, and the first time the report will be run. | `"1970-01-01"` |
| `work_locations` | ✗ | Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.subscriptions.update(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.subscriptions.update(id="string")

```

#### Response

##### Type
[Subscription](/checkr_api_py/types/models/subscription.py)

##### Example
`{"candidate_id": "4722c07dd9a10c3985ae432a", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "interval_count": 1, "interval_unit": "month", "next_occurrence_date": "2014-07-10", "node": "zpy8orej4r614ize", "package": "driver_pro", "start_date": "2014-06-10", "status": "active", "uri": "/v1/subscriptions/e44aa283528e6fde7d542194"}`

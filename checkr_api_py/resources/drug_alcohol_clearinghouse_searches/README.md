
### Retrieve an existing Drug & Alcohol Clearinghouse Search <a name="get"></a>

Returns an existing Drug & Alcohol Clearinghouse Search with the input ID.


**API Endpoint**: `GET /drug_alcohol_clearinghouse_searches/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Drug & Alcohol Clearinghouse Search to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.drug_alcohol_clearinghouse_searches.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.drug_alcohol_clearinghouse_searches.get(id="string")

```

#### Response

##### Type
[DrugAlcoholClearinghouse](/checkr_api_py/types/models/drug_alcohol_clearinghouse.py)

##### Example
`{"cancellation_reason": "candidate_missing_consent", "cancellation_reason_description": "Candidate consent not provided", "id": "e44aa283528e6fde7d542194", "query_result": "Driver Not Prohibited", "report_id": "539fd88c101897f7cd000007", "status": "complete"}`


### Retrieve an existing International Motor Vehicle Report <a name="get"></a>

Returns an existing International Motor Vehicle Report with the input ID.


**API Endpoint**: `GET /international_motor_vehicle_reports/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the International Motor Vehicle Report to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.international_motor_vehicle_reports.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.international_motor_vehicle_reports.get(id="string")

```

#### Response

##### Type
[InternationalMotorVehicleReport](/checkr_api_py/types/models/international_motor_vehicle_report.py)

##### Example
`{"cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "could be anything", "result": "clear", "status": "complete", "turnaround_time": 90, "uri": "could be anything", "country": "CA", "pdf_url": "https://eu-west-1-checkr-staging.s3.eu-west-1.amazonaws.com/document.pdf"}`

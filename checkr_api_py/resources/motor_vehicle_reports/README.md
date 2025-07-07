
### Retrieve an existing Motor Vehicle Report <a name="get"></a>

Returns an existing Motor Vehicle Report with the input ID.


**API Endpoint**: `GET /motor_vehicle_reports/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Motor Vehicle Report to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.motor_vehicle_reports.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.motor_vehicle_reports.get(id="string")

```

#### Response

##### Type
[MotorVehicleReport](/checkr_api_py/types/models/motor_vehicle_report.py)

##### Example
`{"assessment": "eligible", "cancellation_reason": "complete_now_customer_requested", "cancellation_reason_description": "Customer requested Complete Now prior to screening completion", "completed_at": "2014-01-18T12:35:30Z", "created_at": "2014-01-18T12:34:00Z", "id": "e44aa283528e6fde7d542194", "turnaround_time": "could be anything", "uri": "could be anything", "dob": "1980-01-01", "expiration_date": "2016-07-24", "first_issued_date": "2000-01-14", "full_name": "John Alfred Smith", "issued_date": "2006-12-03", "license_class": "C", "license_number": "F2111132", "license_state": "CA", "license_status": "valid, expired, not_found", "license_type": "personal, commercial, or non-commercial", "previous_license_number": "F2111132", "previous_license_state": "CA", "privilege_to_drive": "valid", "type_": "standard"}`

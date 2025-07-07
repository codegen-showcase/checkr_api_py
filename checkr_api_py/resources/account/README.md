
### Retrieve authenticated account details <a name="list"></a>

Returns Account details for the authenticated account.


**API Endpoint**: `GET /account`

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.account.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.account.list()

```

#### Response

##### Type
[Account](/checkr_api_py/types/models/account.py)

##### Example
`{"adverse_action_email": "john.doe@example.com", "api_authorized": True, "authorized": True, "available_screenings": ["county_civil_search", "county_criminal_search", "municipal_criminal_search", "education_verification", "employment_verification", "federal_civil_search", "federal_criminal_search", "motor_vehicle_report", "national_criminal_search", "sex_offender_search", "ssn_trace", "state_criminal_search", "international_adverse_media_search", "international_education_verification"], "billing_email": "john.doe@example.com", "compliance_contact_email": "compliance.team@example.com", "created_at": "2020-01-07T00:26:49Z", "default_compliance_city": "San Francisco", "default_compliance_state": "CA", "name": "Acme Corp", "support_email": "support@example.com", "support_phone": "206-555-0188", "technical_contact_email": "jane.smith@example.com", "uri": "/v1/accounts/e44aa283528e6fde7d542194", "uri_name": "acme-corp"}`

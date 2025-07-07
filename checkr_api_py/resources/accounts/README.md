
### Create a new Account <a name="create"></a>

Creates a customer Account associated with your [Partner Application](#section/Checkr-Partners).
Only Checkr Partners are authorized to use this endpoint.


**API Endpoint**: `POST /accounts`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `client_id` | ✓ | Client credentials provided as part of your Partner Application. | `"56269e3411a549fd07ed8d92"` |
| `company` | ✓ |  | `{"city": "San Francisco", "dba_name": "Acme", "incorporation_state": "CA", "industry": "72", "phone": "206-555-0100", "state": "CA", "street": "123 Main Street", "tax_id": "123456789", "website": "https://www.example.com", "zipcode": "94107"}` |
| `name` | ✓ | Name of Account displayed in the Dashboard. | `"Acme Corporation"` |
| `purpose` | ✓ | Permissible purpose to run background checks. Determines which background checks the Account is credentialed for.  | `"employment"` |
| `user` | ✓ |  | `{"email": "user@example.com", "full_name": "Jeanette Hughes"}` |
| `default_compliance_city` | ✗ | Fallback compliance city if candidate location is not provided.  | `"San Francisco"` |
| `default_compliance_state` | ✗ | Fallback compliance state if candidate location is not provided. Format: `ISO 3166-2:US`.  | `"CA"` |
| `oauth_authorize` | ✗ | Allows skipping of the /oauth/authorize call | `True` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.accounts.create(
    client_id="56269e3411a549fd07ed8d92",
    company={
        "city": "San Francisco",
        "dba_name": "Acme",
        "incorporation_state": "CA",
        "industry": "72",
        "phone": "206-555-0100",
        "state": "CA",
        "street": "123 Main Street",
        "tax_id": "123456789",
        "website": "https://www.example.com",
        "zipcode": "94107",
    },
    name="Acme Corporation",
    purpose="employment",
    user={"email": "user@example.com", "full_name": "Jeanette Hughes"},
    default_compliance_city="San Francisco",
    default_compliance_state="CA",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.accounts.create(
    client_id="56269e3411a549fd07ed8d92",
    company={
        "city": "San Francisco",
        "dba_name": "Acme",
        "incorporation_state": "CA",
        "industry": "72",
        "phone": "206-555-0100",
        "state": "CA",
        "street": "123 Main Street",
        "tax_id": "123456789",
        "website": "https://www.example.com",
        "zipcode": "94107",
    },
    name="Acme Corporation",
    purpose="employment",
    user={"email": "user@example.com", "full_name": "Jeanette Hughes"},
    default_compliance_city="San Francisco",
    default_compliance_state="CA",
)

```

#### Response

##### Type
[Account](/checkr_api_py/types/models/account.py)

##### Example
`{"adverse_action_email": "john.doe@example.com", "api_authorized": True, "authorized": True, "available_screenings": ["county_civil_search", "county_criminal_search", "municipal_criminal_search", "education_verification", "employment_verification", "federal_civil_search", "federal_criminal_search", "motor_vehicle_report", "national_criminal_search", "sex_offender_search", "ssn_trace", "state_criminal_search", "international_adverse_media_search", "international_education_verification"], "billing_email": "john.doe@example.com", "compliance_contact_email": "compliance.team@example.com", "created_at": "2020-01-07T00:26:49Z", "default_compliance_city": "San Francisco", "default_compliance_state": "CA", "name": "Acme Corp", "support_email": "support@example.com", "support_phone": "206-555-0188", "technical_contact_email": "jane.smith@example.com", "uri": "/v1/accounts/e44aa283528e6fde7d542194", "uri_name": "acme-corp"}`

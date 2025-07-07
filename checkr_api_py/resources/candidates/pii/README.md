
### Request PII removal for a Candidate <a name="delete"></a>

Requests the removal of PII from an existing Candidate

Requesting the removal of PII from a candidate who has already had PII removed will result in an error.


**API Endpoint**: `DELETE /candidates/{id}/pii`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `deletion_contact_email_address` | ✓ | Email address of person requesting candidate's PII removal. | `"john.smith@gmail.com"` |
| `id` | ✓ | The Candidate's ID. | `"string"` |
| `deletion_contact_first_name` | ✗ | First name of person requesting candidate's PII removal. | `"John"` |
| `deletion_contact_last_name` | ✗ | Last name of person requesting candidate's PII removal. | `"Smith"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.pii.delete(
    deletion_contact_email_address="john.smith@gmail.com",
    id="string",
    deletion_contact_first_name="John",
    deletion_contact_last_name="Smith",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.pii.delete(
    deletion_contact_email_address="john.smith@gmail.com",
    id="string",
    deletion_contact_first_name="John",
    deletion_contact_last_name="Smith",
)

```

#### Response

##### Type
[Candidate](/checkr_api_py/types/models/candidate.py)

##### Example
`{"dob": "1970-01-22", "driver_license_number": "F2111655", "driver_license_state": "CA", "email": "john.smith@gmail.com", "first_name": "John", "id": "e44aa283528e6fde7d542194", "last_name": "Smith", "middle_name": "Alfred", "mother_maiden_name": "Jones", "phone": "5555555555", "postal_address": {"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}, "previous_driver_license_number": "F1501739", "previous_driver_license_state": "MD", "ssn": "XXX-XX-4645", "uri": "/v1/candidates/e44aa283528e6fde7d542194", "zipcode": "90401"}`


### Delete an existing Professional License <a name="delete"></a>

Deletes an existing Professional License


**API Endpoint**: `DELETE /candidates/{candidate_id}/professional_licenses/{license_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID | `"string"` |
| `license_id` | ✓ | The ID of the license to delete. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.professional_licenses.delete(
    candidate_id="string", license_id="string"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.professional_licenses.delete(
    candidate_id="string", license_id="string"
)

```

#### Response

##### Type
[CandidatesProfessionalLicensesDeleteResponse](/checkr_api_py/types/models/candidates_professional_licenses_delete_response.py)

##### Example
`{"expiration_date": "2033-01-30", "id": "e44aa283528e6fde7d542194", "issuer_name": "Medical Board of California", "issuer_region": "CA", "license_number": "A 12345", "license_type": "Physician", "deleted_at": "2023-10-10T01:16:27.000Z"}`

### List existing Professional Licenses <a name="list"></a>

Returns a list of existing Professional Licenses for the given Candidate ID.


**API Endpoint**: `GET /candidates/{candidate_id}/professional_licenses`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.professional_licenses.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.professional_licenses.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesProfessionalLicensesListResponse](/checkr_api_py/types/models/candidates_professional_licenses_list_response.py)

##### Example
`{"count": 1}`

### Create a new Professional License <a name="create"></a>

Creates a new Professional License for a given candidate. A maximum of two licenses may exist for each candidate. When a report is run with [Professional License Verification](#tag/Professional-License-Verification), all candidate licenses existing at the time of report creation will be included for verification.


**API Endpoint**: `POST /candidates/{candidate_id}/professional_licenses`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID | `"string"` |
| `data` | ✗ |  | `{"expiration_date": "2033-01-30", "id": "e44aa283528e6fde7d542194", "issuer_name": "Medical Board of California", "issuer_region": "CA", "license_number": "A 12345", "license_type": "Physician", "certification_document_id": "string"}` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.professional_licenses.create(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.professional_licenses.create(candidate_id="string")

```

#### Response

##### Type
[ProfessionalLicense](/checkr_api_py/types/models/professional_license.py)

##### Example
`{"expiration_date": "2033-01-30", "id": "e44aa283528e6fde7d542194", "issuer_name": "Medical Board of California", "issuer_region": "CA", "license_number": "A 12345", "license_type": "Physician"}`

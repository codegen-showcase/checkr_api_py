
### Delete an existing Driver License <a name="delete"></a>

Deletes a specific driver license for a given candidate.


**API Endpoint**: `DELETE /candidates/{candidate_id}/driver_licenses/{driver_license_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `driver_license_id` | ✓ | The Driver License ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.driver_licenses.delete(
    candidate_id="string", driver_license_id="string"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.driver_licenses.delete(
    candidate_id="string", driver_license_id="string"
)

```

#### Response

##### Type
[DriverLicense](/checkr_api_py/types/models/driver_license.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "current": True, "id": "e44aa283528e6fde7d542194", "issued_dates": [{"source": "client", "value": "2010-01-30"}], "number": "F2222222", "source": "Self-Disclosure", "state": "CA", "uri": "/v1/candidates/551564b7865af96a28b13f36/driver_licenses/e44aa283528e6fde7d542194"}`

### List existing Driver Licenses <a name="list"></a>

Returns a list of existing Driver Licenses for the input Candidate ID.


**API Endpoint**: `GET /candidates/{candidate_id}/driver_licenses`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.driver_licenses.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.driver_licenses.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesDriverLicensesListResponse](/checkr_api_py/types/models/candidates_driver_licenses_list_response.py)

##### Example
`{"count": 1}`

### Retrieve an existing Driver License <a name="get"></a>

Returns a specific driver license for a given candidate.


**API Endpoint**: `GET /candidates/{candidate_id}/driver_licenses/{driver_license_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `driver_license_id` | ✓ | The Driver License ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.driver_licenses.get(
    candidate_id="string", driver_license_id="string"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.driver_licenses.get(
    candidate_id="string", driver_license_id="string"
)

```

#### Response

##### Type
[DriverLicense](/checkr_api_py/types/models/driver_license.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "current": True, "id": "e44aa283528e6fde7d542194", "issued_dates": [{"source": "client", "value": "2010-01-30"}], "number": "F2222222", "source": "Self-Disclosure", "state": "CA", "uri": "/v1/candidates/551564b7865af96a28b13f36/driver_licenses/e44aa283528e6fde7d542194"}`

### Create a new Driver License <a name="create"></a>

Creates a new Driver License for a given candidate.

If a `current` driver license is created for a candidate with an existing driver license marked `current`, the existing license will be updated to reflect that it is no longer `current`.

If a `candidate_driver_license` exists with the `state` and `number` passed in with the POST request, a new license will not be created. The `current` and `issued_date` values of the existing license will be updated with on the parameters passed.

**Note:** When a new driver license is created, Checkr will attempt to apply the new license information to resolve any existing exceptions for the candidate's most recent MVR screening if the screening has not yet produced reportable results.


See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid driver license number input by state.


**API Endpoint**: `POST /candidates/{candidate_id}/driver_licenses`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `current` | ✓ | Defines whether the driver license is the candidate's current license. `true` if the license is the candidate's current license, `false` otherwise. | `True` |
| `number` | ✓ | The driver license number. | `"F2222222"` |
| `state` | ✓ | The state that issued the driver license. | `"CA"` |
| `issued_date` | ✗ | The issued date of the driver license. | `"2010-01-30"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.driver_licenses.create(
    candidate_id="string",
    current=True,
    number="F2222222",
    state="CA",
    issued_date="2010-01-30",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.driver_licenses.create(
    candidate_id="string",
    current=True,
    number="F2222222",
    state="CA",
    issued_date="2010-01-30",
)

```

#### Response

##### Type
[DriverLicense](/checkr_api_py/types/models/driver_license.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "current": True, "id": "e44aa283528e6fde7d542194", "issued_dates": [{"source": "client", "value": "2010-01-30"}], "number": "F2222222", "source": "Self-Disclosure", "state": "CA", "uri": "/v1/candidates/551564b7865af96a28b13f36/driver_licenses/e44aa283528e6fde7d542194"}`

### Update an existing Driver License <a name="update"></a>

Updates an existing Driver License for a given candidate.

**Note**: Updating an existing license to `current: true` will set any existing `current` license to `current: false`.


**API Endpoint**: `POST /candidates/{candidate_id}/driver_licenses/{driver_license_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `driver_license_id` | ✓ | The Driver License ID. | `"string"` |
| `current` | ✗ | The updated current status of the driver license. `true` if the license is the candidate's current license, `false` otherwise. | `True` |
| `issued_date` | ✗ | The updated issued date of the driver license. | `"2010-01-30"` |
| `number` | ✗ | The updated number of the driver license. | `"F1111111"` |
| `state` | ✗ | The updated state that issued the driver license. | `"CA"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.driver_licenses.update(
    candidate_id="string",
    driver_license_id="string",
    issued_date="2010-01-30",
    number="F1111111",
    state="CA",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.driver_licenses.update(
    candidate_id="string",
    driver_license_id="string",
    issued_date="2010-01-30",
    number="F1111111",
    state="CA",
)

```

#### Response

##### Type
[DriverLicense](/checkr_api_py/types/models/driver_license.py)

##### Example
`{"candidate_id": "551564b7865af96a28b13f36", "current": True, "id": "e44aa283528e6fde7d542194", "issued_dates": [{"source": "client", "value": "2010-01-30"}], "number": "F2222222", "source": "Self-Disclosure", "state": "CA", "uri": "/v1/candidates/551564b7865af96a28b13f36/driver_licenses/e44aa283528e6fde7d542194"}`

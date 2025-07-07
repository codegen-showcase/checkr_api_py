
### Delete an existing School <a name="delete"></a>

Deletes an existing School with the input `school_id`.


**API Endpoint**: `DELETE /candidates/{candidate_id}/schools/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `id` | ✓ | The School's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.schools.delete(candidate_id="string", id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.schools.delete(candidate_id="string", id="string")

```

#### Response

##### Type
[School](/checkr_api_py/types/models/school.py)

##### Example
`{"candidate_id": "83ebeagdec0948690863766f792ead24d61fe3f9", "degree": "BA", "end_date": "2017-05-10", "id": "e44aa283528e6fde7d542194", "major": "Russian Literature", "minor": "Background Checks", "name": "College University", "phone": "415-111-1111", "school_url": "www.collegeuniversity.com", "start_date": "2012-09-22", "uri": "/v1/schools/e44aa283528e6fde7d542194", "year_awarded": 2017}`

### List existing Schools <a name="list"></a>

Returns a list of existing Schools for the input `candidate_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/schools`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | Returns the list of schools for the input `candidate_id`. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.schools.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.schools.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesSchoolsListResponse](/checkr_api_py/types/models/candidates_schools_list_response.py)

##### Example
`{}`

### Retrieve an existing School <a name="get"></a>

Returns an existing School with the input `school_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/schools/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `id` | ✓ | The School's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.schools.get(candidate_id="string", id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.schools.get(candidate_id="string", id="string")

```

#### Response

##### Type
[School](/checkr_api_py/types/models/school.py)

##### Example
`{"candidate_id": "83ebeagdec0948690863766f792ead24d61fe3f9", "degree": "BA", "end_date": "2017-05-10", "id": "e44aa283528e6fde7d542194", "major": "Russian Literature", "minor": "Background Checks", "name": "College University", "phone": "415-111-1111", "school_url": "www.collegeuniversity.com", "start_date": "2012-09-22", "uri": "/v1/schools/e44aa283528e6fde7d542194", "year_awarded": 2017}`

### Create a new School <a name="create"></a>

Creates a new School resource.

Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.

If the country is not US, the following parameters are required in addition to those marked as required below:

- year_awarded
- phone
- minor
- start_date
- end_date
- current
- address
  - street
  - city
  - zipcode
  - state
  - country


**API Endpoint**: `POST /candidates/{candidate_id}/schools`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `address` | ✓ |  | `{"city": "San Francisco", "country": "US", "state": "CA", "street": "123 Main St.", "unit": "2000", "zipcode": "90401"}` |
| `candidate_id_path` | ✓ | Creates a School for the input `candidate_id`. | `"string"` |
| `degree` | ✓ | Degree awarded to the Candidate. | `"BA"` |
| `major` | ✓ | Candidate’s major. | `"Russian Literature"` |
| `name` | ✓ | Name of the School. | `"College University"` |
| `candidate_id` | ✗ | Candidate linked to this School resource. | `"83ebeagdec0948690863766f792ead24d61fe3f9"` |
| `current` | ✗ | Defines whether the Candidate is currently enrolled. | `True` |
| `end_date` | ✗ | Candidate’s end date with the School. | `"2017-05-10"` |
| `id` | ✗ |  | `"e44aa283528e6fde7d542194"` |
| `minor` | ✗ | Candidate’s minor. | `"Background Checks"` |
| `object` | ✗ |  | `"school"` |
| `phone` | ✗ | School's phone number. | `"415-111-1111"` |
| `school_url` | ✗ | School’s website. | `"www.collegeuniversity.com"` |
| `start_date` | ✗ | Candidate’s start date with the School. | `"2012-09-22"` |
| `year_awarded` | ✗ | Year in which the degree was awarded. | `2017` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.schools.create(
    address={
        "city": "San Francisco",
        "country": "US",
        "state": "CA",
        "street": "123 Main St.",
        "unit": "2000",
        "zipcode": "90401",
    },
    candidate_id_path="string",
    degree="BA",
    major="Russian Literature",
    name="College University",
    candidate_id="83ebeagdec0948690863766f792ead24d61fe3f9",
    end_date="2017-05-10",
    minor="Background Checks",
    phone="415-111-1111",
    school_url="www.collegeuniversity.com",
    start_date="2012-09-22",
    year_awarded=2017,
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.schools.create(
    address={
        "city": "San Francisco",
        "country": "US",
        "state": "CA",
        "street": "123 Main St.",
        "unit": "2000",
        "zipcode": "90401",
    },
    candidate_id_path="string",
    degree="BA",
    major="Russian Literature",
    name="College University",
    candidate_id="83ebeagdec0948690863766f792ead24d61fe3f9",
    end_date="2017-05-10",
    minor="Background Checks",
    phone="415-111-1111",
    school_url="www.collegeuniversity.com",
    start_date="2012-09-22",
    year_awarded=2017,
)

```

#### Response

##### Type
[School](/checkr_api_py/types/models/school.py)

##### Example
`{"candidate_id": "83ebeagdec0948690863766f792ead24d61fe3f9", "degree": "BA", "end_date": "2017-05-10", "id": "e44aa283528e6fde7d542194", "major": "Russian Literature", "minor": "Background Checks", "name": "College University", "phone": "415-111-1111", "school_url": "www.collegeuniversity.com", "start_date": "2012-09-22", "uri": "/v1/schools/e44aa283528e6fde7d542194", "year_awarded": 2017}`

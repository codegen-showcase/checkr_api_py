
### Delete an existing Employer <a name="delete"></a>

Deletes an existing Employer with the input `id`.


**API Endpoint**: `DELETE /candidates/{candidate_id}/employers/{employer_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `employer_id` | ✓ | The Employer's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.employers.delete(candidate_id="string", employer_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.employers.delete(
    candidate_id="string", employer_id="string"
)

```

#### Response

##### Type
[Employer](/checkr_api_py/types/models/employer.py)

##### Example
`{"candidate_id": "xxx", "contract_type": "full_time", "do_not_contact": False, "employer_url": "www.employer.com", "end_date": "2017-05-01", "id": "e44aa283528e6fde7d542194", "name": "Checkr", "position": "Software Engineer", "salary": 10000, "start_date": "2016-06-01", "uri": "/v1/candidates/e44aa283528e6fde7d542194/employers/ca27df84be5b50dfa7ee1cda"}`

### List existing Employers <a name="list"></a>

Returns a list of existing Employers for the input `candidate_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/employers`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | Returns the list of employers for the input `candidate_id`. | `"string"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.employers.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.employers.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesEmployersListResponse](/checkr_api_py/types/models/candidates_employers_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Employer <a name="get"></a>

Returns an existing Employer with the input `candidate_id` or `employer_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/employers/{employer_id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | The Candidate's ID. | `"string"` |
| `employer_id` | ✓ | The Employer's ID. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.employers.get(candidate_id="string", employer_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.employers.get(candidate_id="string", employer_id="string")

```

#### Response

##### Type
[Employer](/checkr_api_py/types/models/employer.py)

##### Example
`{"candidate_id": "xxx", "contract_type": "full_time", "do_not_contact": False, "employer_url": "www.employer.com", "end_date": "2017-05-01", "id": "e44aa283528e6fde7d542194", "name": "Checkr", "position": "Software Engineer", "salary": 10000, "start_date": "2016-06-01", "uri": "/v1/candidates/e44aa283528e6fde7d542194/employers/ca27df84be5b50dfa7ee1cda"}`

### Create a new Employer <a name="create"></a>

Creates a new Employer resource.

If the country is not US, the following parameters will be required in addition to those marked as required in the table below:

- salary
- address:
  - street
  - country
  - zipcode
- manager:
  - name
  - title

Validation for `start_date` and `end_date` is performed to ensure logical dates are provided. `end_date` must be after `start_date`, and both dates must be after 1900-01-01.


**API Endpoint**: `POST /candidates/{candidate_id}/employers`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `address` | ✓ |  | `{"city": "San Francisco", "country": "US", "state": "CA", "street": "123 Main St.", "unit": "2000", "zipcode": "90401"}` |
| `candidate_id_path` | ✓ | Create an employer for the input `candidate_id`. | `"string"` |
| `contract_type` | ✓ | Candidate’s contract type. | `"full_time"` |
| `name` | ✓ | Candidate’s employer’s name. | `"Checkr"` |
| `position` | ✓ | Candidate’s position or title. | `"Software Engineer"` |
| `start_date` | ✓ | Candidate’s start date with the employer. | `"2016-06-01"` |
| `candidate_id` | ✗ | ID of the Candidate being screened. | `"xxx"` |
| `do_not_contact` | ✗ | If `true`, the employer will not be contacted about the Candidate. | `False` |
| `employer_url` | ✗ | Employer’s website. | `"www.employer.com"` |
| `end_date` | ✗ | Candidate’s end date with the employer. | `"2017-05-01"` |
| `id` | ✗ |  | `"e44aa283528e6fde7d542194"` |
| `manager` | ✗ |  | `{"email": "joesmith@checkr.co", "name": "Joe Smith", "phone": "212-555-1234", "title": "Engineering Manager"}` |
| `note` | ✗ | A text note used to add context for an employment gap. | `"Took time off to travel abroad."` |
| `object` | ✗ |  | `"employer"` |
| `salary` | ✗ | Candidate’s gross salary in dollars annually. | `10000` |
| `type` | ✗ | Type of employment history to be created.  If type is set to `gap` only `start_date` is required, and only `start_date`, `end_date`, and `note` will be recorded.  | `"employer"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.employers.create(
    address={
        "city": "San Francisco",
        "country": "US",
        "state": "CA",
        "street": "123 Main St.",
        "unit": "2000",
        "zipcode": "90401",
    },
    candidate_id_path="string",
    contract_type="full_time",
    name="Checkr",
    position="Software Engineer",
    start_date="2016-06-01",
    candidate_id="xxx",
    do_not_contact=False,
    employer_url="www.employer.com",
    end_date="2017-05-01",
    note="Took time off to travel abroad.",
    salary=10000,
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.employers.create(
    address={
        "city": "San Francisco",
        "country": "US",
        "state": "CA",
        "street": "123 Main St.",
        "unit": "2000",
        "zipcode": "90401",
    },
    candidate_id_path="string",
    contract_type="full_time",
    name="Checkr",
    position="Software Engineer",
    start_date="2016-06-01",
    candidate_id="xxx",
    do_not_contact=False,
    employer_url="www.employer.com",
    end_date="2017-05-01",
    note="Took time off to travel abroad.",
    salary=10000,
)

```

#### Response

##### Type
[Employer](/checkr_api_py/types/models/employer.py)

##### Example
`{"candidate_id": "xxx", "contract_type": "full_time", "do_not_contact": False, "employer_url": "www.employer.com", "end_date": "2017-05-01", "id": "e44aa283528e6fde7d542194", "name": "Checkr", "position": "Software Engineer", "salary": 10000, "start_date": "2016-06-01", "uri": "/v1/candidates/e44aa283528e6fde7d542194/employers/ca27df84be5b50dfa7ee1cda"}`

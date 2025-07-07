
### List existing Candidates <a name="list"></a>

Lists existing Candidates with the input parameters.

<b>Note: </b>This call will not return candidates with non-US `work_locations`. Use [GET /candidates/{id}](#operation/getCandidate) to retrieve candidates outside the US.


**API Endpoint**: `GET /candidates`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `adjudication` | ✗ | Returns candidates with the input adjudication. `Null` if no adjudication has been made. | `"string"` |
| `created_after` | ✗ | Returns candidates created after the input date. | `"1970-01-01T00:00:00"` |
| `created_before` | ✗ | Returns candidates created before the input date. | `"1970-01-01T00:00:00"` |
| `custom_id` | ✗ | Returns candidates with the input `custom_id`. | `"string"` |
| `driver_license_number` | ✗ | Returns candidates with the input `driver_license_number`. | `"string"` |
| `email` | ✗ | Returns candidates with the input email address. | `"string"` |
| `full_name` | ✗ | Returns candidates with the input `full_name`. | `"string"` |
| `geo_id` | ✗ | Returns candidates with the input `geo_id`. | `"string"` |
| `metadata` | ✗ | Returns candidates matching the input key-values. Input keys will be matched exactly. Input values will be pre- and post-pended with wildcards. (For example: A query for 1234 will return results for *1234*.) | `{}` |
| `page` | ✗ | Specifies the page number to retrieve. | `123.0` |
| `per_page` | ✗ | Indicates how many records each page should contain. The default value is 25 records. | `123.0` |
| `program_id` | ✗ | Returns candidates with the input `program_id`. | `"string"` |
| `report_adjudicated_after` | ✗ | Returns candidates adjudicated after the input date. | `"1970-01-01T00:00:00"` |
| `report_adjudicated_before` | ✗ | Returns candidates adjudicated before the input date. | `"1970-01-01T00:00:00"` |
| `report_adjudicator_email` | ✗ | Returns candidates with a report adjudicated by someone with input `adjudicator_email`. | `"string"` |
| `report_revised_after` | ✗ | Returns candidates with a report revised after the input date. | `"1970-01-01T00:00:00"` |
| `report_revised_before` | ✗ | Returns candidates with a report revised before the input date. | `"1970-01-01T00:00:00"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.list()

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.list()

```

#### Response

##### Type
[CandidatesListResponse](/checkr_api_py/types/models/candidates_list_response.py)

##### Example
`{"count": 2}`

### Retrieve an existing Candidate <a name="get"></a>

Retrieves an existing Candidate.


**API Endpoint**: `GET /candidates/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | The Candidate's ID. | `"string"` |
| `include` | ✗ | Comma delimited string specifying the resources to be embedded in the returned Candidate object. See [Embedding Resources](#section/Reference/Embedding-Resources). | `"reports"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.get(id="string", include="reports")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.get(id="string", include="reports")

```

#### Response

##### Type
[Candidate](/checkr_api_py/types/models/candidate.py)

##### Example
`{"dob": "1970-01-22", "driver_license_number": "F2111655", "driver_license_state": "CA", "email": "john.smith@gmail.com", "first_name": "John", "id": "e44aa283528e6fde7d542194", "last_name": "Smith", "middle_name": "Alfred", "mother_maiden_name": "Jones", "phone": "5555555555", "postal_address": {"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}, "previous_driver_license_number": "F1501739", "previous_driver_license_state": "MD", "ssn": "XXX-XX-4645", "uri": "/v1/candidates/e44aa283528e6fde7d542194", "zipcode": "90401"}`

### Create a new Candidate <a name="create"></a>

Creates a new Candidate resource.

### Required attributes

The Candidate resource’s required attributes vary depending on its intended use. If this resource is to be used in conjunction with the Invitations API (in which the invitation apply form collects the Candidate's personal information), the only strictly required Candidate attribute is `email`.

If this resource is to be used to generate any other report type, other personal information is also required.

Attributes required to generate a Report include:
- `first_name`
- `middle_name` or `no_middle_name`
- `last_name`
- `dob`

Attributes required to generate a Report with a criminal check screening:
- `ssn`
- `zipcode`

Attributes required to generate a report with a Motor Vehicle Record (MVR) screening:
- `driver_license_number`
- `driver_license_state`

See [Driver License validation](#section/Reference/Driver-License-validation) in the Reference section for a list of valid input by state.

Attributes recommended to generate a report with an Identity Document Verification screening:
- `phone` (mobile phone number)

Validation for these attributes is performed when requesting a Report, as the requirements depend on the Package.

Checkr's product incorporates SSN field controls designed to not accept SSNs with the following characteristics:

  - SSNs without exactly 9 numeric characters
  - SSNs that start with 666 (666-34-3768)
  - SSNs that start with 9 (967-65-4325)
  - SSNs that are a single digit (111-11-1111)
  - SSNs that are sequential digits (123-45-6789)


**API Endpoint**: `POST /candidates`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `email` | ✓ | Candidate’s email address.  | `"john.smith@gmail.com"` |
| `copy_requested` | ✗ | If `true`, the candidate has asked to receive a copy of their report. | `True` |
| `custom_id` | ✗ | Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API. | `"HRIS-27"` |
| `dob` | ✗ | Candidate’s date of birth. | `"1970-01-22"` |
| `driver_license_number` | ✗ | Candidate’s driver license number. | `"F2111655"` |
| `driver_license_state` | ✗ | Candidate’s driver license state of issue. Format: `ISO 3166-2:US`.  | `"CA"` |
| `first_name` | ✗ | Candidate’s first name.  | `"John"` |
| `geo_ids` | ✗ | Array of Geo IDs. | `["79f943e212cce7de21c054a8"]` |
| `last_name` | ✗ | Candidate’s last name. | `"Smith"` |
| `metadata` | ✗ |  | `{}` |
| `middle_name` | ✗ | Candidate’s middle name. This field is required if `no_middle_name` is `false`.  | `"Alfred"` |
| `mother_maiden_name` | ✗ | Candidate’s mother’s maiden name.  | `"Jones"` |
| `no_middle_name` | ✗ | Required if no `middle_name` is provided. `true` if the candidate has no middle name.  | `True` |
| `object` | ✗ |  | `"candidate"` |
| `phone` | ✗ | Candidate’s phone number. | `"5555555555"` |
| `postal_address` | ✗ | The candidate postal address is the address Checkr will use to send postal mail to the candidate. Each candidate can be associated with only one postal address. | `{"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}` |
| `previous_driver_license_number` | ✗ | Candidate’s previous driver license number. | `"F1501739"` |
| `previous_driver_license_state` | ✗ | State that issued the candidate’s previous driver license. Format: `ISO 3166-2:US`.  | `"MD"` |
| `report_ids` | ✗ | Array of Report IDs. | `["532e71cfe88a1d4e8d00000d"]` |
| `ssn` | ✗ | Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits. | `"XXX-XX-4645"` |
| `work_locations` | ✗ | <font color="red">Required</font> for non-US candidates.  Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.  | `[{"city": "San Francisco", "country": "US", "state": "CA"}]` |
| `zipcode` | ✗ | Candidate’s 5-digit zip code. | `"90401"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.create(
    email="john.smith@gmail.com",
    custom_id="HRIS-27",
    dob="1970-01-22",
    driver_license_number="F2111655",
    driver_license_state="CA",
    first_name="John",
    last_name="Smith",
    middle_name="Alfred",
    mother_maiden_name="Jones",
    phone="5555555555",
    postal_address={
        "city": "San Francisco",
        "name": "John Alfred Smith",
        "state": "CA",
        "street": "123 Main Street",
        "street2": "APT A",
        "zipcode": "94108",
    },
    previous_driver_license_number="F1501739",
    previous_driver_license_state="MD",
    ssn="XXX-XX-4645",
    zipcode="90401",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.create(
    email="john.smith@gmail.com",
    custom_id="HRIS-27",
    dob="1970-01-22",
    driver_license_number="F2111655",
    driver_license_state="CA",
    first_name="John",
    last_name="Smith",
    middle_name="Alfred",
    mother_maiden_name="Jones",
    phone="5555555555",
    postal_address={
        "city": "San Francisco",
        "name": "John Alfred Smith",
        "state": "CA",
        "street": "123 Main Street",
        "street2": "APT A",
        "zipcode": "94108",
    },
    previous_driver_license_number="F1501739",
    previous_driver_license_state="MD",
    ssn="XXX-XX-4645",
    zipcode="90401",
)

```

#### Response

##### Type
[Candidate](/checkr_api_py/types/models/candidate.py)

##### Example
`{"dob": "1970-01-22", "driver_license_number": "F2111655", "driver_license_state": "CA", "email": "john.smith@gmail.com", "first_name": "John", "id": "e44aa283528e6fde7d542194", "last_name": "Smith", "middle_name": "Alfred", "mother_maiden_name": "Jones", "phone": "5555555555", "postal_address": {"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}, "previous_driver_license_number": "F1501739", "previous_driver_license_state": "MD", "ssn": "XXX-XX-4645", "uri": "/v1/candidates/e44aa283528e6fde7d542194", "zipcode": "90401"}`

### Update an existing Candidate <a name="update"></a>

Updates an existing Candidate.

Attempts to update a field that cannot be updated will return a 400 error stating "... cannot be updated”. For example, attempting to update an SSN will return 400 stating "Candidate SSN can not be updated because it has reports”. 

Updating `geo_ids` will **replace** all existing Geos. To keep existing geos, include their IDs in the update request. `geo_ids` cannot be updated if the candidate's work location is outside the US.
Only fields with `null` values can be updated after a Report has been ordered for a Candidate with the exception of the following fields:
- email
- phone
- previous_driver_license_number
- previous_driver_license_state
- copy_requested
- custom_id
- geo_ids

Updating metadata with an empty value (null or empty object) will delete existing metadata. Individual keys may also be set and unset.
- Adding a new key-value pair will maintain all existing key-value pairs.
- Providing a new value for an existing key will update the old value to the new value.
- Providing an empty value for an existing key will remove that key from the metadata object.
- When all keys in the metadata object have empty values, the object will be deleted.


**API Endpoint**: `POST /candidates/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id_path` | ✓ | The Candidate's ID. | `"string"` |
| `adjudication` | ✗ | The adjudication for the Candidate’s most recently created Report. | `"engaged"` |
| `copy_requested` | ✗ | If `true`, the candidate has asked to receive a copy of their report. | `True` |
| `custom_id` | ✗ | Client-assigned unique ID for the Candidate. Can be used to map Checkr Candidate IDs to your internal tracking system, and to search for Candidates through both the Dashboard and the API. | `"string"` |
| `dob` | ✗ | Candidate’s date of birth. | `"1970-01-22"` |
| `driver_license_number` | ✗ | Candidate’s driver license number. | `"F2111655"` |
| `driver_license_state` | ✗ | Candidate’s driver license state of issue. Format: `ISO 3166-2:US`.  | `"CA"` |
| `email` | ✗ | Candidate’s email address.  | `"john.smith@gmail.com"` |
| `first_name` | ✗ | Candidate’s first name.  | `"John"` |
| `geo_ids` | ✗ | Array of Geo IDs. | `["79f943e212cce7de21c054a8"]` |
| `id` | ✗ |  | `"e44aa283528e6fde7d542194"` |
| `last_name` | ✗ | Candidate’s last name. | `"Smith"` |
| `metadata` | ✗ |  | `{}` |
| `middle_name` | ✗ | Candidate’s middle name. This field is required if `no_middle_name` is `false`.  | `"Alfred"` |
| `mother_maiden_name` | ✗ | Candidate’s mother’s maiden name.  | `"Jones"` |
| `no_middle_name` | ✗ | Required if no `middle_name` is provided. `true` if the candidate has no middle name.  | `True` |
| `object` | ✗ |  | `"candidate"` |
| `phone` | ✗ | Candidate’s phone number. | `"5555555555"` |
| `postal_address` | ✗ | Candidate's postal address. | `{"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}` |
| `previous_driver_license_number` | ✗ | Candidate’s previous driver license number. | `"F1501739"` |
| `previous_driver_license_state` | ✗ | State that issued the candidate’s previous driver license. Format: `ISO 3166-2:US`.  | `"MD"` |
| `report_ids` | ✗ | Array of Report IDs. | `["532e71cfe88a1d4e8d00000d"]` |
| `ssn` | ✗ | Candidate’s Social Security Number. This value will be redacted in all return calls, except for the last four digits. | `"XXX-XX-4645"` |
| `uri` | ✗ |  | `"/v1/candidates/e44aa283528e6fde7d542194"` |
| `zipcode` | ✗ | Candidate’s 5-digit zip code. | `"90401"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.update(
    id_path="string",
    dob="1970-01-22",
    driver_license_number="F2111655",
    driver_license_state="CA",
    email="john.smith@gmail.com",
    first_name="John",
    last_name="Smith",
    middle_name="Alfred",
    mother_maiden_name="Jones",
    phone="5555555555",
    postal_address={
        "city": "San Francisco",
        "name": "John Alfred Smith",
        "state": "CA",
        "street": "123 Main Street",
        "street2": "APT A",
        "zipcode": "94108",
    },
    previous_driver_license_number="F1501739",
    previous_driver_license_state="MD",
    ssn="XXX-XX-4645",
    uri="/v1/candidates/e44aa283528e6fde7d542194",
    zipcode="90401",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.update(
    id_path="string",
    dob="1970-01-22",
    driver_license_number="F2111655",
    driver_license_state="CA",
    email="john.smith@gmail.com",
    first_name="John",
    last_name="Smith",
    middle_name="Alfred",
    mother_maiden_name="Jones",
    phone="5555555555",
    postal_address={
        "city": "San Francisco",
        "name": "John Alfred Smith",
        "state": "CA",
        "street": "123 Main Street",
        "street2": "APT A",
        "zipcode": "94108",
    },
    previous_driver_license_number="F1501739",
    previous_driver_license_state="MD",
    ssn="XXX-XX-4645",
    uri="/v1/candidates/e44aa283528e6fde7d542194",
    zipcode="90401",
)

```

#### Response

##### Type
[Candidate](/checkr_api_py/types/models/candidate.py)

##### Example
`{"dob": "1970-01-22", "driver_license_number": "F2111655", "driver_license_state": "CA", "email": "john.smith@gmail.com", "first_name": "John", "id": "e44aa283528e6fde7d542194", "last_name": "Smith", "middle_name": "Alfred", "mother_maiden_name": "Jones", "phone": "5555555555", "postal_address": {"city": "San Francisco", "name": "John Alfred Smith", "state": "CA", "street": "123 Main Street", "street2": "APT A", "zipcode": "94108"}, "previous_driver_license_number": "F1501739", "previous_driver_license_state": "MD", "ssn": "XXX-XX-4645", "uri": "/v1/candidates/e44aa283528e6fde7d542194", "zipcode": "90401"}`


### List existing Form I-9s <a name="list"></a>

Retrieves all I-9s for the authenticated Checkr account.


**API Endpoint**: `GET /i9/forms_i9`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `order` | ✗ | Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.  | `"asc"` |
| `order_by` | ✗ | Returns records listed by `order_by` parameter.   If neither is specified, records will be ordered by start_date.  | `"full_name"` |
| `page` | ✗ | Specifies the page number to retrieve. | `123` |
| `per_page` | ✗ | Indicates how many records each page should contain. | `123` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.forms_i9.list(order="asc", order_by="full_name")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.forms_i9.list(order="asc", order_by="full_name")

```

#### Response

##### Type
[I9FormsI9ListResponse](/checkr_api_py/types/models/i9_forms_i9_list_response.py)

##### Example
`{"count": 1}`

### Retrieve a Form I-9 <a name="get"></a>

Retrieves an existing Form I-9.


**API Endpoint**: `GET /i9/forms_i9/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Form I9 | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.forms_i9.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.forms_i9.get(id="string")

```

#### Response

##### Type
[FormI9](/checkr_api_py/types/models/form_i9.py)

##### Example
`{"authorized_representative_email": "lee.perry@domain.com", "authorized_representative_first_name": "Lee", "authorized_representative_last_name": "Perry", "candidate_id": "3de7e278beb24d14a3785e2dd02cca49", "created_at": "2023-04-29T16:21:11Z", "form_i9_url": "https://integration.i9complete.com/Content/tracker/YWg1ZDg5SDM5RVMzbWxh", "id": "1a16ef5f9c1f1df045e74bb4", "open_tasks": "complete_section_2", "open_tasks_url": "", "order_progress": "section_1_incomplete", "start_date": "2023-04-29", "uri": "v1/forms_i9/1a16ef5f9c1f1df045e74bb4", "workflow_type": "remote_section_1_only", "worksite_id": "8046067e32ad6b25a9078735", "worksite_uri": "v1/i9/worksites/8046067e32ad6b25a9078735"}`

### Create a new Form I-9 <a name="create"></a>

Creates a new Form I-9 resource. This resource allow the creation of a single
Form I-9 and also the creation of a bulk of Forms I-9 in one request.


**API Endpoint**: `POST /i9/forms_i9`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | Candidate resource Id.  | `"3de7e278beb24d14a3785e2dd02cca49"` |
| `email` | ✓ | Candidate email address. | `"john.doe@example.com"` |
| `start_date` | ✓ | Candidate start date. | `"2023-04-29"` |
| `workflow_type` | ✓ | Workflow type.  For additional insights into workflow types, please consider reviewing the [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).  | `"remote_section_1_only"` |
| `worksite_id` | ✓ | Worksite resource Id. | `"8046067e32ad6b25a9078735"` |
| `authorized_representative_email` | ✗ | Email address of authorized representative. | `"lee.perry@domain.com"` |
| `authorized_representative_first_name` | ✗ | First name of authorized representative. | `"Lee"` |
| `authorized_representative_last_name` | ✗ | Last name of authorized representative. | `"Perry"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.forms_i9.create(
    candidate_id="3de7e278beb24d14a3785e2dd02cca49",
    email="john.doe@example.com",
    start_date="2023-04-29",
    workflow_type="remote_section_1_only",
    worksite_id="8046067e32ad6b25a9078735",
    authorized_representative_email="lee.perry@domain.com",
    authorized_representative_first_name="Lee",
    authorized_representative_last_name="Perry",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.forms_i9.create(
    candidate_id="3de7e278beb24d14a3785e2dd02cca49",
    email="john.doe@example.com",
    start_date="2023-04-29",
    workflow_type="remote_section_1_only",
    worksite_id="8046067e32ad6b25a9078735",
    authorized_representative_email="lee.perry@domain.com",
    authorized_representative_first_name="Lee",
    authorized_representative_last_name="Perry",
)

```

#### Response

##### Type
[FormI9](/checkr_api_py/types/models/form_i9.py)

##### Example
`{"authorized_representative_email": "lee.perry@domain.com", "authorized_representative_first_name": "Lee", "authorized_representative_last_name": "Perry", "candidate_id": "3de7e278beb24d14a3785e2dd02cca49", "created_at": "2023-04-29T16:21:11Z", "form_i9_url": "https://integration.i9complete.com/Content/tracker/YWg1ZDg5SDM5RVMzbWxh", "id": "1a16ef5f9c1f1df045e74bb4", "open_tasks": "complete_section_2", "open_tasks_url": "", "order_progress": "section_1_incomplete", "start_date": "2023-04-29", "uri": "v1/forms_i9/1a16ef5f9c1f1df045e74bb4", "workflow_type": "remote_section_1_only", "worksite_id": "8046067e32ad6b25a9078735", "worksite_uri": "v1/i9/worksites/8046067e32ad6b25a9078735"}`

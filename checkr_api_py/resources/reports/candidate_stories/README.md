
### Create a new Candidate Story <a name="create"></a>

Create a new Candidate Story for the input `report_id`.


**API Endpoint**: `POST /reports/{report_id}/candidate_stories`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `content` | ✓ | Additional information provided by Candidate. | `"Since my case, I have received the following certifications (see attachments)"` |
| `documents` | ✓ | An array of documents to attach to the Candidate Story. Can be empty. | `[{"filename": "evidence_of_rehab.pdf", "tempfile": "https://tempfilebucket.aws.example.com/abYwtudnakfnafl", "type_": "application/pdf"}]` |
| `report_id` | ✓ | Create an candidate story for the input `report_id`. | `"string"` |
| `record_id` | ✗ | ID of the Record existing on a Screening to which the Candidate Story is linked. When no record ID is provided, the Candidate Story is considered General Information.  | `"af3393b7d751206c7c67b6e5"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.reports.candidate_stories.create(
    content="Since my case, I have received the following certifications (see attachments)",
    documents=[
        {
            "filename": "evidence_of_rehab.pdf",
            "tempfile": "https://tempfilebucket.aws.example.com/abYwtudnakfnafl",
            "type_": "application/pdf",
        }
    ],
    report_id="string",
    record_id="af3393b7d751206c7c67b6e5",
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.reports.candidate_stories.create(
    content="Since my case, I have received the following certifications (see attachments)",
    documents=[
        {
            "filename": "evidence_of_rehab.pdf",
            "tempfile": "https://tempfilebucket.aws.example.com/abYwtudnakfnafl",
            "type_": "application/pdf",
        }
    ],
    report_id="string",
    record_id="af3393b7d751206c7c67b6e5",
)

```

#### Response

##### Type
[CandidateStory](/checkr_api_py/types/models/candidate_story.py)

##### Example
`{"content": "Since my case, I have received the following certifications (see attachments)", "created_at": "2020-04-17T07:48:34Z", "id": "e44aa283528e6fde7d542194", "report_id": "af3393b7d751206c7c67b6e5", "uri": "/v1/candidate_stories/e44aa283528e6fde7d542194"}`

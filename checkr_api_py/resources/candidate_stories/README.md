
### Delete a Candidate Story <a name="delete"></a>

Deletes the existing Candidate Story corresponding to the input ID.

**API Endpoint**: `DELETE /candidate_stories/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Candidate Story. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidate_stories.delete(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidate_stories.delete(id="string")

```

#### Response

##### Type
[CandidateStory](/checkr_api_py/types/models/candidate_story.py)

##### Example
`{"content": "Since my case, I have received the following certifications (see attachments)", "created_at": "2020-04-17T07:48:34Z", "id": "e44aa283528e6fde7d542194", "report_id": "af3393b7d751206c7c67b6e5", "uri": "/v1/candidate_stories/e44aa283528e6fde7d542194"}`

### Retrieve a Candidate Story <a name="get"></a>

Returns the existing Candidate Story corresponding to the input ID.

**API Endpoint**: `GET /candidate_stories/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Candidate Story. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidate_stories.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidate_stories.get(id="string")

```

#### Response

##### Type
[CandidateStory](/checkr_api_py/types/models/candidate_story.py)

##### Example
`{"content": "Since my case, I have received the following certifications (see attachments)", "created_at": "2020-04-17T07:48:34Z", "id": "e44aa283528e6fde7d542194", "report_id": "af3393b7d751206c7c67b6e5", "uri": "/v1/candidate_stories/e44aa283528e6fde7d542194"}`

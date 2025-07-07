
### List a Candidate's Documents <a name="list"></a>

Returns an array of candidate-provided Documents for the input `candidate_id`.


**API Endpoint**: `GET /candidates/{candidate_id}/documents`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | ID of the Candidate for whom documents will be retrieved. | `"string"` |
| `types[]` | ✗ | The type of candidate-provided document to return. If `types[]` is not included in the call, all available Candidate Documents will be returned. | `["alien_id"]` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.documents.list(candidate_id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.documents.list(candidate_id="string")

```

#### Response

##### Type
[CandidatesDocumentsListResponse](/checkr_api_py/types/models/candidates_documents_list_response.py)

##### Example
`{"count": 1}`

### Upload a new Candidate Document <a name="create"></a>

Uploads a new Candidate Document.

**API Endpoint**: `POST /candidates/{candidate_id}/documents`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `candidate_id` | ✓ | Upload a document for the input `candidate_id`. | `"string"` |
| `file` | ✓ | Path to the document on your local file system.  Valid MIME types: `image/gif`, `image/jpg`, `image/jpeg`, `image/png`, `image/bmp`, `image/tiff`, `application/pdf`, `image/heic`.  | `open("uploads/file.pdf", "rb")` |
| `type` | ✓ |  | `"alien_id"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.candidates.documents.create(
    candidate_id="string", file=open("uploads/file.pdf", "rb"), type_="alien_id"
)

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.candidates.documents.create(
    candidate_id="string", file=open("uploads/file.pdf", "rb"), type_="alien_id"
)

```

#### Response

##### Type
[Document](/checkr_api_py/types/models/document.py)

##### Example
`{"content_type": "image/jpeg", "created_at": "2015-02-11T20:01:50Z", "download_uri": "https://checkr-documents.checkr.com/download_path", "filename": "1423684910_candidate_driver_license.jpg", "filesize": 8576, "id": "e44aa283528e6fde7d542194", "type_": "driver_license"}`

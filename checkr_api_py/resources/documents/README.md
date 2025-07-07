
### Retrieve a Document <a name="get"></a>

Returns an existing Document with the input ID.

Report Document IDs can be retrieved from the [Retrieve an existing Report](#operation/getReport)
endpoint. Candidate Document IDs can be retrieved using the
[List a Candidate's Documents](#operation/getCandidateDocuments) endpoint.


**API Endpoint**: `GET /documents/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Document to retrieve. | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.documents.get(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.documents.get(id="string")

```

#### Response

##### Type
[Document](/checkr_api_py/types/models/document.py)

##### Example
`{"content_type": "image/jpeg", "created_at": "2015-02-11T20:01:50Z", "download_uri": "https://checkr-documents.checkr.com/download_path", "filename": "1423684910_candidate_driver_license.jpg", "filesize": 8576, "id": "e44aa283528e6fde7d542194", "type_": "driver_license"}`

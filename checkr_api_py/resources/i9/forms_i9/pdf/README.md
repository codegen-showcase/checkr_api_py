
### Retrieve Form I-9 PDF file <a name="list"></a>

Retrieves a Form I-9 PDF file associated with the Form I-9 ID. 

This endpoint returns a pre-signed S3 URL, valid for 5 minutes.


**API Endpoint**: `GET /i9/forms_i9/{id}/pdf`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | ID of the Form I9 | `"string"` |

#### Synchronous Client

```python
from checkr_api_py import Client
from os import getenv

client = Client(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = client.i9.forms_i9.pdf.list(id="string")

```

#### Asynchronous Client

```python
from checkr_api_py import AsyncClient
from os import getenv

client = AsyncClient(username=getenv("API_USERNAME"), password=getenv("API_PASSWORD"))
res = await client.i9.forms_i9.pdf.list(id="string")

```

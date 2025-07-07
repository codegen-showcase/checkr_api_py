from checkr_api_py.core import AsyncBaseClient, SyncBaseClient
from checkr_api_py.resources.i9.forms_i9 import AsyncFormsI9Client, FormsI9Client
from checkr_api_py.resources.i9.worksites import AsyncWorksitesClient, WorksitesClient


class I9Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.worksites = WorksitesClient(base_client=self._base_client)
        self.forms_i9 = FormsI9Client(base_client=self._base_client)


class AsyncI9Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.worksites = AsyncWorksitesClient(base_client=self._base_client)
        self.forms_i9 = AsyncFormsI9Client(base_client=self._base_client)

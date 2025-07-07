import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class CandidateStoriesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        content: str,
        documents: typing.List[params.ReportsCandidateStoriesCreateBodyDocumentsItem],
        report_id: str,
        record_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidateStory:
        """
        Create a new Candidate Story

        Create a new Candidate Story for the input `report_id`.


        POST /reports/{report_id}/candidate_stories

        Args:
            record_id: ID of the Record existing on a Screening to which the Candidate Story is linked.
        When no record ID is provided, the Candidate Story is considered General Information.

            content: Additional information provided by Candidate.
            documents: An array of documents to attach to the Candidate Story. Can be empty.
            report_id: Create an candidate story for the input `report_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.candidate_stories.create(
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
        """
        _json = to_encodable(
            item={"record_id": record_id, "content": content, "documents": documents},
            dump_with=params._SerializerReportsCandidateStoriesCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/reports/{report_id}/candidate_stories",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )


class AsyncCandidateStoriesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        content: str,
        documents: typing.List[params.ReportsCandidateStoriesCreateBodyDocumentsItem],
        report_id: str,
        record_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidateStory:
        """
        Create a new Candidate Story

        Create a new Candidate Story for the input `report_id`.


        POST /reports/{report_id}/candidate_stories

        Args:
            record_id: ID of the Record existing on a Screening to which the Candidate Story is linked.
        When no record ID is provided, the Candidate Story is considered General Information.

            content: Additional information provided by Candidate.
            documents: An array of documents to attach to the Candidate Story. Can be empty.
            report_id: Create an candidate story for the input `report_id`.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.candidate_stories.create(
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
        """
        _json = to_encodable(
            item={"record_id": record_id, "content": content, "documents": documents},
            dump_with=params._SerializerReportsCandidateStoriesCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/reports/{report_id}/candidate_stories",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )

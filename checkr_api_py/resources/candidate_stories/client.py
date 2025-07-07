import typing

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
)
from checkr_api_py.types import models


class CandidateStoriesClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.CandidateStory:
        """
        Delete a Candidate Story

        Deletes the existing Candidate Story corresponding to the input ID.

        DELETE /candidate_stories/{id}

        Args:
            id: ID of the Candidate Story.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidate_stories.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/candidate_stories/{id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.CandidateStory:
        """
        Retrieve a Candidate Story

        Returns the existing Candidate Story corresponding to the input ID.

        GET /candidate_stories/{id}

        Args:
            id: ID of the Candidate Story.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidate_stories.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidate_stories/{id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )


class AsyncCandidateStoriesClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.CandidateStory:
        """
        Delete a Candidate Story

        Deletes the existing Candidate Story corresponding to the input ID.

        DELETE /candidate_stories/{id}

        Args:
            id: ID of the Candidate Story.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidate_stories.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/candidate_stories/{id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.CandidateStory:
        """
        Retrieve a Candidate Story

        Returns the existing Candidate Story corresponding to the input ID.

        GET /candidate_stories/{id}

        Args:
            id: ID of the Candidate Story.
            request_options: Additional options to customize the HTTP request

        Returns:
            Candidate Story details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidate_stories.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidate_stories/{id}",
            auth_names=["basic_auth"],
            cast_to=models.CandidateStory,
            request_options=request_options or default_request_options(),
        )

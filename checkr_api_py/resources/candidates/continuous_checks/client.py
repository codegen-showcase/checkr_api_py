import typing
import typing_extensions

from checkr_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class ContinuousChecksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesContinuousChecksListResponse:
        """
        List existing Continuous Checks

        Returns a list of existing Continuous Checks.


        GET /candidates/{candidate_id}/continuous_checks

        Args:
            candidate_id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Continuous Checks

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.continuous_checks.list(candidate_id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/continuous_checks",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesContinuousChecksListResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        type_: typing_extensions.Literal["criminal", "mvr"],
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContinuousCheck:
        """
        Create a new Continuous Check

        Creates a new Continuous Check resource.


        POST /candidates/{candidate_id}/continuous_checks

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts with Nodes.

        `custom_id` of the associated node.

            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: The Candidate's ID.
            type: Defines the screening type(s) for this Continuous Check.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.continuous_checks.create(
            candidate_id="string", type_="criminal"
        )
        ```
        """
        _json = to_encodable(
            item={"node": node, "work_locations": work_locations, "type_": type_},
            dump_with=params._SerializerCandidatesContinuousChecksCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/continuous_checks",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )


class AsyncContinuousChecksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        candidate_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesContinuousChecksListResponse:
        """
        List existing Continuous Checks

        Returns a list of existing Continuous Checks.


        GET /candidates/{candidate_id}/continuous_checks

        Args:
            candidate_id: The Candidate's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Continuous Checks

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.continuous_checks.list(candidate_id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/continuous_checks",
            auth_names=["basic_auth"],
            cast_to=models.CandidatesContinuousChecksListResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        type_: typing_extensions.Literal["criminal", "mvr"],
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ContinuousCheck:
        """
        Create a new Continuous Check

        Creates a new Continuous Check resource.


        POST /candidates/{candidate_id}/continuous_checks

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts with Nodes.

        `custom_id` of the associated node.

            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: The Candidate's ID.
            type: Defines the screening type(s) for this Continuous Check.
            request_options: Additional options to customize the HTTP request

        Returns:
            Continuous Check was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.continuous_checks.create(
            candidate_id="string", type_="criminal"
        )
        ```
        """
        _json = to_encodable(
            item={"node": node, "work_locations": work_locations, "type_": type_},
            dump_with=params._SerializerCandidatesContinuousChecksCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/continuous_checks",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.ContinuousCheck,
            request_options=request_options or default_request_options(),
        )

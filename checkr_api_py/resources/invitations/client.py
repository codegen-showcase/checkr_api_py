import typing
import typing_extensions

from checkr_api_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class InvitationsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Invitation:
        """
        Cancel an existing Invitation

        Cancels an existing Invitation.


        DELETE /invitations/{id}

        Args:
            id: The Invitation's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invitations.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/invitations/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )

    def list(
        self,
        *,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["completed", "expired", "pending"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvitationsListResponse:
        """
        List existing Invitations

        Returns a list of existing Invitations with the input `status` or `candidate_id`.

        * If no parameters are passed, returns all Invitations.

        * If `candidate_id` or `status` is passed, returns Invitations that match the input parameter.

        * If both `candidate_id` and `status` are passed, return Invitations that match both parameters.

        Returns 400 if the (optional) `status` parameter is not `pending`, `expired`, or `completed`.
        <b>Note: </b>This call will not return invitations with non-US `work_locations`. Use [GET /invitations/{id}](#operation/getInvitation) to retrieve candidates outside the US.


        GET /invitations

        Args:
            candidate_id: ID of the candidate to whom the invitation was issued.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            status: Status of the Invitation.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Invitations

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invitations.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(candidate_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "candidate_id",
                to_encodable(item=candidate_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "completed", "expired", "pending"
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/invitations",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.InvitationsListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        id: str,
        include_deleted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invitation:
        """
        Retrieve an existing Invitation

        Returns an existing Invitation with the input ID.


        GET /invitations/{id}

        Args:
            include_deleted: Retrieve an invitation that has been deleted
            id: The Invitation's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invitations.get(id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_deleted, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include_deleted",
                to_encodable(item=include_deleted, dump_with=bool),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/invitations/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        package: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invitation:
        """
        Create a new Invitation

        Creates a new Invitation resource.


        POST /invitations

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            tags: Array of tags for the Report.
            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the Candidate for whom the Invitation is created.
            package: `slug` of the associated package.

            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.invitations.create(
            candidate_id="551564b7865af96a28b13f36", package="driver_pro"
        )
        ```
        """
        _json = to_encodable(
            item={
                "node": node,
                "tags": tags,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
            },
            dump_with=params._SerializerInvitationsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/invitations",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )


class AsyncInvitationsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Invitation:
        """
        Cancel an existing Invitation

        Cancels an existing Invitation.


        DELETE /invitations/{id}

        Args:
            id: The Invitation's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation was successfully canceled

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invitations.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/invitations/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self,
        *,
        candidate_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[
                typing_extensions.Literal["completed", "expired", "pending"]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.InvitationsListResponse:
        """
        List existing Invitations

        Returns a list of existing Invitations with the input `status` or `candidate_id`.

        * If no parameters are passed, returns all Invitations.

        * If `candidate_id` or `status` is passed, returns Invitations that match the input parameter.

        * If both `candidate_id` and `status` are passed, return Invitations that match both parameters.

        Returns 400 if the (optional) `status` parameter is not `pending`, `expired`, or `completed`.
        <b>Note: </b>This call will not return invitations with non-US `work_locations`. Use [GET /invitations/{id}](#operation/getInvitation) to retrieve candidates outside the US.


        GET /invitations

        Args:
            candidate_id: ID of the candidate to whom the invitation was issued.
            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain. The default value is 25 records.
            status: Status of the Invitation.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Invitations

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invitations.list()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(candidate_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "candidate_id",
                to_encodable(item=candidate_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=typing.Optional[float]),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(
                    item=status,
                    dump_with=typing_extensions.Literal[
                        "completed", "expired", "pending"
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/invitations",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.InvitationsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        id: str,
        include_deleted: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invitation:
        """
        Retrieve an existing Invitation

        Returns an existing Invitation with the input ID.


        GET /invitations/{id}

        Args:
            include_deleted: Retrieve an invitation that has been deleted
            id: The Invitation's ID.
            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invitations.get(id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(include_deleted, type_utils.NotGiven):
            encode_query_param(
                _query,
                "include_deleted",
                to_encodable(item=include_deleted, dump_with=bool),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/invitations/{id}",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        package: str,
        node: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tags: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        work_locations: typing.Union[
            typing.Optional[typing.List[params.WorkLocation]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Invitation:
        """
        Create a new Invitation

        Creates a new Invitation resource.


        POST /invitations

        Args:
            node: <font color="red">Required</font> for hierarchy-enabled accounts.

        `custom_id` of the associated node.

            tags: Array of tags for the Report.
            work_locations: <font color="red">Required</font> for hierarchy-enabled accounts.

        Array of locations described using country, state, and city. When country is not specified defaults to US. State is required for US candidates. Country is required for non-US candidates.

            candidate_id: ID of the Candidate for whom the Invitation is created.
            package: `slug` of the associated package.

            request_options: Additional options to customize the HTTP request

        Returns:
            Invitation was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.invitations.create(
            candidate_id="551564b7865af96a28b13f36", package="driver_pro"
        )
        ```
        """
        _json = to_encodable(
            item={
                "node": node,
                "tags": tags,
                "work_locations": work_locations,
                "candidate_id": candidate_id,
                "package": package,
            },
            dump_with=params._SerializerInvitationsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/invitations",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Invitation,
            request_options=request_options or default_request_options(),
        )

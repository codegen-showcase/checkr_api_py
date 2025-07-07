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
from checkr_api_py.resources.i9.forms_i9.pdf import AsyncPdfClient, PdfClient
from checkr_api_py.types import models, params


class FormsI9Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.pdf = PdfClient(base_client=self._base_client)

    def list(
        self,
        *,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "full_name", "open_task", "start_date", "worksite_name"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9FormsI9ListResponse:
        """
        List existing Form I-9s

        Retrieves all I-9s for the authenticated Checkr account.


        GET /i9/forms_i9

        Args:
            order: Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.

            order_by: Returns records listed by `order_by` parameter.

        If neither is specified, records will be ordered by start_date.

            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Forms I-9

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.forms_i9.list(order="asc", order_by="full_name")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal[
                        "full_name", "open_task", "start_date", "worksite_name"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/i9/forms_i9",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.I9FormsI9ListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.FormI9:
        """
        Retrieve a Form I-9

        Retrieves an existing Form I-9.


        GET /i9/forms_i9/{id}

        Args:
            id: ID of the Form I9
            request_options: Additional options to customize the HTTP request

        Returns:
            Form I-9 details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.forms_i9.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/i9/forms_i9/{id}",
            auth_names=["basic_auth"],
            cast_to=models.FormI9,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        email: str,
        start_date: str,
        workflow_type: typing_extensions.Literal[
            "employee_appointment", "employer_appointment", "remote_section_1_only"
        ],
        worksite_id: str,
        authorized_representative_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        authorized_representative_first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        authorized_representative_last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FormI9:
        """
        Create a new Form I-9

        Creates a new Form I-9 resource. This resource allow the creation of a single
        Form I-9 and also the creation of a bulk of Forms I-9 in one request.


        POST /i9/forms_i9

        Args:
            authorized_representative_email: Email address of authorized representative.
            authorized_representative_first_name: First name of authorized representative.
            authorized_representative_last_name: Last name of authorized representative.
            candidate_id: Candidate resource Id.

            email: Candidate email address.
            start_date: Candidate start date.
            workflow_type: Workflow type.

        For additional insights into workflow types, please consider reviewing the [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).

            worksite_id: Worksite resource Id.
            request_options: Additional options to customize the HTTP request

        Returns:
            Resource created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.i9.forms_i9.create(
            candidate_id="3de7e278beb24d14a3785e2dd02cca49",
            email="john.doe@example.com",
            start_date="2023-04-29",
            workflow_type="remote_section_1_only",
            worksite_id="8046067e32ad6b25a9078735",
            authorized_representative_email="lee.perry@domain.com",
            authorized_representative_first_name="Lee",
            authorized_representative_last_name="Perry",
        )
        ```
        """
        _json = to_encodable(
            item={
                "authorized_representative_email": authorized_representative_email,
                "authorized_representative_first_name": authorized_representative_first_name,
                "authorized_representative_last_name": authorized_representative_last_name,
                "candidate_id": candidate_id,
                "email": email,
                "start_date": start_date,
                "workflow_type": workflow_type,
                "worksite_id": worksite_id,
            },
            dump_with=params._SerializerI9FormsI9CreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/i9/forms_i9",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.FormI9,
            request_options=request_options or default_request_options(),
        )


class AsyncFormsI9Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.pdf = AsyncPdfClient(base_client=self._base_client)

    async def list(
        self,
        *,
        order: typing.Union[
            typing.Optional[typing_extensions.Literal["asc", "desc"]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        order_by: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "full_name", "open_task", "start_date", "worksite_name"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        per_page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.I9FormsI9ListResponse:
        """
        List existing Form I-9s

        Retrieves all I-9s for the authenticated Checkr account.


        GET /i9/forms_i9

        Args:
            order: Returns records listed in ascending or descending order of the order_by parameter. If neither is specified, records will be listed in descending order.

            order_by: Returns records listed by `order_by` parameter.

        If neither is specified, records will be ordered by start_date.

            page: Specifies the page number to retrieve.
            per_page: Indicates how many records each page should contain.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Forms I-9

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.forms_i9.list(order="asc", order_by="full_name")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(order, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order",
                to_encodable(
                    item=order, dump_with=typing_extensions.Literal["asc", "desc"]
                ),
                style="form",
                explode=True,
            )
        if not isinstance(order_by, type_utils.NotGiven):
            encode_query_param(
                _query,
                "order_by",
                to_encodable(
                    item=order_by,
                    dump_with=typing_extensions.Literal[
                        "full_name", "open_task", "start_date", "worksite_name"
                    ],
                ),
                style="form",
                explode=True,
            )
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(per_page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "per_page",
                to_encodable(item=per_page, dump_with=int),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/i9/forms_i9",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.I9FormsI9ListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.FormI9:
        """
        Retrieve a Form I-9

        Retrieves an existing Form I-9.


        GET /i9/forms_i9/{id}

        Args:
            id: ID of the Form I9
            request_options: Additional options to customize the HTTP request

        Returns:
            Form I-9 details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.forms_i9.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/i9/forms_i9/{id}",
            auth_names=["basic_auth"],
            cast_to=models.FormI9,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        email: str,
        start_date: str,
        workflow_type: typing_extensions.Literal[
            "employee_appointment", "employer_appointment", "remote_section_1_only"
        ],
        worksite_id: str,
        authorized_representative_email: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        authorized_representative_first_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        authorized_representative_last_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.FormI9:
        """
        Create a new Form I-9

        Creates a new Form I-9 resource. This resource allow the creation of a single
        Form I-9 and also the creation of a bulk of Forms I-9 in one request.


        POST /i9/forms_i9

        Args:
            authorized_representative_email: Email address of authorized representative.
            authorized_representative_first_name: First name of authorized representative.
            authorized_representative_last_name: Last name of authorized representative.
            candidate_id: Candidate resource Id.

            email: Candidate email address.
            start_date: Candidate start date.
            workflow_type: Workflow type.

        For additional insights into workflow types, please consider reviewing the [Form I-9 definitions](#section/Reference/Form-I-9-definitions-lessBETAgreater).

            worksite_id: Worksite resource Id.
            request_options: Additional options to customize the HTTP request

        Returns:
            Resource created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.i9.forms_i9.create(
            candidate_id="3de7e278beb24d14a3785e2dd02cca49",
            email="john.doe@example.com",
            start_date="2023-04-29",
            workflow_type="remote_section_1_only",
            worksite_id="8046067e32ad6b25a9078735",
            authorized_representative_email="lee.perry@domain.com",
            authorized_representative_first_name="Lee",
            authorized_representative_last_name="Perry",
        )
        ```
        """
        _json = to_encodable(
            item={
                "authorized_representative_email": authorized_representative_email,
                "authorized_representative_first_name": authorized_representative_first_name,
                "authorized_representative_last_name": authorized_representative_last_name,
                "candidate_id": candidate_id,
                "email": email,
                "start_date": start_date,
                "workflow_type": workflow_type,
                "worksite_id": worksite_id,
            },
            dump_with=params._SerializerI9FormsI9CreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/i9/forms_i9",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.FormI9,
            request_options=request_options or default_request_options(),
        )

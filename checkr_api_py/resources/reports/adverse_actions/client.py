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


class AdverseActionsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        adverse_item_ids: typing.List[str],
        report_id: str,
        medium: typing.Union[
            typing.Optional[params.ReportsAdverseActionsCreateBodyMedium],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        post_notice_scheduled_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AdverseAction:
        """
        Create a new Adverse Action

        Creates a new Adverse Action.

        <b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.


        POST /reports/{report_id}/adverse_actions

        Args:
            medium: The medium through which the Adverse Action notification should be sent.

            post_notice_scheduled_at: Time at which the Post-Adverse Action notification will be sent. Default is 7 days after creation.
            adverse_item_ids: IDs of Adverse Items selected for the Adverse Action.
            report_id: The ID of the Report for which the Adverse Action will be created.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.adverse_actions.create(
            adverse_item_ids=["string"],
            report_id="string",
            post_notice_scheduled_at="2016-10-07T12:34:00Z",
        )
        ```
        """
        _json = to_encodable(
            item={
                "medium": medium,
                "post_notice_scheduled_at": post_notice_scheduled_at,
                "adverse_item_ids": adverse_item_ids,
            },
            dump_with=params._SerializerReportsAdverseActionsCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path=f"/reports/{report_id}/adverse_actions",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )


class AsyncAdverseActionsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        adverse_item_ids: typing.List[str],
        report_id: str,
        medium: typing.Union[
            typing.Optional[params.ReportsAdverseActionsCreateBodyMedium],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        post_notice_scheduled_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AdverseAction:
        """
        Create a new Adverse Action

        Creates a new Adverse Action.

        <b>Note: </b>Report must be in a `consider` status and cannot have any existing Adverse Actions that have not been canceled.


        POST /reports/{report_id}/adverse_actions

        Args:
            medium: The medium through which the Adverse Action notification should be sent.

            post_notice_scheduled_at: Time at which the Post-Adverse Action notification will be sent. Default is 7 days after creation.
            adverse_item_ids: IDs of Adverse Items selected for the Adverse Action.
            report_id: The ID of the Report for which the Adverse Action will be created.
            request_options: Additional options to customize the HTTP request

        Returns:
            Adverse Action was successfully created

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.adverse_actions.create(
            adverse_item_ids=["string"],
            report_id="string",
            post_notice_scheduled_at="2016-10-07T12:34:00Z",
        )
        ```
        """
        _json = to_encodable(
            item={
                "medium": medium,
                "post_notice_scheduled_at": post_notice_scheduled_at,
                "adverse_item_ids": adverse_item_ids,
            },
            dump_with=params._SerializerReportsAdverseActionsCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path=f"/reports/{report_id}/adverse_actions",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.AdverseAction,
            request_options=request_options or default_request_options(),
        )

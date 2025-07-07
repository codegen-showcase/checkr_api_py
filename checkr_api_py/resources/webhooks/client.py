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


class WebhooksClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WebhookDelete:
        """
        Delete a Webhook

        Deletes the existing Webhook corresponding to the input ID.

        DELETE /webhooks/{id}

        Args:
            id: ID of the Webhook.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.delete(id="string")
        ```
        """
        return self._base_client.request(
            method="DELETE",
            path=f"/webhooks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.WebhookDelete,
            request_options=request_options or default_request_options(),
        )

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WebhooksListResponse:
        """
        List existing Webhooks

        Returns a list of existing Webhooks


        GET /webhooks

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Webhooks

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.list()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/webhooks",
            auth_names=["basic_auth"],
            cast_to=models.WebhooksListResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Webhook:
        """
        Retrieve a Webhook

        Returns the existing Webhook corresponding to the input ID.

        GET /webhooks/{id}

        Args:
            id: ID of the Webhook.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.get(id="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/webhooks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Webhook,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        webhook_url: str,
        include_object: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        live: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Webhook:
        """
        Create a new Webhook

        Creates a new Webhook resource. An account can have a maximum of 2 webhooks.

        Any webhook URL that fails to accept with a 2XX status code at least one request over a period of 60 days will be removed automatically - e.g. webhooks failing for 100% of the requests during 60 or more days.


        POST /webhooks

        Args:
            include_object: When `true`, the webhook event payload will include the related object.
            live: When 'true', the webhook is for the live environment.
            webhook_url: The URL which receives the webhook event payload. This must be an HTTPS or an AWS SNS URL. For more information, see [Supported Webhook URLs](#section/Webhooks/Supported-webhook-URLs) section.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.webhooks.create(webhook_url="https://example.com", live=True)
        ```
        """
        _json = to_encodable(
            item={
                "include_object": include_object,
                "live": live,
                "webhook_url": webhook_url,
            },
            dump_with=params._SerializerWebhooksCreateBody,
        )
        return self._base_client.request(
            method="POST",
            path="/webhooks",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Webhook,
            request_options=request_options or default_request_options(),
        )


class AsyncWebhooksClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WebhookDelete:
        """
        Delete a Webhook

        Deletes the existing Webhook corresponding to the input ID.

        DELETE /webhooks/{id}

        Args:
            id: ID of the Webhook.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.delete(id="string")
        ```
        """
        return await self._base_client.request(
            method="DELETE",
            path=f"/webhooks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.WebhookDelete,
            request_options=request_options or default_request_options(),
        )

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.WebhooksListResponse:
        """
        List existing Webhooks

        Returns a list of existing Webhooks


        GET /webhooks

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Webhooks

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.list()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/webhooks",
            auth_names=["basic_auth"],
            cast_to=models.WebhooksListResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Webhook:
        """
        Retrieve a Webhook

        Returns the existing Webhook corresponding to the input ID.

        GET /webhooks/{id}

        Args:
            id: ID of the Webhook.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.get(id="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/webhooks/{id}",
            auth_names=["basic_auth"],
            cast_to=models.Webhook,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        webhook_url: str,
        include_object: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        live: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Webhook:
        """
        Create a new Webhook

        Creates a new Webhook resource. An account can have a maximum of 2 webhooks.

        Any webhook URL that fails to accept with a 2XX status code at least one request over a period of 60 days will be removed automatically - e.g. webhooks failing for 100% of the requests during 60 or more days.


        POST /webhooks

        Args:
            include_object: When `true`, the webhook event payload will include the related object.
            live: When 'true', the webhook is for the live environment.
            webhook_url: The URL which receives the webhook event payload. This must be an HTTPS or an AWS SNS URL. For more information, see [Supported Webhook URLs](#section/Webhooks/Supported-webhook-URLs) section.
            request_options: Additional options to customize the HTTP request

        Returns:
            Webhook details

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.webhooks.create(webhook_url="https://example.com", live=True)
        ```
        """
        _json = to_encodable(
            item={
                "include_object": include_object,
                "live": live,
                "webhook_url": webhook_url,
            },
            dump_with=params._SerializerWebhooksCreateBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/webhooks",
            auth_names=["basic_auth"],
            json=_json,
            cast_to=models.Webhook,
            request_options=request_options or default_request_options(),
        )

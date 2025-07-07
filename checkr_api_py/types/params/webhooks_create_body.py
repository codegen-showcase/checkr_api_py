import pydantic
import typing
import typing_extensions


class WebhooksCreateBody(typing_extensions.TypedDict):
    """
    WebhooksCreateBody
    """

    include_object: typing_extensions.NotRequired[bool]
    """
    When `true`, the webhook event payload will include the related object.
    """

    live: typing_extensions.NotRequired[bool]
    """
    When 'true', the webhook is for the live environment.
    """

    webhook_url: typing_extensions.Required[str]
    """
    The URL which receives the webhook event payload. This must be an HTTPS or an AWS SNS URL. For more information, see [Supported Webhook URLs](#section/Webhooks/Supported-webhook-URLs) section.
    """


class _SerializerWebhooksCreateBody(pydantic.BaseModel):
    """
    Serializer for WebhooksCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    include_object: typing.Optional[bool] = pydantic.Field(
        alias="include_object", default=None
    )
    live: typing.Optional[bool] = pydantic.Field(alias="live", default=None)
    webhook_url: str = pydantic.Field(
        alias="webhook_url",
    )

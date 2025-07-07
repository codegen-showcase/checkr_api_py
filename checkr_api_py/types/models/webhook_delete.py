import pydantic
import typing
import typing_extensions


class WebhookDelete(pydantic.BaseModel):
    """
    WebhookDelete
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_id: typing.Optional[str] = pydantic.Field(alias="account_id", default=None)
    """
    The account associated with the webhook.
    """
    application_id: typing.Optional[str] = pydantic.Field(
        alias="application_id", default=None
    )
    """
    The application associated with the webhook.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the webhook was created.
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Time at which the webhook was deleted.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    include_object: typing.Optional[bool] = pydantic.Field(
        alias="include_object", default=None
    )
    """
    When `true`, the webhook event payload will include the related object.
    """
    object: typing.Optional[typing_extensions.Literal["webhook"]] = pydantic.Field(
        alias="object", default=None
    )
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """
    webhook_url: str = pydantic.Field(
        alias="webhook_url",
    )
    """
    The URL which receives the webhook event payload. This must be an HTTPS or an AWS SNS URL.
    """

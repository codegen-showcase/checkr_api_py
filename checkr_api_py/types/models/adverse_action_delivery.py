import pydantic
import typing
import typing_extensions


class AdverseActionDelivery(pydantic.BaseModel):
    """
    Details about the delivery state of the Adverse Action.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
    """
    Reason for the current state. Typically, this an error message, e.g. the raw response from an email provider.
    """
    state: typing.Optional[
        typing_extensions.Literal[
            "delivered", "error", "none", "queued", "sent", "unknown", "unopened"
        ]
    ] = pydantic.Field(alias="state", default=None)
    """
    Status of delivery for the Adverse Action.
    """
    updated_at: typing.Optional[str] = pydantic.Field(alias="updated_at", default=None)
    """
    Time at which the delivery state was updated.
    """

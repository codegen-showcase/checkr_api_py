import pydantic
import typing
import typing_extensions

from .adverse_action_delivery import AdverseActionDelivery
from .adverse_item import AdverseItem


class AdverseAction(pydantic.BaseModel):
    """
    AdverseAction
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    adverse_items: typing.Optional[typing.List[AdverseItem]] = pydantic.Field(
        alias="adverse_items", default=None
    )
    """
    Array of Adverse Items on which the Action is based.
    """
    canceled_at: typing.Optional[str] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Time at which the Adverse Action was canceled.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Adverse Action was created.
    """
    delivery: typing.Optional[AdverseActionDelivery] = pydantic.Field(
        alias="delivery", default=None
    )
    """
    Details about the delivery state of the Adverse Action.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    individualized_assessment_engaged: typing.Optional[bool] = pydantic.Field(
        alias="individualized_assessment_engaged", default=None
    )
    object: typing.Optional[typing_extensions.Literal["adverse_action"]] = (
        pydantic.Field(alias="object", default=None)
    )
    post_notice_ready_at: typing.Optional[str] = pydantic.Field(
        alias="post_notice_ready_at", default=None
    )
    """
    Timestamp after which the post notice can be sent. (Often 7 days after `created_at`.)
    
    """
    post_notice_scheduled_at: typing.Optional[str] = pydantic.Field(
        alias="post_notice_scheduled_at", default=None
    )
    """
    Timestamp at which the post Adverse Action notification will be sent. This time is
    dependent on the time at which the Pre-Adverse Action was created, and related settings
    within your Checkr system.
    
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="report_id", default=None)
    """
    ID of the Report causing this adverse action.
    """
    status: typing.Optional[
        typing_extensions.Literal["canceled", "complete", "dispute", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the Adverse Action.
    """
    uri: typing.Optional[str] = pydantic.Field(alias="uri", default=None)
    """
    URI of the resource.
    """

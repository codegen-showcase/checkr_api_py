import pydantic
import typing
import typing_extensions

from .employer import Employer
from .employment_verification_records_item_events_item import (
    EmploymentVerificationRecordsItemEventsItem,
)
from .employment_verification_records_item_result import (
    EmploymentVerificationRecordsItemResult,
)


class EmploymentVerificationRecordsItem(pydantic.BaseModel):
    """
    EmploymentVerificationRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[
        typing_extensions.Literal[
            "complete_now_customer_requested",
            "international_entry_not_supported",
            "no_history_required_information",
        ]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    """
    The reason the screening was canceled.
    """
    cancellation_reason_description: typing.Optional[
        typing_extensions.Literal[
            "Candidate declared no history",
            "Customer requested Complete Now prior to screening completion",
            "Screening does not support international entries",
        ]
    ] = pydantic.Field(alias="cancellation_reason_description", default=None)
    """
    Description of the `cancellation_reason` for the screening.
    """
    employer: typing.Optional[Employer] = pydantic.Field(alias="employer", default=None)
    events: typing.Optional[
        typing.List[EmploymentVerificationRecordsItemEventsItem]
    ] = pydantic.Field(alias="events", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    result: typing.Optional[EmploymentVerificationRecordsItemResult] = pydantic.Field(
        alias="result", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["clear", "consider", "pending"]
    ] = pydantic.Field(alias="status", default=None)

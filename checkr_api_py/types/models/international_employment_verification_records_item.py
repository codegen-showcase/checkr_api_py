import pydantic
import typing
import typing_extensions

from .international_employment_verification_records_item_employer import (
    InternationalEmploymentVerificationRecordsItemEmployer,
)
from .international_employment_verification_records_item_events_item import (
    InternationalEmploymentVerificationRecordsItemEventsItem,
)
from .international_employment_verification_records_item_result import (
    InternationalEmploymentVerificationRecordsItemResult,
)


class InternationalEmploymentVerificationRecordsItem(pydantic.BaseModel):
    """
    InternationalEmploymentVerificationRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    ISO country code of the jurisdiction where the search was run
    """
    employer: typing.Optional[
        InternationalEmploymentVerificationRecordsItemEmployer
    ] = pydantic.Field(alias="employer", default=None)
    events: typing.Optional[
        typing.List[InternationalEmploymentVerificationRecordsItemEventsItem]
    ] = pydantic.Field(alias="events", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    pdf_url: typing.Optional[str] = pydantic.Field(alias="pdf_url", default=None)
    """
    URL to PDF document containing screening result details
    """
    result: typing.Optional[InternationalEmploymentVerificationRecordsItemResult] = (
        pydantic.Field(alias="result", default=None)
    )
    status: typing.Optional[
        typing_extensions.Literal["clear", "consider", "pending"]
    ] = pydantic.Field(alias="status", default=None)

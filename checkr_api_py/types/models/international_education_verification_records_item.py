import pydantic
import typing
import typing_extensions

from .international_education_verification_records_item_events_item import (
    InternationalEducationVerificationRecordsItemEventsItem,
)
from .international_education_verification_records_item_result import (
    InternationalEducationVerificationRecordsItemResult,
)
from .international_education_verification_records_item_school import (
    InternationalEducationVerificationRecordsItemSchool,
)


class InternationalEducationVerificationRecordsItem(pydantic.BaseModel):
    """
    InternationalEducationVerificationRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    ISO country code of the jurisdiction where the search was run
    """
    events: typing.Optional[
        typing.List[InternationalEducationVerificationRecordsItemEventsItem]
    ] = pydantic.Field(alias="events", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    pdf_url: typing.Optional[str] = pydantic.Field(alias="pdf_url", default=None)
    """
    URL to PDF document containing screening result details
    """
    result: typing.Optional[InternationalEducationVerificationRecordsItemResult] = (
        pydantic.Field(alias="result", default=None)
    )
    school: typing.Optional[InternationalEducationVerificationRecordsItemSchool] = (
        pydantic.Field(alias="school", default=None)
    )
    status: typing.Optional[
        typing_extensions.Literal["clear", "consider", "pending"]
    ] = pydantic.Field(alias="status", default=None)

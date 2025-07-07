import pydantic
import typing

from .education_verification_records_item_result_degrees_item import (
    EducationVerificationRecordsItemResultDegreesItem,
)


class EducationVerificationRecordsItemResult(pydantic.BaseModel):
    """
    EducationVerificationRecordsItemResult
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    degrees: typing.Optional[
        typing.List[EducationVerificationRecordsItemResultDegreesItem]
    ] = pydantic.Field(alias="degrees", default=None)
    """
    Array of degrees verified by vendors
    """
    verified: typing.Optional[bool] = pydantic.Field(alias="verified", default=None)

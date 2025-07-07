import pydantic
import typing


class InternationalEducationVerificationRecordsItemResult(pydantic.BaseModel):
    """
    InternationalEducationVerificationRecordsItemResult
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    verified: typing.Optional[bool] = pydantic.Field(alias="verified", default=None)

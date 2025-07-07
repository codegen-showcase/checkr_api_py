import pydantic
import typing


class EducationVerificationRecordsItemResultDegreesItem(pydantic.BaseModel):
    """
    EducationVerificationRecordsItemResultDegreesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    major_concentrations: typing.Optional[str] = pydantic.Field(
        alias="major_concentrations", default=None
    )
    majors: typing.Optional[str] = pydantic.Field(alias="majors", default=None)
    minors: typing.Optional[str] = pydantic.Field(alias="minors", default=None)
    title: typing.Optional[str] = pydantic.Field(alias="title", default=None)
    year_awarded: typing.Optional[str] = pydantic.Field(
        alias="year_awarded", default=None
    )

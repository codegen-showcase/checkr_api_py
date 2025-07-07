import pydantic
import typing


class SexOffenderSearchRecordsItem(pydantic.BaseModel):
    """
    SexOffenderSearchRecordsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    age: typing.Optional[int] = pydantic.Field(alias="age", default=None)
    """
    Age listed on the record.
    """
    dob: typing.Optional[str] = pydantic.Field(alias="dob", default=None)
    """
    Date of birth listed on the record.
    """
    full_name: typing.Optional[str] = pydantic.Field(alias="full_name", default=None)
    """
    Name listed on the record.
    """
    registration_end: typing.Optional[str] = pydantic.Field(
        alias="registration_end", default=None
    )
    """
    End date for the registration.
    """
    registration_start: typing.Optional[str] = pydantic.Field(
        alias="registration_start", default=None
    )
    """
    Start date for the registration.
    """
    registry: typing.Optional[str] = pydantic.Field(alias="registry", default=None)
    """
    State in which the record was registered.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State listed for the record.
    """

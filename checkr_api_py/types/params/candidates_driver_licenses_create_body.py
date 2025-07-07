import pydantic
import typing
import typing_extensions


class CandidatesDriverLicensesCreateBody(typing_extensions.TypedDict):
    """
    CandidatesDriverLicensesCreateBody
    """

    current: typing_extensions.Required[bool]
    """
    Defines whether the driver license is the candidate's current license. `true` if the license is the candidate's current license, `false` otherwise.
    """

    issued_date: typing_extensions.NotRequired[str]
    """
    The issued date of the driver license.
    """

    number: typing_extensions.Required[str]
    """
    The driver license number.
    """

    state: typing_extensions.Required[str]
    """
    The state that issued the driver license.
    """


class _SerializerCandidatesDriverLicensesCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesDriverLicensesCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    current: bool = pydantic.Field(
        alias="current",
    )
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    number: str = pydantic.Field(
        alias="number",
    )
    state: str = pydantic.Field(
        alias="state",
    )

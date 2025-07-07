import pydantic
import typing
import typing_extensions


class CandidatesDriverLicensesUpdateBody(typing_extensions.TypedDict):
    """
    CandidatesDriverLicensesUpdateBody
    """

    current: typing_extensions.NotRequired[bool]
    """
    The updated current status of the driver license. `true` if the license is the candidate's current license, `false` otherwise.
    """

    issued_date: typing_extensions.NotRequired[str]
    """
    The updated issued date of the driver license.
    """

    number: typing_extensions.NotRequired[str]
    """
    The updated number of the driver license.
    """

    state: typing_extensions.NotRequired[str]
    """
    The updated state that issued the driver license.
    """


class _SerializerCandidatesDriverLicensesUpdateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesDriverLicensesUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    current: typing.Optional[bool] = pydantic.Field(alias="current", default=None)
    issued_date: typing.Optional[str] = pydantic.Field(
        alias="issued_date", default=None
    )
    number: typing.Optional[str] = pydantic.Field(alias="number", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)

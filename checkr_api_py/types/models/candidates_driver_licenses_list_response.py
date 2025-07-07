import pydantic
import typing
import typing_extensions

from .driver_license import DriverLicense


class CandidatesDriverLicensesListResponse(pydantic.BaseModel):
    """
    CandidatesDriverLicensesListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    data: typing.Optional[typing.List[DriverLicense]] = pydantic.Field(
        alias="data", default=None
    )
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )
    """
    A list
    """

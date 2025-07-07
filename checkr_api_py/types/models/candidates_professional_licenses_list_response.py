import pydantic
import typing
import typing_extensions

from .professional_license import ProfessionalLicense


class CandidatesProfessionalLicensesListResponse(pydantic.BaseModel):
    """
    CandidatesProfessionalLicensesListResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    data: typing.Optional[typing.List[ProfessionalLicense]] = pydantic.Field(
        alias="data", default=None
    )
    object: typing.Optional[typing_extensions.Literal["list"]] = pydantic.Field(
        alias="object", default=None
    )

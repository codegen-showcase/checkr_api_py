import pydantic
import typing


class ProfessionalLicenseVerificationCertificationsItemResultSubResultsItem(
    pydantic.BaseModel
):
    """
    ProfessionalLicenseVerificationCertificationsItemResultSubResultsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Certifying organization's name for the data returned.
    """
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    """
    Certifying organization specific data value.
    """

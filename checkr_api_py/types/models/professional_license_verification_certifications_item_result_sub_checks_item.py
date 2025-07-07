import pydantic
import typing
import typing_extensions


class ProfessionalLicenseVerificationCertificationsItemResultSubChecksItem(
    pydantic.BaseModel
):
    """
    ProfessionalLicenseVerificationCertificationsItemResultSubChecksItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    name: typing.Optional[
        typing_extensions.Literal[
            "data_consistency", "found", "in_good_standing", "not_expired"
        ]
    ] = pydantic.Field(alias="name", default=None)
    """
    `not_expired`: Certification active.<br>
    `data_consistency`: Certification matches candidate PII.<br>
    `in_good_standing`: Certification not revoked.<br>
    `found`: Certification found given license identifier.<br>
    
    """
    status: typing.Optional[typing_extensions.Literal["clear", "consider"]] = (
        pydantic.Field(alias="status", default=None)
    )

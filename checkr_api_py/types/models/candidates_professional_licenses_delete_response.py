import pydantic
import typing


class CandidatesProfessionalLicensesDeleteResponse(pydantic.BaseModel):
    """
    CandidatesProfessionalLicensesDeleteResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    """
    Expiration date of the professional license
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    issuer_name: typing.Optional[str] = pydantic.Field(
        alias="issuer_name", default=None
    )
    """
    Name of the organization that issued the professional license
    """
    issuer_region: typing.Optional[str] = pydantic.Field(
        alias="issuer_region", default=None
    )
    """
    2-letter abbreviation of US state where license was issued. For licenses not issued for a specific state, use "United States".
    """
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    """
    Unique identifier assigned to license by issuer. Format may vary
    """
    license_type: typing.Optional[str] = pydantic.Field(
        alias="license_type", default=None
    )
    """
    Category or industry of professional license
    """
    deleted_at: typing.Optional[str] = pydantic.Field(alias="deleted_at", default=None)
    """
    Timestamp of record deletion
    """

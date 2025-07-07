import pydantic
import typing
import typing_extensions


class CandidatesProfessionalLicensesCreateBody(typing_extensions.TypedDict):
    """
    CandidatesProfessionalLicensesCreateBody
    """

    expiration_date: typing_extensions.NotRequired[str]
    """
    Expiration date of the professional license
    """

    id: typing_extensions.NotRequired[str]
    """
    ID of the resource.
    """

    issuer_name: typing_extensions.NotRequired[str]
    """
    Name of the organization that issued the professional license
    """

    issuer_region: typing_extensions.NotRequired[str]
    """
    2-letter abbreviation of US state where license was issued. For licenses not issued for a specific state, use "United States".
    """

    license_number: typing_extensions.NotRequired[str]
    """
    Unique identifier assigned to license by issuer. Format may vary
    """

    license_type: typing_extensions.NotRequired[str]
    """
    Category or industry of professional license
    """

    certification_document_id: typing_extensions.Required[str]
    """
    ID of document previously created with the [uploadDocument](/#operation/uploadDocument) endpoint. Document must be of `type` `professional_license_certification_image` and should contain an image proof of professional license to be verified.
    """


class _SerializerCandidatesProfessionalLicensesCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesProfessionalLicensesCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    expiration_date: typing.Optional[str] = pydantic.Field(
        alias="expiration_date", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    issuer_name: typing.Optional[str] = pydantic.Field(
        alias="issuer_name", default=None
    )
    issuer_region: typing.Optional[str] = pydantic.Field(
        alias="issuer_region", default=None
    )
    license_number: typing.Optional[str] = pydantic.Field(
        alias="license_number", default=None
    )
    license_type: typing.Optional[str] = pydantic.Field(
        alias="license_type", default=None
    )
    certification_document_id: str = pydantic.Field(
        alias="certification_document_id",
    )

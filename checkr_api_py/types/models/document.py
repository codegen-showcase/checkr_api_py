import pydantic
import typing
import typing_extensions


class Document(pydantic.BaseModel):
    """
    Document
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    content_type: typing.Optional[str] = pydantic.Field(
        alias="content_type", default=None
    )
    """
    File’s content type.
    """
    created_at: typing.Optional[str] = pydantic.Field(alias="created_at", default=None)
    """
    Time at which the Document was created.
    """
    download_uri: typing.Optional[str] = pydantic.Field(
        alias="download_uri", default=None
    )
    """
    JSON encoded URL of the document. This URL is valid for 15 minutes.
    """
    filename: typing.Optional[str] = pydantic.Field(alias="filename", default=None)
    """
    File’s name.
    """
    filesize: typing.Optional[int] = pydantic.Field(alias="filesize", default=None)
    """
    File’s size in bytes.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the resource.
    """
    object: typing.Optional[typing_extensions.Literal["document"]] = pydantic.Field(
        alias="object", default=None
    )
    type_: typing.Optional[
        typing_extensions.Literal[
            "consent",
            "credit_report_consent_form",
            "degree",
            "diploma",
            "driver_license",
            "driver_license_back",
            "driver_license_history",
            "drug_screen_donor_pass",
            "education_certificate",
            "education_proof",
            "employment_proof",
            "health_screening_occupational_health_document",
            "health_screening_result_certificate",
            "international_consent_form",
            "order_summary_pdf",
            "passport",
            "paystub",
            "pdf_credit_report",
            "pdf_health_report",
            "pdf_individualized_assessment",
            "pdf_professional_license_verification_report",
            "pdf_report",
            "pdf_self_disclosure",
            "pdf_wisconsin_doj",
            "previous_driver_license",
            "professional_license_certification_image",
            "screening_pass",
            "selfie",
            "ssn_card",
            "state_id_card",
            "state_id_card_back",
            "tax_form1099",
            "tax_form_schedule_c",
            "tax_form_w2",
            "transcript",
        ]
    ] = pydantic.Field(alias="type", default=None)
    """
    The type of Document.
    """

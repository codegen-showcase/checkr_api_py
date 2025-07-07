import httpx
import pydantic
import typing
import typing_extensions


class CandidatesDocumentsCreateBody(typing_extensions.TypedDict):
    """
    CandidatesDocumentsCreateBody
    """

    file: typing_extensions.Required[httpx._types.FileTypes]
    """
    Path to the document on your local file system.
    
    Valid MIME types: `image/gif`, `image/jpg`, `image/jpeg`, `image/png`, `image/bmp`, `image/tiff`, `application/pdf`, `image/heic`.
    
    """

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "alien_id",
            "citizenship_certificate",
            "consent",
            "credit_report_consent_form",
            "degree",
            "diploma",
            "driver_license",
            "driver_license_back",
            "driver_license_history",
            "education_certificate",
            "education_proof",
            "electronic_consent_form",
            "employment_proof",
            "government_id",
            "international_consent_form",
            "military_id",
            "national_id",
            "national_id_back",
            "passport",
            "passport_signature_page",
            "paystub",
            "previous_driver_license",
            "professional_license_certification_image",
            "selfie",
            "ssn_card",
            "state_id_card",
            "state_id_card_back",
            "student_id",
            "tax_form1099",
            "tax_form_schedule_c",
            "tax_form_w2",
            "taxpayer_id",
            "transcript",
        ]
    ]


class _SerializerCandidatesDocumentsCreateBody(pydantic.BaseModel):
    """
    Serializer for CandidatesDocumentsCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    file: typing.Optional[typing.Any] = pydantic.Field(
        alias="file", default=None, exclude=True
    )
    type_: typing_extensions.Literal[
        "alien_id",
        "citizenship_certificate",
        "consent",
        "credit_report_consent_form",
        "degree",
        "diploma",
        "driver_license",
        "driver_license_back",
        "driver_license_history",
        "education_certificate",
        "education_proof",
        "electronic_consent_form",
        "employment_proof",
        "government_id",
        "international_consent_form",
        "military_id",
        "national_id",
        "national_id_back",
        "passport",
        "passport_signature_page",
        "paystub",
        "previous_driver_license",
        "professional_license_certification_image",
        "selfie",
        "ssn_card",
        "state_id_card",
        "state_id_card_back",
        "student_id",
        "tax_form1099",
        "tax_form_schedule_c",
        "tax_form_w2",
        "taxpayer_id",
        "transcript",
    ] = pydantic.Field(
        alias="type",
    )

    @staticmethod
    def get_files_from_typed_dict(
        item: CandidatesDocumentsCreateBody,
    ) -> typing.List[typing.Tuple[str, httpx._types.FileTypes]]:
        files: typing.List[typing.Tuple[str, httpx._types.FileTypes]] = []

        file = item.get("file", None)
        if isinstance(file, list):
            files.extend([("file", f) for f in file])
        elif file is not None:
            files.append(("file", file))

        return files

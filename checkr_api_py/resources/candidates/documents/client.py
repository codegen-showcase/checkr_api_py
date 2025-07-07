import httpx
import typing
import typing_extensions

from checkr_api_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    filter_not_given,
    to_encodable,
    type_utils,
)
from checkr_api_py.types import models, params


class DocumentsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        candidate_id: str,
        types: typing.Union[
            typing.Optional[
                typing.List[
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
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesDocumentsListResponse:
        """
        List a Candidate's Documents

        Returns an array of candidate-provided Documents for the input `candidate_id`.


        GET /candidates/{candidate_id}/documents

        Args:
            types[]: The type of candidate-provided document to return. If `types[]` is not included in the call, all available Candidate Documents will be returned.
            candidate_id: ID of the Candidate for whom documents will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Documents

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.documents.list(candidate_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(types, type_utils.NotGiven):
            encode_query_param(
                _query,
                "types[]",
                to_encodable(
                    item=types,
                    dump_with=typing.List[
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
                    ],
                ),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/documents",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesDocumentsListResponse,
            request_options=request_options or default_request_options(),
        )

    def create(
        self,
        *,
        candidate_id: str,
        file: httpx._types.FileTypes,
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
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Upload a new Candidate Document

        Uploads a new Candidate Document.

        POST /candidates/{candidate_id}/documents

        Args:
            candidate_id: Upload a document for the input `candidate_id`.
            file: Path to the document on your local file system.

        Valid MIME types: `image/gif`, `image/jpg`, `image/jpeg`, `image/png`, `image/bmp`, `image/tiff`, `application/pdf`, `image/heic`.

            type: typing_extensions.Literal["alien_id", "citizenship_certificate", "consent", "credit_report_consent_form", "degree", "diploma", "driver_license", "driver_license_back", "driver_license_history", "education_certificate", "education_proof", "electronic_consent_form", "employment_proof", "government_id", "international_consent_form", "military_id", "national_id", "national_id_back", "passport", "passport_signature_page", "paystub", "previous_driver_license", "professional_license_certification_image", "selfie", "ssn_card", "state_id_card", "state_id_card_back", "student_id", "tax_form1099", "tax_form_schedule_c", "tax_form_w2", "taxpayer_id", "transcript"]
            request_options: Additional options to customize the HTTP request

        Returns:
            Document was successfully uploaded

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.candidates.documents.create(
            candidate_id="string", file=open("uploads/file.pdf", "rb"), type_="alien_id"
        )
        ```
        """
        _data = to_encodable(
            item={"file": file, "type_": type_},
            dump_with=params._SerializerCandidatesDocumentsCreateBody,
        )
        _files = (
            params._SerializerCandidatesDocumentsCreateBody.get_files_from_typed_dict(
                filter_not_given({"file": file, "type_": type_})
            )
        )
        return self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/documents",
            auth_names=["basic_auth"],
            data=_data,
            files=_files,
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )


class AsyncDocumentsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        candidate_id: str,
        types: typing.Union[
            typing.Optional[
                typing.List[
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
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.CandidatesDocumentsListResponse:
        """
        List a Candidate's Documents

        Returns an array of candidate-provided Documents for the input `candidate_id`.


        GET /candidates/{candidate_id}/documents

        Args:
            types[]: The type of candidate-provided document to return. If `types[]` is not included in the call, all available Candidate Documents will be returned.
            candidate_id: ID of the Candidate for whom documents will be retrieved.
            request_options: Additional options to customize the HTTP request

        Returns:
            List of Documents

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.documents.list(candidate_id="string")
        ```
        """
        _query: QueryParams = {}
        if not isinstance(types, type_utils.NotGiven):
            encode_query_param(
                _query,
                "types[]",
                to_encodable(
                    item=types,
                    dump_with=typing.List[
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
                    ],
                ),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path=f"/candidates/{candidate_id}/documents",
            auth_names=["basic_auth"],
            query_params=_query,
            cast_to=models.CandidatesDocumentsListResponse,
            request_options=request_options or default_request_options(),
        )

    async def create(
        self,
        *,
        candidate_id: str,
        file: httpx._types.FileTypes,
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
        ],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Upload a new Candidate Document

        Uploads a new Candidate Document.

        POST /candidates/{candidate_id}/documents

        Args:
            candidate_id: Upload a document for the input `candidate_id`.
            file: Path to the document on your local file system.

        Valid MIME types: `image/gif`, `image/jpg`, `image/jpeg`, `image/png`, `image/bmp`, `image/tiff`, `application/pdf`, `image/heic`.

            type: typing_extensions.Literal["alien_id", "citizenship_certificate", "consent", "credit_report_consent_form", "degree", "diploma", "driver_license", "driver_license_back", "driver_license_history", "education_certificate", "education_proof", "electronic_consent_form", "employment_proof", "government_id", "international_consent_form", "military_id", "national_id", "national_id_back", "passport", "passport_signature_page", "paystub", "previous_driver_license", "professional_license_certification_image", "selfie", "ssn_card", "state_id_card", "state_id_card_back", "student_id", "tax_form1099", "tax_form_schedule_c", "tax_form_w2", "taxpayer_id", "transcript"]
            request_options: Additional options to customize the HTTP request

        Returns:
            Document was successfully uploaded

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.candidates.documents.create(
            candidate_id="string", file=open("uploads/file.pdf", "rb"), type_="alien_id"
        )
        ```
        """
        _data = to_encodable(
            item={"file": file, "type_": type_},
            dump_with=params._SerializerCandidatesDocumentsCreateBody,
        )
        _files = (
            params._SerializerCandidatesDocumentsCreateBody.get_files_from_typed_dict(
                filter_not_given({"file": file, "type_": type_})
            )
        )
        return await self._base_client.request(
            method="POST",
            path=f"/candidates/{candidate_id}/documents",
            auth_names=["basic_auth"],
            data=_data,
            files=_files,
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )

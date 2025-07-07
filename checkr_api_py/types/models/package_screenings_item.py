import pydantic
import typing
import typing_extensions


class PackageScreeningsItem(pydantic.BaseModel):
    """
    PackageScreeningsItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    subtype: typing.Optional[str] = pydantic.Field(alias="subtype", default=None)
    type_: typing.Optional[
        typing_extensions.Literal[
            "county_civil_search",
            "county_criminal_search",
            "credit_report",
            "drug_screening",
            "education_verification",
            "employment_verification",
            "eviction_search",
            "facis_search",
            "federal_civil_search",
            "federal_criminal_search",
            "global_watchlist_search",
            "international_criminal_search",
            "motor_vehicle_report",
            "municipal_criminal_search",
            "national_criminal_search",
            "personal_reference_verification",
            "professional_license_verification",
            "professional_reference_verification",
            "sex_offender_search",
            "ssn_trace",
            "state_criminal_search",
        ]
    ] = pydantic.Field(alias="type", default=None)

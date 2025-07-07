import pydantic
import typing
import typing_extensions


class AssessedObject(pydantic.BaseModel):
    """
    TODO

    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    object_id: typing.Optional[str] = pydantic.Field(alias="object_id", default=None)
    """
    ID of the resource.
    """
    object_type: typing.Optional[
        typing_extensions.Literal[
            "child_abuse_search",
            "criminal_charge",
            "drug_screening",
            "drug_screening_v2",
            "education_verification",
            "employment_verification",
            "global_watchlist_charge",
            "motor_vehicle_report",
            "occupational_health_screening",
            "sex_offender_search",
        ]
    ] = pydantic.Field(alias="object_type", default=None)

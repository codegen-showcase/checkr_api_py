import pydantic
import typing
import typing_extensions


class DrugAlcoholClearinghouse(pydantic.BaseModel):
    """
    DrugAlcoholClearinghouse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[
        typing_extensions.Literal["candidate_missing_consent", "request_withdrawn"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    """
    The reason the screening was canceled.
    """
    cancellation_reason_description: typing.Optional[
        typing_extensions.Literal["Candidate consent not provided", "Request withdrawn"]
    ] = pydantic.Field(alias="cancellation_reason_description", default=None)
    """
    Description of the `cancellation_reason` for the screening.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    ID of the resource.
    """
    query_result: typing.Optional[
        typing_extensions.Literal["Driver Not Prohibited", "Driver Prohibited"]
    ] = pydantic.Field(alias="query_result", default=None)
    """
    The result of the Drug & Alcohol Clearinghouse query.
    """
    report_id: typing.Optional[str] = pydantic.Field(alias="report_id", default=None)
    """
    The ID of the Report.
    """
    status: typing.Optional[
        typing_extensions.Literal["canceled", "complete", "pending"]
    ] = pydantic.Field(alias="status", default=None)
    """
    The status of the screening.
    """

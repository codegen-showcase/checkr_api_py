import pydantic
import typing
import typing_extensions

from .report_drug_screening_analytes_item import ReportDrugScreeningAnalytesItem
from .report_drug_screening_events_item import ReportDrugScreeningEventsItem


class ReportDrugScreening(pydantic.BaseModel):
    """
    Embedded Drug Screening object
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    analytes: typing.Optional[typing.List[ReportDrugScreeningAnalytesItem]] = (
        pydantic.Field(alias="analytes", default=None)
    )
    """
    Array of result analytes from the Drug Screening Panel
    """
    appointment_id: typing.Optional[str] = pydantic.Field(
        alias="appointment_id", default=None
    )
    """
    ID of the Appointment linked to the Drug Screening.
    """
    disposition: typing.Optional[
        typing_extensions.Literal["canceled", "negative", "positive"]
    ] = pydantic.Field(alias="disposition", default=None)
    """
    Medical evaluation for entire screening
    """
    events: typing.Optional[typing.List[ReportDrugScreeningEventsItem]] = (
        pydantic.Field(alias="events", default=None)
    )
    """
    Array of drug screening events
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    ID of the Drug Screening linked to the Report.
    """
    mro_notes: typing.Optional[str] = pydantic.Field(alias="mro_notes", default=None)
    """
    Notes from Medical Review Officer
    """
    result: typing.Optional[typing_extensions.Literal["clear", "consider"]] = (
        pydantic.Field(alias="result", default=None)
    )
    """
    Outcome of the Drug Screening.
    
    """
    screening_pass_expires_at: typing.Optional[str] = pydantic.Field(
        alias="screening_pass_expires_at", default=None
    )
    """
    Time the Candidate has to complete the drug screening
    """
    status: typing.Optional[
        typing_extensions.Literal[
            "canceled", "clear", "complete", "consider", "pending", "suspended"
        ]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the Drug Screening.
    
    """

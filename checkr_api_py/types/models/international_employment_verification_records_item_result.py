import pydantic
import typing

from .international_employment_verification_records_item_result_contract_type import (
    InternationalEmploymentVerificationRecordsItemResultContractType,
)
from .international_employment_verification_records_item_result_end_date import (
    InternationalEmploymentVerificationRecordsItemResultEndDate,
)
from .international_employment_verification_records_item_result_position import (
    InternationalEmploymentVerificationRecordsItemResultPosition,
)
from .international_employment_verification_records_item_result_questions_item import (
    InternationalEmploymentVerificationRecordsItemResultQuestionsItem,
)
from .international_employment_verification_records_item_result_salary import (
    InternationalEmploymentVerificationRecordsItemResultSalary,
)
from .international_employment_verification_records_item_result_start_date import (
    InternationalEmploymentVerificationRecordsItemResultStartDate,
)


class InternationalEmploymentVerificationRecordsItemResult(pydantic.BaseModel):
    """
    InternationalEmploymentVerificationRecordsItemResult
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contract_type: typing.Optional[
        InternationalEmploymentVerificationRecordsItemResultContractType
    ] = pydantic.Field(alias="contract_type", default=None)
    end_date: typing.Optional[
        InternationalEmploymentVerificationRecordsItemResultEndDate
    ] = pydantic.Field(alias="end_date", default=None)
    position: typing.Optional[
        InternationalEmploymentVerificationRecordsItemResultPosition
    ] = pydantic.Field(alias="position", default=None)
    questions: typing.Optional[
        typing.List[InternationalEmploymentVerificationRecordsItemResultQuestionsItem]
    ] = pydantic.Field(alias="questions", default=None)
    """
    List of questions for the candidate's employer.
    """
    salary: typing.Optional[
        InternationalEmploymentVerificationRecordsItemResultSalary
    ] = pydantic.Field(alias="salary", default=None)
    start_date: typing.Optional[
        InternationalEmploymentVerificationRecordsItemResultStartDate
    ] = pydantic.Field(alias="start_date", default=None)

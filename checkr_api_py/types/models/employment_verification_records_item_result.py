import pydantic
import typing

from .employment_verification_records_item_result_contract_type import (
    EmploymentVerificationRecordsItemResultContractType,
)
from .employment_verification_records_item_result_end_date import (
    EmploymentVerificationRecordsItemResultEndDate,
)
from .employment_verification_records_item_result_position import (
    EmploymentVerificationRecordsItemResultPosition,
)
from .employment_verification_records_item_result_questions_item import (
    EmploymentVerificationRecordsItemResultQuestionsItem,
)
from .employment_verification_records_item_result_salary import (
    EmploymentVerificationRecordsItemResultSalary,
)
from .employment_verification_records_item_result_start_date import (
    EmploymentVerificationRecordsItemResultStartDate,
)


class EmploymentVerificationRecordsItemResult(pydantic.BaseModel):
    """
    EmploymentVerificationRecordsItemResult
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    contract_type: typing.Optional[
        EmploymentVerificationRecordsItemResultContractType
    ] = pydantic.Field(alias="contract_type", default=None)
    end_date: typing.Optional[EmploymentVerificationRecordsItemResultEndDate] = (
        pydantic.Field(alias="end_date", default=None)
    )
    position: typing.Optional[EmploymentVerificationRecordsItemResultPosition] = (
        pydantic.Field(alias="position", default=None)
    )
    questions: typing.Optional[
        typing.List[EmploymentVerificationRecordsItemResultQuestionsItem]
    ] = pydantic.Field(alias="questions", default=None)
    """
    List of questions for the candidate's employer.
    """
    salary: typing.Optional[EmploymentVerificationRecordsItemResultSalary] = (
        pydantic.Field(alias="salary", default=None)
    )
    start_date: typing.Optional[EmploymentVerificationRecordsItemResultStartDate] = (
        pydantic.Field(alias="start_date", default=None)
    )

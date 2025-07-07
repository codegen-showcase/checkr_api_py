import pydantic
import typing

from .license_info import LicenseInfo
from .violation import Violation


class LicenseReport(pydantic.BaseModel):
    """
    LicenseReport
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actual_license_class: typing.Optional[str] = pydantic.Field(
        alias="actual_license_class", default=None
    )
    """
    The actual, verified license class this driver is eligible for. **Example:** G, G1, G2
    """
    is_valid_license_class: typing.Optional[bool] = pydantic.Field(
        alias="is_valid_license_class", default=None
    )
    """
    Boolean check to confirm if the License Classes match
    """
    license_infos: typing.Optional[typing.List[LicenseInfo]] = pydantic.Field(
        alias="license_infos", default=None
    )
    """
    Array of LicenseInfo objects
    """
    license_status: typing.Optional[str] = pydantic.Field(
        alias="license_status", default=None
    )
    """
    Final result of the search
    """
    violations: typing.Optional[typing.List[Violation]] = pydantic.Field(
        alias="violations", default=None
    )
    """
    Array of Violation objects.
    
    **Note:** The violations, if any, will show up only if `include_driver_history` is set to `true`. Otherwise, it will return an empty violation array.
    
    """

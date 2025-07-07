import httpx
import typing

from checkr_api_py.core import AsyncBaseClient, AuthBasic, SyncBaseClient
from checkr_api_py.environment import Environment, _get_base_url
from checkr_api_py.resources.account import AccountClient, AsyncAccountClient
from checkr_api_py.resources.accounts import AccountsClient, AsyncAccountsClient
from checkr_api_py.resources.adverse_actions import (
    AdverseActionsClient,
    AsyncAdverseActionsClient,
)
from checkr_api_py.resources.candidate_stories import (
    AsyncCandidateStoriesClient,
    CandidateStoriesClient,
)
from checkr_api_py.resources.candidates import AsyncCandidatesClient, CandidatesClient
from checkr_api_py.resources.continuous_checks import (
    AsyncContinuousChecksClient,
    ContinuousChecksClient,
)
from checkr_api_py.resources.counties import AsyncCountiesClient, CountiesClient
from checkr_api_py.resources.county_criminal_searches import (
    AsyncCountyCriminalSearchesClient,
    CountyCriminalSearchesClient,
)
from checkr_api_py.resources.documents import AsyncDocumentsClient, DocumentsClient
from checkr_api_py.resources.drug_alcohol_clearinghouse_searches import (
    AsyncDrugAlcoholClearinghouseSearchesClient,
    DrugAlcoholClearinghouseSearchesClient,
)
from checkr_api_py.resources.education_verifications import (
    AsyncEducationVerificationsClient,
    EducationVerificationsClient,
)
from checkr_api_py.resources.employment_verifications import (
    AsyncEmploymentVerificationsClient,
    EmploymentVerificationsClient,
)
from checkr_api_py.resources.facis_searches import (
    AsyncFacisSearchesClient,
    FacisSearchesClient,
)
from checkr_api_py.resources.federal_civil_district_searches import (
    AsyncFederalCivilDistrictSearchesClient,
    FederalCivilDistrictSearchesClient,
)
from checkr_api_py.resources.federal_civil_searches import (
    AsyncFederalCivilSearchesClient,
    FederalCivilSearchesClient,
)
from checkr_api_py.resources.federal_criminal_searches import (
    AsyncFederalCriminalSearchesClient,
    FederalCriminalSearchesClient,
)
from checkr_api_py.resources.federal_district_criminal_searches import (
    AsyncFederalDistrictCriminalSearchesClient,
    FederalDistrictCriminalSearchesClient,
)
from checkr_api_py.resources.geos import AsyncGeosClient, GeosClient
from checkr_api_py.resources.global_watchlist_searches import (
    AsyncGlobalWatchlistSearchesClient,
    GlobalWatchlistSearchesClient,
)
from checkr_api_py.resources.hierarchy import AsyncHierarchyClient, HierarchyClient
from checkr_api_py.resources.i9 import AsyncI9Client, I9Client
from checkr_api_py.resources.international_adverse_media_searches import (
    AsyncInternationalAdverseMediaSearchesClient,
    InternationalAdverseMediaSearchesClient,
)
from checkr_api_py.resources.international_criminal_searches import (
    AsyncInternationalCriminalSearchesClient,
    InternationalCriminalSearchesClient,
)
from checkr_api_py.resources.international_education_verifications import (
    AsyncInternationalEducationVerificationsClient,
    InternationalEducationVerificationsClient,
)
from checkr_api_py.resources.international_employment_verifications import (
    AsyncInternationalEmploymentVerificationsClient,
    InternationalEmploymentVerificationsClient,
)
from checkr_api_py.resources.international_global_watchlist_searches import (
    AsyncInternationalGlobalWatchlistSearchesClient,
    InternationalGlobalWatchlistSearchesClient,
)
from checkr_api_py.resources.international_identity_document_validation import (
    AsyncInternationalIdentityDocumentValidationClient,
    InternationalIdentityDocumentValidationClient,
)
from checkr_api_py.resources.international_motor_vehicle_reports import (
    AsyncInternationalMotorVehicleReportsClient,
    InternationalMotorVehicleReportsClient,
)
from checkr_api_py.resources.invitations import (
    AsyncInvitationsClient,
    InvitationsClient,
)
from checkr_api_py.resources.motor_vehicle_reports import (
    AsyncMotorVehicleReportsClient,
    MotorVehicleReportsClient,
)
from checkr_api_py.resources.national_criminal_searches import (
    AsyncNationalCriminalSearchesClient,
    NationalCriminalSearchesClient,
)
from checkr_api_py.resources.nodes import AsyncNodesClient, NodesClient
from checkr_api_py.resources.packages import AsyncPackagesClient, PackagesClient
from checkr_api_py.resources.personal_reference_verifications import (
    AsyncPersonalReferenceVerificationsClient,
    PersonalReferenceVerificationsClient,
)
from checkr_api_py.resources.professional_license_verifications import (
    AsyncProfessionalLicenseVerificationsClient,
    ProfessionalLicenseVerificationsClient,
)
from checkr_api_py.resources.professional_reference_verifications import (
    AsyncProfessionalReferenceVerificationsClient,
    ProfessionalReferenceVerificationsClient,
)
from checkr_api_py.resources.programs import AsyncProgramsClient, ProgramsClient
from checkr_api_py.resources.reports import AsyncReportsClient, ReportsClient
from checkr_api_py.resources.sex_offender_searches import (
    AsyncSexOffenderSearchesClient,
    SexOffenderSearchesClient,
)
from checkr_api_py.resources.ssn_traces import AsyncSsnTracesClient, SsnTracesClient
from checkr_api_py.resources.state_criminal_searches import (
    AsyncStateCriminalSearchesClient,
    StateCriminalSearchesClient,
)
from checkr_api_py.resources.subscriptions import (
    AsyncSubscriptionsClient,
    SubscriptionsClient,
)
from checkr_api_py.resources.users import AsyncUsersClient, UsersClient
from checkr_api_py.resources.verifications import (
    AsyncVerificationsClient,
    VerificationsClient,
)
from checkr_api_py.resources.webhooks import AsyncWebhooksClient, WebhooksClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "basic_auth", AuthBasic(username=username, password=password)
        )
        self.adverse_actions = AdverseActionsClient(base_client=self._base_client)
        self.candidate_stories = CandidateStoriesClient(base_client=self._base_client)
        self.candidates = CandidatesClient(base_client=self._base_client)
        self.continuous_checks = ContinuousChecksClient(base_client=self._base_client)
        self.geos = GeosClient(base_client=self._base_client)
        self.i9 = I9Client(base_client=self._base_client)
        self.invitations = InvitationsClient(base_client=self._base_client)
        self.nodes = NodesClient(base_client=self._base_client)
        self.packages = PackagesClient(base_client=self._base_client)
        self.reports = ReportsClient(base_client=self._base_client)
        self.subscriptions = SubscriptionsClient(base_client=self._base_client)
        self.webhooks = WebhooksClient(base_client=self._base_client)
        self.account = AccountClient(base_client=self._base_client)
        self.counties = CountiesClient(base_client=self._base_client)
        self.county_criminal_searches = CountyCriminalSearchesClient(
            base_client=self._base_client
        )
        self.documents = DocumentsClient(base_client=self._base_client)
        self.drug_alcohol_clearinghouse_searches = (
            DrugAlcoholClearinghouseSearchesClient(base_client=self._base_client)
        )
        self.education_verifications = EducationVerificationsClient(
            base_client=self._base_client
        )
        self.employment_verifications = EmploymentVerificationsClient(
            base_client=self._base_client
        )
        self.facis_searches = FacisSearchesClient(base_client=self._base_client)
        self.federal_civil_district_searches = FederalCivilDistrictSearchesClient(
            base_client=self._base_client
        )
        self.federal_civil_searches = FederalCivilSearchesClient(
            base_client=self._base_client
        )
        self.federal_criminal_searches = FederalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.federal_district_criminal_searches = FederalDistrictCriminalSearchesClient(
            base_client=self._base_client
        )
        self.global_watchlist_searches = GlobalWatchlistSearchesClient(
            base_client=self._base_client
        )
        self.hierarchy = HierarchyClient(base_client=self._base_client)
        self.international_adverse_media_searches = (
            InternationalAdverseMediaSearchesClient(base_client=self._base_client)
        )
        self.international_criminal_searches = InternationalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.international_education_verifications = (
            InternationalEducationVerificationsClient(base_client=self._base_client)
        )
        self.international_employment_verifications = (
            InternationalEmploymentVerificationsClient(base_client=self._base_client)
        )
        self.international_global_watchlist_searches = (
            InternationalGlobalWatchlistSearchesClient(base_client=self._base_client)
        )
        self.international_identity_document_validation = (
            InternationalIdentityDocumentValidationClient(base_client=self._base_client)
        )
        self.international_motor_vehicle_reports = (
            InternationalMotorVehicleReportsClient(base_client=self._base_client)
        )
        self.motor_vehicle_reports = MotorVehicleReportsClient(
            base_client=self._base_client
        )
        self.national_criminal_searches = NationalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.personal_reference_verifications = PersonalReferenceVerificationsClient(
            base_client=self._base_client
        )
        self.professional_license_verifications = (
            ProfessionalLicenseVerificationsClient(base_client=self._base_client)
        )
        self.professional_reference_verifications = (
            ProfessionalReferenceVerificationsClient(base_client=self._base_client)
        )
        self.programs = ProgramsClient(base_client=self._base_client)
        self.sex_offender_searches = SexOffenderSearchesClient(
            base_client=self._base_client
        )
        self.ssn_traces = SsnTracesClient(base_client=self._base_client)
        self.state_criminal_searches = StateCriminalSearchesClient(
            base_client=self._base_client
        )
        self.users = UsersClient(base_client=self._base_client)
        self.verifications = VerificationsClient(base_client=self._base_client)
        self.accounts = AccountsClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.ENVIRONMENT,
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "basic_auth", AuthBasic(username=username, password=password)
        )
        self.adverse_actions = AsyncAdverseActionsClient(base_client=self._base_client)
        self.candidate_stories = AsyncCandidateStoriesClient(
            base_client=self._base_client
        )
        self.candidates = AsyncCandidatesClient(base_client=self._base_client)
        self.continuous_checks = AsyncContinuousChecksClient(
            base_client=self._base_client
        )
        self.geos = AsyncGeosClient(base_client=self._base_client)
        self.i9 = AsyncI9Client(base_client=self._base_client)
        self.invitations = AsyncInvitationsClient(base_client=self._base_client)
        self.nodes = AsyncNodesClient(base_client=self._base_client)
        self.packages = AsyncPackagesClient(base_client=self._base_client)
        self.reports = AsyncReportsClient(base_client=self._base_client)
        self.subscriptions = AsyncSubscriptionsClient(base_client=self._base_client)
        self.webhooks = AsyncWebhooksClient(base_client=self._base_client)
        self.account = AsyncAccountClient(base_client=self._base_client)
        self.counties = AsyncCountiesClient(base_client=self._base_client)
        self.county_criminal_searches = AsyncCountyCriminalSearchesClient(
            base_client=self._base_client
        )
        self.documents = AsyncDocumentsClient(base_client=self._base_client)
        self.drug_alcohol_clearinghouse_searches = (
            AsyncDrugAlcoholClearinghouseSearchesClient(base_client=self._base_client)
        )
        self.education_verifications = AsyncEducationVerificationsClient(
            base_client=self._base_client
        )
        self.employment_verifications = AsyncEmploymentVerificationsClient(
            base_client=self._base_client
        )
        self.facis_searches = AsyncFacisSearchesClient(base_client=self._base_client)
        self.federal_civil_district_searches = AsyncFederalCivilDistrictSearchesClient(
            base_client=self._base_client
        )
        self.federal_civil_searches = AsyncFederalCivilSearchesClient(
            base_client=self._base_client
        )
        self.federal_criminal_searches = AsyncFederalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.federal_district_criminal_searches = (
            AsyncFederalDistrictCriminalSearchesClient(base_client=self._base_client)
        )
        self.global_watchlist_searches = AsyncGlobalWatchlistSearchesClient(
            base_client=self._base_client
        )
        self.hierarchy = AsyncHierarchyClient(base_client=self._base_client)
        self.international_adverse_media_searches = (
            AsyncInternationalAdverseMediaSearchesClient(base_client=self._base_client)
        )
        self.international_criminal_searches = AsyncInternationalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.international_education_verifications = (
            AsyncInternationalEducationVerificationsClient(
                base_client=self._base_client
            )
        )
        self.international_employment_verifications = (
            AsyncInternationalEmploymentVerificationsClient(
                base_client=self._base_client
            )
        )
        self.international_global_watchlist_searches = (
            AsyncInternationalGlobalWatchlistSearchesClient(
                base_client=self._base_client
            )
        )
        self.international_identity_document_validation = (
            AsyncInternationalIdentityDocumentValidationClient(
                base_client=self._base_client
            )
        )
        self.international_motor_vehicle_reports = (
            AsyncInternationalMotorVehicleReportsClient(base_client=self._base_client)
        )
        self.motor_vehicle_reports = AsyncMotorVehicleReportsClient(
            base_client=self._base_client
        )
        self.national_criminal_searches = AsyncNationalCriminalSearchesClient(
            base_client=self._base_client
        )
        self.personal_reference_verifications = (
            AsyncPersonalReferenceVerificationsClient(base_client=self._base_client)
        )
        self.professional_license_verifications = (
            AsyncProfessionalLicenseVerificationsClient(base_client=self._base_client)
        )
        self.professional_reference_verifications = (
            AsyncProfessionalReferenceVerificationsClient(base_client=self._base_client)
        )
        self.programs = AsyncProgramsClient(base_client=self._base_client)
        self.sex_offender_searches = AsyncSexOffenderSearchesClient(
            base_client=self._base_client
        )
        self.ssn_traces = AsyncSsnTracesClient(base_client=self._base_client)
        self.state_criminal_searches = AsyncStateCriminalSearchesClient(
            base_client=self._base_client
        )
        self.users = AsyncUsersClient(base_client=self._base_client)
        self.verifications = AsyncVerificationsClient(base_client=self._base_client)
        self.accounts = AsyncAccountsClient(base_client=self._base_client)

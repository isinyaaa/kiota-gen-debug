from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.error import Error
    from .....models.model_version import ModelVersion
    from .....models.model_version_create import ModelVersionCreate
    from .....models.model_version_list import ModelVersionList
    from .....models.order_by_field import OrderByField
    from .....models.sort_order import SortOrder
    from .item.with_modelversion_item_request_builder import WithModelversionItemRequestBuilder

class Model_versionsRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to list and create zero or more `ModelVersion` entities.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new Model_versionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha3/model_versions{?nextPageToken*,orderBy*,pageSize*,sortOrder*}", path_parameters)
    
    def by_modelversion_id(self,modelversion_id: str) -> WithModelversionItemRequestBuilder:
        """
        The REST endpoint/path used to get, update, and delete single instances of an `ModelVersion`. This path contains `GET`, `PUT`, and `DELETE` operations used to perform the get, update, and delete tasks, respectively.
        param modelversion_id: A unique identifier for a `ModelVersion`.
        Returns: WithModelversionItemRequestBuilder
        """
        if not modelversion_id:
            raise TypeError("modelversion_id cannot be null.")
        from .item.with_modelversion_item_request_builder import WithModelversionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["modelversionId"] = modelversion_id
        return WithModelversionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ModelVersionList]:
        """
        Gets a list of all `ModelVersion` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelVersionList]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "401": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.model_version_list import ModelVersionList

        return await self.request_adapter.send_async(request_info, ModelVersionList, error_mapping)
    
    async def post(self,body: Optional[ModelVersionCreate] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[ModelVersion]:
        """
        Creates a new instance of a `ModelVersion`.
        param body: Represents a ModelVersion belonging to a RegisteredModel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ModelVersion]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.model_version import ModelVersion

        return await self.request_adapter.send_async(request_info, ModelVersion, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Gets a list of all `ModelVersion` entities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[ModelVersionCreate] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Creates a new instance of a `ModelVersion`.
        param body: Represents a ModelVersion belonging to a RegisteredModel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, '{+baseurl}/api/model_registry/v1alpha3/model_versions', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> Model_versionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Model_versionsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return Model_versionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class Model_versionsRequestBuilderGetQueryParameters():
        """
        Gets a list of all `ModelVersion` entities.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "next_page_token":
                return "nextPageToken"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "page_size":
                return "pageSize"
            if original_name == "sort_order":
                return "sortOrder"
            return original_name
        
        # Token to use to retrieve next page of results.
        next_page_token: Optional[str] = None

        # Specifies the order by criteria for listing entities.
        order_by: Optional[OrderByField] = None

        # Number of entities in each page.
        page_size: Optional[str] = None

        # Specifies the sort order for listing entities, defaults to ASC.
        sort_order: Optional[SortOrder] = None

    

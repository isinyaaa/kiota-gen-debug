from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inference_service_custom_properties import InferenceService_customProperties
    from .inference_service_state import InferenceServiceState

@dataclass
class InferenceService(AdditionalDataHolder, Parsable):
    """
    An `InferenceService` entity in a `ServingEnvironment` represents a deployed `ModelVersion` from a `RegisteredModel` created by Model Serving.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    from .inference_service_state import InferenceServiceState

    # - DEPLOYED: A state indicating that the `InferenceService` should be deployed.- UNDEPLOYED: A state indicating that the `InferenceService` should be un-deployed.The state indicates the desired state of inference service.See the associated `ServeModel` for the actual status of service deployment action.
    desired_state: Optional[InferenceServiceState] = InferenceServiceState("DEPLOYED")
    # Output only. Create time of the resource in millisecond since epoch.
    create_time_since_epoch: Optional[str] = None
    # User provided custom properties which are not defined by its type.
    custom_properties: Optional[InferenceService_customProperties] = None
    # An optional description about the resource.
    description: Optional[str] = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: Optional[str] = None
    # Output only. The unique server generated id of the resource.
    id: Optional[str] = None
    # Output only. Last update time of the resource since epoch in millisecondsince epoch.
    last_update_time_since_epoch: Optional[str] = None
    # ID of the `ModelVersion` to serve. If it's unspecified, then the latest `ModelVersion` by creation order will be served.
    model_version_id: Optional[str] = None
    # The client provided name of the artifact. This field is optional. If set,it must be unique among all the artifacts of the same artifact type withina database instance and cannot be changed once set.
    name: Optional[str] = None
    # ID of the `RegisteredModel` to serve.
    registered_model_id: Optional[str] = None
    # Model runtime.
    runtime: Optional[str] = None
    # ID of the parent `ServingEnvironment` for this `InferenceService` entity.
    serving_environment_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceService:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceService
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InferenceService()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .inference_service_custom_properties import InferenceService_customProperties
        from .inference_service_state import InferenceServiceState

        from .inference_service_custom_properties import InferenceService_customProperties
        from .inference_service_state import InferenceServiceState

        fields: Dict[str, Callable[[Any], None]] = {
            "createTimeSinceEpoch": lambda n : setattr(self, 'create_time_since_epoch', n.get_str_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(InferenceService_customProperties)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "desiredState": lambda n : setattr(self, 'desired_state', n.get_enum_value(InferenceServiceState)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastUpdateTimeSinceEpoch": lambda n : setattr(self, 'last_update_time_since_epoch', n.get_str_value()),
            "modelVersionId": lambda n : setattr(self, 'model_version_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "registeredModelId": lambda n : setattr(self, 'registered_model_id', n.get_str_value()),
            "runtime": lambda n : setattr(self, 'runtime', n.get_str_value()),
            "servingEnvironmentId": lambda n : setattr(self, 'serving_environment_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("desiredState", self.desired_state)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("modelVersionId", self.model_version_id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("registeredModelId", self.registered_model_id)
        writer.write_str_value("runtime", self.runtime)
        writer.write_str_value("servingEnvironmentId", self.serving_environment_id)
        writer.write_additional_data_value(self.additional_data)
    


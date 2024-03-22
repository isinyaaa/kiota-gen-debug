from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .execution_state import ExecutionState
    from .serve_model_custom_properties import ServeModel_customProperties

@dataclass
class ServeModel(AdditionalDataHolder, Parsable):
    """
    An ML model serving action.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    from .execution_state import ExecutionState

    # The state of the Execution. The state transitions are  NEW -> RUNNING -> COMPLETE | CACHED | FAILED | CANCELEDCACHED means the execution is skipped due to cached results.CANCELED means the execution is skipped due to precondition not met. It isdifferent from CACHED in that a CANCELED execution will not have any eventassociated with it. It is different from FAILED in that there is nounexpected error happened and it is regarded as a normal state.See also: ml-metadata Execution.State
    last_known_state: Optional[ExecutionState] = ExecutionState("UNKNOWN")
    # Output only. Create time of the resource in millisecond since epoch.
    create_time_since_epoch: Optional[str] = None
    # User provided custom properties which are not defined by its type.
    custom_properties: Optional[ServeModel_customProperties] = None
    # An optional description about the resource.
    description: Optional[str] = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: Optional[str] = None
    # Output only. The unique server generated id of the resource.
    id: Optional[str] = None
    # Output only. Last update time of the resource since epoch in millisecondsince epoch.
    last_update_time_since_epoch: Optional[str] = None
    # ID of the `ModelVersion` that was served in `InferenceService`.
    model_version_id: Optional[str] = None
    # The client provided name of the artifact. This field is optional. If set,it must be unique among all the artifacts of the same artifact type withina database instance and cannot be changed once set.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServeModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServeModel
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServeModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .execution_state import ExecutionState
        from .serve_model_custom_properties import ServeModel_customProperties

        from .execution_state import ExecutionState
        from .serve_model_custom_properties import ServeModel_customProperties

        fields: Dict[str, Callable[[Any], None]] = {
            "createTimeSinceEpoch": lambda n : setattr(self, 'create_time_since_epoch', n.get_str_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(ServeModel_customProperties)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastKnownState": lambda n : setattr(self, 'last_known_state', n.get_enum_value(ExecutionState)),
            "lastUpdateTimeSinceEpoch": lambda n : setattr(self, 'last_update_time_since_epoch', n.get_str_value()),
            "modelVersionId": lambda n : setattr(self, 'model_version_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("externalId", self.external_id)
        writer.write_enum_value("lastKnownState", self.last_known_state)
        writer.write_str_value("modelVersionId", self.model_version_id)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    


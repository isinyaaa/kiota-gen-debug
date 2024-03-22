from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .model_version_custom_properties import ModelVersion_customProperties
    from .model_version_state import ModelVersionState

@dataclass
class ModelVersion(AdditionalDataHolder, Parsable):
    """
    Represents a ModelVersion belonging to a RegisteredModel.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    from .model_version_state import ModelVersionState

    # - LIVE: A state indicating that the `ModelVersion` exists- ARCHIVED: A state indicating that the `ModelVersion` has been archived.
    state: Optional[ModelVersionState] = ModelVersionState("LIVE")
    # Name of the author.
    author: Optional[str] = None
    # Output only. Create time of the resource in millisecond since epoch.
    create_time_since_epoch: Optional[str] = None
    # User provided custom properties which are not defined by its type.
    custom_properties: Optional[ModelVersion_customProperties] = None
    # An optional description about the resource.
    description: Optional[str] = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: Optional[str] = None
    # Output only. The unique server generated id of the resource.
    id: Optional[str] = None
    # Output only. Last update time of the resource since epoch in millisecondsince epoch.
    last_update_time_since_epoch: Optional[str] = None
    # The client provided name of the artifact. This field is optional. If set,it must be unique among all the artifacts of the same artifact type withina database instance and cannot be changed once set.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModelVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelVersion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ModelVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .model_version_custom_properties import ModelVersion_customProperties
        from .model_version_state import ModelVersionState

        from .model_version_custom_properties import ModelVersion_customProperties
        from .model_version_state import ModelVersionState

        fields: Dict[str, Callable[[Any], None]] = {
            "author": lambda n : setattr(self, 'author', n.get_str_value()),
            "createTimeSinceEpoch": lambda n : setattr(self, 'create_time_since_epoch', n.get_str_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(ModelVersion_customProperties)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastUpdateTimeSinceEpoch": lambda n : setattr(self, 'last_update_time_since_epoch', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ModelVersionState)),
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
        writer.write_str_value("author", self.author)
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    


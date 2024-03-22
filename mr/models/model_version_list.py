from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_resource_list import BaseResourceList
    from .model_version import ModelVersion

from .base_resource_list import BaseResourceList

@dataclass
class ModelVersionList(BaseResourceList):
    """
    List of ModelVersion entities.
    """
    # Array of `ModelVersion` entities.
    items: Optional[List[ModelVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModelVersionList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelVersionList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ModelVersionList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_resource_list import BaseResourceList
        from .model_version import ModelVersion

        from .base_resource_list import BaseResourceList
        from .model_version import ModelVersion

        fields: Dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ModelVersion)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("items", self.items)
    


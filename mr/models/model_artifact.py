from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact_state import ArtifactState
    from .model_artifact_custom_properties import ModelArtifact_customProperties

@dataclass
class ModelArtifact(AdditionalDataHolder, Parsable):
    """
    An ML model artifact.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The artifactType property
    artifact_type: Optional[str] = "model-artifact"
    from .artifact_state import ArtifactState

    #  - PENDING: A state indicating that the artifact may exist. - LIVE: A state indicating that the artifact should exist, unless somethingexternal to the system deletes it. - MARKED_FOR_DELETION: A state indicating that the artifact should be deleted. - DELETED: A state indicating that the artifact has been deleted. - ABANDONED: A state indicating that the artifact has been abandoned, which may bedue to a failed or cancelled execution. - REFERENCE: A state indicating that the artifact is a reference artifact. Atexecution start time, the orchestrator produces an output artifact foreach output key with state PENDING. However, for an intermediateartifact, this first artifact's state will be REFERENCE. Intermediateartifacts emitted during a component's execution will copy the REFERENCEartifact's attributes. At the end of an execution, the artifact stateshould remain REFERENCE instead of being changed to LIVE.See also: ml-metadata Artifact.State
    state: Optional[ArtifactState] = ArtifactState("UNKNOWN")
    # Output only. Create time of the resource in millisecond since epoch.
    create_time_since_epoch: Optional[str] = None
    # User provided custom properties which are not defined by its type.
    custom_properties: Optional[ModelArtifact_customProperties] = None
    # An optional description about the resource.
    description: Optional[str] = None
    # The external id that come from the clients’ system. This field is optional.If set, it must be unique among all resources within a database instance.
    external_id: Optional[str] = None
    # Output only. The unique server generated id of the resource.
    id: Optional[str] = None
    # Output only. Last update time of the resource since epoch in millisecondsince epoch.
    last_update_time_since_epoch: Optional[str] = None
    # Name of the model format.
    model_format_name: Optional[str] = None
    # Version of the model format.
    model_format_version: Optional[str] = None
    # The client provided name of the artifact. This field is optional. If set,it must be unique among all the artifacts of the same artifact type withina database instance and cannot be changed once set.
    name: Optional[str] = None
    # Name of the service account with storage secret.
    service_account_name: Optional[str] = None
    # Storage secret name.
    storage_key: Optional[str] = None
    # Path for model in storage provided by `storageKey`.
    storage_path: Optional[str] = None
    # The uniform resource identifier of the physical artifact.May be empty if there is no physical artifact.
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ModelArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelArtifact
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ModelArtifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .artifact_state import ArtifactState
        from .model_artifact_custom_properties import ModelArtifact_customProperties

        from .artifact_state import ArtifactState
        from .model_artifact_custom_properties import ModelArtifact_customProperties

        fields: Dict[str, Callable[[Any], None]] = {
            "artifactType": lambda n : setattr(self, 'artifact_type', n.get_str_value()),
            "createTimeSinceEpoch": lambda n : setattr(self, 'create_time_since_epoch', n.get_str_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(ModelArtifact_customProperties)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lastUpdateTimeSinceEpoch": lambda n : setattr(self, 'last_update_time_since_epoch', n.get_str_value()),
            "modelFormatName": lambda n : setattr(self, 'model_format_name', n.get_str_value()),
            "modelFormatVersion": lambda n : setattr(self, 'model_format_version', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "serviceAccountName": lambda n : setattr(self, 'service_account_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ArtifactState)),
            "storageKey": lambda n : setattr(self, 'storage_key', n.get_str_value()),
            "storagePath": lambda n : setattr(self, 'storage_path', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_str_value("artifactType", self.artifact_type)
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("modelFormatName", self.model_format_name)
        writer.write_str_value("modelFormatVersion", self.model_format_version)
        writer.write_str_value("name", self.name)
        writer.write_str_value("serviceAccountName", self.service_account_name)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("storageKey", self.storage_key)
        writer.write_str_value("storagePath", self.storage_path)
        writer.write_str_value("uri", self.uri)
        writer.write_additional_data_value(self.additional_data)
    


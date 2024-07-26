# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/cloud_audit/proto/audit_log.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.rpc.context import attribute_context_pb2 as google_dot_rpc_dot_context_dot_attribute__context__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/cloud_audit/proto/audit_log.proto',
  package='google.cloud.audit',
  syntax='proto3',
  serialized_options=b'\n\026com.google.cloud.auditB\rAuditLogProtoP\001Z7google.golang.org/genproto/googleapis/cloud/audit;audit\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/cloud/cloud_audit/proto/audit_log.proto\x12\x12google.cloud.audit\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a*google/rpc/context/attribute_context.proto\x1a\x17google/rpc/status.proto\"\xfa\x04\n\x08\x41uditLog\x12\x14\n\x0cservice_name\x18\x07 \x01(\t\x12\x13\n\x0bmethod_name\x18\x08 \x01(\t\x12\x15\n\rresource_name\x18\x0b \x01(\t\x12?\n\x11resource_location\x18\x14 \x01(\x0b\x32$.google.cloud.audit.ResourceLocation\x12\x38\n\x17resource_original_state\x18\x13 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1a\n\x12num_response_items\x18\x0c \x01(\x03\x12\"\n\x06status\x18\x02 \x01(\x0b\x32\x12.google.rpc.Status\x12\x43\n\x13\x61uthentication_info\x18\x03 \x01(\x0b\x32&.google.cloud.audit.AuthenticationInfo\x12\x41\n\x12\x61uthorization_info\x18\t \x03(\x0b\x32%.google.cloud.audit.AuthorizationInfo\x12=\n\x10request_metadata\x18\x04 \x01(\x0b\x32#.google.cloud.audit.RequestMetadata\x12(\n\x07request\x18\x10 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08response\x18\x11 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08metadata\x18\x12 \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x0cservice_data\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"\x99\x02\n\x12\x41uthenticationInfo\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x12\x1a\n\x12\x61uthority_selector\x18\x02 \x01(\t\x12\x36\n\x15third_party_principal\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12 \n\x18service_account_key_name\x18\x05 \x01(\t\x12Y\n\x1fservice_account_delegation_info\x18\x06 \x03(\x0b\x32\x30.google.cloud.audit.ServiceAccountDelegationInfo\x12\x19\n\x11principal_subject\x18\x08 \x01(\t\"\x96\x01\n\x11\x41uthorizationInfo\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x12\n\npermission\x18\x02 \x01(\t\x12\x0f\n\x07granted\x18\x03 \x01(\x08\x12J\n\x13resource_attributes\x18\x05 \x01(\x0b\x32-.google.rpc.context.AttributeContext.Resource\"\xf5\x01\n\x0fRequestMetadata\x12\x11\n\tcaller_ip\x18\x01 \x01(\t\x12\"\n\x1a\x63\x61ller_supplied_user_agent\x18\x02 \x01(\t\x12\x16\n\x0e\x63\x61ller_network\x18\x03 \x01(\t\x12H\n\x12request_attributes\x18\x07 \x01(\x0b\x32,.google.rpc.context.AttributeContext.Request\x12I\n\x16\x64\x65stination_attributes\x18\x08 \x01(\x0b\x32).google.rpc.context.AttributeContext.Peer\"I\n\x10ResourceLocation\x12\x19\n\x11\x63urrent_locations\x18\x01 \x03(\t\x12\x1a\n\x12original_locations\x18\x02 \x03(\t\"\xa8\x03\n\x1cServiceAccountDelegationInfo\x12\x65\n\x15\x66irst_party_principal\x18\x01 \x01(\x0b\x32\x44.google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipalH\x00\x12\x65\n\x15third_party_principal\x18\x02 \x01(\x0b\x32\x44.google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipalH\x00\x1a\x61\n\x13\x46irstPartyPrincipal\x12\x17\n\x0fprincipal_email\x18\x01 \x01(\t\x12\x31\n\x10service_metadata\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x1aJ\n\x13ThirdPartyPrincipal\x12\x33\n\x12third_party_claims\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\n\tAuthorityBe\n\x16\x63om.google.cloud.auditB\rAuditLogProtoP\x01Z7google.golang.org/genproto/googleapis/cloud/audit;audit\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_rpc_dot_context_dot_attribute__context__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_AUDITLOG = _descriptor.Descriptor(
  name='AuditLog',
  full_name='google.cloud.audit.AuditLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='google.cloud.audit.AuditLog.service_name', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method_name', full_name='google.cloud.audit.AuditLog.method_name', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.cloud.audit.AuditLog.resource_name', index=2,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_location', full_name='google.cloud.audit.AuditLog.resource_location', index=3,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_original_state', full_name='google.cloud.audit.AuditLog.resource_original_state', index=4,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_response_items', full_name='google.cloud.audit.AuditLog.num_response_items', index=5,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.cloud.audit.AuditLog.status', index=6,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication_info', full_name='google.cloud.audit.AuditLog.authentication_info', index=7,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorization_info', full_name='google.cloud.audit.AuditLog.authorization_info', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_metadata', full_name='google.cloud.audit.AuditLog.request_metadata', index=9,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='google.cloud.audit.AuditLog.request', index=10,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='google.cloud.audit.AuditLog.response', index=11,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.cloud.audit.AuditLog.metadata', index=12,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_data', full_name='google.cloud.audit.AuditLog.service_data', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=831,
)


_AUTHENTICATIONINFO = _descriptor.Descriptor(
  name='AuthenticationInfo',
  full_name='google.cloud.audit.AuthenticationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal_email', full_name='google.cloud.audit.AuthenticationInfo.principal_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authority_selector', full_name='google.cloud.audit.AuthenticationInfo.authority_selector', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='third_party_principal', full_name='google.cloud.audit.AuthenticationInfo.third_party_principal', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_key_name', full_name='google.cloud.audit.AuthenticationInfo.service_account_key_name', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_delegation_info', full_name='google.cloud.audit.AuthenticationInfo.service_account_delegation_info', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='principal_subject', full_name='google.cloud.audit.AuthenticationInfo.principal_subject', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=834,
  serialized_end=1115,
)


_AUTHORIZATIONINFO = _descriptor.Descriptor(
  name='AuthorizationInfo',
  full_name='google.cloud.audit.AuthorizationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='google.cloud.audit.AuthorizationInfo.resource', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permission', full_name='google.cloud.audit.AuthorizationInfo.permission', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='granted', full_name='google.cloud.audit.AuthorizationInfo.granted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_attributes', full_name='google.cloud.audit.AuthorizationInfo.resource_attributes', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1118,
  serialized_end=1268,
)


_REQUESTMETADATA = _descriptor.Descriptor(
  name='RequestMetadata',
  full_name='google.cloud.audit.RequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='caller_ip', full_name='google.cloud.audit.RequestMetadata.caller_ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='caller_supplied_user_agent', full_name='google.cloud.audit.RequestMetadata.caller_supplied_user_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='caller_network', full_name='google.cloud.audit.RequestMetadata.caller_network', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_attributes', full_name='google.cloud.audit.RequestMetadata.request_attributes', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_attributes', full_name='google.cloud.audit.RequestMetadata.destination_attributes', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1271,
  serialized_end=1516,
)


_RESOURCELOCATION = _descriptor.Descriptor(
  name='ResourceLocation',
  full_name='google.cloud.audit.ResourceLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_locations', full_name='google.cloud.audit.ResourceLocation.current_locations', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_locations', full_name='google.cloud.audit.ResourceLocation.original_locations', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1518,
  serialized_end=1591,
)


_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL = _descriptor.Descriptor(
  name='FirstPartyPrincipal',
  full_name='google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='principal_email', full_name='google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal.principal_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_metadata', full_name='google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal.service_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1832,
  serialized_end=1929,
)

_SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL = _descriptor.Descriptor(
  name='ThirdPartyPrincipal',
  full_name='google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='third_party_claims', full_name='google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipal.third_party_claims', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1931,
  serialized_end=2005,
)

_SERVICEACCOUNTDELEGATIONINFO = _descriptor.Descriptor(
  name='ServiceAccountDelegationInfo',
  full_name='google.cloud.audit.ServiceAccountDelegationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_party_principal', full_name='google.cloud.audit.ServiceAccountDelegationInfo.first_party_principal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='third_party_principal', full_name='google.cloud.audit.ServiceAccountDelegationInfo.third_party_principal', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL, _SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Authority', full_name='google.cloud.audit.ServiceAccountDelegationInfo.Authority',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1594,
  serialized_end=2018,
)

_AUDITLOG.fields_by_name['resource_location'].message_type = _RESOURCELOCATION
_AUDITLOG.fields_by_name['resource_original_state'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOG.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_AUDITLOG.fields_by_name['authentication_info'].message_type = _AUTHENTICATIONINFO
_AUDITLOG.fields_by_name['authorization_info'].message_type = _AUTHORIZATIONINFO
_AUDITLOG.fields_by_name['request_metadata'].message_type = _REQUESTMETADATA
_AUDITLOG.fields_by_name['request'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOG.fields_by_name['response'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOG.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUDITLOG.fields_by_name['service_data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_AUTHENTICATIONINFO.fields_by_name['third_party_principal'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_AUTHENTICATIONINFO.fields_by_name['service_account_delegation_info'].message_type = _SERVICEACCOUNTDELEGATIONINFO
_AUTHORIZATIONINFO.fields_by_name['resource_attributes'].message_type = google_dot_rpc_dot_context_dot_attribute__context__pb2._ATTRIBUTECONTEXT_RESOURCE
_REQUESTMETADATA.fields_by_name['request_attributes'].message_type = google_dot_rpc_dot_context_dot_attribute__context__pb2._ATTRIBUTECONTEXT_REQUEST
_REQUESTMETADATA.fields_by_name['destination_attributes'].message_type = google_dot_rpc_dot_context_dot_attribute__context__pb2._ATTRIBUTECONTEXT_PEER
_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL.fields_by_name['service_metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL.containing_type = _SERVICEACCOUNTDELEGATIONINFO
_SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL.fields_by_name['third_party_claims'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL.containing_type = _SERVICEACCOUNTDELEGATIONINFO
_SERVICEACCOUNTDELEGATIONINFO.fields_by_name['first_party_principal'].message_type = _SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL
_SERVICEACCOUNTDELEGATIONINFO.fields_by_name['third_party_principal'].message_type = _SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL
_SERVICEACCOUNTDELEGATIONINFO.oneofs_by_name['Authority'].fields.append(
  _SERVICEACCOUNTDELEGATIONINFO.fields_by_name['first_party_principal'])
_SERVICEACCOUNTDELEGATIONINFO.fields_by_name['first_party_principal'].containing_oneof = _SERVICEACCOUNTDELEGATIONINFO.oneofs_by_name['Authority']
_SERVICEACCOUNTDELEGATIONINFO.oneofs_by_name['Authority'].fields.append(
  _SERVICEACCOUNTDELEGATIONINFO.fields_by_name['third_party_principal'])
_SERVICEACCOUNTDELEGATIONINFO.fields_by_name['third_party_principal'].containing_oneof = _SERVICEACCOUNTDELEGATIONINFO.oneofs_by_name['Authority']
DESCRIPTOR.message_types_by_name['AuditLog'] = _AUDITLOG
DESCRIPTOR.message_types_by_name['AuthenticationInfo'] = _AUTHENTICATIONINFO
DESCRIPTOR.message_types_by_name['AuthorizationInfo'] = _AUTHORIZATIONINFO
DESCRIPTOR.message_types_by_name['RequestMetadata'] = _REQUESTMETADATA
DESCRIPTOR.message_types_by_name['ResourceLocation'] = _RESOURCELOCATION
DESCRIPTOR.message_types_by_name['ServiceAccountDelegationInfo'] = _SERVICEACCOUNTDELEGATIONINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuditLog = _reflection.GeneratedProtocolMessageType('AuditLog', (_message.Message,), {
  'DESCRIPTOR' : _AUDITLOG,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.AuditLog)
  })
_sym_db.RegisterMessage(AuditLog)

AuthenticationInfo = _reflection.GeneratedProtocolMessageType('AuthenticationInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONINFO,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.AuthenticationInfo)
  })
_sym_db.RegisterMessage(AuthenticationInfo)

AuthorizationInfo = _reflection.GeneratedProtocolMessageType('AuthorizationInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZATIONINFO,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.AuthorizationInfo)
  })
_sym_db.RegisterMessage(AuthorizationInfo)

RequestMetadata = _reflection.GeneratedProtocolMessageType('RequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTMETADATA,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.RequestMetadata)
  })
_sym_db.RegisterMessage(RequestMetadata)

ResourceLocation = _reflection.GeneratedProtocolMessageType('ResourceLocation', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELOCATION,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.ResourceLocation)
  })
_sym_db.RegisterMessage(ResourceLocation)

ServiceAccountDelegationInfo = _reflection.GeneratedProtocolMessageType('ServiceAccountDelegationInfo', (_message.Message,), {

  'FirstPartyPrincipal' : _reflection.GeneratedProtocolMessageType('FirstPartyPrincipal', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEACCOUNTDELEGATIONINFO_FIRSTPARTYPRINCIPAL,
    '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.audit.ServiceAccountDelegationInfo.FirstPartyPrincipal)
    })
  ,

  'ThirdPartyPrincipal' : _reflection.GeneratedProtocolMessageType('ThirdPartyPrincipal', (_message.Message,), {
    'DESCRIPTOR' : _SERVICEACCOUNTDELEGATIONINFO_THIRDPARTYPRINCIPAL,
    '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.audit.ServiceAccountDelegationInfo.ThirdPartyPrincipal)
    })
  ,
  'DESCRIPTOR' : _SERVICEACCOUNTDELEGATIONINFO,
  '__module__' : 'google.cloud.cloud_audit.proto.audit_log_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.audit.ServiceAccountDelegationInfo)
  })
_sym_db.RegisterMessage(ServiceAccountDelegationInfo)
_sym_db.RegisterMessage(ServiceAccountDelegationInfo.FirstPartyPrincipal)
_sym_db.RegisterMessage(ServiceAccountDelegationInfo.ThirdPartyPrincipal)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmi/hw_management_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dmi import commons_pb2 as dmi_dot_commons__pb2
from dmi import hw_pb2 as dmi_dot_hw__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dmi/hw_management_service.proto',
  package='dmi',
  syntax='proto3',
  serialized_options=_b('Z9github.com/opencord/device-management-interface/v3/go/dmi'),
  serialized_pb=_b('\n\x1f\x64mi/hw_management_service.proto\x12\x03\x64mi\x1a\x11\x64mi/commons.proto\x1a\x0c\x64mi/hw.proto\":\n\x18PhysicalInventoryRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\"w\n\x19PhysicalInventoryResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x1b\n\x06reason\x18\x02 \x01(\x0e\x32\x0b.dmi.Reason\x12 \n\tinventory\x18\x03 \x01(\x0b\x32\r.dmi.Hardware\"v\n\x19HWComponentInfoGetRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12!\n\x0e\x63omponent_uuid\x18\x02 \x01(\x0b\x32\t.dmi.Uuid\x12\x16\n\x0e\x63omponent_name\x18\x03 \x01(\t\"\xa1\x01\n\x19HWComponentInfoSetRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12!\n\x0e\x63omponent_uuid\x18\x02 \x01(\x0b\x32\t.dmi.Uuid\x12\x16\n\x0e\x63omponent_name\x18\x03 \x01(\t\x12)\n\x07\x63hanges\x18\x04 \x01(\x0b\x32\x18.dmi.ModifiableComponent\"V\n\x1aHWComponentInfoSetResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x1b\n\x06reason\x18\x02 \x01(\x0e\x32\x0b.dmi.Reason\"w\n\x1bStartManagingDeviceResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x1b\n\x06reason\x18\x02 \x01(\x0e\x32\x0b.dmi.Reason\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x03 \x01(\x0b\x32\t.dmi.Uuid\")\n\x19StopManagingDeviceRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"V\n\x1aStopManagingDeviceResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x1b\n\x06reason\x18\x02 \x01(\x0e\x32\x0b.dmi.Reason2\xbf\x03\n\x19NativeHWManagementService\x12S\n\x13StartManagingDevice\x12\x18.dmi.ModifiableComponent\x1a .dmi.StartManagingDeviceResponse0\x01\x12U\n\x12StopManagingDevice\x12\x1e.dmi.StopManagingDeviceRequest\x1a\x1f.dmi.StopManagingDeviceResponse\x12W\n\x14GetPhysicalInventory\x12\x1d.dmi.PhysicalInventoryRequest\x1a\x1e.dmi.PhysicalInventoryResponse0\x01\x12\x46\n\x12GetHWComponentInfo\x12\x1e.dmi.HWComponentInfoGetRequest\x1a\x0e.dmi.Component0\x01\x12U\n\x12SetHWComponentInfo\x12\x1e.dmi.HWComponentInfoSetRequest\x1a\x1f.dmi.HWComponentInfoSetResponseB;Z9github.com/opencord/device-management-interface/v3/go/dmib\x06proto3')
  ,
  dependencies=[dmi_dot_commons__pb2.DESCRIPTOR,dmi_dot_hw__pb2.DESCRIPTOR,])




_PHYSICALINVENTORYREQUEST = _descriptor.Descriptor(
  name='PhysicalInventoryRequest',
  full_name='dmi.PhysicalInventoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.PhysicalInventoryRequest.device_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=73,
  serialized_end=131,
)


_PHYSICALINVENTORYRESPONSE = _descriptor.Descriptor(
  name='PhysicalInventoryResponse',
  full_name='dmi.PhysicalInventoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.PhysicalInventoryResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.PhysicalInventoryResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inventory', full_name='dmi.PhysicalInventoryResponse.inventory', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=133,
  serialized_end=252,
)


_HWCOMPONENTINFOGETREQUEST = _descriptor.Descriptor(
  name='HWComponentInfoGetRequest',
  full_name='dmi.HWComponentInfoGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.HWComponentInfoGetRequest.device_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_uuid', full_name='dmi.HWComponentInfoGetRequest.component_uuid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_name', full_name='dmi.HWComponentInfoGetRequest.component_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=254,
  serialized_end=372,
)


_HWCOMPONENTINFOSETREQUEST = _descriptor.Descriptor(
  name='HWComponentInfoSetRequest',
  full_name='dmi.HWComponentInfoSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.HWComponentInfoSetRequest.device_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_uuid', full_name='dmi.HWComponentInfoSetRequest.component_uuid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_name', full_name='dmi.HWComponentInfoSetRequest.component_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='changes', full_name='dmi.HWComponentInfoSetRequest.changes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=375,
  serialized_end=536,
)


_HWCOMPONENTINFOSETRESPONSE = _descriptor.Descriptor(
  name='HWComponentInfoSetResponse',
  full_name='dmi.HWComponentInfoSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.HWComponentInfoSetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.HWComponentInfoSetResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=538,
  serialized_end=624,
)


_STARTMANAGINGDEVICERESPONSE = _descriptor.Descriptor(
  name='StartManagingDeviceResponse',
  full_name='dmi.StartManagingDeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.StartManagingDeviceResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.StartManagingDeviceResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.StartManagingDeviceResponse.device_uuid', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=626,
  serialized_end=745,
)


_STOPMANAGINGDEVICEREQUEST = _descriptor.Descriptor(
  name='StopManagingDeviceRequest',
  full_name='dmi.StopManagingDeviceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dmi.StopManagingDeviceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=747,
  serialized_end=788,
)


_STOPMANAGINGDEVICERESPONSE = _descriptor.Descriptor(
  name='StopManagingDeviceResponse',
  full_name='dmi.StopManagingDeviceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.StopManagingDeviceResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.StopManagingDeviceResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=790,
  serialized_end=876,
)

_PHYSICALINVENTORYREQUEST.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_PHYSICALINVENTORYRESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_PHYSICALINVENTORYRESPONSE.fields_by_name['reason'].enum_type = dmi_dot_commons__pb2._REASON
_PHYSICALINVENTORYRESPONSE.fields_by_name['inventory'].message_type = dmi_dot_hw__pb2._HARDWARE
_HWCOMPONENTINFOGETREQUEST.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_HWCOMPONENTINFOGETREQUEST.fields_by_name['component_uuid'].message_type = dmi_dot_hw__pb2._UUID
_HWCOMPONENTINFOSETREQUEST.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_HWCOMPONENTINFOSETREQUEST.fields_by_name['component_uuid'].message_type = dmi_dot_hw__pb2._UUID
_HWCOMPONENTINFOSETREQUEST.fields_by_name['changes'].message_type = dmi_dot_hw__pb2._MODIFIABLECOMPONENT
_HWCOMPONENTINFOSETRESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_HWCOMPONENTINFOSETRESPONSE.fields_by_name['reason'].enum_type = dmi_dot_commons__pb2._REASON
_STARTMANAGINGDEVICERESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_STARTMANAGINGDEVICERESPONSE.fields_by_name['reason'].enum_type = dmi_dot_commons__pb2._REASON
_STARTMANAGINGDEVICERESPONSE.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_STOPMANAGINGDEVICERESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_STOPMANAGINGDEVICERESPONSE.fields_by_name['reason'].enum_type = dmi_dot_commons__pb2._REASON
DESCRIPTOR.message_types_by_name['PhysicalInventoryRequest'] = _PHYSICALINVENTORYREQUEST
DESCRIPTOR.message_types_by_name['PhysicalInventoryResponse'] = _PHYSICALINVENTORYRESPONSE
DESCRIPTOR.message_types_by_name['HWComponentInfoGetRequest'] = _HWCOMPONENTINFOGETREQUEST
DESCRIPTOR.message_types_by_name['HWComponentInfoSetRequest'] = _HWCOMPONENTINFOSETREQUEST
DESCRIPTOR.message_types_by_name['HWComponentInfoSetResponse'] = _HWCOMPONENTINFOSETRESPONSE
DESCRIPTOR.message_types_by_name['StartManagingDeviceResponse'] = _STARTMANAGINGDEVICERESPONSE
DESCRIPTOR.message_types_by_name['StopManagingDeviceRequest'] = _STOPMANAGINGDEVICEREQUEST
DESCRIPTOR.message_types_by_name['StopManagingDeviceResponse'] = _STOPMANAGINGDEVICERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PhysicalInventoryRequest = _reflection.GeneratedProtocolMessageType('PhysicalInventoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _PHYSICALINVENTORYREQUEST,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PhysicalInventoryRequest)
  ))
_sym_db.RegisterMessage(PhysicalInventoryRequest)

PhysicalInventoryResponse = _reflection.GeneratedProtocolMessageType('PhysicalInventoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _PHYSICALINVENTORYRESPONSE,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PhysicalInventoryResponse)
  ))
_sym_db.RegisterMessage(PhysicalInventoryResponse)

HWComponentInfoGetRequest = _reflection.GeneratedProtocolMessageType('HWComponentInfoGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _HWCOMPONENTINFOGETREQUEST,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.HWComponentInfoGetRequest)
  ))
_sym_db.RegisterMessage(HWComponentInfoGetRequest)

HWComponentInfoSetRequest = _reflection.GeneratedProtocolMessageType('HWComponentInfoSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _HWCOMPONENTINFOSETREQUEST,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.HWComponentInfoSetRequest)
  ))
_sym_db.RegisterMessage(HWComponentInfoSetRequest)

HWComponentInfoSetResponse = _reflection.GeneratedProtocolMessageType('HWComponentInfoSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _HWCOMPONENTINFOSETRESPONSE,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.HWComponentInfoSetResponse)
  ))
_sym_db.RegisterMessage(HWComponentInfoSetResponse)

StartManagingDeviceResponse = _reflection.GeneratedProtocolMessageType('StartManagingDeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _STARTMANAGINGDEVICERESPONSE,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.StartManagingDeviceResponse)
  ))
_sym_db.RegisterMessage(StartManagingDeviceResponse)

StopManagingDeviceRequest = _reflection.GeneratedProtocolMessageType('StopManagingDeviceRequest', (_message.Message,), dict(
  DESCRIPTOR = _STOPMANAGINGDEVICEREQUEST,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.StopManagingDeviceRequest)
  ))
_sym_db.RegisterMessage(StopManagingDeviceRequest)

StopManagingDeviceResponse = _reflection.GeneratedProtocolMessageType('StopManagingDeviceResponse', (_message.Message,), dict(
  DESCRIPTOR = _STOPMANAGINGDEVICERESPONSE,
  __module__ = 'dmi.hw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.StopManagingDeviceResponse)
  ))
_sym_db.RegisterMessage(StopManagingDeviceResponse)


DESCRIPTOR._options = None

_NATIVEHWMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='NativeHWManagementService',
  full_name='dmi.NativeHWManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=879,
  serialized_end=1326,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartManagingDevice',
    full_name='dmi.NativeHWManagementService.StartManagingDevice',
    index=0,
    containing_service=None,
    input_type=dmi_dot_hw__pb2._MODIFIABLECOMPONENT,
    output_type=_STARTMANAGINGDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopManagingDevice',
    full_name='dmi.NativeHWManagementService.StopManagingDevice',
    index=1,
    containing_service=None,
    input_type=_STOPMANAGINGDEVICEREQUEST,
    output_type=_STOPMANAGINGDEVICERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPhysicalInventory',
    full_name='dmi.NativeHWManagementService.GetPhysicalInventory',
    index=2,
    containing_service=None,
    input_type=_PHYSICALINVENTORYREQUEST,
    output_type=_PHYSICALINVENTORYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetHWComponentInfo',
    full_name='dmi.NativeHWManagementService.GetHWComponentInfo',
    index=3,
    containing_service=None,
    input_type=_HWCOMPONENTINFOGETREQUEST,
    output_type=dmi_dot_hw__pb2._COMPONENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetHWComponentInfo',
    full_name='dmi.NativeHWManagementService.SetHWComponentInfo',
    index=4,
    containing_service=None,
    input_type=_HWCOMPONENTINFOSETREQUEST,
    output_type=_HWCOMPONENTINFOSETRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NATIVEHWMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['NativeHWManagementService'] = _NATIVEHWMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)

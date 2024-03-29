# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmi/sw_management_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dmi import commons_pb2 as dmi_dot_commons__pb2
from dmi import hw_pb2 as dmi_dot_hw__pb2
from dmi import sw_image_pb2 as dmi_dot_sw__image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x64mi/sw_management_service.proto\x12\x03\x64mi\x1a\x11\x64mi/commons.proto\x1a\x0c\x64mi/hw.proto\x1a\x12\x64mi/sw_image.proto\"u\n\x1aSoftwareVersionInformation\x12*\n\x0f\x61\x63tive_versions\x18\x01 \x03(\x0b\x32\x11.dmi.ImageVersion\x12+\n\x10standby_versions\x18\x02 \x03(\x0b\x32\x11.dmi.ImageVersion\"\xad\x02\n%GetSoftwareVersionInformationResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x41\n\x06reason\x18\x02 \x01(\x0e\x32\x31.dmi.GetSoftwareVersionInformationResponse.Reason\x12-\n\x04info\x18\x03 \x01(\x0b\x32\x1f.dmi.SoftwareVersionInformation\x12\x15\n\rreason_detail\x18\x04 \x01(\t\"^\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x03\"a\n\x14\x44ownloadImageRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12)\n\nimage_info\x18\x02 \x01(\x0b\x32\x15.dmi.ImageInformation\"C\n\rConfigRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12\x12\n\nconfig_url\x18\x02 \x01(\t\"\xa3\x02\n\x0e\x43onfigResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12*\n\x06reason\x18\x02 \x01(\x0e\x32\x1a.dmi.ConfigResponse.Reason\x12\x15\n\rreason_detail\x18\x03 \x01(\t\"\xb0\x01\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x19\n\x15\x45RROR_FETCHING_CONFIG\x10\x03\x12\x12\n\x0eINVALID_CONFIG\x10\x04\x12!\n\x1dOPERATION_ALREADY_IN_PROGRESS\x10\x05\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x06\":\n\x18StartupConfigInfoRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\"\x8b\x02\n\x19StartupConfigInfoResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x35\n\x06reason\x18\x02 \x01(\x0e\x32%.dmi.StartupConfigInfoResponse.Reason\x12\x12\n\nconfig_url\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\t\x12\x15\n\rreason_detail\x18\x05 \x01(\t\"^\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x03\"N\n\x16UploadDebugInfoRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12\x14\n\x0clocation_url\x18\x03 \x01(\t\"\xe6\x04\n\x15UploadDebugInfoStatus\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12\x37\n\x06status\x18\x02 \x01(\x0e\x32\'.dmi.UploadDebugInfoStatus.UploadStatus\x12\x18\n\x10percent_uploaded\x18\x03 \x01(\x05\x12\x31\n\x06reason\x18\x04 \x01(\x0e\x32!.dmi.UploadDebugInfoStatus.Reason\x12\x14\n\x0clocation_url\x18\x05 \x01(\t\x12\x11\n\tfile_name\x18\x06 \x01(\t\"U\n\x0cUploadStatus\x12\x1b\n\x17UNDEFINED_UPLOAD_STATUS\x10\x00\x12\x0c\n\x08\x43OMPLETE\x10\x01\x12\x0f\n\x0bIN_PROGRESS\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"\xa6\x02\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x18\n\x14\x44\x45VICE_NOT_REACHABLE\x10\x03\x12\x1f\n\x1bREMOTE_LOCATION_UNREACHABLE\x10\x04\x12%\n!REMOTE_LOCATION_PERMISSION_DENIED\x10\x05\x12\x17\n\x13\x45RROR_DURING_UPLOAD\x10\x06\x12\x0f\n\x0b\x44\x45VICE_BUSY\x10\x07\x12\x14\n\x10\x45RROR_IN_REQUEST\x10\x08\x12\x19\n\x15\x44\x45VICE_IN_WRONG_STATE\x10\t\x12!\n\x1dOPERATION_ALREADY_IN_PROGRESS\x10\n2\x9c\x04\n\x1fNativeSoftwareManagementService\x12Q\n\x12GetSoftwareVersion\x12\x0f.dmi.HardwareID\x1a*.dmi.GetSoftwareVersionInformationResponse\x12>\n\rDownloadImage\x12\x19.dmi.DownloadImageRequest\x1a\x10.dmi.ImageStatus0\x01\x12\x34\n\rActivateImage\x12\x0f.dmi.HardwareID\x1a\x10.dmi.ImageStatus0\x01\x12;\n\x14RevertToStandbyImage\x12\x0f.dmi.HardwareID\x1a\x10.dmi.ImageStatus0\x01\x12G\n\x1aUpdateStartupConfiguration\x12\x12.dmi.ConfigRequest\x1a\x13.dmi.ConfigResponse0\x01\x12\\\n\x1bGetStartupConfigurationInfo\x12\x1d.dmi.StartupConfigInfoRequest\x1a\x1e.dmi.StartupConfigInfoResponse\x12L\n\x0fUploadDebugInfo\x12\x1b.dmi.UploadDebugInfoRequest\x1a\x1a.dmi.UploadDebugInfoStatus0\x01\x42;Z9github.com/opencord/device-management-interface/v3/go/dmib\x06proto3')



_SOFTWAREVERSIONINFORMATION = DESCRIPTOR.message_types_by_name['SoftwareVersionInformation']
_GETSOFTWAREVERSIONINFORMATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetSoftwareVersionInformationResponse']
_DOWNLOADIMAGEREQUEST = DESCRIPTOR.message_types_by_name['DownloadImageRequest']
_CONFIGREQUEST = DESCRIPTOR.message_types_by_name['ConfigRequest']
_CONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ConfigResponse']
_STARTUPCONFIGINFOREQUEST = DESCRIPTOR.message_types_by_name['StartupConfigInfoRequest']
_STARTUPCONFIGINFORESPONSE = DESCRIPTOR.message_types_by_name['StartupConfigInfoResponse']
_UPLOADDEBUGINFOREQUEST = DESCRIPTOR.message_types_by_name['UploadDebugInfoRequest']
_UPLOADDEBUGINFOSTATUS = DESCRIPTOR.message_types_by_name['UploadDebugInfoStatus']
_GETSOFTWAREVERSIONINFORMATIONRESPONSE_REASON = _GETSOFTWAREVERSIONINFORMATIONRESPONSE.enum_types_by_name['Reason']
_CONFIGRESPONSE_REASON = _CONFIGRESPONSE.enum_types_by_name['Reason']
_STARTUPCONFIGINFORESPONSE_REASON = _STARTUPCONFIGINFORESPONSE.enum_types_by_name['Reason']
_UPLOADDEBUGINFOSTATUS_UPLOADSTATUS = _UPLOADDEBUGINFOSTATUS.enum_types_by_name['UploadStatus']
_UPLOADDEBUGINFOSTATUS_REASON = _UPLOADDEBUGINFOSTATUS.enum_types_by_name['Reason']
SoftwareVersionInformation = _reflection.GeneratedProtocolMessageType('SoftwareVersionInformation', (_message.Message,), {
  'DESCRIPTOR' : _SOFTWAREVERSIONINFORMATION,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.SoftwareVersionInformation)
  })
_sym_db.RegisterMessage(SoftwareVersionInformation)

GetSoftwareVersionInformationResponse = _reflection.GeneratedProtocolMessageType('GetSoftwareVersionInformationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSOFTWAREVERSIONINFORMATIONRESPONSE,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.GetSoftwareVersionInformationResponse)
  })
_sym_db.RegisterMessage(GetSoftwareVersionInformationResponse)

DownloadImageRequest = _reflection.GeneratedProtocolMessageType('DownloadImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADIMAGEREQUEST,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.DownloadImageRequest)
  })
_sym_db.RegisterMessage(DownloadImageRequest)

ConfigRequest = _reflection.GeneratedProtocolMessageType('ConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGREQUEST,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ConfigRequest)
  })
_sym_db.RegisterMessage(ConfigRequest)

ConfigResponse = _reflection.GeneratedProtocolMessageType('ConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGRESPONSE,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ConfigResponse)
  })
_sym_db.RegisterMessage(ConfigResponse)

StartupConfigInfoRequest = _reflection.GeneratedProtocolMessageType('StartupConfigInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTUPCONFIGINFOREQUEST,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.StartupConfigInfoRequest)
  })
_sym_db.RegisterMessage(StartupConfigInfoRequest)

StartupConfigInfoResponse = _reflection.GeneratedProtocolMessageType('StartupConfigInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTUPCONFIGINFORESPONSE,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.StartupConfigInfoResponse)
  })
_sym_db.RegisterMessage(StartupConfigInfoResponse)

UploadDebugInfoRequest = _reflection.GeneratedProtocolMessageType('UploadDebugInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADDEBUGINFOREQUEST,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.UploadDebugInfoRequest)
  })
_sym_db.RegisterMessage(UploadDebugInfoRequest)

UploadDebugInfoStatus = _reflection.GeneratedProtocolMessageType('UploadDebugInfoStatus', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADDEBUGINFOSTATUS,
  '__module__' : 'dmi.sw_management_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.UploadDebugInfoStatus)
  })
_sym_db.RegisterMessage(UploadDebugInfoStatus)

_NATIVESOFTWAREMANAGEMENTSERVICE = DESCRIPTOR.services_by_name['NativeSoftwareManagementService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/opencord/device-management-interface/v3/go/dmi'
  _SOFTWAREVERSIONINFORMATION._serialized_start=93
  _SOFTWAREVERSIONINFORMATION._serialized_end=210
  _GETSOFTWAREVERSIONINFORMATIONRESPONSE._serialized_start=213
  _GETSOFTWAREVERSIONINFORMATIONRESPONSE._serialized_end=514
  _GETSOFTWAREVERSIONINFORMATIONRESPONSE_REASON._serialized_start=420
  _GETSOFTWAREVERSIONINFORMATIONRESPONSE_REASON._serialized_end=514
  _DOWNLOADIMAGEREQUEST._serialized_start=516
  _DOWNLOADIMAGEREQUEST._serialized_end=613
  _CONFIGREQUEST._serialized_start=615
  _CONFIGREQUEST._serialized_end=682
  _CONFIGRESPONSE._serialized_start=685
  _CONFIGRESPONSE._serialized_end=976
  _CONFIGRESPONSE_REASON._serialized_start=800
  _CONFIGRESPONSE_REASON._serialized_end=976
  _STARTUPCONFIGINFOREQUEST._serialized_start=978
  _STARTUPCONFIGINFOREQUEST._serialized_end=1036
  _STARTUPCONFIGINFORESPONSE._serialized_start=1039
  _STARTUPCONFIGINFORESPONSE._serialized_end=1306
  _STARTUPCONFIGINFORESPONSE_REASON._serialized_start=420
  _STARTUPCONFIGINFORESPONSE_REASON._serialized_end=514
  _UPLOADDEBUGINFOREQUEST._serialized_start=1308
  _UPLOADDEBUGINFOREQUEST._serialized_end=1386
  _UPLOADDEBUGINFOSTATUS._serialized_start=1389
  _UPLOADDEBUGINFOSTATUS._serialized_end=2003
  _UPLOADDEBUGINFOSTATUS_UPLOADSTATUS._serialized_start=1621
  _UPLOADDEBUGINFOSTATUS_UPLOADSTATUS._serialized_end=1706
  _UPLOADDEBUGINFOSTATUS_REASON._serialized_start=1709
  _UPLOADDEBUGINFOSTATUS_REASON._serialized_end=2003
  _NATIVESOFTWAREMANAGEMENTSERVICE._serialized_start=2006
  _NATIVESOFTWAREMANAGEMENTSERVICE._serialized_end=2546
# @@protoc_insertion_point(module_scope)

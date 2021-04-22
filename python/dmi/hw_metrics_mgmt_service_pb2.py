# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmi/hw_metrics_mgmt_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dmi import commons_pb2 as dmi_dot_commons__pb2
from dmi import hw_pb2 as dmi_dot_hw__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dmi/hw_metrics_mgmt_service.proto',
  package='dmi',
  syntax='proto3',
  serialized_options=b'Z9github.com/opencord/device-management-interface/v3/go/dmi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!dmi/hw_metrics_mgmt_service.proto\x12\x03\x64mi\x1a\x11\x64mi/commons.proto\x1a\x0c\x64mi/hw.proto\x1a\x1bgoogle/protobuf/empty.proto\"a\n\x0cMetricConfig\x12#\n\tmetric_id\x18\x01 \x01(\x0e\x32\x10.dmi.MetricNames\x12\x15\n\ris_configured\x18\x02 \x01(\x08\x12\x15\n\rpoll_interval\x18\x03 \x01(\r\"3\n\rMetricsConfig\x12\"\n\x07metrics\x18\x01 \x03(\x0b\x32\x11.dmi.MetricConfig\"\xff\x01\n\x13ListMetricsResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12/\n\x06reason\x18\x02 \x01(\x0e\x32\x1f.dmi.ListMetricsResponse.Reason\x12#\n\x07metrics\x18\x03 \x01(\x0b\x32\x12.dmi.MetricsConfig\x12\x15\n\rreason_detail\x18\x04 \x01(\t\"^\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x03\"\x8d\x01\n\x1bMetricsConfigurationRequest\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12%\n\x07\x63hanges\x18\x02 \x01(\x0b\x32\x12.dmi.MetricsConfigH\x00\x12\x1a\n\x10reset_to_default\x18\x03 \x01(\x08H\x00\x42\x0b\n\toperation\"\xa0\x02\n\x1cMetricsConfigurationResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12\x38\n\x06reason\x18\x02 \x01(\x0e\x32(.dmi.MetricsConfigurationResponse.Reason\x12\x15\n\rreason_detail\x18\x03 \x01(\t\"\x91\x01\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x1d\n\x19POLL_INTERVAL_UNSUPPORTED\x10\x03\x12\x12\n\x0eINVALID_METRIC\x10\x04\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x05\"k\n\x0eMetricMetaData\x12\x1e\n\x0b\x64\x65vice_uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\x12!\n\x0e\x63omponent_uuid\x18\x02 \x01(\x0b\x32\t.dmi.Uuid\x12\x16\n\x0e\x63omponent_name\x18\x03 \x01(\t\"\x84\x01\n\x06Metric\x12#\n\tmetric_id\x18\x01 \x01(\x0e\x32\x10.dmi.MetricNames\x12,\n\x0fmetric_metadata\x18\x02 \x01(\x0b\x32\x13.dmi.MetricMetaData\x12\'\n\x05value\x18\x03 \x01(\x0b\x32\x18.dmi.ComponentSensorData\"_\n\x10GetMetricRequest\x12&\n\tmeta_data\x18\x01 \x01(\x0b\x32\x13.dmi.MetricMetaData\x12#\n\tmetric_id\x18\x02 \x01(\x0e\x32\x10.dmi.MetricNames\"\x9f\x02\n\x11GetMetricResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.dmi.Status\x12-\n\x06reason\x18\x02 \x01(\x0e\x32\x1d.dmi.GetMetricResponse.Reason\x12\x1b\n\x06metric\x18\x03 \x01(\x0b\x32\x0b.dmi.Metric\x12\x15\n\rreason_detail\x18\x04 \x01(\t\"\x89\x01\n\x06Reason\x12\x14\n\x10UNDEFINED_REASON\x10\x00\x12\x12\n\x0eUNKNOWN_DEVICE\x10\x01\x12\x15\n\x11UNKNOWN_COMPONENT\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\x12\x12\n\x0eINVALID_METRIC\x10\x04\x12\x16\n\x12\x44\x45VICE_UNREACHABLE\x10\x05*\xd9\x05\n\x0bMetricNames\x12\x19\n\x15METRIC_NAME_UNDEFINED\x10\x00\x12\x14\n\x10METRIC_FAN_SPEED\x10\x01\x12\x13\n\x0fMETRIC_CPU_TEMP\x10\x64\x12\x1f\n\x1bMETRIC_CPU_USAGE_PERCENTAGE\x10\x65\x12\x1c\n\x17METRIC_TRANSCEIVER_TEMP\x10\xc8\x01\x12\x1f\n\x1aMETRIC_TRANSCEIVER_VOLTAGE\x10\xc9\x01\x12\x1c\n\x17METRIC_TRANSCEIVER_BIAS\x10\xca\x01\x12 \n\x1bMETRIC_TRANSCEIVER_RX_POWER\x10\xcb\x01\x12 \n\x1bMETRIC_TRANSCEIVER_TX_POWER\x10\xcc\x01\x12\"\n\x1dMETRIC_TRANSCEIVER_WAVELENGTH\x10\xcd\x01\x12\x15\n\x10METRIC_DISK_TEMP\x10\xac\x02\x12\x19\n\x14METRIC_DISK_CAPACITY\x10\xad\x02\x12\x16\n\x11METRIC_DISK_USAGE\x10\xae\x02\x12!\n\x1cMETRIC_DISK_USAGE_PERCENTAGE\x10\xaf\x02\x12&\n!METRIC_DISK_READ_WRITE_PERCENTAGE\x10\xb0\x02\x12(\n#METRIC_DISK_FAULTY_CELLS_PERCENTAGE\x10\xb1\x02\x12\x14\n\x0fMETRIC_RAM_TEMP\x10\x90\x03\x12\x18\n\x13METRIC_RAM_CAPACITY\x10\x91\x03\x12\x15\n\x10METRIC_RAM_USAGE\x10\x92\x03\x12 \n\x1bMETRIC_RAM_USAGE_PERCENTAGE\x10\x93\x03\x12\x15\n\x10METRIC_POWER_MAX\x10\xf4\x03\x12\x17\n\x12METRIC_POWER_USAGE\x10\xf5\x03\x12\"\n\x1dMETRIC_POWER_USAGE_PERCENTAGE\x10\xf6\x03\x12\"\n\x1dMETRIC_INNER_SURROUNDING_TEMP\x10\xd8\x04\x32\xb1\x02\n\x1eNativeMetricsManagementService\x12\x38\n\x0bListMetrics\x12\x0f.dmi.HardwareID\x1a\x18.dmi.ListMetricsResponse\x12\x61\n\x1aUpdateMetricsConfiguration\x12 .dmi.MetricsConfigurationRequest\x1a!.dmi.MetricsConfigurationResponse\x12:\n\tGetMetric\x12\x15.dmi.GetMetricRequest\x1a\x16.dmi.GetMetricResponse\x12\x36\n\rStreamMetrics\x12\x16.google.protobuf.Empty\x1a\x0b.dmi.Metric0\x01\x42;Z9github.com/opencord/device-management-interface/v3/go/dmib\x06proto3'
  ,
  dependencies=[dmi_dot_commons__pb2.DESCRIPTOR,dmi_dot_hw__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_METRICNAMES = _descriptor.EnumDescriptor(
  name='MetricNames',
  full_name='dmi.MetricNames',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='METRIC_NAME_UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_FAN_SPEED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_CPU_TEMP', index=2, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_CPU_USAGE_PERCENTAGE', index=3, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_TEMP', index=4, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_VOLTAGE', index=5, number=201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_BIAS', index=6, number=202,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_RX_POWER', index=7, number=203,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_TX_POWER', index=8, number=204,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_TRANSCEIVER_WAVELENGTH', index=9, number=205,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_TEMP', index=10, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_CAPACITY', index=11, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_USAGE', index=12, number=302,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_USAGE_PERCENTAGE', index=13, number=303,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_READ_WRITE_PERCENTAGE', index=14, number=304,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_DISK_FAULTY_CELLS_PERCENTAGE', index=15, number=305,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_RAM_TEMP', index=16, number=400,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_RAM_CAPACITY', index=17, number=401,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_RAM_USAGE', index=18, number=402,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_RAM_USAGE_PERCENTAGE', index=19, number=403,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_POWER_MAX', index=20, number=500,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_POWER_USAGE', index=21, number=501,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_POWER_USAGE_PERCENTAGE', index=22, number=502,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METRIC_INNER_SURROUNDING_TEMP', index=23, number=600,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1581,
  serialized_end=2310,
)
_sym_db.RegisterEnumDescriptor(_METRICNAMES)

MetricNames = enum_type_wrapper.EnumTypeWrapper(_METRICNAMES)
METRIC_NAME_UNDEFINED = 0
METRIC_FAN_SPEED = 1
METRIC_CPU_TEMP = 100
METRIC_CPU_USAGE_PERCENTAGE = 101
METRIC_TRANSCEIVER_TEMP = 200
METRIC_TRANSCEIVER_VOLTAGE = 201
METRIC_TRANSCEIVER_BIAS = 202
METRIC_TRANSCEIVER_RX_POWER = 203
METRIC_TRANSCEIVER_TX_POWER = 204
METRIC_TRANSCEIVER_WAVELENGTH = 205
METRIC_DISK_TEMP = 300
METRIC_DISK_CAPACITY = 301
METRIC_DISK_USAGE = 302
METRIC_DISK_USAGE_PERCENTAGE = 303
METRIC_DISK_READ_WRITE_PERCENTAGE = 304
METRIC_DISK_FAULTY_CELLS_PERCENTAGE = 305
METRIC_RAM_TEMP = 400
METRIC_RAM_CAPACITY = 401
METRIC_RAM_USAGE = 402
METRIC_RAM_USAGE_PERCENTAGE = 403
METRIC_POWER_MAX = 500
METRIC_POWER_USAGE = 501
METRIC_POWER_USAGE_PERCENTAGE = 502
METRIC_INNER_SURROUNDING_TEMP = 600


_LISTMETRICSRESPONSE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='dmi.ListMetricsResponse.Reason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REASON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DEVICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_UNREACHABLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=418,
  serialized_end=512,
)
_sym_db.RegisterEnumDescriptor(_LISTMETRICSRESPONSE_REASON)

_METRICSCONFIGURATIONRESPONSE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='dmi.MetricsConfigurationResponse.Reason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REASON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DEVICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POLL_INTERVAL_UNSUPPORTED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_METRIC', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_UNREACHABLE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=802,
  serialized_end=947,
)
_sym_db.RegisterEnumDescriptor(_METRICSCONFIGURATIONRESPONSE_REASON)

_GETMETRICRESPONSE_REASON = _descriptor.EnumDescriptor(
  name='Reason',
  full_name='dmi.GetMetricResponse.Reason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_REASON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_DEVICE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_COMPONENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_METRIC', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_UNREACHABLE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1441,
  serialized_end=1578,
)
_sym_db.RegisterEnumDescriptor(_GETMETRICRESPONSE_REASON)


_METRICCONFIG = _descriptor.Descriptor(
  name='MetricConfig',
  full_name='dmi.MetricConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_id', full_name='dmi.MetricConfig.metric_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_configured', full_name='dmi.MetricConfig.is_configured', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='poll_interval', full_name='dmi.MetricConfig.poll_interval', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=104,
  serialized_end=201,
)


_METRICSCONFIG = _descriptor.Descriptor(
  name='MetricsConfig',
  full_name='dmi.MetricsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='dmi.MetricsConfig.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=203,
  serialized_end=254,
)


_LISTMETRICSRESPONSE = _descriptor.Descriptor(
  name='ListMetricsResponse',
  full_name='dmi.ListMetricsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.ListMetricsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.ListMetricsResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='dmi.ListMetricsResponse.metrics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason_detail', full_name='dmi.ListMetricsResponse.reason_detail', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTMETRICSRESPONSE_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=512,
)


_METRICSCONFIGURATIONREQUEST = _descriptor.Descriptor(
  name='MetricsConfigurationRequest',
  full_name='dmi.MetricsConfigurationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.MetricsConfigurationRequest.device_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changes', full_name='dmi.MetricsConfigurationRequest.changes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reset_to_default', full_name='dmi.MetricsConfigurationRequest.reset_to_default', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='dmi.MetricsConfigurationRequest.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=515,
  serialized_end=656,
)


_METRICSCONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='MetricsConfigurationResponse',
  full_name='dmi.MetricsConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.MetricsConfigurationResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.MetricsConfigurationResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason_detail', full_name='dmi.MetricsConfigurationResponse.reason_detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METRICSCONFIGURATIONRESPONSE_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=947,
)


_METRICMETADATA = _descriptor.Descriptor(
  name='MetricMetaData',
  full_name='dmi.MetricMetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_uuid', full_name='dmi.MetricMetaData.device_uuid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='component_uuid', full_name='dmi.MetricMetaData.component_uuid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='component_name', full_name='dmi.MetricMetaData.component_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=949,
  serialized_end=1056,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='dmi.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metric_id', full_name='dmi.Metric.metric_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_metadata', full_name='dmi.Metric.metric_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dmi.Metric.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1059,
  serialized_end=1191,
)


_GETMETRICREQUEST = _descriptor.Descriptor(
  name='GetMetricRequest',
  full_name='dmi.GetMetricRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='dmi.GetMetricRequest.meta_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric_id', full_name='dmi.GetMetricRequest.metric_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1193,
  serialized_end=1288,
)


_GETMETRICRESPONSE = _descriptor.Descriptor(
  name='GetMetricResponse',
  full_name='dmi.GetMetricResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dmi.GetMetricResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='dmi.GetMetricResponse.reason', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metric', full_name='dmi.GetMetricResponse.metric', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason_detail', full_name='dmi.GetMetricResponse.reason_detail', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETMETRICRESPONSE_REASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1291,
  serialized_end=1578,
)

_METRICCONFIG.fields_by_name['metric_id'].enum_type = _METRICNAMES
_METRICSCONFIG.fields_by_name['metrics'].message_type = _METRICCONFIG
_LISTMETRICSRESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_LISTMETRICSRESPONSE.fields_by_name['reason'].enum_type = _LISTMETRICSRESPONSE_REASON
_LISTMETRICSRESPONSE.fields_by_name['metrics'].message_type = _METRICSCONFIG
_LISTMETRICSRESPONSE_REASON.containing_type = _LISTMETRICSRESPONSE
_METRICSCONFIGURATIONREQUEST.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_METRICSCONFIGURATIONREQUEST.fields_by_name['changes'].message_type = _METRICSCONFIG
_METRICSCONFIGURATIONREQUEST.oneofs_by_name['operation'].fields.append(
  _METRICSCONFIGURATIONREQUEST.fields_by_name['changes'])
_METRICSCONFIGURATIONREQUEST.fields_by_name['changes'].containing_oneof = _METRICSCONFIGURATIONREQUEST.oneofs_by_name['operation']
_METRICSCONFIGURATIONREQUEST.oneofs_by_name['operation'].fields.append(
  _METRICSCONFIGURATIONREQUEST.fields_by_name['reset_to_default'])
_METRICSCONFIGURATIONREQUEST.fields_by_name['reset_to_default'].containing_oneof = _METRICSCONFIGURATIONREQUEST.oneofs_by_name['operation']
_METRICSCONFIGURATIONRESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_METRICSCONFIGURATIONRESPONSE.fields_by_name['reason'].enum_type = _METRICSCONFIGURATIONRESPONSE_REASON
_METRICSCONFIGURATIONRESPONSE_REASON.containing_type = _METRICSCONFIGURATIONRESPONSE
_METRICMETADATA.fields_by_name['device_uuid'].message_type = dmi_dot_hw__pb2._UUID
_METRICMETADATA.fields_by_name['component_uuid'].message_type = dmi_dot_hw__pb2._UUID
_METRIC.fields_by_name['metric_id'].enum_type = _METRICNAMES
_METRIC.fields_by_name['metric_metadata'].message_type = _METRICMETADATA
_METRIC.fields_by_name['value'].message_type = dmi_dot_hw__pb2._COMPONENTSENSORDATA
_GETMETRICREQUEST.fields_by_name['meta_data'].message_type = _METRICMETADATA
_GETMETRICREQUEST.fields_by_name['metric_id'].enum_type = _METRICNAMES
_GETMETRICRESPONSE.fields_by_name['status'].enum_type = dmi_dot_commons__pb2._STATUS
_GETMETRICRESPONSE.fields_by_name['reason'].enum_type = _GETMETRICRESPONSE_REASON
_GETMETRICRESPONSE.fields_by_name['metric'].message_type = _METRIC
_GETMETRICRESPONSE_REASON.containing_type = _GETMETRICRESPONSE
DESCRIPTOR.message_types_by_name['MetricConfig'] = _METRICCONFIG
DESCRIPTOR.message_types_by_name['MetricsConfig'] = _METRICSCONFIG
DESCRIPTOR.message_types_by_name['ListMetricsResponse'] = _LISTMETRICSRESPONSE
DESCRIPTOR.message_types_by_name['MetricsConfigurationRequest'] = _METRICSCONFIGURATIONREQUEST
DESCRIPTOR.message_types_by_name['MetricsConfigurationResponse'] = _METRICSCONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['MetricMetaData'] = _METRICMETADATA
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['GetMetricRequest'] = _GETMETRICREQUEST
DESCRIPTOR.message_types_by_name['GetMetricResponse'] = _GETMETRICRESPONSE
DESCRIPTOR.enum_types_by_name['MetricNames'] = _METRICNAMES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetricConfig = _reflection.GeneratedProtocolMessageType('MetricConfig', (_message.Message,), {
  'DESCRIPTOR' : _METRICCONFIG,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.MetricConfig)
  })
_sym_db.RegisterMessage(MetricConfig)

MetricsConfig = _reflection.GeneratedProtocolMessageType('MetricsConfig', (_message.Message,), {
  'DESCRIPTOR' : _METRICSCONFIG,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.MetricsConfig)
  })
_sym_db.RegisterMessage(MetricsConfig)

ListMetricsResponse = _reflection.GeneratedProtocolMessageType('ListMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTMETRICSRESPONSE,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ListMetricsResponse)
  })
_sym_db.RegisterMessage(ListMetricsResponse)

MetricsConfigurationRequest = _reflection.GeneratedProtocolMessageType('MetricsConfigurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _METRICSCONFIGURATIONREQUEST,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.MetricsConfigurationRequest)
  })
_sym_db.RegisterMessage(MetricsConfigurationRequest)

MetricsConfigurationResponse = _reflection.GeneratedProtocolMessageType('MetricsConfigurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _METRICSCONFIGURATIONRESPONSE,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.MetricsConfigurationResponse)
  })
_sym_db.RegisterMessage(MetricsConfigurationResponse)

MetricMetaData = _reflection.GeneratedProtocolMessageType('MetricMetaData', (_message.Message,), {
  'DESCRIPTOR' : _METRICMETADATA,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.MetricMetaData)
  })
_sym_db.RegisterMessage(MetricMetaData)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.Metric)
  })
_sym_db.RegisterMessage(Metric)

GetMetricRequest = _reflection.GeneratedProtocolMessageType('GetMetricRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICREQUEST,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.GetMetricRequest)
  })
_sym_db.RegisterMessage(GetMetricRequest)

GetMetricResponse = _reflection.GeneratedProtocolMessageType('GetMetricResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMETRICRESPONSE,
  '__module__' : 'dmi.hw_metrics_mgmt_service_pb2'
  # @@protoc_insertion_point(class_scope:dmi.GetMetricResponse)
  })
_sym_db.RegisterMessage(GetMetricResponse)


DESCRIPTOR._options = None

_NATIVEMETRICSMANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='NativeMetricsManagementService',
  full_name='dmi.NativeMetricsManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=2313,
  serialized_end=2618,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListMetrics',
    full_name='dmi.NativeMetricsManagementService.ListMetrics',
    index=0,
    containing_service=None,
    input_type=dmi_dot_hw__pb2._HARDWAREID,
    output_type=_LISTMETRICSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateMetricsConfiguration',
    full_name='dmi.NativeMetricsManagementService.UpdateMetricsConfiguration',
    index=1,
    containing_service=None,
    input_type=_METRICSCONFIGURATIONREQUEST,
    output_type=_METRICSCONFIGURATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMetric',
    full_name='dmi.NativeMetricsManagementService.GetMetric',
    index=2,
    containing_service=None,
    input_type=_GETMETRICREQUEST,
    output_type=_GETMETRICRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamMetrics',
    full_name='dmi.NativeMetricsManagementService.StreamMetrics',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_METRIC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NATIVEMETRICSMANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['NativeMetricsManagementService'] = _NATIVEMETRICSMANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)

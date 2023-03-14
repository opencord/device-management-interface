# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dmi/hw.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x64mi/hw.proto\x12\x03\x64mi\x1a\x1fgoogle/protobuf/timestamp.proto\"\x14\n\x04Uuid\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"%\n\nHardwareID\x12\x17\n\x04uuid\x18\x01 \x01(\x0b\x32\t.dmi.Uuid\"\x12\n\x03Uri\x12\x0b\n\x03uri\x18\x01 \x01(\t\"\xb5\x02\n\x0e\x43omponentState\x12\x36\n\x12state_last_changed\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x0b\x61\x64min_state\x18\x02 \x01(\x0e\x32\x18.dmi.ComponentAdminState\x12+\n\noper_state\x18\x03 \x01(\x0e\x32\x17.dmi.ComponentOperState\x12-\n\x0busage_state\x18\x04 \x01(\x0e\x32\x18.dmi.ComponentUsageState\x12-\n\x0b\x61larm_state\x18\x05 \x01(\x0e\x32\x18.dmi.ComponentAlarmState\x12\x31\n\rstandby_state\x18\x06 \x01(\x0e\x32\x1a.dmi.ComponentStandbyState\"\x90\x02\n\x13\x43omponentSensorData\x12\r\n\x05value\x18\x01 \x01(\x05\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.dmi.DataValueType\x12\x1e\n\x05scale\x18\x03 \x01(\x0e\x32\x0f.dmi.ValueScale\x12\x11\n\tprecision\x18\x04 \x01(\x05\x12!\n\x06status\x18\x05 \x01(\x0e\x32\x11.dmi.SensorStatus\x12\x15\n\runits_display\x18\x06 \x01(\t\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x19\n\x11value_update_rate\x18\x08 \x01(\r\x12\x11\n\tdata_type\x18\t \x01(\t\"\xe1\x05\n\x17PortComponentAttributes\x12\x42\n\x0e\x63onnector_type\x18\x01 \x01(\x0e\x32*.dmi.PortComponentAttributes.ConnectorType\x12\x31\n\x05speed\x18\x02 \x01(\x0e\x32\".dmi.PortComponentAttributes.Speed\x12\x37\n\x08protocol\x18\x03 \x01(\x0e\x32%.dmi.PortComponentAttributes.Protocol\x12\x16\n\x0ephysical_label\x18\x04 \x01(\t\x12\x15\n\rmapping_label\x18\x05 \x01(\t\x12\'\n\rpon_id_config\x18\x06 \x01(\x0b\x32\x10.dmi.PonIdConfig\x12\x1d\n\x15speed_autonegotiation\x18\x07 \x01(\x08\"p\n\rConnectorType\x12\x1c\n\x18\x43ONNECTOR_TYPE_UNDEFINED\x10\x00\x12\x08\n\x04RJ45\x10\x01\x12\x0c\n\x08\x46IBER_LC\x10\x02\x12\x0f\n\x0b\x46IBER_SC_PC\x10\x03\x12\r\n\tFIBER_MPO\x10\x04\x12\t\n\x05RS232\x10\x05\"\xae\x01\n\x05Speed\x12\x13\n\x0fSPEED_UNDEFINED\x10\x00\x12\x0b\n\x07\x44YNAMIC\x10\x01\x12\r\n\tGIGABIT_1\x10\x02\x12\x0e\n\nGIGABIT_10\x10\x03\x12\x0e\n\nGIGABIT_25\x10\x04\x12\x0e\n\nGIGABIT_40\x10\x05\x12\x0f\n\x0bGIGABIT_100\x10\x06\x12\x0f\n\x0bGIGABIT_400\x10\x07\x12\x10\n\x0cMEGABIT_2500\x10\x08\x12\x10\n\x0cMEGABIT_1250\x10\t\"|\n\x08Protocol\x12\x16\n\x12PROTOCOL_UNDEFINED\x10\x00\x12\x0c\n\x08\x45THERNET\x10\x01\x12\x08\n\x04GPON\x10\x02\x12\t\n\x05XGPON\x10\x03\x12\n\n\x06XGSPON\x10\x04\x12\t\n\x05GFAST\x10\x05\x12\n\n\x06SERIAL\x10\x06\x12\x08\n\x04\x45PON\x10\x07\x12\x08\n\x04\x42ITS\x10\x08\"H\n\x1dPortComponentChangeAttributes\x12\'\n\rpon_id_config\x18\x01 \x01(\x0b\x32\x10.dmi.PonIdConfig\"P\n$TransceiverComponentChangeAttributes\x12(\n\ntrans_type\x18\x01 \x01(\x0e\x32\x14.dmi.TransceiverType\"B\n\x0bPonIdConfig\x12\x0e\n\x06pon_id\x18\x01 \x01(\x0c\x12#\n\x1bpon_id_transmit_periodicity\x18\x02 \x01(\r\"6\n\x1c\x43ontainerComponentAttributes\x12\x16\n\x0ephysical_label\x18\x01 \x01(\t\"\xb3\x01\n\x16PsuComponentAttributes\x12G\n\x11supported_voltage\x18\x01 \x01(\x0e\x32,.dmi.PsuComponentAttributes.SupportedVoltage\"P\n\x10SupportedVoltage\x12\x1f\n\x1bSUPPORTED_VOLTAGE_UNDEFINED\x10\x00\x12\x07\n\x03V48\x10\x01\x12\x08\n\x04V230\x10\x02\x12\x08\n\x04V115\x10\x03\"\xab\x04\n\x1fTransceiverComponentsAttributes\x12\x44\n\x0b\x66orm_factor\x18\x01 \x01(\x0e\x32/.dmi.TransceiverComponentsAttributes.FormFactor\x12(\n\ntrans_type\x18\x02 \x01(\x0e\x32\x14.dmi.TransceiverType\x12\x14\n\x0cmax_distance\x18\x03 \x01(\r\x12+\n\x12max_distance_scale\x18\x04 \x01(\x0e\x32\x0f.dmi.ValueScale\x12\x15\n\rrx_wavelength\x18\x05 \x03(\r\x12\x15\n\rtx_wavelength\x18\x06 \x03(\r\x12)\n\x10wavelength_scale\x18\x07 \x01(\x0e\x32\x0f.dmi.ValueScale\x12\x10\n\x08tx_power\x18\x08 \x03(\x05\x12\'\n\x0etx_power_scale\x18\t \x01(\x0e\x32\x0f.dmi.ValueScale\"\xc0\x01\n\nFormFactor\x12\x17\n\x13\x46ORM_FACTOR_UNKNOWN\x10\x00\x12\x08\n\x04QSFP\x10\x01\x12\r\n\tQSFP_PLUS\x10\x02\x12\n\n\x06QSFP28\x10\x03\x12\x07\n\x03SFP\x10\x04\x12\x0c\n\x08SFP_PLUS\x10\x05\x12\x07\n\x03XFP\x10\x06\x12\x08\n\x04\x43\x46P4\x10\x07\x12\x08\n\x04\x43\x46P2\x10\x08\x12\x08\n\x04\x43PAK\x10\t\x12\x06\n\x02X2\x10\n\x12\t\n\x05OTHER\x10\x0b\x12\x07\n\x03\x43\x46P\x10\x0c\x12\x0c\n\x08\x43\x46P2_ACO\x10\r\x12\x0c\n\x08\x43\x46P2_DCO\x10\x0e\"\xe8\x05\n\tComponent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x05\x63lass\x18\x02 \x01(\x0e\x32\x12.dmi.ComponentType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06parent\x18\x04 \x01(\t\x12\x16\n\x0eparent_rel_pos\x18\x05 \x01(\x05\x12 \n\x08\x63hildren\x18\x06 \x03(\x0b\x32\x0e.dmi.Component\x12\x14\n\x0chardware_rev\x18\x07 \x01(\t\x12\x14\n\x0c\x66irmware_rev\x18\x08 \x01(\t\x12\x14\n\x0csoftware_rev\x18\t \x01(\t\x12\x12\n\nserial_num\x18\n \x01(\t\x12\x10\n\x08mfg_name\x18\x0b \x01(\t\x12\x12\n\nmodel_name\x18\x0c \x01(\t\x12\r\n\x05\x61lias\x18\r \x01(\t\x12\x10\n\x08\x61sset_id\x18\x0e \x01(\t\x12\x0e\n\x06is_fru\x18\x0f \x01(\x08\x12,\n\x08mfg_date\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\x03uri\x18\x11 \x01(\x0b\x32\x08.dmi.Uri\x12\x17\n\x04uuid\x18\x12 \x01(\x0b\x32\t.dmi.Uuid\x12\"\n\x05state\x18\x13 \x01(\x0b\x32\x13.dmi.ComponentState\x12-\n\x0bsensor_data\x18\x14 \x03(\x0b\x32\x18.dmi.ComponentSensorData\x12\x31\n\tport_attr\x18\x32 \x01(\x0b\x32\x1c.dmi.PortComponentAttributesH\x00\x12;\n\x0e\x63ontainer_attr\x18\x33 \x01(\x0b\x32!.dmi.ContainerComponentAttributesH\x00\x12/\n\x08psu_attr\x18\x34 \x01(\x0b\x32\x1b.dmi.PsuComponentAttributesH\x00\x12@\n\x10transceiver_attr\x18\x35 \x01(\x0b\x32$.dmi.TransceiverComponentsAttributesH\x00\x42\n\n\x08specific\"\x8a\x01\n\x08Hardware\x12/\n\x0blast_change\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1c\n\x04root\x18\x02 \x01(\x0b\x32\x0e.dmi.Component\x12/\n\x0blast_booted\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xe9\x02\n\x13ModifiableComponent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x05\x63lass\x18\x02 \x01(\x0e\x32\x12.dmi.ComponentType\x12\x1e\n\x06parent\x18\x03 \x01(\x0b\x32\x0e.dmi.Component\x12\x16\n\x0eparent_rel_pos\x18\x04 \x01(\x05\x12\r\n\x05\x61lias\x18\x05 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x06 \x01(\t\x12\x15\n\x03uri\x18\x07 \x01(\x0b\x32\x08.dmi.Uri\x12-\n\x0b\x61\x64min_state\x18\x08 \x01(\x0e\x32\x18.dmi.ComponentAdminState\x12\x37\n\tport_attr\x18\x32 \x01(\x0b\x32\".dmi.PortComponentChangeAttributesH\x00\x12=\n\x08trx_attr\x18\x33 \x01(\x0b\x32).dmi.TransceiverComponentChangeAttributesH\x00\x42\n\n\x08specific*\xb4\x03\n\rComponentType\x12\x1c\n\x18\x43OMPONENT_TYPE_UNDEFINED\x10\x00\x12\x1a\n\x16\x43OMPONENT_TYPE_UNKNOWN\x10\x01\x12\x1a\n\x16\x43OMPONENT_TYPE_CHASSIS\x10\x02\x12\x1c\n\x18\x43OMPONENT_TYPE_BACKPLANE\x10\x03\x12\x1c\n\x18\x43OMPONENT_TYPE_CONTAINER\x10\x04\x12\x1f\n\x1b\x43OMPONENT_TYPE_POWER_SUPPLY\x10\x05\x12\x16\n\x12\x43OMPONENT_TYPE_FAN\x10\x06\x12\x19\n\x15\x43OMPONENT_TYPE_SENSOR\x10\x07\x12\x19\n\x15\x43OMPONENT_TYPE_MODULE\x10\x08\x12\x17\n\x13\x43OMPONENT_TYPE_PORT\x10\t\x12\x16\n\x12\x43OMPONENT_TYPE_CPU\x10\n\x12\x1a\n\x16\x43OMPONENT_TYPE_BATTERY\x10\x0b\x12\x1a\n\x16\x43OMPONENT_TYPE_STORAGE\x10\x0c\x12\x19\n\x15\x43OMPONENT_TYPE_MEMORY\x10\r\x12\x1e\n\x1a\x43OMPONENT_TYPE_TRANSCEIVER\x10\x0e*\xb3\x01\n\x13\x43omponentAdminState\x12\x1e\n\x1a\x43OMP_ADMIN_STATE_UNDEFINED\x10\x00\x12\x1c\n\x18\x43OMP_ADMIN_STATE_UNKNOWN\x10\x01\x12\x1b\n\x17\x43OMP_ADMIN_STATE_LOCKED\x10\x02\x12\"\n\x1e\x43OMP_ADMIN_STATE_SHUTTING_DOWN\x10\x03\x12\x1d\n\x19\x43OMP_ADMIN_STATE_UNLOCKED\x10\x04*\xa8\x01\n\x12\x43omponentOperState\x12\x1d\n\x19\x43OMP_OPER_STATE_UNDEFINED\x10\x00\x12\x1b\n\x17\x43OMP_OPER_STATE_UNKNOWN\x10\x01\x12\x1c\n\x18\x43OMP_OPER_STATE_DISABLED\x10\x02\x12\x1b\n\x17\x43OMP_OPER_STATE_ENABLED\x10\x03\x12\x1b\n\x17\x43OMP_OPER_STATE_TESTING\x10\x04*\xa6\x01\n\x13\x43omponentUsageState\x12\x1e\n\x1a\x43OMP_USAGE_STATE_UNDEFINED\x10\x00\x12\x1c\n\x18\x43OMP_USAGE_STATE_UNKNOWN\x10\x01\x12\x19\n\x15\x43OMP_USAGE_STATE_IDLE\x10\x02\x12\x1b\n\x17\x43OMP_USAGE_STATE_ACTIVE\x10\x03\x12\x19\n\x15\x43OMP_USAGE_STATE_BUSY\x10\x04*\x8f\x02\n\x13\x43omponentAlarmState\x12\x1e\n\x1a\x43OMP_ALARM_STATE_UNDEFINED\x10\x00\x12\x1c\n\x18\x43OMP_ALARM_STATE_UNKNOWN\x10\x01\x12!\n\x1d\x43OMP_ALARM_STATE_UNDER_REPAIR\x10\x02\x12\x1d\n\x19\x43OMP_ALARM_STATE_CRITICAL\x10\x03\x12\x1a\n\x16\x43OMP_ALARM_STATE_MAJOR\x10\x04\x12\x1a\n\x16\x43OMP_ALARM_STATE_MINOR\x10\x05\x12\x1c\n\x18\x43OMP_ALARM_STATE_WARNING\x10\x06\x12\"\n\x1e\x43OMP_ALARM_STATE_INDETERMINATE\x10\x07*\xbc\x01\n\x15\x43omponentStandbyState\x12 \n\x1c\x43OMP_STANDBY_STATE_UNDEFINED\x10\x00\x12\x1e\n\x1a\x43OMP_STANDBY_STATE_UNKNOWN\x10\x01\x12\x1a\n\x16\x43OMP_STANDBY_STATE_HOT\x10\x02\x12\x1b\n\x17\x43OMP_STANDBY_STATE_COLD\x10\x03\x12(\n$COMP_STANDBY_STATE_PROVIDING_SERVICE\x10\x04*\x9d\x03\n\rDataValueType\x12\x18\n\x14VALUE_TYPE_UNDEFINED\x10\x00\x12\x14\n\x10VALUE_TYPE_OTHER\x10\x01\x12\x16\n\x12VALUE_TYPE_UNKNOWN\x10\x02\x12\x17\n\x13VALUE_TYPE_VOLTS_AC\x10\x03\x12\x17\n\x13VALUE_TYPE_VOLTS_DC\x10\x04\x12\x16\n\x12VALUE_TYPE_AMPERES\x10\x05\x12\x14\n\x10VALUE_TYPE_WATTS\x10\x06\x12\x14\n\x10VALUE_TYPE_HERTZ\x10\x07\x12\x16\n\x12VALUE_TYPE_CELSIUS\x10\x08\x12\x19\n\x15VALUE_TYPE_PERCENT_RH\x10\t\x12\x12\n\x0eVALUE_TYPE_RPM\x10\n\x12\x12\n\x0eVALUE_TYPE_CMM\x10\x0b\x12\x1a\n\x16VALUE_TYPE_TRUTH_VALUE\x10\x0c\x12\x16\n\x12VALUE_TYPE_PERCENT\x10\r\x12\x15\n\x11VALUE_TYPE_METERS\x10\x0e\x12\x14\n\x10VALUE_TYPE_BYTES\x10\x0f\x12\x12\n\x0eVALUE_TYPE_DBM\x10\x10*\xa4\x03\n\nValueScale\x12\x19\n\x15VALUE_SCALE_UNDEFINED\x10\x00\x12\x15\n\x11VALUE_SCALE_YOCTO\x10\x01\x12\x15\n\x11VALUE_SCALE_ZEPTO\x10\x02\x12\x14\n\x10VALUE_SCALE_ATTO\x10\x03\x12\x15\n\x11VALUE_SCALE_FEMTO\x10\x04\x12\x14\n\x10VALUE_SCALE_PICO\x10\x05\x12\x14\n\x10VALUE_SCALE_NANO\x10\x06\x12\x15\n\x11VALUE_SCALE_MICRO\x10\x07\x12\x15\n\x11VALUE_SCALE_MILLI\x10\x08\x12\x15\n\x11VALUE_SCALE_UNITS\x10\t\x12\x14\n\x10VALUE_SCALE_KILO\x10\n\x12\x14\n\x10VALUE_SCALE_MEGA\x10\x0b\x12\x14\n\x10VALUE_SCALE_GIGA\x10\x0c\x12\x14\n\x10VALUE_SCALE_TERA\x10\r\x12\x14\n\x10VALUE_SCALE_PETA\x10\x0e\x12\x13\n\x0fVALUE_SCALE_EXA\x10\x0f\x12\x15\n\x11VALUE_SCALE_ZETTA\x10\x10\x12\x15\n\x11VALUE_SCALE_YOTTA\x10\x11*\x82\x01\n\x0cSensorStatus\x12\x1b\n\x17SENSOR_STATUS_UNDEFINED\x10\x00\x12\x14\n\x10SENSOR_STATUS_OK\x10\x01\x12\x1d\n\x19SENSOR_STATUS_UNAVAILABLE\x10\x02\x12 \n\x1cSENSOR_STATUS_NONOPERATIONAL\x10\x03*\xa4\x01\n\x0fTransceiverType\x12\x12\n\x0eTYPE_UNDEFINED\x10\x00\x12\x0c\n\x08\x45THERNET\x10\x01\x12\x08\n\x04GPON\x10\x02\x12\t\n\x05XGPON\x10\x03\x12\n\n\x06XGSPON\x10\x04\x12\x08\n\x04\x43PON\x10\x05\x12\x0b\n\x07NG_PON2\x10\x06\x12\x08\n\x04\x45PON\x10\x07\x12\x15\n\x11\x43OMBO_GPON_XGSPON\x10\x08\x12\x16\n\x11TYPE_NOT_DETECTED\x10\xff\x01\x42;Z9github.com/opencord/device-management-interface/v3/go/dmib\x06proto3')

_COMPONENTTYPE = DESCRIPTOR.enum_types_by_name['ComponentType']
ComponentType = enum_type_wrapper.EnumTypeWrapper(_COMPONENTTYPE)
_COMPONENTADMINSTATE = DESCRIPTOR.enum_types_by_name['ComponentAdminState']
ComponentAdminState = enum_type_wrapper.EnumTypeWrapper(_COMPONENTADMINSTATE)
_COMPONENTOPERSTATE = DESCRIPTOR.enum_types_by_name['ComponentOperState']
ComponentOperState = enum_type_wrapper.EnumTypeWrapper(_COMPONENTOPERSTATE)
_COMPONENTUSAGESTATE = DESCRIPTOR.enum_types_by_name['ComponentUsageState']
ComponentUsageState = enum_type_wrapper.EnumTypeWrapper(_COMPONENTUSAGESTATE)
_COMPONENTALARMSTATE = DESCRIPTOR.enum_types_by_name['ComponentAlarmState']
ComponentAlarmState = enum_type_wrapper.EnumTypeWrapper(_COMPONENTALARMSTATE)
_COMPONENTSTANDBYSTATE = DESCRIPTOR.enum_types_by_name['ComponentStandbyState']
ComponentStandbyState = enum_type_wrapper.EnumTypeWrapper(_COMPONENTSTANDBYSTATE)
_DATAVALUETYPE = DESCRIPTOR.enum_types_by_name['DataValueType']
DataValueType = enum_type_wrapper.EnumTypeWrapper(_DATAVALUETYPE)
_VALUESCALE = DESCRIPTOR.enum_types_by_name['ValueScale']
ValueScale = enum_type_wrapper.EnumTypeWrapper(_VALUESCALE)
_SENSORSTATUS = DESCRIPTOR.enum_types_by_name['SensorStatus']
SensorStatus = enum_type_wrapper.EnumTypeWrapper(_SENSORSTATUS)
_TRANSCEIVERTYPE = DESCRIPTOR.enum_types_by_name['TransceiverType']
TransceiverType = enum_type_wrapper.EnumTypeWrapper(_TRANSCEIVERTYPE)
COMPONENT_TYPE_UNDEFINED = 0
COMPONENT_TYPE_UNKNOWN = 1
COMPONENT_TYPE_CHASSIS = 2
COMPONENT_TYPE_BACKPLANE = 3
COMPONENT_TYPE_CONTAINER = 4
COMPONENT_TYPE_POWER_SUPPLY = 5
COMPONENT_TYPE_FAN = 6
COMPONENT_TYPE_SENSOR = 7
COMPONENT_TYPE_MODULE = 8
COMPONENT_TYPE_PORT = 9
COMPONENT_TYPE_CPU = 10
COMPONENT_TYPE_BATTERY = 11
COMPONENT_TYPE_STORAGE = 12
COMPONENT_TYPE_MEMORY = 13
COMPONENT_TYPE_TRANSCEIVER = 14
COMP_ADMIN_STATE_UNDEFINED = 0
COMP_ADMIN_STATE_UNKNOWN = 1
COMP_ADMIN_STATE_LOCKED = 2
COMP_ADMIN_STATE_SHUTTING_DOWN = 3
COMP_ADMIN_STATE_UNLOCKED = 4
COMP_OPER_STATE_UNDEFINED = 0
COMP_OPER_STATE_UNKNOWN = 1
COMP_OPER_STATE_DISABLED = 2
COMP_OPER_STATE_ENABLED = 3
COMP_OPER_STATE_TESTING = 4
COMP_USAGE_STATE_UNDEFINED = 0
COMP_USAGE_STATE_UNKNOWN = 1
COMP_USAGE_STATE_IDLE = 2
COMP_USAGE_STATE_ACTIVE = 3
COMP_USAGE_STATE_BUSY = 4
COMP_ALARM_STATE_UNDEFINED = 0
COMP_ALARM_STATE_UNKNOWN = 1
COMP_ALARM_STATE_UNDER_REPAIR = 2
COMP_ALARM_STATE_CRITICAL = 3
COMP_ALARM_STATE_MAJOR = 4
COMP_ALARM_STATE_MINOR = 5
COMP_ALARM_STATE_WARNING = 6
COMP_ALARM_STATE_INDETERMINATE = 7
COMP_STANDBY_STATE_UNDEFINED = 0
COMP_STANDBY_STATE_UNKNOWN = 1
COMP_STANDBY_STATE_HOT = 2
COMP_STANDBY_STATE_COLD = 3
COMP_STANDBY_STATE_PROVIDING_SERVICE = 4
VALUE_TYPE_UNDEFINED = 0
VALUE_TYPE_OTHER = 1
VALUE_TYPE_UNKNOWN = 2
VALUE_TYPE_VOLTS_AC = 3
VALUE_TYPE_VOLTS_DC = 4
VALUE_TYPE_AMPERES = 5
VALUE_TYPE_WATTS = 6
VALUE_TYPE_HERTZ = 7
VALUE_TYPE_CELSIUS = 8
VALUE_TYPE_PERCENT_RH = 9
VALUE_TYPE_RPM = 10
VALUE_TYPE_CMM = 11
VALUE_TYPE_TRUTH_VALUE = 12
VALUE_TYPE_PERCENT = 13
VALUE_TYPE_METERS = 14
VALUE_TYPE_BYTES = 15
VALUE_TYPE_DBM = 16
VALUE_SCALE_UNDEFINED = 0
VALUE_SCALE_YOCTO = 1
VALUE_SCALE_ZEPTO = 2
VALUE_SCALE_ATTO = 3
VALUE_SCALE_FEMTO = 4
VALUE_SCALE_PICO = 5
VALUE_SCALE_NANO = 6
VALUE_SCALE_MICRO = 7
VALUE_SCALE_MILLI = 8
VALUE_SCALE_UNITS = 9
VALUE_SCALE_KILO = 10
VALUE_SCALE_MEGA = 11
VALUE_SCALE_GIGA = 12
VALUE_SCALE_TERA = 13
VALUE_SCALE_PETA = 14
VALUE_SCALE_EXA = 15
VALUE_SCALE_ZETTA = 16
VALUE_SCALE_YOTTA = 17
SENSOR_STATUS_UNDEFINED = 0
SENSOR_STATUS_OK = 1
SENSOR_STATUS_UNAVAILABLE = 2
SENSOR_STATUS_NONOPERATIONAL = 3
TYPE_UNDEFINED = 0
ETHERNET = 1
GPON = 2
XGPON = 3
XGSPON = 4
CPON = 5
NG_PON2 = 6
EPON = 7
COMBO_GPON_XGSPON = 8
TYPE_NOT_DETECTED = 255


_UUID = DESCRIPTOR.message_types_by_name['Uuid']
_HARDWAREID = DESCRIPTOR.message_types_by_name['HardwareID']
_URI = DESCRIPTOR.message_types_by_name['Uri']
_COMPONENTSTATE = DESCRIPTOR.message_types_by_name['ComponentState']
_COMPONENTSENSORDATA = DESCRIPTOR.message_types_by_name['ComponentSensorData']
_PORTCOMPONENTATTRIBUTES = DESCRIPTOR.message_types_by_name['PortComponentAttributes']
_PORTCOMPONENTCHANGEATTRIBUTES = DESCRIPTOR.message_types_by_name['PortComponentChangeAttributes']
_TRANSCEIVERCOMPONENTCHANGEATTRIBUTES = DESCRIPTOR.message_types_by_name['TransceiverComponentChangeAttributes']
_PONIDCONFIG = DESCRIPTOR.message_types_by_name['PonIdConfig']
_CONTAINERCOMPONENTATTRIBUTES = DESCRIPTOR.message_types_by_name['ContainerComponentAttributes']
_PSUCOMPONENTATTRIBUTES = DESCRIPTOR.message_types_by_name['PsuComponentAttributes']
_TRANSCEIVERCOMPONENTSATTRIBUTES = DESCRIPTOR.message_types_by_name['TransceiverComponentsAttributes']
_COMPONENT = DESCRIPTOR.message_types_by_name['Component']
_HARDWARE = DESCRIPTOR.message_types_by_name['Hardware']
_MODIFIABLECOMPONENT = DESCRIPTOR.message_types_by_name['ModifiableComponent']
_PORTCOMPONENTATTRIBUTES_CONNECTORTYPE = _PORTCOMPONENTATTRIBUTES.enum_types_by_name['ConnectorType']
_PORTCOMPONENTATTRIBUTES_SPEED = _PORTCOMPONENTATTRIBUTES.enum_types_by_name['Speed']
_PORTCOMPONENTATTRIBUTES_PROTOCOL = _PORTCOMPONENTATTRIBUTES.enum_types_by_name['Protocol']
_PSUCOMPONENTATTRIBUTES_SUPPORTEDVOLTAGE = _PSUCOMPONENTATTRIBUTES.enum_types_by_name['SupportedVoltage']
_TRANSCEIVERCOMPONENTSATTRIBUTES_FORMFACTOR = _TRANSCEIVERCOMPONENTSATTRIBUTES.enum_types_by_name['FormFactor']
Uuid = _reflection.GeneratedProtocolMessageType('Uuid', (_message.Message,), {
  'DESCRIPTOR' : _UUID,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.Uuid)
  })
_sym_db.RegisterMessage(Uuid)

HardwareID = _reflection.GeneratedProtocolMessageType('HardwareID', (_message.Message,), {
  'DESCRIPTOR' : _HARDWAREID,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.HardwareID)
  })
_sym_db.RegisterMessage(HardwareID)

Uri = _reflection.GeneratedProtocolMessageType('Uri', (_message.Message,), {
  'DESCRIPTOR' : _URI,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.Uri)
  })
_sym_db.RegisterMessage(Uri)

ComponentState = _reflection.GeneratedProtocolMessageType('ComponentState', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTSTATE,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ComponentState)
  })
_sym_db.RegisterMessage(ComponentState)

ComponentSensorData = _reflection.GeneratedProtocolMessageType('ComponentSensorData', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENTSENSORDATA,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ComponentSensorData)
  })
_sym_db.RegisterMessage(ComponentSensorData)

PortComponentAttributes = _reflection.GeneratedProtocolMessageType('PortComponentAttributes', (_message.Message,), {
  'DESCRIPTOR' : _PORTCOMPONENTATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PortComponentAttributes)
  })
_sym_db.RegisterMessage(PortComponentAttributes)

PortComponentChangeAttributes = _reflection.GeneratedProtocolMessageType('PortComponentChangeAttributes', (_message.Message,), {
  'DESCRIPTOR' : _PORTCOMPONENTCHANGEATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PortComponentChangeAttributes)
  })
_sym_db.RegisterMessage(PortComponentChangeAttributes)

TransceiverComponentChangeAttributes = _reflection.GeneratedProtocolMessageType('TransceiverComponentChangeAttributes', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCEIVERCOMPONENTCHANGEATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.TransceiverComponentChangeAttributes)
  })
_sym_db.RegisterMessage(TransceiverComponentChangeAttributes)

PonIdConfig = _reflection.GeneratedProtocolMessageType('PonIdConfig', (_message.Message,), {
  'DESCRIPTOR' : _PONIDCONFIG,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PonIdConfig)
  })
_sym_db.RegisterMessage(PonIdConfig)

ContainerComponentAttributes = _reflection.GeneratedProtocolMessageType('ContainerComponentAttributes', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERCOMPONENTATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ContainerComponentAttributes)
  })
_sym_db.RegisterMessage(ContainerComponentAttributes)

PsuComponentAttributes = _reflection.GeneratedProtocolMessageType('PsuComponentAttributes', (_message.Message,), {
  'DESCRIPTOR' : _PSUCOMPONENTATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.PsuComponentAttributes)
  })
_sym_db.RegisterMessage(PsuComponentAttributes)

TransceiverComponentsAttributes = _reflection.GeneratedProtocolMessageType('TransceiverComponentsAttributes', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCEIVERCOMPONENTSATTRIBUTES,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.TransceiverComponentsAttributes)
  })
_sym_db.RegisterMessage(TransceiverComponentsAttributes)

Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), {
  'DESCRIPTOR' : _COMPONENT,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.Component)
  })
_sym_db.RegisterMessage(Component)

Hardware = _reflection.GeneratedProtocolMessageType('Hardware', (_message.Message,), {
  'DESCRIPTOR' : _HARDWARE,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.Hardware)
  })
_sym_db.RegisterMessage(Hardware)

ModifiableComponent = _reflection.GeneratedProtocolMessageType('ModifiableComponent', (_message.Message,), {
  'DESCRIPTOR' : _MODIFIABLECOMPONENT,
  '__module__' : 'dmi.hw_pb2'
  # @@protoc_insertion_point(class_scope:dmi.ModifiableComponent)
  })
_sym_db.RegisterMessage(ModifiableComponent)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/opencord/device-management-interface/v3/go/dmi'
  _COMPONENTTYPE._serialized_start=3735
  _COMPONENTTYPE._serialized_end=4171
  _COMPONENTADMINSTATE._serialized_start=4174
  _COMPONENTADMINSTATE._serialized_end=4353
  _COMPONENTOPERSTATE._serialized_start=4356
  _COMPONENTOPERSTATE._serialized_end=4524
  _COMPONENTUSAGESTATE._serialized_start=4527
  _COMPONENTUSAGESTATE._serialized_end=4693
  _COMPONENTALARMSTATE._serialized_start=4696
  _COMPONENTALARMSTATE._serialized_end=4967
  _COMPONENTSTANDBYSTATE._serialized_start=4970
  _COMPONENTSTANDBYSTATE._serialized_end=5158
  _DATAVALUETYPE._serialized_start=5161
  _DATAVALUETYPE._serialized_end=5574
  _VALUESCALE._serialized_start=5577
  _VALUESCALE._serialized_end=5997
  _SENSORSTATUS._serialized_start=6000
  _SENSORSTATUS._serialized_end=6130
  _TRANSCEIVERTYPE._serialized_start=6133
  _TRANSCEIVERTYPE._serialized_end=6297
  _UUID._serialized_start=54
  _UUID._serialized_end=74
  _HARDWAREID._serialized_start=76
  _HARDWAREID._serialized_end=113
  _URI._serialized_start=115
  _URI._serialized_end=133
  _COMPONENTSTATE._serialized_start=136
  _COMPONENTSTATE._serialized_end=445
  _COMPONENTSENSORDATA._serialized_start=448
  _COMPONENTSENSORDATA._serialized_end=720
  _PORTCOMPONENTATTRIBUTES._serialized_start=723
  _PORTCOMPONENTATTRIBUTES._serialized_end=1460
  _PORTCOMPONENTATTRIBUTES_CONNECTORTYPE._serialized_start=1045
  _PORTCOMPONENTATTRIBUTES_CONNECTORTYPE._serialized_end=1157
  _PORTCOMPONENTATTRIBUTES_SPEED._serialized_start=1160
  _PORTCOMPONENTATTRIBUTES_SPEED._serialized_end=1334
  _PORTCOMPONENTATTRIBUTES_PROTOCOL._serialized_start=1336
  _PORTCOMPONENTATTRIBUTES_PROTOCOL._serialized_end=1460
  _PORTCOMPONENTCHANGEATTRIBUTES._serialized_start=1462
  _PORTCOMPONENTCHANGEATTRIBUTES._serialized_end=1534
  _TRANSCEIVERCOMPONENTCHANGEATTRIBUTES._serialized_start=1536
  _TRANSCEIVERCOMPONENTCHANGEATTRIBUTES._serialized_end=1616
  _PONIDCONFIG._serialized_start=1618
  _PONIDCONFIG._serialized_end=1684
  _CONTAINERCOMPONENTATTRIBUTES._serialized_start=1686
  _CONTAINERCOMPONENTATTRIBUTES._serialized_end=1740
  _PSUCOMPONENTATTRIBUTES._serialized_start=1743
  _PSUCOMPONENTATTRIBUTES._serialized_end=1922
  _PSUCOMPONENTATTRIBUTES_SUPPORTEDVOLTAGE._serialized_start=1842
  _PSUCOMPONENTATTRIBUTES_SUPPORTEDVOLTAGE._serialized_end=1922
  _TRANSCEIVERCOMPONENTSATTRIBUTES._serialized_start=1925
  _TRANSCEIVERCOMPONENTSATTRIBUTES._serialized_end=2480
  _TRANSCEIVERCOMPONENTSATTRIBUTES_FORMFACTOR._serialized_start=2288
  _TRANSCEIVERCOMPONENTSATTRIBUTES_FORMFACTOR._serialized_end=2480
  _COMPONENT._serialized_start=2483
  _COMPONENT._serialized_end=3227
  _HARDWARE._serialized_start=3230
  _HARDWARE._serialized_end=3368
  _MODIFIABLECOMPONENT._serialized_start=3371
  _MODIFIABLECOMPONENT._serialized_end=3732
# @@protoc_insertion_point(module_scope)
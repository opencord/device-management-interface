// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: dmi/commons.proto

#include "dmi/commons.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

namespace dmi {
}  // namespace dmi
void InitDefaults_dmi_2fcommons_2eproto() {
}

constexpr ::google::protobuf::Metadata* file_level_metadata_dmi_2fcommons_2eproto = nullptr;
const ::google::protobuf::EnumDescriptor* file_level_enum_descriptors_dmi_2fcommons_2eproto[2];
constexpr ::google::protobuf::ServiceDescriptor const** file_level_service_descriptors_dmi_2fcommons_2eproto = nullptr;
const ::google::protobuf::uint32 TableStruct_dmi_2fcommons_2eproto::offsets[1] = {};
static constexpr ::google::protobuf::internal::MigrationSchema* schemas = nullptr;
static constexpr ::google::protobuf::Message* const* file_default_instances = nullptr;

::google::protobuf::internal::AssignDescriptorsTable assign_descriptors_table_dmi_2fcommons_2eproto = {
  {}, AddDescriptors_dmi_2fcommons_2eproto, "dmi/commons.proto", schemas,
  file_default_instances, TableStruct_dmi_2fcommons_2eproto::offsets,
  file_level_metadata_dmi_2fcommons_2eproto, 0, file_level_enum_descriptors_dmi_2fcommons_2eproto, file_level_service_descriptors_dmi_2fcommons_2eproto,
};

const char descriptor_table_protodef_dmi_2fcommons_2eproto[] =
  "\n\021dmi/commons.proto\022\003dmi*\?\n\006Status\022\024\n\020UN"
  "DEFINED_STATUS\020\000\022\r\n\tOK_STATUS\020\001\022\020\n\014ERROR"
  "_STATUS\020\002*\?\n\010LogLevel\022\t\n\005TRACE\020\000\022\t\n\005DEBU"
  "G\020\001\022\010\n\004INFO\020\002\022\010\n\004WARN\020\003\022\t\n\005ERROR\020\004B;Z9gi"
  "thub.com/opencord/device-management-inte"
  "rface/v3/go/dmib\006proto3"
  ;
::google::protobuf::internal::DescriptorTable descriptor_table_dmi_2fcommons_2eproto = {
  false, InitDefaults_dmi_2fcommons_2eproto, 
  descriptor_table_protodef_dmi_2fcommons_2eproto,
  "dmi/commons.proto", &assign_descriptors_table_dmi_2fcommons_2eproto, 223,
};

void AddDescriptors_dmi_2fcommons_2eproto() {
  static constexpr ::google::protobuf::internal::InitFunc deps[1] =
  {
  };
 ::google::protobuf::internal::AddDescriptors(&descriptor_table_dmi_2fcommons_2eproto, deps, 0);
}

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_dmi_2fcommons_2eproto = []() { AddDescriptors_dmi_2fcommons_2eproto(); return true; }();
namespace dmi {
const ::google::protobuf::EnumDescriptor* Status_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_dmi_2fcommons_2eproto);
  return file_level_enum_descriptors_dmi_2fcommons_2eproto[0];
}
bool Status_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
    case 2:
      return true;
    default:
      return false;
  }
}

const ::google::protobuf::EnumDescriptor* LogLevel_descriptor() {
  ::google::protobuf::internal::AssignDescriptors(&assign_descriptors_table_dmi_2fcommons_2eproto);
  return file_level_enum_descriptors_dmi_2fcommons_2eproto[1];
}
bool LogLevel_IsValid(int value) {
  switch (value) {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
      return true;
    default:
      return false;
  }
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace dmi
namespace google {
namespace protobuf {
}  // namespace protobuf
}  // namespace google

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>

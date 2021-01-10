// Code generated by protoc-gen-go. DO NOT EDIT.
// source: dmi/sw_management_service.proto

package dmi

import (
	context "context"
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type GetSoftwareVersionInformationResponse_Reason int32

const (
	GetSoftwareVersionInformationResponse_UNDEFINED_REASON GetSoftwareVersionInformationResponse_Reason = 0
	GetSoftwareVersionInformationResponse_UNKNOWN_DEVICE   GetSoftwareVersionInformationResponse_Reason = 1
	GetSoftwareVersionInformationResponse_INTERNAL_ERROR   GetSoftwareVersionInformationResponse_Reason = 2
)

var GetSoftwareVersionInformationResponse_Reason_name = map[int32]string{
	0: "UNDEFINED_REASON",
	1: "UNKNOWN_DEVICE",
	2: "INTERNAL_ERROR",
}

var GetSoftwareVersionInformationResponse_Reason_value = map[string]int32{
	"UNDEFINED_REASON": 0,
	"UNKNOWN_DEVICE":   1,
	"INTERNAL_ERROR":   2,
}

func (x GetSoftwareVersionInformationResponse_Reason) String() string {
	return proto.EnumName(GetSoftwareVersionInformationResponse_Reason_name, int32(x))
}

func (GetSoftwareVersionInformationResponse_Reason) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{1, 0}
}

type ConfigResponse_Reason int32

const (
	ConfigResponse_UNDEFINED_REASON              ConfigResponse_Reason = 0
	ConfigResponse_UNKNOWN_DEVICE                ConfigResponse_Reason = 1
	ConfigResponse_INTERNAL_ERROR                ConfigResponse_Reason = 2
	ConfigResponse_ERROR_FETCHING_CONFIG         ConfigResponse_Reason = 3
	ConfigResponse_INVALID_CONFIG                ConfigResponse_Reason = 4
	ConfigResponse_OPERATION_ALREADY_IN_PROGRESS ConfigResponse_Reason = 5
)

var ConfigResponse_Reason_name = map[int32]string{
	0: "UNDEFINED_REASON",
	1: "UNKNOWN_DEVICE",
	2: "INTERNAL_ERROR",
	3: "ERROR_FETCHING_CONFIG",
	4: "INVALID_CONFIG",
	5: "OPERATION_ALREADY_IN_PROGRESS",
}

var ConfigResponse_Reason_value = map[string]int32{
	"UNDEFINED_REASON":              0,
	"UNKNOWN_DEVICE":                1,
	"INTERNAL_ERROR":                2,
	"ERROR_FETCHING_CONFIG":         3,
	"INVALID_CONFIG":                4,
	"OPERATION_ALREADY_IN_PROGRESS": 5,
}

func (x ConfigResponse_Reason) String() string {
	return proto.EnumName(ConfigResponse_Reason_name, int32(x))
}

func (ConfigResponse_Reason) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{4, 0}
}

type SoftwareVersionInformation struct {
	ActiveVersions       []*ImageVersion `protobuf:"bytes,1,rep,name=active_versions,json=activeVersions,proto3" json:"active_versions,omitempty"`
	StandbyVersions      []*ImageVersion `protobuf:"bytes,2,rep,name=standby_versions,json=standbyVersions,proto3" json:"standby_versions,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *SoftwareVersionInformation) Reset()         { *m = SoftwareVersionInformation{} }
func (m *SoftwareVersionInformation) String() string { return proto.CompactTextString(m) }
func (*SoftwareVersionInformation) ProtoMessage()    {}
func (*SoftwareVersionInformation) Descriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{0}
}

func (m *SoftwareVersionInformation) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_SoftwareVersionInformation.Unmarshal(m, b)
}
func (m *SoftwareVersionInformation) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_SoftwareVersionInformation.Marshal(b, m, deterministic)
}
func (m *SoftwareVersionInformation) XXX_Merge(src proto.Message) {
	xxx_messageInfo_SoftwareVersionInformation.Merge(m, src)
}
func (m *SoftwareVersionInformation) XXX_Size() int {
	return xxx_messageInfo_SoftwareVersionInformation.Size(m)
}
func (m *SoftwareVersionInformation) XXX_DiscardUnknown() {
	xxx_messageInfo_SoftwareVersionInformation.DiscardUnknown(m)
}

var xxx_messageInfo_SoftwareVersionInformation proto.InternalMessageInfo

func (m *SoftwareVersionInformation) GetActiveVersions() []*ImageVersion {
	if m != nil {
		return m.ActiveVersions
	}
	return nil
}

func (m *SoftwareVersionInformation) GetStandbyVersions() []*ImageVersion {
	if m != nil {
		return m.StandbyVersions
	}
	return nil
}

type GetSoftwareVersionInformationResponse struct {
	Status               Status                                       `protobuf:"varint,1,opt,name=status,proto3,enum=dmi.Status" json:"status,omitempty"`
	Reason               GetSoftwareVersionInformationResponse_Reason `protobuf:"varint,2,opt,name=reason,proto3,enum=dmi.GetSoftwareVersionInformationResponse_Reason" json:"reason,omitempty"`
	Info                 *SoftwareVersionInformation                  `protobuf:"bytes,3,opt,name=info,proto3" json:"info,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                                     `json:"-"`
	XXX_unrecognized     []byte                                       `json:"-"`
	XXX_sizecache        int32                                        `json:"-"`
}

func (m *GetSoftwareVersionInformationResponse) Reset()         { *m = GetSoftwareVersionInformationResponse{} }
func (m *GetSoftwareVersionInformationResponse) String() string { return proto.CompactTextString(m) }
func (*GetSoftwareVersionInformationResponse) ProtoMessage()    {}
func (*GetSoftwareVersionInformationResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{1}
}

func (m *GetSoftwareVersionInformationResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_GetSoftwareVersionInformationResponse.Unmarshal(m, b)
}
func (m *GetSoftwareVersionInformationResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_GetSoftwareVersionInformationResponse.Marshal(b, m, deterministic)
}
func (m *GetSoftwareVersionInformationResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_GetSoftwareVersionInformationResponse.Merge(m, src)
}
func (m *GetSoftwareVersionInformationResponse) XXX_Size() int {
	return xxx_messageInfo_GetSoftwareVersionInformationResponse.Size(m)
}
func (m *GetSoftwareVersionInformationResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_GetSoftwareVersionInformationResponse.DiscardUnknown(m)
}

var xxx_messageInfo_GetSoftwareVersionInformationResponse proto.InternalMessageInfo

func (m *GetSoftwareVersionInformationResponse) GetStatus() Status {
	if m != nil {
		return m.Status
	}
	return Status_UNDEFINED_STATUS
}

func (m *GetSoftwareVersionInformationResponse) GetReason() GetSoftwareVersionInformationResponse_Reason {
	if m != nil {
		return m.Reason
	}
	return GetSoftwareVersionInformationResponse_UNDEFINED_REASON
}

func (m *GetSoftwareVersionInformationResponse) GetInfo() *SoftwareVersionInformation {
	if m != nil {
		return m.Info
	}
	return nil
}

type DownloadImageRequest struct {
	DeviceUuid           *Uuid             `protobuf:"bytes,1,opt,name=device_uuid,json=deviceUuid,proto3" json:"device_uuid,omitempty"`
	ImageInfo            *ImageInformation `protobuf:"bytes,2,opt,name=image_info,json=imageInfo,proto3" json:"image_info,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *DownloadImageRequest) Reset()         { *m = DownloadImageRequest{} }
func (m *DownloadImageRequest) String() string { return proto.CompactTextString(m) }
func (*DownloadImageRequest) ProtoMessage()    {}
func (*DownloadImageRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{2}
}

func (m *DownloadImageRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_DownloadImageRequest.Unmarshal(m, b)
}
func (m *DownloadImageRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_DownloadImageRequest.Marshal(b, m, deterministic)
}
func (m *DownloadImageRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_DownloadImageRequest.Merge(m, src)
}
func (m *DownloadImageRequest) XXX_Size() int {
	return xxx_messageInfo_DownloadImageRequest.Size(m)
}
func (m *DownloadImageRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_DownloadImageRequest.DiscardUnknown(m)
}

var xxx_messageInfo_DownloadImageRequest proto.InternalMessageInfo

func (m *DownloadImageRequest) GetDeviceUuid() *Uuid {
	if m != nil {
		return m.DeviceUuid
	}
	return nil
}

func (m *DownloadImageRequest) GetImageInfo() *ImageInformation {
	if m != nil {
		return m.ImageInfo
	}
	return nil
}

type ConfigRequest struct {
	DeviceUuid *Uuid `protobuf:"bytes,1,opt,name=device_uuid,json=deviceUuid,proto3" json:"device_uuid,omitempty"`
	// Location of the configuration file, authentication (user/pass) if any should be in the url string
	// The config_url would contain the protocol, credentials, the IP address/DNS of the server and the path of the file
	// e.g. sftp://download_user:download_pass@192.168.0.1:22/OLT-configs/config-v1.2.3.xml
	ConfigUrl            string   `protobuf:"bytes,2,opt,name=config_url,json=configUrl,proto3" json:"config_url,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ConfigRequest) Reset()         { *m = ConfigRequest{} }
func (m *ConfigRequest) String() string { return proto.CompactTextString(m) }
func (*ConfigRequest) ProtoMessage()    {}
func (*ConfigRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{3}
}

func (m *ConfigRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ConfigRequest.Unmarshal(m, b)
}
func (m *ConfigRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ConfigRequest.Marshal(b, m, deterministic)
}
func (m *ConfigRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ConfigRequest.Merge(m, src)
}
func (m *ConfigRequest) XXX_Size() int {
	return xxx_messageInfo_ConfigRequest.Size(m)
}
func (m *ConfigRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ConfigRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ConfigRequest proto.InternalMessageInfo

func (m *ConfigRequest) GetDeviceUuid() *Uuid {
	if m != nil {
		return m.DeviceUuid
	}
	return nil
}

func (m *ConfigRequest) GetConfigUrl() string {
	if m != nil {
		return m.ConfigUrl
	}
	return ""
}

type ConfigResponse struct {
	Status               Status                `protobuf:"varint,1,opt,name=status,proto3,enum=dmi.Status" json:"status,omitempty"`
	Reason               ConfigResponse_Reason `protobuf:"varint,2,opt,name=reason,proto3,enum=dmi.ConfigResponse_Reason" json:"reason,omitempty"`
	XXX_NoUnkeyedLiteral struct{}              `json:"-"`
	XXX_unrecognized     []byte                `json:"-"`
	XXX_sizecache        int32                 `json:"-"`
}

func (m *ConfigResponse) Reset()         { *m = ConfigResponse{} }
func (m *ConfigResponse) String() string { return proto.CompactTextString(m) }
func (*ConfigResponse) ProtoMessage()    {}
func (*ConfigResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_000929e4bec891d7, []int{4}
}

func (m *ConfigResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ConfigResponse.Unmarshal(m, b)
}
func (m *ConfigResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ConfigResponse.Marshal(b, m, deterministic)
}
func (m *ConfigResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ConfigResponse.Merge(m, src)
}
func (m *ConfigResponse) XXX_Size() int {
	return xxx_messageInfo_ConfigResponse.Size(m)
}
func (m *ConfigResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ConfigResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ConfigResponse proto.InternalMessageInfo

func (m *ConfigResponse) GetStatus() Status {
	if m != nil {
		return m.Status
	}
	return Status_UNDEFINED_STATUS
}

func (m *ConfigResponse) GetReason() ConfigResponse_Reason {
	if m != nil {
		return m.Reason
	}
	return ConfigResponse_UNDEFINED_REASON
}

func init() {
	proto.RegisterEnum("dmi.GetSoftwareVersionInformationResponse_Reason", GetSoftwareVersionInformationResponse_Reason_name, GetSoftwareVersionInformationResponse_Reason_value)
	proto.RegisterEnum("dmi.ConfigResponse_Reason", ConfigResponse_Reason_name, ConfigResponse_Reason_value)
	proto.RegisterType((*SoftwareVersionInformation)(nil), "dmi.SoftwareVersionInformation")
	proto.RegisterType((*GetSoftwareVersionInformationResponse)(nil), "dmi.GetSoftwareVersionInformationResponse")
	proto.RegisterType((*DownloadImageRequest)(nil), "dmi.DownloadImageRequest")
	proto.RegisterType((*ConfigRequest)(nil), "dmi.ConfigRequest")
	proto.RegisterType((*ConfigResponse)(nil), "dmi.ConfigResponse")
}

func init() { proto.RegisterFile("dmi/sw_management_service.proto", fileDescriptor_000929e4bec891d7) }

var fileDescriptor_000929e4bec891d7 = []byte{
	// 671 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xac, 0x54, 0x5f, 0x4f, 0x13, 0x4f,
	0x14, 0xfd, 0x6d, 0xcb, 0xaf, 0x49, 0x6f, 0xa5, 0x2c, 0x23, 0x24, 0xd0, 0x84, 0x80, 0x35, 0x26,
	0x84, 0x84, 0x16, 0x0b, 0x2f, 0x8a, 0x31, 0xa9, 0xed, 0xb6, 0x6c, 0xc4, 0x2d, 0x4e, 0x5b, 0x8c,
	0xbc, 0x6c, 0x86, 0xee, 0xb4, 0x4c, 0xc2, 0xce, 0xd4, 0xd9, 0xd9, 0x56, 0xdf, 0xfd, 0x08, 0xc6,
	0xf8, 0x31, 0xfd, 0x08, 0x66, 0x67, 0xb6, 0x56, 0xfe, 0x25, 0x60, 0x7c, 0xdb, 0x3d, 0x73, 0xce,
	0xb9, 0x77, 0xf7, 0x9e, 0x3b, 0xb0, 0x19, 0x84, 0xac, 0x1a, 0x4d, 0xfd, 0x90, 0x70, 0x32, 0xa2,
	0x21, 0xe5, 0xca, 0x8f, 0xa8, 0x9c, 0xb0, 0x01, 0xad, 0x8c, 0xa5, 0x50, 0x02, 0x65, 0x83, 0x90,
	0x95, 0x96, 0x13, 0xd6, 0x40, 0x84, 0xa1, 0xe0, 0x91, 0xc1, 0x4b, 0x8f, 0x12, 0xe8, 0x62, 0x9a,
	0xbe, 0xa1, 0xd4, 0x86, 0x85, 0x64, 0x94, 0x2a, 0xcb, 0xdf, 0x2d, 0x28, 0x75, 0xc5, 0x50, 0x4d,
	0x89, 0xa4, 0xa7, 0x54, 0x46, 0x4c, 0x70, 0x97, 0x0f, 0x85, 0x0c, 0x89, 0x62, 0x82, 0xa3, 0x97,
	0xb0, 0x44, 0x06, 0x8a, 0x4d, 0xa8, 0x3f, 0x31, 0x87, 0xd1, 0x9a, 0xb5, 0x95, 0xdd, 0x2e, 0xd4,
	0x96, 0x2b, 0x41, 0xc8, 0x2a, 0x6e, 0xe2, 0x94, 0xca, 0x70, 0xd1, 0x30, 0xd3, 0xd7, 0x08, 0xbd,
	0x02, 0x3b, 0x52, 0x84, 0x07, 0xe7, 0x5f, 0xe6, 0xe2, 0xcc, 0x5d, 0xe2, 0xa5, 0x94, 0x3a, 0x53,
	0x97, 0xbf, 0x65, 0xe0, 0x59, 0x9b, 0xaa, 0xbb, 0x7b, 0xc3, 0x34, 0x1a, 0x0b, 0x1e, 0x51, 0xf4,
	0x14, 0x72, 0x91, 0x22, 0x2a, 0x4e, 0x5a, 0xb3, 0xb6, 0x8b, 0xb5, 0x82, 0x76, 0xef, 0x6a, 0x08,
	0xa7, 0x47, 0xc8, 0x85, 0x9c, 0xa4, 0x24, 0x12, 0x7c, 0x2d, 0xa3, 0x49, 0xcf, 0x35, 0xe9, 0x5e,
	0x05, 0x2a, 0x58, 0x0b, 0x71, 0x6a, 0x80, 0xf6, 0x61, 0x81, 0xf1, 0xa1, 0x58, 0xcb, 0x6e, 0x59,
	0xdb, 0x85, 0xda, 0xa6, 0xa9, 0x76, 0xb7, 0x8b, 0x26, 0x97, 0x5b, 0x90, 0x33, 0x36, 0x68, 0x05,
	0xec, 0xbe, 0xd7, 0x74, 0x5a, 0xae, 0xe7, 0x34, 0x7d, 0xec, 0xd4, 0xbb, 0x1d, 0xcf, 0xfe, 0x0f,
	0x21, 0x28, 0xf6, 0xbd, 0xb7, 0x5e, 0xe7, 0x83, 0xe7, 0x37, 0x9d, 0x53, 0xb7, 0xe1, 0xd8, 0x56,
	0x82, 0xb9, 0x5e, 0xcf, 0xc1, 0x5e, 0xfd, 0xd8, 0x77, 0x30, 0xee, 0x60, 0x3b, 0x53, 0xfe, 0x0c,
	0x2b, 0x4d, 0x31, 0xe5, 0x97, 0x82, 0x04, 0xfa, 0xff, 0x61, 0xfa, 0x29, 0xa6, 0x91, 0x42, 0x3b,
	0x50, 0x08, 0x68, 0x92, 0x08, 0x3f, 0x8e, 0x59, 0xa0, 0xff, 0x44, 0xa1, 0x96, 0xd7, 0xbd, 0xf5,
	0x63, 0x16, 0x60, 0x30, 0xa7, 0xc9, 0x33, 0x3a, 0x00, 0xd0, 0x11, 0xf0, 0xf5, 0x67, 0x64, 0x34,
	0x75, 0x75, 0x3e, 0x92, 0x3f, 0x9b, 0xcf, 0xb3, 0x19, 0x52, 0x3e, 0x83, 0xc5, 0x86, 0xe0, 0x43,
	0x36, 0xfa, 0x9b, 0x92, 0x1b, 0x00, 0x03, 0x2d, 0xf6, 0x63, 0x79, 0xa9, 0x4b, 0xe6, 0x71, 0xde,
	0x20, 0x7d, 0x79, 0x59, 0xfe, 0x9a, 0x81, 0xe2, 0xcc, 0xfc, 0x21, 0x53, 0xad, 0x5d, 0x9b, 0x6a,
	0x49, 0x93, 0xae, 0x3a, 0x5d, 0x1b, 0x5f, 0xf9, 0x87, 0xf5, 0x6f, 0x46, 0x81, 0xd6, 0x61, 0x55,
	0x3f, 0xfa, 0x2d, 0xa7, 0xd7, 0x38, 0x72, 0xbd, 0xb6, 0xdf, 0xe8, 0x78, 0x2d, 0xb7, 0x6d, 0x67,
	0x0d, 0xfd, 0xb4, 0x7e, 0xec, 0x36, 0x67, 0xd8, 0x02, 0x7a, 0x02, 0x1b, 0x9d, 0x13, 0x07, 0xd7,
	0x7b, 0x6e, 0xc7, 0xf3, 0xeb, 0xc7, 0xd8, 0xa9, 0x37, 0x3f, 0xfa, 0xae, 0xe7, 0x9f, 0xe0, 0x4e,
	0x1b, 0x3b, 0xdd, 0xae, 0xfd, 0x7f, 0xed, 0x67, 0x06, 0x36, 0x3d, 0x92, 0x2c, 0xd1, 0x2c, 0x4f,
	0xef, 0x7e, 0x6f, 0x7c, 0xd7, 0x2c, 0x3c, 0x7a, 0x0f, 0xe8, 0x66, 0x6a, 0xd1, 0x92, 0xfe, 0xf0,
	0x23, 0x22, 0x83, 0x04, 0x75, 0x9b, 0xa5, 0x9d, 0xfb, 0xe7, 0x1b, 0xbd, 0x86, 0xc5, 0x2b, 0x99,
	0x42, 0xeb, 0x5a, 0x7c, 0x5b, 0xce, 0x4a, 0xf6, 0x3c, 0x27, 0x66, 0x16, 0x7b, 0x16, 0x3a, 0x80,
	0xc5, 0x7a, 0xb2, 0xfa, 0x44, 0x51, 0xa3, 0xbf, 0xd1, 0xcd, 0x6d, 0xaa, 0x43, 0x58, 0xc1, 0x74,
	0x42, 0xa5, 0xea, 0x89, 0xae, 0xd9, 0xfd, 0x07, 0x88, 0xdb, 0x50, 0xea, 0x8f, 0x03, 0xa2, 0x12,
	0x44, 0xaa, 0x78, 0x6c, 0x46, 0x1e, 0x4b, 0x73, 0x6b, 0xa1, 0x2b, 0x31, 0x30, 0x8d, 0x3f, 0xbe,
	0x25, 0x1a, 0x7b, 0xd6, 0x9b, 0xc3, 0xb3, 0x17, 0x23, 0xa6, 0x2e, 0xe2, 0xf3, 0xca, 0x40, 0x84,
	0x55, 0x31, 0xa6, 0x7c, 0x20, 0x64, 0x50, 0x35, 0xd1, 0xdd, 0x9d, 0x5f, 0xb8, 0xbb, 0x8c, 0x2b,
	0x2a, 0x87, 0x64, 0x40, 0xab, 0x93, 0xfd, 0xea, 0x48, 0x54, 0x83, 0x90, 0x9d, 0xe7, 0xf4, 0x1d,
	0xba, 0xff, 0x2b, 0x00, 0x00, 0xff, 0xff, 0x55, 0x2e, 0xda, 0x40, 0xa0, 0x05, 0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// NativeSoftwareManagementServiceClient is the client API for NativeSoftwareManagementService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type NativeSoftwareManagementServiceClient interface {
	// Get the software version information of the Active and Standby images
	GetSoftwareVersion(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (*GetSoftwareVersionInformationResponse, error)
	// Downloads and installs the image in the standby partition, returns the status/progress of the Install
	DownloadImage(ctx context.Context, in *DownloadImageRequest, opts ...grpc.CallOption) (NativeSoftwareManagementService_DownloadImageClient, error)
	// Activates and runs the OLT with the image in the standby partition. If things are fine this image will
	// henceforth be marked as the Active Partition. The old working image would remain on the Standby partition.
	// Any possibly required (sub-)steps like "commit" are left to the "Device Manager"
	ActivateImage(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (NativeSoftwareManagementService_ActivateImageClient, error)
	// Marks the image in the Standby as Active and reboots the device, so that it boots from that image which was in the standby.
	// This API is to be used if operator wants to go back to the previous software
	RevertToStandbyImage(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (NativeSoftwareManagementService_RevertToStandbyImageClient, error)
	// This API can be used to let the devices pickup their properitary configuration which they need at startup.
	UpdateStartupConfiguration(ctx context.Context, in *ConfigRequest, opts ...grpc.CallOption) (NativeSoftwareManagementService_UpdateStartupConfigurationClient, error)
}

type nativeSoftwareManagementServiceClient struct {
	cc *grpc.ClientConn
}

func NewNativeSoftwareManagementServiceClient(cc *grpc.ClientConn) NativeSoftwareManagementServiceClient {
	return &nativeSoftwareManagementServiceClient{cc}
}

func (c *nativeSoftwareManagementServiceClient) GetSoftwareVersion(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (*GetSoftwareVersionInformationResponse, error) {
	out := new(GetSoftwareVersionInformationResponse)
	err := c.cc.Invoke(ctx, "/dmi.NativeSoftwareManagementService/GetSoftwareVersion", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *nativeSoftwareManagementServiceClient) DownloadImage(ctx context.Context, in *DownloadImageRequest, opts ...grpc.CallOption) (NativeSoftwareManagementService_DownloadImageClient, error) {
	stream, err := c.cc.NewStream(ctx, &_NativeSoftwareManagementService_serviceDesc.Streams[0], "/dmi.NativeSoftwareManagementService/DownloadImage", opts...)
	if err != nil {
		return nil, err
	}
	x := &nativeSoftwareManagementServiceDownloadImageClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type NativeSoftwareManagementService_DownloadImageClient interface {
	Recv() (*ImageStatus, error)
	grpc.ClientStream
}

type nativeSoftwareManagementServiceDownloadImageClient struct {
	grpc.ClientStream
}

func (x *nativeSoftwareManagementServiceDownloadImageClient) Recv() (*ImageStatus, error) {
	m := new(ImageStatus)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *nativeSoftwareManagementServiceClient) ActivateImage(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (NativeSoftwareManagementService_ActivateImageClient, error) {
	stream, err := c.cc.NewStream(ctx, &_NativeSoftwareManagementService_serviceDesc.Streams[1], "/dmi.NativeSoftwareManagementService/ActivateImage", opts...)
	if err != nil {
		return nil, err
	}
	x := &nativeSoftwareManagementServiceActivateImageClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type NativeSoftwareManagementService_ActivateImageClient interface {
	Recv() (*ImageStatus, error)
	grpc.ClientStream
}

type nativeSoftwareManagementServiceActivateImageClient struct {
	grpc.ClientStream
}

func (x *nativeSoftwareManagementServiceActivateImageClient) Recv() (*ImageStatus, error) {
	m := new(ImageStatus)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *nativeSoftwareManagementServiceClient) RevertToStandbyImage(ctx context.Context, in *HardwareID, opts ...grpc.CallOption) (NativeSoftwareManagementService_RevertToStandbyImageClient, error) {
	stream, err := c.cc.NewStream(ctx, &_NativeSoftwareManagementService_serviceDesc.Streams[2], "/dmi.NativeSoftwareManagementService/RevertToStandbyImage", opts...)
	if err != nil {
		return nil, err
	}
	x := &nativeSoftwareManagementServiceRevertToStandbyImageClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type NativeSoftwareManagementService_RevertToStandbyImageClient interface {
	Recv() (*ImageStatus, error)
	grpc.ClientStream
}

type nativeSoftwareManagementServiceRevertToStandbyImageClient struct {
	grpc.ClientStream
}

func (x *nativeSoftwareManagementServiceRevertToStandbyImageClient) Recv() (*ImageStatus, error) {
	m := new(ImageStatus)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *nativeSoftwareManagementServiceClient) UpdateStartupConfiguration(ctx context.Context, in *ConfigRequest, opts ...grpc.CallOption) (NativeSoftwareManagementService_UpdateStartupConfigurationClient, error) {
	stream, err := c.cc.NewStream(ctx, &_NativeSoftwareManagementService_serviceDesc.Streams[3], "/dmi.NativeSoftwareManagementService/UpdateStartupConfiguration", opts...)
	if err != nil {
		return nil, err
	}
	x := &nativeSoftwareManagementServiceUpdateStartupConfigurationClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type NativeSoftwareManagementService_UpdateStartupConfigurationClient interface {
	Recv() (*ConfigResponse, error)
	grpc.ClientStream
}

type nativeSoftwareManagementServiceUpdateStartupConfigurationClient struct {
	grpc.ClientStream
}

func (x *nativeSoftwareManagementServiceUpdateStartupConfigurationClient) Recv() (*ConfigResponse, error) {
	m := new(ConfigResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// NativeSoftwareManagementServiceServer is the server API for NativeSoftwareManagementService service.
type NativeSoftwareManagementServiceServer interface {
	// Get the software version information of the Active and Standby images
	GetSoftwareVersion(context.Context, *HardwareID) (*GetSoftwareVersionInformationResponse, error)
	// Downloads and installs the image in the standby partition, returns the status/progress of the Install
	DownloadImage(*DownloadImageRequest, NativeSoftwareManagementService_DownloadImageServer) error
	// Activates and runs the OLT with the image in the standby partition. If things are fine this image will
	// henceforth be marked as the Active Partition. The old working image would remain on the Standby partition.
	// Any possibly required (sub-)steps like "commit" are left to the "Device Manager"
	ActivateImage(*HardwareID, NativeSoftwareManagementService_ActivateImageServer) error
	// Marks the image in the Standby as Active and reboots the device, so that it boots from that image which was in the standby.
	// This API is to be used if operator wants to go back to the previous software
	RevertToStandbyImage(*HardwareID, NativeSoftwareManagementService_RevertToStandbyImageServer) error
	// This API can be used to let the devices pickup their properitary configuration which they need at startup.
	UpdateStartupConfiguration(*ConfigRequest, NativeSoftwareManagementService_UpdateStartupConfigurationServer) error
}

func RegisterNativeSoftwareManagementServiceServer(s *grpc.Server, srv NativeSoftwareManagementServiceServer) {
	s.RegisterService(&_NativeSoftwareManagementService_serviceDesc, srv)
}

func _NativeSoftwareManagementService_GetSoftwareVersion_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(HardwareID)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(NativeSoftwareManagementServiceServer).GetSoftwareVersion(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/dmi.NativeSoftwareManagementService/GetSoftwareVersion",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(NativeSoftwareManagementServiceServer).GetSoftwareVersion(ctx, req.(*HardwareID))
	}
	return interceptor(ctx, in, info, handler)
}

func _NativeSoftwareManagementService_DownloadImage_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(DownloadImageRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(NativeSoftwareManagementServiceServer).DownloadImage(m, &nativeSoftwareManagementServiceDownloadImageServer{stream})
}

type NativeSoftwareManagementService_DownloadImageServer interface {
	Send(*ImageStatus) error
	grpc.ServerStream
}

type nativeSoftwareManagementServiceDownloadImageServer struct {
	grpc.ServerStream
}

func (x *nativeSoftwareManagementServiceDownloadImageServer) Send(m *ImageStatus) error {
	return x.ServerStream.SendMsg(m)
}

func _NativeSoftwareManagementService_ActivateImage_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(HardwareID)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(NativeSoftwareManagementServiceServer).ActivateImage(m, &nativeSoftwareManagementServiceActivateImageServer{stream})
}

type NativeSoftwareManagementService_ActivateImageServer interface {
	Send(*ImageStatus) error
	grpc.ServerStream
}

type nativeSoftwareManagementServiceActivateImageServer struct {
	grpc.ServerStream
}

func (x *nativeSoftwareManagementServiceActivateImageServer) Send(m *ImageStatus) error {
	return x.ServerStream.SendMsg(m)
}

func _NativeSoftwareManagementService_RevertToStandbyImage_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(HardwareID)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(NativeSoftwareManagementServiceServer).RevertToStandbyImage(m, &nativeSoftwareManagementServiceRevertToStandbyImageServer{stream})
}

type NativeSoftwareManagementService_RevertToStandbyImageServer interface {
	Send(*ImageStatus) error
	grpc.ServerStream
}

type nativeSoftwareManagementServiceRevertToStandbyImageServer struct {
	grpc.ServerStream
}

func (x *nativeSoftwareManagementServiceRevertToStandbyImageServer) Send(m *ImageStatus) error {
	return x.ServerStream.SendMsg(m)
}

func _NativeSoftwareManagementService_UpdateStartupConfiguration_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(ConfigRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(NativeSoftwareManagementServiceServer).UpdateStartupConfiguration(m, &nativeSoftwareManagementServiceUpdateStartupConfigurationServer{stream})
}

type NativeSoftwareManagementService_UpdateStartupConfigurationServer interface {
	Send(*ConfigResponse) error
	grpc.ServerStream
}

type nativeSoftwareManagementServiceUpdateStartupConfigurationServer struct {
	grpc.ServerStream
}

func (x *nativeSoftwareManagementServiceUpdateStartupConfigurationServer) Send(m *ConfigResponse) error {
	return x.ServerStream.SendMsg(m)
}

var _NativeSoftwareManagementService_serviceDesc = grpc.ServiceDesc{
	ServiceName: "dmi.NativeSoftwareManagementService",
	HandlerType: (*NativeSoftwareManagementServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetSoftwareVersion",
			Handler:    _NativeSoftwareManagementService_GetSoftwareVersion_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "DownloadImage",
			Handler:       _NativeSoftwareManagementService_DownloadImage_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "ActivateImage",
			Handler:       _NativeSoftwareManagementService_ActivateImage_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "RevertToStandbyImage",
			Handler:       _NativeSoftwareManagementService_RevertToStandbyImage_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "UpdateStartupConfiguration",
			Handler:       _NativeSoftwareManagementService_UpdateStartupConfiguration_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "dmi/sw_management_service.proto",
}

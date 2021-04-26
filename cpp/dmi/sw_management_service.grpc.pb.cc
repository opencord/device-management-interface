// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: dmi/sw_management_service.proto

#include "dmi/sw_management_service.pb.h"
#include "dmi/sw_management_service.grpc.pb.h"

#include <grpc++/impl/codegen/async_stream.h>
#include <grpc++/impl/codegen/async_unary_call.h>
#include <grpc++/impl/codegen/channel_interface.h>
#include <grpc++/impl/codegen/client_unary_call.h>
#include <grpc++/impl/codegen/method_handler_impl.h>
#include <grpc++/impl/codegen/rpc_service_method.h>
#include <grpc++/impl/codegen/service_type.h>
#include <grpc++/impl/codegen/sync_stream.h>
namespace dmi {

static const char* NativeSoftwareManagementService_method_names[] = {
  "/dmi.NativeSoftwareManagementService/GetSoftwareVersion",
  "/dmi.NativeSoftwareManagementService/DownloadImage",
  "/dmi.NativeSoftwareManagementService/ActivateImage",
  "/dmi.NativeSoftwareManagementService/RevertToStandbyImage",
  "/dmi.NativeSoftwareManagementService/UpdateStartupConfiguration",
  "/dmi.NativeSoftwareManagementService/GetStartupConfigurationInfo",
};

std::unique_ptr< NativeSoftwareManagementService::Stub> NativeSoftwareManagementService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  std::unique_ptr< NativeSoftwareManagementService::Stub> stub(new NativeSoftwareManagementService::Stub(channel));
  return stub;
}

NativeSoftwareManagementService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_GetSoftwareVersion_(NativeSoftwareManagementService_method_names[0], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_DownloadImage_(NativeSoftwareManagementService_method_names[1], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_ActivateImage_(NativeSoftwareManagementService_method_names[2], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_RevertToStandbyImage_(NativeSoftwareManagementService_method_names[3], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_UpdateStartupConfiguration_(NativeSoftwareManagementService_method_names[4], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_GetStartupConfigurationInfo_(NativeSoftwareManagementService_method_names[5], ::grpc::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status NativeSoftwareManagementService::Stub::GetSoftwareVersion(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::dmi::GetSoftwareVersionInformationResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_GetSoftwareVersion_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::dmi::GetSoftwareVersionInformationResponse>* NativeSoftwareManagementService::Stub::AsyncGetSoftwareVersionRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::dmi::GetSoftwareVersionInformationResponse>(channel_.get(), cq, rpcmethod_GetSoftwareVersion_, context, request);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::DownloadImageRaw(::grpc::ClientContext* context, const ::dmi::DownloadImageRequest& request) {
  return new ::grpc::ClientReader< ::dmi::ImageStatus>(channel_.get(), rpcmethod_DownloadImage_, context, request);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncDownloadImageRaw(::grpc::ClientContext* context, const ::dmi::DownloadImageRequest& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::dmi::ImageStatus>(channel_.get(), cq, rpcmethod_DownloadImage_, context, request, tag);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::ActivateImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request) {
  return new ::grpc::ClientReader< ::dmi::ImageStatus>(channel_.get(), rpcmethod_ActivateImage_, context, request);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncActivateImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::dmi::ImageStatus>(channel_.get(), cq, rpcmethod_ActivateImage_, context, request, tag);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::RevertToStandbyImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request) {
  return new ::grpc::ClientReader< ::dmi::ImageStatus>(channel_.get(), rpcmethod_RevertToStandbyImage_, context, request);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncRevertToStandbyImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::dmi::ImageStatus>(channel_.get(), cq, rpcmethod_RevertToStandbyImage_, context, request, tag);
}

::grpc::ClientReader< ::dmi::ConfigResponse>* NativeSoftwareManagementService::Stub::UpdateStartupConfigurationRaw(::grpc::ClientContext* context, const ::dmi::ConfigRequest& request) {
  return new ::grpc::ClientReader< ::dmi::ConfigResponse>(channel_.get(), rpcmethod_UpdateStartupConfiguration_, context, request);
}

::grpc::ClientAsyncReader< ::dmi::ConfigResponse>* NativeSoftwareManagementService::Stub::AsyncUpdateStartupConfigurationRaw(::grpc::ClientContext* context, const ::dmi::ConfigRequest& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::dmi::ConfigResponse>(channel_.get(), cq, rpcmethod_UpdateStartupConfiguration_, context, request, tag);
}

::grpc::Status NativeSoftwareManagementService::Stub::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest& request, ::dmi::StartupConfigInfoResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_GetStartupConfigurationInfo_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::dmi::StartupConfigInfoResponse>* NativeSoftwareManagementService::Stub::AsyncGetStartupConfigurationInfoRaw(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::dmi::StartupConfigInfoResponse>(channel_.get(), cq, rpcmethod_GetStartupConfigurationInfo_, context, request);
}

NativeSoftwareManagementService::Service::Service() {
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[0],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::GetSoftwareVersionInformationResponse>(
          std::mem_fn(&NativeSoftwareManagementService::Service::GetSoftwareVersion), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[1],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::DownloadImageRequest, ::dmi::ImageStatus>(
          std::mem_fn(&NativeSoftwareManagementService::Service::DownloadImage), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[2],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::ImageStatus>(
          std::mem_fn(&NativeSoftwareManagementService::Service::ActivateImage), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[3],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::ImageStatus>(
          std::mem_fn(&NativeSoftwareManagementService::Service::RevertToStandbyImage), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[4],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::ConfigRequest, ::dmi::ConfigResponse>(
          std::mem_fn(&NativeSoftwareManagementService::Service::UpdateStartupConfiguration), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[5],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< NativeSoftwareManagementService::Service, ::dmi::StartupConfigInfoRequest, ::dmi::StartupConfigInfoResponse>(
          std::mem_fn(&NativeSoftwareManagementService::Service::GetStartupConfigurationInfo), this)));
}

NativeSoftwareManagementService::Service::~Service() {
}

::grpc::Status NativeSoftwareManagementService::Service::GetSoftwareVersion(::grpc::ServerContext* context, const ::dmi::HardwareID* request, ::dmi::GetSoftwareVersionInformationResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeSoftwareManagementService::Service::DownloadImage(::grpc::ServerContext* context, const ::dmi::DownloadImageRequest* request, ::grpc::ServerWriter< ::dmi::ImageStatus>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeSoftwareManagementService::Service::ActivateImage(::grpc::ServerContext* context, const ::dmi::HardwareID* request, ::grpc::ServerWriter< ::dmi::ImageStatus>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeSoftwareManagementService::Service::RevertToStandbyImage(::grpc::ServerContext* context, const ::dmi::HardwareID* request, ::grpc::ServerWriter< ::dmi::ImageStatus>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeSoftwareManagementService::Service::UpdateStartupConfiguration(::grpc::ServerContext* context, const ::dmi::ConfigRequest* request, ::grpc::ServerWriter< ::dmi::ConfigResponse>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeSoftwareManagementService::Service::GetStartupConfigurationInfo(::grpc::ServerContext* context, const ::dmi::StartupConfigInfoRequest* request, ::dmi::StartupConfigInfoResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace dmi


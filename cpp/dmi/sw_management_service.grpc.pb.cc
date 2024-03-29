// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: dmi/sw_management_service.proto

#include "dmi/sw_management_service.pb.h"
#include "dmi/sw_management_service.grpc.pb.h"

#include <functional>
#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/channel_interface.h>
#include <grpcpp/impl/codegen/client_unary_call.h>
#include <grpcpp/impl/codegen/client_callback.h>
#include <grpcpp/impl/codegen/message_allocator.h>
#include <grpcpp/impl/codegen/method_handler.h>
#include <grpcpp/impl/codegen/rpc_service_method.h>
#include <grpcpp/impl/codegen/server_callback.h>
#include <grpcpp/impl/codegen/server_callback_handlers.h>
#include <grpcpp/impl/codegen/server_context.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/sync_stream.h>
namespace dmi {

static const char* NativeSoftwareManagementService_method_names[] = {
  "/dmi.NativeSoftwareManagementService/GetSoftwareVersion",
  "/dmi.NativeSoftwareManagementService/DownloadImage",
  "/dmi.NativeSoftwareManagementService/ActivateImage",
  "/dmi.NativeSoftwareManagementService/RevertToStandbyImage",
  "/dmi.NativeSoftwareManagementService/UpdateStartupConfiguration",
  "/dmi.NativeSoftwareManagementService/GetStartupConfigurationInfo",
  "/dmi.NativeSoftwareManagementService/UploadDebugInfo",
};

std::unique_ptr< NativeSoftwareManagementService::Stub> NativeSoftwareManagementService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< NativeSoftwareManagementService::Stub> stub(new NativeSoftwareManagementService::Stub(channel));
  return stub;
}

NativeSoftwareManagementService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_GetSoftwareVersion_(NativeSoftwareManagementService_method_names[0], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_DownloadImage_(NativeSoftwareManagementService_method_names[1], ::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_ActivateImage_(NativeSoftwareManagementService_method_names[2], ::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_RevertToStandbyImage_(NativeSoftwareManagementService_method_names[3], ::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_UpdateStartupConfiguration_(NativeSoftwareManagementService_method_names[4], ::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_GetStartupConfigurationInfo_(NativeSoftwareManagementService_method_names[5], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_UploadDebugInfo_(NativeSoftwareManagementService_method_names[6], ::grpc::internal::RpcMethod::SERVER_STREAMING, channel)
  {}

::grpc::Status NativeSoftwareManagementService::Stub::GetSoftwareVersion(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::dmi::GetSoftwareVersionInformationResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetSoftwareVersion_, context, request, response);
}

void NativeSoftwareManagementService::Stub::experimental_async::GetSoftwareVersion(::grpc::ClientContext* context, const ::dmi::HardwareID* request, ::dmi::GetSoftwareVersionInformationResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetSoftwareVersion_, context, request, response, std::move(f));
}

void NativeSoftwareManagementService::Stub::experimental_async::GetSoftwareVersion(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::GetSoftwareVersionInformationResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetSoftwareVersion_, context, request, response, std::move(f));
}

void NativeSoftwareManagementService::Stub::experimental_async::GetSoftwareVersion(::grpc::ClientContext* context, const ::dmi::HardwareID* request, ::dmi::GetSoftwareVersionInformationResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetSoftwareVersion_, context, request, response, reactor);
}

void NativeSoftwareManagementService::Stub::experimental_async::GetSoftwareVersion(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::GetSoftwareVersionInformationResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetSoftwareVersion_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::dmi::GetSoftwareVersionInformationResponse>* NativeSoftwareManagementService::Stub::AsyncGetSoftwareVersionRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::GetSoftwareVersionInformationResponse>::Create(channel_.get(), cq, rpcmethod_GetSoftwareVersion_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::dmi::GetSoftwareVersionInformationResponse>* NativeSoftwareManagementService::Stub::PrepareAsyncGetSoftwareVersionRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::GetSoftwareVersionInformationResponse>::Create(channel_.get(), cq, rpcmethod_GetSoftwareVersion_, context, request, false);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::DownloadImageRaw(::grpc::ClientContext* context, const ::dmi::DownloadImageRequest& request) {
  return ::grpc_impl::internal::ClientReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), rpcmethod_DownloadImage_, context, request);
}

void NativeSoftwareManagementService::Stub::experimental_async::DownloadImage(::grpc::ClientContext* context, ::dmi::DownloadImageRequest* request, ::grpc::experimental::ClientReadReactor< ::dmi::ImageStatus>* reactor) {
  ::grpc_impl::internal::ClientCallbackReaderFactory< ::dmi::ImageStatus>::Create(stub_->channel_.get(), stub_->rpcmethod_DownloadImage_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncDownloadImageRaw(::grpc::ClientContext* context, const ::dmi::DownloadImageRequest& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_DownloadImage_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::PrepareAsyncDownloadImageRaw(::grpc::ClientContext* context, const ::dmi::DownloadImageRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_DownloadImage_, context, request, false, nullptr);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::ActivateImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request) {
  return ::grpc_impl::internal::ClientReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), rpcmethod_ActivateImage_, context, request);
}

void NativeSoftwareManagementService::Stub::experimental_async::ActivateImage(::grpc::ClientContext* context, ::dmi::HardwareID* request, ::grpc::experimental::ClientReadReactor< ::dmi::ImageStatus>* reactor) {
  ::grpc_impl::internal::ClientCallbackReaderFactory< ::dmi::ImageStatus>::Create(stub_->channel_.get(), stub_->rpcmethod_ActivateImage_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncActivateImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_ActivateImage_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::PrepareAsyncActivateImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_ActivateImage_, context, request, false, nullptr);
}

::grpc::ClientReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::RevertToStandbyImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request) {
  return ::grpc_impl::internal::ClientReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), rpcmethod_RevertToStandbyImage_, context, request);
}

void NativeSoftwareManagementService::Stub::experimental_async::RevertToStandbyImage(::grpc::ClientContext* context, ::dmi::HardwareID* request, ::grpc::experimental::ClientReadReactor< ::dmi::ImageStatus>* reactor) {
  ::grpc_impl::internal::ClientCallbackReaderFactory< ::dmi::ImageStatus>::Create(stub_->channel_.get(), stub_->rpcmethod_RevertToStandbyImage_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::AsyncRevertToStandbyImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_RevertToStandbyImage_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::dmi::ImageStatus>* NativeSoftwareManagementService::Stub::PrepareAsyncRevertToStandbyImageRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ImageStatus>::Create(channel_.get(), cq, rpcmethod_RevertToStandbyImage_, context, request, false, nullptr);
}

::grpc::ClientReader< ::dmi::ConfigResponse>* NativeSoftwareManagementService::Stub::UpdateStartupConfigurationRaw(::grpc::ClientContext* context, const ::dmi::ConfigRequest& request) {
  return ::grpc_impl::internal::ClientReaderFactory< ::dmi::ConfigResponse>::Create(channel_.get(), rpcmethod_UpdateStartupConfiguration_, context, request);
}

void NativeSoftwareManagementService::Stub::experimental_async::UpdateStartupConfiguration(::grpc::ClientContext* context, ::dmi::ConfigRequest* request, ::grpc::experimental::ClientReadReactor< ::dmi::ConfigResponse>* reactor) {
  ::grpc_impl::internal::ClientCallbackReaderFactory< ::dmi::ConfigResponse>::Create(stub_->channel_.get(), stub_->rpcmethod_UpdateStartupConfiguration_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::dmi::ConfigResponse>* NativeSoftwareManagementService::Stub::AsyncUpdateStartupConfigurationRaw(::grpc::ClientContext* context, const ::dmi::ConfigRequest& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ConfigResponse>::Create(channel_.get(), cq, rpcmethod_UpdateStartupConfiguration_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::dmi::ConfigResponse>* NativeSoftwareManagementService::Stub::PrepareAsyncUpdateStartupConfigurationRaw(::grpc::ClientContext* context, const ::dmi::ConfigRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::ConfigResponse>::Create(channel_.get(), cq, rpcmethod_UpdateStartupConfiguration_, context, request, false, nullptr);
}

::grpc::Status NativeSoftwareManagementService::Stub::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest& request, ::dmi::StartupConfigInfoResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_GetStartupConfigurationInfo_, context, request, response);
}

void NativeSoftwareManagementService::Stub::experimental_async::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest* request, ::dmi::StartupConfigInfoResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetStartupConfigurationInfo_, context, request, response, std::move(f));
}

void NativeSoftwareManagementService::Stub::experimental_async::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::StartupConfigInfoResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_GetStartupConfigurationInfo_, context, request, response, std::move(f));
}

void NativeSoftwareManagementService::Stub::experimental_async::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest* request, ::dmi::StartupConfigInfoResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetStartupConfigurationInfo_, context, request, response, reactor);
}

void NativeSoftwareManagementService::Stub::experimental_async::GetStartupConfigurationInfo(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::StartupConfigInfoResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_GetStartupConfigurationInfo_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::dmi::StartupConfigInfoResponse>* NativeSoftwareManagementService::Stub::AsyncGetStartupConfigurationInfoRaw(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::StartupConfigInfoResponse>::Create(channel_.get(), cq, rpcmethod_GetStartupConfigurationInfo_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::dmi::StartupConfigInfoResponse>* NativeSoftwareManagementService::Stub::PrepareAsyncGetStartupConfigurationInfoRaw(::grpc::ClientContext* context, const ::dmi::StartupConfigInfoRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::StartupConfigInfoResponse>::Create(channel_.get(), cq, rpcmethod_GetStartupConfigurationInfo_, context, request, false);
}

::grpc::ClientReader< ::dmi::UploadDebugInfoStatus>* NativeSoftwareManagementService::Stub::UploadDebugInfoRaw(::grpc::ClientContext* context, const ::dmi::UploadDebugInfoRequest& request) {
  return ::grpc_impl::internal::ClientReaderFactory< ::dmi::UploadDebugInfoStatus>::Create(channel_.get(), rpcmethod_UploadDebugInfo_, context, request);
}

void NativeSoftwareManagementService::Stub::experimental_async::UploadDebugInfo(::grpc::ClientContext* context, ::dmi::UploadDebugInfoRequest* request, ::grpc::experimental::ClientReadReactor< ::dmi::UploadDebugInfoStatus>* reactor) {
  ::grpc_impl::internal::ClientCallbackReaderFactory< ::dmi::UploadDebugInfoStatus>::Create(stub_->channel_.get(), stub_->rpcmethod_UploadDebugInfo_, context, request, reactor);
}

::grpc::ClientAsyncReader< ::dmi::UploadDebugInfoStatus>* NativeSoftwareManagementService::Stub::AsyncUploadDebugInfoRaw(::grpc::ClientContext* context, const ::dmi::UploadDebugInfoRequest& request, ::grpc::CompletionQueue* cq, void* tag) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::UploadDebugInfoStatus>::Create(channel_.get(), cq, rpcmethod_UploadDebugInfo_, context, request, true, tag);
}

::grpc::ClientAsyncReader< ::dmi::UploadDebugInfoStatus>* NativeSoftwareManagementService::Stub::PrepareAsyncUploadDebugInfoRaw(::grpc::ClientContext* context, const ::dmi::UploadDebugInfoRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncReaderFactory< ::dmi::UploadDebugInfoStatus>::Create(channel_.get(), cq, rpcmethod_UploadDebugInfo_, context, request, false, nullptr);
}

NativeSoftwareManagementService::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::GetSoftwareVersionInformationResponse>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::HardwareID* req,
             ::dmi::GetSoftwareVersionInformationResponse* resp) {
               return service->GetSoftwareVersion(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[1],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::DownloadImageRequest, ::dmi::ImageStatus>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::DownloadImageRequest* req,
             ::grpc_impl::ServerWriter<::dmi::ImageStatus>* writer) {
               return service->DownloadImage(ctx, req, writer);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[2],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::ImageStatus>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::HardwareID* req,
             ::grpc_impl::ServerWriter<::dmi::ImageStatus>* writer) {
               return service->ActivateImage(ctx, req, writer);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[3],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::HardwareID, ::dmi::ImageStatus>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::HardwareID* req,
             ::grpc_impl::ServerWriter<::dmi::ImageStatus>* writer) {
               return service->RevertToStandbyImage(ctx, req, writer);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[4],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::ConfigRequest, ::dmi::ConfigResponse>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::ConfigRequest* req,
             ::grpc_impl::ServerWriter<::dmi::ConfigResponse>* writer) {
               return service->UpdateStartupConfiguration(ctx, req, writer);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[5],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< NativeSoftwareManagementService::Service, ::dmi::StartupConfigInfoRequest, ::dmi::StartupConfigInfoResponse>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::StartupConfigInfoRequest* req,
             ::dmi::StartupConfigInfoResponse* resp) {
               return service->GetStartupConfigurationInfo(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeSoftwareManagementService_method_names[6],
      ::grpc::internal::RpcMethod::SERVER_STREAMING,
      new ::grpc::internal::ServerStreamingHandler< NativeSoftwareManagementService::Service, ::dmi::UploadDebugInfoRequest, ::dmi::UploadDebugInfoStatus>(
          [](NativeSoftwareManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::UploadDebugInfoRequest* req,
             ::grpc_impl::ServerWriter<::dmi::UploadDebugInfoStatus>* writer) {
               return service->UploadDebugInfo(ctx, req, writer);
             }, this)));
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

::grpc::Status NativeSoftwareManagementService::Service::UploadDebugInfo(::grpc::ServerContext* context, const ::dmi::UploadDebugInfoRequest* request, ::grpc::ServerWriter< ::dmi::UploadDebugInfoStatus>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace dmi


// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: dmi/hw_events_mgmt_service.proto

#include "dmi/hw_events_mgmt_service.pb.h"
#include "dmi/hw_events_mgmt_service.grpc.pb.h"

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

static const char* NativeEventsManagementService_method_names[] = {
  "/dmi.NativeEventsManagementService/ListEvents",
  "/dmi.NativeEventsManagementService/UpdateEventsConfiguration",
};

std::unique_ptr< NativeEventsManagementService::Stub> NativeEventsManagementService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< NativeEventsManagementService::Stub> stub(new NativeEventsManagementService::Stub(channel));
  return stub;
}

NativeEventsManagementService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_ListEvents_(NativeEventsManagementService_method_names[0], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_UpdateEventsConfiguration_(NativeEventsManagementService_method_names[1], ::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status NativeEventsManagementService::Stub::ListEvents(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::dmi::ListEventsResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_ListEvents_, context, request, response);
}

void NativeEventsManagementService::Stub::experimental_async::ListEvents(::grpc::ClientContext* context, const ::dmi::HardwareID* request, ::dmi::ListEventsResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_ListEvents_, context, request, response, std::move(f));
}

void NativeEventsManagementService::Stub::experimental_async::ListEvents(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::ListEventsResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_ListEvents_, context, request, response, std::move(f));
}

void NativeEventsManagementService::Stub::experimental_async::ListEvents(::grpc::ClientContext* context, const ::dmi::HardwareID* request, ::dmi::ListEventsResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_ListEvents_, context, request, response, reactor);
}

void NativeEventsManagementService::Stub::experimental_async::ListEvents(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::ListEventsResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_ListEvents_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::dmi::ListEventsResponse>* NativeEventsManagementService::Stub::AsyncListEventsRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::ListEventsResponse>::Create(channel_.get(), cq, rpcmethod_ListEvents_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::dmi::ListEventsResponse>* NativeEventsManagementService::Stub::PrepareAsyncListEventsRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::ListEventsResponse>::Create(channel_.get(), cq, rpcmethod_ListEvents_, context, request, false);
}

::grpc::Status NativeEventsManagementService::Stub::UpdateEventsConfiguration(::grpc::ClientContext* context, const ::dmi::EventsConfigurationRequest& request, ::dmi::EventsConfigurationResponse* response) {
  return ::grpc::internal::BlockingUnaryCall(channel_.get(), rpcmethod_UpdateEventsConfiguration_, context, request, response);
}

void NativeEventsManagementService::Stub::experimental_async::UpdateEventsConfiguration(::grpc::ClientContext* context, const ::dmi::EventsConfigurationRequest* request, ::dmi::EventsConfigurationResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_UpdateEventsConfiguration_, context, request, response, std::move(f));
}

void NativeEventsManagementService::Stub::experimental_async::UpdateEventsConfiguration(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::EventsConfigurationResponse* response, std::function<void(::grpc::Status)> f) {
  ::grpc_impl::internal::CallbackUnaryCall(stub_->channel_.get(), stub_->rpcmethod_UpdateEventsConfiguration_, context, request, response, std::move(f));
}

void NativeEventsManagementService::Stub::experimental_async::UpdateEventsConfiguration(::grpc::ClientContext* context, const ::dmi::EventsConfigurationRequest* request, ::dmi::EventsConfigurationResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_UpdateEventsConfiguration_, context, request, response, reactor);
}

void NativeEventsManagementService::Stub::experimental_async::UpdateEventsConfiguration(::grpc::ClientContext* context, const ::grpc::ByteBuffer* request, ::dmi::EventsConfigurationResponse* response, ::grpc::experimental::ClientUnaryReactor* reactor) {
  ::grpc_impl::internal::ClientCallbackUnaryFactory::Create(stub_->channel_.get(), stub_->rpcmethod_UpdateEventsConfiguration_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::dmi::EventsConfigurationResponse>* NativeEventsManagementService::Stub::AsyncUpdateEventsConfigurationRaw(::grpc::ClientContext* context, const ::dmi::EventsConfigurationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::EventsConfigurationResponse>::Create(channel_.get(), cq, rpcmethod_UpdateEventsConfiguration_, context, request, true);
}

::grpc::ClientAsyncResponseReader< ::dmi::EventsConfigurationResponse>* NativeEventsManagementService::Stub::PrepareAsyncUpdateEventsConfigurationRaw(::grpc::ClientContext* context, const ::dmi::EventsConfigurationRequest& request, ::grpc::CompletionQueue* cq) {
  return ::grpc_impl::internal::ClientAsyncResponseReaderFactory< ::dmi::EventsConfigurationResponse>::Create(channel_.get(), cq, rpcmethod_UpdateEventsConfiguration_, context, request, false);
}

NativeEventsManagementService::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeEventsManagementService_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< NativeEventsManagementService::Service, ::dmi::HardwareID, ::dmi::ListEventsResponse>(
          [](NativeEventsManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::HardwareID* req,
             ::dmi::ListEventsResponse* resp) {
               return service->ListEvents(ctx, req, resp);
             }, this)));
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      NativeEventsManagementService_method_names[1],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< NativeEventsManagementService::Service, ::dmi::EventsConfigurationRequest, ::dmi::EventsConfigurationResponse>(
          [](NativeEventsManagementService::Service* service,
             ::grpc_impl::ServerContext* ctx,
             const ::dmi::EventsConfigurationRequest* req,
             ::dmi::EventsConfigurationResponse* resp) {
               return service->UpdateEventsConfiguration(ctx, req, resp);
             }, this)));
}

NativeEventsManagementService::Service::~Service() {
}

::grpc::Status NativeEventsManagementService::Service::ListEvents(::grpc::ServerContext* context, const ::dmi::HardwareID* request, ::dmi::ListEventsResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeEventsManagementService::Service::UpdateEventsConfiguration(::grpc::ServerContext* context, const ::dmi::EventsConfigurationRequest* request, ::dmi::EventsConfigurationResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace dmi


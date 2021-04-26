// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: dmi/hw_metrics_mgmt_service.proto

#include "dmi/hw_metrics_mgmt_service.pb.h"
#include "dmi/hw_metrics_mgmt_service.grpc.pb.h"

#include <grpc++/impl/codegen/async_stream.h>
#include <grpc++/impl/codegen/async_unary_call.h>
#include <grpc++/impl/codegen/channel_interface.h>
#include <grpc++/impl/codegen/client_unary_call.h>
#include <grpc++/impl/codegen/method_handler_impl.h>
#include <grpc++/impl/codegen/rpc_service_method.h>
#include <grpc++/impl/codegen/service_type.h>
#include <grpc++/impl/codegen/sync_stream.h>
namespace dmi {

static const char* NativeMetricsManagementService_method_names[] = {
  "/dmi.NativeMetricsManagementService/ListMetrics",
  "/dmi.NativeMetricsManagementService/UpdateMetricsConfiguration",
  "/dmi.NativeMetricsManagementService/GetMetric",
  "/dmi.NativeMetricsManagementService/StreamMetrics",
};

std::unique_ptr< NativeMetricsManagementService::Stub> NativeMetricsManagementService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  std::unique_ptr< NativeMetricsManagementService::Stub> stub(new NativeMetricsManagementService::Stub(channel));
  return stub;
}

NativeMetricsManagementService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_ListMetrics_(NativeMetricsManagementService_method_names[0], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_UpdateMetricsConfiguration_(NativeMetricsManagementService_method_names[1], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_GetMetric_(NativeMetricsManagementService_method_names[2], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_StreamMetrics_(NativeMetricsManagementService_method_names[3], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  {}

::grpc::Status NativeMetricsManagementService::Stub::ListMetrics(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::dmi::ListMetricsResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_ListMetrics_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::dmi::ListMetricsResponse>* NativeMetricsManagementService::Stub::AsyncListMetricsRaw(::grpc::ClientContext* context, const ::dmi::HardwareID& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::dmi::ListMetricsResponse>(channel_.get(), cq, rpcmethod_ListMetrics_, context, request);
}

::grpc::Status NativeMetricsManagementService::Stub::UpdateMetricsConfiguration(::grpc::ClientContext* context, const ::dmi::MetricsConfigurationRequest& request, ::dmi::MetricsConfigurationResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_UpdateMetricsConfiguration_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::dmi::MetricsConfigurationResponse>* NativeMetricsManagementService::Stub::AsyncUpdateMetricsConfigurationRaw(::grpc::ClientContext* context, const ::dmi::MetricsConfigurationRequest& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::dmi::MetricsConfigurationResponse>(channel_.get(), cq, rpcmethod_UpdateMetricsConfiguration_, context, request);
}

::grpc::Status NativeMetricsManagementService::Stub::GetMetric(::grpc::ClientContext* context, const ::dmi::GetMetricRequest& request, ::dmi::GetMetricResponse* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_GetMetric_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::dmi::GetMetricResponse>* NativeMetricsManagementService::Stub::AsyncGetMetricRaw(::grpc::ClientContext* context, const ::dmi::GetMetricRequest& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::dmi::GetMetricResponse>(channel_.get(), cq, rpcmethod_GetMetric_, context, request);
}

::grpc::ClientReader< ::dmi::Metric>* NativeMetricsManagementService::Stub::StreamMetricsRaw(::grpc::ClientContext* context, const ::google::protobuf::Empty& request) {
  return new ::grpc::ClientReader< ::dmi::Metric>(channel_.get(), rpcmethod_StreamMetrics_, context, request);
}

::grpc::ClientAsyncReader< ::dmi::Metric>* NativeMetricsManagementService::Stub::AsyncStreamMetricsRaw(::grpc::ClientContext* context, const ::google::protobuf::Empty& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::dmi::Metric>(channel_.get(), cq, rpcmethod_StreamMetrics_, context, request, tag);
}

NativeMetricsManagementService::Service::Service() {
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeMetricsManagementService_method_names[0],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< NativeMetricsManagementService::Service, ::dmi::HardwareID, ::dmi::ListMetricsResponse>(
          std::mem_fn(&NativeMetricsManagementService::Service::ListMetrics), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeMetricsManagementService_method_names[1],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< NativeMetricsManagementService::Service, ::dmi::MetricsConfigurationRequest, ::dmi::MetricsConfigurationResponse>(
          std::mem_fn(&NativeMetricsManagementService::Service::UpdateMetricsConfiguration), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeMetricsManagementService_method_names[2],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< NativeMetricsManagementService::Service, ::dmi::GetMetricRequest, ::dmi::GetMetricResponse>(
          std::mem_fn(&NativeMetricsManagementService::Service::GetMetric), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      NativeMetricsManagementService_method_names[3],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< NativeMetricsManagementService::Service, ::google::protobuf::Empty, ::dmi::Metric>(
          std::mem_fn(&NativeMetricsManagementService::Service::StreamMetrics), this)));
}

NativeMetricsManagementService::Service::~Service() {
}

::grpc::Status NativeMetricsManagementService::Service::ListMetrics(::grpc::ServerContext* context, const ::dmi::HardwareID* request, ::dmi::ListMetricsResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeMetricsManagementService::Service::UpdateMetricsConfiguration(::grpc::ServerContext* context, const ::dmi::MetricsConfigurationRequest* request, ::dmi::MetricsConfigurationResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeMetricsManagementService::Service::GetMetric(::grpc::ServerContext* context, const ::dmi::GetMetricRequest* request, ::dmi::GetMetricResponse* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status NativeMetricsManagementService::Service::StreamMetrics(::grpc::ServerContext* context, const ::google::protobuf::Empty* request, ::grpc::ServerWriter< ::dmi::Metric>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace dmi


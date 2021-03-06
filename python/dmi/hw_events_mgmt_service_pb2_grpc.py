# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dmi import hw_events_mgmt_service_pb2 as dmi_dot_hw__events__mgmt__service__pb2
from dmi import hw_pb2 as dmi_dot_hw__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NativeEventsManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListEvents = channel.unary_unary(
                '/dmi.NativeEventsManagementService/ListEvents',
                request_serializer=dmi_dot_hw__pb2.HardwareID.SerializeToString,
                response_deserializer=dmi_dot_hw__events__mgmt__service__pb2.ListEventsResponse.FromString,
                )
        self.UpdateEventsConfiguration = channel.unary_unary(
                '/dmi.NativeEventsManagementService/UpdateEventsConfiguration',
                request_serializer=dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationResponse.FromString,
                )
        self.StreamEvents = channel.unary_stream(
                '/dmi.NativeEventsManagementService/StreamEvents',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dmi_dot_hw__events__mgmt__service__pb2.Event.FromString,
                )


class NativeEventsManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListEvents(self, request, context):
        """List the supported events for the passed device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEventsConfiguration(self, request, context):
        """Updates the configuration of the list of events in the request
        The default behavior of the device is to report all the supported events
        This configuration is persisted across reboots of the device or the device manager
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamEvents(self, request, context):
        """Initiate the server streaming of the events
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NativeEventsManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEvents,
                    request_deserializer=dmi_dot_hw__pb2.HardwareID.FromString,
                    response_serializer=dmi_dot_hw__events__mgmt__service__pb2.ListEventsResponse.SerializeToString,
            ),
            'UpdateEventsConfiguration': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEventsConfiguration,
                    request_deserializer=dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationRequest.FromString,
                    response_serializer=dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationResponse.SerializeToString,
            ),
            'StreamEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamEvents,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dmi_dot_hw__events__mgmt__service__pb2.Event.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dmi.NativeEventsManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NativeEventsManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeEventsManagementService/ListEvents',
            dmi_dot_hw__pb2.HardwareID.SerializeToString,
            dmi_dot_hw__events__mgmt__service__pb2.ListEventsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEventsConfiguration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeEventsManagementService/UpdateEventsConfiguration',
            dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationRequest.SerializeToString,
            dmi_dot_hw__events__mgmt__service__pb2.EventsConfigurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeEventsManagementService/StreamEvents',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dmi_dot_hw__events__mgmt__service__pb2.Event.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

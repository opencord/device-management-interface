# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from dmi import hw_management_service_pb2 as dmi_dot_hw__management__service__pb2
from dmi import hw_pb2 as dmi_dot_hw__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class NativeHWManagementServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartManagingDevice = channel.unary_stream(
                '/dmi.NativeHWManagementService/StartManagingDevice',
                request_serializer=dmi_dot_hw__pb2.ModifiableComponent.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.StartManagingDeviceResponse.FromString,
                )
        self.StopManagingDevice = channel.unary_unary(
                '/dmi.NativeHWManagementService/StopManagingDevice',
                request_serializer=dmi_dot_hw__management__service__pb2.StopManagingDeviceRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.StopManagingDeviceResponse.FromString,
                )
        self.GetManagedDevices = channel.unary_unary(
                '/dmi.NativeHWManagementService/GetManagedDevices',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.ManagedDevicesResponse.FromString,
                )
        self.GetPhysicalInventory = channel.unary_stream(
                '/dmi.NativeHWManagementService/GetPhysicalInventory',
                request_serializer=dmi_dot_hw__management__service__pb2.PhysicalInventoryRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.PhysicalInventoryResponse.FromString,
                )
        self.GetHWComponentInfo = channel.unary_stream(
                '/dmi.NativeHWManagementService/GetHWComponentInfo',
                request_serializer=dmi_dot_hw__management__service__pb2.HWComponentInfoGetRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.HWComponentInfoGetResponse.FromString,
                )
        self.SetHWComponentInfo = channel.unary_unary(
                '/dmi.NativeHWManagementService/SetHWComponentInfo',
                request_serializer=dmi_dot_hw__management__service__pb2.HWComponentInfoSetRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.HWComponentInfoSetResponse.FromString,
                )
        self.SetLoggingEndpoint = channel.unary_unary(
                '/dmi.NativeHWManagementService/SetLoggingEndpoint',
                request_serializer=dmi_dot_hw__management__service__pb2.SetLoggingEndpointRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.FromString,
                )
        self.GetLoggingEndpoint = channel.unary_unary(
                '/dmi.NativeHWManagementService/GetLoggingEndpoint',
                request_serializer=dmi_dot_hw__pb2.Uuid.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.GetLoggingEndpointResponse.FromString,
                )
        self.SetMsgBusEndpoint = channel.unary_unary(
                '/dmi.NativeHWManagementService/SetMsgBusEndpoint',
                request_serializer=dmi_dot_hw__management__service__pb2.SetMsgBusEndpointRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.FromString,
                )
        self.GetMsgBusEndpoint = channel.unary_unary(
                '/dmi.NativeHWManagementService/GetMsgBusEndpoint',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.GetMsgBusEndpointResponse.FromString,
                )
        self.GetLoggableEntities = channel.unary_unary(
                '/dmi.NativeHWManagementService/GetLoggableEntities',
                request_serializer=dmi_dot_hw__management__service__pb2.GetLoggableEntitiesRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.GetLogLevelResponse.FromString,
                )
        self.SetLogLevel = channel.unary_unary(
                '/dmi.NativeHWManagementService/SetLogLevel',
                request_serializer=dmi_dot_hw__management__service__pb2.SetLogLevelRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.SetLogLevelResponse.FromString,
                )
        self.GetLogLevel = channel.unary_unary(
                '/dmi.NativeHWManagementService/GetLogLevel',
                request_serializer=dmi_dot_hw__management__service__pb2.GetLogLevelRequest.SerializeToString,
                response_deserializer=dmi_dot_hw__management__service__pb2.GetLogLevelResponse.FromString,
                )


class NativeHWManagementServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartManagingDevice(self, request, context):
        """Initializes context for a device and sets up required states
        In the call to StartManagingDevice, the fields of ModifiableComponent which are relevant
        and their meanings in this context is mentioned below:
        name = The unique name that needs to be assigned to this hardware;
        class = COMPONENT_TYPE_UNDEFINED;
        parent = nil;
        alias = Optional;
        asset_id = Optional;
        uri = IP Address of the Hardware;
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopManagingDevice(self, request, context):
        """Stop management of a device and clean up any context and caches for that device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManagedDevices(self, request, context):
        """Returns an object containing a list of devices managed by this entity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPhysicalInventory(self, request, context):
        """Get the HW inventory details of the Device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHWComponentInfo(self, request, context):
        """Get the details of a particular HW component
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetHWComponentInfo(self, request, context):
        """Sets the permissible attributes of a HW component
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLoggingEndpoint(self, request, context):
        """Sets the location to which logs need to be shipped
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoggingEndpoint(self, request, context):
        """Gets the configured location to which the logs are being shipped
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMsgBusEndpoint(self, request, context):
        """Sets the location of the Message Bus to which events and metrics are shipped
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMsgBusEndpoint(self, request, context):
        """Gets the configured location to which the events and metrics are being shipped
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLoggableEntities(self, request, context):
        """Gets the entities of a device on which log can be configured. A few are expected, like OS, PON Management etc.
        In general an entity is any item within an hardware system that can emit logs, e.g. service, process, subsystem,
        interface, package etc.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLogLevel(self, request, context):
        """Sets the log level for one or more devices for each given entity to a certain level.
        If only one EntitiesLogLevel is provided for the device and that request contains only a log level with
        no entity in the list it's assumed that the caller wants to set that level for all the entities.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLogLevel(self, request, context):
        """Gets the configured log level for a certain entity on a certain device.
        If no entity is specified in the request all the entities with their log level should be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NativeHWManagementServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartManagingDevice': grpc.unary_stream_rpc_method_handler(
                    servicer.StartManagingDevice,
                    request_deserializer=dmi_dot_hw__pb2.ModifiableComponent.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.StartManagingDeviceResponse.SerializeToString,
            ),
            'StopManagingDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.StopManagingDevice,
                    request_deserializer=dmi_dot_hw__management__service__pb2.StopManagingDeviceRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.StopManagingDeviceResponse.SerializeToString,
            ),
            'GetManagedDevices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManagedDevices,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.ManagedDevicesResponse.SerializeToString,
            ),
            'GetPhysicalInventory': grpc.unary_stream_rpc_method_handler(
                    servicer.GetPhysicalInventory,
                    request_deserializer=dmi_dot_hw__management__service__pb2.PhysicalInventoryRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.PhysicalInventoryResponse.SerializeToString,
            ),
            'GetHWComponentInfo': grpc.unary_stream_rpc_method_handler(
                    servicer.GetHWComponentInfo,
                    request_deserializer=dmi_dot_hw__management__service__pb2.HWComponentInfoGetRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.HWComponentInfoGetResponse.SerializeToString,
            ),
            'SetHWComponentInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SetHWComponentInfo,
                    request_deserializer=dmi_dot_hw__management__service__pb2.HWComponentInfoSetRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.HWComponentInfoSetResponse.SerializeToString,
            ),
            'SetLoggingEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLoggingEndpoint,
                    request_deserializer=dmi_dot_hw__management__service__pb2.SetLoggingEndpointRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.SerializeToString,
            ),
            'GetLoggingEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoggingEndpoint,
                    request_deserializer=dmi_dot_hw__pb2.Uuid.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.GetLoggingEndpointResponse.SerializeToString,
            ),
            'SetMsgBusEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMsgBusEndpoint,
                    request_deserializer=dmi_dot_hw__management__service__pb2.SetMsgBusEndpointRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.SerializeToString,
            ),
            'GetMsgBusEndpoint': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMsgBusEndpoint,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.GetMsgBusEndpointResponse.SerializeToString,
            ),
            'GetLoggableEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLoggableEntities,
                    request_deserializer=dmi_dot_hw__management__service__pb2.GetLoggableEntitiesRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.GetLogLevelResponse.SerializeToString,
            ),
            'SetLogLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLogLevel,
                    request_deserializer=dmi_dot_hw__management__service__pb2.SetLogLevelRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.SetLogLevelResponse.SerializeToString,
            ),
            'GetLogLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLogLevel,
                    request_deserializer=dmi_dot_hw__management__service__pb2.GetLogLevelRequest.FromString,
                    response_serializer=dmi_dot_hw__management__service__pb2.GetLogLevelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dmi.NativeHWManagementService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NativeHWManagementService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartManagingDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeHWManagementService/StartManagingDevice',
            dmi_dot_hw__pb2.ModifiableComponent.SerializeToString,
            dmi_dot_hw__management__service__pb2.StartManagingDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopManagingDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/StopManagingDevice',
            dmi_dot_hw__management__service__pb2.StopManagingDeviceRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.StopManagingDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetManagedDevices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/GetManagedDevices',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dmi_dot_hw__management__service__pb2.ManagedDevicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPhysicalInventory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeHWManagementService/GetPhysicalInventory',
            dmi_dot_hw__management__service__pb2.PhysicalInventoryRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.PhysicalInventoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHWComponentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dmi.NativeHWManagementService/GetHWComponentInfo',
            dmi_dot_hw__management__service__pb2.HWComponentInfoGetRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.HWComponentInfoGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetHWComponentInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/SetHWComponentInfo',
            dmi_dot_hw__management__service__pb2.HWComponentInfoSetRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.HWComponentInfoSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLoggingEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/SetLoggingEndpoint',
            dmi_dot_hw__management__service__pb2.SetLoggingEndpointRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoggingEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/GetLoggingEndpoint',
            dmi_dot_hw__pb2.Uuid.SerializeToString,
            dmi_dot_hw__management__service__pb2.GetLoggingEndpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMsgBusEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/SetMsgBusEndpoint',
            dmi_dot_hw__management__service__pb2.SetMsgBusEndpointRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.SetRemoteEndpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMsgBusEndpoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/GetMsgBusEndpoint',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            dmi_dot_hw__management__service__pb2.GetMsgBusEndpointResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLoggableEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/GetLoggableEntities',
            dmi_dot_hw__management__service__pb2.GetLoggableEntitiesRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.GetLogLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLogLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/SetLogLevel',
            dmi_dot_hw__management__service__pb2.SetLogLevelRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.SetLogLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLogLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dmi.NativeHWManagementService/GetLogLevel',
            dmi_dot_hw__management__service__pb2.GetLogLevelRequest.SerializeToString,
            dmi_dot_hw__management__service__pb2.GetLogLevelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

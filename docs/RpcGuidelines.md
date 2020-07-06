# RPC Implementation Guidelines

This page specifies the expected behaviour of RPCs for an implementation of the Device Manager.

## Unimplemented features

If a feature present in the Device Management Interface API, as described in .proto files, is not implemented by the
Device Manager component for a particular device or set of devices, it is required that the component returns a
gRPC `UNIMPLEMENTED (12)` error code for that API. More details on the gRPC codes can be found in
the [gRPC specification](https://grpc.github.io/grpc/core/md_doc_statuscodes.html).

The response for a certain API can change depending on the state of underlying device(s). As an example,
a bare minimum device with no software installed on it that has just BMC might support only image management APIs but
not events and metrics, returning `UNIMPLEMENTED` for these.

Once a fully fledged software is installed on the device through BMC then the RPC responses for events and metrics will
contain the elements that the device supports through a more complete protocol and set of calls.

## API Specific details

Each API of the `.protos` contained in the [protos](../protos/) directory has his set of specific elements that
need to be taken into account, such as how to generate events and handle different states of operations.
Please refer to each of those files.
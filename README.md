# Device Management Interface

## Overview

This repository holds the `.proto` files and documentation for the device management interface.

The proto files and APIs are based on [RFC-8348](https://tools.ietf.org/html/rfc8348) from IETF and WT-383 from BBF
and are intended to be used over gRPC to communicate from an NMS/EMS to a device manager.
The device manager will then translate the commands to the device native interface (e.g. Redfish or NETCONF with
proprietary yang models).

Related documentations can be found in the [docs/](./docs) directory.

For anybody looking to implement a Device Manager component we suggest looking at the [RPC guidelines](docs/RpcGuidelines.md).
Each API in the `.proto` files has an explanation in its own `.md` file. Examples of the APIs can be found [here](docs/Examples.md)

## Meetings

Please join us in the weekly meeting:

Time: 8AM PST/5PM CET on Fridays

Meeting link: https://onf.zoom.us/j/92568509208

Agenda: [google doc](https://docs.google.com/document/d/16CIUUWGfYv9UGT4LxXuHHDvu1q9J4PYowlpijqL27F4/edit?usp=sharing)

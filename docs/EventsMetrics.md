# Events and Metrics

The events and periodic metrics are asynchronously sent out by implementations of a Device Manager. A Device Manager implementing this interface should write these to a Kafka bus.

Kafka has been chosen as a means to export from the device manager as it is suitable for handling asynchronous events. Persistence for the events and metrics can be easily achieved using Kafka. Moreover, Kafka gives the flexibility of handling and processing the events and metrics by different/multiple north-bound components/processes. Implementations could choose to have different services (with potentially multiple instances) handling the events and metrics.

![Events and Metrics](images/events_metrics.png "Events and Metrics flow")

The Kafka topics to which these are written should be configurable at startup of the components, so that different deployments have the flexibility of choosing those.
The recommendation is to use **dm.events** for the events and **dm.metrics** for the metrics as the names of the Kafka topics.

The two protobuf messages which are used for this are:

```protobuf
message Metric {
    MetricNames metric_id = 1;
    MetricMetaData metric_metadata = 2;
    ComponentSensorData value = 3;
}

// Asynchronous event message
message Event {
    EventMetaData event_metadata = 1;
    EventIds event_id = 2;
    google.protobuf.Timestamp raised_ts = 3;
    // Optional threshold information for an event
    ThresholdInformation threshold_info = 4;
    // Any additional info regarding the event
    string add_info = 5;
    // For component state change events, conveys the old and new states
    StateChangeInfo state_change_info = 6;
    // For generic events (event_id = EVENT_COMPONENT_GENERIC_EVENT)
    GenericEventInfo generic_event_info = 7;
}
```

For state change events (such as `EVENT_COMPONENT_ADMIN_STATE_CHANGED`, `EVENT_COMPONENT_OPER_STATE_CHANGED`, etc.), the `state_change_info` field is populated. The `StateChangeInfo` message uses a `oneof` to represent the specific type of state change, ensuring only the relevant state change is set:

```protobuf
message StateChangeInfo {
    oneof state_change {
        AdminStateChange admin_state_change = 1;
        OperStateChange oper_state_change = 2;
        AlarmStateChange alarm_state_change = 3;
        UsageStateChange usage_state_change = 4;
        StandbyStateChange standby_state_change = 5;
    }
}

message AdminStateChange {
    ComponentAdminState old = 1;
    ComponentAdminState new = 2;
}
message OperStateChange {
    ComponentOperState old = 1;
    ComponentOperState new = 2;
}
message AlarmStateChange {
    ComponentAlarmState old = 1;
    ComponentAlarmState new = 2;
}
message UsageStateChange {
    ComponentUsageState old = 1;
    ComponentUsageState new = 2;
}
message StandbyStateChange {
    ComponentStandbyState old = 1;
    ComponentStandbyState new = 2;
}
```

> See [protos/dmi/hw_events_mgmt_service.proto](protos/dmi/hw_events_mgmt_service.proto) for the authoritative definitions.

Note: The on-demand metrics query using the API `GetMetric` is returned over gRPC and not over the Kafka bus.

The device/device manager implementations shall persist the active events across device reboot. On device reboot, the alarms which are no longer active shall be cleared.

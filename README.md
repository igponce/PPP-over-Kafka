# PPP-Over Kafka Transport

## Why?

1 - Because we can!
2 - To filter, document, log traffic.
3 - To REPLAY network traffic :-)
4 - To INTERCEPT data leaks?

## Scenario

[ Your PC ] --- PPP Link (over Kafka ) --- [ Some Gateway ]

### How?

We'll need two topics for the connection: Rx, and TX topics.

PPP --> Kafka_gw --> Tx_topic --> Kafka_gw --> PPP

PPP <-- Kafka_gw <-- RX Topic <-- Kafka_gw <-- PPP

### Real-time content stripping
# Now we'll use some KSQL to remove payloads from the data stream.
# Yes, TCP Streams.


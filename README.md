<<<<<<< HEAD
# PPP-Over Kafka Transport

## Why?

1 - Because we can!
2 - To filter, document, log traffic.
3 - To REPLAY network traffic :-)
4 - To INTERCEPT data leaks?

## Scenario
=======
# PPPoK : PPP over Kafka Transport

This set of scripts is meant to setup a PPP link on a *nix box using Kafka as a transport "protocol".

## *Why the #@! do you want to do that?

Sometimes you receive data from IoT, embedded controllers in UDP form and you need a way to *reliably* store (and later) forward that data to destintation in a reliable manner.
... or maybe you just need to have an audit log on a unmodifiable system...
... or you want to store communications that you can replay layer (great for debugging)...

So, we're building a small swiss army knife using Kafka as the blade, wirecutter, can opener, etc...

## Initial Idea

Back in 2001, Scott Bronston wrote an interesting [PPP-SSH tunneling howto](http://www.tldp.org/HOWTO/ppp-ssh/).
In his paper, Scott told us to use the (relatively) unknown use of PPP with a pipe (in the unix world anything that could be done with a socket can also be done to a file, pipe, named pipe, etc...).

The novel idea was using ssh on the other end of the pipe, plus a second PPP daemon in the remote host.

Orignal_host | PPP | -> | SSH | --> Remote_host | PPPd|

All the "magic" here was done using [PPPd](https://linux.die.net/man/8/pppd) *pty* option

## Implementation scenario
>>>>>>> 455a05928f6927cf5be40b73593060a4f859c9e2

[ Your PC ] --- PPP Link (over Kafka ) --- [ Some Gateway ]

### How?

We'll need two topics for the connection: Rx, and TX topics.

PPP --> Kafka_gw --> Tx_topic --> Kafka_gw --> PPP

PPP <-- Kafka_gw <-- RX Topic <-- Kafka_gw <-- PPP

<<<<<<< HEAD
### Real-time content stripping
# Now we'll use some KSQL to remove payloads from the data stream.
# Yes, TCP Streams.
=======

## Use cases - 

- To ( filter / document / log ) network traffic.
- To REPLAY network traffic :-)
- To INTERCEPT data leaks?

>>>>>>> 455a05928f6927cf5be40b73593060a4f859c9e2


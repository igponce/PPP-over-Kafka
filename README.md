# PPPoK : PPP over Kafka Transport

This set of scripts is meant to setup a PPP link on a *nix box using Kafka as a transport "protocol".

*Why the #@! do you want to do that?

Sometimes you receive data from IoT, embedded controllers in UDP form and you need a way to *reliably* store (and later) forward that data to destintation in a reliable manner.
... or maybe you just need to have an audit log on a unmodifiable system...
... or you want to store communications that you can replay layer (great for debugging)...

So, we're building a small swiss army knife using Kafka as the blade, wirecutter, can opener, etc...

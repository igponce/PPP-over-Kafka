# PPPd Kafka Transporter
#
# Base: Debian
#     Paquetes necesarios:
# - Librdkafka
# - ippd (debian)
# - kafka (base)

# Para configuración:
#    ZK_QUORUM: _____
#    BOOTSTRAP_SERVERS: ____
#    upstream_topic: ____
#    downstream_topic: ____
   
FROM debian:stretch
   RUN apt-get update
   RUN apt-get install -y ppp
   RUN echo "PPP installed"
   RUN apt-get install -y python3-confluent-kafka
   RUN apt-get install -y openjdk-8-jre-headless

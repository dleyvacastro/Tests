FROM python:latest
WORKDIR /app
# ------------------------------
# Copy the application source code to the container
# ------------------------------
ADD runinit.sh runinit.sh
ADD software software
# ------------------------------
# Installing main apps and dependencies
# ------------------------------

# ENV DB_HOST='localhost'
# ENV DB_NAME='maticas'
# ENV DB_USER='dave'
# ENV DB_PASSWORD='0000'
# ENV DB_SSLMODE='disable'
# ENV MQTT_BROKER='localhost'
# ENV MQTT_PORT=1883
# ENV MQTT_USERNAME='dio'
# ENV MQTT_PASSWORD='123'
# ENV MQTT_CLIENT_ID='listener'

RUN apt update && apt upgrade -y \
    && apt install -y mosquitto mosquitto-clients \
    && apt install -y postgresql \
    && apt install -y iproute2 \
    && apt autoremove \
    && apt clean \
    && rm -rf /etc/mosquitto/* \
    && pip install pycairo \
    && pip install matplotlib \
    && pip install python-dotenv \
    && pip install flask \
    && pip install pandas \
    && pip install paho-mqtt \
    && pip install psycopg2 \
    && pip install schedule \
    && pip install flask_mysqldb \
    && pip install dash \
#     && source software/venv/bin/activate \
    && chmod +x /app/runinit.sh

# ------------------------------
# Setting up mosquitto configuration
# ------------------------------
ADD mosquitto.conf /etc/mosquitto/mosquitto.conf
ADD passfile /etc/mosquitto/passfile
# RUN ip=$(ip a | grep -w "inet" | awk -F' ' 'FNR == 2 {print $2}' | awk -F'/' '{print $1}') \
#     && echo "listener 1883 $ip" >> /etc/mosquitto/mosquitto.conf \
#     && echo "mqtt_broker = \"$ip\"" >> /app/software/db_mqtt_interface/mqtt_python/dirty8w8.py \
#     && echo "mqtt_broker = \"$ip\"" >> /app/software/daemon/dirty9w9.py
# ------------------------------
# Setting up postgresql configuration
# ------------------------------
USER postgres
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER dave WITH PASSWORD '0000';" && \
    psql --command "CREATE DATABASE maticas WITH OWNER dave;" && \
    psql --command "GRANT ALL PRIVILEGES ON DATABASE maticas TO dave;"

USER root
RUN /etc/init.d/postgresql start && \
    cd /app/software/db_mqtt_interface/db && \
    python ./main.py
EXPOSE 1883 5000
#CMD ["/usr/sbin/mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]
# -------------------------------
# Setting up the application server
# -------------------------------
CMD /app/runinit.sh


FROM postgres:latest AS base

RUN mkdir keys certs pgconf
RUN chmod og-rwx keys certs pgconf
COPY pg_hba.conf pgconf
COPY postgresql.conf pgconf

# Create a key-pair that will serve both as the root CA and the server key-pair
RUN openssl req -new -x509 -days 365 -nodes -out certs/ca.crt -keyout keys/ca.key -subj "/CN=root-ca"
RUN cp certs/ca.crt pgconf/ca.crt

# Create the server key and CSR and sign with root key
RUN openssl req -new -nodes -out server.csr -keyout pgconf/server.key -subj "/CN=localhost"
RUN openssl x509 -req -in server.csr -days 365 -CA certs/ca.crt -CAkey keys/ca.key -CAcreateserial -out pgconf/server.crt && rm server.csr

# Client Certs
RUN openssl req -new -nodes -out client.csr -keyout keys/client.key -subj "/CN=erpv"
RUN chmod og-rwx keys/*
RUN chmod og-rwx certs/*
RUN chmod og-rwx pgconf/*
RUN chown -R postgres:postgres pgconf
RUN openssl x509 -req -in client.csr -days 365 -CA certs/ca.crt -CAkey keys/ca.key -CAcreateserial -out certs/client.crt && rm client.csr

CMD ["-c", "config_file=pgconf/postgresql.conf"]
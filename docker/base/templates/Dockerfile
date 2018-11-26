FROM gigaquads-base:latest

ARG FREEZE=false

COPY scripts /scripts
RUN chmod +x /scripts/*

RUN /scripts/build

CMD ["/scripts/entrypoint"]

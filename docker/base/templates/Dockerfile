{%- set project = project.context.project -%}
FROM registry.lib.land/gigaquads/base:latest

ARG FREEZE=false
ENV FREEZE=${FREEZE}

{% if build %}
ARG BUILD_DEST={{ build.dest }}
ARG BUILD_REPO_SERVER={{ build.repo.server }}
ARG BUILD_REPO_ORG={{ build.repo.org }}
ARG BUILD_REPO_NAME={{ build.repo.name }}
ARG BUILD_REPO_BRANCH={{ build.repo.branch}}
{% if build.repo.gitlab_host %}
ARG BUILD_REPO_GITLAB_HOST={{ build.repo.gitlab_host }}
ARG BUILD_REPO_GITLAB_TOKEN={{ build.repo.gitlab_token }}
{% endif %}

ENV BUILD_REPO_DEST=${BUILD_REPO_DEST} \
    BUILD_REPO_SERVER=${BUILD_REPO_SERVER} \
    BUILD_REPO_ORG=${BUILD_REPO_ORG} \
    BUILD_REPO_NAME=${BUILD_REPO_NAME} \
    BUILD_REPO_BRANCH=${BUILD_REPO_BRANCH} \
    BUILD_REPO_GITLAB_HOST=${BUILD_REPO_GITLAB_HOST} \
    BUILD_REPO_GITLAB_TOKEN=${BUILD_REPO_GITLAB_TOKEN}
{% endif %}

WORKDIR /src

COPY scripts /scripts
RUN chmod +x /scripts/*
RUN /scripts/debug
RUN /scripts/build

{% if expose %}
EXPOSE {{ expose }} 
{% endif %}

{% if entrypoint %}
ENTRYPOINT ["{{ entrypoint }}"]
{% endif %}

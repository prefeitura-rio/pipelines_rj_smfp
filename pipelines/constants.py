# -*- coding: utf-8 -*-
from enum import Enum


class constants(Enum):
    ######################################
    # Automatically managed,
    # please do not change these values
    ######################################
    # Docker image
    DOCKER_TAG = "AUTO_REPLACE_DOCKER_TAG"
    DOCKER_IMAGE_NAME = "AUTO_REPLACE_DOCKER_IMAGE"
    DOCKER_IMAGE = f"{DOCKER_IMAGE_NAME}:{DOCKER_TAG}"
    GCS_FLOWS_BUCKET = "datario-public"

    ######################################
    # Agent labels
    ######################################
    RJ_SMFP_AGENT_LABEL = "smfp"
    RJ_LOCAL_IPLAN_AGENT_LABEL = "local-iplan"

    ######################################
    # Other constants
    ######################################

    # DBT TRANSFORM
    GCS_BUCKET = {"prod": "rj-smfp_dbt", "dev": "rj-smfp-dev_dbt"}
    REPOSITORY_URL = "https://github.com/prefeitura-rio/queries-rj-smfp.git"

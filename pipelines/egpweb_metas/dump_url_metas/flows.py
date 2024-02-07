# -*- coding: utf-8 -*-
"""
Database dumping flows for segovi project
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.dump_url.flows import dump_url_flow
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import handler_inject_bd_credentials

from pipelines.constants import constants
from pipelines.egpweb_metas.dump_url_metas.schedules import (
    egpweb_dump_url_gsheets_daily_update_schedule,
)

smfp_gsheets_egpweb_flow = deepcopy(dump_url_flow)
smfp_gsheets_egpweb_flow.name = "SMFP: EGPWeb - Ingerir tabelas de URL"
smfp_gsheets_egpweb_flow.state_handlers = [handler_inject_bd_credentials]
smfp_gsheets_egpweb_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
smfp_gsheets_egpweb_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

smfp_gsheets_egpweb_default_parameters = {
    "materialize_to_datario": False,
}
smfp_gsheets_egpweb_flow = set_default_parameters(
    smfp_gsheets_egpweb_flow, default_parameters=smfp_gsheets_egpweb_default_parameters
)

smfp_gsheets_egpweb_flow.schedule = egpweb_dump_url_gsheets_daily_update_schedule

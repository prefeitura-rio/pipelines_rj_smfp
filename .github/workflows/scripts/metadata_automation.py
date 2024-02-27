# -*- coding: utf-8 -*-
from prefeitura_rio.actions.fetch_metadata import fetch_metadata_and_save
from prefeitura_rio.actions.metadata_to_dbt_schema import metadata_to_dbt_schema

if __name__ == "__main__":
    dataset_ids = ["recursos_humanos_ergon_comlurb"]
    fetch_metadata_and_save(dataset_ids=dataset_ids)
    metadata_to_dbt_schema(dataset_ids=dataset_ids)

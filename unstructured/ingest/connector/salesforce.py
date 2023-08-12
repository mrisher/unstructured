import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Type, List


from unstructured.ingest.interfaces import (
    BaseConnector,
    BaseConnectorConfig,
    BaseIngestDoc,
    ConnectorCleanupMixin,
    IngestDocCleanupMixin,
    StandardConnectorConfig,
)
from unstructured.ingest.logger import logger
from unstructured.utils import requires_dependencies

@dataclass
class SimpleSalesforceConfig(BaseConnectorConfig):
    """ Connector specific attributes"""
    salesforce_categories: List[str]
    salesforce_username: str
    salesforce_password: str
    salesforce_token: str
    recursive: bool = False

    @staticmethod
    def parse_folders(folder_str: str) -> List[str]:
        """Parses a comma separated string of Outlook folders into a list."""
        return [x.strip() for x in folder_str.split(",")]


class SalesforceIngestDoc(IngestDocCleanupMixin, BaseIngestDoc):
    @requires_dependencies(["simple_salesforce"], extras="salesforce")
    def get_file(self):
        super().get_file()


@requires_dependencies(["simple_salesforce"], extras="salesforce")
class SalesforceConnector(ConnectorCleanupMixin, BaseConnector):
    ingest_doc_cls: Type[SalesforceIngestDoc] = SalesforceIngestDoc

    def __init__(
        self,
        config: SimpleSalesforceConfig,
        standard_config: StandardConnectorConfig,
    ) -> None:
        super().__init__(standard_config, config)

    def initialize(self):
        pass

    def get_ingest_docs(self):
        return super().get_ingest_docs()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_injestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        datainegstionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(datainegstionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
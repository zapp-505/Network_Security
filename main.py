from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_injestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__ == '__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        datainegstionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(datainegstionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(datainegstionartifact,data_validation_config)
        logging.info("initiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
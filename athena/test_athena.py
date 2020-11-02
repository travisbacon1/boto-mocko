import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
import athena

class Example(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.batch_get_named_query_response = {
            'NamedQueries': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Database': 'string',
                    'QueryString': 'string',
                    'NamedQueryId': 'string',
                    'WorkGroup': 'string'
                },
            ],
            'UnprocessedNamedQueryIds': [
                {
                    'NamedQueryId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                }
            ]
        }
    
        cls.batch_get_query_execution_response = {
            'QueryExecutions': [
                {
                    'QueryExecutionId': 'string',
                    'Query': 'string',
                    'StatementType': 'DDL',
                    'ResultConfiguration': {
                        'OutputLocation': 'string',
                        'EncryptionConfiguration': {
                            'EncryptionOption': 'SSE_S3',
                            'KmsKey': 'string'
                        }
                    },
                    'QueryExecutionContext': {
                        'Database': 'string',
                        'Catalog': 'string'
                    },
                    'Status': {
                        'State': 'QUEUED',
                        'StateChangeReason': 'string',
                        'SubmissionDateTime': datetime(2015, 1, 1),
                        'CompletionDateTime': datetime(2015, 1, 1)
                    },
                    'Statistics': {
                        'EngineExecutionTimeInMillis': 123,
                        'DataScannedInBytes': 123,
                        'DataManifestLocation': 'string',
                        'TotalExecutionTimeInMillis': 123,
                        'QueryQueueTimeInMillis': 123,
                        'QueryPlanningTimeInMillis': 123,
                        'ServiceProcessingTimeInMillis': 123
                    },
                    'WorkGroup': 'string'
                },
            ],
            'UnprocessedQueryExecutionIds': [
                {
                    'QueryExecutionId': 'string',
                    'ErrorCode': 'string',
                    'ErrorMessage': 'string'
                },
            ]
        }

        cls.can_paginate_response = True

        # TODO: cls.create_data_catalog_response = {}

        cls.create_named_query_response = {
            'NamedQueryId': 'string'
        }
    
    @patch('boto3.client')
    def test_batch_get_named_query(self, athena_mock):
        athena_mock.return_value.batch_get_named_query.return_value = self.batch_get_named_query_response
        response = athena.batch_get_named_query()
        self.assertEqual(response, self.batch_get_named_query_response)

    @patch('boto3.client')
    def test_batch_get_query_execution(self, athena_mock):
        athena_mock.return_value.batch_get_query_execution.return_value = self.batch_get_query_execution_response
        response = athena.batch_get_query_execution()
        self.assertEqual(response, self.batch_get_query_execution_response)

    @patch('boto3.client')
    def test_can_paginate(self, athena_mock):
        athena_mock.return_value.can_paginate.return_value = self.can_paginate_response
        response = athena.can_paginate()
        self.assertEqual(response, self.can_paginate_response)

    @patch('boto3.client')
    def test_create_named_query_response(self, athena_mock):
        athena_mock.return_value.create_named_query.return_value = self.create_named_query_response
        response = athena.create_named_query()
        self.assertEqual(response, self.create_named_query_response)

if __name__ == '__main__':
    unittest.main()
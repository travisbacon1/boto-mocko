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

        cls.create_data_catalog_response = {}

        cls.create_named_query_response = {
            'NamedQueryId': 'string'
        }

        cls.create_work_group_response = {}

        cls.delete_data_catalog_response = {}

        cls.delete_work_group_response = {}

        cls.generate_presigned_url_response = "presigned_url"

        cls.get_data_catalog_response = {
            'DataCatalog': {
                'Name': 'string',
                'Description': 'string',
                'Type': 'LAMBDA',
                'Parameters': {
                    'string': 'string'
                }
            }
        }

        cls.get_database_response = {
            'Database': {
                'Name': 'string',
                'Description': 'string',
                'Parameters': {
                    'string': 'string'
                }
            }
        }
    
        cls.get_named_query_response = {
            'NamedQuery': {
                'Name': 'string',
                'Description': 'string',
                'Database': 'string',
                'QueryString': 'string',
                'NamedQueryId': 'string',
                'WorkGroup': 'string'
            }
        }

        cls.get_query_execution_response = {
            'QueryExecution': {
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
            }
        }

        cls.get_query_results_response = {
            'UpdateCount': 123,
            'ResultSet': {
                'Rows': [
                    {
                        'Data': [
                            {
                                'VarCharValue': 'string'
                            },
                        ]
                    },
                ],
                'ResultSetMetadata': {
                    'ColumnInfo': [
                        {
                            'CatalogName': 'string',
                            'SchemaName': 'string',
                            'TableName': 'string',
                            'Name': 'string',
                            'Label': 'string',
                            'Type': 'string',
                            'Precision': 123,
                            'Scale': 123,
                            'Nullable': 'NOT_NULL',
                            'CaseSensitive': True|False
                        },
                    ]
                }
            },
            'NextToken': 'string'
        }

        cls.get_table_metadata_response = {
            'TableMetadata': {
                'Name': 'string',
                'CreateTime': datetime(2015, 1, 1),
                'LastAccessTime': datetime(2015, 1, 1),
                'TableType': 'string',
                'Columns': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string'
                    },
                ],
                'PartitionKeys': [
                    {
                        'Name': 'string',
                        'Type': 'string',
                        'Comment': 'string'
                    },
                ],
                'Parameters': {
                    'string': 'string'
                }
            }
        }

        # cls.waiter = WaiterModel(waiter_json_model)

        cls.get_work_group_response = {
            'WorkGroup': {
                'Name': 'string',
                'State': 'ENABLED',
                'Configuration': {
                    'ResultConfiguration': {
                        'OutputLocation': 'string',
                        'EncryptionConfiguration': {
                            'EncryptionOption': 'SSE_S3',
                            'KmsKey': 'string'
                        }
                    },
                    'EnforceWorkGroupConfiguration': True,
                    'PublishCloudWatchMetricsEnabled': True,
                    'BytesScannedCutoffPerQuery': 123,
                    'RequesterPaysEnabled': True
                },
                'Description': 'string',
                'CreationTime': datetime(2015, 1, 1)
            }
        }

        cls.list_data_catalogs_response = {
            'DataCatalogsSummary': [
                {
                    'CatalogName': 'string',
                    'Type': 'LAMBDA'
                }
            ],
            'NextToken': 'string'
        }

        cls.list_databases_response = {
            'DatabaseList': [
                {
                    'Name': 'string',
                    'Description': 'string',
                    'Parameters': {
                        'string': 'string'
                    }
                }
            ],
            'NextToken': 'string'
        }

        cls.list_query_executions_response = {
            'QueryExecutionIds': [
                'string',
            ],
            'NextToken': 'string'
        }

        cls.list_table_metadata_response = {
            'TableMetadataList': [
                {
                    'Name': 'string',
                    'CreateTime': datetime(2015, 1, 1),
                    'LastAccessTime': datetime(2015, 1, 1),
                    'TableType': 'string',
                    'Columns': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string'
                        },
                    ],
                    'PartitionKeys': [
                        {
                            'Name': 'string',
                            'Type': 'string',
                            'Comment': 'string'
                        },
                    ],
                    'Parameters': {
                        'string': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }

        cls.list_tags_for_resource_response = {
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'NextToken': 'string'
        }

        cls.list_work_groups_response = {
            'WorkGroups': [
                {
                    'Name': 'string',
                    'State': 'ENABLED',
                    'Description': 'string',
                    'CreationTime': datetime(2015, 1, 1)
                },
            ],
            'NextToken': 'string'
        }

        cls.start_query_execution_response = {
            'QueryExecutionId': 'string'
        }

        cls.stop_query_execution_response = {}

        cls.tag_resource_response = {}

        cls.untag_resource_response = {}

        cls.update_data_catalog_response = {}

        cls.update_work_group_response = {}

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
    def test_create_data_catalog(self, athena_mock):
        athena_mock.return_value.create_data_catalog.return_value = self.create_data_catalog_response
        response = athena.create_data_catalog()
        self.assertEqual(response, self.create_data_catalog_response)

    @patch('boto3.client')
    def test_create_named_query_response(self, athena_mock):
        athena_mock.return_value.create_named_query.return_value = self.create_named_query_response
        response = athena.create_named_query()
        self.assertEqual(response, self.create_named_query_response)
    
    @patch('boto3.client')
    def test_create_work_group_response(self, athena_mock):
        athena_mock.return_value.create_work_group.return_value = self.create_work_group_response
        response = athena.create_work_group()
        self.assertEqual(response, self.create_work_group_response)

    @patch('boto3.client')
    def test_delete_data_catalog(self, athena_mock):
        athena_mock.return_value.delete_data_catalog.return_value = self.delete_data_catalog_response
        response = athena.delete_data_catalog()
        self.assertEqual(response, self.delete_data_catalog_response)
    
    @patch('boto3.client')
    def test_delete_work_group(self, athena_mock):
        athena_mock.return_value.delete_work_group.return_value = self.delete_work_group_response
        response = athena.delete_work_group()
        self.assertEqual(response, self.delete_work_group_response)

    @patch('boto3.client')
    def test_generate_presigned_url(self, athena_mock):
        athena_mock.return_value.generate_presigned_url.return_value = self.generate_presigned_url_response
        response = athena.generate_presigned_url()
        self.assertEqual(response, self.generate_presigned_url_response)

    @patch('boto3.client')
    def test_get_data_catalog(self, athena_mock):
        athena_mock.return_value.get_data_catalog.return_value = self.get_data_catalog_response
        response = athena.get_data_catalog()
        self.assertEqual(response, self.get_data_catalog_response)

    @patch('boto3.client')
    def test_get_database(self, athena_mock):
        athena_mock.return_value.get_database.return_value = self.get_database_response
        response = athena.get_database()
        self.assertEqual(response, self.get_database_response)

    @patch('boto3.client')
    def test_get_named_query(self, athena_mock):
        athena_mock.return_value.get_named_query.return_value = self.get_named_query_response
        response = athena.get_named_query()
        self.assertEqual(response, self.get_named_query_response)

    @patch('boto3.client')
    def test_get_query_execution(self, athena_mock):
        athena_mock.return_value.get_query_execution.return_value = self.get_query_execution_response
        response = athena.get_query_execution()
        self.assertEqual(response, self.get_query_execution_response)
    
    @patch('boto3.client')
    def test_get_query_results(self, athena_mock):
        athena_mock.return_value.get_query_results.return_value = self.get_query_results_response
        response = athena.get_query_results()
        self.assertEqual(response, self.get_query_results_response)

    @patch('boto3.client')
    def test_get_table_metadata(self, athena_mock):
        athena_mock.return_value.get_table_metadata.return_value = self.get_table_metadata_response
        response = athena.get_table_metadata()
        self.assertEqual(response, self.get_table_metadata_response)

    # @patch('boto3.client')
    # def test_get_waiter(self, athena_mock):
    #     athena_mock.return_value.get_waiter.return_value = self.get_waiter_response
    #     response = athena.get_waiter()
    #     self.assertEqual(response, self.get_waiter_response)

    @patch('boto3.client')
    def test_get_work_group(self, athena_mock):
        athena_mock.return_value.get_work_group.return_value = self.get_work_group_response
        response = athena.get_work_group()
        self.assertEqual(response, self.get_work_group_response)

    @patch('boto3.client')
    def test_list_data_catalogs(self, athena_mock):
        athena_mock.return_value.list_data_catalogs.return_value = self.list_data_catalogs_response
        response = athena.list_data_catalogs()
        self.assertEqual(response, self.list_data_catalogs_response)

    @patch('boto3.client')
    def test_list_databases(self, athena_mock):
        athena_mock.return_value.list_databases.return_value = self.list_databases_response
        response = athena.list_databases()
        self.assertEqual(response, self.list_databases_response)

    @patch('boto3.client')
    def test_list_databases(self, athena_mock):
        athena_mock.return_value.list_query_executions.return_value = self.list_query_executions_response
        response = athena.list_query_executions()
        self.assertEqual(response, self.list_query_executions_response)

    @patch('boto3.client')
    def test_list_table_metadata(self, athena_mock):
        athena_mock.return_value.list_table_metadata.return_value = self.list_table_metadata_response
        response = athena.list_table_metadata()
        self.assertEqual(response, self.list_table_metadata_response)

    @patch('boto3.client')
    def test_list_tags_for_resource(self, athena_mock):
        athena_mock.return_value.list_tags_for_resource.return_value = self.list_tags_for_resource_response
        response = athena.list_tags_for_resource()
        self.assertEqual(response, self.list_tags_for_resource_response)

    @patch('boto3.client')
    def test_list_work_groups(self, athena_mock):
        athena_mock.return_value.list_work_groups.return_value = self.list_work_groups_response
        response = athena.list_work_groups()
        self.assertEqual(response, self.list_work_groups_response)

    @patch('boto3.client')
    def test_start_query_execution(self, athena_mock):
        athena_mock.return_value.start_query_execution.return_value = self.start_query_execution_response
        response = athena.start_query_execution()
        self.assertEqual(response, self.start_query_execution_response)

    @patch('boto3.client')
    def test_stop_query_execution(self, athena_mock):
        athena_mock.return_value.stop_query_execution.return_value = self.stop_query_execution_response
        response = athena.stop_query_execution()
        self.assertEqual(response, self.stop_query_execution_response)

    @patch('boto3.client')
    def test_tag_resource(self, athena_mock):
        athena_mock.return_value.tag_resource.return_value = self.tag_resource_response
        response = athena.tag_resource()
        self.assertEqual(response, self.tag_resource_response)
    
    @patch('boto3.client')
    def test_untag_resource(self, athena_mock):
        athena_mock.return_value.untag_resource.return_value = self.untag_resource_response
        response = athena.untag_resource()
        self.assertEqual(response, self.untag_resource_response)

    @patch('boto3.client')
    def test_update_data_catalog(self, athena_mock):
        athena_mock.return_value.update_data_catalog.return_value = self.update_data_catalog_response
        response = athena.update_data_catalog()
        self.assertEqual(response, self.update_data_catalog_response)

    @patch('boto3.client')
    def test_update_work_group(self, athena_mock):
        athena_mock.return_value.update_work_group.return_value = self.update_work_group_response
        response = athena.update_work_group()
        self.assertEqual(response, self.update_work_group_response)

if __name__ == '__main__':
    unittest.main()
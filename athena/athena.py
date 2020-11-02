import boto3

def batch_get_named_query():
    athena = boto3.client('athena')
    response = athena.batch_get_named_query(
        NamedQueryIds=[
            'string'
        ]
    )
    return response

def batch_get_query_execution():
    athena = boto3.client('athena')
    response = athena.batch_get_query_execution(
        QueryExecutionIds=[
            'string'
        ]
    )
    return response

def can_paginate():
    athena = boto3.client('athena')
    response = athena.can_paginate("foo_bar_operation")
    return response

def create_named_query():
    athena = boto3.client('athena')
    response = athena.create_named_query(
        Name='string',
        Description='string',
        Database='string'
    )
    return response
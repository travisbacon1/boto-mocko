#!/bin/bash

aws_sdk=$1
boto3_call=$2

if [ $# -eq 0 ]
  then
    echo "Please select Boto3 client & API call to patch"
    select sdk in athena dynamoDB
    do
        aws_sdk=$sdk
        break
    done
    select boto3_call in $(cat ./athena/boto_calls.txt)
    do
        boto3_call=$boto3_call
        break
    done
fi

echo "Generating function & test for $aws_sdk client $boto3_call() API call"
echo ""

head -n 1 $aws_sdk/$aws_sdk.py > output_patch/$aws_sdk.py
echo "" >> output_patch/$aws_sdk.py

cat $aws_sdk/$aws_sdk.py | pcregrep -M  "def $boto3_call.(\n|.)*?return" >> output_patch/$aws_sdk.py

head -n 8 $aws_sdk/test_$aws_sdk.py > output_patch/test_$aws_sdk.py
echo "" >> output_patch/test_$aws_sdk.py
cat $aws_sdk/test_$aws_sdk.py | pcregrep -M  "$boto3_call\_response.(\n|.)*?cls" | sed '$d' >> output_patch/test_$aws_sdk.py

echo "    @patch('boto3.client')" >> output_patch/test_$aws_sdk.py
cat $aws_sdk/test_$aws_sdk.py | pcregrep -M  "def test_$boto3_call.(\n|.)*?self.assertEqual" >> output_patch/test_$aws_sdk.py
echo "" >> output_patch/test_$aws_sdk.py
tail -n 2 $aws_sdk/test_$aws_sdk.py >> output_patch/test_$aws_sdk.py

echo "Running unit test on patch"

python3 output_patch/test_$aws_sdk.py
rm -rf output_patch/__pycache__
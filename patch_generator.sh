#!/bin/bash

aws_sdk=$1
api_call=$2

echo "Generating function & test for $1 client $2() API call"
echo ""

head -n 1 $1/$1.py > output_patch/$1.py
echo "" >> output_patch/$1.py

cat $1/$1.py | pcregrep -M  "def $2.(\n|.)*?return" >> output_patch/$1.py

head -n 8 $1/test_$1.py > output_patch/test_$1.py
echo "" >> output_patch/test_$1.py
cat $1/test_$1.py | pcregrep -M  "$2_response.(\n|.)*?cls" | sed '$d' >> output_patch/test_$1.py

echo "    @patch('boto3.client')" >> output_patch/test_$1.py
cat $1/test_$1.py | pcregrep -M  "def test_$2.(\n|.)*?self.assertEqual" >> output_patch/test_$1.py
echo "" >> output_patch/test_$1.py
tail -n 2 $1/test_$1.py >> output_patch/test_$1.py

echo "Running unit test on patch"

python3 output_patch/test_$1.py
rm -rf output_patch/__pycache__
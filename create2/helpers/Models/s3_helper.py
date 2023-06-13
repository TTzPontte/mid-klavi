import logging
import requests
import boto3
from botocore.exceptions import ClientError


class S3Helper:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def save_to_s3(self, body, bucket_name, key):
        """Save data to S3."""
        try:
            self.s3_client.put_object(
                Body=body,
                Bucket=bucket_name,
                Key=key
            )
        except ClientError as e:
            logging.error(e)
            raise requests.exceptions.ClientError(f"Failed to save data to S3. Bucket: {bucket_name}, Key: {key}")

    def list_files_in_s3_bucket(self, bucket_name, enquiry_cpf, report_types):
        files = []
        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
            print(response)

            # Check if 'Contents' key is present in the response
            if 'Contents' in response:
                files.append(response['Contents'])
                return files
        return None

    def count_files_in_s3_bucket(self, enquiry_cpf, report_types):
        file_counts = {report_type: 0 for report_type in report_types}

        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket="openfinance-dev", Prefix=prefix)
            print(response)

            # Check if 'Contents' key is present in the response
            if 'Contents' in response:
                file_counts[report_type] = len(response['Contents'])
            else:
                file_counts[report_type] = 0

        return file_counts

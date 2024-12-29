import boto3

class Bucket:
    def __init__(self, identifier, region, profile=None):
        self.__profile = profile
        self.__region = region
        self.__session = self.create_session()
        self.__account_id = self.get_account_id()

        self.__bucket_name = f"{identifier}-{self.__account_id}-{region}-bucket"

    def create_bucket(self):
        s3_client = self.__session.client("s3")
        bucket_config = {'CreateBucketConfiguration': {'LocationConstraint': self.__region}} if self.__region != "us-east-1" else {}
        response = s3_client.create_bucket(
                Bucket=self.__bucket_name,
                **bucket_config
        )
        print(response)

    def get_account_id(self):
        return self.__session.client("sts").get_caller_identity().get("Account")

    def create_session(self):
        return boto3.Session(profile_name=self.__profile, region_name=self.__region)
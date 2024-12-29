from Bucket import Bucket
from config import bucket_config
import os
from botocore.exceptions import ProfileNotFound, EndpointConnectionError

def main():
    profile = bucket_config.get('profile', os.environ.get('AWS_DEFAULT_PROFILE'))
    region = bucket_config.get('region', os.environ.get('AWS_DEFAULT_REGION'))

    try:
        s3_bucket = Bucket(identifier=bucket_config['identifier'],
                           region=region,
                           profile=profile)
        s3_bucket.create_bucket()
    except (ProfileNotFound, EndpointConnectionError) as exc:
        print(f"[!!!! ERROR !!!!]: {exc}")

if __name__ == '__main__':
    main()
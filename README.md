#### Summary (TL; DR):
The first iteration of this activity attempts to create a unique s3 bucket in us-east-1 region. In future iterations, I will update the bucket with

1. Versioning 
2. Encryption (KMS, S3 Keys, Custom Keys)
3. Replication Rules

#### Description
The bucket name follows the pattern `<<UNIQUE_IDENTIFIER>>-<<ACCOUNT_ID>>-<<REGION_NAME>>-bucket`

- `<<UNIQUE_IDENTIFIER>>`: This parameter is configured with a random string to help make the bucket unique. Provided 
                           as input to the script.
- `<<ACCOUNT_ID>>`: This parameter is the account id in which the bucket is being created. Provided as input to the 
                    script
- `<<REGION_NAME>>`: This is the region in which the bucket is created. This is determined at run time.


#### Lessons Learnt:

1. If you are connecting to AWS using profile, then you create a session first using the appropriate
   1. `PROFILE_NAME`
   2. `REGION_NAME`
2. Using the session created, you can then create a client targeting the appropriate resource.
3. S3 naming standards does not allow upper case characters or hyphens in the bucket name.
4. If the bucket is being created in us-east-1 region then the parameter `CreateBucketConfiguration` cannot be passed 
   as us-east-1 is the default region for S3 bucket. This parameter is mandatory though if the region is not us-east-1.
5. You can optionally tie down the bucket AZ by providing the parameter `Location` also as part of 
   `CreateBucketConfiguration` parameter.
6. The script will not error out, if you retry to create an existing bucket programmatically 
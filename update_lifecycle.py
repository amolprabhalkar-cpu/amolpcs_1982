# update_lifecycle.py
import boto3

def update_lifecycle(bucket_name):
    s3 = boto3.client('s3')

    lifecycle_config = {
        'Rules': [
            {
                'ID': 'MoveToGlacierAfter30Days',
                'Filter': {'Prefix': ''},  # Apply to all objects
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ],
                'Expiration': {
                    'Days': 365
                }
            }
        ]
    }

    s3.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_config
    )

    print(f"✅ Lifecycle policy updated for bucket: {bucket_name}")

if __name__ == "__main__":
    # Apna bucket name yahan daalo
    bucket_name = "amolpcs126789"
    update_lifecycle(bucket_name)

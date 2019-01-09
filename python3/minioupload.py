# Import Minio library.
from minio import Minio
from minio.error import ResponseError

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('nextcloud.vm6.info:443',
                    access_key='abdulkerimak',
                    secret_key='platinumgoat98*/',
                    secure=True)

# Make a bucket with the make_bucket API call.
try:
    minioClient.fput_object('test', 'ak.pdf', 'ak.pdf')
except ResponseError as err:
               print(err)
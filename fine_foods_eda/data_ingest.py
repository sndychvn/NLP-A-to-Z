# https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/explore-data-blob
import tables

import pandas as pd

from azure.storage.blob import BlockBlobService

STORAGEACCOUNTNAME= "amazonfoodstorage"
STORAGEACCOUNTKEY= "FR6Uy/fHFs5NU7aGuRmuR67n8v8hWXo7mtcfKQ857JbwGwR2G0Vqo0ZfcOjDZ+Kl4RaHEMzuFOtJX0HYqg9WXw=="
LOCALFILENAME= "Reviews.csv"
CONTAINERNAME= "datanlp111220"
BLOBNAME= "Reviews.csv"

#download from blob
t1=time.time()
blob_service=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
blob_service.get_blob_to_path(CONTAINERNAME,BLOBNAME,LOCALFILENAME)
t2=time.time()
print(("It takes %s seconds to download "+BLOBNAME) % (t2 - t1))
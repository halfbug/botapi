from fastapi import APIRouter, HTTPException

# from google.cloud import storage

router = APIRouter()

# Initialize Google Cloud Storage client
# client = storage.Client()

# @router.get("/file/{file_name}", response_model=str)
# async def read_file(file_name: str):
#     try:
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         content = blob.download_as_string().decode("utf-8")
#         return content
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.post("/file/{file_name}", response_model=str)
# async def write_file(file_name: str, content: str):
#     try:
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         blob.upload_from_string(content)
#         return "File created successfully"
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.put("/file/{file_name}", response_model=str)
# async def update_file(file_name: str, content: str):
#     try:
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         blob.upload_from_string(content)
#         return "File updated successfully"
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @router.delete("/file/{file_name}", response_model=str)
# async def delete_file(file_name: str):
#     try:
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(file_name)
#         blob.delete()
#         return "File deleted successfully"
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
@router.get("/file/{file_name}", response_model=str)
async def read_file(file_name: str):
    try:
        # bucket = client.get_bucket(bucket_name)
        # blob = bucket.blob(file_name)
        # content = blob.download_as_string().decode("utf-8")
        return {"file": "content"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

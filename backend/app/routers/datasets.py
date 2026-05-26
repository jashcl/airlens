from fastapi import APIRouter, UploadFile, File
from ..schemas import DatasetUploadResponse
from ..services.data_loader import process_upload, load_latest_cleaned

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.post("/upload", response_model=DatasetUploadResponse)
async def upload_dataset(file: UploadFile = File(...)):
    return await process_upload(file)

@router.get("/latest")
def latest_dataset_info():
    df = load_latest_cleaned()
    return {"rows": len(df), "cities": sorted(df["City"].dropna().astype(str).unique().tolist()), "columns": list(df.columns)}

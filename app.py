import os
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.index import app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def serve_index():
    index_file = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "Shree Sudhakar Group API is running. Place index.html in root directory."}

@app.get("/admin")
async def serve_admin():
    admin_file = os.path.join(BASE_DIR, "admin.html")
    if os.path.exists(admin_file):
        return FileResponse(admin_file)
    return {"message": "Admin dashboard template not found."}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    print("\n" + "=" * 65)
    print("   SHREE SUDHAKAR GROUP - LOCAL SERVER")
    print("   ---------------------------------------------")
    print(f"   * Website:         http://localhost:{port}")
    print(f"   * Admin Portal:    http://localhost:{port}/admin")
    print(f"   * Health check:    http://localhost:{port}/api/health")
    print(f"   * Enquiry API:     http://localhost:{port}/api/enquiry")
    print("=" * 65 + "\n")
    uvicorn.run("app:app", host="127.0.0.1", port=port, reload=True)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI(title="P-Cubed Pro · Planning Dashboard")


@app.get("/")
async def root():
    return RedirectResponse(url="/prd-status.html")


# Serve all HTML pages under /  (inter-page links like href="delivery-plan.html" work as-is)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

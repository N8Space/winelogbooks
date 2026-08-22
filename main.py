from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Production API",
    description="FastAPI service hosted on Azure App Service",
    version="0.1.0",
)


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>FastAPI on Azure</title>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; justify-content: center; align-items: center; height: 90vh; margin: 0; background: #0f172a; color: #f8fafc; }
          .card { background: #1e293b; padding: 2.5rem; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); text-align: center; max-width: 480px; }
          h1 { margin-bottom: 0.5rem; color: #38bdf8; font-size: 1.75rem; }
          p { color: #94a3b8; line-height: 1.5; }
          a { display: inline-block; margin-top: 1rem; color: #38bdf8; text-decoration: none; font-weight: 600; }
          a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <div class="card">
          <h1>FastAPI Backend Active</h1>
          <p>CI/CD pipeline and custom domain routing are configured and working.</p>
          <a href="/docs" target="_blank">View Interactive API Docs &rarr;</a>
        </div>
      </body>
    </html>
    """


@app.get("/health")
async def health_check():
    return {"status": "healthy", "runtime": "Python 3.13"}
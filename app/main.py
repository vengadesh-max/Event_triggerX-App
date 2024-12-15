from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi.responses import HTMLResponse


# Correct imports
from app.triggers import router as triggers_router
from app.event_logs import router as event_logs_router
from app.database import create_tables

app = FastAPI(
    title="Event Trigger Platform",
    description="Platform to manage and log event triggers (API and Scheduled).",
    version="1.0.0",
)

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include API routers
app.include_router(triggers_router, prefix="/triggers", tags=["Triggers"])
app.include_router(event_logs_router, prefix="/event_logs", tags=["Event Logs"])


async def app_lifespan(app: FastAPI):
    """
    Lifespan event handler to manage application startup and shutdown tasks.
    """
    print("Initializing database...")
    create_tables()  # Initialize database during startup
    print("Database initialized successfully.")
    yield
    print("Shutting down...")


@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint of the application.
    """
    return HTMLResponse(
        content="""
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body style="text-align: center; margin-top: 20%;">
            <h1>Welcome to the Event Trigger Platform!</h1>
            <p>Click the button below to visit the API Documentation.</p>
            <a href="https://event-triggerx-app.onrender.com/docs" target="_blank">
                <button style="font-size: 16px; padding: 10px 20px; cursor: pointer;">
                    Go to API Docs
                </button>
            </a>
        </body>
    </html>
    """
    )

# FastAPI Test Project

A simple FastAPI-based REST API project with basic endpoints.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sakwangjin/fast-api-test.git
cd fast-api-test
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI) at http://localhost:8000/docs
- Alternative API documentation (ReDoc) at http://localhost:8000/redoc

## Available Endpoints

- GET `/`: Welcome message
- GET `/health`: Health check endpoint

## License

MIT
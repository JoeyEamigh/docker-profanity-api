import uvicorn

from app import app

"""Project entry point.

Init app, routes and launch server.
"""

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=False, debug=False)

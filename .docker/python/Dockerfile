ARG PYTHON_VERSION

FROM python:${PYTHON_VERSION:-3.10}-slim

WORKDIR /usr/src/app

# Install dependencies
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install debugpy for debugging
RUN pip install debugpy

# Copy application code
COPY app/ .

# Expose ports
EXPOSE 8000 5678

# Conditional CMD based on $DEBUG environment variable
CMD ["/bin/sh", "-c", "if [ \"$DEBUG\" = \"true\" ]; then python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 app.py; else python app.py; fi"]

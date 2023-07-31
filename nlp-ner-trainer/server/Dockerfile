# Stage 1: Node.js dependencies
FROM node:lts as node_stage
USER root
RUN npm install -g express body-parser cors spacy
WORKDIR /workspace

# Stage 2: Python dependencies
FROM python:3.10 as python_stage
WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip

# Stage 3: Final image
FROM node:lts

# Copy Node.js dependencies from node_stage
COPY --from=node_stage /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node_stage /usr/local/bin /usr/local/bin
COPY --from=node_stage /workspace /workspace

# Copy Python dependencies from python_stage
COPY --from=python_stage /usr/local/bin /usr/local/bin
COPY --from=python_stage /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=python_stage /usr/local/lib/libpython3.10.so.1.0 /usr/local/lib/libpython3.10.so.1.0

# Set the LD_LIBRARY_PATH environment variable for Python
ENV LD_LIBRARY_PATH /usr/local/lib

# Set the working directory
WORKDIR /workspace

# File name: Dockerfile
FROM rayproject/ray:2.9.0-aarch64

# Set the working dir for the container to /serve_app
WORKDIR /serve_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copies the local `fake.py` file into the WORKDIR
COPY embedding-image.py .
# RUN serve run embedding_image:clip_app_embedding
CMD ["serve run", "embedding_image:clip_app_embedding"]
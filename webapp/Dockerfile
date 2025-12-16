# Stage 1: Build virtualenv and install dependencies as root (standard practice for installing OS packages)
FROM debian:12-slim AS build

# Create a non-root user and group before installing packages
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Install OS-level dependencies needed for building Python packages (gcc, etc.)
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev

# Create the virtual environment
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel

# Build the virtualenv: Only re-execute this step when requirements.txt changes
FROM build AS build-venv
# Switch to the non-root user *for this stage only* to test permissions if necessary,
# but installing pip packages in /venv is fine to do as root during build time.
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Stage 3: The final runtime image (Distroless with Python3)
# Note: Distroless images generally prioritize security and have minimal tools
FROM gcr.io/distroless/python3-debian12

# Copy the non-root user and group definitions created in the 'build' stage
# This is crucial because distroless images don't have standard user management tools (like useradd)
COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /etc/group /etc/group
RUN chown -R appuser:appgroup /app

# Set the USER to run as the newly created non-root user 'appuser'
USER appuser

# Copy the virtualenv from the build-venv stage
COPY --from=build-venv /venv /venv

# Copy the application code from the host machine into the container's working directory
COPY . /app

# Set the working directory for subsequent instructions and the entrypoint
WORKDIR /app

# Define the command that runs when the container starts
ENTRYPOINT ["/venv/bin/python3", "psutil_example.py"]

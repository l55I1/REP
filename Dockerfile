FROM python:3.9-slim

# Set working directorys
WORKDIR /app

# Copy Python source files
COPY generate_property_checks.py .
COPY property_template.py.jinja .

# Install Jinja
RUN pip install Jinja2

# Command to run Python script
CMD ["sh", "-c", "python generate_property_checks.py"]

FROM python:3.9-slim

# Install dependencies (openjdk for Java, nodejs for JavaScript, and cleanup)
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get install -y openjdk-17-jdk

# Set working directorys
WORKDIR /app

# Copy Python, JavaScript, and Java source files
COPY python.py .
COPY javascript.js .
COPY Java.java .

# Compile Java file
RUN javac Java.java

# Command to run Python script, Node.js script, and Java class
CMD ["sh", "-c", "python python.py && node javascript.js && java Java"]

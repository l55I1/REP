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

COPY python_0_to_10.py .
COPY javascript_0_to_10.js .
COPY Java_0_to_10.java .

# Compile Java file
RUN javac Java.java
RUN javac Java_0_to_10.java

# Command to run Python script, Node.js script, and Java class
CMD ["sh", "-c", "echo random range: 0 to 1 && python python.py && node javascript.js && java Java && echo && echo random range: 0 to 10 && python python_0_to_10.py && node javascript_0_to_10.js && java Java_0_to_10"]

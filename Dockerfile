FROM python:3.9-slim

# Install dependencies (openjdk for Java, nodejs for JavaScript, and cleanup)
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get install -y openjdk-17-jdk

# Set working directorys
WORKDIR /app

# Copy Python, JavaScript, and Java source files
COPY python_small_tolerance.py .
COPY javascript_small_tolerance.js .
COPY Java_small_tolerance.java .

# Compile Java file
RUN javac Java_small_tolerance.java

# Command to run Python script, Node.js script, and Java class
CMD ["sh", "-c", "echo \"tolerance \" && for i in {10..20}; do echo -n \"     1e-\$i\"; done; echo && python python_small_tolerance.py && node javascript_small_tolerance.js && java Java_small_tolerance"]

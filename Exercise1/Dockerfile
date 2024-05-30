# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory in the container to /Exercise1
WORKDIR /Exercise1

# Copy the current directory contents into the container at /Exercise1
COPY . /Exercise1

# Install pip and upgrade it to the latest version
RUN python -m pip install --upgrade pip

# Install the required Python packages individually to better catch errors
RUN pip install matplotlib==3.4.3 && \
    pip install plotly_express==0.4.1 && \
    pip install pandas==1.2.4 && \
    pip install numpy==1.20.2 && \
    pip install dash==1.21.0 && \
    pip install scikit-learn==0.24.2


# Run ex1_0_setup.py when the container launches
CMD ["python", "src/ex1_0_setup.py"]

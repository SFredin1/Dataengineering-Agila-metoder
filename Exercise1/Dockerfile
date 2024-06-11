# Use the official Python 3.9 image from the Docker Hub
FROM python:3.9

# Set the working directory in the container to /Exercise1
WORKDIR /Exercise1

# Copy the current directory contents into the container at /Exercise1
COPY . /Exercise1

# Install pip and upgrade it to the latest version
RUN python -m pip install --upgrade pip

# Install the required Python packages
RUN pip install matplotlib plotly_express pandas numpy dash scikit-learn

# Run the print_packages.py script when the container launches
CMD ["python", "print_packages.py"]


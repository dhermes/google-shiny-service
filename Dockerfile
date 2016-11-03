FROM gcr.io/google_appengine/python

RUN virtualenv -p /opt/python3.5/bin/python3.5 /env

# Setting these environment variables are the same as running
# source /env/bin/activate.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Copy the application's requirements.txt and run pip to install all
# dependencies into the virtualenv.
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Add the application source code.
ADD . /app

# Expose gRPC and HTTP ports.
EXPOSE 50051
EXPOSE 8080

# Run the application.
CMD honcho start

FROM debian:8

# Install required build libraries
RUN apt-get update && apt-get install -y \
    devscripts \
    debhelper \
    build-essential

RUN mkdir -p /workspace
COPY src /workspace
WORKDIR /workspace

# The generated package will be moved into this folder
VOLUME /build

# Install build dependencies
RUN mk-build-deps -i -r -t 'apt-get -y'

# Create the debian package
ENTRYPOINT ["debuild", "--post-dpkg-buildpackage-hook=mv *.deb /build"]
CMD ["-us", "-uc"]

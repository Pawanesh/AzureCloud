FROM centos as build

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*


RUN yum -q -y update && yum -q -y install git
RUN yum -q -y update && yum -q -y install cmake
RUN yum -q -y update && yum -q -y install autoconf
RUN yum -q -y update && yum -q -y install libtool
RUN yum -q -y update && yum -q -y install pkg-config 

RUN yum -q -y update && yum -q -y install openssl
RUN git clone https://github.com/Microsoft/cpprestsdk.git casablanca
RUN cd casablanca
RUN mkdir build.release
RUN cd build.release
RUN cmake -G Ninja .. -DCMAKE_BUILD_TYPE=Release
RUN ninja

#RUN yum -q -y update && yum -q -y install libcpprest


WORKDIR /src
COPY CMakeLists.txt main.cpp ./
RUN cmake . && make

FROM centos as app

RUN cd /etc/yum.repos.d/
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN yum -q -y update && yum -q -y install openssl
RUN git clone https://github.com/Microsoft/cpprestsdk.git casablanca
RUN cd casablanca
RUN mkdir build.release
RUN cd build.debug
RUN cmake -G Ninja .. -DCMAKE_BUILD_TYPE=Release
RUN ninja

#RUN yum -q -y update && yum -q -y install  libcpprest
WORKDIR /app
COPY --from=build /src/main ./
STOPSIGNAL SIGTERM

EXPOSE 8080

ENTRYPOINT ["/app/main"]
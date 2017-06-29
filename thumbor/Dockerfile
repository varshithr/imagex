FROM python:2

VOLUME /data

# Things required for a python/pip environment
COPY system-requirements.txt /usr/src/app/system-requirements.txt
RUN  \
    awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }' /etc/apt/sources.list > /etc/apt/sources.list.d/backports.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y autoremove && \
    xargs apt-get -y -q install < /usr/src/app/system-requirements.txt && \
    apt-get clean

ENV HOME /usr/src/app
ENV SHELL bash
ENV WORKON_HOME /usr/src/app
WORKDIR /usr/src/app
ENV REDIS_PASS scriptbees

ENV REDIS_STORAGE_SERVER_HOST "localhost"
ENV REDIS_STORAGE_SERVER_PORT 6379
ENV REDIS_STORAGE_SERVER_DB 0
ENV REDIS_STORAGE_SERVER_PASSWORD "scriptbees"
ENV REDIS_RESULT_STORAGE_SERVER_HOST "localhost"
ENV REDIS_RESULT_STORAGE_SERVER_PORT 6379
ENV REDIS_RESULT_STORAGE_SERVER_DB 1
ENV REDIS_RESULT_STORAGE_SERVER_PASSWORD "localhost"
ENV REDIS_QUEUE_SERVER_HOST "redis"
ENV REDIS_QUEUE_SERVER_PORT 6379
ENV REDIS_QUEUE_SERVER_DB 2
ENV REDIS_QUEUE_SERVER_PASSWORD "scriptbees"

ARG DOCKERHOST=172.17.0.1
ENV DOCKERHOST ${DOCKERHOST}

RUN pip install argparse
RUN pip install envtpl==0.4.1
RUN pip install boto==2.42.0
RUN pip install botocore==1.2.11
RUN pip install dateutils==0.6.6
RUN pip install numpy==1.11.0
RUN pip install pyremotecv==0.5.0
RUN pip install remotecv==2.2.1
RUN pip install opencv-engine==1.0.1
RUN pip install thumbor==6.3.0
RUN pip install tc-aws==6.0.2
RUN pip install tc-core==0.4.0
RUN pip install tc-shortener==0.2.2
RUN pip install raven==5.15.0
RUN pip install tc-redis==1.0.1
RUN pip install pgmagick==0.6.5
RUN pip install graphicsmagick-engine==0.1.1
RUN pip install git+http://github.com/sbaechler/thumbor-universalimages.git

COPY conf/thumbor.conf.tpl /usr/src/app/thumbor.conf.tpl

RUN \
    ln /usr/lib/python2.7/dist-packages/cv2.x86_64-linux-gnu.so /usr/local/lib/python2.7/cv2.so && \
    ln /usr/lib/python2.7/dist-packages/cv.py /usr/local/lib/python2.7/cv.py

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["thumbor"]

EXPOSE 8000

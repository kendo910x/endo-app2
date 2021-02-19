From python

ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
RUN pip install Flask
COPY app.py /home/
CMD python /home/app.py

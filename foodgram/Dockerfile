FROM python:3.7-slim 

WORKDIR /app 

COPY requirements.txt /app 

RUN pip3 install -r /app/requirements.txt --no-cache-dir 

COPY . /app 

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]  


ENV DB_ENGINE django.db.backends.postgresql
ENV DB_NAME foodgram
ENV POSTGRES_USER postgres 
ENV POSTGRES_PASSWORD lomonosova372 
ENV DB_HOST db
ENV DB_PORT 5432 
ENV SECRET_KEY 'vabz0bm(@jzxw!pruv)5z*@om7jjqjwew-5kxy@f2ai9j$uy4u'

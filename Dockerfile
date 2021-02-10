FROM python:3.8

# Собираем только нужные исходниики
RUN set -ex && mkdir -p /flask_core/app_flask/
WORKDIR /flask_core/app_flask/
COPY app_flask .

WORKDIR /flask_core/
COPY ./main_flask.py ./requirements.txt ./

# Устанавливаем фласк. Предварительно создать на рабочей машине: sudo pipenv lock -r > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Пробрасываем волюмы и порты
VOLUME /flask_core/app_flask

EXPOSE 5000

# Запускаем фласк - в режиме отладки. Чтобы сразу изменения в коде отражались на фласке
ENV FLASK_APP /flask_core/main_flask.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

CMD ["flask","run"]


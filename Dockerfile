FROM python:3.12.4

WORKDIR /notes_ke

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
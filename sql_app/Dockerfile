FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD  main.py .


RUN pip3 install bcrypt cffi click cryptography ecdsa fastapi h11 passlib pyasn1 pycparser pydantic python-jose python-multipart SQLAlchemy SQLAlchemy-Utils starlette uvicorn


EXPOSE 8000

CMD ["uvicorn","sql_app.main:app","--host=0.0.0.0", "--reload"]
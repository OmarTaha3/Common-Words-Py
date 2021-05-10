#base image
FROM python
COPY . /OmarTaha's_Assighment_1
WORKDIR /OmarTaha's_Assighment_1
CMD python pycode.py
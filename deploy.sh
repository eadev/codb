# COMPLIAMOS EL CÓDIGO PARA GENERAR EL PAQUETE PIP
python setup.py bdist_wheel
# PUBLICAMOS EL RELEASE
# python -m twine upload dist/*

#INSTALACIÓN LOCAL
# python -m pip install dist/dokr-0.1-py3-none-any.whl
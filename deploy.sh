# COMPLIAMOS EL CÓDIGO PARA GENERAR EL PAQUETE PIP
python setup.py bdist_wheel

# PUBLICAMOS EL RELEASE
python -m twine upload dist/*

#INSTALACIÓN LOCAL
# python -m pip install dist/codb-1.0-py3-none-any.whl
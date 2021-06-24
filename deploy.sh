# ELIMINAMOS LA CARPETAS
rm -rf dist
rm -rf build
rm -rf codb.egg-info

# COMPLIAMOS EL CÓDIGO PARA GENERAR EL PAQUETE PIP
python setup.py bdist_wheel

# PUBLICAMOS EL RELEASE
# python -m twine upload dist/*

#INSTALACIÓN LOCAL
python -m pip install dist/codb-1.2.0-py3-none-any.whl --force-reinstall
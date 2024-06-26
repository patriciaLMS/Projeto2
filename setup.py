# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="adaptGame.py", icon="Recursos/icone4.ico") ]
cx_Freeze.setup(
    name = "Matemática e Euclides", 
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["Recursos"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi

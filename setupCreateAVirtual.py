from cx_Freeze import setup, Executable





executables = [Executable("createAVirtual.py")]

setup(
    name="Crear Asistente",
    version="0.1",
    description="Crea un Asistente Virtual con Rasa",
    executables=executables,
)
import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name = 'Super Dino',
    options = {
        "build_exe":{
                        "packages": ['pygame'],
                        "include_files": ['dino_runner']
                    }
              },
    executables = executables
)
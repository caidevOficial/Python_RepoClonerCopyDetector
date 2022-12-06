import os

# directories_filtered = list[str](
#     filter(
#             lambda file: 'Repositories' in file[0],
#             os.walk('.', topdown=False)
#         )
# )
# print(directories_filtered)


# directories_red = list[str](
#     filter(
#         lambda filename: filename.startwith('repositories'), 
#         directories_filtered
#     )
# )


# print(directories_red)
"""
[
    ('.\\Repositories\\test_files\\repo1', [], ['funciones.c', 'funciones.h', 'main.c']), 
    ('.\\Repositories\\test_files\\repo2\\TrabajoPractico1', [], ['funciones.c', 'funciones.h', 'funciones.o', 'main.c', 'main.o', 'TrabajoPractico1.cbp']), 
    ('.\\Repositories\\test_files\\repo2', ['TrabajoPractico1'], []), 
    ('.\\Repositories\\test_files', ['repo1', 'repo2'], []), 
    ('.\\Repositories\\test_files2', [], ['main.c', 'main2.c']), 
    ('.\\Repositories', ['test_files', 'test_files2'], [])
]       

"""

directories = list[str](filter(lambda file: 'Repositories' in file[0], os.walk('.', topdown=False)))
for sufix in ['.c', '.h']:
    for index in directories:
        if index[2]:
            files = list[str](filter(lambda file: str(file).endswith('.c'), index[2]))
            if files:
                for filename in files:
                    if not filename in ["spect.c", "spects.c"]:
                        file_path = os.path.join(index[0], filename)
                        file_stats = os.stat(file_path).st_size
                        print(file_path, file_stats)
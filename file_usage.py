import pathlib

current_directory = pathlib.Path(__file__).parent
files = current_directory.rglob("*")

biggest_files = {}
for file in files:
  if file.is_file():
    if not biggest_files.get(file.suffix):
      biggest_files[file.suffix] = []
    
    biggest_files[file.suffix].append(file)

for file_type in biggest_files:
   sorted_files = biggest_files[file_type]
   sorted_files.sort(key=lambda path: path.stat().st_size)
   print(f"{file_type} files")
   for file in sorted_files[-3:]:
    print(f"{file}: {round(file.stat().st_size/1000000, 2)} megabytes")
   print("\n")
  

from pathlib import Path

class InvalidFilePathError(Exception):
    pass

file_types = { 'image' : ['.jpg','.png','.jpeg','.gif'],
               'document' : ['.pdf','.docx','.txt'],
               'spreadsheet' : ['.xlsx','.numbers'],
               'audio' : ['.mp3','.wav','.flac'],
               'video' : ['.mp4', '.mkv', '.mov'],
               'archive' : ['.zip','.tar','.rar']}




while True:
    print("-------------------------------------\n")
    print("          HELLO!!!\n")
    print("  WELCOME TO THE FILE SORTER\n")
    print("HERE YOU CAN SORT FILES FOR ANY FOLDER\n")
    print("THE FOLLOWING KINDS OF FILES ARE SORTED:")
    print("1. IMAGES: .jpg, .png, .jpeg, .gif")
    print("2. DOCUMENTS: .pdf, .docx, .txt")
    print("3. SPREADSHEETS: .xlsx, .numbers")
    print("4. AUDIO: .mp3, .wav, .flac")
    print("5. VIDEO: .mp4, .mkv, .mov")
    print("6. ARCHIVE: .zip, .tar, .rar")
    print("WHAT WOULD YOU LIKE TO DO?\n")
    print(" (1) Sort files")
    print(" (2) Exit program\n")
    try:
        choice = int(input("Enter your choice (1 or 2): "))
    except ValueError:
        print("Please enter an integer (1 or 2)")
        continue
    print("\n")
    if (choice == 1):
        category = {'image':[],
                    'document':[],
                    'spreadsheet':[],
                    'audio':[],
                    'video':[],
                    'archive':[]}
        print("Please ensure that the program is allowed to access the desired folder.")
        print("Please enter the path of the desired folder.")
        print("The program will then sort all files in separate folders. ")
        path = input("Path: ")
        try:
            directory_path = Path(path)
            if (directory_path.exists() == False):
                raise InvalidFilePathError
            if (directory_path.is_dir() == False):
                raise InvalidFilePathError
            print("\n")
            print("GIVEN PATH POINTS TO:", directory_path.name)
            print("\nPROCEED?\n")
            print("(1) Yes \n(2) No")
            try: 
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter an integer (1 or 2)")
                continue
            if (choice == 1):
                print("\nThe given folder contains: \n")
                for file in directory_path.iterdir():
                    print(file.name)
                print("\n")
                for file in directory_path.iterdir():
                    for a in file_types.items():
                        k = a[0]
                        i = a[1]
                        for ext in i:
                            if (file.suffix.lower() == ext):
                                category[k] = category[k] + [file.name]
                
                for a in category.items():
                    k = a[0]
                    i = a[1]
                    for name in i:
                        if (k == 'image'):
                            new_folder = directory_path/'MY_IMAGES'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)


                        if (k == 'document'):
                            new_folder = directory_path/'MY_DOCUMENTS'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)

                        if (k == 'spreadsheet'):
                            new_folder = directory_path/'MY_SPREADSHEETS'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)


                        if (k == 'audio'):
                            new_folder = directory_path/'MY_AUDIO'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)


                        if (k == 'video'):
                            new_folder = directory_path/'MY_VIDEOS'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)


                        if (k == 'archive'):
                            new_folder = directory_path/'MY_ARCHIVES'
                            new_folder.mkdir(parents=True, exist_ok=True)
                            source_file = directory_path/name
                            destination = new_folder/name
                            if (source_file.is_file()):
                                print("\nMoving",name,"to",destination,"...")
                                source_file.rename(destination)


            elif (choice == 2):
                continue
        except InvalidFilePathError:
            if (directory_path.exists() == False):
                print("No such directory exists")
            if (directory_path.is_dir() == False):
                print("The given path does not point to a folder.")
            break
    else:
        break



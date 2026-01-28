import os
from config import FILE_CATEGORIES
from utils import get_file_extension, create_folder, safe_move

def organize_folder(target_folder):
    if not os.path.exists(target_folder):
        print("❌ Folder not found!")
        return

    print(f"📂 Organizing: {target_folder}\n")

    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)

        if os.path.isfile(file_path):
            ext = get_file_extension(file)
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if ext in extensions:
                    category_folder = os.path.join(target_folder, category)
                    create_folder(category_folder)
                    dest_path = os.path.join(category_folder, file)
                    safe_move(file_path, dest_path)
                    print(f"✅ {file} → {category}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(target_folder, "Others")
                create_folder(other_folder)
                dest_path = os.path.join(other_folder, file)
                safe_move(file_path, dest_path)
                print(f"📦 {file} → Others")

    print("\n🎉 Organization complete!")

if __name__ == "__main__":
    folder = input("📥 Enter folder path to organize: ")
    organize_folder(folder.strip())

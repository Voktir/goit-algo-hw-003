import sys
from pathlib import Path
from shutil import copy2

def main():
    try:
        if len(sys.argv) < 2:
            print("Невистачає аргументів: python main.py <вихідна директорія> <тека призначення у разі необхідності>")
            sys.exit(1)
        else:
            outp_path = Path(sys.argv[1])
            dist_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()/'dist'
            if (not outp_path.exists() or not outp_path.is_dir()):
                print("Вказана вихідна дерикторія не знайдена")
                return
            src_to_dst(outp_path, dist_path)
    except Exception as e:
        print("Чьто-то пошло нітак, помилка", e)

def src_to_dst(outp_p: Path, dist_p: Path):
    try:
        dist_p.mkdir(parents=True, exist_ok=True)
        for src_path in outp_p.iterdir():
            if (src_path.is_dir()):
                src_to_dst(src_path, dist_p)
            elif (src_path.is_file()):
                ext = src_path.suffix[1:]
                if ext == "":
                    ext = "no_ext"
                dst_path = dist_p/ext
                dst_path.mkdir(parents=True, exist_ok=True)
                copy2(src_path, dst_path)
            else:
                print(f"Тут {outp_p.name} щось незрозуміле {src_path.name}")
    except Exception as e:
        print("Помилка при операціях з папками/файлами", e)

if __name__ == "__main__":
    main()
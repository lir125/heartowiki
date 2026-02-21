# 빌드 전에 python312.dll을 _py_dll 폴더로 복사 (onefile 번들용)
import os
import shutil
import sys

def main():
    base = getattr(sys, "base_prefix", sys.prefix)
    for name in ["python312.dll", "python311.dll", "python310.dll"]:
        src = os.path.join(base, name)
        if os.path.isfile(src):
            dest_dir = os.path.join(os.path.dirname(__file__), "_py_dll")
            os.makedirs(dest_dir, exist_ok=True)
            dest = os.path.join(dest_dir, name)
            shutil.copy2(src, dest)
            print("Copied:", name, "->", dest_dir)
            return 0
    print("No python3xx.dll found in", base)
    return 1

if __name__ == "__main__":
    sys.exit(main())

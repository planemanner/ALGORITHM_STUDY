"""
Folder Hierarchy
- ROOT
  - REGION
    - DEFECT NAME
      - OK
      - NG
"""
import os
from shutil import copy
from glob import glob
from tqdm import tqdm


def send_file(file_name: str, tgt_dir):
    if file_name.endswith("OK_OK"):
        p = os.path.join(tgt_dir, "OK", os.path.basename(file_name))
        if not os.path.exists(os.path.join(tgt_dir, "OK")):
            os.makedirs(os.path.join(tgt_dir, "OK"))
    if file_name.endswith("NG_NG"):
        if not os.path.exists(os.path.join(tgt_dir, "NG")):
            os.makedirs(os.path.join(tgt_dir, "NG"))
        p = os.path.join(tgt_dir, "NG", os.path.basename(file_name))

    copy(file_name, p)

# OK / NG 단위로 끝낼 수 있게 함수 구성. Memory 에 잡고있지 않도록...


def ok_ng_level_sending(folder_path, tgt_dir):
    fmt = "jpg"
    file_list = glob(os.path.join(folder_path, f"*.{fmt}"))
    for file_path in file_list:
        send_file(file_path, tgt_dir=tgt_dir)


def main(src_dir, tgt_dir):
    region_names = os.listdir(src_dir)
    for region_name in tqdm(region_names):
        region_folder = os.path.join(src_dir, region_name)

        if os.path.isdir(region_folder):
            defect_names = os.listdir(region_folder)

            for defect_name in defect_names:
                defect_folder = os.path.join(region_folder, defect_name)

                if os.path.isdir(defect_folder):
                    ok_ng = os.listdir(defect_folder)
                    for status in ok_ng:
                        status_folder = os.path.join(defect_folder, status)
                        t_dir = os.path.join(tgt_dir, region_name, defect_name)
                        if not os.path.exists(t_dir):
                            os.makedirs(t_dir)

                        ok_ng_level_sending(status_folder, t_dir)


if __name__ == "__main__":
    src_dir = ""
    tgt_dir = ""
    main(src_dir, tgt_dir)
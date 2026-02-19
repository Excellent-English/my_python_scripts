from scripts.hin_id_validation import run_hin_validation
from scripts.dea_id_validation import run_dea_validation
import yaml
from os import path, rename, remove, listdir, stat
import glob
from time import sleep
import FreeSimpleGUI as sg
import sys
from datetime import datetime
import time
import logging

import pathlib


def run_validation():
    # Load Configuration
    with open("config.yaml") as f:

        data = yaml.load(f, Loader=yaml.FullLoader)
        baselocation = working_dir
        lookup_file_dea = working_dir + data["dea"]["files"]["lookup_file"]
        lookup_file_hin = working_dir + data["hin"]["files"]["lookup_file"]
        results_dea = working_dir + data["dea"]["files"]["results_file"]
        dea_db_file = working_dir + data["dea"]["files"]["dea_db_file"]
        results_hin = working_dir + data["hin"]["files"]["results_file"]
        matched_output = working_dir + data["customer"]["files"]["matched_output"]
        unmatched_output = working_dir + data["customer"]["files"]["unmatched_output"]
        cache_file = working_dir + data["customer"]["files"]["cache_file"]
        log_loc = working_dir + data["base"]["log_location"]
        log_level = data["base"]["log_level"]

    if log_level.lower() == "error":
        log_level = logging.ERROR
    elif log_level.lower() == "debug":
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(
        filename=log_loc + r"\run_validation_log.txt",
        filemode="w",
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    logging.info("Begin Validation Process")
    # Clear customer review cache file, and results files
    open(cache_file, "w").close()
    open(results_dea, "w").close()
    open(results_hin, "w").close()

    print(lookup_file_dea)
    print(lookup_file_hin)

    while True:
        sglayout = [
            [sg.Text("Did you update the DEA Database?")],
            [sg.Button("Yes"), sg.Button("No")],
        ]

        window = sg.Window("New Download File", layout=sglayout)
        event, values = window.read()

        if event == "Yes":
            # Check to see if the DEA Database exists, if so, remove it.
            dea_db = glob.glob(working_dir + r"\files\input\cs_active*")

            if len(dea_db) > 0:

                if path.exists(dea_db_file):
                    remove(dea_db_file)
                    rename(dea_db[0], dea_db_file)

            break
        else:
            # Continue with existing dea db file.
            break
    window.Close()

    # Clear and set headers for matched and unmatched files
    with open(matched_output, "w") as f:
        f.write("Customer, SAP Customer Name, DEA_HIN Name, dea_num, hin_num, status")
        f.write("\n")

    with open(unmatched_output, "w") as u:
        # Write file headers
        u.write(
            "DEA_Number,HIN_Number,name,dea_hin_cot,dea_hin_cot_description,address_line_1,"
            + "city,state,postal_code,sched,fee,dea_eff_date,dea_exp_date,hin_eff_date,hin_exp_date,status,recon_acct,"
            + "sales_district,sales_office,sales_group,distrib_center,fk_cot,fk_cot_description,price_list"
        )
        u.write("\n")

    # try:
    if path.exists(lookup_file_hin) and path.exists(lookup_file_dea):
        print("HIN/DEA Lookup files exist, proceeding to validation")

        run_hin_validation()

        run_dea_validation()

        print("DEA and HIN Validation Completed")
        logging.info("End Validation Process")
    else:
        print("files missing")

        # else:
        #     raise Exception("Missing DEA or HIN Lookup Files")

    # except:
    #     while True:
    #         sglayout = [[sg.Text("Missing DEA or HIN Lookup Files")],
    #                     [sg.Button('OK')]]

    #         window = sg.Window('Missing Files', layout=sglayout)
    #         event, values = window.read()
    #         window.Close()
    #         logging.error("Missing File: ", exc_info=True)
    #         sys.exit(0)

    sleep(5)
    dt = datetime.now()
    dt = dt.strftime("%Y%m%d.%H%M%S")

    now = time.time()

    # archive lookup files
    logging.debug("Archive Lookup Files")
    archive_path = baselocation + r"\files\01_input\archive"
    rename(lookup_file_hin, archive_path + r"\hin_lookup_" + dt + ".xlsx")
    rename(lookup_file_dea, archive_path + r"\dea_lookup_" + dt + ".xlsx")

    # remove old archived files
    for f in listdir(archive_path):
        if stat(path.join(archive_path, f)).st_mtime < now - 14 * 86400:
            remove(archive_path + "\\" + f)


if __name__ == "__main__":
    d = pathlib.Path.cwd()
    working_dir = str(d)
    root = d.root
    run_validation()

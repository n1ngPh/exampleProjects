
import os
import sys
import json
import pandas as pd
import numpy as np
from enum import Enum
from typing import Optional
from sklearn.model_selection import train_test_split

ERROR_MARK = "❌"
PASS_MARK = "✔️"

# Max values to show in error message
SHOW_LIMIT = 3


class RunMode(Enum):
    # Verify the contents against sample data.
    SAMPLE = 0
    # Run the contents against the full dataset.
    FULL = 1
    # Perform extra actions.
    EXTRA = 2

    def get_mode_string(mode):
        handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
        match mode:
            case RunMode.SAMPLE:
                return "verifying against sample data"
            case RunMode.FULL:
                return "running against full dataset"
            case RunMode.EXTRA:
                return "running extra functions"
            case other:
                assert other in handled_modes, \
                    "ERROR: Mode was unhandled {}".format(other)

    def get_handled_mode_strings():
        return ["sample", "full", "extra"]

    def get_mode_for_string(string: str):
        assert string in RunMode.get_handled_mode_strings(), \
            "Unhandled mode {}, use one of {}".format(
                string,
                ", ".join(RunMode.get_handled_mode_strings()))
        match string:
            case "sample":
                return RunMode.SAMPLE
            case "full":
                return RunMode.FULL
            case "extra":
                return RunMode.EXTRA


def get_lowercase_keymap(dictionaries, names):
    mapping = {}
    for name in names:
        mapping[name] = {}
    for dictionary, name in zip(dictionaries, names):
        for key in dictionary.keys():
            assert key.lower() not in mapping[name].keys(), \
                "Duplicate keys for lowercased form {}, keys first colliding were {} and {}".format(
                    key.lower(),
                    mapping[name][key.lower()],
                    key.lower()
                )
            mapping[name][key.lower()] = key
    return mapping


def get_lowercase_col_indexmap(lists, names):
    mapping = {}
    for name in names:
        mapping[name] = {}
    for list_i, name in zip(lists, names):
        for col in list_i:
            assert col.lower() not in mapping[name].keys(), \
                "Duplicate columns for lowercased form {}, columns first colliding were {} and {}".format(
                    col.lower(),
                    mapping[name][col.lower()],
                    col
                )
            mapping[name][col.lower()] = col
    return mapping


def check_task1(json_to_check, expected_json):
    return check_task_json(json_to_check, expected_json, "link urls")


def check_task2(json_to_check, expected_json):
    return check_task_json(json_to_check, expected_json, "page tokens")


def check_task3(csv_to_check, expected_csv):
    return check_task_csv(csv_to_check, expected_csv)


def check_task6(csv_to_check, expected_csv):
    return check_task_csv(csv_to_check, expected_csv)


def check_task_json(json_to_check, expected_json, item_name):
    list_of_keys = set([key.lower() for key in json_to_check.keys()])
    list_of_expected_keys = set([key.lower() for key in expected_json.keys()])
    if not list_of_keys == list_of_expected_keys:
        missing_keys = list_of_expected_keys.difference(list_of_keys)
        extra_keys = list_of_keys.difference(list_of_expected_keys)
        if len(missing_keys) > 0:
            print("\t {} Missing keys {}".format(
                ERROR_MARK,
                ", ".join(['"{}"'.format(key) for key in sorted(list(missing_keys))]))
            )
        if len(extra_keys) > 0:
            if len(extra_keys) > SHOW_LIMIT:
                print("\t {} Extra keys   {}".format(
                    ERROR_MARK,
                    ", ".join(['"{}"'.format(key) for key in sorted(list(extra_keys))[:SHOW_LIMIT]]) + ", ...")
                )
            else:
                print("\t {} Extra keys   {}".format(
                    ERROR_MARK,
                    ", ".join(['"{}"'.format(key) for key in sorted(list(extra_keys))]))
                )
        return False

    lowercase_keymap = get_lowercase_keymap(
        [json_to_check, expected_json],
        ["check", "expected"]
    )

    for key in lowercase_keymap["expected"].keys():
        json_to_check_values = set([link.lower() for link in json_to_check[lowercase_keymap["check"][key]]])
        expected_json_values = set([link.lower() for link in expected_json[lowercase_keymap["expected"][key]]])
        if not json_to_check_values == expected_json_values:
            missing_vals = expected_json_values.difference(json_to_check_values)
            extra_vals = json_to_check_values.difference(expected_json_values)
            if len(missing_vals) > 0:
                if len(missing_vals) > SHOW_LIMIT:
                    print("\t {} For seed link {}, missing {} {}".format(
                        ERROR_MARK,
                        key,
                        item_name,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))[:SHOW_LIMIT]]) + ", ..."
                        )
                    )
                else:
                    print("\t {} For seed link {}, missing {} {}".format(
                        ERROR_MARK,
                        key,
                        item_name,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))]))
                    )
            if len(extra_vals) > 0:
                if len(extra_vals) > SHOW_LIMIT:
                    print("\t {} For seed link {}, extra {}   {}".format(
                        ERROR_MARK,
                        key,
                        item_name,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))[:SHOW_LIMIT]]) + ", ..."
                        )
                    )
                else:
                    print("\t {} For seed link {}, extra {}   {}".format(
                        ERROR_MARK,
                        key,
                        item_name,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))])
                        )
                    )
            return False
    return True


def verify_task1(mode: RunMode):
    try:
        from task1 import task1
    except ImportError:
        print("Task 1's function not found.")
        return

    print("=" * 80)
    print(f"Executing Task 1 for {RunMode.get_mode_string(mode)}...\n")
    handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
    starting_links = []
    json_filename = ""
    match mode:
        case RunMode.SAMPLE:
            starting_links = [
                "http://115.146.93.142/samplewiki/A12_scale",
                "http://115.146.93.142/samplewiki/Gerard_Maley"
            ]
            json_filename = "task1_my_sample.json"
        case RunMode.FULL:
            starting_links = [
                "http://115.146.93.142/fullwiki/A12_scale",
                "http://115.146.93.142/fullwiki/Gerard_Maley"
            ]
            json_filename = "task1_my_full.json"
        case RunMode.EXTRA:
            assert mode in handled_modes, "No extra behaviour for Task 1"
        case other:
            assert other in handled_modes, \
                "ERROR: Mode was unhandled {}".format(other)
    task1(starting_links, json_filename)

    print("Checking Task 1's output...\n")
    if os.path.isfile(json_filename):
        print("\tTask 1's JSON output found.\n")
    else:
        print(f"\t {ERROR_MARK} Task 1's JSON output NOT found. "
              "Please check your code.\n")

    sample_filename = "task1_sample.json"
    if mode == RunMode.SAMPLE:
        if os.path.isfile(json_filename):
            if os.path.isfile(sample_filename):
                with open(json_filename) as f:
                    my_json = json.load(f)
                with open(sample_filename) as f:
                    sample_json = json.load(f)
                if check_task1(my_json, sample_json):
                    print(f"\t {PASS_MARK} Your output matches the sample for "
                          "Task 1.")
                else:
                    print(f"\t {ERROR_MARK} Your output does not match the "
                          "sample for Task 1.")
            else:
                print(f"\t {ERROR_MARK} The sample output file is missing, "
                      "download and replace it from the Sample data slide.")

    print("Finished Task 1.")
    print("=" * 80)


def verify_task2(mode: RunMode, extra_mode_url: Optional[str] = None):

    try:
        from task2 import task2
    except ImportError:
        print("Task 2's function not found.")
        return

    print("=" * 80)
    print(f"Executing Task 2 for {RunMode.get_mode_string(mode)}...\n")

    handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
    link_to_extract = ""
    json_filename = ""

    match mode:
        case RunMode.SAMPLE:
            link_to_extract = "http://115.146.93.142/samplewiki/A12_scale"
            json_filename = "task2_my_sample.json"
        case RunMode.FULL:
            link_to_extract = "http://115.146.93.142/fullwiki/Constitution_of_Australia"
            json_filename = "task2_my_full.json"
        case RunMode.EXTRA:
            link_to_extract = extra_mode_url
            json_filename = "task2_my_extra.json"
        case other:
            assert other in handled_modes, \
                "ERROR: Mode was unhandled {}".format(other)

    task2(link_to_extract, json_filename)

    print("Checking Task 2's output...\n")
    if os.path.isfile(json_filename):
        print("\tTask 2's JSON output found.\n")
    else:
        print(f"\t {ERROR_MARK} Task 2's JSON output NOT found. "
              "Please check your code.\n")

    sample_filename = "task2_sample.json"
    if mode == RunMode.SAMPLE:
        if os.path.isfile(json_filename):
            if os.path.isfile(sample_filename):
                with open(json_filename) as f:
                    my_json = json.load(f)
                with open(sample_filename) as f:
                    sample_json = json.load(f)
                if check_task2(my_json, sample_json):
                    print(f"\t {PASS_MARK} Your output matches the sample for "
                          "Task 2.")
                else:
                    print(f"\t {ERROR_MARK} Your output does not match the "
                          "sample for Task 2.")
            else:
                print(f"\t {ERROR_MARK} The sample output file is missing, "
                      "download and replace it from the Sample data slide.")

    print("Finished Task 2.")
    print("=" * 80)


def check_task_csv(csv_to_check, expected_csv):
    # Check columns match.
    check_cols = csv_to_check.columns
    expected_cols = expected_csv.columns

    lowercase_keymap = get_lowercase_col_indexmap(
        [check_cols, expected_cols],
        ["check", "expected"]
    )

    check_cols_lower = set([c.lower() for c in check_cols])
    expected_cols_lower = set([c.lower() for c in expected_cols])

    if not check_cols_lower == expected_cols_lower:
        missing_vals = expected_cols_lower.difference(check_cols_lower)
        extra_vals = check_cols_lower.difference(expected_cols_lower)
        if len(missing_vals) > 0:
            if len(missing_vals) > SHOW_LIMIT:
                print("\t {} CSV is missing columns {}".format(
                    ERROR_MARK,
                    ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))[:SHOW_LIMIT]]) + ", ..."
                    )
                )
            else:
                print("\t {} CSV is missing columns {}".format(
                    ERROR_MARK,
                    ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))]))
                )
            if len(extra_vals) > 0:
                if len(extra_vals) > SHOW_LIMIT:
                    print("\t {} CSV has extra columns  {}".format(
                        ERROR_MARK,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))[:SHOW_LIMIT]]) + ", ..."
                        )
                    )
                else:
                    print("\t {} CSV has extra columns  {}".format(
                        ERROR_MARK,
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))])
                        )
                    )
            return False

    for column in lowercase_keymap["expected"].keys():
        # Check counts
        check_values = set(csv_to_check[lowercase_keymap["check"][column]].values)
        expected_values = set(expected_csv[lowercase_keymap["expected"][column]].values)
        if not check_values == expected_values:
            missing_vals = expected_values.difference(check_values)
            extra_vals = check_values.difference(expected_values)
            # Check values match
            if len(missing_vals) > 0:
                if len(missing_vals) > SHOW_LIMIT:
                    print("\t {} For column {}, missing {} {}".format(
                        ERROR_MARK,
                        column,
                        "value",
                        ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))[:SHOW_LIMIT]]) + ", ..."
                        )
                    )
                else:
                    print("\t {} For column {}, missing {} {}".format(
                        ERROR_MARK,
                        column,
                        "value",
                        ", ".join(['"{}"'.format(key) for key in sorted(list(missing_vals))]))
                    )
            if len(extra_vals) > 0:
                if len(extra_vals) > SHOW_LIMIT:
                    print("\t {} For column {}, extra {}   {}".format(
                        ERROR_MARK,
                        column,
                        "value",
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))[:SHOW_LIMIT]]) + ", ..."
                        )
                    )
                else:
                    print("\t {} For column {}, extra {}   {}".format(
                        ERROR_MARK,
                        column,
                        "value",
                        ", ".join(['"{}"'.format(key) for key in sorted(list(extra_vals))])
                        )
                    )
            return False
        # Check counts of each value match
        counts_check = csv_to_check[lowercase_keymap["check"][column]].value_counts()
        counts_expected = expected_csv[lowercase_keymap["expected"][column]].value_counts()

        difference = counts_expected - counts_check

        difference = difference[abs(difference) > 0]

        if difference.size > 0:
            print("\t {} For column {}, difference in counts for each value".format(
                ERROR_MARK,
                column
                )
            )
            print(difference.head(SHOW_LIMIT))
            if difference.size > SHOW_LIMIT:
                print("\t ...")
            return False

        # Check order matches.
        if not all(csv_to_check[lowercase_keymap["check"][column]] == expected_csv[lowercase_keymap["expected"][column]]):
            print("\t {} For column {}, there was an error in the ordering of the data.".format(
                ERROR_MARK,
                column
                )
            )

            print("\t Items should be ordered:")
            print(expected_csv[lowercase_keymap["expected"][column]][~(csv_to_check[lowercase_keymap["check"][column]] == expected_csv[lowercase_keymap["expected"][column]])].head(SHOW_LIMIT))
            print("\n\t But were ordered:")
            print(csv_to_check[lowercase_keymap["expected"][column]][~(csv_to_check[lowercase_keymap["check"][column]] == expected_csv[lowercase_keymap["expected"][column]])].head(SHOW_LIMIT))

            return False
    return True


def verify_task3(mode):

    try:
        from task3 import task3
    except ImportError:
        print("Task 3's function not found.")
        return

    print("=" * 80)
    print(f"Executing Task 3 for {RunMode.get_mode_string(mode)}...\n")

    handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
    starting_links_json_filename = ""
    starting_links = {}
    csv_filename = ""
    match mode:
        case RunMode.SAMPLE:
            starting_links_json_filename = "task1_sample.json"
            csv_filename = "task3_my_sample.csv"
            if os.path.isfile(starting_links_json_filename):
                with open(starting_links_json_filename) as f:
                    starting_links = json.load(f)
            else:
                print(
                    f"\t {ERROR_MARK} The sample output file for Task 1 is "
                    "required for Task 3 but was missing, download and "
                    "replace it from the Sample data slide."
                )
        case RunMode.FULL:
            starting_links_json_filename = "task1_my_full.json"
            csv_filename = "task3_my_full.csv"
            if os.path.isfile(starting_links_json_filename):
                with open(starting_links_json_filename) as f:
                    starting_links = json.load(f)
            else:
                print(
                    f"\t {ERROR_MARK} The full running mode for Task 3 "
                    "requires the output for Task 1 to be present, "
                    "ensure it was correctly created."
                )
        case RunMode.EXTRA:
            assert mode in handled_modes, "No extra behaviour for Task 3"
        case other:
            assert other in handled_modes, \
                "ERROR: Mode was unhandled {}".format(other)

    task3(starting_links, csv_filename)

    print("Checking Task 3's output...\n")
    if os.path.isfile(csv_filename):
        print("\tTask 3's CSV output found.\n")
    else:
        print(f"\t {ERROR_MARK} Task 3's CSV output NOT found. "
              "Please check your code.\n")

    sample_filename = "task3_sample.csv"
    if mode == RunMode.SAMPLE:
        if os.path.isfile(csv_filename):
            if os.path.isfile(sample_filename):
                my_csv = pd.read_csv(csv_filename)
                sample_csv = pd.read_csv(sample_filename)
                if check_task3(my_csv, sample_csv):
                    print(f"\t {PASS_MARK} Your output matches the sample for "
                          "Task 3.")
                else:
                    print(f"\t {ERROR_MARK} Your output does not match the "
                          "sample for Task 3.")
            else:
                print(f"\t {ERROR_MARK} The sample output file is missing, "
                      "download and replace it from the Sample data slide.")

    print("Finished executing Task 3.")
    print("=" * 80)


def verify_task4(mode):

    try:
        from task4 import task4
    except ImportError:
        print("Task 4's function not found.")
        return

    print("=" * 80)
    print(f"Executing Task 4 for {RunMode.get_mode_string(mode)}...\n")

    handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
    bow_csv_filename = ""
    bow = None
    output_plot_filename = ""
    match mode:
        case RunMode.SAMPLE:
            bow_csv_filename = "task3_sample.csv"
            output_plot_filename = "task4_my_sample.png"
            if os.path.isfile(bow_csv_filename):
                bow = pd.read_csv(bow_csv_filename)
            else:
                print(
                    f"\t {ERROR_MARK} The sample output file for Task 3 is "
                    "required for Task 4 but was missing, download and "
                    "replace it from the Sample data slide."
                )
        case RunMode.FULL:
            bow_csv_filename = "task3_my_full.csv"
            output_plot_filename = "task4_my_full.png"
            if os.path.isfile(bow_csv_filename):
                bow = pd.read_csv(bow_csv_filename)
            else:
                print(
                    f"\t {ERROR_MARK} The full running mode for Task 4 "
                    "requires the output for Task 3 to be present, "
                    "ensure it was correctly created."
                )
        case RunMode.EXTRA:
            assert mode in handled_modes, "No extra behaviour for Task 4"
        case other:
            assert other in handled_modes, \
                "ERROR: Mode was unhandled {}".format(other)

    most_common_words = task4(bow, output_plot_filename)

    print("Checking Task 4's output...\n")
    if os.path.isfile(output_plot_filename):
        print("\tTask 4's plot output found.\n")
        # Check size is sensible.
        if os.path.getsize(output_plot_filename) <= 0:
            print(f"\t {ERROR_MARK} Task 4's plot appears to have "
                  "been created, but the file is empty. Check it has "
                  "output as expected.")
    else:
        print(f"\t {ERROR_MARK} Task 4's plot output NOT found. "
              "Please check your code.\n")

    sample_filename = "task4_sample_words.json"
    if mode == RunMode.SAMPLE:
        if os.path.isfile(sample_filename):
            with open(sample_filename) as f:
                sample_words = json.load(f)
            for seed_url in sample_words.keys():
                if seed_url not in most_common_words.keys():
                    print(f"\t {ERROR_MARK} Your output was missing a key for url {seed_url}")
                    continue
                if set(sample_words[seed_url]) == set(most_common_words[seed_url]):
                    print(f"\t {PASS_MARK} Your output matches the sample for "
                            f"Task 4 for {seed_url}.")
                else:
                    print(f"\t {ERROR_MARK} Your output for most common words for url {seed_url} was:")
                    print("[{}{}]".format(", ".join(most_common_words[seed_url][:11]), ", ..." if len(most_common_words[seed_url]) > 10 else ""))
                    print("\t but should have been:")
                    print("[{}]".format(", ".join(sample_words[seed_url][:11])))
        else:
            print(f"\t {ERROR_MARK} The sample words file is missing, "
                    "download and replace it from the Sample data slide.")


    print("Finished executing Task 4.")
    print("=" * 80)


def verify_task5(mode):
    try:
        from task5 import task5
    except ImportError:
        print("Task 5's function not found.")
        return

    print("=" * 80)
    print(f"Executing Task 5 for {RunMode.get_mode_string(mode)}...\n")

    handled_modes = [RunMode.SAMPLE, RunMode.FULL, RunMode.EXTRA]
    train_bow_df = None
    test_bow_df = None

    tokens_plot_filename = ""
    distribution_plot_filename = ""

    match mode:
        case RunMode.SAMPLE:
            bow_csv_filename = "task3_sample.csv"
            tokens_plot_filename = "task5_my_sample_5a.png"
            distribution_plot_filename = "task5_my_sample_5b.png"
            if os.path.isfile(bow_csv_filename):
                bow = pd.read_csv(bow_csv_filename)
                bow = bow.sort_values(by=["link_url", "seed_url"])
            else:
                print(
                    f"\t {ERROR_MARK} The sample output file for Task 3 is "
                    "required for Task 5 but was missing, download and "
                    "replace it from the Sample data slide."
                )
        case RunMode.FULL:
            bow_csv_filename = "task3_my_full.csv"
            tokens_plot_filename = "task5_my_full_5a.png"
            distribution_plot_filename = "task5_my_full_5b.png"
            if os.path.isfile(bow_csv_filename):
                bow = pd.read_csv(bow_csv_filename)
                bow = bow.sort_values(by=["link_url", "seed_url"])
            else:
                print(
                    f"\t {ERROR_MARK} The full running mode for Task 5 "
                    "requires the output for Task 3 to be present, "
                    "ensure it was correctly created."
                )
        case RunMode.EXTRA:
            assert mode in handled_modes, "No extra behaviour for Task 5"
        case other:
            assert other in handled_modes, \
                "ERROR: Mode was unhandled {}".format(other)

    pca_top10 = task5(bow, tokens_plot_filename, distribution_plot_filename)

    print("Checking Task 5's output...\n")
    if os.path.isfile(tokens_plot_filename):
        print("\tTask 5's tokens plot output found.\n")
        # Check size is sensible.
        if os.path.getsize(tokens_plot_filename) <= 0:
            print(f"\t {ERROR_MARK} Task 5's tokens plot appears to have "
                  "been created, but the file is empty. Check it has "
                  "output as expected.")
    else:
        print(f"\t {ERROR_MARK} Task 5's tokens plot output NOT found. "
              "Please check your code.\n")
    if os.path.isfile(distribution_plot_filename):
        print("\tTask 5's distribution plot output found.\n")
        # Check size is sensible.
        if os.path.getsize(distribution_plot_filename) <= 0:
            print(f"\t {ERROR_MARK} Task 5's distribution plot appears to have "
                  "been created, but the file is empty. Check it has "
                  "output as expected.")
    else:
        print(f"\t {ERROR_MARK} Task 5's distribution plot output NOT found. "
              "Please check your code.\n")

    sample_filename = "task5_sample_pca.json"
    if mode == RunMode.SAMPLE:
        if os.path.isfile(sample_filename):
            with open(sample_filename) as f:
                sample_pca_top10 = json.load(f)
            for component in sample_pca_top10.keys():
                if component not in pca_top10.keys():
                    print(f"\t {ERROR_MARK} Your output was missing a key for component \"{component}\"")
                    continue
                for word_list in ["positive", "negative"]:
                    if word_list not in pca_top10[component].keys():
                        print(f"\t {ERROR_MARK} Your output for component \"{component}\" was missing a key for list of words \"{word_list}\"")
                        continue
                    if set(sample_pca_top10[component][word_list]) == set(pca_top10[component][word_list]):
                        print(f"\t {PASS_MARK} Your output matches the sample for "
                                f"Task 5 for component \"{component}\"'s \"{word_list}\" list.")
                    else:
                        print(f"\t {ERROR_MARK} Your output for \"{word_list}\" list for component \"{component}\" was:")
                        print("[{}{}]".format(", ".join(pca_top10[component][word_list][:11]), ", ..." if len(pca_top10[component][word_list]) > 10 else ""))
                        print("\t but should have been:")
                        print("[{}]".format(", ".join(sample_pca_top10[component][word_list][:11])))
                for weights_list in ["positive_weights", "negative_weights"]:
                    if not len(pca_top10[component][weights_list]) == len(sample_pca_top10[component][weights_list]) or not np.allclose(pca_top10[component][weights_list], sample_pca_top10[component][weights_list], rtol=0, atol=1e-3):
                        print(f"\t {ERROR_MARK} Your output for the \"{weights_list}\" value for component \"{component}\" was:")
                        print("[{}{}]".format(", ".join(["{}".format(x) for x in pca_top10[component][weights_list][:11]]), ", ..." if len(pca_top10[component][weights_list]) > 10 else ""))
                        print("\t but should have been:")
                        print("[{}]".format(", ".join(["{}".format(x) for x in sample_pca_top10[component][weights_list][:11]])))
                    else:
                        print(f"\t {PASS_MARK} Your output matches the sample for "
                              f"Task 5 for component \"{component}\"'s \"{weights_list}\" list.")

        else:
            print(f"\t {ERROR_MARK} The sample words file is missing, "
                    "download and replace it from the Sample data slide.")


    print("Finished executing Task 5.")
    print("=" * 80)


def verify_task6():
    print("Checking if task6.pdf exists...\n")
    if os.path.isfile("task6.pdf"):
        print(f"\t {PASS_MARK} Report task6.pdf found.\n")
        if os.path.getsize("task6.pdf") <= 0:
            print(f"\t {ERROR_MARK} Report task6.pdf was empty! Please check it uploaded correctly.\n")
    else:
        print(f"\t {ERROR_MARK} Report task6.pdf NOT found. Please check the file name or upload the file.\n")

    print("Finished Task 6.")
    print("=" * 80)


def main():
    args = sys.argv
    assert len(args) >= 2, "Please provide a task."
    task = args[1]
    assert task in ["all"] + ["task" + str(i) for i in range(1, 8)], \
        "Invalid task."
    if len(args) > 2:
        assert args[2].lower() in RunMode.get_handled_mode_strings(), \
            "Run mode was invalid, should be one of [{}]".format(
            ", ".join(RunMode.get_handled_mode_strings()))
        mode = RunMode.get_mode_for_string(args[2])
    else:
        mode = None
    if task == "task1":
        assert mode is not None, "Please ensure you have also provided a mode."
        verify_task1(mode)
    elif task == "task2":
        assert mode is not None, "Please ensure you have also provided a mode."
        if mode == RunMode.EXTRA:
            assert len(args) >= 4, "Please provide a url for extra mode."
            verify_task2(mode, extra_mode_url=args[3])
        else:
            verify_task2(mode)
    elif task == "task3":
        assert mode is not None, "Please ensure you have also provided a mode."
        verify_task3(mode)
    elif task == "task4":
        assert mode is not None, "Please ensure you have also provided a mode."
        verify_task4(mode)
    elif task == "task5":
        assert mode is not None, "Please ensure you have also provided a mode."
        verify_task5(mode)
    elif task == "task6":
        verify_task6()
    elif task == "all":
        assert mode is not None, "Please ensure you have also provided a mode."
        verify_task1(mode)
        verify_task2(mode)
        verify_task3(mode)
        verify_task4(mode)
        verify_task5(mode)
        verify_task6()

if __name__ == "__main__":
    main()




"""
Simple task script that runs on Beaker via Gantry.
Accepts a WILL_FAIL argument to control whether the job succeeds or fails.
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="Simple Beaker task")
    parser.add_argument(
        "--will-fail",
        action="store_true",
        default=False,
        help="If set, the job will raise an error and exit with a non-zero code.",
    )
    args = parser.parse_args()

    if args.will_fail:
        print("WILL_FAIL is set — raising an error.")
        raise RuntimeError("Job intentionally failed because WILL_FAIL was set.")

    print("Job completed successfully.")


if __name__ == "__main__":
    main()

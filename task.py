import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail", action="store_true", default=False,)
    args = parser.parse_args()

    if args.fail:
        raise RuntimeError("Job intentionally failed because FAIL is set.")

    print("Success!")

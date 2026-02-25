import argparse

from gantry.api import Recipe


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", type=str, required=True)
    parser.add_argument("--budget", type=str, required=True)
    parser.add_argument("--fail", action="store_true", default=False)
    parser.add_argument("--cluster", type=str, nargs="*")
    parser.add_argument("--show-logs", action="store_true", default=True)
    parser.add_argument("--dry-run", action="store_true", default=False)
    args = parser.parse_args()

    task_args = ["python", "task.py"]
    if args.fail:
        task_args.append("--fail")

    recipe = Recipe(
        args=task_args,
        name="dummy-debug-runner",
        workspace=args.workspace,
        budget=args.budget,
        clusters=args.cluster,
        yes=True,
    )

    if args.dry_run:
        recipe.dry_run()
    else:
        recipe.launch(show_logs=args.show_logs)


if __name__ == "__main__":
    main()

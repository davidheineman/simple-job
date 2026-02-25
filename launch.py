"""
Launches a simple Gantry job on Beaker.

Usage:
    python launch.py --workspace ai2/my-workspace --budget ai2/my-budget
    python launch.py --workspace ai2/my-workspace --budget ai2/my-budget --will-fail
"""

import argparse

from gantry.api import Recipe


def main():
    parser = argparse.ArgumentParser(description="Launch a simple Gantry job on Beaker")
    parser.add_argument("--workspace", type=str, required=True, help="Beaker workspace")
    parser.add_argument("--budget", type=str, required=True, help="Beaker budget")
    parser.add_argument(
        "--will-fail",
        action="store_true",
        default=False,
        help="If set, the launched job will intentionally fail.",
    )
    parser.add_argument("--cluster", type=str, nargs="*", help="Beaker cluster(s) to use")
    parser.add_argument("--show-logs", action="store_true", default=True, help="Show job logs")
    parser.add_argument("--dry-run", action="store_true", default=False, help="Dry run only")
    args = parser.parse_args()

    task_args = ["python", "task.py"]
    if args.will_fail:
        task_args.append("--will-fail")

    recipe = Recipe(
        args=task_args,
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

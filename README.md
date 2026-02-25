A dummy library for testing https://github.com/davidheineman/beaker-runner

## Usage

Launch a job that succeeds:
```bash
python launch.py --workspace ai2/my-workspace --budget ai2/my-budget
```

Launch a job that intentionally fails:
```bash
python launch.py --workspace ai2/my-workspace --budget ai2/my-budget --will-fail
```

Dry run (validate without submitting):
```bash
python launch.py --workspace ai2/my-workspace --budget ai2/my-budget --dry-run
```

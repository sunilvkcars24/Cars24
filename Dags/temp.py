name: run_script
on: 
    schedule:
      - cron: "8 0 * * *" #runs at 08:00 UTC everyday
jobs:
  run_review_reports:
    runs-on: ubuntu-latest
    steps:
      - name: checkout repo content
        uses: actions/checkout@v2 # checkout the repository content to github runner.
      - name: setup python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9.7
      - name: execute py script
        run: |
          python test.py

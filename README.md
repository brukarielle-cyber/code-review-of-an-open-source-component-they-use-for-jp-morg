# Code review of an open-source component they use for JP Morgan

a written review of one small module in an open-source project the company depends on, plus a small pull request or a well-written issue.

## Problem

JPMorgan Chase has described building technology skills in house, including training people for technologist roles at one of its tech hubs. HR analyst postings at the company ask interns to compile data packages and use analytics to generate workforce insights, tasks that usually start as a manual spreadsheet pull of headcount, attrition, tenure, and pay data. Doing that pull by hand each time is slow and error prone, especially when it has to be redone for a new team or time period. This project builds a small Python tool that takes a workforce CSV and produces the same kind of one-page summary an HR team would compile: headcount by department, a 12-month attrition rate, average tenure, and compa-ratio by performance rating. I built and analyzed discounted cash flow models in Excel as a research analyst, so I am used to working with spreadsheet data and checking formulas by hand. I oversee membership operations for 100+ active members, which includes managing registration systems, attendance tracking, and participation analytics. My coursework includes Business Analytics, which covers the kind of data summarizing this project applies. The goal is a repository where a loader checks the input data, four metric functions compute the summary, and tests confirm the math against numbers worked out by hand on a small sample file.

## Data

TODO(kitbound): Where the data comes from (with links), when you downloaded it, and what you cleaned. Label anything synthetic.

## Approach

TODO(kitbound): What you built and why: the steps, one choice you made and what you tried instead.

## Results

TODO(kitbound): What you measured, with the number and a chart or table. Report only results you produced.

## Limitations

TODO(kitbound): What the data cannot tell you, and what would make the result wrong.

## How to run

TODO(kitbound): The exact commands to install, run, and test this.

```bash
pip install -r requirements.txt
python -m src.analysis
pytest
```

## Built with AI assistance

I built this project with AI assistance (Kitbound's coach for planning and drafting, and an AI coding assistant for parts of the code). I chose the problem, ran every step, checked the results, and can explain every part. Anything synthetic is labeled synthetic.

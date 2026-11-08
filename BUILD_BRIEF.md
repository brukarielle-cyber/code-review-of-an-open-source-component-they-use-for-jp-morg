# Build brief: Code review of an open-source component they use for JP Morgan

You are working in the repository brukarielle-cyber/code-review-of-an-open-source-component-they-use-for-jp-morg. It already has a README outline, src/, data/, tests/, and a dev container. Keep that structure.

## Goal
a written review of one small module in an open-source project the company depends on, plus a small pull request or a well-written issue.

## Why it matters to JP Morgan
- What JP Morgan does, from its own site: Army Veteran Ashley Wigfall transitioned to a civilian role and charted her path to technologist through mentorship and skills training at the JPMorgan Chase tech hub in Plano, Texas. This project speaks to that work directly. (https://jpmorganchase.com)
- The HR Analyst Intership posting asks for "Pursuing a Bachelor's or Master's degree with expected graduation between December 2027 and June 2028", and this project shows it in practice.
- Recent news: JP Morgan - BBC News. The project connects to what the team is working on now. (https://www.bbc.com/news/topics/cjnwl8q4nr3t)

## In scope
- a written review of one small module in an open-source project the company depends on, plus a small pull request or a well-written issue.
- Use the tools you already know: Excel.

## Out of scope
- No production deployment, custom domains, or cloud infrastructure you would have to pay for.
- No user accounts or authentication systems unless the feature is about authentication.
- No mobile apps unless the role is mobile-focused.
- No full redesign of their product; one feature or one workflow only.
- No code or advanced tooling; a clear written analysis is enough.

## Steps
1. Read JP Morgan's public pages and note one question the team is working on (about 0.5 hours)
2. Pick one module and read it with its tests (about 1 hours)
3. Write a one-page review: what it does, one strength, two concrete improvement ideas (about 1 hours)
4. Open a small pull request (docs fix, test, or bug fix) or a clear issue with reproduction steps (about 1 hours)
5. Write the one-paragraph summary you will paste in emails, and proofread (about 0.5 hours)

## Data and materials
- The company's public API documentation, public SDKs, public changelogs, and public engineering blog posts.
- Open-source repositories and their issue trackers.
- Synthetic data you generate yourself, clearly labeled as synthetic in the README and in the data file names (for example `synthetic_invoices.json`).
- Public datasets where a realistic sample helps, such as Kaggle public datasets or data.gov, with the source and license noted.
- Never use company credentials you were not given, private repositories, scraped data behind a login, or anyone's personal data.

## README sections to fill in
- Problem
- Data
- Approach
- Results
- Limitations
- How to run
- Built with AI assistance
Replace every line that starts with TODO(kitbound). Report only results you actually produced.

## Done when
- The first three lines of the README say what it is and why it matters to this company.
- Uses only public or clearly labeled synthetic data.
- Has an honest limitations section.
- Readable in under five minutes: a reviewer can understand the point from the README alone.
- Opens without login: the repository is public and any demo link works in a private browser window.
- pytest passes

## Rules
- Use only public or clearly labeled synthetic data. Never use credentials, private repositories, or data behind a login.
- Do not use the company's logo or suggest the project is endorsed by them.
- Explain each change so I can defend it in an interview; keep the code small and readable.

# ledger.md
Accounting web application that allows for journal entries to be posted and these changes reflected in reports. These reports can be created dynamically using a combination of Markdown and Jinja templating.

## Motivation
Previously working as an accountant, I found the ability to customise reports in existing programs very inflexible. In cases where you would want to make a custom report to show a client how some specific aspect of their financials were tracking it can prove difficult. I have enjoyed the flexibility of writing Markdown for note taking and thought of combining with the issue I found in creating reports. 

## Future Work
This current version acts as a simple proof of concept, allowing for account balances and entries to be rendered. I would like to expand it to the following:
- Ability to add configurable charts dynamically based on entries over specified time periods and them rendered within the Markdown.
- Have it run locally within a desktop application, with multiple different files able to be created.

## Run Locally
### Docker
```
docker build -t ledger.md .
docker run -p 5000:5000 ledger.md
```
- Navigate to http://localhost:5000/ in the browser.
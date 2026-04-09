# Data Analyst Assignment

This repository contains a clean solution scaffold for the PlatinumRx data analyst assignment across SQL, spreadsheets, and Python.

## What is included

- `SQL/01_Hotel_Schema_Setup.sql`
  - Creates the hotel tables and adds only the rows explicitly visible in the PDF.
- `SQL/02_Hotel_Queries.sql`
  - Solves all 5 hotel SQL questions.
- `SQL/03_Clinic_Schema_Setup.sql`
  - Creates the clinic tables and adds only the rows explicitly visible in the PDF.
- `SQL/04_Clinic_Queries.sql`
  - Solves all 5 clinic SQL questions.
- `Python/01_Time_Converter.py`
  - Converts minutes into a readable `X hrs Y minutes` format.
- `Python/02_Remove_Duplicates.py`
  - Removes duplicate characters from a string using a loop.
- `Spreadsheets/Ticket_Analysis.xlsx`
  - Workbook template with `ticket` and `feedbacks` sheets, formulas, and helper columns.

## Important assumption

The extracted PDF showed only partial sample rows and then `...`, so the exact full dataset was not available in the document text. Because of that:

- the schema is based on the column names shown in the assignment,
- only the rows explicitly visible in the PDF were inserted,
- some queries may return very limited or empty results until more source data is provided.

## SQL notes

- The SQL is written in PostgreSQL-friendly syntax.
- The hotel queries use window functions where the question naturally needs ranking.
- The clinic query file uses `:target_year` and `:target_month` placeholders for parameterized execution.

Examples:

- `:target_year = 2021`
- `:target_month = '2021-03-01'`

If your SQL tool does not support bind variables, replace them with hardcoded values before running.

## Spreadsheet approach

### Question 1

Populate `feedbacks.ticket_created_at` from the `ticket` sheet using `cms_id`.

Excel 365 / Google Sheets:

```excel
=XLOOKUP(A2,ticket!$E:$E,ticket!$B:$B,"")
```

Classic Excel:

```excel
=VLOOKUP(A2,ticket!$E:$B,4,FALSE)
```

### Question 2

Add helper columns in the `ticket` sheet:

- `same_day`

```excel
=INT(B2)=INT(C2)
```

- `same_hour_same_day`

```excel
=AND(INT(B2)=INT(C2),HOUR(B2)=HOUR(C2))
```

Then count outlet-wise results with `COUNTIFS` or a pivot table.

Example `COUNTIFS` for same day:

```excel
=COUNTIFS(ticket!$D:$D,A2,ticket!$F:$F,TRUE)
```

Example `COUNTIFS` for same hour of same day:

```excel
=COUNTIFS(ticket!$D:$D,A2,ticket!$G:$G,TRUE)
```

## Python run commands

```powershell
python .\Python\01_Time_Converter.py
python .\Python\02_Remove_Duplicates.py
```

## Submission checklist

- Run each SQL setup file before its corresponding query file.
- Add more source rows only if you receive them separately from the assignment owner.
- Open the workbook and verify formulas after entering or importing the ticket and feedback data.
- Upload this project to GitHub and share the spreadsheet file or Google Sheets link with viewer access.

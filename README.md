# ISEE calculator

A small Streamlit app that estimates the **ISEE** and **ISPE**, the Italian indicators of a household's economic situation, for students whose family lives and earns in Lebanon. Amounts entered in Lebanese pounds (LBP) are converted to euros, and the result is checked against the scholarship thresholds in `config.json`.

> This is a quick estimate to see whether applying makes sense, not an official calculation. The official ISEE is always issued through a CAF or INPS.

## What it asks for

- Number of people in the household (sets the equivalence scale)
- Area of the main residence and of any other buildings owned
- Bank balance, annual income and annual rent, in LBP

## What it shows

- Estimated ISEE and ISPE in euros
- Whether both are below the thresholds for a full scholarship

## Run it

```bash
pip install streamlit
streamlit run isee_calc.py
```

## Configuration (`config.json`)

| Key | Meaning |
| --- | --- |
| `rate` | LBP per euro used for the conversion |
| `SE` | Equivalence scale by household size |
| `isee_threshold` | ISEE limit for the scholarship (€) |
| `ispe_threashold` | ISPE limit for the scholarship (€) |

Update `rate` and the thresholds each year before using it.

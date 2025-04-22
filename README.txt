# Worker Protection Standard (WPS) Enforcement: Data Analysis & Integration

## Project Goal

This project investigates disparities in the enforcement of the U.S. Environmental Protection Agency’s (EPA) Worker Protection Standard (WPS). We aim to understand:

- How enforcement varies across U.S. states
- Which factors in **agricultural production** and **farm labor structure** explain variability in WPS violations, inspections, and sanctions
- How **self-reported pesticide exposure incidents** from IDS complement or contrast with formal regulatory actions from ECHO

---

## Analytical Objectives

| Aim | Description |
|-----|-------------|
| **Aim 1** | Describe state-level trends in WPS violations, inspections, and sanctions using EPA ECHO data |
| **Aim 2** | Assess whether agricultural production characteristics( EPA pesticide acreage) predict enforcement outcomes |
| **Aim 3** | Analyze how labor characteristics (e.g., H-2A reliance) relate to WPS enforcement |
| **Supplemental** | Use EPA IDS data as a proxy for pesticide exposure events, offering insight into underreporting and regional risk |

---

## Directory Overview

| Folder | Contents |
|--------|----------|
| `originalDataFiles/` | Raw ECHO and USDA datasets |
| `cleanedDataFiles/` | Preprocessed and cleaned CSVs for modeling |
| `IDS/` | IDS topic modeling notebook and filtered exposure data |
| `farmLaborData/` | H-2A authorizations, BLS workforce data, and Ag Census indicators |
| `merge/` | Final merged dataset and model-ready panel data |
| `visualization/` | Jupyter notebooks for charts, maps, and report visuals |
| `project/` | Draft figures, statistical output, and manuscript text |
| `README.md` | This documentation file |

---

## Data Sources Used

| Dataset | Description | Used In |
|---------|-------------|---------|
| `ECHO` | Formal records of WPS violations, inspections, and enforcement actions (EPA) | Aims 1–3 |
| `IDS.csv` | Self-reported pesticide-related incidents (EPA IDS system) | Supplementary |
| `IDS_agriculture.csv` | Filtered IDS incidents relevant to agriculture (via topic modeling) | Supplementary |
| `USDA Ag Census` | State-level data on crop type, farmable land, etc. | Aim 2 |
| `EPA Pesticide Acreage` | Acres treated with pesticide per state | Aim 2 |
| `BLS + H-2A` | Labor force statistics and guest worker programs | Aim 3 |

---

## Data Cleaning Workflow

- **IDS.ipynb**: LDA topic modeling to extract agricultural exposure events from IDS
- **merge_all_data.ipynb**: Panel-level integration of all datasets by State-Year
- **regex_clean.py**: Custom functions for text field cleanup and lemmatization

---

## Output Files

| File | Description |
|------|-------------|
| `IDS_agriculture.csv` | Agriculture-related IDS records filtered by Topic 2 |
| `final_panel_dataset.csv` | Merged dataset with ECHO, IDS, Ag Census, and BLS indicators |
| `wps_analysis_results.pdf` | Final statistical models and graphs |

---

## Visualizations

See `visualization/` for:

- Temporal trend lines (WPS enforcement per state)
- IDS vs. ECHO comparative maps
- Exposure heatmaps overlaid with enforcement activity

---

## Citation Targets

This project is being prepared for submission to one or more of the following journals:

- *American Journal of Industrial Medicine*  
- *New Solutions*  
- *Journal of Agromedicine*  
- *Safety Science*

---

## Team

- Xiaoyu Ju (Lead Analyst)  

---

## Notes

- Data handling complies with EPA public data use policies.
- All sensitive data has been anonymized or filtered.
- IDS topic filtering was conducted using Latent Dirichlet Allocation with manual validation of topics.
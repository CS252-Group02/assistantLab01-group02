# data/

This directory contains the dataset files utilized by the **Study Assistant** application.

## Dataset Inventory

| File | Description | Source | Owner | Update Frequency |
|---|---|---|---|---|
| [`offices.csv`](offices.csv) | Campus office names, room locations, and operating hours | HCMUS Campus Directory & Office Announcements | Security & Data Team (Nguyễn Quốc Bảo, Lê Trọng Đại Nghĩa) | Per semester or upon schedule changes |
| [`README.md`](README.md) | Data directory catalog, schema definitions, and metadata | Internal project documentation | Security & Data Team (Nguyễn Quốc Bảo, Lê Trọng Đại Nghĩa) | As datasets are added or updated |

---

## File Details

### 1. `offices.csv`

- **Description**: Tabular CSV file containing location and schedule information for key campus administrative units and student service facilities. This data is read by the rule-based assistant (`src/assistant/rules.py`) to answer student queries.
- **Source**: University of Science (VNU-HCM) official campus directory, Training Office (Phòng Đào tạo), Student Affairs (Phòng Công tác Sinh viên), Library, and IT Helpdesk schedules.
- **Owner**: Security & Data Team
  - Nguyễn Quốc Bảo (ID: `25125079`)
  - Lê Trọng Đại Nghĩa (ID: `25125089`)
- **Update Frequency**: At the beginning of each academic semester, or whenever campus departments notify relocations or operating hour changes.
- **Schema**:

| Column | Type | Description | Example |
|---|---|---|---|
| `name` | String | Full name of the office or campus facility | `Training Office` |
| `room` | String | Room code and building identifier | `I.101` |
| `hours` | String | Operating days and working hours | `Mon-Fri 07:30-16:30` |

- **Usage Notes**:
  - Keep header names exactly as `name,room,hours`.
  - Office lookups are case-insensitive in the assistant implementation.

---

### 2. `README.md`

- **Description**: Dataset catalog and documentation tracking provenance, ownership, schemas, and update cadences for all files in `data/`.
- **Source**: Internal project data governance and documentation standards.
- **Owner**: Security & Data Team
  - Nguyễn Quốc Bảo (ID: `25125079`)
  - Lê Trọng Đại Nghĩa (ID: `25125089`)
- **Update Frequency**: Updated alongside any changes (additions, modifications, deprecations) to data files in this folder.

---

## Guidelines for Adding or Updating Data

1. **Maintain Schema Consistency**: When editing `offices.csv` or introducing new datasets, preserve column headers and comma-separated formatting.
2. **Document Provenance**: Every new file placed in this directory must be registered in this `README.md` with its source, owner, update frequency, and schema.
3. **Verify Integrity**: Ensure all entries use valid UTF-8 encoding without trailing empty lines or malformed fields that could break parsing in `rules.py`.

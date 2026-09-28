# AtmoSync — Data Dictionary

> This is a starter data dictionary. Field names, types, and tables below are
> assumptions based on a typical atmospheric/weather data sync project.
> Edit them so they match the real AtmoSync schema.

## Overview

| Item | Value |
|------|-------|
| Project | AtmoSync |
| Last updated | 2026-09-28 |
| Data source(s) | _e.g. weather API, sensors, CSV imports_ |
| Storage | _e.g. PostgreSQL, SQLite, MongoDB_ |
| Timezone convention | UTC (ISO 8601) |

## Conventions

- **Timestamps** are stored in UTC using ISO 8601 (`2026-09-28T10:30:00Z`).
- **Units** follow SI/metric unless stated otherwise (°C, hPa, m/s, mm).
- **IDs** are unique identifiers (UUID or auto-increment integer).
- **Nullable** means the field may be empty when data is unavailable.
- Field names use `snake_case`.

## Entities

### 1. `locations`

Places for which atmospheric data is collected.

| Field | Type | Nullable | Description | Example |
|-------|------|----------|-------------|---------|
| `location_id` | UUID / INT | No | Primary key | `a1b2c3d4` |
| `name` | STRING | No | Human-readable place name | `Chennai` |
| `country_code` | STRING(2) | No | ISO 3166-1 alpha-2 code | `IN` |
| `latitude` | DECIMAL(9,6) | No | Latitude in degrees | `13.082700` |
| `longitude` | DECIMAL(9,6) | No | Longitude in degrees | `80.270700` |
| `elevation_m` | FLOAT | Yes | Elevation above sea level in metres | `6.7` |
| `timezone` | STRING | Yes | IANA timezone name | `Asia/Kolkata` |
| `created_at` | TIMESTAMP | No | Record creation time (UTC) | `2026-09-28T10:30:00Z` |

### 2. `observations`

Measured atmospheric readings at a point in time.

| Field | Type | Nullable | Description | Unit | Example |
|-------|------|----------|-------------|------|---------|
| `observation_id` | UUID / INT | No | Primary key | - | `f9e8d7c6` |
| `location_id` | UUID / INT | No | Foreign key to `locations` | - | `a1b2c3d4` |
| `observed_at` | TIMESTAMP | No | Time of measurement (UTC) | - | `2026-09-28T10:00:00Z` |
| `temperature` | FLOAT | Yes | Air temperature | °C | `31.5` |
| `humidity` | FLOAT | Yes | Relative humidity (0-100) | % | `72.0` |
| `pressure` | FLOAT | Yes | Atmospheric pressure | hPa | `1008.4` |
| `wind_speed` | FLOAT | Yes | Wind speed | m/s | `4.2` |
| `wind_direction` | INT | Yes | Wind direction (0-360) | degrees | `210` |
| `precipitation` | FLOAT | Yes | Rainfall in the period | mm | `0.0` |
| `cloud_cover` | INT | Yes | Cloud cover (0-100) | % | `40` |
| `visibility` | FLOAT | Yes | Visibility distance | km | `8.0` |
| `uv_index` | FLOAT | Yes | UV index | - | `6.5` |
| `source_id` | UUID / INT | Yes | Foreign key to `data_sources` | - | `s1` |

### 3. `forecasts`

Predicted atmospheric values.

| Field | Type | Nullable | Description | Example |
|-------|------|----------|-------------|---------|
| `forecast_id` | UUID / INT | No | Primary key | `c3b2a1` |
| `location_id` | UUID / INT | No | Foreign key to `locations` | `a1b2c3d4` |
| `issued_at` | TIMESTAMP | No | When the forecast was generated (UTC) | `2026-09-28T06:00:00Z` |
| `valid_for` | TIMESTAMP | No | Time the forecast applies to (UTC) | `2026-09-29T12:00:00Z` |
| `temperature` | FLOAT | Yes | Predicted temperature (°C) | `33.0` |
| `precipitation_probability` | INT | Yes | Chance of rain (0-100 %) | `60` |
| `condition` | STRING | Yes | Summary label | `Partly cloudy` |

### 4. `data_sources`

Where data comes from.

| Field | Type | Nullable | Description | Example |
|-------|------|----------|-------------|---------|
| `source_id` | UUID / INT | No | Primary key | `s1` |
| `name` | STRING | No | Source name | `Weather API` |
| `type` | STRING | No | `api`, `sensor`, or `file` | `api` |
| `base_url` | STRING | Yes | Endpoint, if applicable | `https://...` |
| `is_active` | BOOLEAN | No | Whether the source is currently used | `true` |

### 5. `sync_logs`

Records of each synchronisation run.

| Field | Type | Nullable | Description | Example |
|-------|------|----------|-------------|---------|
| `sync_id` | UUID / INT | No | Primary key | `sync-001` |
| `source_id` | UUID / INT | No | Foreign key to `data_sources` | `s1` |
| `started_at` | TIMESTAMP | No | Run start time (UTC) | `2026-09-28T10:00:00Z` |
| `finished_at` | TIMESTAMP | Yes | Run end time (UTC) | `2026-09-28T10:00:12Z` |
| `status` | STRING | No | `success`, `partial`, or `failed` | `success` |
| `records_synced` | INT | No | Number of records processed | `240` |
| `error_message` | TEXT | Yes | Failure details, if any | `null` |

## Relationships

```
locations 1 ──── * observations
locations 1 ──── * forecasts
data_sources 1 ─ * observations
data_sources 1 ─ * sync_logs
```

## Enumerations

| Field | Allowed values |
|-------|----------------|
| `sync_logs.status` | `success`, `partial`, `failed` |
| `data_sources.type` | `api`, `sensor`, `file` |

## Data Quality Rules

- `humidity`, `cloud_cover`, and `precipitation_probability` must be between 0 and 100.
- `wind_direction` must be between 0 and 360.
- `latitude` must be between -90 and 90; `longitude` between -180 and 180.
- `pressure` is expected to fall roughly between 870 and 1085 hPa; values outside this range are flagged.
- Duplicate observations (same `location_id` and `observed_at`) are not allowed.

## Change Log for this Document

| Date | Change |
|------|--------|
| 2026-09-28 | Initial draft |

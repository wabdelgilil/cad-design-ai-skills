# SKILL-FA-01: Fire Alarm & Detection

> **Domain:** Fire detection, alarm, emergency voice
> **Standards:** SBC 801 (Fire Protection), SBC 401 Chapter 7, NFPA 72
> **Evidence:** layers `fire alarm 2` (297), `FIRE ALARM` (90), `LIGHT` (169),
> `Fire 1-19` (10)

---

## 1. ⭐ The critical layer warning

**Almost the entire fire-alarm device set sits on layer `LIGHT`** — a *lighting*
layer.

| Block | Inserts | Layer |
| :--- | --- | --- |
| `SMOKE.D` | **115** | `LIGHT` |
| `AUDIBLE APPLIANCE ( BELL )` | **29** | `LIGHT` |
| `FIRE ALARM MANUAL CALL STATION.` | **23** | `LIGHT` |
| `WEATHERPROOF ALARM SIREN WITH FLASHING LIGHT2` | 2 | `LIGHT` |

| Block | Inserts | Layer |
| :--- | --- | --- |
| `WE` | 26 | `FIRE ALARM` |
| `facp` | 1 | `fire alarm 2` |
| `A$Cbee9bb13` | 1 | `fire alarm 2` |

This is a legacy layer assignment in the consultant drawing. It is a **fact to
reproduce**, not a bug to fix. If the drawing is regenerated, keep the devices on
`LIGHT` unless the supervising engineer authorises a migration; a silent
migration breaks the block-to-layer link that QA checks against.

**Block-name traps:** `AUDIBLE APPLIANCE ( BELL )` and
`FIRE ALARM MANUAL CALL STATION.` both end with a **full stop** and the bell
name has **spaces inside the parentheses**. Copy them byte-for-byte.

---

## 2. ⭐ Device addressing (measured on layer `fire alarm 2`)

81 numeric text entities, forming **two address ranges**:

| Loop | Address range | Count |
| :--- | :--- | --- |
| **LOOP 01** | **2 … 48** | 47 devices |
| **LOOP 02** | **70 … 83** | 14 devices |

(The layer `Fire 1-19` carries the note `From FACP To -LOOP02`, confirming that
`70–83` is LOOP02.)

**Rules:**
- Addressing is **sequential and gap-free** inside each loop (`2,3,4…48`;
  `70,71,72…83`).
- Loop ranges **do not overlap** and are offset by 22 (48 → 70).
- The head-end is `facp` (Fire Alarm Control Panel), one per drawing, on
  `fire alarm 2`.
- Address 1 is **not used** — the first device is `2`.

---

## 3. ⭐ Loop cable (verbatim, layers `Fire 1-19` / `fire alarm 2`)

```
\pxqc;2x(2Cx1.5,CU) Fire Retardant Cable\P 01 No. %%C 25 Mm EMT Conduit
From FACP To -LOOP02
```

> **MTEXT-code warning.** The raw string carries `\pxqc;` (a wrapping
> **paragraph** code, ignorable) and the diameter symbol is written as the
> legacy AutoCAD code **`%%C`**, which renders as Ø. So the conduit is 25 mm Ø
> EMT — do not read `%%C` as text, and do not silently drop it, or the conduit
> diameter is lost. `\P` is a line break.

| Field | Value |
| :--- | --- |
| Cable | `2x(2Cx1.5,CU)` — **two** cables, each 2-core × 1.5 mm² copper |
| Type | **Fire Retardant** (not FP / not fire-rated-smoke — the drawing says *retardant*) |
| Conduit | `01 No. %%C 25 Mm EMT` — one 25 mm (Ø25) EMT conduit |
| Route | `From FACP To -LOOP02` |

Read the conduit as **25 mm Ø EMT**; the `Ø` is the `%%C` MTEXT code.

**Rule:** the loop cable in a fire system is routed in **EMT conduit**, sized
25 mm for a 1.5 mm² 2-core pair. Do not substitute PVC conduit for the loop.

---

## 4. Device mix and derived coverage

| Device | Count | Share |
| :--- | --- | --- |
| Smoke detectors `SMOKE.D` | 115 | 68 % |
| Bells / sounders `AUDIBLE APPLIANCE ( BELL )` | 29 | 17 % |
| Manual call stations | 23 | 13 % |
| Weatherproof sirens | 2 | 1 % |
| `WE` (layer `FIRE ALARM`) | 26 | — |
| **Total (layer `LIGHT`)** | **169** | 100 % |

The 115 : 29 : 23 ratio (**4 : 1 : 1**) is a useful sanity fingerprint for a
generated floor: roughly 4 detectors per sounder, 1 sounder per call station.

---

## 5. Coverage geometry

Layer `Camera System` style coverage polylines are not used here; the fire-alarm
coverage on layer `fire alarm 2` is drawn as `LWPOLYLINE` (123) + `CIRCLE` (25) +
`MTEXT` (81) + `LINE` (66). The 25 circles are the **detector coverage radii**,
and they are the measurable quantity for spacing verification:

**Verification method:** for every `SMOKE.D`, find the nearest `CIRCLE` on layer
`fire alarm 2` and record the radius. The distribution of those radii is the
project's actual design spacing, in drawing units. Compare it with SBC 801 /
NFPA 72 spacing for the ceiling height before accepting a generated layout.

> Do not hard-code a spacing number. Extract the circle radii, report the
> min/median/max, and let the engineer confirm against the room height.

---

## 6. Anti-Patterns

1. ❌ **Migrating fire-alarm devices to a new layer** without engineer approval —
   they are on `LIGHT` in the original.
2. ❌ **Using address `1`.** The first device is `2`.
3. ❌ **Overlapping the loop address ranges** — LOOP01 is 2–48, LOOP02 is 70–83.
4. ❌ **Substituting a 2-core-only loop cable** — the spec is `2x(2Cx1.5)`.
5. ❌ **Using PVC conduit for the loop** — it is 25 mm **EMT**.
6. ❌ **Dropping the trailing full stop** from `FIRE ALARM MANUAL CALL STATION.`
7. ❌ **Writing `AUDIBLE APPLIANCE (BELL)`** without the original's inner spaces.
8. ❌ **Claiming a detector spacing** without measuring the coverage circles.
9. ❌ **More than one `facp`** per drawing.

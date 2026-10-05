# SKILL-SEC-01: SECO Power Service & Main Incomer

> **Domain:** Utility service, main incoming feeder, MDB
> **Standards:** SBC 401, SECO (Saudi Electricity Company) distribution
> regulations
> **Evidence:** layer `E_SERVICE` (2 entities) and layer `E-SLD` (395 entities)

---

## 1. ⭐ The confirmed supply point (this settles the grid-voltage question)

Verbatim from layer `E_SERVICE`:

```
SCECO POWER SERVICE (R-Y-B-N) 400V-60HZ
```

| Parameter | Value | Consequence |
| :--- | :--- | :--- |
| Supplier | **SECO** (not SEC — the drawing writes SECO) | the utility is the *Saudi Electricity Company* |
| System | **400 V** | three-phase four-wire |
| Phases | **R – Y – B** | red, yellow, blue |
| Neutral | **N** present | a true 4-wire system, neutral is distributed |
| Frequency | **60 Hz** | Gulf standard, not 50 Hz |
| Phase-to-neutral | **230 V** | derived: 400/√3 |
| Phase-to-phase | **400 V** | derived |

> **This supersedes any assumption.** Per the project rule "verify the site
> voltage in `project_config.json`", the correct setting for this project is
> **400 V / 230 V, 4-wire, 60 Hz**.

**Consequence for breaker poles:**
- Ordinary 230 V single-phase loads → **1P** breakers from the 400 V system.
- 400 V three-phase loads (motors, risers, main incomer) → **3P** (or 4P).
- The consultant nevertheless specifies **2P** for the weather-proof AC
  isolators (see SKILL-SPR-03) — that is a deliberate local choice for
  fully-disconnecting a 230 V unit, not a system-voltage statement.

---

## 2. ⭐ The main feeder (verbatim, layer `E-SLD`)

```
FEEDER FROM SCECO
2X( (4X240) + 1x120 ) mm2 CU/XLPE/PVC\PUPVC   /   2X 160 MM  conduit
```

| Element | Specification |
| :--- | :--- |
| Quantity | **2 circuits** (2X) — dual incomer, i.e. **2 × incomer** |
| Each circuit | `4 × 240 mm²` + `1 × 120 mm²` |
| Insulation | **XLPE** |
| Sheath | **PVC** |
| Armour | **CU** (bare copper / unarmoured) |
| Outer sheath | `PUPVC` |
| Conduit | **2 × 160 mm** (one per circuit) |

**Read as:** two parallel 5-core feeders, each 4×240 + 1×120 mm² Cu/XLPE/PVC,
each in its own 160 mm conduit.

---

## 3. ⭐ Cable fill factor

```
CF = 0.594
```

Stated on the SLD by the consultant. Any conduit-fill calculation for this
project must use **0.594**, not the generic 0.53 (1 cable) / 0.31 (2 cables)
table values, unless the supervising engineer overrides it.

---

## 4. The feeder / distribution schedule (as drawn on `E-SLD`)

| Rating | Tag | T.D.L | Cable | Conduit |
| :--- | :--- | --- | :--- | --- |
| **200 A** | `KHW 200A` | **108.7 KVA** | `2X((4X240)+1x120) mm2 CU/XLPE/PVC\PUPVC` | `2 × 160 mm` |
| **63 A** | `KHW 63A` | 25.9 KVA / 23.0 KVA | `(4X120)+70 mm2` family | `160 mm DIA` |
| **40 A** | `KHW 40A` | **17.9 KVA** | `(4X16)+16 mm2 CU/XLPE/PVC` | `50 mm DIA` |
| — | — | **12.0 KVA** | `(4X10)+10 mm2 CU/XLPE/PVC` | `50 mm DIA` |

Read the column pattern: the conductor size follows the breaker
`(4×N) + N mm²` — i.e. one 4-core group plus one neutral of the same size:
`4×10+10`, `4×16+16`, `4×120+70`.

**`KHW` is the HVAC/air-conditioning breaker tag** — every one of these four
feeders is dedicated to air-conditioning, not to general power. See
SKILL-HVAC-01.

---

## 5. Cable & conduit notation (copy exactly)

| As drawn | Meaning |
| :--- | --- |
| `(4X10)+10 mm2 CU/XLPE/PVC\PPVC CONDUIT 50 MM DIA` | 4×10 mm² + 10 mm² neutral, Cu/XLPE/PVC, in 50 mm PVC conduit |
| `160mm DIA /PVC CONDUIT` | as above, on the homerun text |
| `IN PVC 20 MM DIA Each` | per-cable 20 mm PVC conduit (ELV) |
| `IN PVC 75 MM DIA` / `IN PVC 100 MM DIA` | ELV riser conduits |

`CU/XLPE/PVC` = copper / XLPE insulation / PVC sheath. Keep the slash-separated
form; do not rewrite as "XLPE/PVC copper".

---

## 6. Voltage-drop budget (project rule)

Per the project mandate:

- **Branch circuits:** VD < **3 %**
- **Full line from the meter:** VD < **5 %**

With a 6-floor building and 400 V supply, the split must be verified
calculation-by-calculation. The consultant's own KVA figures (108.7 / 25.9 /
23.0 / 17.9 / 12.0) are the anchor loads for those calculations.

---

## 7. Anti-Patterns

1. ❌ **Writing `SEC` instead of `SECO`.** The drawing says `SCECO POWER SERVICE`.
2. ❌ **Assuming 50 Hz.** The drawing says **60 Hz**.
3. ❌ **Assuming a 3-wire system.** `R-Y-B-N` is explicit: neutral is present
   and must be brought to every DB.
4. ❌ **Using 2P breakers as a *system* statement.** The 400 V system takes 1P
   for 230 V loads; the 2P on AC isolators is a disconnect choice.
5. ❌ **Using the 0.53 / 0.31 conduit-fill defaults** when the project specifies
   `CF = 0.594`.
6. ❌ **Sizing the main incomer below 200 A / 108.7 KVA** without a written
   engineer approval.
7. ❌ **Dropping the neutral** (`1x120`) from the feeder — it is part of the
   5-core spec.

# SKILL-PNL-01: Distribution Panels, SLD & Breaker Schedule

> **Domain:** Panel layout, single-line diagram, breaker sizing, load schedule
> **Evidence:** layers `E-SLD` (395), `E-MDB` (24), `E_Panel Board` (59),
> `CIRCUIT HOMERUNS TEXT` (529), `ELEC-LEGEND` (76)

---

## 1. The panel hierarchy

```
SCECO  400 V / 60 Hz   (R-Y-B-N)
   │
   ├── MDB                layer `E-MDB`   main distribution board
   │      │
   │      ├── AT1-DB … AT6-DB      6 boards
   │      ├── BT1-DB … BT12-DB    12 boards
   │      ├── CT1-DB, CT2-DB       2 boards
   │      └── BL-DB                1 board  (small-power riser)
   │
   └── branch circuits  NN/ <TAG>-DB        (see SKILL-XC-02)
```

**21 sub-distribution boards + 1 MDB.** The `AT` / `BT` / `CT` letter codes are
**not expanded anywhere in the drawing** — treat them as opaque identifiers and
never invent a meaning.

---

## 2. ⭐ The odd/even circuit allocation (applies per board)

| Circuit parity | System | Measured on |
| :--- | :--- | :--- |
| **Odd** `01, 03, 05, 07, 09, 11, 13, 15, 17, 19, 21, 25, 27, 29, 31, 33, 35` | **LIGHTING** | `BL-DB`, `AT3-DB`, `AT4-DB` |
| **Even** `04, 06, 08, 10, 12, 14, 16, 20, 26, 28, 30, 32, 34, 36, 38` | **SMALL POWER** | `BL-DB` |

Allocation steps by **2**, not by 1, so a lighting circuit always has a free
even number beside it. Full evidence table in SKILL-XC-02 §3.

---

## 3. ⭐ Breaker schedule as drawn

### 3.1 Feeder breakers (layer `E-SLD`)

| Tag | Rating | T.D.L | Cable | Conduit | Serves |
| :--- | :--- | --- | :--- | :--- | --- |
| `KHW 200A` | 200 A | 108.7 KVA | `2X((4X240)+1x120) CU/XLPE/PVC` | `2 × 160 mm` | main / largest HVAC group |
| `KHW 63A` | 63 A | 25.9 KVA | `(4X120)+70 CU/XLPE/PVC` | `160 mm DIA` | HVAC group |
| `KHW 63A` | 63 A | 23.0 KVA | — | — | HVAC group |
| `KHW 40A` | 40 A | 17.9 KVA | `(4X16)+16 CU/XLPE/PVC` | `50 mm DIA` | HVAC group |
| — | — | 12.0 KVA | `(4X10)+10 CU/XLPE/PVC` | `50 mm DIA` | HVAC group |
| `ELEVATOR-P` | — | — | — | — | elevator feeder |

### 3.2 The conductor-size pattern

```
(4 X 10) + 10 mm²      -> 50 mm conduit
(4 X 16) + 16 mm²      -> 50 mm conduit
(4 X 120) + 70 mm²     -> 160 mm conduit
(4 X 240) + 120 mm²    -> 2 x 160 mm conduit
```
Four cores plus a neutral sized to the phase conductors, except at 120 mm² where
the neutral is reduced to 70 mm². Reproduce the table verbatim; do not
re-derive the neutral from a generic rule.

### 3.3 Isolator legend (layer `ELEC-LEGEND`)

| Legend text | Rating |
| :--- | :--- |
| `32 A, 230V POWER SWITCH FOR SPLIT AC` | 32 A / 230 V |
| `40 A, 230V POWER ISOLATOR FOR CONCEALED AC ABOVE CEILING` | 40 A / 230 V |
| `40 A, 400V POWER ISOLATOR FOR CONCEALED AC ABOVE CEILING` | 40 A / 400 V |

Note the consultant provides **both** a 230 V and a 400 V 40 A concealed-AC
isolator. Choose by the mechanical schedule, not by default.

### 3.4 Weather-proof isolators (layer `E-POWR-TEXT`, 64 identical)

```
30A, 2P, 230V, IP65, (Weather Proof)
```

64 units, all identical. `2P` at 230 V = fully pole-wise isolation of a
single-phase unit. Copy this string exactly, including `IP65`.

---

## 4. T.D.L (Total Demand Load) — the load schedule

The consultant states `T.D.L = <value> KVA` next to each feeder. The values
measured on the SLD are:

```
108.7   25.9   23.0   17.9   12.0   (KVA)
```

The legend on layer `TEXT` confirms the sheet exists: `ELECTRICAL LOAD` (×8).

**Rule:** every new feeder added to this project must carry a `T.D.L = x.x KVA`
annotation on the SLD, formatted exactly like this (one decimal place, capital
`KVA`). A feeder without a T.D.L annotation is an incomplete drawing.

---

## 5. Panel-tag placement

Panel tags live on layer `E_Panel Board` (59 entities: 37 `MULTILEADER` + 22
`TEXT`) and are repeated on `E-SLD`. The 22 texts on `E_Panel Board` are exactly
the 21 `-DB` tags plus one leader node.

**Rule:** every panel symbol gets exactly one `TEXT` tag of the form
`XY<n>-DB` and one `MULTILEADER` connecting the tag to the board outline. The
leader and the tag must be on layer `E_Panel Board`; the tag text must not be
placed on layer `0`.

---

## 6. MDB

Layer `E-MDB` contains a single repeated block `A$C00FC56C5` (24 inserts). The
`A$C…` prefix is an AutoCAD auto-generated name — **never rename it**, or every
reference in the file is orphaned (see SKILL-XC-01 §5).

The MDB is where the two `2X((4X240)+1x120)` SECO feeders terminate.

---

## 7. Anti-Patterns

1. ❌ **Incrementing circuits by 1** — must step by 2 (odd lighting / even power).
2. ❌ **A feeder with no `T.D.L = x.x KVA`** annotation.
3. ❌ **A 1-decimal vs 2-decimal mismatch** — always one decimal (`17.9`, not `17.90`).
4. ❌ **Renaming `A$C00FC56C5`.**
5. ❌ **Inventing what `AT`/`BT`/`CT` stand for.**
6. ❌ **Using a 40 A concealed-AC isolator rated 400 V for a 230 V split unit** —
   use the 32 A/230 V switch for split AC, per the legend.
7. ❌ **Dropping the neutral from `(4X120)+70`** — 70 mm² is the stated neutral.
8. ❌ **Placing a panel tag on layer `0`** instead of `E_Panel Board`.

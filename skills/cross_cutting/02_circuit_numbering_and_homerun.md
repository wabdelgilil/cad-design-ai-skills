# SKILL-XC-02: Circuit Numbering, Homeruns & Panel Tagging

> **Domain:** ALL electrical systems (lighting, small power, HVAC, ELV)
> **Evidence:** 529 text strings on layer `CIRCUIT HOMERUNS TEXT`, 385 `tyfg`
> arrows on `CIRCUIT HOMERUNS POINTER`, all extracted verbatim from the
> consultant DWG.

---

## 1. The circuit reference format

```
<circuit number> / <panel tag>
```
Examples measured on the drawing: `01/ AT4-DB`, `03/ BT5-DB`, `21/ BL-DB`,
`160mm DIA /PVC CONDUIT`.

- The tag is always `<letters><number>-DB`.
- The circuit number is **zero-padded to two digits**.
- The legend on layer `lighting` states the rule in words:
  *"Lighting circuit number XX in panel named YY"*.

---

## 2. The panel-tag family (complete, measured)

| Family | Tags found | Count |
| :--- | :--- | --- |
| **AT** | `AT1-DB` … `AT6-DB` | 6 |
| **BT** | `BT1-DB` … `BT12-DB` | 12 |
| **CT** | `CT1-DB`, `CT2-DB` | 2 |
| **BL** | `BL-DB` (no number) | 1 |
| **MDB** | main distribution board, layer `E-MDB` | 24 inserts |

Total: **21 sub-distribution boards + 1 MDB** feeding the building.
Floors referenced in the SLD: `GROUND`, `FIRST`, `SECOND`, `THIRD`, `ROOF`,
`TOP ROOF`.

> The AT/BT/CT letters are **not decoded in the drawing**. Do not invent an
> expansion. Treat them as opaque panel identifiers.

---

## 3. ⭐ THE ODD/EVEN RULE (measured, not inferred)

From the 529 homerun texts on `CIRCUIT HOMERUNS TEXT`:

**Odd circuit numbers = LIGHTING. Even circuit numbers = SMALL POWER.**

Evidence on `BL-DB` alone:

| Odd → lighting | Even → power |
| :--- | :--- |
| `01/ BL-DB` | `04/ BL-DB` |
| `03/ BL-DB` | `06/ BL-DB` |
| `05/ BL-DB` | `08/ BL-DB` |
| `07/ BL-DB` | `10/ BL-DB` |
| `09/ BL-DB` | `12/ BL-DB` |
| `11/ BL-DB` | `14/ BL-DB` |
| `13/ BL-DB` | `16/ BL-DB` |
| `15/ BL-DB` | `20/ BL-DB` |
| `19/ BL-DB` | `26/ BL-DB` |
| `25/ BL-DB` | `28/ BL-DB` |
| `27/ BL-DB` | `30/ BL-DB` |
| `29/ BL-DB` | `32/ BL-DB` |
| `31/ BL-DB` | `34/ BL-DB` |
| `33/ BL-DB` | `36/ BL-DB` |
| `35/ BL-DB` | `38/ BL-DB` |

A secondary split is visible inside the odd set: `01/`, `03/`, `05/`, `07/` on
`AT3-DB` / `AT4-DB` are four distinct lighting circuits, so **odd numbers are
allocated in steps of 2** to leave room for an interleaved power circuit.

**Implementation rule:** allocate lighting circuits on odd numbers, power
circuits on even numbers, both incrementing by 2, per panel.

---

## 4. ⭐ The symmetry rule for homerun placement

Measured in the first-floor lighting plan: 16 rows of `tyfg` arrows and `pbx*`
circuit-line blocks all sit on a single vertical axis.

```
mean symmetry axis  X = 178.295      spread 178.290 … 178.305   (±0.015)
```

Verified mirrored pairs (same `y`, `x` equidistant from the axis):

```
y =  6.43   129.45  ↔  227.14
y =  9.54   113.65  ↔  242.94
y = 30.51   112.77  ↔  243.82      plus 134.65 ↔ 221.93
y = 34.90   114.24  ↔  242.35
y = 39.42   129.45  ↔  227.14
y = 66.65   151.14  ↔  205.45
y = 75.94   150.88  ↔  205.71       plus 172.76 ↔ 183.83
```

**Rule:** when laying out homerun arrows and their circuit-line runs, find the
plan's vertical centre axis and place every arrow at a **mirrored** distance
from it. Unpaired arrows on the axis are allowed (measured singletons at
`x = 178.29`, `x = 179.49`, `x = 177.10`).

**Axis detection algorithm:** collect all homerun-anchor x values, sort them, and
search for the value *a* that maximises the number of mirrored pairs
(x, 2a − x) present in the set, within a tolerance of 0.02. Report the winning
*a* and the residual spread.

---

## 5. Homerun block library (`pbx*`)

On layer `Circuit Line` the consultant used a **numbered segment kit**:

| Block | Inserts |
| :--- | :--- |
| `pbx1` … `pbx12` | 3 each (`pbx5` has 2) |
| `pbx13` … `pbx18` | 1 each |
| `*U38` | 17 (anonymous junction/crossing glyph) |

All 18 blocks exist in the block table; **use them instead of drawing free
polylines** for circuit runs, because the numbered kit is what makes a circuit
traceable on site. Reproduce the number sequence exactly.

---

## 6. Area tagging

Seven areas are declared on `CIRCUIT HOMERUNS TEXT`:
`AREA 01` … `AREA 07`.
Circuit references are not prefixed by area in the text itself, so the area is a
**drawing-zone** concept (which sheet/apartment block the circuit serves), not
part of the circuit number. Keep the two separate.

---

## 7. Timer-controlled circuits

`Controlled By Timer` appears 5 times on `CIRCUIT HOMERUNS TEXT`. These are
circuits (typically landscape, lobby and pump loads) that are switched by a
**timer** rather than a local switch. They still need their panel tag — in the
drawing's own format, e.g. `01/ BL-DB`, `37-39-41/ BL-DB` — plus the
`Controlled By Timer` note. Do not omit the note.

---

## 8. Circuit format used in the `Lighting Circuits` layer

`C XX YY P` appears 6 times on layer `Lighting Circuits` — a compact
`C <circuit> <panel> <pole/spare>` form. Preserve it when reproducing that layer;
do not normalise it to the `01/ BL-DB` form used on `CIRCUIT HOMERUNS TEXT`.

---

## 9. Anti-Patterns

1. ❌ **Allocating a lighting circuit on an even number** — contradicts the
   measured odd/even split of the whole drawing.
2. ❌ **One circuit per number (1,2,3,4… instead of 1,3,5,7…).** The consultant
   reserves even numbers for power.
3. ❌ **Homerun arrows placed at arbitrary coordinates** with no symmetry about
   the plan axis.
4. ❌ **Arrow with no panel tag** — every one of the 385 `tyfg` inserts must be
   paired with a panel reference such as `01/ BL-DB`.
5. ❌ **Dropping the `Controlled By Timer` note** on the 5 timed circuits.
6. ❌ **Expanding `AT`/`BT`/`CT` into invented words.**
7. ❌ **Drawing circuit runs as free polylines** instead of the `pbx*` kit.

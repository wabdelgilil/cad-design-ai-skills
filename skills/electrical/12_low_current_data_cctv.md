# SKILL-ELV-01: Low Current — Data, Telephone, TV/MATV, CCTV, Access

> **Domain:** ELV / ICT — the combined data-telecom-TV-CCTV system
> **Standards:** SBC 401 Chapter 8 (communications), TIA-568, BICSI
> **Evidence:** layers `E-DATA` (167), `E-TEL` (52), `E-TV` (2), `tele` (14),
> `Camera System` (206), `E-SLD`/`ELEC-TEXT` (cable schedule), `Power` (floor boxes)

---

## 1. System overview (as drawn)

```
MAIN (DATA TELE CCTV) RACK  WALL MOUNTED (20U)      x2     <- 20U main racks
        │
        ├── A TYPE (DATA TELE) RACK  WALL MOUNTED (8U)   x8
        ├── B TYPE (DATA TELE) RACK  WALL MOUNTED (8U)   x6
        │        └── "NO. OF TYPICAL RACKS" = 1, 2 and 4
        │
        ├── MATV BOX + CASCADABLE ACTIVE/PASSIVE MULTISWITCH
        ├── EL-SAT-DISH  x6
        └── TCP/IP GATWAY INTERFACE  <->  INTERFACE WITH DATA SYSTEM (RS-232 / RJ-45)

Outlets:  TEL1 x50, TEL12 x1, TV1 x2, DATA OUTLET, TELEPHON OUTLET
Floor boxes: see §4
CCTV: layer `Camera System` (206 entities)
```

---

## 2. ⭐ The ELV cable schedule (verbatim)

All on layer `E-SLD` / `ELEC-TEXT`. Copy the strings exactly.

### 2.1 Copper

| As drawn | Use |
| :--- | --- |
| `02.Nos unshielded Twisted Pair (UTP) Telephone Cable (Typical)` | 2-pair tel |
| `03.Nos unshielded Twisted Pair (UTP) Telephone Cable (Typical)` | 3-pair tel |
| `04.Nos unshielded Twisted Pair (UTP) Telephone Cable (Typical)` | 4-pair tel |
| `06.Nos unshielded Twisted Pair (UTP) Telephone Cable (Typical)` | 6-pair tel |
| `05.Nos unshielded Twisted Pair CATE 6 (UTP) DATA Cable (Typical)` | 5× Cat6 data |

Terminations are given on the same layer as `02 Nos.(RJ-11)`, `03 Nos.(RJ-11)`,
`04 Nos.(RJ-11)`, `06 Nos.(RJ-11)`.

> `CATE 6` is a typo for **CAT 6** in the original — reproduce it as drawn.
> Outlet labels on the SLD read `TELEPHON OUTLET` (missing the final `E`) and
> `DATA OUTLET`; both typos are in the original and must be preserved.

### 2.2 Fibre

```
20.Nos unshielded Twisted Pair (UTP) Telephone Cable (Typical) & 20.Nos (SM)FIBER OPTIC CABLE (SMFO)
14.Nos ... & 14.Nos (SM)FIBER OPTIC CABLE (SMFO)
08.Nos ... & 08.Nos (SM)FIBER OPTIC CABLE (SMFO)
02.Nos ... & 02.Nos (SM)FIBER OPTIC CABLE (SMFO)
```

Pattern: **the fibre count always equals the UTP pair count**, and the fibre is
single-mode (`SM`) in an `SMFO` cable. Run them in the same containment.

### 2.3 Coaxial / MATV

| As drawn | Use |
| :--- | --- |
| `12xCOAXIAL (RG-11) TV CABLE   IN PVC 100 MM DIA` | main TV riser (12× RG-11) |
| `02 Nos.COAXIAL RG 6` | branch, small |
| `06 Nos.COAXIAL RG 6` | branch, medium |
| `12 Nos.COAXIAL RG 11` | trunk |
| `IN PVC 20 MM DIA Each` | **per-cable** 20 mm PVC conduit |
| `IN PVC 75 MM DIA` | sub-riser |
| `IN PVC 100 MM DIA` | main riser |

**Rule:** when `IN PVC … Each` is specified, provide **one conduit per cable** —
do not bundle.

Equipment: `CASCADABLE ACTIVE MULTISWITCH` (×2) and
`CASCADABLE PASSIVE MULTISWITCH` (×2), plus `MATV BOX` ×4.
Antenna: `T.V. ANTENNA (UHF-VHF)` and `T.V. lightning arrestor` on layer `tele`,
with `EL-SAT-DISH` ×6.

---

## 3. Rack schedule

| Rack | Type | Wall mounted | Height | Qty |
| :--- | :--- | :--- | :--- | --- |
| Main | `(DATA TELE CCTV)` | yes | **20U** | 2 |
| A type | `(DATA TELE)` | yes | **8U** | 8 |
| B type | `(DATA TELE)` | yes | **8U** | 6 |

Text on the SLD: `NO. OF TYPICAL RACKS` = **1, 2 and 4** — i.e. the number of
typical racks varies by floor; the value is stated per floor, not globally.

**Rule:** rack labels must carry the rack type letter, the U height, and the
quantity note, in that order, matching `A TYPE (DATA TELE) RACK WALL MOUNTED (8U)`.

---

## 4. ⭐ Floor boxes (shared power + data + TV)

Two composition variants appear verbatim on layer `E-DATA`:

```
FLOOR BOX
 1 Doublex Power
 1 Data Outlet
 1 TV Outlet                                       (x20)
```

```
FLOOR BOX
 2 Doublex Power
 1 Data
 1 Tele
 1 HDMI                                           (x1)
```

A floor box is therefore a **multi-service** outlet, and it is split across two
layers:

| Component | Block | Layer |
| :--- | :--- | --- |
| `Doublex Power` | `Boublex Outlet` | `Power` |
| `Data Outlet` / `Data` | (ICT symbol) | `E-DATA` |
| `TV Outlet` | `TV1` | `E-TV` |
| `Tele` | `TEL1` | `E-TEL` |
| `HDMI` | (ICT symbol) | `E-DATA` |

The electrical floor-box symbol is `Floor box 2` (×21) on layer `Power`.

---

## 5. Telephone

| Block | Inserts | Layer |
| :--- | --- | --- |
| `TEL1` | **50** | `E-TEL` |
| `TEL12` | 1 | `E-TEL` |

`TEL1` is the standard single telephone outlet; `TEL12` appears once and is a
special/secondary position. Do not generalise the 12- variant.

---

## 6. CCTV

Layer `Camera System` (206 entities):

| Content | Count |
| :--- | --- |
| `VCR` | 1 |
| `Monitor` | 1 |
| `LWPOLYLINE` (camera field-of-view / coverage) | 204 |

The camera head symbols themselves are **not** on this layer — only the
head-end equipment and the coverage geometry. Any new camera must be placed with
its coverage polyline on `Camera System`, and the head-end
(`VCR`, `Monitor`) reserved at the main rack.

**Note:** `VCR` (video cassette recorder) is the era-correct term used by the
consultant. Use it for fidelity; do not silently substitute "NVR/DVR" in a
reproduction.

---

## 7. Interface requirements

```
INTERFACE WITH DATA SYSTEM (RS-232/RJ-45)
TCP/IP GATWAY INTERFACE
```

The ELV system interfaces with the BMS/other systems through a TCP/IP gateway.
The gateway is a boundary point: power for it belongs to the small-power system,
its wiring to the ELV system.

---

## 8. Anti-Patterns

1. ❌ **Bundling cables when the schedule says `IN PVC … Each`** — one conduit
   per cable.
2. ❌ **Writing `CAT 6` instead of the drawing's `CATE 6`** in a reproduction.
3. ❌ **Fibre count ≠ UTP pair count** — they are always equal in this schedule.
4. ❌ **Putting the power half of a floor box on layer `E-DATA`** — it belongs on
   `Power` as `Boublex Outlet`.
5. ❌ **Specifying a 9U or 12U rack** — only **8U** and **20U** appear.
6. ❌ **Substituting `NVR`/`DVR` for `VCR`** in a faithful reproduction.
7. ❌ **A rack with no `NO. OF TYPICAL RACKS` note** for its floor.
8. ❌ **Forgetting the `T.V. lightning arrestor`** on the antenna riser.

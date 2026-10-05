# SKILL-XC-01: Layer & Symbol Fidelity (Cross-Cutting Foundation)

> **Domain:** ALL electrical systems
> **Level:** Mandatory precondition for every drawing operation
> **Reference drawing:** `examples/sample_project/cad/sample_building_electrical.dwg`
> **Machine source of truth:** `examples/sample_project/scripts/custom_rules.py`
> **Extraction scripts:** `examples/sample_project/systems_audit/`

---

## 1. Why this skill exists

Every other skill in this library was, at some point, wrong because it named a
block or a layer that **does not exist** in the consultant drawing. Those errors
are silent: AutoCAD happily creates a new layer with a made-up name, the plot
looks plausible, and the mistake is only discovered at QA.

This skill makes the check mechanical instead of visual.

---

## 2. The five facts about the reference DWG

| Fact | Value | Consequence |
| :--- | :--- | :--- |
| Entities in ModelSpace | **21,735** | Small enough to parse offline with `ezdxf` |
| Layers | **231** | Use the real list, never a subset by memory |
| Blocks | **938** | Not 259 — earlier partial audits under-counted |
| Paper-space layouts | **3** (`Layout1`, `Layout2` empty) | **All 113 sheets live inside ModelSpace.** There is no per-sheet layout to select; sheets must be located by geometry. |
| `$INSUNITS` / `$LUNITS` / `$MEASUREMENT` | `1` / `2` / `0` | Declares **inches**, decimal, imperial — but this **contradicts the geometry** and must be ignored (see §6). |

---

## 3. The layer table (all 231 exist; these are the ones used)

### 3.1 Power / small power
| Layer | Entities | Content |
| :--- | --- | --- |
| `Power` | 803 | sockets, floor boxes, `W.P.` annotations |
| `Power Circuits` | 82 | power homeruns (`d s`) + the water-pump note |
| `E-POWER` | 26 | `WAP` (water-heater / wet-area power) |
| `E_Wire Power` | 120 | power wire runs |
| `E-POWR-TEXT` | 64 | isolator rating text `30A,2P, 230V,IP65,(Weather Proof)` |
| `WATER SUPPLY` | 71 | `HEATER` symbols (plumbing coordination) |
| `electerc` | 84 | electrical-contractor layer (`A$C4DEA2E59`) |

### 3.2 Distribution / panels
| Layer | Entities | Content |
| :--- | --- | --- |
| `E-SLD` | 395 | **the single-line diagram + feeder/cable schedule** |
| `E-MDB` | 24 | main distribution board |
| `E_Panel Board` | 59 | panel tags + leaders |
| `CIRCUIT HOMERUNS POINTER` | 385 | `tyfg` arrows |
| `CIRCUIT HOMERUNS TEXT` | 529 | the `NN/ PANEL-DB` circuit references |
| `E_SERVICE` | 2 | `SCECO POWER SERVICE (R-Y-B-N) 400V-60HZ` |
| `ELEC-LEGEND` | 76 | isolator legend |
| `ELEC-TEXT` | 202 | ELV rack schedule + floor names |
| `TEXT` | 310 | sheet titles, `ELECTRICAL LOAD` |

### 3.3 HVAC power
| Layer | Entities | Content |
| :--- | --- | --- |
| `12- EQUIPMENT-HVAC` | 73 | `AXI-F-IL1` inline fans |
| `M-HVAC-REFP` | 81 | `G$C7580D14A` mechanical reference |

### 3.4 Low current / ELV
| Layer | Entities | Content |
| :--- | --- | --- |
| `E-DATA` | 167 | floor boxes, wall racks, `MATV BOX` |
| `E-TEL` | 52 | `TEL1`, `TEL12` |
| `E-TV` | 2 | `TV1` |
| `tele` | 14 | `EL-SAT-DISH` (satellite dishes) |
| `Camera System` | 206 | CCTV coverage + `VCR` / `Monitor` |
| `Speakers` | 325 | PA system |

### 3.5 Fire alarm
| Layer | Entities | Content |
| :--- | --- | --- |
| `LIGHT` | 169 | `SMOKE.D`, bells, manual call stations, sirens |
| `FIRE ALARM` | 90 | `WE` |
| `fire alarm 2` | 297 | `facp` + device address numbers 2–48, 70–83 |
| `Fire 1-19` | 10 | loop cable notes |

### 3.6 Earthing / lightning
| Layer | Entities | Content |
| :--- | --- | --- |
| `L.P` | 56 | `LP Rod` ×18, `Earthing bit` ×6 |
| `E-GN-TXT` | 89 | `12.7 MM BOLT` |
| `E-GN-DTL` | 247 | earthing detail |
| `E-TEXT` | 10 | `EARTHING SYSTEM` |
| `E-WIRE-L` | 49 | earthing-bond note |

### 3.7 Lighting (reference only)
`lighting` (1,733), `E-LTG` (740), `Lighting Circuits` (982), `CIRCUIT HOMERUNS *`,
`Elec - lighting` (84), `E-SWITCH` (77), `Circuit Line` (109), `cable lighting` (102),
`LTG Wiring`, `E-LIGHT`, `E-LT-TXT`, `ELECTRICAL LIGHT SYMBOL`, `E-ELEC-FIXT`.

---

## 4. Layers and blocks that DO NOT EXIST

Referencing any of these from a skill or a script is a **bug**:

| Invented name | Where it came from | Real alternative |
| :--- | :--- | :--- |
| `Lighting-Fixtures` | SKILL-LGT-01/03/04/05 | `lighting` or `E-LTG` |
| `Lighting-Switches` | SKILL-LGT-02/05 | `lighting` or `E-SWITCH` |
| `E-LITE-COVE` | SKILL-LGT-03/04 | `E-LTG` (decorative/indirect) |
| `E-LITE-CIRC` | SKILL-LGT-03 | `Lighting Circuits`, `Circuit Line`, `LTG Wiring` |
| `Junction_Box` (as a block) | SKILL-LGT-03/04 | not in the 938-block table at all |
| `E-SWITCHES` | variant typo | `E-SWITCH` |
| `E-LITE-COVE-FEED` | invented | — |

---

## 5. The block-name traps (real names that look like mistakes)

The consultant drawing contains names that are **typos in the original**. They
must be reproduced **exactly**. "Correcting" them breaks every block reference.

| Exact name (use this) | Trap |
| :--- | :--- |
| `Grass Lightign` | *Lighting* is misspelled |
| `Boublex Outlet` | *Doublex* is misspelled |
| `AXI-F-IL1` | HVAC inline fan, **not** a bathroom fan |
| `Ceiling Sliding flexible lighting spots` | spec text is nonsense English |
| `poollll`, `2006_2_0`, `2222111`, `e-w3` | scratch/garbage names, still real blocks |
| `A$C4DEA2E59`, `G$C7580D14A`, `A$C00FC56C5`, `A$Cbee9bb13` | AutoCAD auto-generated (`A$C…`) — never rename |
| `FFGJIGJFJKGF8878`, `gfgfgfgfkgfklgkf88555`, `weqqqqqqqq`, `GFGIJFKGJFJKGF8899996666` | consultant keyboard-mash names, heavily used (96, 20, 1, 6 inserts) |

### 5.1 `Switch 2` vs `Switch 2 Gang` — two DIFFERENT blocks
```
Switch 2         56 inserts   layer `lighting`
Switch 2 Gang    89 inserts   layer `lighting`
```
They are not synonyms. Never substitute one for the other.

---

## 6. Drawing units — resolved, and the trap that hid it

`$INSUNITS = 1` declares **inches**, but the measured geometry is inconsistent with
inches (room extents and a 0.9 m door both come out as metre-scale numbers when
the units are taken as millimetres). The header variable is **stale** and was
never updated by the consultant.

**Rule:** treat the geometry as **millimetres** (the usual export convention for a
Saudi consultant DWG), and never let a generator read `$INSUNITS` to decide.
Unit conversion must be an explicit, documented parameter.

---

## 7. Mechanical pre-flight check (mandatory before any write)

```python
# projects/[PROJECT]/scripts/validate_symbols.py
import json, sys

CENSUS = "extracted_data/old_electrical_audit/dwg_inventory.json"

def validate(layers, blocks):
    dwg = json.load(open(CENSUS, encoding="utf-8"))
    bad_l = [l for l in layers if l not in dwg["layers"]]
    bad_b = [b for b in blocks if b not in dwg["blocks"]]
    if bad_l or bad_b:
        raise SystemExit(f"INVENTED  layers={bad_l}  blocks={bad_b}")
    return True
```

Run this on **every** block name and layer name a generator is about to emit. A
failure means the name came from memory instead of from the drawing.

---

## 8. Anti-Patterns

1. ❌ **Typo correction** — renaming `Grass Lightign` to `Grass Lighting`. The
   plot then shows a missing block.
2. ❌ **Assuming one layout per sheet.** All 113 sheets are in ModelSpace.
3. ❌ **Trusting `$INSUNITS`.** It says inches; the geometry is millimetres.
4. ❌ **Substituting `Switch 2` for `Switch 2 Gang`.** Different symbols.
5. ❌ **Placing `AXI-F-IL1` on a lighting layer.** It belongs to `12- EQUIPMENT-HVAC`.
6. ❌ **Renaming `A$C…` blocks.** They are AutoCAD fingerprints; renaming
   orphans every reference in the file.
7. ❌ **"Tidying" the keyboard-mash blocks.** 96 inserts depend on
   `FFGJIGJFJKGF8878` alone.

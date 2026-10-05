# Master Lighting Skills Library (Core Architectural & Electrical Knowledge)

This directory contains modular, standardized engineering skills governing electrical lighting design, circuiting, and CAD drafting automation. Every skill merges **Fundamental International & Saudi Standards (SBC 401, IEC 60364, IESNA, CIBSE)** with **Inductive Practical Heuristics extracted from top-tier consultant reference drawings**.

---

## Skills Index & Modular Architecture

| Code | Skill Document | Core Domain & Focus | Key Standard / Reference |
| :--- | :--- | :--- | :--- |
| **SKILL-LGT-01** | [`01_fixture_placement_and_grids.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/01_fixture_placement_and_grids.md) | Symmetrical downlight grids ($X_{\text{top}} = X_{\text{bottom}}$), bedside sconces flush mounting, task lighting, architectural clearances. | CIBSE SLL / IESNA / SBC 401 |
| **SKILL-LGT-02** | [`02_switching_and_control_topology.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/02_switching_and_control_topology.md) | Entrance strike-side positioning, 2-way bedside switch geometric mirroring, gang splitting and control ergonomics. | SBC 401 / IEC 60364 |
| **SKILL-LGT-03** | [`03_aesthetic_wiring_and_routing.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/03_aesthetic_wiring_and_routing.md) | Orthogonal & concentric circuit looping, elimination of diagonal spiderwebs, junction boxes, homerun arrow standards. | Professional CAD Practice |
| **SKILL-LGT-04** | [`04_cove_lighting_and_power_feeds.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/04_cove_lighting_and_power_feeds.md) | Indirect cove lighting, uniform wall setback ($35\text{ cm}$), LED driver feed boxes, switching legs. | IESNA Ambient Lighting |
| **SKILL-LGT-05** | [`05_wet_areas_and_services.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/05_wet_areas_and_services.md) | Bathrooms, kitchens, and utilities: fan centered over toilet, vanity mirror light orientation, IP moisture zoning (Zones 0, 1, 2). | SBC 401 Sec 701 / IEC 60364-7-701 |
| **SKILL-LGT-06** | [`06_branch_circuit_loading_and_zoning.md`](file:///d:/programming/ElectricalDesign/core/skills/lighting/06_branch_circuit_loading_and_zoning.md) | Branch circuit loading, 80% continuous rating, functional zoning (Wet, Hospitality, Circulation, Suite), phase balancing (R/Y/B), and Type C MCBs. | SBC 401 / NEC Art 210 / IEC 60898 |

---

## Knowledge Engine Integration

These skill files serve as the programmatic single source of truth for all lighting automation scripts located in:
- `core/electrical_engine/lighting_calculator.py`
- `examples/sample_project/`
- Future production generators under `projects/[PROJECT_NAME]/scripts/`

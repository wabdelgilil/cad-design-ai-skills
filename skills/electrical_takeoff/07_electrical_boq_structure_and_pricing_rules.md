# SKILL-ELE-QTO-07: Electrical BOQ Architecture & Rate Analysis Rules 📊💰

> **The standard 5-tab electrical BOQ structure, mathematical derivation matrices for hidden accessories, procurement margins, and Saudi Arabia 2026 unit rate benchmarks.**

---

## 1. The Standard 5-Tab Electrical BOQ Architecture

To achieve consulting-grade quality, the Electrical BOQ must be organized across **5 dedicated, interactive tabs with 100% dynamic Excel formulas (`=SUM()`, `=ROUND()`)**:

```
5-Tab Electrical BOQ Standard:
├── Tab 1: Executive Summary (ملخص التكلفة والحصر العام)
│   ├── Total Project Cost per System (Lighting, Power, Panels, Feeders, Low Current, Fire Alarm)
│   ├── Material vs. Labor Cost Breakdown & KPI Cards
│   └── Cost per Apartment / Unit (SAR/Unit)
├── Tab 2: Floor by Floor Takeoff (حصر الأدوار التفصيلي)
│   ├── Ground Floor, Typical Floors (1-3), Roof Floor, Upper Roof & Services
│   └── Space-by-Space Fixture Schedules
├── Tab 3: Detailed Priced BOQ & Specs (جدول الأسعار والمواصفات الفنية)
│   ├── Detailed itemized scope with full specifications and approved vendor brands
│   └── Dynamic separation of Material Supply Rate, Labor Rate, and Combined Unit Rate
├── Tab 4: Feeder Cables & Containment (شبكات الكابلات والصواعد ومجاري الحوامل)
│   ├── True 3D Sub-Feeder Schedule (Length, Conductor Sizing, Glands, Lugs, Trays)
│   └── Voltage Drop Verification Matrix
└── Tab 5: Fittings, Backboxes & Consumables (قطع الوصل، العلب الماجيك، والمستهلكات)
    ├── Derivation table for GI backboxes, pull boxes, couplings, cement, and saddles
    └── Procurement Buffer (+10%) for cutting waste and site breakages
```

---

## 2. Mathematical Derivation Matrix for Hidden Accessories

Never omit the hidden containment accessories. Apply these empirical derivation ratios:

| Primary Counted Element | Derived Secondary Accessory | Derivation Formula / Multiplier | Engineering Rationale |
| :--- | :--- | :---: | :--- |
| **Every Wall Switch (1 to 3 Gang)** | 75x75x35mm Flush GI Box | $N_{\text{boxes}} = 1.0 \times N_{\text{switches}}$ | Galvanized flush backbox embedded in plaster |
| **Every Twin 13A Socket** | 135x75x35mm Flush GI Box | $N_{\text{boxes}} = 1.0 \times N_{\text{sockets}}$ | Double gang backbox |
| **Every Water Heater / 20A Isolator**| 75x75x47mm Deep GI Box | $N_{\text{boxes}} = 1.0 \times N_{\text{isolators}}$ | Deep box required to accommodate heavy 4mm² wires |
| **Every 45A Cooker Control Unit** | 135x75x47mm Deep GI Box | $N_{\text{boxes}} = 1.0 \times N_{\text{cookers}}$ | Extra depth for 10mm² conductor loops |
| **Ceiling Lighting Drops (100 m)** | 20mm Circular BESA Box | $N_{\text{boxes}} \approx 25 \text{ pcs per 100m}$ | Junction and suspension point per luminaire |
| **Wall/Ceiling Conduit (100 m)** | Galvanized Saddles / Clips | $N_{\text{clips}} = \frac{100}{0.80} = 125 \text{ pcs}$ | Fixed every 80 cm on ceiling and walls |
| **Conduit Runs (100 m)** | Conduit Couplings & Adapters | $N_{\text{couplings}} \approx 35 \text{ pcs per 100m}$ | 3.0m standard pipe length + box male adapters |
| **Conduit Wire Pulling (100 m)** | Solvent Cement & Primer | 1 Can (250 ml) per 50 meters | Cold solvent welding of PVC joints |
| **Armored SWA Cable (Each Run)** | Brass Gland Kits & Lugs | 2x Gland Kits + 8x Copper Lugs | Terminations at source and destination panels |

---

## 3. Saudi Arabia 2026 Unit Rate Benchmarks (Eastern Province - SAR)

Realistic turnkey execution pricing for high-end residential and commercial buildings in **Al-Khobar / Dammam (SAR 2026)**:

### A. Lighting & Controls:
* **Recessed LED Spotlight 7W-10W (IP20):** Supply = 28 - 45 SAR | Installation = 15 - 25 SAR $\rightarrow$ **Total = 43 - 70 SAR/pt**.
* **Waterproof Bathroom LED Spotlight (IP65):** Supply = 38 - 60 SAR | Installation = 18 - 28 SAR $\rightarrow$ **Total = 56 - 88 SAR/pt**.
* **Linear LED Strip 24V with Profile & Driver:** Supply = 35 - 55 SAR/m | Installation = 20 - 30 SAR/m $\rightarrow$ **Total = 55 - 85 SAR/m**.
* **1-Gang / 2-Gang Switch (Schneider / Legrand):** Supply = 22 - 35 SAR | Installation = 10 - 15 SAR $\rightarrow$ **Total = 32 - 50 SAR/pt**.
* **PIR Ceiling Motion Sensor:** Supply = 85 - 140 SAR | Installation = 30 - 45 SAR $\rightarrow$ **Total = 115 - 185 SAR/pt**.

### B. Small Power & Isolators:
* **Twin 13A Switched Socket (UK BS 1363):** Supply = 28 - 45 SAR | Installation = 12 - 20 SAR $\rightarrow$ **Total = 40 - 65 SAR/pt**.
* **Weatherproof IP65 13A Twin Socket:** Supply = 65 - 95 SAR | Installation = 25 - 35 SAR $\rightarrow$ **Total = 90 - 130 SAR/pt**.
* **20A DP Water Heater Switch with Neon:** Supply = 35 - 50 SAR | Installation = 15 - 25 SAR $\rightarrow$ **Total = 50 - 75 SAR/pt**.
* **45A Cooker Control Unit with Socket:** Supply = 75 - 120 SAR | Installation = 25 - 40 SAR $\rightarrow$ **Total = 100 - 160 SAR/pt**.
* **32A 4P Weatherproof AC Isolator (IP65):** Supply = 85 - 130 SAR | Installation = 30 - 45 SAR $\rightarrow$ **Total = 115 - 175 SAR/pt**.

### C. Distribution Boards & Cable Trays:
* **Apartment Final DB 24-Way TPN (Schneider/ABB):** Supply = 1,400 - 2,200 SAR | Installation = 350 - 550 SAR $\rightarrow$ **Total = 1,750 - 2,750 SAR/panel**.
* **Apartment Final DB 36-Way TPN:** Supply = 2,100 - 3,200 SAR | Installation = 450 - 700 SAR $\rightarrow$ **Total = 2,550 - 3,900 SAR/panel**.
* **Sub-Feeder Cable $4 \times 25 \text{ mm}^2$ XLPE/SWA/PVC:** Supply = 65 - 85 SAR/m | Installation = 22 - 32 SAR/m $\rightarrow$ **Total = 87 - 117 SAR/m**.
* **Perforated Cable Tray 200x50mm HDG with Cover:** Supply = 45 - 65 SAR/m | Installation = 25 - 35 SAR/m $\rightarrow$ **Total = 70 - 100 SAR/m**.

### D. Life Safety & Low Current:
* **Addressable Optical Smoke Detector:** Supply = 95 - 150 SAR | Installation = 30 - 45 SAR $\rightarrow$ **Total = 125 - 195 SAR/pt**.
* **Addressable Sounder / Strobe Beacon:** Supply = 160 - 240 SAR | Installation = 35 - 50 SAR $\rightarrow$ **Total = 195 - 290 SAR/pt**.
* **Twin Cat6A Data Outlet (Complete with Faceplate):** Supply = 45 - 75 SAR | Installation = 20 - 30 SAR $\rightarrow$ **Total = 65 - 105 SAR/pt**.
* **Complete Earth Pit (Rod + Pit + Compound + Clamp):** Supply = 380 - 600 SAR | Installation = 150 - 250 SAR $\rightarrow$ **Total = 530 - 850 SAR/pit**.

---

## 4. Procurement Margin Policy

* **All Point Fixtures & Hardware:** Exact net design count $+ 10\%$ procurement buffer.
* **All Conduits, Wires, and Cabling:** True 3D calculated length $+ 10\%$ waste/cutting allowance.
* **Consumables (Glue, Tapes, Screws, Anchors):** Lump sum estimated at $2.5\% \text{ to } 3.5\%$ of direct installation materials.

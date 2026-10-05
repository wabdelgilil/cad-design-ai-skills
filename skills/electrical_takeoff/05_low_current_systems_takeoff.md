# SKILL-ELE-QTO-05: Low Current & ICT Systems Takeoff 📡📹

> **Engineering guide for quantifying Structured Cabling (Cat6A), CCTV surveillance, SMATV satellite networks, Intercom systems, and Public Address (PA) infrastructure.**

---

## 1. Structured Cabling & Data/Voice Network (ICT)

### A. Field Outlets & Faceplates:
* **Twin RJ45 Cat6A Data Outlet:** Standard behind Smart TVs, work desks, and living rooms. Includes 2x Cat6A unshielded/shielded toolless keystone jacks + faceplate with shutter + label window.
* **Single RJ45 Data Outlet:** Dedicated feeds for Wireless Access Points (WAP) on ceiling and IP Intercom monitors.
* **Ceiling WAP Outlet:** Installed in hallway ceiling slabs to provide full WiFi coverage without dead zones.

### B. Horizontal UTP/FTP Cable Takeoff:
* Each RJ45 port requires a dedicated, continuous home-run 4-pair cable (Zero daisy-chaining permitted):
  $$L_{\text{cable\_per\_drop}} = \left( L_{\text{horizontal}} + H_{\text{wall\_drop}} + H_{\text{rack\_drop}} + 3.0\text{m (Cabinet Slack)} + 0.5\text{m (Outlet Slack)} \right) \times 1.05$$
* **Standard Cable Packaging:** Supplied in 305-meter (1,000 ft) pull boxes.
  $$\text{Boxes of Cat6A Cable} = \left\lceil \frac{\sum L_{\text{cable\_runs}}}{305 \times 0.90} \right\rceil \quad \text{(Accounting for 10% offcut scrap)}$$

### C. Floor Distributor / Main Telecom Room (MTR):
* **Floor Telecom Cabinet (IDF):** 9U / 12U / 18U Wall-mounted 19" rack with glass door, ventilation fans, and PDU.
* **Central Server Rack (MDF):** 42U Free-standing 19" rack (800x1000mm) located in Ground Floor / Basement IT Room.
* **Patch Panels:** 24-Port Cat6A 1U Modular Patch Panel (1 panel for every 24 field data drops).

---

## 2. IP Closed-Circuit Television (CCTV)

### A. Camera Classifications:
1. **Indoor Fixed Dome Cameras (4MP / 8MP):** Wide-angle lens ($2.8\text{mm}$), IR night vision up to 30m, PoE powered. Located at entrance lobbies, corridors, lift lobbies, and staircase landings.
2. **Outdoor Bullet / Turret Cameras (IP67 / IK10):** Motorized varifocal lens ($2.8 - 12\text{mm}$), WDR 120dB, IR up to 50m. Located at building perimeter, vehicle parking gates, and rooftop.
3. **Elevator Traveling Camera:** Specialized wide-angle camera with flat elevator traveling cable.

### B. Video Recording & Storage:
* **Network Video Recorder (NVR):** 32-Channel or 64-Channel 4K NVR with redundant power supply and RAID storage.
* **Surveillance Hard Drives:** Enterprise 24/7 HDDs sized for 31 days continuous recording at 15-20 fps (e.g., $4 \times 8\text{TB} = 32\text{TB}$).

---

## 3. Satellite Master Antenna Television (SMATV)

* **Rooftop Antenna & Dish Array:** 2x High-gain parabolic satellite dishes (120cm - 180cm) with Quattro LNBs.
* **Multiswitches (Cascade / Standalone):** 9x16 or 9x24 multiswitches installed in electrical/telecom shafts.
* **Coaxial Cables:**
  * **RG6 Coaxial Cable (Drop Cable):** From floor multiswitch to apartment TV wall outlets (Loss $< 20\text{ dB/100m @ 1000MHz}$).
  * **RG11 Coaxial Cable (Main Trunk Cable):** From rooftop dishes down through shafts to multiswitches.
* **TV Outlets:** Isolated Screened TV/FM/SAT Triplexer Faceplates.

---

## 4. IP Video Intercom & Public Address (PA)

### A. Intercom Architecture:
* **Outdoor Master Station:** Heavy-duty vandal-resistant IP65 aluminum door station with 7" touchscreen, HD camera, keypad, and RFID card reader.
* **Indoor Apartment Stations:** 7" capacitive color touchscreen monitors inside each apartment (near entrance door at $+1.50$ m). Powered by PoE via standard Cat6 cable.

### B. Public Address / Background Music (PA/BGM):
* **Ceiling Speakers (6W - 10W):** 100V line transformer speakers with fire dome, installed in corridors and lobbies.
* **Horn Speakers (15W - 30W IP66):** Installed in parking areas and rooftop.
* **Fire-Rated Audio Cable:** $2 \times 1.5 \text{ mm}^2$ twisted shielded cable in dedicated red conduit.

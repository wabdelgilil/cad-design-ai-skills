# The "Fork & Extend" Architecture Guide 🍴

Welcome to **`cad-design-ai-skills`**. This guide explains how engineering consultancies, independent MEP designers, and BIM managers can **Fork** this repository to build their own internal corporate engineering brain while staying synchronized with upstream open-source updates.

---

## 🎯 Why Fork?

Every engineering office and geographical region has unique design constraints:
1. **Regional Electrical & Building Codes**:
   * Saudi Arabia: **SBC 401** (400V/230V @ 60Hz, SEC regulations).
   * Egypt: **Egyptian Code of Practice (ECP)** (380V/220V @ 50Hz).
   * UK / Europe: **BS 7671 / IEC 60364** (400V/230V @ 50Hz).
   * USA: **NEC / NFPA 70** (480V/277V or 208V/120V @ 60Hz).
2. **Corporate CAD / BIM Standards**:
   * Custom AutoCAD block libraries, dynamic blocks, and attribute definitions.
   * Specific layer naming standards (e.g. customized AIA or British BS 1192).
   * Corporate title blocks, drawing sheet templates, and standard details.
3. **Approved Vendor Catalogs**:
   * Pre-approved lighting manufacturers (e.g. Philips, Zumtobel, local suppliers).
   * Preferred pump brands (Grundfos, Lowara, Pedrollo) and PPR/PVC pipe brands.

By forking this repository, you get a clean, standardized, AI-ready foundation without starting from scratch.

---

## 🛠️ Step-by-Step Forking Strategy

### Step 1: Fork the Repository
Click the **Fork** button on GitHub to create your firm's copy (e.g., `your-firm/cad-design-ai-skills` or `your-username/firm-mep-brain`).

### Step 2: Establish the Upstream Remote
In your local cloned fork, add the original repository as `upstream`:
```bash
git clone https://github.com/YOUR_ORGANIZATION/cad-design-ai-skills.git
cd cad-design-ai-skills

# Add the open-source original as upstream
git remote add upstream https://github.com/wabdelgilil/cad-design-ai-skills.git
git fetch upstream
```

### Step 3: Add Your Custom Layers & Catalogs
We recommend creating a dedicated directory `firm_extensions/` inside your fork:
```
cad-design-ai-skills/
├── skills/                      # Core upstream skills
├── heuristics/                  # Core heuristics
├── firm_extensions/             # YOUR PROPRIETARY DATA (IGNORED BY UPSTREAM)
│   ├── cad_blocks/              # Your DWG/DXF dynamic blocks
│   ├── approved_vendors.json    # Your firm's pre-approved vendor price lists
│   └── regional_codes/          # Your country's specific building code amendments
```

### Step 4: Staying Synced with Upstream
When new engineering skills, CLI scripts, or CAD tricks are added to the public repo:
```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

---

## 🤝 When and How to Contribute Back (Upstream PRs)

We strongly encourage contributing generic engineering improvements back to the main repository:

### ✅ Ideal Upstream Contributions:
* Fixing a mathematical or engineering formula in a calculator.
* Adding support for a new international standard (e.g. ASHRAE 90.1, NFPA 13 tables).
* Optimizing a Python DXF/AutoCAD scripting trick.
* Adding a new generic CLI engineering tool.

### ❌ What Should Stay in Your Fork:
* Proprietary client drawings or confidential project names.
* Firm-specific commercial discount agreements or private supplier pricing.
* Non-standard internal layer naming only used within your office.

---

## 💡 Support & Discussion
If you need guidance on configuring agent skills for your firm's specific AI setup, open an issue or discussion on GitHub!

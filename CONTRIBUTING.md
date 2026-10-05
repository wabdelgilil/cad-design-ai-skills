# Contributing to CAD Design AI Skills 🤝

Thank you for your interest in contributing! This project thrives on real-world engineering rigor and peer-reviewed code.

---

## 📐 Ground Rules for Contributions

Every skill, formula, and script added to this repository must satisfy our **Three Pillars of Engineering Quality**:

1. **Deterministic & Standard-Based**:
   * Formulas must cite reputable codes (IEC, NFPA, SBC, NEC, ASHRAE, CIBSE) or established consulting practice.
   * No arbitrary guesswork.
2. **Zero Project-Specific or Confidential Leaks**:
   * Never commit actual client drawings, project names, or proprietary cost structures.
   * All examples must use generic identifiers (e.g., `Room 101`, `Standard 3-Bedroom Unit`).
3. **AI Agent Compatibility**:
   * Markdown files must be well-structured with clear headings, parameter ranges, and actionable heuristics so LLMs can read and parse them without ambiguity.

---

## 🚀 How to Submit a Contribution

1. **Fork the repository** on GitHub.
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/add-chilled-water-sizing
   ```
3. **Add your skill, heuristic, or tool**:
   * If adding an engineering skill, place it in `skills/<discipline>/`.
   * If adding an automation script, place it in `cad_automation/` with CLI unit tests.
   * If updating the knowledge graph, update `heuristics/mep_design_heuristics.json`.
4. **Commit with clean conventional commits**:
   ```bash
   git commit -m "feat(hvac): add chilled water pipe sizing velocity and head loss tables"
   ```
5. **Open a Pull Request** against `main`.

---

## 📋 PR Checklist

Before submitting, ensure:
- [ ] No confidential, client, or copyrighted private drawings are included.
- [ ] Technical terminology is standard English.
- [ ] Python scripts run standalone with `--help` and zero required paid third-party licenses.
- [ ] Formatted cleanly in standard Markdown.

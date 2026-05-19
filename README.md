# Chemical Engineering PE Exam Study Guide

Comprehensive study materials for the Chemical Engineering PE exam, covering all 11 major topics.

## Live Website

**Visit:** https://duymlcoding.github.io/Professional-Engineering-Exams-Chemical/

Interactive Jupyter Book with:
- Searchable content
- LaTeX math rendering
- Light and dark mode support
- Mobile-friendly design
- 100+ worked examples

## Topics Covered

1. **Mass and Energy Balance** - Material/energy balances, recycle streams, combustion
2. **Thermodynamics** - Gas laws, cycles, entropy, phase diagrams
3. **Fluid Mechanics** - Flow, pressure drop, pumps, Reynolds numbers
4. **Heat Transfer** - Conduction, convection, radiation, heat exchangers
5. **Mass Transfer** - Diffusion, absorption, distillation, extraction
6. **Chemical Reaction Engineering** - Kinetics, reactors (batch, CSTR, PFR)
7. **Chemical and Phase Equilibria** - VLE, LLE, fugacity, Gibbs energy
8. **Process Design and Economics** - Process flow, economics, optimization
9. **Process Equipment Design** - Vessels, heat exchangers, columns, pumps
10. **Instrumentation and Control** - Control loops, sensors, PID tuning
11. **Materials of Construction** - Corrosion, material selection, codes

## Content Statistics

- **20,000+** lines of study material
- **1,000+** equations
- **100+** worked example problems
- **11** comprehensive chapters

## Repository Structure

```
PE_Chemical/
├── mynotes/              # Jupyter Book source
│   ├── chapters/         # All 11 topic chapters
│   ├── _static/          # Custom CSS (light + dark theme)
│   ├── _config.yml       # Book configuration
│   ├── _toc.yml          # Table of contents
│   └── index.md          # Homepage
└── .github/workflows/    # Auto-deployment to GitHub Pages
```

## Local Development

```bash
# Clone repository
git clone https://github.com/duymlcoding/Professional-Engineering-Exams-Chemical.git
cd Professional-Engineering-Exams-Chemical

# Install dependencies
pip install -r mynotes/requirements.txt

# Build book
jupyter-book build mynotes/ --all

# Preview (open in browser: http://localhost:8000)
cd mynotes/_build/html
python3 -m http.server 8000
```

## Deployment

The website automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

## License

See [LICENSE](LICENSE) file for details.

## Acknowledgments

Content aligned with NCEES Chemical Engineering PE exam specifications. All materials organized for effective exam preparation.

---

**Last Updated:** May 2026

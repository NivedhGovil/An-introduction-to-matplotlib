# Matplotlib Guide and Weather Visualization Project

A beginner-friendly Matplotlib crash course organized into focused modules, followed by a weather-themed visualization project path.  
If you are new to plotting in Python, this repository is designed to help you build confidence step by step.

## What You Will Learn

By working through this guide, you will practice how to:

- Create and display basic line plots
- Style plots with markers, colors, and line formats
- Add titles, axis labels, and custom ticks
- Compare multiple data series in one figure
- Build bar charts and scatter plots
- Save figures and arrange subplot layouts
- Combine these skills into a small weather data visualization workflow

## Module Roadmap (1–7)

Each module includes an `example.py` script and a short local README with explanations.

1. **Module 1: Basic Line Plot**  
   Path: [`1_Basic_Line_Plot/`](./1_Basic_Line_Plot)  
   Focus: first line plot, plotting `x` vs `y`, and Matplotlib defaults.

2. **Module 2: Markers, Line Styles, and Colors**  
   Path: [`2_Markers_Line_Styles/`](./2_Markers_Line_Styles)  
   Focus: marker types, line styles (`-`, `--`, `:`), and plot appearance customization.

3. **Module 3: Titles, Labels, and Ticks**  
   Path: [`3_Titles_Labels_Ticks/`](./3_Titles_Labels_Ticks)  
   Focus: figure text, axis labeling, tick control, and multi-series plotting.

4. **Module 4: Multiple Plots and Format Shorthand**  
   Path: [`4_Multiple_Plots/`](./4_Multiple_Plots)  
   Focus: plotting multiple lines and using Matplotlib format shorthand (for marker/style/color).

5. **Module 5: Bar Charts**  
   Path: [`5_Bar_Charts/`](./5_Bar_Charts)  
   Focus: categorical comparison with `plt.bar(...)`, sizing, and color use.

6. **Module 6: Scatter Plots and Annotations**  
   Path: [`6_Scatter_Plots/`](./6_Scatter_Plots)  
   Focus: scatter visualization, threshold/reference lines, and legends.

7. **Module 7: Tips and Further Reading**  
   Path: [`7_Tips_and_Further_Reading/`](./7_Tips_and_Further_Reading)  
   Focus: saving figures, subplot layouts, and recommended Matplotlib resources.

## Weather Visualization Project (How This Course Leads Into It)

This repository’s original goal includes a weather visualization project after Modules 1–7.  
In this clone, the core learning modules are present, and they map naturally to a weather workflow:

1. Gather weather data (for example: date, temperature, humidity, rainfall, wind speed)
2. Clean/organize values with NumPy or plain Python lists
3. Use:
   - line plots for trends across time
   - bar charts for category/month comparisons
   - scatter plots for relationships (for example, humidity vs temperature)
4. Add titles, labels, legends, and threshold lines to make plots interpretable
5. Save polished figures for reports or presentations

If you add a dedicated weather notebook/script, these modules provide the exact plotting foundation you need.

## Prerequisites

- Python 3.9+ recommended
- Basic Python syntax (variables, lists, functions)
- Familiarity with running Python scripts from a terminal

## Setup

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install --upgrade pip
```

This repository currently does **not** include a `requirements.txt`.  
Install the core learning dependencies manually:

```bash
pip install matplotlib numpy
```

Optional for interactive notebook use:

```bash
pip install notebook
```

## How to Use the Learning Materials

### Option A: Run module scripts directly

From any module folder:

```bash
python example.py
```

### Option B: Use Jupyter Notebook locally

1. Start Jupyter:
   ```bash
   jupyter notebook
   ```
2. Open a new notebook in the repository root or module folder.
3. Copy code from each module’s `example.py` into cells and run step by step.

### Option C: Use Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload a module `example.py` file (or copy/paste code into a notebook cell).
3. Run cells and iterate on plot styles and labels interactively.

## Suggested Learning Path

1. Complete Modules 1–3 to learn plotting basics and readability.
2. Complete Modules 4–6 to compare multiple series and chart types.
3. Finish Module 7 to learn practical plotting habits (saving figures, layout).
4. Build a weather mini-project using real or sample weather data.
5. Refine charts for storytelling quality (titles, labels, legends, color choices).

## Repository Structure

```text
.
├── 1_Basic_Line_Plot/
├── 2_Markers_Line_Styles/
├── 3_Titles_Labels_Ticks/
├── 4_Multiple_Plots/
├── 5_Bar_Charts/
├── 6_Scatter_Plots/
├── 7_Tips_and_Further_Reading/
├── LICENSE
└── README.md
```

## Contributing

Contributions that improve explanations, examples, and beginner clarity are welcome.  
If you contribute, keep examples simple, well-commented, and aligned with the module progression.

## License

This project is licensed under the [MIT License](./LICENSE).

## Future Improvements

- Add a dedicated weather project folder with sample data and end-to-end walkthrough
- Add Jupyter notebook versions of each module for learners who prefer notebook-first study

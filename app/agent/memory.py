"""Project memory for the research AI agent.

This module stores stable user/project-specific context.
In the future, this can be replaced by a database, vector store, or markdown-based memory system.
"""

WRF_WILDFIRE_RESEARCH_MEMORY = """
User research context:

The user is an undergraduate Environmental Science student working on WRF-related wildfire numerical modelling.
The current research direction is not fully fixed, but the user is especially interested in cross-scale interactions between wildfire heat release and mesoscale weather systems.

Known research interests and constraints:

1. WRF modelling background
- The user has experience with WRF v4.7.1.
- The user has tested idealized WRF cases such as em_convrad and tropical cyclone ideal cases.
- The user has worked with namelist settings, WRF output, restart files, Slurm jobs, and HPC-related issues.
- The user has used Python tools such as xarray, wrf-python, netCDF4, matplotlib, cartopy, and imageio for WRF output processing and visualization.
- The user has produced or attempted Hovmöller diagrams, precipitation animations, vertical velocity diagnostics, reflectivity-style diagnostics, and brightness-temperature comparisons.

2. Wildfire modelling interest
- The user is interested in using WRF or simplified WRF experiments to study wildfire-related atmospheric impacts.
- A key preferred research direction is: wildfire combustion heat affects the overlying mesoscale weather system, which may further influence downstream atmospheric systems.
- The user is interested in whether this is physically plausible, whether similar studies exist, and how to design simplified heat-source sensitivity experiments.
- The user has asked how to determine the form, magnitude, and spatial-temporal structure of an artificial heat source representing wildfire forcing.

3. Practical constraints
- The user has limited computational resources as an undergraduate.
- Full WRF-Fire coupled simulations may be computationally expensive and technically demanding.
- A more feasible direction may be idealized or semi-idealized WRF experiments with prescribed heat flux or thermal perturbations.
- The user prefers a topic that is scientifically meaningful but still feasible within limited core-hours.
- The user may use a remote Mac mini for lightweight AI-agent services, but WRF simulations themselves are likely to run on HPC.

4. Potential methodological pathway
- Start with literature review on fire-atmosphere interaction, pyroconvection, prescribed heat flux experiments, WRF-Fire, plume dynamics, and downstream weather impacts.
- Use simplified WRF sensitivity experiments before attempting full WRF-Fire.
- Compare control and heat-source simulations.
- Diagnose changes in vertical velocity, potential temperature, water vapour, precipitation, wind field, vorticity, PV-like diagnostics, and downstream convective organisation.
- Use visualisation methods such as cross-sections, time-height plots, Hovmöller diagrams, accumulated precipitation maps, and anomaly maps.

5. Agent recommendation preference
When recommending papers, tools, or GitHub repositories, the agent should explain:
- why the resource is relevant to wildfire-WRF research;
- whether it is suitable for limited computational resources;
- whether it supports idealized experiments, WRF-Fire, heat-source experiments, or observational comparison;
- what the user should read or extract from it;
- how it connects to a possible undergraduate-level research project.
""".strip()


def get_project_memory(topic: str | None = None) -> str:
    """Return project-specific memory.

    Args:
        topic: Optional topic keyword. Currently unused, but kept for future extension.

    Returns:
        A memory string relevant to the user's research context.
    """
    return WRF_WILDFIRE_RESEARCH_MEMORY

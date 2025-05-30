import pytest
import os

import numpy as np

from pvade.fluid.FlowManager import Flow
from pvade.DataStream import DataStream
from pvade.Parameters import SimParams
from pvade.Utilities import get_input_file, write_metrics
from pvade.geometry.MeshManager import FSIDomain

from dolfinx.common import TimingType, list_timings
import cProfile
import sys
import tqdm.autonotebook

input_path = "pvade/tests/inputs_test/"

solve_iter = 10

rtol = 3.0e-5


@pytest.mark.unit
def test_flow_3dpanels():
    # Get the path to the input file from the command line
    input_file = input_path + "sim_params_alt.yaml"  # get_input_file()

    # Load the parameters object specified by the input file
    params = SimParams(input_file)

    # Initialize the domain and construct the initial mesh
    domain = FSIDomain(params)
    domain.read("pvade/tests/test_mesh/panels3d", params)
    # Initialize the function spaces for the flow
    flow = Flow(domain)
    # # # Specify the boundary conditions
    flow.build_boundary_conditions(domain, params)
    # # # Build the fluid forms
    flow.build_forms(domain, params)
    dataIO = DataStream(domain, flow, params)

    for t_step in range(solve_iter):
        flow.solve(params)

        max_velocity = np.amax(flow.u_k.x.array)
        max_pressure = np.amax(flow.p_k.x.array)

        print("max_velocity = ", max_velocity)
        print("max_pressure = ", max_pressure)

    max_velocity_truth = 16.78961717598599
    max_pressure_truth = 161.00087027677822
    assert np.isclose(max_velocity, max_velocity_truth, rtol=rtol)
    assert np.isclose(max_pressure, max_pressure_truth, rtol=rtol)


@pytest.mark.unit
def test_flow_2dpanels():
    # Get the path to the input file from the command line
    input_file = input_path + "sim_params_alt_2D.yaml"  # get_input_file()

    # Load the parameters object specified by the input file
    params = SimParams(input_file)

    # Initialize the domain and construct the initial mesh
    domain = FSIDomain(params)
    domain.read("pvade/tests/test_mesh/panels2d", params)
    # Initialize the function spaces for the flow
    flow = Flow(domain)
    # # # Specify the boundary conditions
    flow.build_boundary_conditions(domain, params)
    # # # Build the fluid forms
    flow.build_forms(domain, params)
    dataIO = DataStream(domain, flow, params)

    for t_step in range(solve_iter):
        flow.solve(params)

        max_velocity = np.amax(flow.u_k.x.array)
        max_pressure = np.amax(flow.p_k.x.array)

        print("max_velocity = ", max_velocity)
        print("max_pressure = ", max_pressure)

    max_velocity_truth = 3.4734894184978726
    max_pressure_truth = 1.698213865642233
    assert np.isclose(max_velocity, max_velocity_truth, rtol=rtol)
    assert np.isclose(max_pressure, max_pressure_truth, rtol=rtol)


@pytest.mark.unit
def test_flow_2dcylinder():
    # Get the path to the input file from the command line
    input_file = input_path + "2d_cyld.yaml"  # get_input_file()

    # Load the parameters object specified by the input file
    params = SimParams(input_file)

    # Initialize the domain and construct the initial mesh
    domain = FSIDomain(params)
    domain.read("pvade/tests/test_mesh/cylinder2d", params)
    # Initialize the function spaces for the flow
    flow = Flow(domain)
    # # # Specify the boundary conditions
    flow.build_boundary_conditions(domain, params)
    # # # Build the fluid forms
    flow.build_forms(domain, params)
    dataIO = DataStream(domain, flow, params)

    for t_step in range(solve_iter):
        flow.solve(params)

        max_velocity = np.amax(flow.u_k.x.array)
        max_pressure = np.amax(flow.p_k.x.array)

        print("max_velocity = ", max_velocity)
        print("max_pressure = ", max_pressure)

    max_velocity_truth = 1.8113852701695827
    max_pressure_truth = 1.3044593668958533
    assert np.isclose(max_velocity, max_velocity_truth, rtol=rtol)
    assert np.isclose(max_pressure, max_pressure_truth, rtol=rtol)


@pytest.mark.unit
def test_flow_3dcylinder():
    # Get the path to the input file from the command line
    input_file = input_path + "3d_cyld.yaml"  # get_input_file()

    # Load the parameters object specified by the input file
    params = SimParams(input_file)

    # Initialize the domain and construct the initial mesh
    domain = FSIDomain(params)
    domain.read("pvade/tests/test_mesh/cylinder3d", params)
    # Initialize the function spaces for the flow
    flow = Flow(domain)
    # # # Specify the boundary conditions
    flow.build_boundary_conditions(domain, params)
    # # # Build the fluid forms
    flow.build_forms(domain, params)
    dataIO = DataStream(domain, flow, params)

    for t_step in range(solve_iter):
        flow.solve(params)

        max_velocity = np.amax(flow.u_k.x.array)
        max_pressure = np.amax(flow.p_k.x.array)

        print("max_velocity = ", max_velocity)
        print("max_pressure = ", max_pressure)

    max_velocity_truth = 0.6242970092279582
    max_pressure_truth = 0.30929163498498147
    assert np.isclose(max_velocity, max_velocity_truth, rtol=rtol)
    assert np.isclose(max_pressure, max_pressure_truth, rtol=rtol)

import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

class Navbar extends Component {
  render() {
    return (
      <div className="Navbar">
        <ul className="nav nav-bordered navbar-padded justify-content-center">
          <li className="nav-item">
            <NavLink
              className="nav-link"
              activeClassName="active"
              to="/portfolio"
            >
              <i className="icon icon-pie-chart" /> Portfolio
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink
              className="nav-link"
              activeClassName="active"
              to="/analytics"
            >
              <i className="icon icon-gauge" /> Analytics
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink
              className="nav-link"
              activeClassName="active"
              to="/accounts"
            >
              <i className="icon icon-wallet" /> Accounts
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink
              className="nav-link"
              activeClassName="active"
              to="/markets"
            >
              <i className="icon icon-line-graph" /> Markets
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink
              className="nav-link"
              activeClassName="active"
              to="/settings"
            >
              <i className="icon icon-cog" /> Settings
            </NavLink>
          </li>
        </ul>
      </div>
    );
  }
}

export default Navbar;
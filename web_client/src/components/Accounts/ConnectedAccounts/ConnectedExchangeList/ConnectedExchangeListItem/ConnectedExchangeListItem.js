import React, { Component } from "react";
import PropTypes from "prop-types";

class ConnectedExchangeListItem extends Component {
  onClick(event) {
    event.preventDefault();
    this.props.disconnectExchange(this.props.id);
  }

  render() {
    return (
      <li className="ConnectedExchangeListItem list-group-item">
        <div className="row d-flex align-items-center">
          <div className="col-2">{this.props.name}</div>
          <div className="col-xs-4 col-md-6">
            <small className="text-muted">{this.props.syncedAt}</small>
          </div>
          <div className="col-xs-6 col-md-4">
            <button
              className="btn btn-primary btn-outline-secondary pull-right"
              onClick={event => this.onClick(event)}
            >
              Remove
            </button>
          </div>
        </div>
      </li>
    );
  }
}

ConnectedExchangeListItem.propTypes = {
  name: PropTypes.string,
  extension: PropTypes.string,
  backgroundColor: PropTypes.string,
  size: PropTypes.string
};

export default ConnectedExchangeListItem;
